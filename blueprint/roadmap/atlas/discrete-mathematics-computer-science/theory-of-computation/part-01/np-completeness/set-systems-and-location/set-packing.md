---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.SetPacking.SetPackingInstance, MetaMathlibExt.Complexity.NPComplete.SetPacking.WellFormed, MetaMathlibExt.Complexity.NPComplete.SetPacking.SetPackingFeasible, MetaMathlibExt.Complexity.NPComplete.SetPacking.setPackingDec, MetaMathlibExt.Complexity.NPComplete.SetPacking.setPacking_npComplete
statement: formalized
---

# Set packing

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/set-packing/index.html).

## Set-packing instances

A set-packing instance is a triple $(n, C, K)$ consisting of a
natural number $n$, the size of the universe, a finite list $C$ of finite lists of natural numbers,
the subsets, and a natural number $K$, the bound.

Formalized by `MetaMathlibExt.Complexity.NPComplete.SetPacking.SetPackingInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/SetPackingWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/SetPackingWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/set-packing/index.html#set-packing-instance).

## Well-formed set-packing instances

A set-packing instance $(n, C, K)$ is well formed when
every list $s$ in $C$ has no repeated entries and every entry of $s$ is less than $n$, that is,
each member of $C$ lists the elements of a subset of $\{0, \dots, n - 1\}$ without repetition.

Formalized by `MetaMathlibExt.Complexity.NPComplete.SetPacking.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/SetPackingWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/SetPackingWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/set-packing/index.html#well-formed).

## Feasible set-packing instances

A set-packing instance $(n, C, K)$ is feasible when there
is a sublist $D$ of $C$ (a list obtained from $C$ by deleting entries while keeping their order)
with no repeated entries and at least $K$ entries such that any two distinct entries of $D$ have
no element in common.

In particular two copies of the same list, even of the empty list, cannot both be chosen.

Formalized by `MetaMathlibExt.Complexity.NPComplete.SetPacking.SetPackingFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/SetPackingWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/SetPackingWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/set-packing/index.html#set-packing-feasible).

## The SET PACKING decision problem

SET PACKING is the decision problem that accepts a
bitstring $x$ exactly when $x$ decodes, under the canonical bitstring encoding, to a set-packing
instance $(n, C, K)$ that is both well formed and feasible: every list in $C$ has no repeated
entries and only entries less than $n$, and some sublist of $C$ with no repeated entries and at
least $K$ entries has no element in common between any two of its distinct entries. Bitstrings
that do not decode to a set-packing instance are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.SetPacking.setPackingDec`, a definition declared in [WantedExt/Complexity/NPComplete/SetPackingWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/SetPackingWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/set-packing/index.html#set-packing-dec).

## SET PACKING is NP-complete

The SET PACKING decision problem lies in NP, and every
decision problem $L$ in NP has a polynomial-time many-one reduction to SET PACKING.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), SET PACKING; R. M. Karp, "Reducibility among combinatorial problems" (1972).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.SetPacking.setPacking_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/SetPackingWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/SetPackingWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/set-packing/index.html#set-packing-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Set packing](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/set-packing/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/set-packing)
