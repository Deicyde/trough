---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture372.conjecture372, WrittenOnTheWallII.GraphConjecture372.conjecture372.variants.two_paths, WrittenOnTheWallII.GraphConjecture372.conjecture372.variants.regularized
statement: formalized
---

# Written on the Wall II - Conjecture 372

> *References:*
> * [E. DeLaViña, Written on the Wall II, Conjecture 372](http://cms.uhd.edu/faculty/delavinae/research/wowII/open.html)
> * [J. J. Gebendorfer, Total domination and vertex covers of trees covered by two paths](https://doi.org/10.13140/RG.2.2.25035.55849)
>
> The source ratio uses the total domination number, the minimum vertex cover
> cardinality, and the minimum number of pairwise vertex-disjoint paths covering
> all vertices. Singleton paths are allowed. The ratio is restricted to path
> cover number at least two; it is undefined on paths. The last declaration is
> a separate, everywhere-defined formulation for trees of order at least two.

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture372.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/WrittenOnTheWallII/GraphConjecture372.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 3 open.

## `WrittenOnTheWallII.GraphConjecture372.conjecture372`

Open: stated without proof.

> WOWII Conjecture 372 on its positive-denominator domain. If $T$ is a tree with
> more than two vertices and path cover number $p(T) \ge 2$, then
> $\gamma_t(T) \ge \tau(T)/(p(T)-1)$, where $\gamma_t$ is the total domination
> number and $\tau$ is the vertex cover number.

```lean
theorem conjecture372 (hT : T.IsTree) (hn : 2 < Fintype.card α)
    (hp : 2 ≤ T.pathCoverNumber) :
    (T.vertexCoverNum.toNat : ℝ) / ((T.pathCoverNumber : ℝ) - 1) ≤
      T.totalDominationNumber
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture372.lean, line 49](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/WrittenOnTheWallII/GraphConjecture372.lean#L49).

## `WrittenOnTheWallII.GraphConjecture372.conjecture372.variants.two_paths`

Open: stated without proof.

> The two-path variant: a tree $T$ of order at least two with $p(T) \le 2$
> satisfies $\tau(T) \le \gamma_t(T)$.

```lean
theorem conjecture372.variants.two_paths (hT : T.IsTree)
    (hn : 2 ≤ Fintype.card α) (hp : T.pathCoverNumber ≤ 2) :
    T.vertexCoverNum.toNat ≤ T.totalDominationNumber
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture372.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/WrittenOnTheWallII/GraphConjecture372.lean#L60).

## `WrittenOnTheWallII.GraphConjecture372.conjecture372.variants.regularized`

Open: stated without proof.

> A separate formulation with no division: every tree $T$ of order at least two
> satisfies $\tau(T) \le \gamma_t(T)\max\{1,p(T)-1\}$. On paths the factor is one.

```lean
theorem conjecture372.variants.regularized (hT : T.IsTree)
    (hn : 2 ≤ Fintype.card α) :
    T.vertexCoverNum.toNat ≤ T.totalDominationNumber * max 1 (T.pathCoverNumber - 1)
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture372.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/WrittenOnTheWallII/GraphConjecture372.lean#L70).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture372.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/WrittenOnTheWallII/GraphConjecture372.lean)
- [E. DeLaViña, Written on the Wall II, Conjecture 372](http://cms.uhd.edu/faculty/delavinae/research/wowII/open.html)
