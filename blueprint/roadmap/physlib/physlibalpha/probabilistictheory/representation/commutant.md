---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.UnitaryRep.projection, ProbabilisticTheory.QuantumMechanics.UnitaryRep.projection_isStarProjection, ProbabilisticTheory.QuantumMechanics.UnitaryRep.projection_eq_zero_of_not_measurable, ProbabilisticTheory.QuantumMechanics.UnitaryRep.projection_commute, ProbabilisticTheory.QuantumMechanics.UnitaryRep.commute_starProjection_of_mapsTo, ProbabilisticTheory.QuantumMechanics.UnitaryRep.inner_unitary_left, ProbabilisticTheory.QuantumMechanics.UnitaryRep.mapsTo_projection_of_invariant, ProbabilisticTheory.QuantumMechanics.UnitaryRep.mapsTo_of_projection_invariant
statement: formalized
proof: formalized
---

# The commutant of a unitary representation of an abelian group

The module `PhyslibAlpha.ProbabilisticTheory.Representation.Commutant`, [PhyslibAlpha/ProbabilisticTheory/Representation/Commutant.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Commutant.lean): 14 declarations, 10 with a docstring.

> Every bounded operator commuting with a unitary representation of an abelian group is decomposable
> over the characters of the group.

## i. Overview

> The spectral measure `P` of a unitary representation `π` commutes with every bounded operator `T`
> that commutes with all `π(g)`: such an operator maps each spectral subspace into itself, it is
> reduced by the spectral decomposition of `π`. Consequently the closed subspaces invariant under
> the representation are exactly the closed subspaces invariant under the spectral measure, and
> the spectral projection onto a single character `χ` of a countable group is the projection onto
> the subspace of vectors of crystal momentum `χ`.

## ii. Key results

> - `UnitaryRep.projection` : the spectral projection of a set of characters.
> - `UnitaryRep.projection_commute` : the spectral projections commute with the commutant.
> - `UnitaryRep.mapsTo_projection_of_invariant` : spectral projections preserve every closed
>   invariant subspace.
> - `UnitaryRep.range_projection_singleton` : the projection onto the character `χ` is the
>   projection onto the subspace of momentum `χ`.

## iv. References

> * None.

## A. Spectral projections

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.projection`**, a def, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Commutant.lean#L72).

> The spectral projection of a set of characters, as a bounded operator.

```lean
def projection (S : Set (PontryaginDual (Multiplicative G))) : H →L[ℂ] H
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.projection_isStarProjection`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Commutant.lean#L75).

```lean
lemma projection_isStarProjection (S : Set (PontryaginDual (Multiplicative G))) :
    IsStarProjection (projection π S)
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.projection_eq_zero_of_not_measurable`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Commutant.lean#L82).

```lean
lemma projection_eq_zero_of_not_measurable {S : Set (PontryaginDual (Multiplicative G))}
    (hS : ¬ MeasurableSet S) : projection π S = 0
```

## B. Commutation with the commutant

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.projection_commute`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Commutant.lean#L92).

> **The commutant is decomposable**: every bounded operator commuting with the representation
> commutes with every spectral projection.

```lean
lemma projection_commute {T : H →L[ℂ] H}
    (hT : ∀ g, Commute ((π g : unitary (H →L[ℂ] H)) : H →L[ℂ] H) T)
    (S : Set (PontryaginDual (Multiplicative G))) : Commute (projection π S) T
```

## C. Invariant subspaces

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.commute_starProjection_of_mapsTo`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Commutant.lean#L113).

> An operator mapping a closed subspace and its orthogonal complement into themselves commutes
> with the orthogonal projection onto the subspace.

```lean
lemma commute_starProjection_of_mapsTo (W : Submodule ℂ H) [W.HasOrthogonalProjection]
    {T : H →L[ℂ] H} (hW : ∀ v ∈ W, T v ∈ W) (hWo : ∀ v ∈ Wᗮ, T v ∈ Wᗮ) :
    Commute (W.starProjection : H →L[ℂ] H) T
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.inner_unitary_left`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Commutant.lean#L131).

```lean
lemma inner_unitary_left (g : Multiplicative G) (x w : H) :
    ⟪((π g : unitary (H →L[ℂ] H)) : H →L[ℂ] H) x, w⟫_ℂ =
      ⟪x, ((π g⁻¹ : unitary (H →L[ℂ] H)) : H →L[ℂ] H) w⟫_ℂ
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.mapsTo_projection_of_invariant`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Commutant.lean#L142).

> A closed subspace invariant under the representation is invariant under every spectral
> projection.

```lean
lemma mapsTo_projection_of_invariant (W : Submodule ℂ H) [W.HasOrthogonalProjection]
    (hW : ∀ g, ∀ v ∈ W, ((π g : unitary (H →L[ℂ] H)) : H →L[ℂ] H) v ∈ W)
    (S : Set (PontryaginDual (Multiplicative G))) {v : H} (hv : v ∈ W) :
    projection π S v ∈ W
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.mapsTo_of_projection_invariant`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Commutant.lean#L162).

> A closed subspace invariant under every spectral projection is invariant under the
> representation.

```lean
lemma mapsTo_of_projection_invariant (W : Submodule ℂ H) [W.HasOrthogonalProjection]
    (hW : ∀ (S : Set (PontryaginDual (Multiplicative G))), ∀ v ∈ W, projection π S v ∈ W)
    (g : Multiplicative G) {v : H} (hv : v ∈ W) :
    ((π g : unitary (H →L[ℂ] H)) : H →L[ℂ] H) v ∈ W
```

## D. Sectors of definite momentum

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.toEnd`**, a def, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Commutant.lean#L197).

> The linear action of a unitary representation on its Hilbert space.

```lean
def toEnd : Multiplicative G →* Module.End ℂ H
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.toEnd_apply`**, a lemma, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Commutant.lean#L206).

```lean
lemma toEnd_apply (g : Multiplicative G) (v : H) :
    toEnd π g v = ((π g : unitary (H →L[ℂ] H)) : H →L[ℂ] H) v
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.character_mul_projection_singleton`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Commutant.lean#L211).

> The operator `π(g)` acts on the spectral projection of the single character `χ` as the scalar
> `χ(g)`.

```lean
lemma character_mul_projection_singleton (χ : PontryaginDual (Multiplicative G))
    (g : Multiplicative G) :
    ((π g : unitary (H →L[ℂ] H)) : H →L[ℂ] H) * projection π {χ} =
      ((χ g : Circle) : ℂ) • projection π {χ}
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.ae_eq_of_mem_sector`**, a lemma, [line 262](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Commutant.lean#L262).

> A vector of momentum `χ` is carried by the single character `χ`: its spectral measure is
> concentrated at `χ`.

```lean
lemma ae_eq_of_mem_sector (χ : PontryaginDual (Multiplicative G)) {v : H}
    (hv : v ∈ ProbabilisticTheory.Representation.sector (toEnd π) (fun g => ((χ g : Circle) : ℂ))) :
    ∀ᵐ χ' ∂vectorMeasure π v, χ' = χ
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.projection_singleton_eq_self_of_mem_sector`**, a lemma, [line 329](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Commutant.lean#L329).

> **A vector of momentum `χ` lies in the range of the spectral projection of `χ`.**

```lean
lemma projection_singleton_eq_self_of_mem_sector (χ : PontryaginDual (Multiplicative G)) {v : H}
    (hv : v ∈ ProbabilisticTheory.Representation.sector (toEnd π) (fun g => ((χ g : Circle) : ℂ))) :
    projection π {χ} v = v
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.range_projection_singleton`**, a lemma, [line 370](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Commutant.lean#L370).

> **The spectral projection of a single character is the projection onto the sector of
> definite momentum**: its range is the subspace of vectors on which the group acts through the
> character.

```lean
lemma range_projection_singleton (χ : PontryaginDual (Multiplicative G)) :
    LinearMap.range (projection π {χ} : H →L[ℂ] H).toLinearMap =
      ProbabilisticTheory.Representation.sector (toEnd π) (fun g => ((χ g : Circle) : ℂ))
```

## Depends on

- [Crystal momentum sectors](momentumsectors.md)
- [The spectral measure of a vector](vectormeasure.md)

## Proof depends on

- [Operators commuting with a spectral measure](../hilbertspace/part-02/unbounded-boundedintegralcommute.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Representation/Commutant.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Commutant.lean)
