---
declaration: abbrev
origin: cited
lean: TauCeti.D1p0
statement: formalized
---

# The homogeneous Sobolev space `D^{1,p}_0(Ω)`

**The homogeneous Sobolev space `D^{1,p}_0(Ω)`**, the closure in `Lᵖ(Ω, E)` of the gradients
of the test functions `C_c^∞(Ω)`, which is their completion for the gradient norm `‖∇φ‖_p` when
`mu` has full support and `E` has positive dimension. An element is its gradient field in
`Lᵖ(Ω, E)`. For a Haar measure `mu` and a Sobolev conjugate `p⋆ ≠ ∞`, the function it represents
is its image under `TauCeti.D1p0.sobolevEmbeddingL`.

```lean
TauCeti.D1p0.{u_1} {E : Type u_1} [MeasurableSpace E] [NormedAddCommGroup E] [InnerProductSpace ℝ E]
  [FiniteDimensional ℝ E] [BorelSpace E] (mu : MeasureTheory.Measure E)
  [MeasureTheory.IsFiniteMeasureOnCompacts mu] (Omega : TopologicalSpace.Opens E) (p : ENNReal)
  [Fact (1 ≤ p)] : Submodule ℝ ↥(MeasureTheory.Lp E p (mu.restrict ↑Omega))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.D1p0`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/D1p0/Basic.html#TauCeti.D1p0).

## Sources

- [Tau Ceti documentation: `TauCeti.D1p0`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/D1p0/Basic.html#TauCeti.D1p0)
- [Source of `TauCeti.D1p0` in TauCeti/Analysis/Sobolev/D1p0/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Sobolev/D1p0/Basic.lean#L112)
- [Tau Ceti roadmap status: The Yamabe problem and conformal scalar curvature](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Yamabe/STATUS.md)
