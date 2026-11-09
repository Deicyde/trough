---
declaration: theorem
origin: cited
lean: DividedPowerAlgebra.isInternal_homogeneousSubmodule
statement: formalized
proof: formalized
---

# DividedPowerAlgebra.isInternal_homogeneousSubmodule

The homogeneous pieces of the divided power algebra form an internal direct sum: the sum
map `⨁ d, Γ^d_R(M) → Γ_R(M)` is bijective.

```lean
DividedPowerAlgebra.isInternal_homogeneousSubmodule.{u_1, u_2} {R : Type u_1} {M : Type u_2}
  [CommSemiring R] [AddCommMonoid M] [_root_.Module R M] :
  DirectSum.IsInternal DividedPowerAlgebra.homogeneousSubmodule
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`DividedPowerAlgebra.isInternal_homogeneousSubmodule`](https://taucetiproject.org/docs/TauCeti/RingTheory/DividedPowerAlgebra/Grading.html#DividedPowerAlgebra.isInternal_homogeneousSubmodule).

## Sources

- [Tau Ceti documentation: `DividedPowerAlgebra.isInternal_homogeneousSubmodule`](https://taucetiproject.org/docs/TauCeti/RingTheory/DividedPowerAlgebra/Grading.html#DividedPowerAlgebra.isInternal_homogeneousSubmodule)
- [Source of `DividedPowerAlgebra.isInternal_homogeneousSubmodule` in TauCeti/RingTheory/DividedPowerAlgebra/Grading.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/DividedPowerAlgebra/Grading.lean#L131)
- [Tau Ceti roadmap status: Derived module algebra](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DerivedModuleAlgebra/STATUS.md)
