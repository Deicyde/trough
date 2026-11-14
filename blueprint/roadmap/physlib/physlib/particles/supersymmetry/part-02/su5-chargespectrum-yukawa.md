---
declaration: module
origin: cited
lean: SuperSymmetry.SU5.ChargeSpectrum.ofYukawaTerms, SuperSymmetry.SU5.ChargeSpectrum.ofYukawaTerms_subset_of_subset, SuperSymmetry.SU5.ChargeSpectrum.ofYukawaTermsNSum, SuperSymmetry.SU5.ChargeSpectrum.ofYukawaTermsNSum_subset_of_subset, SuperSymmetry.SU5.ChargeSpectrum.YukawaGeneratesDangerousAtLevel, SuperSymmetry.SU5.ChargeSpectrum.YukawaGeneratesDangerousAtLevel_iff_inter, SuperSymmetry.SU5.ChargeSpectrum.yukawaGeneratesDangerousAtLevel_iff_toFinset, SuperSymmetry.SU5.ChargeSpectrum.not_yukawaGeneratesDangerousAtLevel_of_empty
statement: formalized
proof: formalized
---

# Yukawa charges

The module `Physlib.Particles.SuperSymmetry.SU5.ChargeSpectrum.Yukawa`, [Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Yukawa.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Yukawa.lean): 13 declarations (1 instance with no name), 3 with a docstring.

## i. Overview

> In this module we look at the charges associated with the Yukawa terms
> in the super potential, and when they can regenerate
> phenomenologically constrained super-potential terms at different levels.
>
> We do not not consider the regeneration of terms in the Kähler potential within
> this module.

## ii. Key results

> - `ofYukawaTerms`: the multiset of charges associated with the Yukawa terms
> - `ofYukawaTermsNSum`: the multiset of charges associated with up-to `n` copies of the Yukawa terms
>   or equivalently the charges of singlet insertions needed to regenerate Yukawa terms.
> - `YukawaGeneratesDangerousAtLevel`: the proposition that a charge spectrum regenerates a
>   phenomenologically constrained term in the super-potential
>   with up-to `n` insertions of singlets needed to regenerate
>   the Yukawa terms.

## iv. References

> * None.

## A. Charges of the Yukawa terms

**`SuperSymmetry.SU5.ChargeSpectrum.ofYukawaTerms`**, a def, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Yukawa.lean#L68).

> The collection of charges associated with Yukawa terms.
> Correspondingly, the (negative) of the charges of the singlets needed to regenerate all
> Yukawa terms in the potential.

```lean
def ofYukawaTerms (x : ChargeSpectrum 𝓩) : Multiset 𝓩
```

### A.1. Monotonicity of charges of the Yukawa terms

**`SuperSymmetry.SU5.ChargeSpectrum.ofYukawaTerms_subset_of_subset`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Yukawa.lean#L77).

```lean
lemma ofYukawaTerms_subset_of_subset [DecidableEq 𝓩] {x y : ChargeSpectrum 𝓩} (h : x ⊆ y) :
    x.ofYukawaTerms ⊆ y.ofYukawaTerms
```

### A.2. upto n-copies of charges of the Yukawa terms (aka charges of singlet insertions)

**`SuperSymmetry.SU5.ChargeSpectrum.ofYukawaTermsNSum`**, a def, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Yukawa.lean#L102).

> The charges of those terms which can be regenerated with up-to `n`
> insertions of singlets needed to regenerate the Yukawa terms.
> Equivalently, the sum of up-to `n` integers each corresponding to a charge of the
> Yukawa terms.

```lean
def ofYukawaTermsNSum (x : ChargeSpectrum 𝓩) : ℕ → Multiset 𝓩
```

### A.3. Monotonicity of set of charges of upto n-copies of the Yukawa terms

**`SuperSymmetry.SU5.ChargeSpectrum.ofYukawaTermsNSum_subset_of_subset`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Yukawa.lean#L113).

```lean
lemma ofYukawaTermsNSum_subset_of_subset [DecidableEq 𝓩] {x y : ChargeSpectrum 𝓩}
    (h : x ⊆ y) (n : ℕ) :
    x.ofYukawaTermsNSum n ⊆ y.ofYukawaTermsNSum n
```

## B. Regeneration of phenomenologically constrained terms via upto n Yukawa singlet insertions

**`SuperSymmetry.SU5.ChargeSpectrum.YukawaGeneratesDangerousAtLevel`**, a def, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Yukawa.lean#L150).

> For a charge spectrum `x : ChargeSpectrum 𝓩`, the proposition which states that the singlets
> needed to regenerate the Yukawa couplings regenerate a dangerous coupling
> (in the superpotential) with up-to `n` insertions of the scalars.
>
> Note: If defined as (x.ofYukawaTermsNSum n).toFinset ∩ x.phenoConstrainingChargesSP.toFinset ≠ ∅
> the execution time is greatly increased.

```lean
def YukawaGeneratesDangerousAtLevel (x : ChargeSpectrum 𝓩) (n : ℕ) : Prop
```

### B.1. Decidability of `YukawaGeneratesDangerousAtLevel`

**An instance with no name**, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Yukawa.lean#L159).

```lean
instance (x : ChargeSpectrum 𝓩) (n : ℕ) : Decidable (YukawaGeneratesDangerousAtLevel x n)
```

### B.2. Simplifications of condition for regenerating dangerous terms

**`SuperSymmetry.SU5.ChargeSpectrum.YukawaGeneratesDangerousAtLevel_iff_inter`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Yukawa.lean#L169).

```lean
lemma YukawaGeneratesDangerousAtLevel_iff_inter {x : ChargeSpectrum 𝓩} {n : ℕ} :
    YukawaGeneratesDangerousAtLevel x n ↔
    (x.ofYukawaTermsNSum n) ∩ x.phenoConstrainingChargesSP ≠ ∅
```

**`SuperSymmetry.SU5.ChargeSpectrum.yukawaGeneratesDangerousAtLevel_iff_toFinset`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Yukawa.lean#L173).

```lean
lemma yukawaGeneratesDangerousAtLevel_iff_toFinset (x : ChargeSpectrum 𝓩) (n : ℕ) :
    x.YukawaGeneratesDangerousAtLevel n ↔
    (x.ofYukawaTermsNSum n).toFinset ∩ x.phenoConstrainingChargesSP.toFinset ≠ ∅
```

### B.3. Empty charge spectrum does not regenerate dangerous terms

**`SuperSymmetry.SU5.ChargeSpectrum.not_yukawaGeneratesDangerousAtLevel_of_empty`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Yukawa.lean#L204).

```lean
lemma not_yukawaGeneratesDangerousAtLevel_of_empty (n : ℕ) :
    ¬ YukawaGeneratesDangerousAtLevel (∅ : ChargeSpectrum 𝓩) n
```

### B.4. Monotonicity of regeneration of dangerous terms in charge spectra

> If `x` regenerates a dangerous term with up-to `n` insertions of Yukawa singlets,
> and `x ⊆ y`, then `y` also regenerates a dangerous term with up-to `n` insertions.

**`SuperSymmetry.SU5.ChargeSpectrum.yukawaGeneratesDangerousAtLevel_of_subset`**, a lemma, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Yukawa.lean#L217).

```lean
lemma yukawaGeneratesDangerousAtLevel_of_subset {x y : ChargeSpectrum 𝓩} {n : ℕ} (h : x ⊆ y)
    (hx : x.YukawaGeneratesDangerousAtLevel n) :
    y.YukawaGeneratesDangerousAtLevel n
```

### B.5. Monotonicity of regeneration of dangerous terms in level

> If `x` regenerates a dangerous term with up-to `n` insertions of Yukawa singlets,
> then `x` also regenerates a dangerous term with up-to `n + 1` insertions.

**`SuperSymmetry.SU5.ChargeSpectrum.yukawaGeneratesDangerousAtLevel_succ`**, a lemma, [line 245](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Yukawa.lean#L245).

```lean
lemma yukawaGeneratesDangerousAtLevel_succ {x : ChargeSpectrum 𝓩} {n : ℕ}
    (hx : x.YukawaGeneratesDangerousAtLevel n) :
    x.YukawaGeneratesDangerousAtLevel (n + 1)
```

**`SuperSymmetry.SU5.ChargeSpectrum.yukawaGeneratesDangerousAtLevel_add_of_left`**, a lemma, [line 256](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Yukawa.lean#L256).

```lean
lemma yukawaGeneratesDangerousAtLevel_add_of_left {x : ChargeSpectrum 𝓩} {n k : ℕ}
    (hx : x.YukawaGeneratesDangerousAtLevel n) :
    x.YukawaGeneratesDangerousAtLevel (n + k)
```

**`SuperSymmetry.SU5.ChargeSpectrum.yukawaGeneratesDangerousAtLevel_of_le`**, a lemma, [line 263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Yukawa.lean#L263).

```lean
lemma yukawaGeneratesDangerousAtLevel_of_le {x : ChargeSpectrum 𝓩} {n m : ℕ}
    (h : n ≤ m) (hx : x.YukawaGeneratesDangerousAtLevel n) :
    x.YukawaGeneratesDangerousAtLevel m
```

## Depends on

- [Pheno constrained charge spectra](su5-chargespectrum-phenoconstrained.md)

## Sources

- [Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Yukawa.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Yukawa.lean)
