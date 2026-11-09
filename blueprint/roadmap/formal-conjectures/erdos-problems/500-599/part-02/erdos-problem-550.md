---
declaration: theorem
origin: cited
lean: Erdos550.erdos_550
statement: formalized
---

# Erdős Problem 550

> *References:*
> - [erdosproblems.com/550](https://www.erdosproblems.com/550)
> - [Ch77] Chvátal, V., Tree-complete graph Ramsey numbers. J. Graph Theory (1977), 93.
> - [Li26] Li, E., *A Resolution of Erdős Problem 550 on Tree versus Complete Multipartite Ramsey
>   Numbers*, [arXiv:2606.23659](https://arxiv.org/abs/2606.23659) (2026).

*Quoted from [FormalConjectures/ErdosProblems/550.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/550.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/550](https://www.erdosproblems.com/550).

The file states 1 research or textbook statement: 1 solved.

## `Erdos550.erdos_550`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos550/Main.lean#L80](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos550/Main.lean#L80).

> Let $m_1\leq\cdots\leq m_k$ and $n$ be sufficiently large. If $T$ is a tree on $n$ vertices
> and $G$ is the complete multipartite graph with vertex class sizes $m_1,\ldots,m_k$ then prove that
> $$R(T,G)\leq (\chi(G)-1)(R(T,K_{m_1,m_2})-1)+m_1.$$
>
> This problem is #16 in Ramsey Theory in the graphs problem collection.
>
> Li [Li26] proved this, combining an off-Turán tree-embedding theorem with a compactness theorem
> for bounded-rank hypergraph obstructions. The linked formal proof states the bound for trees on an
> arbitrary finite vertex type and with `K_{m_1,m_2}` written as a complete multipartite graph with
> two parts; the statement below is the special case `V = Fin n`.

```lean
theorem erdos_550 :
    ∀ (k : ℕ) (hk : 2 ≤ k) (m : Fin k → ℕ) (hm : Monotone m)
      (hm_pos : ∀ i, 0 < m i),
      ∀ᶠ n : ℕ in atTop,
        ∀ (T : SimpleGraph (Fin n)), T.IsTree →
          SimpleGraph.graphRamsey T
            (SimpleGraph.completeMultipartiteGraph (fun i ↦ Fin (m i))) ≤
            (k - 1) * (SimpleGraph.graphRamsey T
              (completeBipartiteGraph (Fin (m ⟨0, by omega⟩)) (Fin (m ⟨1, by omega⟩))) - 1) +
                m ⟨0, by omega⟩
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/550.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/550.lean#L51).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/550.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/550.lean)
- [erdosproblems.com/550](https://www.erdosproblems.com/550)
