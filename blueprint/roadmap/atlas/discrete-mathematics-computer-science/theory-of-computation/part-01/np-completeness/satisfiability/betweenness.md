---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.Betweenness.BetweennessInstance, MetaMathlibExt.Complexity.NPComplete.Betweenness.WellFormed, MetaMathlibExt.Complexity.NPComplete.Betweenness.BetweennessFeasible, MetaMathlibExt.Complexity.NPComplete.Betweenness.betweennessDec, MetaMathlibExt.Complexity.NPComplete.Betweenness.betweenness_npComplete
statement: formalized
---

# Betweenness

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/betweenness/index.html).

## BETWEENNESS instances

An instance of BETWEENNESS is a pair $(n, T)$ of a natural number
$n$ (the number of elements) and a list $T$ of triples of natural numbers.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Betweenness.BetweennessInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/BetweennessWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/BetweennessWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/betweenness/index.html#betweenness-instance).

## Well-formed BETWEENNESS instances

A BETWEENNESS instance $(n, T)$ is well formed when
every triple $(a, b, c)$ in $T$ satisfies $a < n$, $b < n$ and $c < n$, and $a$, $b$, $c$ are
pairwise distinct.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Betweenness.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/BetweennessWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/BetweennessWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/betweenness/index.html#well-formed).

## BETWEENNESS feasibility

A BETWEENNESS instance $(n, T)$ is feasible when there is an
ordering of the numbers $0, \dots, n-1$ such that for every triple $(a, b, c)$ in $T$, either
$p(a) < p(b) < p(c)$ or $p(c) < p(b) < p(a)$, where $p(m)$ is the position of $m$ in the
ordering, counting from $0$, and $p(m) = n$ when $m$ is not among $0, \dots, n-1$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Betweenness.BetweennessFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/BetweennessWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/BetweennessWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/betweenness/index.html#betweenness-feasible).

## The BETWEENNESS decision problem

BETWEENNESS accepts a bitstring $x$ exactly when $x$
decodes, under the canonical bitstring encoding of pairs $(n, T)$ of a natural number and a list
of triples of natural numbers, to a BETWEENNESS instance that is both well formed and feasible.
Bitstrings that do not decode to such a pair are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Betweenness.betweennessDec`, a definition declared in [WantedExt/Complexity/NPComplete/BetweennessWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/BetweennessWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/betweenness/index.html#betweenness-dec).

## BETWEENNESS is NP-complete

The BETWEENNESS decision problem belongs to NP, and every
decision problem in NP has a polynomial-time many-one reduction to it.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), BETWEENNESS; M. Opatrny, "Total ordering problem" (1979).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.Betweenness.betweenness_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/BetweennessWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/BetweennessWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/betweenness/index.html#betweenness-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Betweenness](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/betweenness/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/satisfiability/betweenness)
