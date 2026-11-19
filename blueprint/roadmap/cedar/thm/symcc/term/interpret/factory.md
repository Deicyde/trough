---
catalog: module
lean: Cedar.Thm.interpret_not, Cedar.Thm.interpret_and, Cedar.Thm.interpret_or, Cedar.Thm.interpret_ite, Cedar.Thm.interpret_implies, Cedar.Thm.interpret_eq, Cedar.Thm.interpret_isNone, Cedar.Thm.interpret_isSome, Cedar.Thm.interpret_noneOf, Cedar.Thm.interpret_someOf, Cedar.Thm.interpret_option_get, Cedar.Thm.interpret_option_get', Cedar.Thm.map_interpret_option_get, Cedar.Thm.interpret_record_get, Cedar.Thm.interpret_app, Cedar.Thm.interpret_ifFalse, Cedar.Thm.interpret_ifTrue, Cedar.Thm.interpret_ifSome, Cedar.Thm.interpret_foldr_ifSome, Cedar.Thm.interpret_string_like, Cedar.Thm.interpret_bvnego, Cedar.Thm.interpret_bvneg, Cedar.Thm.interpret_bvslt, Cedar.Thm.interpret_bvsle, Cedar.Thm.interpret_bvule, Cedar.Thm.interpret_bvsaddo, Cedar.Thm.interpret_bvssubo, Cedar.Thm.interpret_bvsmulo, Cedar.Thm.interpret_bvadd, Cedar.Thm.interpret_bvsub, Cedar.Thm.interpret_bvmul, Cedar.Thm.interpret_bvsdiv, Cedar.Thm.interpret_bvudiv, Cedar.Thm.interpret_bvsrem, Cedar.Thm.interpret_bvsmod, Cedar.Thm.interpret_bvurem, Cedar.Thm.interpret_bvshl, Cedar.Thm.interpret_bvlshr, Cedar.Thm.interpret_bvaddChecked, Cedar.Thm.interpret_bvsubChecked, Cedar.Thm.interpret_bvmulChecked, Cedar.Thm.interpret_zero_extend, Cedar.Thm.interpret_set_member, Cedar.Thm.interpret_set_subset, Cedar.Thm.interpret_set_inter, Cedar.Thm.interpret_set_isEmpty, Cedar.Thm.interpret_set_intersects, Cedar.Thm.interpret_anyTrue, Cedar.Thm.interpret_anyNone, Cedar.Thm.interpret_ifAllSome, Cedar.Thm.interpret_setOf, Cedar.Thm.interpret_recordOf, Cedar.Thm.interpret_ext_decimal_val, Cedar.Thm.interpret_ext_ipaddr_isV4, Cedar.Thm.interpret_ext_ipaddr_addrV4, Cedar.Thm.interpret_ext_ipaddr_prefixV4, Cedar.Thm.interpret_ext_ipaddr_addrV6, Cedar.Thm.interpret_ext_ipaddr_prefixV6, Cedar.Thm.interpret_ext_datetime_val, Cedar.Thm.interpret_ext_datetime_ofBitVec, Cedar.Thm.interpret_ext_duration_val, Cedar.Thm.interpret_ext_duration_ofBitVec, Cedar.Thm.interpret_tagOf
statement: formalized
proof: formalized
---

# Interpretation of Factory functions

`Cedar.Thm.SymCC.Term.Interpret.Factory`, in [Cedar/Thm/SymCC/Term/Interpret/Factory.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean).

> This file basic lemmas about the interpretation of Factory functions.
> -

`Cedar.Thm.interpret_not` (theorem, [line 41](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L41))

```lean
public theorem interpret_not {I : Interpretation} {t : Term} :
  I.WellFormed εs → t.WellFormed εs →
  (Factory.not t).interpret I = Factory.not (t.interpret I)
```

`Cedar.Thm.interpret_and` (theorem, [line 82](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L82))

```lean
public theorem interpret_and {εs : SymEntities} {I : Interpretation} {t₁ t₂ : Term} :
  I.WellFormed εs → t₁.WellFormed εs → t₂.WellFormed εs →
  t₁.typeOf = .bool → t₂.typeOf = .bool →
  (Factory.and t₁ t₂).interpret I = Factory.and (t₁.interpret I) (t₂.interpret I)
```

`Cedar.Thm.interpret_or` (theorem, [line 128](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L128))

```lean
public theorem interpret_or {εs : SymEntities} {I : Interpretation} {t₁ t₂ : Term} :
  I.WellFormed εs → t₁.WellFormed εs → t₂.WellFormed εs →
  t₁.typeOf = .bool → t₂.typeOf = .bool →
  (Factory.or t₁ t₂).interpret I = Factory.or (t₁.interpret I) (t₂.interpret I)
```

`Cedar.Thm.interpret_ite` (theorem, [line 209](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L209))

```lean
public theorem interpret_ite {εs : SymEntities} {I : Interpretation} {t₁ t₂ t₃ : Term} :
  I.WellFormed εs → t₁.WellFormed εs →
  t₂.WellFormed εs → t₃.WellFormed εs →
  t₁.typeOf = .bool → t₂.typeOf = t₃.typeOf →
  (Factory.ite t₁ t₂ t₃).interpret I =
  Factory.ite (t₁.interpret I) (t₂.interpret I) (t₃.interpret I)
```

`Cedar.Thm.interpret_implies` (theorem, [line 237](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L237))

```lean
public theorem interpret_implies {I : Interpretation} {t₁ t₂ : Term} :
  I.WellFormed εs → t₁.WellFormed εs → t₂.WellFormed εs →
  t₁.typeOf = .bool → t₂.typeOf = .bool →
  (Factory.implies t₁ t₂).interpret I = Factory.implies (t₁.interpret I) (t₂.interpret I)
```

`Cedar.Thm.interpret_eq` (theorem, [line 322](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L322))

```lean
public theorem interpret_eq {I : Interpretation} {t₁ t₂ : Term} :
  I.WellFormed εs → t₁.WellFormed εs → t₂.WellFormed εs →
  (Factory.eq t₁ t₂).interpret I = Factory.eq (t₁.interpret I) (t₂.interpret I)
```

`Cedar.Thm.interpret_isNone` (theorem, [line 350](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L350))

```lean
public theorem interpret_isNone {I : Interpretation} {t : Term} :
  I.WellFormed εs → t.WellFormed εs →
  (isNone t).interpret I = isNone (t.interpret I)
```

`Cedar.Thm.interpret_isSome` (theorem, [line 404](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L404))

```lean
public theorem interpret_isSome {I : Interpretation} {t : Term} :
  I.WellFormed εs → t.WellFormed εs →
  (isSome t).interpret I = isSome (t.interpret I)
```

`Cedar.Thm.interpret_noneOf` (theorem, [line 412](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L412))

```lean
public theorem interpret_noneOf {I : Interpretation} {ty : TermType} :
  (noneOf ty).interpret I = Term.none ty
```

`Cedar.Thm.interpret_someOf` (theorem, [line 416](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L416))

```lean
public theorem interpret_someOf {I : Interpretation} {t : Term} :
  (someOf t).interpret I = Term.some (t.interpret I)
```

`Cedar.Thm.interpret_option_get` (theorem, [line 420](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L420))

```lean
public theorem interpret_option_get {εs : SymEntities} (I : Interpretation) {t : Term} {ty : TermType} :
  t.WellFormed εs → t.typeOf = .option ty →
  (Factory.option.get t).interpret I = Factory.option.get' I (t.interpret I)
```

`Cedar.Thm.interpret_option_get'` (theorem, [line 436](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L436))

```lean
public theorem interpret_option_get' {εs : SymEntities} {I : Interpretation} {t : Term} {ty : TermType} :
  I.WellFormed εs → t.WellFormed εs → t.typeOf = .option ty →
  (Factory.option.get' I t).interpret I = Factory.option.get' I (t.interpret I)
```

`Cedar.Thm.map_interpret_option_get` (theorem, [line 450](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L450))

> `map (interpret ∘ option.get)` commutes with `map (option.get' ∘ interpret)`.

```lean
public theorem map_interpret_option_get {εs : SymEntities} {I : Interpretation} {ty : TermType} {ts : List Term}
  (hts : ∀ t ∈ ts, t.WellFormed εs ∧ t.typeOf = .option ty) :
  (ts.map option.get).map (Term.interpret I) = (ts.map (Term.interpret I)).map (option.get' I)
```

`Cedar.Thm.interpret_record_get` (theorem, [line 461](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L461))

```lean
public theorem interpret_record_get {εs : SymEntities} (I : Interpretation) {t : Term} {a : Attr} {rty : Map Attr TermType} {ty : TermType} :
  t.WellFormed εs → t.typeOf = .record rty → rty.find? a = .some ty →
  (Factory.record.get t a).interpret I = Factory.record.get (t.interpret I) a
```

`Cedar.Thm.interpret_app` (theorem, [line 564](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L564))

```lean
public theorem interpret_app {εs : SymEntities} {I : Interpretation} {t : Term} {f : UnaryFunction} :
  I.WellFormed εs → t.WellFormed εs → f.WellFormed εs → t.typeOf = f.argType →
  (Factory.app f t).interpret I = Factory.app (f.interpret I) (t.interpret I)
```

`Cedar.Thm.interpret_ifFalse` (theorem, [line 591](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L591))

```lean
public theorem interpret_ifFalse {εs : SymEntities} {I : Interpretation} {g t : Term} :
  I.WellFormed εs → g.WellFormed εs → g.typeOf = .bool → t.WellFormed εs →
  (ifFalse g t).interpret I = ifFalse (g.interpret I) (t.interpret I)
```

`Cedar.Thm.interpret_ifTrue` (theorem, [line 601](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L601))

```lean
public theorem interpret_ifTrue {εs : SymEntities} {I : Interpretation} {g t : Term} :
  I.WellFormed εs → g.WellFormed εs → g.typeOf = .bool → t.WellFormed εs →
  (ifTrue g t).interpret I = ifTrue (g.interpret I) (t.interpret I)
```

`Cedar.Thm.interpret_ifSome` (theorem, [line 611](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L611))

```lean
public theorem interpret_ifSome {εs : SymEntities} {I : Interpretation} {g t : Term} :
  I.WellFormed εs → g.WellFormed εs → t.WellFormed εs →
  (ifSome g t).interpret I = ifSome (g.interpret I) (t.interpret I)
```

`Cedar.Thm.interpret_foldr_ifSome` (theorem, [line 641](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L641))

> Push `interpret` through a `foldr ifSome` over well-formed guards.

```lean
public theorem interpret_foldr_ifSome {εs : SymEntities} {I : Interpretation} {ty : TermType} {P : Term}
  (hI : I.WellFormed εs)
  (hP : P.WellFormed εs) (hPty : P.typeOf = .option ty) :
  ∀ (ts : List Term), (∀ t ∈ ts, t.WellFormed εs) →
  (ts.foldr (fun tᵢ acc => ifSome tᵢ acc) P).interpret I =
  (ts.map (Term.interpret I)).foldr (fun tᵢ acc => ifSome tᵢ acc) (P.interpret I)
```

`Cedar.Thm.interpret_string_like` (theorem, [line 669](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L669))

```lean
public theorem interpret_string_like {εs : SymEntities} {I : Interpretation} {t : Term} {p : Pattern} :
  I.WellFormed εs → t.WellFormed εs → t.typeOf = .string →
  (Factory.string.like t p).interpret I = Factory.string.like (t.interpret I) p
```

`Cedar.Thm.interpret_bvnego` (theorem, [line 674](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L674))

```lean
public theorem interpret_bvnego {εs : SymEntities} {I : Interpretation} {t : Term} {n : Nat} :
  I.WellFormed εs → t.WellFormed εs → t.typeOf = .bitvec n →
  (Factory.bvnego t).interpret I = Factory.bvnego (t.interpret I)
```

`Cedar.Thm.interpret_bvneg` (theorem, [line 700](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L700))

```lean
public theorem interpret_bvneg {εs : SymEntities} {I : Interpretation} {t : Term} {n : Nat} :
  I.WellFormed εs → t.WellFormed εs → t.typeOf = .bitvec n →
  (Factory.bvneg t).interpret I = Factory.bvneg (t.interpret I)
```

`Cedar.Thm.interpret_bvslt` (theorem, [line 729](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L729))

```lean
public theorem interpret_bvslt {I : Interpretation} {t₁ t₂ : Term} :
  (Factory.bvslt t₁ t₂).interpret I = Factory.bvslt (t₁.interpret I) (t₂.interpret I)
```

`Cedar.Thm.interpret_bvsle` (theorem, [line 733](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L733))

```lean
public theorem interpret_bvsle {I : Interpretation} {t₁ t₂ : Term}  :
  (Factory.bvsle t₁ t₂).interpret I = Factory.bvsle (t₁.interpret I) (t₂.interpret I)
```

`Cedar.Thm.interpret_bvule` (theorem, [line 737](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L737))

```lean
public theorem interpret_bvule {I : Interpretation} {t₁ t₂ : Term}  :
  (Factory.bvule t₁ t₂).interpret I = Factory.bvule (t₁.interpret I) (t₂.interpret I)
```

`Cedar.Thm.interpret_bvsaddo` (theorem, [line 741](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L741))

```lean
public theorem interpret_bvsaddo {I : Interpretation} {t₁ t₂ : Term} :
  (Factory.bvsaddo t₁ t₂).interpret I = Factory.bvsaddo (t₁.interpret I) (t₂.interpret I)
```

`Cedar.Thm.interpret_bvssubo` (theorem, [line 745](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L745))

```lean
public theorem interpret_bvssubo {I : Interpretation} {t₁ t₂ : Term} :
  (Factory.bvssubo t₁ t₂).interpret I = Factory.bvssubo (t₁.interpret I) (t₂.interpret I)
```

`Cedar.Thm.interpret_bvsmulo` (theorem, [line 749](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L749))

```lean
public theorem interpret_bvsmulo {I : Interpretation} {t₁ t₂ : Term} :
  (Factory.bvsmulo t₁ t₂).interpret I = Factory.bvsmulo (t₁.interpret I) (t₂.interpret I)
```

`Cedar.Thm.interpret_bvadd` (theorem, [line 753](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L753))

```lean
public theorem interpret_bvadd {I : Interpretation} {t₁ t₂ : Term} :
  (Factory.bvadd t₁ t₂).interpret I = Factory.bvadd (t₁.interpret I) (t₂.interpret I)
```

`Cedar.Thm.interpret_bvsub` (theorem, [line 757](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L757))

```lean
public theorem interpret_bvsub {I : Interpretation} {t₁ t₂ : Term} :
  (Factory.bvsub t₁ t₂).interpret I = Factory.bvsub (t₁.interpret I) (t₂.interpret I)
```

`Cedar.Thm.interpret_bvmul` (theorem, [line 761](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L761))

```lean
public theorem interpret_bvmul {I : Interpretation} {t₁ t₂ : Term} :
  (Factory.bvmul t₁ t₂).interpret I = Factory.bvmul (t₁.interpret I) (t₂.interpret I)
```

`Cedar.Thm.interpret_bvsdiv` (theorem, [line 765](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L765))

```lean
public theorem interpret_bvsdiv {I : Interpretation} {t₁ t₂ : Term} :
  (Factory.bvsdiv t₁ t₂).interpret I = Factory.bvsdiv (t₁.interpret I) (t₂.interpret I)
```

`Cedar.Thm.interpret_bvudiv` (theorem, [line 769](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L769))

```lean
public theorem interpret_bvudiv {I : Interpretation} {t₁ t₂ : Term} :
  (Factory.bvudiv t₁ t₂).interpret I = Factory.bvudiv (t₁.interpret I) (t₂.interpret I)
```

`Cedar.Thm.interpret_bvsrem` (theorem, [line 773](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L773))

```lean
public theorem interpret_bvsrem {I : Interpretation} {t₁ t₂ : Term} :
  (Factory.bvsrem t₁ t₂).interpret I = Factory.bvsrem (t₁.interpret I) (t₂.interpret I)
```

`Cedar.Thm.interpret_bvsmod` (theorem, [line 777](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L777))

```lean
public theorem interpret_bvsmod {I : Interpretation} {t₁ t₂ : Term} :
  (Factory.bvsmod t₁ t₂).interpret I = Factory.bvsmod (t₁.interpret I) (t₂.interpret I)
```

`Cedar.Thm.interpret_bvurem` (theorem, [line 781](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L781))

```lean
public theorem interpret_bvurem {I : Interpretation} {t₁ t₂ : Term} :
  (Factory.bvurem t₁ t₂).interpret I = Factory.bvurem (t₁.interpret I) (t₂.interpret I)
```

`Cedar.Thm.interpret_bvshl` (theorem, [line 785](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L785))

```lean
public theorem interpret_bvshl {I : Interpretation} {t₁ t₂ : Term} :
  (Factory.bvshl t₁ t₂).interpret I = Factory.bvshl (t₁.interpret I) (t₂.interpret I)
```

`Cedar.Thm.interpret_bvlshr` (theorem, [line 789](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L789))

```lean
public theorem interpret_bvlshr {I : Interpretation} {t₁ t₂ : Term} :
  (Factory.bvlshr t₁ t₂).interpret I = Factory.bvlshr (t₁.interpret I) (t₂.interpret I)
```

`Cedar.Thm.interpret_bvaddChecked` (theorem, [line 801](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L801))

```lean
public theorem interpret_bvaddChecked {εs : SymEntities} {I : Interpretation} {t₁ t₂ : Term} {n : Nat}
  (hI : I.WellFormed εs)
  (hwf₁ : t₁.WellFormed εs) (hwf₂ : t₂.WellFormed εs)
  (hty₁ : t₁.typeOf = .bitvec n)
  (hty₂ : t₂.typeOf = .bitvec n) :
  (Factory.bvaddChecked t₁  t₂).interpret I = Factory.bvaddChecked (t₁.interpret I) (t₂.interpret I)
```

`Cedar.Thm.interpret_bvsubChecked` (theorem, [line 810](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L810))

```lean
public theorem interpret_bvsubChecked {εs : SymEntities} {I : Interpretation} {t₁ t₂ : Term} {n : Nat}
  (hI : I.WellFormed εs)
  (hwf₁ : t₁.WellFormed εs) (hwf₂ : t₂.WellFormed εs)
  (hty₁ : t₁.typeOf = .bitvec n)
  (hty₂ : t₂.typeOf = .bitvec n) :
  (Factory.bvsubChecked t₁  t₂).interpret I = Factory.bvsubChecked (t₁.interpret I) (t₂.interpret I)
```

`Cedar.Thm.interpret_bvmulChecked` (theorem, [line 819](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L819))

```lean
public theorem interpret_bvmulChecked {εs : SymEntities} {I : Interpretation} {t₁ t₂ : Term} {n : Nat}
  (hI : I.WellFormed εs)
  (hwf₁ : t₁.WellFormed εs) (hwf₂ : t₂.WellFormed εs)
  (hty₁ : t₁.typeOf = .bitvec n)
  (hty₂ : t₂.typeOf = .bitvec n) :
  (Factory.bvmulChecked t₁  t₂).interpret I = Factory.bvmulChecked (t₁.interpret I) (t₂.interpret I)
```

`Cedar.Thm.interpret_zero_extend` (theorem, [line 828](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L828))

```lean
public theorem interpret_zero_extend {εs : SymEntities} {I : Interpretation} {n : Nat} {t : Term} :
  I.WellFormed εs → t.WellFormed εs →
  (Factory.zero_extend n t).interpret I = Factory.zero_extend n (t.interpret I)
```

`Cedar.Thm.interpret_set_member` (theorem, [line 851](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L851))

```lean
public theorem interpret_set_member {εs : SymEntities} {I : Interpretation} {t₁ t₂ : Term} :
  t₁.WellFormed εs → t₂.WellFormed εs →
  Term.interpret I (set.member t₁ t₂) = set.member (Term.interpret I t₁) (Term.interpret I t₂)
```

`Cedar.Thm.interpret_set_subset` (theorem, [line 872](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L872))

```lean
public theorem interpret_set_subset  {εs : SymEntities} {I : Interpretation} {t₁ t₂ : Term} :
  t₁.WellFormed εs → t₂.WellFormed εs →
  Term.interpret I (set.subset t₁ t₂) = set.subset (Term.interpret I t₁) (Term.interpret I t₂)
```

`Cedar.Thm.interpret_set_inter` (theorem, [line 897](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L897))

```lean
public theorem interpret_set_inter  {εs : SymEntities} {I : Interpretation} {t₁ t₂ : Term} {ty : TermType} :
  I.WellFormed εs → t₁.WellFormed εs → t₂.WellFormed εs →
  t₁.typeOf = .set ty → t₂.typeOf = .set ty →
  Term.interpret I (set.inter t₁ t₂) = set.inter (Term.interpret I t₁) (Term.interpret I t₂)
```

`Cedar.Thm.interpret_set_isEmpty` (theorem, [line 956](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L956))

```lean
public theorem interpret_set_isEmpty {εs : SymEntities} {t : Term} {ty : TermType} :
  I.WellFormed εs → t.WellFormed εs → t.typeOf = .set ty →
  (set.isEmpty t).interpret I = set.isEmpty (t.interpret I)
```

`Cedar.Thm.interpret_set_intersects` (theorem, [line 986](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L986))

```lean
public theorem interpret_set_intersects {εs : SymEntities} {I : Interpretation} {t₁ t₂ : Term} {ty : TermType} :
  I.WellFormed εs → t₁.WellFormed εs → t₂.WellFormed εs →
  t₁.typeOf = .set ty → t₂.typeOf = .set ty →
  Term.interpret I (set.intersects t₁ t₂) = set.intersects (Term.interpret I t₁) (Term.interpret I t₂)
```

`Cedar.Thm.interpret_anyTrue` (theorem, [line 1029](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L1029))

```lean
public theorem interpret_anyTrue {εs : SymEntities} {I : Interpretation} {ts : List Term} {f : Term → Term} :
  I.WellFormed εs →
  (∀ t ∈ ts, (f t).WellFormed εs ∧ (f t).typeOf = .bool) →
  (∀ t ∈ ts, (f t).interpret I = f (t.interpret I)) →
  (anyTrue f ts).interpret I = anyTrue f (ts.map (Term.interpret I))
```

`Cedar.Thm.interpret_anyNone` (theorem, [line 1040](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L1040))

```lean
public theorem interpret_anyNone {εs : SymEntities} {I : Interpretation} {gs : List Term} :
  I.WellFormed εs →
  (∀ g ∈ gs, g.WellFormed εs) →
  (anyNone gs).interpret I = anyNone (gs.map (Term.interpret I))
```

`Cedar.Thm.interpret_ifAllSome` (theorem, [line 1053](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L1053))

```lean
public theorem interpret_ifAllSome {εs : SymEntities} {I : Interpretation} {gs : List Term} {t : Term} :
  I.WellFormed εs →
  (∀ g ∈ gs, g.WellFormed εs) →
  t.WellFormed εs →
  t.typeOf = .option ty →
  (ifAllSome gs t).interpret I = ifAllSome (gs.map (Term.interpret I)) (t.interpret I)
```

`Cedar.Thm.interpret_setOf` (theorem, [line 1071](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L1071))

```lean
public theorem interpret_setOf {I : Interpretation} {ts : List Term} {ty : TermType} :
  (setOf ts ty).interpret I = setOf (ts.map (Term.interpret I)) ty
```

`Cedar.Thm.interpret_recordOf` (theorem, [line 1075](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L1075))

```lean
public theorem interpret_recordOf {I : Interpretation} {ats : List (Attr × Term)} :
  (recordOf ats).interpret I = recordOf (ats.map (Prod.map id (Term.interpret I)))
```

`Cedar.Thm.interpret_ext_decimal_val` (theorem, [line 1079](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L1079))

```lean
public theorem interpret_ext_decimal_val {I : Interpretation} {t : Term} :
  Term.interpret I (ext.decimal.val t) = ext.decimal.val (t.interpret I)
```

`Cedar.Thm.interpret_ext_ipaddr_isV4` (theorem, [line 1093](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L1093))

```lean
public theorem interpret_ext_ipaddr_isV4 {I : Interpretation} {t : Term} :
  (ext.ipaddr.isV4 t).interpret I  = ext.ipaddr.isV4 (t.interpret I)
```

`Cedar.Thm.interpret_ext_ipaddr_addrV4` (theorem, [line 1100](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L1100))

```lean
public theorem interpret_ext_ipaddr_addrV4 {I : Interpretation} {t : Term} :
  (ext.ipaddr.addrV4 t).interpret I = ext.ipaddr.addrV4' I (t.interpret I)
```

`Cedar.Thm.interpret_ext_ipaddr_prefixV4` (theorem, [line 1108](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L1108))

```lean
public theorem interpret_ext_ipaddr_prefixV4 {I : Interpretation} {t : Term} :
  (ext.ipaddr.prefixV4 t).interpret I = ext.ipaddr.prefixV4' I (t.interpret I)
```

`Cedar.Thm.interpret_ext_ipaddr_addrV6` (theorem, [line 1119](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L1119))

```lean
public theorem interpret_ext_ipaddr_addrV6 {I : Interpretation} {t : Term} :
  (ext.ipaddr.addrV6 t).interpret I = ext.ipaddr.addrV6' I (t.interpret I)
```

`Cedar.Thm.interpret_ext_ipaddr_prefixV6` (theorem, [line 1127](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L1127))

```lean
public theorem interpret_ext_ipaddr_prefixV6 {I : Interpretation} {t : Term} :
  (ext.ipaddr.prefixV6 t).interpret I = ext.ipaddr.prefixV6' I (t.interpret I)
```

`Cedar.Thm.interpret_ext_datetime_val` (theorem, [line 1138](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L1138))

```lean
public theorem interpret_ext_datetime_val {I : Interpretation} {t : Term} :
  Term.interpret I (ext.datetime.val t) = ext.datetime.val (t.interpret I)
```

`Cedar.Thm.interpret_ext_datetime_ofBitVec` (theorem, [line 1152](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L1152))

```lean
public theorem interpret_ext_datetime_ofBitVec {I : Interpretation} {t : Term} :
  Term.interpret I (ext.datetime.ofBitVec t) = ext.datetime.ofBitVec (t.interpret I)
```

`Cedar.Thm.interpret_ext_duration_val` (theorem, [line 1166](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L1166))

```lean
public theorem interpret_ext_duration_val {I : Interpretation} {t : Term} :
  Term.interpret I (ext.duration.val t) = ext.duration.val (t.interpret I)
```

`Cedar.Thm.interpret_ext_duration_ofBitVec` (theorem, [line 1180](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L1180))

```lean
public theorem interpret_ext_duration_ofBitVec {I : Interpretation} {t : Term} :
  Term.interpret I (ext.duration.ofBitVec t) = ext.duration.ofBitVec (t.interpret I)
```

`Cedar.Thm.interpret_tagOf` (theorem, [line 1194](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean#L1194))

```lean
public theorem interpret_tagOf {I : Interpretation} {t₁ t₂ : Term} :
  (tagOf t₁ t₂).interpret I = tagOf (t₁.interpret I) (t₂.interpret I)
```

## Depends on

- [Well-formedness and interpretations](../../data/basic.md)

## Proof depends on

- [Interpretation preserves well-formedness of Terms (Lit)](lit.md)

## Sources

- [Cedar/Thm/SymCC/Term/Interpret/Factory.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Factory.lean)
- [Declaration ledger](../../../../../../sources/cedar/Cedar.Thm.SymCC.Term.Interpret.Factory.json)
