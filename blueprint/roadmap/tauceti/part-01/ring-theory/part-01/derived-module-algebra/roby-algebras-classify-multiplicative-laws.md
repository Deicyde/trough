---
declaration: def
origin: cited
lean: DividedPowerAlgebra.RobyAlgebra.algHomEquiv
statement: formalized
---

# Roby algebras classify multiplicative laws

algebra maps `Γ^d_R(A) →ₐ[R] B` are identified
with the multiplicative polynomial laws `A → B` homogeneous of degree `d`, by composition with the
universal multiplicative law `RobyAlgebra.gamma R A d`. In degree one, multiplicative laws are
also classified by `PolynomialLaw.algHomEquiv`.

```lean
DividedPowerAlgebra.RobyAlgebra.algHomEquiv.{u, u_1, u_2} (R : Type u) [CommSemiring R]
  (A : Type u_1) [Semiring A] [Algebra R A] (d : ℕ) (B : Type u_2) [Semiring B] [Algebra R B] :
  (DividedPowerAlgebra.RobyAlgebra R A d →ₐ[R] B) ≃
    { f // PolynomialLaw.IsHomogeneousOfDegree d f ∧ f.IsMultiplicative }
```

## Depends on

- [Roby representability](roby-representability.md)

## Lean

Formalized in Tau Ceti as [`DividedPowerAlgebra.RobyAlgebra.algHomEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/DividedPowerAlgebra/RobyAlgebra.html#DividedPowerAlgebra.RobyAlgebra.algHomEquiv).

## Sources

- [Tau Ceti documentation: `DividedPowerAlgebra.RobyAlgebra.algHomEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/DividedPowerAlgebra/RobyAlgebra.html#DividedPowerAlgebra.RobyAlgebra.algHomEquiv)
- [Source of `DividedPowerAlgebra.RobyAlgebra.algHomEquiv` in TauCeti/RingTheory/DividedPowerAlgebra/RobyAlgebra.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/DividedPowerAlgebra/RobyAlgebra.lean#L524)
- [Tau Ceti roadmap status: Derived module algebra](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DerivedModuleAlgebra/STATUS.md)
