---
declaration: theorem
origin: cited
lean: Arxiv.«1601.03081».crystals_components_unique
statement: formalized
---

# Unique Crystal Components

> *Reference:* [arxiv/1601.03081](https://arxiv.org/abs/1601.03081)
> **The Biharmonic mean**
> by *Marco Abrate, Stefano Barbero, Umberto Cerruti, Nadir Murru*

*Quoted from [FormalConjectures/Arxiv/1601.03081/UniqueCrystalComponents.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/1601.03081/UniqueCrystalComponents.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 1 test statement and 6 API statements, counted here but not shown.

## `Arxiv.«1601.03081».crystals_components_unique`

Open: stated without proof.

> If $n = ab$ is a crystal, then there are no other pairs of
> positive integers $c, d > 1$, different from the couple $a, b$, such that $n = cd$ and
> $B(c, d) ∈ ℕ$, i.e., the components of the crystals are unique.

```lean
theorem crystals_components_unique (n a b c d : ℕ)
    (hab : IsCrystalWithComponents n a b) (hcd : IsCrystalWithComponents n c d) :
    ({a, b} : Finset ℕ) = {c, d}
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [26 Real functions](../../by-subject/part-01/26-real-functions/README.md). Declared in [FormalConjectures/Arxiv/1601.03081/UniqueCrystalComponents.lean, line 122](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/1601.03081/UniqueCrystalComponents.lean#L122).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Arxiv/1601.03081/UniqueCrystalComponents.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/1601.03081/UniqueCrystalComponents.lean)
- [arxiv/1601.03081](https://arxiv.org/abs/1601.03081)
