---
declaration: theorem
origin: cited
lean: Erdos915.erdos_915, Erdos915.erdos_915.variants.edge_disjoint
statement: formalized
---

# Erdős Problem 915

> *References:*
> - [erdosproblems.com/915](https://www.erdosproblems.com/915)
> - [BoEr62] Bollobás, Béla and Erdős, Pál, *Extremal problems in graph theory*. Mat. Lapok (1962),
>   143--152.
> - [Er67b] Erdős, Paul, *Extremal problems in graph theory*. A Seminar on Graph Theory (1967),
>   54-59.
> - [Ba60] P. Bártfai, *Solution of a problem posed by P. Erdős*. Mat. Lapok (1960), 175-176.
> - [Bo66] Bollobás, B., *On graphs with at most three independent paths connecting any two
>   vertices*. Studia Sci. Math. Hungar. (1966), 137--140.
> - [Le73] Leonard, John L., *On a conjecture of Bollobás and Erdős*. Period. Math. Hungar. (1973),
>   281--284.
> - [Ma73] Mader, W., *Ein Extremalproblem des Zusammenhangs von Graphen*. Math. Z. (1973),
>   223--231.
> - [SoTh74] Sørensen, Bo Aagaard and Thomassen, Carsten, *On $k$-rails in graphs*. J.
>   Combinatorial Theory Ser. B (1974), 143--159.

*Quoted from [FormalConjectures/ErdosProblems/915.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/915.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/915](https://www.erdosproblems.com/915).

The file states 2 research or textbook statements: 2 solved.

## `Erdos915.erdos_915`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos915.lean#L362](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos915.lean#L362).

> Let $G$ be a graph with $1+n(m-1)$ vertices and $1+n\binom{m}{2}$ edges. Must $G$ contain two
> points which are connected by $m$ disjoint paths?
>
> A conjecture of Bollobás and Erdős [BoEr62]. This would be the best possible, as demonstrated by
> $n$ copies of $K_m$ which share a single vertex (but are otherwise disjoint). It is unclear
> whether disjoint here is to mean edge-disjoint or (internally) vertex-disjoint. The above
> construction is valid for either interpretation.
>
> This is the internally vertex-disjoint reading. It is trivial for $m = 2$, and was proved for
> $m = 3$ by Bártfai [Ba60] and for $m = 4$ by Bollobás [Bo66]. Leonard [Le73] disproved this
> conjecture for $m=5$, giving an explicit counterexample with $57$ vertices and $141$ edges, and
> Mader [Ma73] disproved the conjecture in general for all $m \geq 6$. Sørensen and Thomassen
> [SoTh74] proved that the conjectured bound of Bollobás and Erdős holds if the graph is
> $3$-connected.

```lean
theorem erdos_915 :
    ¬ ∀ m n : ℕ, 2 ≤ m → 1 ≤ n → ∀ (V : Type) [Fintype V] (G : SimpleGraph V),
      Fintype.card V = 1 + n * (m - 1) → G.edgeSet.ncard = 1 + n * m.choose 2 →
        ∃ u v : V, u ≠ v ∧ ∃ P : Finset (G.Walk u v), P.card = m ∧ (∀ p ∈ P, p.IsPath) ∧
          (P : Set (G.Walk u v)).Pairwise InternallyDisjoint
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/915.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/915.lean#L65).

## `Erdos915.erdos_915.variants.edge_disjoint`

Solved: stated here without proof.

> The edge-disjoint reading of [erdős_915](https://www.erdosproblems.com/915). Mader [Ma73] proved
> that if a graph with $n$ vertices has more than
> $$\frac{m}{2}(n-1)-\frac{1}{2}(e_0(G)+\cdots+e_{m-2}(G))$$
> edges then $G$ contains two vertices connected by $m$ edge-disjoint paths (where $e_r(G)$ counts
> the number of vertices of degree $\leq r$). In particular, this confirms (and is stronger than)
> the conjecture.

```lean
theorem erdos_915.variants.edge_disjoint :
    ∀ m n : ℕ, 2 ≤ m → 1 ≤ n → ∀ (V : Type) [Fintype V] (G : SimpleGraph V),
      Fintype.card V = 1 + n * (m - 1) → G.edgeSet.ncard = 1 + n * m.choose 2 →
        ∃ u v : V, u ≠ v ∧ ∃ P : Finset (G.Walk u v), P.card = m ∧ (∀ p ∈ P, p.IsPath) ∧
          (P : Set (G.Walk u v)).Pairwise fun p q => List.Disjoint p.edges q.edges
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/915.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/915.lean#L81).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/915.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/915.lean)
- [erdosproblems.com/915](https://www.erdosproblems.com/915)
