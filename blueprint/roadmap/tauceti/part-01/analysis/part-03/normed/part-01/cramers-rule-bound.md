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
TauCeti.norm_det_mul_max_norm_le.{u_1} {R : Type u_1} [SeminormedCommRing R] [NormMulClass R]
  (a b a' b' x y : R) :
  ‖a * b' - b * a'‖ * max ‖x‖ ‖y‖ ≤
    (‖a‖ + ‖b‖ + ‖a'‖ + ‖b'‖) * (‖a * x + b * y‖ + ‖a' * x + b' * y‖)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.norm_det_mul_max_norm_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Ring/LinearForms.html#TauCeti.norm_det_mul_max_norm_le).

## Sources

- [Tau Ceti documentation: `TauCeti.norm_det_mul_max_norm_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Ring/LinearForms.html#TauCeti.norm_det_mul_max_norm_le)
- [Source of `TauCeti.norm_det_mul_max_norm_le` in TauCeti/Analysis/Normed/Ring/LinearForms.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Normed/Ring/LinearForms.lean#L44)
