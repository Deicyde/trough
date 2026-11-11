---
declaration: section
origin: cited
lean: SetFamily.IsIndependent, SetFamily.isIndependent_iff, SetFamily.isIndependent_empty_hypergraph, SetFamily.isIndependent_of_subset, SetFamily.isIndependent_empty_iff, SetFamily.IsSteinerTripleSystem, SetFamily.uniform_of_isSteinerTripleSystem, SetFamily.pairCover_of_isSteinerTripleSystem
statement: formalized
proof: formalized
---

# Independent sets in hypergraphs

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/independent-sets-in-hypergraphs/index.html).

## Independent set in a hypergraph

Let $H$ be a finite hypergraph, that is a finite
family of finite sets of vertices, called its edges. A finite set $I$ of vertices is
independent in $H$ when no edge $e$ of $H$ satisfies $e \subseteq I$.

Formalized by `SetFamily.IsIndependent`, a definition declared in [MathlibExt/Combinatorics/SetFamily/IndependentSet.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SetFamily/IndependentSet.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/independent-sets-in-hypergraphs/index.html#is-independent).

## Independence unfolded

A finite set $I$ of vertices is independent in a finite
hypergraph $H$ if and only if no edge $e$ of $H$ satisfies $e \subseteq I$.

Formalized by `SetFamily.isIndependent_iff`, a theorem declared in [MathlibExt/Combinatorics/SetFamily/IndependentSet.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SetFamily/IndependentSet.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/independent-sets-in-hypergraphs/index.html#is-independent-iff).

## Every set is independent in the empty hypergraph

Every finite set of vertices is
independent in the empty hypergraph, the hypergraph with no edges.

Formalized by `SetFamily.isIndependent_empty_hypergraph`, a theorem declared in [MathlibExt/Combinatorics/SetFamily/IndependentSet.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SetFamily/IndependentSet.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/independent-sets-in-hypergraphs/index.html#is-independent-empty-hypergraph).

## Subsets of independent sets are independent

If a finite set $I$ of vertices is
independent in a finite hypergraph $H$ and $J \subseteq I$, then $J$ is independent in $H$.

Formalized by `SetFamily.isIndependent_of_subset`, a theorem declared in [MathlibExt/Combinatorics/SetFamily/IndependentSet.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SetFamily/IndependentSet.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/independent-sets-in-hypergraphs/index.html#is-independent-of-subset).

## When the empty set is independent

For a finite hypergraph $H$, the empty set is
independent in $H$ if and only if every edge of $H$ is nonempty.

Formalized by `SetFamily.isIndependent_empty_iff`, a theorem declared in [MathlibExt/Combinatorics/SetFamily/IndependentSet.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SetFamily/IndependentSet.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/independent-sets-in-hypergraphs/index.html#is-independent-empty-iff).

## Steiner triple system

A finite hypergraph $H$ on a vertex type $V$, that is a finite
family of finite subsets of $V$, is a Steiner triple system when it is $3$-uniform (every
edge of $H$ has exactly $3$ elements) and any two distinct vertices $u \ne v$ of $V$ lie
together in exactly one edge of $H$.

Formalized by `SetFamily.IsSteinerTripleSystem`, a definition declared in [MathlibExt/Combinatorics/SetFamily/IndependentSet.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SetFamily/IndependentSet.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/independent-sets-in-hypergraphs/index.html#is-steiner-triple-system).

## Steiner triple systems are 3-uniform

If $H$ is a Steiner triple system, then $H$ is
$3$-uniform: every edge of $H$ has exactly $3$ elements.

Formalized by `SetFamily.uniform_of_isSteinerTripleSystem`, a theorem declared in [MathlibExt/Combinatorics/SetFamily/IndependentSet.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SetFamily/IndependentSet.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/independent-sets-in-hypergraphs/index.html#uniform-of-is-steiner-triple-system).

## Pairs in a Steiner triple system

If $H$ is a Steiner triple system on a vertex type
$V$, then for all vertices $u \ne v$ of $V$ there is exactly one edge $e$ of $H$ with
$u \in e$ and $v \in e$.

Formalized by `SetFamily.pairCover_of_isSteinerTripleSystem`, a theorem declared in [MathlibExt/Combinatorics/SetFamily/IndependentSet.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SetFamily/IndependentSet.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/independent-sets-in-hypergraphs/index.html#pair-cover-of-is-steiner-triple-system).

## Unique element of a singleton family

Let $t$ be a finite set of vertices and let
$P$ be a property of finite sets of vertices. If $t$ satisfies $P$, then there is exactly
one finite set $e$ of vertices with $e \in \{t\}$ and $P(e)$.

Formalized by `SetFamily.existsUnique_mem_singleton`, a theorem declared in [MathlibExt/Combinatorics/SetFamily/IndependentSet.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SetFamily/IndependentSet.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/independent-sets-in-hypergraphs/index.html#exists-unique-mem-singleton).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Independent sets in hypergraphs](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/independent-sets-in-hypergraphs/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/independent-sets-in-hypergraphs)
