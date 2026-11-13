---
declaration: theorem
origin: cited
lean: Erdos274.erdos_274, Erdos274.erdos_274.variants.abelian, Erdos274.herzog_schonheim
statement: formalized
---

# Erdős Problem 274

> *References:*
> * [erdosproblems.com/274](https://www.erdosproblems.com/274)
> * [Wikipedia](https://en.wikipedia.org/wiki/Herzog%E2%80%93Sch%C3%B6nheim_conjecture)
> * [arXiv:1803.08301](https://arxiv.org/abs/1803.08301)
> * [arXiv:1803.03569](https://arxiv.org/abs/1803.03569)
> * [PMC7247885](https://pmc.ncbi.nlm.nih.gov/articles/PMC7247885/)
> * [arXiv:1804.11103](https://arxiv.org/abs/1804.11103)

*Quoted from [FormalConjectures/ErdosProblems/274.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/274.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/274](https://www.erdosproblems.com/274).

The file states 3 research or textbook statements: 2 open and 1 solved.

## `Erdos274.erdos_274`

Open: stated without proof.

> If $G$ is a group, can there exist an exact covering of $G$ by more than one coset
> of different sizes? (i.e. each element is contained in exactly one of the cosets.)
>
> The conjectured answer is no: in every such exact covering, two of the subgroups have
> the same cardinality.

```lean
theorem erdos_274 : ∃ (G : Type*) (_ : Group G),
    1 < ENat.card G ∧ ∃ (ι : Type*) (_ : Fintype ι) (P : Group.ExactCovering G ι),
    1 < Fintype.card ι ∧ ∀ i j, i ≠ j → #(P.parts i) ≠ #(P.parts j)
```

Category `research open`; AMS [20 Group theory and generalizations](../../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/ErdosProblems/274.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/274.lean#L63).

## `Erdos274.erdos_274.variants.abelian`

Solved: stated here; a Lean proof is at [https://github.com/Jostamon/erdos274-hs-abelian/blob/2ab8a2e39e7dd7836adf577b52555f069244466f/Erdos274/Main.lean](https://github.com/Jostamon/erdos274-hs-abelian/blob/2ab8a2e39e7dd7836adf577b52555f069244466f/Erdos274/Main.lean).

> If `G` is a finite abelian group then there cannot exist an exact covering of `G` by more
> than one cosets of different sizes? (i.e. each element is contained in exactly one
> of the cosets.)

```lean
theorem erdos_274.variants.abelian {G : Type*} [Fintype G] [CommGroup G]
    (hG : 1 < Fintype.card G) {ι : Type*} [Fintype ι] (P : Group.ExactCovering G ι)
    (hι : 1 < Fintype.card ι) :
    ∃ i j, i ≠ j ∧ #(P.parts i) = #(P.parts j)
```

Category `research solved`; AMS [20 Group theory and generalizations](../../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/ErdosProblems/274.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/274.lean#L76).

## `Erdos274.herzog_schonheim`

Open: stated without proof.

> Let $G$ be a group, and let $A = \{a_1G_1, \dots, a_kG_k\}$ be a finite system of left cosets of
> subgroups $G_1, \dots, G_k$ of $G$.
>
> Herzog and Schönheim conjectured that if $A$ forms a partition of $G$ with $k > 1$, then the
> indices $[G:G_1], \dots, [G:G_k]$ cannot be distinct.

```lean
theorem herzog_schonheim {G : Type*} [Group G] (hG : 1 < ENat.card G) {ι : Type*} [Fintype ι]
    (hι : 1 < Fintype.card ι) (P : Group.ExactCovering G ι) :
    ∃ i j, i ≠ j ∧ (P.parts i).index = (P.parts j).index
```

Category `research open`; AMS [20 Group theory and generalizations](../../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/ErdosProblems/274.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/274.lean#L90).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/274.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/274.lean)
- [erdosproblems.com/274](https://www.erdosproblems.com/274)
