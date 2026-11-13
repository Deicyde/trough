---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture59.conjecture59
statement: formalized
---

# Written on the Wall II - Conjecture 59

> *References:*
> - [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture59.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture59.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `WrittenOnTheWallII.GraphConjecture59.conjecture59`

Solved: stated here; a Lean proof is at [https://github.com/QDKStorm/wowii59-counterexample/blob/main/Counterexample59.lean](https://github.com/QDKStorm/wowii59-counterexample/blob/main/Counterexample59.lean); a Lean proof is at [https://github.com/anagnorisis2peripeteia/formal-conjectures/blob/69388817d384ea44a5ef4b2aed1097c8281f9c3a/FormalConjectures/WrittenOnTheWallII/GraphConjecture59.lean](https://github.com/anagnorisis2peripeteia/formal-conjectures/blob/69388817d384ea44a5ef4b2aed1097c8281f9c3a/FormalConjectures/WrittenOnTheWallII/GraphConjecture59.lean).

> WOWII [Conjecture 59](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
>
> For a simple connected graph $G$, the size $f(G)$ of a largest induced forest
> satisfies $f(G) \ge \lceil \sqrt{\mathrm{residue}(G) \cdot b(G)} \rceil$, where
> $\mathrm{residue}(G)$ is the Havel-Hakimi residue (the number of zeros remaining
> after applying the Havel-Hakimi algorithm to the degree sequence until termination)
> and $b(G)$ is the size of a largest induced bipartite subgraph.
>
> See: Favaron, Mahéo, Saclé (1991) for the residue; DeLaVina's Graffiti.pc for the conjecture.
>
> This conjecture is false. There is a connected counterexample on 123 vertices
> with `residue G = 101`, `b G = 122`, and `G.largestInducedForestSize = 111`.
> Indeed, `101 * 122 = 12322 = 111 ^ 2 + 1`, so the conjectured lower bound is 112.
>
> There is also an 18-vertex counterexample. Take a bipartite chain graph on
> vertices `0, ..., 9`, with parts `{0, ..., 4}` and `{5, ..., 9}`, a hub `10`
> adjacent to every core vertex, and leaves `11, ..., 17` attached at the hub.
> It has residue 10, `b = 17`, and largest induced forest 13.
> `⌈√170⌉ = 14`, so it falsifies the bound.

```lean
theorem conjecture59 :
    ¬ ∀ (α : Type) [Fintype α] [DecidableEq α] [Nontrivial α]
      (G : SimpleGraph α) [DecidableRel G.Adj] (_ : G.Connected),
      ⌈Real.sqrt ((residue G : ℝ) * b G)⌉ ≤ (G.largestInducedForestSize : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture59.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture59.lean#L60).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture59.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture59.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
