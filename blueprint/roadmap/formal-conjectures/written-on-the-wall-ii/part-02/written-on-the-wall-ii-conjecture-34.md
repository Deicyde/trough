---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture34.conjecture34
statement: formalized
---

# Written on the Wall II - Conjecture 34

> *Reference:*
> [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture34.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture34.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `WrittenOnTheWallII.GraphConjecture34.conjecture34`

Solved: stated here; a Lean proof is at [https://github.com/VictorLiwentao/lean-graph-proofs/blob/b60c2e548910b32eb3b602f6a8e67af806e4b9f6/LeanGraphProofs/WOWII34.lean#L350](https://github.com/VictorLiwentao/lean-graph-proofs/blob/b60c2e548910b32eb3b602f6a8e67af806e4b9f6/LeanGraphProofs/WOWII34.lean#L350).

> WOWII [Conjecture 34](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
>
> For a simple connected graph $G$,
> $\operatorname{path}(G) \ge \lceil \operatorname{dist}\_{\operatorname{avg}}(C, V)
> + \operatorname{dist}\_{\operatorname{avg}}(M, V) \rceil$,
> where $\operatorname{path}(G)$ is the number of vertices of a largest induced path of $G$,
> $C$ is the set of center vertices (those with minimum eccentricity), $M$ is the set of
> maximum-degree vertices, and $\operatorname{dist}\_{\operatorname{avg}}(S, V)$ is the average
> of all nonzero distances $\operatorname{dist}\_G(s, v)$ with $s \in S$ and $v \in V$.
>
> The conjecture is false. The counterexample below was documented by
> [Salvatore Mercuri](https://github.com/google-deepmind/formal-conjectures/pull/5733).
> Let $G$ be the tree on $39$ vertices formed by a vertex with three
> pendant leaves, joined by a path of five edges to the root of a perfect binary tree of depth
> four. Then $\operatorname{path}(G) = 11$, while $C$ and $M$ are singletons whose distance sums
> are $154$ and $266$, so the bound is $\lceil (154 + 266) / 38 \rceil = 12$.
>
> Lean formalization by Wentao Li, with AI assistance.

```lean
theorem conjecture34 :
    ¬ ∀ (α : Type) [Fintype α] [DecidableEq α] [Nontrivial α]
      (G : SimpleGraph α) [DecidableRel G.Adj] (h : G.Connected),
      let C : Set α := center G
      let M : Set α := {v | G.degree v = G.maxDegree}
      let distAvg (S : Set α) : ℝ :=
        open scoped Classical in
        let pairs := (S.toFinset ×ˢ Finset.univ).filter (fun p => G.dist p.1 p.2 ≠ 0)
        (∑ p ∈ pairs, (G.dist p.1 p.2 : ℝ)) / pairs.card
      Int.ceil (distAvg C + distAvg M) ≤ (path G : ℤ)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture34.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture34.lean#L58).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture34.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture34.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
