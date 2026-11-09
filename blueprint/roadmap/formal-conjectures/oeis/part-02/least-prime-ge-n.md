---
declaration: theorem
origin: cited
lean: OeisA7918.conjecture1, OeisA7918.conjecture2
statement: formalized
---

# Least prime $\ge n$

> Least prime $\ge n$ (version 1 of the "next prime" function).
>
> *References:*
> - [A007918](https://oeis.org/A007918)

*Quoted from [FormalConjectures/OEIS/7918.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/7918.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 4 test statements, counted here but not shown.

## `OeisA7918.conjecture1`

Open: stated without proof.

> According to the "k-tuple" conjecture, $a(n)$ is the initial term of the
> lexicographically earliest increasing arithmetic progression of $n$ primes;
> the corresponding common differences are given by A061558.

```lean
theorem conjecture1 (n : ℕ) (hn : 0 < n) :
    a n = sInf { p0 : ℕ | ∃ d : ℕ, isApOfNPrimes n p0 d }
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/7918.lean, line 82](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/7918.lean#L82).

## `OeisA7918.conjecture2`

Open: stated without proof.

> If $n > 1$, then $a(n) < n^{n^{1/n}}$.
> - Thomas Ordowski, Feb 23 2023

```lean
theorem conjecture2 (n : ℕ) (hn : 1 < n) :
    (a n : ℝ) < (n : ℝ) ^ ((n : ℝ) ^ (1 / (n : ℝ)))
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/7918.lean, line 91](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/7918.lean#L91).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/7918.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/7918.lean)
- [A007918](https://oeis.org/A007918)
