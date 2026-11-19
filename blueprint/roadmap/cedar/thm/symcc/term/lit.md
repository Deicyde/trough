---
catalog: module
lean: Cedar.Thm.isLiteral_empty, Cedar.Thm.lit_term_set_implies_lit_elt, Cedar.Thm.lit_term_set_impliedBy_lit_elts, Cedar.Thm.isLiteral_set_cons, Cedar.Thm.lit_term_record_implies_lit_value, Cedar.Thm.isLiteral_record_mapOnValues, Cedar.Thm.isLiteral_some, Cedar.Thm.isLiteral_none, Cedar.Thm.isLiteral_prim, Cedar.Thm.wfl_of_type_bool_is_bool, Cedar.Thm.wfl_of_type_bool_is_true_or_false, Cedar.Thm.wfl_of_type_bitvec_is_bitvec, Cedar.Thm.wfl_of_type_datetime_is_datetime, Cedar.Thm.wfl_of_type_duration_is_duration, Cedar.Thm.wfl_of_type_string_is_string, Cedar.Thm.wfl_of_type_entity_is_entity, Cedar.Thm.wfl_of_type_set_is_set, Cedar.Thm.wfl_of_type_record_is_record, Cedar.Thm.wfl_of_type_ext_decimal_is_ext_decimal, Cedar.Thm.wfl_of_type_ext_ipaddr_is_ext_ipaddr, Cedar.Thm.wfl_of_type_ext_datetime_is_ext_datetime, Cedar.Thm.wfl_of_type_ext_duration_is_ext_duration, Cedar.Thm.wfl_of_type_option_is_option, Cedar.Thm.wfl_of_prim_type_is_prim
statement: formalized
proof: formalized
---

# Properties of literal terms

`Cedar.Thm.SymCC.Term.Lit`, in [Cedar/Thm/SymCC/Term/Lit.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Lit.lean).

> This file proves basic lemmas about literal terms
> -

`Cedar.Thm.isLiteral_empty` (theorem, [line 36](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Lit.lean#L36))

```lean
public theorem isLiteral_empty (eltsTy : TermType) :
  Term.isLiteral (.set Set.empty eltsTy)
```

`Cedar.Thm.lit_term_set_implies_lit_elt` (theorem, [line 40](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Lit.lean#L40))

```lean
public theorem lit_term_set_implies_lit_elt {s : Set Term} {ty : TermType} {t : Term} :
  (Term.set s ty).isLiteral → t ∈ s → t.isLiteral
```

`Cedar.Thm.lit_term_set_impliedBy_lit_elts` (theorem, [line 47](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Lit.lean#L47))

```lean
public theorem lit_term_set_impliedBy_lit_elts {s : Set Term} {ty : TermType} :
  (∀ t ∈ s, t.isLiteral) → (Term.set s ty).isLiteral
```

`Cedar.Thm.isLiteral_set_cons` (theorem, [line 51](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Lit.lean#L51))

```lean
public theorem isLiteral_set_cons {hd : Term} {tl : List Term} {ty : TermType} :
  (Term.set (Set.mk (hd :: tl)) ty).isLiteral →
  (hd.isLiteral ∧ (Term.set (Set.mk tl) ty).isLiteral)
```

`Cedar.Thm.lit_term_record_implies_lit_value` (theorem, [line 65](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Lit.lean#L65))

```lean
public theorem lit_term_record_implies_lit_value {r : Map Attr Term} {a : Attr} {t : Term} :
  Term.isLiteral (Term.record r) → (a, t) ∈ r.toList → t.isLiteral
```

`Cedar.Thm.isLiteral_record_mapOnValues` (theorem, [line 74](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Lit.lean#L74))

```lean
public theorem isLiteral_record_mapOnValues {m : Map Attr β} {f : β → Term} :
  (Term.isLiteral (.record (m.mapOnValues f)) ↔ ∀ v ∈ m.values, (f v).isLiteral)
```

`Cedar.Thm.isLiteral_some` (theorem, [line 90](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Lit.lean#L90))

```lean
public theorem isLiteral_some {t : Term} :
  (Term.some t).isLiteral ↔ t.isLiteral
```

`Cedar.Thm.isLiteral_none` (theorem, [line 95](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Lit.lean#L95))

```lean
public theorem isLiteral_none {tty : TermType} :
  (Term.none tty).isLiteral = true
```

`Cedar.Thm.isLiteral_prim` (theorem, [line 100](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Lit.lean#L100))

```lean
public theorem isLiteral_prim {p : TermPrim} :
  (Term.prim p).isLiteral
```

`Cedar.Thm.wfl_of_type_bool_is_bool` (theorem, [line 104](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Lit.lean#L104))

```lean
public theorem wfl_of_type_bool_is_bool {εs : SymEntities} {t : Term} :
  t.WellFormedLiteral εs →
  t.typeOf = .bool →
  ∃ b, t = .prim (.bool b)
```

`Cedar.Thm.wfl_of_type_bool_is_true_or_false` (theorem, [line 120](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Lit.lean#L120))

```lean
public theorem wfl_of_type_bool_is_true_or_false {εs : SymEntities} {t : Term} :
  t.WellFormedLiteral εs →
  t.typeOf = .bool →
  t = .prim (.bool true) ∨ t = .prim (.bool false)
```

`Cedar.Thm.wfl_of_type_bitvec_is_bitvec` (theorem, [line 129](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Lit.lean#L129))

```lean
public theorem wfl_of_type_bitvec_is_bitvec {εs : SymEntities} {t : Term} {n : Nat} :
  t.WellFormedLiteral εs →
  t.typeOf = .bitvec n →
  ∃ (bv : BitVec n), t = .prim (.bitvec bv)
```

`Cedar.Thm.wfl_of_type_datetime_is_datetime` (theorem, [line 148](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Lit.lean#L148))

```lean
public theorem wfl_of_type_datetime_is_datetime {εs : SymEntities} {t : Term}:
  t.WellFormedLiteral εs →
  t.typeOf = .ext .datetime →
  ∃ (d : Cedar.Spec.Ext.Datetime), t = .prim (.ext (.datetime d))
```

`Cedar.Thm.wfl_of_type_duration_is_duration` (theorem, [line 163](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Lit.lean#L163))

```lean
public theorem wfl_of_type_duration_is_duration {εs : SymEntities} {t : Term}:
  t.WellFormedLiteral εs →
  t.typeOf = .ext .duration →
  ∃ (d : Duration), t = .prim (.ext (.duration d))
```

`Cedar.Thm.wfl_of_type_string_is_string` (theorem, [line 178](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Lit.lean#L178))

```lean
public theorem wfl_of_type_string_is_string {εs : SymEntities} {t : Term} :
  t.WellFormedLiteral εs →
  t.typeOf = .string →
  ∃ (s : String), t = .prim (.string s)
```

`Cedar.Thm.wfl_of_type_entity_is_entity` (theorem, [line 194](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Lit.lean#L194))

```lean
public theorem wfl_of_type_entity_is_entity {εs : SymEntities} {t : Term} {ety : EntityType} :
  t.WellFormedLiteral εs →
  t.typeOf = .entity ety →
  ∃ (uid : EntityUID), t = .prim (.entity uid) ∧ uid.ty = ety
```

`Cedar.Thm.wfl_of_type_set_is_set` (theorem, [line 213](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Lit.lean#L213))

```lean
public theorem wfl_of_type_set_is_set {εs : SymEntities} {t : Term} {ty : TermType} :
  t.WellFormedLiteral εs →
  t.typeOf = .set ty →
  ∃ (s : Set Term), t = .set s ty
```

`Cedar.Thm.wfl_of_type_record_is_record` (theorem, [line 232](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Lit.lean#L232))

```lean
public theorem wfl_of_type_record_is_record {εs : SymEntities} {t : Term} {rty : Map Attr TermType} :
  t.WellFormedLiteral εs →
  t.typeOf = .record rty →
  ∃ (r : Map Attr Term), t = .record r
```

`Cedar.Thm.wfl_of_type_ext_decimal_is_ext_decimal` (theorem, [line 263](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Lit.lean#L263))

```lean
public theorem wfl_of_type_ext_decimal_is_ext_decimal {εs : SymEntities} {t : Term} :
  t.WellFormedLiteral εs →
  t.typeOf = .ext .decimal →
  ∃ (d : Ext.Decimal), t = .prim (.ext (.decimal d))
```

`Cedar.Thm.wfl_of_type_ext_ipaddr_is_ext_ipaddr` (theorem, [line 269](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Lit.lean#L269))

```lean
public theorem wfl_of_type_ext_ipaddr_is_ext_ipaddr {εs : SymEntities} {t : Term} :
  t.WellFormedLiteral εs →
  t.typeOf = .ext .ipAddr →
  ∃ (ip : IPAddr), t = .prim (.ext (.ipaddr ip))
```

`Cedar.Thm.wfl_of_type_ext_datetime_is_ext_datetime` (theorem, [line 275](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Lit.lean#L275))

```lean
public theorem wfl_of_type_ext_datetime_is_ext_datetime {εs : SymEntities} {t : Term} :
  t.WellFormedLiteral εs →
  t.typeOf = .ext .datetime →
  ∃ (d : Ext.Datetime), t = .prim (.ext (.datetime d))
```

`Cedar.Thm.wfl_of_type_ext_duration_is_ext_duration` (theorem, [line 281](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Lit.lean#L281))

```lean
public theorem wfl_of_type_ext_duration_is_ext_duration {εs : SymEntities} {t : Term} :
  t.WellFormedLiteral εs →
  t.typeOf = .ext .duration →
  ∃ (d : Ext.Datetime.Duration), t = .prim (.ext (.duration d))
```

`Cedar.Thm.wfl_of_type_option_is_option` (theorem, [line 287](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Lit.lean#L287))

```lean
public theorem wfl_of_type_option_is_option {εs : SymEntities} {t : Term} {ty : TermType} :
  t.WellFormedLiteral εs →
  t.typeOf = .option ty →
  t = .none ty ∨ ∃ t', t = .some t' ∧ t'.typeOf = ty
```

`Cedar.Thm.wfl_of_prim_type_is_prim` (theorem, [line 304](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Lit.lean#L304))

```lean
public theorem wfl_of_prim_type_is_prim {εs : SymEntities} {t : Term} {pty : TermPrimType} :
  t.WellFormedLiteral εs →
  t.typeOf = .prim pty →
  ∃ (p : TermPrim), t = .prim p
```

## Depends on

- [Well-formedness and interpretations](../data/basic.md)

## Proof depends on

- [Properties of Terms](typeof.md)

## Sources

- [Cedar/Thm/SymCC/Term/Lit.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Lit.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Term.Lit.json)
