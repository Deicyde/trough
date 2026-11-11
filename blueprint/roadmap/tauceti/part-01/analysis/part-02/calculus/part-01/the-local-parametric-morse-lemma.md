---
declaration: theorem
origin: cited
lean: TauCeti.exists_parametric_morse_chart_of_contDiffOn
statement: formalized
proof: formalized
---

# The local parametric Morse lemma

If a family `f (b, v)` is `C^{n+2}` on a neighbourhood
`W` of `(b₀, 0)`, with `1 ≤ n ≤ ∞`, its zero section is critical in the fibre direction near
`b₀`, and its vertical Hessian at `b₀` is invertible, then there is a `C^n` chart `ψ` with
product source in `W`, given on its source by the canonical coordinate
`(b, v) ↦ (b, parametricMorseCoord f (b, v))`, preserving the base parameter in both directions
and fixing the zero section, on whose source `f` is its value on the zero section plus half the
vertical Hessian read in the chart.

```lean
TauCeti.exists_parametric_morse_chart_of_contDiffOn.{u_2, u_3} {n : ℕ∞} {P : Type u_2}
  {F : Type u_3} [NormedAddCommGroup P] [NormedSpace ℝ P] [FiniteDimensional ℝ P]
  [NormedAddCommGroup F] [NormedSpace ℝ F] [FiniteDimensional ℝ F] {f : P × F → ℝ} {b₀ : P}
  {W : Set (P × F)} (hW : W ∈ nhds (b₀, 0)) (hf : ContDiffOn ℝ (↑n + 2) f W)
  (hcrit : ∀ᶠ (b : P) in nhds b₀, fderiv ℝ (fun v => f (b, v)) 0 = 0)
  (hH : (fderiv ℝ (fderiv ℝ fun v => f (b₀, v)) 0).IsInvertible) (hn : n ≠ 0) :
  ∃ ψ U V,
    IsOpen U ∧
      IsOpen V ∧
        b₀ ∈ U ∧
          0 ∈ V ∧
            ψ.source = U ×ˢ V ∧
              U ×ˢ V ⊆ W ∧
                (∀ z ∈ ψ.source, ↑ψ z = (z.1, TauCeti.parametricMorseCoord f z)) ∧
                  (∀ (z : P × F), (↑ψ z).1 = z.1) ∧
                    (∀ (b : P), ↑ψ (b, 0) = (b, 0)) ∧
                      (∀ z ∈ ψ.target, (↑ψ.symm z).1 = z.1) ∧
                        ContDiffOn ℝ (↑n) (↑ψ) ψ.source ∧
                          ContDiffOn ℝ (↑n) (↑ψ.symm) ψ.target ∧
                            ∀ z ∈ ψ.source,
                              f z =
                                f (z.1, 0) +
                                  2⁻¹ *
                                    ((fderiv ℝ (fderiv ℝ fun v => f (z.1, v)) 0) (↑ψ z).2) (↑ψ z).2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The parametric Morse lemma, as a local chart](../part-02/the-parametric-morse-lemma-as-a-local-chart.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_parametric_morse_chart_of_contDiffOn`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Morse/LocalNormalForm.html#TauCeti.exists_parametric_morse_chart_of_contDiffOn).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_parametric_morse_chart_of_contDiffOn`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Morse/LocalNormalForm.html#TauCeti.exists_parametric_morse_chart_of_contDiffOn)
- [Source of `TauCeti.exists_parametric_morse_chart_of_contDiffOn` in TauCeti/Analysis/Calculus/Morse/LocalNormalForm.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Calculus/Morse/LocalNormalForm.lean#L85)
