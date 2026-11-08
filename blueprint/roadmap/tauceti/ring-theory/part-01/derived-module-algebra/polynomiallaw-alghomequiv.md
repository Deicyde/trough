---
declaration: def
origin: cited
lean: PolynomialLaw.algHomEquiv
statement: formalized
---

# PolynomialLaw.algHomEquiv

Algebra maps `A →ₐ[R] B` are identified with the multiplicative polynomial laws
`A →ₚₗ[R] B` homogeneous of degree one, by `φ ↦ φ.toLinearMap.toPolynomialLaw` with inverse
`IsHomogeneousOfDegree.toAlgHom`.

```lean
PolynomialLaw.algHomEquiv.{u, u_1, u_2} (R : Type u) [CommSemiring R] (A : Type u_1) (B : Type u_2)
  [Semiring A] [Algebra R A] [Semiring B] [Algebra R B] :
  (A →ₐ[R] B) ≃ { f // PolynomialLaw.IsHomogeneousOfDegree 1 f ∧ f.IsMultiplicative }
```

## Depends on

- [PolynomialLaw.IsMultiplicative](polynomiallaw-ismultiplicative.md)

## Lean

Formalized in Tau Ceti as [`PolynomialLaw.algHomEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/PolynomialLaw/Multiplicative.html#PolynomialLaw.algHomEquiv).

## Sources

- [Tau Ceti documentation: `PolynomialLaw.algHomEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/PolynomialLaw/Multiplicative.html#PolynomialLaw.algHomEquiv)
- [Source of `PolynomialLaw.algHomEquiv` in TauCeti/RingTheory/PolynomialLaw/Multiplicative.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/PolynomialLaw/Multiplicative.lean#L230)
- [Tau Ceti roadmap status: Derived module algebra](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DerivedModuleAlgebra/STATUS.md)
