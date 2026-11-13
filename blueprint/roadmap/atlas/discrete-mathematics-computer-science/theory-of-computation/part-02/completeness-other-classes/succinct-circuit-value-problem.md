---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.SuccinctCircuitValueEXPComplete.SCVGate, MetaMathlibExt.Complexity.KeyTheorems.SuccinctCircuitValueEXPComplete.scvCircuitEval, MetaMathlibExt.Complexity.KeyTheorems.SuccinctCircuitValueEXPComplete.scvCircuitOutputs, MetaMathlibExt.Complexity.KeyTheorems.SuccinctCircuitValueEXPComplete.scvBitsOf, MetaMathlibExt.Complexity.KeyTheorems.SuccinctCircuitValueEXPComplete.scvBitsToNum, MetaMathlibExt.Complexity.KeyTheorems.SuccinctCircuitValueEXPComplete.succDesc, MetaMathlibExt.Complexity.KeyTheorems.SuccinctCircuitValueEXPComplete.succGateInfo, MetaMathlibExt.Complexity.KeyTheorems.SuccinctCircuitValueEXPComplete.succGateVal
statement: formalized
---

# Succinct circuit value problem

13 results, 12 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/succinct-circuit-value-problem/index.html).

## Encoded gates (Succinct Circuit Value)

An encoded gate is a pair $(k, r)$ of a natural
number $k$, the kind of the gate, and a list $r$ of natural numbers, its references.

These pairs are the shared (kind, references) encoding of gates of flat Boolean circuits.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.SuccinctCircuitValueEXPComplete.SCVGate`, an abbreviation declared in [WantedExt/Complexity/KeyTheorems/SuccinctCircuitValueEXPCompleteWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/SuccinctCircuitValueEXPCompleteWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/succinct-circuit-value-problem/index.html#scvgate).

## Gate values of an encoded circuit (Succinct Circuit Value)

Let $C$ be a list of encoded
gates, $a$ a list of booleans and $n \in \mathbb{N}$. Decode each gate of $C$ into a gate of a
flat Boolean circuit on $n$ inputs, and assign to input $j < n$ the entry $a_j$ of $a$, read as
false when $j$ is at least the length of $a$. The result is the list of the values of all gates
of the decoded circuit under this assignment, in order.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.SuccinctCircuitValueEXPComplete.scvCircuitEval`, a definition declared in [WantedExt/Complexity/KeyTheorems/SuccinctCircuitValueEXPCompleteWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/SuccinctCircuitValueEXPCompleteWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/succinct-circuit-value-problem/index.html#scv-circuit-eval).

## Outputs of an encoded circuit (Succinct Circuit Value)

Let $C$ be a list of encoded
gates, $a$ a list of booleans and $k, n \in \mathbb{N}$. Decode each gate of $C$ into a gate of a
flat Boolean circuit on $n$ inputs and evaluate the decoded circuit with input $j < n$ set to the
entry $a_j$ of $a$, read as false when $j$ is at least the length of $a$. The outputs of $C$ on
$a$ are the last $k$ of the resulting gate values, or all of them if $C$ has fewer than $k$
gates.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.SuccinctCircuitValueEXPComplete.scvCircuitOutputs`, a definition declared in [WantedExt/Complexity/KeyTheorems/SuccinctCircuitValueEXPCompleteWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/SuccinctCircuitValueEXPCompleteWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/succinct-circuit-value-problem/index.html#scv-circuit-outputs).

## Fixed-length binary expansion (Succinct Circuit Value)

For natural numbers $i$ and $n$,
this is the list of $n$ booleans $(b_0, \dots, b_{n-1})$, least significant bit first, where
$b_k$ is true exactly when $\lfloor i / 2^k \rfloor$ is odd. For $i < 2^n$ it is the $n$-bit
binary expansion of $i$; in general it is the $n$-bit expansion of $i \bmod 2^n$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.SuccinctCircuitValueEXPComplete.scvBitsOf`, a definition declared in [WantedExt/Complexity/KeyTheorems/SuccinctCircuitValueEXPCompleteWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/SuccinctCircuitValueEXPCompleteWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/succinct-circuit-value-problem/index.html#scv-bits-of).

## Number with a given binary expansion (Succinct Circuit Value)

A list of booleans
$(b_0, \dots, b_{m-1})$, read least significant bit first, denotes the natural number
$\sum_{k < m} [b_k] \, 2^k$, where $[b_k]$ is $1$ if $b_k$ is true and $0$ otherwise; the empty
list denotes $0$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.SuccinctCircuitValueEXPComplete.scvBitsToNum`, a definition declared in [WantedExt/Complexity/KeyTheorems/SuccinctCircuitValueEXPCompleteWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/SuccinctCircuitValueEXPCompleteWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/succinct-circuit-value-problem/index.html#scv-bits-to-num).

## Gate description in a succinct circuit (Succinct Circuit Value)

Let $C$ be a list of
encoded gates and let $n, i \in \mathbb{N}$. Decode each gate of $C$ into a gate of a flat
Boolean circuit on $n$ inputs and evaluate it with input $j < n$ set to bit $j$ of $i$, least
significant bit first, that is, true exactly when $\lfloor i / 2^j \rfloor$ is odd. The
description of gate $i$ of the circuit succinctly described by $C$ is the list of the last
$2n + 3$ resulting gate values, or of all of them if $C$ has fewer than $2n + 3$ gates.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.SuccinctCircuitValueEXPComplete.succDesc`, a definition declared in [WantedExt/Complexity/KeyTheorems/SuccinctCircuitValueEXPCompleteWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/SuccinctCircuitValueEXPCompleteWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/succinct-circuit-value-problem/index.html#succ-desc).

## Decoded gate description (Succinct Circuit Value)

Let $C$ be a list of encoded gates,
let $n, i \in \mathbb{N}$, and let $d$ be the description of gate $i$ of the circuit succinctly
described by $C$: decode each gate of $C$ into a gate of a flat Boolean circuit on $n$ inputs,
evaluate the decoded circuit with input $j < n$ set to bit $j$ of $i$ (true exactly when
$\lfloor i / 2^j \rfloor$ is odd), and take the last $2n + 3$ gate values, or all of them if $C$
has fewer than $2n + 3$ gates. Read a list of booleans $(b_0, \dots, b_{m-1})$ as the number
$\sum_{k < m} [b_k] \, 2^k$, where $[b_k]$ is $1$ if $b_k$ is true and $0$ otherwise, so the
empty list reads as $0$. The information of gate $i$ is the triple $(t, p_1, p_2)$, where the
gate type $t$ is the number read from the first three entries of $d$, the first predecessor $p_1$
is the number read from the next $n$ entries, and the second predecessor $p_2$ is the number read
from all remaining entries; when $d$ is too short, each part uses only the entries that exist.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.SuccinctCircuitValueEXPComplete.succGateInfo`, a definition declared in [WantedExt/Complexity/KeyTheorems/SuccinctCircuitValueEXPCompleteWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/SuccinctCircuitValueEXPCompleteWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/succinct-circuit-value-problem/index.html#succ-gate-info).

## Value of a gate of a succinct circuit (Succinct Circuit Value)

Let $C$ be a list of
encoded gates, let $n, i \in \mathbb{N}$, let $x$ be a list of booleans (the input) and let $v$
be a list of booleans (the values of earlier gates), where an entry outside $x$ or $v$ reads as
false. Let $(t, p_1, p_2)$ be the decoded description of gate $i$ of the circuit succinctly
described by $C$. If $i < n$, gate $i$ is an input gate and its value is $x_i$. Otherwise its
value is $v_{p_1} \land v_{p_2}$ if $t = 1$, $v_{p_1} \lor v_{p_2}$ if $t = 2$, $\lnot v_{p_1}$
if $t = 3$, true if $t = 4$, and false for every other $t$, including $t = 0$ and $t = 5$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.SuccinctCircuitValueEXPComplete.succGateVal`, a definition declared in [WantedExt/Complexity/KeyTheorems/SuccinctCircuitValueEXPCompleteWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/SuccinctCircuitValueEXPCompleteWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/succinct-circuit-value-problem/index.html#succ-gate-val).

## Evaluation of a succinct circuit (Succinct Circuit Value)

Let $C$ be a list of encoded
gates, $n \in \mathbb{N}$ and $x$ a list of booleans. The gate values of the circuit with $2^n$
gates succinctly described by $C$ on input $x$ form the list $(v_0, \dots, v_{2^n - 1})$, where
each $v_i$ is the value of gate $i$ given $x$ and the values $(v_0, \dots, v_{i-1})$ of the
earlier gates.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.SuccinctCircuitValueEXPComplete.succEval`, a definition declared in [WantedExt/Complexity/KeyTheorems/SuccinctCircuitValueEXPCompleteWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/SuccinctCircuitValueEXPCompleteWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/succinct-circuit-value-problem/index.html#succ-eval).

## Well-formed description circuits (Succinct Circuit Value)

A list $C$ of encoded gates
is a well-formed description circuit on $n$ inputs when $C$ has at least $2n + 3$ gates and the
flat Boolean circuit on $n$ inputs obtained by decoding each gate of $C$ is well-formed, that
is, every gate references only strictly earlier gates.

The length bound guarantees that the $2n + 3$ outputs read as a gate description exist; without
it, missing outputs would silently read as false.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.SuccinctCircuitValueEXPComplete.succDescWellFormed`, a definition declared in [WantedExt/Complexity/KeyTheorems/SuccinctCircuitValueEXPCompleteWanted.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/SuccinctCircuitValueEXPCompleteWanted.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/succinct-circuit-value-problem/index.html#succ-desc-well-formed).

## Well-formed succinct circuit descriptions

Let $C$ be a list of encoded gates, read as a
flat Boolean circuit on $n$ inputs that describes a circuit $D$ with $2^n$ gates. For each gate
$i$ of $D$, let $t_i$, $p_i$ and $q_i$ be its gate type, first predecessor and second
predecessor, as decoded from the outputs of $C$ on the $n$-bit binary expansion of $i$. The
description is well formed when, for every $i < 2^n$: if $i < n$, then $t_i = 0$ (gate $i$ is an
input gate); and if $i \ge n$, then either $t_i = 4$ or $t_i = 5$ (a constant gate), or
$p_i < i$ and $q_i < i$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.SuccinctCircuitValueEXPComplete.succWellFormed`, a definition declared in [WantedExt/Complexity/KeyTheorems/SuccinctCircuitValueEXPCompleteWanted.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/SuccinctCircuitValueEXPCompleteWanted.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/succinct-circuit-value-problem/index.html#succ-well-formed).

## Succinct Circuit Value

The decision problem Succinct Circuit Value accepts a bitstring
exactly when it decodes to a triple $(n, C, x)$ of a natural number $n$, a list $C$ of encoded
gates and a bitstring $x$ such that: $x$ has length $n$; $C$ has at least $2n + 3$ gates and,
read as a flat Boolean circuit on $n$ inputs, is well formed; the circuit $D$ with $2^n$ gates
succinctly described by $C$, whose gate $i$ is described by the outputs of $C$ on the $n$-bit
binary expansion of $i$, is well formed; and the last gate of $D$ outputs true when the first
$n$ gates of $D$ are fed the bits of $x$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.SuccinctCircuitValueEXPComplete.succinctCircuitValueDec`, a definition declared in [WantedExt/Complexity/KeyTheorems/SuccinctCircuitValueEXPCompleteWanted.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/SuccinctCircuitValueEXPCompleteWanted.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/succinct-circuit-value-problem/index.html#succinct-circuit-value-dec).

## Succinct Circuit Value is EXP-complete

The decision problem Succinct Circuit Value
belongs to the class EXP, and every decision problem in EXP reduces to Succinct Circuit Value
by a polynomial-time many-one reduction.

## Sources

- C. H. Papadimitriou, Computational Complexity, Addison-Wesley, 1994, Theorem 20.2 (succinct versions of P-complete problems are EXP-complete); S. A. Cook, "A hierarchy for nondeterministic time complexity", Journal of Computer and System Sciences 7 (1973), 343-353; R. E. Ladner, "The circuit value problem is log space complete for P", SIGACT News 7 (1975), 18-20.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.SuccinctCircuitValueEXPComplete.succinct_circuit_value_exp_complete` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/SuccinctCircuitValueEXPCompleteWanted.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/SuccinctCircuitValueEXPCompleteWanted.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/succinct-circuit-value-problem/index.html#succinct-circuit-value-exp-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Succinct circuit value problem](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/succinct-circuit-value-problem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/completeness-other-classes/succinct-circuit-value-problem)
