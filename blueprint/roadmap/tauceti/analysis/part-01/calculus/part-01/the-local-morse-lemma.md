---
declaration: theorem
origin: cited
lean: TauCeti.IsNondegenerateCriticalPoint.exists_morse_chart_of_contDiffOn
statement: formalized
proof: formalized
---

# The local Morse lemma

If `g` is `C^{n+2}` on a
neighbourhood `U` of a nondegenerate critical point `a`, with `1 ≤ n ≤ ∞`, there is a chart `ψ`
with source in `U`, sending `a` to `0`, `C^n` in both directions, on whose source `g` is its
Hessian quadratic form read in the chart.

```lean
TauCeti.IsNondegenerateCriticalPoint.exists_morse_chart_of_contDiffOn.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {g : E → ℝ} {a : E} {U : Set E}
  {n : ℕ∞} (hU : U ∈ nhds a) (hg : ContDiffOn ℝ (↑n + 2) g U)
  (h : TauCeti.IsNondegenerateCriticalPoint g a) (hn : n ≠ 0) :
  ∃ ψ,
    ψ.source ⊆ U ∧
      a ∈ ψ.source ∧
        ↑ψ a = 0 ∧
          ContDiffOn ℝ (↑n) (↑ψ) ψ.source ∧
            ContDiffOn ℝ (↑n) (↑ψ.symm) ψ.target ∧
              ∀ y ∈ ψ.source, g y = g a + 2⁻¹ * ((fderiv ℝ (fderiv ℝ g) a) (↑ψ y)) (↑ψ y)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Morse lemma](the-morse-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsNondegenerateCriticalPoint.exists_morse_chart_of_contDiffOn`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Morse/LocalNormalForm.html#TauCeti.IsNondegenerateCriticalPoint.exists_morse_chart_of_contDiffOn).

## Sources

- [Tau Ceti documentation: `TauCeti.IsNondegenerateCriticalPoint.exists_morse_chart_of_contDiffOn`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Morse/LocalNormalForm.html#TauCeti.IsNondegenerateCriticalPoint.exists_morse_chart_of_contDiffOn)
- [Source of `TauCeti.IsNondegenerateCriticalPoint.exists_morse_chart_of_contDiffOn` in TauCeti/Analysis/Calculus/Morse/LocalNormalForm.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Calculus/Morse/LocalNormalForm.lean#L43)
