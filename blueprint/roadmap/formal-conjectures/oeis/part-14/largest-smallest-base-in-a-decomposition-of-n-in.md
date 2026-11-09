---
declaration: theorem
origin: cited
lean: OeisA241898.conjecture_1, OeisA241898.conjecture_2
statement: formalized
---

# Largest smallest-base in a decomposition of $n$ into at most four squares

> The sequence $a(n)$ is the largest integer $k$ such that $n = k^2 + \dots$ is a
> decomposition of $n$ into a sum of at most four nondecreasing squares:
> $$a(n) = \max \{k \ge 1 : \exists b_1, b_2, b_3 \in \{0\} \cup [k, n],
>   k^2 + b_1^2 + b_2^2 + b_3^2 = n\}$$
>
> *References:*
> - [A241898](https://oeis.org/A241898)

*Quoted from [FormalConjectures/OEIS/241898.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/241898.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA241898.conjecture_1`

Solved: stated here without proof.

> "From the data that I have, it would seem that $a(n)$ is greater than $7$ for all $n > 599$."
> - _David S. Newman_, May 02 2014
>
> This is false: since every four-square decomposition of a multiple of $8$ uses only even squares,
> $a(4m) = 2a(m)$ for all even $m \ge 2$. From $a(46) = 1$ (via $46 = 1^2 + 3^2 + 6^2$) we obtain
> $a(184) = 2$ and $a(736) = a(16 \cdot 46) = 4 \le 7$.

```lean
theorem conjecture_1 : ¬ ∀ n : ℕ, 599 < n → 7 < a n
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/241898.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/241898.lean#L79).

## `OeisA241898.conjecture_2`

Open: stated without proof.

> "By Lagrange's Theorem every number can be written as a sum of four squares. Can the same be
> said of the set of $\{a^2 \mid a \text{ is any integer not equal to } 7\}$? If this could be
> proved, it would only remain to check if all the numbers up to $599$ can be written as the sum
> of $4$ squares none of which is $7^2$."
> - _David S. Newman_, May 02 2014
>
> Note that $0 \in \mathbb{N} \setminus \{7\}$ allows representations as a sum of at most four
> positive squares none of which is $7^2$.

```lean
theorem conjecture_2 :
    ∀ n : ℕ, ∃ a b c d : ℕ,
      a ≠ 7 ∧ b ≠ 7 ∧ c ≠ 7 ∧ d ≠ 7 ∧ a ^ 2 + b ^ 2 + c ^ 2 + d ^ 2 = n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/241898.lean, line 93](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/241898.lean#L93).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/241898.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/241898.lean)
- [A241898](https://oeis.org/A241898)
