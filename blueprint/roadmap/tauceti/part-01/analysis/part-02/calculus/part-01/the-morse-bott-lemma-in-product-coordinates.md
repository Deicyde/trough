---
declaration: theorem
origin: cited
lean: TauCeti.exists_morseBott_chart_of_contDiffOn
statement: formalized
proof: formalized
---

# The Morse–Bott lemma in product coordinates

Let `f` be `C^{n+2}` on a neighbourhood `W`
of `(a, 0)`, with `1 ≤ n ≤ ∞`, such that every point `(b, 0)` with `b` near `a` is critical and the
kernel of the Hessian at `(a, 0)` consists of base directions. Then there is a `C^n` chart `ψ`
with product source `U ×ˢ V` in `W`, preserving the base parameter in both directions and fixing
the zero section, such that on `U` the vertical Hessian is invertible and the critical value is
constant, and on the source of `ψ` the function `f` is that critical value plus half the vertical
Hessian read in the chart.

```lean
TauCeti.exists_morseBott_chart_of_contDiffOn.{u_1, u_2} {P : Type u_1} {F : Type u_2}
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
                          (∀ b ∈ U, f (b, 0) = f (a, 0)) ∧
                            (∀ b ∈ U, (fderiv ℝ (fderiv ℝ fun v => f (b, v)) 0).IsInvertible) ∧
                              ∀ z ∈ ψ.source,
                                f z =
                                  f (a, 0) +
                                    2⁻¹ *
                                      ((fderiv ℝ (fderiv ℝ fun v => f (z.1, v)) 0) (↑ψ z).2)
                                        (↑ψ z).2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The local parametric Morse lemma](the-local-parametric-morse-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_morseBott_chart_of_contDiffOn`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Morse/Bott.html#TauCeti.exists_morseBott_chart_of_contDiffOn).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_morseBott_chart_of_contDiffOn`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Morse/Bott.html#TauCeti.exists_morseBott_chart_of_contDiffOn)
- [Source of `TauCeti.exists_morseBott_chart_of_contDiffOn` in TauCeti/Analysis/Calculus/Morse/Bott.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Calculus/Morse/Bott.lean#L106)
