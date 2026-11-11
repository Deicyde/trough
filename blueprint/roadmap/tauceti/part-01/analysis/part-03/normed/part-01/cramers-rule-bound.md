---
declaration: theorem
origin: cited
lean: TauCeti.norm_det_mul_max_norm_le
statement: formalized
proof: formalized
---

# Cramer's rule bound

**Cramer's rule bound** for two linear forms `L = a x + b y` and `L' = a' x + b' y` in two
variables: the determinant `D = a b' - b a'` satisfies
`‖D‖ max(‖x‖, ‖y‖) ≤ (‖a‖ + ‖b‖ + ‖a'‖ + ‖b'‖) (‖L‖ + ‖L'‖)`.

```lean
TauCeti.norm_det_mul_max_norm_le.{u_1} {𝕜 : Type u_1} [NormedField 𝕜] (a b a' b' x y : 𝕜) :
  ‖a * b' - b * a'‖ * max ‖x‖ ‖y‖ ≤
    (‖a‖ + ‖b‖ + ‖a'‖ + ‖b'‖) * (‖a * x + b * y‖ + ‖a' * x + b' * y‖)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.norm_det_mul_max_norm_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Field/LinearForms.html#TauCeti.norm_det_mul_max_norm_le).

## Sources

- [Tau Ceti documentation: `TauCeti.norm_det_mul_max_norm_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Field/LinearForms.html#TauCeti.norm_det_mul_max_norm_le)
- [Source of `TauCeti.norm_det_mul_max_norm_le` in TauCeti/Analysis/Normed/Field/LinearForms.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Field/LinearForms.lean#L47)
