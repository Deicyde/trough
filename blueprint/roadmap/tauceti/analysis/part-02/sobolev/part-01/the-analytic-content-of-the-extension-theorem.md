---
declaration: theorem
origin: cited
lean: TauCeti.W1p0.hasWeakFDerivOn_indicator
statement: formalized
proof: formalized
---

# The analytic content of the extension theorem

The zero-extension of `u ∈ W^{1,p}_0(Ω)`
is weakly differentiable on the larger open set `Ω'`, with weak gradient the zero-extension of the
weak gradient of `u`.  This is the statement that can *fail* for a general `u ∈ W^{1,p}(Ω)`: with
no condition forcing `u` to vanish towards `∂Ω`, its zero-extension need not be weakly
differentiable on `Ω'` at all.

```lean
TauCeti.W1p0.hasWeakFDerivOn_indicator.{u_1} {E : Type u_1} [MeasurableSpace E]
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [BorelSpace E]
  {mu : MeasureTheory.Measure E} [mu.IsAddHaarMeasure] {Omega Omega' : TopologicalSpace.Opens E}
  {p : ENNReal} [Fact (1 ≤ p)] (hsub : Omega ≤ Omega') (u : ↥(TauCeti.W1p0 mu Omega p)) :
  TauCeti.HasWeakFDerivOn mu Omega' ((↑Omega).indicator ↑↑(TauCeti.W1p.value ↑u)) fun x =>
    (innerSL ℝ) ((↑Omega).indicator (↑↑(TauCeti.W1p.gradient ↑u)) x)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.W1p0.hasWeakFDerivOn_indicator`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/W1p/Extension.html#TauCeti.W1p0.hasWeakFDerivOn_indicator).

## Sources

- [Tau Ceti documentation: `TauCeti.W1p0.hasWeakFDerivOn_indicator`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/W1p/Extension.html#TauCeti.W1p0.hasWeakFDerivOn_indicator)
- [Source of `TauCeti.W1p0.hasWeakFDerivOn_indicator` in TauCeti/Analysis/Sobolev/W1p/Extension.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Sobolev/W1p/Extension.lean#L323)
