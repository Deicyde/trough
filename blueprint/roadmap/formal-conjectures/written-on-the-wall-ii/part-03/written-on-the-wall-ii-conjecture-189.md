---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture189.conjecture189
statement: formalized
---

# Written on the Wall II - Conjecture 189

> **Verbatim statement (WOWII #189, status O):**
> > If G is a simple connected graph with n > 1 such that maximum { dist_even(v) : dist_even(v) is the number of vertices at even distance from v } ≤ 1 + σ(G), then G has a Hamiltonian path.
>
> **Source:** http://cms.uhd.edu/faculty/delavinae/research/wowII/all.html#conj189
>
>
> *Reference:*
> [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture189.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture189.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `WrittenOnTheWallII.GraphConjecture189.conjecture189`

Open: stated without proof.

> WOWII [Conjecture 189](http://cms.uhd.edu/faculty/delavinae/research/wowII/all.html#conj189)
> (status O):
>
> For a simple connected graph `G`, if `max_v distEven(v) ≤ 1 + σ(G)`,
> then `G` has a Hamiltonian path.
>
> Here `distEven(v)` is the number of vertices at even distance from `v`, and
> `σ(G)` is the **second-smallest degree** of `G`'s degree sequence (per
> WOWII defEntry 65).

```lean
theorem conjecture189 (G : SimpleGraph α) [DecidableRel G.Adj] (h : G.Connected)
    (hσ : (Finset.univ.image (distEven G)).max' (by simp) ≤ 1 + secondSmallestDegree G) :
    ∃ a b : α, ∃ p : G.Walk a b, p.IsHamiltonian
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture189.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture189.lean#L54).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture189.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture189.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
