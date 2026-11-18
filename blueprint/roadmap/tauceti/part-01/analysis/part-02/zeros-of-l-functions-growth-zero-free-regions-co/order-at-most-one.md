---
declaration: theorem
origin: cited
lean: TauCeti.LFunctions.dirichletData_completed_orderLE_one
statement: formalized
proof: formalized
---

# Order at most one

The completed function of a primitive nonprincipal Dirichlet record
is entire of order at most one.

```lean
TauCeti.LFunctions.dirichletData_completed_orderLE_one {N : ℕ} [NeZero N]
  (χ : DirichletCharacter ℂ N) (hχ : χ.IsPrimitive) (hne : χ ≠ 1) :
  TauCeti.OrderLE (TauCeti.LFunctions.dirichletData χ hχ).completed 1
```

## Depends on

- [Completed L-function data in the analytic normalization](../../../number-theory/part-01/l-functions-completions-and-functional-equations/completed-l-function-data-in-the-analytic-normal.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LFunctions.dirichletData_completed_orderLE_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LFunctions/Zeros/Completion/Dirichlet/Growth.html#TauCeti.LFunctions.dirichletData_completed_orderLE_one).

## Sources

- [Tau Ceti documentation: `TauCeti.LFunctions.dirichletData_completed_orderLE_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LFunctions/Zeros/Completion/Dirichlet/Growth.html#TauCeti.LFunctions.dirichletData_completed_orderLE_one)
- [Source of `TauCeti.LFunctions.dirichletData_completed_orderLE_one` in TauCeti/NumberTheory/LFunctions/Zeros/Completion/Dirichlet/Growth.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/LFunctions/Zeros/Completion/Dirichlet/Growth.lean#L65)
- [Tau Ceti roadmap status: Zeros of L-functions — growth, zero-free regions, counting, and the explicit formula](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ZerosOfLFunctions/STATUS.md)
