---
declaration: theorem
origin: cited
lean: TauCeti.IsJordanCurve.exists_homeomorph_closedBall_filledHull, TauCeti.IsJordanCurve.exists_homeomorph_compl_ball_compl_filledHull_sdiff, TauCeti.exists_continuousOn_bijOn_upperHalfPlaneSet_of_isJordanCurve_insert_infty
statement: formalized
proof: formalized
---

# Carathéodory's theorem for the inside of a Jordan curve

For a Jordan curve `C ⊆ ℂ` and a
point `p` of its inside `filledHull C \ C`, there is a map `g`, holomorphic on the open unit disc
with `g 0 = p`, carrying the disc bijectively onto the inside and the unit circle bijectively onto
`C`, which restricts to a homeomorphism of the closed disc onto `filledHull C`.

```lean
TauCeti.IsJordanCurve.exists_homeomorph_closedBall_filledHull {C : Set ℂ} {p : ℂ}
  (hC : TauCeti.IsJordanCurve C) (hp : p ∈ TauCeti.filledHull C \ C) :
  ∃ g,
    ContinuousOn g (Metric.closedBall 0 1) ∧
      DifferentiableOn ℂ g (Metric.ball 0 1) ∧
        Set.BijOn g (Metric.ball 0 1) (TauCeti.filledHull C \ C) ∧
          Set.BijOn g (Metric.sphere 0 1) C ∧
            g 0 = p ∧ ∃ e, ∀ (z : ↑(Metric.closedBall 0 1)), ↑(e z) = g ↑z
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Carathéodory's continuity theorem, as a characterization](../../../part-01/conformal-mapping-and-the-geometric-theory-of-ho/part-01/caratheodorys-continuity-theorem-as-a-characteri.md)
- [Cauchy estimate](cauchy-estimate.md)
- [The converse of Cauchy's theorem](../../../../number-theory/part-01/bounded-laplace-and-ordered-dirichlet-boundary-c/the-converse-of-cauchys-theorem.md)
- [The frontier of a complementary component of a Jordan curve is the whole curve](../../../part-01/conformal-mapping-and-the-geometric-theory-of-ho/part-01/the-frontier-of-a-complementary-component-of-a-j.md)
- [Generalized winding number (HW Def 2.1)](../../../part-01/contour-integration-and-the-hungerbuhler-wasem-g/generalized-winding-number-hw-def-2-1.md)
- [The homology Cauchy theorem (roadmap `homologyCauchyTheorem`, Layer 3)](../../../part-01/contour-integration-and-the-hungerbuhler-wasem-g/the-homology-cauchy-theorem-roadmap-homologycauc.md)
- [Hurwitz's theorem](../../../part-01/conformal-mapping-and-the-geometric-theory-of-ho/part-01/hurwitzs-theorem.md)
- [Janiszewski's theorem](../../../part-01/conformal-mapping-and-the-geometric-theory-of-ho/part-01/janiszewskis-theorem.md)
- [The Jordan curve theorem](../../../part-01/conformal-mapping-and-the-geometric-theory-of-ho/part-02/the-jordan-curve-theorem.md)
- [The Jordan separation theorem](../../../part-01/conformal-mapping-and-the-geometric-theory-of-ho/part-01/the-jordan-separation-theorem.md)
- [Montel's selection theorem](../part-02/montels-selection-theorem.md)
- [The Riemann mapping theorem](../../../part-01/conformal-mapping-and-the-geometric-theory-of-ho/part-01/the-riemann-mapping-theorem.md)
- [Rouché's theorem for a disc, classical form](../../../part-01/conformal-mapping-and-the-geometric-theory-of-ho/part-02/rouches-theorem-for-a-disc-classical-form.md)
- [Strict Schwarz lemma](../../../part-01/conformal-mapping-and-the-geometric-theory-of-ho/part-02/strict-schwarz-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsJordanCurve.exists_homeomorph_closedBall_filledHull`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Jordan/Complement.html#TauCeti.IsJordanCurve.exists_homeomorph_closedBall_filledHull).

## Other forms

**Carathéodory's theorem for the outside of a Jordan curve.** Formalized in Tau Ceti as [`TauCeti.IsJordanCurve.exists_homeomorph_compl_ball_compl_filledHull_sdiff`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Jordan/Complement.html#TauCeti.IsJordanCurve.exists_homeomorph_compl_ball_compl_filledHull_sdiff).

```lean
TauCeti.IsJordanCurve.exists_homeomorph_compl_ball_compl_filledHull_sdiff {C : Set ℂ}
  (hC : TauCeti.IsJordanCurve C) :
  ∃ h,
    ContinuousOn h (Metric.ball 0 1)ᶜ ∧
      DifferentiableOn ℂ h (Metric.closedBall 0 1)ᶜ ∧
        Set.BijOn h (Metric.closedBall 0 1)ᶜ (TauCeti.filledHull C)ᶜ ∧
          Set.BijOn h (Metric.sphere 0 1) C ∧
            Filter.Tendsto h (Bornology.cobounded ℂ) (Bornology.cobounded ℂ) ∧
              ∃ e, ∀ (z : ↑(Metric.ball 0 1)ᶜ), ↑(e z) = h ↑z
```

**Carathéodory's theorem on the closed upper half-plane for an unbounded Jordan domain.** Formalized in Tau Ceti as [`TauCeti.exists_continuousOn_bijOn_upperHalfPlaneSet_of_isJordanCurve_insert_infty`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Jordan/Unbounded.html#TauCeti.exists_continuousOn_bijOn_upperHalfPlaneSet_of_isJordanCurve_insert_infty).

```lean
TauCeti.exists_continuousOn_bijOn_upperHalfPlaneSet_of_isJordanCurve_insert_infty {U : Set ℂ}
  (hUo : IsOpen U) (hUc : IsConnected U)
  (hUJ : TauCeti.IsJordanCurve (insert OnePoint.infty (OnePoint.some '' frontier U))) :
  ∃ f,
    ContinuousOn f {z | 0 ≤ z.im} ∧
      DifferentiableOn ℂ f UpperHalfPlane.upperHalfPlaneSet ∧
        Set.BijOn f UpperHalfPlane.upperHalfPlaneSet U ∧
          Set.BijOn f {z | 0 ≤ z.im} (closure U) ∧
            Set.BijOn f {z | z.im = 0} (frontier U) ∧
              Filter.Tendsto f (Bornology.cobounded ℂ ⊓ Filter.principal {z | 0 ≤ z.im})
                (Bornology.cobounded ℂ)
```

## Sources

- [Tau Ceti documentation: `TauCeti.IsJordanCurve.exists_homeomorph_closedBall_filledHull`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Jordan/Complement.html#TauCeti.IsJordanCurve.exists_homeomorph_closedBall_filledHull)
- [Source of `TauCeti.IsJordanCurve.exists_homeomorph_closedBall_filledHull` in TauCeti/Analysis/Complex/Conformal/Jordan/Complement.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/Conformal/Jordan/Complement.lean#L63)
