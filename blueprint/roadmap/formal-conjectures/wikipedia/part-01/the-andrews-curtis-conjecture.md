---
declaration: theorem
origin: cited
lean: AndrewsCurtis.andrews_curtis_conjecture
statement: formalized
---

# The Andrews-Curtis conjecture

> The conjecture says that every normally generating `n`-tuple in the free group
> on `n` generators is Andrews-Curtis equivalent to the standard free basis.
>
> References:
>
> * [Wikipedia, Andrews-Curtis conjecture](https://en.wikipedia.org/wiki/Andrews%E2%80%93Curtis_conjecture)
> * [A. D. Myasnikov, A. G. Myasnikov and V. Shpilrain,
>   *On the Andrews-Curtis equivalence*](https://arxiv.org/abs/math/0302080)

*Quoted from [FormalConjectures/Wikipedia/AndrewsCurtis.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/AndrewsCurtis.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `AndrewsCurtis.andrews_curtis_conjecture`

Open: stated without proof.

> **The Andrews-Curtis conjecture.**
>
> Every normally generating `n`-tuple in the free group of rank `n` is
> Andrews-Curtis equivalent to the standard tuple of free generators.

```lean
theorem andrews_curtis_conjecture (n : ℕ) (r : RelatorTuple n)
    (hr : NormallyGenerates r) :
    Equivalent r (standardRelators n)
```

Category `research open`; AMS [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/Wikipedia/AndrewsCurtis.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/AndrewsCurtis.lean#L77).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/AndrewsCurtis.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/AndrewsCurtis.lean)
- [Wikipedia, Andrews-Curtis conjecture](https://en.wikipedia.org/wiki/Andrews%E2%80%93Curtis_conjecture)
