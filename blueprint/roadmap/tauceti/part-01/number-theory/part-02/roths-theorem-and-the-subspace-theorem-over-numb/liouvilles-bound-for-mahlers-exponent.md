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

- [Liouville's inequality](../diophantine-approximation/liouvilles-inequality.md)

## Lean

Formalized in Tau Ceti as [`IsAlgebraic.mahlerExponent_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/MahlerExponent.html#IsAlgebraic.mahlerExponent_le).

## Sources

- [Tau Ceti documentation: `IsAlgebraic.mahlerExponent_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/MahlerExponent.html#IsAlgebraic.mahlerExponent_le)
- [Source of `IsAlgebraic.mahlerExponent_le` in TauCeti/NumberTheory/DiophantineApproximation/MahlerExponent.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/DiophantineApproximation/MahlerExponent.lean#L151)
- [Tau Ceti roadmap status: Roth's theorem and the Subspace Theorem over number fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SubspaceTheorem/STATUS.md)
