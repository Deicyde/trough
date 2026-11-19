---
declaration: theorem
origin: cited
lean: TauCeti.harmonicForms.toDeRhamCohomology_injective
statement: formalized
proof: formalized
---

# Harmonic representatives are unique

on a compact oriented boundaryless Riemannian
manifold, a harmonic form whose de Rham class vanishes is zero, so the de Rham class map on
harmonic forms is injective.

```lean
TauCeti.harmonicForms.toDeRhamCohomology_injective.{u_1, u_2, u_3} {E : Type u_1} {H : Type u_2}
  {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [FiniteDimensional ℝ E]
  [IsManifold I (↑⊤) M] [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I (↑⊤) E fun x => TangentSpace I x] {m k l : ℕ}
  [BoundarylessManifold I M] [T2Space M] [CompactSpace M]
  (o : TauCeti.Manifold.Orientation I M (Fin m)) (hkl : k + l = m) :
  Function.Injective ⇑(TauCeti.harmonicForms.toDeRhamCohomology o hkl)
```

## Depends on

- [TauCeti.harmonicForms](tauceti-harmonicforms.md)

## Proof depends on

- [Green's formula for `d*d`](greens-formula-for-d-d.md)
- [TauCeti.SmoothForm.hodgeLaplacian](tauceti-smoothform-hodgelaplacian.md)
- [TauCeti.SmoothForm.hodgeStar](tauceti-smoothform-hodgestar.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.harmonicForms.toDeRhamCohomology_injective`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/Harmonic.html#TauCeti.harmonicForms.toDeRhamCohomology_injective).

## Sources

- [Tau Ceti documentation: `TauCeti.harmonicForms.toDeRhamCohomology_injective`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/Harmonic.html#TauCeti.harmonicForms.toDeRhamCohomology_injective)
- [Source of `TauCeti.harmonicForms.toDeRhamCohomology_injective` in TauCeti/Geometry/Manifold/DeRham/Harmonic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/DeRham/Harmonic.lean#L371)
- [Tau Ceti roadmap status: Complex manifolds, Dolbeault theory and Kähler geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ComplexKahlerGeometry/STATUS.md)
