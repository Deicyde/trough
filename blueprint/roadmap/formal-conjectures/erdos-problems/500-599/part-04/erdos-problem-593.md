---
declaration: theorem
origin: cited
lean: Erdos593.erdos_593, Erdos593.erdos_593.variants.obligatory_implies_two_colorable, Erdos593.erdos_593.variants.two_colorable_implies_obligatory, Erdos593.erdos_593.variants.common_pair_not_obligatory, Erdos593.erdos_593.variants.graph_case_bipartite_obligatory, Erdos593.erdos_593.variants.graph_case_no_odd_cycle, Erdos593.erdos_593.variants.uncountable_vertices_if_large_chromatic, Erdos593.erdos_593.variants.nonempty_edges_if_large_chromatic, Erdos593.erdos_593.variants.obligatory_monotone, Erdos593.erdos_593.variants.empty_hypergraph_obligatory
statement: formalized
---

# Erdős Problem 593

> *References:*
> - [erdosproblems.com/593](https://www.erdosproblems.com/593)
> - [EGH75] Erdős, Paul and Galvin, Fred and Hajnal, András, On set-systems having large
>   chromatic number and not containing prescribed subsystems.
>   Infinite and finite sets (Colloq., Keszthely, 1973; dedicated to P. Erdős on his 60th
>   birthday), Vol. I. Colloq. Math. Soc. János Bolyai 10, North-Holland (1975), 425–513.
> - [Er95d] Erdős, Paul, Some of my favourite problems in various branches of combinatorics.
>   Matematiche (Catania) 47 (1992), no. 2, 231–240 (1995).
> - [EHR73] Erdős, Paul and Hajnal, András and Rothschild, Bruce, On chromatic number of graphs
>   and set-systems. Cambridge Summer School in Mathematical Logic (Cambridge, 1971),
>   Lecture Notes in Math. 337, Springer (1973), 531–538.

*Quoted from [FormalConjectures/ErdosProblems/593.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/593.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/593](https://www.erdosproblems.com/593).

The file states 10 research or textbook statements: 1 open, 5 solved and 4 textbook results. It also has 1 test statement, counted here but not shown.

## `Erdos593.erdos_593`

Open: stated without proof.

> **Erdős Problem 593 (\$500)**: Characterize those finite 3-uniform hypergraphs which appear
> in every 3-uniform hypergraph of chromatic number $> \aleph_0$.
>
> The answer is the set of obligatory finite 3-uniform hypergraphs, represented here on the
> labelled vertex sets `Fin n`.
>
> Two-colorability (Property B) is a necessary condition, see
> `erdos_593.variants.obligatory_implies_two_colorable`, but it is not sufficient: two triples
> sharing a pair form a 2-colorable hypergraph that is not obligatory, see
> `erdos_593.variants.common_pair_not_obligatory`. In the graph case ($r = 2$) the problem is
> completely solved by Erdős–Galvin–Hajnal [EGH75]: the obligatory graphs are exactly the finite
> bipartite graphs.
>
> A resolution has been claimed by E. Li (arXiv:2606.24882, 2026); at the time of writing
> erdosproblems.com still lists the problem as open.

```lean
theorem erdos_593 :
    {p : Σ n : ℕ, UniformHypergraph (Fin n) 3 | p.2.IsObligatory} = erdos_593.answer
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/593.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/593.lean#L64).

## `Erdos593.erdos_593.variants.obligatory_implies_two_colorable`

Solved: stated here without proof.

> **Necessary direction**: every obligatory finite 3-uniform hypergraph is 2-colorable.
>
> This follows from two constructions in [EGH75]. By [EHR73] (see [EGH75, p. 426]) there are
> 3-uniform hypergraphs of arbitrarily large chromatic number consisting of edge-disjoint
> triples, so an obligatory `F` is linear (no two edges share two vertices). By the remark
> preceding [EGH75, Theorem 10.9] there are, for every infinite cardinal $\kappa$, 3-uniform
> hypergraphs of chromatic number $> \kappa$ all of whose linear sub-hypergraphs are
> 2-colorable. An obligatory `F` appears in such a hypergraph, hence is 2-colorable.

```lean
theorem erdos_593.variants.obligatory_implies_two_colorable :
    ∀ (W : Type) [Fintype W] (F : UniformHypergraph W 3),
      F.IsObligatory → F.IsNColorable 2
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/593.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/593.lean#L79).

## `Erdos593.erdos_593.variants.two_colorable_implies_obligatory`

Solved: stated here without proof.

> **Sufficient direction fails**: it is not the case that every finite 2-colorable 3-uniform
> hypergraph is obligatory.
>
> The hypergraph `commonPair` with edges $\{0,1,2\}$ and $\{0,1,3\}$ is 2-colorable but does
> not appear in the 3-uniform hypergraphs of large chromatic number consisting of edge-disjoint
> triples constructed in [EHR73], see `erdos_593.variants.common_pair_not_obligatory`.

```lean
theorem erdos_593.variants.two_colorable_implies_obligatory :
    ¬ ∀ (W : Type) [Fintype W] (F : UniformHypergraph W 3),
      F.IsNColorable 2 → F.IsObligatory
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/593.lean, line 93](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/593.lean#L93).

## `Erdos593.erdos_593.variants.common_pair_not_obligatory`

Solved: stated here without proof.

> Two triples sharing a pair are **not** obligatory: by [EHR73] (see [EGH75, p. 426]) there are
> 3-uniform hypergraphs of arbitrarily large chromatic number consisting of edge-disjoint
> triples, and `commonPair` does not appear in any of them.

```lean
theorem erdos_593.variants.common_pair_not_obligatory : ¬ commonPair.IsObligatory
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/593.lean, line 118](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/593.lean#L118).

## `Erdos593.erdos_593.variants.graph_case_bipartite_obligatory`

Solved: stated here without proof.

> **Graph analogue — bipartite graphs are obligatory (Erdős–Galvin–Hajnal [EGH75])**:
> For the 2-uniform (graph) case, a graph of chromatic cardinal $> \aleph_0$ must contain all
> finite bipartite graphs. Specifically, for every finite bipartite graph `F` and every graph
> `G` with chromatic cardinal $> \aleph_0$, there is a graph embedding from `F` into `G`.
>
> This uses `F ⊑ G` (`SimpleGraph.IsContained`, an injective graph homomorphism), aligned with
> the injective edge-preserving map used in the hypergraph `Appears` definition. A graph embedding
> `F ↪g G` would require an induced copy, which the theorem does not provide.

```lean
theorem erdos_593.variants.graph_case_bipartite_obligatory :
    ∀ (V : Type*) (G : SimpleGraph V),
      ℵ₀ < G.chromaticCardinal →
      ∀ (W : Type*) [Fintype W] (F : SimpleGraph W), F.IsBipartite →
        F ⊑ G
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/593.lean, line 134](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/593.lean#L134).

## `Erdos593.erdos_593.variants.graph_case_no_odd_cycle`

Solved: stated here without proof.

> **Graph analogue — no odd cycle is obligatory (Erdős–Galvin–Hajnal [EGH75])**:
> For every odd $k \geq 3$, there exists a graph with chromatic cardinal $\aleph_1$ that
> contains no cycle of length $k$. This shows the class of obligatory graphs is strictly
> smaller than all finite graphs.

```lean
theorem erdos_593.variants.graph_case_no_odd_cycle :
    ∀ k : ℕ, Odd k → 3 ≤ k →
      ∃ (V : Type*) (G : SimpleGraph V),
        G.chromaticCardinal = ℵ_ 1 ∧
        IsEmpty (cycleGraph k →g G)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/593.lean, line 149](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/593.lean#L149).

## `Erdos593.erdos_593.variants.uncountable_vertices_if_large_chromatic`

Textbook result, proved here.

> **Vertices must be uncountable**: Every 3-uniform hypergraph with chromatic cardinal
> $> \aleph_0$ must have an uncountable vertex set.
>
> **Proof:** If `V` is countable, there exists an injection `φ : V → ℕ`. Using distinct natural
> numbers as colors gives a proper coloring, so $\chi(H) \leq \#\mathbb{N} = \aleph_0$,
> contradicting $\chi(H) > \aleph_0$.

```lean
theorem erdos_593.variants.uncountable_vertices_if_large_chromatic
    {V : Type} (H : UniformHypergraph V 3) (hχ : ℵ₀ < H.chromaticCardinal) :
    ¬ Countable V
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/593.lean, line 166](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/593.lean#L166).

## `Erdos593.erdos_593.variants.nonempty_edges_if_large_chromatic`

Textbook result, proved here.

> **No hyperedges implies chromatic cardinal ≤ 1**: A 3-uniform hypergraph with no edges can
> be properly colored with a single color, so its chromatic cardinal is at most 1. In
> particular, $\chi(H) > \aleph_0$ implies `H` has at least one hyperedge.

```lean
theorem erdos_593.variants.nonempty_edges_if_large_chromatic
    {V : Type} (H : UniformHypergraph V 3) (hχ : ℵ₀ < H.chromaticCardinal) :
    H.edgeSet.Nonempty
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/593.lean, line 183](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/593.lean#L183).

## `Erdos593.erdos_593.variants.obligatory_monotone`

Textbook result, proved here.

> **Monotonicity of the obligatory property**: If `F₁` appears in `F₂` and `F₂` is obligatory,
> then `F₁` is also obligatory.
>
> **Proof:** For any `H` with $\chi(H) > \aleph_0$, since `F₂` is obligatory, `F₂` appears
> in `H` via some injection `φ₂`. Since `F₁` appears in `F₂` via `φ₁`, the composition
> `φ₂ ∘ φ₁` witnesses that `F₁` appears in `H`.

```lean
theorem erdos_593.variants.obligatory_monotone
    {W₁ W₂ : Type} [Fintype W₁] [Fintype W₂] [DecidableEq W₂]
    {F₁ : UniformHypergraph W₁ 3} {F₂ : UniformHypergraph W₂ 3}
    (h12 : F₁.Appears F₂) (hObl : F₂.IsObligatory) :
    F₁.IsObligatory
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/593.lean, line 207](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/593.lean#L207).

## `Erdos593.erdos_593.variants.empty_hypergraph_obligatory`

Textbook result, proved here.

> **The empty hypergraph is trivially obligatory**: The 3-uniform hypergraph on `PEmpty` (no
> vertices, no edges) appears in every hypergraph via the empty injection.
>
> This degenerate case confirms the definition is well-formed.

```lean
theorem erdos_593.variants.empty_hypergraph_obligatory :
    UniformHypergraph.IsObligatory (W := PEmpty) (k := 3)
      (UniformHypergraph.ofFinset ∅ (by simp [Finset.IsUniform]))
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/593.lean, line 222](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/593.lean#L222).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/593.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/593.lean)
- [erdosproblems.com/593](https://www.erdosproblems.com/593)
