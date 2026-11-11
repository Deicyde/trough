---
declaration: theorem
origin: cited
lean: TauCeti.NodalGluing.existsUnique_iso_gluedCurveHomeomorph_eq_iff
statement: formalized
proof: formalized
---

# TauCeti.NodalGluing.existsUnique_iso_gluedCurveHomeomorph_eq_iff

A node-preserving homeomorphism is induced by a unique analytic nodal isomorphism exactly
when its normalization lift is holomorphic away from the flag points.

```lean
TauCeti.NodalGluing.existsUnique_iso_gluedCurveHomeomorph_eq_iff.{u_1, u_2, u_3, u_4, u_5, u_6}
  {ι : Type u_1} {Flag : Type u_2} {X : ι → Type u_3} [(i : ι) → TopologicalSpace (X i)]
  [(i : ι) → ChartedSpace ℂ (X i)] [∀ (i : ι), T2Space (X i)] [Finite Flag] {ι' : Type u_4}
  {Flag' : Type u_5} {X' : ι' → Type u_6} [(i : ι') → TopologicalSpace (X' i)]
  [(i : ι') → ChartedSpace ℂ (X' i)] [∀ (i : ι'), T2Space (X' i)] [Finite Flag']
  [IsManifold (modelWithCornersSelf ℂ ℂ) 1 ((i : ι) × X i)]
  [IsManifold (modelWithCornersSelf ℂ ℂ) 1 ((i : ι') × X' i)]
  {d : TauCeti.NodalGluing.FlagPairData ι Flag X}
  {d' : TauCeti.NodalGluing.FlagPairData ι' Flag' X'}
  {h : TauCeti.NodalGluing.GluedCurve d ≃ₜ TauCeti.NodalGluing.GluedCurve d'}
  {hN :
    ∀ (z : TauCeti.NodalGluing.GluedCurve d),
      h z ∈ TauCeti.NodalGluing.nodeSet d' ↔ z ∈ TauCeti.NodalGluing.nodeSet d}
  {hX :
    ∀ x ∈ TauCeti.NodalGluing.flagPointSet d,
      ∀ U ∈ nhds x, ∃ V ∈ nhds x, V ⊆ U ∧ IsConnected (V \ {x})}
  {hX' :
    ∀ x ∈ TauCeti.NodalGluing.flagPointSet d',
      ∀ U ∈ nhds x, ∃ V ∈ nhds x, V ⊆ U ∧ IsConnected (V \ {x})} :
  (∃! e, e.gluedCurveHomeomorph = h) ↔
    MDiff[(TauCeti.NodalGluing.flagPointSet d)ᶜ] ⇑(TauCeti.NodalGluing.liftHomeomorph h hN hX hX')
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Osgood's lemma](../../complex-manifolds-dolbeault-theory-and-kahler-ge/osgoods-lemma.md)
- [Riemann's removable singularity theorem on complex curves](../../../part-02/manifold/part-03/riemanns-removable-singularity-theorem-on-comple.md)
- [Rouché's theorem for a disc, classical form](../../../../analysis/part-02/complex/part-03/rouches-theorem-for-a-disc-classical-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.NodalGluing.existsUnique_iso_gluedCurveHomeomorph_eq_iff`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/NodalGluing/HolomorphicLift.html#TauCeti.NodalGluing.existsUnique_iso_gluedCurveHomeomorph_eq_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.NodalGluing.existsUnique_iso_gluedCurveHomeomorph_eq_iff`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/NodalGluing/HolomorphicLift.html#TauCeti.NodalGluing.existsUnique_iso_gluedCurveHomeomorph_eq_iff)
- [Source of `TauCeti.NodalGluing.existsUnique_iso_gluedCurveHomeomorph_eq_iff` in TauCeti/AlgebraicGeometry/Curves/NodalGluing/HolomorphicLift.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/Curves/NodalGluing/HolomorphicLift.lean#L109)
- [Tau Ceti roadmap status: Analytic families and moduli of complex curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ComplexCurveModuli/STATUS.md)
