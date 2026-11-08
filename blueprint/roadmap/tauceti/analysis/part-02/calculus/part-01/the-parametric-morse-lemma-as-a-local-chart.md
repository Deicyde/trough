---
declaration: theorem
origin: cited
lean: TauCeti.exists_parametric_morse_chart
statement: formalized
proof: formalized
---

# The parametric Morse lemma, as a local chart

The chart has a product source containing
`(a, 0)`, preserves the base parameter in both directions, and fixes the zero section. Its
quadratic equation uses the vertical Hessian on that same zero section. The base and the fiber
are Banach spaces, so the ordinary inverse function theorem applies to their product.

```lean
TauCeti.exists_parametric_morse_chart.{u_1, u_2} {P : Type u_1} {E : Type u_2}
  [NormedAddCommGroup P] [NormedSpace ℝ P] [NormedAddCommGroup E] [NormedSpace ℝ E]
  [CompleteSpace E] {f : P × E → ℝ} {a : P} {n : ℕ∞} [CompleteSpace P] (hf : ContDiff ℝ (↑n + 2) f)
  (hcrit : ∀ᶠ (b : P) in nhds a, fderiv ℝ (fun v => f (b, v)) 0 = 0)
  (hH : (fderiv ℝ (fderiv ℝ fun v => f (a, v)) 0).IsInvertible) (hn : n ≠ 0) :
  ∃ ψ U V,
    IsOpen U ∧
      IsOpen V ∧
        a ∈ U ∧
          0 ∈ V ∧
            ψ.source = U ×ˢ V ∧
              (∀ (z : P × E), (↑ψ z).1 = z.1) ∧
                (∀ (b : P), ↑ψ (b, 0) = (b, 0)) ∧
                  (∀ z ∈ ψ.target, (↑ψ.symm z).1 = z.1) ∧
                    ContDiffOn ℝ (↑n) (↑ψ) ψ.source ∧
                      ContDiffOn ℝ (↑n) (↑ψ.symm) ψ.target ∧
                        ∀ z ∈ ψ.source,
                          f z =
                            f (z.1, 0) +
                              2⁻¹ * ((fderiv ℝ (fderiv ℝ fun v => f (z.1, v)) 0) (↑ψ z).2) (↑ψ z).2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The inverse function theorem produces a `C^n` inverse](the-inverse-function-theorem-produces-a-c-n-inve.md)
- [Taylor's formula to second order](../part-02/taylors-formula-to-second-order.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_parametric_morse_chart`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Morse/Parametric.html#TauCeti.exists_parametric_morse_chart).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_parametric_morse_chart`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Morse/Parametric.html#TauCeti.exists_parametric_morse_chart)
- [Source of `TauCeti.exists_parametric_morse_chart` in TauCeti/Analysis/Calculus/Morse/Parametric.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Calculus/Morse/Parametric.lean#L96)
