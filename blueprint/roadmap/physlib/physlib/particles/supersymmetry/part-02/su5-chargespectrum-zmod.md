---
declaration: module
origin: cited
lean: SuperSymmetry.SU5.ChargeSpectrum.ZModCharges, SuperSymmetry.SU5.ChargeSpectrum.ZModCharges_one_eq, SuperSymmetry.SU5.ChargeSpectrum.ZModCharges_two_eq, SuperSymmetry.SU5.ChargeSpectrum.ZModCharges_three_eq, SuperSymmetry.SU5.ChargeSpectrum.ZModCharges_four_eq, SuperSymmetry.SU5.ChargeSpectrum.ZModCharges_five_eq, SuperSymmetry.SU5.ChargeSpectrum.ZModCharges_six_eq, SuperSymmetry.SU5.ChargeSpectrum.ZModZModCharges
statement: formalized
proof: formalized
---

# Charge spectra with values in `ZMod n`

The module `Physlib.Particles.SuperSymmetry.SU5.ChargeSpectrum.ZMod`, [Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/ZMod.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/ZMod.lean): 8 declarations, 6 with a docstring.

## i. Overview

> The way that we have defined `ChargeSpectrum` means we can consider values
> of charges which are not only elements of `ℤ`, but also elements of other types.
>
> In this file we will consider `ChargeSpectrum` which have values in `ZMod n` for various
> natural numbers `n`, as well as charge spectra with values in `ZMod n × ZMod m`.
>
> In this file we focus on 4-insertions of singlets to be phenomenologically viable.
> In other files we usually just consider one.

## ii. Key results

> - `ZModCharges n` : The finite set of `ZMod n` valued charges which are complete,
>   not pheno-constrained and don't regenerate dangerous couplings
>   with the Yukawa term up-to 4-inserstions of singlets.
> - `ZModZModCharges m n` : The finite set of `ZMod n × ZMod m` valued charges which are complete,
>   not pheno-constrained and don't regenerate dangerous couplings
>   with the Yukawa term up-to 4-inserstions of singlets.

## iv. References

> * None.

## A. The finite set of viable `ZMod n` charge spectra

### A.1. General construction

**`SuperSymmetry.SU5.ChargeSpectrum.ZModCharges`**, a def, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/ZMod.lean#L80).

> The finite set of `ZMod n` valued charges which are complete,
> not pheno-constrained and don't regenerate dangerous couplings
> with the Yukawa term up-to 4-inserstions of singlets.

```lean
def ZModCharges (n : ℕ) [NeZero n] : Finset (ChargeSpectrum (ZMod n))
```

### A.2. Finite set of viable `ZMod 1` charge spectra is empty

**`SuperSymmetry.SU5.ChargeSpectrum.ZModCharges_one_eq`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/ZMod.lean#L92).

> This lemma corresponds to the statement that there are no choices of `ℤ₁` representations
> which give a phenomenologically viable theory.

```lean
lemma ZModCharges_one_eq : ZModCharges 1 = ∅
```

### A.3. Finite set of viable `ZMod 2` charge spectra is empty

**`SuperSymmetry.SU5.ChargeSpectrum.ZModCharges_two_eq`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/ZMod.lean#L103).

> This lemma corresponds to the statement that there are no choices of `ℤ₂` representations
> which give a phenomenologically viable theory.

```lean
lemma ZModCharges_two_eq : ZModCharges 2 = ∅
```

### A.4. Finite set of viable `ZMod 3` charge spectra is empty

**`SuperSymmetry.SU5.ChargeSpectrum.ZModCharges_three_eq`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/ZMod.lean#L114).

> This lemma corresponds to the statement that there are no choices of `ℤ₃` representations
> which give a phenomenologically viable theory.

```lean
lemma ZModCharges_three_eq : ZModCharges 3 = ∅
```

### A.5. Finite set of viable `ZMod 4` has four elements

**`SuperSymmetry.SU5.ChargeSpectrum.ZModCharges_four_eq`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/ZMod.lean#L123).

```lean
lemma ZModCharges_four_eq : ZModCharges 4 = {⟨some 0, some 2, {1}, {3}⟩,
    ⟨some 0, some 2, {3}, {1}⟩, ⟨some 1, some 2, {0}, {3}⟩, ⟨some 3, some 2, {0}, {1}⟩}
```

### A.6. Finite set of viable `ZMod 5` charge spectra is empty (pseudo result)

**`SuperSymmetry.SU5.ChargeSpectrum.ZModCharges_five_eq`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/ZMod.lean#L136).

> This lemma corresponds to the statement that there are no choices of `ℤ₅` representations
> which give a phenomenologically viable theory.

```lean
lemma ZModCharges_five_eq : ZModCharges 5 = ∅
```

### A.7. Finite set of viable `ZMod 6` charge spectra is non-empty (pseudo result)

**`SuperSymmetry.SU5.ChargeSpectrum.ZModCharges_six_eq`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/ZMod.lean#L145).

```lean
lemma ZModCharges_six_eq : ZModCharges 6 = {⟨some 0, some 2, {5}, {1}⟩,
    ⟨some 0, some 4, {1}, {5}⟩, ⟨some 1, some 0, {2}, {3}⟩, ⟨some 1, some 2, {4}, {1}⟩,
    ⟨some 1, some 4, {0}, {5}⟩, ⟨some 1, some 4, {3}, {2}⟩, ⟨some 2, some 0, {1}, {3}⟩,
    ⟨some 2, some 4, {5}, {5}⟩, ⟨some 3, some 2, {5}, {4}⟩, ⟨some 3, some 4, {1}, {2}⟩,
    ⟨some 4, some 0, {5}, {3}⟩, ⟨some 4, some 2, {1}, {1}⟩, ⟨some 5, some 0, {4}, {3}⟩,
    ⟨some 5, some 2, {0}, {1}⟩, ⟨some 5, some 2, {3}, {4}⟩, ⟨some 5, some 4, {2}, {5}⟩}
```

## B. The finite set of viable `ZMod n × ZMod m` charge spectra

### B.1. General construction

**`SuperSymmetry.SU5.ChargeSpectrum.ZModZModCharges`**, a def, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/ZMod.lean#L168).

> The finite set of `ZMod n × ZMod m` valued charges which are complete,
> not pheno-constrained and don't regenerate dangerous couplings
> with the Yukawa term up-to 4-inserstions of singlets.

```lean
def ZModZModCharges (n m : ℕ) [NeZero n] [NeZero m] : Finset (ChargeSpectrum (ZMod n × ZMod m))
```

## Depends on

- [Completions of charges](../part-01/su5-chargespectrum-completions.md)
- [Yukawa charges](su5-chargespectrum-yukawa.md)

## Sources

- [Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/ZMod.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/ZMod.lean)
