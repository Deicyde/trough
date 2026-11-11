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
- [Source of `TauCeti.LFunctions.re_mem_Ioo_of_dirichletData_entireCompletion_eq_zero` in TauCeti/NumberTheory/LFunctions/Zeros/Completion/Dirichlet/Zeros.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LFunctions/Zeros/Completion/Dirichlet/Zeros.lean#L61)
- [Tau Ceti roadmap status: Zeros of L-functions — growth, zero-free regions, counting, and the explicit formula](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ZerosOfLFunctions/STATUS.md)
