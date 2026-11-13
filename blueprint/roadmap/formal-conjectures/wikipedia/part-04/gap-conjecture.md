---
declaration: theorem
origin: cited
lean: GapConjecture.gap_conjecture
statement: formalized
---

# Gap conjecture

> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Gromov%27s_theorem_on_groups_of_polynomial_growth#The_gap_conjecture)
> - [On the Gap Conjecture concerning group growth](https://arxiv.org/pdf/1202.6044) by
>   *Rostislav Grigorchuk*

*Quoted from [FormalConjectures/Wikipedia/GapConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/GapConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `GapConjecture.gap_conjecture`

Open: stated without proof.

> If a finitely generated group has superpolynomial growth, then with respect to any finite
> generating set its growth function is at least $e^{\sqrt n}$ in Grigorchuk's preorder on
> growth functions, where the comparison is witnessed by linearly rescaling the radius.

```lean
theorem gap_conjecture :
    ∀ (G : Type) [Group G] (S : Set G), S.Finite → Subgroup.closure S = ⊤ →
      HasSuperPolynomialGrowth G →
      ∃ C : ℕ, 0 < C ∧
        ∀ᶠ n : ℕ in atTop, Real.exp (Real.sqrt (n : ℝ)) ≤
          (GrowthFunction S (C * n) : ℝ)
```

Category `research open`; AMS [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/Wikipedia/GapConjecture.lean, line 41](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/GapConjecture.lean#L41).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/GapConjecture.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/GapConjecture.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Gromov%27s_theorem_on_groups_of_polynomial_growth#The_gap_conjecture)
