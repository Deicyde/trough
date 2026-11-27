---
declaration: theorem
origin: cited
lean: SmithNumber.mcdaniel_infinitely_many_smith_numbers, SmithNumber.infinite_smith_brothers
statement: formalized
---

# McDaniel's Theorem on Smith Numbers and the Smith Brothers Problem

> Coined by Albert Wilansky (1982), a base-$b$ *Smith number* ($b \ge 2$; `OEIS A006753` for $b = 10$)
> is a composite integer $n$ whose base-$b$ digit sum matches the total base-$b$ digit sum across its
> prime factors with multiplicity.
>
> Wayne L. McDaniel (1987) proved that base-$10$ Smith numbers form an infinite set. Adjacent
> base-$10$ Smith numbers $(n, n + 1)$—beginning at $(728, 729)$—form *Smith brothers* (the least
> starting term of $k$ consecutive base-$10$ Smith numbers is `OEIS A059754`); whether infinitely many
> pairs of Smith brothers exist remains open.
>
> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Smith_number)
> - [OEIS A006753](https://oeis.org/A006753)
> - [OEIS A059754](https://oeis.org/A059754)
> - A. Wilansky, *Smith numbers*, Two-Year Coll. Math. J. **13** (1982), no. 1, 21.
> - W. L. McDaniel, *The existence of infinitely many k-Smith numbers*, Fibonacci Quart. **25**
>   (1987), no. 1, 76–80.

*Quoted from [FormalConjectures/Wikipedia/SmithNumber.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/SmithNumber.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 2 test statements and 2 API statements, counted here but not shown.

## `SmithNumber.mcdaniel_infinitely_many_smith_numbers`

Solved: stated here without proof.

> **McDaniel's Theorem (1987)**: Infinitely many base-$10$ Smith numbers exist.

```lean
theorem mcdaniel_infinitely_many_smith_numbers :
    {n : ℕ | IsSmithNumber 10 n}.Infinite
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/SmithNumber.lean, line 100](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/SmithNumber.lean#L100).

## `SmithNumber.infinite_smith_brothers`

Open: stated without proof.

> Do infinitely many consecutive base-$10$ Smith-number pairs $(n, n + 1)$ (Smith brothers) exist?

```lean
theorem infinite_smith_brothers :
    {n : ℕ | IsSmithNumber 10 n ∧ IsSmithNumber 10 (n + 1)}.Infinite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/SmithNumber.lean, line 108](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/SmithNumber.lean#L108).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/SmithNumber.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/SmithNumber.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Smith_number)
