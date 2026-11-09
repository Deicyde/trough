---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture199.conjecture199
statement: formalized
---

# Written on the Wall II - Conjecture 199

> **Verbatim statement (WOWII #199, status O):**
> > If G is a simple connected graph with n > 1 such that tree(G) - 2 ≤ κ(G), then G has a Hamiltonian path.
>
> **Source:** http://cms.uhd.edu/faculty/delavinae/research/wowII/all.html#conj199
>
>
> *Reference:*
> [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture199.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture199.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 4 test statements, counted here but not shown.

## `WrittenOnTheWallII.GraphConjecture199.conjecture199`

Open: stated without proof.

> WOWII [Conjecture 199](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
>
> For a simple connected graph `G`, if `tree(G) - 2 ≤ κ(G)`, then `G` has a Hamiltonian path.
> The nontrivial vertex type encodes the source assumption $n > 1$.
> Here `tree(G)` is the number of vertices in a largest induced tree and
> `κ(G) = vertexConnectivity G` is the vertex connectivity of `G`.

```lean
theorem conjecture199 (G : SimpleGraph α) (h : G.Connected)
    (hκ : largestInducedTreeSize G - 2 ≤ vertexConnectivity G) :
    ∃ a b : α, ∃ p : G.Walk a b, p.IsHamiltonian
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture199.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture199.lean#L51).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture199.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture199.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
