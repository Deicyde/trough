---
declaration: module
origin: cited
lean: QuantumMechanics.SpaceDHilbertSpace.fourierUnitary, QuantumMechanics.SpaceDHilbertSpace.fourierUnitary_apply, QuantumMechanics.SpaceDHilbertSpace.fourierUnitary_symm_apply, QuantumMechanics.SpaceDHilbertSpace.schwartzIncl_fourier_eq, QuantumMechanics.SpaceDHilbertSpace.schwartzIncl_fourierInv_eq, QuantumMechanics.SpaceDHilbertSpace.fourierInv_schwartzIncl_fourier, QuantumMechanics.SpaceDHilbertSpace.fourierUnitary_map_schwartzSubmodule
statement: formalized
proof: formalized
---

# The Fourier transform on `SpaceDHilbertSpace`

The module `Physlib.QuantumMechanics.HilbertSpaces.SpaceD.Fourier`, [Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Fourier.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Fourier.lean): 7 declarations, 7 with a docstring.

## i. Overview

> In this module we define the Fourier transform on `SpaceDHilbertSpace d` as a unitary operator.
> Mathlib's L² Fourier transform `MeasureTheory.Lp.fourierTransformₗᵢ` is a linear isometry
> equivalence of `Lp ℂ 2 volume`, hence of `SpaceDHilbertSpace d`, onto itself; packaged as
> `fourierUnitary d`.

## ii. Key results

> - `fourierUnitary d` : the L² Fourier transform as a unitary
>   `SpaceDHilbertSpace d ≃ₗᵢ[ℂ] SpaceDHilbertSpace d`, acting as `𝓕`/`𝓕⁻`
>   (`fourierUnitary_apply`, `fourierUnitary_symm_apply`).
> - `schwartzIncl_fourier_eq` : `𝓕 (schwartzIncl f) = schwartzIncl (𝓕 f)`.
> - `schwartzIncl_fourierInv_eq` : the inverse acts by the inverse Schwartz Fourier transform.
> - `fourierUnitary_map_schwartzSubmodule` : `fourierUnitary d` maps the Schwartz submodule onto
>   itself.

## iv. References

> * None.

## A. The Fourier unitary

**`QuantumMechanics.SpaceDHilbertSpace.fourierUnitary`**, a def, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Fourier.lean#L55).

> The L² Fourier transform as a unitary on `SpaceDHilbertSpace d`.

```lean
noncomputable def fourierUnitary (d : ℕ) :
    SpaceDHilbertSpace d ≃ₗᵢ[ℂ] SpaceDHilbertSpace d
```

**`QuantumMechanics.SpaceDHilbertSpace.fourierUnitary_apply`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Fourier.lean#L61).

> `fourierUnitary d` acts as the L² Fourier transform `𝓕`.

```lean
lemma fourierUnitary_apply (ψ : SpaceDHilbertSpace d) : fourierUnitary d ψ = 𝓕 ψ
```

**`QuantumMechanics.SpaceDHilbertSpace.fourierUnitary_symm_apply`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Fourier.lean#L65).

> `(fourierUnitary d).symm` acts as the inverse L² Fourier transform `𝓕⁻`.

```lean
lemma fourierUnitary_symm_apply (ψ : SpaceDHilbertSpace d) : (fourierUnitary d).symm ψ = 𝓕⁻ ψ
```

## B. Action on the Schwartz submodule

**`QuantumMechanics.SpaceDHilbertSpace.schwartzIncl_fourier_eq`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Fourier.lean#L71).

> Applying `fourierUnitary d` to the L² class of a Schwartz map `f` gives the L² class of the
> Schwartz Fourier transform `𝓕 f`.

```lean
lemma schwartzIncl_fourier_eq (f : 𝓢(Space d, ℂ)) :
    𝓕 (schwartzIncl volume f) = schwartzIncl volume (𝓕 f)
```

**`QuantumMechanics.SpaceDHilbertSpace.schwartzIncl_fourierInv_eq`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Fourier.lean#L76).

> Applying `𝓕⁻` to the L² class of a Schwartz map `f` gives the L² class of the inverse
> Schwartz Fourier transform `𝓕⁻ f`.

```lean
lemma schwartzIncl_fourierInv_eq (f : 𝓢(Space d, ℂ)) :
    𝓕⁻ (schwartzIncl volume f) = schwartzIncl volume (𝓕⁻ f)
```

**`QuantumMechanics.SpaceDHilbertSpace.fourierInv_schwartzIncl_fourier`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Fourier.lean#L82).

> Pulling the L² class of `𝓕 f` back through the Fourier unitary recovers the L² class of `f`.

```lean
lemma fourierInv_schwartzIncl_fourier (f : 𝓢(Space d, ℂ)) :
    𝓕⁻ (schwartzIncl volume (𝓕 f)) = schwartzIncl volume f
```

**`QuantumMechanics.SpaceDHilbertSpace.fourierUnitary_map_schwartzSubmodule`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Fourier.lean#L87).

> The Fourier unitary maps the Schwartz submodule onto itself.

```lean
lemma fourierUnitary_map_schwartzSubmodule :
    (SchwartzSubmodule d).map (fourierUnitary d).toLinearMap = SchwartzSubmodule d
```

## Depends on

- [Schwartz submodule](schwartzsubmodule.md)

## Sources

- [Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Fourier.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Fourier.lean)
