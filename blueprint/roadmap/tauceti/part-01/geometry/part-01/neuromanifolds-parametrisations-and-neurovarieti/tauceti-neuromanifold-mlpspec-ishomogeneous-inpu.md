---
declaration: theorem
origin: cited
lean: TauCeti.Neuromanifold.MLPSpec.isHomogeneous_inputPolynomial_polynomialRealizeWeights_monomial
statement: formalized
proof: formalized
---

# TauCeti.Neuromanifold.MLPSpec.isHomogeneous_inputPolynomial_polynomialRealizeWeights_monomial

The jointly polynomial tuple of a bias-free monomial MLP is homogeneous in its inputs of
degree the product of the hidden exponents, with a linear output head.

```lean
TauCeti.Neuromanifold.MLPSpec.isHomogeneous_inputPolynomial_polynomialRealizeWeights_monomial.{u_1}
  {K : Type u_1} {L : ℕ} [CommSemiring K] (A : TauCeti.Neuromanifold.MLPSpec K L)
  (r : Fin (L - 1) → ℕ) (o : Fin (A.width (Fin.last L))) :
  (TauCeti.Neuromanifold.inputPolynomial (A.polynomialRealizeWeights fun j => Polynomial.X ^ r j)
        o).IsHomogeneous
    (∏ j, r j)
```

## Depends on

- [TauCeti.Neuromanifold.MLPSpec](tauceti-neuromanifold-mlpspec.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Neuromanifold.MLPSpec.isHomogeneous_inputPolynomial_polynomialRealizeWeights_monomial`](https://taucetiproject.org/docs/TauCeti/Geometry/Neuromanifold/MLP/Homogeneous.html#TauCeti.Neuromanifold.MLPSpec.isHomogeneous_inputPolynomial_polynomialRealizeWeights_monomial).

## Sources

- [Tau Ceti documentation: `TauCeti.Neuromanifold.MLPSpec.isHomogeneous_inputPolynomial_polynomialRealizeWeights_monomial`](https://taucetiproject.org/docs/TauCeti/Geometry/Neuromanifold/MLP/Homogeneous.html#TauCeti.Neuromanifold.MLPSpec.isHomogeneous_inputPolynomial_polynomialRealizeWeights_monomial)
- [Source of `TauCeti.Neuromanifold.MLPSpec.isHomogeneous_inputPolynomial_polynomialRealizeWeights_monomial` in TauCeti/Geometry/Neuromanifold/MLP/Homogeneous.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Neuromanifold/MLP/Homogeneous.lean#L141)
- [Tau Ceti roadmap status: Neuromanifolds, parametrisations, and neurovarieties](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/Neuromanifolds/STATUS.md)
