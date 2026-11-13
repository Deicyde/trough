---
declaration: theorem
origin: cited
lean: OeisA195441.conjecture
statement: formalized
---

# Denominator of $B_{n+1}(x) - B_{n+1}$

> The sequence $a(n)$ is the least common multiple of the denominators of the coefficients of the
> polynomial $B_{n+1}(x) - B_{n+1}$, where $B_m(x) = \sum_{k=0}^m \binom{m}{k} B_{m-k} x^k$ is the
> $m$-th Bernoulli polynomial and $B_m$ is the $m$-th Bernoulli number.
>
> *References:*
> - [A195441](https://oeis.org/A195441)
> - [Finiteness of Bernoulli polynomials](https://arxiv.org/abs/2310.01325)
>   by *Bernd C. Kellner*, J. Integer Seq. 27 (2024)

*Quoted from [FormalConjectures/OEIS/195441.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/195441.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA195441.conjecture`

Open: stated without proof.

> The equation $a(n-1) = \operatorname{rad}(n+1)$ has only finitely many solutions, where
> $\operatorname{rad}(n)$ is the radical of $n$. It is conjectured that
> $S = \{3, 5, 8, 9, 11, 27, 29, 35, 59\}$ is the full set of all such solutions.
> - _Bernd C. Kellner_, Oct 18 2023

```lean
theorem conjecture :
    {n : ℕ | 1 ≤ n ∧ a (n - 1) = UniqueFactorizationMonoid.radical (n + 1)} =
      ({3, 5, 8, 9, 11, 27, 29, 35, 59} : Finset ℕ)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/195441.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/195441.lean#L68).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/195441.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/195441.lean)
- [A195441](https://oeis.org/A195441)
