---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture58.conjecture58
statement: formalized
---

# Written on the Wall II - Conjecture 58

> *Reference:*
> [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
>
> ## Counterexample
>
> The conjecture is false. A counterexample is given by taking $K_{3,3}$
> (with bipartition $\{0,1,2\}$, $\{3,4,5\}$) and $K_{73}$ (on vertices $\{6,\ldots,78\}$),
> then adding edges between vertex $0$ and every vertex of $K_{73}$.
>
> This graph $G$ has $n = 79$ vertices and satisfies:
> - $b(G) \ge 7$: the set $\{0,1,2,3,4,5,6\}$ induces a bipartite subgraph
> - $f(G) \le 6$: the largest induced forest has at most 6 vertices
> - $l_{\mathrm{avg}}(G) = 92/79$
> - $\lceil b(G) / l_{\mathrm{avg}}(G) \rceil \ge 7 > 6 \ge f(G)$

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture58.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture58.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `WrittenOnTheWallII.GraphConjecture58.conjecture58`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/4bd72a06842a10e1b8d7bb0fd6b1ef5e6bd20210/FormalConjectures/WrittenOnTheWallII/GraphConjecture58.lean#L772](https://github.com/mo271/formal-conjectures/blob/4bd72a06842a10e1b8d7bb0fd6b1ef5e6bd20210/FormalConjectures/WrittenOnTheWallII/GraphConjecture58.lean#L772).

> WOWII [Conjecture 58](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
>
> For a connected graph `G`, the size `f(G)` of a largest induced forest satisfies
> `f(G) ≥ ceil( b(G) / average l(v) )` where `b(G)` is the largest induced
> bipartite subgraph and `l(v)` is the independence number of `G.neighborSet v`.
>
> This conjecture is false. A counterexample is the graph described in the module docstring
> above: a $K_{3,3}$ joined to a $K_{73}$ via vertex $0$, giving
> $\lceil b/l_{\mathrm{avg}} \rceil \ge 7 > 6 \ge f(G)$.
>
> The counterexample has been found by Moritz Firsching and Goran Žužić using an
> experimental pipeline.

```lean
theorem conjecture58 :
    ¬ ∀ (α : Type) [Fintype α] [DecidableEq α] [Nontrivial α]
      (G : SimpleGraph α) [DecidableRel G.Adj] (_hG : G.Connected),
      Nat.ceil (G.b / G.l_avg) ≤ G.largestInducedForestSize
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture58.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture58.lean#L63).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture58.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture58.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
