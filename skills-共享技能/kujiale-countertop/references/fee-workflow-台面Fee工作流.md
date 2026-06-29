# 台面 Fee 工作流

## Fee 自定义对象

```text
对象名称：费用
描述：工艺费用
业务模块：台面
自定义对象名称/唯一标识：Fee
继承类型：parammodelMap/ParamModelInstance
数据配置：关闭
```

按当前脚本需要配置属性：

| 属性 | 类型 | 用途 |
| --- | --- | --- |
| `price` | `number` | 工艺费价格 |
| `count` | `number` | 数量，可选 |
| `length` | `number` | 长度，可选 |
| `brandgood` | `brandgood/PBrandgood` | 工艺费商品 |

发布后在台面脚本“可用类型”中确认 `Fee`。

## generateFee 入口

唯一标识必须为：

```text
generateFee
```

函数签名：

```ts
function generateFee(countertop: Countertop): Fee[]
```

其他名称不会被系统自动调用。若提示唯一标识存在，编辑已有入口。

## 商品创建

已验证的历史工艺费案例通常使用：

```ts
buildPBrandGood(数字商品ID)
```

部分环境也提供：

```ts
createPBrandGood("3FO...")
```

只使用当前台面模块“可用脚本”中存在且能通过最小脚本验证的函数。公开案例使用占位符，不提交企业专属商品 ID。

## 发布顺序

1. 发布 `Fee` 自定义对象。
2. 发布可选子脚本。
3. 发布 `generateFee`。
4. 重新生成台面或触发对应输出。
5. 查 `service.dcs-countertop` 日志。
6. 搜索导出 JSON 中的目标商品。
