---
declaration: theorem
origin: cited
lean: TauCeti.Manifold.SobolevH1.exists_lintegral_exp_mul_sq_le, TauCeti.Manifold.exists_mem_nhds_setLIntegral_exp_mul_abs_rpow_le, TauCeti.Manifold.exists_lintegral_exp_mul_abs_rpow_le
statement: formalized
proof: formalized
---

# Trudinger's inequality on `H¹`

On a closed surface with a continuous Riemannian metric,
there are `β > 0` and `C` such that `∫ exp (β w²) dV ≤ C` on the closed unit ball of `H¹(M)`.

```lean
TauCeti.Manifold.SobolevH1.exists_lintegral_exp_mul_sq_le.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] [CompactSpace M] [IsManifold I 1 M] [MeasurableSpace M]
  [BorelSpace M] [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContinuousRiemannianBundle E fun x => TangentSpace I x] (hE : Module.finrank ℝ E = 2) :
  ∃ β > 0,
    ∃ C,
      ∀ (w : TauCeti.Manifold.SobolevH1 I M),
        ‖w‖ ≤ 1 →
          ∫⁻ (x : M),
              ENNReal.ofReal
                (Real.exp
                  (β * ↑↑(TauCeti.Manifold.SobolevH1.toLp w) x ^ 2)) ∂TauCeti.riemannianVolume I M ≤
            ↑C
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Trudinger's inequality on `W^{1,n}_0(Ω)`](../../../../analysis/part-03/sobolev/part-02/trudingers-inequality-on-w-1-n-0.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Manifold.SobolevH1.exists_lintegral_exp_mul_sq_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Sobolev/Trudinger.html#TauCeti.Manifold.SobolevH1.exists_lintegral_exp_mul_sq_le).

## Other forms

**Trudinger's inequality near a point.** Formalized in Tau Ceti as [`TauCeti.Manifold.exists_mem_nhds_setLIntegral_exp_mul_abs_rpow_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Trudinger.html#TauCeti.Manifold.exists_mem_nhds_setLIntegral_exp_mul_abs_rpow_le).

```lean
TauCeti.Manifold.exists_mem_nhds_setLIntegral_exp_mul_abs_rpow_le.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I 1 M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContinuousRiemannianBundle E fun x => TangentSpace I x] [MeasurableSpace M] [BorelSpace M]
  [LindelofSpace M] (hn : 2 ≤ Module.finrank ℝ E) (c : M) :
  ∃ V ∈ nhds c,
    ∃ β > 0,
      ∃ C,
        ∀ (u : M → ℝ),
          ContMDiff I (modelWithCornersSelf ℝ ℝ) 1 u →
            MeasureTheory.eLpNorm (fun x => ‖TauCeti.Manifold.mgradient I u x‖)
                    (↑(Module.finrank ℝ E)) (TauCeti.riemannianVolume I M) +
                  MeasureTheory.eLpNorm u (↑(Module.finrank ℝ E)) (TauCeti.riemannianVolume I M) ≤
                1 →
              ∫⁻ (x : M) in V,
                  ENNReal.ofReal
                    (Real.exp
                      (β *
                        |u x| ^
                          (↑(Module.finrank ℝ E) /
                            (↑(Module.finrank ℝ E) - 1)))) ∂TauCeti.riemannianVolume I M ≤
                ↑C
```

**Trudinger's inequality on a closed Riemannian manifold.** Formalized in Tau Ceti as [`TauCeti.Manifold.exists_lintegral_exp_mul_abs_rpow_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Trudinger.html#TauCeti.Manifold.exists_lintegral_exp_mul_abs_rpow_le).

```lean
TauCeti.Manifold.exists_lintegral_exp_mul_abs_rpow_le.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I 1 M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContinuousRiemannianBundle E fun x => TangentSpace I x] [MeasurableSpace M] [BorelSpace M]
  [CompactSpace M] (hn : 2 ≤ Module.finrank ℝ E) :
  ∃ β > 0,
    ∃ C,
      ∀ (u : M → ℝ),
        ContMDiff I (modelWithCornersSelf ℝ ℝ) 1 u →
          MeasureTheory.eLpNorm (fun x => ‖TauCeti.Manifold.mgradient I u x‖)
                  (↑(Module.finrank ℝ E)) (TauCeti.riemannianVolume I M) +
                MeasureTheory.eLpNorm u (↑(Module.finrank ℝ E)) (TauCeti.riemannianVolume I M) ≤
              1 →
            ∫⁻ (x : M),
                ENNReal.ofReal
                  (Real.exp
                    (β *
                      |u x| ^
                        (↑(Module.finrank ℝ E) /
                          (↑(Module.finrank ℝ E) - 1)))) ∂TauCeti.riemannianVolume I M ≤
              ↑C
```

## Sources

- [Tau Ceti documentation: `TauCeti.Manifold.SobolevH1.exists_lintegral_exp_mul_sq_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Sobolev/Trudinger.html#TauCeti.Manifold.SobolevH1.exists_lintegral_exp_mul_sq_le)
- [Source of `TauCeti.Manifold.SobolevH1.exists_lintegral_exp_mul_sq_le` in TauCeti/Geometry/Manifold/Riemannian/Sobolev/Trudinger.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Riemannian/Sobolev/Trudinger.lean#L106)
