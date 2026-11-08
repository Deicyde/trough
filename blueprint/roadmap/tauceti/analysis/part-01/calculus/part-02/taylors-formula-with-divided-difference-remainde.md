---
declaration: theorem
origin: cited
lean: TauCeti.sum_add_pow_sub_smul_iterate_dslope, TauCeti.map_add_eq_add_hessianAverage
statement: formalized
proof: formalized
---

# Taylor's formula with divided-difference remainder

For every function `f` and every `n`,
`f b = Σ_{j<n} (b - a)^j • c_j + (b - a)^n • q_n b`, where `c_j = (swap dslope a)^[j] f a` and
`q_n = (swap dslope a)^[n] f`. This is `n` applications of `f b = f a + (b - a) • dslope f a b`.
When the `c_j` vanish this is Mathlib's `pow_sub_smul_iterate_dslope_of_zero`.

```lean
TauCeti.sum_add_pow_sub_smul_iterate_dslope.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2}
  [NontriviallyNormedField 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E] (f : 𝕜 → E) (a b : 𝕜)
  (n : ℕ) :
  ∑ j ∈ Finset.range n, (b - a) ^ j • (Function.swap dslope a)^[j] f a +
      (b - a) ^ n • (Function.swap dslope a)^[n] f b =
    f b
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.sum_add_pow_sub_smul_iterate_dslope`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/DSlope/Basic.html#TauCeti.sum_add_pow_sub_smul_iterate_dslope).

## Other forms

**Taylor's formula to second order, with the remainder written as the averaged Hessian evaluated twice on the increment.** Formalized in Tau Ceti as [`TauCeti.map_add_eq_add_hessianAverage`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Morse/NormalForm.html#TauCeti.map_add_eq_add_hessianAverage).

```lean
TauCeti.map_add_eq_add_hessianAverage.{u, v} {E : Type u} {F : Type v} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F] [CompleteSpace F] {f : E → F}
  (hf : ContDiff ℝ 2 f) (x v : E) :
  f (x + v) = f x + (fderiv ℝ f x) v + 2⁻¹ • ((TauCeti.hessianAverage f x v) v) v
```

## Sources

- [Tau Ceti documentation: `TauCeti.sum_add_pow_sub_smul_iterate_dslope`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/DSlope/Basic.html#TauCeti.sum_add_pow_sub_smul_iterate_dslope)
- [Source of `TauCeti.sum_add_pow_sub_smul_iterate_dslope` in TauCeti/Analysis/Calculus/DSlope/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Calculus/DSlope/Basic.lean#L56)
