---
declaration: theorem
origin: cited
lean: Oppermann.oppermann_conjecture.parts.i, Oppermann.oppermann_conjecture.parts.ii, Oppermann.oppermann_conjecture, Oppermann.oppermann_implies_brocard, Oppermann.oppermann_implies_legendre, Oppermann.oppermann_conjecture.ferreira_large_x
statement: formalized
---

# Oppermann's Conjecture

> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Oppermann%27s_conjecture)
> - [Luan Alberto Ferreira, *Real exponential sums over primes and prime gaps*](https://arxiv.org/abs/2307.08725)

*Quoted from [FormalConjectures/Wikipedia/Oppermann.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Oppermann.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 6 research or textbook statements: 3 open, 1 solved and 2 textbook results.

## `Oppermann.oppermann_conjecture.parts.i`

Open: stated without proof.

> For every integer $x \ge 2$ there exists a prime between $x(x-1)$ and $x^2$.

```lean
theorem oppermann_conjecture.parts.i (x : ℕ) (hx : 2 ≤ x) :
    ∃ p ∈ Ioo (x * (x - 1)) (x^2), p.Prime
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Oppermann.lean, line 38](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Oppermann.lean#L38).

## `Oppermann.oppermann_conjecture.parts.ii`

Open: stated without proof.

> For every integer $x \ge 2$ there exists a prime between $x^2$ and $x(x+1)$.

```lean
theorem oppermann_conjecture.parts.ii (x : ℕ) (hx : 2 ≤ x) :
    ∃ p ∈ Ioo (x^2) (x * (x + 1)), p.Prime
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Oppermann.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Oppermann.lean#L46).

## `Oppermann.oppermann_conjecture`

Open: stated without proof.

> **Oppermann's Conjecture**:
> For every integer $x \ge 2$, the following hold:
> - There exists a prime between $x(x-1)$ and $x^2$.
> - There exists a prime between $x^2$ and $x(x+1)$.

```lean
theorem oppermann_conjecture (x : ℕ) (hx : 2 ≤ x) :
    (∃ p ∈ Ioo (x * (x - 1)) (x^2), p.Prime) ∧
    (∃ p ∈ Ioo (x^2) (x * (x + 1)), p.Prime)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Oppermann.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Oppermann.lean#L57).

## `Oppermann.oppermann_implies_brocard`

Textbook result, proved here.

> Oppermann's conjecture implies Brocard's conjecture.

```lean
theorem oppermann_implies_brocard (n : ℕ) (hn : 1 ≤ n) (P : type_of% oppermann_conjecture) :
    letI prev := n.nth Nat.Prime
    letI next := (n+1).nth Nat.Prime
    4 ≤ ((Ioo (prev ^ 2) (next ^ 2)).filter Nat.Prime).card
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Oppermann.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Oppermann.lean#L64).

## `Oppermann.oppermann_implies_legendre`

Textbook result, proved here.

> Oppermann's conjecture implies Legendre's conjecture.

```lean
theorem oppermann_implies_legendre (n : ℕ) (hn : 1 ≤ n) (P : type_of% oppermann_conjecture) :
    ∃ p ∈ Ioo (n ^ 2) ((n + 1) ^ 2), p.Prime
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Oppermann.lean, line 106](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Oppermann.lean#L106).

## `Oppermann.oppermann_conjecture.ferreira_large_x`

Solved: stated here without proof.

> Ferreira proved that Oppermann's conjecture is true for sufficiently large x.

```lean
theorem oppermann_conjecture.ferreira_large_x : ∀ᶠ x in atTop,
    (∃ p ∈ Ioo (x * (x - 1)) (x^2), p.Prime) ∧
    (∃ p ∈ Ioo (x^2) (x * (x + 1)), p.Prime)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Oppermann.lean, line 117](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Oppermann.lean#L117).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/Oppermann.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Oppermann.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Oppermann%27s_conjecture)
