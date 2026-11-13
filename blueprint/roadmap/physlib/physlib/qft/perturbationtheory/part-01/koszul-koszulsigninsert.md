---
declaration: module
origin: cited
lean: Wick.koszulSignInsert, Wick.koszulSignInsert_boson, Wick.koszulSignInsert_mul_self, Wick.koszulSignInsert_le_forall, Wick.koszulSignInsert_ge_forall_append, Wick.koszulSignInsert_eq_filter, Wick.koszulSignInsert_eq_cons, Wick.koszulSignInsert_eq_grade
statement: formalized
proof: formalized
---

# Koszul sign insert

The module `Physlib.QFT.PerturbationTheory.Koszul.KoszulSignInsert`, [Physlib/QFT/PerturbationTheory/Koszul/KoszulSignInsert.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/Koszul/KoszulSignInsert.lean): 18 declarations, 3 with a docstring.

**`Wick.koszulSignInsert`**, a def, [line 27](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/Koszul/KoszulSignInsert.lean#L27).

> Gives a factor of `-1` when inserting `a` into a list `List I` in the ordered position
> for each fermion-fermion cross.

```lean
def koszulSignInsert {𝓕 : Type} (q : 𝓕 → FieldStatistic) (le : 𝓕 → 𝓕 → Prop)
    [DecidableRel le] (φ : 𝓕) : List 𝓕 → ℂ
```

**`Wick.koszulSignInsert_boson`**, a lemma, [line 35](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/Koszul/KoszulSignInsert.lean#L35).

> When inserting a boson the `koszulSignInsert` is always `1`.

```lean
lemma koszulSignInsert_boson (q : 𝓕 → FieldStatistic) (le : 𝓕 → 𝓕 → Prop) [DecidableRel le]
    (φ : 𝓕) (ha : q φ = bosonic) : (φs : List 𝓕) → koszulSignInsert q le φ φs = 1
```

**`Wick.koszulSignInsert_mul_self`**, a lemma, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/Koszul/KoszulSignInsert.lean#L45).

```lean
lemma koszulSignInsert_mul_self (φ : 𝓕) :
    (φs : List 𝓕) → koszulSignInsert q le φ φs * koszulSignInsert q le φ φs = 1
```

**`Wick.koszulSignInsert_le_forall`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/Koszul/KoszulSignInsert.lean#L61).

```lean
lemma koszulSignInsert_le_forall (φ : 𝓕) (φs : List 𝓕) (hi : ∀ φ', le φ φ') :
    koszulSignInsert q le φ φs = 1
```

**`Wick.koszulSignInsert_ge_forall_append`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/Koszul/KoszulSignInsert.lean#L72).

```lean
lemma koszulSignInsert_ge_forall_append (φs : List 𝓕) (φ' φ : 𝓕) (hi : ∀ φ'', le φ'' φ) :
    koszulSignInsert q le φ' φs = koszulSignInsert q le φ' (φs ++ [φ])
```

**`Wick.koszulSignInsert_eq_filter`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/Koszul/KoszulSignInsert.lean#L82).

```lean
lemma koszulSignInsert_eq_filter (φ : 𝓕) : (φs : List 𝓕) →
    koszulSignInsert q le φ φs =
    koszulSignInsert q le φ (List.filter (fun i => decide (¬ le φ i)) φs)
```

**`Wick.koszulSignInsert_eq_cons`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/Koszul/KoszulSignInsert.lean#L100).

```lean
lemma koszulSignInsert_eq_cons [Std.Total le] (φ : 𝓕) (φs : List 𝓕) :
    koszulSignInsert q le φ φs = koszulSignInsert q le φ (φ :: φs)
```

**`Wick.koszulSignInsert_eq_grade`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/Koszul/KoszulSignInsert.lean#L108).

```lean
lemma koszulSignInsert_eq_grade (φ : 𝓕) (φs : List 𝓕) :
    koszulSignInsert q le φ φs = if ofList q [φ] = fermionic ∧
    ofList q (List.filter (fun i => decide (¬ le φ i)) φs) = fermionic then -1 else 1
```

**`Wick.koszulSignInsert_eq_perm`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/Koszul/KoszulSignInsert.lean#L142).

```lean
lemma koszulSignInsert_eq_perm (φs φs' : List 𝓕) (φ : 𝓕) (h : φs.Perm φs') :
    koszulSignInsert q le φ φs = koszulSignInsert q le φ φs'
```

**`Wick.koszulSignInsert_eq_sort`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/Koszul/KoszulSignInsert.lean#L154).

```lean
lemma koszulSignInsert_eq_sort (φs : List 𝓕) (φ : 𝓕) :
    koszulSignInsert q le φ φs = koszulSignInsert q le φ (List.insertionSort le φs)
```

**`Wick.koszulSignInsert_eq_exchangeSign_take`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/Koszul/KoszulSignInsert.lean#L159).

```lean
lemma koszulSignInsert_eq_exchangeSign_take [Std.Total le] [IsTrans 𝓕 le] (φ : 𝓕) (φs : List 𝓕) :
    koszulSignInsert q le φ φs = 𝓢(q φ, ofList q
    ((List.insertionSort le φs).take (orderedInsertPos le (List.insertionSort le φs) φ)))
```

**`Wick.koszulSignInsert_insertIdx`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/Koszul/KoszulSignInsert.lean#L209).

```lean
lemma koszulSignInsert_insertIdx (i j : 𝓕) (r : List 𝓕) (n : ℕ) (hn : n ≤ r.length) :
    koszulSignInsert q le j (List.insertIdx r n i) = koszulSignInsert q le j (i :: r)
```

**`Wick.koszulSignCons`**, a def, [line 216](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/Koszul/KoszulSignInsert.lean#L216).

> The difference in `koszulSignInsert` on inserting `r0` into `r` compared to
> into `r1 :: r` for any `r`.

```lean
def koszulSignCons (φ0 φ1 : 𝓕) : ℂ
```

**`Wick.koszulSignCons_eq_exchangeSign`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/Koszul/KoszulSignInsert.lean#L220).

```lean
lemma koszulSignCons_eq_exchangeSign (φ0 φ1 : 𝓕) : koszulSignCons q le φ0 φ1 =
    if le φ0 φ1 then 1 else 𝓢(q φ0, q φ1)
```

**`Wick.koszulSignInsert_cons`**, a lemma, [line 235](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/Koszul/KoszulSignInsert.lean#L235).

```lean
lemma koszulSignInsert_cons (r0 r1 : 𝓕) (r : List 𝓕) :
    koszulSignInsert q le r0 (r1 :: r) = (koszulSignCons q le r0 r1) *
    koszulSignInsert q le r0 r
```

**`Wick.koszulSignInsert_of_le_mem`**, a lemma, [line 240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/Koszul/KoszulSignInsert.lean#L240).

```lean
lemma koszulSignInsert_of_le_mem (φ0 : 𝓕) : (φs : List 𝓕) → (h : ∀ b ∈ φs, le φ0 b) →
    koszulSignInsert q le φ0 φs = 1
```

**`Wick.koszulSignInsert_eq_rel_eq_stat`**, a lemma, [line 252](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/Koszul/KoszulSignInsert.lean#L252).

```lean
lemma koszulSignInsert_eq_rel_eq_stat {ψ φ : 𝓕} [IsTrans 𝓕 le]
    (h1 : le φ ψ) (h2 : le ψ φ) (hq : q ψ = q φ) : (φs : List 𝓕) →
    koszulSignInsert q le φ φs = koszulSignInsert q le ψ φs
```

**`Wick.koszulSignInsert_eq_remove_same_stat_append`**, a lemma, [line 273](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/Koszul/KoszulSignInsert.lean#L273).

```lean
lemma koszulSignInsert_eq_remove_same_stat_append {ψ φ φ' : 𝓕} [IsTrans 𝓕 le]
    (h1 : le φ ψ) (h2 : le ψ φ) (hq : q ψ = q φ) : (φs : List 𝓕) →
    koszulSignInsert q le φ' (φ :: ψ :: φs) = koszulSignInsert q le φ' φs
```

## Depends on

- [List lemmas](../../../mathematics/formathlib/list.md)
- [Exchange sign for field statistics](fieldstatistics-exchangesign.md)

## Sources

- [Physlib/QFT/PerturbationTheory/Koszul/KoszulSignInsert.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/Koszul/KoszulSignInsert.lean)
