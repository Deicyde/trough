---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.SuccinctThreeSATNEXPComplete.S3Gate, MetaMathlibExt.Complexity.KeyTheorems.SuccinctThreeSATNEXPComplete.s3CircuitEval, MetaMathlibExt.Complexity.KeyTheorems.SuccinctThreeSATNEXPComplete.s3CircuitOutputs, MetaMathlibExt.Complexity.KeyTheorems.SuccinctThreeSATNEXPComplete.s3ValidGate, MetaMathlibExt.Complexity.KeyTheorems.SuccinctThreeSATNEXPComplete.s3WellFormed, MetaMathlibExt.Complexity.KeyTheorems.SuccinctThreeSATNEXPComplete.s3BitsOf, MetaMathlibExt.Complexity.KeyTheorems.SuccinctThreeSATNEXPComplete.s3BitsToNum, MetaMathlibExt.Complexity.KeyTheorems.SuccinctThreeSATNEXPComplete.succLiteral
statement: formalized
---

# Succinct 3SAT

11 results, 10 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/succinct-3sat/index.html).

## Encoded gates

An encoded gate is a pair $(k, r)$ of a natural number $k$, the kind of
the gate, and a list $r$ of natural numbers, its references. This is the (kind, references)
encoding of the gates of a flat Boolean circuit.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.SuccinctThreeSATNEXPComplete.S3Gate`, an abbreviation declared in [WantedExt/Complexity/KeyTheorems/SuccinctThreeSATNEXPCompleteWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/SuccinctThreeSATNEXPCompleteWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/succinct-3sat/index.html#s3-gate).

## Gate values of an encoded circuit

Let $C = (g_0, \dots, g_{m-1})$ be a list of gates,
each encoded as a (kind, references) pair, let $\alpha$ be a list of booleans and let $n$ be a
natural number. The gate values of $C$ on $\alpha$ are the values $(v_0, \dots, v_{m-1})$ of the
flat Boolean circuit on $n + 2$ inputs obtained by decoding every $g_j$, when input $i$ is given
entry $i$ of $\alpha$, read as false when $i$ is at least the length of $\alpha$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.SuccinctThreeSATNEXPComplete.s3CircuitEval`, a definition declared in [WantedExt/Complexity/KeyTheorems/SuccinctThreeSATNEXPCompleteWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/SuccinctThreeSATNEXPCompleteWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/succinct-3sat/index.html#s3-circuit-eval).

## Outputs of an encoded circuit

Let $C$ be a list of $m$ gates encoded as
(kind, references) pairs, let $\alpha$ be a list of booleans and let $k$ and $n$ be natural
numbers. The last $k$ outputs of $C$ on $\alpha$ are the last $k$ of the gate values
$(v_0, \dots, v_{m-1})$ of $C$ on $\alpha$ as a circuit on $n + 2$ inputs, that is
$(v_{m-k}, \dots, v_{m-1})$; when $k > m$ they are all $m$ gate values.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.SuccinctThreeSATNEXPComplete.s3CircuitOutputs`, a definition declared in [WantedExt/Complexity/KeyTheorems/SuccinctThreeSATNEXPCompleteWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/SuccinctThreeSATNEXPCompleteWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/succinct-3sat/index.html#s3-circuit-outputs).

## Valid gates of a succinct 3SAT descriptor

Let $C$ be a list of gates encoded as
(kind, references) pairs and let $n$ and $j$ be natural numbers. Gate $j$ of $C$ is valid when
$C$ has more than $j$ entries and its entry $j$ (counting from $0$) is one of: $(0, [i])$ with
$i < n + 2$ (an input gate); $(1, [b])$ with $b \le 1$ (a constant gate); $(2, [a])$ with
$a < j$ (a negation gate); or $(3, r)$ or $(4, r)$ where every entry $a$ of $r$ satisfies
$a < j$ (a conjunction or disjunction gate). Every other entry is invalid.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.SuccinctThreeSATNEXPComplete.s3ValidGate`, a definition declared in [WantedExt/Complexity/KeyTheorems/SuccinctThreeSATNEXPCompleteWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/SuccinctThreeSATNEXPCompleteWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/succinct-3sat/index.html#s3-valid-gate).

## Well-formed succinct 3SAT descriptors

Let $C$ be a list of gates encoded as
(kind, references) pairs and let $n$ be a natural number. The descriptor $C$ is well-formed for
$n$ when $C$ has at least $n + 1$ gates, every gate of $C$ is valid for $n$, and the flat Boolean
circuit on $n + 2$ inputs obtained by decoding every gate of $C$ is well-formed.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.SuccinctThreeSATNEXPComplete.s3WellFormed`, a definition declared in [WantedExt/Complexity/KeyTheorems/SuccinctThreeSATNEXPCompleteWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/SuccinctThreeSATNEXPCompleteWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/succinct-3sat/index.html#s3-well-formed).

## Lowest $n$ bits of a number, least significant first

For natural numbers $i$ and $n$,
this is the list of booleans $(b_0, \dots, b_{n-1})$ of length $n$ in which $b_k$ is true exactly
when $\lfloor i / 2^k \rfloor$ is odd: the $n$ lowest binary digits of $i$, least significant bit
first.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.SuccinctThreeSATNEXPComplete.s3BitsOf`, a definition declared in [WantedExt/Complexity/KeyTheorems/SuccinctThreeSATNEXPCompleteWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/SuccinctThreeSATNEXPCompleteWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/succinct-3sat/index.html#s3-bits-of).

## Value of a list of bits, least significant first

A list of booleans
$(b_0, \dots, b_{m-1})$ represents the natural number $\sum_{k < m} [b_k]\, 2^k$, where $[b_k]$
is $1$ if $b_k$ is true and $0$ otherwise.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.SuccinctThreeSATNEXPComplete.s3BitsToNum`, a definition declared in [WantedExt/Complexity/KeyTheorems/SuccinctThreeSATNEXPCompleteWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/SuccinctThreeSATNEXPCompleteWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/succinct-3sat/index.html#s3-bits-to-num).

## Literals of a succinctly described formula

Let $C$ be a list of gates encoded as
(kind, references) pairs and let $n$, $i$ and $j$ be natural numbers. Give $C$, as a circuit on
$n + 2$ inputs, the input consisting of the $n$ lowest bits of $i$ followed by the $2$ lowest
bits of $j$, each least significant bit first, and let $(o_0, \dots, o_{p-1})$ be its last
$n + 1$ outputs. Literal $j$ of clause $i$ is the pair $(v, s)$ with
$v = \sum_{k < \min(n, p)} [o_k]\, 2^k$, where $[o_k]$ is $1$ if $o_k$ is true and $0$
otherwise, and polarity $s = o_n$, read as false when $p \le n$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.SuccinctThreeSATNEXPComplete.succLiteral`, a definition declared in [WantedExt/Complexity/KeyTheorems/SuccinctThreeSATNEXPCompleteWanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/SuccinctThreeSATNEXPCompleteWanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/succinct-3sat/index.html#succ-literal).

## Satisfied clauses of a succinctly described formula

Let $C$ be a list of gates encoded
as (kind, references) pairs, let $n$ and $i$ be natural numbers, and let $\sigma$ assign a
boolean to every natural number. Clause $i$ of the formula described by $C$ for $n$ is satisfied
by $\sigma$ when, for some $j < 3$, literal $j$ of clause $i$ of that formula is a pair $(v, s)$
with $\sigma(v) = s$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.SuccinctThreeSATNEXPComplete.succClauseSat`, a definition declared in [WantedExt/Complexity/KeyTheorems/SuccinctThreeSATNEXPCompleteWanted.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/SuccinctThreeSATNEXPCompleteWanted.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/succinct-3sat/index.html#succ-clause-sat).

## Succinct 3SAT

Succinct 3SAT is the decision problem that accepts a bitstring $x$
exactly when $x$ decodes, under the canonical bitstring encoding, to a pair $(n, C)$ of a natural
number $n$ and a list $C$ of gates encoded as (kind, references) pairs such that $C$ is a
well-formed descriptor for $n$ and some assignment $\sigma$ of booleans to the natural numbers
satisfies clause $c$ of the formula described by $C$ for every $c < 2^n$. Bitstrings that do not
decode are rejected.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.SuccinctThreeSATNEXPComplete.succinctThreeSatDec`, a definition declared in [WantedExt/Complexity/KeyTheorems/SuccinctThreeSATNEXPCompleteWanted.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/SuccinctThreeSATNEXPCompleteWanted.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/succinct-3sat/index.html#succinct-three-sat-dec).

## Succinct 3SAT is NEXP-complete

The succinct 3SAT decision problem lies in NEXP, and every
decision problem in NEXP has a polynomial-time many-one reduction to it.

## Sources

- C. H. Papadimitriou, Computational Complexity, Addison-Wesley, 1994, Theorem 20.3 (succinct 3SAT is NEXP-complete); C. H. Papadimitriou and M. Yannakakis, "A note on succinct representations of graphs", Information and Control 71 (1986), 181-185.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.SuccinctThreeSATNEXPComplete.succinct_three_sat_nexp_complete` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/SuccinctThreeSATNEXPCompleteWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/SuccinctThreeSATNEXPCompleteWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/succinct-3sat/index.html#succinct-three-sat-nexp-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Succinct 3SAT](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/succinct-3sat/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/completeness-other-classes/succinct-3sat)
