---
declaration: theorem
origin: cited
lean: TauCeti.sq_norm_sub_sub_mul_sq_norm_one_sub_conj_mul
statement: formalized
proof: formalized
---

# The Apollonius identity for the Moebius factor

For every `z : ℂ`,

`‖z - a‖ ^ 2 - t ^ 2 * ‖1 - conj a * z‖ ^ 2`
`  = (1 - t ^ 2 * ‖a‖ ^ 2)`
`      * (‖z - pseudoHyperbolicCenter a t‖ ^ 2 - pseudoHyperbolicRadius a t ^ 2)`.

Both sides are real quadratics in `z.re` and `z.im` with the same leading coefficient
`1 - t ^ 2 * ‖a‖ ^ 2`, and the definitions of `TauCeti.pseudoHyperbolicCenter` and
`TauCeti.pseudoHyperbolicRadius` are exactly what completes the square. No hypothesis is placed on
`z`, and the disc hypothesis on `a` enters only through the nonvanishing of the denominator.

```lean
TauCeti.sq_norm_sub_sub_mul_sq_norm_one_sub_conj_mul (a z : ℂ) (t : ℝ)
  (hD : 1 - t ^ 2 * ‖a‖ ^ 2 ≠ 0) :
  ‖z - a‖ ^ 2 - t ^ 2 * ‖1 - (starRingEnd ℂ) a * z‖ ^ 2 =
    (1 - t ^ 2 * ‖a‖ ^ 2) *
      (‖z - TauCeti.pseudoHyperbolicCenter a t‖ ^ 2 - TauCeti.pseudoHyperbolicRadius a t ^ 2)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.sq_norm_sub_sub_mul_sq_norm_one_sub_conj_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Poincare/Ball.html#TauCeti.sq_norm_sub_sub_mul_sq_norm_one_sub_conj_mul).

## Sources

- [Tau Ceti documentation: `TauCeti.sq_norm_sub_sub_mul_sq_norm_one_sub_conj_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Poincare/Ball.html#TauCeti.sq_norm_sub_sub_mul_sq_norm_one_sub_conj_mul)
- [Source of `TauCeti.sq_norm_sub_sub_mul_sq_norm_one_sub_conj_mul` in TauCeti/Analysis/Complex/Conformal/Poincare/Ball.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/Conformal/Poincare/Ball.lean#L304)
