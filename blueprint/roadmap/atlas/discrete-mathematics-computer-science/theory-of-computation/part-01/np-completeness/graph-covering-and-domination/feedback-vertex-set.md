---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.FeedbackVertexSet.FeedbackVertexSetInstance, MetaMathlibExt.Complexity.NPComplete.FeedbackVertexSet.Graph, MetaMathlibExt.Complexity.NPComplete.FeedbackVertexSet.WellFormed, MetaMathlibExt.Complexity.NPComplete.FeedbackVertexSet.FeedbackVertexSetFeasible, MetaMathlibExt.Complexity.NPComplete.FeedbackVertexSet.feedbackVertexSetDec, MetaMathlibExt.Complexity.NPComplete.FeedbackVertexSet.feedbackVertexSet_npComplete
statement: formalized
---

# Feedback vertex set

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/feedback-vertex-set/index.html).

## Instances of FEEDBACK VERTEX SET

An instance of FEEDBACK VERTEX SET is a triple
$(n, es, K)$ of a natural number $n$ (the number of vertices), a list $es$ of pairs of natural
numbers (the edges) and a natural number $K$ (the bound).

Formalized by `MetaMathlibExt.Complexity.NPComplete.FeedbackVertexSet.FeedbackVertexSetInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/FeedbackVertexSetWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/FeedbackVertexSetWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/feedback-vertex-set/index.html#feedback-vertex-set-instance).

## Graph of a FEEDBACK VERTEX SET instance

For an instance $(n, es, K)$ of FEEDBACK VERTEX
SET, its graph is the simple graph on $\{0, \dots, n-1\}$ in which distinct vertices $i$ and
$j$ are adjacent when $(i, j)$ or $(j, i)$ belongs to $es$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.FeedbackVertexSet.Graph`, a definition declared in [WantedExt/Complexity/NPComplete/FeedbackVertexSetWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/FeedbackVertexSetWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/feedback-vertex-set/index.html#graph).

## Well-formed FEEDBACK VERTEX SET instances

An instance $(n, es, K)$ of FEEDBACK VERTEX
SET is well formed when the list $es$ has no repeated entries and every pair $(u, v)$ in $es$
satisfies $u < n$, $v < n$ and $u \ne v$, and $(v, u)$ does not belong to $es$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.FeedbackVertexSet.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/FeedbackVertexSetWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/FeedbackVertexSetWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/feedback-vertex-set/index.html#well-formed).

## Feedback vertex sets within the bound

An instance $(n, es, K)$ of FEEDBACK VERTEX SET is
feasible when there is a set $S$ of at most $K$ vertices of its graph such that the subgraph of
its graph induced on the vertices outside $S$ is acyclic.

Formalized by `MetaMathlibExt.Complexity.NPComplete.FeedbackVertexSet.FeedbackVertexSetFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/FeedbackVertexSetWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/FeedbackVertexSetWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/feedback-vertex-set/index.html#feedback-vertex-set-feasible).

## FEEDBACK VERTEX SET as a decision problem

The decision problem FEEDBACK VERTEX SET
accepts a bitstring $x$ exactly when $x$ decodes, under the canonical bitstring encoding of
instances, to an instance of FEEDBACK VERTEX SET that is well formed and feasible. Bitstrings
that do not decode to an instance are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.FeedbackVertexSet.feedbackVertexSetDec`, a definition declared in [WantedExt/Complexity/NPComplete/FeedbackVertexSetWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/FeedbackVertexSetWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/feedback-vertex-set/index.html#feedback-vertex-set-dec).

## FEEDBACK VERTEX SET is NP-complete

The decision problem FEEDBACK VERTEX SET belongs to
NP, and every decision problem in NP reduces to FEEDBACK VERTEX SET by a polynomial-time
many-one reduction.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), FEEDBACK VERTEX SET.

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.FeedbackVertexSet.feedbackVertexSet_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/FeedbackVertexSetWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/FeedbackVertexSetWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/feedback-vertex-set/index.html#feedback-vertex-set-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Feedback vertex set](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/feedback-vertex-set/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/feedback-vertex-set)
