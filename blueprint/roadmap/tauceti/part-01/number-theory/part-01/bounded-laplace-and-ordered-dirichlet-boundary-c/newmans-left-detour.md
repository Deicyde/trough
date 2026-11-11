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
- [Source of `TauCeti.LSeries.newmanDetour` in TauCeti/NumberTheory/LSeries/Newman/Detour.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LSeries/Newman/Detour.lean#L66)
- [Tau Ceti roadmap status: Bounded Laplace and ordered Dirichlet boundary convergence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/TauberianBoundaryConvergence/STATUS.md)
