---
declaration: theorem
origin: cited
lean: TauCeti.exists_contDiffOn_holderOnWith_fderiv_pi_inv_smul_integral_sub_inv_smul
statement: formalized
proof: formalized
---

# TauCeti.exists_contDiffOn_holderOnWith_fderiv_pi_inv_smul_integral_sub_inv_smul

For finite-dimensional complex normed targets, the actual Cauchy integral is `C¹` near
an output disc, its real derivative has a uniform supremum and Hölder bound, and it solves
`conjWirtingerDeriv T x 1 = f x`. The constant depends only on the target norm, exponent and
the two fixed discs.
The compatible real scalar action remains a parameter because it determines the derivative's
continuous-linear-map carrier.

```lean
TauCeti.exists_contDiffOn_holderOnWith_fderiv_pi_inv_smul_integral_sub_inv_smul.{u_1} {F : Type u_1}
  [NormedAddCommGroup F] [NormedSpace ℂ F] [NormedSpace ℝ F] [IsScalarTower ℝ ℂ F]
  [FiniteDimensional ℂ F] {α : NNReal} (hα : 0 < α) (hα1 : α < 1) (c : ℂ) {r R : ℝ} (hr : 0 ≤ r)
  (hR : 0 ≤ R) :
  ∃ C,
    ∀ {f : ℂ → F} {H M : NNReal},
      Function.support f ⊆ Metric.closedBall c r →
        HolderWith H α f →
          (∀ (x : ℂ), ‖f x‖ ≤ ↑M) →
            have T := fun w => (↑Real.pi)⁻¹ • ∫ (z : ℂ), (w - z)⁻¹ • f z;
            ContDiffOn ℝ 1 T (Metric.ball c (R + 1)) ∧
              HolderOnWith (C * (H + M)) α (fderiv ℝ T) (Metric.closedBall c R) ∧
                (∀ x ∈ Metric.closedBall c R, ‖fderiv ℝ T x‖ ≤ ↑C * (↑H + ↑M)) ∧
                  ∀ x ∈ Metric.ball c (R + 1), (TauCeti.conjWirtingerDeriv T x) 1 = f x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Cauchy–Pompeiu formula for a compactly supported `C¹` map `u : ℂ → F`](the-cauchy-pompeiu-formula-for-a-compactly-suppo.md)
- [The global Schauder estimate on the whole space](../../part-03/pde/part-01/the-global-schauder-estimate-on-the-whole-space.md)
- [Radial fundamental theorem of calculus](../../../measure-theory/constructions/radial-fundamental-theorem-of-calculus.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_contDiffOn_holderOnWith_fderiv_pi_inv_smul_integral_sub_inv_smul`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Pompeiu/Holder/Gain.html#TauCeti.exists_contDiffOn_holderOnWith_fderiv_pi_inv_smul_integral_sub_inv_smul).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_contDiffOn_holderOnWith_fderiv_pi_inv_smul_integral_sub_inv_smul`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Pompeiu/Holder/Gain.html#TauCeti.exists_contDiffOn_holderOnWith_fderiv_pi_inv_smul_integral_sub_inv_smul)
- [Source of `TauCeti.exists_contDiffOn_holderOnWith_fderiv_pi_inv_smul_integral_sub_inv_smul` in TauCeti/Analysis/Complex/Pompeiu/Holder/Gain.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/Pompeiu/Holder/Gain.lean#L364)
- [Tau Ceti roadmap status: Elliptic analysis of pseudoholomorphic curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PseudoholomorphicCurveAnalysis/STATUS.md)
