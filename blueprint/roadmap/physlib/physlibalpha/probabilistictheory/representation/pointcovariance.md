---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.UnitaryRep.autCont, ProbabilisticTheory.QuantumMechanics.UnitaryRep.dualAct, ProbabilisticTheory.QuantumMechanics.UnitaryRep.dualAct_apply, ProbabilisticTheory.QuantumMechanics.UnitaryRep.dualAct_mul, ProbabilisticTheory.QuantumMechanics.UnitaryRep.dualAct_one, ProbabilisticTheory.QuantumMechanics.UnitaryRep.dualActEquiv, ProbabilisticTheory.QuantumMechanics.UnitaryRep.IsCovariantRep, ProbabilisticTheory.QuantumMechanics.UnitaryRep.measurable_dualAct
statement: formalized
proof: formalized
---

# Covariance of the spectral measure under a finite group of symmetries

The module `PhyslibAlpha.ProbabilisticTheory.Representation.PointCovariance`, [PhyslibAlpha/ProbabilisticTheory/Representation/PointCovariance.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/PointCovariance.lean): 14 declarations, 8 with a docstring.

> A group acting on the translation group acts on its characters, and the spectral measure of a
> covariant representation is covariant.

## i. Overview

> Let a discrete abelian group `G` of translations be represented unitarily by `π`, and let a group
> `P` act on `G` by automorphisms `φ p`. The group `P` acts on the characters of `G` by
> `(p • χ)(g) = χ(φ(p⁻¹) g)`. A unitary representation `ρ` of `P` on the same space is *covariant*
> when `ρ(p) π(g) ρ(p)⁻¹ = π(φ(p) g)`. Together `π` and `ρ` represent the semidirect product
> `G ⋊ P`: for a crystal, `G` is the group of lattice translations and `P` its point group.
>
> The spectral measure of a vector `ξ`, the distribution of `ξ` over the characters, is determined
> by its Fourier transform `g ↦ ⟨ξ, π(g) ξ⟩`. Since the transform of `ρ(p) ξ` is that of `ξ`
> composed with `φ(p⁻¹)`, the spectral measure of `ρ(p) ξ` is the pushforward of that of `ξ` under
> the action of `p` on the characters. Consequently the spectral projection of the image of a set of
> characters is carried to the image of the projection by `ρ(p)`:
> `ρ(p) P(S) = P(p • S) ρ(p)`. The unitary `ρ(p)` carries the sector of total momenta in `S` onto the
> sector of total momenta in `p • S`.

## ii. Key results

> - `UnitaryRep.dualAct` : the action of a group of automorphisms on the characters.
> - `UnitaryRep.vectorMeasure_rho` : the spectral measure of `ρ(p) ξ` is the pushforward of that of
>   `ξ`.
> - `UnitaryRep.rho_mul_projection` : `ρ(p) P(S) = P(p • S) ρ(p)`.

## iv. References

> * None.

## A. The action on the characters

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.autCont`**, a def, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/PointCovariance.lean#L70).

> The automorphism `φ p` of the translation group as a continuous homomorphism.

```lean
def autCont (p : P) : Multiplicative G →ₜ* Multiplicative G
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.dualAct`**, a def, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/PointCovariance.lean#L75).

> The action of `p` on a character `χ`: `(p • χ)(g) = χ(φ(p⁻¹) g)`.

```lean
def dualAct (p : P) : PontryaginDual (Multiplicative G) →ₜ* PontryaginDual (Multiplicative G)
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.dualAct_apply`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/PointCovariance.lean#L78).

```lean
lemma dualAct_apply (p : P) (χ : PontryaginDual (Multiplicative G)) (g : Multiplicative G) :
    dualAct φ p χ g = χ (φ p⁻¹ g)
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.dualAct_mul`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/PointCovariance.lean#L81).

```lean
lemma dualAct_mul (p q : P) (χ : PontryaginDual (Multiplicative G)) :
    dualAct φ (p * q) χ = dualAct φ p (dualAct φ q χ)
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.dualAct_one`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/PointCovariance.lean#L88).

```lean
lemma dualAct_one (χ : PontryaginDual (Multiplicative G)) : dualAct φ 1 χ = χ
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.dualActEquiv`**, a def, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/PointCovariance.lean#L95).

> The action of `p` on the characters is a bijection.

```lean
def dualActEquiv (p : P) :
    PontryaginDual (Multiplicative G) ≃ PontryaginDual (Multiplicative G)
```

## B. Covariance of the spectral measure

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.IsCovariantRep`**, a def, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/PointCovariance.lean#L113).

> The representation `ρ` of `P` is covariant with respect to the translations `π` and the
> action `φ`: `ρ(p) π(g) = π(φ(p) g) ρ(p)`.

```lean
def IsCovariantRep : Prop
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.measurable_dualAct`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/PointCovariance.lean#L116).

```lean
lemma measurable_dualAct (p : P) : Measurable (dualAct φ p)
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.isCovariantRep_comp`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/PointCovariance.lean#L125).

> A representation of a group `Q` acting on the translations, restricted to the translations,
> is covariant when the group relation `s t(a) = t(φ(s) a) s` holds.

```lean
lemma isCovariantRep_comp {Q : Type*} [Group Q] (φ : Q →* MulAut (Multiplicative G))
    (U : Q →* unitary (H →L[ℂ] H)) (τ : Multiplicative G →* Q)
    (h : ∀ (s : Q) (a : Multiplicative G), s * τ a = τ (φ s a) * s) :
    IsCovariantRep φ (U.comp τ) U
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.inner_rho_translation`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/PointCovariance.lean#L138).

> The matrix coefficient of the translated vector.

```lean
lemma inner_rho_translation (hcov : IsCovariantRep φ π ρ) (p : P) (g : Multiplicative G)
    (ξ : H) :
    ⟪((ρ p : unitary (H →L[ℂ] H)) : H →L[ℂ] H) ξ,
        ((π g : unitary (H →L[ℂ] H)) : H →L[ℂ] H) (((ρ p : unitary (H →L[ℂ] H)) : H →L[ℂ] H) ξ)⟫_ℂ
      = ⟪ξ, ((π (φ p⁻¹ g) : unitary (H →L[ℂ] H)) : H →L[ℂ] H) ξ⟫_ℂ
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.vectorMeasure_rho`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/PointCovariance.lean#L156).

> **The spectral measure of `ρ(p) ξ` is the pushforward of that of `ξ`** under the action of `p`
> on the characters.

```lean
lemma vectorMeasure_rho (hcov : IsCovariantRep φ π ρ) (p : P) (ξ : H) :
    vectorMeasure π (((ρ p : unitary (H →L[ℂ] H)) : H →L[ℂ] H) ξ) =
      Measure.map (dualAct φ p) (vectorMeasure π ξ)
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.norm_sq_projection`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/PointCovariance.lean#L168).

```lean
lemma norm_sq_projection (S : Set (PontryaginDual (Multiplicative G))) (hS : MeasurableSet S)
    (η : H) : ‖projection π S η‖ ^ 2 = (vectorMeasure π η S).toReal
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.inner_projection_self`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/PointCovariance.lean#L174).

```lean
lemma inner_projection_self (S : Set (PontryaginDual (Multiplicative G))) (η : H) :
    ⟪projection π S η, η⟫_ℂ = ((‖projection π S η‖ ^ 2 : ℝ) : ℂ)
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.rho_mul_projection`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/PointCovariance.lean#L189).

> **The spectral projections are covariant**: `ρ(p) P(S) = P(p • S) ρ(p)` for every measurable
> set `S` of characters. The unitary `ρ(p)` carries the sector of momenta in `S` onto the sector of
> momenta in `p • S`.

```lean
lemma rho_mul_projection (hcov : IsCovariantRep φ π ρ) (p : P)
    {S : Set (PontryaginDual (Multiplicative G))} (hS : MeasurableSet S) :
    ((ρ p : unitary (H →L[ℂ] H)) : H →L[ℂ] H) * projection π S =
      projection π (dualAct φ p '' S) * ((ρ p : unitary (H →L[ℂ] H)) : H →L[ℂ] H)
```

## Depends on

- [The commutant of a unitary representation of an abelian group](commutant.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Representation/PointCovariance.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/PointCovariance.lean)
