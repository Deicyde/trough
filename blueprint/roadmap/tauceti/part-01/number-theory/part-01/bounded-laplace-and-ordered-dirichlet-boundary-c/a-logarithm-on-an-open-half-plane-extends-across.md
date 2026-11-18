---
declaration: theorem
origin: cited
lean: TauCeti.exists_differentiableOn_eqOn_exp_comp_le_re
statement: formalized
proof: formalized
---

# A logarithm on an open half-plane extends across its boundary line

Let `g` be holomorphic
on an open set `V` containing the closed half-plane `{s | a ≤ re s}` and zero-free on that closed
half-plane, and let `f` be a holomorphic logarithm of `g` on the open half-plane `{s | a < re s}`.
Then some open neighbourhood `Ω` of the closed half-plane carries a holomorphic logarithm `F` of
`g` that agrees with `f` on the open half-plane.

The neighbourhood is a union of discs centred on the line `re s = a`; it need not contain a strip
`{s | a - δ < re s}` of uniform width.

```lean
TauCeti.exists_differentiableOn_eqOn_exp_comp_le_re {a : ℝ} {V : Set ℂ} {f g : ℂ → ℂ}
  (hV : IsOpen V) (hcover : {s | a ≤ s.re} ⊆ V) (hg : DifferentiableOn ℂ g V)
  (hg₀ : ∀ (s : ℂ), a ≤ s.re → g s ≠ 0) (hf : DifferentiableOn ℂ f {s | a < s.re})
  (hfg : Set.EqOn (Complex.exp ∘ f) g {s | a < s.re}) :
  ∃ Ω,
    IsOpen Ω ∧
      {s | a ≤ s.re} ⊆ Ω ∧
        ∃ F, DifferentiableOn ℂ F Ω ∧ Set.EqOn (Complex.exp ∘ F) g Ω ∧ Set.EqOn F f {s | a < s.re}
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_differentiableOn_eqOn_exp_comp_le_re`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/BranchLogRoot.html#TauCeti.exists_differentiableOn_eqOn_exp_comp_le_re).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_differentiableOn_eqOn_exp_comp_le_re`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/BranchLogRoot.html#TauCeti.exists_differentiableOn_eqOn_exp_comp_le_re)
- [Source of `TauCeti.exists_differentiableOn_eqOn_exp_comp_le_re` in TauCeti/Analysis/Complex/BranchLogRoot.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/BranchLogRoot.lean#L386)
- [Tau Ceti roadmap status: Bounded Laplace and ordered Dirichlet boundary convergence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TauberianBoundaryConvergence/STATUS.md)
