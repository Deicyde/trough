---
declaration: theorem
origin: cited
lean: TauCeti.morera
statement: formalized
proof: formalized
---

# Morera's theorem

A continuous function with values in a complex Banach space, defined on
an open set of `ℂ` and conservative there (its integrals over the boundaries of rectangles in the
set vanish), is complex differentiable on that set.

```lean
TauCeti.morera.{u_1} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℂ E] [CompleteSpace E]
  {U : Set ℂ} {f : ℂ → E} (hU : IsOpen U) (hcont : ContinuousOn f U)
  (hcons : Complex.IsConservativeOn f U) : DifferentiableOn ℂ f U
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.morera`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Morera.html#TauCeti.morera).

## Sources

- [Tau Ceti documentation: `TauCeti.morera`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Morera.html#TauCeti.morera)
- [Source of `TauCeti.morera` in TauCeti/Analysis/Complex/Conformal/Morera.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/Conformal/Morera.lean#L37)
