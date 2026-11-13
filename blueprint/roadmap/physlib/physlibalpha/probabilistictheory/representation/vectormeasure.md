---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.UnitaryRep.vectorMeasure, ProbabilisticTheory.QuantumMechanics.UnitaryRep.vectorMeasure_apply, ProbabilisticTheory.QuantumMechanics.UnitaryRep.vectorMeasure_univ, ProbabilisticTheory.QuantumMechanics.UnitaryRep.vectorMeasure_eq_map, ProbabilisticTheory.QuantumMechanics.UnitaryRep.inner_eq_integral_vectorMeasure, ProbabilisticTheory.QuantumMechanics.UnitaryRep.eq_vectorMeasure_of_transform_eq
statement: formalized
proof: formalized
---

# The spectral measure of a vector

The module `PhyslibAlpha.ProbabilisticTheory.Representation.VectorMeasure`, [PhyslibAlpha/ProbabilisticTheory/Representation/VectorMeasure.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/VectorMeasure.lean): 7 declarations (1 instance with no name), 5 with a docstring.

> The distribution of a vector over the characters of the group, and its uniqueness.

## i. Overview

> For a unitary representation `π` of an abelian group and a vector `ξ`, the diagonal measure
> `S ↦ ‖P(S) ξ‖²` of the spectral measure is a finite measure `μ_ξ` on the Pontryagin dual with
> `⟪ξ, π(g) ξ⟫ = ∫ χ(g) dμ_ξ(χ)`. It is the distribution of `ξ` over the characters of the group;
> for a state it is the momentum distribution. Its total mass is `‖ξ‖²`. For a countable group, a
> finite measure on the dual is determined by its Fourier–Stieltjes transform, so `μ_ξ` is the
> unique measure with this property.

## ii. Key results

> - `UnitaryRep.vectorMeasure` : the spectral measure `μ_ξ` of a vector.
> - `UnitaryRep.inner_eq_integral_vectorMeasure` : `⟪ξ, π(g) ξ⟫ = ∫ χ(g) dμ_ξ(χ)`.
> - `UnitaryRep.vectorMeasure_univ` : the total mass of `μ_ξ` is `‖ξ‖²`.
> - `UnitaryRep.eq_vectorMeasure_of_transform_eq` : uniqueness of the spectral measure of a vector.

## iv. References

> * None.

## A. The spectral measure of a vector

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.vectorMeasure`**, a def, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/VectorMeasure.lean#L67).

> The spectral measure `S ↦ ‖P(S) ξ‖²` of a vector `ξ`, a finite measure on the Pontryagin dual:
> the distribution of `ξ` over the characters of the group.

```lean
def vectorMeasure (ξ : H) : Measure (PontryaginDual (Multiplicative G))
```

**An instance with no name**, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/VectorMeasure.lean#L70).

```lean
instance (ξ : H) : IsFiniteMeasure (vectorMeasure π ξ)
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.vectorMeasure_apply`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/VectorMeasure.lean#L73).

```lean
lemma vectorMeasure_apply (ξ : H) {S : Set (PontryaginDual (Multiplicative G))}
    (hS : MeasurableSet S) :
    vectorMeasure π ξ S = ENNReal.ofReal (‖spectralMeasure π S ξ‖ ^ 2)
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.vectorMeasure_univ`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/VectorMeasure.lean#L79).

> The total mass of the spectral measure of a vector is its squared norm.

```lean
lemma vectorMeasure_univ (ξ : H) : vectorMeasure π ξ univ = ENNReal.ofReal (‖ξ‖ ^ 2)
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.vectorMeasure_eq_map`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/VectorMeasure.lean#L83).

> The vector measure is the pushforward of the Riesz measure of the vector state.

```lean
lemma vectorMeasure_eq_map (ξ : H) :
    vectorMeasure π ξ = Measure.map (dual π) (starHomScalarMeasure (family π).starHom ξ)
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.inner_eq_integral_vectorMeasure`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/VectorMeasure.lean#L91).

> **The spectral measure of a vector represents its matrix coefficients**:
> `⟪ξ, π(g) ξ⟫ = ∫ χ(g) dμ_ξ(χ)`.

```lean
lemma inner_eq_integral_vectorMeasure (ξ : H) (g : Multiplicative G) :
    ⟪ξ, ((π g : unitary (H →L[ℂ] H)) : H →L[ℂ] H) ξ⟫_ℂ =
      ∫ χ, ((χ g : Circle) : ℂ) ∂vectorMeasure π ξ
```

## B. Uniqueness

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.eq_vectorMeasure_of_transform_eq`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/VectorMeasure.lean#L111).

> **Uniqueness of the spectral measure of a vector.** For a countable group, a finite measure on
> the Pontryagin dual whose Fourier–Stieltjes transform is `g ↦ ⟪ξ, π(g) ξ⟫` is the spectral
> measure of `ξ`.

```lean
lemma eq_vectorMeasure_of_transform_eq (ξ : H) (μ : Measure (PontryaginDual (Multiplicative G)))
    [IsFiniteMeasure μ]
    (h : ∀ g : Multiplicative G, ∫ χ, ((χ g : Circle) : ℂ) ∂μ =
      ⟪ξ, ((π g : unitary (H →L[ℂ] H)) : H →L[ℂ] H) ξ⟫_ℂ) :
    μ = vectorMeasure π ξ
```

## Depends on

- [The spectral measure of a unitary representation of an abelian group](abelianspectral.md)

## Proof depends on

- [Uniqueness of Fourier--Stieltjes measures on a Pontryagin dual](../../mathematics/part-02/tauceti/part-01/analysis-fourier-pontryagin-uniqueness.md)
- [Topology of Pontryagin duals](../../mathematics/part-02/tauceti/part-02/topology-algebra-pontryagindual.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Representation/VectorMeasure.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/VectorMeasure.lean)
