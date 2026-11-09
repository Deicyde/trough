---
declaration: theorem
origin: cited
lean: Orientation.integrationCurrent_extDerivCLM
statement: formalized
proof: formalized
---

# Stokes' theorem for test forms

the integration current annihilates every exact test
form.

```lean
Orientation.integrationCurrent_extDerivCLM.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E] {k : ℕ}
  (o : Orientation ℝ E (Fin (k + 1))) (Ω : TopologicalSpace.Opens E)
  (ω : TestFunction Ω (E [⋀^Fin k]→L[ℝ] ℝ) ⊤) :
  (o.integrationCurrent Ω) (TestFunction.extDerivCLM ω) = 0
```

## Depends on

- [Orientation.integrationCurrent](orientation-integrationcurrent.md)
- [TestFunction.extDerivCLM](testfunction-extderivclm.md)

## Lean

Formalized in Tau Ceti as [`Orientation.integrationCurrent_extDerivCLM`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/TestFunction/IntegrationCurrent.html#Orientation.integrationCurrent_extDerivCLM).

## Sources

- [Tau Ceti documentation: `Orientation.integrationCurrent_extDerivCLM`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/TestFunction/IntegrationCurrent.html#Orientation.integrationCurrent_extDerivCLM)
- [Source of `Orientation.integrationCurrent_extDerivCLM` in TauCeti/Analysis/Distribution/TestFunction/IntegrationCurrent.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Distribution/TestFunction/IntegrationCurrent.lean#L145)
- [Tau Ceti roadmap status: Integral currents, geometric homology and minimizing hypersurfaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GeometricCurrents/STATUS.md)
