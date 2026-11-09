---
declaration: theorem
origin: cited
lean: OeisA109845.conjecture
statement: formalized
---

# Conjectures associated with A109845

> $a(1) = 2$; $a(2n)$ = lcm of all previous terms + 1; $a(2n+1)$ = lcm of all previous terms - 1.
>
> *References:*
> - [A109845](https://oeis.org/A109845)

*Quoted from [FormalConjectures/OEIS/109845.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/109845.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA109845.conjecture`

Open: stated without proof.

> Conjecture: There are infinitely many primes in this sequence.

```lean
theorem conjecture : Set.Infinite {n : ℕ | (a n).Prime}
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/109845.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/109845.lean#L69).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/109845.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/109845.lean)
- [A109845](https://oeis.org/A109845)
