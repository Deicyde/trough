---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.PrecoloringExtension.PrecoloringExtensionInstance, MetaMathlibExt.Complexity.NPComplete.PrecoloringExtension.WellFormed, MetaMathlibExt.Complexity.NPComplete.PrecoloringExtension.PrecoloringExtensionFeasible, MetaMathlibExt.Complexity.NPComplete.PrecoloringExtension.precoloringExtensionDec, MetaMathlibExt.Complexity.NPComplete.PrecoloringExtension.precoloringExtension_npComplete
statement: formalized
---

# Precoloring extension

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/precoloring-extension/index.html).

## Instances of PRECOLORING EXTENSION

An instance of precoloring extension is a tuple
$(n, E, c, K)$ consisting of a natural number $n$ (the number of vertices), a list $E$ of pairs
of natural numbers (the edges), a list $c$ of natural numbers (the partial coloring, where an
entry $0$ means uncolored and an entry $k + 1$ means color $k$), and a natural number $K$ (the
number of colors).

Formalized by `MetaMathlibExt.Complexity.NPComplete.PrecoloringExtension.PrecoloringExtensionInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/PrecoloringExtensionWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/PrecoloringExtensionWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/precoloring-extension/index.html#precoloring-extension-instance).

## Well-formed precoloring extension instances

An instance $(n, E, c, K)$ of precoloring
extension is well formed when the edge list $E$ has no repeated entries, every edge $(u, v)$ in
$E$ satisfies $u < n$, $v < n$, $u \ne v$ and $(v, u) \notin E$, and the partial coloring $c$
has length $n$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.PrecoloringExtension.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/PrecoloringExtensionWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/PrecoloringExtensionWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/precoloring-extension/index.html#well-formed).

## Feasible precoloring extension instances

An instance $(n, E, c, K)$ of precoloring
extension is feasible when there is a list $\chi = (\chi_0, \dots, \chi_{n-1})$ of $n$ natural
numbers such that $\chi_v < K$ for every vertex $v < n$, $\chi_v = c_v - 1$ for every vertex
$v < n$ with $c_v \ne 0$, and $\chi_u \ne \chi_v$ for every edge $(u, v)$ in $E$. Here $c_v$ is
the entry of $c$ at position $v$, and an entry of a list at a position beyond its length is read
as $0$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.PrecoloringExtension.PrecoloringExtensionFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/PrecoloringExtensionWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/PrecoloringExtensionWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/precoloring-extension/index.html#precoloring-extension-feasible).

## PRECOLORING EXTENSION as a decision problem

The decision problem PRECOLORING EXTENSION
accepts a bitstring $x$ exactly when $x$ decodes, under the canonical bitstring encoding, to a
precoloring extension instance that is well formed and feasible; bitstrings that do not decode
are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.PrecoloringExtension.precoloringExtensionDec`, a definition declared in [WantedExt/Complexity/NPComplete/PrecoloringExtensionWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/PrecoloringExtensionWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/precoloring-extension/index.html#precoloring-extension-dec).

## PRECOLORING EXTENSION is NP-complete

The decision problem PRECOLORING EXTENSION lies in
NP, and every decision problem in NP reduces to it by a polynomial-time many-one reduction.

## Sources

- M. Biro, M. Hujter, and Z. Tuza, "Precoloring extension. I. Interval graphs", Discrete Mathematics 100 (1992), 267-279 (NP- completeness on interval graphs, hence on general graphs); hardness also follows directly from Garey-Johnson CHROMATIC NUMBER (GT4) by taking the precoloring to be empty.

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.PrecoloringExtension.precoloringExtension_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/PrecoloringExtensionWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/PrecoloringExtensionWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/precoloring-extension/index.html#precoloring-extension-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Precoloring extension](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/precoloring-extension/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/precoloring-extension)
