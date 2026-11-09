---
declaration: theorem
origin: cited
lean: OeisA52709.conjecture
statement: formalized
---

# Expansion of g.f. $(1-\sqrt{1-4x-4x^2})/(2(1+x))$

> The $n$-th term $a(n)$ is given by
>
> $$a(n) = \sum_{k=0}^{n-1} \frac{1}{k+1} \binom{2k}{k} \binom{k}{n-1-k}$$
>
> *References:*
> - [A052709](https://oeis.org/A052709)

*Quoted from [FormalConjectures/OEIS/52709.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/52709.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 6 test statements, counted here but not shown.

## `OeisA52709.conjecture`

Solved: stated here; a Lean proof is at [https://github.com/epoch-research/LeanOpenProblems-results/blob/f02efd9a8c5fc6a735d2a90c33e24f7278ce0ffc/runs/oeis-full-50usd-ant-j0j0g4uzligm1k41/oeis_52709_conjecture_0/Submission/Spec.lean#L1289](https://github.com/epoch-research/LeanOpenProblems-results/blob/f02efd9a8c5fc6a735d2a90c33e24f7278ce0ffc/runs/oeis-full-50usd-ant-j0j0g4uzligm1k41/oeis_52709_conjecture_0/Submission/Spec.lean#L1289).

> Conjecture: for $n > 0$, $a(n)$ is also the number of sequences of length $n - 1$ covering an
> initial interval of positive integers and avoiding three terms
> $(\dots, x, \dots, y, \dots, z, \dots)$ such that $x \le y \le z$.
> - Gus Wiseman, Jun 17 2021

```lean
theorem conjecture (n : ℕ) (hn : 0 < n) [Fintype (sequencesCountedByA052709 n)] :
    a n = Fintype.card (sequencesCountedByA052709 n)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/52709.lean, line 97](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/52709.lean#L97).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/52709.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/52709.lean)
- [A052709](https://oeis.org/A052709)
