---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.CircuitValuePComplete.CVGate, MetaMathlibExt.Complexity.KeyTheorems.CircuitValuePComplete.cvCircuitEval, MetaMathlibExt.Complexity.KeyTheorems.CircuitValuePComplete.CVWellFormed, MetaMathlibExt.Complexity.KeyTheorems.CircuitValuePComplete.cvpDec, MetaMathlibExt.Complexity.KeyTheorems.CircuitValuePComplete.cvp_p_complete
statement: formalized
---

# Circuit value problem

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/circuit-value-problem/index.html).

## Encoded circuit gates

An encoded gate of a flat Boolean circuit is a pair $(k, r)$ of a
natural number $k$, the kind of the gate, and a list $r$ of natural numbers, its references.

Such a pair is read as a gate by the shared (kind, references) decoding of flat circuit gates.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.CircuitValuePComplete.CVGate`, an abbreviation declared in [WantedExt/Complexity/KeyTheorems/CircuitValuePCompleteWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/CircuitValuePCompleteWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/circuit-value-problem/index.html#cvgate).

## Evaluation of an encoded Boolean circuit

Let $n$ be a number of inputs, let $C$ be a
list of gates, each encoded as a (kind, references) pair, and let $a = (a_0, a_1, \dots)$ be a
list of booleans. The evaluation of $C$ on $a$ is the list of values of all gates, in order, of
the flat Boolean circuit on $n$ inputs obtained by decoding each pair of $C$, under the
assignment that sends each input $i < n$ to $a_i$, or to false when $i$ is at least the length
of $a$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.CircuitValuePComplete.cvCircuitEval`, a definition declared in [WantedExt/Complexity/KeyTheorems/CircuitValuePCompleteWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/CircuitValuePCompleteWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/circuit-value-problem/index.html#cv-circuit-eval).

## Well-formed encoded circuits

A list $C$ of encoded gates, each a (kind, references)
pair, is well formed as a circuit on $n$ inputs when the flat Boolean circuit on $n$ inputs
obtained by decoding each pair of $C$ is well formed: every decoded gate references only strictly
earlier gates.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.CircuitValuePComplete.CVWellFormed`, a definition declared in [WantedExt/Complexity/KeyTheorems/CircuitValuePCompleteWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/CircuitValuePCompleteWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/circuit-value-problem/index.html#cvwell-formed).

## The Circuit Value Problem

The Circuit Value Problem is the decision problem that accepts
a bitstring $x$ exactly when $x$ decodes, under the canonical bitstring encoding of such triples,
to a triple $(n, C, a)$ of a natural number $n$, a list $C$ of encoded gates and a list $a$ of
booleans such that the flat Boolean circuit on $n$ inputs obtained by decoding the gates of $C$
is well formed, $a$ has length $n$, and the evaluation of $C$ on $a$ is a nonempty list whose
last entry is true. It rejects every bitstring that does not decode.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.CircuitValuePComplete.cvpDec`, a definition declared in [WantedExt/Complexity/KeyTheorems/CircuitValuePCompleteWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/CircuitValuePCompleteWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/circuit-value-problem/index.html#cvp-dec).

## The Circuit Value Problem is P-complete

The Circuit Value Problem is in P, and every
decision problem in P is log-space many-one reducible to the Circuit Value Problem.

## Sources

- R. E. Ladner, "The circuit value problem is log space complete for P", SIGACT News 7 (1975), 18-20; S. A. Cook, "A hierarchy for nondeterministic time complexity", Journal of Computer and System Sciences 7 (1973), 343-353.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.CircuitValuePComplete.cvp_p_complete` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/CircuitValuePCompleteWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/CircuitValuePCompleteWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/circuit-value-problem/index.html#cvp-p-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Circuit value problem](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/circuit-value-problem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/completeness-other-classes/circuit-value-problem)
