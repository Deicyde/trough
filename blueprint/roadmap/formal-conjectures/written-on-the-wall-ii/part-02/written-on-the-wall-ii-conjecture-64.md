---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture64.conjecture64
statement: formalized
---

# Written on the Wall II - Conjecture 64

> *References:*
> - [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
> - [J. J. Gebendorfer, Clique Blow-ups of the 5-Cycle and Written on the Wall II
>   Conjecture 64](https://doi.org/10.5281/zenodo.21595503)
>
> Gebendorfer recorded the disproof on 26 July 2026, crediting Kuberwastaken's
> earlier $C_5[K_4]$ certificate for the graph and its induced-forest computation.
> The linked Lean certificate formalizes this 20-vertex counterexample.

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture64.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture64.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `WrittenOnTheWallII.GraphConjecture64.conjecture64`

Solved: stated here; a Lean proof is at [https://github.com/Kuberwastaken/c5-k4/blob/8c0a76079e5c7153bdc2dd6d97a9821ee25b2620/lean/GraphConjecture64.lean](https://github.com/Kuberwastaken/c5-k4/blob/8c0a76079e5c7153bdc2dd6d97a9821ee25b2620/lean/GraphConjecture64.lean).

> WOWII Conjecture 64 proposed that every finite simple connected graph $G$ satisfies
>
> $$
> f(G) \geq \left\lceil\sqrt{\alpha(G)\bigl(1+(|V(G)|\bmod\Delta(G))\bigr)}\right\rceil,
> $$
>
> where $f(G)$ is the maximum order of an induced forest.
> For $C_5[K_4]$, the forest number is $4$, the independence number is $2$,
> and the proposed lower bound is $\lceil\sqrt{2(1+9)}\rceil=5$.
>
> The remainder and product in the radicand are computed in $\mathbb{N}$ before
> coercion to $\mathbb{R}$. Nontriviality excludes the one-vertex graph, whose
> maximum degree is zero.

```lean
theorem conjecture64 :
    ¬ ∀ (α : Type) [Fintype α] [DecidableEq α] [Nontrivial α]
      (G : SimpleGraph α) [DecidableRel G.Adj] (_h : G.Connected),
      ⌈Real.sqrt ((G.indepNum * (1 + Fintype.card α % G.maxDegree) : ℕ) : ℝ)⌉ ≤
        (G.largestInducedForestSize : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture64.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture64.lean#L56).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture64.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture64.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
