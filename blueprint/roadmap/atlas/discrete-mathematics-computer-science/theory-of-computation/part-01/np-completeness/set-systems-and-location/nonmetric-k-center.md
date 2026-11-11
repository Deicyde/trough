---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.KCenter.KCenterInstance, MetaMathlibExt.Complexity.NPComplete.KCenter.WellFormed, MetaMathlibExt.Complexity.NPComplete.KCenter.KCenterFeasible, MetaMathlibExt.Complexity.NPComplete.KCenter.kCenterDec, MetaMathlibExt.Complexity.NPComplete.KCenter.kCenter_npComplete
statement: formalized
---

# Nonmetric k-center

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/nonmetric-k-center/index.html).

## k-center instances

An instance of generalized nonmetric k-center is a triple $(D, K, B)$
of a finite list $D$ of rows, each a finite list of natural numbers (row $c$ lists the costs from
client $c$ to the locations), and natural numbers $K$, the bound on the number of locations, and
$B$, the radius.

Formalized by `MetaMathlibExt.Complexity.NPComplete.KCenter.KCenterInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/KCenterWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/KCenterWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/nonmetric-k-center/index.html#kcenter-instance).

## Well-formed k-center instances

A k-center instance $(D, K, B)$ is well formed when all
rows of $D$ have the same length.

Formalized by `MetaMathlibExt.Complexity.NPComplete.KCenter.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/KCenterWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/KCenterWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/nonmetric-k-center/index.html#well-formed).

## Feasible k-center instances

Let $(D, K, B)$ be a k-center instance with rows
$D_0, \dots, D_{m-1}$, and let $n$ be the length of $D_0$, with $n = 0$ if $m = 0$. For $c < m$
and a natural number $f$, write $D_c(f)$ for the entry of $D_c$ at position $f$, counting from
$0$, and set $D_c(f) = 0$ if $D_c$ has at most $f$ entries. The instance is feasible when there
is a set $S$ of at most $K$ locations $f < n$ such that every client $c < m$ has some $f \in S$
with $D_c(f) \le B$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.KCenter.KCenterFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/KCenterWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/KCenterWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/nonmetric-k-center/index.html#kcenter-feasible).

## Generalized nonmetric k-center as a decision problem

This decision problem accepts a
bitstring $x$ exactly when $x$ decodes, under the canonical bitstring encoding, to a k-center
instance that is well formed and feasible; bitstrings that do not decode to an instance are
rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.KCenter.kCenterDec`, a definition declared in [WantedExt/Complexity/NPComplete/KCenterWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/KCenterWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/nonmetric-k-center/index.html#k-center-dec).

## k-CENTER (GENERALIZED, NONMETRIC) is NP-complete

The decision problem of generalized
nonmetric k-center on bitstrings is NP-complete: it belongs to NP, and every decision problem in
NP has a polynomial-time many-one reduction to it.

## Sources

- O. Kariv and S. L. Hakimi, "An algorithmic approach to network location problems. I: The p-centers", SIAM Journal on Applied Mathematics 37 (1979), 513-538.

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.KCenter.kCenter_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/KCenterWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/KCenterWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/nonmetric-k-center/index.html#k-center-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Nonmetric k-center](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/nonmetric-k-center/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/nonmetric-k-center)
