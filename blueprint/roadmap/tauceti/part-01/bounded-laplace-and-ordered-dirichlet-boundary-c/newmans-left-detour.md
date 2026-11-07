---
declaration: def
origin: cited
lean: TauCeti.LSeries.newmanDetour
statement: formalized
---

# Newman's left detour

The parabolic arc `s ↦ -δ (1 - s²) - R s I`, which on `[-1, 1]`
runs from `R * I` to `-R * I`; for `R, δ ≥ 0` it stays in the strip `-δ ≤ re z ≤ 0`,
`|im z| ≤ R`.

```lean
TauCeti.LSeries.newmanDetour (R δ s : ℝ) : ℂ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.LSeries.newmanDetour`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/Newman/Detour.html#TauCeti.LSeries.newmanDetour).

## Sources

- [Tau Ceti documentation: `TauCeti.LSeries.newmanDetour`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/Newman/Detour.html#TauCeti.LSeries.newmanDetour)
- [Source of `TauCeti.LSeries.newmanDetour` in TauCeti/NumberTheory/LSeries/Newman/Detour.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LSeries/Newman/Detour.lean#L66)
- [Tau Ceti roadmap status: Bounded Laplace and ordered Dirichlet boundary convergence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/TauberianBoundaryConvergence/STATUS.md)
