---
declaration: theorem
origin: cited
lean: TauCeti.harmonicForms.toDeRhamCohomology_bijective_zero, TauCeti.harmonicForms.toDeRhamCohomology_bijective_top
statement: formalized
proof: formalized
---

# The Hodge theorem in degree zero

on a compact oriented boundaryless Riemannian manifold,
every degree-zero de Rham class has exactly one harmonic representative.

```lean
TauCeti.harmonicForms.toDeRhamCohomology_bijective_zero.{u_1, u_2, u_3} {E : Type u_1}
  {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [FiniteDimensional ℝ E]
  [IsManifold I (↑⊤) M] [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I (↑⊤) E fun x => TangentSpace I x] {m l : ℕ}
  [BoundarylessManifold I M] [T2Space M] [CompactSpace M]
  (o : TauCeti.Manifold.Orientation I M (Fin m)) (hl : 0 + l = m) :
  Function.Bijective ⇑(TauCeti.harmonicForms.toDeRhamCohomology o hl)
```

## Depends on

- [TauCeti.harmonicForms](tauceti-harmonicforms.md)

## Proof depends on

- [The compactly supported Poincaré lemma on the line](../../part-02/manifold/part-01/the-compactly-supported-poincare-lemma-on-the-li.md)
- [Green's formula for `d*d`](greens-formula-for-d-d.md)
- [Harmonic representatives are unique](harmonic-representatives-are-unique.md)
- [The Poincaré lemma on manifolds](../../part-02/manifold/part-03/the-poincare-lemma-on-manifolds.md)
- [TauCeti.SmoothForm.hodgeLaplacian](tauceti-smoothform-hodgelaplacian.md)
- [TauCeti.SmoothForm.hodgeStar](tauceti-smoothform-hodgestar.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.harmonicForms.toDeRhamCohomology_bijective_zero`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/Harmonic.html#TauCeti.harmonicForms.toDeRhamCohomology_bijective_zero).

## Other forms

**The Hodge theorem in the top degree.** Formalized in Tau Ceti as [`TauCeti.harmonicForms.toDeRhamCohomology_bijective_top`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/Harmonic.html#TauCeti.harmonicForms.toDeRhamCohomology_bijective_top).

```lean
TauCeti.harmonicForms.toDeRhamCohomology_bijective_top.{u_1, u_2, u_3} {E : Type u_1} {H : Type u_2}
  {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [FiniteDimensional ℝ E]
  [IsManifold I (↑⊤) M] [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I (↑⊤) E fun x => TangentSpace I x] {m : ℕ}
  [BoundarylessManifold I M] [T2Space M] [CompactSpace M]
  (o : TauCeti.Manifold.Orientation I M (Fin m)) (hm : m + 0 = m) :
  Function.Bijective ⇑(TauCeti.harmonicForms.toDeRhamCohomology o hm)
```

## Sources

- [Tau Ceti documentation: `TauCeti.harmonicForms.toDeRhamCohomology_bijective_zero`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/Harmonic.html#TauCeti.harmonicForms.toDeRhamCohomology_bijective_zero)
- [Source of `TauCeti.harmonicForms.toDeRhamCohomology_bijective_zero` in TauCeti/Geometry/Manifold/DeRham/Harmonic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/DeRham/Harmonic.lean#L393)
