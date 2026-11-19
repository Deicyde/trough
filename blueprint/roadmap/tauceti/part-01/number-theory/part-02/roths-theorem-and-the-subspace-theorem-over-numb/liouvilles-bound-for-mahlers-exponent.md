---
declaration: theorem
origin: cited
lean: IsAlgebraic.mahlerExponent_le, IsAlgebraic.algebraicApproximationExponent_le
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
- [Northcott's theorem for the Mahler measure](../../part-01/diophantine-approximation-and-transcendence/northcotts-theorem-for-the-mahler-measure.md)

## Lean

Formalized in Tau Ceti as [`IsAlgebraic.mahlerExponent_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/MahlerExponent.html#IsAlgebraic.mahlerExponent_le).

## Other forms

**Liouville's bound for Koksma's exponent.** Formalized in Tau Ceti as [`IsAlgebraic.algebraicApproximationExponent_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/AlgebraicExponent.html#IsAlgebraic.algebraicApproximationExponent_le).

```lean
IsAlgebraic.algebraicApproximationExponent_le {ξ : ℝ} (hξ : IsAlgebraic ℚ ξ) (n : ℕ) :
  TauCeti.algebraicApproximationExponent n ξ ≤ ↑((minpoly ℚ ξ).natDegree - 1)
```

## Sources

- [Tau Ceti documentation: `IsAlgebraic.mahlerExponent_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/MahlerExponent.html#IsAlgebraic.mahlerExponent_le)
- [Source of `IsAlgebraic.mahlerExponent_le` in TauCeti/NumberTheory/DiophantineApproximation/MahlerExponent.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/DiophantineApproximation/MahlerExponent.lean#L150)
- [Tau Ceti roadmap status: Roth's theorem and the Subspace Theorem over number fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SubspaceTheorem/STATUS.md)
