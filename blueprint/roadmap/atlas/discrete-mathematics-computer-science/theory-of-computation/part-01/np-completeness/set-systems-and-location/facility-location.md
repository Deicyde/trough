---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.FacilityLocation.FacilityLocationInstance, MetaMathlibExt.Complexity.NPComplete.FacilityLocation.WellFormed, MetaMathlibExt.Complexity.NPComplete.FacilityLocation.FacilityLocationFeasible, MetaMathlibExt.Complexity.NPComplete.FacilityLocation.facilityLocationDec, MetaMathlibExt.Complexity.NPComplete.FacilityLocation.facilityLocation_npComplete
statement: formalized
---

# Facility location

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/facility-location/index.html).

## Facility location instances

A facility location instance is a triple $(o, D, B)$ made of
a finite list $o$ of natural numbers (the opening costs of the facilities), a finite list $D$ of
finite lists of natural numbers (the $c$-th list holds the costs of assigning client $c$ to each
facility), and a natural number $B$ (the budget).

Formalized by `MetaMathlibExt.Complexity.NPComplete.FacilityLocation.FacilityLocationInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/FacilityLocationWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/FacilityLocationWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/facility-location/index.html#facility-location-instance).

## Well-formed facility location instances

A facility location instance $(o, D, B)$, with
opening costs $o$ and assignment-cost rows $D$, is well-formed when every row of $D$ has the same
length as $o$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.FacilityLocation.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/FacilityLocationWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/FacilityLocationWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/facility-location/index.html#well-formed).

## Feasible facility location instances

Let $(o, D, B)$ be a facility location instance
with opening costs $o = (o_0, \dots, o_{n-1})$, assignment-cost rows $D = (D_0, \dots, D_{m-1})$
and budget $B$, and write $D_{c,j}$ for the $j$-th entry of the row $D_c$, read as $0$ when $D_c$
has no $j$-th entry. The instance is feasible when there is a map $\sigma$ from the clients
$\{0, \dots, m-1\}$ to the facilities $\{0, \dots, n-1\}$ such that the opening costs of the
facilities in the image of $\sigma$ plus the assignment costs stay within the budget:
$\sum_{j \in \sigma(\{0, \dots, m-1\})} o_j + \sum_{c=0}^{m-1} D_{c,\sigma(c)} \le B$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.FacilityLocation.FacilityLocationFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/FacilityLocationWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/FacilityLocationWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/facility-location/index.html#facility-location-feasible).

## The FACILITY LOCATION decision problem

FACILITY LOCATION is the decision problem that
accepts a bitstring $x$ exactly when $x$ decodes, under the canonical bitstring encoding, to a
facility location instance that is well-formed and feasible; bitstrings that do not decode to an
instance are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.FacilityLocation.facilityLocationDec`, a definition declared in [WantedExt/Complexity/NPComplete/FacilityLocationWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/FacilityLocationWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/facility-location/index.html#facility-location-dec).

## FACILITY LOCATION is NP-complete

FACILITY LOCATION belongs to NP, and every decision
problem $L$ in NP reduces to FACILITY LOCATION by a polynomial-time many-one reduction: there is
a polynomial-time computable map $f$ on bitstrings such that, for every bitstring $x$, $L$
accepts $x$ exactly when FACILITY LOCATION accepts $f(x)$.

## Sources

- G. Cornuéjols, G. L. Nemhauser, and L. A. Wolsey, "The uncapacitated facility location problem", in P. B. Mirchandani and R. L. Francis, eds., Discrete Location Theory, Wiley, 1990, 119-171.

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.FacilityLocation.facilityLocation_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/FacilityLocationWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/FacilityLocationWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/facility-location/index.html#facility-location-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Facility location](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/facility-location/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/facility-location)
