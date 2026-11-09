---
declaration: theorem
origin: cited
lean: Toronto.DiscreteTopology.of_t2_of_torontoSpace
statement: formalized
---

# Toronto spaces

> A *Toronto space* is a topological space
> which is homeomorphic to all of its subspaces of same cardinality.
>
> It is conjectured that every T2, Toronto space is discrete.
> W.R. Brian proved that this holds under GCH.
>
> *References:*
>  - [Wikipedia](https://en.wikipedia.org/wiki/Toronto_space)
>  - [The Toronto problem](https://wrbrian.wordpress.com/wp-content/uploads/2012/01/thetorontoproblem.pdf) by *W.R. Brian*

*Quoted from [FormalConjectures/Wikipedia/Toronto.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Toronto.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 1 test statement, counted here but not shown.

## `Toronto.DiscreteTopology.of_t2_of_torontoSpace`

Open: stated without proof.

> Any T2, Toronto space is discrete.

```lean
theorem DiscreteTopology.of_t2_of_torontoSpace [T2Space X] [TorontoSpace X] :
    DiscreteTopology X
```

Category `research open`; AMS [54 General topology](../../by-subject/part-02/54-general-topology/README.md). Declared in [FormalConjectures/Wikipedia/Toronto.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Toronto.lean#L66).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/Toronto.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Toronto.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Toronto_space)
