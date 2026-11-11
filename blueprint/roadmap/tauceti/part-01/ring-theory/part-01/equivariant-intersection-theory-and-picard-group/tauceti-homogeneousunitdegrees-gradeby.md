---
declaration: theorem
origin: cited
lean: TauCeti.homogeneousUnitDegrees_gradeBy
statement: formalized
proof: formalized
---

# TauCeti.homogeneousUnitDegrees_gradeBy

For the group algebra `R[G]` over a nontrivial commutative semiring, graded by an additive
homomorphism `f : G →+ ι` (so that `single g r` has degree `f g`), the degrees of the homogeneous
units are the range of `f`: each `single g 1` is a homogeneous unit of degree `f g`, and a nonzero
element of degree `d` has a monomial of degree `d`.

```lean
TauCeti.homogeneousUnitDegrees_gradeBy.{u_1, u_2, u_3} {ι : Type u_1} {G : Type u_2} [AddGroup ι]
  [AddGroup G] (R : Type u_3) [CommSemiring R] [Nontrivial R] (f : G →+ ι) :
  TauCeti.homogeneousUnitDegrees (AddMonoidAlgebra.gradeBy R ⇑f) = f.range
```

## Depends on

- [TauCeti.homogeneousUnitDegrees](tauceti-homogeneousunitdegrees.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.homogeneousUnitDegrees_gradeBy`](https://taucetiproject.org/docs/TauCeti/Algebra/MonoidAlgebra/Grading.html#TauCeti.homogeneousUnitDegrees_gradeBy).

## Sources

- [Tau Ceti documentation: `TauCeti.homogeneousUnitDegrees_gradeBy`](https://taucetiproject.org/docs/TauCeti/Algebra/MonoidAlgebra/Grading.html#TauCeti.homogeneousUnitDegrees_gradeBy)
- [Source of `TauCeti.homogeneousUnitDegrees_gradeBy` in TauCeti/Algebra/MonoidAlgebra/Grading.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/MonoidAlgebra/Grading.lean#L81)
- [Tau Ceti roadmap status: Equivariant intersection theory and Picard groups of quotient stacks](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/EquivariantIntersectionTheory/STATUS.md)
