---
declaration: theorem
origin: cited
lean: OeisA92243.conjecture1, OeisA92243.conjecture2, OeisA92243.conjecture3, OeisA92243.conjecture4, OeisA92243.conjecture5
statement: formalized
---

# Tug of war score between prime gap increases and decreases

> Score at stage $n$ in "tug of war" between prime gap increases vs. prime gap decreases:
> start with score $= 0$ at $n = 1$ and at stage $k > 1$, increase (resp. decrease) the score by $1$
> if the $k$-th prime gap is greater (resp. less) than the previous prime gap.
>
> *References:*
> - [A092243](https://oeis.org/A092243)

*Quoted from [FormalConjectures/OEIS/92243.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/92243.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 5 open. It also has 4 test statements, counted here but not shown.

## `OeisA92243.conjecture1`

Open: stated without proof.

> Is the score $a(n) > 0$ for some $n > 250000$?

```lean
theorem conjecture1 : ∃ n > 250000, a n > 0
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/92243.lean, line 88](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/92243.lean#L88).

## `OeisA92243.conjecture2`

Open: stated without proof.

> Is the score $a(n)$ bounded from below?

```lean
theorem conjecture2 : ∃ B : ℤ, ∀ n : ℕ, B ≤ a n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/92243.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/92243.lean#L94).

## `OeisA92243.conjecture3`

Open: stated without proof.

> Is the score $a(n)$ bounded from above?

```lean
theorem conjecture3 : ∃ B : ℤ, ∀ n : ℕ, a n ≤ B
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/92243.lean, line 100](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/92243.lean#L100).

## `OeisA92243.conjecture4`

Open: stated without proof.

> Is the score $a(n) > 0$ for infinitely many values of $n$?

```lean
theorem conjecture4 : Set.Infinite {n : ℕ | a n > 0}
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/92243.lean, line 106](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/92243.lean#L106).

## `OeisA92243.conjecture5`

Open: stated without proof.

> Is the score $a(n) < 0$ for infinitely many values of $n$?

```lean
theorem conjecture5 : Set.Infinite {n : ℕ | a n < 0}
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/92243.lean, line 112](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/92243.lean#L112).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/92243.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/92243.lean)
- [A092243](https://oeis.org/A092243)
