---
declaration: theorem
origin: cited
lean: TauCeti.W1p.exists_dist_preciseRepresentative_le
statement: formalized
proof: formalized
---

# The local Morrey inequality

Let `n < p ≤ ∞`, where `n` is the dimension, and let
`α = 1 - n / p`. There is a constant `C > 0`, depending only on `n`, `p` and the Haar measure `μ`,
such that the following holds. Let `u ∈ W^{1,p}(Ω)` and let `x, y` be points with
`closedBall x (2 |x - y|) ⊆ Ω`. Then the precise representative `u*` of `u` satisfies

`|u*(x) - u*(y)| ≤ C ‖∇u‖_{Lᵖ(B(x, 2 |x - y|))} |x - y|^α`.

```lean
TauCeti.W1p.exists_dist_preciseRepresentative_le.{u_1} {E : Type u_1} [MeasurableSpace E]
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [BorelSpace E]
  {mu : MeasureTheory.Measure E} [mu.IsAddHaarMeasure] {p : ENNReal} [Fact (1 ≤ p)]
  (hp : ↑(Module.finrank ℝ E) < p) :
  ∃ C,
    0 < C ∧
      ∀ {Omega : TopologicalSpace.Opens E} (u : ↥(TauCeti.W1p mu Omega p)) {x y : E},
        Metric.closedBall x (2 * dist x y) ⊆ ↑Omega →
          dist (TauCeti.MeasureTheory.preciseRepresentative mu (↑↑(TauCeti.W1p.value u)) x)
              (TauCeti.MeasureTheory.preciseRepresentative mu (↑↑(TauCeti.W1p.value u)) y) ≤
            C *
                (MeasureTheory.eLpNorm (↑↑(TauCeti.W1p.gradient u)) p
                    (mu.restrict (Metric.ball x (2 * dist x y)))).toReal *
              dist x y ^ ↑(1 - ↑(Module.finrank ℝ E) / p).toNNReal
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The pointwise Morrey estimate](../part-02/the-pointwise-morrey-estimate.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.W1p.exists_dist_preciseRepresentative_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/W1p/InteriorMorrey.html#TauCeti.W1p.exists_dist_preciseRepresentative_le).

## Sources

- [Tau Ceti documentation: `TauCeti.W1p.exists_dist_preciseRepresentative_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/W1p/InteriorMorrey.html#TauCeti.W1p.exists_dist_preciseRepresentative_le)
- [Source of `TauCeti.W1p.exists_dist_preciseRepresentative_le` in TauCeti/Analysis/Sobolev/W1p/InteriorMorrey.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Sobolev/W1p/InteriorMorrey.lean#L124)
