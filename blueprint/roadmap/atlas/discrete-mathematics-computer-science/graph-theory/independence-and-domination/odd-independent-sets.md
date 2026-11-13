---
declaration: section
origin: cited
lean: SimpleGraph.IsOddIndependent, SimpleGraph.IsOddIndependent.isIndepSet, SimpleGraph.IsOddIndependent.finite_inter, SimpleGraph.IsOddIndependent.empty_or_odd, SimpleGraph.isOddIndependent_empty, SimpleGraph.isOddIndependent_singleton
statement: formalized
proof: formalized
---

# Odd independent sets

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/odd-independent-sets/index.html).

## Odd independent set

A set $S$ of vertices of a simple graph $G$ is odd independent if
$S$ is an independent set of $G$ and, for every vertex $v \notin S$, the set of neighbours of $v$
that lie in $S$ is finite and is either empty or has an odd number of elements.

Formalized by `SimpleGraph.IsOddIndependent`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/OddIndependent.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/OddIndependent.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/odd-independent-sets/index.html#is-odd-independent).

## Odd independent sets are independent

If $S$ is an odd independent set of a simple graph
$G$, then $S$ is an independent set of $G$: no two distinct vertices of $S$ are adjacent.

Formalized by `SimpleGraph.IsOddIndependent.isIndepSet`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/OddIndependent.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/OddIndependent.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/odd-independent-sets/index.html#is-indep-set).

## Outside vertices have finitely many neighbours in an odd independent set

Let $S$ be an
odd independent set of a simple graph $G$ and let $v$ be a vertex with $v \notin S$. Then only
finitely many neighbours of $v$ lie in $S$.

Formalized by `SimpleGraph.IsOddIndependent.finite_inter`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/OddIndependent.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/OddIndependent.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/odd-independent-sets/index.html#finite-inter).

## Outside vertices see an empty or odd part of an odd independent set

Let $S$ be an odd
independent set of a simple graph $G$ and let $v$ be a vertex with $v \notin S$. Then the set of
neighbours of $v$ that lie in $S$ is either empty or has an odd number of elements.

Formalized by `SimpleGraph.IsOddIndependent.empty_or_odd`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/OddIndependent.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/OddIndependent.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/odd-independent-sets/index.html#empty-or-odd).

## The empty set is odd independent

The empty set is odd independent in any simple graph.

Formalized by `SimpleGraph.isOddIndependent_empty`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/OddIndependent.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/OddIndependent.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/odd-independent-sets/index.html#is-odd-independent-empty).

## Singletons are odd independent

For every vertex $a$ of a simple graph $G$, the singleton
$\{a\}$ is odd independent in $G$.

Formalized by `SimpleGraph.isOddIndependent_singleton`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/OddIndependent.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/OddIndependent.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/odd-independent-sets/index.html#is-odd-independent-singleton).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Odd independent sets](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/odd-independent-sets/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/independence-and-domination/odd-independent-sets)
