---
catalog: module
lean: Cedar.Thm.compile_evaluate_hasAttr_record, Cedar.Thm.compile_evaluate_hasAttr_entity, Cedar.Thm.compile_evaluate_hasAttr, Cedar.Thm.interpret_compileHasAttr, Cedar.Thm.compileHasAttr_false_of_getAttr_error_typeOf_eq, Cedar.Thm.compileGetAttr_noSuchAttribute_of_error_typeOf_eq, Cedar.Thm.interpret_compileGetAttr_error_of_compileHasAttr_false, Cedar.Thm.interpret_option_get_aux, Cedar.Thm.compileHasAttr_interpret_ok, Cedar.Thm.compile_interpret_hasAttr, Cedar.Thm.compile_evaluate_getAttr_record, Cedar.Thm.compile_evaluate_getAttr_entity, Cedar.Thm.compile_evaluate_getAttr, Cedar.Thm.interpret_compileGetAttr, Cedar.Thm.compileGetAttr_interpret_ok, Cedar.Thm.compileGetAttr_ok_typeOf_eq, Cedar.Thm.compile_interpret_getAttr
statement: formalized
proof: formalized
---

# Attr

`Cedar.Thm.SymCC.Compiler.Attr`, in [Cedar/Thm/SymCC/Compiler/Attr.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Attr.lean).

> This file proves the compilation lemmas for `.hasAttr` and `.getAttr` expressions.
> -

`Cedar.Thm.compile_evaluate_hasAttr_record` (theorem, [line 76](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Attr.lean#L76))

```lean
theorem compile_evaluate_hasAttr_record
  {a : Attr} {v₁ : Value} {es : Entities}
  {εs : SymEntities} {t₁ t₂ : Term} {ty₁ : TermType} {rty rty': Map Attr TermType}
  (hwφ₁ : Term.WellFormed εs t₁)
  (hty₁ : Term.typeOf t₁ = TermType.option ty₁)
  (hwo : Term.WellFormed εs (option.get t₁) ∧ Term.typeOf (option.get t₁) = TermType.record rty')
  (hwφ₂: Term.WellFormed εs t₂ ∧ Term.typeOf t₂ = TermType.option TermType.bool)
  (ha : RecordHasAttr t₂ (option.get t₁) rty a)
  (ih : (Except.ok v₁ : Spec.Result Value) ∼ t₁) :
  (hasAttr v₁ a es : Spec.Result Value) ∼ ifSome t₁ t₂
```

`Cedar.Thm.compile_evaluate_hasAttr_entity` (theorem, [line 145](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Attr.lean#L145))

```lean
theorem compile_evaluate_hasAttr_entity
  {a : Attr} {v₁ : Value} {es : Entities}
  {εs : SymEntities} {t₁ t₂ : Term} {fₐ : UnaryFunction}
  {ety : EntityType} {rty : Map Attr TermType}
  (heq : SameEntities es εs)
  (hwε : εs.WellFormed)
  (hwf₁ : Value.WellFormed es v₁)
  (hwφ₁ : Term.WellFormed εs t₁)
  (hty₁ : Term.typeOf t₁ = TermType.option (.entity ety))
  (hwo  : Term.WellFormed εs (option.get t₁) ∧ Term.typeOf (option.get t₁) = .entity ety)
  (hwφ₂ : Term.WellFormed εs t₂ ∧ Term.typeOf t₂ = TermType.option TermType.bool)
  (hf : εs.attrs ety = some fₐ)
  (ha : RecordHasAttr t₂ (app fₐ (option.get t₁)) rty a)
  (ih : (Except.ok v₁ : Spec.Result Value) ∼ t₁) :
  (hasAttr v₁ a es : Spec.Result Value) ∼ ifSome t₁ t₂
```

`Cedar.Thm.compile_evaluate_hasAttr` (theorem, [line 186](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Attr.lean#L186))

```lean
theorem compile_evaluate_hasAttr {x₁ : Expr} {a : Attr} {env : Env} {εnv : SymEnv} {t : Term}
  (heq : env ∼ εnv)
  (hwe : env.WellFormedFor (.hasAttr x₁ a))
  (hwε : εnv.WellFormedFor (.hasAttr x₁ a))
  (hok : compile (.hasAttr x₁ a) εnv = .ok t)
  (ih  : CompileEvaluate x₁) :
  evaluate (.hasAttr x₁ a) env.request env.entities ∼ t
```

`Cedar.Thm.interpret_compileHasAttr` (theorem, [line 260](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Attr.lean#L260))

```lean
theorem interpret_compileHasAttr {t t₁: Term} {a : Attr} {εs : SymEntities} {I : Interpretation}
  (hwε : εs.WellFormed)
  (hI  : Interpretation.WellFormed I εs)
  (hwt : Term.WellFormed εs t₁)
  (hok : compileHasAttr t₁ a εs = Except.ok t) :
  compileHasAttr (t₁.interpret I) a (εs.interpret I) = .ok (t.interpret I)
```

`Cedar.Thm.compileHasAttr_false_of_getAttr_error_typeOf_eq` (theorem, [line 332](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Attr.lean#L332))

```lean
theorem compileHasAttr_false_of_getAttr_error_typeOf_eq
  {t₁ t₂ : Term} {a : Attr} {εs : SymEntities} {e : SymCC.Error}
  (hwε : εs.WellFormed)
  (hw₁ : t₁.WellFormed εs)
  (hw₂ : t₂.WellFormed εs)
  (hty : t₁.typeOf = t₂.typeOf)
  (hha : compileHasAttr t₁ a εs = .ok (⊙ false))
  (hga : compileGetAttr t₁ a εs = .error e) :
  compileHasAttr t₂ a εs = .ok (⊙ false)
```

`Cedar.Thm.compileGetAttr_noSuchAttribute_of_error_typeOf_eq` (theorem, [line 350](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Attr.lean#L350))

```lean
theorem compileGetAttr_noSuchAttribute_of_error_typeOf_eq
  {t₁ t₂ : Term} {a : Attr} {εs : SymEntities} {e : SymCC.Error}
  (hwε : εs.WellFormed)
  (hw₁ : t₁.WellFormed εs)
  (hw₂ : t₂.WellFormed εs)
  (hty : t₁.typeOf = t₂.typeOf)
  (hha : compileHasAttr t₁ a εs = .ok (⊙ false))
  (hga : compileGetAttr t₁ a εs = .error e) :
  compileGetAttr t₂ a εs = .error .noSuchAttribute
```

`Cedar.Thm.interpret_compileGetAttr_error_of_compileHasAttr_false` (theorem, [line 368](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Attr.lean#L368))

```lean
theorem interpret_compileGetAttr_error_of_compileHasAttr_false
  {t₁ : Term} {a : Attr} {εs : SymEntities} {I : Interpretation} {e : SymCC.Error}
  (hwε : εs.WellFormed)
  (hI : I.WellFormed εs)
  (hwt : t₁.WellFormed εs)
  (hha : compileHasAttr t₁ a εs = .ok (⊙ false))
  (hga : compileGetAttr t₁ a εs = .error e) :
  compileGetAttr (t₁.interpret I) a (εs.interpret I) = .error .noSuchAttribute
```

`Cedar.Thm.interpret_option_get_aux` (theorem, [line 387](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Attr.lean#L387))

```lean
theorem interpret_option_get_aux {εs : SymEntities} {I : Interpretation} {t : Term} {ty : TermType}
  (hI  : I.WellFormed εs)
  (hwt : t.WellFormed εs)
  (hty : t.typeOf = .option ty) :
  Term.WellFormed (SymEntities.interpret I εs) (Term.interpret I (option.get t)) ∧
  Term.WellFormed (SymEntities.interpret I εs) (option.get (Term.interpret I t)) ∧
  Term.typeOf (Term.interpret I (option.get t)) = Term.typeOf (option.get (Term.interpret I t))
```

`Cedar.Thm.compileHasAttr_interpret_ok` (theorem, [line 407](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Attr.lean#L407))

```lean
theorem compileHasAttr_interpret_ok {εs : SymEntities} {I : Interpretation}
  {t₁ t_ha : Term} {a : Attr} {ty : TermType}
  (hI : I.WellFormed εs) (hwε : εs.WellFormed)
  (hwt : t₁.WellFormed εs) (hty : t₁.typeOf = .option ty)
  (hi : compileHasAttr ((option.get t₁).interpret I) a (εs.interpret I) = .ok (t_ha.interpret I)) :
  ∃ t', compileHasAttr (option.get (t₁.interpret I)) a (εs.interpret I) = .ok t'
```

`Cedar.Thm.compile_interpret_hasAttr` (theorem, [line 418](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Attr.lean#L418))

```lean
theorem compile_interpret_hasAttr {x₁ : Expr} {a : Attr} {εnv : SymEnv} {I : Interpretation} {t : Term}
  (hI  : I.WellFormed εnv.entities)
  (hwε : εnv.WellFormedFor (.hasAttr x₁ a))
  (hok : compile (.hasAttr x₁ a) εnv = .ok t)
  (ih  : CompileInterpret x₁) :
  compile (.hasAttr x₁ a) (εnv.interpret I) = .ok (t.interpret I)
```

`Cedar.Thm.compile_evaluate_getAttr_record` (theorem, [line 488](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Attr.lean#L488))

```lean
theorem compile_evaluate_getAttr_record
  {a : Attr} {v₁ : Value} {es : Entities}
  {εs : SymEntities} {t₁ t₂ : Term} {ty₁ tyₐ : TermType} {rty rty': Map Attr TermType}
  (hwφ₁ : Term.WellFormed εs t₁)
  (hty₁ : Term.typeOf t₁ = TermType.option ty₁)
  (hwo  : Term.WellFormed εs (option.get t₁) ∧ Term.typeOf (option.get t₁) = TermType.record rty')
  (hwφ₂ : Term.WellFormed εs t₂)
  (htyₐ : Term.typeOf t₂ = TermType.option tyₐ)
  (ha   : RecordGetAttr t₂ (option.get t₁) rty a)
  (ih   : (Except.ok v₁ : Spec.Result Value) ∼ t₁) :
  (getAttr v₁ a es : Spec.Result Value) ∼ ifSome t₁ t₂
```

`Cedar.Thm.compile_evaluate_getAttr_entity` (theorem, [line 526](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Attr.lean#L526))

```lean
theorem compile_evaluate_getAttr_entity
  {a : Attr} {v₁ : Value} {es : Entities}
  {εs : SymEntities} {t₁ t₂ : Term} {fₐ : UnaryFunction}
  {ety : EntityType} {tyₐ : TermType} {rty : Map Attr TermType}
  (heq : SameEntities es εs)
  (hwε : εs.WellFormed)
  (hwf₁ : Value.WellFormed es v₁)
  (hwφ₁ : Term.WellFormed εs t₁)
  (hty₁ : Term.typeOf t₁ = TermType.option (.entity ety))
  (hwo  : Term.WellFormed εs (option.get t₁) ∧ Term.typeOf (option.get t₁) = .entity ety)
  (hwφ₂ : Term.WellFormed εs t₂)
  (htyₐ : Term.typeOf t₂ = TermType.option tyₐ)
  (hf : εs.attrs ety = some fₐ)
  (ha : RecordGetAttr t₂ (app fₐ (option.get t₁)) rty a)
  (ih : (Except.ok v₁ : Spec.Result Value) ∼ t₁) :
  (getAttr v₁ a es : Spec.Result Value) ∼ ifSome t₁ t₂
```

`Cedar.Thm.compile_evaluate_getAttr` (theorem, [line 573](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Attr.lean#L573))

```lean
theorem compile_evaluate_getAttr {x₁ : Expr} {a : Attr} {env : Env} {εnv : SymEnv} {t : Term}
  (heq : env ∼ εnv)
  (hwe : env.WellFormedFor (.getAttr x₁ a))
  (hwε : εnv.WellFormedFor (.getAttr x₁ a))
  (hok : compile (.getAttr x₁ a) εnv = .ok t)
  (ih  : CompileEvaluate x₁) :
  evaluate (.getAttr x₁ a) env.request env.entities ∼ t
```

`Cedar.Thm.interpret_compileGetAttr` (theorem, [line 610](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Attr.lean#L610))

```lean
theorem interpret_compileGetAttr {t t₁: Term} {a : Attr} {εs : SymEntities} {I : Interpretation}
  (hwε : εs.WellFormed)
  (hI  : Interpretation.WellFormed I εs)
  (hwt : Term.WellFormed εs t₁)
  (hok : compileGetAttr t₁ a εs = Except.ok t) :
  compileGetAttr (t₁.interpret I) a (εs.interpret I) = .ok (t.interpret I)
```

`Cedar.Thm.compileGetAttr_interpret_ok` (theorem, [line 669](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Attr.lean#L669))

```lean
theorem compileGetAttr_interpret_ok {εs : SymEntities} {I : Interpretation}
  {t₁ t_ga : Term} {a : Attr} {ty : TermType}
  (hI : I.WellFormed εs) (hwε : εs.WellFormed)
  (hwt : t₁.WellFormed εs) (hty : t₁.typeOf = .option ty)
  (hi : compileGetAttr ((option.get t₁).interpret I) a (εs.interpret I) = .ok (t_ga.interpret I)) :
  ∃ t', compileGetAttr (option.get (t₁.interpret I)) a (εs.interpret I) = .ok t'
```

`Cedar.Thm.compileGetAttr_ok_typeOf_eq` (theorem, [line 721](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Attr.lean#L721))

```lean
theorem compileGetAttr_ok_typeOf_eq {t t₁ t₂ t₃ : Term} {a : Attr} {εs : SymEntities}
  (hwε : εs.WellFormed)
  (hw₁ : t₁.WellFormed εs)
  (hw₂ : t₂.WellFormed εs)
  (hty : t₁.typeOf = t₂.typeOf)
  (hok₁ : compileGetAttr t₁ a εs = Except.ok t)
  (hok₂ : compileGetAttr t₂ a εs = Except.ok t₃) :
  t₃.typeOf = t.typeOf
```

`Cedar.Thm.compile_interpret_getAttr` (theorem, [line 749](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Attr.lean#L749))

```lean
theorem compile_interpret_getAttr {x₁ : Expr} {a : Attr} {εnv : SymEnv} {I : Interpretation} {t : Term}
  (hI  : I.WellFormed εnv.entities)
  (hwε : εnv.WellFormedFor (.getAttr x₁ a))
  (hok : compile (.getAttr x₁ a) εnv = .ok t)
  (ih  : CompileInterpret x₁) :
  compile (.getAttr x₁ a) (εnv.interpret I) = .ok (t.interpret I)
```

## Depends on

- [Compiler/Basic](basic.md)
- [Invert](invert.md)

## Proof depends on

- [Compiler/WellTyped](welltyped.md)
- [Properties of interpretations on symbolic environments](../env/interpret.md)
- [Interpretation of Factory functions](../term/interpret/factory.md)
- [Properties of the `Same` predicate on Terms](../term/same.md)

## Sources

- [Cedar/Thm/SymCC/Compiler/Attr.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Attr.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Compiler.Attr.json)
