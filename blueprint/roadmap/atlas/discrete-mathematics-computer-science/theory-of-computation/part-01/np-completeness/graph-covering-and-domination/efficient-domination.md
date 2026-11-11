---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.EfficientDomination.EfficientDominationInstance, MetaMathlibExt.Complexity.NPComplete.EfficientDomination.Graph, MetaMathlibExt.Complexity.NPComplete.EfficientDomination.WellFormed, MetaMathlibExt.Complexity.NPComplete.EfficientDomination.EfficientDominationFeasible, MetaMathlibExt.Complexity.NPComplete.EfficientDomination.efficientDominationDec, MetaMathlibExt.Complexity.NPComplete.EfficientDomination.efficientDomination_npComplete
statement: formalized
---

# Efficient domination

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/efficient-domination/index.html).

## Efficient Domination instances

An instance of EFFICIENT DOMINATION is a pair $(n, E)$
of a natural number $n$, the number of vertices, and a list $E$ of pairs of natural numbers, the
edges.

Formalized by `MetaMathlibExt.Complexity.NPComplete.EfficientDomination.EfficientDominationInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/EfficientDominationWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/EfficientDominationWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/efficient-domination/index.html#efficient-domination-instance).

## Graph of an Efficient Domination instance

For an instance $(n, E)$, its graph is the
simple graph on the vertex set $\{0, \dots, n - 1\}$ in which distinct vertices $u$ and $v$ are
adjacent when $(u, v)$ or $(v, u)$ belongs to $E$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.EfficientDomination.Graph`, a definition declared in [WantedExt/Complexity/NPComplete/EfficientDominationWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/EfficientDominationWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/efficient-domination/index.html#graph).

## Well-formed Efficient Domination instances

An instance $(n, E)$ is well formed when the
list $E$ has no repeated entries and every pair $(a, b)$ in $E$ satisfies $a < n$, $b < n$ and
$a \ne b$, and $(b, a)$ does not belong to $E$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.EfficientDomination.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/EfficientDominationWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/EfficientDominationWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/efficient-domination/index.html#well-formed).

## Instances with an efficient dominating set

An instance $(n, E)$ of EFFICIENT DOMINATION
is feasible when its graph has an efficient dominating set (a perfect code): a set $S$ of
vertices such that every vertex $v$ has exactly one vertex $u \in S$ with $u = v$ or $u$
adjacent to $v$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.EfficientDomination.EfficientDominationFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/EfficientDominationWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/EfficientDominationWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/efficient-domination/index.html#efficient-domination-feasible).

## EFFICIENT DOMINATION (PERFECT CODE) as a decision problem

The decision problem
EFFICIENT DOMINATION accepts a bitstring $x$ exactly when $x$ decodes, under the canonical
bitstring encoding of instances, to an instance $(n, E)$ that is well formed and whose graph has
an efficient dominating set. Bitstrings that do not decode to an instance are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.EfficientDomination.efficientDominationDec`, a definition declared in [WantedExt/Complexity/NPComplete/EfficientDominationWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/EfficientDominationWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/efficient-domination/index.html#efficient-domination-dec).

## EFFICIENT DOMINATION (PERFECT CODE) is NP-complete

The decision problem EFFICIENT
DOMINATION belongs to NP, and every decision problem in NP reduces to it by a polynomial-time
many-one reduction.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), EFFICIENT DOMINATION; D. G. Corneil and Y. Perl, "Clustering and domination in perfect graphs" (1984) and the perfect-code literature.

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.EfficientDomination.efficientDomination_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/EfficientDominationWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/EfficientDominationWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/efficient-domination/index.html#efficient-domination-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Efficient domination](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/efficient-domination/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/efficient-domination)
