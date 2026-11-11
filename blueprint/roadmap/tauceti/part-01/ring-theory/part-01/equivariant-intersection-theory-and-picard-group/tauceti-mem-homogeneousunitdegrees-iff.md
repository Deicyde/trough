---
declaration: theorem
origin: cited
lean: TauCeti.mem_homogeneousUnitDegrees_iff
statement: formalized
proof: formalized
---

# TauCeti.mem_homogeneousUnitDegrees_iff

In a ring graded by an additive group, a degree lies in `homogeneousUnitDegrees 𝒜` if and only
if it is the degree of a homogeneous unit: products and inverses of homogeneous units are
homogeneous units, so the generating set is already a subgroup.

```lean
TauCeti.mem_homogeneousUnitDegrees_iff.{u_1, u_2, u_3} {ι : Type u_1} {A : Type u_2} {σ : Type u_3}
  [DecidableEq ι] [AddGroup ι] [Semiring A] [SetLike σ A] [AddSubmonoidClass σ A] {𝒜 : ι → σ}
  [GradedRing 𝒜] {d : ι} : d ∈ TauCeti.homogeneousUnitDegrees 𝒜 ↔ ∃ u, ↑u ∈ 𝒜 d
```

## Depends on

- [TauCeti.homogeneousUnitDegrees](tauceti-homogeneousunitdegrees.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.mem_homogeneousUnitDegrees_iff`](https://taucetiproject.org/docs/TauCeti/RingTheory/GradedAlgebra/Homogeneous/Units.html#TauCeti.mem_homogeneousUnitDegrees_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.mem_homogeneousUnitDegrees_iff`](https://taucetiproject.org/docs/TauCeti/RingTheory/GradedAlgebra/Homogeneous/Units.html#TauCeti.mem_homogeneousUnitDegrees_iff)
- [Source of `TauCeti.mem_homogeneousUnitDegrees_iff` in TauCeti/RingTheory/GradedAlgebra/Homogeneous/Units.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/GradedAlgebra/Homogeneous/Units.lean#L121)
- [Tau Ceti roadmap status: Equivariant intersection theory and Picard groups of quotient stacks](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/EquivariantIntersectionTheory/STATUS.md)
