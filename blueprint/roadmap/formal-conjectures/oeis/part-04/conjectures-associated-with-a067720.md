---
declaration: theorem
origin: cited
lean: OeisA67720.a_of_primes, OeisA67720.prime_add_one_of_a
statement: formalized
---

# Conjectures associated with A067720

> A067720 lists numbers $k$ such that $\varphi(k^2 + 1) = k \cdot \varphi(k + 1)$,
> where $\varphi$ is Euler's totient function.
>
> The sequence exhibits a strong connection to primes: for almost all terms $k$,
> $k + 1$ is prime. The conjecture states that $k = 8$ is the only exception.
>
> *References:*
> - [A067720](https://oeis.org/A067720)

*Quoted from [FormalConjectures/OEIS/67720.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/67720.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 textbook result. It also has 6 test statements, counted here but not shown.

## `OeisA67720.a_of_primes`

Textbook result, proved here.

> If $k + 1$ and $k^2 + 1$ are both prime, then $k$ is in the sequence.

```lean
theorem a_of_primes {k : ℕ} (hk : (k + 1).Prime) (hk' : (k ^ 2 + 1).Prime) : A k
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/67720.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/67720.lean#L74).

## `OeisA67720.prime_add_one_of_a`

Open: stated without proof.

> For members of the sequence other than $8$, we have $k + 1$ is prime.

```lean
theorem prime_add_one_of_a {k : ℕ} (h : A k) (hne : k ≠ 8) : (k + 1).Prime
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/67720.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/67720.lean#L79).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/67720.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/67720.lean)
- [A067720](https://oeis.org/A067720)
