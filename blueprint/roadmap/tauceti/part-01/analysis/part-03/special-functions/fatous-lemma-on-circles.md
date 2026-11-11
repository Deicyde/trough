---
declaration: theorem
origin: cited
lean: TauCeti.volume_setOf_tendsto_circleMap_nhdsNE_zero
statement: formalized
proof: formalized
---

# Fatou's lemma on circles

If `log⁺ ‖f‖⁻¹` is integrable on the circles about `c` of
radii `ρ n`, and its circle averages there are at most `B`, then the angles in one period along
which `f (circleMap c (ρ n) θ)` tends to `0` through nonzero values form a null set.

```lean
TauCeti.volume_setOf_tendsto_circleMap_nhdsNE_zero {f : ℂ → ℂ} {c : ℂ} {ρ : ℕ → ℝ} {B : ℝ}
  (hf : ∀ (n : ℕ), CircleIntegrable (fun z => ‖f z‖⁻¹.posLog) c (ρ n))
  (hB : ∀ (n : ℕ), Real.circleAverage (fun z => ‖f z‖⁻¹.posLog) c (ρ n) ≤ B) :
  MeasureTheory.volume
      {θ |
        θ ∈ Set.Ioc 0 (2 * Real.pi) ∧
          Filter.Tendsto (fun n => f (circleMap c (ρ n) θ)) Filter.atTop (nhdsWithin 0 {0}ᶜ)} =
    0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.volume_setOf_tendsto_circleMap_nhdsNE_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Integrability/PosLog.html#TauCeti.volume_setOf_tendsto_circleMap_nhdsNE_zero).

## Sources

- [Tau Ceti documentation: `TauCeti.volume_setOf_tendsto_circleMap_nhdsNE_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Integrability/PosLog.html#TauCeti.volume_setOf_tendsto_circleMap_nhdsNE_zero)
- [Source of `TauCeti.volume_setOf_tendsto_circleMap_nhdsNE_zero` in TauCeti/Analysis/SpecialFunctions/Integrability/PosLog.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/SpecialFunctions/Integrability/PosLog.lean#L124)
