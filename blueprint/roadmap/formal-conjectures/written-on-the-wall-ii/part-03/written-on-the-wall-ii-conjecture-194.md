---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture194.conjecture194
statement: formalized
---

# Written on the Wall II - Conjecture 194

> *Reference:*
> [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
>
> ## Counterexample
>
> The conjecture is false. Take a clique on vertices `0, ..., 10`, four additional vertices
> `11, ..., 14` adjacent to every clique vertex, and three leaves attached at `11`, `12`, and `14`.
> This connected graph has independence number `4`, while the sum of the independence numbers of its
> vertex neighbourhoods is `54`, so their average is `3`. Thus it satisfies the conjecture's
> hypothesis with equality. However, its three leaves would all have to be endpoints of a Hamiltonian
> path, which is impossible.

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture194.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture194.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `WrittenOnTheWallII.GraphConjecture194.conjecture194`

Solved: stated here; a Lean proof is at [https://github.com/anagnorisis2peripeteia/formal-conjectures/blob/4bff865a14c2cd61fefbffbe9c49cbfc5a89ac45/FormalConjectures/WrittenOnTheWallII/GraphConjecture194.lean#L128-L140](https://github.com/anagnorisis2peripeteia/formal-conjectures/blob/4bff865a14c2cd61fefbffbe9c49cbfc5a89ac45/FormalConjectures/WrittenOnTheWallII/GraphConjecture194.lean#L128-L140).

> WOWII [Conjecture 194](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
>
> For a simple connected graph `G`, if `α(G) ≤ 1 + l_avg(G)`, then `G` has a Hamiltonian path.
> Here `α(G) = G.indepNum` is the independence number, and
> `l_avg(G) = averageIndepNeighbors G` is the average over all vertices of the independence number
> of the neighbourhood.
> A Hamiltonian path is a walk visiting every vertex exactly once. The answer is no, as witnessed by
> the 18-vertex graph described above.
>
> Counterexample (Graph6): `Q~~~~~~~~~~~~}~}^~??G??_??_`

```lean
theorem conjecture194 :
    ¬ ∀ (α : Type) [Fintype α] [DecidableEq α] [Nontrivial α]
      (G : SimpleGraph α) (_h : G.Connected),
      (G.indepNum : ℝ) ≤ 1 + averageIndepNeighbors G →
      ∃ a b : α, ∃ p : G.Walk a b, p.IsHamiltonian
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture194.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture194.lean#L58).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture194.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture194.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
