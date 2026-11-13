---
declaration: section
origin: cited
lean: SimpleGraph.Subgraph.IsRetract, SimpleGraph.HasCore, SimpleGraph.IsLocalInjection, SimpleGraph.IsLocalIsomorphism, SimpleGraph.Covers, SimpleGraph.IsFolding
statement: formalized
proof: formalized
---

# Graph homomorphisms, cores and covers

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/graph-homomorphisms-cores-and-covers/index.html).

## Retract

Let $Y$ be a subgraph of a graph $X$. A *retraction* from $X$ to $Y$ is a
homomorphism $f$ from $X$ to $Y$, regarded as a graph in its own right, whose restriction to the
vertex set of $Y$ is the identity map. We say that $Y$ is a *retract* of $X$ if there is a
retraction from $X$ to $Y$.

Formalized by `SimpleGraph.Subgraph.IsRetract`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/AlgebraicGraphTheory/Homomorphisms.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/AlgebraicGraphTheory/Homomorphisms.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/graph-homomorphisms-cores-and-covers/index.html#is-retract).

## Core of a graph

A finite graph $X$ is a *core* if every homomorphism from $X$ to itself
is a bijection. For finite graphs $X$ and $Y$, $Y$ is a *core of* $X$ if $Y$ is a core, there is a
homomorphism from $X$ to $Y$, and there is an injective homomorphism from $Y$ to $X$; that is, $Y$
is isomorphic to a subgraph of $X$.

Formalized by `SimpleGraph.HasCore`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/AlgebraicGraphTheory/Homomorphisms.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/AlgebraicGraphTheory/Homomorphisms.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/graph-homomorphisms-cores-and-covers/index.html#has-core).

## Local injection

A homomorphism $f$ from a finite graph $X$ to a finite graph $Y$ is a
*local injection* if any two distinct vertices of $X$ with the same image under $f$ are at
distance at least $3$ in $X$.

Vertices in different components of $X$ count as being at infinite distance.

Formalized by `SimpleGraph.IsLocalInjection`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/AlgebraicGraphTheory/Homomorphisms.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/AlgebraicGraphTheory/Homomorphisms.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/graph-homomorphisms-cores-and-covers/index.html#is-local-injection).

## Local isomorphism

A homomorphism $f$ from a finite graph $X$ to a finite graph $Y$ is a
*local isomorphism* if for every vertex $x$ of $X$, $f$ maps the set of neighbours of $x$
bijectively onto the set of neighbours of $f(x)$.

Formalized by `SimpleGraph.IsLocalIsomorphism`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/AlgebraicGraphTheory/Homomorphisms.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/AlgebraicGraphTheory/Homomorphisms.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/graph-homomorphisms-cores-and-covers/index.html#is-local-isomorphism).

## Graph cover

A finite graph $X$ *covers* a finite graph $Y$ if there is a surjective local
isomorphism from $X$ to $Y$.

Formalized by `SimpleGraph.Covers`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/AlgebraicGraphTheory/Homomorphisms.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/AlgebraicGraphTheory/Homomorphisms.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/graph-homomorphisms-cores-and-covers/index.html#covers).

## Folding of a graph homomorphism

A homomorphism from X to Y is a *simple folding* if it has one fibre consisting of two vertices
at distance two, and all other fibres are singletons. A homomorphism is a *folding* if it is the
composition of a non-negative number of simple foldings.

Formalized by `SimpleGraph.IsFolding`, an inductive type declared in [MathlibExt/Combinatorics/SimpleGraph/AlgebraicGraphTheory/Homomorphisms.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/AlgebraicGraphTheory/Homomorphisms.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/graph-homomorphisms-cores-and-covers/index.html#folding-of-a-graph-homomorphism).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Graph homomorphisms, cores and covers](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/graph-homomorphisms-cores-and-covers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/algebraic-graph-theory/part-01/graph-homomorphisms-cores-and-covers)
