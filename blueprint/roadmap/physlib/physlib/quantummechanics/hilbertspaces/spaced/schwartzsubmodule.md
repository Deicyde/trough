---
declaration: module
origin: cited
lean: QuantumMechanics.SpaceDHilbertSpace.schwartzIncl, QuantumMechanics.SpaceDHilbertSpace.SchwartzSubmodule, QuantumMechanics.SpaceDHilbertSpace.schwartzEquiv, QuantumMechanics.SpaceDHilbertSpace.SchwartzSubmodule.schwartzEquiv_apply_coe, QuantumMechanics.SpaceDHilbertSpace.SchwartzSubmodule.schwartzEquiv_coe_ae, QuantumMechanics.SpaceDHilbertSpace.SchwartzSubmodule.schwartzEquiv_symm_coe_ae, QuantumMechanics.SpaceDHilbertSpace.SchwartzSubmodule.schwartzEquiv_ae_eq, QuantumMechanics.SpaceDHilbertSpace.SchwartzSubmodule.zero_eq_top
statement: formalized
proof: formalized
---

# Schwartz submodule

The module `Physlib.QuantumMechanics.HilbertSpaces.SpaceD.SchwartzSubmodule`, [Physlib/QuantumMechanics/HilbertSpaces/SpaceD/SchwartzSubmodule.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/SchwartzSubmodule.lean): 15 declarations (1 instance with no name), 4 with a docstring.

## i. Overview

> In this module we define the Schwartz submodule of `SpaceDHilbertSpace d μ`.
> `SchwartzSubmodule d μ` consists of the `μ`-a.e. equal equivalence classes of Schwartz maps
> on `Space d`.
>
> This is an import subspace of the Hilbert space. For one, the Fourier transform maps the Schwartz
> submodule into itself. It also is a convenient dense domain on which to define derivative operators.

## ii. Key results

> - `SchwartzSubmodule d μ`: Submodule of `SpaceDHilbertSpace d μ` consisting of the L² equivalence
>   classes of Schwartz maps `𝓢(Space d, ℂ)`.
> - `SchwartzSubmoduleOn Ω μ`: The projection of `SchwartzSubmodule d μ`
>   onto `SpaceDHilbertSpaceOn Ω μ`.

## iv. References

> * None.

## A. SchwartzSubmodule

**`QuantumMechanics.SpaceDHilbertSpace.schwartzIncl`**, a def, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/SchwartzSubmodule.lean#L57).

> The continuous linear map including Schwartz maps into `SpaceDHilbertSpace d μ`.

```lean
def schwartzIncl {d : ℕ} (μ : Measure (Space d)) [μ.HasTemperateGrowth] :
    𝓢(Space d, ℂ) →L[ℂ] SpaceDHilbertSpace d μ
```

**`QuantumMechanics.SpaceDHilbertSpace.SchwartzSubmodule`**, an abbrev, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/SchwartzSubmodule.lean#L62).

> The submodule of `SpaceDHilbertSpace d` corresponding to Schwartz maps.

```lean
abbrev SchwartzSubmodule (d : ℕ) (μ : Measure (Space d) := volume) [μ.HasTemperateGrowth] :
    Submodule ℂ (SpaceDHilbertSpace d μ)
```

**`QuantumMechanics.SpaceDHilbertSpace.schwartzEquiv`**, a def, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/SchwartzSubmodule.lean#L68).

> The linear equivalence between the Schwartz maps `𝓢(Space d, ℂ)` and the Schwartz submodule
> of `SpaceDHilbertSpace d μ`.

```lean
def schwartzEquiv
    {d : ℕ} (μ : Measure (Space d)) [μ.HasTemperateGrowth] [μ.IsOpenPosMeasure] :
    𝓢(Space d, ℂ) ≃ₗ[ℂ] SchwartzSubmodule d μ
```

### A.1. Coercions

**An instance with no name**, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/SchwartzSubmodule.lean#L83).

```lean
instance : CoeFun (SchwartzSubmodule d μ) fun _ ↦ Space d → ℂ
```

**`QuantumMechanics.SpaceDHilbertSpace.SchwartzSubmodule.schwartzEquiv_apply_coe`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/SchwartzSubmodule.lean#L86).

```lean
lemma schwartzEquiv_apply_coe : ↑(schwartzEquiv μ f) = schwartzIncl μ f
```

**`QuantumMechanics.SpaceDHilbertSpace.SchwartzSubmodule.schwartzEquiv_coe_ae`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/SchwartzSubmodule.lean#L88).

```lean
lemma schwartzEquiv_coe_ae : schwartzEquiv μ f =ᵐ[μ] f
```

**`QuantumMechanics.SpaceDHilbertSpace.SchwartzSubmodule.schwartzEquiv_symm_coe_ae`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/SchwartzSubmodule.lean#L90).

```lean
lemma schwartzEquiv_symm_coe_ae : (schwartzEquiv μ).symm ψ =ᵐ[μ] ψ
```

**`QuantumMechanics.SpaceDHilbertSpace.SchwartzSubmodule.schwartzEquiv_ae_eq`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/SchwartzSubmodule.lean#L94).

```lean
lemma schwartzEquiv_ae_eq (h : schwartzEquiv μ f =ᵐ[μ] schwartzEquiv μ g) : f = g
```

### A.2. Misc.

**`QuantumMechanics.SpaceDHilbertSpace.SchwartzSubmodule.zero_eq_top`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/SchwartzSubmodule.lean#L102).

```lean
lemma zero_eq_top (μ : Measure (Space 0)) [μ.HasTemperateGrowth] [μ.IsOpenPosMeasure] :
    SchwartzSubmodule 0 μ = ⊤
```

**`QuantumMechanics.SpaceDHilbertSpace.SchwartzSubmodule.dense`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/SchwartzSubmodule.lean#L125).

```lean
lemma dense [IsFiniteMeasureOnCompacts μ] :
    Dense (SchwartzSubmodule d μ : Set (SpaceDHilbertSpace d μ))
```

**`QuantumMechanics.SpaceDHilbertSpace.SchwartzSubmodule.schwartzEquiv_inner`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/SchwartzSubmodule.lean#L129).

```lean
lemma schwartzEquiv_inner :
    ⟪schwartzEquiv μ f, schwartzEquiv μ g⟫_ℂ = ∫ x, starRingEnd ℂ (f x) * g x ∂μ
```

**`QuantumMechanics.SpaceDHilbertSpace.SchwartzSubmodule.schwartzIncl_ker`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/SchwartzSubmodule.lean#L136).

```lean
lemma schwartzIncl_ker : (schwartzIncl μ).ker = (⊥ : Submodule ℂ 𝓢(Space d, ℂ))
```

**`QuantumMechanics.SpaceDHilbertSpace.SchwartzSubmodule.toTemperedDistribution_schwartzIncl_eq`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/SchwartzSubmodule.lean#L140).

```lean
lemma toTemperedDistribution_schwartzIncl_eq :
    toTemperedDistribution (schwartzIncl μ g) = g.toTemperedDistributionCLM (Space d) ℂ μ
```

## B. SchwartzSubmoduleOn

**`QuantumMechanics.SpaceDHilbertSpaceOn.SchwartzSubmoduleOn`**, an abbrev, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/SchwartzSubmodule.lean#L156).

> The projection of `SchwartzSubmodule d μ` onto `SpaceDHilbertSpaceOn Ω μ`.

```lean
abbrev SchwartzSubmoduleOn
    {d : ℕ} (Ω : Set (Space d)) (μ : Measure (Space d) := volume) [μ.HasTemperateGrowth] :
    Submodule ℂ (SpaceDHilbertSpaceOn Ω μ)
```

**`QuantumMechanics.SpaceDHilbertSpaceOn.SchwartzSubmoduleOn.mem_iff`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/SchwartzSubmodule.lean#L166).

```lean
lemma mem_iff {ψ : SpaceDHilbertSpaceOn Ω μ} :
    ψ ∈ SchwartzSubmoduleOn Ω μ ↔ ∃ φ : SchwartzSubmodule d μ, subspaceProjection Ω μ φ = ψ
```

## Depends on

- [Hilbert spaces for quantum mechanics on `Space d`](basic.md)

## Sources

- [Physlib/QuantumMechanics/HilbertSpaces/SpaceD/SchwartzSubmodule.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/SchwartzSubmodule.lean)
