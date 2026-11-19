---
declaration: abbrev
origin: cited
lean: TauCeti.ShiftClassGroup
statement: formalized
---

# TauCeti.ShiftClassGroup

The shift classes of a graded ring: the degree group modulo the degrees of the homogeneous
units. The shifts `A(d)` and `A(e)` of the graded module `A` are graded-isomorphic exactly when
`d` and `e` have the same class (`ShiftClassGroup.mk_eq_mk_iff`).

```lean
TauCeti.ShiftClassGroup.{u_1, u_2, u_3} {ι : Type u_1} {A : Type u_2} {σ : Type u_3}
  [AddCommGroup ι] [Monoid A] [SetLike σ A] (𝒜 : ι → σ) : Type u_1
```

## Depends on

- [TauCeti.homogeneousUnitDegrees](tauceti-homogeneousunitdegrees.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ShiftClassGroup`](https://taucetiproject.org/docs/TauCeti/RingTheory/GradedAlgebra/Homogeneous/Units.html#TauCeti.ShiftClassGroup).

## Sources

- [Tau Ceti documentation: `TauCeti.ShiftClassGroup`](https://taucetiproject.org/docs/TauCeti/RingTheory/GradedAlgebra/Homogeneous/Units.html#TauCeti.ShiftClassGroup)
- [Source of `TauCeti.ShiftClassGroup` in TauCeti/RingTheory/GradedAlgebra/Homogeneous/Units.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/GradedAlgebra/Homogeneous/Units.lean#L140)
- [Tau Ceti roadmap status: Equivariant intersection theory and Picard groups of quotient stacks](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/EquivariantIntersectionTheory/STATUS.md)
