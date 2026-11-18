---
declaration: module
origin: cited
lean: SuperSymmetry.SU5.ChargeSpectrum.IsComplete, SuperSymmetry.SU5.ChargeSpectrum.not_isComplete_empty, SuperSymmetry.SU5.ChargeSpectrum.isComplete_mono, SuperSymmetry.SU5.ChargeSpectrum.completions, SuperSymmetry.SU5.ChargeSpectrum.mem_completions_iff, SuperSymmetry.SU5.ChargeSpectrum.completions_nodup, SuperSymmetry.SU5.ChargeSpectrum.completions_eq_singleton_of_complete, SuperSymmetry.SU5.ChargeSpectrum.self_mem_completions_iff_isComplete
statement: formalized
proof: formalized
---

# Completions of charges

The module `Physlib.Particles.SuperSymmetry.SU5.ChargeSpectrum.Completions`, [Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Completions.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Completions.lean): 15 declarations (1 instance with no name), 11 with a docstring.

## i. Overview

> Recall that a charge spectrum has optional `Hu` and `Hd` charges, and
> can have an empty set of `5`-bar or `10` charges.
>
> We say a charge spectrum is complete if it has all types of fields present, i.e.
> the `Hd` and `Hu` charges are present, and the sets of `5`-bar and `10` charges are non-empty.
>
> Given a non-complete charge spectrum `x` we can find all the completions of `x`,
> which charges in given subsets. That is, all charge spectra `y` which are a super set of `x`,
> are complete, and have their charges in the given subsets.

## ii. Key results

> - `IsComplete` : A predicate saying a charge spectrum is complete.
> - `completions` : Given a charge spectrum `x` and finite sets of charges `S5` and `S10`,
>   the multiset of completions of `x` with charges in `S5` and `S10`.
> - `completionsTopYukawa` : A fast version of `completions` for an `x` which is in
>   `minimallyAllowsTermsOfFinset S5 S10 .topYukawa`, or in other words has a `qHu` charge,
>   a non-empty set of `10` charges, but does not have a `qHd` charge or any `5`-bar charges.

## iv. References

> * None.

## A. The IsComplete predicate

> We say a charge spectrum is complete if it has all types of fields present, i.e.
> the `Hd` and `Hu` charges are present, and the sets of `5`-bar and `10` charges are non-empty.

**`SuperSymmetry.SU5.ChargeSpectrum.IsComplete`**, a def, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Completions.lean#L74).

> A charge spectrum is complete if it has all types of fields.

```lean
def IsComplete (x : ChargeSpectrum 𝓩) : Prop
```

**An instance with no name**, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Completions.lean#L77).

```lean
instance [DecidableEq 𝓩] (x : ChargeSpectrum 𝓩) : Decidable (IsComplete x)
```

### A.1. The empty spectrum is not complete

> The empty charge spectrum is not complete, since it has no charges present.

**`SuperSymmetry.SU5.ChargeSpectrum.not_isComplete_empty`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Completions.lean#L89).

```lean
lemma not_isComplete_empty : ¬ IsComplete (∅ : ChargeSpectrum 𝓩)
```

### A.2. The predicate `IsCompelete` is monotonic

> The predicate `IsComplete` is monotonic with respect to the subset relation. That is, if `x` is a
> subset of `y` and `x` is complete, then `y` is also complete.

**`SuperSymmetry.SU5.ChargeSpectrum.isComplete_mono`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Completions.lean#L101).

```lean
lemma isComplete_mono {x y : ChargeSpectrum 𝓩} (h : x ⊆ y) (hx : IsComplete x) :
    IsComplete y
```

## B. Multiset of completions

> The completions of a charge spectrum `x` with charges in given finite sets `S5` and `S10`
> are all the charge spectra `y` which are a super set of `x`, are complete, and have
> their charges in `S5` and `S10`.

**`SuperSymmetry.SU5.ChargeSpectrum.completions`**, a def, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Completions.lean#L131).

> Given a collection of charges `x` in `ofFinset S5 S10`,
> the minimal charges `y` in `ofFinset S5 S10` which are a super sets of `x` and are
> complete.

```lean
def completions (S5 S10 : Finset 𝓩) (x : ChargeSpectrum 𝓩) : Multiset (ChargeSpectrum 𝓩)
```

### B.1. A membership condition

> A simple relation for membership of a charge spectrum in the completions of another.

**`SuperSymmetry.SU5.ChargeSpectrum.mem_completions_iff`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Completions.lean#L146).

```lean
lemma mem_completions_iff {S5 S10 : Finset 𝓩} {x y : ChargeSpectrum 𝓩} :
    y ∈ completions S5 S10 x ↔
    y.qHd ∈ (if x.qHd.isSome then {x.qHd} else S5.val.map fun y => some y) ∧
    y.qHu ∈ (if x.qHu.isSome then {x.qHu} else S5.val.map fun y => some y) ∧
    y.Q5 ∈ (if x.Q5 ≠ ∅ then {x.Q5} else S5.val.map fun y => {y}) ∧
    y.Q10 ∈ (if x.Q10 ≠ ∅ then {x.Q10} else S10.val.map fun y => {y})
```

### B.2. No duplicate condition

**`SuperSymmetry.SU5.ChargeSpectrum.completions_nodup`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Completions.lean#L171).

> For speed we define `completions` to be a multiset, but in fact it has no duplicates,
> so it could be defined as a finite set.

```lean
lemma completions_nodup (S5 S10 : Finset 𝓩) (x : ChargeSpectrum 𝓩) :
    (completions S5 S10 x).Nodup
```

### B.3. Completions of a complete charge spectrum

**`SuperSymmetry.SU5.ChargeSpectrum.completions_eq_singleton_of_complete`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Completions.lean#L188).

> The completions of a complete charge spectrum is just the singleton containing itself.

```lean
lemma completions_eq_singleton_of_complete {S5 S10 : Finset 𝓩} (x : ChargeSpectrum 𝓩)
    (hcomplete : IsComplete x) :
    completions S5 S10 x = {x}
```

### B.4. Membership of own completions

**`SuperSymmetry.SU5.ChargeSpectrum.self_mem_completions_iff_isComplete`**, a lemma, [line 213](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Completions.lean#L213).

> If a charge spectrum `x` is a member of its own completion then it is complete,
> and vice versa.

```lean
lemma self_mem_completions_iff_isComplete {S5 S10 : Finset 𝓩} (x : ChargeSpectrum 𝓩) :
    x ∈ completions S5 S10 x ↔ IsComplete x
```

### B.5. Completeness of members of completions

> We now show that any member of the completions of a charge spectrum is complete.

**`SuperSymmetry.SU5.ChargeSpectrum.mem_completions_isComplete`**, a lemma, [line 236](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Completions.lean#L236).

> A charge spectrum which is a member of the completions of another charge
> spectrum is complete.

```lean
lemma mem_completions_isComplete {S5 S10 : Finset 𝓩} {x y : ChargeSpectrum 𝓩}
    (hx : y ∈ completions S5 S10 x) : IsComplete y
```

### B.6. Subset of members of completions

> We show that any member of the completions of a charge spectrum is a super set of that
> charge spectrum.

**`SuperSymmetry.SU5.ChargeSpectrum.self_subset_mem_completions`**, a lemma, [line 281](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Completions.lean#L281).

> If `y` is in the completions of `x` then `x ⊆ y`.

```lean
lemma self_subset_mem_completions (S5 S10 : Finset 𝓩) (x y : ChargeSpectrum 𝓩)
    (hy : y ∈ completions S5 S10 x) : x ⊆ y
```

**`SuperSymmetry.SU5.ChargeSpectrum.exist_completions_subset_of_complete`**, a lemma, [line 302](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Completions.lean#L302).

> If `x` is a subset of `y` and `y` is complete, then there is a completion of `x` which is also
> a subset of `y`.

```lean
lemma exist_completions_subset_of_complete (S5 S10 : Finset 𝓩) (x y : ChargeSpectrum 𝓩)
    (hsubset : x ⊆ y) (hy : y ∈ ofFinset S5 S10) (hycomplete : IsComplete y) :
    ∃ z ∈ completions S5 S10 x, z ⊆ y
```

## C. Completions for top Yukawa

> We give a fast version of `completions` in the case when `x` has a `qHu` charge,
> and a non-empty set of `10` charges, but does not have a `qHd` charge or any `5`-bar charges.
> Here we only need to specify the allowed `5`-bar charges, not the allowed `10` charges.
>
> This is the case for charges which minimally allow the top Yukawa coupling.
>
> These definitions are primarily for speed, as this is the most common case we will
> look at.

**`SuperSymmetry.SU5.ChargeSpectrum.completionsTopYukawa`**, a def, [line 366](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Completions.lean#L366).

> A fast version of `completions` for an `x` which is in
> `minimallyAllowsTermsOfFinset S5 S10 .topYukawa`.

```lean
def completionsTopYukawa (S5 : Finset 𝓩) (x : ChargeSpectrum 𝓩) :
    Multiset (ChargeSpectrum 𝓩)
```

### C.1. No duplicates in completionsTopYukawa

> Like for `completions`, we define `completionsTopYukawa` as a multiset for speed,
> however, we can show it has no duplicates.

**`SuperSymmetry.SU5.ChargeSpectrum.completionsTopYukawa_nodup`**, a lemma, [line 381](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Completions.lean#L381).

> The multiset `completionsTopYukawa S5 x` has no duplicates.

```lean
lemma completionsTopYukawa_nodup {S5 : Finset 𝓩} (x : ChargeSpectrum 𝓩) :
    (completionsTopYukawa S5 x).Nodup
```

### C.2. Equivalence of completions and completionsTopYukawa

> For charges `x` which are in `minimallyAllowsTermsOfFinset S5 S10 .topYukawa`,
> we show that `completions S5 S10 x` and `completionsTopYukawa S5 x` are equal multisets.

**`SuperSymmetry.SU5.ChargeSpectrum.completions_eq_completionsTopYukawa_of_mem_minimallyAllowsTermsOfFinset`**, a lemma, [line 401](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Completions.lean#L401).

> The multisets `completions S5 S10 x` and `completionsTopYukawa S5 x` are equivalent if
> `x` minimally allows the top Yukawa.

```lean
lemma completions_eq_completionsTopYukawa_of_mem_minimallyAllowsTermsOfFinset [AddCommGroup 𝓩]
    {S5 S10 : Finset 𝓩} (x : ChargeSpectrum 𝓩)
    (hx : x ∈ minimallyAllowsTermsOfFinset S5 S10 .topYukawa) :
    completions S5 S10 x = completionsTopYukawa S5 x
```

## Depends on

- [The set of charges which minimally allows a potential term](../part-02/su5-chargespectrum-minimallyallowsterm-offinset.md)

## Sources

- [Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Completions.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Completions.lean)
