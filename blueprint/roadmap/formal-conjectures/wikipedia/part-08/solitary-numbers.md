---
declaration: theorem
origin: cited
lean: SolitaryNumber.is_ten_solitary, SolitaryNumber.infinite_club_exists
statement: formalized
---

# Solitary Numbers

> *References:*
> - [Solitary number (Wikipedia)](https://en.wikipedia.org/wiki/Solitary_number)
> - [Solitary number large clubs (Wikipedia)](https://en.wikipedia.org/wiki/Solitary_number#Large_clubs)

*Quoted from [FormalConjectures/Wikipedia/SolitaryNumber.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SolitaryNumber.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open.

## `SolitaryNumber.is_ten_solitary`

Open: stated without proof.

> **Is 10 a solitary number?**  The smallest positive integer whose solitary status is
> currently unresolved is $10$, with abundancy index $\sigma(10) / 10 = 9/5$.

```lean
theorem is_ten_solitary : IsSolitary 10
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/SolitaryNumber.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SolitaryNumber.lean#L52).

## `SolitaryNumber.infinite_club_exists`

Open: stated without proof.

> **Existence of an infinite club.**  A *club* is an abundancy equivalence class, i.e.
> the set of all positive integers friendly with a given $n$.  It is unknown whether any club
> is infinite.

```lean
theorem infinite_club_exists :
    ∃ n, 0 < n ∧ {m : ℕ | Friendly m n}.Infinite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/SolitaryNumber.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SolitaryNumber.lean#L61).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/SolitaryNumber.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SolitaryNumber.lean)
- [Solitary number (Wikipedia)](https://en.wikipedia.org/wiki/Solitary_number)
