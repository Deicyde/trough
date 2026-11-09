---
declaration: theorem
origin: cited
lean: Erdos621.erdos_621
statement: formalized
---

# Erdős Problem 621

> *References:*
> - [erdosproblems.com/621](https://www.erdosproblems.com/621)
> - [EGT96] Erdős, Paul and Gallai, Tibor and Tuza, Zsolt, *Covering and independence in triangle
>   structures*. Discrete Math. (1996), 89-101.
> - [Er99] Erdős, Paul, *A selection of problems and results in combinatorics*.
>   Combin. Probab. Comput. (1999), 1-6.
> - [NoSu16] S. Norin and Y.-R. Sun, *Triangle-free independent sets vs. cuts*. arXiv:1602.04370
>   (2016).

*Quoted from [FormalConjectures/ErdosProblems/621.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/621.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/621](https://www.erdosproblems.com/621).

The file states 1 research or textbook statement: 1 solved.

## `Erdos621.erdos_621`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/68da20b96673899166e94638f5a7fffeb7231d35/src/latest/ErdosProblems/Erdos621.lean](https://github.com/plby/lean-proofs/blob/68da20b96673899166e94638f5a7fffeb7231d35/src/latest/ErdosProblems/Erdos621.lean).

> Let $G$ be a graph on $n$ vertices, $\alpha_1(G)$ be the maximum number of edges that contain
> at most one edge from every triangle, and $\tau_1(G)$ be the minimum number of edges that
> contain at least one edge from every triangle.
>
> Is it true that$$\alpha_1(G)+\tau_1(G) \leq \frac{n^2}{4}?$$
>
> A problem of Erdős, Gallai, and Tuza [EGT96], who observe that this is probably quite difficult
> since there are different examples where equality hold: the complete graph, the complete
> bipartite graph, and the graph obtained from $K_{m,m}$ by adding one vertex joined to every
> other.
>
> This is true, and was proved by Norin and Sun [NoSu16], who in fact proved
> that$$\alpha_1(G)+\tau_B(G) \leq \frac{n^2}{4},$$where $\tau_B(G)$ is the minimum number of
> edges that need to be removed to make the graph bipartite.
>
> Here $\alpha_1(G)$ and $\tau_1(G)$ are taken over subsets of the edge set of $G$, and the
> inequality is stated multiplied through by $4$ so that it lives in the natural numbers.
>
> The linked file states $\tau_1$ as the least number of edges whose deletion leaves $G$
> triangle-free, which is the same as meeting every triangle of $G$, and quantifies over an
> arbitrary `Fintype V` rather than `Fin n`.

```lean
theorem erdos_621 :
    ∀ (n : ℕ) (G : SimpleGraph (Fin n)) (a t : ℕ),
      IsGreatest {k : ℕ | ∃ A ⊆ G.edgeFinset, A.card = k ∧
        ∀ x y z : Fin n, G.Adj x y → G.Adj y z → G.Adj x z →
          (({s(x, y), s(y, z), s(x, z)} : Finset (Sym2 (Fin n))) ∩ A).card ≤ 1} a →
      IsLeast {k : ℕ | ∃ T ⊆ G.edgeFinset, T.card = k ∧
        ∀ x y z : Fin n, G.Adj x y → G.Adj y z → G.Adj x z →
          (T ∩ ({s(x, y), s(y, z), s(x, z)} : Finset (Sym2 (Fin n)))).Nonempty} t →
      4 * (a + t) ≤ n ^ 2
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/621.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/621.lean#L65).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/621.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/621.lean)
- [erdosproblems.com/621](https://www.erdosproblems.com/621)
