---
declaration: module
origin: cited
lean: PhyslibAlpha.ProbabilisticTheory.QuantumMechanics.UnitaryRep.koopmanIsometry, PhyslibAlpha.ProbabilisticTheory.QuantumMechanics.UnitaryRep.compMeasurePreserving_congr, PhyslibAlpha.ProbabilisticTheory.QuantumMechanics.UnitaryRep.koopmanIsometry_apply, PhyslibAlpha.ProbabilisticTheory.QuantumMechanics.UnitaryRep.koopmanIsometry_mul, PhyslibAlpha.ProbabilisticTheory.QuantumMechanics.UnitaryRep.koopmanIsometry_one, PhyslibAlpha.ProbabilisticTheory.QuantumMechanics.UnitaryRep.koopmanEquiv, PhyslibAlpha.ProbabilisticTheory.QuantumMechanics.UnitaryRep.koopmanEquiv_one, PhyslibAlpha.ProbabilisticTheory.QuantumMechanics.UnitaryRep.koopmanEquiv_mul
statement: formalized
proof: formalized
---

# The Koopman representation of a measure-preserving action

The module `PhyslibAlpha.ProbabilisticTheory.Representation.Koopman`, [PhyslibAlpha/ProbabilisticTheory/Representation/Koopman.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Representation/Koopman.lean): 12 declarations, 6 with a docstring.

> An abelian group acting on a probability space by measure-preserving maps acts unitarily on `L²`.

## i. Overview

> Let an abelian group `G` act on a measurable space `X` by bijections preserving a measure `μ`, for
> example lattice translations acting on the configurations of a classical spin system with a
> translation-invariant ensemble `μ`. Then `(U_g f)(x) = f(g⁻¹ x)` is a unitary representation of `G`
> on `L²(μ)`: the Koopman representation. The spectral theorem for unitary representations applies:
> every `f ∈ L²(μ)`, an observable of the classical system, has a spectral measure `ν_f` on the
> characters of `G` with `∫ χ(g) dν_f(χ) = ⟨f, U_g f⟩ = ∫ f̄(x) f(g⁻¹ x) dμ(x)`, the Fourier transform
> of its correlation function. This is the structure factor of a classical lattice system. The
> spectral projection of the trivial character projects onto the translation-invariant functions.
> Nothing about quantum mechanics enters: this is the same representation theory that governs
> quantum systems.

## ii. Key results

> - `UnitaryRep.koopman` : the Koopman representation on `L²(μ)`.
> - `UnitaryRep.koopman_apply_ae` : it acts by composition with the inverse group action.

## iv. References

> * None.

## A. The Koopman operators

**`PhyslibAlpha.ProbabilisticTheory.QuantumMechanics.UnitaryRep.koopmanIsometry`**, a def, [line 72](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Representation/Koopman.lean#L72).

> The composition operator `f ↦ f ∘ T_g⁻¹` on `L²(μ)` as a linear isometry.

```lean
def koopmanIsometry (g : Γ) : Lp E 2 μ →ₗᵢ[ℂ] Lp E 2 μ
```

**`PhyslibAlpha.ProbabilisticTheory.QuantumMechanics.UnitaryRep.compMeasurePreserving_congr`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Representation/Koopman.lean#L76).

```lean
lemma compMeasurePreserving_congr {f f' : X → X} (hf : MeasurePreserving f μ μ)
    (hf' : MeasurePreserving f' μ μ) (e : f = f') (g : Lp E 2 μ) :
    Lp.compMeasurePreserving f hf g = Lp.compMeasurePreserving f' hf' g
```

**`PhyslibAlpha.ProbabilisticTheory.QuantumMechanics.UnitaryRep.koopmanIsometry_apply`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Representation/Koopman.lean#L82).

```lean
lemma koopmanIsometry_apply (g : Γ) (f : Lp E 2 μ) :
    koopmanIsometry μ T hT g f = Lp.compMeasurePreserving (T g⁻¹) (hT g⁻¹) f
```

**`PhyslibAlpha.ProbabilisticTheory.QuantumMechanics.UnitaryRep.koopmanIsometry_mul`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Representation/Koopman.lean#L86).

```lean
lemma koopmanIsometry_mul (g h : Γ) (f : Lp E 2 μ) :
    koopmanIsometry μ T hT (g * h) f = koopmanIsometry μ T hT g (koopmanIsometry μ T hT h f)
```

**`PhyslibAlpha.ProbabilisticTheory.QuantumMechanics.UnitaryRep.koopmanIsometry_one`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Representation/Koopman.lean#L97).

```lean
lemma koopmanIsometry_one (f : Lp E 2 μ) : koopmanIsometry μ T hT 1 f = f
```

## B. The unitary representation

**`PhyslibAlpha.ProbabilisticTheory.QuantumMechanics.UnitaryRep.koopmanEquiv`**, a def, [line 107](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Representation/Koopman.lean#L107).

> The Koopman operator as a linear isometric equivalence.

```lean
def koopmanEquiv (g : Γ) : Lp E 2 μ ≃ₗᵢ[ℂ] Lp E 2 μ
```

**`PhyslibAlpha.ProbabilisticTheory.QuantumMechanics.UnitaryRep.koopmanEquiv_one`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Representation/Koopman.lean#L119).

```lean
lemma koopmanEquiv_one : koopmanEquiv (E := E) μ T hT 1 = 1
```

**`PhyslibAlpha.ProbabilisticTheory.QuantumMechanics.UnitaryRep.koopmanEquiv_mul`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Representation/Koopman.lean#L123).

```lean
lemma koopmanEquiv_mul (g h : Γ) :
    koopmanEquiv (E := E) μ T hT (g * h) =
      koopmanEquiv (E := E) μ T hT g * koopmanEquiv (E := E) μ T hT h
```

**`PhyslibAlpha.ProbabilisticTheory.QuantumMechanics.UnitaryRep.koopman`**, a def, [line 130](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Representation/Koopman.lean#L130).

> **The Koopman representation**: a group acting on a measure space by measure-preserving
> bijections acts unitarily on `L²(μ)` by `(U_g f)(x) = f(g⁻¹ x)`.

```lean
def koopman : Γ →* unitary (Lp E 2 μ →L[ℂ] Lp E 2 μ)
```

**`PhyslibAlpha.ProbabilisticTheory.QuantumMechanics.UnitaryRep.koopman_apply`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Representation/Koopman.lean#L136).

> The Koopman operator acts by composition with the inverse of the group action.

```lean
lemma koopman_apply (g : Γ) (f : Lp E 2 μ) :
    ((koopman μ T hT g : unitary (Lp E 2 μ →L[ℂ] Lp E 2 μ)) : Lp E 2 μ →L[ℂ] Lp E 2 μ) f =
      Lp.compMeasurePreserving (T g⁻¹) (hT g⁻¹) f
```

**`PhyslibAlpha.ProbabilisticTheory.QuantumMechanics.UnitaryRep.inner_koopman`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Representation/Koopman.lean#L142).

> **The correlation function of an observable**: the matrix coefficient of the Koopman
> representation is the covariance `∫ ⟨f(x), f(g⁻¹ x)⟩ dμ(x)` of `f` with its translate.

```lean
lemma inner_koopman (g : Γ) (f : Lp E 2 μ) :
    ⟪f, ((koopman μ T hT g : unitary (Lp E 2 μ →L[ℂ] Lp E 2 μ)) : Lp E 2 μ →L[ℂ] Lp E 2 μ) f⟫_ℂ =
      ∫ x, ⟪f x, f (T g⁻¹ x)⟫_ℂ ∂μ
```

## C. Invariant functions

**`PhyslibAlpha.ProbabilisticTheory.QuantumMechanics.UnitaryRep.range_projection_one_koopman`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Representation/Koopman.lean#L169).

> **Invariant observables of a classical system have zero momentum**: the spectral projection of
> the trivial character of the Koopman representation projects onto the translation-invariant
> functions in `L²(μ)`.

```lean
lemma range_projection_one_koopman :
    LinearMap.range (projection (koopman (E := E) μ T hT)
        {(1 : PontryaginDual (Multiplicative G))} : Lp E 2 μ →L[ℂ] Lp E 2 μ).toLinearMap =
      PhyslibAlpha.ProbabilisticTheory.Representation.sector
        (toEnd (koopman (E := E) μ T hT)) (fun _ => (1 : ℂ))
```

## Depends on

- [The commutant of a unitary representation of an abelian group](commutant.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Representation/Koopman.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Representation/Koopman.lean)
