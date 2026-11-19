---
catalog: module
lean: Cedar.Spec.Ext.toInt?', Cedar.Spec.Ext.toNat?'
statement: formalized
proof: formalized
---

# Ext/Util

`Cedar.Spec.Ext.Util`, in [Cedar/Spec/Ext/Util.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/Util.lean).

`Cedar.Spec.Ext.toInt?'` (definition, [line 11](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/Util.lean#L11))

> Helper function that wraps String.toInt? but returns .none if the string contains '_'.
> This prevents the undocumented behavior where String.toInt? allows '_' characters.

```lean
public def toInt?' (str : String) : Option Int
```

`Cedar.Spec.Ext.toNat?'` (definition, [line 18](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/Util.lean#L18))

> Helper function that wraps String.toNat? but returns .none if the string contains '_'.
> This prevents the undocumented behavior where String.toNat? allows '_' characters.

```lean
public def toNat?' (str : String) : Option Nat
```

## Depends on

Its statements use no other Cedar module's declarations.

## Sources

- [Cedar/Spec/Ext/Util.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/Util.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Spec.Ext.Util.json)
