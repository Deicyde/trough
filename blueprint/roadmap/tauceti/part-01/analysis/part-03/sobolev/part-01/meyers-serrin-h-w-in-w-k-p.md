---
declaration: theorem
origin: cited
lean: TauCeti.Wkp.dense_contDiffOn_representatives
statement: formalized
proof: formalized
---

# Meyers–Serrin: `H = W` in `W^{k,p}(Ω)`

For `1 ≤ p < ∞`, every order `k` and an
arbitrary open set `Ω`, the elements of `W^{k,p}(Ω)` represented by functions smooth on `Ω` are
dense in `W^{k,p}(Ω)`, in the full Sobolev norm.

```lean
TauCeti.Wkp.dense_contDiffOn_representatives.{u_1} {E : Type u_1} [MeasurableSpace E]
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [BorelSpace E]
  {mu : MeasureTheory.Measure E} [mu.IsAddHaarMeasure] {Omega : TopologicalSpace.Opens E}
  {p : ENNReal} [Fact (1 ≤ p)] (hp : p ≠ ⊤) (k : ℕ) :
  Dense {u | ∃ f, ContDiffOn ℝ (↑⊤) f ↑Omega ∧ ↑↑(TauCeti.Wkp.value k u) =ᵐ[mu.restrict ↑Omega] f}
```

## Depends on

- [TauCeti.Wkp](../../../part-01/partial-differential-equations/tauceti-wkp.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Wkp.dense_contDiffOn_representatives`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Wkp/MeyersSerrin.html#TauCeti.Wkp.dense_contDiffOn_representatives).

## Sources

- [Tau Ceti documentation: `TauCeti.Wkp.dense_contDiffOn_representatives`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Wkp/MeyersSerrin.html#TauCeti.Wkp.dense_contDiffOn_representatives)
- [Source of `TauCeti.Wkp.dense_contDiffOn_representatives` in TauCeti/Analysis/Sobolev/Wkp/MeyersSerrin.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Sobolev/Wkp/MeyersSerrin.lean#L317)
