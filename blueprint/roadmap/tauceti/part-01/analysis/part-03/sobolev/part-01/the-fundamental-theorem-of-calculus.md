---
declaration: theorem
origin: cited
lean: TauCeti.WeakDerivStep.integral_weakFDeriv_apply_one_eq_sub
statement: formalized
proof: formalized
---

# The fundamental theorem of calculus

The integrals of the weak derivative of a path are
the increments of its continuous representative.

```lean
TauCeti.WeakDerivStep.integral_weakFDeriv_apply_one_eq_sub.{u_1} {F : Type u_1}
  [NormedAddCommGroup F] [NormedSpace ℝ F] [CompleteSpace F] {p : ENNReal} [Fact (1 ≤ p)]
  (hp : p ≠ ⊤)
  (u :
    ↥(TauCeti.WeakDerivStep MeasureTheory.volume ⊤ p
        (ContinuousLinearMap.id ℝ ↥(MeasureTheory.Lp F p (MeasureTheory.volume.restrict ↑⊤)))))
  (s t : ℝ) :
  ∫ (r : ℝ) in s..t,
      (↑↑(TauCeti.WeakDerivStep.weakFDeriv
                (ContinuousLinearMap.id ℝ
                  ↥(MeasureTheory.Lp F p (MeasureTheory.volume.restrict ↑⊤)))
                u)
          r)
        1 =
    ((TauCeti.WeakDerivStep.toZeroAtInfty hp) u) t - ((TauCeti.WeakDerivStep.toZeroAtInfty hp) u) s
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The fundamental theorem of calculus for a continuous representative](the-fundamental-theorem-of-calculus-for-a-contin.md)
- [The fundamental theorem of calculus for weak derivatives on the line](the-fundamental-theorem-of-calculus-for-weak-der-2.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.WeakDerivStep.integral_weakFDeriv_apply_one_eq_sub`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/GraphStep/ZeroAtInfty.html#TauCeti.WeakDerivStep.integral_weakFDeriv_apply_one_eq_sub).

## Sources

- [Tau Ceti documentation: `TauCeti.WeakDerivStep.integral_weakFDeriv_apply_one_eq_sub`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/GraphStep/ZeroAtInfty.html#TauCeti.WeakDerivStep.integral_weakFDeriv_apply_one_eq_sub)
- [Source of `TauCeti.WeakDerivStep.integral_weakFDeriv_apply_one_eq_sub` in TauCeti/Analysis/Sobolev/GraphStep/ZeroAtInfty.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Sobolev/GraphStep/ZeroAtInfty.lean#L296)
