---
declaration: theorem
origin: cited
lean: TauCeti.exists_linearEquiv_iff_exists_isUnit_mem
statement: formalized
proof: formalized
---

# TauCeti.exists_linearEquiv_iff_exists_isUnit_mem

A grading `ℳ` of `A` compatible with `𝒜` is graded-isomorphic to the shift `A(d)`, whose
degree-`n` piece is `𝒜 (n + d)`, if and only if it has a homogeneous generator of degree `-d`: a
unit lying in `ℳ (-d)`.

```lean
TauCeti.exists_linearEquiv_iff_exists_isUnit_mem.{u_1, u_2, u_3, u_4} {ι : Type u_1} {A : Type u_2}
  {σ : Type u_3} {σM : Type u_4} [DecidableEq ι] [Semiring A] [SetLike σ A] [AddSubmonoidClass σ A]
  [SetLike σM A] [AddGroup ι] (𝒜 : ι → σ) [GradedRing 𝒜] (ℳ : ι → σM) [AddSubmonoidClass σM A]
  [DirectSum.Decomposition ℳ] [SetLike.GradedSMul 𝒜 ℳ] {d : ι} :
  (∃ φ, ∀ (n : ι) (x : A), φ x ∈ ℳ n ↔ x ∈ 𝒜 (n + d)) ↔ ∃ u, IsUnit u ∧ u ∈ ℳ (-d)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_linearEquiv_iff_exists_isUnit_mem`](https://taucetiproject.org/docs/TauCeti/RingTheory/GradedAlgebra/Homogeneous/Units.html#TauCeti.exists_linearEquiv_iff_exists_isUnit_mem).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_linearEquiv_iff_exists_isUnit_mem`](https://taucetiproject.org/docs/TauCeti/RingTheory/GradedAlgebra/Homogeneous/Units.html#TauCeti.exists_linearEquiv_iff_exists_isUnit_mem)
- [Source of `TauCeti.exists_linearEquiv_iff_exists_isUnit_mem` in TauCeti/RingTheory/GradedAlgebra/Homogeneous/Units.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/GradedAlgebra/Homogeneous/Units.lean#L193)
- [Tau Ceti roadmap status: Equivariant intersection theory and Picard groups of quotient stacks](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/EquivariantIntersectionTheory/STATUS.md)
