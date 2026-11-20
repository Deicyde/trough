---
declaration: theorem
origin: cited
lean: OeisA87571.conjecture
statement: formalized
---

# Smallest prime formed by concatenation $n, n-1, \dots, n-k$

> $a(n)$ is the smallest prime which has the form of the concatenation
> $n, n-1, n-2, \dots, n-k$ for some $k < n$, or $0$ if no such prime exists.
>
> *References:*
> - [A087571](https://oeis.org/A087571)

*Quoted from [FormalConjectures/OEIS/87571.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/87571.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA87571.conjecture`

Open: stated without proof.

> Conjecture: There are infinitely many composite numbers $n$ such that $a(n)$ is nonzero.

```lean
theorem conjecture (M : ℕ) : ∃ n > M, 1 < n ∧ ¬ n.Prime ∧ a n ≠ 0
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/87571.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/87571.lean#L75).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/87571.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/87571.lean)
- [A087571](https://oeis.org/A087571)
