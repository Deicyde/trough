---
declaration: theorem
origin: cited
lean: TauCeti.PDE.exists_holderOnWith_of_abs_sum_mul_fderiv_fderiv_le, TauCeti.PDE.exists_holderOnWith_of_sum_mul_fderiv_fderiv_eq
statement: formalized
proof: formalized
---

# The interior Hölder estimate of Krylov and Safonov

**The interior Hölder estimate of Krylov and Safonov** (Caffarelli–Cabré, Proposition 4.10,
for classical functions). Let `κ > 0`. There are `0 < α ≤ 1` and `C > 0`, depending only on the
dimension and on `κ`, with the following property. Let `a` be uniformly elliptic on
`B(x₀, 2 r)` with constants `λ ≤ Λ ≤ κ λ`, and let `u` be `C²` in `B(x₀, 2 r)` with `|u| ≤ M`
and `|∑ᵢⱼ aⁱʲ ∂ᵢ∂ⱼu| ≤ f` there, where `f ∈ Lⁿ(B(x₀, 2 r))`. Then `u` is `α`-Hölder on
`B(x₀, r)` with constant `C r^(-α) (M + r ‖f‖_{Lⁿ(B(x₀, 2 r))} / λ)`.

The coefficients need no regularity, not even measurability, and need not be symmetric.

```lean
TauCeti.PDE.exists_holderOnWith_of_abs_sum_mul_fderiv_fderiv_le.{u_1} {ι : Type u_1} [Fintype ι]
  [DecidableEq ι] [Nonempty ι] {κ : ℝ} (hκ : 0 < κ) :
  ∃ α C,
    0 < α ∧
      α ≤ 1 ∧
        0 < C ∧
          ∀ ⦃lam Lam r M : ℝ⦄ ⦃x₀ : EuclideanSpace ℝ ι⦄ ⦃a : EuclideanSpace ℝ ι → Matrix ι ι ℝ⦄
            ⦃u f : EuclideanSpace ℝ ι → ℝ⦄,
            0 < r →
              TauCeti.PDE.UniformlyEllipticOn (Metric.ball x₀ (2 * r)) a lam Lam →
                Lam ≤ κ * lam →
                  ContDiffOn ℝ 2 u (Metric.ball x₀ (2 * r)) →
                    (∀ x ∈ Metric.ball x₀ (2 * r), |u x| ≤ M) →
                      (∀ x ∈ Metric.ball x₀ (2 * r),
                          |∑ i,
                                ∑ j,
                                  a x i j *
                                    ((fderiv ℝ (fderiv ℝ u) x) (EuclideanSpace.single i 1))
                                      (EuclideanSpace.single j 1)| ≤
                            f x) →
                        MeasureTheory.MemLp f (↑(Fintype.card ι))
                            (MeasureTheory.volume.restrict (Metric.ball x₀ (2 * r))) →
                          HolderOnWith
                            (C * r ^ (-↑α) *
                                (M +
                                  r *
                                      (MeasureTheory.eLpNorm f (↑(Fintype.card ι))
                                          (MeasureTheory.volume.restrict
                                            (Metric.ball x₀ (2 * r)))).toReal /
                                    lam)).toNNReal
                            α u (Metric.ball x₀ r)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Aleksandrov–Bakelman–Pucci estimate for strong subsolutions](../../../part-02/partial-differential-equations/the-aleksandrov-bakelman-pucci-estimate-for-stro.md)
- [The Krylov–Safonov covering lemma](../../../../measure-theory/integral/part-02/the-krylov-safonov-covering-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.exists_holderOnWith_of_abs_sum_mul_fderiv_fderiv_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/KrylovSafonov/Holder.html#TauCeti.PDE.exists_holderOnWith_of_abs_sum_mul_fderiv_fderiv_le).

## Other forms

**The interior Hölder estimate of Krylov and Safonov.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_holderOnWith_of_sum_mul_fderiv_fderiv_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/KrylovSafonov/Holder.html#TauCeti.PDE.exists_holderOnWith_of_sum_mul_fderiv_fderiv_eq).

```lean
TauCeti.PDE.exists_holderOnWith_of_sum_mul_fderiv_fderiv_eq.{u_1} {ι : Type u_1} [Fintype ι]
  [DecidableEq ι] [Nonempty ι] {κ : ℝ} (hκ : 0 < κ) :
  ∃ α C,
    0 < α ∧
      α ≤ 1 ∧
        0 < C ∧
          ∀ ⦃lam Lam r M : ℝ⦄ ⦃x₀ : EuclideanSpace ℝ ι⦄ ⦃a : EuclideanSpace ℝ ι → Matrix ι ι ℝ⦄
            ⦃u f : EuclideanSpace ℝ ι → ℝ⦄,
            0 < r →
              TauCeti.PDE.UniformlyEllipticOn (Metric.ball x₀ (2 * r)) a lam Lam →
                Lam ≤ κ * lam →
                  ContDiffOn ℝ 2 u (Metric.ball x₀ (2 * r)) →
                    (∀ x ∈ Metric.ball x₀ (2 * r), |u x| ≤ M) →
                      (∀ x ∈ Metric.ball x₀ (2 * r),
                          ∑ i,
                              ∑ j,
                                a x i j *
                                  ((fderiv ℝ (fderiv ℝ u) x) (EuclideanSpace.single i 1))
                                    (EuclideanSpace.single j 1) =
                            f x) →
                        MeasureTheory.MemLp f (↑(Fintype.card ι))
                            (MeasureTheory.volume.restrict (Metric.ball x₀ (2 * r))) →
                          HolderOnWith
                            (C * r ^ (-↑α) *
                                (M +
                                  r *
                                      (MeasureTheory.eLpNorm f (↑(Fintype.card ι))
                                          (MeasureTheory.volume.restrict
                                            (Metric.ball x₀ (2 * r)))).toReal /
                                    lam)).toNNReal
                            α u (Metric.ball x₀ r)
```

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.exists_holderOnWith_of_abs_sum_mul_fderiv_fderiv_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/KrylovSafonov/Holder.html#TauCeti.PDE.exists_holderOnWith_of_abs_sum_mul_fderiv_fderiv_le)
- [Source of `TauCeti.PDE.exists_holderOnWith_of_abs_sum_mul_fderiv_fderiv_le` in TauCeti/Analysis/PDE/Regularity/KrylovSafonov/Holder.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/Regularity/KrylovSafonov/Holder.lean#L406)
