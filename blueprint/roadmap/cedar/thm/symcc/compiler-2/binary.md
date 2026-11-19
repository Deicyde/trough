---
catalog: module
lean: Cedar.Thm.interpret_compileInₑ, Cedar.Thm.interpret_compileInₛ, Cedar.Thm.interpret_hasTag, Cedar.Thm.interpret_getTag, Cedar.Thm.compile_interpret_binaryApp, Cedar.Thm.same_entities_ancestors_none_of_type, Cedar.Thm.same_entities_ancestors_some_of_type, Cedar.Thm.compile_evaluate_binaryApp
statement: formalized
proof: formalized
---

# Compiler/Binary

`Cedar.Thm.SymCC.Compiler.Binary`, in [Cedar/Thm/SymCC/Compiler/Binary.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Binary.lean).

> This file proves the compilation lemmas for `.binaryApp` expressions.
> -

`Cedar.Thm.interpret_compileInₑ` (theorem, [line 74](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Binary.lean#L74))

```lean
theorem interpret_compileInₑ {t₁ t₂: Term} {ety₁ ety₂ : EntityType} {εs : SymEntities} {I : Interpretation}
  (hwε : SymEntities.WellFormed εs)
  (hI : Interpretation.WellFormed I εs)
  (hwφ₁ : Term.WellFormed εs t₁)
  (hwφ₂ : Term.WellFormed εs t₂)
  (hwl₁ : Term.WellFormed εs (Term.interpret I t₁) ∧ Term.typeOf (Term.interpret I t₁) = Term.typeOf t₁)
  (hwl₂ : Term.WellFormed εs (Term.interpret I t₂) ∧ Term.typeOf (Term.interpret I t₂) = Term.typeOf t₂)
  (hty₁ : Term.typeOf t₁ = TermType.entity ety₁)
  (hty₂ : Term.typeOf t₂ = TermType.entity ety₂) :
  Term.interpret I (SymCC.compileInₑ t₁ t₂ (SymEntities.ancestorsOfType εs ety₁ ety₂)) =
  SymCC.compileInₑ (Term.interpret I t₁) (Term.interpret I t₂) (SymEntities.ancestorsOfType (SymEntities.interpret I εs) ety₁ ety₂)
```

`Cedar.Thm.interpret_compileInₛ` (theorem, [line 139](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Binary.lean#L139))

```lean
theorem interpret_compileInₛ {t₁ t₂: Term} {ety₁ ety₂ : EntityType} {εs : SymEntities} {I : Interpretation}
  (hwε : SymEntities.WellFormed εs)
  (hI : Interpretation.WellFormed I εs)
  (hwφ₁ : Term.WellFormed εs t₁)
  (hwφ₂ : Term.WellFormed εs t₂)
  (hwl₁ : Term.WellFormed εs (Term.interpret I t₁) ∧ Term.typeOf (Term.interpret I t₁) = Term.typeOf t₁)
  (hwl₂ : Term.WellFormed εs (Term.interpret I t₂) ∧ Term.typeOf (Term.interpret I t₂) = Term.typeOf t₂)
  (hty₁ : Term.typeOf t₁ = .entity ety₁)
  (hty₂ : Term.typeOf t₂ = .set (.entity ety₂)) :
  Term.interpret I (SymCC.compileInₛ t₁ t₂ (SymEntities.ancestorsOfType εs ety₁ ety₂)) =
  SymCC.compileInₛ (Term.interpret I t₁) (Term.interpret I t₂) (SymEntities.ancestorsOfType (SymEntities.interpret I εs) ety₁ ety₂)
```

`Cedar.Thm.interpret_hasTag` (theorem, [line 160](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Binary.lean#L160))

```lean
theorem interpret_hasTag {t₁ t₂ : Term} {ety : EntityType} {εs : SymEntities} {τs : SymTags} {I : Interpretation}
  (hwτ : τs.WellFormed εs ety)
  (hI : I.WellFormed εs)
  (hwφ₁ : Term.WellFormed εs t₁)
  (hwφ₂ : Term.WellFormed εs t₂)
  (hty₁ : t₁.typeOf = TermType.entity ety) :
  (SymTags.interpret I τs).hasTag (Term.interpret I t₁) (Term.interpret I t₂) = Term.interpret I (τs.hasTag t₁ t₂)
```

`Cedar.Thm.interpret_getTag` (theorem, [line 174](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Binary.lean#L174))

```lean
theorem interpret_getTag {t₁ t₂ : Term} {ety : EntityType} {εs : SymEntities} {τs : SymTags} {I : Interpretation}
  (hwτ : τs.WellFormed εs ety)
  (hI : I.WellFormed εs)
  (hwφ₁ : Term.WellFormed εs t₁)
  (hwφ₂ : Term.WellFormed εs t₂)
  (hty₁ : t₁.typeOf = TermType.entity ety)
  (hty₂ : t₂.typeOf = .string) :
  (SymTags.interpret I τs).getTag (Term.interpret I t₁) (Term.interpret I t₂) = Term.interpret I (τs.getTag t₁ t₂)
```

`Cedar.Thm.compile_interpret_binaryApp` (theorem, [line 346](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Binary.lean#L346))

```lean
theorem compile_interpret_binaryApp {op₂ : BinaryOp} {x₁ x₂ : Expr} {εnv : SymEnv} {I : Interpretation} {t : Term}
  (hI  : I.WellFormed εnv.entities)
  (hwε : εnv.WellFormedFor (.binaryApp op₂ x₁ x₂))
  (hok : compile (.binaryApp op₂ x₁ x₂) εnv = .ok t)
  (ih₁ : CompileInterpret x₁)
  (ih₂ : CompileInterpret x₂) :
  compile (.binaryApp op₂ x₁ x₂) (εnv.interpret I) = .ok (t.interpret I)
```

`Cedar.Thm.same_entities_ancestors_none_of_type` (theorem, [line 779](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Binary.lean#L779))

```lean
theorem same_entities_ancestors_none_of_type {es : Entities} {εs : SymEntities} {e₁ e₂ : EntityUID}
  (heq : es ∼ εs)
  (hno : SymEntities.ancestorsOfType εs e₁.ty e₂.ty = none) :
  ¬ e₂ ∈ Entities.ancestorsOrEmpty es e₁
```

`Cedar.Thm.same_entities_ancestors_some_of_type` (theorem, [line 800](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Binary.lean#L800))

```lean
theorem same_entities_ancestors_some_of_type {es : Entities} {εs : SymEntities} {e₁ : EntityUID} {ety₂ : EntityType} {ancs : UnaryFunction}
  (heq : es ∼ εs)
  (hwf : Value.WellFormed es (Value.prim (Prim.entityUID e₁)))
  (hso : SymEntities.ancestorsOfType εs e₁.ty ety₂ = some ancs) :
  ∃ (ts : Set Term),
    app ancs (Term.prim (TermPrim.entity e₁)) = Term.set ts (TermType.entity ety₂) ∧
    (Term.set ts (TermType.entity ety₂)).isLiteral ∧
    (∀ (e₂ : EntityUID), e₂.ty = ety₂ →
      ((Term.prim (TermPrim.entity e₂) ∈ ts ↔ e₂ ∈ Entities.ancestorsOrEmpty es e₁)))
```

`Cedar.Thm.compile_evaluate_binaryApp` (theorem, [line 1278](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Binary.lean#L1278))

```lean
theorem compile_evaluate_binaryApp {op₂ : BinaryOp} {x₁ x₂ : Expr} {env : Env} {εnv : SymEnv} {t : Term}
  (heq : env ∼ εnv)
  (hwe : env.WellFormedFor (.binaryApp op₂ x₁ x₂))
  (hwε : εnv.WellFormedFor (.binaryApp op₂ x₁ x₂))
  (hok : compile (.binaryApp op₂ x₁ x₂) εnv = .ok t)
  (ih₁ : CompileEvaluate x₁)
  (ih₂ : CompileEvaluate x₂) :
  evaluate (.binaryApp op₂ x₁ x₂) env.request env.entities ∼ t
```

## Depends on

- [Compiler/Basic](basic.md)

## Proof depends on

- [Compiler/WF](wf.md)
- [Properties of interpretations on symbolic environments](../env/interpret.md)
- [Interpretation of Factory functions](../term/interpret/factory.md)
- [Properties of the `Same` predicate on Terms](../term/same.md)

## Sources

- [Cedar/Thm/SymCC/Compiler/Binary.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Binary.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Compiler.Binary.json)
