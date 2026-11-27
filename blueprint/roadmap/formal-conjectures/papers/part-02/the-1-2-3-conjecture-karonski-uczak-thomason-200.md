---
declaration: theorem
origin: cited
lean: OneTwoThreeConjecture.one_two_three_conjecture, OneTwoThreeConjecture.one_two_three_conjecture.variants.one_to_five, OneTwoThreeConjecture.one_two_three_conjecture.variants.one_to_thirty, OneTwoThreeConjecture.one_two_three_conjecture.variants.isolated_edge_necessary, OneTwoThreeConjecture.one_two_three_conjecture.variants.two_weights_insufficient
statement: formalized
---

# The 1-2-3 conjecture (Karoński–Łuczak–Thomason 2004; proved by Keusch 2024)

> *References:*
> * [KLT04] Karoński, M., Łuczak, T. and Thomason, A. (2004). "Edge weights and vertex colours."
>   *J. Combin. Theory Ser. B* 91, pp. 151--157.
> * [ABDMRT07] Addario-Berry, L., Dalal, K., McDiarmid, C., Reed, B. A. and Thomason, A.
>   (2007). "Vertex-colouring edge-weightings." *Combinatorica* 27, pp. 1--12.
> * [KKP10] Kalkowski, M., Karoński, M. and Pfender, F. (2010). "Vertex-coloring edge-weightings:
>   towards the 1-2-3-conjecture." *J. Combin. Theory Ser. B* 100, pp. 347--349.
> * [Ke24] Keusch, R. (2024). "A solution to the 1-2-3 conjecture."
>   *J. Combin. Theory Ser. B* 166, pp. 183--202.
>   [arXiv:2303.02611](https://arxiv.org/abs/2303.02611)

*Quoted from [FormalConjectures/Paper/OneTwoThreeConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Paper/OneTwoThreeConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 5 solved.

## `OneTwoThreeConjecture.one_two_three_conjecture`

Solved: stated here without proof.

> **The 1-2-3 conjecture (Karoński–Łuczak–Thomason 2004), proved by Keusch (2024).**
>
> Every finite simple graph with no isolated edge admits an edge weighting with weights in
> $\{1, 2, 3\}$ such that adjacent vertices have different weighted degrees.

```lean
theorem one_two_three_conjecture :
    ∀ {V : Type} [Fintype V] [DecidableEq V] (G : SimpleGraph V) [DecidableRel G.Adj],
      NoIsolatedEdge G →
      ∃ w : Sym2 V → ℕ, (∀ e ∈ G.edgeFinset, 1 ≤ w e ∧ w e ≤ 3) ∧
        IsVertexColouringWeighting G w
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Paper/OneTwoThreeConjecture.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Paper/OneTwoThreeConjecture.lean#L66).

## `OneTwoThreeConjecture.one_two_three_conjecture.variants.one_to_five`

Solved: stated here; a Lean proof is at [https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-13-000017](https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-13-000017).

> **Kalkowski–Karoński–Pfender (2010): weights in $\{1, \dots, 5\}$ suffice.**
>
> *Reference:* [KKP10].

```lean
theorem one_two_three_conjecture.variants.one_to_five
    {V : Type} [Fintype V] [DecidableEq V] (G : SimpleGraph V) [DecidableRel G.Adj]
    (hG : NoIsolatedEdge G) :
    ∃ w : Sym2 V → ℕ, (∀ e ∈ G.edgeFinset, 1 ≤ w e ∧ w e ≤ 5) ∧
      IsVertexColouringWeighting G w
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Paper/OneTwoThreeConjecture.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Paper/OneTwoThreeConjecture.lean#L80).

## `OneTwoThreeConjecture.one_two_three_conjecture.variants.one_to_thirty`

Solved: stated here; a Lean proof is at [https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-13-000017](https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-13-000017).

> **Addario-Berry–Dalal–McDiarmid–Reed–Thomason (2007): weights in $\{1, \dots, 30\}$ suffice.**
>
> *Reference:* [ABDMRT07]; see also the introduction of [KKP10].

```lean
theorem one_two_three_conjecture.variants.one_to_thirty
    {V : Type} [Fintype V] [DecidableEq V] (G : SimpleGraph V) [DecidableRel G.Adj]
    (hG : NoIsolatedEdge G) :
    ∃ w : Sym2 V → ℕ, (∀ e ∈ G.edgeFinset, 1 ≤ w e ∧ w e ≤ 30) ∧
      IsVertexColouringWeighting G w
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Paper/OneTwoThreeConjecture.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Paper/OneTwoThreeConjecture.lean#L94).

## `OneTwoThreeConjecture.one_two_three_conjecture.variants.isolated_edge_necessary`

Proved here.

> **The hypothesis "no isolated edge" is necessary.**
>
> A single edge `K₂` has no vertex-colouring edge weighting at all: both endpoints receive the
> weight of the unique edge as their weighted degree.

```lean
theorem one_two_three_conjecture.variants.isolated_edge_necessary :
    ¬ ∃ w : Sym2 (Fin 2) → ℕ, IsVertexColouringWeighting (completeGraph (Fin 2)) w
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Paper/OneTwoThreeConjecture.lean, line 108](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Paper/OneTwoThreeConjecture.lean#L108).

## `OneTwoThreeConjecture.one_two_three_conjecture.variants.two_weights_insufficient`

Proved here.

> **Weights $\{1, 2\}$ do not suffice: the triangle.**
>
> In `K₃` the three vertex sums are `a + b`, `a + c`, `b + c` for the three edge weights
> `a, b, c`, and they are pairwise distinct only if `a, b, c` are, which is impossible with
> two available weights. Hence the constant `3` in the conjecture cannot be lowered to `2`.

```lean
theorem one_two_three_conjecture.variants.two_weights_insufficient :
    ¬ ∃ w : Sym2 (Fin 3) → ℕ, (∀ e ∈ (completeGraph (Fin 3)).edgeFinset, 1 ≤ w e ∧ w e ≤ 2) ∧
      IsVertexColouringWeighting (completeGraph (Fin 3)) w
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Paper/OneTwoThreeConjecture.lean, line 134](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Paper/OneTwoThreeConjecture.lean#L134).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/OneTwoThreeConjecture.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Paper/OneTwoThreeConjecture.lean)
- [arXiv:2303.02611](https://arxiv.org/abs/2303.02611)
