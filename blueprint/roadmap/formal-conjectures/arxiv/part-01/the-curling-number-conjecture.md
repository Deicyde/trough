---
declaration: theorem
origin: cited
lean: Arxiv.«0912.2382».curling_number_conjecture
statement: formalized
---

# The Curling Number Conjecture

> *Reference:* [arxiv/0912.2382](https://arxiv.org/abs/0912.2382)
> **The Curling Number Conjecture**
> by *Benjamin Chaffin and N. J. A. Sloane*

*Quoted from [FormalConjectures/Arxiv/0912.2382/CurlingNumberConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/0912.2382/CurlingNumberConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 2 test statements and 7 API statements, counted here but not shown.

## `Arxiv.«0912.2382».curling_number_conjecture`

Open: stated without proof.

> Starting from any nonempty finite integer sequence, repeatedly appending its curling number
> eventually gives a sequence with curling number $1$ [Chaffin and Sloane, Conjecture 1].

```lean
theorem curling_number_conjecture (S₀ : List ℤ) (h : S₀ ≠ []) : ∃ m, k (S S₀ m) = 1
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Arxiv/0912.2382/CurlingNumberConjecture.lean, line 130](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/0912.2382/CurlingNumberConjecture.lean#L130).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Arxiv/0912.2382/CurlingNumberConjecture.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/0912.2382/CurlingNumberConjecture.lean)
- [arxiv/0912.2382](https://arxiv.org/abs/0912.2382)
