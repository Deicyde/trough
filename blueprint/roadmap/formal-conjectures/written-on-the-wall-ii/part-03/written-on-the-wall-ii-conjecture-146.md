---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture146.conjecture146
statement: formalized
---

# Written on the Wall II - Conjecture 146

> *Reference:*
> [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
>
> ## Definitions
>
> The **square** of a graph $G$, denoted $G^2$, is the graph on the same vertex set
> where two distinct vertices are adjacent if and only if their distance in $G$ is at
> most $2$.
>
> The **radius of $G^2$** is the minimum eccentricity of any vertex in $G^2$, i.e.,
>
> $$\mathrm{rad}(G^2) = \min_{v \in V} \max_{u \in V} \mathrm{dist}_{G^2}(u, v).$$

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture146.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture146.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `WrittenOnTheWallII.GraphConjecture146.conjecture146`

Solved: stated here; a Lean proof is at [https://github.com/akakabrian/WOW-146/blob/f9e0ad75d829170804ce1d8f9fd4c1d4a0085203/WOW146/Conjecture146.lean](https://github.com/akakabrian/WOW-146/blob/f9e0ad75d829170804ce1d8f9fd4c1d4a0085203/WOW146/Conjecture146.lean).

> WOWII [Conjecture 146](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
>
> For a simple connected graph $G$,
> $\mathrm{tree}(G) \ge 2 \cdot \mathrm{ecc}(B) / \mathrm{rad}(G^2)$
> where $\mathrm{tree}(G)$ is the number of vertices in a largest induced subtree,
> $\mathrm{ecc}(B)$ is the eccentricity of the boundary vertices of $G$ (`eccSet`
> and `maxEccentricityVertices`), and $\mathrm{rad}(G^2)$ is the radius of the square
> graph of $G$.
>
> We state the inequality in the form
> $\mathrm{tree}(G) \cdot \mathrm{rad}(G^2) \ge 2 \cdot \mathrm{ecc}(B)$ to avoid division.
>
> ## Informal proof
>
> Write $t$ for the largest induced-tree order, $r$ and $d$ for the radius and
> diameter of $G$, and $p$ for the eccentricity of its peripheral set.  First,
> the distance in the graph square is
> $\operatorname{dist}_{G^2}(u,v)=\lceil\operatorname{dist}_G(u,v)/2\rceil$,
> so $\operatorname{rad}(G^2)=\lceil r/2\rceil$.  A diametral geodesic is an
> induced path, giving $t\ge d+1$, while $p\le d-1$.  These bounds settle every
> case except $r=2$, $d=4$, and $p=3$.  In that remaining configuration, choose
> a centre and shortest paths to two diametral vertices and to a vertex at
> distance three from the peripheral set.  A finite case analysis on the two
> possible cross-arm edges (and then the possible chords) always produces an
> induced tree on at least six vertices.  Hence $t\,\operatorname{rad}(G^2)
> \ge 2p$ in the exceptional case as well.

```lean
theorem conjecture146 (G : SimpleGraph α) [DecidableRel G.Adj] (h : G.Connected)
    (hrad : 0 < graphSquareRadius G) :
    2 * eccSet G (maxEccentricityVertices G : Set α) ≤
    largestInducedTreeSize G * graphSquareRadius G
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture146.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture146.lean#L79).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture146.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture146.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
