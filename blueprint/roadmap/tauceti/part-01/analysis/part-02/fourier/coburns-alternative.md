---
declaration: theorem
origin: cited
lean: TauCeti.ker_toeplitz_eq_bot_or_ker_adjoint_toeplitz_eq_bot
statement: formalized
proof: formalized
---

# Coburn's alternative

For a nonzero essentially bounded symbol `a`, either the Toeplitz
operator `T_a` or its adjoint has trivial kernel.

```lean
TauCeti.ker_toeplitz_eq_bot_or_ker_adjoint_toeplitz_eq_bot
  {a : ↥(MeasureTheory.Lp ℂ ⊤ AddCircle.haarAddCircle)} (ha : a ≠ 0) :
  (↑(TauCeti.toeplitz a)).ker = ⊥ ∨ (↑(ContinuousLinearMap.adjoint (TauCeti.toeplitz a))).ker = ⊥
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Fatou's lemma on circles](../../part-03/special-functions/fatous-lemma-on-circles.md)
- [Jensen's inequality from below](../complex/part-02/jensens-inequality-from-below.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ker_toeplitz_eq_bot_or_ker_adjoint_toeplitz_eq_bot`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/Hardy/Coburn.html#TauCeti.ker_toeplitz_eq_bot_or_ker_adjoint_toeplitz_eq_bot).

## Sources

- [Tau Ceti documentation: `TauCeti.ker_toeplitz_eq_bot_or_ker_adjoint_toeplitz_eq_bot`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/Hardy/Coburn.html#TauCeti.ker_toeplitz_eq_bot_or_ker_adjoint_toeplitz_eq_bot)
- [Source of `TauCeti.ker_toeplitz_eq_bot_or_ker_adjoint_toeplitz_eq_bot` in TauCeti/Analysis/Fourier/Hardy/Coburn.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Fourier/Hardy/Coburn.lean#L106)
