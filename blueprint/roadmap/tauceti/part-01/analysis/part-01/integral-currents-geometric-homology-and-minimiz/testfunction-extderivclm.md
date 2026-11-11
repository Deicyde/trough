---
declaration: def
origin: cited
lean: TestFunction.extDerivCLM
statement: formalized
---

# TestFunction.extDerivCLM

The **exterior derivative** of test `k`-forms on `Ω` with coefficients in `F`, as a
continuous linear map into the test `(k + 1)`-forms. It is the alternatization
`ContinuousAlternatingMap.alternatizeUncurryFinCLM` of the Fréchet derivative
`TestFunction.fderivCLM`, so pointwise it is Mathlib's `extDeriv`.

```lean
TestFunction.extDerivCLM.{u_1, u_2} {E : Type u_1} {F : Type u_2} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F] {Ω : TopologicalSpace.Opens E}
  {k : ℕ} : TestFunction Ω (E [⋀^Fin k]→L[ℝ] F) ⊤ →L[ℝ] TestFunction Ω (E [⋀^Fin (k + 1)]→L[ℝ] F) ⊤
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TestFunction.extDerivCLM`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/TestFunction/ExtDeriv.html#TestFunction.extDerivCLM).

## Sources

- [Tau Ceti documentation: `TestFunction.extDerivCLM`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/TestFunction/ExtDeriv.html#TestFunction.extDerivCLM)
- [Source of `TestFunction.extDerivCLM` in TauCeti/Analysis/Distribution/TestFunction/ExtDeriv.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Distribution/TestFunction/ExtDeriv.lean#L64)
- [Tau Ceti roadmap status: Integral currents, geometric homology and minimizing hypersurfaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GeometricCurrents/STATUS.md)
