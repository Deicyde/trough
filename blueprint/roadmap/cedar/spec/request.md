---
catalog: module
lean: Cedar.Spec.Request
statement: formalized
proof: formalized
---

# Request

`Cedar.Spec.Request`, in [Cedar/Spec/Request.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Request.lean).

> This file defines Cedar requests.

`Cedar.Spec.Request` (structure, [line 30](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Request.lean#L30))

```lean
public structure Request where
  principal : EntityUID
  action : EntityUID
  resource : EntityUID
  context : Map Attr Value
```

## Depends on

- [Value](value.md)

## Sources

- [Cedar/Spec/Request.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Request.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.Spec.Request.json)
