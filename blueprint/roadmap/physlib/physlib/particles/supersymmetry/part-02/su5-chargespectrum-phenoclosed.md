---
declaration: module
origin: cited
lean: SuperSymmetry.SU5.ChargeSpectrum.IsPhenoClosedQ5, SuperSymmetry.SU5.ChargeSpectrum.isPhenClosedQ5_of_isPhenoConstrainedQ5, SuperSymmetry.SU5.ChargeSpectrum.IsPhenoClosedQ10, SuperSymmetry.SU5.ChargeSpectrum.isPhenClosedQ10_of_isPhenoConstrainedQ10, SuperSymmetry.SU5.ChargeSpectrum.ContainsPhenoCompletionsOfMinimallyAllows, SuperSymmetry.SU5.ChargeSpectrum.containsPhenoCompletionsOfMinimallyAllows_iff_completionsTopYukawa, SuperSymmetry.SU5.ChargeSpectrum.containsPhenoCompletionsOfMinimallyAllows_of_subset, SuperSymmetry.SU5.ChargeSpectrum.completeMinSubset
statement: formalized
proof: formalized
---

# Phenomenologically closed sets of charge spectra

The module `Physlib.Particles.SuperSymmetry.SU5.ChargeSpectrum.PhenoClosed`, [Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/PhenoClosed.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/PhenoClosed.lean): 14 declarations (1 instance with no name), 5 with a docstring.

## i. Overview

> The main goal of this file is to prove the lemma
> `completeness_of_isPhenoClosedQ5_isPhenoClosedQ10`, which
> allows us to prove that a multiset of charge spectra contains all
> phenomenologically viable charge spectra, given a finite set of allowed
> `5`-bar and `10`-dimensional.
>
> This lemma relies on the multiset of charge spectra satisfying a number of conditions,
> which include three which are defined in this file: `IsPhenoClosedQ5`, `IsPhenoClosedQ10` and
> `ContainsPhenoCompletionsOfMinimallyAllows`.

## ii. Key results

> - `IsPhenoClosedQ5` : The proposition that a multiset of charges is phenomenologically closed
>   under addition of `5`-bar charges from a finite set `S5`.
> - `IsPhenoClosedQ10` : The proposition that a multiset of charges is phenomenologically closed
>   under addition of `10`-dimensional charges from a finite set `S10`.
> - `ContainsPhenoCompletionsOfMinimallyAllows` : The proposition that a multiset of charges
>   contains all phenomenologically viable completions of charge spectra which permit the
>   top Yukawa.
> - `completeMinSubset` : For a given `S5 S10 : Finset 𝓩`,
>   the minimal multiset of charges which satisfies the condition
>   `ContainsPhenoCompletionsOfMinimallyAllows`.
> - `completeness_of_isPhenoClosedQ5_isPhenoClosedQ10` : A lemma for simplifying the proof
>   that a multiset contains all phenomenologically viable charge spectra.
> - `viableChargesMultiset` : A computable multiset containing all phenomenologically viable
>   charge spectra for a given `S5 S10 : Finset 𝓩`.

## iv. References

> * None.

## A. Phenomenologically closed under additions of 5-bar charges

**`SuperSymmetry.SU5.ChargeSpectrum.IsPhenoClosedQ5`**, a def, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/PhenoClosed.lean#L86).

> The proposition that for multiset set of charges `charges`,
> adding individual elements of `S5` to the `Q5` charges of elements of `charges` again
> leads to an element in `charges` or a charge which is phenomenologically constrained,
> or regenerates dangerous couplings with one singlet insertion.

```lean
def IsPhenoClosedQ5 (S5 : Finset 𝓩) (charges : Multiset (ChargeSpectrum 𝓩)) : Prop
```

### A.1. Simplification using pheno-constrained due to additional of 5-bar charge

**`SuperSymmetry.SU5.ChargeSpectrum.isPhenClosedQ5_of_isPhenoConstrainedQ5`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/PhenoClosed.lean#L97).

```lean
lemma isPhenClosedQ5_of_isPhenoConstrainedQ5 {S5 : Finset 𝓩} {charges : Multiset (ChargeSpectrum 𝓩)}
    (h : ∀ q5 ∈ S5, ∀ x ∈ charges,
      let y : ChargeSpectrum 𝓩 := ⟨x.qHd, x.qHu, insert q5 x.Q5, x.Q10⟩
      IsPhenoConstrainedQ5 x q5 ∨ y ∈ charges ∨ YukawaGeneratesDangerousAtLevel y 1) :
    IsPhenoClosedQ5 S5 charges
```

## B. Phenomenologically closed under additions of 10d charges

**`SuperSymmetry.SU5.ChargeSpectrum.IsPhenoClosedQ10`**, a def, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/PhenoClosed.lean#L121).

> The proposition that for multiset set of charges `charges`,
> adding individual elements of `S10` to the `Q10` charges of elements of `charges` again
> leads to an element in `charges` or a charge which is phenomenologically constrained,
> or regenerates dangerous couplings with one singlet insertion.

```lean
def IsPhenoClosedQ10 (S10 : Finset 𝓩) (charges : Multiset (ChargeSpectrum 𝓩)) : Prop
```

### B.1. Simplification using pheno-constrained due to additional of 10d charge

**`SuperSymmetry.SU5.ChargeSpectrum.isPhenClosedQ10_of_isPhenoConstrainedQ10`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/PhenoClosed.lean#L132).

```lean
lemma isPhenClosedQ10_of_isPhenoConstrainedQ10 {S10 : Finset 𝓩}
    {charges : Multiset (ChargeSpectrum 𝓩)}
    (h : ∀ q10 ∈ S10, ∀ x ∈ charges,
      let y : ChargeSpectrum 𝓩 := ⟨x.qHd, x.qHu, x.Q5, insert q10 x.Q10⟩
      IsPhenoConstrainedQ10 x q10 ∨ y ∈ charges ∨ YukawaGeneratesDangerousAtLevel y 1) :
    IsPhenoClosedQ10 S10 charges
```

## C. Prop for multiset containing all pheno-viable completions of charges permitting top Yukawa

**`SuperSymmetry.SU5.ChargeSpectrum.ContainsPhenoCompletionsOfMinimallyAllows`**, a def, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/PhenoClosed.lean#L157).

> The proposition that for multiset set of charges `charges` contains all
> viable completions of charges which allow the top Yukawa, given allowed values
> of `5`d and `10`d charges `S5` and `S10`.

```lean
def ContainsPhenoCompletionsOfMinimallyAllows (S5 S10 : Finset 𝓩)
    (charges : Multiset (ChargeSpectrum 𝓩)) : Prop
```

### C.1. Simplification using fast version of completions of charges permitting top Yukawa

**`SuperSymmetry.SU5.ChargeSpectrum.containsPhenoCompletionsOfMinimallyAllows_iff_completionsTopYukawa`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/PhenoClosed.lean#L169).

```lean
lemma containsPhenoCompletionsOfMinimallyAllows_iff_completionsTopYukawa {S5 S10 : Finset 𝓩}
    {charges : Multiset (ChargeSpectrum 𝓩)} :
    ContainsPhenoCompletionsOfMinimallyAllows S5 S10 charges ↔
    ∀ x ∈ (minimallyAllowsTermsOfFinset S5 S10 topYukawa),
    ∀ y ∈ completionsTopYukawa S5 x, ¬ y.IsPhenoConstrained
      ∧ ¬ y.YukawaGeneratesDangerousAtLevel 1 → y ∈ charges
```

### C.2. Decidability of proposition

**An instance with no name**, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/PhenoClosed.lean#L192).

```lean
instance {S5 S10 : Finset 𝓩} {charges : Multiset (ChargeSpectrum 𝓩)} :
    Decidable (ContainsPhenoCompletionsOfMinimallyAllows S5 S10 charges)
```

### C.3. Monotonicity of proposition

**`SuperSymmetry.SU5.ChargeSpectrum.containsPhenoCompletionsOfMinimallyAllows_of_subset`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/PhenoClosed.lean#L202).

```lean
lemma containsPhenoCompletionsOfMinimallyAllows_of_subset {S5 S10 : Finset 𝓩}
    {charges charges' : Multiset (ChargeSpectrum 𝓩)}
    (h' : ContainsPhenoCompletionsOfMinimallyAllows S5 S10 charges)
    (h : ∀ x ∈ charges, x ∈ charges') :
    ContainsPhenoCompletionsOfMinimallyAllows S5 S10 charges'
```

### C.4. `completeMinSubset`: Minimal multiset with viable completions of top-permitting charges

**`SuperSymmetry.SU5.ChargeSpectrum.completeMinSubset`**, a def, [line 218](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/PhenoClosed.lean#L218).

> For a given `S5 S10 : Finset 𝓩`, the minimal multiset of charges which satisfies
> the condition `ContainsPhenoCompletionsOfMinimallyAllows`.
> That is to say, every multiset of charges which satisfies
> `ContainsPhenoCompletionsOfMinimallyAllows` has `completeMinSubset` as a subset.

```lean
def completeMinSubset (S5 S10 : Finset 𝓩) : Multiset (ChargeSpectrum 𝓩)
```

#### C.4.1. The multiset `completeMinSubset` has no duplicates

**`SuperSymmetry.SU5.ChargeSpectrum.completeMinSubset_nodup`**, a lemma, [line 229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/PhenoClosed.lean#L229).

```lean
lemma completeMinSubset_nodup {S5 S10 : Finset 𝓩} :
    (completeMinSubset S5 S10).Nodup
```

#### C.4.2. The multiset `completeMinSubset` is minimal

**`SuperSymmetry.SU5.ChargeSpectrum.completeMinSubset_subset_iff_containsPhenoCompletionsOfMinimallyAllows`**, a lemma, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/PhenoClosed.lean#L242).

```lean
lemma completeMinSubset_subset_iff_containsPhenoCompletionsOfMinimallyAllows
    (S5 S10 : Finset 𝓩) (charges : Multiset (ChargeSpectrum 𝓩)) :
    completeMinSubset S5 S10 ⊆ charges ↔
    ContainsPhenoCompletionsOfMinimallyAllows S5 S10 charges
```

#### C.4.3. The multiset `completeMinSubset` contains all completions

**`SuperSymmetry.SU5.ChargeSpectrum.completeMinSubset_containsPhenoCompletionsOfMinimallyAllows`**, a lemma, [line 267](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/PhenoClosed.lean#L267).

```lean
lemma completeMinSubset_containsPhenoCompletionsOfMinimallyAllows (S5 S10 : Finset 𝓩) :
    ContainsPhenoCompletionsOfMinimallyAllows S5 S10 (completeMinSubset S5 S10)
```

## D. Multisets containing all pheno-viable charge spectra

### D.1. Lemma for simplifying proof that a multiset contains all pheno-viable charge spectra

> The multiset of charges `charges` contains precisely those charges (given a finite set
> of allowed charges) which
> - allow the top Yukawa term,
> - are not phenomenologically constrained,
> - do not generate dangerous couplings with one singlet insertion,
> - and are complete,
> if the following conditions hold:
> - every element of `charges` allows the top Yukawa term,
> - every element of `charges` is not phenomenologically constrained,
> - every element of `charges` does not generate dangerous couplings with one singlet insertion,
> - every element of `charges` is complete,
> - `charges` is `IsPhenoClosedQ5` with respect to `S5`,
> - `charges` is `IsPhenoClosedQ10` with respect to `S10`
> - and satisfies `ContainsPhenoCompletionsOfMinimallyAllows S5 S10 charges`.
> The importance of this lemma is that it is only regarding properties of finite-set `charges`
> not of the whole space of possible charges.

**`SuperSymmetry.SU5.ChargeSpectrum.completeness_of_isPhenoClosedQ5_isPhenoClosedQ10`**, a lemma, [line 302](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/PhenoClosed.lean#L302).

```lean
lemma completeness_of_isPhenoClosedQ5_isPhenoClosedQ10
    {S5 S10 : Finset 𝓩} {charges : Multiset (ChargeSpectrum 𝓩)}
    (charges_topYukawa : ∀ x ∈ charges, x.AllowsTerm .topYukawa)
    (charges_not_isPhenoConstrained : ∀ x ∈ charges, ¬ x.IsPhenoConstrained)
    (charges_yukawa : ∀ x ∈ charges, ¬ x.YukawaGeneratesDangerousAtLevel 1)
    (charges_complete : ∀ x ∈ charges, x.IsComplete)
    (charges_isPhenoClosedQ5 : IsPhenoClosedQ5 S5 charges)
    (charges_isPhenoClosedQ10 : IsPhenoClosedQ10 S10 charges)
    (charges_exist : ContainsPhenoCompletionsOfMinimallyAllows S5 S10 charges)
    {x : ChargeSpectrum 𝓩} (hsub : x ∈ ofFinset S5 S10) :
    x ∈ charges ↔ AllowsTerm x .topYukawa ∧
    ¬ IsPhenoConstrained x ∧ ¬ YukawaGeneratesDangerousAtLevel x 1 ∧ IsComplete x
```

### D.2. Computable multiset containing all pheno-viable charge spectra

**`SuperSymmetry.SU5.ChargeSpectrum.viableChargesMultiset`**, a def, [line 398](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/PhenoClosed.lean#L398).

> All charges, for a given `S5 S10 : Finset 𝓩`,
> which permit a top Yukawa coupling, are not phenomenologically constrained,
> and do not regenerate dangerous couplings with one insertion of a Yukawa coupling.
>
> This is the unique multiset without duplicates which satisfies:
> `completeness_of_isPhenoClosedQ5_isPhenoClosedQ10`.
>
> Note this is fast for evaluation, but to slow with `decide`.

```lean
unsafe def viableChargesMultiset (S5 S10 : Finset 𝓩) :
    Multiset (ChargeSpectrum 𝓩)
```

## Depends on

- [Minimal super set](../part-01/su5-chargespectrum-minimalsuperset.md)
- [Yukawa charges](su5-chargespectrum-yukawa.md)

## Sources

- [Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/PhenoClosed.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/PhenoClosed.lean)
