---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture85.conjecture85
statement: formalized
---

# Written on the Wall II - Conjecture 85

> *Reference:*
> [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
>
> ## Counterexample
>
> The conjecture is false for the lexicographic product $C_5[K_4]$. This graph
> has minimum even-distance count $9$ and largest induced-tree order $4$. The
> conjectured lower bound is therefore $\lceil\sqrt{1 + 2 \cdot 9}\rceil =
> \lceil\sqrt{19}\rceil = 5 > 4$.

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture85.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture85.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `WrittenOnTheWallII.GraphConjecture85.conjecture85`

Solved: stated here; a Lean proof is at [https://github.com/Kuberwastaken/wowii-63-85-counterexample/blob/cba739842ec59adf7426c180009175b31935701d/lean/WOWII85.lean#L171-L183](https://github.com/Kuberwastaken/wowii-63-85-counterexample/blob/cba739842ec59adf7426c180009175b31935701d/lean/WOWII85.lean#L171-L183).

> WOWII [Conjecture 85](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
> asked whether every simple connected graph $G$ satisfies
> $\operatorname{tree}(G) \geq
> \lceil\sqrt{1 + 2\min_v \operatorname{distEven}(v)}\rceil$.
> The answer is no, as witnessed by $C_5[K_4]$.

```lean
theorem conjecture85 :
    ¬ ∀ (α : Type) [Fintype α] [DecidableEq α] [Nontrivial α]
      (G : SimpleGraph α) (_h : G.Connected),
      let minDistEven := (Finset.univ.image (G.distEven ·)).min' (by simp)
      ⌈Real.sqrt (1 + 2 * (minDistEven : ℝ))⌉ ≤
        (G.largestInducedTreeSize : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture85.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture85.lean#L50).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture85.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture85.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
