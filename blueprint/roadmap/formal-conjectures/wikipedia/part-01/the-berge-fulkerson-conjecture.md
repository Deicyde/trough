---
declaration: theorem
origin: cited
lean: BergeFulkersonConjecture.berge_fulkerson_conjecture, BergeFulkersonConjecture.berge_fulkerson_conjecture.variants.berge, BergeFulkersonConjecture.berge_fulkerson_conjecture.variants.fan_raspaud, BergeFulkersonConjecture.berge_fulkerson_conjecture.variants.petersen
statement: formalized
---

# The Berge–Fulkerson conjecture

> *References:*
> * [Wikipedia](https://en.wikipedia.org/wiki/Petersen%27s_theorem#Related_conjectures)
> * [Fu71] Fulkerson, D. R. (1971). "Blocking and anti-blocking pairs of polyhedra."
>   *Math. Programming* 1, pp. 168--194.
> * [Se79] Seymour, P. D. (1979). "On multi-colourings of cubic graphs, and conjectures of
>   Fulkerson and Tutte." *Proc. London Math. Soc.* 38, pp. 423--460.
> * [Ma11] Mazzuoccolo, G. (2011). "The equivalence of two conjectures of Berge and Fulkerson."
>   *J. Graph Theory* 68, pp. 125--128.
> * [FR94] Fan, G. and Raspaud, A. (1994). "Fulkerson's conjecture and circuit covers."
>   *J. Combin. Theory Ser. B* 61, pp. 133--138.
> * [Pe91] Petersen, J. (1891). "Die Theorie der regulären graphs." *Acta Math.* 15,
>   pp. 193--220.

*Quoted from [FormalConjectures/Wikipedia/BergeFulkersonConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/BergeFulkersonConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 3 open and 1 solved. It also has 1 API statement, counted here but not shown.

## `BergeFulkersonConjecture.berge_fulkerson_conjecture`

Open: stated without proof.

> **The Berge–Fulkerson conjecture (Fulkerson 1971).**
>
> Every bridgeless cubic graph has six perfect matchings such that every edge lies in exactly two
> of them.

```lean
theorem berge_fulkerson_conjecture :
    ∀ {V : Type} [Fintype V] [DecidableEq V] (G : SimpleGraph V) [DecidableRel G.Adj],
      IsCubic G → G.IsBridgeless →
      ∃ M : Fin 6 → G.Subgraph, IsPerfectMatchingCover G 6 2 M
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/BergeFulkersonConjecture.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/BergeFulkersonConjecture.lean#L64).

## `BergeFulkersonConjecture.berge_fulkerson_conjecture.variants.berge`

Open: stated without proof.

> **Berge's conjecture: five perfect matchings covering every edge.**
>
> Every bridgeless cubic graph has five perfect matchings whose union is the whole edge set.
> Mazzuoccolo [Ma11] proved this to be equivalent to the Berge–Fulkerson conjecture.
>
> *Reference:* [Ma11].

```lean
theorem berge_fulkerson_conjecture.variants.berge :
    ∀ {V : Type} [Fintype V] [DecidableEq V] (G : SimpleGraph V) [DecidableRel G.Adj],
      IsCubic G → G.IsBridgeless →
      ∃ M : Fin 5 → G.Subgraph, (∀ i, (M i).IsPerfectMatching) ∧
        ∀ e ∈ G.edgeSet, ∃ i, e ∈ (M i).edgeSet
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/BergeFulkersonConjecture.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/BergeFulkersonConjecture.lean#L79).

## `BergeFulkersonConjecture.berge_fulkerson_conjecture.variants.fan_raspaud`

Open: stated without proof.

> **The Fan–Raspaud conjecture (1994).**
>
> Every bridgeless cubic graph has three perfect matchings with no edge common to all three.
> This would follow from the Berge–Fulkerson conjecture.
>
> *Reference:* [FR94].

```lean
theorem berge_fulkerson_conjecture.variants.fan_raspaud :
    ∀ {V : Type} [Fintype V] [DecidableEq V] (G : SimpleGraph V) [DecidableRel G.Adj],
      IsCubic G → G.IsBridgeless →
      ∃ M : Fin 3 → G.Subgraph, (∀ i, (M i).IsPerfectMatching) ∧
        ∀ e, ¬ (e ∈ (M 0).edgeSet ∧ e ∈ (M 1).edgeSet ∧ e ∈ (M 2).edgeSet)
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/BergeFulkersonConjecture.lean, line 95](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/BergeFulkersonConjecture.lean#L95).

## `BergeFulkersonConjecture.berge_fulkerson_conjecture.variants.petersen`

Solved: stated here without proof.

> **Petersen's theorem (1891): every bridgeless cubic graph has a perfect matching.**
>
> This is the case of a single perfect matching, and is the starting point for all of the
> above.
>
> *Reference:* [Pe91].

```lean
theorem berge_fulkerson_conjecture.variants.petersen
    {V : Type} [Fintype V] [DecidableEq V] (G : SimpleGraph V) [DecidableRel G.Adj]
    (hcubic : IsCubic G) (hbridgeless : G.IsBridgeless) :
    ∃ M : G.Subgraph, M.IsPerfectMatching
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/BergeFulkersonConjecture.lean, line 111](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/BergeFulkersonConjecture.lean#L111).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/BergeFulkersonConjecture.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/BergeFulkersonConjecture.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Petersen%27s_theorem#Related_conjectures)
