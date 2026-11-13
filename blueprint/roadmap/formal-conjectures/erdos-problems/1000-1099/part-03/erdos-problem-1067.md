---
declaration: theorem
origin: cited
lean: Erdos1067.erdos_1067, Erdos1067.erdos_1067.variants.infinite_edge_connectivity
statement: formalized
---

# Erdős Problem 1067

> *References:*
> - [erdosproblems.com/1067](https://www.erdosproblems.com/1067)
> - [BoPi24] N. Bowler and M. Pitz, A note on uncountably chromatic graphs. arXiv:2402.05984 (2024).
> - [ErHa66] Erdős, P. and Hajnal, A., On chromatic number of graphs and set-systems. Acta Math. Acad.
>   Sci. Hungar. (1966), 61-99.
> - [Ko13] Komjáth, Péter, A note on chromatic number and connectivity of infinite graphs. Israel
>   J. Math. (2013), 499--506.
> - [So15] Soukup, Dániel T., Trees, ladders and graphs. J. Combin. Theory Ser. B (2015), 96--116.
> - [Th17] Thomassen, Carsten, Infinitely connected subgraphs in graphs of uncountable chromatic
>   number. Combinatorica (2017), 785--793.

*Quoted from [FormalConjectures/ErdosProblems/1067.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1067.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1067](https://www.erdosproblems.com/1067).

The file states 2 research or textbook statements: 2 solved.

## `Erdos1067.erdos_1067`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.24.0/ErdosProblems/Erdos1067.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.24.0/ErdosProblems/Erdos1067.lean).

> Does every graph with chromatic number $\aleph_1$ contain an infinitely connected subgraph with
> chromatic number $\aleph_1$?
>
> Komjáth [Ko13] proved that it is consistent that the answer is no. This was improved by
> Soukup [So15], who constructed a counterexample using no extra set-theoretical assumptions. A
> simpler elementary example was given by Bowler and Pitz [BoPi24].
>
> This was formalized in Lean by Alexeev using Aristotle and Aleph Prover.

```lean
theorem erdos_1067 :
    ¬ ∀ (V : Type) (G : SimpleGraph V), G.chromaticCardinal = ℵ_ 1 →
      ∃ (H : G.Subgraph), H.coe.chromaticCardinal = ℵ_ 1 ∧ InfinitelyConnected H.coe
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1067.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1067.lean#L61).

## `Erdos1067.erdos_1067.variants.infinite_edge_connectivity`

Solved: stated here without proof.

> Does every graph with chromatic number $\aleph_1$ contain an infinitely edge-connected subgraph
> with chromatic number $\aleph_1$?
>
> Thomassen [Th17] proved that the answer is yes: every graph of uncountable chromatic number has a
> subgraph with infinite edge-connectivity and uncountable chromatic number.

```lean
theorem erdos_1067.variants.infinite_edge_connectivity :
    ∀ (V : Type) (G : SimpleGraph V), G.chromaticCardinal = ℵ_ 1 →
      ∃ (H : G.Subgraph), H.coe.chromaticCardinal = ℵ_ 1 ∧ InfinitelyEdgeConnected H.coe
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1067.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1067.lean#L74).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1067.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1067.lean)
- [erdosproblems.com/1067](https://www.erdosproblems.com/1067)
