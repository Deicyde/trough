---
declaration: theorem
origin: cited
lean: Taxicab.taxicab_for_5_2_2, Taxicab.taxicab_for_5_2_n
statement: formalized
---

# Taxicab numbers

> A *taxicab number* for natural numbers $k, m, n$ is the
> smallest number $x$ that can be expressed as a sum of $m$
> positive $k$-th powers in at least $n$ distinct ways. The
> most famous taxicab number is
> $ 1729 = 1³ + 12³ = 9³ + 10³, $
> also known as the Hardy–Ramanujan number.
>
> However, a taxicab number is not known for $k=5$, $m=2$, and any $n ≥ 2$:
> No positive integer is known that can be written as the
> sum of two 5th powers in more than one way, and it is not
> known whether such a number exists.
>
> In particular, it is not known whether there exists a
> taxicab number for $k=5$, $m=2$, and $n=2$.
>
> *References:*
>  - [Wikipedia](https://en.wikipedia.org/wiki/Taxicab_number)
>  - [Generalized taxicab number](https://en.wikipedia.org/wiki/Generalized_taxicab_number)
>  - [OEIS taxicab cubes](https://oeis.org/A001235)
>  - [OEIS taxicab 4th powers](https://oeis.org/A018786)
>  - [OEIS taxicab conjecture](https://oeis.org/A088703)

*Quoted from [FormalConjectures/Wikipedia/Taxicab.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Taxicab.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 3 test statements, counted here but not shown.

## `Taxicab.taxicab_for_5_2_2`

Open: stated without proof.

> Taxicab number for $k=5$, $m=2$, and $n=2$ is not known.
> Whether such a number exists is also not known.

```lean
theorem taxicab_for_5_2_2 : ∃ x : ℕ, IsTaxicabFor 5 2 2 x
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Taxicab.lean, line 101](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Taxicab.lean#L101).

## `Taxicab.taxicab_for_5_2_n`

Open: stated without proof.

> Taxicab number for $k=5$ and $m=2$ is not-known for any $n ≥ 2$.
> Whether such a number exists is also not known.

```lean
theorem taxicab_for_5_2_n : ∃ n : ℕ, n ≥ 2 ∧ (∃ x : ℕ, IsTaxicabFor 5 2 n x)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Taxicab.lean, line 107](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Taxicab.lean#L107).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/Taxicab.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Taxicab.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Taxicab_number)
