---
declaration: theorem
origin: cited
lean: DiscreteConvolution.tsum_addRingConvolution_sq_le, DiscreteConvolution.tsum_addRingConvolution_sq_le'
statement: formalized
proof: formalized
---

# Young's inequality

**Young's inequality** `‖f ⋆ g‖₂ ≤ ‖g‖₁ ‖f‖₂` for families in `ℝ≥0∞` on an additive group,
in squared form. No summability hypotheses are needed.

```lean
DiscreteConvolution.tsum_addRingConvolution_sq_le.{u_1} {G : Type u_1} [AddGroup G]
  (f g : G → ENNReal) :
  ∑' (x : G), DiscreteConvolution.addRingConvolution f g x ^ 2 ≤
    (∑' (x : G), g x) ^ 2 * ∑' (x : G), f x ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hölder's inequality for unconditional sums in `ℝ≥0∞`](../../mean-inequalities/holders-inequality-for-unconditional-sums-in-r0.md)

## Lean

Formalized in Tau Ceti as [`DiscreteConvolution.tsum_addRingConvolution_sq_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Lp/DiscreteConvolution.html#DiscreteConvolution.tsum_addRingConvolution_sq_le).

## Other forms

**Young's inequality.** Formalized in Tau Ceti as [`DiscreteConvolution.tsum_addRingConvolution_sq_le'`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Lp/DiscreteConvolution.html#DiscreteConvolution.tsum_addRingConvolution_sq_le').

```lean
DiscreteConvolution.tsum_addRingConvolution_sq_le'.{u_1} {G : Type u_1} [AddGroup G]
  (f g : G → ENNReal) :
  ∑' (x : G), DiscreteConvolution.addRingConvolution f g x ^ 2 ≤
    (∑' (x : G), f x) ^ 2 * ∑' (x : G), g x ^ 2
```

## Sources

- [Tau Ceti documentation: `DiscreteConvolution.tsum_addRingConvolution_sq_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Lp/DiscreteConvolution.html#DiscreteConvolution.tsum_addRingConvolution_sq_le)
- [Source of `DiscreteConvolution.tsum_addRingConvolution_sq_le` in TauCeti/Analysis/Normed/Lp/DiscreteConvolution.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Lp/DiscreteConvolution.lean#L102)
