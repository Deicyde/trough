---
catalog: module
lean: Cedar.Thm.CompileIfSym, Cedar.Thm.compile_ite_ok_implies, Cedar.Thm.CompileAndSym, Cedar.Thm.compile_and_ok_implies, Cedar.Thm.CompileOrSym, Cedar.Thm.compile_or_ok_implies, Cedar.Thm.compileAttrsOf_ok_implies, Cedar.Thm.RecordHasAttr, Cedar.Thm.compileHasAttr_ok_implies, Cedar.Thm.compile_hasAttr_ok_implies, Cedar.Thm.RecordGetAttr, Cedar.Thm.compileGetAttr_ok_implies, Cedar.Thm.compile_getAttr_ok_implies, Cedar.Thm.compileApp₁_ok_implies, Cedar.Thm.compile_unaryApp_ok_implies, Cedar.Thm.compileApp₂_less_ok_implies, Cedar.Thm.compileApp₂_lessEq_ok_implies, Cedar.Thm.compileApp₂_add_ok_implies, Cedar.Thm.compileApp₂_sub_ok_implies, Cedar.Thm.compileApp₂_mul_ok_implies, Cedar.Thm.reducibleEq_ok_false_implies, Cedar.Thm.reducibleEq_ok_true_implies, Cedar.Thm.compileApp₂_eq_ok_implies, Cedar.Thm.compileApp₂_contains_ok_implies, Cedar.Thm.compileApp₂_containsAll_ok_implies, Cedar.Thm.compileApp₂_containsAny_ok_implies, Cedar.Thm.compileHasTag_ok_implies, Cedar.Thm.compileApp₂_hasTag_ok_implies, Cedar.Thm.compileGetTag_ok_implies, Cedar.Thm.compileApp₂_getTag_ok_implies, Cedar.Thm.compileInₑ.isEq, Cedar.Thm.compileInₑ.isEq_def, Cedar.Thm.compileInₑ.isIn, Cedar.Thm.compileInₑ.isIn_def, Cedar.Thm.compileInₑ_def, Cedar.Thm.compileInₛ.isIn₁, Cedar.Thm.compileInₛ.isIn₁_def, Cedar.Thm.compileInₛ.isIn₂, Cedar.Thm.compileInₛ.isIn₂_def, Cedar.Thm.compileInₛ_def, Cedar.Thm.compileApp₂_mem_ok_implies, Cedar.Thm.compile_binaryApp_ok_implies, Cedar.Thm.compileSet_ok_implies, Cedar.Thm.compile_set_ok_implies, Cedar.Thm.compile_record_ok_implies, Cedar.Thm.compileCall_decimal_ok_implies, Cedar.Thm.compileCall_decimal_lessThan_ok_implies, Cedar.Thm.compileCall_decimal_lessThanOrEqual_ok_implies, Cedar.Thm.compileCall_decimal_greaterThan_ok_implies, Cedar.Thm.compileCall_decimal_greaterThanOrEqual_ok_implies, Cedar.Thm.compileCall_ipAddr_ok_implies, Cedar.Thm.compileCall_ipAddr_isIpv4_ok_implies, Cedar.Thm.compileCall_ipAddr_isIpv6_ok_implies, Cedar.Thm.compileCall_ipAddr_isLoopback_ok_implies, Cedar.Thm.compileCall_ipAddr_isMulticast_ok_implies, Cedar.Thm.compileCall_ipAddr_isInRange_ok_implies, Cedar.Thm.compileCall_datetime_ok_implies, Cedar.Thm.compileCall_datetime_offset_ok_implies, Cedar.Thm.compileCall_datetime_durationSince_ok_implies, Cedar.Thm.compileCall_datetime_toDate_ok_implies, Cedar.Thm.compileCall_datetime_toTime_ok_implies, Cedar.Thm.compileCall_duration_ok_implies, Cedar.Thm.compileCall_duration_toMilliseconds_ok_implies, Cedar.Thm.compileCall_duration_toSeconds_ok_implies, Cedar.Thm.compileCall_duration_toMinutes_ok_implies, Cedar.Thm.compileCall_duration_toHours_ok_implies, Cedar.Thm.compileCall_duration_toDays_ok_implies, Cedar.Thm.compile_call_ok_implies
statement: formalized
proof: formalized
---

# Invert

`Cedar.Thm.SymCC.Compiler.Invert`, in [Cedar/Thm/SymCC/Compiler/Invert.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean).

> This file proves inversion lemmas for `compile`.
> -

`Cedar.Thm.CompileIfSym` (definition, [line 35](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L35))

```lean
def CompileIfSym (t t₁ : Term) (r₂ r₃ : SymCC.Result Term) : Prop
```

`Cedar.Thm.compile_ite_ok_implies` (theorem, [line 43](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L43))

```lean
theorem compile_ite_ok_implies {x₁ x₂ x₃ : Expr} {εnv : SymEnv} {t : Term}
  (h₁ : compile (.ite x₁ x₂ x₃) εnv = .ok t) :
  ∃ t₁,
    (compile x₁ εnv) = .ok t₁ ∧
    match t₁ with
     | .some (.prim (.bool true))  => t = compile x₂ εnv
     | .some (.prim (.bool false)) => t = compile x₃ εnv
     | t₁ => CompileIfSym t t₁ (compile x₂ εnv) (compile x₃ εnv)
```

`Cedar.Thm.CompileAndSym` (definition, [line 73](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L73))

```lean
def CompileAndSym (t t₁ : Term) (r₂ : SymCC.Result Term): Prop
```

`Cedar.Thm.compile_and_ok_implies` (theorem, [line 80](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L80))

```lean
theorem compile_and_ok_implies {x₁ x₂ : Expr} {εnv : SymEnv} {t : Term}
  (h₁ : compile (.and x₁ x₂) εnv = .ok t) :
  ∃ t₁,
    (compile x₁ εnv) = .ok t₁ ∧
    match t₁ with
     | .some (.prim (.bool false)) => t = t₁
     | _ => CompileAndSym t t₁ (compile x₂ εnv)
```

`Cedar.Thm.CompileOrSym` (definition, [line 108](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L108))

```lean
def CompileOrSym (t t₁ : Term) (r₂ : SymCC.Result Term): Prop
```

`Cedar.Thm.compile_or_ok_implies` (theorem, [line 115](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L115))

```lean
theorem compile_or_ok_implies {x₁ x₂ : Expr} {εnv : SymEnv} {t : Term}
  (h₁ : compile (.or x₁ x₂) εnv = .ok t) :
  ∃ t₁,
    (compile x₁ εnv) = .ok t₁ ∧
    match t₁ with
    | .some (.prim (.bool true)) => t = t₁
    | _ => CompileOrSym t t₁ (compile x₂ εnv)
```

`Cedar.Thm.compileAttrsOf_ok_implies` (theorem, [line 144](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L144))

```lean
theorem compileAttrsOf_ok_implies {t t₁ : Term} {εs : SymEntities}
  (h₁ : compileAttrsOf t₁ εs = .ok t) :
  (∃ rty, t₁.typeOf = .record rty ∧ t = t₁) ∨
  (∃ ety fₐ, t₁.typeOf = .entity ety ∧ εs.attrs ety = .some fₐ ∧ t = app fₐ t₁)
```

`Cedar.Thm.RecordHasAttr` (definition, [line 164](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L164))

```lean
def RecordHasAttr (t t₁ : Term) (rty : Map Attr TermType) (a : Attr) : Prop
```

`Cedar.Thm.compileHasAttr_ok_implies` (theorem, [line 171](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L171))

```lean
theorem compileHasAttr_ok_implies {t t₁ : Term} {a : Attr} {εs : SymEntities}
  (h₁ : compileHasAttr t₁ a εs = .ok t) :
  ∃ t₂ rty,
    compileAttrsOf t₁ εs = .ok t₂ ∧
    RecordHasAttr t t₂ rty a
```

`Cedar.Thm.compile_hasAttr_ok_implies` (theorem, [line 189](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L189))

```lean
theorem compile_hasAttr_ok_implies {a : Attr} {x₁ : Expr} {εnv : SymEnv} {t : Term}
  (h₁ : compile (.hasAttr x₁ a) εnv = .ok t) :
  ∃ t₁ t₂,
    (compile x₁ εnv) = .ok t₁ ∧
    (compileHasAttr (option.get t₁) a εnv.entities) = .ok t₂ ∧
    t = ifSome t₁ t₂
```

`Cedar.Thm.RecordGetAttr` (definition, [line 205](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L205))

```lean
def RecordGetAttr (t t₁ : Term) (rty : Map Attr TermType) (a : Attr) : Prop
```

`Cedar.Thm.compileGetAttr_ok_implies` (theorem, [line 212](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L212))

```lean
theorem compileGetAttr_ok_implies {t t₁ : Term} {a : Attr} {εs : SymEntities}
  (h₁ : compileGetAttr t₁ a εs = .ok t) :
  ∃ t₂ rty,
    compileAttrsOf t₁ εs = .ok t₂ ∧
    RecordGetAttr t t₂ rty a
```

`Cedar.Thm.compile_getAttr_ok_implies` (theorem, [line 237](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L237))

```lean
theorem compile_getAttr_ok_implies {a : Attr} {x₁ : Expr} {εnv : SymEnv} {t : Term}
  (h₁ : compile (.getAttr x₁ a) εnv = .ok t) :
  ∃ t₁ t₂,
    (compile x₁ εnv) = .ok t₁ ∧
    (compileGetAttr (option.get t₁) a εnv.entities) = .ok t₂ ∧
    t = ifSome t₁ t₂
```

`Cedar.Thm.compileApp₁_ok_implies` (theorem, [line 253](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L253))

```lean
theorem compileApp₁_ok_implies {op₁ : UnaryOp} {t t₁ : Term}
  (h₁ : compileApp₁ op₁ t₁ = .ok t) :
  match op₁ with
  | .not     => t₁.typeOf = .bool ∧ t = Term.some (not t₁)
  | .neg     => t₁.typeOf = .bitvec 64 ∧ t = ifFalse (bvnego t₁) (bvneg t₁)
  | .like p  => t₁.typeOf = .string ∧ t = Term.some (string.like t₁ p)
  | .is ety₁ => ∃ ety₂, t₁.typeOf = .entity ety₂ ∧ t = Term.some (ety₁ = ety₂ : Bool)
  | .isEmpty => (∃ ty, t₁.typeOf = .set ty) ∧ t = Term.some (set.isEmpty t₁)
```

`Cedar.Thm.compile_unaryApp_ok_implies` (theorem, [line 280](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L280))

```lean
theorem compile_unaryApp_ok_implies {op₁ : UnaryOp} {x₁ : Expr} {εnv : SymEnv} {t : Term}
  (h₁ : compile (.unaryApp op₁ x₁) εnv = .ok t) :
  ∃ t₁ t₂,
    (compile x₁ εnv) = .ok t₁ ∧
    (compileApp₁ op₁ (option.get t₁)) = .ok t₂ ∧
    t = ifSome t₁ t₂
```

`Cedar.Thm.compileApp₂_less_ok_implies` (theorem, [line 308](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L308))

```lean
theorem compileApp₂_less_ok_implies {t t₁ t₂ : Term} {εs : SymEntities} :
  compileApp₂ .less t₁ t₂ εs = .ok t →
  (
    (t₁.typeOf = .bitvec 64 ∧ t₂.typeOf = .bitvec 64 ∧ t = Term.some (bvslt t₁ t₂)) ∨
    (t₁.typeOf = .ext .duration ∧ t₂.typeOf = .ext .duration ∧ t = Term.some (bvslt (ext.duration.val t₁) (ext.duration.val t₂))) ∨
    (t₁.typeOf = .ext .datetime ∧ t₂.typeOf = .ext .datetime ∧ t = Term.some (bvslt (ext.datetime.val t₁) (ext.datetime.val t₂)))
  )
```

`Cedar.Thm.compileApp₂_lessEq_ok_implies` (theorem, [line 317](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L317))

```lean
theorem compileApp₂_lessEq_ok_implies {t t₁ t₂ : Term} {εs : SymEntities} :
  compileApp₂ .lessEq t₁ t₂ εs = .ok t →
  (
    (t₁.typeOf = .bitvec 64 ∧ t₂.typeOf = .bitvec 64 ∧ t = Term.some (bvsle t₁ t₂)) ∨
    (t₁.typeOf = .ext .duration ∧ t₂.typeOf = .ext .duration ∧ t = Term.some (bvsle (ext.duration.val t₁) (ext.duration.val t₂))) ∨
    (t₁.typeOf = .ext .datetime ∧ t₂.typeOf = .ext .datetime ∧ t = Term.some (bvsle (ext.datetime.val t₁) (ext.datetime.val t₂)))
  )
```

`Cedar.Thm.compileApp₂_add_ok_implies` (theorem, [line 326](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L326))

```lean
theorem compileApp₂_add_ok_implies {t t₁ t₂ : Term} {εs : SymEntities} :
  compileApp₂ .add t₁ t₂ εs = .ok t →
  t₁.typeOf = .bitvec 64 ∧ t₂.typeOf = .bitvec 64 ∧ t = ifFalse (bvsaddo t₁ t₂) (bvadd t₁ t₂)
```

`Cedar.Thm.compileApp₂_sub_ok_implies` (theorem, [line 331](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L331))

```lean
theorem compileApp₂_sub_ok_implies {t t₁ t₂ : Term} {εs : SymEntities} :
  compileApp₂ .sub t₁ t₂ εs = .ok t →
  t₁.typeOf = .bitvec 64 ∧ t₂.typeOf = .bitvec 64 ∧ t = ifFalse (bvssubo t₁ t₂) (bvsub t₁ t₂)
```

`Cedar.Thm.compileApp₂_mul_ok_implies` (theorem, [line 336](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L336))

```lean
theorem compileApp₂_mul_ok_implies {t t₁ t₂ : Term} {εs : SymEntities} :
  compileApp₂ .mul t₁ t₂ εs = .ok t →
  t₁.typeOf = .bitvec 64 ∧ t₂.typeOf = .bitvec 64 ∧ t = ifFalse (bvsmulo t₁ t₂) (bvmul t₁ t₂)
```

`Cedar.Thm.reducibleEq_ok_false_implies` (theorem, [line 341](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L341))

```lean
theorem reducibleEq_ok_false_implies {ty₁ ty₂ : TermType} :
  reducibleEq ty₁ ty₂ = Except.ok false →
  (¬ ty₁ = ty₂ ∧ ty₁.isPrimType ∧ ty₂.isPrimType)
```

`Cedar.Thm.reducibleEq_ok_true_implies` (theorem, [line 353](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L353))

```lean
theorem reducibleEq_ok_true_implies {ty₁ ty₂ : TermType} :
  reducibleEq ty₁ ty₂ = .ok true → ty₁ = ty₂
```

`Cedar.Thm.compileApp₂_eq_ok_implies` (theorem, [line 362](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L362))

```lean
theorem compileApp₂_eq_ok_implies {t t₁ t₂ : Term} {εs : SymEntities} :
  compileApp₂ .eq t₁ t₂ εs = .ok t →
  ((reducibleEq t₁.typeOf t₂.typeOf = .ok true ∧ t = Term.some (eq t₁ t₂)) ∨
   (reducibleEq t₁.typeOf t₂.typeOf = .ok false ∧ t = Term.some false))
```

`Cedar.Thm.compileApp₂_contains_ok_implies` (theorem, [line 377](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L377))

```lean
theorem compileApp₂_contains_ok_implies {t t₁ t₂ : Term} {εs : SymEntities} :
  compileApp₂ .contains t₁ t₂ εs = .ok t →
  t₁.typeOf = .set t₂.typeOf ∧ t = Term.some (set.member t₂ t₁)
```

`Cedar.Thm.compileApp₂_containsAll_ok_implies` (theorem, [line 390](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L390))

```lean
theorem compileApp₂_containsAll_ok_implies {t t₁ t₂ : Term} {εs : SymEntities} :
  compileApp₂ .containsAll t₁ t₂ εs = .ok t →
  ∃ ty, t₁.typeOf = .set ty ∧ t₂.typeOf = .set ty ∧ t = Term.some (set.subset t₂ t₁)
```

`Cedar.Thm.compileApp₂_containsAny_ok_implies` (theorem, [line 404](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L404))

```lean
theorem compileApp₂_containsAny_ok_implies {t t₁ t₂ : Term} {εs : SymEntities} :
  compileApp₂ .containsAny t₁ t₂ εs = .ok t →
  ∃ ty, t₁.typeOf = .set ty ∧ t₂.typeOf = .set ty ∧ t = Term.some (set.intersects t₁ t₂)
```

`Cedar.Thm.compileHasTag_ok_implies` (theorem, [line 418](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L418))

```lean
theorem compileHasTag_ok_implies {t t₁ t₂ : Term} {tags : Option (Option SymTags)} :
  compileHasTag t₁ t₂ tags = .ok t →
  (tags = .some .none ∧ t = Term.some false) ∨
  (∃ τs, tags = .some (.some τs) ∧ t = Term.some (τs.hasTag t₁ t₂))
```

`Cedar.Thm.compileApp₂_hasTag_ok_implies` (theorem, [line 429](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L429))

```lean
theorem compileApp₂_hasTag_ok_implies {t t₁ t₂ : Term} {εs : SymEntities} :
  compileApp₂ .hasTag t₁ t₂ εs = .ok t →
  ∃ ety, t₁.typeOf = .entity ety ∧ t₂.typeOf = .string ∧ compileHasTag t₁ t₂ (εs.tags ety) = .ok t
```

`Cedar.Thm.compileGetTag_ok_implies` (theorem, [line 438](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L438))

```lean
theorem compileGetTag_ok_implies {t t₁ t₂ : Term} {tags : Option (Option SymTags)} :
  compileGetTag t₁ t₂ tags = .ok t →
  ∃ τs, tags = .some (.some τs) ∧ t = τs.getTag t₁ t₂
```

`Cedar.Thm.compileApp₂_getTag_ok_implies` (theorem, [line 447](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L447))

```lean
theorem compileApp₂_getTag_ok_implies {t t₁ t₂ : Term} {εs : SymEntities} :
  compileApp₂ .getTag t₁ t₂ εs = .ok t →
  ∃ ety, t₁.typeOf = .entity ety ∧ t₂.typeOf = .string ∧ compileGetTag t₁ t₂ (εs.tags ety) = .ok t
```

`Cedar.Thm.compileInₑ.isEq` (definition, [line 456](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L456))

```lean
def compileInₑ.isEq (t₁ t₂ : Term) : Term
```

`Cedar.Thm.compileInₑ.isEq_def` (theorem, [line 459](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L459))

```lean
theorem compileInₑ.isEq_def :
  compileInₑ.isEq t₁ t₂ = SymCC.compileInₑ.isEq t₁ t₂
```

`Cedar.Thm.compileInₑ.isIn` (definition, [line 464](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L464))

```lean
def compileInₑ.isIn (t₁ t₂ : Term) (ancs? : Option UnaryFunction) : Term
```

`Cedar.Thm.compileInₑ.isIn_def` (theorem, [line 469](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L469))

```lean
theorem compileInₑ.isIn_def :
  compileInₑ.isIn t₁ t₂ ancs? = SymCC.compileInₑ.isIn t₁ t₂ ancs?
```

`Cedar.Thm.compileInₑ_def` (theorem, [line 474](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L474))

```lean
theorem compileInₑ_def  {t₁ t₂ : Term} {ancs? : Option UnaryFunction} :
  compileInₑ t₁ t₂ ancs? = Factory.or (compileInₑ.isEq t₁ t₂) (compileInₑ.isIn t₁ t₂ ancs?)
```

`Cedar.Thm.compileInₛ.isIn₁` (definition, [line 480](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L480))

```lean
def compileInₛ.isIn₁ (t ts : Term) : Term
```

`Cedar.Thm.compileInₛ.isIn₁_def` (theorem, [line 483](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L483))

```lean
theorem compileInₛ.isIn₁_def :
  compileInₛ.isIn₁ t ts = SymCC.compileInₛ.isIn₁ t ts
```

`Cedar.Thm.compileInₛ.isIn₂` (definition, [line 488](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L488))

```lean
def compileInₛ.isIn₂ (t ts : Term) (ancs? : Option UnaryFunction) : Term
```

`Cedar.Thm.compileInₛ.isIn₂_def` (theorem, [line 493](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L493))

```lean
theorem compileInₛ.isIn₂_def :
  compileInₛ.isIn₂ t ts ancs? = SymCC.compileInₛ.isIn₂ t ts ancs?
```

`Cedar.Thm.compileInₛ_def` (theorem, [line 498](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L498))

```lean
theorem compileInₛ_def  {t ts : Term} {ancs? : Option UnaryFunction} :
  compileInₛ t ts ancs? = Factory.or (compileInₛ.isIn₁ t ts) (compileInₛ.isIn₂ t ts ancs?)
```

`Cedar.Thm.compileApp₂_mem_ok_implies` (theorem, [line 504](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L504))

```lean
theorem compileApp₂_mem_ok_implies {t t₁ t₂ : Term} {εs : SymEntities} :
  compileApp₂ .mem t₁ t₂ εs = .ok t →
  ∃ ety₁ ety₂, t₁.typeOf = .entity ety₁ ∧
    ((t₂.typeOf = .entity ety₂ ∧ t = Term.some (compileInₑ t₁ t₂ (εs.ancestorsOfType ety₁ ety₂))) ∨
     (t₂.typeOf = .set (.entity ety₂) ∧ t = Term.some (compileInₛ t₁ t₂ (εs.ancestorsOfType ety₁ ety₂))))
```

`Cedar.Thm.compile_binaryApp_ok_implies` (theorem, [line 520](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L520))

```lean
theorem compile_binaryApp_ok_implies {op₂ : BinaryOp} {x₁ x₂ : Expr} {εnv : SymEnv} {t : Term}
  (hok : compile (.binaryApp op₂ x₁ x₂) εnv = .ok t) :
  ∃ t₁ t₂ t₃,
    (compile x₁ εnv) = .ok t₁ ∧
    (compile x₂ εnv) = .ok t₂ ∧
    (compileApp₂ op₂ (option.get t₁) (option.get t₂) εnv.entities) = .ok t₃ ∧
    t = ifSome t₁ (ifSome t₂ t₃)
```

`Cedar.Thm.compileSet_ok_implies` (theorem, [line 538](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L538))

```lean
theorem compileSet_ok_implies {ts : List Term} {t : Term}
  (hok : compileSet ts = .ok t) :
  ∃ ty hd tl,
    ts = hd :: tl ∧
    (∀ t ∈ ts, t.typeOf = .option ty) ∧
    t = ifAllSome ts (Term.some (setOf (ts.map option.get) ty))
```

`Cedar.Thm.compile_set_ok_implies` (theorem, [line 557](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L557))

```lean
theorem compile_set_ok_implies {xs : List Expr} {εnv : SymEnv} {t : Term}
  (hok : compile (.set xs) εnv = .ok t) :
  ∃ ts,
    List.Forall₂ (λ x t => (compile x εnv) = .ok t) xs ts ∧
    compileSet ts = .ok t
```

`Cedar.Thm.compile_record_ok_implies` (theorem, [line 570](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L570))

```lean
theorem compile_record_ok_implies {axs : List (Attr × Expr)} {εnv : SymEnv} {t : Term}
  (hok : compile (.record axs) εnv = .ok t) :
  ∃ ats,
    List.Forall₂ (λ px pt => px.fst = pt.fst ∧ compile px.snd εnv = .ok pt.snd) axs ats ∧
    t = compileRecord ats
```

`Cedar.Thm.compileCall_decimal_ok_implies` (theorem, [line 638](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L638))

```lean
theorem compileCall_decimal_ok_implies {ts : List Term} {t : Term} :
  compileCall ExtFun.decimal ts = .ok t →
  ∃ (s : String) (d : Ext.Decimal),
    ts = [.some (.prim (.string s))] ∧
    Ext.Decimal.decimal s = .some d ∧
    t = Term.some (.prim (.ext (.decimal d)))
```

`Cedar.Thm.compileCall_decimal_lessThan_ok_implies` (theorem, [line 646](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L646))

```lean
theorem compileCall_decimal_lessThan_ok_implies {ts : List Term} {t : Term} :
  compileCall ExtFun.lessThan ts = .ok t →
  ∃ t₁ t₂,
    ts = [t₁, t₂] ∧
    t₁.typeOf = .option (.ext .decimal) ∧
    t₂.typeOf = .option (.ext .decimal) ∧
    t = ifSome t₁ (ifSome t₂ (Term.some (Decimal.lessThan (option.get t₁) (option.get t₂))))
```

`Cedar.Thm.compileCall_decimal_lessThanOrEqual_ok_implies` (theorem, [line 655](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L655))

```lean
theorem compileCall_decimal_lessThanOrEqual_ok_implies {ts : List Term} {t : Term} :
  compileCall ExtFun.lessThanOrEqual ts = .ok t →
  ∃ t₁ t₂,
    ts = [t₁, t₂] ∧
    t₁.typeOf = .option (.ext .decimal) ∧
    t₂.typeOf = .option (.ext .decimal) ∧
    t = ifSome t₁ (ifSome t₂ (Term.some (Decimal.lessThanOrEqual (option.get t₁) (option.get t₂))))
```

`Cedar.Thm.compileCall_decimal_greaterThan_ok_implies` (theorem, [line 664](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L664))

```lean
theorem compileCall_decimal_greaterThan_ok_implies {ts : List Term} {t : Term} :
  compileCall ExtFun.greaterThan ts = .ok t →
  ∃ t₁ t₂,
    ts = [t₁, t₂] ∧
    t₁.typeOf = .option (.ext .decimal) ∧
    t₂.typeOf = .option (.ext .decimal) ∧
    t = ifSome t₁ (ifSome t₂ (Term.some (Decimal.greaterThan (option.get t₁) (option.get t₂))))
```

`Cedar.Thm.compileCall_decimal_greaterThanOrEqual_ok_implies` (theorem, [line 673](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L673))

```lean
theorem compileCall_decimal_greaterThanOrEqual_ok_implies {ts : List Term} {t : Term} :
  compileCall ExtFun.greaterThanOrEqual ts = .ok t →
  ∃ t₁ t₂,
    ts = [t₁, t₂] ∧
    t₁.typeOf = .option (.ext .decimal) ∧
    t₂.typeOf = .option (.ext .decimal) ∧
    t = ifSome t₁ (ifSome t₂ (Term.some (Decimal.greaterThanOrEqual (option.get t₁) (option.get t₂))))
```

`Cedar.Thm.compileCall_ipAddr_ok_implies` (theorem, [line 682](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L682))

```lean
theorem compileCall_ipAddr_ok_implies {ts : List Term} {t : Term} :
  compileCall ExtFun.ip ts = .ok t →
  ∃ (s : String) (ip : Ext.IPAddr.IPNet),
    ts = [.some (.prim (.string s))] ∧
    Ext.IPAddr.ip s = .some ip ∧
    t = Term.some (.prim (.ext (.ipaddr ip)))
```

`Cedar.Thm.compileCall_ipAddr_isIpv4_ok_implies` (theorem, [line 690](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L690))

```lean
theorem compileCall_ipAddr_isIpv4_ok_implies {ts : List Term} {t : Term} :
  compileCall ExtFun.isIpv4 ts = .ok t →
  ∃ t₁,
    ts = [t₁] ∧
    t₁.typeOf = .option (.ext .ipAddr) ∧
    t = ifSome t₁ (Term.some (IPAddr.isIpv4 (option.get t₁)))
```

`Cedar.Thm.compileCall_ipAddr_isIpv6_ok_implies` (theorem, [line 698](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L698))

```lean
theorem compileCall_ipAddr_isIpv6_ok_implies {ts : List Term} {t : Term} :
  compileCall ExtFun.isIpv6 ts = .ok t →
  ∃ t₁,
    ts = [t₁] ∧
    t₁.typeOf = .option (.ext .ipAddr) ∧
    t = ifSome t₁ (Term.some (IPAddr.isIpv6 (option.get t₁)))
```

`Cedar.Thm.compileCall_ipAddr_isLoopback_ok_implies` (theorem, [line 706](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L706))

```lean
theorem compileCall_ipAddr_isLoopback_ok_implies {ts : List Term} {t : Term} :
  compileCall ExtFun.isLoopback ts = .ok t →
  ∃ t₁,
    ts = [t₁] ∧
    t₁.typeOf = .option (.ext .ipAddr) ∧
    t = ifSome t₁ (Term.some (IPAddr.isLoopback (option.get t₁)))
```

`Cedar.Thm.compileCall_ipAddr_isMulticast_ok_implies` (theorem, [line 714](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L714))

```lean
theorem compileCall_ipAddr_isMulticast_ok_implies {ts : List Term} {t : Term} :
  compileCall ExtFun.isMulticast ts = .ok t →
  ∃ t₁,
    ts = [t₁] ∧
    t₁.typeOf = .option (.ext .ipAddr) ∧
    t = ifSome t₁ (Term.some (IPAddr.isMulticast (option.get t₁)))
```

`Cedar.Thm.compileCall_ipAddr_isInRange_ok_implies` (theorem, [line 722](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L722))

```lean
theorem compileCall_ipAddr_isInRange_ok_implies {ts : List Term} {t : Term} :
  compileCall ExtFun.isInRange ts = .ok t →
  ∃ t₁ t₂ ts',
    ts = t₁ :: t₂ :: ts' ∧
    t₁.typeOf = .option (.ext .ipAddr) ∧
    (∀ tᵢ ∈ t₂ :: ts', tᵢ.typeOf = .option (.ext .ipAddr)) ∧
    t = ifSome t₁ ((t₂ :: ts').foldr (fun tᵢ acc => ifSome tᵢ acc)
          (Term.some (IPAddr.isInRangeV (option.get t₁) ((t₂ :: ts').map option.get))))
```

`Cedar.Thm.compileCall_datetime_ok_implies` (theorem, [line 741](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L741))

```lean
theorem compileCall_datetime_ok_implies {ts : List Term} {t : Term} :
  compileCall ExtFun.datetime ts = .ok t →
  ∃ (s : String) (d : Ext.Datetime),
    ts = [.some (.prim (.string s))] ∧
    Ext.Datetime.datetime s = .some d ∧
    t = Term.some (.prim (.ext (.datetime d)))
```

`Cedar.Thm.compileCall_datetime_offset_ok_implies` (theorem, [line 749](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L749))

```lean
theorem compileCall_datetime_offset_ok_implies {ts : List Term} {t : Term} :
  compileCall ExtFun.offset ts = .ok t →
  ∃ t₁ t₂,
    ts = [t₁, t₂] ∧
    t₁.typeOf = .option (.ext .datetime) ∧
    t₂.typeOf = .option (.ext .duration) ∧
    t = ifSome t₁ (ifSome t₂ (Datetime.offset (option.get t₁) (option.get t₂)))
```

`Cedar.Thm.compileCall_datetime_durationSince_ok_implies` (theorem, [line 758](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L758))

```lean
theorem compileCall_datetime_durationSince_ok_implies {ts : List Term} {t : Term} :
  compileCall ExtFun.durationSince ts = .ok t →
  ∃ t₁ t₂,
    ts = [t₁, t₂] ∧
    t₁.typeOf = .option (.ext .datetime) ∧
    t₂.typeOf = .option (.ext .datetime) ∧
    t = ifSome t₁ (ifSome t₂ (Datetime.durationSince (option.get t₁) (option.get t₂)))
```

`Cedar.Thm.compileCall_datetime_toDate_ok_implies` (theorem, [line 767](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L767))

```lean
theorem compileCall_datetime_toDate_ok_implies {ts : List Term} {t : Term} :
  compileCall ExtFun.toDate ts = .ok t →
  ∃ t₁,
    ts = [t₁] ∧
    t₁.typeOf = .option (.ext .datetime) ∧
    t = ifSome t₁ (Datetime.toDate (option.get t₁))
```

`Cedar.Thm.compileCall_datetime_toTime_ok_implies` (theorem, [line 775](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L775))

```lean
theorem compileCall_datetime_toTime_ok_implies {ts : List Term} {t : Term} :
  compileCall ExtFun.toTime ts = .ok t →
  ∃ t₁,
    ts = [t₁] ∧
    t₁.typeOf = .option (.ext .datetime) ∧
    t = ifSome t₁ (Term.some (Datetime.toTime (option.get t₁)))
```

`Cedar.Thm.compileCall_duration_ok_implies` (theorem, [line 783](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L783))

```lean
theorem compileCall_duration_ok_implies {ts : List Term} {t : Term} :
  compileCall ExtFun.duration ts = .ok t →
  ∃ (s : String) (d : Ext.Datetime.Duration),
    ts = [.some (.prim (.string s))] ∧
    Ext.Datetime.duration s = .some d ∧
    t = Term.some (.prim (.ext (.duration d)))
```

`Cedar.Thm.compileCall_duration_toMilliseconds_ok_implies` (theorem, [line 791](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L791))

```lean
theorem compileCall_duration_toMilliseconds_ok_implies {ts : List Term} {t : Term} :
  compileCall ExtFun.toMilliseconds ts = .ok t →
  ∃ t₁,
    ts = [t₁] ∧
    t₁.typeOf = .option (.ext .duration) ∧
    t = ifSome t₁ (Term.some (Duration.toMilliseconds (option.get t₁)))
```

`Cedar.Thm.compileCall_duration_toSeconds_ok_implies` (theorem, [line 799](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L799))

```lean
theorem compileCall_duration_toSeconds_ok_implies {ts : List Term} {t : Term} :
  compileCall ExtFun.toSeconds ts = .ok t →
  ∃ t₁,
    ts = [t₁] ∧
    t₁.typeOf = .option (.ext .duration) ∧
    t = ifSome t₁ (Term.some (Duration.toSeconds (option.get t₁)))
```

`Cedar.Thm.compileCall_duration_toMinutes_ok_implies` (theorem, [line 807](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L807))

```lean
theorem compileCall_duration_toMinutes_ok_implies {ts : List Term} {t : Term} :
  compileCall ExtFun.toMinutes ts = .ok t →
  ∃ t₁,
    ts = [t₁] ∧
    t₁.typeOf = .option (.ext .duration) ∧
    t = ifSome t₁ (Term.some (Duration.toMinutes (option.get t₁)))
```

`Cedar.Thm.compileCall_duration_toHours_ok_implies` (theorem, [line 815](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L815))

```lean
theorem compileCall_duration_toHours_ok_implies {ts : List Term} {t : Term} :
  compileCall ExtFun.toHours ts = .ok t →
  ∃ t₁,
    ts = [t₁] ∧
    t₁.typeOf = .option (.ext .duration) ∧
    t = ifSome t₁ (Term.some (Duration.toHours (option.get t₁)))
```

`Cedar.Thm.compileCall_duration_toDays_ok_implies` (theorem, [line 823](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L823))

```lean
theorem compileCall_duration_toDays_ok_implies {ts : List Term} {t : Term} :
  compileCall ExtFun.toDays ts = .ok t →
  ∃ t₁,
    ts = [t₁] ∧
    t₁.typeOf = .option (.ext .duration) ∧
    t = ifSome t₁ (Term.some (Duration.toDays (option.get t₁)))
```

`Cedar.Thm.compile_call_ok_implies` (theorem, [line 831](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean#L831))

```lean
theorem compile_call_ok_implies {f : ExtFun} {xs : List Expr} {εnv : SymEnv} {t : Term}
  (hok : compile (.call f xs) εnv = .ok t) :
  ∃ ts,
    List.Forall₂ (λ x t => (compile x εnv) = .ok t) xs ts ∧
    compileCall f ts = .ok t
```

## Depends on

- [Cedar/SymCC/Compiler](../../../symcc/part-01/compiler.md)

## Proof depends on

- [Properties of Lists](../../data/list/lemmas.md)

## Sources

- [Cedar/Thm/SymCC/Compiler/Invert.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Invert.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Compiler.Invert.json)
