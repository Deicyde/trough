---
declaration: theorem
origin: cited
lean: OeisA24356.conjecture
statement: formalized
---

# Determinant of Hankel matrix of the first $2n-1$ prime numbers

> The determinant of the $n \times n$ Hankel matrix whose entries are the first $2n-1$ prime numbers.
> The matrix $M$ has entries $M_{i, j} = p_{i+j}$ for $i, j \in \{0, \dots, n-1\}$,
> where $p_k = \mathrm{Nat.nth\;Nat.Prime} (k)$ is the $k$-th prime starting at $p_0=2$.
> $a(0)=1$ by convention.
>
> *References:*
> - [A024356](https://oeis.org/A024356)

*Quoted from [FormalConjectures/OEIS/24356.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/24356.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 4 test statements, counted here but not shown.

## `OeisA24356.conjecture`

Open: stated without proof.

> "I conjecture that $a(4)$ is the only zero. - _Jon Perry_, Mar 22 2004"
>
> Stated as a biconditional: the claim that $a(4)$ is *the only* zero asserts both that $a(4) = 0$
> and that no other index vanishes. A bare implication `a n = 0 → n = 4` would be satisfied
> vacuously by a sequence with no zero at all. The existence direction is certified by `a_4`; the
> uniqueness direction is the open part.

```lean
theorem conjecture : ∀ n : ℕ, a n = 0 ↔ n = 4
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [15 Linear and multilinear algebra; matrix theory](../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md). Declared in [FormalConjectures/OEIS/24356.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/24356.lean#L85).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/24356.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/24356.lean)
- [A024356](https://oeis.org/A024356)
