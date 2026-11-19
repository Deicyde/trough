---
catalog: module
lean: Cedar.Thm.interpret_term_prim, Cedar.Thm.interpret_term_var, Cedar.Thm.interpret_term_none, Cedar.Thm.interpret_term_some, Cedar.Thm.interpret_term_set, Cedar.Thm.interpret_term_set_empty, Cedar.Thm.interpret_term_set_mk_nil, Cedar.Thm.interpret_term_record, Cedar.Thm.interpret_term_app_not, Cedar.Thm.interpret_term_app_and, Cedar.Thm.interpret_term_app_or, Cedar.Thm.interpret_term_app_eq, Cedar.Thm.interpret_term_app_ite, Cedar.Thm.interpret_term_app_uuf, Cedar.Thm.interpret_term_app_bvneg, Cedar.Thm.interpret_term_app_bvadd, Cedar.Thm.interpret_term_app_bvsub, Cedar.Thm.interpret_term_app_bvmul, Cedar.Thm.interpret_term_app_bvsdiv, Cedar.Thm.interpret_term_app_bvudiv, Cedar.Thm.interpret_term_app_bvsrem, Cedar.Thm.interpret_term_app_bvsmod, Cedar.Thm.interpret_term_app_bvurem, Cedar.Thm.interpret_term_app_bvshl, Cedar.Thm.interpret_term_app_bvlshr, Cedar.Thm.interpret_term_app_bvnego, Cedar.Thm.interpret_term_app_bvsaddo, Cedar.Thm.interpret_term_app_bvssubo, Cedar.Thm.interpret_term_app_bvsmulo, Cedar.Thm.interpret_term_app_bvslt, Cedar.Thm.interpret_term_app_bvsle, Cedar.Thm.interpret_term_app_bvult, Cedar.Thm.interpret_term_app_bvule, Cedar.Thm.interpret_term_app_zero_extend, Cedar.Thm.interpret_term_app_set_member, Cedar.Thm.interpret_term_app_set_subset, Cedar.Thm.interpret_term_app_set_inter, Cedar.Thm.interpret_term_app_option_get, Cedar.Thm.interpret_term_app_record_get, Cedar.Thm.interpret_term_app_string_like, Cedar.Thm.interpret_term_app_ext_decimal_val, Cedar.Thm.interpret_term_app_ext_ipaddr_isV4, Cedar.Thm.interpret_term_app_ext_ipaddr_addrV4, Cedar.Thm.interpret_term_app_ext_ipaddr_prefixV4, Cedar.Thm.interpret_term_app_ext_ipaddr_addrV6, Cedar.Thm.interpret_term_app_ext_ipaddr_prefixV6, Cedar.Thm.interpret_term_app_ext_datetime_val, Cedar.Thm.interpret_term_app_ext_datetime_ofBitVec, Cedar.Thm.interpret_term_app_ext_duration_val, Cedar.Thm.interpret_term_app_ext_duration_ofBitVec
statement: formalized
proof: formalized
---

# Interpretation of Terms and Factory functions

`Cedar.Thm.SymCC.Term.Interpret.Basic`, in [Cedar/Thm/SymCC/Term/Interpret/Basic.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean).

> This file basic lemmas about the interpretation of terms and
> the Factory functions for creating terms.
> -

`Cedar.Thm.interpret_term_prim` (theorem, [line 41](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L41))

```lean
public theorem interpret_term_prim {I : Interpretation} {p : TermPrim} :
  (Term.prim p).interpret I = Term.prim p
```

`Cedar.Thm.interpret_term_var` (theorem, [line 46](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L46))

```lean
public theorem interpret_term_var {I : Interpretation} {v : TermVar} :
  (Term.var v).interpret I = I.vars v
```

`Cedar.Thm.interpret_term_none` (theorem, [line 51](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L51))

```lean
public theorem interpret_term_none {I : Interpretation} {ty : TermType} :
  (Term.none ty).interpret I = Term.none ty
```

`Cedar.Thm.interpret_term_some` (theorem, [line 56](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L56))

```lean
public theorem interpret_term_some {I : Interpretation} {t : Term} :
  (Term.some t).interpret I = Term.some (t.interpret I)
```

`Cedar.Thm.interpret_term_set` (theorem, [line 61](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L61))

```lean
public theorem interpret_term_set {I : Interpretation} {s : Set Term} {ty : TermType} :
  (Term.set s ty).interpret I =
  Term.set (s.map (Term.interpret I)) ty
```

`Cedar.Thm.interpret_term_set_empty` (theorem, [line 67](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L67))

```lean
public theorem interpret_term_set_empty {ty : TermType} :
  Term.interpret I (Term.set Set.empty ty) = Term.set Set.empty ty
```

`Cedar.Thm.interpret_term_set_mk_nil` (theorem, [line 72](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L72))

```lean
public theorem interpret_term_set_mk_nil {ty : TermType} :
  Term.interpret I (Term.set (Set.mk []) ty) = Term.set (Set.mk []) ty
```

`Cedar.Thm.interpret_term_record` (theorem, [line 79](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L79))

```lean
public theorem interpret_term_record {I : Interpretation} {r : Map Attr Term} :
  (Term.record r).interpret I =
  Term.record (r.mapOnValues (Term.interpret I))
```

`Cedar.Thm.interpret_term_app_not` (theorem, [line 98](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L98))

```lean
public theorem interpret_term_app_not {I : Interpretation} {t₁ : Term} {ty : TermType} :
  (Term.app .not [t₁] ty).interpret I =
  Factory.not (t₁.interpret I)
```

`Cedar.Thm.interpret_term_app_and` (theorem, [line 104](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L104))

```lean
public theorem interpret_term_app_and {I : Interpretation} {t₁ t₂ : Term} {ty : TermType} :
  (Term.app .and [t₁, t₂] ty).interpret I =
  Factory.and (t₁.interpret I) (t₂.interpret I)
```

`Cedar.Thm.interpret_term_app_or` (theorem, [line 110](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L110))

```lean
public theorem interpret_term_app_or {I : Interpretation} {t₁ t₂ : Term} {ty : TermType} :
  (Term.app .or [t₁, t₂] ty).interpret I =
  Factory.or (t₁.interpret I) (t₂.interpret I)
```

`Cedar.Thm.interpret_term_app_eq` (theorem, [line 116](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L116))

```lean
public theorem interpret_term_app_eq {I : Interpretation} {t₁ t₂ : Term} {ty : TermType} :
  (Term.app .eq [t₁, t₂] ty).interpret I =
  Factory.eq (t₁.interpret I) (t₂.interpret I)
```

`Cedar.Thm.interpret_term_app_ite` (theorem, [line 122](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L122))

```lean
public theorem interpret_term_app_ite {I : Interpretation} {t₁ t₂ t₃ : Term} {ty : TermType} :
  (Term.app .ite [t₁, t₂, t₃] ty).interpret I =
  Factory.ite (t₁.interpret I) (t₂.interpret I) (t₃.interpret I)
```

`Cedar.Thm.interpret_term_app_uuf` (theorem, [line 128](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L128))

```lean
public theorem interpret_term_app_uuf {I : Interpretation} {f : UUF} {t₁ : Term} {ty : TermType} :
  (Term.app (.uuf f) [t₁] ty).interpret I =
  Factory.app (.udf (I.funs f)) (t₁.interpret I)
```

`Cedar.Thm.interpret_term_app_bvneg` (theorem, [line 134](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L134))

```lean
public theorem interpret_term_app_bvneg {I : Interpretation} {t₁ : Term} {ty : TermType} :
  (Term.app .bvneg [t₁] ty).interpret I =
  Factory.bvneg (t₁.interpret I)
```

`Cedar.Thm.interpret_term_app_bvadd` (theorem, [line 140](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L140))

```lean
public theorem interpret_term_app_bvadd {I : Interpretation} {t₁ t₂ : Term} {ty : TermType} :
  (Term.app .bvadd [t₁, t₂] ty).interpret I =
  Factory.bvadd (t₁.interpret I) (t₂.interpret I)
```

`Cedar.Thm.interpret_term_app_bvsub` (theorem, [line 146](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L146))

```lean
public theorem interpret_term_app_bvsub {I : Interpretation} {t₁ t₂ : Term} {ty : TermType} :
  (Term.app .bvsub [t₁, t₂] ty).interpret I =
  Factory.bvsub (t₁.interpret I) (t₂.interpret I)
```

`Cedar.Thm.interpret_term_app_bvmul` (theorem, [line 152](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L152))

```lean
public theorem interpret_term_app_bvmul {I : Interpretation} {t₁ t₂ : Term} {ty : TermType} :
  (Term.app .bvmul [t₁, t₂] ty).interpret I =
  Factory.bvmul (t₁.interpret I) (t₂.interpret I)
```

`Cedar.Thm.interpret_term_app_bvsdiv` (theorem, [line 158](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L158))

```lean
public theorem interpret_term_app_bvsdiv {I : Interpretation} {t₁ t₂ : Term} {ty : TermType} :
  (Term.app .bvsdiv [t₁, t₂] ty).interpret I =
  Factory.bvsdiv (t₁.interpret I) (t₂.interpret I)
```

`Cedar.Thm.interpret_term_app_bvudiv` (theorem, [line 164](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L164))

```lean
public theorem interpret_term_app_bvudiv {I : Interpretation} {t₁ t₂ : Term} {ty : TermType} :
  (Term.app .bvudiv [t₁, t₂] ty).interpret I =
  Factory.bvudiv (t₁.interpret I) (t₂.interpret I)
```

`Cedar.Thm.interpret_term_app_bvsrem` (theorem, [line 170](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L170))

```lean
public theorem interpret_term_app_bvsrem {I : Interpretation} {t₁ t₂ : Term} {ty : TermType} :
  (Term.app .bvsrem [t₁, t₂] ty).interpret I =
  Factory.bvsrem (t₁.interpret I) (t₂.interpret I)
```

`Cedar.Thm.interpret_term_app_bvsmod` (theorem, [line 176](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L176))

```lean
public theorem interpret_term_app_bvsmod {I : Interpretation} {t₁ t₂ : Term} {ty : TermType} :
  (Term.app .bvsmod [t₁, t₂] ty).interpret I =
  Factory.bvsmod (t₁.interpret I) (t₂.interpret I)
```

`Cedar.Thm.interpret_term_app_bvurem` (theorem, [line 182](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L182))

```lean
public theorem interpret_term_app_bvurem {I : Interpretation} {t₁ t₂ : Term} {ty : TermType} :
  (Term.app .bvurem [t₁, t₂] ty).interpret I =
  Factory.bvurem (t₁.interpret I) (t₂.interpret I)
```

`Cedar.Thm.interpret_term_app_bvshl` (theorem, [line 188](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L188))

```lean
public theorem interpret_term_app_bvshl {I : Interpretation} {t₁ t₂ : Term} {ty : TermType} :
  (Term.app .bvshl [t₁, t₂] ty).interpret I =
  Factory.bvshl (t₁.interpret I) (t₂.interpret I)
```

`Cedar.Thm.interpret_term_app_bvlshr` (theorem, [line 194](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L194))

```lean
public theorem interpret_term_app_bvlshr {I : Interpretation} {t₁ t₂ : Term} {ty : TermType} :
  (Term.app .bvlshr [t₁, t₂] ty).interpret I =
  Factory.bvlshr (t₁.interpret I) (t₂.interpret I)
```

`Cedar.Thm.interpret_term_app_bvnego` (theorem, [line 200](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L200))

```lean
public theorem interpret_term_app_bvnego {I : Interpretation} {t₁ : Term} {ty : TermType} :
  (Term.app .bvnego [t₁] ty).interpret I =
  Factory.bvnego (t₁.interpret I)
```

`Cedar.Thm.interpret_term_app_bvsaddo` (theorem, [line 206](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L206))

```lean
public theorem interpret_term_app_bvsaddo {I : Interpretation} {t₁ t₂ : Term} {ty : TermType} :
  (Term.app .bvsaddo [t₁, t₂] ty).interpret I =
  Factory.bvsaddo (t₁.interpret I) (t₂.interpret I)
```

`Cedar.Thm.interpret_term_app_bvssubo` (theorem, [line 212](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L212))

```lean
public theorem interpret_term_app_bvssubo {I : Interpretation} {t₁ t₂ : Term} {ty : TermType} :
  (Term.app .bvssubo [t₁, t₂] ty).interpret I =
  Factory.bvssubo (t₁.interpret I) (t₂.interpret I)
```

`Cedar.Thm.interpret_term_app_bvsmulo` (theorem, [line 218](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L218))

```lean
public theorem interpret_term_app_bvsmulo {I : Interpretation} {t₁ t₂ : Term} {ty : TermType} :
  (Term.app .bvsmulo [t₁, t₂] ty).interpret I =
  Factory.bvsmulo (t₁.interpret I) (t₂.interpret I)
```

`Cedar.Thm.interpret_term_app_bvslt` (theorem, [line 224](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L224))

```lean
public theorem interpret_term_app_bvslt {I : Interpretation} {t₁ t₂ : Term} {ty : TermType} :
  (Term.app .bvslt [t₁, t₂] ty).interpret I =
  Factory.bvslt (t₁.interpret I) (t₂.interpret I)
```

`Cedar.Thm.interpret_term_app_bvsle` (theorem, [line 230](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L230))

```lean
public theorem interpret_term_app_bvsle {I : Interpretation} {t₁ t₂ : Term} {ty : TermType} :
  (Term.app .bvsle [t₁, t₂] ty).interpret I =
  Factory.bvsle (t₁.interpret I) (t₂.interpret I)
```

`Cedar.Thm.interpret_term_app_bvult` (theorem, [line 236](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L236))

```lean
public theorem interpret_term_app_bvult {I : Interpretation} {t₁ t₂ : Term} {ty : TermType} :
  (Term.app .bvult [t₁, t₂] ty).interpret I =
  Factory.bvult (t₁.interpret I) (t₂.interpret I)
```

`Cedar.Thm.interpret_term_app_bvule` (theorem, [line 242](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L242))

```lean
public theorem interpret_term_app_bvule {I : Interpretation} {t₁ t₂ : Term} {ty : TermType} :
  (Term.app .bvule [t₁, t₂] ty).interpret I =
  Factory.bvule (t₁.interpret I) (t₂.interpret I)
```

`Cedar.Thm.interpret_term_app_zero_extend` (theorem, [line 248](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L248))

```lean
public theorem interpret_term_app_zero_extend {I : Interpretation} {n : Nat} {t₁ : Term} {ty : TermType} :
  (Term.app (.zero_extend n) [t₁] ty).interpret I =
  Factory.zero_extend n (t₁.interpret I)
```

`Cedar.Thm.interpret_term_app_set_member` (theorem, [line 254](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L254))

```lean
public theorem interpret_term_app_set_member {I : Interpretation} {t₁ t₂ : Term} {ty : TermType} :
  (Term.app Op.set.member [t₁, t₂] ty).interpret I =
  Factory.set.member (t₁.interpret I) (t₂.interpret I)
```

`Cedar.Thm.interpret_term_app_set_subset` (theorem, [line 260](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L260))

```lean
public theorem interpret_term_app_set_subset {I : Interpretation} {t₁ t₂ : Term} {ty : TermType} :
  (Term.app Op.set.subset [t₁, t₂] ty).interpret I =
  Factory.set.subset (t₁.interpret I) (t₂.interpret I)
```

`Cedar.Thm.interpret_term_app_set_inter` (theorem, [line 266](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L266))

```lean
public theorem interpret_term_app_set_inter {I : Interpretation} {t₁ t₂ : Term} {ty : TermType} :
  (Term.app Op.set.inter [t₁, t₂] ty).interpret I =
  Factory.set.inter (t₁.interpret I) (t₂.interpret I)
```

`Cedar.Thm.interpret_term_app_option_get` (theorem, [line 272](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L272))

```lean
public theorem interpret_term_app_option_get {I : Interpretation} {t₁ : Term} {ty : TermType} :
  (Term.app Op.option.get [t₁] ty).interpret I =
  Factory.option.get' I (t₁.interpret I)
```

`Cedar.Thm.interpret_term_app_record_get` (theorem, [line 278](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L278))

```lean
public theorem interpret_term_app_record_get {I : Interpretation} {a : Attr} {t₁ : Term} {ty : TermType} :
  (Term.app (Op.record.get a) [t₁] ty).interpret I =
  Factory.record.get (t₁.interpret I) a
```

`Cedar.Thm.interpret_term_app_string_like` (theorem, [line 284](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L284))

```lean
public theorem interpret_term_app_string_like {I : Interpretation} {p : Pattern} {t₁ : Term} {ty : TermType} :
  (Term.app (Op.string.like p) [t₁] ty).interpret I =
  Factory.string.like (t₁.interpret I) p
```

`Cedar.Thm.interpret_term_app_ext_decimal_val` (theorem, [line 290](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L290))

```lean
public theorem interpret_term_app_ext_decimal_val {I : Interpretation} {t₁ : Term} {ty : TermType} :
  (Term.app (.ext ExtOp.decimal.val) [t₁] ty).interpret I =
  Factory.ext.decimal.val (t₁.interpret I)
```

`Cedar.Thm.interpret_term_app_ext_ipaddr_isV4` (theorem, [line 296](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L296))

```lean
public theorem interpret_term_app_ext_ipaddr_isV4 {I : Interpretation} {t₁ : Term} {ty : TermType} :
  (Term.app (.ext ExtOp.ipaddr.isV4) [t₁] ty).interpret I =
  Factory.ext.ipaddr.isV4 (t₁.interpret I)
```

`Cedar.Thm.interpret_term_app_ext_ipaddr_addrV4` (theorem, [line 302](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L302))

```lean
public theorem interpret_term_app_ext_ipaddr_addrV4 {I : Interpretation} {t₁ : Term} {ty : TermType} :
  (Term.app (.ext ExtOp.ipaddr.addrV4) [t₁] ty).interpret I =
  Factory.ext.ipaddr.addrV4' I (t₁.interpret I)
```

`Cedar.Thm.interpret_term_app_ext_ipaddr_prefixV4` (theorem, [line 308](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L308))

```lean
public theorem interpret_term_app_ext_ipaddr_prefixV4 {I : Interpretation} {t₁ : Term} {ty : TermType} :
  (Term.app (.ext ExtOp.ipaddr.prefixV4) [t₁] ty).interpret I =
  Factory.ext.ipaddr.prefixV4' I (t₁.interpret I)
```

`Cedar.Thm.interpret_term_app_ext_ipaddr_addrV6` (theorem, [line 314](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L314))

```lean
public theorem interpret_term_app_ext_ipaddr_addrV6 {I : Interpretation} {t₁ : Term} {ty : TermType} :
  (Term.app (.ext ExtOp.ipaddr.addrV6) [t₁] ty).interpret I =
  Factory.ext.ipaddr.addrV6' I (t₁.interpret I)
```

`Cedar.Thm.interpret_term_app_ext_ipaddr_prefixV6` (theorem, [line 320](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L320))

```lean
public theorem interpret_term_app_ext_ipaddr_prefixV6 {I : Interpretation} {t₁ : Term} {ty : TermType} :
  (Term.app (.ext ExtOp.ipaddr.prefixV6) [t₁] ty).interpret I =
  Factory.ext.ipaddr.prefixV6' I (t₁.interpret I)
```

`Cedar.Thm.interpret_term_app_ext_datetime_val` (theorem, [line 326](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L326))

```lean
public theorem interpret_term_app_ext_datetime_val {I : Interpretation} {t₁ : Term} {ty : TermType} :
  (Term.app (.ext ExtOp.datetime.val) [t₁] ty).interpret I =
  Factory.ext.datetime.val (t₁.interpret I)
```

`Cedar.Thm.interpret_term_app_ext_datetime_ofBitVec` (theorem, [line 332](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L332))

```lean
public theorem interpret_term_app_ext_datetime_ofBitVec {I : Interpretation} {t₁ : Term} {ty : TermType} :
  (Term.app (.ext ExtOp.datetime.ofBitVec) [t₁] ty).interpret I =
  Factory.ext.datetime.ofBitVec (t₁.interpret I)
```

`Cedar.Thm.interpret_term_app_ext_duration_val` (theorem, [line 338](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L338))

```lean
public theorem interpret_term_app_ext_duration_val {I : Interpretation} {t₁ : Term} {ty : TermType} :
  (Term.app (.ext ExtOp.duration.val) [t₁] ty).interpret I =
  Factory.ext.duration.val (t₁.interpret I)
```

`Cedar.Thm.interpret_term_app_ext_duration_ofBitVec` (theorem, [line 344](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean#L344))

```lean
public theorem interpret_term_app_ext_duration_ofBitVec {I : Interpretation} {t₁ : Term} {ty : TermType} :
  (Term.app (.ext ExtOp.duration.ofBitVec) [t₁] ty).interpret I =
  Factory.ext.duration.ofBitVec (t₁.interpret I)
```

## Depends on

- [Interpretations](../../../../symcc/part-01/interpretation.md)

## Proof depends on

- [Map properties](../../../data/map.md)

## Sources

- [Cedar/Thm/SymCC/Term/Interpret/Basic.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Basic.lean)
- [Declaration ledger](../../../../../../sources/cedar/Cedar.Thm.SymCC.Term.Interpret.Basic.json)
