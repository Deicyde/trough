---
declaration: theorem
origin: cited
lean: Erdos1068.erdos_1068
statement: formalized
---

# Erdős Problem 1068

> *Reference:* [erdosproblems.com/1068](https://www.erdosproblems.com/1068)

*Quoted from [FormalConjectures/ErdosProblems/1068.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1068.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1068](https://www.erdosproblems.com/1068).

The file states 1 research or textbook statement: 1 open.

## `Erdos1068.erdos_1068`

Open: stated without proof.

> Does every graph with chromatic number $\aleph_1$ contain a countable subgraph which is
> infinitely connected?

```lean
theorem erdos_1068 :
    ∀ (V : Type) (G : SimpleGraph V), G.chromaticCardinal = ℵ_  1 →
      ∃ s : Set V, s.Countable ∧ InfinitelyConnected (G.induce s)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1068.lean, line 37](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1068.lean#L37).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1068.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1068.lean)
- [erdosproblems.com/1068](https://www.erdosproblems.com/1068)
