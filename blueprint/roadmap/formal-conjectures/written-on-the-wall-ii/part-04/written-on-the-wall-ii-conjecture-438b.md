---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture438b.conjecture438b
statement: formalized
---

# Written on the Wall II - Conjecture 438b

> *Reference:*
> [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
>
> WOWII 438b asks whether
>
> `alpha₂(G) ≤ alpha(G) + alpha(G[V \ H₂]) + |E(G[H₂])|`,
>
> where `H₂` is the set of vertices of degree at most two. The conjecture is
> true. In fact, the same inequality holds with an arbitrary vertex subset in
> place of `H₂`.

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture438b.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture438b.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `WrittenOnTheWallII.GraphConjecture438b.conjecture438b`

Solved: stated here; a Lean proof is at [https://github.com/Kuberwastaken/c5-k4/blob/e62f216625438bc099707e466d2825ab483717a4/lean/GraphConjecture438b.lean](https://github.com/Kuberwastaken/c5-k4/blob/e62f216625438bc099707e466d2825ab483717a4/lean/GraphConjecture438b.lean).

> WOWII 438b states that every connected graph of order greater than three
> satisfies
> `alpha₂(G) ≤ alpha(G) + alpha(G[V \ H₂]) + |E(G[H₂])|`.

```lean
theorem conjecture438b :
    ∀ (V : Type) [Fintype V] [DecidableEq V] (G : SimpleGraph V)
      [DecidableRel G.Adj], G.Connected → 3 < Fintype.card V →
      alphaTwo G ≤ G.indepNum +
        indepNumOn G (Finset.univ \ lowDegreeLayer G) +
        (internalEdges G (lowDegreeLayer G)).card
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture438b.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture438b.lean#L50).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture438b.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture438b.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
