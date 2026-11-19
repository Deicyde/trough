---
declaration: theorem
origin: cited
lean: TauCeti.eq_map_mulLeft_of_isUnit_mem
statement: formalized
proof: formalized
---

# Shift classification, submodule form

If a grading `ℳ` of a commutative algebra `A`,
compatible with the grading `𝒜`, has a homogeneous unit `u ∈ ℳ c`, then `ℳ n = u • 𝒜 (n - c)` for
every `n`: the graded module `(A, ℳ)` is the shift `A(-c)`.

```lean
TauCeti.eq_map_mulLeft_of_isUnit_mem.{u_1, u_2, u_3} {ι : Type u_1} {R : Type u_2} {A : Type u_3}
  [DecidableEq ι] [AddGroup ι] [CommSemiring R] [CommSemiring A] [Algebra R A]
  (𝒜 ℳ : ι → Submodule R A) [GradedAlgebra 𝒜] [DirectSum.Decomposition ℳ] [SetLike.GradedSMul 𝒜 ℳ]
  {u : A} (hu : IsUnit u) {c : ι} (hmem : u ∈ ℳ c) (n : ι) :
  ℳ n = Submodule.map (LinearMap.mulLeft R u) (𝒜 (n - c))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.eq_map_mulLeft_of_isUnit_mem`](https://taucetiproject.org/docs/TauCeti/RingTheory/GradedAlgebra/Homogeneous/Units.html#TauCeti.eq_map_mulLeft_of_isUnit_mem).

## Sources

- [Tau Ceti documentation: `TauCeti.eq_map_mulLeft_of_isUnit_mem`](https://taucetiproject.org/docs/TauCeti/RingTheory/GradedAlgebra/Homogeneous/Units.html#TauCeti.eq_map_mulLeft_of_isUnit_mem)
- [Source of `TauCeti.eq_map_mulLeft_of_isUnit_mem` in TauCeti/RingTheory/GradedAlgebra/Homogeneous/Units.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/GradedAlgebra/Homogeneous/Units.lean#L243)
- [Tau Ceti roadmap status: Equivariant intersection theory and Picard groups of quotient stacks](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/EquivariantIntersectionTheory/STATUS.md)
