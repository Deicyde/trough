---
declaration: theorem
origin: cited
lean: OeisA262446.conjecture_1, OeisA262446.conjecture_2
statement: formalized
---

# Additive decompositions of $\pi(\frac{n(n+1)}{2} + 1)$

> Number of ways to write $\pi(\frac{n(n+1)}{2} + 1) = \pi(\frac{k(k+1)}{2} + 1) +
> \pi(\frac{m(m+1)}{2} + 1)$ with $0 < k < m < n$, where $\pi(x)$ is the prime-counting function.
>
> *References:*
> - [A262446](https://oeis.org/A262446)
> - [Problems on combinatorial properties of primes](https://arxiv.org/abs/1402.6641)
>   by *Zhi-Wei Sun*, arXiv:1402.6641 (2014)

*Quoted from [FormalConjectures/OEIS/262446.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/262446.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 5 test statements, counted here but not shown.

## `OeisA262446.conjecture_1`

Open: stated without proof.

> Conjecture: $a(n) > 0$ for all $n > 3$.

```lean
theorem conjecture_1 (n : ℕ) (hn : 3 < n) : 0 < a n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/262446.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/262446.lean#L71).

## `OeisA262446.conjecture_2`

Open: stated without proof.

> Conjecture: $a(n) = 1$ only for $n = 4, 6, 11, 21, 54, 253, 325$.

```lean
theorem conjecture_2 (n : ℕ) (hn : 3 < n) :
    a n = 1 ↔ n ∈ singletons
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/262446.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/262446.lean#L78).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/262446.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/262446.lean)
- [A262446](https://oeis.org/A262446)
