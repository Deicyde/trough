---
declaration: theorem
origin: cited
lean: Erdos842.erdos_842
statement: formalized
---

# Erdős Problem 842

> *References:*
> - [erdosproblems.com/842](https://www.erdosproblems.com/842)
> - [Er92b] Erdős, Paul, _Some of my favourite problems in various branches of combinatorics_.
>   Matematiche (Catania) (1992), 231-240.
> - [FlSt92] Fleischner, Herbert and Stiebitz, Michael, _A solution to a colouring problem of
>   P. Erdős_. Discrete Math. (1992), 39--48.

*Quoted from [FormalConjectures/ErdosProblems/842.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/842.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/842](https://www.erdosproblems.com/842).

The file states 1 research or textbook statement: 1 solved.

## `Erdos842.erdos_842`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos842.lean#L46](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos842.lean#L46).

> Let $G$ be a graph on $3n$ vertices formed by taking $n$ vertex disjoint triangles and adding a
> Hamiltonian cycle (with all new edges) between these vertices. Does $G$ have chromatic number at
> most $3$?
>
> The answer is yes, proved by Fleischner and Stiebitz [FlSt92].

```lean
theorem erdos_842 :
    ∀ (V : Type) (G : SimpleGraph V) (n : ℕ), IsTrianglesPlusHamiltonianCycle G n →
      G.chromaticNumber ≤ 3
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/842.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/842.lean#L54).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/842.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/842.lean)
- [erdosproblems.com/842](https://www.erdosproblems.com/842)
