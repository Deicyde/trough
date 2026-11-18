---
declaration: module
origin: cited
lean: SuperSymmetry.SU5.ChargeSpectrum.ofFieldLabel, SuperSymmetry.SU5.ChargeSpectrum.ofFieldLabel_empty, SuperSymmetry.SU5.ChargeSpectrum.ofFieldLabel_mono, SuperSymmetry.SU5.ChargeSpectrum.mem_ofFieldLabel_fiveHd, SuperSymmetry.SU5.ChargeSpectrum.mem_ofFieldLabel_fiveHu, SuperSymmetry.SU5.ChargeSpectrum.mem_ofFieldLabel_fiveMatter, SuperSymmetry.SU5.ChargeSpectrum.ext_ofFieldLabel
statement: formalized
proof: formalized
---

# Charges associated with a field label

The module `Physlib.Particles.SuperSymmetry.SU5.ChargeSpectrum.OfFieldLabel`, [Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/OfFieldLabel.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/OfFieldLabel.lean): 7 declarations, 4 with a docstring.

## i. Overview

> Recall that a `FieldLabel` is one of the seven possible superfields in the SU(5) GUT,
> corresponding to the fields present and their conjugates.
>
> Given a charge spectrum `x : ChargeSpectrum 𝓩`, we are interested in the finite set of
> charges carried by representations associated with a given `FieldLabel`.
>
> Results in this module will be used to find the charges associated with
> terms in the potential.

## ii. Key results

> - `ofFieldLabel` : Given a charge spectrum `x : ChargeSpectrum 𝓩`,
>   `ofFieldLabel x F` is the finite set of charges associated with representations
>   corresponding to the field label `F`.

## iv. References

> * None.

## A. Charges associated with a field label

> We first define `ofFieldLabel`, which given a charge spectrum `x : ChargeSpectrum 𝓩` and
> a `FieldLabel`, returns the finite set of charges associated with representations
> corresponding to that `FieldLabel`.

**`SuperSymmetry.SU5.ChargeSpectrum.ofFieldLabel`**, a def, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/OfFieldLabel.lean#L64).

> Given an `x : ChargeSpectrum 𝓩`, the charges associated with a given `FieldLabel`.

```lean
def ofFieldLabel (x : ChargeSpectrum 𝓩) : FieldLabel → Finset 𝓩
```

### A.1. The field labels for the empty charge spectrum

> We show that the charges associated with any field label for the empty charge spectrum is empty.
> This follows directly from the definition.

**`SuperSymmetry.SU5.ChargeSpectrum.ofFieldLabel_empty`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/OfFieldLabel.lean#L84).

> `ofFieldLabel ∅ F` is empty for any field label `F`.

```lean
lemma ofFieldLabel_empty (F : FieldLabel) :
    ofFieldLabel (∅ : ChargeSpectrum 𝓩) F = ∅
```

### A.2. Monotonicity of `ofFieldLabel`

> We show that the function `ofFieldLabel` is monotone in the charge spectrum, with relation to
> the subset relation. That is for a fixed field label `F`, if `x ⊆ y` are charge spectra,
> then `ofFieldLabel x F ⊆ ofFieldLabel y F`.

**`SuperSymmetry.SU5.ChargeSpectrum.ofFieldLabel_mono`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/OfFieldLabel.lean#L99).

> The function `ofFieldLabel` is monotone in the charge spectrum.

```lean
lemma ofFieldLabel_mono {x y : ChargeSpectrum 𝓩} (h : x ⊆ y) (F : FieldLabel) :
    x.ofFieldLabel F ⊆ y.ofFieldLabel F
```

### A.3. Membership of conjugate charges

> We show that a charge is a member of the finite sets associated with a field label if and only if
> its negative is a member of the finite set associated with the conjugate field label.

**`SuperSymmetry.SU5.ChargeSpectrum.mem_ofFieldLabel_fiveHd`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/OfFieldLabel.lean#L113).

```lean
lemma mem_ofFieldLabel_fiveHd (x : 𝓩) (y : ChargeSpectrum 𝓩) :
    x ∈ y.ofFieldLabel FieldLabel.fiveHd ↔ -x ∈ y.ofFieldLabel .fiveBarHd
```

**`SuperSymmetry.SU5.ChargeSpectrum.mem_ofFieldLabel_fiveHu`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/OfFieldLabel.lean#L118).

```lean
lemma mem_ofFieldLabel_fiveHu (x : 𝓩) (y : ChargeSpectrum 𝓩) :
    x ∈ y.ofFieldLabel FieldLabel.fiveHu ↔ -x ∈ y.ofFieldLabel .fiveBarHu
```

**`SuperSymmetry.SU5.ChargeSpectrum.mem_ofFieldLabel_fiveMatter`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/OfFieldLabel.lean#L123).

```lean
lemma mem_ofFieldLabel_fiveMatter (x : 𝓩) (y : ChargeSpectrum 𝓩) :
    x ∈ y.ofFieldLabel FieldLabel.fiveMatter ↔ -x ∈ y.ofFieldLabel .fiveBarMatter
```

### A.4. Extensionality of charge spectra via `ofFieldLabel`

> We show that two charge spectra are equal if they are equal on all field labels.
>
> This extensionality lemma is actually overkill in most cases, as there are a lot more
> direct ways to show that two charge spectra are equal.

**`SuperSymmetry.SU5.ChargeSpectrum.ext_ofFieldLabel`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/OfFieldLabel.lean#L139).

> Two charges are equal if they are equal on all field labels.

```lean
lemma ext_ofFieldLabel {x y : ChargeSpectrum 𝓩} (h : ∀ F, x.ofFieldLabel F = y.ofFieldLabel F) :
    x = y
```

## Depends on

- [Charge Spectrum](su5-chargespectrum-basic.md)
- [The field labels](su5-fieldlabels.md)

## Sources

- [Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/OfFieldLabel.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/OfFieldLabel.lean)
