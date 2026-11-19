---
catalog: module
lean: BitVec.width, BitVec.signedMin, BitVec.signedMax, BitVec.overflows, Cedar.SymCC.EntityTag, Cedar.SymCC.EntityTag.mk, Cedar.SymCC.EntityTag.wf
statement: formalized
proof: formalized
---

# Data

`Cedar.SymCC.Data`, in [Cedar/SymCC/Data.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Data.lean).

> This file contains generic utility functions shared by `SymCC` modules.

`BitVec.width` (definition, [line 26](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Data.lean#L26))

```lean
public def BitVec.width {n : Nat} (_ : BitVec n) : Nat
```

`BitVec.signedMin` (definition, [line 28](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Data.lean#L28))

```lean
public def BitVec.signedMin (n : Nat) : Int
```

`BitVec.signedMax` (definition, [line 30](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Data.lean#L30))

```lean
public def BitVec.signedMax (n : Nat) : Int
```

`BitVec.overflows` (definition, [line 32](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Data.lean#L32))

```lean
public def BitVec.overflows (n : Nat) (i : Int) : Bool
```

`Cedar.SymCC.EntityTag` (abbreviation, [line 40](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Data.lean#L40))

```lean
public abbrev EntityTag (α)
```

`Cedar.SymCC.EntityTag.mk` (abbreviation, [line 42](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Data.lean#L42))

```lean
public abbrev EntityTag.mk {α} (entity tag : α) : EntityTag α
```

`Cedar.SymCC.EntityTag.wf` (abbreviation, [line 45](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Data.lean#L45))

```lean
public abbrev EntityTag.wf {α} : EntityTag α → Bool
```

## Depends on

- [Map](../../data/map.md)

## Sources

- [Cedar/SymCC/Data.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Data.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.SymCC.Data.json)
