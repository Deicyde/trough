---
declaration: theorem
origin: cited
lean: IsAlgebraic.irrationalityExponent_eq_two
statement: formalized
proof: formalized
---

# IsAlgebraic.irrationalityExponent_eq_two

The irrationality exponent of a real algebraic irrational number is two.

```lean
IsAlgebraic.irrationalityExponent_eq_two {α : ℝ} (hα : IsAlgebraic ℚ α) (hirr : Irrational α) :
  TauCeti.irrationalityExponent α = 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Roth's theorem (Roth, 1955)](roths-theorem-roth-1955.md)

## Lean

Formalized in Tau Ceti as [`IsAlgebraic.irrationalityExponent_eq_two`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Roth/Theorem.html#IsAlgebraic.irrationalityExponent_eq_two).

## Sources

- [Tau Ceti documentation: `IsAlgebraic.irrationalityExponent_eq_two`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Roth/Theorem.html#IsAlgebraic.irrationalityExponent_eq_two)
- [Source of `IsAlgebraic.irrationalityExponent_eq_two` in TauCeti/NumberTheory/DiophantineApproximation/Roth/Theorem.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/DiophantineApproximation/Roth/Theorem.lean#L282)
- [Tau Ceti roadmap status: Diophantine approximation and transcendence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/DiophantineApproximationAndTranscendence/STATUS.md)
