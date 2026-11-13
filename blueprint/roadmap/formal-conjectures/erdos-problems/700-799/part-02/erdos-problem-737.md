---
declaration: theorem
origin: cited
lean: Erdos737.erdos_737, Erdos737.erdos_737.variants.uncountable
statement: formalized
---

# Erdős Problem 737

> *References:*
> - [erdosproblems.com/737](https://www.erdosproblems.com/737)
> - [EHS74] Erdős, P. and Hajnal, A. and Shelah, S., *On some general properties of chromatic
>   numbers*. Topics in topology (Proc. Colloq., Keszthely, 1972) (1974), 243-255.
> - [Th83] Thomassen, Carsten, *Cycles in graphs of uncountable chromatic number*. Combinatorica
>   (1983), 133-134.

*Quoted from [FormalConjectures/ErdosProblems/737.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/737.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/737](https://www.erdosproblems.com/737).

The file states 2 research or textbook statements: 2 solved. It also has 1 test statement, counted here but not shown.

## `Erdos737.erdos_737`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos737.lean#L1266](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos737.lean#L1266).

> Let $G$ be a graph with chromatic number $\aleph_1$. Must there exist an edge $e$ such that, for
> all large $n$, $G$ contains a cycle of length $n$ containing $e$?
>
> The answer is yes, proved by Thomassen [Th83]. Erdős, Hajnal, and Shelah [EHS74] proved that $G$
> must contain all sufficiently large cycles (see Erdős Problem 594).

```lean
theorem erdos_737 :
    ∀ (V : Type) (G : SimpleGraph V), ChromaticNumberAlephOne G →
      ∃ e ∈ G.edgeSet, ∃ N : ℕ, ∀ n : ℕ, N ≤ n →
        CycleThroughEdgeOfLength G e n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/737.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/737.lean#L65).

## `Erdos737.erdos_737.variants.uncountable`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos737.lean#L1181](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos737.lean#L1181).

> The title and abstract of [Th83] state the result for graphs of uncountable chromatic number,
> that is, graphs with no proper colouring by `ℕ`. This is stronger than `erdos_737`.

```lean
theorem erdos_737.variants.uncountable :
    ∀ (V : Type) (G : SimpleGraph V), IsEmpty (G.Coloring ℕ) →
      ∃ e ∈ G.edgeSet, ∃ N : ℕ, ∀ n : ℕ, N ≤ n →
        CycleThroughEdgeOfLength G e n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/737.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/737.lean#L78).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/737.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/737.lean)
- [erdosproblems.com/737](https://www.erdosproblems.com/737)
