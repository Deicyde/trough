---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture200.conjecture200
statement: formalized
---

# Written on the Wall II - Conjecture 200

> *Reference:*
> [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
>
> ## Counterexample
>
> For every integer $q \geq 5$, let $C = \{a,b\} \cup D$ have $q$ vertices and
> induce $K_q$ minus the edge $ab$. Add two nonadjacent vertices $x,y$, each
> complete to $C$; a vertex $z$ adjacent exactly to $a,b$; and, for every
> $d \in D$, a pendant vertex $p_d$ adjacent exactly to $d$.
>
> The local-neighbourhood independence numbers are $2$ at $x,y,z$, $1$ at each
> $p_d$, and $3$ at every vertex of $C$. Their sum is $4q+4$, while the graph has
> $2q+1$ vertices, so
>
> $$\left\lceil 1 + l_{\mathrm{avg}}(G)\right\rceil = 4.$$
>
> The vertices $\{a,x,y,z\}$ induce a claw, and a case split on the number of
> vertices from $C$ shows that no induced tree has more than four vertices.
> Thus $\operatorname{tree}(G)=4$. Finally, the graph has $q-2 \geq 3$ pendant
> vertices, but a Hamiltonian path has only two endpoints.
>
> The smallest member of this family has 11 vertices and graph6 encoding
> `J??FFBRq}N_`.
> This is a smallest counterexample overall: an exhaustive search over all
> 11,989,760 connected graphs on 4 ≤ n ≤ 10 vertices (via nauty's `geng`;
> graphs on at most 3 vertices are trivially traceable) found no graph
> satisfying the premise without a Hamiltonian path.

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture200.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture200.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `WrittenOnTheWallII.GraphConjecture200.conjecture200`

Solved: stated here; a Lean proof is at [https://github.com/infinityscroll/formal-conjectures/blob/9dd290db402c49922fa42793e4a7cfb802daf5c1/FormalConjectures/WrittenOnTheWallII/GraphConjecture200Counterexample.lean#L24-L195](https://github.com/infinityscroll/formal-conjectures/blob/9dd290db402c49922fa42793e4a7cfb802daf5c1/FormalConjectures/WrittenOnTheWallII/GraphConjecture200Counterexample.lean#L24-L195).

> WOWII [Conjecture 200](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
>
> For a simple connected graph `G`, if `tree(G) = ⌈1 + l_avg(G)⌉`, then `G` has a Hamiltonian path.
> Here `tree(G)` is the number of vertices of a largest induced tree subgraph, and
> `l_avg(G) = averageIndepNeighbors G` is the average over all vertices of the independence number
> of the neighbourhood.
> A Hamiltonian path is a walk visiting every vertex exactly once.
>
> This conjecture is false. The counterexample family in the module docstring
> satisfies the equality hypothesis and has no Hamiltonian path.

```lean
theorem conjecture200 :
    ¬ ∀ (α : Type) [Fintype α] [DecidableEq α] [Nontrivial α]
      (G : SimpleGraph α) (_h : G.Connected),
      (largestInducedTreeSize G : ℝ) = ⌈1 + averageIndepNeighbors G⌉ →
      ∃ a b : α, ∃ p : G.Walk a b, p.IsHamiltonian
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture200.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture200.lean#L71).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture200.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture200.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
