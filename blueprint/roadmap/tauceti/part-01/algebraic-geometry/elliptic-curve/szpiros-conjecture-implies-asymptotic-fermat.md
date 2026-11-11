---
declaration: theorem
origin: cited
lean: TauCeti.AlgorithmicSzpiroConjecture.asymptoticFermat
statement: formalized
proof: formalized
---

# Szpiro's conjecture implies asymptotic Fermat

If `TauCeti.AlgorithmicSzpiroConjecture`
holds, there is an `N` such that `aⁿ + bⁿ = cⁿ` has no solution in positive integers for any
exponent `n ≥ N`. The bound `N` depends on the constant of Szpiro's conjecture for `ε = 1`, so it
is ineffective.

```lean
TauCeti.AlgorithmicSzpiroConjecture.asymptoticFermat (h : TauCeti.AlgorithmicSzpiroConjecture) :
  TauCeti.AsymptoticFermat
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Szpiro's conjecture for Frey curves](szpiros-conjecture-for-frey-curves.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgorithmicSzpiroConjecture.asymptoticFermat`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/FreyCurve/Szpiro.html#TauCeti.AlgorithmicSzpiroConjecture.asymptoticFermat), assuming [`TauCeti.AlgorithmicSzpiroConjecture`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Szpiro.html#TauCeti.AlgorithmicSzpiroConjecture), a proposition Tau Ceti defines.

## Sources

- [Tau Ceti documentation: `TauCeti.AlgorithmicSzpiroConjecture.asymptoticFermat`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/FreyCurve/Szpiro.html#TauCeti.AlgorithmicSzpiroConjecture.asymptoticFermat)
- [Source of `TauCeti.AlgorithmicSzpiroConjecture.asymptoticFermat` in TauCeti/AlgebraicGeometry/EllipticCurve/FreyCurve/Szpiro.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/EllipticCurve/FreyCurve/Szpiro.lean#L96)
