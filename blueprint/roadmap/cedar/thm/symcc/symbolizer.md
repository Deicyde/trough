---
catalog: module
lean: Cedar.Thm.value_symbolize?_well_typed, Cedar.Thm.value_symbolize?_not_none, Cedar.Thm.value_symbolize?_not_some, Cedar.Thm.value_symbolize?_wf, Cedar.Thm.value?_symbolize?_id, Cedar.Thm.value_symbolize?_is_lit
statement: formalized
proof: formalized
---

# Thm/SymCC/Symbolizer

`Cedar.Thm.SymCC.Symbolizer`, in [Cedar/Thm/SymCC/Symbolizer.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Symbolizer.lean).

> Theorems that `Value.symbolizer?` produces well-formed, well-typed literals.

`Cedar.Thm.value_symbolize?_well_typed` (theorem, [line 33](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Symbolizer.lean#L33))

> The results of `symbolize?` has the correct type.

```lean
theorem value_symbolize?_well_typed
  {Γ : TypeEnv} {v : Value} {ty : CedarType} {t : Term}
  (hwf_ty : ty.WellFormed Γ)
  (hwt_v : InstanceOfType Γ v ty)
  (hsym : v.symbolize? ty = .some t) :
  t.typeOf = TermType.ofType ty
```

`Cedar.Thm.value_symbolize?_not_none` (theorem, [line 158](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Symbolizer.lean#L158))

> The results of `symbolize?` is not Term.none.

```lean
theorem value_symbolize?_not_none
  {v : Value} {ty : CedarType} {t : Term} {ty' : TermType}
  (hsome : v.symbolize? ty = .some t) :
  t ≠ .none ty'
```

`Cedar.Thm.value_symbolize?_not_some` (theorem, [line 182](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Symbolizer.lean#L182))

> The results of `symbolize?` is not Term.some.

```lean
theorem value_symbolize?_not_some
  {v : Value} {ty : CedarType} {t : Term} {t' : Term}
  (hsome : v.symbolize? ty = .some t) :
  t ≠ .some t'
```

`Cedar.Thm.value_symbolize?_wf` (theorem, [line 206](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Symbolizer.lean#L206))

> The results of `symbolize?` is well-formed.

```lean
theorem value_symbolize?_wf
  {Γ : TypeEnv} {env : Env}
  {v : Value} {ty : CedarType} {t : Term}
  (hinst : InstanceOfWellFormedEnvironment env.request env.entities Γ)
  (hwf_ty : ty.WellFormed Γ)
  (hwf_v : v.WellFormed env.entities)
  (hwt_v : InstanceOfType Γ v ty)
  (hsym : v.symbolize? ty = .some t) :
  t.WellFormed (SymEnv.ofEnv Γ).entities
```

`Cedar.Thm.value?_symbolize?_id` (theorem, [line 384](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Symbolizer.lean#L384))

> `symbolize?` is the right inverse of `value?`,
> on sufficiently well-formed inputs

```lean
theorem value?_symbolize?_id
  {Γ : TypeEnv} {entities : Entities}
  {v : Value} {ty : CedarType}
  (hwf_Γ : Γ.WellFormed)
  (hwf_ty : ty.WellFormed Γ)
  (hwf_v : v.WellFormed entities)
  (hwt_v : InstanceOfType Γ v ty) :
  ∃ t,
    v.symbolize? ty = .some t ∧
    t.value? = .some v
```

`Cedar.Thm.value_symbolize?_is_lit` (theorem, [line 739](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Symbolizer.lean#L739))

```lean
theorem value_symbolize?_is_lit
  {v : Value} {ty : CedarType} {t : Term}
  (hsym : v.symbolize? ty = .some t) :
  t.isLiteral
```

## Depends on

- [Cedar/SymCC/Symbolizer](../../symcc/part-01/symbolizer.md)
- [Well-formedness and interpretations](data/basic.md)
- [Typechecker/Types](../validation-2/typechecker-2/types.md)

## Proof depends on

- [ofEnv](env/ofenv.md)
- [ofType](term/oftype.md)

## Sources

- [Cedar/Thm/SymCC/Symbolizer.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Symbolizer.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Thm.SymCC.Symbolizer.json)
