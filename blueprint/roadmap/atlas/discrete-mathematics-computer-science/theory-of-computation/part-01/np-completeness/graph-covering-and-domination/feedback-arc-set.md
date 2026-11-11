---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.FeedbackArcSet.FeedbackArcSetInstance, MetaMathlibExt.Complexity.NPComplete.FeedbackArcSet.DAdj, MetaMathlibExt.Complexity.NPComplete.FeedbackArcSet.WellFormed, MetaMathlibExt.Complexity.NPComplete.FeedbackArcSet.FeedbackArcSetFeasible, MetaMathlibExt.Complexity.NPComplete.FeedbackArcSet.feedbackArcSetDec, MetaMathlibExt.Complexity.NPComplete.FeedbackArcSet.feedbackArcSet_npComplete
statement: formalized
---

# Feedback arc set

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/feedback-arc-set/index.html).

## Instances of FEEDBACK ARC SET

An instance of FEEDBACK ARC SET is a triple $(n, E, K)$
consisting of a natural number $n$ (the number of vertices), a finite list $E$ of ordered pairs
of natural numbers (the arcs) and a natural number $K$ (the bound).

Formalized by `MetaMathlibExt.Complexity.NPComplete.FeedbackArcSet.FeedbackArcSetInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/FeedbackArcSetWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/FeedbackArcSetWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/feedback-arc-set/index.html#feedback-arc-set-instance).

## Directed adjacency for FEEDBACK ARC SET

For a list $E$ of ordered pairs of natural numbers
and natural numbers $u$ and $v$, the directed adjacency test returns true when the pair $(u, v)$
occurs in $E$, that is, when $E$ contains an arc from $u$ to $v$, and false otherwise.

Formalized by `MetaMathlibExt.Complexity.NPComplete.FeedbackArcSet.DAdj`, a definition declared in [WantedExt/Complexity/NPComplete/FeedbackArcSetWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/FeedbackArcSetWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/feedback-arc-set/index.html#dadj).

## Well-formed FEEDBACK ARC SET instances

An instance $(n, E, K)$ of FEEDBACK ARC SET is
well formed when the list $E$ has no repeated entries and every pair $(u, v)$ in $E$ satisfies
$u < n$, $v < n$ and $u \ne v$; that is, $E$ lists distinct arcs, without loops, of a directed
graph on the vertices $0, \dots, n-1$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.FeedbackArcSet.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/FeedbackArcSetWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/FeedbackArcSetWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/feedback-arc-set/index.html#well-formed).

## Feasible FEEDBACK ARC SET instances

An instance $(n, E, K)$ of FEEDBACK ARC SET is
feasible when there is an ordering $v_0, v_1, \dots, v_{n-1}$ of the vertices $0, \dots, n-1$, in
which each of them occurs exactly once, such that at most $K$ entries $(u, v)$ of the list $E$,
counted with repetition, are backward, meaning that the position of $v$ in the ordering is
strictly smaller than the position of $u$. Here $v_j$ has position $j$, and a number that is not
among $0, \dots, n-1$ has position $n$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.FeedbackArcSet.FeedbackArcSetFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/FeedbackArcSetWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/FeedbackArcSetWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/feedback-arc-set/index.html#feedback-arc-set-feasible).

## FEEDBACK ARC SET as a decision problem

The decision problem FEEDBACK ARC SET accepts a
bitstring $x$ exactly when $x$ decodes, under the canonical bitstring encoding of instances, to
an instance $(n, E, K)$ of FEEDBACK ARC SET that is well formed and feasible. Bitstrings that do
not decode to an instance are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.FeedbackArcSet.feedbackArcSetDec`, a definition declared in [WantedExt/Complexity/NPComplete/FeedbackArcSetWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/FeedbackArcSetWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/feedback-arc-set/index.html#feedback-arc-set-dec).

## FEEDBACK ARC SET is NP-complete

The decision problem FEEDBACK ARC SET belongs to NP, and
every decision problem in NP reduces to FEEDBACK ARC SET by a polynomial-time many-one
reduction.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), FEEDBACK ARC SET; R. M. Karp, "Reducibility among combinatorial problems" (1972).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.FeedbackArcSet.feedbackArcSet_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/FeedbackArcSetWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/FeedbackArcSetWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/feedback-arc-set/index.html#feedback-arc-set-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Feedback arc set](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/feedback-arc-set/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/feedback-arc-set)
