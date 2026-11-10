---
declaration: theorem
origin: cited
lean: PebblingNumberConjecture.pebbling_number_conjecture
statement: formalized
---

# Pebbling number conjecture

> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Graph_pebbling)
> - [Pebbling on Graph Products and Other Binary Graph Constructions](https://arxiv.org/abs/1801.07808)

*Quoted from [FormalConjectures/Wikipedia/PebblingNumberConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/PebblingNumberConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 3 API statements, counted here but not shown.

## `PebblingNumberConjecture.pebbling_number_conjecture`

Open: stated without proof.

> The pebbling number conjecture:
> the pebbling number of a Cartesian product of connected graphs is at most equal to the product
> of the pebbling numbers of the factors. See
> [Asplund, Hurlbert, and Kenter](https://arxiv.org/abs/1801.07808).

```lean
theorem pebbling_number_conjecture {W : Type} [Fintype V] [Fintype W] [DecidableEq W]
    (G : SimpleGraph V) (H : SimpleGraph W) (hG : G.Connected) (hH : H.Connected) :
    PebblingNumber (G □ H) ≤ PebblingNumber G * PebblingNumber H
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/PebblingNumberConjecture.lean, line 134](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/PebblingNumberConjecture.lean#L134).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/PebblingNumberConjecture.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/PebblingNumberConjecture.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Graph_pebbling)
