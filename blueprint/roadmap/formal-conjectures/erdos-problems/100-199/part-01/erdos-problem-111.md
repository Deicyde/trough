---
declaration: theorem
origin: cited
lean: Erdos111.erdos_111, Erdos111.erdos_111.variants.lower_bound, Erdos111.erdos_111.variants.upper_bound_existence, Erdos111.erdos_111.variants.erdos_conjecture
statement: formalized
---

# Erdős Problem 111

> *References:*
> - [erdosproblems.com/111](https://www.erdosproblems.com/111)
> - [Er81] Erdős, P., On the combinatorial problems which I would most like to see solved. (1981)
> - [EHS82] Erdős, P., Hajnal, A., and Szemerédi, E., On almost bipartite large chromatic graphs.
>   Theory and practice of combinatorics (1982), 117–123.
> - [Er87] Erdős, P., Some problems on finite and infinite graphs. (1987)
> - [Er90] Erdős, P., Some of my favourite unsolved problems. (1990)
> - [Er97d] Erdős, P., Some recent problems and results in graph theory. (1997)
> - [Er97f] Erdős, P., Some unsolved problems. (1997)
>
> See also Erdős Problem [74].
>
> ## Formalization notes
>
> - **`bipartiteDistance G`**: the minimum number of edges to delete from a (finite) simple graph $G$
>   to make it bipartite. Defined as the infimum over all spanning subgraphs $H \leq G$ with
>   `H.IsBipartite` of the number of edges in `G.edgeSet \ H.edgeSet`.
>
> - **`hG G n`**: for a graph $G$ on vertex type $V$, `hG G n` is the supremum over all sets $S$ of
>   vertices of cardinality $n$ of `bipartiteDistance (G.induce S)`. This matches the problem's
>   formulation: "any subgraph of $G$ on $n$ vertices can be made bipartite after deleting at most
>   $h_G(n)$ edges."

*Quoted from [FormalConjectures/ErdosProblems/111.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/111.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/111](https://www.erdosproblems.com/111).

The file states 4 research or textbook statements: 2 open and 2 solved.

## `Erdos111.erdos_111`

Open: stated without proof.

> **Erdős Problem 111** (Erdős, Hajnal, Szemerédi [EHS82]):
>
> If $G$ is a graph with chromatic number $\aleph_1$, is it true that $h_G(n)/n \to \infty$?
>
> Formally: for every graph $G$ (on a type $V$) with chromatic cardinal $\aleph_1$, the ratio
> $h_G(n)/n$ tends to infinity: for every constant $C$, all sufficiently large $n$ satisfy
> $h_G(n) > C \cdot n$.

```lean
theorem erdos_111 :
    ∀ (V : Type) (G : SimpleGraph V), G.chromaticCardinal = ℵ_ 1 →
      Filter.Tendsto (fun n : ℕ => (hG G n : ℝ) / n) Filter.atTop Filter.atTop
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/111.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/111.lean#L83).

## `Erdos111.erdos_111.variants.lower_bound`

Solved: stated here without proof.

> **Linear lower bound (ZFC, [EHS82])**: Every graph $G$ with chromatic number $\aleph_1$ has
> $h_G(n) \geq c \cdot n$ for some positive constant $c > 0$ and all sufficiently large $n$
> (i.e., the *linear* lower bound $h_G(n) \gg n$ is known).
>
> This follows from the fact that every graph with uncountable chromatic number contains
> $\aleph_1$ vertex-disjoint odd cycles of some fixed odd length $\ell$: any induced subgraph
> on $n$ vertices containing $\gg n / \ell$ such cycles requires removing $\gg n$ edges to
> become bipartite.
>
> This is a *strictly weaker* statement than the headline `erdos_111`, which asks for
> $h_G(n)/n \to \infty$ (i.e., $h_G(n)$ grows *super-linearly* — the constant `c` could be
> taken arbitrarily large for a fixed graph $G$). Whether the linear lower bound can be
> improved to super-linear remains the open question.

```lean
theorem erdos_111.variants.lower_bound :
    ∀ (V : Type) (G : SimpleGraph V), G.chromaticCardinal = ℵ_ 1 →
      ∃ c : ℝ, 0 < c ∧
        ∀ᶠ n : ℕ in Filter.atTop, c * n ≤ hG G n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/111.lean, line 106](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/111.lean#L106).

## `Erdos111.erdos_111.variants.upper_bound_existence`

Solved: stated here without proof.

> **Upper bound existence (Erdős-Hajnal-Szemerédi [EHS82])**: There exists a graph $G$ with
> chromatic number $\aleph_1$ such that $h_G(n) \ll n^{3/2}$, i.e., there is a constant $C > 0$
> with $h_G(n) \leq C \cdot n^{3/2}$ for all $n$.

```lean
theorem erdos_111.variants.upper_bound_existence :
    ∃ (V : Type) (G : SimpleGraph V), G.chromaticCardinal = ℵ_ 1 ∧
      (fun n : ℕ => (hG G n : ℝ)) =O[atTop] (fun n : ℕ => (n : ℝ) ^ (3 / 2 : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/111.lean, line 118](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/111.lean#L118).

## `Erdos111.erdos_111.variants.erdos_conjecture`

Open: stated without proof.

> Erdős conjectured [Er81] that for every $\varepsilon > 0$ there is a graph $G$ with
> $\chi(G) = \aleph_1$ such that $h_G(n) \ll n^{1+\varepsilon}$.
> The graph is chosen after $\varepsilon$.

```lean
theorem erdos_111.variants.erdos_conjecture :
    ∀ ε : ℝ, 0 < ε → ∃ (V : Type) (G : SimpleGraph V),
      G.chromaticCardinal = ℵ_ 1 ∧
        (fun n : ℕ => (hG G n : ℝ)) =O[atTop] (fun n : ℕ => (n : ℝ) ^ (1 + ε))
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/111.lean, line 129](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/111.lean#L129).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/111.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/111.lean)
- [erdosproblems.com/111](https://www.erdosproblems.com/111)
