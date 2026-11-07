---
declaration: theorem
origin: cited
lean: IsAlgebraic.irrationalityExponent_eq_two
statement: formalized
proof: formalized
---

# IsAlgebraic.irrationalityExponent\_eq\_two

The irrationality exponent of a real algebraic irrational number is two.

```lean
IsAlgebraic.irrationalityExponent_eq_two {α : ℝ} (hα : IsAlgebraic ℚ α) (hirr : Irrational α) :
  TauCeti.irrationalityExponent α = 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [IsAlgebraic.finite\_setOfPred\_abs\_sub\_le\_mulHeight₁\_rpow\_neg](isalgebraic-finite-setofpred-abs-sub-le-mulheigh.md)

## Lean

Formalized in Tau Ceti as [`IsAlgebraic.irrationalityExponent_eq_two`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Roth/Theorem.html#IsAlgebraic.irrationalityExponent_eq_two).

## Sources

- [Tau Ceti documentation: `IsAlgebraic.irrationalityExponent_eq_two`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Roth/Theorem.html#IsAlgebraic.irrationalityExponent_eq_two)
- [Source of `IsAlgebraic.irrationalityExponent_eq_two` in TauCeti/NumberTheory/DiophantineApproximation/Roth/Theorem.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/DiophantineApproximation/Roth/Theorem.lean#L294)
- [Tau Ceti roadmap status: Diophantine approximation and transcendence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DiophantineApproximationAndTranscendence/STATUS.md)
