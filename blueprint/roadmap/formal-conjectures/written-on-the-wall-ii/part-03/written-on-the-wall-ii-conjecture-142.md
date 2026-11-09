---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture142.conjecture142
statement: formalized
---

# Written on the Wall II - Conjecture 142

> *Reference:*
> [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture142.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture142.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `WrittenOnTheWallII.GraphConjecture142.conjecture142`

Solved: stated here; a Lean proof is at [https://github.com/AlperTheKing/formal-conjectures/blob/46bf39015f5c3c3ba3bfcf9f752b4b1e49b584ac/FormalConjecturesForMathlib/WrittenOnTheWallII/GraphConjecture142Proof.lean#L3927-L3932](https://github.com/AlperTheKing/formal-conjectures/blob/46bf39015f5c3c3ba3bfcf9f752b4b1e49b584ac/FormalConjecturesForMathlib/WrittenOnTheWallII/GraphConjecture142Proof.lean#L3927-L3932).

> WOWII [Conjecture 142](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/):
>
> For a simple connected graph $G$,
> $\mathrm{tree}(G) \ge (2/3) \cdot \mathrm{girth}(G) + \mathrm{ecc}(B)$
> where $\mathrm{tree}(G)$ is the largest induced tree size, $\mathrm{girth}(G)$
> is the length of the shortest cycle ($0$ if acyclic), $B$ is the set of
> boundary vertices (those of maximum eccentricity), and $\mathrm{ecc}(B)$ is
> the eccentricity of the set $B$.
>
> **Proof sketch.** The proof first strengthens the real-valued target to the
> integral bound
> $$
> \mathrm{ecc}(B) + \mathrm{girth}(G)
>   - \lfloor \mathrm{girth}(G) / 3 \rfloor \leq \mathrm{tree}(G).
> $$
> For a cyclic graph, start with a shortest cycle $K$. It is chordless, so
> removing one vertex leaves an induced path on $\mathrm{girth}(G)-1$ vertices.
> Shortest paths from selected vertices to $K$ are called *descents*. Pairwise
> noninteracting descents attach to the retained cycle path as disjoint branches.
> If two descents interact, the proof cuts at the first interaction encountered
> from the outer endpoint toward the cycle and splices the paths there.
> Minimality of that interaction makes the retained prefix disjoint and
> nonadjacent to the first descent; geodesicity excludes chords, while girth at
> least five rules out extra cross-edges and cycle attachments.
>
> Choose a vertex realizing $\mathrm{ecc}(B)$ and two endpoints of a diametral
> geodesic. Either two of their descents interact, directly giving a sufficiently
> long spliced tree, or all three are separate, in which case a three-point
> distance inequality forces their total length to be large enough. This proves
> the integral bound in the main range. Girths three and four, small
> $\mathrm{ecc}(B)$, and the two remaining congruence cases are handled by
> separate geodesic/cycle certificates with one or two descents; the acyclic case
> follows from a diametral path. Finally,
> $$
> \mathrm{girth}(G)-\lfloor\mathrm{girth}(G)/3\rfloor
>   = \lceil 2\,\mathrm{girth}(G)/3\rceil
>   \geq 2\,\mathrm{girth}(G)/3,
> $$
> which gives the stated real-valued inequality.
>
> The argument was developed with assistance from ChatGPT Pro. The linked Lean 4
> formalization was produced with assistance from OpenAI Codex and checked by
> Lean.

```lean
theorem conjecture142 (G : SimpleGraph α) [DecidableRel G.Adj] (h : G.Connected) :
    let B : Set α := (maxEccentricityVertices G : Set α)
    (2 : ℝ) / 3 * (G.girth : ℝ) + (eccSet G B : ℝ) ≤ (largestInducedTreeSize G : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture142.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture142.lean#L83).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture142.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture142.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
