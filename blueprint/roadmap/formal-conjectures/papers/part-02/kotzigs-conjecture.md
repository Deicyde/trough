---
declaration: theorem
origin: cited
lean: KotzigConjecture.kotzig_conjecture
statement: formalized
---

# Kotzig's Conjecture

> *Reference:* A. Kotzig, cited in A. Rosa, *On certain valuations of the vertices of a graph*,
> Theory of Graphs (Internat. Sympos., Rome, 1966), Gordon and Breach, 1967, pp. 349–355.
>
> Kotzig conjectured that for every $n$, the complete graph $K_{2n+1}$ decomposes into copies of
> any $n$-edge tree via cyclic shifts of a single embedding. This is strictly stronger than
> Ringel's conjecture; see `Paper/RingelConjecture.lean`. The large-$n$ case is proved by
> Montgomery–Pokrovskiy–Sudakov; see `Arxiv/2001.02665/RingelConjecture.lean`.

*Quoted from [FormalConjectures/Paper/KotzigConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/KotzigConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `KotzigConjecture.kotzig_conjecture`

Open: stated without proof.

> For any tree $T$ with $n$ edges, the complete graph $K_{2n+1}$ decomposes into
> $2n+1$ edge-disjoint copies of $T$ via cyclic shifts of a single embedding.
>
> The $2n+1$ copies are $f_0, f_1, \dots, f_{2n}$ where $f_i(v) = f_0(v) + i$ for all vertices
> $v$ — each copy is obtained by adding $i \pmod{2n+1}$ to every vertex of the base copy.
> This is strictly stronger than `RingelConjecture.ringel_conjecture`.

```lean
theorem kotzig_conjecture {V : Type} [Finite V]
    (T : SimpleGraph V) (hT : T.IsTree)
    (n : ℕ) (hn : T.edgeSet.ncard = n) :
    ∃ f : Fin (2 * n + 1) → (V ↪ Fin (2 * n + 1)),
      (∀ i v, f i v = f 0 v + i) ∧
      Pairwise (fun i j => Disjoint (T.map (f i)).edgeSet (T.map (f j)).edgeSet) ∧
      ⨆ i, T.map (f i) = (⊤ : SimpleGraph (Fin (2 * n + 1)))
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Paper/KotzigConjecture.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/KotzigConjecture.lean#L46).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/KotzigConjecture.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/KotzigConjecture.lean)
