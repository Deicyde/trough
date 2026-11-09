---
declaration: theorem
origin: cited
lean: OeisA212844.conjecture
statement: formalized
---

# Remainder of $2^{n+2}$ modulo $n$

> The sequence $a(n) = 2^{n+2} \bmod n$.
>
> *References:*
> - [A212844](https://oeis.org/A212844)

*Quoted from [FormalConjectures/OEIS/212844.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/212844.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA212844.conjecture`

Open: stated without proof.

> "Conjecture: every integer $k \ge 0$ appears in $a(n)$ at least once."

```lean
theorem conjecture (k : ℕ) : ∃ n : ℕ, 1 ≤ n ∧ a n = k
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/212844.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/212844.lean#L56).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/212844.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/212844.lean)
- [A212844](https://oeis.org/A212844)
