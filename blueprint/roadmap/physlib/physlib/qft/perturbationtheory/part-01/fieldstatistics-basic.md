---
declaration: module
origin: cited
lean: FieldStatistic, FieldStatistic.bosonic_mul_bosonic, FieldStatistic.bosonic_mul_fermionic, FieldStatistic.fermionic_mul_bosonic, FieldStatistic.fermionic_mul_fermionic, FieldStatistic.mul_bosonic, FieldStatistic.mul_self, FieldStatistic.fermionic_not_eq_bonsic
statement: formalized
proof: formalized
---

# Field statistics

The module `Physlib.QFT.PerturbationTheory.FieldStatistics.Basic`, [Physlib/QFT/PerturbationTheory/FieldStatistics/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/Basic.lean): 43 declarations (3 instances with no name), 5 with a docstring.

> Basic properties related to whether a field, or list of fields, is bosonic or fermionic.

**`FieldStatistic`**, an inductive, [line 26](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/Basic.lean#L26).

> The type `FieldStatistic` is the type containing two elements `bosonic` and `fermionic`.
> This type is used to specify if a field or operator obeys bosonic or fermionic statistics.

```lean
inductive FieldStatistic : Type where
  | bosonic : FieldStatistic
  | fermionic : FieldStatistic
```

**An instance with no name**, [line 43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/Basic.lean#L43).

> The type `FieldStatistic` carries an instance of a commutative group in which
> - `bosonic * bosonic = bosonic`
> - `bosonic * fermionic = fermionic`
> - `fermionic * bosonic = fermionic`
> - `fermionic * fermionic = bosonic`
>
> This group is isomorphic to `ℤ₂`.

```lean
instance : CommGroup FieldStatistic
```

**`FieldStatistic.bosonic_mul_bosonic`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/Basic.lean#L65).

```lean
lemma bosonic_mul_bosonic : bosonic * bosonic = bosonic
```

**`FieldStatistic.bosonic_mul_fermionic`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/Basic.lean#L68).

```lean
lemma bosonic_mul_fermionic : bosonic * fermionic = fermionic
```

**`FieldStatistic.fermionic_mul_bosonic`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/Basic.lean#L71).

```lean
lemma fermionic_mul_bosonic : fermionic * bosonic = fermionic
```

**`FieldStatistic.fermionic_mul_fermionic`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/Basic.lean#L74).

```lean
lemma fermionic_mul_fermionic : fermionic * fermionic = bosonic
```

**`FieldStatistic.mul_bosonic`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/Basic.lean#L77).

```lean
lemma mul_bosonic (a : FieldStatistic) : a * bosonic = a
```

**`FieldStatistic.mul_self`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/Basic.lean#L81).

```lean
lemma mul_self (a : FieldStatistic) : a * a = 1
```

**An instance with no name**, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/Basic.lean#L85).

> Field statics form a finite type.

```lean
instance : Fintype FieldStatistic
```

**`FieldStatistic.fermionic_not_eq_bonsic`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/Basic.lean#L95).

```lean
lemma fermionic_not_eq_bonsic : ¬ fermionic = bosonic
```

**`FieldStatistic.bonsic_eq_fermionic_false`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/Basic.lean#L99).

```lean
lemma bonsic_eq_fermionic_false : bosonic = fermionic ↔ false
```

**`FieldStatistic.neq_fermionic_iff_eq_bosonic`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/Basic.lean#L103).

```lean
lemma neq_fermionic_iff_eq_bosonic (a : FieldStatistic) : ¬ a = fermionic ↔ a = bosonic
```

**`FieldStatistic.neq_bosonic_iff_eq_fermionic`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/Basic.lean#L109).

```lean
lemma neq_bosonic_iff_eq_fermionic (a : FieldStatistic) : ¬ a = bosonic ↔ a = fermionic
```

**`FieldStatistic.bosonic_ne_iff_fermionic_eq`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/Basic.lean#L115).

```lean
lemma bosonic_ne_iff_fermionic_eq (a : FieldStatistic) : ¬ bosonic = a ↔ fermionic = a
```

**`FieldStatistic.fermionic_ne_iff_bosonic_eq`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/Basic.lean#L121).

```lean
lemma fermionic_ne_iff_bosonic_eq (a : FieldStatistic) : ¬ fermionic = a ↔ bosonic = a
```

**`FieldStatistic.eq_self_if_eq_bosonic`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/Basic.lean#L126).

```lean
lemma eq_self_if_eq_bosonic {a : FieldStatistic} :
    (if a = bosonic then bosonic else fermionic) = a
```

**`FieldStatistic.eq_self_if_bosonic_eq`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/Basic.lean#L130).

```lean
lemma eq_self_if_bosonic_eq {a : FieldStatistic} :
    (if bosonic = a then bosonic else fermionic) = a
```

**`FieldStatistic.mul_eq_one_iff`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/Basic.lean#L134).

```lean
lemma mul_eq_one_iff (a b : FieldStatistic) : a * b = 1 ↔ a = b
```

**`FieldStatistic.one_eq_mul_iff`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/Basic.lean#L137).

```lean
lemma one_eq_mul_iff (a b : FieldStatistic) : 1 = a * b ↔ a = b
```

**`FieldStatistic.mul_eq_iff_eq_mul`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/Basic.lean#L140).

```lean
lemma mul_eq_iff_eq_mul (a b c : FieldStatistic) : a * b = c ↔ a = b * c
```

**`FieldStatistic.mul_eq_iff_eq_mul'`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/Basic.lean#L146).

```lean
lemma mul_eq_iff_eq_mul' (a b c : FieldStatistic) : a * b = c ↔ b = a * c
```

**`FieldStatistic.ofList`**, a def, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/Basic.lean#L154).

> The field statistics of a list of fields is fermionic if there is an odd number of fermions,
> otherwise it is bosonic.

```lean
def ofList (s : 𝓕 → FieldStatistic) : (φs : List 𝓕) → FieldStatistic
```

**`FieldStatistic.ofList_cons_eq_mul`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/Basic.lean#L158).

```lean
lemma ofList_cons_eq_mul (s : 𝓕 → FieldStatistic) (φ : 𝓕) (φs : List 𝓕) :
    ofList s (φ :: φs) = s φ * ofList s φs
```

**`FieldStatistic.ofList_eq_prod`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/Basic.lean#L164).

```lean
lemma ofList_eq_prod (s : 𝓕 → FieldStatistic) : (φs : List 𝓕) →
    ofList s φs = (List.map s φs).prod
```

**`FieldStatistic.ofList_singleton`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/Basic.lean#L172).

```lean
lemma ofList_singleton (s : 𝓕 → FieldStatistic) (φ : 𝓕) : ofList s [φ] = s φ
```

**`FieldStatistic.ofList_freeMonoid`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/Basic.lean#L177).

```lean
lemma ofList_freeMonoid (s : 𝓕 → FieldStatistic) (φ : 𝓕) : ofList s (FreeMonoid.of φ) = s φ
```

**`FieldStatistic.ofList_empty`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/Basic.lean#L181).

```lean
lemma ofList_empty (s : 𝓕 → FieldStatistic) : ofList s [] = bosonic
```

**`FieldStatistic.ofList_append`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/Basic.lean#L185).

```lean
lemma ofList_append (s : 𝓕 → FieldStatistic) (φs φs' : List 𝓕) :
    ofList s (φs ++ φs') = if ofList s φs = ofList s φs' then bosonic else fermionic
```

**`FieldStatistic.ofList_append_eq_mul`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/Basic.lean#L197).

```lean
lemma ofList_append_eq_mul (s : 𝓕 → FieldStatistic) (φs φs' : List 𝓕) :
    ofList s (φs ++ φs') = ofList s φs * ofList s φs'
```

**`FieldStatistic.ofList_perm`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/Basic.lean#L204).

```lean
lemma ofList_perm (s : 𝓕 → FieldStatistic) {l l' : List 𝓕} (h : l.Perm l') :
    ofList s l = ofList s l'
```

**`FieldStatistic.ofList_orderedInsert`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/Basic.lean#L209).

```lean
lemma ofList_orderedInsert (s : 𝓕 → FieldStatistic) (le1 : 𝓕 → 𝓕 → Prop) [DecidableRel le1]
    (φs : List 𝓕) (φ : 𝓕) : ofList s (List.orderedInsert le1 φ φs) = ofList s (φ :: φs)
```

**`FieldStatistic.ofList_insertionSort`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/Basic.lean#L214).

```lean
lemma ofList_insertionSort (s : 𝓕 → FieldStatistic) (le1 : 𝓕 → 𝓕 → Prop) [DecidableRel le1]
    (φs : List 𝓕) : ofList s (List.insertionSort le1 φs) = ofList s φs
```

**`FieldStatistic.ofList_map_eq_finset_prod`**, a lemma, [line 218](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/Basic.lean#L218).

```lean
lemma ofList_map_eq_finset_prod (s : 𝓕 → FieldStatistic) :
    (φs : List 𝓕) → (l : List (Fin φs.length)) → (hl : l.Nodup) →
    ofList s (l.map φs.get) = ∏ (i : Fin φs.length), if i ∈ l then s φs[i] else 1
```

**`FieldStatistic.ofList_pair`**, a lemma, [line 250](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/Basic.lean#L250).

```lean
lemma ofList_pair (s : 𝓕 → FieldStatistic) (φ1 φ2 : 𝓕) :
    ofList s [φ1, φ2] = s φ1 * s φ2
```

## ofList and take

**`FieldStatistic.ofList_take_insert`**, a lemma, [line 263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/Basic.lean#L263).

```lean
lemma ofList_take_insert (n : ℕ) (φ : 𝓕) (φs : List 𝓕) :
    ofList q (List.take n φs) = ofList q (List.take n (List.insertIdx φs n φ))
```

**`FieldStatistic.ofList_take_eraseIdx`**, a lemma, [line 268](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/Basic.lean#L268).

```lean
lemma ofList_take_eraseIdx (n : ℕ) (φs : List 𝓕) :
    ofList q (List.take n (φs.eraseIdx n)) = ofList q (List.take n φs)
```

**`FieldStatistic.ofList_take_zero`**, a lemma, [line 273](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/Basic.lean#L273).

```lean
lemma ofList_take_zero (φs : List 𝓕) :
    ofList q (List.take 0 φs) = 1
```

**`FieldStatistic.ofList_take_succ_cons`**, a lemma, [line 278](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/Basic.lean#L278).

```lean
lemma ofList_take_succ_cons (n : ℕ) (φ1 : 𝓕) (φs : List 𝓕) :
    ofList q ((φ1 :: φs).take (n + 1)) = q φ1 * ofList q (φs.take n)
```

**`FieldStatistic.ofList_take_insertIdx_gt`**, a lemma, [line 283](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/Basic.lean#L283).

```lean
lemma ofList_take_insertIdx_gt (n m : ℕ) (φ1 : 𝓕) (φs : List 𝓕) (hn : n < m) :
    ofList q ((List.insertIdx φs m φ1).take n) = ofList q (φs.take n)
```

**`FieldStatistic.ofList_insert_lt_eq`**, a lemma, [line 287](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/Basic.lean#L287).

```lean
lemma ofList_insert_lt_eq (n m : ℕ) (φ1 : 𝓕) (φs : List 𝓕) (hn : m ≤ n)
    (hm : m ≤ φs.length) :
    ofList q ((List.insertIdx φs m φ1).take (n + 1)) =
    ofList q ((φ1 :: φs).take (n + 1))
```

**`FieldStatistic.ofList_take_insertIdx_le`**, a lemma, [line 295](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/Basic.lean#L295).

```lean
lemma ofList_take_insertIdx_le (n m : ℕ) (φ1 : 𝓕) (φs : List 𝓕) (hn : m ≤ n) (hm : m ≤ φs.length) :
    ofList q ((List.insertIdx φs m φ1).take (n + 1)) = q φ1 * ofList q (φs.take n)
```

**An instance with no name**, [line 302](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/Basic.lean#L302).

> The instance of an additive monoid on `FieldStatistic`.

```lean
instance : AddMonoid FieldStatistic
```

**`FieldStatistic.add_eq_mul`**, a lemma, [line 320](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/Basic.lean#L320).

```lean
lemma add_eq_mul (a b : FieldStatistic) : a + b = a * b
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Proof depends on

- [List lemmas](../../../mathematics/formathlib/list-insertidx.md)

## Sources

- [Physlib/QFT/PerturbationTheory/FieldStatistics/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/Basic.lean)
