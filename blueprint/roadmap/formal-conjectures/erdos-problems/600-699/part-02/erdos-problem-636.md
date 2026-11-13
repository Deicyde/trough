---
declaration: theorem
origin: cited
lean: Erdos636.erdos_636, Erdos636.erdos_636.variants.erdos_faudree_sos, Erdos636.erdos_636.variants.best_possible
statement: formalized
---

# Erdős Problem 636

> *References:*
> - [erdosproblems.com/636](https://www.erdosproblems.com/636)
> - [AlKo09] Alon, N. and Kostochka, A. V., *Induced subgraphs with distinct sizes*.
>   Random Structures Algorithms 34 (2009), 45-53.
> - [Er93] Erdős, Paul, *Some of my favorite solved and unsolved problems in graph theory*.
>   Quaestiones Math. (1993), 333-350.
> - [Er97d] Erdős, Paul, *Some recent problems and results in graph theory*. Discrete Math. (1997),
>   81-85.
> - [KwSu21] Kwan, M. and Sudakov, B., *Proof of a conjecture on induced subgraphs of Ramsey graphs*.
>   Trans. Amer. Math. Soc. 372 (2019), 5571-5594.
>   [arXiv:1712.05656](https://arxiv.org/abs/1712.05656)

*Quoted from [FormalConjectures/ErdosProblems/636.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/636.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/636](https://www.erdosproblems.com/636).

The file states 3 research or textbook statements: 3 solved.

## `Erdos636.erdos_636`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos636.lean#L739](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos636.lean#L739).

> Suppose $G$ is a graph on $n$ vertices which contains no complete graph or independent set on
> $\gg \log n$ many vertices. Must $G$ contain $\gg n^{5/2}$ induced subgraphs which pairwise differ
> in either the number of vertices or the number of edges?
>
> A problem of Erdős, Faudree, and Sós (although in [Er93] Erdős credits this question to Alon and
> Bollobás). This was proved by Kwan and Sudakov [KwSu21].

```lean
theorem erdos_636 :
    ∀ C > (0 : ℝ), ∃ γ > (0 : ℝ), ∀ᶠ n : ℕ in atTop, ∀ G : SimpleGraph (Fin n),
      (G.cliqueNum : ℝ) < C * Real.log n → (G.indepNum : ℝ) < C * Real.log n →
        HasManyDistinctInducedSubgraphs G (γ * (n : ℝ) ^ (5 / 2 : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/636.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/636.lean#L63).

## `Erdos636.erdos_636.variants.erdos_faudree_sos`

Solved: stated here without proof.

> Erdős, Faudree, and Sós proved that there exist $\gg n^{3/2}$ many such subgraphs, as stated on
> erdosproblems.com. Section 2 of [KwSu21] describes two short proofs of this weaker bound.

```lean
theorem erdos_636.variants.erdos_faudree_sos :
    ∀ C > (0 : ℝ), ∃ γ > (0 : ℝ), ∀ᶠ n : ℕ in atTop, ∀ G : SimpleGraph (Fin n),
      (G.cliqueNum : ℝ) < C * Real.log n → (G.indepNum : ℝ) < C * Real.log n →
        HasManyDistinctInducedSubgraphs G (γ * (n : ℝ) ^ (3 / 2 : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/636.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/636.lean#L74).

## `Erdos636.erdos_636.variants.best_possible`

Solved: stated here without proof.

> Erdős, Faudree, and Sós note that the exponent $5/2$ would be best possible: there are graphs on
> $n$ vertices with no complete graph or independent set on $\gg \log n$ many vertices which contain
> only $O(n^{5/2})$ induced subgraphs that pairwise differ in either the number of vertices or the
> number of edges. For example, the random graph $G(n, 1/2)$ has this property with high
> probability. This is the remark following Theorem 1.1 in [KwSu21], where it is proved in sketch
> form by a concentration inequality and a union bound; see also [AlKo09, Section 4].

```lean
theorem erdos_636.variants.best_possible :
    ∃ C > (0 : ℝ), ∃ K : ℝ, ∀ᶠ n : ℕ in atTop, ∃ G : SimpleGraph (Fin n),
      (G.cliqueNum : ℝ) < C * Real.log n ∧ (G.indepNum : ℝ) < C * Real.log n ∧
        ¬ HasManyDistinctInducedSubgraphs G (K * (n : ℝ) ^ (5 / 2 : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/636.lean, line 89](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/636.lean#L89).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/636.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/636.lean)
- [erdosproblems.com/636](https://www.erdosproblems.com/636)
