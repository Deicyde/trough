---
declaration: theorem
origin: cited
lean: OeisA230507.conjecture_1, OeisA230507.conjecture_2
statement: formalized
---

# Triples summing to $n$ with $2m+1$ and $2m^3+1$ prime

> Number of ways to write $n = x + y + z$ with $x \le y \le z$, where $x, y, z$ are positive integers
> such that $2m + 1$ and $2m^3 + 1$ are both prime for $m \in \{x, y, z\}$.
>
> *References:*
> - [A230507](https://oeis.org/A230507)

*Quoted from [FormalConjectures/OEIS/230507.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/230507.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 6 test statements, counted here but not shown.

## `OeisA230507.conjecture_1`

Open: stated without proof.

> Conjecture (i): $a(n) > 0$ for all $n > 2$.

```lean
theorem conjecture_1 (n : ℕ) (hn : n > 2) : a n > 0
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/230507.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/230507.lean#L67).

## `OeisA230507.conjecture_2`

Open: stated without proof.

> Conjecture (ii): Any integer $n > 8$ can be written as $x + y + z$ ($x, y, z > 0$) with
> $2x + 1, 2y + 1, 2z - 1, 2x^4 - 1, 2y^4 - 1, 2z^4 - 1$ all prime.

```lean
theorem conjecture_2 (n : ℕ) (hn : n > 8) :
    ∃ x y z : ℕ, 0 < x ∧ 0 < y ∧ 0 < z ∧ x + y + z = n ∧
      (2 * x + 1).Prime ∧ (2 * y + 1).Prime ∧ (2 * z - 1).Prime ∧
      (2 * x ^ 4 - 1).Prime ∧ (2 * y ^ 4 - 1).Prime ∧ (2 * z ^ 4 - 1).Prime
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/230507.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/230507.lean#L75).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/230507.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/230507.lean)
- [A230507](https://oeis.org/A230507)
