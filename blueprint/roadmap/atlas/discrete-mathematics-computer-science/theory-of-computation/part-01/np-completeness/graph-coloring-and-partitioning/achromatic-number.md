---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.AchromaticNumber.AchromaticNumberInstance, MetaMathlibExt.Complexity.NPComplete.AchromaticNumber.WellFormed, MetaMathlibExt.Complexity.NPComplete.AchromaticNumber.AchromaticNumberFeasible, MetaMathlibExt.Complexity.NPComplete.AchromaticNumber.achromaticNumberDec, MetaMathlibExt.Complexity.NPComplete.AchromaticNumber.achromaticNumber_npComplete
statement: formalized
---

# Achromatic number

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/achromatic-number/index.html).

## Instances of ACHROMATIC NUMBER

An instance of ACHROMATIC NUMBER is a triple $(n, E, K)$
of a natural number $n$ (the number of vertices), a finite list $E$ of ordered pairs of natural
numbers (the edges) and a natural number $K$ (the bound).

Formalized by `MetaMathlibExt.Complexity.NPComplete.AchromaticNumber.AchromaticNumberInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/AchromaticNumberWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/AchromaticNumberWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/achromatic-number/index.html#achromatic-number-instance).

## Well-formed ACHROMATIC NUMBER instances

An instance $(n, E, K)$ of ACHROMATIC NUMBER is
well-formed when the list $E$ has no repeated entries and every pair $(u, v)$ in $E$ satisfies
$u < n$, $v < n$, $u \ne v$ and $(v, u) \notin E$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.AchromaticNumber.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/AchromaticNumberWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/AchromaticNumberWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/achromatic-number/index.html#well-formed).

## Feasible ACHROMATIC NUMBER instances

An instance $(n, E, K)$ of ACHROMATIC NUMBER is
feasible when there are a natural number $q \ge K$ and a list $c = (c_0, \dots, c_{n-1})$ of $n$
natural numbers, with $c_u$ read as $0$ for $u \ge n$, such that $c_v < q$ for every $v < n$, every
$a < q$ equals $c_v$ for some $v < n$, $c_u \ne c_v$ for every pair $(u, v)$ in $E$, and for all
distinct $a, b < q$ some pair $(u, v)$ in $E$ has $(c_u, c_v) = (a, b)$ or
$(c_u, c_v) = (b, a)$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.AchromaticNumber.AchromaticNumberFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/AchromaticNumberWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/AchromaticNumberWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/achromatic-number/index.html#achromatic-number-feasible).

## ACHROMATIC NUMBER as a decision problem

The ACHROMATIC NUMBER decision problem accepts a
bitstring $x$ exactly when $x$ decodes, under the canonical bitstring encoding of instances
$(n, E, K)$, to an instance of ACHROMATIC NUMBER that is well-formed and feasible; it rejects
every bitstring that does not decode to an instance.

Formalized by `MetaMathlibExt.Complexity.NPComplete.AchromaticNumber.achromaticNumberDec`, a definition declared in [WantedExt/Complexity/NPComplete/AchromaticNumberWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/AchromaticNumberWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/achromatic-number/index.html#achromatic-number-dec).

## ACHROMATIC NUMBER is NP-complete

The ACHROMATIC NUMBER decision problem belongs to NP, and
every decision problem in NP has a polynomial-time many-one reduction to it.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), ACHROMATIC NUMBER; M. Farber et al., "The achromatic number of graphs" (1986).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.AchromaticNumber.achromaticNumber_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/AchromaticNumberWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/AchromaticNumberWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/achromatic-number/index.html#achromatic-number-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Achromatic number](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/achromatic-number/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/achromatic-number)
