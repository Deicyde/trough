---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.CVRP.CVRPInstance, MetaMathlibExt.Complexity.NPComplete.CVRP.RouteLength, MetaMathlibExt.Complexity.NPComplete.CVRP.WellFormed, MetaMathlibExt.Complexity.NPComplete.CVRP.CVRPFeasible, MetaMathlibExt.Complexity.NPComplete.CVRP.cvrpDec, MetaMathlibExt.Complexity.NPComplete.CVRP.cvrp_npComplete
statement: formalized
---

# Capacitated vehicle routing

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/capacitated-vehicle-routing/index.html).

## Capacitated vehicle routing instances

A capacitated vehicle routing instance is a tuple
$(n, d, D, m, C, K)$ consisting of a natural number $n$ (the number of customers), a list $d$ of
natural numbers (the demands), a list $D$ of lists of natural numbers (the distance matrix, whose
rows and columns include the depot), and natural numbers $m$ (the number of vehicles), $C$ (the
capacity) and $K$ (the bound on the total length).

Formalized by `MetaMathlibExt.Complexity.NPComplete.CVRP.CVRPInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/CVRPWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/CVRPWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/capacitated-vehicle-routing/index.html#cvrpinstance).

## Length of a route

Let $D$ be a list of lists of natural numbers, read as a distance
matrix whose entry $D_{u,v}$ is the entry at position $v$ of the row at position $u$ (positions
counted from $0$), or $0$ if there is no such entry, and let $o$ be a natural number, the depot.
The length of the empty route is $0$, and the length of a route given by a list
$(r_1, \dots, r_k)$ of natural numbers with $k \ge 1$ is
$D_{o,r_1} + \sum_{j=1}^{k-1} D_{r_j,r_{j+1}} + D_{r_k,o}$, where the sum is $0$ when $k = 1$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.CVRP.RouteLength`, a definition declared in [WantedExt/Complexity/NPComplete/CVRPWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/CVRPWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/capacitated-vehicle-routing/index.html#route-length).

## Well-formed capacitated vehicle routing instances

A capacitated vehicle routing instance
$(n, d, D, m, C, K)$ is well formed when the demand list $d$ has length $n$, the distance matrix
$D$ has $n + 1$ rows, and every row of $D$ has length $n + 1$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.CVRP.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/CVRPWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/CVRPWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/capacitated-vehicle-routing/index.html#well-formed).

## Feasibility of a capacitated vehicle routing instance

Let $(n, d, D, m, C, K)$ be a
capacitated vehicle routing instance, with customers $0, \dots, n - 1$ and depot $n$, and let the
demand $d_c$ of $c$ be the entry of the list $d$ at position $c$ (counting from $0$), or $0$ if
$d$ has no such entry. The instance is feasible when there is a list of at most $m$ routes, each
a list of natural numbers, such that every route has no repeated entries and only entries less
than $n$; every customer $c < n$ lies on some route, and all routes of the list that contain $c$
are equal; the demands of the entries of each route sum to at most $C$; and the lengths of the
routes, for the distance matrix $D$ and depot $n$, sum to at most $K$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.CVRP.CVRPFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/CVRPWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/CVRPWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/capacitated-vehicle-routing/index.html#cvrpfeasible).

## Capacitated vehicle routing as a decision problem

The decision problem CAPACITATED
VEHICLE ROUTING accepts a bitstring $x$ exactly when $x$ decodes, under the canonical bitstring
encoding, to a capacitated vehicle routing instance that is well formed and feasible; it rejects
every bitstring that does not decode.

Formalized by `MetaMathlibExt.Complexity.NPComplete.CVRP.cvrpDec`, a definition declared in [WantedExt/Complexity/NPComplete/CVRPWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/CVRPWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/capacitated-vehicle-routing/index.html#cvrp-dec).

## CAPACITATED VEHICLE ROUTING is NP-complete

The decision problem CAPACITATED VEHICLE
ROUTING lies in NP, and every decision problem in NP has a polynomial-time many-one reduction to
it.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), VEHICLE ROUTING (capacitated); G. B. Dantzig and J. H. Ramser, "The truck dispatching problem" (1959).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.CVRP.cvrp_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/CVRPWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/CVRPWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/capacitated-vehicle-routing/index.html#cvrp-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Capacitated vehicle routing](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/capacitated-vehicle-routing/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/capacitated-vehicle-routing)
