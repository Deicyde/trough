---
declaration: theorem
origin: cited
lean: TauCeti.exists_normalized_morseBott_chart_of_contDiffOn
statement: formalized
proof: formalized
---

# The normalized Morse–Bott lemma in product coordinates

Under the hypotheses of
`TauCeti.exists_morseBott_chart_of_contDiffOn`, there is a `C^n` chart `ψ` from a product
neighbourhood `U ×ˢ V ⊆ W` of `(a, 0)` onto an open subset of `P × ℝᵐ`, `m = dim F`, preserving
the base parameter in both directions and fixing the zero section, in which

`f z = f (a, 0) - Σ_{i < λ} (ψ z).2ᵢ² + Σ_{i ≥ λ} (ψ z).2ᵢ²`

on the whole source, where `λ` is the Morse index of `f` at `(a, 0)`.

```lean
TauCeti.exists_normalized_morseBott_chart_of_contDiffOn.{u_1, u_2} {P : Type u_1} {F : Type u_2}
  [NormedAddCommGroup P] [NormedSpace ℝ P] [NormedAddCommGroup F] [NormedSpace ℝ F] {f : P × F → ℝ}
  {a : P} [FiniteDimensional ℝ P] [FiniteDimensional ℝ F] {W : Set (P × F)} {n : ℕ∞}
  (hW : W ∈ nhds (a, 0)) (hf : ContDiffOn ℝ (↑n + 2) f W)
  (hcrit : ∀ᶠ (b : P) in nhds a, fderiv ℝ f (b, 0) = 0)
  (hker : (↑(fderiv ℝ (fderiv ℝ f) (a, 0))).ker ≤ (LinearMap.inl ℝ P F).range) (hn : n ≠ 0) :
  ∃ ψ U V,
    IsOpen U ∧
      IsOpen V ∧
        a ∈ U ∧
          0 ∈ V ∧
            ψ.source = U ×ˢ V ∧
              U ×ˢ V ⊆ W ∧
                (∀ (z : P × F), (↑ψ z).1 = z.1) ∧
                  (∀ (b : P), ↑ψ (b, 0) = (b, 0)) ∧
                    (∀ z ∈ ψ.target, (↑ψ.symm z).1 = z.1) ∧
                      ContDiffOn ℝ (↑n) (↑ψ) ψ.source ∧
                        ContDiffOn ℝ (↑n) (↑ψ.symm) ψ.target ∧
                          ∀ z ∈ ψ.source,
                            f z =
                              f (a, 0) +
                                ∑ i,
                                  (if ↑i < TauCeti.morseIndex f (a, 0) then -1 else 1) *
                                    (↑ψ z).2.ofLp i ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Morse–Bott lemma in product coordinates](../part-01/the-morse-bott-lemma-in-product-coordinates.md)
- [Sylvester's law of inertia for regular forms](../../../../linear-algebra/quadratic-form/sylvesters-law-of-inertia-for-regular-forms.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_normalized_morseBott_chart_of_contDiffOn`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Morse/Bott.html#TauCeti.exists_normalized_morseBott_chart_of_contDiffOn).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_normalized_morseBott_chart_of_contDiffOn`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Morse/Bott.html#TauCeti.exists_normalized_morseBott_chart_of_contDiffOn)
- [Source of `TauCeti.exists_normalized_morseBott_chart_of_contDiffOn` in TauCeti/Analysis/Calculus/Morse/Bott.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Calculus/Morse/Bott.lean#L314)
