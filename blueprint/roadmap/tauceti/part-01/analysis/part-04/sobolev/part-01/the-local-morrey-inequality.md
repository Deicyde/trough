---
declaration: theorem
origin: cited
lean: TauCeti.W1p.exists_dist_preciseRepresentative_le, TauCeti.MemWkpLoc.exists_dist_halfPlanePreciseRepresentative_le, TauCeti.MemWkpLoc.exists_dist_iteratedFDeriv_le, TauCeti.MemWkpLoc.exists_dist_preciseRepresentative_le
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

- [TauCeti.MemWkpLoc](../../../part-01/elliptic-analysis-of-pseudoholomorphic-curves/tauceti-memwkploc.md)

## Proof depends on

- [The pointwise Morrey estimate](../part-02/the-pointwise-morrey-estimate.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.W1p.exists_dist_preciseRepresentative_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/W1p/InteriorMorrey.html#TauCeti.W1p.exists_dist_preciseRepresentative_le).

## Other forms

**The local Morrey inequality across the real axis.** Formalized in Tau Ceti as [`TauCeti.MemWkpLoc.exists_dist_halfPlanePreciseRepresentative_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Local/Morrey/HalfDisc.html#TauCeti.MemWkpLoc.exists_dist_halfPlanePreciseRepresentative_le).

```lean
TauCeti.MemWkpLoc.exists_dist_halfPlanePreciseRepresentative_le.{u_1} {F : Type u_1}
  [NormedAddCommGroup F] [NormedSpace ℝ F] {p : ENNReal} [FiniteDimensional ℝ F] (hp : 2 < p) :
  ∃ C,
    0 < C ∧
      ∀ {Ω : TopologicalSpace.Opens ℂ},
        (∀ z ∈ Ω, (starRingEnd ℂ) z ∈ Ω) →
          ∀ {u : ℂ → F} {D : ℂ → ℂ →L[ℝ] F},
            TauCeti.MemWkpLoc p (↑Ω ∩ {z | 0 ≤ z.im}) 1 u →
              TauCeti.HasWeakFDerivOn MeasureTheory.volume
                  (TopologicalSpace.Opens.interior (↑Ω ∩ {z | 0 ≤ z.im})) u D →
                ∀ {x y : ℂ},
                  Metric.closedBall x (2 * dist x y) ⊆ ↑Ω →
                    dist (TauCeti.halfPlanePreciseRepresentative u x)
                        (TauCeti.halfPlanePreciseRepresentative u y) ≤
                      C *
                          (MeasureTheory.eLpNorm D p
                              (MeasureTheory.volume.restrict
                                ((Metric.ball x (2 * dist x y) ∪
                                    Metric.ball ((starRingEnd ℂ) x) (2 * dist x y)) ∩
                                  {z | 0 ≤ z.im}))).toReal *
                        dist x y ^ ↑(1 - 2 / p).toNNReal
```

**The local Morrey inequality at higher order.** Formalized in Tau Ceti as [`TauCeti.MemWkpLoc.exists_dist_iteratedFDeriv_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Local/Morrey/Higher.html#TauCeti.MemWkpLoc.exists_dist_iteratedFDeriv_le).

```lean
TauCeti.MemWkpLoc.exists_dist_iteratedFDeriv_le.{u_1} {F : Type u_1} [NormedAddCommGroup F]
  [NormedSpace ℝ F] {p : ENNReal} [FiniteDimensional ℝ F] (hp : 2 < p) (k : ℕ) :
  ∃ C,
    0 < C ∧
      ∀ {Ω : TopologicalSpace.Opens ℂ} {u g : ℂ → F} {E : ℂ → ℂ →L[ℝ] ℂ [×k]→L[ℝ] F},
        TauCeti.MemWkpLoc p (↑Ω) (k + 1) u →
          ContDiffOn ℝ (↑k) g ↑Ω →
            u =ᵐ[MeasureTheory.volume.restrict ↑Ω] g →
              TauCeti.HasWeakFDerivOn MeasureTheory.volume Ω (iteratedFDeriv ℝ k g) E →
                ∀ {x y : ℂ},
                  Metric.closedBall x (2 * dist x y) ⊆ ↑Ω →
                    dist (iteratedFDeriv ℝ k g x) (iteratedFDeriv ℝ k g y) ≤
                      C *
                          (MeasureTheory.eLpNorm E p
                              (MeasureTheory.volume.restrict
                                (Metric.ball x (2 * dist x y)))).toReal *
                        dist x y ^ ↑(1 - 2 / p).toNNReal
```

**The local Morrey inequality for `W^{1,p}_loc` maps.** Formalized in Tau Ceti as [`TauCeti.MemWkpLoc.exists_dist_preciseRepresentative_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Local/Morrey.html#TauCeti.MemWkpLoc.exists_dist_preciseRepresentative_le).

```lean
TauCeti.MemWkpLoc.exists_dist_preciseRepresentative_le.{u_1} {F : Type u_1} [NormedAddCommGroup F]
  [NormedSpace ℝ F] {p : ENNReal} [FiniteDimensional ℝ F] (hp : 2 < p) :
  ∃ C,
    0 < C ∧
      ∀ {Ω : TopologicalSpace.Opens ℂ} {u : ℂ → F} {D : ℂ → ℂ →L[ℝ] F},
        TauCeti.MemWkpLoc p (↑Ω) 1 u →
          TauCeti.HasWeakFDerivOn MeasureTheory.volume Ω u D →
            ∀ {x y : ℂ},
              Metric.closedBall x (2 * dist x y) ⊆ ↑Ω →
                dist (TauCeti.MeasureTheory.preciseRepresentative MeasureTheory.volume u x)
                    (TauCeti.MeasureTheory.preciseRepresentative MeasureTheory.volume u y) ≤
                  C *
                      (MeasureTheory.eLpNorm D p
                          (MeasureTheory.volume.restrict (Metric.ball x (2 * dist x y)))).toReal *
                    dist x y ^ ↑(1 - 2 / p).toNNReal
```

## Sources

- [Tau Ceti documentation: `TauCeti.W1p.exists_dist_preciseRepresentative_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/W1p/InteriorMorrey.html#TauCeti.W1p.exists_dist_preciseRepresentative_le)
- [Source of `TauCeti.W1p.exists_dist_preciseRepresentative_le` in TauCeti/Analysis/Sobolev/W1p/InteriorMorrey.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Sobolev/W1p/InteriorMorrey.lean#L124)
