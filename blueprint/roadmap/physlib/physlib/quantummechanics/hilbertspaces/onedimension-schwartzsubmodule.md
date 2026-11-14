---
declaration: module
origin: cited
lean: QuantumMechanics.OneDimension.HilbertSpace.schwartzIncl, QuantumMechanics.OneDimension.HilbertSpace.schwartzIncl_injective, QuantumMechanics.OneDimension.HilbertSpace.schwartzIncl_coe_ae, QuantumMechanics.OneDimension.HilbertSpace.schwartzIncl_inner
statement: formalized
proof: formalized
---

# Schwartz submodule of the Hilbert space

The module `Physlib.QuantumMechanics.HilbertSpaces.OneDimension.SchwartzSubmodule`, [Physlib/QuantumMechanics/HilbertSpaces/OneDimension/SchwartzSubmodule.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/SchwartzSubmodule.lean): 4 declarations, 1 with a docstring.

> This can be used to define e.g.
> the rigged Hilbert space.

**`QuantumMechanics.OneDimension.HilbertSpace.schwartzIncl`**, a def, [line 34](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/SchwartzSubmodule.lean#L34).

> The continuous linear map including Schwartz functions into the hilbert space.

```lean
def schwartzIncl : 𝓢(ℝ, ℂ) →L[ℂ] HilbertSpace
```

**`QuantumMechanics.OneDimension.HilbertSpace.schwartzIncl_injective`**, a lemma, [line 37](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/SchwartzSubmodule.lean#L37).

```lean
lemma schwartzIncl_injective : Function.Injective schwartzIncl
```

**`QuantumMechanics.OneDimension.HilbertSpace.schwartzIncl_coe_ae`**, a lemma, [line 40](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/SchwartzSubmodule.lean#L40).

```lean
lemma schwartzIncl_coe_ae (ψ : 𝓢(ℝ, ℂ)) :
    ψ.1 =ᶠ[ae volume] (schwartzIncl ψ)
```

**`QuantumMechanics.OneDimension.HilbertSpace.schwartzIncl_inner`**, a lemma, [line 43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/SchwartzSubmodule.lean#L43).

```lean
lemma schwartzIncl_inner (ψ1 ψ2 : 𝓢(ℝ, ℂ)) :
    ⟪schwartzIncl ψ1, schwartzIncl ψ2⟫_ℂ = ∫ x : ℝ, starRingEnd ℂ (ψ1 x) * ψ2 x
```

## Depends on

- [Hilbert space for one dimension quantum mechanics](onedimension-basic.md)

## Sources

- [Physlib/QuantumMechanics/HilbertSpaces/OneDimension/SchwartzSubmodule.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/SchwartzSubmodule.lean)
