---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture144.conjecture144
statement: formalized
---

# Written on the Wall II - Conjecture 144

> *Reference:*
> [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture144.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture144.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `WrittenOnTheWallII.GraphConjecture144.conjecture144`

Solved: stated here; a Lean proof is at [https://github.com/beowulf127/wowii144-lean/blob/046429d509b28c90ee2ec38ae27c1ad377c6a5fc/WOWII144/Main.lean](https://github.com/beowulf127/wowii144-lean/blob/046429d509b28c90ee2ec38ae27c1ad377c6a5fc/WOWII144/Main.lean).

> WOWII [Conjecture 144](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
>
> For a simple connected graph $G$,
> $\mathrm{tree}(G) \ge \mathrm{girth}(G) - 1 + \mathrm{ecc}(\mathrm{Centers})$
> where $\mathrm{tree}(G)$ is the largest induced tree size, $\mathrm{girth}(G)$ is
> the length of the shortest cycle ($0$ if acyclic),
> $\mathrm{Centers} = G.\mathrm{center}$ is the set of vertices with minimum
> eccentricity (the center of $G$), and $\mathrm{ecc}(\mathrm{Centers})$ is the
> eccentricity of the center set — the maximum distance from any non-center
> vertex to the nearest center vertex.
>
> **Proof sketch.** Let $g = \mathrm{girth}(G)$ and
> $e = \mathrm{ecc}(G, \mathrm{center}(G))$. The acyclic and $e = 0$ cases are
> immediate. If $g \le e + 2$, the formalized Bacsó--Tuza induced-path argument,
> with an elementary $e = 1$ case, produces an induced tree on at least $2e + 1$
> vertices. Since $g - 1 + e \le 2e + 1$, this proves the result.
>
> Suppose instead that $e + 3 \le g$, and fix a shortest cycle $C$. Removing one
> vertex of $C$ leaves an induced tree on $g - 1$ vertices. Analyze the connected
> components outside $C$. If one has at least $e$ vertices, it supplies an
> attached rooted induced tree of order $e$. Otherwise, let $D$ be the sum of the
> components' attachment depths. If $D \ge e$, select pairwise edge-separated
> rooted branches of total order $e$ and attach them to $C$, deleting a suitable
> cycle vertex. If $D < e$, shortest-cycle contact restrictions bound
> corresponding exclusion arcs. Their complement consists of central cycle
> vertices and $D$-dominates the graph, forcing $e \le D$, a contradiction.
>
> Finite graph search was used only during discovery to test candidate
> structural lemmas and reject false proof templates; no finite-search result is
> used in the universal proof.

```lean
theorem conjecture144 (G : SimpleGraph α) (h : G.Connected) :
    (G.girth : ℝ) - 1 + (ecc G G.center : ℝ) ≤ (largestInducedTreeSize G : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture144.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture144.lean#L71).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture144.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture144.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
