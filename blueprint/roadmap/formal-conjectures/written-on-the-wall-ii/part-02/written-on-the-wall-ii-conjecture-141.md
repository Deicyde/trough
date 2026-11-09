---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture141.conjecture141
statement: formalized
proof: formalized
---

# Written on the Wall II - Conjecture 141

> *Reference:*
> [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture141.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture141.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `WrittenOnTheWallII.GraphConjecture141.conjecture141`

Proved here.

> WOWII [Conjecture 141](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
>
> For a simple connected graph $G$,
> $\mathrm{tree}(G) \ge (1/2) \cdot \mathrm{girth}(G) - 1 + \max_v l(v)$
> where $\mathrm{tree}(G)$ is the number of vertices of a largest induced tree subgraph,
> $\mathrm{girth}(G)$ is the length of the shortest cycle ($0$ if acyclic), and
> $l(v)$ (`indepNeighborsCard G v`) is the independence number of the neighbourhood of $v$.

```lean
theorem conjecture141 (G : SimpleGraph α) [DecidableRel G.Adj] (h : G.Connected) :
    (G.girth : ℝ) / 2 - 1 + ((Finset.univ.sup (indepNeighborsCard G) : ℕ) : ℝ) ≤
    (largestInducedTreeSize G : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture141.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture141.lean#L45).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture141.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture141.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
