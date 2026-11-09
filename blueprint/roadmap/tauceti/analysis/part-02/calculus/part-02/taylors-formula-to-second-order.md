---
declaration: theorem
origin: cited
lean: TauCeti.map_add_eq_add_hessianAverage, TauCeti.sum_add_pow_sub_smul_iterate_dslope
statement: formalized
proof: formalized
---

# Taylor's formula to second order

**Taylor's formula to second order**, with the remainder written as the averaged Hessian
evaluated twice on the increment.

```lean
TauCeti.map_add_eq_add_hessianAverage.{u, v} {E : Type u} {F : Type v} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F] [CompleteSpace F] {f : E → F}
  (hf : ContDiff ℝ 2 f) (x v : E) :
  f (x + v) = f x + (fderiv ℝ f x) v + 2⁻¹ • ((TauCeti.hessianAverage f x v) v) v
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.map_add_eq_add_hessianAverage`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Morse/NormalForm.html#TauCeti.map_add_eq_add_hessianAverage).

## Other forms

**Taylor's formula with divided-difference remainder.** Formalized in Tau Ceti as [`TauCeti.sum_add_pow_sub_smul_iterate_dslope`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/DSlope/Basic.html#TauCeti.sum_add_pow_sub_smul_iterate_dslope).

```lean
TauCeti.sum_add_pow_sub_smul_iterate_dslope.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2}
  [NontriviallyNormedField 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E] (f : 𝕜 → E) (a b : 𝕜)
  (n : ℕ) :
  ∑ j ∈ Finset.range n, (b - a) ^ j • (Function.swap dslope a)^[j] f a +
      (b - a) ^ n • (Function.swap dslope a)^[n] f b =
    f b
```

## Sources

- [Tau Ceti documentation: `TauCeti.map_add_eq_add_hessianAverage`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Morse/NormalForm.html#TauCeti.map_add_eq_add_hessianAverage)
- [Source of `TauCeti.map_add_eq_add_hessianAverage` in TauCeti/Analysis/Calculus/Morse/NormalForm.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Calculus/Morse/NormalForm.lean#L213)
