---
declaration: theorem
origin: cited
lean: OeisA280864.conjecture
statement: formalized
---

# The cup-of-coffee sequence

> The sequence starts with $1, 2$. Each later term is the least unused positive integer such that,
> for every prime, runs of consecutive multiples have length exactly two. The local rule requires
> prime factors that have just appeared to occur once more, and forbids prime factors that occurred
> in both of the preceding terms.
>
> *References:*
> - [A280864](https://oeis.org/A280864)

*Quoted from [FormalConjectures/OEIS/280864.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/280864.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 15 test statements and 2 API statements, counted here but not shown.

## `OeisA280864.conjecture`

Open: stated without proof.

> Conjectured to be a permutation of the positive integers.

```lean
theorem conjecture :
    ∃ a : ℕ → ℕ, FollowsRule a ∧ ∀ k > 0, ∃ n, a n = k
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/280864.lean, line 238](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/280864.lean#L238).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/280864.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/280864.lean)
- [A280864](https://oeis.org/A280864)
