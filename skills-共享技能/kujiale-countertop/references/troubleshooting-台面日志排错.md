# 台面日志排错

## 日志写法

```ts
import { printSystemLog } from "system";
import { numberToString } from "basic";

printSystemLog("台面脚本：0 start");
printSystemLog(["台面脚本：1 数量", numberToString(count)].join(" - "));
```

不要使用字符串 `+` 拼接。统一添加前缀和步骤序号。

## 查询

```text
日志平台：https://tetris.qunhequnhe.com/log
service：service.dcs-countertop
```

## 洞判断诊断矩阵

| 结果 | 结论 |
| --- | --- |
| 全部洞 = 0 | 当前台面没有洞，或对象/触发时机不对 |
| 全部洞 > 0，水槽洞 = 0 | 洞关联商品不是 `ProdCategory.SINK` |
| 水槽洞 > 0，台下盆洞 = 0 | 当前水槽不是台下盆，先确认设计事实 |
| 台下盆水槽洞 > 0，Fee = 0 | 厚度、商品或 `Fee.newInstance` 未命中 |
| 已创建日志存在，JSON 无商品 | 查询输出服务和商品有效性 |

## 定义错误

### Fee 未找到

- 创建并发布 `Fee`；
- 业务模块选 `台面`；
- 在“可用类型”确认 `Fee`。

### calcHoleFee 未找到

`calcHoleFee` 只是可选子脚本。可以把逻辑合并到 `generateFee`。若保留，先发布子脚本，再发布调用者。

### generateFee 已存在但不可见

清除筛选并让管理员按唯一标识定位。不要创建改名入口。

### 保存只报格式错误

用最小函数缩小范围，并在浏览器 Network 查看 `/kb-editor/api/customdef` 返回。
