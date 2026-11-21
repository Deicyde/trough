---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture19.conjecture19
statement: formalized
---

# Written on the Wall II - Conjecture 19

> *Reference:*
> [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture19.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/WrittenOnTheWallII/GraphConjecture19.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `WrittenOnTheWallII.GraphConjecture19.conjecture19`

Solved: stated here; a Lean proof is at [https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-16-000014](https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-16-000014).

> WOWII [Conjecture 19](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
>
> If $G$ is connected then the size $b(G)$ of a largest induced bipartite subgraph
> satisfies
> $b(G) \ge \left\lfloor \frac{\sum_v \mathrm{ecc}(v)}{|V|} + \sup_v l(v) \right\rfloor$,
> where $\mathrm{ecc}(v)$ denotes eccentricity and $l(v)$ is the independence number of the
> neighbourhood of $v$.
>
> **Proof outline.** Pick $u$ maximising $l(u)$, let $e = \mathrm{ecc}(u)$ and
> $D = \mathrm{diam}(G)$, and let $I \subseteq N(u)$ be an independent set with $|I| = l(u)$.
> Any family of sets $B_d$, each independent and contained in the distance sphere
> $\{v \mid \mathrm{dist}(u, v) = d\}$, induces a bipartite subgraph (colour by the parity of
> $\mathrm{dist}(u, \cdot)$), so $b(G) \ge \sum_d |B_d|$.
> * If $D \le e$, every eccentricity is at most $e$, so the average is at most $e$. Take
>   $B_0 = \{u\}$, $B_1 = I$, and one vertex of a geodesic from $u$ to an eccentric vertex on
>   each sphere $2 \le d \le e$; this gives $b(G) \ge e + l(u)$.
> * If $e < D$, the average eccentricity is strictly less than $D$. Take a diametral pair
>   $x, y$. On each sphere $d$ in a suitable range, the vertices of geodesics $u \to x$ and
>   $u \to y$ at distance $d$ from $u$ are at distance at least $2$ from each other (triangle
>   inequality with $\mathrm{dist}(x, y) = D$), so they can share $B_d$; counting gives
>   $b(G) \ge D - 1 + l(u)$.
> In both cases the floor of the average plus $l(u)$ is at most $b(G)$.

```lean
theorem conjecture19 (G : SimpleGraph α) [Nontrivial α] (h_conn : G.Connected) :
    ⌊(∑ v ∈ Finset.univ, ((G.eccent v).toNat : ℝ)) / (Fintype.card α : ℝ) +
      sSup (Set.range (indepNeighbors G))⌋ ≤ b G
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture19.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/WrittenOnTheWallII/GraphConjecture19.lean#L64).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture19.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/WrittenOnTheWallII/GraphConjecture19.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
