---
declaration: theorem
origin: cited
lean: TauCeti.Polynomial.exists_analyticOnNhd_nonmonic_root_sub_eq_zpow_mul_unit_conj
statement: formalized
proof: formalized
---

# TauCeti.Polynomial.exists_analyticOnNhd_nonmonic_root_sub_eq_zpow_mul_unit_conj

Construct nonmonic Puiseux branches with global Laurent difference units respecting
conjugation. The unique conjugation permutation preserves the difference exponents and
interchanges their units on the full product. Exponents and units are indexed only by
unequal labels. Poles, collisions on the hyperplane, degree drops, nullified central fibers,
and degrees zero and one are allowed.

```lean
TauCeti.Polynomial.exists_analyticOnNhd_nonmonic_root_sub_eq_zpow_mul_unit_conj.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℂ E] [FiniteDimensional ℂ E] {U : Set E}
  [SimplyConnectedSpace ↑U] {F : E × ℂ → Polynomial ℂ} {d n a c : ℕ} {R R' : ℝ} {u v : E × ℂ → ℂ}
  {τ : E → E} (hU : IsOpen U) (hR' : 0 < R') (hn : n ≠ 0) (hR : R' ^ n ≤ R) (hdvd : d.factorial ∣ n)
  (hF : ∀ i ≤ d, AnalyticOnNhd ℂ (fun b => (F b).coeff i) (U ×ˢ Metric.ball 0 R))
  (hdeg : ∀ b ∈ U ×ˢ (Metric.ball 0 R \ {0}), (F b).natDegree = d)
  (hu : AnalyticOnNhd ℂ u (U ×ˢ Metric.ball 0 R)) (hu0 : ∀ b ∈ U ×ˢ Metric.ball 0 R, u b ≠ 0)
  (hv : AnalyticOnNhd ℂ v (U ×ˢ Metric.ball 0 R)) (hv0 : ∀ b ∈ U ×ˢ Metric.ball 0 R, v b ≠ 0)
  (hlead : ∀ b ∈ U ×ˢ (Metric.ball 0 R \ {0}), (F b).coeff d = b.2 ^ a * u b)
  (hdiscr : ∀ b ∈ U ×ˢ (Metric.ball 0 R \ {0}), (F b).discr = b.2 ^ c * v b) (hτ : ContinuousOn τ U)
  (hτU : Set.MapsTo τ U U) (hττ : ∀ x ∈ U, τ (τ x) = x)
  (hconj :
    ∀ b ∈ U ×ˢ (Metric.ball 0 R \ {0}),
      F (τ b.1, (starRingEnd ℂ) b.2) = Polynomial.map (starRingEnd ℂ) (F b)) :
  ∃ r g,
    (∀ (i : Fin d), AnalyticOnNhd ℂ (r i) (U ×ˢ (Metric.ball 0 R' \ {0}))) ∧
      (∀ (i : Fin d),
          AnalyticOnNhd ℂ (g i) (U ×ˢ Metric.ball 0 R') ∧
            Set.EqOn (g i) (fun b => b.2 ^ (n * a) * r i b) (U ×ˢ (Metric.ball 0 R' \ {0}))) ∧
        (∀ b ∈ U ×ˢ (Metric.ball 0 R' \ {0}),
            (Function.Injective fun i => r i b) ∧
              F (b.1, b.2 ^ n) =
                Polynomial.C ((F (b.1, b.2 ^ n)).coeff d) *
                  ∏ i, (Polynomial.X - Polynomial.C (r i b))) ∧
          ∃! σ,
            Function.Involutive ⇑σ ∧
              (∀ (i : Fin d),
                  ∀ b ∈ U ×ˢ (Metric.ball 0 R' \ {0}),
                    r (σ i) b = (starRingEnd ℂ) (r i (τ b.1, (starRingEnd ℂ) b.2))) ∧
                (∀ (i : Fin d),
                    ∀ b ∈ U ×ˢ Metric.ball 0 R',
                      g (σ i) b = (starRingEnd ℂ) (g i (τ b.1, (starRingEnd ℂ) b.2))) ∧
                  ∃ e w,
                    ∀ (i j : Fin d) (hij : i ≠ j),
                      AnalyticOnNhd ℂ (w i j hij) (U ×ˢ Metric.ball 0 R') ∧
                        (∀ b ∈ U ×ˢ Metric.ball 0 R', w i j hij b ≠ 0) ∧
                          (∀ b ∈ U ×ˢ (Metric.ball 0 R' \ {0}),
                              r i b - r j b = b.2 ^ e i j hij * w i j hij b) ∧
                            e (σ i) (σ j) ⋯ = e i j hij ∧
                              ∀ b ∈ U ×ˢ Metric.ball 0 R',
                                w (σ i) (σ j) ⋯ b =
                                  (starRingEnd ℂ) (w i j hij (τ b.1, (starRingEnd ℂ) b.2))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The analytic implicit root theorem](../../../analysis/part-03/analytic/the-analytic-implicit-root-theorem.md)
- [Hadamard's lemma along a graph](../../../analysis/part-03/analytic/hadamards-lemma-along-a-graph.md)
- [The isomorphism `π₁(S¹) ≃* ℤ` is the degree](../../../algebraic-topology/universal-covers/the-isomorphism-1-s1-z-is-the-degree.md)
- [The Riemann extension theorem across a coordinate hyperplane](../../../analysis/part-03/complex/part-04/the-riemann-extension-theorem-across-a-coordinat.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Polynomial.exists_analyticOnNhd_nonmonic_root_sub_eq_zpow_mul_unit_conj`](https://taucetiproject.org/docs/TauCeti/Analysis/Polynomial/Puiseux/RootDifference/Symmetry.html#TauCeti.Polynomial.exists_analyticOnNhd_nonmonic_root_sub_eq_zpow_mul_unit_conj).

## Sources

- [Tau Ceti documentation: `TauCeti.Polynomial.exists_analyticOnNhd_nonmonic_root_sub_eq_zpow_mul_unit_conj`](https://taucetiproject.org/docs/TauCeti/Analysis/Polynomial/Puiseux/RootDifference/Symmetry.html#TauCeti.Polynomial.exists_analyticOnNhd_nonmonic_root_sub_eq_zpow_mul_unit_conj)
- [Source of `TauCeti.Polynomial.exists_analyticOnNhd_nonmonic_root_sub_eq_zpow_mul_unit_conj` in TauCeti/Analysis/Polynomial/Puiseux/RootDifference/Symmetry.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Polynomial/Puiseux/RootDifference/Symmetry.lean#L92)
- [Tau Ceti roadmap status: Real algebraic geometry: sign determination and cylindrical decomposition](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/RealAlgebraicGeometry/STATUS.md)
