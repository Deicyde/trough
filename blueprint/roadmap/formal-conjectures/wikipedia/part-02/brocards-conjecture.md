---
declaration: theorem
origin: cited
lean: Brocard.brocard_conjecture, Brocard.brocard_conjecture.ferreira_large_n
statement: formalized
---

# Brocard's Conjecture

> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Brocard%27s_conjecture)
> - [Luan Alberto Ferreira, *Real exponential sums over primes and prime gaps*](https://arxiv.org/abs/2307.08725)

*Quoted from [FormalConjectures/Wikipedia/BrocardConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/BrocardConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Brocard.brocard_conjecture`

Open: stated without proof.

> **Brocard's Conjecture**
> For every `n ≥ 2`, between the squares of the `n`-th and `(n+1)`-th primes,
> there are at least four prime numbers.

```lean
theorem brocard_conjecture (n : ℕ) (hn : 1 ≤ n) :
    letI prev := n.nth Nat.Prime;
    letI next := (n+1).nth Nat.Prime;
    4 ≤ ((Ioo (prev^2) (next^2)).filter Nat.Prime).card
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/BrocardConjecture.lean, line 40](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/BrocardConjecture.lean#L40).

## `Brocard.brocard_conjecture.ferreira_large_n`

Solved: stated here without proof.

> Ferreira proved that Brocard's conjecture is true for sufficiently large n.

```lean
theorem brocard_conjecture.ferreira_large_n : ∀ᶠ n in atTop,
    letI prev := n.nth Nat.Prime;
    letI next := (n+1).nth Nat.Prime;
    4 ≤ ((Ioo (prev^2) (next^2)).filter Nat.Prime).card
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/BrocardConjecture.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/BrocardConjecture.lean#L50).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/BrocardConjecture.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/BrocardConjecture.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Brocard%27s_conjecture)
