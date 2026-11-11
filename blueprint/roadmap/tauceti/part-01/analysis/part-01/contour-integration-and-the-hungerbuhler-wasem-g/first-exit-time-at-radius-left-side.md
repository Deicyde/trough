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
- [Source of `TauCeti.Contour.firstExitTimeLeft` in TauCeti/Analysis/Contour/ExitTime.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Contour/ExitTime.lean#L99)
- [Tau Ceti roadmap status: Contour integration and the Hungerbühler–Wasem generalized residue theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/ContourIntegration/STATUS.md)
