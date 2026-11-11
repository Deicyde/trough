---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.EditStep, Cslib.Algorithms.Lean.EditScript, Cslib.Algorithms.Lean.EditStep.cost, Cslib.Algorithms.Lean.EditScript.cost, Cslib.Algorithms.Lean.EditScript.apply?, Cslib.Algorithms.Lean.EditScript.Transforms, Cslib.Algorithms.Lean.EditDistanceResult, Cslib.Algorithms.Lean.EditDistanceCost
statement: formalized
proof: formalized
---

# Edit distance

26 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/edit-distance/index.html).

## Edit step

An edit step over a type $\alpha$ is one of four operations, for
$a, b \in \alpha$: keep $a$ (consume the input value $a$ and reproduce it), delete $a$ (consume
$a$), insert $a$ (produce $a$ without consuming input), or substitute $a$ by $b$ (consume $a$
and produce $b$).

Formalized by `Cslib.Algorithms.Lean.EditStep`, an inductive type declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Script.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Script.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/edit-distance/index.html#edit-step).

## Edit script

An edit script over a type $\alpha$ is a finite list of edit steps over
$\alpha$, applied from left to right.

Formalized by `Cslib.Algorithms.Lean.EditScript`, an abbreviation declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Script.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Script.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/edit-distance/index.html#edit-script).

## Unit cost of an edit step

The cost of an edit step is $0$ for a keep step and $1$ for a
deletion, an insertion or a substitution.

Formalized by `Cslib.Algorithms.Lean.EditStep.cost`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Script.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Script.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/edit-distance/index.html#cost).

## Cost of an edit script

The cost of an edit script is the sum of the unit costs of its
steps; the empty script has cost $0$.

Formalized by `Cslib.Algorithms.Lean.EditScript.cost`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Script.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Script.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/edit-distance/index.html#cost-2).

## Running an edit script

Over a type $\alpha$ with a boolean equality test, running an
edit script on an input list processes the steps from left to right and either fails or
returns an output list. A keep step with value $a$ consumes the next input value $b$ and
outputs $a$; a deletion of $a$ consumes $b$ and outputs nothing; a substitution of $a$ by $c$
consumes $b$ and outputs $c$. Each of these three fails if the input is exhausted or if the
equality test of $a$ against $b$ fails. An insertion of $c$ outputs $c$ without consuming input.
When the script ends, the run succeeds with the outputs in order if the input is used up, and
fails if input values remain.

Formalized by `Cslib.Algorithms.Lean.EditScript.apply?`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Script.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Script.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/edit-distance/index.html#apply).

## An edit script transforming one list into another

Over a type with a boolean equality
test, an edit script transforms a list $x$ into a list $y$ when running the script on $x$
succeeds and outputs $y$.

Formalized by `Cslib.Algorithms.Lean.EditScript.Transforms`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Script.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Script.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/edit-distance/index.html#transforms).

## Edit-distance result record

An edit-distance result over a type $\alpha$ consists of a
natural number, the reported distance, and an edit script over $\alpha$.

The record imposes no relation between the two fields; it is meant to hold a minimum edit
distance and a script realizing it.

Formalized by `Cslib.Algorithms.Lean.EditDistanceResult`, a structure declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Script.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Script.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/edit-distance/index.html#edit-distance-result).

## Edit-distance cost counters

An edit-distance cost record is a pair of natural numbers:
the number of dynamic-programming table cells initialized or transitioned, and the number of
operations emitted while reconstructing an edit script.

Formalized by `Cslib.Algorithms.Lean.EditDistanceCost`, a structure declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Script.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Script.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/edit-distance/index.html#edit-distance-cost).

## Total edit-distance cost

The total of an edit-distance cost record is the number of table
cells initialized or transitioned plus the number of operations emitted during reconstruction.

Formalized by `Cslib.Algorithms.Lean.EditDistanceCost.total`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Script.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Script.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/edit-distance/index.html#total).

## Edit distance algorithm

Given lists $s = s_1 \cdots s_m$ and $t = t_1 \cdots t_n$ over a
type with a Boolean equality test, the algorithm fills a table $D(i, j)$ for $0 \le i \le m$ and
$0 \le j \le n$ by $D(0, j) = j$, $D(i, 0) = i$ and
$D(i, j) = \min(D(i-1, j-1) + c_{ij}, D(i-1, j) + 1, D(i, j-1) + 1)$ for $i, j \ge 1$,
where $c_{ij}$ is $0$ if the test reports $s_i = t_j$ and $1$ otherwise. It then walks back
from $(m, n)$ to $(0, 0)$: on the boundary it deletes the remaining $s_i$ or inserts the
remaining $t_j$; otherwise it takes a move attaining the minimum, preferring the diagonal move
(a keep of $s_i$ if the test reports $s_i = t_j$, else a substitution of $t_j$ for $s_i$),
then a deletion of $s_i$, then an insertion of $t_j$. It returns the distance $D(m, n)$
together with the edit script of the chosen moves in left-to-right order. Each of the
$(m + 1)(n + 1)$ table entries is charged as one cell transition and each emitted operation
as one reconstruction step.

Formalized by `Cslib.Algorithms.Lean.editDistance`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Algorithm.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Algorithm.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/edit-distance/index.html#edit-distance).

## Correctness of the returned edit script

For lists $s$ and $t$ over a type whose Boolean
equality test agrees with equality, the edit script returned by the edit distance algorithm on
$s$ and $t$ transforms $s$ into $t$.

Formalized by `Cslib.Algorithms.Lean.editDistance_script_applies`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Algorithm.lean, line 875](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Algorithm.lean#L875). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/edit-distance/index.html#edit-distance-script-applies).

## The returned edit script realizes the distance

For lists $s$ and $t$ over a type with a
Boolean equality test, the unit cost of the edit script returned by the edit distance algorithm
on $s$ and $t$ equals the distance it returns.

Formalized by `Cslib.Algorithms.Lean.editDistance_script_cost`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Algorithm.lean, line 880](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Algorithm.lean#L880). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/edit-distance/index.html#edit-distance-script-cost).

## Minimality of the computed edit distance

Let $s$ and $t$ be lists over a type whose
Boolean equality test agrees with equality. Every edit script that transforms $s$ into $t$ has
unit cost at least the distance returned by the edit distance algorithm on $s$ and $t$.

Formalized by `Cslib.Algorithms.Lean.editDistance_minimal`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Algorithm.lean, line 886](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Algorithm.lean#L886). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/edit-distance/index.html#edit-distance-minimal).

## Edit distance from the empty list

For every list $t$ over a type with a Boolean equality
test, the distance returned by the edit distance algorithm from the empty list to $t$ is the
length of $t$.

Formalized by `Cslib.Algorithms.Lean.editDistance_nil_left`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Algorithm.lean, line 897](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Algorithm.lean#L897). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/edit-distance/index.html#edit-distance-nil-left).

## Edit distance to the empty list

For every list $s$ over a type with a Boolean equality
test, the distance returned by the edit distance algorithm from $s$ to the empty list is the
length of $s$.

Formalized by `Cslib.Algorithms.Lean.editDistance_nil_right`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Algorithm.lean, line 903](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Algorithm.lean#L903). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/edit-distance/index.html#edit-distance-nil-right).

## Edit distance of a list to itself

For every list $s$ over a type whose Boolean equality
test agrees with equality, the distance returned by the edit distance algorithm from $s$ to $s$
is $0$.

Formalized by `Cslib.Algorithms.Lean.editDistance_self`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Algorithm.lean, line 910](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Algorithm.lean#L910). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/edit-distance/index.html#edit-distance-self).

## Edit distance vanishes only on equal lists

For lists $s$ and $t$ over a type whose
Boolean equality test agrees with equality, the distance returned by the dynamic-programming
edit distance algorithm on $s$ and $t$ is $0$ if and only if $s = t$.

Formalized by `Cslib.Algorithms.Lean.editDistance_eq_zero_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Algorithm.lean, line 916](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Algorithm.lean#L916). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/edit-distance/index.html#edit-distance-eq-zero-iff).

## Table cost of the edit distance algorithm

For lists $s$ and $t$ over a type with a
Boolean equality test, write $|s|$ and $|t|$ for their lengths. The number of table-cell
transitions charged by the dynamic-programming edit distance algorithm on $s$ and $t$ is exactly
$(|s| + 1)(|t| + 1)$, one per pair of a prefix of $s$ and a prefix of $t$.

Formalized by `Cslib.Algorithms.Lean.editDistance_cellTransitions`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Algorithm.lean, line 926](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Algorithm.lean#L926). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/edit-distance/index.html#edit-distance-cell-transitions).

## Reconstruction cost of the edit distance algorithm

For lists $s$ and $t$ over a type with
a Boolean equality test, the number of reconstruction steps charged by the edit distance
algorithm on $s$ and $t$ equals the length of the edit script it returns.

Formalized by `Cslib.Algorithms.Lean.editDistance_reconstructionSteps`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Algorithm.lean, line 932](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Algorithm.lean#L932). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/edit-distance/index.html#edit-distance-reconstruction-steps).

## Reconstruction cost bound for edit distance

For lists $s$ and $t$ over a type with a
Boolean equality test, write $|s|$ and $|t|$ for their lengths. The number of reconstruction
steps charged by the edit distance algorithm on $s$ and $t$ is at most $|s| + |t|$.

Formalized by `Cslib.Algorithms.Lean.editDistance_reconstructionSteps_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Algorithm.lean, line 938](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Algorithm.lean#L938). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/edit-distance/index.html#edit-distance-reconstruction-steps-le).

## Running time of the edit distance algorithm

For lists $s$ and $t$ over a type with a
Boolean equality test, the total number of events charged by the edit distance algorithm on $s$
and $t$, that is its cell transitions plus its reconstruction steps, equals
$(|s| + 1)(|t| + 1) + k$, where $k$ is the length of the edit script it returns.

Formalized by `Cslib.Algorithms.Lean.editDistance_time`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Algorithm.lean, line 944](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Algorithm.lean#L944). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/edit-distance/index.html#edit-distance-time).

## Every edit script has an inverse of the same cost

Every script has an inverse of the same cost (swap insertions and deletions, reverse
substitutions).

Formalized by `Cslib.Algorithms.Lean.EditScript.exists_inverse`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Metric.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Metric.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/edit-distance/index.html#exists-inverse).

## Composition of edit scripts is subadditive in cost

Two scripts compose into one whose cost is at most the sum of their costs.

Formalized by `Cslib.Algorithms.Lean.EditScript.exists_compose`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Metric.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Metric.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/edit-distance/index.html#exists-compose).

## Symmetry

**Symmetry** of unit-cost edit distance.

Formalized by `Cslib.Algorithms.Lean.editDistance_comm`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Metric.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Metric.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/edit-distance/index.html#edit-distance-comm).

## The triangle inequality

**The triangle inequality** for unit-cost edit distance.

Formalized by `Cslib.Algorithms.Lean.editDistance_triangle`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Metric.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Metric.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/edit-distance/index.html#edit-distance-triangle).

## Edit distance between distinct lists is positive

Distinct lists are at positive distance.

Formalized by `Cslib.Algorithms.Lean.editDistance_pos_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Metric.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/EditDistance/Metric.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/edit-distance/index.html#edit-distance-pos-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Edit distance](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/edit-distance/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/string-algorithms/edit-distance)
