---
declaration: theorem
origin: cited
lean: TauCeti.LFunctions.re_mem_Ioo_of_dirichletData_entireCompletion_eq_zero
statement: formalized
proof: formalized
---

# TauCeti.LFunctions.re_mem_Ioo_of_dirichletData_entireCompletion_eq_zero

Every zero of a nonprincipal primitive Dirichlet entire completion lies in the open
critical strip.

```lean
TauCeti.LFunctions.re_mem_Ioo_of_dirichletData_entireCompletion_eq_zero {N : ℕ} [NeZero N]
  (χ : DirichletCharacter ℂ N) (hχ : χ.IsPrimitive) (hne : χ ≠ 1) {ρ : ℂ}
  (hρ : (TauCeti.LFunctions.dirichletData χ hχ).entireCompletion ρ = 0) : ρ.re ∈ Set.Ioo 0 1
```

## Depends on

- [Completed L-function data in the analytic normalization](../../../number-theory/part-01/l-functions-completions-and-functional-equations/completed-l-function-data-in-the-analytic-normal.md)
- [TauCeti.LFunctions.AnalyticLFunctionData.entireCompletion](tauceti-lfunctions-analyticlfunctiondata-entirec.md)

## Proof depends on

- [Osgood's lemma](../../../geometry/part-01/complex-manifolds-dolbeault-theory-and-kahler-ge/osgoods-lemma.md)
- [TauCeti.LFunctions.dirichletData_hasFunctionalEquation](../../../number-theory/part-01/l-functions-completions-and-functional-equations/tauceti-lfunctions-dirichletdata-hasfunctionaleq.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LFunctions.re_mem_Ioo_of_dirichletData_entireCompletion_eq_zero`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LFunctions/Zeros/Completion/Dirichlet/Zeros.html#TauCeti.LFunctions.re_mem_Ioo_of_dirichletData_entireCompletion_eq_zero).

## Sources

- [Tau Ceti documentation: `TauCeti.LFunctions.re_mem_Ioo_of_dirichletData_entireCompletion_eq_zero`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LFunctions/Zeros/Completion/Dirichlet/Zeros.html#TauCeti.LFunctions.re_mem_Ioo_of_dirichletData_entireCompletion_eq_zero)
- [Source of `TauCeti.LFunctions.re_mem_Ioo_of_dirichletData_entireCompletion_eq_zero` in TauCeti/NumberTheory/LFunctions/Zeros/Completion/Dirichlet/Zeros.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/LFunctions/Zeros/Completion/Dirichlet/Zeros.lean#L61)
- [Tau Ceti roadmap status: Zeros of L-functions — growth, zero-free regions, counting, and the explicit formula](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ZerosOfLFunctions/STATUS.md)
