---
catalog: module
lean: Cedar.Thm.swf_implies_interpret_acyclicity, Cedar.Thm.interpret_acyclicity_implies_acyclic
statement: formalized
proof: formalized
---

# Acyclicity

`Cedar.Thm.SymCC.Enforcer.Acyclicity`, in [Cedar/Thm/SymCC/Enforcer/Acyclicity.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Acyclicity.lean).

> This file proves properties of the `acyclicity` function in `Cedar/SymCC/Enforcer.lean`.
> -

`Cedar.Thm.swf_implies_interpret_acyclicity` (theorem, [line 101](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Acyclicity.lean#L101))

```lean
theorem swf_implies_interpret_acyclicity {x : Expr} {t : Term} {ety : EntityType} {env : Env} {εnv : SymEnv} {I : Interpretation}
  (heq : env ∼ SymEnv.interpret I εnv)
  (hI : I.WellFormed εnv.entities)
  (hwε : εnv.WellFormedFor x)
  (hse : env.StronglyWellFormedFor x)
  (hok : compile x εnv = Except.ok t)
  (hty : t.typeOf = .option (.entity ety)) :
  (acyclicity t εnv.entities).interpret I = true
```

`Cedar.Thm.interpret_acyclicity_implies_acyclic` (theorem, [line 130](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Acyclicity.lean#L130))

```lean
theorem interpret_acyclicity_implies_acyclic {t : Term} {ts : Set Term} {uid : EntityUID} {δ : SymEntityData} {f : UUF} {εnv : SymEnv} {I : Interpretation}
  (hwε : εnv.WellFormed)
  (hI  : I.WellFormed εnv.entities)
  (hwt : t.WellFormed εnv.entities)
  (hδ  : Map.find? εnv.entities uid.ty = some δ)
  (hf  : δ.ancestors.find? uid.ty = some (UnaryFunction.uuf f))
  (ht  : t.interpret I = (Term.entity uid).some)
  (heq : app ((UnaryFunction.uuf f).interpret I) (Term.entity uid) = Term.set ts (TermType.entity uid.ty))
  (ha  : Term.interpret I (acyclicity t εnv.entities) = true) :
  Term.entity uid ∉ ts
```

## Depends on

- [Strongly well-formed ancestor relations](../data/hierarchy.md)

## Proof depends on

- [Enforcer/Util](util.md)
- [Basic properties of strongly well-formed symbolic environments](../env/swf.md)

## Sources

- [Cedar/Thm/SymCC/Enforcer/Acyclicity.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Acyclicity.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Enforcer.Acyclicity.json)
