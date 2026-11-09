---
declaration: theorem
origin: cited
lean: Erdos801.erdos_801
statement: formalized
---

# Erdős Problem 801

> *References:*
> - [erdosproblems.com/801](https://www.erdosproblems.com/801)
> - [Er79g] Erdős, Paul, *Some old and new problems in various branches of combinatorics*.
>   Proceedings of the Tenth Southeastern Conference on Combinatorics, Graph Theory and Computing
>   (Florida Atlantic Univ., Boca Raton, Fla., 1979) (1979), 19-37.
> - [Al96b] Alon, Noga, *Independence numbers of locally sparse graphs and a Ramsey type problem*.
>   Random Structures Algorithms (1996), 271-278.

*Quoted from [FormalConjectures/ErdosProblems/801.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/801.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/801](https://www.erdosproblems.com/801).

The file states 1 research or textbook statement: 1 solved.

## `Erdos801.erdos_801`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos801.lean#L1841](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos801.lean#L1841).

> If $G$ is a graph on $n$ vertices containing no independent set on $>n^{1/2}$ vertices then there
> is a set of $\leq n^{1/2}$ vertices containing $\gg n^{1/2}\log n$ edges.
>
> Proved by Alon [Al96b].

```lean
theorem erdos_801 : ∃ c : ℝ, 0 < c ∧ ∀ᶠ n : ℕ in atTop,
    ∀ G : SimpleGraph (Fin n), (G.indepNum : ℝ) ≤ √n →
      ∃ S : Finset (Fin n), (S.card : ℝ) ≤ √n ∧
        c * √n * Real.log n ≤ (G.induce (S : Set (Fin n))).edgeSet.ncard
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/801.lean, line 47](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/801.lean#L47).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/801.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/801.lean)
- [erdosproblems.com/801](https://www.erdosproblems.com/801)
