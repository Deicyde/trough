---
declaration: structure
origin: cited
lean: TauCeti.CStarAction.ConvolutionAlgebra
statement: formalized
---

# TauCeti.CStarAction.ConvolutionAlgebra

The convolution ⋆-algebra of the C⋆-dynamical system `(A, G, α)` with respect to `μ`: the
compactly supported continuous functions `G → A`, with twisted convolution as product and the
twisted involution as star. Use `ConvolutionAlgebra.toConv` and `ConvolutionAlgebra.ofConv` to
pass to and from `C_c(G, A)`, whose own product and star are pointwise.

```lean
TauCeti.CStarAction.ConvolutionAlgebra.{u_1, u_2} {G : Type u_1} {A : Type u_2} [Group G]
  [TopologicalSpace G] [NonUnitalCStarAlgebra A] [MeasurableSpace G] (α : TauCeti.CStarAction G A)
  (μ : MeasureTheory.Measure G) : Type (max u_1 u_2)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.CStarAction.ConvolutionAlgebra`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Action/Convolution/Algebra.html#TauCeti.CStarAction.ConvolutionAlgebra).

## Sources

- [Tau Ceti documentation: `TauCeti.CStarAction.ConvolutionAlgebra`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Action/Convolution/Algebra.html#TauCeti.CStarAction.ConvolutionAlgebra)
- [Source of `TauCeti.CStarAction.ConvolutionAlgebra` in TauCeti/Analysis/CStarAlgebra/Action/Convolution/Algebra.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/CStarAlgebra/Action/Convolution/Algebra.lean#L107)
- [Tau Ceti roadmap status: Operator-algebra dynamics, crossed products, and equilibrium](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/OperatorAlgebraDynamics/STATUS.md)
