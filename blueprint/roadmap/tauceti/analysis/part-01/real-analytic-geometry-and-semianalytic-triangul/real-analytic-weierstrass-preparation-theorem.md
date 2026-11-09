---
declaration: theorem
origin: cited
lean: AnalyticAt.exists_weierstrassPreparation_real
statement: formalized
proof: formalized
---

# Real analytic Weierstrass preparation theorem

Let `f : (ι → ℝ) × ℝ → ℝ` be real analytic
at `(x₀, t₀)`, with `ι` finite, and suppose the vertical slice `t ↦ f (x₀, t)` has finite order of
vanishing `d` at `t₀`. Then there exist real analytic coefficient functions `c : Fin d → (ι → ℝ) →
ℝ` vanishing at `x₀` and a real analytic function `u` nonvanishing at `(x₀, t₀)` such that near
`(x₀, t₀)`,
`f (x, t) = (TauCeti.Polynomial.monicOfCoeff (fun i ↦ c i x)).eval (t - t₀) * u (x, t)`.

```lean
AnalyticAt.exists_weierstrassPreparation_real {ι : Type} [Fintype ι] {f : (ι → ℝ) × ℝ → ℝ}
  {x₀ : ι → ℝ} {t₀ : ℝ} {d : ℕ} (hf : AnalyticAt ℝ f (x₀, t₀))
  (hd : analyticOrderAt (fun t => f (x₀, t)) t₀ = ↑d) :
  ∃ c u,
    (∀ (i : Fin d), AnalyticAt ℝ (c i) x₀) ∧
      (∀ (i : Fin d), c i x₀ = 0) ∧
        AnalyticAt ℝ u (x₀, t₀) ∧
          u (x₀, t₀) ≠ 0 ∧
            f =ᶠ[nhds (x₀, t₀)] fun p =>
              Polynomial.eval (p.2 - t₀) (TauCeti.Polynomial.monicOfCoeff fun i => c i p.1) * u p
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Complex analytic Weierstrass preparation theorem](../../part-02/complex/part-01/complex-analytic-weierstrass-preparation-theorem.md)
- [Osgood's lemma](../../../geometry/part-01/complex-manifolds-dolbeault-theory-and-kahler-ge/osgoods-lemma.md)

## Lean

Formalized in Tau Ceti as [`AnalyticAt.exists_weierstrassPreparation_real`](https://taucetiproject.org/docs/TauCeti/Analysis/Analytic/Complexification/Weierstrass.html#AnalyticAt.exists_weierstrassPreparation_real).

## Sources

- [Tau Ceti documentation: `AnalyticAt.exists_weierstrassPreparation_real`](https://taucetiproject.org/docs/TauCeti/Analysis/Analytic/Complexification/Weierstrass.html#AnalyticAt.exists_weierstrassPreparation_real)
- [Source of `AnalyticAt.exists_weierstrassPreparation_real` in TauCeti/Analysis/Analytic/Complexification/Weierstrass.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Analytic/Complexification/Weierstrass.lean#L173)
