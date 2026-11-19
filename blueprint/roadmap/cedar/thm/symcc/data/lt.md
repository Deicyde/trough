---
catalog: module
lean: Cedar.Thm.ExtOp.strictLT, Cedar.Thm.TermPrimType.strictLT, Cedar.Thm.TermType.strictLT, Cedar.Thm.UUF.strictLT, Cedar.Thm.PatElem.strictLT, Cedar.Thm.Op.strictLT, Cedar.Thm.TermVar.strictLT, Cedar.Thm.TermPrim.strictLT, Cedar.Thm.Term.strictLT
statement: formalized
proof: formalized
---

# Strict ordering of Cedar terms

`Cedar.Thm.SymCC.Data.LT`, in [Cedar/Thm/SymCC/Data/LT.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/LT.lean).

> This file contains proofs that the less-than (`<`) relation on Cedar terms is
> strict.

`Cedar.Thm.ExtOp.strictLT` (instance, [line 115](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/LT.lean#L115))

```lean
public instance ExtOp.strictLT : StrictLT ExtOp
```

`Cedar.Thm.TermPrimType.strictLT` (instance, [line 171](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/LT.lean#L171))

```lean
public instance TermPrimType.strictLT : StrictLT TermPrimType
```

`Cedar.Thm.TermType.strictLT` (instance, [line 337](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/LT.lean#L337))

```lean
public instance TermType.strictLT : StrictLT TermType
```

`Cedar.Thm.UUF.strictLT` (instance, [line 418](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/LT.lean#L418))

```lean
public instance UUF.strictLT : StrictLT UUF
```

`Cedar.Thm.PatElem.strictLT` (instance, [line 455](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/LT.lean#L455))

```lean
public instance PatElem.strictLT : StrictLT PatElem
```

`Cedar.Thm.Op.strictLT` (instance, [line 654](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/LT.lean#L654))

```lean
public instance Op.strictLT : StrictLT Op
```

`Cedar.Thm.TermVar.strictLT` (instance, [line 707](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/LT.lean#L707))

```lean
public instance TermVar.strictLT : StrictLT TermVar
```

`Cedar.Thm.TermPrim.strictLT` (instance, [line 788](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/LT.lean#L788))

```lean
public instance TermPrim.strictLT : StrictLT TermPrim
```

`Cedar.Thm.Term.strictLT` (instance, [line 1212](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/LT.lean#L1212))

```lean
public instance Term.strictLT : StrictLT Term
```

## Depends on

- [Term](../../../symcc/part-01/term.md)

## Proof depends on

- [Thm/Data/LT](../../data/lt.md)

## Sources

- [Cedar/Thm/SymCC/Data/LT.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/LT.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Data.LT.json)
