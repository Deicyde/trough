---
declaration: def
origin: cited
lean: DividedPowerAlgebra.baseChangeHomogeneousEquiv
statement: formalized
---

# Base change of homogeneous divided powers

for a commutative `R`-algebra `S`, the base
change isomorphism restricts to an `S`-linear isomorphism
`S ⊗[R] Γ^d_R(M) ≃ₗ[S] Γ^d_S(S ⊗[R] M)` taking `1 ⊗ dp R d m` to `dp S d (1 ⊗ m)`
(`baseChangeHomogeneousEquiv_one_tmul_dp`). No flatness is assumed.

```lean
DividedPowerAlgebra.baseChangeHomogeneousEquiv.{u_1, u_2, u_3} (R : Type u_1) [CommSemiring R]
  (M : Type u_2) [AddCommMonoid M] [_root_.Module R M] (S : Type u_3) [CommSemiring S] [Algebra R S]
  (d : ℕ) :
  TensorProduct R S ↥(DividedPowerAlgebra.homogeneousSubmodule d) ≃ₗ[S]
    ↥(DividedPowerAlgebra.homogeneousSubmodule d)
```

## Depends on

- [Base change of divided power algebras](base-change-of-divided-power-algebras.md)

## Proof depends on

- [DividedPowerAlgebra.isInternal_homogeneousSubmodule](dividedpoweralgebra-isinternal-homogeneoussubmod.md)

## Lean

Formalized in Tau Ceti as [`DividedPowerAlgebra.baseChangeHomogeneousEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/DividedPowerAlgebra/BaseChange.html#DividedPowerAlgebra.baseChangeHomogeneousEquiv).

## Sources

- [Tau Ceti documentation: `DividedPowerAlgebra.baseChangeHomogeneousEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/DividedPowerAlgebra/BaseChange.html#DividedPowerAlgebra.baseChangeHomogeneousEquiv)
- [Source of `DividedPowerAlgebra.baseChangeHomogeneousEquiv` in TauCeti/RingTheory/DividedPowerAlgebra/BaseChange.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/DividedPowerAlgebra/BaseChange.lean#L196)
- [Tau Ceti roadmap status: Derived module algebra](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DerivedModuleAlgebra/STATUS.md)
