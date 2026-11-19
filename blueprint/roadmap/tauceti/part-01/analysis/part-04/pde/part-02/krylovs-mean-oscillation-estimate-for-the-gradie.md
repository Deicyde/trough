---
declaration: theorem
origin: cited
lean: TauCeti.PDE.setIntegral_ball_norm_gradient_sub_setAverage_sq_le_add_of_norm_matrixBilinearForm_sub_le, TauCeti.PDE.setAverage_ball_norm_gradient_sub_setAverage_sq_le_of_norm_matrixBilinearForm_sub_le
statement: formalized
proof: formalized
---

# Krylov's mean oscillation estimate for the gradient

Let `u ∈ H¹(Ω)` solve
`-∂ᵢ(aⁱʲ ∂ⱼu) = -div G` weakly on an open set `Ω ⊆ ℝ^{n+1}`, that is
`∫_Ω ⟨a ∇u, ∇φ⟩ = ∫_Ω ⟨G, ∇φ⟩` for every test function `φ`, let `ball x₀ r ⊆ Ω`, and let `A` be a
constant matrix, uniformly elliptic with constants `0 < λ ≤ Λ`. Suppose that `a` is measurable on
`B_r = ball x₀ r` and that the deviation `θ(x) = ‖a(x) - A‖`, in the operator norm of the attached
bilinear forms, is bounded there. Then for `0 < ρ ≤ r` and every constant vector `c` with
`G - c ∈ L²(B_r)`, the square mean oscillation `ψ(t) = ∫_{B_t} ‖∇u - (∇u)_{B_t}‖²` satisfies

`ψ(ρ) ≤ 4 D (ρ / r)^(n + 3) ψ(r) + (2 (4 D + 2) / λ²) (∫_{B_r} θ² ‖∇u‖² + ∫_{B_r} ‖G - c‖²)`,

with `D = 2^(3n + 13) (n + 2)² (Λ / λ)^((n + 3) / 2)`. For `a = A` this is
`TauCeti.PDE.setIntegral_ball_norm_gradient_sub_setAverage_sq_le_add_of_forall_energyFormH1_eq`,
up to the factor `2`.

```lean
TauCeti.PDE.setIntegral_ball_norm_gradient_sub_setAverage_sq_le_add_of_norm_matrixBilinearForm_sub_le
  {n : ℕ} {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ (Fin (n + 1)))}
  {A : Matrix (Fin (n + 1)) (Fin (n + 1)) ℝ}
  {a : EuclideanSpace ℝ (Fin (n + 1)) → Matrix (Fin (n + 1)) (Fin (n + 1)) ℝ}
  {G : EuclideanSpace ℝ (Fin (n + 1)) → EuclideanSpace ℝ (Fin (n + 1))}
  {x₀ c : EuclideanSpace ℝ (Fin (n + 1))} {ρ r lam Lam K : ℝ}
  (hA : TauCeti.PDE.UniformlyEllipticOn (Metric.ball x₀ r) (fun x => A) lam Lam)
  (ha : MeasureTheory.AEStronglyMeasurable a (MeasureTheory.volume.restrict (Metric.ball x₀ r)))
  (haK :
    ∀ x ∈ Metric.ball x₀ r,
      ‖TauCeti.PDE.matrixBilinearForm (a x) - TauCeti.PDE.matrixBilinearForm A‖ ≤ K)
  {u : ↥(TauCeti.W1p MeasureTheory.volume Omega 2)}
  (hu :
    ∀ (φ : TestFunction Omega ℝ ⊤),
      TauCeti.PDE.energyFormH1 a 0 0 u
          ((TauCeti.W1p.ofTestFunctionₗ MeasureTheory.volume Omega 2) φ) =
        ∫ (x : EuclideanSpace ℝ (Fin (n + 1))) in ↑Omega, inner ℝ (G x) (gradient (⇑φ) x))
  (hball : Metric.ball x₀ r ⊆ ↑Omega)
  (hGc :
    MeasureTheory.MemLp (fun x => G x - c) 2 (MeasureTheory.volume.restrict (Metric.ball x₀ r)))
  (hρ : 0 < ρ) (hρr : ρ ≤ r) :
  ∫ (x : EuclideanSpace ℝ (Fin (n + 1))) in Metric.ball x₀ ρ,
      ‖↑↑(TauCeti.W1p.gradient u) x -
            ⨍ (y : EuclideanSpace ℝ (Fin (n + 1))) in Metric.ball x₀ ρ,
              ↑↑(TauCeti.W1p.gradient u) y‖ ^
        2 ≤
    (4 * (2 ^ (3 * n + 13) * (↑n + 2) ^ 2 * √(Lam / lam) ^ (n + 3)) * (ρ / r) ^ (n + 3) *
        ∫ (x : EuclideanSpace ℝ (Fin (n + 1))) in Metric.ball x₀ r,
          ‖↑↑(TauCeti.W1p.gradient u) x -
                ⨍ (y : EuclideanSpace ℝ (Fin (n + 1))) in Metric.ball x₀ r,
                  ↑↑(TauCeti.W1p.gradient u) y‖ ^
            2) +
      2 * (4 * (2 ^ (3 * n + 13) * (↑n + 2) ^ 2 * √(Lam / lam) ^ (n + 3)) + 2) / lam ^ 2 *
        ((∫ (x : EuclideanSpace ℝ (Fin (n + 1))) in Metric.ball x₀ r,
            ‖TauCeti.PDE.matrixBilinearForm (a x) - TauCeti.PDE.matrixBilinearForm A‖ ^ 2 *
              ‖↑↑(TauCeti.W1p.gradient u) x‖ ^ 2) +
          ∫ (x : EuclideanSpace ℝ (Fin (n + 1))) in Metric.ball x₀ r, ‖G x - c‖ ^ 2)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The du Bois-Reymond lemma](../../../part-03/distribution/the-du-bois-reymond-lemma.md)
- [Green's second identity against a test function](../../sobolev/part-01/greens-second-identity-against-a-test-function.md)
- [Gårding's inequality on `H¹(Ω)`](gardings-inequality-on-h1.md)
- [Hölder's inequality for disjoint pieces](../../../../measure-theory/function/part-01/holders-inequality-for-disjoint-pieces.md)
- [Hölder's inequality with a bounded weight](../../../../measure-theory/integral/part-02/holders-inequality-with-a-bounded-weight.md)
- [Jensen's inequality for the square of a mean](../../../../measure-theory/integral/part-02/jensens-inequality-for-the-square-of-a-mean.md)
- [The Lipschitz bound for bounded harmonic functions](../../../part-03/inner-product-space/part-02/the-lipschitz-bound-for-bounded-harmonic-functio.md)
- [Meyers–Serrin: `H = W` in `W^{k,p}(Ω)`](../../sobolev/part-02/meyers-serrin-h-w-in-w-k-p.md)
- [The Mihlin–Hörmander multiplier theorem on `Lᵖ`](../../../part-02/partial-differential-equations/the-mihlin-hormander-multiplier-theorem-on-lp.md)
- [The Poincaré inequality on a ball](../../sobolev/part-02/the-poincare-inequality-on-a-ball.md)
- [Rademacher's theorem for locally Lipschitz functions](../../../part-03/calculus/part-02/rademachers-theorem-for-locally-lipschitz-functi.md)
- [Weyl's lemma for continuous functions](../../../part-03/inner-product-space/part-03/weyls-lemma-for-continuous-functions.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.setIntegral_ball_norm_gradient_sub_setAverage_sq_le_add_of_norm_matrixBilinearForm_sub_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/MeanOscillation.html#TauCeti.PDE.setIntegral_ball_norm_gradient_sub_setAverage_sq_le_add_of_norm_matrixBilinearForm_sub_le).

## Other forms

**Krylov's mean oscillation estimate for the gradient, averaged form.** Formalized in Tau Ceti as [`TauCeti.PDE.setAverage_ball_norm_gradient_sub_setAverage_sq_le_of_norm_matrixBilinearForm_sub_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/MeanOscillation.html#TauCeti.PDE.setAverage_ball_norm_gradient_sub_setAverage_sq_le_of_norm_matrixBilinearForm_sub_le).

```lean
TauCeti.PDE.setAverage_ball_norm_gradient_sub_setAverage_sq_le_of_norm_matrixBilinearForm_sub_le
  {n : ℕ} {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ (Fin (n + 1)))}
  {A : Matrix (Fin (n + 1)) (Fin (n + 1)) ℝ}
  {a : EuclideanSpace ℝ (Fin (n + 1)) → Matrix (Fin (n + 1)) (Fin (n + 1)) ℝ}
  {G : EuclideanSpace ℝ (Fin (n + 1)) → EuclideanSpace ℝ (Fin (n + 1))}
  {x₀ c : EuclideanSpace ℝ (Fin (n + 1))} {ρ r lam Lam K : ℝ}
  (hA : TauCeti.PDE.UniformlyEllipticOn (Metric.ball x₀ r) (fun x => A) lam Lam)
  (ha : MeasureTheory.AEStronglyMeasurable a (MeasureTheory.volume.restrict (Metric.ball x₀ r)))
  (haK :
    ∀ x ∈ Metric.ball x₀ r,
      ‖TauCeti.PDE.matrixBilinearForm (a x) - TauCeti.PDE.matrixBilinearForm A‖ ≤ K)
  {u : ↥(TauCeti.W1p MeasureTheory.volume Omega 2)}
  (hu :
    ∀ (φ : TestFunction Omega ℝ ⊤),
      TauCeti.PDE.energyFormH1 a 0 0 u
          ((TauCeti.W1p.ofTestFunctionₗ MeasureTheory.volume Omega 2) φ) =
        ∫ (x : EuclideanSpace ℝ (Fin (n + 1))) in ↑Omega, inner ℝ (G x) (gradient (⇑φ) x))
  (hball : Metric.ball x₀ r ⊆ ↑Omega)
  (hGc :
    MeasureTheory.MemLp (fun x => G x - c) 2 (MeasureTheory.volume.restrict (Metric.ball x₀ r)))
  {q q' : ℝ} (hq : q.HolderConjugate q')
  (hgq :
    MeasureTheory.MemLp (↑↑(TauCeti.W1p.gradient u)) (ENNReal.ofReal (2 * q))
      (MeasureTheory.volume.restrict (Metric.ball x₀ r)))
  (hρ : 0 < ρ) (hρr : ρ ≤ r) :
  ⨍ (x : EuclideanSpace ℝ (Fin (n + 1))) in Metric.ball x₀ ρ,
      ‖↑↑(TauCeti.W1p.gradient u) x -
            ⨍ (y : EuclideanSpace ℝ (Fin (n + 1))) in Metric.ball x₀ ρ,
              ↑↑(TauCeti.W1p.gradient u) y‖ ^
        2 ≤
    (4 * (2 ^ (3 * n + 13) * (↑n + 2) ^ 2 * √(Lam / lam) ^ (n + 3)) * (ρ / r) ^ 2 *
        ⨍ (x : EuclideanSpace ℝ (Fin (n + 1))) in Metric.ball x₀ r,
          ‖↑↑(TauCeti.W1p.gradient u) x -
                ⨍ (y : EuclideanSpace ℝ (Fin (n + 1))) in Metric.ball x₀ r,
                  ↑↑(TauCeti.W1p.gradient u) y‖ ^
            2) +
      2 * (4 * (2 ^ (3 * n + 13) * (↑n + 2) ^ 2 * √(Lam / lam) ^ (n + 3)) + 2) / lam ^ 2 *
          (r / ρ) ^ (n + 1) *
        ((⨍ (x : EuclideanSpace ℝ (Fin (n + 1))) in Metric.ball x₀ r, ‖G x - c‖ ^ 2) +
          (K ^ (2 * q' - 1) *
                ⨍ (x : EuclideanSpace ℝ (Fin (n + 1))) in Metric.ball x₀ r,
                  ‖TauCeti.PDE.matrixBilinearForm (a x) - TauCeti.PDE.matrixBilinearForm A‖) ^
              q'⁻¹ *
            (⨍ (x : EuclideanSpace ℝ (Fin (n + 1))) in Metric.ball x₀ r,
                ‖↑↑(TauCeti.W1p.gradient u) x‖ ^ (2 * q)) ^
              q⁻¹)
```

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.setIntegral_ball_norm_gradient_sub_setAverage_sq_le_add_of_norm_matrixBilinearForm_sub_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/MeanOscillation.html#TauCeti.PDE.setIntegral_ball_norm_gradient_sub_setAverage_sq_le_add_of_norm_matrixBilinearForm_sub_le)
- [Source of `TauCeti.PDE.setIntegral_ball_norm_gradient_sub_setAverage_sq_le_add_of_norm_matrixBilinearForm_sub_le` in TauCeti/Analysis/PDE/Regularity/MeanOscillation.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/Regularity/MeanOscillation.lean#L89)
