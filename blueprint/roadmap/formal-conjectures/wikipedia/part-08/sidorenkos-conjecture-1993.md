---
declaration: theorem
origin: cited
lean: SidorenkoConjecture.sidorenko_conjecture, SidorenkoConjecture.sidorenko_conjecture_graphon, SidorenkoConjecture.sidorenko_tree_graphon, SidorenkoConjecture.sidorenko_even_cycle_graphon, SidorenkoConjecture.sidorenko_completeBipartiteGraph_graphon, SidorenkoConjecture.tournament_anti_sidorenko_trees_conjecture, SidorenkoConjecture.tournament_anti_sidorenko_trees_conjecture_tournamenton, SidorenkoConjecture.tournament_anti_sidorenko_single_even_degree_tree, SidorenkoConjecture.tournament_anti_sidorenko_spider234, SidorenkoConjecture.sidorenko_K2, SidorenkoConjecture.sidorenko_K22, SidorenkoConjecture.sidorenko_tree_subsingleton, SidorenkoConjecture.sidorenko_tree, SidorenkoConjecture.sidorenko_conjecture.variants.complete_bipartite, SidorenkoConjecture.sidorenko_conjecture.variants.even_cycle, SidorenkoConjecture.sidorenko_conjecture.variants.path_blakley_roy, SidorenkoConjecture.sidorenko_conjecture.variants.star, SidorenkoConjecture.sidorenko_conjecture.variants.non_bipartite_necessary
statement: formalized
---

# Sidorenko's conjecture (1993)

> *References:*
> * [Wikipedia](https://en.wikipedia.org/wiki/Sidorenko%27s_conjecture)
> * [Si93] Sidorenko, A. (1993). "A correlation inequality for bipartite graphs."
>   *Graphs Combin.* 9, pp. 201--204.
> * [CoFo10] Conlon, D. and Fox, J. (2010). "Bounds for graph regularity and removal lemmas."
>   *Geom. Funct. Anal.* 22, pp. 1191--1256.
> * [KLL18] Kim, J.H., Lee, C., Lee, J. (2018). "Two approaches to Sidorenko's conjecture."
>   *Trans. Amer. Math. Soc.* 370, pp. 8515--8552.
> * [ArXiv2605] [arXiv:2605.14138](https://arxiv.org/abs/2605.14138)
> * [BR65] Blakley, G. R. and Roy, P. (1965). "A Hölder type inequality for symmetric matrices
>   with nonnegative entries." *Proc. Amer. Math. Soc.* 16, pp. 1244--1245.
> * [OAI26a] OpenAI, *A counterexample to Sidorenko's conjecture*. OpenAI Math Release preprint
>   (2026).
>   https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-counterexample-to-Sidorenkos-conjecture-September-23-2026/paper.pdf

*Quoted from [FormalConjectures/Wikipedia/SidorenkoConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SidorenkoConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 18 research or textbook statements: 2 open and 16 solved. It also has 9 API statements, counted here but not shown.

## `SidorenkoConjecture.sidorenko_conjecture`

Solved: stated here; a Lean proof is at [https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Combinatorics/Sidorenko/RandomHost.lean#L319](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Combinatorics/Sidorenko/RandomHost.lean#L319).

> **Sidorenko's conjecture (1993).**
>
> For every finite bipartite simple graph $H$ and every finite simple graph $G$:
> $t(H, G) \ge t(K_2, G)^{e(H)}$, where $K_2$ denotes the single-edge graph on 2 vertices
> (i.e. `completeGraph (Fin 2)`).
>
> This is false. It was disproved by an internal OpenAI model in September 2026 [OAI26a]; see the
> linked Lean proof, which gives a bipartite $H$ with $35$ vertices and $66$ edges and a finite
> host $G$ with $t(H, G) < t(K_2, G)^{66}$.

```lean
theorem sidorenko_conjecture :
    ¬ ∀ {V W : Type} [Fintype V] [Fintype W] [DecidableEq V] [DecidableEq W] [Nonempty W]
      (H : SimpleGraph V) (G : SimpleGraph W)
      [DecidableRel H.Adj] [DecidableRel G.Adj],
      H.IsBipartite →
      homDensity (completeGraph (Fin 2)) G ^ H.edgeFinset.card ≤ homDensity H G
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/SidorenkoConjecture.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SidorenkoConjecture.lean#L72).

## `SidorenkoConjecture.sidorenko_conjecture_graphon`

Solved: stated here without proof.

> **Sidorenko's conjecture for graphons (1993).**
>
> For every finite bipartite simple graph $H$ and every graphon $W$ on $[0, 1]$ with Lebesgue measure:
> $t(H, W) \ge t(K_2, W)^{e(H)}$, where $t(K_2, W) = p(W)$ is the edge density of $W$,
> and $t(H, W)$ is the graphon homomorphism density of $H$ in $W$.
>
> This is false. The finite counterexample of [OAI26a] (see `sidorenko_conjecture`) also refutes
> the graphon form: the step graphon of the finite host graph has the same homomorphism
> densities and the same edge density as the host. This reduction is not part of the linked Lean
> proof of the finite form.

```lean
theorem sidorenko_conjecture_graphon :
    ¬ ∀ {V : Type*} [Fintype V] [DecidableEq V] (H : SimpleGraph V) [DecidableRel H.Adj],
      H.IsBipartite →
      ∀ (W : Graphon),
        (graphonEdgeDensity W) ^ H.edgeFinset.card ≤ graphonHomDensity H W
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/SidorenkoConjecture.lean, line 93](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SidorenkoConjecture.lean#L93).

## `SidorenkoConjecture.sidorenko_tree_graphon`

Solved: stated here without proof.

> **Case: `H` is a tree (Sidorenko 1993, graphon version).**
>
> If `H` is a finite tree then Sidorenko's inequality holds for all graphons on $[0, 1]$.

```lean
theorem sidorenko_tree_graphon {V : Type*} [Fintype V] [DecidableEq V]
    (H : SimpleGraph V) [DecidableRel H.Adj] (hTree : H.IsTree)
    (W : LimitObjects.Graphon) :
    (graphonEdgeDensity W) ^ H.edgeFinset.card ≤ graphonHomDensity H W
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/SidorenkoConjecture.lean, line 108](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SidorenkoConjecture.lean#L108).

## `SidorenkoConjecture.sidorenko_even_cycle_graphon`

Solved: stated here without proof.

> **Case: `H = C_{2k}` is an even cycle (Sidorenko 1993, graphon version).**
>
> Every even cycle $C_{2k}$ satisfies Sidorenko's inequality for all graphons on $[0, 1]$.

```lean
theorem sidorenko_even_cycle_graphon (k : ℕ) (hk : 1 ≤ k)
    (W : LimitObjects.Graphon) :
    (graphonEdgeDensity W) ^ (cycleGraph (2 * k)).edgeFinset.card ≤
      graphonHomDensity (cycleGraph (2 * k)) W
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/SidorenkoConjecture.lean, line 120](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SidorenkoConjecture.lean#L120).

## `SidorenkoConjecture.sidorenko_completeBipartiteGraph_graphon`

Solved: stated here without proof.

> **Case: `H = K_{a,b}` is a complete bipartite graph (Sidorenko 1993, graphon version).**
>
> Every complete bipartite graph $K_{a,b}$ satisfies Sidorenko's inequality for all graphons on $[0, 1]$.

```lean
theorem sidorenko_completeBipartiteGraph_graphon {A B : Type*} [Fintype A] [Fintype B]
    [DecidableEq A] [DecidableEq B] (W : LimitObjects.Graphon) :
    (graphonEdgeDensity W) ^ (completeBipartiteGraph A B).edgeFinset.card ≤
      graphonHomDensity (completeBipartiteGraph A B) W
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/SidorenkoConjecture.lean, line 133](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SidorenkoConjecture.lean#L133).

## `SidorenkoConjecture.tournament_anti_sidorenko_trees_conjecture`

Open: stated without proof.

> **Tournament Anti-Sidorenko (TAS) Trees Conjecture.**
>
> For every finite undirected tree $T$, there exists an orientation $\vec{T}$ of its edges such that
> for any finite tournament $G$, the homomorphism density satisfies:
> $$ t_{\vec{T}}(G) \le 2^{-e(T)} $$
> where $e(T)$ is the total number of edges in $T$.

```lean
theorem tournament_anti_sidorenko_trees_conjecture :
    ∀ {V : Type*} [Fintype V] [DecidableEq V] (T : SimpleGraph V) [DecidableRel T.Adj],
      T.IsTree →
      ∃ (D : Digraph V),
        D.IsOrientation T ∧
        ∀ {W : Type*} [Fintype W] [DecidableEq W] [Nonempty W]
          (G : Digraph W) [DecidableRel G.Adj],
          G.IsTournament →
          Digraph.homDensity D G ≤ (1 / 2 : ℝ) ^ T.edgeFinset.card
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/SidorenkoConjecture.lean, line 151](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SidorenkoConjecture.lean#L151).

## `SidorenkoConjecture.tournament_anti_sidorenko_trees_conjecture_tournamenton`

Open: stated without proof.

> **Tournament Anti-Sidorenko (TAS) Trees Conjecture (Tournamenton limit version).**
>
> For every finite undirected tree $T$, there exists an orientation $\vec{T}$ of its edges such that
> for every tournamenton $W : [0, 1]^2 \to [0, 1]$, the homomorphism density satisfies:
> $$ t_{\vec{T}}(W) \le 2^{-e(T)} $$
> where $e(T)$ is the total number of edges in $T$.

```lean
theorem tournament_anti_sidorenko_trees_conjecture_tournamenton :
    ∀ {V : Type*} [Fintype V] [DecidableEq V] (T : SimpleGraph V) [DecidableRel T.Adj],
      T.IsTree →
      ∃ (D : Digraph V),
        D.IsOrientation T ∧
        ∀ (W : LimitObjects.Tournamenton),
          tournamentonHomDensity D W ≤ (1 / 2 : ℝ) ^ T.edgeFinset.card
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/SidorenkoConjecture.lean, line 172](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SidorenkoConjecture.lean#L172).

## `SidorenkoConjecture.tournament_anti_sidorenko_single_even_degree_tree`

Solved: stated here without proof.

> **TAS Trees Conjecture: Trees with a single even-degree vertex.**
>
> Proven case of TAS Trees Conjecture: any tree containing exactly one vertex of even degree
> possesses an orientation satisfying the Tournament Anti-Sidorenko inequality $t_{\vec{T}}(G) \le 2^{-e(T)}$.

```lean
theorem tournament_anti_sidorenko_single_even_degree_tree {V : Type*} [Fintype V] [DecidableEq V]
    (T : SimpleGraph V) [DecidableRel T.Adj] (hTree : T.IsTree)
    (hEven : (Finset.univ.filter (fun v => Even (T.degree v))).card = 1) :
    ∃ (D : Digraph V),
      D.IsOrientation T ∧
      ∀ {W : Type*} [Fintype W] [DecidableEq W] [Nonempty W]
        (G : Digraph W) [DecidableRel G.Adj],
        G.IsTournament →
        Digraph.homDensity D G ≤ (1 / 2 : ℝ) ^ T.edgeFinset.card
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/SidorenkoConjecture.lean, line 189](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SidorenkoConjecture.lean#L189).

## `SidorenkoConjecture.tournament_anti_sidorenko_spider234`

Solved: stated here without proof.

> **TAS Trees Conjecture: The $(2,3,4)$-spider tree (Solved case).**
>
> The $(2,3,4)$-spider tree satisfies the Tournament Anti-Sidorenko Trees Conjecture.
>
> *Reference:*
> * [ArXiv 2605.14138](https://arxiv.org/abs/2605.14138)

```lean
theorem tournament_anti_sidorenko_spider234 {V : Type*} [Fintype V] [DecidableEq V]
    (T : SimpleGraph V) [DecidableRel T.Adj] (hSpider : IsSpider234 T) :
    ∃ (D : Digraph V),
      D.IsOrientation T ∧
      ∀ {W : Type*} [Fintype W] [DecidableEq W] [Nonempty W]
        (G : Digraph W) [DecidableRel G.Adj],
        G.IsTournament →
        Digraph.homDensity D G ≤ (1 / 2 : ℝ) ^ T.edgeFinset.card
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/SidorenkoConjecture.lean, line 226](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SidorenkoConjecture.lean#L226).

## `SidorenkoConjecture.sidorenko_K2`

Proved here.

> **Case `H = K_2` (single edge): Sidorenko's inequality holds trivially with equality.**
>
> When `H` is `K_2` (the single-edge graph on 2 vertices), `e(H) = 1`, so the RHS of Sidorenko's
> inequality is just `t(K_2, G)^1 = t(K_2, G) = t(H, G)`, which equals the LHS. Hence the
> inequality holds as equality.
>
> The proof records that `(completeGraph (Fin 2)).edgeFinset.card = 1` and then reduces the claim
> to `t(K_2, G) ≤ t(K_2, G)`, which is `le_refl`.

```lean
theorem sidorenko_K2 {W : Type} [Fintype W] [DecidableEq W]
    (G : SimpleGraph W) [DecidableRel G.Adj] :
    homDensity (completeGraph (Fin 2)) G ^
      ((completeGraph (Fin 2)).edgeFinset.card) ≤
      homDensity (completeGraph (Fin 2)) G
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/SidorenkoConjecture.lean, line 249](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SidorenkoConjecture.lean#L249).

## `SidorenkoConjecture.sidorenko_K22`

Proved here.

> **Case `H = K_{2,2}` (four-cycle, also called `C_4`): Sidorenko's conjecture holds, by
> Cauchy–Schwarz.**
>
> The textbook statement at `H = K_{2,2}` is
> `t(K_2, G)^{e(K_{2,2})} = t(K_2, G)^4 ≤ t(K_{2,2}, G)`.
>
> **Proof sketch.** Write `d(a) := G.degree a`. Then
> - `homCount(K_2, G) = ∑_a d(a) = 2·|E(G)|` (handshaking).
> - `homCount(K_{2,2}, G) = ∑_{b₀, b₁} |N(b₀) ∩ N(b₁)|²` (product structure of bipartite
>   homomorphism).
> - `∑_{b₀, b₁} |N(b₀) ∩ N(b₁)| = ∑_a d(a)²` (swap sums).
> - Cauchy–Schwarz #1: `(∑_{b₀, b₁} |N(b₀) ∩ N(b₁)|)² ≤ |W|² · ∑_{b₀, b₁} |N(b₀) ∩ N(b₁)|²`.
> - Cauchy–Schwarz #2: `(∑_a d(a))² ≤ |W| · ∑_a d(a)²`.
> - Chain: `(∑_a d(a))⁴ ≤ |W|⁴ · homCount(K_{2,2}, G)`.
> - Divide by `|W|^8` to get `t(K_2, G)^4 ≤ t(K_{2,2}, G)`.
>
> The proof uses `Finset.sum_mul_sq_le_sq_mul_sq` (discrete Cauchy–Schwarz) from
> `Mathlib.Algebra.Order.BigOperators.Ring.Finset`.
>
> **Status (2026-04-22):** main theorem closed sorry-free. See [Si93].

```lean
theorem sidorenko_K22 {W : Type} [Fintype W] [DecidableEq W]
    (G : SimpleGraph W) [DecidableRel G.Adj] :
    homDensity (completeGraph (Fin 2)) G ^
      ((completeBipartiteGraph (Fin 2) (Fin 2)).edgeFinset.card) ≤
      homDensity (completeBipartiteGraph (Fin 2) (Fin 2)) G
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/SidorenkoConjecture.lean, line 535](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SidorenkoConjecture.lean#L535).

## `SidorenkoConjecture.sidorenko_tree_subsingleton`

Proved here.

> **Base case of Sidorenko for trees.** When the tree `H` has at most one vertex,
> both sides of Sidorenko's inequality evaluate to `1` (there are no edges, and every
> function is a homomorphism). Thus the inequality `1 ≤ 1` holds trivially.
>
> This covers the `|V(T)| = 1` base case of the induction on tree size.

```lean
theorem sidorenko_tree_subsingleton {V W : Type} [Fintype V] [Fintype W]
    [Subsingleton V] [DecidableEq V] [DecidableEq W] [Nonempty W]
    (H : SimpleGraph V) (G : SimpleGraph W)
    [DecidableRel H.Adj] [DecidableRel G.Adj] :
    homDensity (completeGraph (Fin 2)) G ^ (H.edgeFinset.card) ≤ homDensity H G
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/SidorenkoConjecture.lean, line 704](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SidorenkoConjecture.lean#L704).

## `SidorenkoConjecture.sidorenko_tree`

Solved: stated here without proof.

> **Case: `H` is a tree (Sidorenko 1993).**
>
> If `H` is a finite tree then Sidorenko's inequality holds.
>
> **Proof idea (Sidorenko 1993):** by induction on the tree, applying Jensen / convexity. The
> number of homomorphisms from a tree `T` with `v` vertices and `v - 1` edges into `G` factors
> nicely in the degree sequence of `G`, and AM–GM / convexity gives the required lower bound.
>
> **Current status (2026-04-22, partial):**
> - The subsingleton base case (`|V(T)| ≤ 1`) is dispatched via `sidorenko_tree_subsingleton`.
> - The main inductive step (leaf extraction + AM–GM on the degree sequence) is deferred;
>   it requires a walk-parametrised homomorphism count for trees and a discrete Jensen
>   inequality. See [Si93].
>
> The full proof is left as `sorry`; the subsingleton case is closed.

```lean
theorem sidorenko_tree {V W : Type} [Fintype V] [Fintype W]
    [DecidableEq V] [DecidableEq W] [Nonempty W]
    (H : SimpleGraph V) (G : SimpleGraph W)
    [DecidableRel H.Adj] [DecidableRel G.Adj]
    (hTree : H.IsTree) :
    homDensity (completeGraph (Fin 2)) G ^ (H.edgeFinset.card) ≤ homDensity H G
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/SidorenkoConjecture.lean, line 737](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SidorenkoConjecture.lean#L737).

## `SidorenkoConjecture.sidorenko_conjecture.variants.complete_bipartite`

Solved: stated here without proof.

> **Case: complete bipartite graphs `K_{s,t}` (Sidorenko 1993).**
>
> Sidorenko's inequality holds when `H = K_{s,t}` is a complete bipartite graph. This is one
> of the earliest known cases; it follows from repeated applications of the Cauchy–Schwarz /
> Hölder inequality. The `s = t = 2` instance is `sidorenko_K22`.
>
> *Reference:* [Si93].

```lean
theorem sidorenko_conjecture.variants.complete_bipartite (s t : ℕ)
    [DecidableRel (completeBipartiteGraph (Fin s) (Fin t)).Adj]
    {W : Type} [Fintype W] [DecidableEq W] [Nonempty W]
    (G : SimpleGraph W) [DecidableRel G.Adj] :
    homDensity (completeGraph (Fin 2)) G ^
        ((completeBipartiteGraph (Fin s) (Fin t)).edgeFinset.card) ≤
      homDensity (completeBipartiteGraph (Fin s) (Fin t)) G
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/SidorenkoConjecture.lean, line 776](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SidorenkoConjecture.lean#L776).

## `SidorenkoConjecture.sidorenko_conjecture.variants.even_cycle`

Solved: stated here without proof.

> **Case: even cycles `C_{2k}` (Sidorenko 1993).**
>
> Sidorenko's inequality holds for every even cycle `C_{2k}` with `k ≥ 2`
> (`cycleGraph (2 * k)`). Even cycles are bipartite; the `k = 2` case `C_4` coincides
> with `K_{2,2}` (`sidorenko_K22`).
>
> *Reference:* [Si93].

```lean
theorem sidorenko_conjecture.variants.even_cycle (k : ℕ) (hk : 2 ≤ k)
    {W : Type} [Fintype W] [DecidableEq W] [Nonempty W]
    (G : SimpleGraph W) [DecidableRel G.Adj] :
    homDensity (completeGraph (Fin 2)) G ^
        ((cycleGraph (2 * k)).edgeFinset.card) ≤
      homDensity (cycleGraph (2 * k)) G
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/SidorenkoConjecture.lean, line 795](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SidorenkoConjecture.lean#L795).

## `SidorenkoConjecture.sidorenko_conjecture.variants.path_blakley_roy`

Solved: stated here without proof.

> **Case: paths, the Blakley–Roy inequality (1965).**
>
> For the path `P_n` on `n` vertices (`pathGraph n`), Sidorenko's inequality
> `t(K_2, G)^{e(P_n)} ≤ t(P_n, G)` is the Blakley–Roy inequality, established well before
> Sidorenko's general conjecture. Paths are trees, so this is also a special case of
> `sidorenko_tree`.
>
> *Reference:* [BR65].

```lean
theorem sidorenko_conjecture.variants.path_blakley_roy (n : ℕ)
    [DecidableRel (pathGraph n).Adj]
    {W : Type} [Fintype W] [DecidableEq W] [Nonempty W]
    (G : SimpleGraph W) [DecidableRel G.Adj] :
    homDensity (completeGraph (Fin 2)) G ^ ((pathGraph n).edgeFinset.card) ≤
      homDensity (pathGraph n) G
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/SidorenkoConjecture.lean, line 814](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SidorenkoConjecture.lean#L814).

## `SidorenkoConjecture.sidorenko_conjecture.variants.star`

Proved here.

> **Case: stars `K_{1,m}` (Sidorenko).**
>
> Sidorenko's inequality holds for every star `K_{1,m} = completeBipartiteGraph (Fin 1) (Fin m)`.
> This is a fully proved instance of both `sidorenko_conjecture.variants.complete_bipartite` and
> `sidorenko_tree` (a star is a complete bipartite graph and a tree).
>
> **Proof.** With `d(c) := G.degree c` and `N := |W|`, the star has `m` edges, so the desired
> inequality is `(∑_c d(c) / N^2)^m ≤ (∑_c d(c)^m) / N^{m+1}` (using `t(K_2, G) = ∑_c d(c) / N^2`
> and `t(K_{1,m}, G) = ∑_c d(c)^m / N^{m+1}` via `homCount_star_eq_sum_degree_pow`). After clearing
> denominators this is `(∑_c d(c))^m ≤ N^{m-1} · ∑_c d(c)^m`, the power-mean (Jensen) inequality
> `Finset.pow_sum_div_card_le_sum_pow`.

```lean
theorem sidorenko_conjecture.variants.star (m : ℕ)
    [DecidableRel (completeBipartiteGraph (Fin 1) (Fin m)).Adj]
    {W : Type} [Fintype W] [DecidableEq W] [Nonempty W]
    (G : SimpleGraph W) [DecidableRel G.Adj] :
    homDensity (completeGraph (Fin 2)) G ^
        ((completeBipartiteGraph (Fin 1) (Fin m)).edgeFinset.card) ≤
      homDensity (completeBipartiteGraph (Fin 1) (Fin m)) G
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/SidorenkoConjecture.lean, line 933](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SidorenkoConjecture.lean#L933).

## `SidorenkoConjecture.sidorenko_conjecture.variants.non_bipartite_necessary`

Proved here.

> **Bipartiteness is necessary: the triangle is not a Sidorenko graph.**
>
> The hypothesis `H.IsBipartite` in `sidorenko_conjecture` cannot be dropped. For the
> triangle `H = K_3` (chromatic number `3`, hence not bipartite) and the single edge
> `G = K_2`, Sidorenko's inequality fails: the putative lower bound is
> `t(K_2, K_2)^{e(K_3)} = (1/2)^3 = 1/8`, while the actual density is `t(K_3, K_2) = 0`,
> because there is no graph homomorphism from `K_3` into the triangle-free graph `K_2`
> (such a homomorphism would be an injection `Fin 3 ↪ Fin 2`). So the lower bound `1/8`
> strictly exceeds the true value `0`.
>
> More generally, any `H` containing an odd cycle fails Sidorenko's inequality against a
> suitable bipartite `G`, since then `t(H, G) = 0 < t(K_2, G)^{e(H)}`.

```lean
theorem sidorenko_conjecture.variants.non_bipartite_necessary :
    homDensity (completeGraph (Fin 3)) (completeGraph (Fin 2)) <
      homDensity (completeGraph (Fin 2)) (completeGraph (Fin 2)) ^
        ((completeGraph (Fin 3)).edgeFinset.card)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/SidorenkoConjecture.lean, line 992](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SidorenkoConjecture.lean#L992).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/SidorenkoConjecture.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SidorenkoConjecture.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Sidorenko%27s_conjecture)
