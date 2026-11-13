---
declaration: theorem
origin: cited
lean: Arxiv.«2001.02665».ringel_conjecture_large, Arxiv.«2001.02665».kotzig_conjecture_large
statement: formalized
---

# Ringel's Conjecture and Kotzig's Conjecture for large $n$

> *Reference:* [arxiv/2001.02665](https://arxiv.org/abs/2001.02665)
> **A proof of Ringel's Conjecture**
> by *Richard Montgomery, Alexey Pokrovskiy, Benny Sudakov*
>
> The original conjecture of Ringel (1963), which remains open, is stated in
> `Paper/RingelConjecture.lean`. The referenced paper proves it for all sufficiently large $n$.
>
> Montgomery–Pokrovskiy–Sudakov actually prove the strictly stronger statement conjectured by
> Kotzig: the decomposition can always be realized by cyclic shifts of a single copy of $T$.
> Kotzig's conjecture (all $n$) remains open; see `Paper/KotzigConjecture.lean`.

*Quoted from [FormalConjectures/Arxiv/2001.02665/RingelConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/2001.02665/RingelConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 solved.

## `Arxiv.«2001.02665».ringel_conjecture_large`

Solved: stated here without proof.

> For all sufficiently large $n$, the complete graph $K_{2n+1}$ decomposes into
> $2n+1$ edge-disjoint copies of any tree $T$ with $n$ edges.
>
> A "copy" of $T$ is the image $T.\text{map}(f_i)$ of $T$ under a vertex embedding
> $f_i : V \hookrightarrow \text{Fin}(2n+1)$; the copies are pairwise edge-disjoint
> and together cover every edge of $K_{2n+1}$.
>
> This follows from `kotzig_conjecture_large`; see `Paper/RingelConjecture.lean` for the open form.

```lean
theorem ringel_conjecture_large :
    ∀ᶠ (n : ℕ) in Filter.atTop, ∀ {V : Type} [Finite V] (T : SimpleGraph V),
      T.IsTree → T.edgeSet.ncard = n →
      ∃ f : Fin (2 * n + 1) → (V ↪ Fin (2 * n + 1)),
        Pairwise (fun i j => Disjoint (T.map (f i)).edgeSet (T.map (f j)).edgeSet) ∧
        ⨆ i, T.map (f i) = (⊤ : SimpleGraph (Fin (2 * n + 1)))
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Arxiv/2001.02665/RingelConjecture.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/2001.02665/RingelConjecture.lean#L51).

## `Arxiv.«2001.02665».kotzig_conjecture_large`

Solved: stated here without proof.

> For all sufficiently large $n$, the complete graph $K_{2n+1}$ decomposes into
> $2n+1$ edge-disjoint copies of any tree $T$ with $n$ edges via cyclic shifts of a single
> embedding.
>
> The $2n+1$ copies are $f_0, f_1, \dots, f_{2n}$ where $f_i(v) = f_0(v) + i$ for all vertices
> $v$ — that is, each copy is obtained by adding $i \pmod{2n+1}$ to every vertex of the
> base copy. This is strictly stronger than `ringel_conjecture_large`.
>
> Kotzig conjectured this holds for all $n$; see `Paper/KotzigConjecture.lean`. Montgomery,
> Pokrovskiy, and Sudakov prove it for all sufficiently large $n$.

```lean
theorem kotzig_conjecture_large :
    ∀ᶠ (n : ℕ) in Filter.atTop, ∀ {V : Type} [Finite V] (T : SimpleGraph V),
      T.IsTree → T.edgeSet.ncard = n →
      ∃ f : Fin (2 * n + 1) → (V ↪ Fin (2 * n + 1)),
        (∀ i v, f i v = f 0 v + i) ∧
        Pairwise (fun i j => Disjoint (T.map (f i)).edgeSet (T.map (f j)).edgeSet) ∧
        ⨆ i, T.map (f i) = (⊤ : SimpleGraph (Fin (2 * n + 1)))
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Arxiv/2001.02665/RingelConjecture.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/2001.02665/RingelConjecture.lean#L72).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Arxiv/2001.02665/RingelConjecture.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/2001.02665/RingelConjecture.lean)
- [arxiv/2001.02665](https://arxiv.org/abs/2001.02665)
