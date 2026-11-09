---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture33.conjecture33
statement: formalized
---

# Written on the Wall II - Conjecture 33

> *Reference:*
> [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture33.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture33.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `WrittenOnTheWallII.GraphConjecture33.conjecture33`

Solved: stated here without proof.

> WOWII [Conjecture 33](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
>
> For a simple connected graph $G$,
> $\operatorname{path}(G) \ge \lceil 2 \operatorname{dist}\_{\operatorname{avg}}(M, V) \rceil$,
> where $\operatorname{path}(G)$ is the number of vertices of a largest induced path of $G$,
> $M$ is the set of maximum-degree vertices, and
> $\operatorname{dist}\_{\operatorname{avg}}(M, V)$ is the average of all nonzero distances
> $\operatorname{dist}\_G(m, v)$ with $m \in M$ and $v \in V$.
>
> The conjecture is false: the source records an October 2005 counterexample with
> $\operatorname{path}(G) = 7$ and $\operatorname{dist}\_{\operatorname{avg}}(M, V) = 3.56$.

```lean
theorem conjecture33 :
    ¬ ∀ (α : Type) [Fintype α] [DecidableEq α] [Nontrivial α]
      (G : SimpleGraph α) [DecidableRel G.Adj] (h : G.Connected),
      let M : Set α := {v | G.degree v = G.maxDegree}
      let distAvg : ℝ :=
        open scoped Classical in
        let pairs := (M.toFinset ×ˢ Finset.univ).filter (fun p => G.dist p.1 p.2 ≠ 0)
        (∑ p ∈ pairs, (G.dist p.1 p.2 : ℝ)) / pairs.card
      Int.ceil (2 * distAvg) ≤ (path G : ℤ)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture33.lean, line 49](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture33.lean#L49).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture33.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture33.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
