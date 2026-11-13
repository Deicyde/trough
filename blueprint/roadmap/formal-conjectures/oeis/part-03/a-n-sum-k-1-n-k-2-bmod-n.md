---
declaration: theorem
origin: cited
lean: OeisA48153.conjecture
statement: formalized
---

# $a(n) = \sum_{k=1}^n (k^2 \bmod n)$

> *References:*
> - [A048153](https://oeis.org/A048153)

*Quoted from [FormalConjectures/OEIS/48153.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/48153.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA48153.conjecture`

Solved: stated here; a Lean proof is at [https://github.com/epoch-research/LeanOpenProblems-results/blob/f02efd9a8c5fc6a735d2a90c33e24f7278ce0ffc/runs/oeis-lite-200usd-ant-me0xxoowyqauyrvj/oeis_48153_conjecture_0/Submission/Spec.lean#L3215](https://github.com/epoch-research/LeanOpenProblems-results/blob/f02efd9a8c5fc6a735d2a90c33e24f7278ce0ffc/runs/oeis-lite-200usd-ant-me0xxoowyqauyrvj/oeis_48153_conjecture_0/Submission/Spec.lean#L3215).

> "Conjecture: $a(n) <= \frac{n^2-1}{2}$. - _Aspen A.M. Meissner_, Mar 06 2025"

```lean
theorem conjecture (n : ℕ) (hn : 1 ≤ n) : a n ≤ (n ^ 2 - 1) / 2
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/48153.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/48153.lean#L64).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/48153.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/48153.lean)
- [A048153](https://oeis.org/A048153)
