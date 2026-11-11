---
declaration: theorem
origin: cited
lean: Distribution.tendsto_integral_smul_cauchyTransform_sub
statement: formalized
proof: formalized
---

# The Sokhotski–Plemelj formula

Let `u` be a complex-valued distribution on `ℝ` and `χ` a
real test function equal to one near the support of `u` (so that `u` has compact support). Then
`u` is the difference of the boundary values of its Cauchy transform `C` from the upper and the
lower half-plane: for every real test function `φ`,

`∫ φ(x) (C(x + iε) - C(x - iε)) dx → u φ` as `ε → 0⁺`.

```lean
Distribution.tendsto_integral_smul_cauchyTransform_sub (u : Distribution ⊤ ℂ ⊤)
  {χ : TestFunction ⊤ ℝ ⊤} (hχ : ∀ᶠ (t : ℝ) in nhdsSet (Distribution.dsupport ⇑u), χ t = 1)
  (φ : TestFunction ⊤ ℝ ⊤) :
  Filter.Tendsto
    (fun ε =>
      ∫ (x : ℝ),
        φ x •
          (u.cauchyTransform χ (↑x + ↑ε * Complex.I) - u.cauchyTransform χ (↑x - ↑ε * Complex.I)))
    (nhdsWithin 0 (Set.Ioi 0)) (nhds (u φ))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [A distribution has finite order on each compact set](../../part-01/integral-currents-geometric-homology-and-minimiz/a-distribution-has-finite-order-on-each-compact.md)
- [The derivative of a regularization](../../part-01/integral-currents-geometric-homology-and-minimiz/the-derivative-of-a-regularization.md)
- [Uniform first-order Taylor estimate in a parameter](../../part-02/calculus/part-02/uniform-first-order-taylor-estimate-in-a-paramet.md)

## Lean

Formalized in Tau Ceti as [`Distribution.tendsto_integral_smul_cauchyTransform_sub`](https://taucetiproject.org/docs/TauCeti/Analysis/Hyperfunction/Plemelj.html#Distribution.tendsto_integral_smul_cauchyTransform_sub).

## Sources

- [Tau Ceti documentation: `Distribution.tendsto_integral_smul_cauchyTransform_sub`](https://taucetiproject.org/docs/TauCeti/Analysis/Hyperfunction/Plemelj.html#Distribution.tendsto_integral_smul_cauchyTransform_sub)
- [Source of `Distribution.tendsto_integral_smul_cauchyTransform_sub` in TauCeti/Analysis/Hyperfunction/Plemelj.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Hyperfunction/Plemelj.lean#L257)
