---
declaration: theorem
origin: cited
lean: TauCeti.norm_springForce
statement: formalized
proof: formalized
---

# Hooke's law

Away from zero length, `‖w‖ ≠ 0`, the force of a spring has magnitude `|κ|`
times the deviation `|‖w‖ - ℓ₀|` of its length from the rest length.

```lean
TauCeti.norm_springForce.{u_1} {E : Type u_1} [SeminormedAddCommGroup E] [NormedSpace ℝ E]
  (κ ℓ₀ : ℝ) {w : E} (hw : ‖w‖ ≠ 0) : ‖TauCeti.springForce κ ℓ₀ w‖ = |κ| * |‖w‖ - ℓ₀|
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.norm_springForce`](https://taucetiproject.org/docs/TauCeti/Analysis/SpringSystem/Basic.html#TauCeti.norm_springForce).

## Sources

- [Tau Ceti documentation: `TauCeti.norm_springForce`](https://taucetiproject.org/docs/TauCeti/Analysis/SpringSystem/Basic.html#TauCeti.norm_springForce)
- [Source of `TauCeti.norm_springForce` in TauCeti/Analysis/SpringSystem/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/SpringSystem/Basic.lean#L116)
