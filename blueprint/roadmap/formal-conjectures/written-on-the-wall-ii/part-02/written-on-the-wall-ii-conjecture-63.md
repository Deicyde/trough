---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture63.conjecture63
statement: formalized
---

# Written on the Wall II - Conjecture 63

> *Reference:*
> [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
>
> ## Counterexample
>
> The conjecture is false for the lexicographic product $C_5[K_4]$. This graph
> has minimum even-distance count $9$, while its largest induced forest and
> largest induced bipartite subgraph both have order $4$. The conjectured lower
> bound is therefore $\lceil(9 + 4 + 1)/3\rceil = 5 > 4$.

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture63.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture63.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `WrittenOnTheWallII.GraphConjecture63.conjecture63`

Solved: stated here; a Lean proof is at [https://github.com/Kuberwastaken/wowii-63-85-counterexample/blob/cba739842ec59adf7426c180009175b31935701d/lean/WOWII63.lean#L184-L195](https://github.com/Kuberwastaken/wowii-63-85-counterexample/blob/cba739842ec59adf7426c180009175b31935701d/lean/WOWII63.lean#L184-L195).

> WOWII [Conjecture 63](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
> asked whether every simple connected graph $G$ satisfies
> $f(G) \geq \lceil(\min_v \operatorname{distEven}(v) + b(G) + 1)/3\rceil$.
> The answer is no, as witnessed by $C_5[K_4]$.

```lean
theorem conjecture63 :
    ¬ ∀ (α : Type) [Fintype α] [DecidableEq α] [Nontrivial α]
      (G : SimpleGraph α) (_h : G.Connected),
      let minDistEven := (Finset.univ.image (G.distEven ·)).min' (by simp)
      ⌈((minDistEven : ℝ) + G.b + 1) / 3⌉ ≤ (G.largestInducedForestSize : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture63.lean, line 49](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture63.lean#L49).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture63.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture63.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
