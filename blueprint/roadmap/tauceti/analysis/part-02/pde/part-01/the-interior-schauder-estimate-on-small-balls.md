---
declaration: theorem
origin: cited
lean: TauCeti.PDE.exists_holderOnWith_iteratedFDeriv_two_closedBall_of_sum_smul_fderiv_fderiv, TauCeti.PDE.exists_holderOnWith_iteratedFDeriv_two_of_sum_smul_fderiv_fderiv, TauCeti.PDE.exists_holderOnWith_iteratedFDeriv_two_of_sum_smul_fderiv_fderiv_of_holderOnWith, TauCeti.PDE.exists_holderOnWith_iteratedFDeriv_two_of_laplacian, TauCeti.PDE.exists_holderOnWith_iteratedFDeriv_two_of_sum_smul_fderiv_fderiv_add_fderiv_add_mul
statement: formalized
proof: formalized
---

# The interior Schauder estimate on small balls

Let `0 < α < 1`. There is `C₀ > 0`,
depending only on dimension and `α`, with the following property. Let `0 < λ`, `Λ`, `L`, `M` and
`0 < R` be given, put `κ = C₀ (Λ / λ)^(1 + (n+1)/4 + α/2)`, and assume the scale condition

`2 κ (n+1)² (1 + 2ᵅ) L Rᵅ ≤ λ`.

Then for every `ρ < R` there is `C`, depending only on `n`, `α`, `λ`, `Λ`, `L`, `M`, `R` and `ρ`,
with the following property. Let `a` be `α`-Hölder entrywise with constant `L` and bounded entrywise
by `M` on the closed ball `closedBall x₀ R`, and suppose `a x₀` has ellipticity bounds `λ, Λ`. Put
`L u = ∑ᵢⱼ aᵢⱼ ∂ᵢⱼu`. Let `u` be `C²` on the open ball `B_R`, with `|u|`, `‖Du‖` and `‖D²u‖` bounded
by `N` there and with `D²u` `α`-Hölder on `B_R` (with any constant). If `L u` is `α`-Hölder on `B_R`
with constant `K`, then `D²u` is `α`-Hölder on `closedBall x₀ ρ` with constant `C (K + N)`.

The constant `C` does not depend on the centre `x₀` or on the coefficient field `a` beyond the
bounds `λ`, `Λ`, `L` and `M`; this uniformity is what makes the estimate usable on infinitely many
balls at once.

```lean
TauCeti.PDE.exists_holderOnWith_iteratedFDeriv_two_closedBall_of_sum_smul_fderiv_fderiv {n : ℕ}
  {α : NNReal} (hα : 0 < α) (hα1 : α < 1) :
  ∃ C₀,
    0 < C₀ ∧
      ∀ {lam Lam : ℝ} {L M : NNReal} {R : ℝ},
        0 < lam →
          0 < R →
            2 * (C₀ * (Lam / lam) ^ (1 + (↑n + 1) / 4 + ↑α / 2)) * (↑n + 1) ^ 2 *
                  ((1 + 2 ^ ↑α) * ↑L * R ^ ↑α) ≤
                lam →
              ∀ {ρ : ℝ},
                ρ < R →
                  ∃ C,
                    ∀ {a : EuclideanSpace ℝ (Fin (n + 1)) → Matrix (Fin (n + 1)) (Fin (n + 1)) ℝ}
                      {x₀ : EuclideanSpace ℝ (Fin (n + 1))},
                      (∀ (ξ : EuclideanSpace ℝ (Fin (n + 1))),
                          lam * ‖ξ‖ ^ 2 ≤ (a x₀).toQuadraticForm' ξ.ofLp) →
                        (∀ (ξ : EuclideanSpace ℝ (Fin (n + 1))),
                            (a x₀).toQuadraticForm' ξ.ofLp ≤ Lam * ‖ξ‖ ^ 2) →
                          (∀ (i j : Fin (n + 1)),
                              HolderOnWith L α (fun x => a x i j) (Metric.closedBall x₀ R)) →
                            (∀ x ∈ Metric.closedBall x₀ R, ∀ (i j : Fin (n + 1)), |a x i j| ≤ ↑M) →
                              ∀ {u : EuclideanSpace ℝ (Fin (n + 1)) → ℝ} {N K V : NNReal},
                                ContDiffOn ℝ 2 u (Metric.ball x₀ R) →
                                  (∀ x ∈ Metric.ball x₀ R, |u x| ≤ ↑N) →
                                    (∀ x ∈ Metric.ball x₀ R, ‖fderiv ℝ u x‖ ≤ ↑N) →
                                      (∀ x ∈ Metric.ball x₀ R, ‖iteratedFDeriv ℝ 2 u x‖ ≤ ↑N) →
                                        HolderOnWith V α (iteratedFDeriv ℝ 2 u) (Metric.ball x₀ R) →
                                          HolderOnWith K α
                                              (fun x =>
                                                ∑ i,
                                                  ∑ j,
                                                    a x i j •
                                                      ((fderiv ℝ (fderiv ℝ u) x)
                                                          (EuclideanSpace.single i 1))
                                                        (EuclideanSpace.single j 1))
                                              (Metric.ball x₀ R) →
                                            HolderOnWith (C * (K + N)) α (iteratedFDeriv ℝ 2 u)
                                              (Metric.closedBall x₀ ρ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The du Bois-Reymond lemma](../../distribution/the-du-bois-reymond-lemma.md)
- [Green's first identity against `H¹₀(Ω)`](greens-first-identity-against-h10.md)
- [Green's second identity against a test function](../../sobolev/part-01/greens-second-identity-against-a-test-function.md)
- [Gårding's inequality on `H¹(Ω)`](gardings-inequality-on-h1.md)
- [Hölder's bound on an average](../../../../measure-theory/integral/part-01/holders-bound-on-an-average.md)
- [Hölder's inequality for the integral of a product](../../../../measure-theory/function/holders-inequality-for-the-integral-of-a-product.md)
- [Jensen's inequality for the square of a mean](../../../../measure-theory/integral/part-01/jensens-inequality-for-the-square-of-a-mean.md)
- [The Lipschitz bound for bounded harmonic functions](../../inner-product-space/part-02/the-lipschitz-bound-for-bounded-harmonic-functio.md)
- [The local Campanato estimate](../../../../measure-theory/function/the-local-campanato-estimate.md)
- [Local Hölder bounds near a compact set are uniform on a thickening](../../../../topology/metric-space/local-holder-bounds-near-a-compact-set-are-unifo.md)
- [Meyers–Serrin: `H = W` in `W^{k,p}(Ω)`](../../sobolev/part-01/meyers-serrin-h-w-in-w-k-p.md)
- [The Poincaré inequality on a ball](../../sobolev/part-02/the-poincare-inequality-on-a-ball.md)
- [Rademacher's theorem for locally Lipschitz functions](../../calculus/part-01/rademachers-theorem-for-locally-lipschitz-functi.md)
- [Schauder estimate for a Hessian supported in a ball](../part-02/schauder-estimate-for-a-hessian-supported-in-a-b.md)
- [TauCeti.Wkp](../../../part-01/partial-differential-equations/tauceti-wkp.md)
- [Weyl's lemma for continuous functions](../../inner-product-space/part-03/weyls-lemma-for-continuous-functions.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.exists_holderOnWith_iteratedFDeriv_two_closedBall_of_sum_smul_fderiv_fderiv`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/Schauder/Interior.html#TauCeti.PDE.exists_holderOnWith_iteratedFDeriv_two_closedBall_of_sum_smul_fderiv_fderiv).

## Other forms

**Interior Schauder estimate for constant-coefficient operators, classical form.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_holderOnWith_iteratedFDeriv_two_of_sum_smul_fderiv_fderiv`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/Schauder/Basic.html#TauCeti.PDE.exists_holderOnWith_iteratedFDeriv_two_of_sum_smul_fderiv_fderiv).

```lean
TauCeti.PDE.exists_holderOnWith_iteratedFDeriv_two_of_sum_smul_fderiv_fderiv {n : ℕ} {α : NNReal}
  (hα : 0 < α) (hα1 : α < 1) :
  ∃ C,
    0 ≤ C ∧
      ∀ {A : Matrix (Fin (n + 1)) (Fin (n + 1)) ℝ} {lam Lam : ℝ},
        0 < lam →
          (∀ (ξ : EuclideanSpace ℝ (Fin (n + 1))), lam * ‖ξ‖ ^ 2 ≤ A.toQuadraticForm' ξ.ofLp) →
            (∀ (ξ : EuclideanSpace ℝ (Fin (n + 1))), A.toQuadraticForm' ξ.ofLp ≤ Lam * ‖ξ‖ ^ 2) →
              ∀ {U S : Set (EuclideanSpace ℝ (Fin (n + 1)))}
                {u : EuclideanSpace ℝ (Fin (n + 1)) → ℝ} {K : NNReal} {R : ℝ},
                IsOpen U →
                  ContDiffOn ℝ 2 u U →
                    Bornology.IsBounded S →
                      0 < R →
                        Metric.cthickening R S ⊆ U →
                          HolderOnWith K α
                              (fun x =>
                                ∑ i,
                                  ∑ j,
                                    A i j •
                                      ((fderiv ℝ (fderiv ℝ u) x) (EuclideanSpace.single i 1))
                                        (EuclideanSpace.single j 1))
                              (Metric.thickening R S) →
                            HolderOnWith
                              (C * (Lam / lam) ^ (1 + (↑n + 1) / 4 + ↑α / 2) *
                                  (↑K / lam +
                                    R ^ (-((↑n + 1) / 2 + ↑α)) *
                                      (MeasureTheory.eLpNorm (iteratedFDeriv ℝ 2 u) 2
                                          (MeasureTheory.volume.restrict
                                            (Metric.thickening R S))).toReal)).toNNReal
                              α (iteratedFDeriv ℝ 2 u) S
```

**The interior Schauder estimate for Hölder coefficients.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_holderOnWith_iteratedFDeriv_two_of_sum_smul_fderiv_fderiv_of_holderOnWith`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/Schauder/HolderCoefficient.html#TauCeti.PDE.exists_holderOnWith_iteratedFDeriv_two_of_sum_smul_fderiv_fderiv_of_holderOnWith).

```lean
TauCeti.PDE.exists_holderOnWith_iteratedFDeriv_two_of_sum_smul_fderiv_fderiv_of_holderOnWith {n : ℕ}
  {α : NNReal} (hα : 0 < α) (hα1 : α < 1) {Ω K : Set (EuclideanSpace ℝ (Fin (n + 1)))}
  (hΩ : IsOpen Ω) (hK : IsCompact K) (hKΩ : K ⊆ Ω)
  {a : EuclideanSpace ℝ (Fin (n + 1)) → Matrix (Fin (n + 1)) (Fin (n + 1)) ℝ}
  (ha :
    ∀ x ∈ K,
      ∃ r > 0, ∃ L, ∀ (i j : Fin (n + 1)), HolderOnWith L α (fun y => a y i j) (Metric.ball x r))
  (hell :
    ∀ x ∈ K,
      ∃ lam,
        0 < lam ∧
          ∀ (ξ : EuclideanSpace ℝ (Fin (n + 1))), lam * ‖ξ‖ ^ 2 ≤ (a x).toQuadraticForm' ξ.ofLp) :
  ∃ C,
    ∀ {u : EuclideanSpace ℝ (Fin (n + 1)) → ℝ} {N M : NNReal},
      ContDiffOn ℝ 2 u Ω →
        (∀ x ∈ Ω, |u x| ≤ ↑N) →
          (∀ x ∈ Ω, ‖fderiv ℝ u x‖ ≤ ↑N) →
            (∀ x ∈ Ω, ‖iteratedFDeriv ℝ 2 u x‖ ≤ ↑N) →
              (∀ S ⊆ Ω, IsCompact S → ∃ V, HolderOnWith V α (iteratedFDeriv ℝ 2 u) S) →
                HolderOnWith M α
                    (fun x =>
                      ∑ i,
                        ∑ j,
                          a x i j •
                            ((fderiv ℝ (fderiv ℝ u) x) (EuclideanSpace.single i 1))
                              (EuclideanSpace.single j 1))
                    Ω →
                  HolderOnWith (C * (M + N)) α (iteratedFDeriv ℝ 2 u) K
```

**Interior Schauder estimate for Poisson's equation, classical form.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_holderOnWith_iteratedFDeriv_two_of_laplacian`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/Schauder/Basic.html#TauCeti.PDE.exists_holderOnWith_iteratedFDeriv_two_of_laplacian).

```lean
TauCeti.PDE.exists_holderOnWith_iteratedFDeriv_two_of_laplacian {n : ℕ} {α : NNReal} (hα : 0 < α)
  (hα1 : α < 1) :
  ∃ C,
    0 ≤ C ∧
      ∀ {U S : Set (EuclideanSpace ℝ (Fin (n + 1)))} {u : EuclideanSpace ℝ (Fin (n + 1)) → ℝ}
        {K : NNReal} {R : ℝ},
        IsOpen U →
          ContDiffOn ℝ 2 u U →
            Bornology.IsBounded S →
              0 < R →
                Metric.cthickening R S ⊆ U →
                  HolderOnWith K α (Laplacian.laplacian u) (Metric.thickening R S) →
                    HolderOnWith
                      (C *
                          (↑K +
                            R ^ (-((↑n + 1) / 2 + ↑α)) *
                              (MeasureTheory.eLpNorm (iteratedFDeriv ℝ 2 u) 2
                                  (MeasureTheory.volume.restrict
                                    (Metric.thickening R S))).toReal)).toNNReal
                      α (iteratedFDeriv ℝ 2 u) S
```

**The interior Schauder estimate with lower-order terms.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_holderOnWith_iteratedFDeriv_two_of_sum_smul_fderiv_fderiv_add_fderiv_add_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/Schauder/LowerOrder.html#TauCeti.PDE.exists_holderOnWith_iteratedFDeriv_two_of_sum_smul_fderiv_fderiv_add_fderiv_add_mul).

```lean
TauCeti.PDE.exists_holderOnWith_iteratedFDeriv_two_of_sum_smul_fderiv_fderiv_add_fderiv_add_mul
  {n : ℕ} {α : NNReal} (hα : 0 < α) (hα1 : α < 1) {Ω K : Set (EuclideanSpace ℝ (Fin (n + 1)))}
  (hΩ : IsOpen Ω) (hK : IsCompact K) (hKΩ : K ⊆ Ω)
  {a : EuclideanSpace ℝ (Fin (n + 1)) → Matrix (Fin (n + 1)) (Fin (n + 1)) ℝ}
  {b : EuclideanSpace ℝ (Fin (n + 1)) → EuclideanSpace ℝ (Fin (n + 1))}
  {c : EuclideanSpace ℝ (Fin (n + 1)) → ℝ}
  (ha :
    ∀ x ∈ K,
      ∃ r > 0, ∃ L, ∀ (i j : Fin (n + 1)), HolderOnWith L α (fun y => a y i j) (Metric.ball x r))
  (hb : ∀ x ∈ K, ∃ r > 0, ∃ L, HolderOnWith L α b (Metric.ball x r))
  (hc : ∀ x ∈ K, ∃ r > 0, ∃ L, HolderOnWith L α c (Metric.ball x r))
  (hell :
    ∀ x ∈ K,
      ∃ lam,
        0 < lam ∧
          ∀ (ξ : EuclideanSpace ℝ (Fin (n + 1))), lam * ‖ξ‖ ^ 2 ≤ (a x).toQuadraticForm' ξ.ofLp) :
  ∃ C,
    ∀ {u : EuclideanSpace ℝ (Fin (n + 1)) → ℝ} {N M : NNReal},
      ContDiffOn ℝ 2 u Ω →
        (∀ x ∈ Ω, |u x| ≤ ↑N) →
          (∀ x ∈ Ω, ‖fderiv ℝ u x‖ ≤ ↑N) →
            (∀ x ∈ Ω, ‖iteratedFDeriv ℝ 2 u x‖ ≤ ↑N) →
              (∀ S ⊆ Ω, IsCompact S → ∃ V, HolderOnWith V α (iteratedFDeriv ℝ 2 u) S) →
                HolderOnWith M α
                    (fun x =>
                      ∑ i,
                            ∑ j,
                              a x i j •
                                ((fderiv ℝ (fderiv ℝ u) x) (EuclideanSpace.single i 1))
                                  (EuclideanSpace.single j 1) +
                          (fderiv ℝ u x) (b x) +
                        c x * u x)
                    Ω →
                  HolderOnWith (C * (M + N)) α (iteratedFDeriv ℝ 2 u) K
```

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.exists_holderOnWith_iteratedFDeriv_two_closedBall_of_sum_smul_fderiv_fderiv`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/Schauder/Interior.html#TauCeti.PDE.exists_holderOnWith_iteratedFDeriv_two_closedBall_of_sum_smul_fderiv_fderiv)
- [Source of `TauCeti.PDE.exists_holderOnWith_iteratedFDeriv_two_closedBall_of_sum_smul_fderiv_fderiv` in TauCeti/Analysis/PDE/Regularity/Hessian/Schauder/Interior.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/PDE/Regularity/Hessian/Schauder/Interior.lean#L332)
