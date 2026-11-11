---
declaration: theorem
origin: cited
lean: TauCeti.LFunctions.dirichletData_hasFunctionalEquation
statement: formalized
proof: formalized
---

# TauCeti.LFunctions.dirichletData_hasFunctionalEquation

The conductor-normalized Dirichlet completion satisfies the functional equation against
the conjugate card, with Mathlib's Gauss-sum root number.

```lean
TauCeti.LFunctions.dirichletData_hasFunctionalEquation {N : ℕ} [NeZero N]
  (χ : DirichletCharacter ℂ N) (hχ : χ.IsPrimitive) :
  (TauCeti.LFunctions.dirichletData χ hχ).HasFunctionalEquation
```

## Depends on

- [Completed L-function data in the analytic normalization](completed-l-function-data-in-the-analytic-normal.md)

## Proof depends on

- [Osgood's lemma](../../../geometry/part-01/complex-manifolds-dolbeault-theory-and-kahler-ge/osgoods-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LFunctions.dirichletData_hasFunctionalEquation`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LFunctions/Dirichlet/Basic.html#TauCeti.LFunctions.dirichletData_hasFunctionalEquation).

## Sources

- [Tau Ceti documentation: `TauCeti.LFunctions.dirichletData_hasFunctionalEquation`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LFunctions/Dirichlet/Basic.html#TauCeti.LFunctions.dirichletData_hasFunctionalEquation)
- [Source of `TauCeti.LFunctions.dirichletData_hasFunctionalEquation` in TauCeti/NumberTheory/LFunctions/Dirichlet/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LFunctions/Dirichlet/Basic.lean#L192)
- [Tau Ceti roadmap status: L-functions — completions and functional equations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/LFunctions/STATUS.md)
