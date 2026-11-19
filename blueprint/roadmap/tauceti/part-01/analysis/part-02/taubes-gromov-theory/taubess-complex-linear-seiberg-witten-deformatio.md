---
declaration: def
origin: cited
lean: TauCeti.SeibergWitten.complexDeformationOperator
statement: formalized
---

# Taubes's complex-linear Seiberg–Witten deformation operator

**Taubes's complex-linear Seiberg–Witten deformation operator**
`δ_ω = complexLinearPart J₁ J′ δ₀ = (δ₀ - J′ ∘ δ₀ ∘ J₁) / 2`, acting from smooth one-forms to
`Ω⁰(M) × Ω⁺(M)` on an oriented Riemannian four-manifold with a compatible almost complex structure
`J`.

```lean
TauCeti.SeibergWitten.complexDeformationOperator.{u_1, u_2, u_3} {E : Type u_1} {H : Type u_2}
  {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [FiniteDimensional ℝ E]
  [IsManifold I (↑⊤) M] [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I (↑⊤) E fun x => TangentSpace I x]
  (o : TauCeti.Manifold.Orientation I M (Fin (2 + 2)))
  (J : TauCeti.SmoothAlmostComplexStructure I M) (hJo : J.IsCompatibleOrientation o) :
  TauCeti.SmoothForm I M ℝ 1 →ₗ[ℝ]
    TauCeti.SmoothForm I M ℝ 0 × ↥(TauCeti.SmoothForm.selfDualForms o)
```

## Depends on

- [TauCeti.SmoothForm.hodgeStar](../../../geometry/part-01/complex-manifolds-dolbeault-theory-and-kahler-ge/tauceti-smoothform-hodgestar.md)

## Proof depends on

- [Jacobi's formula, by rows](../../../linear-algebra/part-01/matrix/jacobis-formula-by-rows.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SeibergWitten.complexDeformationOperator`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/SeibergWitten/ComplexDeformation.html#TauCeti.SeibergWitten.complexDeformationOperator).

## Sources

- [Tau Ceti documentation: `TauCeti.SeibergWitten.complexDeformationOperator`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/SeibergWitten/ComplexDeformation.html#TauCeti.SeibergWitten.complexDeformationOperator)
- [Source of `TauCeti.SeibergWitten.complexDeformationOperator` in TauCeti/Analysis/PDE/SeibergWitten/ComplexDeformation.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/SeibergWitten/ComplexDeformation.lean#L407)
- [Tau Ceti roadmap status: Taubes–Gromov theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TaubesGromov/STATUS.md)
