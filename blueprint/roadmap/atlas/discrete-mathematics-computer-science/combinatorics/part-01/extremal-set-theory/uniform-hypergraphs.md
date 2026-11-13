---
declaration: section
origin: cited
lean: SetFamily.IsUniform, SetFamily.ContainsSubgraph, SetFamily.isUniform_iff, SetFamily.containsSubgraph_iff, SetFamily.IsIntersecting, SetFamily.isIntersecting_iff
statement: formalized
proof: formalized
---

# Uniform hypergraphs

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/uniform-hypergraphs/index.html).

## Uniform hypergraphs

Let $H$ be a finite family of finite subsets of a type $V$, viewed as
a hypergraph with edge set $H$, and let $r \in \mathbb{N}$. Then $H$ is $r$-uniform when every
edge $e \in H$ has exactly $r$ elements.

Formalized by `SetFamily.IsUniform`, a definition declared in [MathlibExt/Combinatorics/SetFamily/UniformHypergraph.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SetFamily/UniformHypergraph.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/uniform-hypergraphs/index.html#is-uniform).

## Subhypergraph containment

Let $H$ be a finite family of finite subsets of a type $V$,
viewed as a hypergraph with edge set $H$, and let $m, k \in \mathbb{N}$. Then $H$ contains a
subgraph with $m$ vertices and at least $k$ edges when there is a set $S$ of exactly $m$ elements
of $V$ such that at least $k$ edges of $H$ are subsets of $S$.

Formalized by `SetFamily.ContainsSubgraph`, a definition declared in [MathlibExt/Combinatorics/SetFamily/UniformHypergraph.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SetFamily/UniformHypergraph.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/uniform-hypergraphs/index.html#contains-subgraph).

## Characterization of uniform hypergraphs

Let $H$ be a finite family of finite subsets of
a type $V$ and let $r \in \mathbb{N}$. Then $H$ is $r$-uniform if and only if every member
$e \in H$ has exactly $r$ elements.

Formalized by `SetFamily.isUniform_iff`, a theorem declared in [MathlibExt/Combinatorics/SetFamily/UniformHypergraph.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SetFamily/UniformHypergraph.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/uniform-hypergraphs/index.html#is-uniform-iff).

## Characterization of subhypergraph containment

Let $H$ be a finite family of finite
subsets of a type $V$ and let $m, k \in \mathbb{N}$. Then $H$ contains a subgraph with $m$
vertices and at least $k$ edges if and only if there is a set $S$ of exactly $m$ elements of $V$
such that at least $k$ members of $H$ are subsets of $S$.

Formalized by `SetFamily.containsSubgraph_iff`, a theorem declared in [MathlibExt/Combinatorics/SetFamily/UniformHypergraph.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SetFamily/UniformHypergraph.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/uniform-hypergraphs/index.html#contains-subgraph-iff).

## Intersecting families

Let $F$ be a finite family of finite subsets of a type $\alpha$.
Then $F$ is intersecting when every two distinct members meet: for all $A, B \in F$ with
$A \neq B$, the intersection $A \cap B$ is nonempty.

The distinctness is load-bearing: the singleton family $\{\emptyset\}$ is intersecting.

Formalized by `SetFamily.IsIntersecting`, a definition declared in [MathlibExt/Combinatorics/SetFamily/UniformHypergraph.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SetFamily/UniformHypergraph.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/uniform-hypergraphs/index.html#is-intersecting).

## Characterization of intersecting families

Let $F$ be a finite family of finite subsets
of a type $\alpha$. Then $F$ is intersecting if and only if for all $A, B \in F$ with $A \neq B$,
the intersection $A \cap B$ is nonempty.

Formalized by `SetFamily.isIntersecting_iff`, a theorem declared in [MathlibExt/Combinatorics/SetFamily/UniformHypergraph.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SetFamily/UniformHypergraph.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/uniform-hypergraphs/index.html#is-intersecting-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Uniform hypergraphs](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/uniform-hypergraphs/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/extremal-set-theory/uniform-hypergraphs)
