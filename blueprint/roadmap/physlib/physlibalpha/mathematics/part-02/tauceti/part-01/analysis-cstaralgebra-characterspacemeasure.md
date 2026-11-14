---
declaration: module
origin: cited
lean: LinearMap.exists_isFiniteMeasure_integral_characterSpace_eq, WeakDual.CharacterSpace.integral_apply_star_mul_self, StarSubalgebra.integral_norm_sq_eq_norm_apply_sq, StarSubalgebra.exists_isFiniteMeasure_integral_characterSpace_eq_inner
statement: formalized
proof: formalized
---

# Positive functionals on commutative C⋆-algebras are measures on the character space

The module `PhyslibAlpha.Mathematics.TauCeti.Analysis.CStarAlgebra.CharacterSpaceMeasure`, [PhyslibAlpha/Mathematics/TauCeti/Analysis/CStarAlgebra/CharacterSpaceMeasure.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/CStarAlgebra/CharacterSpaceMeasure.lean): 4 declarations, 4 with a docstring; 5 private, not shown.

> Let `A` be a unital commutative C⋆-algebra, with character space `Δ = characterSpace ℂ A`.

## i. Overview

> Let `A` be a unital commutative C⋆-algebra, with character space `Δ = characterSpace ℂ A`. A
> linear functional `f : A → ℂ` that is nonnegative on every `star a * a` is integration against a
> finite inner regular positive measure on `Δ`:
>
> `f a = ∫ ω, ω a ∂μ`.
>
> The Gelfand transform identifies `A` with `C(Δ, ℂ)`, and under this identification
> `star a * a` runs through the nonnegative functions, so `f` becomes a positive linear functional
> on `C(Δ, ℝ)`. The compact space `Δ` then carries its Riesz–Markov–Kakutani measure.
>
> This is the commutative case of the passage from positive functionals to spectral data; it turns
> a cyclic commuting family of operators, such as a unitary representation of an abelian group,
> into a measure on the joint spectrum.

## ii. Key results

> * `LinearMap.exists_isFiniteMeasure_integral_characterSpace_eq`: a functional nonnegative on
>   `star a * a` is integration against a finite inner regular measure on the character space.
> * `WeakDual.CharacterSpace.integral_apply_star_mul_self`: integrating `ω ↦ ω (star a * a)`
>   gives the squared `L²` norm of `ω ↦ ω a`, so a measure representing a functional `f` computes
>   `f (star a * a)`.
> * `StarSubalgebra.exists_isFiniteMeasure_integral_characterSpace_eq_inner`: for a closed
>   commutative star algebra of operators on a Hilbert space, each positive vector functional
>   `a ↦ ⟪ξ, a ξ⟫` is integration against a finite inner regular measure on the character space.
> * `StarSubalgebra.integral_norm_sq_eq_norm_apply_sq`: a measure representing such a functional
>   computes `‖a ξ‖²` as the squared `L²` norm of `ω ↦ ω a`.

## iv. References

> * W. Rudin, *Functional Analysis*, 2nd ed., McGraw–Hill (1991), Theorem 11.18 and §12.
> * G. J. Murphy, *C⋆-Algebras and Operator Theory*, Academic Press (1990), §2.1.

## A. Development

**`LinearMap.exists_isFiniteMeasure_integral_characterSpace_eq`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/CStarAlgebra/CharacterSpaceMeasure.lean#L142).

> **Positive functionals on a commutative C⋆-algebra are measures on its character space.**
> A linear functional on a unital commutative C⋆-algebra that is nonnegative on every
> `star a * a` is integration against a finite inner regular positive measure `μ` on the
> character space: `f a = ∫ ω, ω a ∂μ`.

```lean
lemma LinearMap.exists_isFiniteMeasure_integral_characterSpace_eq (f : A →ₗ[ℂ] ℂ)
    (hf : ∀ a, 0 ≤ f (star a * a)) :
    ∃ μ : Measure (characterSpace ℂ A), IsFiniteMeasure μ ∧ μ.InnerRegular ∧
      ∀ a, f a = ∫ ω, ω a ∂μ
```

**`WeakDual.CharacterSpace.integral_apply_star_mul_self`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/CStarAlgebra/CharacterSpaceMeasure.lean#L174).

> For a measure `μ` on the character space of a unital C⋆-algebra, integrating
> `ω ↦ ω (star a * a) = |ω a|²` gives the squared `L²` norm of `ω ↦ ω a`. Hence if `μ` represents a
> functional `f`, as in `LinearMap.exists_isFiniteMeasure_integral_characterSpace_eq`, then
> `f (star a * a) = ∫ |ω a|² dμ(ω)`.

```lean
lemma WeakDual.CharacterSpace.integral_apply_star_mul_self {E : Type*} [CStarAlgebra E]
    [MeasurableSpace (characterSpace ℂ E)] (μ : Measure (characterSpace ℂ E)) (a : E) :
    ∫ ω, ω (star a * a) ∂μ = ((∫ ω, ‖ω a‖ ^ 2 ∂μ : ℝ) : ℂ)
```

**`StarSubalgebra.integral_norm_sq_eq_norm_apply_sq`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/CStarAlgebra/CharacterSpaceMeasure.lean#L200).

> For a closed star algebra `B` of operators, if a measure `μ` on the character space
> represents the positive vector functional of `ξ`, then `∫ |ω a|² dμ(ω) = ‖a ξ‖²` for every
> `a ∈ B`.

```lean
lemma StarSubalgebra.integral_norm_sq_eq_norm_apply_sq {μ : Measure (characterSpace ℂ B)}
    {ξ : H} (hμ : ∀ a : B, ⟪ξ, (a : H →L[ℂ] H) ξ⟫_ℂ = ∫ ω, ω a ∂μ) (a : B) :
    ∫ ω, ‖ω a‖ ^ 2 ∂μ = ‖(a : H →L[ℂ] H) ξ‖ ^ 2
```

**`StarSubalgebra.exists_isFiniteMeasure_integral_characterSpace_eq_inner`**, a lemma, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/CStarAlgebra/CharacterSpaceMeasure.lean#L215).

> **Positive vector functionals are measures on the character space.** For a closed
> commutative star algebra `B` of operators on a complex Hilbert space and a vector `ξ`, the
> positive vector functional `a ↦ ⟪ξ, a ξ⟫` is integration against a finite inner regular positive
> measure on the character space of `B`.

```lean
lemma StarSubalgebra.exists_isFiniteMeasure_integral_characterSpace_eq_inner (ξ : H) :
    ∃ μ : Measure (characterSpace ℂ B), IsFiniteMeasure μ ∧ μ.InnerRegular ∧
      ∀ a : B, ⟪ξ, (a : H →L[ℂ] H) ξ⟫_ℂ = ∫ ω, ω a ∂μ
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/TauCeti/Analysis/CStarAlgebra/CharacterSpaceMeasure.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/CStarAlgebra/CharacterSpaceMeasure.lean)
