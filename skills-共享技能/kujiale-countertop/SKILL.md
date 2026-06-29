---
name: kujiale-countertop
description: 酷家乐工艺编辑器台面领域脚本知识。用于台面生成、孔洞、台盆安装方式、前后挡水、工艺费、Fee、generateFee、Countertop#customOutput、台面虚拟五金，以及处理未找到定义、生成结果缺失和台面日志诊断等问题。
---

# 酷家乐台面脚本

## 核心原则

1. 先确定台面执行入口，再选择对象和返回值。
2. 台面工艺费虚拟模型优先使用 `Fee` + `generateFee`。
3. 不要把台面域缺少 `VirtualModel` 误判为“设计中不能生成虚拟五金”。
4. 不要跨业务域直接搬运 `postProcess/addChildren`。
5. 用最小脚本确认类型、入口和发布状态，再添加业务条件。

## 入口选择

| 需求 | 首选入口 |
| --- | --- |
| 生成台面工艺费虚拟模型 | `generateFee(countertop: Countertop): Fee[]` |
| 修改单个台面输出参数 | `Countertop#customOutput`，需确认环境开放和白名单 |
| 台面规则提示 | `ruleCheck` 或对应台面规则检测入口 |
| 输出后统一追加模型 | 改用设计后处理 Skill |

## 开发流程

1. 确认业务模块为 `台面`。
2. 在“可用类型/脚本”确认所需类型。
3. 若 `Fee` 未定义，创建并发布 `Fee` 自定义对象。
4. 若 `generateFee` 提示唯一标识已存在，编辑已有入口；不要改名规避。
5. 每条脚本只定义一个普通函数，唯一标识与函数名一致。
6. 加入带统一前缀和序号的 `printSystemLog`。
7. 验证正向与反向场景，并检查输出 JSON。

## 精确判断台下盆水槽孔

```ts
let sinkBottomHoles = countertop.moldingArea.holes.filter(hole =>
hole.isProdCategory(ProdCategory.SINK) &&
hole.isMoldingType(MoldingType.BOTTOM)
);
```

不要用“排除龙头孔”代替“水槽孔”，否则其他洞也可能命中。

若日志显示水槽洞大于 0、台下盆洞等于 0，先确认设计实际是否为台上盆或台中盆。不要为了让结果生成而删除正确条件。

## 参考资料

- 实现台面 `Fee` 与虚拟五金时，读取 [fee-workflow-台面Fee工作流.md](references/fee-workflow-台面Fee工作流.md)。
- 排查日志和定义错误时，读取 [troubleshooting-台面日志排错.md](references/troubleshooting-台面日志排错.md)。
- 处理本次已验证需求时，读取 [sink-bottom-virtual-hardware-台下盆按厚度生成虚拟五金.md](references/cases-成功案例/sink-bottom-virtual-hardware-台下盆按厚度生成虚拟五金.md)。

## 证据优先级

1. 真实脚本运行日志与输出 JSON；
2. 同入口、同业务模块的成功案例；
3. 编辑器“可用类型/脚本”；
4. 推断。

若推断与运行结果冲突，以运行结果为准，并把差异记录进案例。
