---
declaration: theorem
origin: cited
lean: TauCeti.AlgorithmicModifiedSzpiroConjecture.algorithmicSzpiroConjecture
statement: formalized
proof: formalized
---

# The modified Szpiro conjecture implies Szpiro's conjecture, with the same constants

the
relation `1728 Δ = c₄³ - c₆²` on the reduced minimal model gives `|Δ_min| ≤ max (|c₄|³, c₆²)`.

```lean
TauCeti.AlgorithmicModifiedSzpiroConjecture.algorithmicSzpiroConjecture
  (h : TauCeti.AlgorithmicModifiedSzpiroConjecture) : TauCeti.AlgorithmicSzpiroConjecture
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Jacobian criterion as two equalities, the form `Nonsingular` negates](../elliptic-curve/the-jacobian-criterion-as-two-equalities-the-for.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgorithmicModifiedSzpiroConjecture.algorithmicSzpiroConjecture`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Szpiro.html#TauCeti.AlgorithmicModifiedSzpiroConjecture.algorithmicSzpiroConjecture).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgorithmicModifiedSzpiroConjecture.algorithmicSzpiroConjecture`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Szpiro.html#TauCeti.AlgorithmicModifiedSzpiroConjecture.algorithmicSzpiroConjecture)
- [Source of `TauCeti.AlgorithmicModifiedSzpiroConjecture.algorithmicSzpiroConjecture` in TauCeti/AlgebraicGeometry/EllipticCurve/Szpiro.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/EllipticCurve/Szpiro.lean#L189)
