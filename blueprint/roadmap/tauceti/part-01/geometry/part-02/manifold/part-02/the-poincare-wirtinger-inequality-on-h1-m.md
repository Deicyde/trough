---
declaration: theorem
origin: cited
lean: TauCeti.Manifold.SobolevH1.exists_norm_toLp_sq_le, TauCeti.Manifold.exists_eLpNorm_sub_average_le_mul_eLpNorm_mgradient
statement: formalized
proof: formalized
---

# The Poincaré–Wirtinger inequality on `H¹(M)`

On a closed connected manifold with a
continuous metric there is a constant `C` such that every `w ∈ H¹(M)` satisfies
`‖w‖²_{L²} ≤ C D(w, w) + (∫ w dV)² / Vol(M)`, where `D` is the Dirichlet form.

```lean
TauCeti.Manifold.SobolevH1.exists_norm_toLp_sq_le.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [CompactSpace M] [IsManifold I 1 M] [MeasurableSpace M] [BorelSpace M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContinuousRiemannianBundle E fun x => TangentSpace I x] [I.Boundaryless]
  [PreconnectedSpace M] :
  ∃ C,
    0 ≤ C ∧
      ∀ (w : TauCeti.Manifold.SobolevH1 I M),
        ‖TauCeti.Manifold.SobolevH1.toLp w‖ ^ 2 ≤
          C * (TauCeti.Manifold.SobolevH1.dirichletForm w) w +
            ((TauCeti.riemannianVolume I M).real Set.univ)⁻¹ *
              (∫ (x : M), ↑↑(TauCeti.Manifold.SobolevH1.toLp w) x ∂TauCeti.riemannianVolume I M) ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hölder's bound on an average](../../../../measure-theory/integral/part-01/holders-bound-on-an-average.md)
- [The Poincaré–Wirtinger inequality on a ball](../../../../analysis/part-03/sobolev/part-02/the-poincare-wirtinger-inequality-on-a-ball.md)

## Informally uses

- [The `L²` Poincaré–Wirtinger inequality in integral form](../part-01/the-l2-poincare-wirtinger-inequality-in-integral.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Manifold.SobolevH1.exists_norm_toLp_sq_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Poisson.html#TauCeti.Manifold.SobolevH1.exists_norm_toLp_sq_le).

## Other forms

**The Poincaré–Wirtinger inequality on a closed Riemannian manifold.** Formalized in Tau Ceti as [`TauCeti.Manifold.exists_eLpNorm_sub_average_le_mul_eLpNorm_mgradient`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Poincare.html#TauCeti.Manifold.exists_eLpNorm_sub_average_le_mul_eLpNorm_mgradient).

```lean
TauCeti.Manifold.exists_eLpNorm_sub_average_le_mul_eLpNorm_mgradient.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I 1 M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContinuousRiemannianBundle E fun x => TangentSpace I x] [MeasurableSpace M] [BorelSpace M]
  [CompactSpace M] [PreconnectedSpace M] {p : ENNReal} (hp : 1 ≤ p) (hp' : p ≠ ⊤) :
  ∃ C,
    ∀ (u : M → ℝ),
      ContMDiff I (modelWithCornersSelf ℝ ℝ) 1 u →
        MeasureTheory.eLpNorm (fun x => u x - ⨍ (y : M), u y ∂TauCeti.riemannianVolume I M) p
            (TauCeti.riemannianVolume I M) ≤
          ↑C *
            MeasureTheory.eLpNorm (fun x => ‖TauCeti.Manifold.mgradient I u x‖) p
              (TauCeti.riemannianVolume I M)
```

## Sources

- [Tau Ceti documentation: `TauCeti.Manifold.SobolevH1.exists_norm_toLp_sq_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Poisson.html#TauCeti.Manifold.SobolevH1.exists_norm_toLp_sq_le)
- [Source of `TauCeti.Manifold.SobolevH1.exists_norm_toLp_sq_le` in TauCeti/Geometry/Manifold/Riemannian/Poisson.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Riemannian/Poisson.lean#L103)
