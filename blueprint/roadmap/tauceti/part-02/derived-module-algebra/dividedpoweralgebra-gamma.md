---
declaration: def
origin: cited
lean: DividedPowerAlgebra.gamma
statement: formalized
---

# DividedPowerAlgebra.gamma

The universal homogeneous polynomial law `γ_d : M → Γ^d_R(M)` of degree `d`. After scalar
extension to a commutative `R`-algebra `S` it sends `∑ⱼ sⱼ ⊗ mⱼ` to
`∑_{∑ⱼ nⱼ = d} (∏ⱼ sⱼ ^ nⱼ) ⊗ ∏ⱼ dp R nⱼ mⱼ` (see `gamma_toFun_sum_tmul`), and its ground value is
`m ↦ dp R d m` (see `ground_gamma_apply`).

```lean
DividedPowerAlgebra.gamma.{u, u_1} (R : Type u) [CommSemiring R] (M : Type u_1) [AddCommMonoid M]
  [_root_.Module R M] (d : ℕ) : M →ₚₗ[R] ↥(DividedPowerAlgebra.homogeneousSubmodule d)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [DividedPowerAlgebra.isInternal_homogeneousSubmodule](dividedpoweralgebra-isinternal-homogeneoussubmod.md)

## Lean

Formalized in Tau Ceti as [`DividedPowerAlgebra.gamma`](https://taucetiproject.org/docs/TauCeti/RingTheory/DividedPowerAlgebra/UniversalLaw.html#DividedPowerAlgebra.gamma).

## Sources

- [Tau Ceti documentation: `DividedPowerAlgebra.gamma`](https://taucetiproject.org/docs/TauCeti/RingTheory/DividedPowerAlgebra/UniversalLaw.html#DividedPowerAlgebra.gamma)
- [Source of `DividedPowerAlgebra.gamma` in TauCeti/RingTheory/DividedPowerAlgebra/UniversalLaw.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/DividedPowerAlgebra/UniversalLaw.lean#L97)
- [Tau Ceti roadmap status: Derived module algebra](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DerivedModuleAlgebra/STATUS.md)
