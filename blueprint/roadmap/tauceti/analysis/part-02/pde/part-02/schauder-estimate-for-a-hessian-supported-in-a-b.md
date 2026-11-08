---
declaration: theorem
origin: cited
lean: TauCeti.PDE.exists_holderWith_iteratedFDeriv_two_of_support_subset_closedBall
statement: formalized
proof: formalized
---

# Schauder estimate for a Hessian supported in a ball

Let `0 < α < 1`. There is
`C > 0`, depending only on dimension and `α`, with the following property. Let `a` be
`α`-Hölder entrywise with constant `L` on the support ball, and suppose `a x₀` has
ellipticity bounds `λ, Λ`,
with `λ > 0`. Put

`Lu = ∑ᵢⱼ aᵢⱼ ∂ᵢⱼu`.

If the Hessian of a global `C²` function `u` is supported in the closed ball of radius `R`
about `x₀` and is globally `α`-Hölder a priori, then the scale condition

`2 κ (n+1)² (L Rᵅ + 2ᵅ L rᵅ) ≤ λ`,

where `κ = C (Λ / λ)^(1 + (n+1)/4 + α/2)`, implies the estimate

`[D²u]ᵅ ≤ 2 κ ([Lu]ᵅ / λ + ((n+1)² 2ᵅ L / λ |Bᵣ|⁻¹/²
  + r^(-(n+1)/2-α)) ‖D²u‖₂)`.

Thus no uniform comparison of `a` with one constant matrix is assumed: the support condition
allows the coefficients to be retracted to the support ball and frozen at its centre.

```lean
TauCeti.PDE.exists_holderWith_iteratedFDeriv_two_of_support_subset_closedBall {n : ℕ} {α : NNReal}
  (hα : 0 < α) (hα1 : α < 1) :
  ∃ C,
    0 < C ∧
      ∀ {a : EuclideanSpace ℝ (Fin (n + 1)) → Matrix (Fin (n + 1)) (Fin (n + 1)) ℝ}
        {x₀ : EuclideanSpace ℝ (Fin (n + 1))} {lam Lam : ℝ},
        0 < lam →
          (∀ (ξ : EuclideanSpace ℝ (Fin (n + 1))), lam * ‖ξ‖ ^ 2 ≤ (a x₀).toQuadraticForm' ξ.ofLp) →
            (∀ (ξ : EuclideanSpace ℝ (Fin (n + 1))),
                (a x₀).toQuadraticForm' ξ.ofLp ≤ Lam * ‖ξ‖ ^ 2) →
              ∀ {L K : NNReal} {R r : ℝ},
                0 ≤ R →
                  0 < r →
                    2 * (C * (Lam / lam) ^ (1 + (↑n + 1) / 4 + ↑α / 2)) * (↑n + 1) ^ 2 *
                          (↑L * R ^ ↑α + ↑L * 2 ^ ↑α * r ^ ↑α) ≤
                        lam →
                      (∀ (i j : Fin (n + 1)),
                          HolderOnWith L α (fun x => a x i j) (Metric.closedBall x₀ R)) →
                        ∀ {u : EuclideanSpace ℝ (Fin (n + 1)) → ℝ},
                          ContDiff ℝ 2 u →
                            MemHolder α (iteratedFDeriv ℝ 2 u) →
                              Function.support (iteratedFDeriv ℝ 2 u) ⊆ Metric.closedBall x₀ R →
                                (HolderWith K α fun x =>
                                    ∑ i,
                                      ∑ j,
                                        a x i j •
                                          ((fderiv ℝ (fderiv ℝ u) x) (EuclideanSpace.single i 1))
                                            (EuclideanSpace.single j 1)) →
                                  HolderWith
                                    (2 * (C * (Lam / lam) ^ (1 + (↑n + 1) / 4 + ↑α / 2)) *
                                        (↑K / lam +
                                          ((↑n + 1) ^ 2 * (↑L * 2 ^ ↑α) / lam *
                                                (MeasureTheory.volume (Metric.ball 0 r) ^
                                                    (-2⁻¹)).toReal +
                                              r ^ (-((↑n + 1) / 2 + ↑α))) *
                                            (MeasureTheory.eLpNorm (iteratedFDeriv ℝ 2 u) 2
                                                MeasureTheory.volume).toReal)).toNNReal
                                    α (iteratedFDeriv ℝ 2 u)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hölder's bound on an average](../../../../measure-theory/euclidean-isoperimetry-sharp-inequalities-and-ri/part-02/holders-bound-on-an-average.md)

## Informally uses

- [The interior Schauder estimate on small balls](../part-01/the-interior-schauder-estimate-on-small-balls.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.exists_holderWith_iteratedFDeriv_two_of_support_subset_closedBall`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/Schauder/CompactSupport.html#TauCeti.PDE.exists_holderWith_iteratedFDeriv_two_of_support_subset_closedBall).

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.exists_holderWith_iteratedFDeriv_two_of_support_subset_closedBall`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/Schauder/CompactSupport.html#TauCeti.PDE.exists_holderWith_iteratedFDeriv_two_of_support_subset_closedBall)
- [Source of `TauCeti.PDE.exists_holderWith_iteratedFDeriv_two_of_support_subset_closedBall` in TauCeti/Analysis/PDE/Regularity/Hessian/Schauder/CompactSupport.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/PDE/Regularity/Hessian/Schauder/CompactSupport.lean#L49)
