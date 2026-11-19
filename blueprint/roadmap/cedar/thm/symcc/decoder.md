---
catalog: module
lean: Cedar.Thm.default_lit_wf, Cedar.Thm.default_lit_is_lit, Cedar.Thm.default_lit_well_typed
statement: formalized
proof: formalized
---

# Thm/SymCC/Decoder

`Cedar.Thm.SymCC.Decoder`, in [Cedar/Thm/SymCC/Decoder.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Decoder.lean).

> Some facts about `default*`

`Cedar.Thm.default_lit_wf` (theorem, [line 41](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Decoder.lean#L41))

> `Decoder.defaultLit` is well-formed if given
> sufficiently well-formed `eidOf` and `ty`.

```lean
public theorem default_lit_wf
  {εs : SymEntities}
  {eidOf : EntityType → String} {ty : TermType}
  (hwf_ty : ty.WellFormed εs)
  (hwf_eidOf : ∀ ety, εs.isValidEntityType ety → εs.isValidEntityUID { ty := ety, eid := eidOf ety }) :
  (Decoder.defaultLit eidOf ty).WellFormed εs
```

`Cedar.Thm.default_lit_is_lit` (theorem, [line 103](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Decoder.lean#L103))

```lean
public theorem default_lit_is_lit
  {eidOf : EntityType → String} {ty : TermType} :
  (Decoder.defaultLit eidOf ty).isLiteral
```

`Cedar.Thm.default_lit_well_typed` (theorem, [line 122](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Decoder.lean#L122))

```lean
public theorem default_lit_well_typed
  {eidOf : EntityType → String} {ty : TermType} :
  (Decoder.defaultLit eidOf ty).typeOf = ty
```

## Depends on

- [Cedar/SymCC/Decoder](../../symcc/part-01/decoder.md)
- [Well-formedness and interpretations](data/basic.md)

## Proof depends on

- [Properties of literal terms](term/lit.md)

## Sources

- [Cedar/Thm/SymCC/Decoder.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Decoder.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Thm.SymCC.Decoder.json)
