---
declaration: module
origin: cited
lean: Electromagnetism.ThreeDimension.gaussLawElectric, Electromagnetism.ThreeDimension.gaussLawMagnetic, Electromagnetism.ThreeDimension.ampereLaw, Electromagnetism.ThreeDimension.faradayLaw
statement: formalized
proof: formalized
---

# A. Maxwell's equations in three dimensions

The module `Physlib.Electromagnetism.ThreeDimension.MaxwellEquations`, [Physlib/Electromagnetism/ThreeDimension/MaxwellEquations.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/ThreeDimension/MaxwellEquations.lean): 4 declarations, 4 with a docstring, 4 listed as significant.

> Maxwell's equations relate electric and magnetic fields to electric charge and current. In three
> spatial dimensions they can be written using the familiar divergence, curl, and time-derivative
> operators of vector calculus.

## A.1. Main results

> This module proves the four differential equations:
>
> - `gaussLawElectric`, relating the divergence of the electric field to charge density;
> - `gaussLawMagnetic`, stating that the magnetic field is divergence-free;
> - `ampereLaw`, including both the electric current and displacement-current terms;
> - `faradayLaw`, relating the curl of the electric field to the time derivative of the magnetic
>   field.

## A.2. Relation to the covariant formulation

> The electric and magnetic fields are obtained from an electromagnetic potential. Gauss's law for
> the electric field and Ampère's law are derived from the covariant extremality condition
> `IsExtrema`, while the two homogeneous equations follow from the potential definitions and
> smoothness assumptions. The results therefore connect the tensorial backend to the standard
> three-dimensional presentation.

## A.3. Current scope

> The statements here are pointwise differential equations in free space. Integral formulations,
> boundary conditions, and constitutive laws for material media are outside the current scope of this
> module.

**`Electromagnetism.ThreeDimension.gaussLawElectric`**, a theorem, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/ThreeDimension/MaxwellEquations.lean#L66). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Gauss's law for the electric field.

```lean
theorem gaussLawElectric (t : Time) (x : Space)
    (h : IsExtrema 𝓕 V J₄) (hV : ContDiff ℝ ∞ V) (hJ : ContDiff ℝ ∞ J₄) :
    (∇ ⬝ E t) x = ρ t x / ε₀
```

**`Electromagnetism.ThreeDimension.gaussLawMagnetic`**, a theorem, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/ThreeDimension/MaxwellEquations.lean#L72). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Gauss's law for the magnetic field.

```lean
theorem gaussLawMagnetic (t : Time) (x : Space) (hV : ContDiff ℝ ∞ V) :
    (∇ ⬝ B t) x = 0
```

**`Electromagnetism.ThreeDimension.ampereLaw`**, a theorem, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/ThreeDimension/MaxwellEquations.lean#L77). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Ampère's law.

```lean
theorem ampereLaw (t : Time) (x : Space)
    (h : IsExtrema 𝓕 V J₄) (hV : ContDiff ℝ ∞ V) (hJ : ContDiff ℝ ∞ J₄) :
      (∇ ⨯ B t) x = μ₀ • J t x + μ₀ • ε₀ • ∂ₜ (fun t => E t x) t
```

**`Electromagnetism.ThreeDimension.faradayLaw`**, a theorem, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/ThreeDimension/MaxwellEquations.lean#L86). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Faraday's law.

```lean
theorem faradayLaw (t : Time) (x : Space) (hV : ContDiff ℝ ∞ V) :
    (∇ ⨯ E t) x = - ∂ₜ (fun t => B t x) t
```

## Depends on

- [Extrema of the Lagrangian density](../dynamics/isextrema.md)

## Proof depends on

- [Three-Dimensional Electromagnetism](basic.md)

## Sources

- [Physlib/Electromagnetism/ThreeDimension/MaxwellEquations.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/ThreeDimension/MaxwellEquations.lean)
