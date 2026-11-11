---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.RCPSP.RCPSPInstance, MetaMathlibExt.Complexity.NPComplete.RCPSP.WellFormed, MetaMathlibExt.Complexity.NPComplete.RCPSP.RCPSPFeasible, MetaMathlibExt.Complexity.NPComplete.RCPSP.rcpspDec, MetaMathlibExt.Complexity.NPComplete.RCPSP.rcpsp_npComplete
statement: formalized
---

# Resource-constrained project scheduling

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/resource-constrained-project-scheduling/index.html).

## Instances of resource-constrained project scheduling

An instance of
resource-constrained project scheduling (an RCPSP instance) is a quadruple $(J, P, C, D)$: a list
$J$ of jobs, each a pair $(p, r) \in \mathbb{N} \times \mathbb{N}$ of a duration $p$ and a
resource demand $r$; a list $P$ of precedence pairs $(a, b) \in \mathbb{N} \times \mathbb{N}$ of
job indices; a resource capacity $C \in \mathbb{N}$; and a deadline $D \in \mathbb{N}$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.RCPSP.RCPSPInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/RCPSPWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/RCPSPWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/resource-constrained-project-scheduling/index.html#rcpspinstance).

## Well-formed RCPSP instances

An RCPSP instance $(J, P, C, D)$ whose job list $J$ has
$n$ jobs is well formed when every precedence pair $(a, b) \in P$ satisfies $a < n$, $b < n$ and
$a \ne b$, and there is a listing of $0, 1, \dots, n-1$, each exactly once, in which $a$ comes
before $b$ for every $(a, b) \in P$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.RCPSP.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/RCPSPWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/RCPSPWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/resource-constrained-project-scheduling/index.html#well-formed).

## Feasible RCPSP instances

Let $(J, P, C, D)$ be an RCPSP instance with $n$ jobs, where
job $j < n$ has duration $p_j$ and resource demand $r_j$, and set $p_j = 0$ for $j \ge n$. The
instance is feasible when there are start times $s_0, \dots, s_{n-1} \in \mathbb{N}$, with
$s_j = 0$ for $j \ge n$, such that every job finishes by the deadline ($s_j + p_j \le D$ for all
$j < n$), every precedence pair $(a, b) \in P$ satisfies $s_a + p_a \le s_b$, and at every time
$t < D$ the total demand of the jobs active at $t$ (the jobs $j < n$ with
$s_j \le t < s_j + p_j$) is at most $C$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.RCPSP.RCPSPFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/RCPSPWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/RCPSPWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/resource-constrained-project-scheduling/index.html#rcpspfeasible).

## Resource-constrained project scheduling as a decision problem

RESOURCE-CONSTRAINED
PROJECT SCHEDULING is the decision problem that accepts a bitstring $x$ exactly when $x$ decodes,
under the canonical bitstring encoding of RCPSP instances, to an RCPSP instance that is well
formed and feasible. Bitstrings that do not decode to an instance are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.RCPSP.rcpspDec`, a definition declared in [WantedExt/Complexity/NPComplete/RCPSPWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/RCPSPWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/resource-constrained-project-scheduling/index.html#rcpsp-dec).

## RESOURCE-CONSTRAINED PROJECT SCHEDULING is NP-complete

The decision problem
RESOURCE-CONSTRAINED PROJECT SCHEDULING belongs to NP, and every decision problem in NP has a
polynomial-time many-one reduction to it.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), BIN PACKING; J. Blazewicz, J. K. Lenstra, and A. H. G. Rinnooy Kan, "Scheduling subject to resource constraints: classification and complexity", Discrete Applied Mathematics 5 (1983), 11-24 (classification).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.RCPSP.rcpsp_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/RCPSPWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/RCPSPWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/resource-constrained-project-scheduling/index.html#rcpsp-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Resource-constrained project scheduling](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/resource-constrained-project-scheduling/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/scheduling/resource-constrained-project-scheduling)
