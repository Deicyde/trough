---
declaration: theorem
origin: cited
lean: TauCeti.W1p.exists_dist_preciseRepresentative_le_top
statement: formalized
proof: formalized
---

# The endpoint local Morrey estimate

A `W^{1,∞}(Ω)` precise representative satisfies
an interior Lipschitz estimate with constant `C ‖∇u‖`, where `C > 0` depends only on the
space and Haar measure. The estimate applies whenever the closed ball of radius twice the
distance of the two points lies in `Ω`.

```lean
TauCeti.W1p.exists_dist_preciseRepresentative_le_top.{u_1} {E : Type u_1} [MeasurableSpace E]
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [BorelSpace E]
  {mu : MeasureTheory.Measure E} [mu.IsAddHaarMeasure] :
  ∃ C,
    0 < C ∧
      ∀ {Omega : TopologicalSpace.Opens E} (u : ↥(TauCeti.W1p mu Omega ⊤)) {x y : E},
        Metric.closedBall x (2 * dist x y) ⊆ ↑Omega →
          dist (TauCeti.MeasureTheory.preciseRepresentative mu (↑↑(TauCeti.W1p.value u)) x)
              (TauCeti.MeasureTheory.preciseRepresentative mu (↑↑(TauCeti.W1p.value u)) y) ≤
            C * ‖TauCeti.W1p.gradient u‖ * dist x y
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The local Morrey inequality](the-local-morrey-inequality.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.W1p.exists_dist_preciseRepresentative_le_top`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/W1p/InteriorMorrey.html#TauCeti.W1p.exists_dist_preciseRepresentative_le_top).

## Sources

- [Tau Ceti documentation: `TauCeti.W1p.exists_dist_preciseRepresentative_le_top`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/W1p/InteriorMorrey.html#TauCeti.W1p.exists_dist_preciseRepresentative_le_top)
- [Source of `TauCeti.W1p.exists_dist_preciseRepresentative_le_top` in TauCeti/Analysis/Sobolev/W1p/InteriorMorrey.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Sobolev/W1p/InteriorMorrey.lean#L241)
