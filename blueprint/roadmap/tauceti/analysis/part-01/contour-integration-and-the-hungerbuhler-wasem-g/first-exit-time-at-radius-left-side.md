---
declaration: def
origin: cited
lean: TauCeti.Contour.firstExitTimeLeft
statement: formalized
---

# First exit time at radius `ε` (left side)

the `sSup` of the times `t ∈ [t₀ - δ, t₀]`
with `ε ≤ ‖γ t - s‖` — the latest outside-the-ball time before `t₀`, which is the first exit
when moving left from `t₀`. The junk value is `sSup ∅` when the defining set is empty.

```lean
TauCeti.Contour.firstExitTimeLeft.{u_1} {E : Type u_1} [Sub E] [Norm E] (γ : ℝ → E) (t₀ δ : ℝ)
  (s : E) (ε : ℝ) : ℝ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Contour.firstExitTimeLeft`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/ExitTime.html#TauCeti.Contour.firstExitTimeLeft).

## Sources

- [Tau Ceti documentation: `TauCeti.Contour.firstExitTimeLeft`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/ExitTime.html#TauCeti.Contour.firstExitTimeLeft)
- [Source of `TauCeti.Contour.firstExitTimeLeft` in TauCeti/Analysis/Contour/ExitTime.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Contour/ExitTime.lean#L97)
- [Tau Ceti roadmap status: Contour integration and the Hungerbühler–Wasem generalized residue theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ContourIntegration/STATUS.md)
