---
declaration: theorem
origin: cited
lean: Erdos73.erdos_73
statement: formalized
---

# Erdős Problem 73

> *References:*
> - [erdosproblems.com/73](https://www.erdosproblems.com/73)
> - [Re99] Reed, B., Mangoes and Blueberries. Combinatorica (1999), 267-296.

*Quoted from [FormalConjectures/ErdosProblems/73.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/73.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/73](https://www.erdosproblems.com/73).

The file states 1 research or textbook statement: 1 solved.

## `Erdos73.erdos_73`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos73.lean#L122](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos73.lean#L122).

> Let $k\ge 0$. Let $G$ be a graph such that every subgraph $H$ contains an independent set of size
> $\ge (n-k)/2$, where $n$ is the number of vertices of $H$. Must $G$ be the union of a bipartite
> graph and $O_k(1)$ many vertices?
>
> Proved by Reed [Re99].
>
> The linked formal proof (Alexeev and Codex, following Reed's mangoes-and-blueberries argument)
> states the hypothesis as `∀ H : G.Subgraph, H.verts.ncard ≤ 2 * H.coe.indepNum + k` and the
> conclusion as `(G.induce Dᶜ).IsBipartite`, for graphs on `Fin n` (and, equivalently, on any
> finite vertex type); this implies the statement below.

```lean
theorem erdos_73 :
    ∀ (k : ℕ), ∃ (C : ℕ),
      ∀ (V : Type) [Fintype V] (G : SimpleGraph V),
        (∀ (S : Finset V), ∃ (I : Finset V), I ⊆ S ∧ (G.induce (I : Set V)).edgeSet = ∅ ∧
          (I.card : ℝ) ≥ (S.card - k : ℝ) / 2) →
        ∃ (D : Finset V), D.card ≤ C ∧
          (G.induce (D : Set V)ᶜ).Colorable 2
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/73.lean, line 47](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/73.lean#L47).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/73.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/73.lean)
- [erdosproblems.com/73](https://www.erdosproblems.com/73)
