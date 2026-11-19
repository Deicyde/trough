---
catalog: module
lean: Cedar.SymCC.compileExtHasAttrRec, Cedar.Thm.compileExtHasAttr_eq_compileExtHasAttrRec
statement: formalized
proof: formalized
---

# ExtHasAttrRec

`Cedar.Thm.SymCC.Compiler.ExtHasAttrRec`, in [Cedar/Thm/SymCC/Compiler/ExtHasAttrRec.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/ExtHasAttrRec.lean).

> In this file we prove the equivalence between a recursive and an iterative compilation
> function for extended has. The specs use the iterative implementation, which is more
> efficient and mirrors the Rust implementation, but the proofs rely on the equivalence
> with the recursive implementation (which mimics the recursive compilation of the
> desugared form of extended-has).
>
> The only public theorem, at the end of this module, is:
> ```
> compileExtHasAttr_eq_compileExtHasAttrRec (...) :
>   compileExtHasAttr t as εs = compileExtHasAttrRec t as εs
> ```

`Cedar.SymCC.compileExtHasAttrRec` (definition, [line 40](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/ExtHasAttrRec.lean#L40))

```lean
public def compileExtHasAttrRec (t : Term) (as : List Attr) (εs : SymEntities) : Result Term
```

`Cedar.Thm.compileExtHasAttr_eq_compileExtHasAttrRec` (theorem, [line 140](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/ExtHasAttrRec.lean#L140))

```lean
public theorem compileExtHasAttr_eq_compileExtHasAttrRec (t : Term) (as : List Attr) (εs : SymEntities) :
  compileExtHasAttr t as εs = compileExtHasAttrRec t as εs
```

## Depends on

- [Cedar/SymCC/Compiler](../../../symcc/part-01/compiler.md)

## Sources

- [Cedar/Thm/SymCC/Compiler/ExtHasAttrRec.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/ExtHasAttrRec.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Compiler.ExtHasAttrRec.json)
