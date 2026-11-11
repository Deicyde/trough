---
declaration: section
origin: cited
lean: Cslib.Circuits.Wire.toFin, Cslib.Circuits.Circuit.verifyBooleanCertificate, Cslib.Circuits.Circuit.verifyBooleanCertificate_iff, Cslib.Circuits.Circuit.verifyBooleanCertificate_sound, Cslib.Circuits.Circuit.verifyBooleanCertificate_complete, Cslib.Circuits.Circuit.verifyBooleanCertificate_satisfiable_iff, Cslib.Circuits.Circuit.verifyBooleanCertificate_time, Cslib.Circuits.Circuit.verifyBooleanCertificate_time_le_of_fanInAtMost
statement: formalized
---

# Circuit satisfiability

16 results, 15 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/circuit-satisfiability/index.html).

## Certificate position of a wire

For a wire that refers to one of $n$ inputs or one of $g$
gates, its position in $\{0, \dots, n + g - 1\}$ is $k$ if it is input $k$ and $n + j$ if it is
gate $j$, so the inputs come first and the gates follow.

Formalized by `Cslib.Circuits.Wire.toFin`, a definition declared in [CSLibExt/Algorithms/Lean/Circuit/Verification.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Circuit/Verification.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/circuit-satisfiability/index.html#to-fin).

## Boolean certificate verifier

Let $c$ be a circuit over the Boolean signature with $n$
inputs, $s$ gates and one output, and let $b = (b_0, \dots, b_{m-1})$ be an array of truth values,
read as a value for each wire: input $k$ at position $k$ and gate $j$ at position $n + j$. The
verifier is a computation with a counted cost. It first checks whether $m = n + s$, at cost $1$;
if not, it returns false. Otherwise, for each gate $j < s$ in order, it reads the entries of $b$
at the positions of the argument wires of gate $j$, at cost $1$ per argument, and compares the
Boolean interpretation of the operation of gate $j$ on these values with $b_{n+j}$, at cost $1$;
finally it reads the entry at the position of the output wire, at cost $1$. It returns true
exactly when every comparison succeeds and that output entry is true.

Formalized by `Cslib.Circuits.Circuit.verifyBooleanCertificate`, a definition declared in [CSLibExt/Algorithms/Lean/Circuit/Verification.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Circuit/Verification.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/circuit-satisfiability/index.html#verify-boolean-certificate).

## Characterization of accepted certificates

Let $c$ be a circuit over the Boolean signature
with $n$ inputs, $s$ gates and one output, and let $b = (b_0, \dots, b_{m-1})$ be an array of truth
values, where an entry at a position at or beyond $m$ is read as false and the position of a wire
is $k$ for input $k$ and $n + j$ for gate $j$. The Boolean certificate verifier accepts $b$ if and
only if $m = n + s$, for every gate $j < s$ the Boolean interpretation of the operation of gate $j$
applied to the entries of $b$ at the positions of its argument wires equals $b_{n+j}$, and the
entry of $b$ at the position of the output wire is true.

Formalized by `Cslib.Circuits.Circuit.verifyBooleanCertificate_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Circuit/Verification.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Circuit/Verification.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/circuit-satisfiability/index.html#verify-boolean-certificate-iff).

## Soundness of the Boolean certificate verifier

Let $c$ be a circuit over the Boolean
signature with $n$ inputs, $s$ gates and one output, and let $b = (b_0, \dots, b_{m-1})$ be an array
of truth values, where an entry at a position at or beyond $m$ is read as false and the position
of a wire is $k$ for input $k$ and $n + j$ for gate $j$. If the Boolean certificate verifier
accepts $b$, then, writing $x = (b_0, \dots, b_{n-1})$, the value of every wire of $c$ on input $x$
under the Boolean interpretation equals the entry of $b$ at the position of that wire, and the
output of $c$ on input $x$ is true.

Formalized by `Cslib.Circuits.Circuit.verifyBooleanCertificate_sound`, a theorem declared in [CSLibExt/Algorithms/Lean/Circuit/Verification.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Circuit/Verification.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/circuit-satisfiability/index.html#verify-boolean-certificate-sound).

## Completeness of the Boolean certificate verifier

Let $c$ be a circuit over the Boolean
signature with $n$ inputs, $s$ gates and one output, and let $x = (x_0, \dots, x_{n-1})$ be truth
values on which the output of $c$ under the Boolean interpretation is true. Let $b$ be the array
$(x_0, \dots, x_{n-1}, v_0, \dots, v_{s-1})$, where $v_j$ is the value of gate $j$ of $c$ on input
$x$. Then $b$ has length $n + s$ and the Boolean certificate verifier accepts $b$.

Formalized by `Cslib.Circuits.Circuit.verifyBooleanCertificate_complete`, a theorem declared in [CSLibExt/Algorithms/Lean/Circuit/Verification.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Circuit/Verification.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/circuit-satisfiability/index.html#verify-boolean-certificate-complete).

## Short accepted certificates exist exactly for satisfiable circuits

Let $c$ be a circuit
over the Boolean signature with $n$ inputs, $s$ gates and one output. The Boolean certificate
verifier accepts some array of at most $n + 2s$ truth values if and only if there are truth
values $x_0, \dots, x_{n-1}$ on which the output of $c$ under the Boolean interpretation is
true.

Formalized by `Cslib.Circuits.Circuit.verifyBooleanCertificate_satisfiable_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Circuit/Verification.lean, line 270](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Circuit/Verification.lean#L270). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/circuit-satisfiability/index.html#verify-boolean-certificate-satisfiable-i).

## Cost of the Boolean certificate verifier

Let $c$ be a circuit over the Boolean signature
with $n$ inputs, $s$ gates and one output, and let $b$ be an array of $m$ truth values. The cost
counted by the Boolean certificate verifier on $b$ is $2 + s + \sum_{j < s} a_j$ if $m = n + s$,
where $a_j$ is the number of arguments of gate $j$, and $1$ otherwise.

Formalized by `Cslib.Circuits.Circuit.verifyBooleanCertificate_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Circuit/Verification.lean, line 284](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Circuit/Verification.lean#L284). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/circuit-satisfiability/index.html#verify-boolean-certificate-time).

## Linear cost of the Boolean certificate verifier

Let $K$ be a natural number and let $c$ be
a circuit over the Boolean signature with $n$ inputs, $s$ gates and one output in which every gate
has at most $K$ arguments. Then for every array $b$ of truth values, the cost counted by the
Boolean certificate verifier on $b$ is at most $2 + (K + 1)s$.

Formalized by `Cslib.Circuits.Circuit.verifyBooleanCertificate_time_le_of_fanInAtMost`, a theorem declared in [CSLibExt/Algorithms/Lean/Circuit/Verification.lean, line 296](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Circuit/Verification.lean#L296). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/circuit-satisfiability/index.html#verify-boolean-certificate-time-le-of-fa).

## Circuit-satisfiability instances

An instance of circuit satisfiability is a pair $(n, G)$
of a natural number $n$, the number of variables, and a finite list $G$ of gates, each gate a
triple $(o, a, b)$ of natural numbers: an operation code $o$, a first input $a$ and a second
input $b$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.CircuitSat.CircuitSatInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/CircuitSatWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/CircuitSatWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/circuit-satisfiability/index.html#circuit-sat-instance).

## Resolving a circuit input

Given an assignment $x = (x_0, \dots, x_{n-1})$ of booleans to
the variables and the list $v = (v_0, \dots, v_{k-1})$ of the values of the gates evaluated so
far, an input index $r$ resolves to $x_r$ if $r < n$, to $v_{r-n}$ if $n \le r < n + k$, and to
false if $r \ge n + k$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.CircuitSat.CircuitRef`, a definition declared in [WantedExt/Complexity/NPComplete/CircuitSatWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/CircuitSatWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/circuit-satisfiability/index.html#circuit-ref).

## Value of a gate

Let $x = (x_0, \dots, x_{n-1})$ be an assignment of booleans to the
variables and $v$ the list of values of the earlier gates. An input index $r$ resolves to $x_r$ if
$r < n$, and otherwise to $v_{r-n}$, or to false if that entry does not exist. The value of a gate
$(o, a, b)$ is the conjunction of the resolved inputs $a$ and $b$ if $o = 0$, their disjunction
if $o = 1$, the negation of the resolved input $a$ if $o = 2$, $x_a$ (false if $a \ge n$) if
$o = 3$, true if $o = 4$, and false if $o \ge 5$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.CircuitSat.GateValue`, a definition declared in [WantedExt/Complexity/NPComplete/CircuitSatWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/CircuitSatWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/circuit-satisfiability/index.html#gate-value).

## Evaluating a circuit

Given an assignment of booleans to the variables and a list of gates
$g_1, \dots, g_m$, circuit evaluation returns the list $(v_1, \dots, v_m)$ of gate values, where
$v_k$ is the value of the gate $g_k$ under the assignment and the earlier values
$(v_1, \dots, v_{k-1})$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.CircuitSat.EvalCircuit`, a definition declared in [WantedExt/Complexity/NPComplete/CircuitSatWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/CircuitSatWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/circuit-satisfiability/index.html#eval-circuit).

## Well-formed circuit-satisfiability instances

An instance $(n, G)$ with gates
$G = (g_0, \dots, g_{m-1})$ is well formed when every gate $g_j = (o, a, b)$ satisfies
$o \le 5$, and moreover: if $o = 0$ or $o = 1$ then $a < n + j$ and $b < n + j$; if $o = 2$ then
$a < n + j$; and if $o = 3$ then $a < n$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.CircuitSat.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/CircuitSatWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/CircuitSatWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/circuit-satisfiability/index.html#well-formed).

## Satisfiable circuit instances

An instance $(n, G)$ is satisfiable when there is an
assignment $x \in \{\mathrm{true}, \mathrm{false}\}^n$ of booleans to the $n$ variables such that
the evaluation of the circuit $G$ under $x$ has a last gate value and that value is true. In
particular an instance with no gates is not satisfiable.

Formalized by `MetaMathlibExt.Complexity.NPComplete.CircuitSat.CircuitSatFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/CircuitSatWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/CircuitSatWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/circuit-satisfiability/index.html#circuit-sat-feasible).

## The CIRCUIT SAT decision problem

CIRCUIT SAT is the decision problem that accepts a
bitstring $s$ exactly when $s$ decodes, under the canonical bitstring encoding of
circuit-satisfiability instances, to an instance that is well formed and satisfiable. Bitstrings
that fail to decode are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.CircuitSat.circuitSatDec`, a definition declared in [WantedExt/Complexity/NPComplete/CircuitSatWanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/CircuitSatWanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/circuit-satisfiability/index.html#circuit-sat-dec).

## CIRCUIT SAT is NP-complete

The CIRCUIT SAT decision problem on bitstrings belongs to the
class NP, and every decision problem in NP reduces to it by a polynomial-time many-one reduction.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability: A Guide to the Theory of NP-Completeness* (1979), CIRCUIT SATISFIABILITY; S. A. Cook, "The complexity of theorem-proving procedures" (1971).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.CircuitSat.circuitSat_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/CircuitSatWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/CircuitSatWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/circuit-satisfiability/index.html#circuit-sat-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Circuit satisfiability](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/circuit-satisfiability/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/satisfiability/circuit-satisfiability)
