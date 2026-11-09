---
declaration: theorem
origin: cited
lean: Arxiv.«2607.06396».alon_tarsi_short_cycle_cover
statement: formalized
---

# The Alon-Tarsi short cycle cover conjecture

> *References:*
> - [AlTa85] Alon, N. and Tarsi, M., Covering multigraphs by simple circuits.
>   SIAM J. Algebraic Discrete Methods (1985), 345--350.
> - [arxiv/2607.06396](https://arxiv.org/abs/2607.06396)
>   **Some new results on Sylvester colorings of cubic graphs**
>   by *Luca Ferrarini, Vahan Mkrtchyan*, where this is Conjecture 4.
>
> This file states the finite simple-graph specialization of the source, which allows parallel edges.
>
> Every bridgeless simple graph has a list of cycles covering every edge whose lengths sum to at most
> $\frac{7}{5}|E|$.

*Quoted from [FormalConjectures/Arxiv/2607.06396/AlonTarsi.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2607.06396/AlonTarsi.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 2 test statements and 5 API statements, counted here but not shown.

## `Arxiv.«2607.06396».alon_tarsi_short_cycle_cover`

Open: stated without proof.

> **Conjecture 4 (Alon-Tarsi, 1985), simple-graph specialization.** Every bridgeless simple graph
> has a list of cycles covering
> every edge, with $\sum_{C} |E(C)| \leq \frac{7}{5}|E(G)|$.

```lean
theorem alon_tarsi_short_cycle_cover :
    ∀ (V : Type) [Fintype V] [DecidableEq V] (G : SimpleGraph V)
      [DecidableRel G.Adj], G.IsBridgeless →
      ∃ C : Multiset (Cycle G), IsCycleCover G C ∧
        (totalLength C : ℚ) ≤ 7 / 5 * #G.edgeFinset
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Arxiv/2607.06396/AlonTarsi.lean, line 89](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2607.06396/AlonTarsi.lean#L89).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Arxiv/2607.06396/AlonTarsi.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2607.06396/AlonTarsi.lean)
- [arxiv/2607.06396](https://arxiv.org/abs/2607.06396)
