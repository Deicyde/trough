---
declaration: theorem
origin: cited
lean: Convex.injOn_of_re_mul_deriv_pos
statement: formalized
proof: formalized
---

# Noshiro--Warschawski criterion

A function on a convex set is injective if a fixed
multiple of its derivative has strictly positive real part throughout the set.

```lean
Convex.injOn_of_re_mul_deriv_pos.{u_1} {𝕜 : Type u_1} [RCLike 𝕜] {U : Set 𝕜} (hU : Convex ℝ U)
  {f : 𝕜 → 𝕜} (c : 𝕜) (hf : ∀ z ∈ U, 0 < RCLike.re (c * deriv f z)) : Set.InjOn f U
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Convex.injOn_of_re_mul_deriv_pos`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Deriv/InjOn.html#Convex.injOn_of_re_mul_deriv_pos).

## Sources

- [Tau Ceti documentation: `Convex.injOn_of_re_mul_deriv_pos`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Deriv/InjOn.html#Convex.injOn_of_re_mul_deriv_pos)
- [Source of `Convex.injOn_of_re_mul_deriv_pos` in TauCeti/Analysis/Calculus/Deriv/InjOn.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Calculus/Deriv/InjOn.lean#L29)
