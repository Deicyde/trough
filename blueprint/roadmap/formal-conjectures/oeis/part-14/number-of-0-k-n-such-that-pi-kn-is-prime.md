---
declaration: theorem
origin: cited
lean: OeisA237578.conjecture_1, OeisA237578.conjecture_2, OeisA237578.conjecture_3
statement: formalized
---

# Number of $0 < k < n$ such that $\pi(kn)$ is prime

> Let $\pi$ denote the prime counting function. The sequence $a(n)$ counts the number of integers
> $0 < k < n$ such that $\pi(kn)$ is prime.
>
> *References:*
> - [A237578](https://oeis.org/A237578)

*Quoted from [FormalConjectures/OEIS/237578.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/237578.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 3 open. It also has 5 test statements, counted here but not shown.

## `OeisA237578.conjecture_1`

Open: stated without proof.

> Conjecture: $a(n) > 0$ for all $n > 2$.

```lean
theorem conjecture_1 (n : ℕ) (hn : 2 < n) : 0 < a n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/237578.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/237578.lean#L58).

## `OeisA237578.conjecture_2`

Open: stated without proof.

> and $a(n) = 1$ only for $n = 5, 8, 13$.

```lean
theorem conjecture_2 (n : ℕ) :
    a n = 1 ↔ n = 5 ∨ n = 8 ∨ n = 13
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/237578.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/237578.lean#L65).

## `OeisA237578.conjecture_3`

Open: stated without proof.

> Moreover, for each $n = 1, 2, 3, \dots$, there is a positive integer $k < 3\sqrt{n} + 3$ with
> $\pi(kn)$ prime.

```lean
theorem conjecture_3 (n : ℕ) (hn : 1 ≤ n) :
    ∃ k : ℕ, 0 < k ∧ (k : ℝ) < 3 * Real.sqrt (n : ℝ) + 3 ∧
      (Nat.primeCounting (k * n)).Prime
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/237578.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/237578.lean#L74).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/237578.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/237578.lean)
- [A237578](https://oeis.org/A237578)
