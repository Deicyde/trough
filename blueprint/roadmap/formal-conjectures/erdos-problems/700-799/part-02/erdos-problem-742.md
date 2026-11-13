---
declaration: theorem
origin: cited
lean: Erdos742.erdos_742, Erdos742.variants.plesnik_bound, Erdos742.variants.fan_bound, Erdos742.variants.furedi_bound
statement: formalized
---

# Erdős Problem 742

> *References:*
> - [erdosproblems.com/742](https://www.erdosproblems.com/742)
> - [Pl75] Plesník, Ján, Critical graphs of given diameter. Acta Fac. Rerum Natur. Univ. Comenian.
>   Math. 30 (1975), 71-93.
> - [CaHa79] Caccetta, L. and Häggkvist, R., On diameter critical graphs.
>   Discrete Math. 28 (1979), 223-229.
> - [Fa87] Fan, Genghua, On diameter 2-critical graphs. Discrete Math. 67 (1987), 235-240.
> - [Fü92] Füredi, Zoltán, The maximum number of edges in a minimal graph of diameter 2.
>   J. Graph Theory 16 (1992), 81-98.

*Quoted from [FormalConjectures/ErdosProblems/742.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/742.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/742](https://www.erdosproblems.com/742).

The file states 4 research or textbook statements: 1 open and 3 solved. It also has 1 test statement, counted here but not shown.

## `Erdos742.erdos_742`

Open: stated without proof.

> **Murty-Simon Conjecture**
>
> Let $G$ be a graph on $n$ vertices with diameter $2$ such that deleting any edge increases the
> diameter. Is it true that $G$ has at most $\lfloor n^2 / 4 \rfloor$ edges? Equality is conjectured
> to hold for the complete balanced bipartite graph $K_{\lceil n/2 \rceil, \lfloor n/2 \rfloor}$.
>
> The conjecture is resolved up to a finite check: Fan [Fa87] verified it for $n \leq 24$ and
> $n = 26$, and Füredi [Fü92] proved it for all sufficiently large $n$.

```lean
theorem erdos_742 :
    ∀ (V : Type*) [Fintype V] [DecidableEq V]
    (G : SimpleGraph V) [DecidableRel G.Adj], IsDiameter2Critical G →
    G.edgeFinset.card ≤ (Fintype.card V) ^ 2 / 4
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/742.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/742.lean#L58).

## `Erdos742.variants.plesnik_bound`

Solved: stated here without proof.

> Plesník [Pl75] proved the bound $|E(G)| < 3n(n-1)/8$ for any diameter-$2$-critical graph
> on $n$ vertices.

```lean
theorem plesnik_bound (G : SimpleGraph V) [DecidableRel G.Adj] (hG : IsDiameter2Critical G) :
    (G.edgeFinset.card : ℝ) < 3 * (Fintype.card V : ℝ) * ((Fintype.card V : ℝ) - 1) / 8
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/742.lean, line 103](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/742.lean#L103).

## `Erdos742.variants.fan_bound`

Solved: stated here without proof.

> Fan [Fa87] verified the Murty-Simon conjecture for all $n \leq 24$ and for $n = 26$.

```lean
theorem fan_bound (G : SimpleGraph V) [DecidableRel G.Adj]
    (hn : Fintype.card V ≤ 24 ∨ Fintype.card V = 26) (hG : IsDiameter2Critical G) :
    G.edgeFinset.card ≤ (Fintype.card V) ^ 2 / 4
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/742.lean, line 111](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/742.lean#L111).

## `Erdos742.variants.furedi_bound`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos742.lean#L4279](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos742.lean#L4279).

> Füredi [Fü92] proved the Murty-Simon conjecture for all sufficiently large $n$, that is, there
> exists $n_0$ such that every diameter-$2$-critical graph on $n \geq n_0$ vertices has at most
> $\lfloor n^2 / 4 \rfloor$ edges.

```lean
theorem furedi_bound : ∃ n₀ : ℕ, ∀ (V : Type*) [Fintype V] [DecidableEq V]
    (G : SimpleGraph V) [DecidableRel G.Adj],
    n₀ ≤ Fintype.card V → IsDiameter2Critical G →
      G.edgeFinset.card ≤ (Fintype.card V) ^ 2 / 4
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/742.lean, line 124](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/742.lean#L124).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/742.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/742.lean)
- [erdosproblems.com/742](https://www.erdosproblems.com/742)
