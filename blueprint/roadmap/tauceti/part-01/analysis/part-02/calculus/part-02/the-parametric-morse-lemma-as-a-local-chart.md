---
declaration: theorem
origin: cited
lean: TauCeti.exists_parametric_morse_chart, TauCeti.exists_parametricMorseCoord_chart
statement: formalized
proof: formalized
---

# The parametric Morse lemma, as a local chart

The chart has a product source containing
`(a, 0)` and is given by the canonical coordinate
`(b, v) ↦ (b, parametricMorseCoord f (b, v))`, so it preserves the base parameter and fixes the
zero section; its inverse preserves the base parameter too. Its quadratic equation uses the
vertical Hessian on that same zero section. The base and the fiber are Banach spaces, so the
ordinary inverse function theorem applies to their product.

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
              (∀ (z : P × E), ↑ψ z = (z.1, TauCeti.parametricMorseCoord f z)) ∧
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

- [The inverse function theorem, with a `C^n` inverse on the whole target](../part-01/the-inverse-function-theorem-with-a-c-n-inverse.md)
- [Taylor's formula to second order](taylors-formula-to-second-order.md)

## Informally uses

- [The local parametric Morse lemma](../part-01/the-local-parametric-morse-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_parametric_morse_chart`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Morse/Parametric.html#TauCeti.exists_parametric_morse_chart).

## Other forms

**The parametric Morse lemma along the whole zero section.** Formalized in Tau Ceti as [`TauCeti.exists_parametricMorseCoord_chart`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Morse/ZeroSectionChart.html#TauCeti.exists_parametricMorseCoord_chart).

```lean
TauCeti.exists_parametricMorseCoord_chart.{u_1, u_2} {E : Type u_1} {P : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [CompleteSpace E] [NormedAddCommGroup P]
  [NormedSpace ℝ P] [FiniteDimensional ℝ P] [FiniteDimensional ℝ E] {F : P × E → ℝ}
  {W : Set (P × E)} {U : Set P} {n : ℕ∞} (hW : IsOpen W) (hF : ContDiffOn ℝ (↑n + 2) F W)
  (hU : IsOpen U) (hUW : ∀ b ∈ U, (b, 0) ∈ W) (hcrit : ∀ b ∈ U, fderiv ℝ (fun v => F (b, v)) 0 = 0)
  (hH : ∀ b ∈ U, (fderiv ℝ (fderiv ℝ fun v => F (b, v)) 0).IsInvertible) (hn : n ≠ 0) :
  ∃ ψ,
    ψ.source ⊆ W ∧
      (∀ b ∈ U, (b, 0) ∈ ψ.source) ∧
        (∀ z ∈ ψ.source, ↑ψ z = (z.1, TauCeti.parametricMorseCoord F z)) ∧
          (∀ z ∈ ψ.target, (↑ψ.symm z).1 = z.1) ∧
            ContDiffOn ℝ (↑n) (↑ψ) ψ.source ∧
              ContDiffOn ℝ (↑n) (↑ψ.symm) ψ.target ∧
                ∀ z ∈ ψ.source,
                  F z =
                    F (z.1, 0) +
                      2⁻¹ * ((fderiv ℝ (fderiv ℝ fun v => F (z.1, v)) 0) (↑ψ z).2) (↑ψ z).2
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_parametric_morse_chart`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Morse/Parametric.html#TauCeti.exists_parametric_morse_chart)
- [Source of `TauCeti.exists_parametric_morse_chart` in TauCeti/Analysis/Calculus/Morse/Parametric.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Calculus/Morse/Parametric.lean#L360)
