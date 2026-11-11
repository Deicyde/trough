---
declaration: def
origin: cited
lean: Orientation.integrationCurrent
statement: formalized
---

# Orientation.integrationCurrent

The **oriented integration current** `[[Ω]]` of an open set `Ω` of an oriented real vector
space `E` of dimension `m`: the continuous linear functional `ω ↦ ∫_Ω ω` on test `m`-forms on `Ω`.
For any basis `b` of orientation `o` it is `ω ↦ ∫ x, ω x b ∂b.addHaar`
(`Orientation.integrationCurrent_apply`). If `m` is not the dimension of `E`, it is zero.

```lean
Orientation.integrationCurrent.{u_1} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E] {m : ℕ} {n : ℕ∞}
  (o : Orientation ℝ E (Fin m)) (Ω : TopologicalSpace.Opens E) :
  TestFunction Ω (E [⋀^Fin m]→L[ℝ] ℝ) n →L[ℝ] ℝ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Orientation.integrationCurrent`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/TestFunction/IntegrationCurrent.html#Orientation.integrationCurrent).

## Sources

- [Tau Ceti documentation: `Orientation.integrationCurrent`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/TestFunction/IntegrationCurrent.html#Orientation.integrationCurrent)
- [Source of `Orientation.integrationCurrent` in TauCeti/Analysis/Distribution/TestFunction/IntegrationCurrent.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Distribution/TestFunction/IntegrationCurrent.lean#L82)
- [Tau Ceti roadmap status: Integral currents, geometric homology and minimizing hypersurfaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GeometricCurrents/STATUS.md)
