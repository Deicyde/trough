---
declaration: theorem
origin: cited
lean: HasCompactSupport.exists_norm_iteratedFDeriv_prod_right_sub_sub_le, HasCompactSupport.exists_norm_iteratedFDeriv_sub_sub_add_fderiv_le
statement: formalized
proof: formalized
---

# Uniform first-order Taylor estimate in a parameter

If `g : P × E → F` is `C^{i+1}` with
compact support, then the `i`-th derivative in the second variable of the first-order Taylor
remainder `x ↦ g (p + h, x) - g (p, x) - Dg(p, x) (h, 0)` in the first variable is `o(‖h‖)` as
`h → 0`, uniformly on the whole space.

```lean
HasCompactSupport.exists_norm_iteratedFDeriv_prod_right_sub_sub_le.{u_4, u_5, u_6} {P : Type u_4}
  {E : Type u_5} {F : Type u_6} [NormedAddCommGroup P] [NormedSpace ℝ P] [NormedAddCommGroup E]
  [NormedSpace ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F] {n : WithTop ℕ∞} {g : P × E → F}
  (hgc : HasCompactSupport g) (hg : ContDiff ℝ n g) {i : ℕ} (hi : ↑i + 1 ≤ n) (p : P) {ε : ℝ}
  (hε : 0 < ε) :
  ∃ δ > 0,
    ∀ (h : P),
      ‖h‖ < δ →
        ∀ (y : E),
          ‖iteratedFDeriv ℝ i (fun x => g (p + h, x) - g (p, x) - (fderiv ℝ g (p, x)) (h, 0)) y‖ ≤
            ε * ‖h‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`HasCompactSupport.exists_norm_iteratedFDeriv_prod_right_sub_sub_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/IteratedFDeriv/FDerivApply.html#HasCompactSupport.exists_norm_iteratedFDeriv_prod_right_sub_sub_le).

## Other forms

**Uniform first-order Taylor estimate for all derivatives.** Formalized in Tau Ceti as [`HasCompactSupport.exists_norm_iteratedFDeriv_sub_sub_add_fderiv_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/IteratedFDeriv/FDerivApply.html#HasCompactSupport.exists_norm_iteratedFDeriv_sub_sub_add_fderiv_le).

```lean
HasCompactSupport.exists_norm_iteratedFDeriv_sub_sub_add_fderiv_le.{u_4, u_5} {E : Type u_4}
  {F : Type u_5} [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F]
  {n : WithTop ℕ∞} {f : E → F} (hfc : HasCompactSupport f) (hf : ContDiff ℝ n f) {i : ℕ}
  (hi : ↑i + 1 ≤ n) {ε : ℝ} (hε : 0 < ε) :
  ∃ δ > 0,
    ∀ (h : E),
      ‖h‖ < δ →
        ∀ (y : E), ‖iteratedFDeriv ℝ i (fun z => f (z - h) - f z + (fderiv ℝ f z) h) y‖ ≤ ε * ‖h‖
```

## Sources

- [Tau Ceti documentation: `HasCompactSupport.exists_norm_iteratedFDeriv_prod_right_sub_sub_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/IteratedFDeriv/FDerivApply.html#HasCompactSupport.exists_norm_iteratedFDeriv_prod_right_sub_sub_le)
- [Source of `HasCompactSupport.exists_norm_iteratedFDeriv_prod_right_sub_sub_le` in TauCeti/Analysis/Calculus/IteratedFDeriv/FDerivApply.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Calculus/IteratedFDeriv/FDerivApply.lean#L147)
