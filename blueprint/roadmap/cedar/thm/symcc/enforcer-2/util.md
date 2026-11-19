---
catalog: module
lean: Cedar.Thm.interpret_option_entity_term, Cedar.Thm.compile_interpret_entity_implies_wf, Cedar.Thm.wfl_entity, Cedar.Thm.εs_ancestors_find?_implies_ancestors, Cedar.Thm.εs_ancestors_find?_implies_ancestorsOfType, Cedar.Thm.wf_term_interpret_option_entity_implies_wf_typeOf
statement: formalized
proof: formalized
---

# Enforcer/Util

`Cedar.Thm.SymCC.Enforcer.Util`, in [Cedar/Thm/SymCC/Enforcer/Util.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Util.lean).

> This file contains helper lemmas that are shared by assumption proofs.

`Cedar.Thm.interpret_option_entity_term` (theorem, [line 29](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Util.lean#L29))

```lean
theorem interpret_option_entity_term {εs : SymEntities} {I : Interpretation} {t : Term} {ety : EntityType}:
  I.WellFormed εs →
  t.WellFormed εs →
  t.typeOf = .option (.entity ety) →
  t.interpret I = .none (.entity ety) ∨
  ∃ uid : EntityUID, t.interpret I = .some (.entity uid) ∧ uid.ty = ety
```

`Cedar.Thm.compile_interpret_entity_implies_wf` (theorem, [line 47](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Util.lean#L47))

```lean
theorem compile_interpret_entity_implies_wf {x : Expr} {t : Term} {env : Env} {εnv : SymEnv} {I : Interpretation}
  (heq : env ∼ SymEnv.interpret I εnv)
  (hI : I.WellFormed εnv.entities)
  (hwε : εnv.WellFormedFor x)
  (hwe : env.WellFormedFor x)
  (hok : compile x εnv = Except.ok t)
  (ht : Term.interpret I t = (Term.entity uid).some) :
  Value.WellFormed env.entities (Value.prim (Prim.entityUID uid))
```

`Cedar.Thm.wfl_entity` (theorem, [line 63](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Util.lean#L63))

```lean
theorem wfl_entity {uid : EntityUID} {εs : SymEntities} :
  εs.isValidEntityUID uid →
  Term.WellFormedLiteral εs (Term.entity uid)
```

`Cedar.Thm.εs_ancestors_find?_implies_ancestors` (theorem, [line 71](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Util.lean#L71))

```lean
theorem εs_ancestors_find?_implies_ancestors {ety : EntityType} {δ : SymEntityData} {εs : SymEntities} :
  εs.find? ety = some δ →
  εs.ancestors ety = .some δ.ancestors
```

`Cedar.Thm.εs_ancestors_find?_implies_ancestorsOfType` (theorem, [line 79](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Util.lean#L79))

```lean
theorem εs_ancestors_find?_implies_ancestorsOfType {ety₁ ety₂ : EntityType} {δ : SymEntityData} {f : UnaryFunction} {εs : SymEntities} :
  εs.find? ety₁ = some δ →
  δ.ancestors.find? ety₂ = some f →
  εs.ancestorsOfType ety₁ ety₂ = some f
```

`Cedar.Thm.wf_term_interpret_option_entity_implies_wf_typeOf` (theorem, [line 90](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Util.lean#L90))

```lean
theorem wf_term_interpret_option_entity_implies_wf_typeOf {t : Term} {uid : EntityUID} {εs : SymEntities} {I : Interpretation}
  (hI  : I.WellFormed εs)
  (hwt : t.WellFormed εs)
  (ht  : t.interpret I = (Term.entity uid).some) :
  (t.interpret I).WellFormed εs ∧
  t.typeOf = .option (.entity uid.ty)
```

## Depends on

- [Well-formedness and interpretations](../data/basic.md)

## Proof depends on

- [Thm/SymCC/Compiler](../compiler.md)

## Sources

- [Cedar/Thm/SymCC/Enforcer/Util.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Util.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Enforcer.Util.json)
