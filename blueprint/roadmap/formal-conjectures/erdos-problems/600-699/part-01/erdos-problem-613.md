---
declaration: theorem
origin: cited
lean: Erdos613.erdos_613
statement: formalized
---

# Erdős Problem 613

> *Reference:* [erdosproblems.com/613](https://www.erdosproblems.com/613)

*Quoted from [FormalConjectures/ErdosProblems/613.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/613.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/613](https://www.erdosproblems.com/613).

The file states 1 research or textbook statement: 1 solved.

## `Erdos613.erdos_613`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/1268917deaaaa0d674f651287027baa26cea9920/src/latest/ErdosProblems/Erdos613.lean#L1170](https://github.com/plby/lean-proofs/blob/1268917deaaaa0d674f651287027baa26cea9920/src/latest/ErdosProblems/Erdos613.lean#L1170).

> **Erdős Problem 613:**
> Let $n \geq 3$ and $G$ be a graph with $\binom{2n+1}{2} - \binom{n}{2} - 1$ edges.
> Must $G$ be the union of a bipartite graph and a graph with maximum degree less than $n$?

```lean
theorem erdos_613 :
    ¬ ∀ n ≥ 3, ∀ (V : Type*) [Fintype V] (G : SimpleGraph V), [DecidableRel G.Adj] →
      G.edgeFinset.card = Nat.choose (2 * n + 1) 2 - Nat.choose n 2 - 1 →
      ∃ (B D : SimpleGraph V), [DecidableRel B.Adj] → [DecidableRel D.Adj] →
        G = B ⊔ D ∧ B.IsBipartite ∧ ∀ v, D.degree v < n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/613.lean, line 37](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/613.lean#L37).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/613.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/613.lean)
- [erdosproblems.com/613](https://www.erdosproblems.com/613)
