---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.StructureFactor.correlation, ProbabilisticTheory.QuantumMechanics.StructureFactor.isPositiveDefiniteSub_correlation, ProbabilisticTheory.QuantumMechanics.StructureFactor.exists_measure, ProbabilisticTheory.QuantumMechanics.StructureFactor.integral_one_eq, ProbabilisticTheory.QuantumMechanics.StructureFactor.eq_of_transform_eq, ProbabilisticTheory.QuantumMechanics.StructureFactor.isPositiveDefiniteSub_iff_exists_measure
statement: formalized
proof: formalized
---

# The structure factor of an invariant state

The module `PhyslibAlpha.ProbabilisticTheory.Representation.StructureFactor`, [PhyslibAlpha/ProbabilisticTheory/Representation/StructureFactor.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/StructureFactor.lean): 6 declarations, 6 with a docstring.

> The correlation function of a translation-invariant positive functional is the Fourier transform of
> a positive measure on the momenta.

## i. Overview

> Let `B` be a ⋆-algebra of observables on which a discrete abelian group `G` of translations acts by
> ⋆-automorphisms `α_g`, and let `ω` be a positive linear functional with `ω ∘ α_g = ω`. For an
> observable `a` the correlation function `g ↦ ω(a⋆ α_g(a))` is positive definite on `G`: for any
> finite family of translations `g_i` and scalars `c_i` it is the value of `ω` at `b⋆ b` with
> `b = ∑ c_i α_{g_i}(a)`. By Bochner's theorem for discrete abelian groups it is the Fourier
> transform of a unique finite positive measure `μ_a` on the Pontryagin dual of `G`, the group of
> momenta. This measure is the structure factor of `a`: its total mass is `ω(a⋆ a)`, and
> `∫ χ(g) dμ_a(χ) = ω(a⋆ α_g(a))`. No Hilbert space, representation of the algebra or Hamiltonian is
> needed, and the algebra need not be a C⋆-algebra.

## ii. Key results

> - `StructureFactor.isPositiveDefiniteSub_correlation` : the correlation function is positive
>   definite.
> - `StructureFactor.exists_measure` : the structure factor exists.
> - `StructureFactor.measure_univ` : its total mass is `ω(a⋆ a)`.
> - `StructureFactor.eq_of_transform_eq` : for a countable group it is unique.
> - `StructureFactor.isPositiveDefiniteSub_iff_exists_measure` : positive semidefinite
>   translation-invariant couplings are Fourier transforms of positive measures.

## iv. References

> * None.

**`ProbabilisticTheory.QuantumMechanics.StructureFactor.correlation`**, a def, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/StructureFactor.lean#L70).

> The correlation function `g ↦ ω(a⋆ α_g(a))` of an observable `a`.

```lean
def correlation (a : B) (g : G) : ℂ
```

## A. Positive definiteness of the correlation function

**`ProbabilisticTheory.QuantumMechanics.StructureFactor.isPositiveDefiniteSub_correlation`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/StructureFactor.lean#L75).

> **The correlation function of an invariant positive functional is positive definite.**

```lean
lemma isPositiveDefiniteSub_correlation (hpos : ∀ b : B, 0 ≤ ω (star b * b))
    (hinv : ∀ g b, ω (α g b) = ω b) (a : B) :
    TauCeti.IsPositiveDefiniteSub (correlation ω α a)
```

## B. The structure factor

**`ProbabilisticTheory.QuantumMechanics.StructureFactor.exists_measure`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/StructureFactor.lean#L121).

> **The structure factor exists.** The correlation function of an observable in an invariant
> positive functional is the Fourier transform of a finite positive measure on the momenta:
> `ω(a⋆ α_g(a)) = ∫ χ(g) dμ_a(χ)`.

```lean
lemma exists_measure (hpos : ∀ b : B, 0 ≤ ω (star b * b)) (hinv : ∀ g b, ω (α g b) = ω b)
    (a : B) :
    ∃ μ : Measure (PontryaginDual (Multiplicative G)), IsFiniteMeasure μ ∧ μ.InnerRegular ∧
      ∀ g : G, ∫ χ, ((χ (Multiplicative.ofAdd g) : Circle) : ℂ) ∂μ = correlation ω α a g
```

**`ProbabilisticTheory.QuantumMechanics.StructureFactor.integral_one_eq`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/StructureFactor.lean#L133).

> The total mass of the structure factor is the expectation of `a⋆ a`.

```lean
lemma integral_one_eq {μ : Measure (PontryaginDual (Multiplicative G))}
    (a : B) (h : ∀ g : G, ∫ χ, ((χ (Multiplicative.ofAdd g) : Circle) : ℂ) ∂μ =
      correlation ω α a g) :
    (μ.real univ : ℂ) = ω (star a * a)
```

**`ProbabilisticTheory.QuantumMechanics.StructureFactor.eq_of_transform_eq`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/StructureFactor.lean#L147).

> **The structure factor is unique.** For a countable group a finite measure on the momenta is
> determined by its Fourier transform.

```lean
lemma eq_of_transform_eq {μ ν : Measure (PontryaginDual (Multiplicative G))}
    [IsFiniteMeasure μ] [IsFiniteMeasure ν]
    (h : ∀ g : G, ∫ χ, ((χ (Multiplicative.ofAdd g) : Circle) : ℂ) ∂μ =
      ∫ χ, ((χ (Multiplicative.ofAdd g) : Circle) : ℂ) ∂ν) : μ = ν
```

**`ProbabilisticTheory.QuantumMechanics.StructureFactor.isPositiveDefiniteSub_iff_exists_measure`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/StructureFactor.lean#L170).

> **Positive semidefinite translation-invariant couplings are Fourier transforms of positive
> measures.** A coupling `J(r)` depending only on the displacement `r` is positive semidefinite, in
> the sense that every finite quadratic form `∑ c_i c̄_j J(r_i - r_j)` is nonnegative, if and only if
> it is the Fourier transform of a finite positive measure on the momenta, whose density is the
> dispersion of the coupling.

```lean
lemma isPositiveDefiniteSub_iff_exists_measure (J : G → ℂ) :
    TauCeti.IsPositiveDefiniteSub J ↔
      ∃ μ : Measure (PontryaginDual (Multiplicative G)), IsFiniteMeasure μ ∧ μ.InnerRegular ∧
        ∀ r : G, J r = ∫ χ, ((χ (Multiplicative.ofAdd r) : Circle) : ℂ) ∂μ
```

## Depends on

- [Positive-definite functions on an additive commutative group](../../mathematics/part-02/tauceti/part-01/analysis-positivedefinite-addgroup.md)

## Proof depends on

- [Bochner's theorem on discrete abelian groups](../../mathematics/part-02/tauceti/part-01/analysis-bochner-discretegroup.md)
- [Topology of Pontryagin duals](../../mathematics/part-02/tauceti/part-02/topology-algebra-pontryagindual.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Representation/StructureFactor.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/StructureFactor.lean)
