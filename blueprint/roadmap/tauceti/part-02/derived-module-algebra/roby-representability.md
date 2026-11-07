---
declaration: def
origin: cited
lean: DividedPowerAlgebra.homogeneousLawEquiv
statement: formalized
---

# Roby representability

composition with the universal law `γ_d` is a linear equivalence
between linear maps `Γ^d_R(M) → N` and homogeneous polynomial laws `M → N` of degree `d`.

```lean
DividedPowerAlgebra.homogeneousLawEquiv.{u, u_1, u_2} (R : Type u) [CommSemiring R] (M : Type u_1)
  (N : Type u_2) [AddCommMonoid M] [_root_.Module R M] [AddCommMonoid N] [_root_.Module R N]
  (d : ℕ) :
  (↥(DividedPowerAlgebra.homogeneousSubmodule d) →ₗ[R] N) ≃ₗ[R]
    ↥(PolynomialLaw.homogeneousSubmodule R M N d)
```

## Depends on

- [DividedPowerAlgebra.gamma](dividedpoweralgebra-gamma.md)

## Proof depends on

- [DividedPowerAlgebra.isInternal\_homogeneousSubmodule](dividedpoweralgebra-isinternal-homogeneoussubmod.md)
- [PolynomialLaw.coeff](polynomiallaw-coeff.md)

## Lean

Formalized in Tau Ceti as [`DividedPowerAlgebra.homogeneousLawEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/DividedPowerAlgebra/Representability.html#DividedPowerAlgebra.homogeneousLawEquiv).

## Sources

- [Tau Ceti documentation: `DividedPowerAlgebra.homogeneousLawEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/DividedPowerAlgebra/Representability.html#DividedPowerAlgebra.homogeneousLawEquiv)
- [Source of `DividedPowerAlgebra.homogeneousLawEquiv` in TauCeti/RingTheory/DividedPowerAlgebra/Representability.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/DividedPowerAlgebra/Representability.lean#L438)
- [Tau Ceti roadmap status: Derived module algebra](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DerivedModuleAlgebra/STATUS.md)
