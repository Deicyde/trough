---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture430a.conjecture430a
statement: formalized
---

# Written on the Wall II - Conjecture 430a

> *Reference:*
> [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
>
> The conjecture is false for the nonuniform clique blow-up of `P₇` with blob
> orders `(1,4,12,19,12,4,1)`. Its independent domination number is three, its
> center-neighborhood independence number is two, and its Caro--Wei sum is less
> than two. The claimed inequality therefore becomes `3 ≤ 2`.

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture430a.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture430a.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `WrittenOnTheWallII.GraphConjecture430a.conjecture430a`

Solved: stated here; a Lean proof is at [https://github.com/Kuberwastaken/c5-k4/blob/85fff48cdd7cc1f743802320fdc94db14d1f841e/lean/GraphConjecture430a.lean#L1-L390](https://github.com/Kuberwastaken/c5-k4/blob/85fff48cdd7cc1f743802320fdc94db14d1f841e/lean/GraphConjecture430a.lean#L1-L390).

> WOWII Conjecture 430a asked whether every connected graph `G` of order
> greater than three satisfies
> `i(G) ≤ α(G[N(C)]) + 2 floor(CW(G)-1)`.
> The answer is no, witnessed by a nonuniform `P₇` clique blow-up.

```lean
theorem conjecture430a :
    ¬ ∀ (V : Type) [Fintype V] [DecidableEq V] [Nonempty V]
      (G : SimpleGraph V) [DecidableRel G.Adj],
      G.Connected → 3 < Fintype.card V →
        (G.indepDominationNumber : ℤ) ≤
          ((G.induce
            (setNeighborhood G (centerFinset G) : Set V)).indepNum : ℤ) +
            2 * ⌊caroWei G - 1⌋
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture430a.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture430a.lean#L65).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture430a.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture430a.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
