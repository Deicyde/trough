---
declaration: theorem
origin: cited
lean: TauCeti.LinearPMap.resolvent_eq_mul_inverse_one_sub
statement: formalized
proof: formalized
---

# Local Neumann formula for the resolvent

Inside the ball
`‖mu - lambda‖ * ‖R(lambda)‖ < 1`, the resolvent at `mu` is obtained by multiplying
`R(lambda)` by the ring inverse of `1 - (lambda - mu) R(lambda)`.

```lean
TauCeti.LinearPMap.resolvent_eq_mul_inverse_one_sub.{u_1, u_2} {𝕜 : Type u_1} {X : Type u_2}
  [NontriviallyNormedField 𝕜] [NormedAddCommGroup X] [NormedSpace 𝕜 X]
  [HasSummableGeomSeries (X →L[𝕜] X)] {A : X →ₗ.[𝕜] X} {lambda mu : 𝕜} (h : lambda ∈ A.resolventSet)
  (hmu : ‖mu - lambda‖ * ‖A.resolvent lambda‖ < 1) :
  A.resolvent mu = A.resolvent lambda * Ring.inverse (1 - (lambda - mu) • A.resolvent lambda)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.LinearPMap.resolvent_eq_mul_inverse_one_sub`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Resolvent/Unbounded.html#TauCeti.LinearPMap.resolvent_eq_mul_inverse_one_sub).

## Sources

- [Tau Ceti documentation: `TauCeti.LinearPMap.resolvent_eq_mul_inverse_one_sub`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Resolvent/Unbounded.html#TauCeti.LinearPMap.resolvent_eq_mul_inverse_one_sub)
- [Source of `TauCeti.LinearPMap.resolvent_eq_mul_inverse_one_sub` in TauCeti/Analysis/Normed/Operator/Resolvent/Unbounded.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Operator/Resolvent/Unbounded.lean#L74)
