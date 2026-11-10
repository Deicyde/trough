---
declaration: theorem
origin: cited
lean: OeisA331631.conjecture
statement: formalized
---

# Tripling until the seed's digits reappear

> Starting with the least positive integer not used previously, repeatedly triple it and stop the
> block at the first positive power whose decimal expansion contains the seed's digits. Then repeat
> from the new least missing positive integer.
>
> *References:*
> - [A331631](https://oeis.org/A331631)

*Quoted from [FormalConjectures/OEIS/331631.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/331631.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 21 test statements and 1 API statement, counted here but not shown.

## `OeisA331631.conjecture`

Open: stated without proof.

> [OEIS A331631](https://oeis.org/A331631) states:
> The sequence is conjectured to be a permutation of the positive integers
> (see the Crossrefs section).

```lean
theorem conjecture :
    ∃ a : ℕ → ℕ, FollowsRule a ∧ Function.Injective a ∧
      ∀ k > 0, ∃ n, a n = k
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/331631.lean, line 255](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/331631.lean#L255).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/331631.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/331631.lean)
- [A331631](https://oeis.org/A331631)
