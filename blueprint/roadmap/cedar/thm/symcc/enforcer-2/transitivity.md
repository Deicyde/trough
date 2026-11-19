---
catalog: module
lean: Cedar.Thm.swf_implies_interpret_transitivity, Cedar.Thm.interpret_transitivity_implies_transitive
statement: formalized
proof: formalized
---

# Transitivity

`Cedar.Thm.SymCC.Enforcer.Transitivity`, in [Cedar/Thm/SymCC/Enforcer/Transitivity.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Transitivity.lean).

> This file proves properties of the `transitivity` function in `Cedar/SymCC/Enforcer.lean`.
> -

`Cedar.Thm.swf_implies_interpret_transitivity` (theorem, [line 472](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Transitivity.lean#L472))

```lean
theorem swf_implies_interpret_transitivity {x₁ x₂ : Expr} {t₁ t₂ : Term} {ety₁ ety₂ : EntityType} {env : Env} {εnv : SymEnv} {I : Interpretation}
  (heq : env ∼ SymEnv.interpret I εnv)
  (hI : I.WellFormed εnv.entities)
  (hwε₁ : εnv.WellFormedFor x₁)
  (hwε₂ : εnv.WellFormedFor x₂)
  (hse₁ : env.StronglyWellFormedFor x₁)
  (hse₂ : env.StronglyWellFormedFor x₂)
  (hok₁ : compile x₁ εnv = Except.ok t₁)
  (hok₂ : compile x₂ εnv = Except.ok t₂)
  (hty₁ : t₁.typeOf = .option (.entity ety₁))
  (hty₂ : t₂.typeOf = .option (.entity ety₂)) :
  (transitivity t₁ t₂ εnv.entities).interpret I = true
```

`Cedar.Thm.interpret_transitivity_implies_transitive` (theorem, [line 574](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Transitivity.lean#L574))

```lean
theorem interpret_transitivity_implies_transitive
  {uid₁ uid₂ uid₃ : EntityUID} {t₁ t₂ : Term} {ts₁₂ ts₂₃ : Set Term}
  {δ₁ δ₂ : SymEntityData} {f₁₂ f₂₃ : UUF} {εnv : SymEnv} {I : Interpretation}
  (hwε  : εnv.WellFormed)
  (hI   : I.WellFormed εnv.entities)
  (hwt₁ : t₁.WellFormed εnv.entities)
  (hwt₂ : t₂.WellFormed εnv.entities)
  (ht₁  : t₁.interpret I = (Term.entity uid₁).some)
  (ht₂  : t₂.interpret I = (Term.entity uid₂).some)
  (hδ₁  : εnv.entities.find? uid₁.ty = some δ₁)
  (hf₁  : δ₁.ancestors.find? uid₂.ty = some (UnaryFunction.uuf f₁₂))
  (heq₁ : app ((UnaryFunction.uuf f₁₂).interpret I) (.entity uid₁) = .set ts₁₂ (.entity uid₂.ty))
  (hin₁ : Term.entity uid₂ ∈ ts₁₂)
  (hδ₂  : εnv.entities.find? uid₂.ty = some δ₂)
  (hf₂  : δ₂.ancestors.find? uid₃.ty = some (UnaryFunction.uuf f₂₃))
  (heq₂ : app ((UnaryFunction.uuf f₂₃).interpret I) (.entity uid₂) = .set ts₂₃ (.entity uid₃.ty))
  (hin₂ : Term.entity uid₃ ∈ ts₂₃)
  (htr  : (transitivity t₁ t₂ εnv.entities).interpret I = true) :
  ∃ f₁₃ ts₁₃,
    δ₁.ancestors.find? uid₃.ty = some f₁₃ ∧
    app (f₁₃.interpret I) (.entity uid₁) = .set ts₁₃ (.entity uid₃.ty) ∧
    Term.entity uid₃ ∈ ts₁₃
```

## Depends on

- [Strongly well-formed ancestor relations](../data/hierarchy.md)

## Proof depends on

- [Enforcer/Util](util.md)
- [Basic properties of strongly well-formed symbolic environments](../env/swf.md)

## Sources

- [Cedar/Thm/SymCC/Enforcer/Transitivity.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Transitivity.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Enforcer.Transitivity.json)
