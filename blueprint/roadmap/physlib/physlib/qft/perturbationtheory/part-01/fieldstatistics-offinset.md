---
declaration: module
origin: cited
lean: FieldStatistic.ofFinset, FieldStatistic.ofFinset_empty, FieldStatistic.ofFinset_singleton, FieldStatistic.ofFinset_finset_map, FieldStatistic.ofFinset_insert, FieldStatistic.ofFinset_erase, FieldStatistic.ofFinset_eq_prod, FieldStatistic.ofFinset_union
statement: formalized
proof: formalized
---

# Field statistics of a finite set.

The module `Physlib.QFT.PerturbationTheory.FieldStatistics.OfFinset`, [Physlib/QFT/PerturbationTheory/FieldStatistics/OfFinset.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/OfFinset.lean): 11 declarations, 1 with a docstring.

**`FieldStatistic.ofFinset`**, a def, [line 24](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/OfFinset.lean#L24).

> The field statistic associated with a map `f : Fin n → 𝓕` (usually `.get` of a list)
> and a finite set of elements of `Fin n`.

```lean
def ofFinset {n : ℕ} (q : 𝓕 → FieldStatistic) (f : Fin n → 𝓕) (a : Finset (Fin n)) :
    FieldStatistic
```

**`FieldStatistic.ofFinset_empty`**, a lemma, [line 29](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/OfFinset.lean#L29).

```lean
lemma ofFinset_empty (q : 𝓕 → FieldStatistic) (f : Fin n → 𝓕) :
    ofFinset q f ∅ = 1
```

**`FieldStatistic.ofFinset_singleton`**, a lemma, [line 34](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/OfFinset.lean#L34).

```lean
lemma ofFinset_singleton {n : ℕ} (q : 𝓕 → FieldStatistic) (f : Fin n → 𝓕) (i : Fin n) :
    ofFinset q f {i} = q (f i)
```

**`FieldStatistic.ofFinset_finset_map`**, a lemma, [line 38](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/OfFinset.lean#L38).

```lean
lemma ofFinset_finset_map {n m : ℕ}
    (q : 𝓕 → FieldStatistic) (i : Fin m → Fin n) (hi : Function.Injective i)
    (f : Fin n → 𝓕) (a : Finset (Fin m)) :
    ofFinset q (f ∘ i) a = ofFinset q f (a.map ⟨i, hi⟩)
```

**`FieldStatistic.ofFinset_insert`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/OfFinset.lean#L56).

```lean
lemma ofFinset_insert (q : 𝓕 → FieldStatistic) (φs : List 𝓕) (a : Finset (Fin φs.length))
    (i : Fin φs.length) (h : i ∉ a) :
    ofFinset q φs.get (Insert.insert i a) = (q φs[i]) * ofFinset q φs.get a
```

**`FieldStatistic.ofFinset_erase`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/OfFinset.lean#L74).

```lean
lemma ofFinset_erase (q : 𝓕 → FieldStatistic) (φs : List 𝓕) (a : Finset (Fin φs.length))
    (i : Fin φs.length) (h : i ∈ a) :
    ofFinset q φs.get (a.erase i) = (q φs[i]) * ofFinset q φs.get a
```

**`FieldStatistic.ofFinset_eq_prod`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/OfFinset.lean#L85).

```lean
lemma ofFinset_eq_prod (q : 𝓕 → FieldStatistic) (φs : List 𝓕) (a : Finset (Fin φs.length)) :
    ofFinset q φs.get a = ∏ (i : Fin φs.length), if i ∈ a then (q φs[i]) else 1
```

**`FieldStatistic.ofFinset_union`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/OfFinset.lean#L94).

```lean
lemma ofFinset_union (q : 𝓕 → FieldStatistic) (φs : List 𝓕) (a b : Finset (Fin φs.length)) :
    ofFinset q φs.get a * ofFinset q φs.get b = ofFinset q φs.get ((a ∪ b) \ (a ∩ b))
```

**`FieldStatistic.ofFinset_union_disjoint`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/OfFinset.lean#L108).

```lean
lemma ofFinset_union_disjoint (q : 𝓕 → FieldStatistic) (φs : List 𝓕) (a b : Finset (Fin φs.length))
    (h : Disjoint a b) :
    ofFinset q φs.get a * ofFinset q φs.get b = ofFinset q φs.get (a ∪ b)
```

**`FieldStatistic.ofFinset_filter_mul_neg`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/OfFinset.lean#L114).

```lean
lemma ofFinset_filter_mul_neg (q : 𝓕 → FieldStatistic) (φs : List 𝓕) (a : Finset (Fin φs.length))
    (p : Fin φs.length → Prop) [DecidablePred p] :
    ofFinset q φs.get (Finset.filter p a) *
    ofFinset q φs.get (Finset.filter (fun i => ¬ p i) a) = ofFinset q φs.get a
```

**`FieldStatistic.ofFinset_filter`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/OfFinset.lean#L123).

```lean
lemma ofFinset_filter (q : 𝓕 → FieldStatistic) (φs : List 𝓕) (a : Finset (Fin φs.length))
    (p : Fin φs.length → Prop) [DecidablePred p] :
    ofFinset q φs.get (Finset.filter p a) = ofFinset q φs.get (Finset.filter (fun i => ¬ p i) a) *
    ofFinset q φs.get a
```

## Depends on

- [Field statistics](fieldstatistics-basic.md)

## Sources

- [Physlib/QFT/PerturbationTheory/FieldStatistics/OfFinset.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/OfFinset.lean)
