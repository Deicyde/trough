---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.MaxFlowInP.maxFlowDec, MetaMathlibExt.Complexity.KeyTheorems.MaxFlowInP.max_flow_in_p
statement: formalized
---

# Maximum flow

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/maximum-flow/index.html).

## Max-flow decision problem

The decision problem that accepts a bitstring $x$ exactly when
$x$ decodes, under the canonical bitstring encoding, to a tuple $(n, E, s, t, K)$ of a natural
number $n$, a list $E = (e_0, \dots, e_{m-1})$ of triples $e_j = (u_j, v_j, c_j)$ of natural
numbers and natural numbers $s$, $t$ and $K$ such that $u_j < n$, $v_j < n$ and $u_j \neq v_j$
for every $j < m$, $s < n$, $t < n$ and $s \neq t$, and there are natural numbers
$f_0, \dots, f_{m-1}$ with $f_j \le c_j$ for every $j < m$, with
$\sum_{j : v_j = v} f_j = \sum_{j : u_j = v} f_j$ for every $v < n$ other than $s$ and $t$, and
with $\sum_{j : u_j = s} f_j - \sum_{j : v_j = s} f_j \ge K$, where the subtraction is
truncated at $0$. Bitstrings that do not decode are rejected.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.MaxFlowInP.maxFlowDec`, a definition declared in [WantedExt/Complexity/KeyTheorems/MaxFlowInPWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/MaxFlowInPWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/maximum-flow/index.html#max-flow-dec).

## Max flow is in P (Edmonds-Karp)

The max-flow decision problem belongs to the complexity
class P. This is the problem of deciding, for a vertex count $n$, a list of edges joining
distinct vertices below $n$ with natural-number capacities, distinct vertices $s, t < n$ and a
target $K$, encoded as a bitstring, whether some flow in natural numbers that respects the
capacities and is conserved at every vertex other than $s$ and $t$ has net outflow from $s$ at
least $K$.

## Sources

- J. Edmonds and R. M. Karp, "Theoretical improvements in algorithmic efficiency for network flow problems", Journal of the ACM 19 (1972), 248-264; L. R. Ford Jr. and D. R. Fulkerson, Flows in Networks, Princeton University Press, 1962.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.MaxFlowInP.max_flow_in_p` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/MaxFlowInPWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/MaxFlowInPWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/maximum-flow/index.html#max-flow-in-p).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Maximum flow](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/maximum-flow/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/polynomial-time-problems/maximum-flow)
