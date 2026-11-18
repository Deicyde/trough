---
declaration: def
origin: cited
lean: HilbertBasis.prod
statement: formalized
---

# The product Hilbert basis

Pointwise products of two Hilbert bases form a Hilbert basis of
`L²(μ ⊗ ν)`, indexed by the product of the index types.

```lean
HilbertBasis.prod.{u_1, u_2, u_3, u_4, u_5} {𝕜 : Type u_1} {α : Type u_2} {β : Type u_3} [RCLike 𝕜]
  {mα : MeasurableSpace α} {mβ : MeasurableSpace β} {μ : MeasureTheory.Measure α}
  {ν : MeasureTheory.Measure β} [MeasureTheory.SigmaFinite μ] [MeasureTheory.SigmaFinite ν]
  {ι₁ : Type u_4} {ι₂ : Type u_5} (b₁ : HilbertBasis ι₁ 𝕜 ↥(MeasureTheory.Lp 𝕜 2 μ))
  (b₂ : HilbertBasis ι₂ 𝕜 ↥(MeasureTheory.Lp 𝕜 2 ν)) :
  HilbertBasis (ι₁ × ι₂) 𝕜 ↥(MeasureTheory.Lp 𝕜 2 (μ.prod ν))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The tensor as a bounded bilinear map](the-tensor-as-a-bounded-bilinear-map.md)

## Lean

Formalized in Tau Ceti as [`HilbertBasis.prod`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/L2/Product.html#HilbertBasis.prod).

## Sources

- [Tau Ceti documentation: `HilbertBasis.prod`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/L2/Product.html#HilbertBasis.prod)
- [Source of `HilbertBasis.prod` in TauCeti/Analysis/InnerProductSpace/L2/Product.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/InnerProductSpace/L2/Product.lean#L247)
- [Tau Ceti roadmap status: Weighted orthogonal L² bases — completeness, Hilbert-basis structure, and product bases of orthogonal systems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/OrthogonalL2Bases/STATUS.md)
