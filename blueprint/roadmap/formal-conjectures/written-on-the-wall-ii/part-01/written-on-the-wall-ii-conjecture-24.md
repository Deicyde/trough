---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture24.conjecture24
statement: formalized
---

# Written on the Wall II - Conjecture 24

> **Verbatim statement (WOWII #24, status F):**
> > If G is a simple connected graph, then b(G) ≥ λ(G) + CEIL[minimum of dist_even(v)/3]
>
> **Source:** http://cms.uhd.edu/faculty/delavinae/research/wowII/all.html#conj24
>
> The WOWII page records this conjecture as disproved (status F).
>
> *Reference:*
> [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture24.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture24.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `WrittenOnTheWallII.GraphConjecture24.conjecture24`

Solved: stated here without proof.

> WOWII [Conjecture 24](http://cms.uhd.edu/faculty/delavinae/research/wowII/all.html#conj24)
> (status F, disproved):
>
> For every finite simple connected graph `G`,
> `b(G) ≥ λ(G) + ⌈(min_v dist_even(v)) / 3⌉`
> where `b(G)` is the size of a largest induced bipartite subgraph,
> `λ(G) := max_v l(v)` is the maximum over all vertices of the independence
> number of the open neighbourhood of `v`, and `dist_even(v)` is the number of
> vertices at even distance from `v`.

```lean
theorem conjecture24 :
    ¬ ∀ {α : Type*} [Fintype α] [DecidableEq α] [Nontrivial α],
      ∀ (G : SimpleGraph α) (_ : G.Connected),
        let maxL := (Finset.univ.image (fun v => indepNeighborsCard G v)).max' (by simp)
        let minDistEven := (Finset.univ.image (distEven G)).min' (by simp)
        (maxL : ℝ) + ⌈(minDistEven : ℝ) / 3⌉ ≤ b G
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture24.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture24.lean#L53).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture24.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture24.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
