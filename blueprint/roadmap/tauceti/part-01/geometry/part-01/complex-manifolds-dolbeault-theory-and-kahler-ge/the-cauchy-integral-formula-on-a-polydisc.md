---
declaration: theorem
origin: cited
lean: DifferentiableOn.torusIntegral_prod_sub_inv_smul, ContinuousOn.torusIntegral_prod_sub_inv_smul
statement: formalized
proof: formalized
---

# The Cauchy integral formula on a polydisc

If `f` is complex differentiable on the closed
polydisc with center `c` and polyradius `R`, then for every `w` in the open polydisc, the integral
of `(∏ i, (z i - w i))⁻¹ • f z` over the distinguished boundary `T(c, R)` is `(2πi)ⁿ • f w`.

```lean
DifferentiableOn.torusIntegral_prod_sub_inv_smul.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℂ E] {n : ℕ} [CompleteSpace E] {f : (Fin n → ℂ) → E} {c w : Fin n → ℂ}
  {R : Fin n → ℝ} (hd : DifferentiableOn ℂ f (Set.univ.pi fun i => Metric.closedBall (c i) (R i)))
  (hw : w ∈ Set.univ.pi fun i => Metric.ball (c i) (R i)) :
  (∯ (z : Fin n → ℂ) in T(c, R), (∏ i, (z i - w i))⁻¹ • f z) = (2 * ↑Real.pi * Complex.I) ^ n • f w
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`DifferentiableOn.torusIntegral_prod_sub_inv_smul`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/CauchyIntegralPolydisc.html#DifferentiableOn.torusIntegral_prod_sub_inv_smul).

## Other forms

**The Cauchy integral formula on a polydisc, for separately holomorphic functions.** Formalized in Tau Ceti as [`ContinuousOn.torusIntegral_prod_sub_inv_smul`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/CauchyIntegralPolydisc.html#ContinuousOn.torusIntegral_prod_sub_inv_smul).

```lean
ContinuousOn.torusIntegral_prod_sub_inv_smul.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℂ E] {n : ℕ} [CompleteSpace E] {f : (Fin n → ℂ) → E} {c w : Fin n → ℂ}
  {R : Fin n → ℝ} (hc : ContinuousOn f (Set.univ.pi fun i => Metric.closedBall (c i) (R i)))
  (hd :
    ∀ z ∈ Set.univ.pi fun i => Metric.closedBall (c i) (R i),
      ∀ (i : Fin n),
        z i ∈ Metric.ball (c i) (R i) →
          DifferentiableAt ℂ (fun x => f (Function.update z i x)) (z i))
  (hw : w ∈ Set.univ.pi fun i => Metric.ball (c i) (R i)) :
  (∯ (z : Fin n → ℂ) in T(c, R), (∏ i, (z i - w i))⁻¹ • f z) = (2 * ↑Real.pi * Complex.I) ^ n • f w
```

## Sources

- [Tau Ceti documentation: `DifferentiableOn.torusIntegral_prod_sub_inv_smul`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/CauchyIntegralPolydisc.html#DifferentiableOn.torusIntegral_prod_sub_inv_smul)
- [Source of `DifferentiableOn.torusIntegral_prod_sub_inv_smul` in TauCeti/Analysis/Complex/CauchyIntegralPolydisc.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/CauchyIntegralPolydisc.lean#L212)
