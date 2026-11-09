---
declaration: theorem
origin: cited
lean: TauCeti.AlgorithmicSzpiroConjecture.abcConjectureWithExponent
statement: formalized
proof: formalized
---

# Szpiro's conjecture implies the abc conjecture with exponent `3 / 2`

under
`TauCeti.AlgorithmicSzpiroConjecture`, for every `ε > 0` there is a constant `C` with
`max (|a|, |b|, |c|) ≤ C rad (a b c) ^ (3 / 2 + ε)` for all coprime `a + b = c`. For coprime
positive integers `a + b = c`, Szpiro's bound for Frey curves gives
`(a b c)² ≪_ε rad (a b c) ^ (6 + 4 ε)` (`TauCeti.AlgorithmicSzpiroConjecture.exists_sq_le`), and
`c² ≤ 2 a b c` because `a + b ≤ 2 a b`.

```lean
TauCeti.AlgorithmicSzpiroConjecture.abcConjectureWithExponent
  (h : TauCeti.AlgorithmicSzpiroConjecture) : TauCeti.AbcConjectureWithExponent (3 / 2)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Szpiro's conjecture for Frey curves](szpiros-conjecture-for-frey-curves.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgorithmicSzpiroConjecture.abcConjectureWithExponent`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/FreyCurve/Abc.html#TauCeti.AlgorithmicSzpiroConjecture.abcConjectureWithExponent), assuming [`TauCeti.AlgorithmicSzpiroConjecture`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Szpiro.html#TauCeti.AlgorithmicSzpiroConjecture), a proposition Tau Ceti defines.

## Sources

- [Tau Ceti documentation: `TauCeti.AlgorithmicSzpiroConjecture.abcConjectureWithExponent`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/FreyCurve/Abc.html#TauCeti.AlgorithmicSzpiroConjecture.abcConjectureWithExponent)
- [Source of `TauCeti.AlgorithmicSzpiroConjecture.abcConjectureWithExponent` in TauCeti/AlgebraicGeometry/EllipticCurve/FreyCurve/Abc.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/EllipticCurve/FreyCurve/Abc.lean#L201)
