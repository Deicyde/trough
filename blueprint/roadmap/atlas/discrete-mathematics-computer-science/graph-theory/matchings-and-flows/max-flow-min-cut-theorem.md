---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.Graph.MaxFlowMinCutWanted.IsFeasibleFlow, MathlibExt.Combinatorics.Graph.MaxFlowMinCutWanted.flowValue, MathlibExt.Combinatorics.Graph.MaxFlowMinCutWanted.IsSTCut, MathlibExt.Combinatorics.Graph.MaxFlowMinCutWanted.cutCapacity, MathlibExt.Combinatorics.Graph.MaxFlowMinCutWanted.cutFlow_eq, MathlibExt.Combinatorics.Graph.MaxFlowMinCutWanted.flowValue_le_cutCapacity, MathlibExt.Combinatorics.Graph.MaxFlowMinCutWanted.max_flow_min_cut
statement: formalized
proof: formalized
---

# Max-flow min-cut theorem

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/max-flow-min-cut-theorem/index.html).

## Feasible flow

Let $V$ be a finite set, $c : V \times V \to \mathbb{R}$ a capacity
function and $s, t \in V$. A function $f : V \times V \to \mathbb{R}$ is a feasible $s$-$t$ flow
for $c$ if $0 \le f(u, v) \le c(u, v)$ for all $u, v \in V$ and $f$ is conserved at every vertex
$v \ne s, t$, that is, $\sum_{u \in V} f(u, v) = \sum_{w \in V} f(v, w)$.

Formalized by `MathlibExt.Combinatorics.Graph.MaxFlowMinCutWanted.IsFeasibleFlow`, a definition declared in [MathlibExt/Combinatorics/Graph/MaxFlowMinCut.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Graph/MaxFlowMinCut.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/max-flow-min-cut-theorem/index.html#is-feasible-flow).

## Flow value

For a finite set $V$, a vertex $s \in V$ and a function
$f : V \times V \to \mathbb{R}$, the value of $f$ is its net outflow from the source $s$,
$\sum_{v \in V} f(s, v) - \sum_{u \in V} f(u, s)$.

Formalized by `MathlibExt.Combinatorics.Graph.MaxFlowMinCutWanted.flowValue`, a definition declared in [MathlibExt/Combinatorics/Graph/MaxFlowMinCut.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Graph/MaxFlowMinCut.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/max-flow-min-cut-theorem/index.html#flow-value).

## Source–sink cut

For a finite set $V$ and vertices $s, t \in V$, an $s$-$t$ cut is a
subset $S \subseteq V$ with $s \in S$ and $t \notin S$.

Formalized by `MathlibExt.Combinatorics.Graph.MaxFlowMinCutWanted.IsSTCut`, a definition declared in [MathlibExt/Combinatorics/Graph/MaxFlowMinCut.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Graph/MaxFlowMinCut.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/max-flow-min-cut-theorem/index.html#is-stcut).

## Cut capacity

Let $V$ be a finite set and $c : V \times V \to \mathbb{R}$ a capacity
function. The capacity of a subset $S \subseteq V$ is the total capacity of the arcs leaving $S$,
$\sum_{u \in S} \sum_{v \in V \setminus S} c(u, v)$.

Formalized by `MathlibExt.Combinatorics.Graph.MaxFlowMinCutWanted.cutCapacity`, a definition declared in [MathlibExt/Combinatorics/Graph/MaxFlowMinCut.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Graph/MaxFlowMinCut.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/max-flow-min-cut-theorem/index.html#cut-capacity).

## Flow across a cut

Let $V$ be a finite set, $s, t \in V$, and
$f : V \times V \to \mathbb{R}$ a function conserved at every vertex $v \ne s, t$, that is,
$\sum_{u \in V} f(u, v) = \sum_{w \in V} f(v, w)$; no sign or capacity condition is imposed. Then
for every subset $S \subseteq V$ with $s \in S$ and $t \notin S$, the flow value
$\sum_{v \in V} f(s, v) - \sum_{u \in V} f(u, s)$ of $f$ equals
$\sum_{u \in S} \sum_{v \in V \setminus S} f(u, v) -
\sum_{u \in S} \sum_{v \in V \setminus S} f(v, u)$, the flow leaving $S$ minus the flow
entering $S$.

Formalized by `MathlibExt.Combinatorics.Graph.MaxFlowMinCutWanted.cutFlow_eq`, a theorem declared in [MathlibExt/Combinatorics/Graph/MaxFlowMinCut.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Graph/MaxFlowMinCut.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/max-flow-min-cut-theorem/index.html#cut-flow-eq).

## Weak duality for flows and cuts

Let $V$ be a finite set, $c : V \times V \to \mathbb{R}$
a capacity function and $s, t \in V$. If $f$ is a feasible $s$-$t$ flow for $c$ and $S$ is an
$s$-$t$ cut, then the flow value of $f$ is at most the capacity of $S$ for $c$.

Formalized by `MathlibExt.Combinatorics.Graph.MaxFlowMinCutWanted.flowValue_le_cutCapacity`, a theorem declared in [MathlibExt/Combinatorics/Graph/MaxFlowMinCut.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Graph/MaxFlowMinCut.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/max-flow-min-cut-theorem/index.html#flow-value-le-cut-capacity).

## Max-flow min-cut theorem

Let $V$ be a finite set, $c : V \times V \to \mathbb{R}$ a capacity
function with $c(u, v) \ge 0$ for all $u, v \in V$, and $s, t \in V$ with $s \ne t$. Then there is
a feasible $s$-$t$ flow $f$ for $c$ whose value is at least the value of every feasible $s$-$t$
flow for $c$ and at most the capacity of every $s$-$t$ cut, and there is an $s$-$t$ cut whose
capacity equals the value of $f$. In other words, the maximum value of a feasible $s$-$t$ flow
equals the minimum capacity of an $s$-$t$ cut.

## Sources

- L. R. Ford and D. R. Fulkerson, Canad. J. Math. 8 (1956), 399-404, DOI 10.4153/CJM-1956-045-5.

Formalized by `MathlibExt.Combinatorics.Graph.MaxFlowMinCutWanted.max_flow_min_cut`, a theorem declared in [MathlibExt/Combinatorics/Graph/MaxFlowMinCut.lean, line 631](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Graph/MaxFlowMinCut.lean#L631). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/max-flow-min-cut-theorem/index.html#max-flow-min-cut).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Max-flow min-cut theorem](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/max-flow-min-cut-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/matchings-and-flows/max-flow-min-cut-theorem)
