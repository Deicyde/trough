---
catalog: module
lean: Cedar.Thm.compileAttrsOf_wf, Cedar.Thm.compileHasAttr_wf, Cedar.Thm.compileAnd_preserves_wf, Cedar.Thm.compileGetAttr_wf, Cedar.Thm.compileExtHasAttrRec_wf, Cedar.Thm.compileApp₁_wf_types, Cedar.Thm.compileApp₁_wf, Cedar.Thm.compileInₑ.isEq_wf, Cedar.Thm.compileInₑ.isIn_wf, Cedar.Thm.compileInₑ_wf, Cedar.Thm.compileInₛ.isIn₁_wf, Cedar.Thm.compileInₛ.isIn₂_wf, Cedar.Thm.compileInₛ_wf, Cedar.Thm.compileApp₂_wf_types, Cedar.Thm.compileApp₂_wf, Cedar.Thm.compileCall_wf_types, Cedar.Thm.compileCall_wf, Cedar.Thm.compile_wf, Cedar.Thm.compile_extHasAttr_typeOf, Cedar.Thm.compile_option_get_wf, Cedar.Thm.evaluate_wf, Cedar.Thm.wf_value_uid_implies_exists_entity_data
statement: formalized
proof: formalized
---

# Compiler/WF

`Cedar.Thm.SymCC.Compiler.WF`, in [Cedar/Thm/SymCC/Compiler/WF.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/WF.lean).

> This file proves that both `compile` and `evaluate` preserve well-formedness.
> -

`Cedar.Thm.compileAttrsOf_wf` (theorem, [line 194](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/WF.lean#L194))

```lean
public theorem compileAttrsOf_wf {t t₁: Term} {εs : SymEntities}
  (hwε : εs.WellFormed)
  (hw₁ : Term.WellFormed εs t₁)
  (hok : compileAttrsOf t₁ εs = Except.ok t)  :
  t.WellFormed εs ∧
  ∃ rty, t.typeOf = .record rty ∧
  (t₁.typeOf = .record rty ∨
   ∃ ety fₐ,
    t₁.typeOf = .entity ety ∧ εs.attrs ety = .some fₐ ∧
    fₐ.outType = .record rty)
```

`Cedar.Thm.compileHasAttr_wf` (theorem, [line 225](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/WF.lean#L225))

```lean
public theorem compileHasAttr_wf {t t₁: Term} {a : Attr} {εs : SymEntities}
  (hwε : εs.WellFormed)
  (hw₁ : Term.WellFormed εs t₁)
  (hok : compileHasAttr t₁ a εs = Except.ok t)  :
  t.WellFormed εs ∧ t.typeOf = .option .bool
```

`Cedar.Thm.compileAnd_preserves_wf` (theorem, [line 244](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/WF.lean#L244))

```lean
public theorem compileAnd_preserves_wf {εs : SymEntities} {t₁ t : Term} {r₂ : SymCC.Result Term}
  (hw₁ : t₁.WellFormed εs)
  (hty₁ : t₁.typeOf = .option .bool)
  (hr₂ : ∀ t₂, r₂ = .ok t₂ → t₂.WellFormed εs ∧ t₂.typeOf = .option .bool)
  (hok : compileAnd t₁ r₂ = .ok t) :
  t.WellFormed εs ∧ t.typeOf = .option .bool
```

`Cedar.Thm.compileGetAttr_wf` (theorem, [line 297](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/WF.lean#L297))

```lean
public theorem compileGetAttr_wf {t t₁: Term} {a : Attr} {εs : SymEntities}
  (hwε : εs.WellFormed)
  (hw₁ : Term.WellFormed εs t₁)
  (hok : compileGetAttr t₁ a εs = Except.ok t)  :
  t.WellFormed εs ∧ ∃ tyₐ, t.typeOf = .option tyₐ
```

`Cedar.Thm.compileExtHasAttrRec_wf` (theorem, [line 333](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/WF.lean#L333))

```lean
public theorem compileExtHasAttrRec_wf {t₁ : Term} {attrs : List Attr} {εs : SymEntities} {t : Term}
  (hwε : εs.WellFormed)
  (hw₁ : t₁.WellFormed εs) (hty₁ : ∃ ty, t₁.typeOf = .option ty)
  (hok : compileExtHasAttrRec t₁ attrs εs = .ok t) :
  t.WellFormed εs ∧ t.typeOf = .option .bool
```

`Cedar.Thm.compileApp₁_wf_types` (theorem, [line 419](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/WF.lean#L419))

```lean
public theorem compileApp₁_wf_types {op₁ : UnaryOp} {t t₁: Term} {εs : SymEntities}
  (hw₁ : Term.WellFormed εs t₁)
  (hok : compileApp₁ op₁ t₁ = Except.ok t)  :
  t.WellFormed εs ∧
  match op₁ with
  | .neg => t.typeOf = .option (.bitvec 64)
  | _    => t.typeOf = .option .bool
```

`Cedar.Thm.compileApp₁_wf` (theorem, [line 453](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/WF.lean#L453))

```lean
public theorem compileApp₁_wf {op₁ : UnaryOp} {t t₁: Term} {εs : SymEntities}
  (hw₁ : Term.WellFormed εs t₁)
  (hok : compileApp₁ op₁ t₁ = Except.ok t)  :
  t.WellFormed εs ∧ ∃ ty, t.typeOf = .option ty
```

`Cedar.Thm.compileInₑ.isEq_wf` (theorem, [line 478](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/WF.lean#L478))

```lean
public theorem compileInₑ.isEq_wf {t₁ t₂ : Term} {εs : SymEntities}
  (hw₁  : Term.WellFormed εs t₁)
  (hw₂  : Term.WellFormed εs t₂) :
  (SymCC.compileInₑ.isEq t₁ t₂).WellFormed εs ∧ (SymCC.compileInₑ.isEq t₁ t₂).typeOf = .bool
```

`Cedar.Thm.compileInₑ.isIn_wf` (theorem, [line 489](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/WF.lean#L489))

```lean
public theorem compileInₑ.isIn_wf {t₁ t₂ : Term} {ancs? : Option UnaryFunction} {ety₁ ety₂ : EntityType} {εs : SymEntities}
  (hwε  : εs.WellFormed)
  (hw₁  : Term.WellFormed εs t₁)
  (hty₁ : t₁.typeOf = .entity ety₁)
  (hw₂  : Term.WellFormed εs t₂)
  (hty₂ : t₂.typeOf = .entity ety₂)
  (ha   : ancs? = SymEntities.ancestorsOfType εs ety₁ ety₂) :
  (SymCC.compileInₑ.isIn t₁ t₂ ancs?).WellFormed εs ∧ (SymCC.compileInₑ.isIn t₁ t₂ ancs?).typeOf = .bool
```

`Cedar.Thm.compileInₑ_wf` (theorem, [line 509](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/WF.lean#L509))

```lean
public theorem compileInₑ_wf {t₁ t₂ : Term} {ancs? : Option UnaryFunction} {ety₁ ety₂ : EntityType} {εs : SymEntities}
  (hwε  : εs.WellFormed)
  (hw₁  : Term.WellFormed εs t₁)
  (hty₁ : t₁.typeOf = .entity ety₁)
  (hw₂  : Term.WellFormed εs t₂)
  (hty₂ : t₂.typeOf = .entity ety₂)
  (ha   : ancs? = SymEntities.ancestorsOfType εs ety₁ ety₂) :
  (SymCC.compileInₑ t₁ t₂ ancs?).WellFormed εs ∧ (SymCC.compileInₑ t₁ t₂ ancs?).typeOf = .bool
```

`Cedar.Thm.compileInₛ.isIn₁_wf` (theorem, [line 523](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/WF.lean#L523))

```lean
public theorem compileInₛ.isIn₁_wf {t ts : Term} {εs : SymEntities}
  (hw₁  : Term.WellFormed εs t)
  (hw₂  : Term.WellFormed εs ts) :
  (SymCC.compileInₛ.isIn₁ t ts).WellFormed εs ∧ (SymCC.compileInₛ.isIn₁ t ts).typeOf = .bool
```

`Cedar.Thm.compileInₛ.isIn₂_wf` (theorem, [line 534](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/WF.lean#L534))

```lean
public theorem compileInₛ.isIn₂_wf {t ts : Term} {ancs? : Option UnaryFunction} {ety₁ ety₂ : EntityType} {εs : SymEntities}
  (hwε  : εs.WellFormed)
  (hw₁  : Term.WellFormed εs t)
  (hty₁ : t.typeOf = .entity ety₁)
  (hw₂  : Term.WellFormed εs ts)
  (hty₂ : ts.typeOf = .set (.entity ety₂))
  (ha   : ancs? = SymEntities.ancestorsOfType εs ety₁ ety₂) :
  (SymCC.compileInₛ.isIn₂ t ts ancs?).WellFormed εs ∧ (SymCC.compileInₛ.isIn₂ t ts ancs?).typeOf = .bool
```

`Cedar.Thm.compileInₛ_wf` (theorem, [line 554](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/WF.lean#L554))

```lean
public theorem compileInₛ_wf {t ts : Term} {ancs? : Option UnaryFunction} {ety₁ ety₂ : EntityType} {εs : SymEntities}
  (hwε  : εs.WellFormed)
  (hw₁  : Term.WellFormed εs t)
  (hty₁ : t.typeOf = .entity ety₁)
  (hw₂  : Term.WellFormed εs ts)
  (hty₂ : ts.typeOf = .set (.entity ety₂))
  (ha   : ancs? = SymEntities.ancestorsOfType εs ety₁ ety₂) :
  (SymCC.compileInₛ t ts ancs?).WellFormed εs ∧ (SymCC.compileInₛ t ts ancs?).typeOf = .bool
```

`Cedar.Thm.compileApp₂_wf_types` (theorem, [line 568](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/WF.lean#L568))

```lean
public theorem compileApp₂_wf_types {op₂ : BinaryOp} {t t₁ t₂: Term} {εs : SymEntities}
  (hwε : εs.WellFormed)
  (hw₁ : Term.WellFormed εs t₁)
  (hw₂ : Term.WellFormed εs t₂)
  (hok : compileApp₂ op₂ t₁ t₂ εs = Except.ok t)  :
  t.WellFormed εs ∧
  match op₂ with
  | .add | .sub | .mul => t.typeOf = .option (.bitvec 64)
  | .getTag            => ∃ ety τs, t₁.typeOf = .entity ety ∧ εs.tags ety = some (some τs) ∧ t.typeOf = τs.vals.outType.option
  | _                  => t.typeOf = .option .bool
```

`Cedar.Thm.compileApp₂_wf` (theorem, [line 669](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/WF.lean#L669))

```lean
public theorem compileApp₂_wf {op₂ : BinaryOp} {t t₁ t₂: Term} {εs : SymEntities}
  (hwε : εs.WellFormed)
  (hw₁ : Term.WellFormed εs t₁)
  (hw₂ : Term.WellFormed εs t₂)
  (hok : compileApp₂ op₂ t₁ t₂ εs = Except.ok t)  :
  t.WellFormed εs ∧ ∃ ty, t.typeOf = .option ty
```

`Cedar.Thm.compileCall_wf_types` (theorem, [line 800](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/WF.lean#L800))

```lean
public theorem compileCall_wf_types {f : ExtFun} {ts : List Term} {εs : SymEntities} {t : Term}
  (hwf : ∀ t ∈ ts, Term.WellFormed εs t)
  (hok : compileCall f ts = Except.ok t)  :
  t.WellFormed εs ∧
  match f with
  | .decimal         => t.typeOf = .option (.ext .decimal)
  | .ip              => t.typeOf = .option (.ext .ipAddr)
  | .datetime
  | .offset
  | .toDate          => t.typeOf = .option (.ext .datetime)
  | .toTime
  | .duration
  | .durationSince   => t.typeOf = .option (.ext .duration)
  | .toMilliseconds
  | .toSeconds
  | .toMinutes
  | .toHours
  | .toDays          => t.typeOf = .option (.bitvec 64)
  | _                => t.typeOf = .option .bool
```

`Cedar.Thm.compileCall_wf` (theorem, [line 878](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/WF.lean#L878))

```lean
public theorem compileCall_wf {f : ExtFun} {ts : List Term} {εs : SymEntities} {t : Term}
  (hwf : ∀ t ∈ ts, Term.WellFormed εs t)
  (hok : compileCall f ts = Except.ok t)  :
  t.WellFormed εs ∧ ∃ ty, t.typeOf = .option ty
```

`Cedar.Thm.compile_wf` (theorem, [line 900](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/WF.lean#L900))

```lean
public theorem compile_wf {x : Expr} {εnv : SymEnv} {t : Term} :
  εnv.WellFormedFor x →
  compile x εnv = .ok t →
  (t.WellFormed εnv.entities ∧ ∃ ty, t.typeOf = .option ty)
```

`Cedar.Thm.compile_extHasAttr_typeOf` (theorem, [line 955](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/WF.lean#L955))

```lean
public theorem compile_extHasAttr_typeOf {x₁ : Expr} {a : Attr} {l : List Attr} {εnv : SymEnv} {t : Term}
  (hwf : SymEnv.WellFormedFor εnv (Expr.extHasAttr x₁ a l))
  (hok : compile (Expr.extHasAttr x₁ a l) εnv = Except.ok t) :
  t.typeOf = .option .bool
```

`Cedar.Thm.compile_option_get_wf` (theorem, [line 963](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/WF.lean#L963))

```lean
public theorem compile_option_get_wf {x : Expr} {εnv : SymEnv} {t : Term} :
  εnv.WellFormedFor x →
  compile x εnv = .ok t →
  ∃ ty,
    (t.WellFormed εnv.entities ∧ t.typeOf = .option ty) ∧
    ((option.get t).WellFormed εnv.entities ∧ (option.get t).typeOf = ty)
```

`Cedar.Thm.evaluate_wf` (theorem, [line 1318](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/WF.lean#L1318))

```lean
public theorem evaluate_wf {x : Expr} {env : Env} {v : Value} :
  env.WellFormedFor x →
  evaluate x env.request env.entities = .ok v →
  v.WellFormed env.entities
```

`Cedar.Thm.wf_value_uid_implies_exists_entity_data` (theorem, [line 1349](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/WF.lean#L1349))

```lean
public theorem wf_value_uid_implies_exists_entity_data {es : Entities} {uid : EntityUID}
  (hwf : Value.WellFormed es (Value.prim (Prim.entityUID uid))) :
  ∃ d, es.find? uid = some d
```

## Depends on

- [Spec/Evaluator](../../../spec/evaluator.md)
- [ExtHasAttrRec](exthasattrrec.md)
- [Well-formedness and interpretations](../data/basic.md)

## Proof depends on

- [Invert](invert.md)
- [Well-formed terms and factory functions](../term/wf.md)

## Sources

- [Cedar/Thm/SymCC/Compiler/WF.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/WF.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Compiler.WF.json)
