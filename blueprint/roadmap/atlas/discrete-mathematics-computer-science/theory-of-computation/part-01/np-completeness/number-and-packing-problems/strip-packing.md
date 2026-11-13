---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.StripPacking.StripPackingInstance, MetaMathlibExt.Complexity.NPComplete.StripPacking.WellFormed, MetaMathlibExt.Complexity.NPComplete.StripPacking.StripPackingFeasible, MetaMathlibExt.Complexity.NPComplete.StripPacking.stripPackingDec, MetaMathlibExt.Complexity.NPComplete.StripPacking.stripPacking_npComplete
statement: formalized
---

# Strip packing

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/strip-packing/index.html).

## Strip packing instances

A strip packing instance is a triple $(R, W, H)$ consisting of a
finite list $R = ((w_1, h_1), \dots, (w_n, h_n))$ of pairs of natural numbers, the widths and
heights of the rectangles, a natural number $W$, the width of the strip, and a natural number $H$,
the height bound.

Formalized by `MetaMathlibExt.Complexity.NPComplete.StripPacking.StripPackingInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/StripPackingWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/StripPackingWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/strip-packing/index.html#strip-packing-instance).

## Well-formed strip packing instances

A strip packing instance $(R, W, H)$ is well formed
when every rectangle $(w, h)$ in the list $R$ has $w > 0$ and $h > 0$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.StripPacking.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/StripPackingWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/StripPackingWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/strip-packing/index.html#well-formed).

## Feasible strip packings

A strip packing instance $(R, W, H)$ with
$R = ((w_1, h_1), \dots, (w_n, h_n))$ is feasible when there are natural numbers
$x_1, y_1, \dots, x_n, y_n$ such that $x_j + w_j \le W$ and $y_j + h_j \le H$ for every
$1 \le j \le n$, and for all $1 \le a < b \le n$ at least one of $x_a + w_a \le x_b$,
$x_b + w_b \le x_a$, $y_a + h_a \le y_b$ and $y_b + h_b \le y_a$ holds.

That is, the unrotated rectangles with lower-left corners $(x_j, y_j)$, widths $w_j$ and heights
$h_j$ lie in $[0, W] \times [0, H]$, and any two of them are separated by a vertical or a
horizontal line. When all widths and heights are positive, the latter says that no two of the
rectangles overlap in their interiors.

Formalized by `MetaMathlibExt.Complexity.NPComplete.StripPacking.StripPackingFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/StripPackingWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/StripPackingWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/strip-packing/index.html#strip-packing-feasible).

## The STRIP PACKING decision problem

STRIP PACKING is the decision problem that accepts a
bitstring $x$ exactly when $x$ decodes, under the canonical bitstring encoding of strip packing
instances, to a strip packing instance that is well formed and feasible. Bitstrings that do not
decode to a strip packing instance are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.StripPacking.stripPackingDec`, a definition declared in [WantedExt/Complexity/NPComplete/StripPackingWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/StripPackingWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/strip-packing/index.html#strip-packing-dec).

## STRIP PACKING is NP-complete

The STRIP PACKING decision problem belongs to NP, and every
decision problem $L$ in NP reduces to STRIP PACKING by a polynomial-time many-one reduction.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), STRIP PACKING (axis-aligned, no rotations).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.StripPacking.stripPacking_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/StripPackingWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/StripPackingWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/strip-packing/index.html#strip-packing-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Strip packing](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/strip-packing/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/strip-packing)
