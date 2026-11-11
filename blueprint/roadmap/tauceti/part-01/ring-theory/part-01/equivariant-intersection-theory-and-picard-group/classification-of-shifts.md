---
declaration: theorem
origin: cited
lean: TauCeti.sub_mem_homogeneousUnitDegrees_iff
statement: formalized
proof: formalized
---

# Classification of shifts

The shifts `A(d)` and `A(e)` of the graded module `A`, with
degree-`n` pieces `𝒜 (n + d)` and `𝒜 (n + e)`, are graded-isomorphic if and only if `d - e` is
the degree of a homogeneous unit.

```lean
TauCeti.sub_mem_homogeneousUnitDegrees_iff.{u_1, u_2, u_3} {ι : Type u_1} {A : Type u_2}
  {σ : Type u_3} [DecidableEq ι] [Semiring A] [SetLike σ A] [AddSubmonoidClass σ A] [AddCommGroup ι]
  (𝒜 : ι → σ) [GradedRing 𝒜] {d e : ι} :
  d - e ∈ TauCeti.homogeneousUnitDegrees 𝒜 ↔ ∃ φ, ∀ (n : ι) (x : A), φ x ∈ 𝒜 (n + e) ↔ x ∈ 𝒜 (n + d)
```

## Depends on

- [TauCeti.homogeneousUnitDegrees](tauceti-homogeneousunitdegrees.md)

## Proof depends on

- [TauCeti.mem_homogeneousUnitDegrees_iff](tauceti-mem-homogeneousunitdegrees-iff.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.sub_mem_homogeneousUnitDegrees_iff`](https://taucetiproject.org/docs/TauCeti/RingTheory/GradedAlgebra/Homogeneous/Units.html#TauCeti.sub_mem_homogeneousUnitDegrees_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.sub_mem_homogeneousUnitDegrees_iff`](https://taucetiproject.org/docs/TauCeti/RingTheory/GradedAlgebra/Homogeneous/Units.html#TauCeti.sub_mem_homogeneousUnitDegrees_iff)
- [Source of `TauCeti.sub_mem_homogeneousUnitDegrees_iff` in TauCeti/RingTheory/GradedAlgebra/Homogeneous/Units.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/GradedAlgebra/Homogeneous/Units.lean#L209)
- [Tau Ceti roadmap status: Equivariant intersection theory and Picard groups of quotient stacks](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/EquivariantIntersectionTheory/STATUS.md)
