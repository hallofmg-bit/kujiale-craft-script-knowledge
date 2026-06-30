---
name: shutiao
description: 酷家乐工艺编辑器"设计中"脚本开发与排错知识。当前聚焦"设计中-台面"模块的 generateFee、Fee、Countertop 等对象，用于台面洞、挡水、工艺费、台面虚拟五金、printSystemLog、未找到定义、唯一标识冲突、格式错误、脚本不触发、生成 JSON 无结果等场景。后续将扩展其他业务域。
---

# 酷家乐工艺编辑器"设计中"脚本开发与排错

当前聚焦 **"设计中-台面"** 模块。其他业务域（设计后处理、规则检测、订单后处理、图纸）的要点暂列概览，待有真实验证案例后再补充。

## 先选对执行域

| 需求 | 业务域或入口 | 关键对象 |
| --- | --- | --- |
| 台面洞、挡水、工艺费、台面虚拟五金 | 台面 `generateFee` | `Countertop`、`Fee` |
| 输出 JSON 前统一增改模型 | 设计后处理 `postProcess` | `PostProcessDesignData`、`DesignPostProcessResult` |
| 模型告警和错误提示 | 规则检测 `ruleCheck` | `ModelRuleResult`、`RuleLevel` |
| 订单字段、统计和提审处理 | 订单后处理 | `DcsOrder` |
| 轮廓、孔洞、尺寸和加工图 | 图纸入口 | 图纸与几何对象 |

先在编辑器“可用类型/脚本”中确认当前业务模块真实暴露的类型。某个域找不到 `VirtualModel`，只说明该域不能直接使用它，不代表整个“设计中”能力不支持虚拟五金。

## 通用开发规则

1. 确认业务模块、系统入口、函数签名和触发动作。
2. 唯一标识与入口函数名完全一致；系统入口已存在时编辑原脚本，不改名绕过。
3. 自定义对象和子脚本先保存、发布，再保存调用者。
4. 用最小函数验证 import、入参和返回类型，再加入业务条件。
5. 一条脚本只定义一个普通函数；能合入入口的小逻辑不要拆成子脚本。
6. 避免 `try/catch`、传统 `for`、`while`、字符串 `+` 拼接日志和重复变量名。
7. 同时验证命中、不命中场景，并检查最终输出，不以“保存成功”代替运行成功。

## 日志与排错

统一使用前缀和序号：

```ts
import { printSystemLog } from "system";
import { numberToString } from "basic";

printSystemLog("业务前缀：0 start");
printSystemLog(["业务前缀：1 数量", numberToString(count)].join(" - "));
```

日志查询：

```text
https://tetris.qunhequnhe.com/log
```

| 场景 | service |
| --- | --- |
| 台面 | `service.dcs-countertop` |
| 设计后处理 | `service.dcs-post-process-task` |
| 输出 JSON | `service.superoutputtask` |
| 订单 | `service.dcs-order-design` |

按以下顺序定位问题：

1. **未找到定义**：检查 import 模块、当前业务域的可用类型、自定义对象是否发布、子脚本标识是否一致。
2. **唯一标识已存在**：定位并编辑已有系统入口，不创建同义入口。
3. **格式错误**：缩减为最小函数，检查不支持语法、重复变量、多余逗号，并在浏览器 Network 查看 `/kb-editor/api/customdef` 返回。
4. **运行无结果**：分别打印入口、条件、创建动作和返回数量，区分“未触发”“条件未命中”“结果未被输出链路采纳”“商品无效”。
5. **日志有结果但 JSON 没有**：核对输出服务、商品授权和最终采用的结果对象。

## 各业务域要点

### 台面

- 工艺费或虚拟商品优先走 `Fee + generateFee`。
- `generateFee(countertop: Countertop): Fee[]` 是系统入口，其他函数名不会自动触发。
- `calcHoleFee` 只是可选子脚本，可将其逻辑直接合并进 `generateFee`。
- 精确识别水槽孔，不要用“排除龙头孔”代替“判断水槽孔”。

### 设计后处理

- 用于生成 JSON 或输出阶段的统一增改，通常不会在设计画布中即时展示。
- 使用 `postProcess`、`DesignPostProcessResult`、`ModelPostProcessResult`、`addChildren` 或 `addParameters`。
- 不把此域的 `VirtualModel/addChildren` 直接搬到台面 `generateFee`。

### 规则检测

- 使用 `ruleCheck`，通过 `buildModelCheckResult` 绑定模型，再用 `buildRuleResult` 创建 `WARN` 或 `ERROR`。
- 同时验证命中和不命中，避免重复告警和笛卡尔积式遍历。

### 订单后处理

- 先确认由订单字段、提审页面还是提交审核触发，再核对入口签名和绑定关系。
- 从 `DcsOrder` 过滤目标模型后统计，返回字段要求的基础类型。
- 日志和案例不得包含客户或订单敏感数据。

### 图纸

- 明确图纸入口、坐标系、单位、旋转和偏移。
- 区分设计尺寸与加工尺寸；先验证最小几何，再覆盖 L/U 型、空数据和异常轮廓。

## "设计中-台面"已验证案例

以下案例均来自真实项目，经过运行日志或输出 JSON 验证。新案例按同样格式追加到本节末尾。

### 案例 1：台下盆按厚度生成虚拟五金

> 作者：hallofmg-bit | 验证日期：2025-06 | 来源：工艺编辑器项目实战

### 目标与结论

台面存在“台下盆水槽孔”时，按台面厚度生成一个对应的零价虚拟商品：

```text
厚度 20 -> BG_ID_FOR_20MM
厚度 12 -> BG_ID_FOR_12MM
```

台上盆、台中盆、无水槽孔和其他厚度不生成。正确链路是台面 `Fee + generateFee`，不是设计后处理 `VirtualModel + addChildren`。

### 前置配置

在台面业务模块创建并发布自定义对象：

```text
对象/唯一标识：Fee
继承类型：parammodelMap/ParamModelInstance
属性：
  price      number
  length     number
  brandgood  brandgood/PBrandgood
```

发布后确认 `Fee` 出现在台面脚本“可用类型”中。系统入口唯一标识使用 `generateFee`；若已存在，直接编辑已有入口。

### 完整脱敏脚本

```ts
import { printSystemLog } from "system";
import { Countertop, MoldingType, Fee } from "countertop";
import { createPBrandGood, ProdCategory } from "brandgood";
import { ignoreFailedInList, numberToString } from "basic";

function generateFee(countertop: Countertop): Fee[] {
    let fees: Fee[] = [];

    printSystemLog("水槽孔虚拟五金：0 generateFee start");

    let allHoles = countertop.moldingArea.holes;
    let sinkBottomHoles = allHoles.filter(hole =>
        hole.isProdCategory(ProdCategory.SINK) &&
        hole.isMoldingType(MoldingType.BOTTOM)
    );
    let sinkBottomHoleCount = sinkBottomHoles.size().orElse(0);

    printSystemLog([
        "水槽孔虚拟五金：1 全部洞数量",
        numberToString(allHoles.size().orElse(0))
    ].join(" - "));
    printSystemLog([
        "水槽孔虚拟五金：2 台下盆水槽孔数量",
        numberToString(sinkBottomHoleCount)
    ].join(" - "));

    if (sinkBottomHoleCount > 0) {
        let thickness = countertop.extrusionHeight;
        let hardwareBgId: string = "";

        if (thickness === 20) {
            hardwareBgId = "BG_ID_FOR_20MM";
        }

        if (thickness === 12) {
            hardwareBgId = "BG_ID_FOR_12MM";
        }

        printSystemLog([
            "水槽孔虚拟五金：3 台面厚度",
            numberToString(thickness),
            "商品ID",
            hardwareBgId
        ].join(" - "));

        if (hardwareBgId !== "") {
            let hardwareBg = createPBrandGood(hardwareBgId);
            let holeFee = Fee.newInstance({
                price: 0,
                brandgood: hardwareBg,
                length: 0
            });

            fees.push(holeFee);
            printSystemLog("水槽孔虚拟五金：4 已创建虚拟五金");
        }
    }

    printSystemLog([
        "水槽孔虚拟五金：9 返回Fee数量",
        numberToString(fees.size())
    ].join(" - "));

    return ignoreFailedInList(fees);
}
```

若当前台面模块只支持 `buildPBrandGood(数字商品ID)`，以“可用脚本”中真实存在并通过最小脚本验证的函数为准。

### 验证和诊断

| 日志结果 | 结论 |
| --- | --- |
| 全部洞 = 0 | 台面没有洞或触发时机不对 |
| 全部洞 > 0，水槽洞 = 0 | 孔关联商品不是 `ProdCategory.SINK` |
| 水槽洞 > 0，台下盆洞 = 0 | 当前设计是台上盆或台中盆，不应生成 |
| 台下盆洞 > 0，返回 Fee = 0 | 厚度、商品函数或 `Fee.newInstance` 未命中 |
| 返回 Fee = 1，JSON 无商品 | 检查输出服务和商品有效性 |

已验证反向场景：真实设计为台上盆时，全部洞和水槽洞均为 1，台下盆洞与返回 Fee 均为 0；不生成是正确结果。正向场景应出现“已创建虚拟五金”、返回 Fee 为 1，并在输出 JSON 中找到目标商品。

### 成功经验

最初因台面域中 `VirtualModel` 报“未找到定义”，误推断设计中无法生成虚拟五金。后续根据同一台面业务域的工艺费成功案例和真实日志确认：台面域不能直接使用设计后处理对象，但可以通过 `Fee/generateFee` 生成虚拟商品。判断能力边界时，应以同业务域成功案例、可用类型和运行证据为准。

## 知识维护

- 真实日志和输出 JSON 优先于推断。
- 新案例直接追加到本文件的对应业务域；案例多到影响检索时，再按“一个业务域一个参考文件”拆分。
- 公开版本只保留脱敏脚本、最小日志和结论摘要，不保存企业专属商品 ID 或客户数据。
