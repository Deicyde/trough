---
declaration: def
origin: cited
lean: TauCeti.SeibergWitten.abelianDeformationOperator
statement: formalized
---

# TauCeti.SeibergWitten.abelianDeformationOperator

The **abelian deformation operator** `T a = (-2 d*a, (da)⁺)` of the Seiberg–Witten equations on
an oriented Riemannian four-manifold, from smooth one-forms to smooth functions and smooth
self-dual two-forms, an imaginary form `i a` being indexed by the real form `a`. Its first
component is the formal adjoint `-2 d*` of the infinitesimal gauge action, a rescaling of the
derivative of the Coulomb gauge condition; its second is the derivative of the curvature equation
in the connection direction.

```lean
TauCeti.SeibergWitten.abelianDeformationOperator.{u_1, u_2, u_3} {E : Type u_1} {H : Type u_2}
  {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [FiniteDimensional ℝ E]
  [IsManifold I (↑⊤) M] [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I (↑⊤) E fun x => TangentSpace I x]
  (o : TauCeti.Manifold.Orientation I M (Fin (2 + 2))) :
  TauCeti.SmoothForm I M ℝ 1 →ₗ[ℝ]
    TauCeti.SmoothForm I M ℝ 0 × ↥(TauCeti.SmoothForm.selfDualForms o)
```

## Depends on

- [TauCeti.SmoothForm.hodgeStar](../../../geometry/part-01/complex-manifolds-dolbeault-theory-and-kahler-ge/tauceti-smoothform-hodgestar.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SeibergWitten.abelianDeformationOperator`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/SeibergWitten/AbelianDeformation.html#TauCeti.SeibergWitten.abelianDeformationOperator).

## Sources

- [Tau Ceti documentation: `TauCeti.SeibergWitten.abelianDeformationOperator`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/SeibergWitten/AbelianDeformation.html#TauCeti.SeibergWitten.abelianDeformationOperator)
- [Source of `TauCeti.SeibergWitten.abelianDeformationOperator` in TauCeti/Analysis/PDE/SeibergWitten/AbelianDeformation.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/SeibergWitten/AbelianDeformation.lean#L96)
- [Tau Ceti roadmap status: Four-dimensional Seiberg–Witten theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SeibergWittenTheory/STATUS.md)
