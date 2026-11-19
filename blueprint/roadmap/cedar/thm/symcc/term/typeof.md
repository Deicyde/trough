---
catalog: module
lean: Cedar.Thm.typeOf_bool, Cedar.Thm.typeOf_bv, Cedar.Thm.typeOf_term_none, Cedar.Thm.typeOf_term_some, Cedar.Thm.typeOf_term_some_iff, Cedar.Thm.typeOf_term_prim_isPrimType, Cedar.Thm.typeOf_term_prim_entity, Cedar.Thm.typeOf_term_prim_string, Cedar.Thm.typeOf_term_prim_ext_decimal, Cedar.Thm.typeOf_term_prim_ext_ipaddr, Cedar.Thm.typeOf_term_prim_ext_datetime, Cedar.Thm.typeOf_term_prim_ext_duration, Cedar.Thm.typeOf_term_var, Cedar.Thm.typeOf_term_set, Cedar.Thm.typeOf_term_record_eq, Cedar.Thm.typeOf_term_record_is_record_type, Cedar.Thm.typeOf_term_record_attr_value, Cedar.Thm.typeOf_term_record_attr_value_none, Cedar.Thm.typeOf_term_record_attr_value_typeOf, Cedar.Thm.typeOf_term_record_attr_value_eq, Cedar.Thm.typeOf_term_record_tail, Cedar.Thm.typeOf_term_app, Cedar.Thm.typeOf_wf_term_is_wf, Cedar.Thm.wfp_term_implies_wf_ty, Cedar.Thm.typeOf_option_wf_terms_is_wf, Cedar.Thm.typeOf_term_record_cedarType?_some_implies_attr_cedarType?_some, Cedar.Thm.isPrimType_implies_prim_type, Cedar.Thm.isEntityType_implies_entity_type, Cedar.Thm.isOptionEntityType_implies_option_entity_type, Cedar.Thm.typeOf_ifSome_option, Cedar.Thm.typeOf_ifAllSome_option_type
statement: formalized
proof: formalized
---

# Properties of Terms

`Cedar.Thm.SymCC.Term.TypeOf`, in [Cedar/Thm/SymCC/Term/TypeOf.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/TypeOf.lean).

> This file contains lemmas about the `typeOf` function on Terms.

`Cedar.Thm.typeOf_bool` (theorem, [line 42](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/TypeOf.lean#L42))

```lean
public theorem typeOf_bool {b : Bool} :
  Term.typeOf (Term.prim (TermPrim.bool b)) = TermType.bool
```

`Cedar.Thm.typeOf_bv` (theorem, [line 47](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/TypeOf.lean#L47))

```lean
public theorem typeOf_bv {n : Nat} {bv : BitVec n} :
  Term.typeOf (Term.prim (TermPrim.bitvec bv)) = .bitvec n
```

`Cedar.Thm.typeOf_term_none` (theorem, [line 52](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/TypeOf.lean#L52))

```lean
public theorem typeOf_term_none (ty : TermType) :
  Term.typeOf (Term.none ty) = TermType.option ty
```

`Cedar.Thm.typeOf_term_some` (theorem, [line 57](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/TypeOf.lean#L57))

```lean
public theorem typeOf_term_some {t : Term} :
  Term.typeOf (Term.some t) = TermType.option t.typeOf
```

`Cedar.Thm.typeOf_term_some_iff` (theorem, [line 61](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/TypeOf.lean#L61))

```lean
public theorem typeOf_term_some_iff {t : Term} {ty : TermType} :
  t.typeOf = ty ↔
  Term.typeOf (Term.some t) = TermType.option ty
```

`Cedar.Thm.typeOf_term_prim_isPrimType` (theorem, [line 66](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/TypeOf.lean#L66))

```lean
public theorem typeOf_term_prim_isPrimType (p : TermPrim) :
  (Term.prim p).typeOf.isPrimType
```

`Cedar.Thm.typeOf_term_prim_entity` (theorem, [line 74](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/TypeOf.lean#L74))

```lean
public theorem typeOf_term_prim_entity {uid : EntityUID} :
  (Term.entity uid).typeOf = TermType.entity uid.ty
```

`Cedar.Thm.typeOf_term_prim_string` (theorem, [line 80](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/TypeOf.lean#L80))

```lean
public theorem typeOf_term_prim_string {s : String} :
  (Term.string s).typeOf = TermType.string
```

`Cedar.Thm.typeOf_term_prim_ext_decimal` (theorem, [line 86](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/TypeOf.lean#L86))

```lean
public theorem typeOf_term_prim_ext_decimal {d : Ext.Decimal} :
  (Term.prim (.ext (.decimal d))).typeOf = TermType.ext Validation.ExtType.decimal
```

`Cedar.Thm.typeOf_term_prim_ext_ipaddr` (theorem, [line 91](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/TypeOf.lean#L91))

```lean
public theorem typeOf_term_prim_ext_ipaddr {ip : Ext.IPAddr.IPNet} :
  (Term.prim (.ext (.ipaddr ip))).typeOf = TermType.ext Validation.ExtType.ipAddr
```

`Cedar.Thm.typeOf_term_prim_ext_datetime` (theorem, [line 96](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/TypeOf.lean#L96))

```lean
public theorem typeOf_term_prim_ext_datetime {d : Ext.Datetime} :
  (Term.prim (.ext (.datetime d))).typeOf = TermType.ext Validation.ExtType.datetime
```

`Cedar.Thm.typeOf_term_prim_ext_duration` (theorem, [line 101](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/TypeOf.lean#L101))

```lean
public theorem typeOf_term_prim_ext_duration {d : Ext.Datetime.Duration} :
  (Term.prim (.ext (.duration d))).typeOf = TermType.ext Validation.ExtType.duration
```

`Cedar.Thm.typeOf_term_var` (theorem, [line 106](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/TypeOf.lean#L106))

```lean
public theorem typeOf_term_var (v : TermVar) :
  (Term.var v).typeOf = v.ty
```

`Cedar.Thm.typeOf_term_set` (theorem, [line 111](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/TypeOf.lean#L111))

```lean
public theorem typeOf_term_set {elts : Set Term} {eltsTy : TermType} :
  (Term.set elts eltsTy).typeOf = TermType.set eltsTy
```

`Cedar.Thm.typeOf_term_record_eq` (theorem, [line 116](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/TypeOf.lean#L116))

```lean
public theorem typeOf_term_record_eq  {r : Map Attr Term} :
  Term.typeOf (Term.record r) =
  TermType.record (r.mapOnValues Term.typeOf)
```

`Cedar.Thm.typeOf_term_record_is_record_type` (theorem, [line 121](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/TypeOf.lean#L121))

```lean
public theorem typeOf_term_record_is_record_type {r : Map Attr Term} :
  ∃ rty, (Term.record r).typeOf = TermType.record rty
```

`Cedar.Thm.typeOf_term_record_attr_value` (theorem, [line 127](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/TypeOf.lean#L127))

```lean
public theorem typeOf_term_record_attr_value {r : Map Attr Term} {rty : Map Attr TermType} {a : Attr} {ty : TermType}
  (h₁ : (Term.record r).typeOf = TermType.record rty)
  (h₂ : rty.find? a = .some ty) :
  ∃ t, r.find? a = .some t ∧ t.typeOf = ty
```

`Cedar.Thm.typeOf_term_record_attr_value_none` (theorem, [line 139](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/TypeOf.lean#L139))

```lean
public theorem typeOf_term_record_attr_value_none {r : Map Attr Term} {rty : Map Attr TermType} {a : Attr}
  (h₁ : (Term.record r).typeOf = TermType.record rty)
  (h₂ : rty.find? a = none) :
  r.find? a = none
```

`Cedar.Thm.typeOf_term_record_attr_value_typeOf` (theorem, [line 150](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/TypeOf.lean#L150))

```lean
public theorem typeOf_term_record_attr_value_typeOf {r : Map Attr Term} {a : Attr} {t : Term}
  (h₁ : (Term.record r).typeOf = TermType.record rty)
  (h₂ : r.find? a = .some t) :
  rty.find? a = .some t.typeOf
```

`Cedar.Thm.typeOf_term_record_attr_value_eq` (theorem, [line 160](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/TypeOf.lean#L160))

```lean
public theorem typeOf_term_record_attr_value_eq {r₁ r₂ : Map Attr Term} {rty : Map Attr TermType} {a : Attr} {t₁ t₂ : Term}
  (hty₁ : (Term.record r₁).typeOf = .record rty)
  (hty₂ : (Term.record r₂).typeOf = .record rty)
  (ht₁ : r₁.find? a = .some t₁)
  (ht₂ : r₂.find? a = .some t₂) :
  t₁.typeOf = t₂.typeOf
```

`Cedar.Thm.typeOf_term_record_tail` (theorem, [line 172](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/TypeOf.lean#L172))

```lean
public theorem typeOf_term_record_tail {a : Attr} {t₁ t₂ : Term} {tl₁ tl₂ : List (Attr × Term)} :
  Term.typeOf (Term.record (Map.mk ((a, t₁) :: tl₁))) = Term.typeOf (Term.record (Map.mk ((a, t₂) :: tl₂))) →
  Term.typeOf (Term.record (Map.mk tl₁)) = Term.typeOf (Term.record (Map.mk tl₂))
```

`Cedar.Thm.typeOf_term_app` (theorem, [line 180](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/TypeOf.lean#L180))

```lean
public theorem typeOf_term_app {op : Op} {args : List Term} :
  Term.typeOf (Term.app op args ty) = ty
```

`Cedar.Thm.typeOf_wf_term_is_wf` (theorem, [line 254](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/TypeOf.lean#L254))

```lean
public theorem typeOf_wf_term_is_wf {εs : SymEntities} {t : Term} :
  t.WellFormed εs →
  t.typeOf.WellFormed εs
```

`Cedar.Thm.wfp_term_implies_wf_ty` (theorem, [line 278](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/TypeOf.lean#L278))

```lean
public theorem wfp_term_implies_wf_ty {εs : SymEntities} {t : Term}
  (h : Term.WellFormedPartialApp εs t) :
  t.typeOf.WellFormed εs
```

`Cedar.Thm.typeOf_option_wf_terms_is_wf` (theorem, [line 290](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/TypeOf.lean#L290))

```lean
public theorem typeOf_option_wf_terms_is_wf {εs : SymEntities} {hd : Term} {tl : List Term} {ts : List Term} {ty : TermType}:
  ts = hd :: tl →
  (∀ t ∈ ts, t.WellFormed εs) →
  (∀ t ∈ ts, Term.typeOf t = TermType.option ty) →
  ty.WellFormed εs
```

`Cedar.Thm.typeOf_term_record_cedarType?_some_implies_attr_cedarType?_some` (theorem, [line 303](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/TypeOf.lean#L303))

```lean
public theorem typeOf_term_record_cedarType?_some_implies_attr_cedarType?_some {a : Attr} {t : Term} {r : Map Attr Term} {ty : Validation.CedarType} :
  r.WellFormed →
  (Term.record r).typeOf.cedarType? = some ty →
  (a, t) ∈ r.toList →
  ∃ (tty : TermType) (cty : Validation.CedarType),
    tty.cedarType? = some cty ∧
    (t.typeOf = tty ∨ t.typeOf = .option tty)
```

`Cedar.Thm.isPrimType_implies_prim_type` (theorem, [line 332](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/TypeOf.lean#L332))

```lean
public theorem isPrimType_implies_prim_type {ty : TermType} :
  ty.isPrimType → ∃ pty, ty = .prim pty
```

`Cedar.Thm.isEntityType_implies_entity_type` (theorem, [line 339](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/TypeOf.lean#L339))

```lean
public theorem isEntityType_implies_entity_type {ty : TermType} :
  ty.isEntityType → ∃ ety, ty = .entity ety
```

`Cedar.Thm.isOptionEntityType_implies_option_entity_type` (theorem, [line 347](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/TypeOf.lean#L347))

```lean
public theorem isOptionEntityType_implies_option_entity_type {ty : TermType} :
  ty.isOptionEntityType → ∃ ety, ty = .option (.entity ety)
```

`Cedar.Thm.typeOf_ifSome_option` (theorem, [line 367](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/TypeOf.lean#L367))

```lean
public theorem typeOf_ifSome_option {g t : Term} {ty : TermType} :
  t.typeOf = .option ty →
  (Factory.ifSome g t).typeOf = .option ty
```

`Cedar.Thm.typeOf_ifAllSome_option_type` (theorem, [line 375](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/TypeOf.lean#L375))

```lean
public theorem typeOf_ifAllSome_option_type {gs : List Term} {t : Term} {ty : TermType} :
  t.typeOf = .option ty →
  (Factory.ifAllSome gs t).typeOf = .option ty
```

## Depends on

- [Well-formedness and interpretations](../data/basic.md)

## Proof depends on

- [Basic properties of well-formed symbolic environments](../env/wf.md)

## Sources

- [Cedar/Thm/SymCC/Term/TypeOf.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/TypeOf.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Term.TypeOf.json)
