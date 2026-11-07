---
declaration: theorem
origin: cited
lean: TauCeti.LSeries.wienerIkehara
statement: formalized
proof: formalized
---

# The Wiener--Ikehara theorem

Let `a n ≥ 0` have Dirichlet series with sum `F s` on
`Re s > 1`, and let `G` be continuous on `Re s ≥ 1` with `G s = F s - κ / (s - 1)` on `Re s > 1`.
Then `x⁻¹ ∑_{1 ≤ n ≤ x} a n → κ` as `x → ∞`.

```lean
TauCeti.LSeries.wienerIkehara {a : ℕ → ℝ} {F G : ℂ → ℂ} {κ : ℝ} (ha : 0 ≤ a)
  (hF : ∀ (s : ℂ), 1 < s.re → LSeriesHasSum (fun n => ↑(a n)) s (F s))
  (hG : ContinuousOn G {s | 1 ≤ s.re}) (hGF : ∀ (s : ℂ), 1 < s.re → G s = F s - ↑κ / (s - 1)) :
  Filter.Tendsto (fun x => x⁻¹ * ∑ n ∈ Finset.Icc 1 ⌊x⌋₊, a n) Filter.atTop (nhds κ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.LSeries.wienerIkehara`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/WienerIkehara/SharpCutoff.html#TauCeti.LSeries.wienerIkehara).

## Sources

- [Tau Ceti documentation: `TauCeti.LSeries.wienerIkehara`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/WienerIkehara/SharpCutoff.html#TauCeti.LSeries.wienerIkehara)
- [Source of `TauCeti.LSeries.wienerIkehara` in TauCeti/NumberTheory/LSeries/WienerIkehara/SharpCutoff.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LSeries/WienerIkehara/SharpCutoff.lean#L297)
- [Tau Ceti roadmap status: Arithmetic Dirichlet series and Tauberian methods](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ArithmeticDirichletSeries/STATUS.md)
