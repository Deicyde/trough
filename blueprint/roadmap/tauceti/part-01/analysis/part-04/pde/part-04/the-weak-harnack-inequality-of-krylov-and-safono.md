---
declaration: theorem
origin: cited
lean: TauCeti.PDE.exists_eLpNorm_le_mul_rpow_mul_add_eLpNorm_posPart, TauCeti.PDE.exists_eLpNorm_le_mul_rpow_mul_add_eLpNorm_posPart_of_wkp
statement: formalized
proof: formalized
---

# The weak Harnack inequality of Krylov and Safonov

**The weak Harnack inequality of Krylov and Safonov** (Gilbarg–Trudinger, Theorem 9.22;
Caffarelli–Cabré, Theorem 4.8). Let `κ > 0`. There are `p > 0` and `C > 0`, depending only on the
dimension `n ≥ 1` and on `κ`, with the following property. Let `a` be uniformly elliptic on
`B(c, R)` with constants `λ ≤ Λ ≤ κ λ`, and let `u` be continuous on `closedBall c R`, nonnegative
there and `C²` in `B(c, R)` with `∑ᵢⱼ aⁱʲ ∂ᵢ∂ⱼu ≤ f` there. Then for every `y ∈ B(c, R / 4)`,

`‖u‖_{Lᵖ(B(c, R / (16 √n)))} ≤ C R^(n / p) (u(y) + R ‖f⁺‖_{Lⁿ(B(c, R))} / λ)`.

The coefficients need be neither measurable nor symmetric.

```lean
TauCeti.PDE.exists_eLpNorm_le_mul_rpow_mul_add_eLpNorm_posPart.{u_1} {ι : Type u_1} [Fintype ι]
  [DecidableEq ι] {κ : ℝ} (hκ : 0 < κ) :
  ∃ p C,
    0 < p ∧
      0 < C ∧
        ∀ ⦃lam Lam R : ℝ⦄ ⦃c : EuclideanSpace ℝ ι⦄ ⦃a : EuclideanSpace ℝ ι → Matrix ι ι ℝ⦄
          ⦃u f : EuclideanSpace ℝ ι → ℝ⦄,
          TauCeti.PDE.UniformlyEllipticOn (Metric.ball c R) a lam Lam →
            Lam ≤ κ * lam →
              ContinuousOn u (Metric.closedBall c R) →
                ContDiffOn ℝ 2 u (Metric.ball c R) →
                  (∀ x ∈ Metric.closedBall c R, 0 ≤ u x) →
                    (∀ x ∈ Metric.ball c R,
                        ∑ i,
                            ∑ j,
                              a x i j *
                                ((fderiv ℝ (fderiv ℝ u) x) (EuclideanSpace.single i 1))
                                  (EuclideanSpace.single j 1) ≤
                          f x) →
                      ∀ y ∈ Metric.ball c (R / 4),
                        MeasureTheory.eLpNorm u (ENNReal.ofReal p)
                            (MeasureTheory.volume.restrict
                              (Metric.ball c (R / (16 * √↑(Fintype.card ι))))) ≤
                          ENNReal.ofReal (C * R ^ (↑(Fintype.card ι) / p)) *
                            (ENNReal.ofReal (u y) +
                              ENNReal.ofReal (R / lam) *
                                MeasureTheory.eLpNorm (fun x => (f x)⁺) (↑(Fintype.card ι))
                                  (MeasureTheory.volume.restrict (Metric.ball c R)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Aleksandrov–Bakelman–Pucci estimate for strong subsolutions](../../../part-02/partial-differential-equations/the-aleksandrov-bakelman-pucci-estimate-for-stro.md)
- [The Krylov–Safonov covering lemma](../../../../measure-theory/integral/part-02/the-krylov-safonov-covering-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.exists_eLpNorm_le_mul_rpow_mul_add_eLpNorm_posPart`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/KrylovSafonov/WeakHarnack.html#TauCeti.PDE.exists_eLpNorm_le_mul_rpow_mul_add_eLpNorm_posPart).

## Other forms

**The weak Harnack inequality for strong supersolutions (Gilbarg–Trudinger, Theorem 9.22).** Formalized in Tau Ceti as [`TauCeti.PDE.exists_eLpNorm_le_mul_rpow_mul_add_eLpNorm_posPart_of_wkp`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/KrylovSafonov/WeakHarnack.html#TauCeti.PDE.exists_eLpNorm_le_mul_rpow_mul_add_eLpNorm_posPart_of_wkp).

```lean
TauCeti.PDE.exists_eLpNorm_le_mul_rpow_mul_add_eLpNorm_posPart_of_wkp.{u_1} {ι : Type u_1}
  [Fintype ι] [DecidableEq ι] [Fact (1 ≤ ↑(Fintype.card ι))] {κ : ℝ} (hκ : 0 < κ) :
  ∃ p C,
    0 < p ∧
      0 < C ∧
        ∀ ⦃lam Lam R : ℝ⦄ ⦃c : EuclideanSpace ℝ ι⦄ ⦃Ω : TopologicalSpace.Opens (EuclideanSpace ℝ ι)⦄
          ⦃a : EuclideanSpace ℝ ι → Matrix ι ι ℝ⦄ ⦃ū f : EuclideanSpace ℝ ι → ℝ⦄
          (u : TauCeti.Wkp MeasureTheory.volume Ω (↑(Fintype.card ι)) 2),
          Metric.closedBall c R ⊆ ↑Ω →
            TauCeti.PDE.UniformlyEllipticOn (Metric.ball c R) a lam Lam →
              Lam ≤ κ * lam →
                ContinuousOn ū ↑Ω →
                  ↑↑(TauCeti.Wkp.value 2 u) =ᵐ[MeasureTheory.volume.restrict ↑Ω] ū →
                    (∀ x ∈ Metric.closedBall c R, 0 ≤ ū x) →
                      (∀ᵐ (x : EuclideanSpace ℝ ι) ∂MeasureTheory.volume.restrict (Metric.ball c R),
                          ∑ i,
                              ∑ j,
                                a x i j *
                                  ((↑↑(TauCeti.Wkp.iteratedGradient 1 u) x)
                                        (EuclideanSpace.single j 1)).ofLp
                                    i ≤
                            f x) →
                        ∀ y ∈ Metric.ball c (R / 4),
                          MeasureTheory.eLpNorm ū (ENNReal.ofReal p)
                              (MeasureTheory.volume.restrict
                                (Metric.ball c (R / (16 * √↑(Fintype.card ι))))) ≤
                            ENNReal.ofReal (C * R ^ (↑(Fintype.card ι) / p)) *
                              (ENNReal.ofReal (ū y) +
                                ENNReal.ofReal (R / lam) *
                                  MeasureTheory.eLpNorm (fun x => (f x)⁺) (↑(Fintype.card ι))
                                    (MeasureTheory.volume.restrict (Metric.ball c R)))
```

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.exists_eLpNorm_le_mul_rpow_mul_add_eLpNorm_posPart`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/KrylovSafonov/WeakHarnack.html#TauCeti.PDE.exists_eLpNorm_le_mul_rpow_mul_add_eLpNorm_posPart)
- [Source of `TauCeti.PDE.exists_eLpNorm_le_mul_rpow_mul_add_eLpNorm_posPart` in TauCeti/Analysis/PDE/Regularity/KrylovSafonov/WeakHarnack.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/Regularity/KrylovSafonov/WeakHarnack.lean#L295)
