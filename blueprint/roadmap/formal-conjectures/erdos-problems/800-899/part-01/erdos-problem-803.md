---
declaration: theorem
origin: cited
lean: Erdos803.erdos_803, Erdos803.erdos_803.variants.alon, Erdos803.erdos_803.variants.janzer_sudakov
statement: formalized
---

# Erdős Problem 803

> *References:*
> - [erdosproblems.com/803](https://www.erdosproblems.com/803)
> - [ErSi70] Erdős, P. and Simonovits, M., _Some extremal problems in graph theory_. Combinatorial
>   theory and its applications, I-III (Proc. Colloq., Balatonfüred, 1969) (1970), 377-390.
> - [Al08] Alon, Noga, _Problems and results in extremal combinatorics. II_. Discrete Math. (2008),
>   4460-4472.
> - [JaSu23] Janzer, Oliver and Sudakov, Benny, _Resolution of the Erdős-Sauer problem on regular
>   subgraphs_. Forum Math. Pi (2023), Paper No. e19, 13.

*Quoted from [FormalConjectures/ErdosProblems/803.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/803.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/803](https://www.erdosproblems.com/803).

The file states 3 research or textbook statements: 3 solved.

## `Erdos803.erdos_803`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos803.lean#L448](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos803.lean#L448).

> We call a graph $H$ $D$-balanced (or $D$-almost-regular) if the maximum degree of $H$ is at most
> $D$ times the minimum degree of $H$.
>
> Is it true that for every $m\geq 1$, if $n$ is sufficiently large, any graph on $n$ vertices with
> $\geq n\log n$ edges contains a $O(1)$-balanced subgraph with $m$ vertices and $\gg m\log m$ edges
> (where the implied constants are absolute)?
>
> A problem of Erdős and Simonovits [ErSi70]. Alon [Al08] proved this is false: for every $D>1$
> and large $n$ there is a graph $G$ with $n$ vertices and $\geq n\log n$ edges such that if $H$ is
> a $D$-balanced subgraph then $H$ has $\ll m\sqrt{\log m}+\log D$ many edges.
>
> See also [1077](https://www.erdosproblems.com/1077).

```lean
theorem erdos_803 :
    ¬ ∃ (D c : ℝ), 0 < c ∧ ∀ m ≥ 1, ∀ᶠ n : ℕ in atTop, ∀ G : SimpleGraph (Fin n),
      (n : ℝ) * log n ≤ G.edgeSet.ncard →
        ∃ H : G.Subgraph, H.verts.ncard = m ∧ IsBalanced H.coe D ∧
          c * m * log m ≤ H.edgeSet.ncard
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/803.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/803.lean#L57).

## `Erdos803.erdos_803.variants.alon`

Solved: stated here without proof.

> Alon [Al08] proved that for every $D>1$ and large $n$ there is a graph $G$ with $n$ vertices
> and $\geq n\log n$ edges such that if $H$ is a $D$-balanced subgraph on $m$ vertices then $H$ has
> $\ll m\sqrt{\log m}+\log D$ many edges.

```lean
theorem erdos_803.variants.alon :
    ∃ C : ℝ, ∀ D : ℝ, 1 < D → ∀ᶠ n : ℕ in atTop, ∃ G : SimpleGraph (Fin n),
      (n : ℝ) * log n ≤ G.edgeSet.ncard ∧
      ∀ H : G.Subgraph, IsBalanced H.coe D →
        (H.edgeSet.ncard : ℝ) ≤ C * (H.verts.ncard * √(log H.verts.ncard) + log D)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/803.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/803.lean#L69).

## `Erdos803.erdos_803.variants.janzer_sudakov`

Solved: stated here without proof.

> Janzer and Sudakov [JaSu23] have proved that, for any $k$, if $n$ is sufficiently large then
> any graph on $n$ vertices with at least $n\log n$ edges contains a $O(1)$-balanced subgraph on
> $m\geq k$ vertices with $\gg_k \frac{\sqrt{\log m}}{(\log\log m)^{3/2}}m$ many edges.

```lean
theorem erdos_803.variants.janzer_sudakov :
    ∃ D : ℝ, ∀ k : ℕ, ∃ c > 0, ∀ᶠ n : ℕ in atTop, ∀ G : SimpleGraph (Fin n),
      (n : ℝ) * log n ≤ G.edgeSet.ncard →
        ∃ H : G.Subgraph, k ≤ H.verts.ncard ∧ IsBalanced H.coe D ∧
          c * (√(log H.verts.ncard) / (log (log H.verts.ncard)) ^ (3 / 2 : ℝ)) *
            H.verts.ncard ≤ H.edgeSet.ncard
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/803.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/803.lean#L81).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/803.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/803.lean)
- [erdosproblems.com/803](https://www.erdosproblems.com/803)
