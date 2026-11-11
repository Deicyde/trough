---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.FlowShop.FlowShopInstance, MetaMathlibExt.Complexity.NPComplete.FlowShop.WellFormed, MetaMathlibExt.Complexity.NPComplete.FlowShop.FlowShopFeasible, MetaMathlibExt.Complexity.NPComplete.FlowShop.flowShopDec, MetaMathlibExt.Complexity.NPComplete.FlowShop.flowShop_npComplete
statement: formalized
---

# Three-machine flow shop scheduling

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/three-machine-flow-shop-scheduling/index.html).

## Flow-shop instances

A flow-shop instance is a pair consisting of a finite list of jobs,
each a finite list of natural numbers (its processing times on machines 1, 2 and 3, in that
order), and a natural number $D$, the deadline. The type does not force a job to have exactly
three entries; that is part of well-formedness.

Formalized by `MetaMathlibExt.Complexity.NPComplete.FlowShop.FlowShopInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/FlowShopWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/FlowShopWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/three-machine-flow-shop-scheduling/index.html#flow-shop-instance).

## Well-formed flow-shop instances

A flow-shop instance is well formed when every job in
it is a list of exactly three natural numbers.

Formalized by `MetaMathlibExt.Complexity.NPComplete.FlowShop.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/FlowShopWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/FlowShopWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/three-machine-flow-shop-scheduling/index.html#well-formed).

## Feasible flow-shop schedules

Let an instance consist of jobs $1, \dots, n$, where job $j$
is a list of natural numbers whose $k$-th entry $p_{j,k}$ is its processing time on machine $k$
(read as $0$ if the list has fewer than $k$ entries), and a deadline $D$. The instance is
feasible when there are natural numbers $s_{j,k}$, for each job $j$ and each $k \in \{1, 2, 3\}$,
such that for every job $j$ we have $s_{j,1} + p_{j,1} \le s_{j,2}$,
$s_{j,2} + p_{j,2} \le s_{j,3}$ and $s_{j,3} + p_{j,3} \le D$, and for every machine
$k \in \{1, 2, 3\}$ and all jobs $a < b$ we have $s_{a,k} + p_{a,k} \le s_{b,k}$ or
$s_{b,k} + p_{b,k} \le s_{a,k}$.

Here $s_{j,k}$ is the start time of job $j$ on machine $k$: each job visits machines 1, 2, 3 in
that order, no machine processes two jobs at once, and every job finishes by $D$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.FlowShop.FlowShopFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/FlowShopWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/FlowShopWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/three-machine-flow-shop-scheduling/index.html#flow-shop-feasible).

## The 3-machine flow shop scheduling decision problem

The decision problem
3-MACHINE FLOW SHOP SCHEDULING accepts a bitstring $x$ exactly when $x$ decodes, under the
canonical bitstring encoding of flow-shop instances, to an instance that is well formed and
feasible. Bitstrings that do not decode to an instance are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.FlowShop.flowShopDec`, a definition declared in [WantedExt/Complexity/NPComplete/FlowShopWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/FlowShopWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/three-machine-flow-shop-scheduling/index.html#flow-shop-dec).

## 3-MACHINE FLOW SHOP SCHEDULING is NP-complete

The 3-machine flow shop scheduling
decision problem belongs to NP, and every decision problem in NP reduces to it by a
polynomial-time many-one reduction.

## Sources

- M. R. Garey, D. S. Johnson, and R. Sethi, "The complexity of flowshop and jobshop scheduling", Mathematics of Operations Research 1 (1976), 117-129; T. F. Gonzalez and S. Sahni, "Flowshop and jobshop schedules: complexity and approximation", Operations Research 26 (1978), 36-52.

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.FlowShop.flowShop_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/FlowShopWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/FlowShopWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/three-machine-flow-shop-scheduling/index.html#flow-shop-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Three-machine flow shop scheduling](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/three-machine-flow-shop-scheduling/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/scheduling/three-machine-flow-shop-scheduling)
