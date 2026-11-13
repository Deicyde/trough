---
declaration: theorem
origin: cited
lean: RingelConjecture.ringel_conjecture
statement: formalized
---

# Ringel's Conjecture

> *Reference:* G. Ringel, *Problem 25*, in *Theory of Graphs and its Applications*
> (Proc. Sympos. Smolenice, 1963), Academia, Prague, 1964.
>
> Ringel's conjecture (1963): the complete graph $K_{2n+1}$ decomposes into copies of any tree
> with $n$ edges. It remains open; the case of all sufficiently large $n$ is proved by
> Montgomery–Pokrovskiy–Sudakov, see `Arxiv/2001.02665/RingelConjecture.lean`.

*Quoted from [FormalConjectures/Paper/RingelConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/RingelConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `RingelConjecture.ringel_conjecture`

Open: stated without proof.

> For any tree $T$ with $n$ edges, the complete graph $K_{2n+1}$ decomposes into
> $2n+1$ edge-disjoint copies of $T$.
>
> A "copy" of $T$ is the image $T.\text{map}(f_i)$ of $T$ under a vertex embedding
> $f_i : V \hookrightarrow \text{Fin}(2n+1)$; the copies are pairwise edge-disjoint
> and together cover every edge of $K_{2n+1}$.

```lean
theorem ringel_conjecture {V : Type} [Finite V]
    (T : SimpleGraph V) (hT : T.IsTree)
    (n : ℕ) (hn : T.edgeSet.ncard = n) :
    ∃ f : Fin (2 * n + 1) → (V ↪ Fin (2 * n + 1)),
      Pairwise (fun i j => Disjoint (T.map (f i)).edgeSet (T.map (f j)).edgeSet) ∧
      ⨆ i, T.map (f i) = (⊤ : SimpleGraph (Fin (2 * n + 1)))
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Paper/RingelConjecture.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/RingelConjecture.lean#L45).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/RingelConjecture.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/RingelConjecture.lean)
