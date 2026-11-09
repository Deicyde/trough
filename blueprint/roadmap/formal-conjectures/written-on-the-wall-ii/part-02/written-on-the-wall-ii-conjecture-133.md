---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture133.conjecture133
statement: formalized
---

# Written on the Wall II - Conjecture 133

> *Reference:*
> [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture133.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture133.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `WrittenOnTheWallII.GraphConjecture133.conjecture133`

Open: stated without proof.

> WOWII [Conjecture 133](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/):
>
> For a simple connected graph $G$,
> $\operatorname{path}(G) \ge \operatorname{rad}(G) +
> (\mathrm{avg}_v\, l(v))^{cC_4(G)}$,
> where $\operatorname{path}(G)$ is the path number of the graph (number of vertices of a largest induced path),
> $\operatorname{rad}(G)$ is the radius (minimum eccentricity, as a natural number),
> $\mathrm{avg}_v\, l(v) = l(G)$ is the average independence number of vertex
> neighbourhoods, and $cC_4(G)$ is the $C_4$-free characteristic function
> (1 if $G$ is $C_4$-free, not necessarily induced, and 0 otherwise).

```lean
theorem conjecture133 (G : SimpleGraph α) [DecidableRel G.Adj] (h : G.Connected) :
    let rad := G.radius.toNat
    let hasC4 := ∃ a b c d : α, a ≠ b ∧ a ≠ c ∧ a ≠ d ∧ b ≠ c ∧ b ≠ d ∧ c ≠ d ∧
      G.Adj a b ∧ G.Adj b c ∧ G.Adj c d ∧ G.Adj d a
    let cC4 : ℕ := if hasC4 then 0 else 1
    (rad : ℝ) + l G ^ cC4 ≤ (path G : ℝ)
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture133.lean, line 48](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture133.lean#L48).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture133.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture133.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
