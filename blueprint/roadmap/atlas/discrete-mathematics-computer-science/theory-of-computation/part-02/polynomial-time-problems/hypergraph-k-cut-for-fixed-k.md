---
declaration: section
origin: cited
lean: MathlibExt.Complexity.HypergraphKCutFixedKAMR29Problem0056Wanted.hypergraphKCutDec, MathlibExt.Complexity.HypergraphKCutFixedKAMR29Problem0056Wanted.hypergraphKCutInP, MathlibExt.Complexity.HypergraphKCutFixedKAMR29Problem0056Wanted.hypergraphKCutInP_holds
statement: formalized
---

# Hypergraph k-cut for fixed k

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/hypergraph-k-cut-for-fixed-k/index.html).

## Decision version of hypergraph $k$-cut

For a natural number $k$, this is the decision
problem on bitstrings that decodes an input as a triple $(n, E, B)$: a number $n$ of vertices
$0, \dots, n-1$, a list $E$ of hyperedges, each a list of vertices with a natural-number cost, and
a natural-number budget $B$. It accepts the input iff every hyperedge lists only vertices below
$n$ and there is a partition of the vertices into $k$ non-empty parts, given by a map $f$ from
$\{0, \dots, n-1\}$ onto $\{0, \dots, k-1\}$, such that the total cost of the hyperedges in $E$
(counted with multiplicity) that meet two different parts is at most $B$. Inputs that do not
decode are rejected.

Formalized by `MathlibExt.Complexity.HypergraphKCutFixedKAMR29Problem0056Wanted.hypergraphKCutDec`, a definition declared in [WantedExt/Complexity/HypergraphKCutFixedKAMR29Problem0056Wanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/HypergraphKCutFixedKAMR29Problem0056Wanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/hypergraph-k-cut-for-fixed-k/index.html#hypergraph-kcut-dec).

## The EGRES question on hypergraph $k$-cut for fixed $k$

The statement that for every natural
number $k$, the decision version of hypergraph $k$-cut is in the complexity class P. That problem
accepts a hypergraph on the vertices $0, \dots, n-1$, given by hyperedges with natural-number
costs, and a budget $B$ iff every hyperedge lists only vertices below $n$ and some partition of the
vertices into $k$ non-empty parts has total cost of the hyperedges meeting two parts at most $B$;
inputs that do not decode are rejected.

Formalized by `MathlibExt.Complexity.HypergraphKCutFixedKAMR29Problem0056Wanted.hypergraphKCutInP`, a definition declared in [WantedExt/Complexity/HypergraphKCutFixedKAMR29Problem0056Wanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/HypergraphKCutFixedKAMR29Problem0056Wanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/hypergraph-k-cut-for-fixed-k/index.html#hypergraph-kcut-in-p).

## Hypergraph $k$-cut for fixed $k$ is in P

For every natural number $k$, the decision version
of hypergraph $k$-cut is in the complexity class P. That problem accepts a hypergraph on the
vertices $0, \dots, n-1$, given by hyperedges with natural-number costs, and a budget $B$ iff every
hyperedge lists only vertices below $n$ and some partition of the vertices into $k$ non-empty parts
has total cost of the hyperedges meeting two parts at most $B$; inputs that do not decode are
rejected.

Chandrasekaran and Chekuri give, for every fixed $k$, a deterministic polynomial-time algorithm for
hypergraph $k$-cut with non-negative hyperedge costs, which decides this problem.

## Sources

- EGRES Open (Egerváry Research Group), list of open problems, Minimum k-way cut in a hypergraph, https://oldlemon.cs.elte.hu/egres/open/Minimum_k-way_cut_in_a_hypergraph; resolution: K. Chandrasekaran and C. Chekuri, Hypergraph k-cut for fixed k in deterministic polynomial time, FOCS 2020; arXiv:2009.12442, abstract: for hypergraphs with non-negative hyperedge costs and fixed k, a deterministic polynomial-time algorithm for Hypergraph-k-cut (a least-cost F ⊆ E such that G - F has at least k components, equivalently a partition of V into k non-empty parts minimizing the cost of crossing hyperedges), https://arxiv.org/abs/2009.12442.

Stated but not proved: `MathlibExt.Complexity.HypergraphKCutFixedKAMR29Problem0056Wanted.hypergraphKCutInP_holds` is written with `theorem_wanted` in [WantedExt/Complexity/HypergraphKCutFixedKAMR29Problem0056Wanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/HypergraphKCutFixedKAMR29Problem0056Wanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/hypergraph-k-cut-for-fixed-k/index.html#hypergraph-kcut-in-p-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hypergraph k-cut for fixed k](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/hypergraph-k-cut-for-fixed-k/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/polynomial-time-problems/hypergraph-k-cut-for-fixed-k)
