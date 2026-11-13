---
declaration: theorem
origin: cited
lean: OeisA306477.conjecture
statement: formalized
---

# The 2-4-6-8 Conjecture

> Any integer $n > 0$ can be written as $\binom{w+2}{2} + \binom{x+3}{4} + \binom{y+5}{6} + \binom{z+7}{8}$
> with $w, x, y, z$ nonnegative integers.
>
> Zhi-Wei Sun has offered a $2,468 prize for the first proof (or $2,468 RMB for a counterexample).
>
> The conjecture has been verified for all $n$ up to $1.2 \times 10^{12}$ by Yaakov Baruch (March 2019).
>
> The conjecture is false: $n = 896315812331399$ has no such representation. The counterexample
> was found in the OEIS Open project, with a Lean proof.
>
> *References:*
> - [A306477](https://oeis.org/A306477)
> - [mathoverflow/323541](https://mathoverflow.net/questions/323541): Z.-W. Sun, "Positive integers written as C(w,2) + C(x,4) + C(y,6) + C(z,8) with w,x,y,z in {2,3,...},", Feb. 19, 2019.
> - T. Adamczewski, "OEIS Open: How many conjectures can language models turn into theorems?",
>   [arXiv:2608.11941](https://arxiv.org/abs/2608.11941) [cs.AI], 2026.

*Quoted from [FormalConjectures/OEIS/306477.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/306477.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 6 test statements, counted here but not shown.

## `OeisA306477.conjecture`

Solved: stated here; a Lean proof is at [https://github.com/epoch-research/LeanOpenProblems-results/blob/fd09021e79869476ef83cda231312f1a2a89c8d7/runs/oeis-open-lite-fable51-wm0v421z5ygi8f6b/oeis_306477_conjecture_1/Submission/Spec.lean#L793](https://github.com/epoch-research/LeanOpenProblems-results/blob/fd09021e79869476ef83cda231312f1a2a89c8d7/runs/oeis-open-lite-fable51-wm0v421z5ygi8f6b/oeis_306477_conjecture_1/Submission/Spec.lean#L793).

> **Zhi-Wei Sun's 2-4-6-8 Conjecture (A306477)**: Any integer $n > 0$ can be written as
> $\binom{w+2}{2} + \binom{x+3}{4} + \binom{y+5}{6} + \binom{z+7}{8}$ for nonnegative integers $w, x, y, z$.
>
> This is false: $n = 896315812331399$ is a counterexample.
> See T. Adamczewski, OEIS Open: How many conjectures can language models turn into theorems?,
> [arXiv:2608.11941](https://arxiv.org/abs/2608.11941).

```lean
theorem conjecture : ¬ ∀ n : ℕ, 0 < n → A n
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/306477.lean, line 84](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/306477.lean#L84).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/306477.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/306477.lean)
- [A306477](https://oeis.org/A306477)
