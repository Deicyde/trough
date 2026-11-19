---
declaration: def
origin: cited
lean: TauCeti.Yamabe.yamabeQuotient
statement: formalized
---

# TauCeti.Yamabe.yamabeQuotient

The **Yamabe quotient**
`Q_g(u) = (∫ (aₙ |grad u|² + Scal_g u²) dV_g) / (∫ |u| ^ pₙ dV_g) ^ (2 / pₙ)` of a function `u`
on a Riemannian manifold of dimension `n`, where `aₙ = 4 (n - 1) / (n - 2)` and
`pₙ = 2 n / (n - 2)`. Its classical meaning is for differentiable `u`.

```lean
TauCeti.Yamabe.yamabeQuotient.{u_1, u_2, u_3} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2} [TopologicalSpace H]
  (I : ModelWithCorners ℝ E H) {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M] [T2Space M]
  [SigmaCompactSpace M] [IsManifold I (↑⊤) M] [MeasurableSpace M] [BorelSpace M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I (↑⊤) E fun x => TangentSpace I x]
  [IsContinuousRiemannianBundle E fun x => TangentSpace I x] (u : M → ℝ) : ℝ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Koszul formula](../../../geometry/part-02/manifold/part-03/the-koszul-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Yamabe.yamabeQuotient`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Yamabe/Quotient.html#TauCeti.Yamabe.yamabeQuotient).

## Sources

- [Tau Ceti documentation: `TauCeti.Yamabe.yamabeQuotient`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Yamabe/Quotient.html#TauCeti.Yamabe.yamabeQuotient)
- [Source of `TauCeti.Yamabe.yamabeQuotient` in TauCeti/Analysis/PDE/Yamabe/Quotient.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/Yamabe/Quotient.lean#L98)
- [Tau Ceti roadmap status: The Yamabe problem and conformal scalar curvature](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Yamabe/STATUS.md)
