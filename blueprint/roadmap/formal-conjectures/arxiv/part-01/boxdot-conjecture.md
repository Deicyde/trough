---
declaration: theorem
origin: cited
lean: Arxiv.«1308.0994».BoxdotConjecture
statement: formalized
---

# Boxdot Conjecture

> The Boxdot Conjecture was originally formulated by French and Humberstone and
> has been studied in several works. In particular, see:
>
> *References:*
> - [arxiv/1308.0994](https://arxiv.org/abs/1308.0994)
>   **Cluster Expansion and the Boxdot Conjecture** by *Emil Jeřábek*
> - [The Boxdot Conjecture and the Generalized McKinsey Axiom](https://ojs.victoria.ac.nz/ajl/article/view/4891)
>   by *Christopher Steinsvold*, Australasian Journal of Logic

*Quoted from [FormalConjectures/Arxiv/1308.0994/BoxdotConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/1308.0994/BoxdotConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 3 API statements, counted here but not shown.

## `Arxiv.«1308.0994».BoxdotConjecture`

Solved: stated here; a Lean proof is at [https://github.com/FormalizedFormalLogic/ModalLogic/blob/bdadfabed4167bc8b947cc368451ce83cd30a017/ModalLogicArchive/Modal/Boxdot/Jerabek.lean](https://github.com/FormalizedFormalLogic/ModalLogic/blob/bdadfabed4167bc8b947cc368451ce83cd30a017/ModalLogicArchive/Modal/Boxdot/Jerabek.lean).

> Boxdot Conjecture: every normal modal logic that faithfully interprets KT
> by the boxdot translation is included in KT.

```lean
theorem BoxdotConjecture (L : NormalModalLogic) (H : ∀ φ, L ⊢ ■ φ ↔ KT ⊢ φ) : L.thms ⊆ KT.thms
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md). Declared in [FormalConjectures/Arxiv/1308.0994/BoxdotConjecture.lean, line 238](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/1308.0994/BoxdotConjecture.lean#L238).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Arxiv/1308.0994/BoxdotConjecture.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/1308.0994/BoxdotConjecture.lean)
- [arxiv/1308.0994](https://arxiv.org/abs/1308.0994)
