---
declaration: theorem
origin: cited
lean: ReconstructionConjecture.reconstruction_conjecture, ReconstructionConjecture.reconstruction_conjecture.variants.tree, ReconstructionConjecture.reconstruction_conjecture.variants.disconnected, ReconstructionConjecture.edge_reconstruction_conjecture, ReconstructionConjecture.edge_reconstruction_conjecture.variants.lovasz, ReconstructionConjecture.edge_reconstruction_conjecture.variants.mueller
statement: formalized
---

# The reconstruction conjecture

> *References:*
> * [Wikipedia](https://en.wikipedia.org/wiki/Reconstruction_conjecture)
> * [Ke57] Kelly, P. J. (1957). "A congruence theorem for trees." *Pacific J. Math.* 7,
>   pp. 961--968.
> * [Ul60] Ulam, S. M. (1960). *A Collection of Mathematical Problems.* Interscience, New York.
> * [Ha64] Harary, F. (1964). "On the reconstruction of a graph from a collection of subgraphs."
>   In *Theory of Graphs and its Applications*, Academia, Prague, pp. 47--52.
> * [Lo72] Lovász, L. (1972). "A note on the line reconstruction problem." *J. Combin. Theory
>   Ser. B* 13, pp. 309--310.
> * [Mu77] Müller, V. (1977). "The edge reconstruction hypothesis is true for graphs with more
>   than n·log n edges." *J. Combin. Theory Ser. B* 22, pp. 281--283.
> * [Bo91] Bondy, J. A. (1991). "A graph reconstructor's manual." In *Surveys in Combinatorics*,
>   LMS Lecture Note Series 166, Cambridge University Press, pp. 221--252.

*Quoted from [FormalConjectures/Wikipedia/ReconstructionConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/ReconstructionConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 6 research or textbook statements: 2 open and 4 solved. It also has 1 test statement and 3 API statements, counted here but not shown.

## `ReconstructionConjecture.reconstruction_conjecture`

Open: stated without proof.

> **The reconstruction conjecture** (Kelly [Ke57], Ulam [Ul60]).
>
> Every finite simple graph on at least three vertices is determined up to isomorphism by its
> deck of vertex-deleted subgraphs: any two hypomorphic graphs on at least three vertices are
> isomorphic.

```lean
theorem reconstruction_conjecture {V W : Type} [Fintype V] [Fintype W]
    (hV : 3 ≤ Fintype.card V) (G : SimpleGraph V) (H : SimpleGraph W)
    (h : Hypomorphic G H) : Nonempty (G ≃g H)
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/ReconstructionConjecture.lean, line 92](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/ReconstructionConjecture.lean#L92).

## `ReconstructionConjecture.reconstruction_conjecture.variants.tree`

Solved: stated here without proof.

> **Trees are reconstructible** (Kelly [Ke57]).
>
> Every tree on at least three vertices is determined up to isomorphism by its deck of
> vertex-deleted subgraphs.

```lean
theorem reconstruction_conjecture.variants.tree {V W : Type} [Fintype V] [Fintype W]
    (hV : 3 ≤ Fintype.card V) (G : SimpleGraph V) (H : SimpleGraph W)
    (hc : G.Connected) (ha : G.IsAcyclic) (h : Hypomorphic G H) : Nonempty (G ≃g H)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/ReconstructionConjecture.lean, line 104](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/ReconstructionConjecture.lean#L104).

## `ReconstructionConjecture.reconstruction_conjecture.variants.disconnected`

Solved: stated here without proof.

> **Disconnected graphs are reconstructible.**
>
> Every disconnected graph on at least three vertices is determined up to isomorphism by its
> deck of vertex-deleted subgraphs; see [Bo91].

```lean
theorem reconstruction_conjecture.variants.disconnected {V W : Type} [Fintype V] [Fintype W]
    (hV : 3 ≤ Fintype.card V) (G : SimpleGraph V) (H : SimpleGraph W)
    (hd : ¬G.Connected) (h : Hypomorphic G H) : Nonempty (G ≃g H)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/ReconstructionConjecture.lean, line 116](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/ReconstructionConjecture.lean#L116).

## `ReconstructionConjecture.edge_reconstruction_conjecture`

Open: stated without proof.

> **The edge reconstruction conjecture** (Harary [Ha64]).
>
> Every finite simple graph with at least four edges is determined up to isomorphism by its
> deck of edge-deleted subgraphs: any two edge-hypomorphic graphs on the same vertex set with
> at least four edges are isomorphic.

```lean
theorem edge_reconstruction_conjecture {V : Type} [Fintype V] (G H : SimpleGraph V)
    (hE : 4 ≤ G.edgeSet.ncard) (h : EdgeHypomorphic G H) : Nonempty (G ≃g H)
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/ReconstructionConjecture.lean, line 152](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/ReconstructionConjecture.lean#L152).

## `ReconstructionConjecture.edge_reconstruction_conjecture.variants.lovasz`

Solved: stated here without proof.

> **Lovász (1972): graphs with more than half of all possible edges are edge-reconstructible.**
>
> If a graph on `n` vertices has more than `n (n - 1) / 4` edges, then it is determined up to
> isomorphism by its deck of edge-deleted subgraphs.
>
> *Reference:* [Lo72].

```lean
theorem edge_reconstruction_conjecture.variants.lovasz {V : Type} [Fintype V]
    (G H : SimpleGraph V) (hE : (Fintype.card V).choose 2 < 2 * G.edgeSet.ncard)
    (h : EdgeHypomorphic G H) : Nonempty (G ≃g H)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/ReconstructionConjecture.lean, line 165](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/ReconstructionConjecture.lean#L165).

## `ReconstructionConjecture.edge_reconstruction_conjecture.variants.mueller`

Solved: stated here without proof.

> **Müller (1977): graphs with many edges are edge-reconstructible.**
>
> If a graph on `n` vertices with `m` edges satisfies `n! < 2 ^ (m - 1)`, then it is determined
> up to isomorphism by its deck of edge-deleted subgraphs.
>
> *Reference:* [Mu77].

```lean
theorem edge_reconstruction_conjecture.variants.mueller {V : Type} [Fintype V]
    (G H : SimpleGraph V) (hE : Nat.factorial (Fintype.card V) < 2 ^ (G.edgeSet.ncard - 1))
    (h : EdgeHypomorphic G H) : Nonempty (G ≃g H)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/ReconstructionConjecture.lean, line 179](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/ReconstructionConjecture.lean#L179).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/ReconstructionConjecture.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/ReconstructionConjecture.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Reconstruction_conjecture)
