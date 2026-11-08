---
declaration: theorem
origin: cited
lean: TauCeti.IsNondegenerateCriticalPoint.exists_normal_form, TauCeti.IsNondegenerateCriticalPoint.exists_morse_chart
statement: formalized
proof: formalized
---

# The Morse lemma

Near a nondegenerate critical point `x` of a `C^{n+2}` function `f`,
with `1 ≤ n ≤ ∞`, there is a `C^n` map `φ`, fixing `0` and with derivative the identity there,
in terms of which `f` is exactly its Hessian quadratic form:
`f (x + v) = f x + 2⁻¹ * fderiv ℝ (fderiv ℝ f) x (φ v) (φ v)` for `v` near `0`.

`TauCeti.IsNondegenerateCriticalPoint.exists_morse_chart` repackages this as a chart at
`x`.

```lean
TauCeti.IsNondegenerateCriticalPoint.exists_normal_form.{u} {E : Type u} [NormedAddCommGroup E]
  [NormedSpace ℝ E] {x : E} [CompleteSpace E] {f : E → ℝ} {n : ℕ∞} (hf : ContDiff ℝ (↑n + 2) f)
  (h : TauCeti.IsNondegenerateCriticalPoint f x) (hn : n ≠ 0) :
  ∃ φ U,
    IsOpen U ∧
      0 ∈ U ∧
        φ 0 = 0 ∧
          ContDiffOn ℝ (↑n) φ U ∧
            HasFDerivAt φ (ContinuousLinearMap.id ℝ E) 0 ∧
              ∀ v ∈ U, f (x + v) = f x + 2⁻¹ * ((fderiv ℝ (fderiv ℝ f) x) (φ v)) (φ v)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Taylor's formula to second order](../part-02/taylors-formula-to-second-order.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsNondegenerateCriticalPoint.exists_normal_form`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Morse/NormalForm.html#TauCeti.IsNondegenerateCriticalPoint.exists_normal_form).

## Other forms

**The Morse lemma, as a chart.** Formalized in Tau Ceti as [`TauCeti.IsNondegenerateCriticalPoint.exists_morse_chart`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Morse/NormalForm.html#TauCeti.IsNondegenerateCriticalPoint.exists_morse_chart).

```lean
TauCeti.IsNondegenerateCriticalPoint.exists_morse_chart.{u} {E : Type u} [NormedAddCommGroup E]
  [NormedSpace ℝ E] {x : E} [CompleteSpace E] {f : E → ℝ} {n : ℕ∞} (hf : ContDiff ℝ (↑n + 2) f)
  (h : TauCeti.IsNondegenerateCriticalPoint f x) (hn : n ≠ 0) :
  ∃ ψ,
    x ∈ ψ.source ∧
      ↑ψ x = 0 ∧
        ContDiffOn ℝ (↑n) (↑ψ) ψ.source ∧
          ContDiffOn ℝ (↑n) (↑ψ.symm) ψ.target ∧
            ∀ y ∈ ψ.source, f y = f x + 2⁻¹ * ((fderiv ℝ (fderiv ℝ f) x) (↑ψ y)) (↑ψ y)
```

## Sources

- [Tau Ceti documentation: `TauCeti.IsNondegenerateCriticalPoint.exists_normal_form`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Morse/NormalForm.html#TauCeti.IsNondegenerateCriticalPoint.exists_normal_form)
- [Source of `TauCeti.IsNondegenerateCriticalPoint.exists_normal_form` in TauCeti/Analysis/Calculus/Morse/NormalForm.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Calculus/Morse/NormalForm.lean#L358)
