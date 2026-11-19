---
catalog: module
lean: Cedar.Thm.same_results_implies_exists_outcome, Cedar.Thm.same_outcomes_implies_eq, Cedar.Thm.same_error_implies, Cedar.Thm.same_error_implies_ifSome_error, Cedar.Thm.same_error_implies_ifAllSome_error, Cedar.Thm.same_error_implied_by, Cedar.Thm.same_error_foldr_ifSome, Cedar.Thm.same_ok_implies, Cedar.Thm.same_ok_some_implies, Cedar.Thm.same_ok_some_iff, Cedar.Thm.same_some_implies_ok, Cedar.Thm.same_values_def, Cedar.Thm.same_value_implies_same, Cedar.Thm.same_implies_same_value, Cedar.Thm.same_value_implies_lit, Cedar.Thm.same_ok_value_implies_lit, Cedar.Thm.same_bool_term_implies, Cedar.Thm.same_ok_bool_term_implies, Cedar.Thm.same_bool_implies, Cedar.Thm.same_ok_bool_implies, Cedar.Thm.same_bool, Cedar.Thm.same_ok_bool, Cedar.Thm.same_ok_bool_iff, Cedar.Thm.same_set_term_implies, Cedar.Thm.same_set_implies, Cedar.Thm.same_record_term_implies, Cedar.Thm.same_record_implies, Cedar.Thm.value?_bool, Cedar.Thm.value?_entity, Cedar.Thm.same_entity_term_implies, Cedar.Thm.same_entity_implies, Cedar.Thm.same_string_term_implies, Cedar.Thm.same_string_implies, Cedar.Thm.same_bitvec_term_implies, Cedar.Thm.same_bitvec64_term_implies, Cedar.Thm.same_int_implies, Cedar.Thm.same_int, Cedar.Thm.same_bv, Cedar.Thm.same_int64, Cedar.Thm.same_ext, Cedar.Thm.same_ext_term_implies, Cedar.Thm.same_ext_implies, Cedar.Thm.value?_some_implies_attrValue?_some, Cedar.Thm.value?_attrValue?_none_implies_none, Cedar.Thm.value?_attrValue?_some_implies_same, Cedar.Thm.value?_attrValue?_fst, Cedar.Thm.record_value?_mapM', Cedar.Thm.record_value_find?, Cedar.Thm.record_value?_find?_required, Cedar.Thm.record_value?_find?_optional_some, Cedar.Thm.record_value?_find?_optional_none, Cedar.Thm.record_value?_find?_none, Cedar.Thm.same_prim_value_inj, Cedar.Thm.set_value?_implies_in_value, Cedar.Thm.set_value?_implies_in_term, Cedar.Thm.record_value?_some_implies, Cedar.Thm.record_value?_some_implied_by, Cedar.Thm.record_value?_cons, Cedar.Thm.record_value?_head_none, Cedar.Thm.same_value_inj, Cedar.Thm.term_value?_exists
statement: formalized
proof: formalized
---

# Properties of the `Same` predicate on Terms

`Cedar.Thm.SymCC.Term.Same`, in [Cedar/Thm/SymCC/Term/Same.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean).

> This file contains lemmas about the `Same` predicate on Terms.

`Cedar.Thm.same_results_implies_exists_outcome` (theorem, [line 40](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L40))

```lean
public theorem same_results_implies_exists_outcome {res : Spec.Result Value} {t : Term} :
  res ∼ t → ∃ (o : Outcome Value), res ∼ o ∧ o ∼ t
```

`Cedar.Thm.same_outcomes_implies_eq` (theorem, [line 49](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L49))

```lean
public theorem same_outcomes_implies_eq {o₁ o₂ : Outcome Value} {t : Term} :
  o₁ ∼ t → o₂ ∼ t → o₁ = o₂
```

`Cedar.Thm.same_error_implies` (theorem, [line 66](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L66))

```lean
public theorem same_error_implies {e : Spec.Error} {t : Term} :
  (Except.error e : Spec.Result Value) ∼ t →
  (¬ e = .entityDoesNotExist) ∧
  (∃ ty, t = Term.none ty)
```

`Cedar.Thm.same_error_implies_ifSome_error` (theorem, [line 79](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L79))

```lean
public theorem same_error_implies_ifSome_error {e : Spec.Error} {t₁ t₂ : Term} {ty₂ : TermType} :
  (Except.error e : Spec.Result Value) ∼ t₁ →
  t₂.typeOf = .option ty₂ →
  (Except.error e : Spec.Result Value) ∼ ifSome t₁ t₂
```

`Cedar.Thm.same_error_implies_ifAllSome_error` (theorem, [line 91](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L91))

```lean
public theorem same_error_implies_ifAllSome_error {e : Spec.Error} {ts : List Term} {t₁ t₂ : Term} {ty₂ : TermType} :
  (Except.error e : Spec.Result Value) ∼ t₁ →
  t₁ ∈ ts →
  t₂.typeOf = .option ty₂ →
  (Except.error e : Spec.Result Value) ∼ ifAllSome ts t₂
```

`Cedar.Thm.same_error_implied_by` (theorem, [line 103](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L103))

```lean
public theorem same_error_implied_by {e : Spec.Error} {ty : TermType} :
  ¬e = Error.entityDoesNotExist →
  (Except.error e : Spec.Result Value) ∼ Term.none ty
```

`Cedar.Thm.same_error_foldr_ifSome` (theorem, [line 113](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L113))

> If some guard in the list corresponds to an errored evaluation (so it is a `none`),
> the whole `ifSome` fold reduces to that error.

```lean
public theorem same_error_foldr_ifSome {e : Spec.Error} {ts : List Term} {P : Term} {ty : TermType} {tⱼ : Term}
  (hP : P.typeOf = .option ty)
  (hj : tⱼ ∈ ts)
  (hsame : (Except.error e : Spec.Result Value) ∼ tⱼ) :
  (Except.error e : Spec.Result Value) ∼ ts.foldr (fun tᵢ acc => ifSome tᵢ acc) P
```

`Cedar.Thm.same_ok_implies` (theorem, [line 131](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L131))

```lean
public theorem same_ok_implies {v : Value} {t : Term} :
  (Except.ok v : Spec.Result Value) ∼ t →
  ∃ t', t = .some t' ∧ v ∼ t'
```

`Cedar.Thm.same_ok_some_implies` (theorem, [line 143](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L143))

```lean
public theorem same_ok_some_implies {v : Value} {t : Term} :
  (Except.ok v : Spec.Result Value) ∼ (Term.some t) → v ∼ t
```

`Cedar.Thm.same_ok_some_iff` (theorem, [line 152](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L152))

```lean
public theorem same_ok_some_iff {v : Value} {t : Term} :
  (Except.ok v : Spec.Result Value) ∼ (Term.some t) ↔ v ∼ t
```

`Cedar.Thm.same_some_implies_ok` (theorem, [line 161](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L161))

```lean
public theorem same_some_implies_ok {r : Spec.Result Value} {t : Term} :
  r ∼ (Term.some t) →
  ∃ v, r = .ok v ∧ v ∼ t
```

`Cedar.Thm.same_values_def` (theorem, [line 173](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L173))

```lean
public theorem same_values_def {v : Value} {t : Term} :
  v ∼ t ↔ t.value? = .some v
```

`Cedar.Thm.same_value_implies_same` (theorem, [line 177](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L177))

```lean
public theorem same_value_implies_same {v : Value} {t : Term} :
  SameValues v t → v ∼ t
```

`Cedar.Thm.same_implies_same_value` (theorem, [line 183](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L183))

```lean
public theorem same_implies_same_value {v : Value} {t : Term} :
  v ∼ t → SameValues v t
```

`Cedar.Thm.same_value_implies_lit` (theorem, [line 187](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L187))

```lean
public theorem same_value_implies_lit {v : Value} {t : Term} :
  v ∼ t → t.isLiteral
```

`Cedar.Thm.same_ok_value_implies_lit` (theorem, [line 233](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L233))

```lean
public theorem same_ok_value_implies_lit {v : Value} {t : Term} :
  (Except.ok v : Spec.Result Value) ∼ t → t.isLiteral
```

`Cedar.Thm.same_bool_term_implies` (theorem, [line 244](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L244))

```lean
public theorem same_bool_term_implies {v : Value} {b : Bool} :
  v ∼ (Term.prim (TermPrim.bool b)) →
  v = .prim (.bool b)
```

`Cedar.Thm.same_ok_bool_term_implies` (theorem, [line 252](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L252))

```lean
public theorem same_ok_bool_term_implies {v : Value} {b : Bool} :
  (Except.ok v : Spec.Result Value) ∼ (Term.some (Term.prim (TermPrim.bool b))) →
  v = .prim (.bool b)
```

`Cedar.Thm.same_bool_implies` (theorem, [line 277](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L277))

```lean
public theorem same_bool_implies {b : Bool} {t : Term} :
  Value.prim (Prim.bool b) ∼ t →
  t = .prim (.bool b)
```

`Cedar.Thm.same_ok_bool_implies` (theorem, [line 282](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L282))

```lean
public theorem same_ok_bool_implies {b : Bool} {t : Term} :
  (Except.ok (Value.prim (Prim.bool b)) : Spec.Result Value) ∼ t →
  t = .some (.prim (.bool b))
```

`Cedar.Thm.same_bool` (theorem, [line 292](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L292))

```lean
public theorem same_bool {b : Bool} :
  Value.prim (Prim.bool b) ∼ Term.prim (TermPrim.bool b)
```

`Cedar.Thm.same_ok_bool` (theorem, [line 297](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L297))

```lean
public theorem same_ok_bool {b : Bool} :
  (Except.ok (Value.prim (Prim.bool b)) : Spec.Result Value) ∼ Term.some (Term.prim (TermPrim.bool b))
```

`Cedar.Thm.same_ok_bool_iff` (theorem, [line 302](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L302))

```lean
public theorem same_ok_bool_iff {b₁ b₂ : Bool} :
  b₁ = b₂ ↔
  (Except.ok (Value.prim (Prim.bool b₁)) : Spec.Result Value) ∼ Term.some (Term.prim (TermPrim.bool b₂))
```

`Cedar.Thm.same_set_term_implies` (theorem, [line 315](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L315))

```lean
public theorem same_set_term_implies {v : Value} {ts : Set Term} {ty : TermType} :
  v ∼ (Term.set ts ty) →
  ∃ vs, v = .set vs ∧ (Term.set ts ty).value? = vs
```

`Cedar.Thm.same_set_implies` (theorem, [line 329](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L329))

```lean
public theorem same_set_implies {vs : Set Value} {t : Term} {ty : TermType} :
  (Value.set vs) ∼ t → t.typeOf = .set ty →
  ∃ ts, t = .set ts ty ∧ (Term.set ts ty).value? = vs
```

`Cedar.Thm.same_record_term_implies` (theorem, [line 354](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L354))

```lean
public theorem same_record_term_implies {v : Value} {rt : Map Attr Term} :
  SameValues v (Term.record rt) →
  ∃ rv, v = .record rv ∧ (Term.record rt).value? = rv
```

`Cedar.Thm.same_record_implies` (theorem, [line 367](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L367))

```lean
public theorem same_record_implies {avs : Map Attr Value} {t : Term} {rty : Map Attr TermType} :
  (Value.record avs) ∼ t → t.typeOf = .record rty →
  ∃ ats, t = .record ats ∧ (Term.record ats).value? = Value.record avs
```

`Cedar.Thm.value?_bool` (theorem, [line 389](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L389))

```lean
public theorem value?_bool {b : Bool} :
  (Term.prim (.bool b)).value? = some (Value.prim (.bool b))
```

`Cedar.Thm.value?_entity` (theorem, [line 394](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L394))

```lean
public theorem value?_entity {uid : EntityUID} :
  (Term.prim (TermPrim.entity uid)).value? = some (Value.prim (.entityUID uid))
```

`Cedar.Thm.same_entity_term_implies` (theorem, [line 398](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L398))

```lean
public theorem same_entity_term_implies {v : Value} {uid : EntityUID} :
  v ∼ Term.prim (TermPrim.entity uid) → v = Value.prim (.entityUID uid)
```

`Cedar.Thm.same_entity_implies` (theorem, [line 405](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L405))

```lean
public theorem same_entity_implies {uid : EntityUID} {t : Term} :
  Value.prim (Prim.entityUID uid) ∼ t →
  t = .prim (.entity uid)
```

`Cedar.Thm.same_string_term_implies` (theorem, [line 411](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L411))

```lean
public theorem same_string_term_implies {v : Value} {s : String} :
  v ∼ Term.prim (TermPrim.string s) → v = Value.prim (.string s)
```

`Cedar.Thm.same_string_implies` (theorem, [line 418](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L418))

```lean
public theorem same_string_implies {s : String} {t : Term} :
  Value.prim (Prim.string s) ∼ t →
  t = .prim (.string s)
```

`Cedar.Thm.same_bitvec_term_implies` (theorem, [line 424](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L424))

```lean
public theorem same_bitvec_term_implies {v : Value} {n : Nat} {bv : BitVec n} :
  v ∼ Term.prim (TermPrim.bitvec bv) →
  ∃ i, v = Value.prim (.int i) ∧ bv.toInt = i ∧ n = 64
```

`Cedar.Thm.same_bitvec64_term_implies` (theorem, [line 442](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L442))

```lean
public theorem same_bitvec64_term_implies {v : Value} {bv : BitVec 64} :
  v ∼ Term.prim (TermPrim.bitvec bv) →
  ∃ i, v = Value.prim (.int i) ∧ bv.toInt = i
```

`Cedar.Thm.same_int_implies` (theorem, [line 451](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L451))

```lean
public theorem same_int_implies {t : Term} {bv : BitVec 64} {i : Int64} :
  BitVec.toInt bv = i.toInt →
  Value.prim (Prim.int i) ∼ t →
  t = Term.prim (TermPrim.bitvec bv)
```

`Cedar.Thm.same_int` (theorem, [line 477](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L477))

```lean
public theorem same_int {i : Int} {bv : BitVec 64}
  (h₁ : Int64.MIN ≤ i ∧ i ≤ Int64.MAX)
  (h₂ : BitVec.toInt bv = i) :
  Value.prim (Prim.int (Int64.ofIntChecked i h₁)) ∼ Term.prim (TermPrim.bitvec bv)
```

`Cedar.Thm.same_bv` (theorem, [line 484](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L484))

```lean
public theorem same_bv {bv : BitVec 64} :
  Value.prim (Prim.int (Int64.ofInt bv.toInt)) ∼ Term.prim (TermPrim.bitvec bv)
```

`Cedar.Thm.same_int64` (theorem, [line 490](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L490))

```lean
public theorem same_int64 {i : Int64} :
  Value.prim (Prim.int i) ∼ Term.prim (TermPrim.bitvec i.toBitVec)
```

`Cedar.Thm.same_ext` (theorem, [line 498](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L498))

```lean
public theorem same_ext {x : Ext} :
  Value.ext x ∼ Term.prim (TermPrim.ext x)
```

`Cedar.Thm.same_ext_term_implies` (theorem, [line 503](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L503))

```lean
public theorem same_ext_term_implies {v : Value} {x : Ext} :
  v ∼ Term.prim (TermPrim.ext x) → v = Value.ext x
```

`Cedar.Thm.same_ext_implies` (theorem, [line 510](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L510))

```lean
public theorem same_ext_implies  {x : Ext} {t : Term} :
  Value.ext x ∼ t →
  t = .prim (.ext x)
```

`Cedar.Thm.value?_some_implies_attrValue?_some` (theorem, [line 516](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L516))

```lean
public theorem value?_some_implies_attrValue?_some {a : Attr} {tₐ : Term} {vₐ : Value}
  (hv : Term.value? tₐ = some vₐ) :
  Term.value?.attrValue? a tₐ = some (a, some vₐ)
```

`Cedar.Thm.value?_attrValue?_none_implies_none` (theorem, [line 556](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L556))

```lean
public theorem value?_attrValue?_none_implies_none {a : Attr} {t : Term}
  (hv : Term.value?.attrValue? a t = some (a, none)) :
  ∃ ty, t = .none ty
```

`Cedar.Thm.value?_attrValue?_some_implies_same` (theorem, [line 567](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L567))

```lean
public theorem value?_attrValue?_some_implies_same {a : Attr} {t : Term} {v : Value} :
  Term.value?.attrValue? a t = some (a, some v) →
  match t.typeOf with
  | .option _ => ∃ t', t = .some t' ∧ v ∼ t'
  | _         => v ∼ t
```

`Cedar.Thm.value?_attrValue?_fst` (theorem, [line 603](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L603))

```lean
public theorem value?_attrValue?_fst {a : Attr} {t : Term} {av : Attr × Option Value} :
  Term.value?.attrValue? a t = some av → a = av.fst
```

`Cedar.Thm.record_value?_mapM'` (theorem, [line 633](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L633))

```lean
public theorem record_value?_mapM' {rt : Map Attr Term} {rv : Map Attr Value}
  (hr : Term.value? (Term.record rt) = some (Value.record rv)) :
  ∃ avs,
    rt.toList.mapM' (fun x => Term.value?.attrValue? x.fst x.snd) = some avs ∧
    Map.mk (List.filterMap (fun x => Option.map (Prod.mk x.fst) x.snd) avs) = rv
```

`Cedar.Thm.record_value_find?` (theorem, [line 646](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L646))

```lean
public theorem record_value_find? {a : Attr} {tₐ : Term} {rt : Map Attr Term} {avs : List (Attr × Option Value)}
  (hf : Map.find? rt a = some tₐ)
  (hr : rt.toList.mapM' (λ x => Term.value?.attrValue? x.fst x.snd) = some avs) :
  ∃ av, av ∈ avs ∧ Term.value?.attrValue? a tₐ = some av
```

`Cedar.Thm.record_value?_find?_required` (theorem, [line 656](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L656))

```lean
public theorem record_value?_find?_required {a : Attr} {tₐ : Term} {rt : Map Attr Term} {rv : Map Attr Value}
  (hw  : rt.WellFormed)
  (hty : ∀ (ty : TermType), tₐ.typeOf = TermType.option ty → False)
  (hf  : Map.find? rt a = some tₐ)
  (hr  : Term.value? (Term.record rt) = some (Value.record rv)) :
  ∃ vₐ, Map.find? rv a = some vₐ ∧ tₐ.value? = some vₐ
```

`Cedar.Thm.record_value?_find?_optional_some` (theorem, [line 688](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L688))

```lean
public theorem record_value?_find?_optional_some {a : Attr} {tₐ : Term} {rt : Map Attr Term} {rv : Map Attr Value}
  (hw : rt.WellFormed)
  (hf : Map.find? rt a = some (.some tₐ))
  (hr : Term.value? (Term.record rt) = some (Value.record rv)) :
  ∃ vₐ, Map.find? rv a = some vₐ ∧ tₐ.value? = some vₐ
```

`Cedar.Thm.record_value?_find?_optional_none` (theorem, [line 716](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L716))

```lean
public theorem record_value?_find?_optional_none {a : Attr} {ty : TermType} {rt : Map Attr Term} {rv : Map Attr Value}
  (hw : rt.WellFormed)
  (hf : Map.find? rt a = some (.none ty))
  (hr : Term.value? (Term.record rt) = some (Value.record rv)) :
  Map.find? rv a = none
```

`Cedar.Thm.record_value?_find?_none` (theorem, [line 752](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L752))

```lean
public theorem record_value?_find?_none {a : Attr} {rt : Map Attr Term} {rv : Map Attr Value}
  (hw : rt.WellFormed)
  (hf : Map.find? rt a = none)
  (hr : Term.value? (Term.record rt) = some (Value.record rv)) :
  Map.find? rv a = none
```

`Cedar.Thm.same_prim_value_inj` (theorem, [line 781](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L781))

```lean
public theorem same_prim_value_inj {v : Value} {p : TermPrim} {t : Term} :
  v ∼ (Term.prim p) → v ∼ t → (Term.prim p) = t
```

`Cedar.Thm.set_value?_implies_in_value` (theorem, [line 807](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L807))

```lean
public theorem set_value?_implies_in_value {vs : Set Value} {ts : Set Term} {ty : TermType} :
  Term.value? (Term.set ts ty) = some (Value.set vs) →
  ∀ t, t ∈ ts → ∃ v, v ∈ vs ∧ t.value? = some v
```

`Cedar.Thm.set_value?_implies_in_term` (theorem, [line 822](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L822))

```lean
public theorem set_value?_implies_in_term {vs : Set Value} {ts : Set Term} {ty : TermType} :
  Term.value? (Term.set ts ty) = some (Value.set vs) →
  ∀ v, v ∈ vs → ∃ t, t ∈ ts ∧ t.value? = some v
```

`Cedar.Thm.record_value?_some_implies` (theorem, [line 851](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L851))

```lean
public theorem record_value?_some_implies {ats : List (Attr × Term)} {avs : List (Attr × Value)} :
  (Term.record (Map.mk ats)).value? = some (Value.record (Map.mk avs)) →
  ∃ (avs' : List (Attr × Option Value)),
    List.mapM (λ (x : Attr × Term) => Term.value?.attrValue? x.fst x.snd) ats = some avs' ∧
    List.filterMap (λ (x : Attr × Option Value) => Option.map (Prod.mk x.fst) x.snd) avs' = avs
```

`Cedar.Thm.record_value?_some_implied_by` (theorem, [line 865](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L865))

```lean
public theorem record_value?_some_implied_by {ats : List (Attr × Term)} {avs : List (Attr × Value)} {avs' : List (Attr × Option Value)} :
  List.mapM (λ (x : Attr × Term) => Term.value?.attrValue? x.fst x.snd) ats = some avs' →
  List.filterMap (λ (x : Attr × Option Value) => Option.map (Prod.mk x.fst) x.snd) avs' = avs →
  (Term.record (Map.mk ats)).value? = some (Value.record (Map.mk avs))
```

`Cedar.Thm.record_value?_cons` (theorem, [line 873](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L873))

```lean
public theorem record_value?_cons {a : Attr} {t : Term} {ats : List (Attr × Term)} {avs : List (Attr × Value)} :
  (Term.record (Map.mk ((a, t) :: ats))).value? = some (Value.record (Map.mk avs)) →
  ∃ vₒ, Term.value?.attrValue? a t = .some (a, vₒ) ∧
    match vₒ with
    | .some v => ∃ avs', avs = (a, v) :: avs' ∧ (Term.record (Map.mk ats)).value? = some (Value.record (Map.mk avs'))
    | .none   => (Term.record (Map.mk ats)).value? = some (Value.record (Map.mk avs))
```

`Cedar.Thm.record_value?_head_none` (theorem, [line 900](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L900))

```lean
public theorem record_value?_head_none {a : Attr} {t : Term} {ats : List (Attr × Term)} {avs : List (Attr × Value)} :
  ((a, t) :: ats).SortedBy Prod.fst →
  Term.value? (Term.record (Map.mk ((a, t) :: ats))) = some (Value.record (Map.mk avs)) →
  Term.value?.attrValue? a t = some (a, none) →
  Map.find? (Map.mk avs) a = none
```

`Cedar.Thm.same_value_inj` (theorem, [line 1140](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L1140))

```lean
public theorem same_value_inj {t₁ t₂ : Term} {v : Value} {εs : SymEntities} :
  t₁.WellFormed εs → t₂.WellFormed εs → t₁.typeOf = t₂.typeOf →
  v ∼ t₁ → v ∼ t₂ → t₁ = t₂
```

`Cedar.Thm.term_value?_exists` (theorem, [line 1187](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean#L1187))

```lean
public theorem term_value?_exists {t : Term} {ty : Validation.CedarType} {εs : SymEntities} :
  t.WellFormedLiteral εs →
  t.typeOf.cedarType? = .some ty →
  ∃ (v : Value), t.value? = some v
```

## Depends on

- [Well-formedness and interpretations](../data/basic.md)

## Proof depends on

- [Bitvector utilities](../data/bitvec.md)
- [Basic properties of partial evaluation of terms](pe.md)

## Sources

- [Cedar/Thm/SymCC/Term/Same.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Same.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Term.Same.json)
