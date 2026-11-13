---
declaration: module
origin: cited
lean: SuperSymmetry.SU5.ChargeSpectrum.IsPhenoConstrained, SuperSymmetry.SU5.ChargeSpectrum.decidableIsPhenoConstrained, SuperSymmetry.SU5.ChargeSpectrum.not_isPhenoConstrained_empty, SuperSymmetry.SU5.ChargeSpectrum.isPhenoConstrained_mono, SuperSymmetry.SU5.ChargeSpectrum.phenoConstrainingChargesSP, SuperSymmetry.SU5.ChargeSpectrum.phenoConstrainingChargesSP_empty, SuperSymmetry.SU5.ChargeSpectrum.phenoConstrainingChargesSP_mono, SuperSymmetry.SU5.ChargeSpectrum.IsPhenoConstrainedQ5
statement: formalized
proof: formalized
---

# Pheno constrained charge spectra

The module `Physlib.Particles.SuperSymmetry.SU5.ChargeSpectrum.PhenoConstrained`, [Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/PhenoConstrained.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/PhenoConstrained.lean): 15 declarations, 4 with a docstring.

## i. Overview

> We define a predicate `IsPhenoConstrained` on `ChargeSpectrum 𝓩` which is true if the charge
> spectrum allows any super-potential or Kähler potential term leading to proton decay or
> R-parity violation.
>
> We prove basic properties of this predicate including monotonicity.
>
> We define some variations of this result.

## ii. Key results

> - `IsPhenoConstrained`: The predicate defining a pheno-constrained charge spectrum
>   as one allowing any term leading to proton decay or R-parity violation.
> - `phenoConstrainingChargesSP`: The multiset of charges of terms in the super-potential
>   leading to a pheno-constrained charge spectrum.
> - `IsPhenoConstrainedQ5`: The predicate defining when a charge spectrum becomes
>   pheno-constrained after adding a single charge to the `Q5` set.
> - `IsPhenoConstrainedQ10`: The predicate defining when a charge spectrum becomes
>   pheno-constrained after adding a single charge to the `Q10` set.

## iv. References

> * None.

## A. Phenomenological constrained charge spectra

**`SuperSymmetry.SU5.ChargeSpectrum.IsPhenoConstrained`**, a def, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/PhenoConstrained.lean#L76).

> A charge is pheno-constrained if it leads to the presence of any term causing proton decay
> ` {W1, Λ, W2, K1}` or R-parity violation `{β, Λ, W2, W4, K1, K2}`.

```lean
def IsPhenoConstrained (x : ChargeSpectrum 𝓩) : Prop
```

### A.1. Decidability of `IsPhenoConstrained`

**`SuperSymmetry.SU5.ChargeSpectrum.decidableIsPhenoConstrained`**, an instance, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/PhenoConstrained.lean#L86).

```lean
instance decidableIsPhenoConstrained [DecidableEq 𝓩] (x : ChargeSpectrum 𝓩) :
    Decidable x.IsPhenoConstrained
```

### A.2. The empty charge spectrum is not pheno-constrained

> The empty charge spectrum does not allow any terms, and so is not pheno-constrained.

**`SuperSymmetry.SU5.ChargeSpectrum.not_isPhenoConstrained_empty`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/PhenoConstrained.lean#L100).

```lean
lemma not_isPhenoConstrained_empty :
    ¬ IsPhenoConstrained (∅ : ChargeSpectrum 𝓩)
```

### A.3. Monotonicity of being pheno-constrained

> If a charge spectrum `x` is pheno-constrained, then any charge spectrum `y` containing `x`
> is also pheno-constrained.

**`SuperSymmetry.SU5.ChargeSpectrum.isPhenoConstrained_mono`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/PhenoConstrained.lean#L113).

```lean
lemma isPhenoConstrained_mono {x y : ChargeSpectrum 𝓩} (h : x ⊆ y)
    (hx : x.IsPhenoConstrained) : y.IsPhenoConstrained
```

## B. Charges of pheno-constraining terms in the super potential

**`SuperSymmetry.SU5.ChargeSpectrum.phenoConstrainingChargesSP`**, a def, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/PhenoConstrained.lean#L128).

> The collection of charges of super-potential terms leading to a pheno-constrained model.

```lean
def phenoConstrainingChargesSP (x : ChargeSpectrum 𝓩) : Multiset 𝓩
```

### B.1. The empty charge spectrum has an empty set of pheno-constraining term charges

**`SuperSymmetry.SU5.ChargeSpectrum.phenoConstrainingChargesSP_empty`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/PhenoConstrained.lean#L139).

```lean
lemma phenoConstrainingChargesSP_empty :
    phenoConstrainingChargesSP (∅ : ChargeSpectrum 𝓩) = ∅
```

### B.2. The charges of pheno-constraining terms in the SP is monotone

**`SuperSymmetry.SU5.ChargeSpectrum.phenoConstrainingChargesSP_mono`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/PhenoConstrained.lean#L148).

```lean
lemma phenoConstrainingChargesSP_mono [DecidableEq 𝓩] {x y : ChargeSpectrum 𝓩} (h : x ⊆ y) :
    x.phenoConstrainingChargesSP ⊆ y.phenoConstrainingChargesSP
```

## C. Phenomenologically constrained charge spectra after adding a single Q5 charge

> We now define `IsPhenoConstrainedQ5` which gives the condition that a charge spectrum becomes
> pheno-constrained after adding a single charge to the `Q5` set.

**`SuperSymmetry.SU5.ChargeSpectrum.IsPhenoConstrainedQ5`**, a def, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/PhenoConstrained.lean#L171).

> The proposition which is true if the addition of a charge `q5` to a set of charge `x` leads
> `x` to being phenomenologically constrained.

```lean
def IsPhenoConstrainedQ5 [DecidableEq 𝓩] (x : ChargeSpectrum 𝓩) (q5 : 𝓩) : Prop
```

### C.2. Reducing the condition `IsPhenoConstrainedQ5`

**`SuperSymmetry.SU5.ChargeSpectrum.isPhenoConstrainedQ5_iff`**, a lemma, [line 182](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/PhenoConstrained.lean#L182).

```lean
lemma isPhenoConstrainedQ5_iff [DecidableEq 𝓩] (x : ChargeSpectrum 𝓩) (q5 : 𝓩) :
    x.IsPhenoConstrainedQ5 q5 ↔
    x.AllowsTermQ5 q5 β ∨ x.AllowsTermQ5 q5 Λ ∨ x.AllowsTermQ5 q5 W4 ∨
    x.AllowsTermQ5 q5 K1 ∨ x.AllowsTermQ5 q5 W1
```

### C.3. Decidability of `IsPhenoConstrainedQ5`

**`SuperSymmetry.SU5.ChargeSpectrum.decidableIsPhenoConstrainedQ5`**, an instance, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/PhenoConstrained.lean#L194).

```lean
instance decidableIsPhenoConstrainedQ5 [DecidableEq 𝓩] (x : ChargeSpectrum 𝓩) (q5 : 𝓩) :
    Decidable (x.IsPhenoConstrainedQ5 q5)
```

### C.4. Charge spectra with added `Q5` charge is pheno-constrained iff

**`SuperSymmetry.SU5.ChargeSpectrum.isPhenoConstrained_insertQ5_iff_isPhenoConstrainedQ5`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/PhenoConstrained.lean#L204).

```lean
lemma isPhenoConstrained_insertQ5_iff_isPhenoConstrainedQ5 [DecidableEq 𝓩] {qHd qHu : Option 𝓩}
    {Q5 Q10: Finset 𝓩} {q5 : 𝓩} :
    IsPhenoConstrained ⟨qHd, qHu, insert q5 Q5, Q10⟩↔
    IsPhenoConstrainedQ5 ⟨qHd, qHu, Q5, Q10⟩ q5 ∨
    IsPhenoConstrained ⟨qHd, qHu, Q5, Q10⟩
```

## D. Phenomenologically constrained charge spectra after adding a single Q10 charge

> We now define `IsPhenoConstrainedQ10` which gives the condition that a charge spectrum becomes
> pheno-constrained after adding a single charge to the `Q10` set.

**`SuperSymmetry.SU5.ChargeSpectrum.IsPhenoConstrainedQ10`**, a def, [line 238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/PhenoConstrained.lean#L238).

> The proposition which is true if the addition of a charge `q10` to a set of charges `x` leads
> `x` to being phenomenologically constrained.

```lean
def IsPhenoConstrainedQ10 [DecidableEq 𝓩] (x : ChargeSpectrum 𝓩) (q10 : 𝓩) : Prop
```

### D.2. Reducing the condition `IsPhenoConstrainedQ10`

**`SuperSymmetry.SU5.ChargeSpectrum.isPhenoConstrainedQ10_iff`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/PhenoConstrained.lean#L249).

```lean
lemma isPhenoConstrainedQ10_iff [DecidableEq 𝓩] (x : ChargeSpectrum 𝓩) (q10 : 𝓩) :
    x.IsPhenoConstrainedQ10 q10 ↔ x.AllowsTermQ10 q10 Λ ∨ x.AllowsTermQ10 q10 W2 ∨
    x.AllowsTermQ10 q10 K1 ∨ x.AllowsTermQ10 q10 K2 ∨ x.AllowsTermQ10 q10 W1
```

### D.3. Decidability of `IsPhenoConstrainedQ10`

**`SuperSymmetry.SU5.ChargeSpectrum.decidableIsPhenoConstrainedQ10`**, an instance, [line 260](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/PhenoConstrained.lean#L260).

```lean
instance decidableIsPhenoConstrainedQ10 [DecidableEq 𝓩] (x : ChargeSpectrum 𝓩) (q10 : 𝓩) :
    Decidable (x.IsPhenoConstrainedQ10 q10)
```

### D.4. Charge spectra with added `Q10` charge is pheno-constrained iff

**`SuperSymmetry.SU5.ChargeSpectrum.isPhenoConstrained_insertQ10_iff_isPhenoConstrainedQ10`**, a lemma, [line 270](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/PhenoConstrained.lean#L270).

```lean
lemma isPhenoConstrained_insertQ10_iff_isPhenoConstrainedQ10 [DecidableEq 𝓩] {qHd qHu : Option 𝓩}
    {Q5 Q10: Finset 𝓩} {q10 : 𝓩} :
    IsPhenoConstrained ⟨qHd, qHu, Q5, insert q10 Q10⟩ ↔
    IsPhenoConstrainedQ10 ⟨qHd, qHu, Q5, Q10⟩ q10 ∨
    IsPhenoConstrained ⟨qHd, qHu, Q5, Q10⟩
```

## Depends on

- [Charges allowing terms](../part-01/su5-chargespectrum-allowsterm.md)

## Sources

- [Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/PhenoConstrained.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/PhenoConstrained.lean)
