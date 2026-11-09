---
declaration: theorem
origin: cited
lean: OeisA109909.conjecture
statement: formalized
---

# Conjectures associated with A109909

> $a(n)$ = number of primes of the form $k(n-k)-1$.
>
> *References:*
> - [A109909](https://oeis.org/A109909)

*Quoted from [FormalConjectures/OEIS/109909.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/109909.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA109909.conjecture`

Open: stated without proof.

> Conjecture: $a(n) > 0$ for $n > 3$.

```lean
theorem conjecture : ∀ n > 3, a n > 0
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/109909.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/109909.lean#L61).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/109909.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/109909.lean)
- [A109909](https://oeis.org/A109909)
