---
declaration: module
origin: cited
lean: SuperSymmetry.SU5.ChargeSpectrum.minimalSuperSet, SuperSymmetry.SU5.ChargeSpectrum.self_subset_mem_minimalSuperSet, SuperSymmetry.SU5.ChargeSpectrum.self_not_mem_minimalSuperSet, SuperSymmetry.SU5.ChargeSpectrum.self_ne_mem_minimalSuperSet, SuperSymmetry.SU5.ChargeSpectrum.card_of_mem_minimalSuperSet, SuperSymmetry.SU5.ChargeSpectrum.insert_Q5_mem_minimalSuperSet, SuperSymmetry.SU5.ChargeSpectrum.insert_Q10_mem_minimalSuperSet, SuperSymmetry.SU5.ChargeSpectrum.some_qHd_mem_minimalSuperSet_of_none
statement: formalized
proof: formalized
---

# Minimal super set

The module `Physlib.Particles.SuperSymmetry.SU5.ChargeSpectrum.MinimalSuperSet`, [Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimalSuperSet.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimalSuperSet.lean): 14 declarations, 2 with a docstring.

## i. Overview

> The minimally super set of a spectrum of charges `x` is the finite set of
> spectrums of charges `y` such that `x ⊆ y` and there is no `z` such that `x ⊆ z ⊂ y`.
> The minimal super set is defined using a finite set of possible charges in the `5`-bar and `10`
> representations of `su(5)`. This is to ensure that the minimal super set is itself finite.
>
> In this file we define the minimal super set and prove some basic properties of it.

## ii. Key results

> - `minimalSuperSet`: the minimal super set of a charge spectrum.
> - `exists_minimalSuperSet`: the existence of a member of the minimal super set
>   between two charge spectra.
> - `subset_insert_filter_card_zero`: a statement related to closure properties of multisets
>   of charge spectra under a proposition `p` satisfying certain properties. The proof
>   of this result relies on induction on minimal super sets.

## iv. References

> * None.

## A. The minimal super set

> We define the minimal super set.

**`SuperSymmetry.SU5.ChargeSpectrum.minimalSuperSet`**, a def, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimalSuperSet.lean#L67).

> Given a collection of charges `x` in `ofFinset S5 S10`,
> the minimal charges `y` in `ofFinset S5 S10` which are a super sets of `x`.

```lean
def minimalSuperSet (S5 S10 : Finset 𝓩) (x : ChargeSpectrum 𝓩) : Finset (ChargeSpectrum 𝓩)
```

### A.1. Members of the minimal super set are super sets

> We show the basic property of a member `y ∈ minimalSuperSet S5 S10 x`, that is
> that they are indeed super sets, namely `x ⊆ y`.

**`SuperSymmetry.SU5.ChargeSpectrum.self_subset_mem_minimalSuperSet`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimalSuperSet.lean#L84).

```lean
lemma self_subset_mem_minimalSuperSet (S5 S10 : Finset 𝓩) (x y : ChargeSpectrum 𝓩)
    (hy : y ∈ minimalSuperSet S5 S10 x) : x ⊆ y
```

### A.2. Self is not a member of the minimal super set

> A charge spectrum is not a member of its own minimal super set. We give
> two different forms of this result.

**`SuperSymmetry.SU5.ChargeSpectrum.self_not_mem_minimalSuperSet`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimalSuperSet.lean#L127).

```lean
lemma self_not_mem_minimalSuperSet (S5 S10 : Finset 𝓩) (x : ChargeSpectrum 𝓩) :
    x ∉ minimalSuperSet S5 S10 x
```

**`SuperSymmetry.SU5.ChargeSpectrum.self_ne_mem_minimalSuperSet`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimalSuperSet.lean#L131).

```lean
lemma self_ne_mem_minimalSuperSet (S5 S10 : Finset 𝓩) (x y : ChargeSpectrum 𝓩)
    (hy : y ∈ minimalSuperSet S5 S10 x) : x ≠ y
```

### A.3. Cardinality of member of the minimal super set

> We show that any member `y` of the minimal super set of `x` has cardinality one more than
> that of `x`. I.e. it contains exactly one more unique charge.

**`SuperSymmetry.SU5.ChargeSpectrum.card_of_mem_minimalSuperSet`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimalSuperSet.lean#L146).

```lean
lemma card_of_mem_minimalSuperSet {S5 S10 : Finset 𝓩} {x : ChargeSpectrum 𝓩}
    (y : ChargeSpectrum 𝓩) (hy : y ∈ minimalSuperSet S5 S10 x) :
    card y = card x + 1
```

### A.4. Inserting charges and minimal super sets

> We show that inserting a charge from `S5` or `S10` into `x`'s `Q5` or `Q10` respectively
> which is not already present in `x` gives a member of the minimal super set.
>
> Likewise we show that if `x` has no `qHd` or `qHu` charge, then inserting a charge from `S5`
> into `qHd` or `qHu` respectively gives a member of the minimal super set.

**`SuperSymmetry.SU5.ChargeSpectrum.insert_Q5_mem_minimalSuperSet`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimalSuperSet.lean#L200).

```lean
lemma insert_Q5_mem_minimalSuperSet {S5 S10 : Finset 𝓩} {x : ChargeSpectrum 𝓩}
    (z : 𝓩) (hz : z ∈ S5) (hznot : z ∉ x.Q5) :
    ⟨x.qHd, x.qHu, insert z x.Q5, x.Q10⟩ ∈ minimalSuperSet S5 S10 x
```

**`SuperSymmetry.SU5.ChargeSpectrum.insert_Q10_mem_minimalSuperSet`**, a lemma, [line 213](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimalSuperSet.lean#L213).

```lean
lemma insert_Q10_mem_minimalSuperSet {S5 S10 : Finset 𝓩} {x : ChargeSpectrum 𝓩}
    (z : 𝓩) (hz : z ∈ S10) (hznot : z ∉ x.Q10) :
    ⟨x.qHd, x.qHu, x.Q5, insert z x.Q10⟩ ∈ minimalSuperSet S5 S10 x
```

**`SuperSymmetry.SU5.ChargeSpectrum.some_qHd_mem_minimalSuperSet_of_none`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimalSuperSet.lean#L226).

```lean
lemma some_qHd_mem_minimalSuperSet_of_none {S5 S10 : Finset 𝓩}
    {x2 : Option 𝓩 × Finset 𝓩 × Finset 𝓩} (z : 𝓩) (hz : z ∈ S5) :
    ⟨some z, x2.1, x2.2.1, x2.2.2⟩ ∈ minimalSuperSet S5 S10 ⟨none, x2.1, x2.2.1, x2.2.2⟩
```

**`SuperSymmetry.SU5.ChargeSpectrum.some_qHu_mem_minimalSuperSet_of_none`**, a lemma, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimalSuperSet.lean#L231).

```lean
lemma some_qHu_mem_minimalSuperSet_of_none {S5 S10 : Finset 𝓩}
    {x1 : Option 𝓩} {x2 : Finset 𝓩 × Finset 𝓩} (z : 𝓩) (hz : z ∈ S5) :
    ⟨x1, some z, x2.1,x2.2⟩ ∈ minimalSuperSet S5 S10 ⟨x1, none, x2.1, x2.2⟩
```

### A.5. Existence of a minimal super set member between two charges

> We show that if `y` has charges from `S5` and `S10` and is a super set of `x` but not equal to `x`
> then there is a `z` in the minimal super set of `x` which is a subset of `y`.
>
> This shows, in a sense, that `minimalSuperSet` is "minimal", although it does not
> go all the way to doing that. In particular, it does show that every minimal super set
> is a member of `minimalSuperSet`.

**`SuperSymmetry.SU5.ChargeSpectrum.exists_minimalSuperSet`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimalSuperSet.lean#L249).

```lean
lemma exists_minimalSuperSet (S5 S10 : Finset 𝓩) {x y : ChargeSpectrum 𝓩}
    (hy : y ∈ ofFinset S5 S10) (hsubset : x ⊆ y)
    (hxneqy : x ≠ y) : ∃ z ∈ minimalSuperSet S5 S10 x, z ⊆ y
```

## B. Induction properties on the minimal super set

> We now prove a number of induction properties related to minimal super sets.

### B.1. Lifting propositions from minimal super sets to super sets

> We show that for a proposition `p` on charge spectra with the property that
> it is true on all minimal super sets of `x` if it true on `x` itself, then it is true on all
> super sets of `x` if it is true for `x` itself.

**`SuperSymmetry.SU5.ChargeSpectrum.minimalSuperSet_induction_on_inductive`**, a lemma, [line 325](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimalSuperSet.lean#L325).

```lean
lemma minimalSuperSet_induction_on_inductive {S5 S10 : Finset 𝓩}
    (p : ChargeSpectrum 𝓩 → Prop)
    (hp : (x : ChargeSpectrum 𝓩) → p x → ∀ y ∈ minimalSuperSet S5 S10 x, p y)
    (x : ChargeSpectrum 𝓩) (hbase : p x)
    (y : ChargeSpectrum 𝓩) (hy : y ∈ ofFinset S5 S10) (hsubset : x ⊆ y) :
    (n : ℕ) → (hn : n = y.card - x.card) → p y
  | 0, hn => by
    have hxy : x = y := by
      refine eq_of_subset_card hsubset ?_
      have hl : card x ≤ card y := card_mono hsubset
      omega
    subst hxy
    simp_all
  | Nat.succ n, hn => by
    have hxy : x ≠ y := by
      intro h
      subst h
      simp at hn
    obtain ⟨z, hz, hsubsetz⟩
```

### B.2. Closure of multisets based on proposition for minimal super sets

> We show that for a predicate `p` on charge spectrum,
> if a multiset `T` of complete charge spectra has the property that
> - all insertions of a `q10` charge either ends in `T` or fails `p`.
> - all insertions of a `q5` charge either ends in `T` or fails `p`.
> Then if `x` is in `T` then all members of the minimal super set of `x` either
> are in `T` or fail `p`.

**`SuperSymmetry.SU5.ChargeSpectrum.insert_filter_card_zero`**, a lemma, [line 364](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimalSuperSet.lean#L364).

```lean
lemma insert_filter_card_zero
    (T : Multiset (ChargeSpectrum 𝓩)) (S5 S10 : Finset 𝓩)
    (p : ChargeSpectrum 𝓩 → Prop) [DecidablePred p]
    (hComplet : ∀ x ∈ T, IsComplete x)
    (h10 : ∀ q10 : S10, ((T.map fun x => ⟨x.qHd, x.qHu, x.Q5, insert q10.1 x.Q10⟩).filter
      fun y => (y ∉ T ∧ p y)) = ∅)
    (h5 : ∀ q5 : S5, ((T.map fun x => ⟨x.qHd, x.qHu, insert q5.1 x.Q5, x.Q10⟩).filter
      fun y => (y ∉ T ∧ p y)) = ∅) :
    ∀ x ∈ T, ∀ y ∈ minimalSuperSet S5 S10 x, y ∉ T → ¬ p y
```

### B.3. Closure of multisets based on propositions

> We show that for a predicate `p` on charge spectrum which if false on a charge spectrum
> is also false on all its super sets,
> if a multiset `T` of complete charge spectra has the property that
> - all insertions of a `q10` charge either ends in `T` or fails `p`.
> - all insertions of a `q5` charge either ends in `T` or fails `p`.
> Then if `y` is not in `T` then it does not satisfy `p`.
>
> We first prove this with an explicit induction argument, `n`, and then
> we prove it in a more user friendly way.

**`SuperSymmetry.SU5.ChargeSpectrum.subset_insert_filter_card_zero_inductive`**, a lemma, [line 409](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimalSuperSet.lean#L409).

```lean
lemma subset_insert_filter_card_zero_inductive
    (T : Multiset (ChargeSpectrum 𝓩))
    (S5 S10 : Finset 𝓩)
    (p : ChargeSpectrum 𝓩 → Prop) [DecidablePred p]
    (hnotSubset : ∀ (x y : ChargeSpectrum 𝓩), x ⊆ y → ¬ p x → ¬ p y)
    (hComplet : ∀ x ∈ T, IsComplete x)
    (x : ChargeSpectrum 𝓩)
    (hx : x ∈ T) (y : ChargeSpectrum 𝓩) (hsubset : x ⊆ y)
    (hy : y ∈ ofFinset S5 S10)
    (h10 : ∀ q10 : S10, ((T.map fun x => ⟨x.qHd, x.qHu, x.Q5, insert q10.1 x.Q10⟩).filter
      fun y => (y ∉ T ∧ p y)) = ∅)
    (h5 : ∀ q5 : S5, ((T.map fun x => ⟨x.qHd, x.qHu, insert q5.1 x.Q5, x.Q10⟩).filter
      fun y => (y ∉ T ∧ p y)) = ∅) :
    (n : ℕ) → (hn : n = y.card - x.card) → y ∉ T → ¬ p y
  | 0, hn, hnot_in_T => by
    have hxy : x = y := by
      refine eq_of_subset_card hsubset ?_
      have hl : x.card ≤ y.card := card_mono hsubset
      omega
    subst hxy
    simp_all
  | Nat.succ n, hn, hnot_in_T => by
    have hxy : x ≠ y := by
      intro h
      subst h
      simp at hn
    obtain ⟨z, hz, hsubsetz⟩
```

**`SuperSymmetry.SU5.ChargeSpectrum.subset_insert_filter_card_zero`**, a lemma, [line 456](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimalSuperSet.lean#L456).

> For a proposition `p` if `(T.uniqueMap4 (insert q10.1)).toMultiset.filter p`
> and `(T.uniqueMap3 (insert q5.1)).toMultiset.filter p` for all `q5 ∈ S5` and `q10 ∈ S10` then
> if `x ∈ T` and `x ⊆ y` if `y ∉ T` then `¬ p y`.
> This assumes that all charges in `T` are complete, and that `p` satisfies
> `x ⊆ y → ¬ p x → ¬ p y`.

```lean
lemma subset_insert_filter_card_zero
    (T : Multiset (ChargeSpectrum 𝓩))
    (S5 S10 : Finset 𝓩)
    (p : ChargeSpectrum 𝓩 → Prop) [DecidablePred p]
    (hnotSubset : ∀ (x y : ChargeSpectrum 𝓩), x ⊆ y → ¬ p x → ¬ p y)
    (hComplet : ∀ x ∈ T, IsComplete x)
    (x : ChargeSpectrum 𝓩)
    (hx : x ∈ T) (y : ChargeSpectrum 𝓩) (hsubset : x ⊆ y)
    (hy : y ∈ ofFinset S5 S10)
    (h10 : ∀ q10 : S10, ((T.map fun x => ⟨x.qHd, x.qHu, x.Q5, insert q10.1 x.Q10⟩).filter
      fun y => (y ∉ T ∧ p y)) = ∅)
    (h5 : ∀ q5 : S5, ((T.map fun x => ⟨x.qHd, x.qHu, insert q5.1 x.Q5, x.Q10⟩).filter
      fun y => (y ∉ T ∧ p y)) = ∅) :
      y ∉ T → ¬ p y
```

## Depends on

- [Completions of charges](su5-chargespectrum-completions.md)

## Sources

- [Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimalSuperSet.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimalSuperSet.lean)
