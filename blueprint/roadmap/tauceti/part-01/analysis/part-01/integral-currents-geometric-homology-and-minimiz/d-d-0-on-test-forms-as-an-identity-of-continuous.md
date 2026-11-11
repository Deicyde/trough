---
declaration: theorem
origin: cited
lean: TestFunction.extDerivCLM_comp_extDerivCLM
statement: formalized
proof: formalized
---

# `d ∘ d = 0` on test forms, as an identity of continuous linear maps

```lean
TestFunction.extDerivCLM_comp_extDerivCLM.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F]
  {Ω : TopologicalSpace.Opens E} {k : ℕ} : TestFunction.extDerivCLM ∘SL TestFunction.extDerivCLM = 0
```

## Depends on

- [TestFunction.extDerivCLM](testfunction-extderivclm.md)

## Lean

Formalized in Tau Ceti as [`TestFunction.extDerivCLM_comp_extDerivCLM`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/TestFunction/ExtDeriv.html#TestFunction.extDerivCLM_comp_extDerivCLM).

## Sources

- [Tau Ceti documentation: `TestFunction.extDerivCLM_comp_extDerivCLM`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/TestFunction/ExtDeriv.html#TestFunction.extDerivCLM_comp_extDerivCLM)
- [Source of `TestFunction.extDerivCLM_comp_extDerivCLM` in TauCeti/Analysis/Distribution/TestFunction/ExtDeriv.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Distribution/TestFunction/ExtDeriv.lean#L93)
- [Tau Ceti roadmap status: Integral currents, geometric homology and minimizing hypersurfaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GeometricCurrents/STATUS.md)
