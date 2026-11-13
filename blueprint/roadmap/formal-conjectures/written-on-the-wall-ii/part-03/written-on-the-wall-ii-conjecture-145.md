---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture145.conjecture145
statement: formalized
---

# Written on the Wall II - Conjecture 145

> The WOWII HTML uses $\lambda_{\min}(\overline{G})$ (the bar denotes graph complement).
> The formal statement below uses the local-independence minimum of $G^c$.
>
> *Reference:*
> [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
>
> ## Definitions
>
> The **local independence minimum** $\mathrm{lMin}(G)$ is:
>
> $$\mathrm{lMin}(G) = \min_{v \in V(G)} l(v)$$
>
> where $l(v) = \mathrm{indepNeighborsCard}(G, v)$ is the independence number of the
> neighbourhood of $v$. This is the minimum over all vertices of the local
> independence number.
>
> The **boundary vertices** $B(G)$ of a connected graph are the vertices $v$ such
> that the eccentricity of $v$ equals the diameter of $G$.
>
> The **eccentricity of a set** $\mathrm{ecc}(S) = \max_{u \notin S} \min_{w \in S}
> \mathrm{dist}(u, w)$. In the conjecture below, $\mathrm{ecc}(B)$ is the
> eccentricity of the boundary set.
>
> **Conjecture 145:** $\mathrm{tree}(G) \ge 2 \cdot \mathrm{ecc}(B) /
> \lambda_{\min}(\overline{G})$ where $\mathrm{tree}(G)$ is `largestInducedTreeSize G`,
> $\mathrm{ecc}(B)$ is the eccentricity of the boundary vertices, and
> $\lambda_{\min}(\overline{G})$ is the local independence minimum of the complement
> $\overline{G}$.

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture145.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture145.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `WrittenOnTheWallII.GraphConjecture145.conjecture145`

Solved: stated here; a Lean proof is at [https://github.com/DomTheDeveloper/crl/blob/2ee448baa80c98f0c8b9a0c1c3d9421200f99aa5/math/wowii145/WOW145/145.lean](https://github.com/DomTheDeveloper/crl/blob/2ee448baa80c98f0c8b9a0c1c3d9421200f99aa5/math/wowii145/WOW145/145.lean).

> WOWII [Conjecture 145](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
>
> For a simple connected graph $G$,
> $\mathrm{tree}(G) \ge 2 \cdot \mathrm{ecc}(B) / \lambda_{\min}(\overline{G})$
> where $\mathrm{tree}(G)$ is the number of vertices in a largest induced subtree,
> $\mathrm{ecc}(B)$ is the eccentricity of the boundary vertices (`eccSet` and
> `boundaryVertices`), and $\lambda_{\min}(\overline{G})$ is the minimum local
> independence number of the complement graph.
>
> We state the inequality in the form
> $\mathrm{tree}(G) \cdot \mathrm{lMin}(\overline{G}) \ge 2 \cdot \mathrm{ecc}(B)$
> to avoid division.
>
> ## Provenance
>
> Solved by Dominic Dabish.
>
> ProofOrchestrator, using OpenAI GPT-5.6 Thinking, assisted with the mathematical
> argument and Lean formalization; all formal claims were checked by the pinned
> Lean compiler.

```lean
theorem conjecture145 (G : SimpleGraph α) [DecidableRel G.Adj] (h : G.Connected)
    (hlMin : 0 < localIndependenceMin Gᶜ) :
    2 * eccSet G (maxEccentricityVertices G : Set α) ≤
    largestInducedTreeSize G * localIndependenceMin Gᶜ
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture145.lean, line 89](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture145.lean#L89).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture145.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture145.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
