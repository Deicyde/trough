---
declaration: module
origin: cited
lean: QuantumMechanics.OneDimension.HilbertSpace.planewaveFunctional, QuantumMechanics.OneDimension.HilbertSpace.planewaveFunctional_apply, QuantumMechanics.OneDimension.HilbertSpace.eq_of_eq_planewaveFunctional
statement: formalized
proof: formalized
---

# Plane waves

The module `Physlib.QuantumMechanics.HilbertSpaces.OneDimension.PlaneWaves`, [Physlib/QuantumMechanics/HilbertSpaces/OneDimension/PlaneWaves.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/PlaneWaves.lean): 3 declarations, 2 with a docstring.

> We define plane waves as a member of the dual of the Schwartz submodule of the 1d Hilbert space.
>
> This module has been generalized to d-dimensions in
> `QuantumMechanics/HilbertSpaces/SpaceD/MomentumStates.lean` and will be removed in the near future.

**`QuantumMechanics.OneDimension.HilbertSpace.planewaveFunctional`**, a def, [line 36](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/PlaneWaves.lean#L36).

> Plane waves as a member of the dual of the
> Schwartz submodule of the Hilbert space.
>
> For a given `k` this corresponds to the plane wave
> `exp (2π I k x)`.

```lean
def planewaveFunctional (k : ℝ) : 𝓢(ℝ, ℂ) →L[ℂ] ℂ
```

**`QuantumMechanics.OneDimension.HilbertSpace.planewaveFunctional_apply`**, a lemma, [line 40](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/PlaneWaves.lean#L40).

```lean
lemma planewaveFunctional_apply (k : ℝ) (ψ : 𝓢(ℝ, ℂ)) :
    planewaveFunctional k ψ = 𝓕 ψ k
```

**`QuantumMechanics.OneDimension.HilbertSpace.eq_of_eq_planewaveFunctional`**, a lemma, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/PlaneWaves.lean#L45).

> Two elements of the Schwartz submodule are equal if and only if they are equal on
> all applications of `planewaveFunctional`.

```lean
lemma eq_of_eq_planewaveFunctional {ψ1 ψ2 : 𝓢(ℝ, ℂ)}
    (h : ∀ k, planewaveFunctional k ψ1 = planewaveFunctional k ψ2) :
    ψ1 = ψ2
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/QuantumMechanics/HilbertSpaces/OneDimension/PlaneWaves.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/PlaneWaves.lean)
