---
declaration: theorem
origin: cited
lean: ContinuousOn.monotoneOn_of_integral_deriv_mul_nonpos
statement: formalized
proof: formalized
---

# The monotone du Bois-Reymond lemma

A real function continuous on an open interval whose
distributional derivative is nonnegative, in the sense that `∫ x, deriv ψ x * f x ≤ 0` for every
nonnegative test function `ψ` on the interval, is monotone on the interval.

```lean
ContinuousOn.monotoneOn_of_integral_deriv_mul_nonpos {a b : ℝ} {f : ℝ → ℝ}
  (hf : ContinuousOn f (Set.Ioo a b))
  (h :
    ∀ (ψ : ℝ → ℝ),
      ContDiff ℝ (↑⊤) ψ →
        tsupport ψ ⊆ Set.Ioo a b → (∀ (x : ℝ), 0 ≤ ψ x) → ∫ (x : ℝ), deriv ψ x * f x ≤ 0) :
  MonotoneOn f (Set.Ioo a b)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContinuousOn.monotoneOn_of_integral_deriv_mul_nonpos`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/DuBoisReymond.html#ContinuousOn.monotoneOn_of_integral_deriv_mul_nonpos).

## Sources

- [Tau Ceti documentation: `ContinuousOn.monotoneOn_of_integral_deriv_mul_nonpos`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/DuBoisReymond.html#ContinuousOn.monotoneOn_of_integral_deriv_mul_nonpos)
- [Source of `ContinuousOn.monotoneOn_of_integral_deriv_mul_nonpos` in TauCeti/Analysis/Distribution/DuBoisReymond.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Distribution/DuBoisReymond.lean#L279)
