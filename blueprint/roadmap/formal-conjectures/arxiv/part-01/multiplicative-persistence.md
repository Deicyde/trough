---
declaration: theorem
origin: cited
lean: Arxiv.«2110.04263».multiplicative_persistence_conjecture
statement: formalized
---

# Multiplicative persistence

> Multiply the decimal digits of a natural number, then repeat. The multiplicative-persistence
> conjecture says that a single digit is always reached in at most eleven steps.
>
> *References:*
> * Eric Brier, Christophe Clavier, Linda Gutsche, and David Naccache,
>   [*The Multiplicative Persistence Conjecture Is True for Odd Targets*](
>   https://arxiv.org/abs/2110.04263)
> * [OEIS A003001](https://oeis.org/A003001)

*Quoted from [FormalConjectures/Arxiv/2110.04263/MultiplicativePersistence.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Arxiv/2110.04263/MultiplicativePersistence.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 8 test statements, counted here but not shown.

## `Arxiv.«2110.04263».multiplicative_persistence_conjecture`

Open: stated without proof.

> The multiplicative-persistence conjecture: every natural number reaches a single decimal digit
> after at most eleven iterations of the digit-product map.
>
> The bound is sharp: $277777788888899$ has multiplicative persistence eleven.
>
> *Reference:* [arXiv:2110.04263](https://arxiv.org/abs/2110.04263)

```lean
theorem multiplicative_persistence_conjecture :
    ∀ n : ℕ, ∃ k ≤ 11, (digitProduct^[k]) n < 10
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Arxiv/2110.04263/MultiplicativePersistence.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Arxiv/2110.04263/MultiplicativePersistence.lean#L99).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Arxiv/2110.04263/MultiplicativePersistence.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Arxiv/2110.04263/MultiplicativePersistence.lean)
- [https://arxiv.org/abs/2110.04263](https://arxiv.org/abs/2110.04263)
