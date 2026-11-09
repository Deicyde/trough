---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture198a.conjecture198a
statement: formalized
---

# Written on the Wall II - Conjecture 198a

> *Reference:*
> [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture198a.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture198a.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `WrittenOnTheWallII.GraphConjecture198a.conjecture198a`

Solved: stated here; a Lean proof is at [https://github.com/lukekabbash/wowii-198a-lean/blob/49f080bbaee83821e9e9744eef14c5acaae2a101/lean/src/ConditionalMain.lean#L52-L57](https://github.com/lukekabbash/wowii-198a-lean/blob/49f080bbaee83821e9e9744eef14c5acaae2a101/lean/src/ConditionalMain.lean#L52-L57).

> WOWII [Conjecture 198a](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
>
> For a simple connected graph `G`, if `b(G) ≤ 2 + ecc_avg(G)`, then `G` has a Hamiltonian path.
> Here `b(G)` is the number of vertices in a largest induced bipartite subgraph, and
> `ecc_avg(G)` is the average eccentricity of `G`.
> A Hamiltonian path is a walk visiting every vertex exactly once.
>
> Proofs and formalizations include:
> * [Ben Cohen, *Average Eccentricity, Induced Bipartite Subgraphs, and Hamiltonian Paths*](https://zenodo.org/records/21481944) (July 21, 2026); [Lean 4 formalization](https://github.com/bzcohen588/written-on-the-wall-198a/blob/5481927df49c374b06fa0931b5aa24f9296faa04/Conjecture198a.lean), publicly posted and verified September 16, 2026.
> * [Luke Kabbash, *A Hamiltonian-Path Criterion from Bipartite Number and Average Eccentricity*](https://github.com/lukekabbash/wowii-198a-lean/blob/49f080bbaee83821e9e9744eef14c5acaae2a101/paper/main.pdf); Lean 4 formalization publicly posted and passed its recorded verification July 23, 2026.

```lean
theorem conjecture198a (G : SimpleGraph α) (h : G.Connected)
    (hb : b G ≤ 2 + averageEccentricity G) :
    ∃ a b : α, ∃ p : G.Walk a b, p.IsHamiltonian
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture198a.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture198a.lean#L50).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture198a.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture198a.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
