---
declaration: theorem
origin: cited
lean: Erdos577.erdos_577
statement: formalized
---

# Erdős Problem 577

> *References:*
> - [erdosproblems.com/577](https://www.erdosproblems.com/577)
> - [Wa10] Wang, Hong, *Proof of the Erdős-Faudree conjecture on quadrilaterals*.
>   Graphs Combin. (2010), 833-877. [DOI](https://doi.org/10.1007/s00373-010-0948-3)

*Quoted from [FormalConjectures/ErdosProblems/577.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/577.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/577](https://www.erdosproblems.com/577).

The file states 1 research or textbook statement: 1 solved.

## `Erdos577.erdos_577`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos577.lean](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos577.lean).

> If $G$ is a graph with $4k$ vertices and minimum degree at least $2k$ then $G$ contains $k$
> vertex-disjoint $4$-cycles.
>
> A conjecture of Erdős and Faudree. Proved by Wang [Wa10].

```lean
theorem erdos_577 (k : ℕ) (G : SimpleGraph (Fin (4 * k)))
    (hG : 2 * k ≤ G.minDegree) :
    ∃ cycles : Fin k → (cycleGraph 4).Copy G,
      Pairwise fun i j => Disjoint (Set.range (fun v => cycles i v))
        (Set.range (fun v => cycles j v))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/577.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/577.lean#L46).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/577.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/577.lean)
- [erdosproblems.com/577](https://www.erdosproblems.com/577)
