---
declaration: theorem
origin: cited
lean: OeisA109671.conjecture
statement: formalized
---

# Conjectures associated with A109671

> $a(1)=1$; thereafter, $a(2n)=a(n)$, $a(2n+1)$ is the smallest positive number
> such that $|a(2n+1)-a(2n-1)|=a(n)$.
> Conjecture: Does the sequence contain every positive integer?
>
> *References:*
> - [A109671](https://oeis.org/A109671)

*Quoted from [FormalConjectures/OEIS/109671.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/109671.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA109671.conjecture`

Open: stated without proof.

> Does the sequence contain every positive integer (cf. A169741)?

```lean
theorem conjecture :
    ∀ m : ℕ, 0 < m → ∃ n : ℕ, 0 < n ∧ a n = m
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/109671.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/109671.lean#L74).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/109671.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/109671.lean)
- [A109671](https://oeis.org/A109671)
