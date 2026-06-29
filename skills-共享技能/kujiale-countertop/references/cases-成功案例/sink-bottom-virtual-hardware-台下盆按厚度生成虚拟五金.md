---
title: 台下盆按台面厚度生成虚拟五金
domain: countertop
entry: generateFee
business_module: 台面
author: community
verified_at: 2026-06-26
environment: 真实设计方案与 dcs-countertop 日志
status: verified
---

# 台下盆按厚度生成虚拟五金

## 业务目标

台面存在台下盆水槽孔时，根据台面厚度生成一个对应的工艺费虚拟模型：

```text
厚度 20 -> BG_ID_FOR_20MM
厚度 12 -> BG_ID_FOR_12MM
```

台上盆、台中盆、无水槽孔或其他厚度不生成。

## 关键结论

- 使用台面工艺费链路 `Fee + generateFee`，而不是设计后处理 `VirtualModel + addChildren`。
- `Fee` 需要先创建为台面模块自定义对象。
- 精确条件是 `ProdCategory.SINK` 与 `MoldingType.BOTTOM`。
- `calcHoleFee` 不是必须，可将逻辑合并进 `generateFee`，减少依赖。

## 脱敏脚本

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

printSystemLog(["水槽孔虚拟五金：1 全部洞数量", numberToString(allHoles.size().orElse(0))].join(" - "));
printSystemLog(["水槽孔虚拟五金：2 台下盆水槽孔数量", numberToString(sinkBottomHoleCount)].join(" - "));

if (sinkBottomHoleCount > 0) {
let thickness = countertop.extrusionHeight;
let hardwareBgId: string = "";

if (thickness === 20) {
hardwareBgId = "BG_ID_FOR_20MM";
}

if (thickness === 12) {
hardwareBgId = "BG_ID_FOR_12MM";
}

printSystemLog(["水槽孔虚拟五金：3 台面厚度", numberToString(thickness), "商品ID", hardwareBgId].join(" - "));

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

printSystemLog(["水槽孔虚拟五金：9 返回Fee数量", numberToString(fees.size())].join(" - "));

return ignoreFailedInList(fees);
}
```

若当前台面模块只支持 `buildPBrandGood`，将字符串占位符替换为已授权的数字商品 ID。

## 验证记录

### 反向场景：台上盆

日志：

```text
全部洞数量 - 1
水槽洞数量 - 1
台下盆洞数量 - 0
返回Fee数量 - 0
```

设计事实确认当前水槽确为台上盆，因此不生成是正确结果。

### 正向场景：台下盆

预期：

```text
台下盆水槽孔数量 - 1
已创建虚拟五金
返回Fee数量 - 1
```

同时在输出 JSON 中确认目标商品存在。

## 失败经验

最初误用设计后处理 `VirtualModel/addChildren`，并因台面脚本域中 `VirtualModel` 报红而推断设计中不支持生成虚拟五金。后来通过同业务域的台盆工艺费成功案例确认，台面设计中应使用 `Fee/generateFee`。

正确结论：

```text
台面域不能直接搬用设计后处理的 VirtualModel/addChildren，
但可以通过 Fee 工艺费链路生成台面虚拟模型。
```

## 已知限制

- `generateFee` 的自动触发依赖系统入口和当前环境配置。
- 商品创建函数以当前“可用脚本”为准。
- 公开仓库不保存企业专属商品 ID。
- 脚本编辑器语法不是完整 TypeScript。

## 来源摘要

- 酷家乐内部“工艺费”与“台盆工艺费”成功案例；
- 工艺编辑器入门与日志排错资料；
- 真实设计方案、台面日志与输出 JSON 验证。
