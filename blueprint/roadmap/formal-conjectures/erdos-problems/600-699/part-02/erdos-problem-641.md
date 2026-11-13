---
declaration: theorem
origin: cited
lean: Erdos641.erdos_641
statement: formalized
---

# Erdős Problem 641

> *References:*
> - [erdosproblems.com/641](https://www.erdosproblems.com/641)
> - [Er92b] Erdős, Paul, *Some of my favourite problems in various branches of combinatorics*.
>   Le Matematiche (1992), 231–240.
> - [Er97d] Erdős, Paul, *Some recent problems and results in graph theory*.
>   Discrete Math. (1997), 81–85, p.84.
> - [JSS24] Janzer, Barnabás, Steiner, Raphael, and Sudakov, Benny,
>   *Chromatic number and regular subgraphs*. arXiv:2410.02437 (2024).

*Quoted from [FormalConjectures/ErdosProblems/641.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/641.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/641](https://www.erdosproblems.com/641).

The file states 1 research or textbook statement: 1 solved.

## `Erdos641.erdos_641`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos641.lean](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos641.lean).

> Is there some function $f$ such that for all $k\geq 1$ if a finite graph $G$ has chromatic
> number $\geq f(k)$ then $G$ has $k$ edge disjoint cycles on the same set of vertices?
>
> A problem of Erdős and Hajnal. This was resolved in the negative by Janzer, Steiner,
> and Sudakov [JSS24] - in fact, this fails even at $k=2$.

```lean
theorem erdos_641 : ¬ ∃ f : ℕ → ℕ, ErdosHajnalProperty f
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/641.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/641.lean#L70).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/641.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/641.lean)
- [erdosproblems.com/641](https://www.erdosproblems.com/641)
