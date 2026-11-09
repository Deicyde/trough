---
declaration: theorem
origin: cited
lean: Erdos53.erdos_53, Erdos53.erdos_53.variants.upper
statement: formalized
---

# Erdős Problem 53

> *References:*
> - [erdosproblems.com/53](https://www.erdosproblems.com/53)
> - [Er77c] Erdős, Paul, *Problems and results on combinatorial number theory. III*. Number theory
>   day (Proc. Conf., Rockefeller Univ., New York, 1976) (1977), 43-72.
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980).
> - [ErSz83] Erdős, P. and Szemerédi, E., *On sums and products of integers*. Studies in pure
>   mathematics (1983), 213-218.
> - [Er91] Erdős, P., *Problems and results in combinatorial analysis and combinatorial number
>   theory*. Graph theory, combinatorics, and applications, Vol. 1 (Kalamazoo, MI, 1988) (1991),
>   397-406.
> - [Er97] Erdős, Paul, *Problems in number theory*. New Zealand J. Math. (1997), 155-160.
> - [Er97e] Erdős, Paul, *Some of my favourite unsolved problems*. Math. Japon. (1997), 527-537.
> - [Ch03] Chang, M.-C., *The Erdős-Szemerédi problem on sum set and product set*. Annals of Math.
>   (2003), 939-957.

*Quoted from [FormalConjectures/ErdosProblems/53.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/53.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/53](https://www.erdosproblems.com/53).

The file states 2 research or textbook statements: 2 solved.

## `Erdos53.erdos_53`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos53.lean#L3084](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos53.lean#L3084).

> Let $A$ be a finite set of integers. Is it true that, for every $k$, if $\lvert A\rvert$ is
> sufficiently large depending on $k$, then there are least $\lvert A\rvert^k$ many integers which
> are either the sum or product of distinct elements of $A$?
>
> Asked by Erdős and Szemerédi [ErSz83]. Solved in this form by Chang [Ch03].
>
> Erdős and Szemerédi proved that there exist arbitrarily large sets $A$ such that the number of
> integers which are the sum or product of distinct elements of $A$ is at most
>
> $$\exp\left(c \frac{(\log \lvert A\rvert)^2}{\log\log\lvert A\rvert}\right)$$
>
> for some constant $c>0$. (erdosproblems.com multiplies by $\log\log\lvert A\rvert$;
> [ErSz83, Theorem 2] divides by it.)
>
> See also [52](https://www.erdosproblems.com/52).

```lean
theorem erdos_53 : ∀ k : ℕ, ∃ N : ℕ, ∀ A : Finset ℤ, N ≤ A.card →
    A.card ^ k ≤ (sumsAndProducts A).card
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/53.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/53.lean#L68).

## `Erdos53.erdos_53.variants.upper`

Solved: stated here without proof.

> Erdős and Szemerédi [ErSz83] proved that there exist arbitrarily large sets $A$ such that the
> number of integers which are the sum or product of distinct elements of $A$ is at most
>
> $$\exp\left(c \frac{(\log \lvert A\rvert)^2}{\log\log\lvert A\rvert}\right)$$
>
> for some constant $c>0$. (erdosproblems.com multiplies by $\log\log\lvert A\rvert$;
> [ErSz83, Theorem 2] divides by it.)

```lean
theorem erdos_53.variants.upper : ∃ c : ℝ, 0 < c ∧ ∀ N : ℕ, ∃ A : Finset ℤ, N ≤ A.card ∧
    ((sumsAndProducts A).card : ℝ) ≤
      Real.exp (c * Real.log A.card ^ 2 / Real.log (Real.log A.card))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/53.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/53.lean#L80).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/53.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/53.lean)
- [erdosproblems.com/53](https://www.erdosproblems.com/53)
