---
declaration: def
origin: cited
lean: MeasureTheory.Lp.prodMulL
statement: formalized
---

# The tensor as a bounded bilinear map

`prodMulL F G = prodMul F G`, packaged so that
either operand can be fixed: `prodMulL F` fixes the left factor, `prodMulL.flip G` the right.
Its operator norm is at most `1`; neither measure needs to be s-finite.

```lean
MeasureTheory.Lp.prodMulL.{u_1, u_2, u_3} {𝕜 : Type u_1} {α : Type u_2} {β : Type u_3}
  {mα : MeasurableSpace α} {mβ : MeasurableSpace β} {μ : MeasureTheory.Measure α}
  {ν : MeasureTheory.Measure β} [NontriviallyNormedField 𝕜] :
  ↥(MeasureTheory.Lp 𝕜 2 μ) →L[𝕜] ↥(MeasureTheory.Lp 𝕜 2 ν) →L[𝕜] ↥(MeasureTheory.Lp 𝕜 2 (μ.prod ν))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Lp.prodMulL`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Lp/Product.html#MeasureTheory.Lp.prodMulL).

## Sources

- [Tau Ceti documentation: `MeasureTheory.Lp.prodMulL`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Lp/Product.html#MeasureTheory.Lp.prodMulL)
- [Source of `MeasureTheory.Lp.prodMulL` in TauCeti/MeasureTheory/Function/Lp/Product.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/MeasureTheory/Function/Lp/Product.lean#L180)
- [Tau Ceti roadmap status: Weighted orthogonal L² bases — completeness, Hilbert-basis structure, and product bases of orthogonal systems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/OrthogonalL2Bases/STATUS.md)
