---
declaration: theorem
origin: cited
lean: OeisA109227.conjecture
statement: formalized
---

# Conjectures associated with A109227

> Binary strings that have 1's where primes occur, 0's elsewhere and every term ends
> with the $n$-th prime index.
>
> Conjecture: $a(2)$ and $a(121)$ are primes. Are there any more?
>
> *References:*
> - [A109227](https://oeis.org/A109227)

*Quoted from [FormalConjectures/OEIS/109227.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/109227.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA109227.conjecture`

Open: stated without proof.

> Conjecture: $a(2)$ and $a(121)$ are primes. Are there any more?

```lean
theorem conjecture :
    ∃ n > 0, n ≠ 2 ∧ n ≠ 121 ∧ (a n).Prime
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/109227.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/109227.lean#L85).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/109227.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/109227.lean)
- [A109227](https://oeis.org/A109227)
