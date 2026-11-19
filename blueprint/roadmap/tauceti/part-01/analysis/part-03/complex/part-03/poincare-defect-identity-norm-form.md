---
declaration: theorem
origin: cited
lean: TauCeti.norm_sq_one_sub_conj_mul_sub_norm_sq_sub
statement: formalized
proof: formalized
---

# Poincaré defect identity (norm form)

The difference of the squared norms of the Moebius
denominator and numerator factors is the product of the two hyperbolic defects:
`‖1 - conj w * z‖ ^ 2 - ‖z - w‖ ^ 2 = (1 - ‖z‖ ^ 2) * (1 - ‖w‖ ^ 2)`.

```lean
TauCeti.norm_sq_one_sub_conj_mul_sub_norm_sq_sub (z w : ℂ) :
  ‖1 - (starRingEnd ℂ) w * z‖ ^ 2 - ‖z - w‖ ^ 2 = (1 - ‖z‖ ^ 2) * (1 - ‖w‖ ^ 2)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.norm_sq_one_sub_conj_mul_sub_norm_sq_sub`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/PseudoHyperbolic.html#TauCeti.norm_sq_one_sub_conj_mul_sub_norm_sq_sub).

## Sources

- [Tau Ceti documentation: `TauCeti.norm_sq_one_sub_conj_mul_sub_norm_sq_sub`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/PseudoHyperbolic.html#TauCeti.norm_sq_one_sub_conj_mul_sub_norm_sq_sub)
- [Source of `TauCeti.norm_sq_one_sub_conj_mul_sub_norm_sq_sub` in TauCeti/Analysis/Complex/Conformal/PseudoHyperbolic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/Conformal/PseudoHyperbolic.lean#L192)
