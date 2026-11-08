---
declaration: theorem
origin: cited
lean: TauCeti.exists_openPartialHomeomorph_fderiv_eq_const
statement: formalized
proof: formalized
---

# The straightening theorem (flow-box theorem)

A `C^n` vector field `w`, `1 ≤ n`, defined
near a point `a` of a finite-dimensional real normed space, with `w a ≠ 0`, is constant in suitable
`C^n` coordinates: there is an open partial homeomorphism `φ`, `C^n` on its source with `C^n`
inverse on its target, such that `a ∈ φ.source` and `dφ_y (w y) = w a` for every `y ∈ φ.source`.

```lean
TauCeti.exists_openPartialHomeomorph_fderiv_eq_const.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [FiniteDimensional ℝ E] {n : ℕ∞} (hn : 1 ≤ n) {w : E → E} {s : Set E} {a : E}
  (hw : ContDiffOn ℝ (↑n) w s) (hs : s ∈ nhds a) (ha : w a ≠ 0) :
  ∃ φ,
    a ∈ φ.source ∧
      (∀ y ∈ φ.source, ContDiffAt ℝ (↑n) (↑φ) y) ∧
        (∀ z ∈ φ.target, ContDiffAt ℝ (↑n) (↑φ.symm) z) ∧
          ∀ y ∈ φ.source, (fderiv ℝ (↑φ) y) (w y) = w a
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The inverse function theorem produces a `C^n` inverse](../calculus/part-01/the-inverse-function-theorem-produces-a-c-n-inve.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_openPartialHomeomorph_fderiv_eq_const`](https://taucetiproject.org/docs/TauCeti/Analysis/ODE/Straightening.html#TauCeti.exists_openPartialHomeomorph_fderiv_eq_const).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_openPartialHomeomorph_fderiv_eq_const`](https://taucetiproject.org/docs/TauCeti/Analysis/ODE/Straightening.html#TauCeti.exists_openPartialHomeomorph_fderiv_eq_const)
- [Source of `TauCeti.exists_openPartialHomeomorph_fderiv_eq_const` in TauCeti/Analysis/ODE/Straightening.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/ODE/Straightening.lean#L144)
