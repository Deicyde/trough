---
declaration: theorem
origin: cited
lean: Superperfect.twoFivePerfect
statement: formalized
---

# (m,k)-perfect numbers

> A positive integer $n$ is $(m,k)$-perfect if $\sigma^m(n)=kn$, where $\sigma^m$ is the
> $m$-th iterate of the sum-of-divisors function.
>
> *References:*
>  - [Wikipedia](https://en.wikipedia.org/wiki/Superperfect_number#Generalizations)
>  - [Wikipedia](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_mathematics#General)

*Quoted from [FormalConjectures/Wikipedia/Superperfectnumbers.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Superperfectnumbers.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 1 test statement, counted here but not shown.

## `Superperfect.twoFivePerfect`

Open: stated without proof.

> There does not exist a $(2,5)$-perfect number

```lean
theorem twoFivePerfect : ¬ ∃ n, Nat.IsPerfectFor n 2 5
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Superperfectnumbers.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Superperfectnumbers.lean#L45).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/Superperfectnumbers.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Superperfectnumbers.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Superperfect_number#Generalizations)
