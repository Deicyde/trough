---
declaration: theorem
origin: cited
lean: IsAlgebraic.mahlerExponent_le
statement: formalized
proof: formalized
---

# Liouville's bound for Mahler's exponent

If `ξ` is a real algebraic number of degree `D`
over `ℚ`, then `wₙ(ξ) ≤ D - 1` for every `n`.

```lean
IsAlgebraic.mahlerExponent_le {ξ : ℝ} (hξ : IsAlgebraic ℚ ξ) (n : ℕ) :
  TauCeti.mahlerExponent n ξ ≤ ↑((minpoly ℚ ξ).natDegree - 1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Liouville's inequality](liouvilles-inequality.md)

## Lean

Formalized in Tau Ceti as [`IsAlgebraic.mahlerExponent_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/MahlerExponent.html#IsAlgebraic.mahlerExponent_le).

## Sources

- [Tau Ceti documentation: `IsAlgebraic.mahlerExponent_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/MahlerExponent.html#IsAlgebraic.mahlerExponent_le)
- [Source of `IsAlgebraic.mahlerExponent_le` in TauCeti/NumberTheory/DiophantineApproximation/MahlerExponent.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/DiophantineApproximation/MahlerExponent.lean#L162)
