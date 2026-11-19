---
declaration: theorem
origin: cited
lean: TauCeti.hasFPowerSeriesOnBall_tsum
statement: formalized
proof: formalized
---

# TauCeti.hasFPowerSeriesOnBall_tsum

A normally convergent family of power series on a common ball can be summed degree by
degree: the sum has the power series obtained by summing the continuous multilinear maps.
The norm bound is imposed at the radius itself, not just at each point of the open ball.

```lean
TauCeti.hasFPowerSeriesOnBall_tsum.{u_1, u_2, u_3, u_4} {𝕜 : Type u_1} [NontriviallyNormedField 𝕜]
  {E : Type u_2} [NormedAddCommGroup E] [NormedSpace 𝕜 E] {F : Type u_3} [NormedAddCommGroup F]
  [NormedSpace 𝕜 F] [CompleteSpace F] {ι : Type u_4} {g : ι → E → F}
  {p : ι → FormalMultilinearSeries 𝕜 E F} {x : E} {r : NNReal} (hr : 0 < r)
  (hg : ∀ (i : ι), HasFPowerSeriesOnBall (g i) (p i) x ↑r)
  (hsum : Summable fun ki => ‖p ki.2 ki.1‖ * ↑r ^ ki.1) :
  HasFPowerSeriesOnBall (fun z => ∑' (i : ι), g i z) (fun k => ∑' (i : ι), p i k) x ↑r
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.hasFPowerSeriesOnBall_tsum`](https://taucetiproject.org/docs/TauCeti/Analysis/Analytic/InfiniteSum.html#TauCeti.hasFPowerSeriesOnBall_tsum).

## Sources

- [Tau Ceti documentation: `TauCeti.hasFPowerSeriesOnBall_tsum`](https://taucetiproject.org/docs/TauCeti/Analysis/Analytic/InfiniteSum.html#TauCeti.hasFPowerSeriesOnBall_tsum)
- [Source of `TauCeti.hasFPowerSeriesOnBall_tsum` in TauCeti/Analysis/Analytic/InfiniteSum.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Analytic/InfiniteSum.lean#L40)
- [Tau Ceti roadmap status: Linear forms in logarithms, Baker's theorem over `ℂ` and `ℂ_p`](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/LinearFormsInLogarithms/STATUS.md)
