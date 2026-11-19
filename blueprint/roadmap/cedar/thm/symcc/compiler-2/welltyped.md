---
catalog: module
lean: Cedar.Thm.CompileWellTyped, Cedar.Thm.CompileWellTypedCondition, Cedar.Thm.CompileWellTypedAndWF, Cedar.Thm.ofRecordType_preserves_attr, Cedar.Thm.isCedarRecordType_implies_isRecordType, Cedar.Thm.compile_well_typed_lit, Cedar.Thm.compile_well_typed_var, Cedar.Thm.compile_well_typed_ite, Cedar.Thm.compile_well_typed_or_and, Cedar.Thm.compile_well_typed_unaryApp, Cedar.Thm.compile_binaryApp_wf_types, Cedar.Thm.compile_ok_implies_compile_well_typed_binaryApp, Cedar.Thm.compile_well_typed_binaryApp, Cedar.Thm.compile_well_typed_getAttr, Cedar.Thm.compile_well_typed_hasAttr, Cedar.Thm.compileHasAttr_always_ok, Cedar.Thm.compileGetAttr_always_ok, Cedar.Thm.compileExtHasAttrRec_ne_error, Cedar.Thm.compile_well_typed_extHasAttr, Cedar.Thm.compile_well_typed_set, Cedar.Thm.compile_well_typed_record, Cedar.Thm.compile_well_typed_call, Cedar.Thm.compile_well_typed_on_wf_expr
statement: formalized
proof: formalized
---

# Compiler/WellTyped

`Cedar.Thm.SymCC.Compiler.WellTyped`, in [Cedar/Thm/SymCC/Compiler/WellTyped.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/WellTyped.lean).

> This file contains theorems saying that `compile` succeeds
> with the correct term type on well-typed expressions.

`Cedar.Thm.CompileWellTyped` (definition, [line 27](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/WellTyped.lean#L27))

> States the symbolic compiler succeeds on a typed expression `tx` and
> produces a term `t` with the corresponding type.

```lean
def CompileWellTyped (tx : TypedExpr) (εnv : SymEnv) : Prop
```

`Cedar.Thm.CompileWellTypedCondition` (definition, [line 35](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/WellTyped.lean#L35))

> A sufficient condition for `CompileWellTyped` to hold.

```lean
def CompileWellTypedCondition (tx : TypedExpr) (Γ : TypeEnv) (εnv : SymEnv) : Prop
```

`Cedar.Thm.CompileWellTypedAndWF` (definition, [line 44](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/WellTyped.lean#L44))

> A stronger version of `CompileWellTyped` that
> also includes well-formedness of the term

```lean
def CompileWellTypedAndWF (tx : TypedExpr) (εnv : SymEnv) : Prop
```

`Cedar.Thm.ofRecordType_preserves_attr` (theorem, [line 80](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/WellTyped.lean#L80))

> If some attribute exists in a record type,
> then it should still exist after applying `TermType.ofRecordType`

```lean
theorem ofRecordType_preserves_attr
  {rty : RecordType} {attr : Attr} {qty : Qualified CedarType} {ty : CedarType}
  (hattr_exists : Data.Map.find? rty attr = some qty)
  (hattr_ty : qty.getType = ty) :
  ∃ attr_ty : TermType,
    (Data.Map.mk (TermType.ofRecordType rty.1)).find? attr = some attr_ty ∧
    match attr_ty with
    | .option attr_ty' => TermType.ofType ty = attr_ty' ∧ ¬qty.isRequired
    | _ => TermType.ofType ty = attr_ty ∧ qty.isRequired
```

`Cedar.Thm.isCedarRecordType_implies_isRecordType` (theorem, [line 174](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/WellTyped.lean#L174))

```lean
theorem isCedarRecordType_implies_isRecordType
  {ty : TermType}
  (hty : TermType.isCedarRecordType ty) :
  TermType.isRecordType ty
```

`Cedar.Thm.compile_well_typed_lit` (theorem, [line 403](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/WellTyped.lean#L403))

```lean
theorem compile_well_typed_lit {p : Prim} {tx : CedarType} {Γ : TypeEnv} {εnv : SymEnv}
  (h : CompileWellTypedCondition (.lit p tx) Γ εnv) :
  CompileWellTyped (.lit p tx) εnv
```

`Cedar.Thm.compile_well_typed_var` (theorem, [line 422](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/WellTyped.lean#L422))

```lean
theorem compile_well_typed_var {v : Var} {ty : CedarType} {Γ : TypeEnv} {εnv : SymEnv}
  (hcond : CompileWellTypedCondition (.var v ty) Γ εnv) :
  CompileWellTyped (.var v ty) εnv
```

`Cedar.Thm.compile_well_typed_ite` (theorem, [line 460](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/WellTyped.lean#L460))

```lean
theorem compile_well_typed_ite
  {a : TypedExpr} {b : TypedExpr} {c : TypedExpr} {ty : CedarType}
  {Γ : TypeEnv} {εnv : SymEnv}
  (iha : CompileWellTypedAndWF a εnv)
  (ihb : CompileWellTypedAndWF b εnv)
  (ihc : CompileWellTypedAndWF c εnv)
  (hcond_ite : CompileWellTypedCondition (.ite a b c ty) Γ εnv) :
  CompileWellTyped (.ite a b c ty) εnv
```

`Cedar.Thm.compile_well_typed_or_and` (theorem, [line 512](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/WellTyped.lean#L512))

> Combined case for `or` and `and`

```lean
theorem compile_well_typed_or_and
  {a : TypedExpr} {b : TypedExpr} {ty : CedarType}
  {Γ : TypeEnv} {εnv : SymEnv}
  (iha : CompileWellTypedAndWF a εnv)
  (ihb : CompileWellTypedAndWF b εnv) :
  (CompileWellTypedCondition (.or a b ty) Γ εnv →
    CompileWellTyped (.or a b ty) εnv) ∧
  (CompileWellTypedCondition (.and a b ty) Γ εnv →
    CompileWellTyped (.and a b ty) εnv)
```

`Cedar.Thm.compile_well_typed_unaryApp` (theorem, [line 556](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/WellTyped.lean#L556))

```lean
theorem compile_well_typed_unaryApp
  {op : UnaryOp} {expr : TypedExpr} {ty : CedarType}
  {Γ : TypeEnv} {εnv : SymEnv}
  (ihexpr : CompileWellTypedAndWF expr εnv)
  (hcond : CompileWellTypedCondition (.unaryApp op expr ty) Γ εnv) :
  CompileWellTyped (.unaryApp op expr ty) εnv
```

`Cedar.Thm.compile_binaryApp_wf_types` (theorem, [line 643](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/WellTyped.lean#L643))

> Similar to `compileApp₂_wf_types`, but for `compile`

```lean
theorem compile_binaryApp_wf_types
  {op : BinaryOp} {a : TypedExpr} {b : TypedExpr} {ty : CedarType}
  {t : Term} {tcomp_a : Term} {tcomp_b : Term}
  {εnv : SymEnv}
  (hwf_ent : εnv.entities.WellFormed)
  (hok_a : compile a.toExpr εnv = Except.ok tcomp_a)
  (hok_b : compile b.toExpr εnv = Except.ok tcomp_b)
  (hwf_get_comp_a : Term.WellFormed εnv.entities (Factory.option.get tcomp_a))
  (hwf_get_comp_b : Term.WellFormed εnv.entities (Factory.option.get tcomp_b))
  (hok : compile (TypedExpr.toExpr (.binaryApp op a b ty)) εnv = .ok t) :
  match op with
    | .add | .sub | .mul => t.typeOf = .option (.bitvec 64)
    | .getTag            =>
      ∃ ety τs,
        (Factory.option.get tcomp_a).typeOf = .entity ety ∧
        εnv.entities.tags ety = some (some τs) ∧
        t.typeOf = τs.vals.outType.option
    | _                  => t.typeOf = .option .bool
```

`Cedar.Thm.compile_ok_implies_compile_well_typed_binaryApp` (theorem, [line 703](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/WellTyped.lean#L703))

> Since we have the nice lemma `compileApp₂_wf_types`,
> it's enough to prove that `compile` of a `binaryApp` succeeds.

```lean
theorem compile_ok_implies_compile_well_typed_binaryApp
  {op : BinaryOp} {a : TypedExpr} {b : TypedExpr} {ty : CedarType}
  {Γ : TypeEnv} {εnv : SymEnv}
  (iha : CompileWellTypedAndWF a εnv)
  (ihb : CompileWellTypedAndWF b εnv)
  (hcond : CompileWellTypedCondition (.binaryApp op a b ty) Γ εnv)
  (hok : ∃ t : Term,
    compile (TypedExpr.toExpr (.binaryApp op a b ty)) εnv = .ok t) :
  CompileWellTyped (.binaryApp op a b ty) εnv
```

`Cedar.Thm.compile_well_typed_binaryApp` (theorem, [line 745](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/WellTyped.lean#L745))

```lean
theorem compile_well_typed_binaryApp
  {op : BinaryOp} {a : TypedExpr} {b : TypedExpr} {ty : CedarType}
  {Γ : TypeEnv} {εnv : SymEnv}
  (iha : CompileWellTypedAndWF a εnv)
  (ihb : CompileWellTypedAndWF b εnv)
  (hcond : CompileWellTypedCondition (.binaryApp op a b ty) Γ εnv) :
  CompileWellTyped (.binaryApp op a b ty) εnv
```

`Cedar.Thm.compile_well_typed_getAttr` (theorem, [line 822](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/WellTyped.lean#L822))

```lean
theorem compile_well_typed_getAttr
  {expr : TypedExpr} {attr : Attr} {ty : CedarType}
  {Γ : TypeEnv} {εnv : SymEnv}
  (ihexpr : CompileWellTypedAndWF expr εnv)
  (hcond : CompileWellTypedCondition (.getAttr expr attr ty) Γ εnv) :
  CompileWellTyped (.getAttr expr attr ty) εnv
```

`Cedar.Thm.compile_well_typed_hasAttr` (theorem, [line 956](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/WellTyped.lean#L956))

```lean
theorem compile_well_typed_hasAttr
  {expr : TypedExpr} {attr : Attr} {ty : CedarType}
  {Γ : TypeEnv} {εnv : SymEnv}
  (ihexpr : CompileWellTypedAndWF expr εnv)
  (hcond : CompileWellTypedCondition (.hasAttr expr attr ty) Γ εnv) :
  CompileWellTyped (.hasAttr expr attr ty) εnv
```

`Cedar.Thm.compileHasAttr_always_ok` (theorem, [line 1074](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/WellTyped.lean#L1074))

```lean
public theorem compileHasAttr_always_ok {t₁ : Term} {a : Attr} {εs : SymEntities}
  (hwε : εs.WellFormed)
  (hw₁ : t₁.WellFormed εs)
  (hty₁ : (∃ ety, t₁.typeOf = .entity ety) ∨ (∃ rty, t₁.typeOf = .record rty))
  : ∃ t, compileHasAttr t₁ a εs = .ok t
```

`Cedar.Thm.compileGetAttr_always_ok` (theorem, [line 1103](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/WellTyped.lean#L1103))

```lean
public theorem compileGetAttr_always_ok {t₁ : Term} {a : Attr} {εs : SymEntities}
  (hwε : εs.WellFormed)
  (hw₁ : t₁.WellFormed εs)
  (hty₁ : (∃ ety, t₁.typeOf = .entity ety) ∨ (∃ rty, t₁.typeOf = .record rty))
  (hhas : compileHasAttr t₁ a εs ≠ .ok (Term.some (Term.prim (.bool false))))
  : ∃ t, compileGetAttr t₁ a εs = .ok t
```

`Cedar.Thm.compileExtHasAttrRec_ne_error` (theorem, [line 1429](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/WellTyped.lean#L1429))

```lean
public theorem compileExtHasAttrRec_ne_error {t₁ : Term} {attrs : List Attr} {εs : SymEntities} {e : SymCC.Error}
  {Γ : TypeEnv} {cty : CedarType}
  (hwε : εs.WellFormed)
  (hw₁ : t₁.WellFormed εs)
  (hty₁ : (∃ ety, t₁.typeOf = .option (.entity ety)) ∨ (∃ rty, t₁.typeOf = .option (.record rty)))
  (hchain : ExtHasAttrChainValid Γ.ets cty attrs)
  (hεs : εs = (SymEnv.ofEnv Γ).entities)
  (hty_cty : t₁.typeOf = .option (TermType.ofType cty))
  : compileExtHasAttrRec t₁ attrs εs ≠ .error e
```

`Cedar.Thm.compile_well_typed_extHasAttr` (theorem, [line 1504](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/WellTyped.lean#L1504))

```lean
theorem compile_well_typed_extHasAttr
  {expr : TypedExpr} {attr : Attr} {attrs : List Attr} {ty : CedarType}
  {Γ : TypeEnv} {εnv : SymEnv}
  (ihexpr : CompileWellTypedAndWF expr εnv)
  (hcond : CompileWellTypedCondition (.extHasAttr expr attr attrs ty) Γ εnv) :
  CompileWellTyped (.extHasAttr expr attr attrs ty) εnv
```

`Cedar.Thm.compile_well_typed_set` (theorem, [line 1557](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/WellTyped.lean#L1557))

```lean
theorem compile_well_typed_set
  {xs : List TypedExpr} {ty : CedarType}
  {Γ : TypeEnv} {εnv : SymEnv}
  (ihxs : ∀ x, x ∈ xs → CompileWellTypedAndWF x εnv)
  (hcond : CompileWellTypedCondition (.set xs ty) Γ εnv) :
  CompileWellTyped (.set xs ty) εnv
```

`Cedar.Thm.compile_well_typed_record` (theorem, [line 1676](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/WellTyped.lean#L1676))

```lean
theorem compile_well_typed_record
  {xs : List (Attr × TypedExpr)} {ty : CedarType}
  {Γ : TypeEnv} {εnv : SymEnv}
  (ihxs : ∀ a x, (a, x) ∈ xs → CompileWellTypedAndWF x εnv)
  (hcond : CompileWellTypedCondition (.record xs ty) Γ εnv) :
  CompileWellTyped (.record xs ty) εnv
```

`Cedar.Thm.compile_well_typed_call` (theorem, [line 1797](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/WellTyped.lean#L1797))

```lean
theorem compile_well_typed_call
  {xfn : ExtFun} {xs : List TypedExpr} {ty : CedarType}
  {Γ : TypeEnv} {εnv : SymEnv}
  (ihxs : ∀ x, x ∈ xs → CompileWellTypedAndWF x εnv)
  (hcond : CompileWellTypedCondition (.call xfn xs ty) Γ εnv) :
  CompileWellTyped (.call xfn xs ty) εnv
```

`Cedar.Thm.compile_well_typed_on_wf_expr` (theorem, [line 2006](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/WellTyped.lean#L2006))

> Compiling a well-typed expression should produce a term of the corresponding `TermType`,
> assuming that the expression is well-formed in the symbolic environment.

```lean
theorem compile_well_typed_on_wf_expr {Γ : TypeEnv} {εnv : SymEnv} {tx : TypedExpr} :
  CompileWellTypedCondition tx Γ εnv →
  CompileWellTyped tx εnv
```

## Depends on

- [ExtHasAttrRec](exthasattrrec.md)
- [Well-formedness and interpretations](../data/basic.md)
- [Expr/Definition](../../welltyped/expr-2/definition.md)

## Proof depends on

- [Compiler/WF](wf.md)
- [ofEnv](../env/ofenv.md)
- [ofType](../term/oftype.md)

## Sources

- [Cedar/Thm/SymCC/Compiler/WellTyped.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/WellTyped.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Compiler.WellTyped.json)
