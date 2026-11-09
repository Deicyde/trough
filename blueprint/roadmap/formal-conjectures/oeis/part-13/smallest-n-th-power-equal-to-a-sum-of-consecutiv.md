---
declaration: theorem
origin: cited
lean: OeisA230718.conjecture
statement: formalized
---

# Smallest $n$-th power equal to a sum of consecutive immediately preceding positive $n$-th powers

> Smallest $n$-th power equal to a sum of some consecutive, immediately preceding, positive $n$-th
> powers, or $0$ if none.
>
> *References:*
> - [A230718](https://oeis.org/A230718)

*Quoted from [FormalConjectures/OEIS/230718.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/230718.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 4 test statements, counted here but not shown.

## `OeisA230718.conjecture`

Open: stated without proof.

> Is $a(n) \ne 0$ for any $n > 3$?

```lean
theorem conjecture : ∃ n > 3, a n ≠ 0
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/230718.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/230718.lean#L71).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/230718.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/230718.lean)
- [A230718](https://oeis.org/A230718)
