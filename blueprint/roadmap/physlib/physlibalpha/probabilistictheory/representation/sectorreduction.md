---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.UnitaryRep.sector, ProbabilisticTheory.QuantumMechanics.UnitaryRep.mem_sector_iff, ProbabilisticTheory.QuantumMechanics.UnitaryRep.dualAct_image_image, ProbabilisticTheory.QuantumMechanics.UnitaryRep.measurableSet_dualAct_image, ProbabilisticTheory.QuantumMechanics.UnitaryRep.rho_inv_rho, ProbabilisticTheory.QuantumMechanics.UnitaryRep.rho_rho_inv, ProbabilisticTheory.QuantumMechanics.UnitaryRep.norm_rho, ProbabilisticTheory.QuantumMechanics.UnitaryRep.rho_projection_apply
statement: formalized
proof: formalized
---

# Symmetry reduction of translation-invariant operators to momentum sectors

The module `PhyslibAlpha.ProbabilisticTheory.Representation.SectorReduction`, [PhyslibAlpha/ProbabilisticTheory/Representation/SectorReduction.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/SectorReduction.lean): 16 declarations, 5 with a docstring.

> A bounded operator commuting with the translations and a covariant point group is reduced by the
> momentum sectors, and the symmetry relates its restrictions to sectors in one orbit.

## i. Overview

> Let `π` represent the translations `G` and `ρ` a covariant representation of a group `P` acting on
> `G`, so that together they represent `G ⋊ P`. The *sector* of a set `S` of characters is the range
> of the spectral projection `P(S)` of `π`: the vectors whose total momentum lies in `S`. A bounded
> operator `T` commuting with all `π(g)` commutes with every `P(S)`, and so restricts to each
> sector. If `T` also commutes with `ρ`, then `ρ(p)` restricts to a unitary equivalence of the
> sector of `S` and the sector of `p • S` which intertwines the restrictions of `T`. In particular
> the spectrum of `T` on the sector of `S` is the spectrum of `T` on the sector of `p • S`.
>
> For a single momentum, this says that the fibre Hamiltonians at momenta related by the point group
> are unitarily equivalent, so the spectrum is determined by the momenta in an irreducible zone. The
> statement makes no assumption on the nature of `T`: it applies to one particle, to many particles,
> to spins, to anything with a unitary representation of the symmetry group. For a self-adjoint
> generator `H` of an unbounded dynamics, `T` is the unitary group `e^{itH}`.

## ii. Key results

> - `UnitaryRep.sector` : the range of a spectral projection.
> - `UnitaryRep.sectorEquiv` : the isometric equivalence of the sectors of `S` and `p • S`.
> - `UnitaryRep.spectrum_sectorOp_eq` : the spectra of an invariant operator on the two sectors
>   agree.

## iv. References

> * None.

## A. Sectors

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.sector`**, a def, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/SectorReduction.lean#L77).

> The sector of a set of characters: the vectors of total momentum in the set, the range of the
> spectral projection.

```lean
def sector (S : Set (PontryaginDual (Multiplicative G))) : Submodule ℂ H
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.mem_sector_iff`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/SectorReduction.lean#L81).

```lean
lemma mem_sector_iff (S : Set (PontryaginDual (Multiplicative G))) (x : H) :
    x ∈ sector π S ↔ ∃ y, projection π S y = x
```

## B. The equivalence of sectors

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.dualAct_image_image`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/SectorReduction.lean#L89).

```lean
lemma dualAct_image_image (p : P) (S : Set (PontryaginDual (Multiplicative G))) :
    dualAct φ p⁻¹ '' (dualAct φ p '' S) = S
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.measurableSet_dualAct_image`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/SectorReduction.lean#L97).

```lean
lemma measurableSet_dualAct_image (p : P) {S : Set (PontryaginDual (Multiplicative G))}
    (hS : MeasurableSet S) : MeasurableSet (dualAct φ p '' S)
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.rho_inv_rho`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/SectorReduction.lean#L112).

```lean
lemma rho_inv_rho (p : P) (x : H) : (𝓡 p⁻¹) ((𝓡 p) x) = x
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.rho_rho_inv`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/SectorReduction.lean#L117).

```lean
lemma rho_rho_inv (p : P) (x : H) : (𝓡 p) ((𝓡 p⁻¹) x) = x
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.norm_rho`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/SectorReduction.lean#L120).

```lean
lemma norm_rho (p : P) (x : H) : ‖(𝓡 p) x‖ = ‖x‖
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.rho_projection_apply`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/SectorReduction.lean#L138).

```lean
lemma rho_projection_apply (p : P) {S : Set (PontryaginDual (Multiplicative G))}
    (hS : MeasurableSet S) (y : H) :
    (𝓡 p) (projection π S y) = projection π (dualAct φ p '' S) ((𝓡 p) y)
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.rho_mem_sector`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/SectorReduction.lean#L144).

```lean
lemma rho_mem_sector (p : P) {S : Set (PontryaginDual (Multiplicative G))}
    (hS : MeasurableSet S) {x : H} (hx : x ∈ sector π S) :
    (𝓡 p) x ∈ sector π (dualAct φ p '' S)
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.rho_inv_mem_sector`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/SectorReduction.lean#L151).

```lean
lemma rho_inv_mem_sector (p : P) {S : Set (PontryaginDual (Multiplicative G))}
    (hS : MeasurableSet S) {y : H} (hy : y ∈ sector π (dualAct φ p '' S)) :
    (𝓡 p⁻¹) y ∈ sector π S
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.sectorEquiv`**, a def, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/SectorReduction.lean#L161).

> **The equivalence of sectors**: `ρ(p)` is an isometric equivalence of the sector of `S` onto
> the sector of `p • S`.

```lean
def sectorEquiv (p : P) {S : Set (PontryaginDual (Multiplicative G))} (hS : MeasurableSet S) :
    sector π S ≃ₗᵢ[ℂ] sector π (dualAct φ p '' S)
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.coe_sectorEquiv`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/SectorReduction.lean#L171).

```lean
lemma coe_sectorEquiv (p : P) {S : Set (PontryaginDual (Multiplicative G))}
    (hS : MeasurableSet S) (x : sector π S) :
    ((sectorEquiv hcov p hS x : sector π (dualAct φ p '' S)) : H) = (𝓡 p) x.1
```

## C. Invariant operators

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.sectorOp`**, a def, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/SectorReduction.lean#L184).

> An operator commuting with the translations restricts to each sector.

```lean
def sectorOp (hT : ∀ g, Commute ((π g : unitary (H →L[ℂ] H)) : H →L[ℂ] H) T)
    (S : Set (PontryaginDual (Multiplicative G))) : Module.End ℂ (sector π S)
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.coe_sectorOp`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/SectorReduction.lean#L193).

```lean
lemma coe_sectorOp (hT : ∀ g, Commute ((π g : unitary (H →L[ℂ] H)) : H →L[ℂ] H) T)
    (S : Set (PontryaginDual (Multiplicative G))) (x : sector π S) :
    ((sectorOp hT S x : sector π S) : H) = T x.1
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.sectorEquiv_sectorOp`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/SectorReduction.lean#L203).

> **The equivalence of sectors intertwines the restrictions of an invariant operator.**

```lean
lemma sectorEquiv_sectorOp (p : P) {S : Set (PontryaginDual (Multiplicative G))}
    (hS : MeasurableSet S) (x : sector π S) :
    sectorEquiv hcov p hS (sectorOp hTπ S x) = sectorOp hTπ (dualAct φ p '' S)
      (sectorEquiv hcov p hS x)
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.spectrum_sectorOp_eq`**, a lemma, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/SectorReduction.lean#L215).

> **Symmetry reduction.** The spectrum of an operator invariant under the translations and the
> covariant point group, restricted to the sector of the characters in `S`, is its spectrum on the
> sector of the characters in `p • S`.

```lean
lemma spectrum_sectorOp_eq (p : P) {S : Set (PontryaginDual (Multiplicative G))}
    (hS : MeasurableSet S) :
    spectrum ℂ (sectorOp hTπ S) = spectrum ℂ (sectorOp hTπ (dualAct φ p '' S))
```

## Depends on

- [Covariance of the spectral measure under a finite group of symmetries](pointcovariance.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Representation/SectorReduction.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/SectorReduction.lean)
