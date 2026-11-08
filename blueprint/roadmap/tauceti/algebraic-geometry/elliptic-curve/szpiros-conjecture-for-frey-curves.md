---
declaration: theorem
origin: cited
lean: TauCeti.AlgorithmicSzpiroConjecture.exists_sq_le, TauCeti.AlgorithmicSzpiroConjecture.exists_sq_le_mul_radical_rpow, TauCeti.AlgorithmicSzpiroConjecture.asymptoticFermat, TauCeti.AlgorithmicSzpiroConjecture.abcConjectureWithExponent
statement: formalized
proof: formalized
---

# Szpiro's conjecture for Frey curves

Under `TauCeti.AlgorithmicSzpiroConjecture`, for every
`ε > 0` there is a constant `C` such that `(A B (A + B))² ≤ C rad (A B (A + B)) ^ (6 + ε)` for all
coprime integers `A` and `B` with `A B (A + B) ≠ 0`. This applies Szpiro's conjecture to the curve
of `TauCeti.exists_natAbs_sq_le_absNorm_minimalDiscriminantIdeal`.

```lean
TauCeti.AlgorithmicSzpiroConjecture.exists_sq_le (h : TauCeti.AlgorithmicSzpiroConjecture) {ε : ℝ}
  (hε : 0 < ε) :
  ∃ C,
    ∀ (A B : ℤ),
      IsCoprime A B →
        A * B * (A + B) ≠ 0 →
          ↑(A * B * (A + B)) ^ 2 ≤
            C * ↑(UniqueFactorizationMonoid.radical (A * B * (A + B)).natAbs) ^ (6 + ε)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Jacobian criterion as two equalities, the form `Nonsingular` negates](the-jacobian-criterion-as-two-equalities-the-for.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgorithmicSzpiroConjecture.exists_sq_le`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/FreyCurve/Abc.html#TauCeti.AlgorithmicSzpiroConjecture.exists_sq_le).

## Other forms

**Szpiro's conjecture for Frey curves.** Formalized in Tau Ceti as [`TauCeti.AlgorithmicSzpiroConjecture.exists_sq_le_mul_radical_rpow`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/FreyCurve/Szpiro.html#TauCeti.AlgorithmicSzpiroConjecture.exists_sq_le_mul_radical_rpow).

```lean
TauCeti.AlgorithmicSzpiroConjecture.exists_sq_le_mul_radical_rpow
  (h : TauCeti.AlgorithmicSzpiroConjecture) {ε : ℝ} (hε : 0 < ε) :
  ∃ C,
    ∀ (A B : ℤ),
      IsCoprime A B →
        4 ∣ A + 1 →
          32 ∣ B →
            B ≠ 0 →
              ↑(A * B * (A + B)) ^ 2 ≤
                C * ↑(UniqueFactorizationMonoid.radical (A * B * (A + B))) ^ (6 + ε)
```

**Szpiro's conjecture implies asymptotic Fermat.** Formalized in Tau Ceti as [`TauCeti.AlgorithmicSzpiroConjecture.asymptoticFermat`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/FreyCurve/Szpiro.html#TauCeti.AlgorithmicSzpiroConjecture.asymptoticFermat).

```lean
TauCeti.AlgorithmicSzpiroConjecture.asymptoticFermat (h : TauCeti.AlgorithmicSzpiroConjecture) :
  TauCeti.AsymptoticFermat
```

**Szpiro's conjecture implies the abc conjecture with exponent `3 / 2`.** Formalized in Tau Ceti as [`TauCeti.AlgorithmicSzpiroConjecture.abcConjectureWithExponent`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/FreyCurve/Abc.html#TauCeti.AlgorithmicSzpiroConjecture.abcConjectureWithExponent).

```lean
TauCeti.AlgorithmicSzpiroConjecture.abcConjectureWithExponent
  (h : TauCeti.AlgorithmicSzpiroConjecture) : TauCeti.AbcConjectureWithExponent (3 / 2)
```

## Sources

- [Tau Ceti documentation: `TauCeti.AlgorithmicSzpiroConjecture.exists_sq_le`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/FreyCurve/Abc.html#TauCeti.AlgorithmicSzpiroConjecture.exists_sq_le)
- [Source of `TauCeti.AlgorithmicSzpiroConjecture.exists_sq_le` in TauCeti/AlgebraicGeometry/EllipticCurve/FreyCurve/Abc.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/EllipticCurve/FreyCurve/Abc.lean#L171)
