---
declaration: theorem
origin: cited
lean: JugglerConjecture.juggler_conjecture
statement: formalized
---

# Juggler conjecture

> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Juggler_sequence)

*Quoted from [FormalConjectures/Wikipedia/JugglerConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/JugglerConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 1 test statement, counted here but not shown.

## `JugglerConjecture.juggler_conjecture`

Open: stated without proof.

> Now form a sequence beginning with any positive integer, where each subsequent term is obtained
> by applying the operation defined above to the previous term.
> The **Juggler Conjecture** states that for any positive integer $n$, there exists a natural number
> $m$ such that the $m$-th term of the sequence is $1$.

```lean
theorem juggler_conjecture (n : ℕ) (hn : n > 0) : ∃ m, jugglerStep^[m] n = 1
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [37 Dynamical systems and ergodic theory](../../by-subject/part-02/37-dynamical-systems-and-ergodic-theory/README.md). Declared in [FormalConjectures/Wikipedia/JugglerConjecture.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/JugglerConjecture.lean#L45).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/JugglerConjecture.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/JugglerConjecture.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Juggler_sequence)
