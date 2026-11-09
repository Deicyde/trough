---
declaration: def
origin: cited
lean: DividedPowerAlgebra.baseChangeEquiv
statement: formalized
---

# Base change of divided power algebras

for a commutative `R`-algebra `S`, the canonical
map `S ⊗[R] Γ_R(M) → Γ_S(S ⊗[R] M)` is an isomorphism of `S`-algebras. No flatness is
assumed.

```lean
DividedPowerAlgebra.baseChangeEquiv.{u_1, u_2, u_3} (R : Type u_1) [CommSemiring R] (M : Type u_2)
  [AddCommMonoid M] [_root_.Module R M] (S : Type u_3) [CommSemiring S] [Algebra R S] :
  TensorProduct R S (DividedPowerAlgebra R M) ≃ₐ[S] DividedPowerAlgebra S (TensorProduct R S M)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`DividedPowerAlgebra.baseChangeEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/DividedPowerAlgebra/BaseChange.html#DividedPowerAlgebra.baseChangeEquiv).

## Sources

- [Tau Ceti documentation: `DividedPowerAlgebra.baseChangeEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/DividedPowerAlgebra/BaseChange.html#DividedPowerAlgebra.baseChangeEquiv)
- [Source of `DividedPowerAlgebra.baseChangeEquiv` in TauCeti/RingTheory/DividedPowerAlgebra/BaseChange.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/DividedPowerAlgebra/BaseChange.lean#L97)
- [Tau Ceti roadmap status: Derived module algebra](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DerivedModuleAlgebra/STATUS.md)
