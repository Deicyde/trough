---
declaration: theorem
origin: cited
lean: TauCeti.Neuromanifold.realizedFunctions_polynomialRealization
statement: formalized
proof: formalized
---

# TauCeti.Neuromanifold.realizedFunctions_polynomialRealization

The functions realized by a jointly polynomial tuple are the evaluations of its coefficient
image.

```lean
TauCeti.Neuromanifold.realizedFunctions_polynomialRealization.{u_1, u_2, u_3, u_4} {W : Type u_1}
  {X : Type u_2} {J : Type u_3} [Fintype J] {K : Type u_4} [CommSemiring K]
  (P : J → MvPolynomial (W ⊕ X) K) :
  TauCeti.Neuromanifold.realizedFunctions (TauCeti.Neuromanifold.polynomialRealization P) =
    ⇑(MvPolynomial.tupleEvaluation J
          (MvPolynomial.restrictTotalDegree X K (TauCeti.Neuromanifold.polynomialInputDegree P))) ''
      Set.range (TauCeti.Neuromanifold.polynomialCoefficientMap P)
```

## Depends on

- [TauCeti.Neuromanifold.polynomialCoefficientMap](tauceti-neuromanifold-polynomialcoefficientmap.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Neuromanifold.realizedFunctions_polynomialRealization`](https://taucetiproject.org/docs/TauCeti/Geometry/Neuromanifold/Polynomial/Presentation.html#TauCeti.Neuromanifold.realizedFunctions_polynomialRealization).

## Sources

- [Tau Ceti documentation: `TauCeti.Neuromanifold.realizedFunctions_polynomialRealization`](https://taucetiproject.org/docs/TauCeti/Geometry/Neuromanifold/Polynomial/Presentation.html#TauCeti.Neuromanifold.realizedFunctions_polynomialRealization)
- [Source of `TauCeti.Neuromanifold.realizedFunctions_polynomialRealization` in TauCeti/Geometry/Neuromanifold/Polynomial/Presentation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Neuromanifold/Polynomial/Presentation.lean#L44)
- [Tau Ceti roadmap status: Neuromanifolds, parametrisations, and neurovarieties](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/Neuromanifolds/STATUS.md)
