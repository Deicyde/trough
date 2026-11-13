---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture32.conjecture32
statement: formalized
---

# Written on the Wall II - Conjecture 32

> *Reference:*
> [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture32.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture32.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `WrittenOnTheWallII.GraphConjecture32.conjecture32`

Solved: stated here; a Lean proof is at [https://github.com/VictorLiwentao/lean-graph-proofs/blob/b60c2e548910b32eb3b602f6a8e67af806e4b9f6/LeanGraphProofs/WOWII32.lean#L114](https://github.com/VictorLiwentao/lean-graph-proofs/blob/b60c2e548910b32eb3b602f6a8e67af806e4b9f6/LeanGraphProofs/WOWII32.lean#L114).

> WOWII [Conjecture 32](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
>
> For a simple connected graph $G$,
> $\operatorname{path}(G) \ge \operatorname{dist}\_{\operatorname{avg}}(A) + 0.5 \cdot \operatorname{ecc}\_{\operatorname{avg}}(M)$,
> where $\operatorname{path}(G)$ is the number of vertices of a largest induced path of $G$,
> $A$ is the set of minimum-degree vertices, $M$ is the set of maximum-degree vertices,
> $\operatorname{dist}\_{\operatorname{avg}}(A)$ is the average of all nonzero distances
> $\operatorname{dist}\_G(u, v)$ with $u, v \in A$ (i.e. the average over ordered pairs of
> distinct vertices of $A$; it is taken to be $0$ when $A$ has fewer than two vertices), and
> $\operatorname{ecc}\_{\operatorname{avg}}(M)$ is the average eccentricity of the vertices
> in $M$.
>
> The conjecture is false, the authors present a counterexample: "The path on 5 vertices
> is a counterexample, path = 5, distavg(A) = 4 and the average of eccentricity of maximum
> degree vertices is 8/3."
>
> Independent Lean formalization by Wentao Li, with AI assistance. An earlier Lean proof
> is recorded in the Epoch review archived in
> [tadamcz/fc-review-results](https://github.com/tadamcz/fc-review-results/blob/971290dd3e0e4dce063f98feaa8ecb9e51acd5ec/data/782312817c/files/WrittenOnTheWallII/GraphConjecture32.json).

```lean
theorem conjecture32 :
    ¬ ∀ (α : Type) [Fintype α] [DecidableEq α] [Nontrivial α]
      (G : SimpleGraph α) [DecidableRel G.Adj] (h : G.Connected),
      let A : Finset α := Finset.univ.filter (fun v => G.degree v = G.minDegree)
      let M : Finset α := Finset.univ.filter (fun v => G.degree v = G.maxDegree)
      let distavgA : ℝ := (∑ p ∈ A.offDiag, (G.dist p.1 p.2 : ℝ)) / (A.offDiag.card : ℝ)
      let eccavg (S : Finset α) : ℝ := (∑ v ∈ S, (G.eccent v).toNat) / (S.card : ℝ)
      distavgA + (1 / 2 : ℝ) * eccavg M ≤ (path G : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture32.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture32.lean#L59).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture32.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture32.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
