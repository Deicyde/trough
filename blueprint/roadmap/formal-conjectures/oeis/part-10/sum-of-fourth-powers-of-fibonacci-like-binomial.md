---
declaration: theorem
origin: cited
lean: OeisA181546.conjecture
statement: formalized
---

# Sum of fourth powers of Fibonacci-like binomial coefficients

> The sequence is defined by
>
> $$a(n) = \sum_{k=0}^{\lfloor n/2 \rfloor} \binom{n-k}{k}^4.$$
>
> *References:*
> - [A181546](https://oeis.org/A181546)

*Quoted from [FormalConjectures/OEIS/181546.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/181546.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA181546.conjecture`

Solved: stated here; a Lean proof is at [https://github.com/epoch-research/LeanOpenProblems-results/blob/f02efd9a8c5fc6a735d2a90c33e24f7278ce0ffc/runs/oeis-full-50usd-ant-j0j0g4uzligm1k41/oeis_181546_conjecture_0/Submission/Spec.lean#L1210](https://github.com/epoch-research/LeanOpenProblems-results/blob/f02efd9a8c5fc6a735d2a90c33e24f7278ce0ffc/runs/oeis-full-50usd-ant-j0j0g4uzligm1k41/oeis_181546_conjecture_0/Submission/Spec.lean#L1210).

> Conjecture: Given $F(n,L) = \sum_{k=0}^{\lfloor n/2 \rfloor} \binom{n-k}{k}^L$, then
> $\lim_{n\to\infty} F(n+1,L)/F(n,L) = (\mathrm{Fibonacci}(L)\sqrt{5} + \mathrm{Lucas}(L))/2$ for
> $L \ge 0$ where $\mathrm{Fibonacci}(n) = \mathrm{A000045}(n)$ and
> $\mathrm{Lucas}(n) = \mathrm{A000032}(n)$.

```lean
theorem conjecture (L : ℕ) :
    Tendsto (fun n => (F (n + 1) L : ℝ) / (F n L : ℝ)) atTop (nhds (limitValue L))
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/181546.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/181546.lean#L80).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/181546.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/181546.lean)
- [A181546](https://oeis.org/A181546)
