---
declaration: def
origin: cited
lean: TauCeti.W1p.frontierTrace
statement: formalized
---

# The trace operator of a bounded Lipschitz domain

**The trace operator of a bounded Lipschitz domain**, `W^{1,p}(Ω) → Lᵖ(frontier Ω)` for
`p < ∞` and normalized `dim E`-dimensional Euclidean Hausdorff measure on the frontier. It is
characterized by `TauCeti.W1p.frontierTrace_ae_eq_of_continuousOn` and
`TauCeti.W1p.eq_frontierTrace`: it is the unique bounded linear operator sending every function
continuous up to the boundary to its restriction to the frontier.

```lean
TauCeti.W1p.frontierTrace.{u_1} {E : Type u_1} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
  [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E]
  {Ω : TopologicalSpace.Opens (WithLp 2 (ℝ × E))} {L : NNReal} {p : ENNReal} [Fact (1 ≤ p)]
  (hp : p ≠ ⊤) (hΩ : (↑Ω).IsLipschitzDomainWith L) (hb : Bornology.IsBounded ↑Ω) :
  ↥(TauCeti.W1p MeasureTheory.volume Ω p) →L[ℝ]
    ↥(MeasureTheory.Lp ℝ p
        ((MeasureTheory.Measure.euclideanHausdorffMeasure (Module.finrank ℝ E)).restrict
          (frontier ↑Ω)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Rademacher's theorem for locally Lipschitz functions](../../part-02/calculus/part-01/rademachers-theorem-for-locally-lipschitz-functi.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.W1p.frontierTrace`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/LipschitzDomain/Trace/Frontier.html#TauCeti.W1p.frontierTrace).

## Sources

- [Tau Ceti documentation: `TauCeti.W1p.frontierTrace`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/LipschitzDomain/Trace/Frontier.html#TauCeti.W1p.frontierTrace)
- [Source of `TauCeti.W1p.frontierTrace` in TauCeti/Analysis/Sobolev/LipschitzDomain/Trace/Frontier.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Sobolev/LipschitzDomain/Trace/Frontier.lean#L214)
- [Tau Ceti roadmap status: Partial differential equations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/PDE/STATUS.md)
