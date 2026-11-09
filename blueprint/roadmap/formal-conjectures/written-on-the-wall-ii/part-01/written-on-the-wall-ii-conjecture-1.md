---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture1.conjecture1
statement: formalized
---

# Written on the Wall II - Conjecture 1

> *Reference:*
> [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture1.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture1.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `WrittenOnTheWallII.GraphConjecture1.conjecture1`

Solved: stated here; a Lean proof is at [https://github.com/MiskinAleksandr23/WOWII-1/blob/eda16f6e96b313bd112351ae9859133b77d537c9/WOWII1/GraphConjecture1.lean](https://github.com/MiskinAleksandr23/WOWII-1/blob/eda16f6e96b313bd112351ae9859133b77d537c9/WOWII1/GraphConjecture1.lean).

> WOWII [Conjecture 1](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
>
> For a simple connected graph `G` the maximum number of leaves of a spanning
> tree satisfies `Ls(G) ≥ n(G) + 1 - 2·m(G)` where `n(G)` counts vertices and
> `m(G)` is the size of a maximum matching.
>
> A formal proof reduces to a spanning tree `T`. If `I` is the set of non-leaves
> of `T`, Hall's theorem applied to a bipartition of `T` gives a matching `M`
> with `|I| + 1 ≤ 2 * |M|`. Since `|V|` is the sum of the numbers of leaves and
> non-leaves, and every matching and leaf count constructed in `T` is admissible
> for the corresponding supremum in `G`, the stated inequality follows.

```lean
theorem conjecture1 {α : Type*} [Fintype α] [DecidableEq α] [Nontrivial α]
    (G : SimpleGraph α) [DecidableRel G.Adj] (h_conn : G.Connected) :
    (Fintype.card α : ℝ) + 1 - 2 * matchingNumber G ≤ (Ls G : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture1.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture1.lean#L51).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture1.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture1.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
