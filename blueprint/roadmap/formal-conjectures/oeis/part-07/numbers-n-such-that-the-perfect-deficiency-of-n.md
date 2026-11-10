---
declaration: theorem
origin: cited
lean: OeisA108864.conjecture
statement: formalized
---

# Numbers $n$ such that the perfect deficiency of $n$ is $\le 10$.

> The perfect deficiency of $n$ (A109883) is the remainder after greedily subtracting
> from $n$ its divisors in increasing order, skipping any divisor larger than the
> current remainder.
>
> *References:*
> - [A108864](https://oeis.org/A108864)
> - [A109883](https://oeis.org/A109883)

*Quoted from [FormalConjectures/OEIS/108864.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/108864.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA108864.conjecture`

Open: stated without proof.

> Is $1155$ the last odd number in this sequence?
> ($1155$ is the $59$th term starting from $1$, corresponding to $a(58) = 1155$).

```lean
theorem conjecture :
    ∀ n > 58, Even (a n)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/108864.lean, line 105](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/108864.lean#L105).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/108864.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/108864.lean)
- [A108864](https://oeis.org/A108864)
