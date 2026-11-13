---
declaration: theorem
origin: cited
lean: Erdos595.erdos_595, Erdos595.erdos_595.variants.folkman_finite, Erdos595.erdos_595.variants.subgraph_of_countable_union, Erdos595.erdos_595.variants.triangle_free_is_union, Erdos595.erdos_595.variants.complete_nat_is_union, Erdos595.erdos_595.variants.K4_not_cliqueFree
statement: formalized
---

# Erdős Problem 595

> *References:*
> - [erdosproblems.com/595](https://www.erdosproblems.com/595)
> - [Er87] Erdős, Paul, Problems and results on set systems and hypergraphs. Extremal problems
>   for finite sets (Visegrád, 1991), Bolyai Soc. Math. Stud. (1994), 217-227.
> - [Fo70] Folkman, Jon, Graphs with monochromatic complete subgraphs in every edge coloring.
>   SIAM J. Appl. Math. (1970), 19:340-345.
> - [NeRo75] Nešetřil, Jaroslav and Rödl, Vojtěch, Type theory of partition problems of graphs.
>   Recent advances in graph theory (Proc. Second Czechoslovak Sympos., Prague, 1974),
>   Academia, Prague (1975), 405-412.

*Quoted from [FormalConjectures/ErdosProblems/595.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/595.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/595](https://www.erdosproblems.com/595).

The file states 6 research or textbook statements: 1 open, 1 solved and 4 textbook results. It also has 1 test statement, counted here but not shown.

## `Erdos595.erdos_595`

Open: stated without proof.

> **Erdős Problem 595 (\$250)**: Is there an infinite graph $G$ which contains no $K_4$ and is
> not the union of countably many triangle-free graphs?
>
> A problem of Erdős and Hajnal [Er87].

```lean
theorem erdos_595 :
    ∃ (V : Type*) (_ : Infinite V) (G : SimpleGraph V),
      G.CliqueFree 4 ∧ ¬IsCountableUnionOfTriangleFree G
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/595.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/595.lean#L54).

## `Erdos595.erdos_595.variants.folkman_finite`

Solved: stated here without proof.

> **Folkman–Nešetřil–Rödl (finite version) [Fo70, NeRo75]**: For every `n ≥ 1`, there exists a
> graph `G` (on a finite vertex set) that contains no $K_4$ and whose edges cannot be covered by
> `n` triangle-free graphs.
>
> More precisely: for every `n : ℕ` with `1 ≤ n`, there exist a finite type `V` and a graph
> `G : SimpleGraph V` with:
> 1. `G.CliqueFree 4` (no $K_4$), and
> 2. For every family `H : Fin n → SimpleGraph V` of triangle-free graphs, `G ≠ ⨆ i, H i`.
>
> This is the finite analogue of Problem 595. The proofs of Folkman [Fo70] and Nešetřil–Rödl
> [NeRo75] give different explicit constructions.

```lean
theorem erdos_595.variants.folkman_finite :
    ∀ n : ℕ, 1 ≤ n →
    ∃ (V : Type*) (_ : Fintype V) (G : SimpleGraph V),
      G.CliqueFree 4 ∧
      ∀ (H : Fin n → SimpleGraph V), (∀ i, (H i).CliqueFree 3) → G ≠ ⨆ i, H i
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/595.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/595.lean#L77).

## `Erdos595.erdos_595.variants.subgraph_of_countable_union`

Textbook result, proved here.

> **Monotonicity**: If `G` is a countable union of triangle-free graphs and `H ≤ G` (i.e., `H` is
> a subgraph of `G`), then `H` is also a countable union of triangle-free graphs.
>
> **Proof**: If `G = ⨆ i, G_i` with each `G_i` triangle-free, then `H = ⨆ i, H ⊓ G_i`.
> Each `H ⊓ G_i` is triangle-free because it is a subgraph of `G_i`.

```lean
theorem erdos_595.variants.subgraph_of_countable_union
    {V : Type*} {G H : SimpleGraph V}
    (hH : H ≤ G) (hG : IsCountableUnionOfTriangleFree G) :
    IsCountableUnionOfTriangleFree H
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/595.lean, line 93](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/595.lean#L93).

## `Erdos595.erdos_595.variants.triangle_free_is_union`

Textbook result, proved here.

> **Triangle-free graphs are trivially countable unions of triangle-free graphs**: if `G` is
> already triangle-free, then `G = ⨆ i : ℕ, G_i` where `G_0 = G` and `G_i = ⊥` for `i ≥ 1`.

```lean
theorem erdos_595.variants.triangle_free_is_union
    {V : Type*} (G : SimpleGraph V) (hG : G.CliqueFree 3) :
    IsCountableUnionOfTriangleFree G
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/595.lean, line 115](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/595.lean#L115).

## `Erdos595.erdos_595.variants.complete_nat_is_union`

Textbook result, proved here.

> **The complete graph `⊤` on `ℕ` is a countable union of triangle-free graphs**: we decompose
> it into the family of star graphs `{H_m}_{m : ℕ}`, where `H_m` is the graph with edges `{m, n}`
> for all `n ≠ m`. Each star is triangle-free (any two non-center vertices share no edge within
> the star), and their union covers all edges of `⊤`.
>
> **Proof sketch (star triangle-free):** If `{a, b, c}` were a triangle in `H_m`, then each of
> the three edges `{a, b}`, `{a, c}`, `{b, c}` would pass through `m`. In particular, from
> `{a, b}` we get `a = m` or `b = m`; from `{b, c}` we get `b = m` or `c = m`. Case analysis
> shows that two vertices must equal `m`, contradicting the triangle having three distinct vertices.

```lean
theorem erdos_595.variants.complete_nat_is_union :
    IsCountableUnionOfTriangleFree (⊤ : SimpleGraph ℕ)
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/595.lean, line 144](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/595.lean#L144).

## `Erdos595.erdos_595.variants.K4_not_cliqueFree`

Textbook result, proved here.

> **The complete graph `⊤` on `Fin 4` is not $K_4$-free**: `⊤` on `Fin 4` equals the complete
> graph $K_4$, so it contains $K_4$ as a subgraph and is not $K_4$-free.
>
> This sanity check confirms the $K_4$-free hypothesis of Problem 595 is non-trivial.

```lean
theorem erdos_595.variants.K4_not_cliqueFree :
    ¬ (⊤ : SimpleGraph (Fin 4)).CliqueFree 4
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/595.lean, line 198](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/595.lean#L198).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/595.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/595.lean)
- [erdosproblems.com/595](https://www.erdosproblems.com/595)
