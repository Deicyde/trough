---
declaration: section
origin: cited
lean: Cslib.Complexity.DenseSAT.Clause, Cslib.Complexity.DenseSAT.CNF, Cslib.Complexity.DenseSAT.clauseSat, Cslib.Complexity.DenseSAT.cnfSat, Cslib.Complexity.DenseSAT.decodeAux, Cslib.Complexity.DenseSAT.decodeCNF, Cslib.Complexity.DenseSAT.encodeSlot, Cslib.Complexity.DenseSAT.encodeClause
statement: formalized
proof: formalized
---

# Dense CNF encoding of SAT

72 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html).

## Dense clause

A clause is a finite list of slots, where slot $j$ records how the variable
$x_j$ occurs: the slot is either empty (the variable is absent) or holds a Boolean $b$, meaning
the literal $x_j = b$; so $b$ true gives $x_j$ and $b$ false gives $\lnot x_j$.

Formalized by `Cslib.Complexity.DenseSAT.Clause`, an abbreviation declared in [CSLibExt/Computability/Complexity/DenseSAT.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseSAT.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#clause).

## Dense CNF formula

A CNF formula is a finite list of dense clauses, read as the conjunction
of its clauses.

Formalized by `Cslib.Complexity.DenseSAT.CNF`, an abbreviation declared in [CSLibExt/Computability/Complexity/DenseSAT.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseSAT.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#cnf).

## Satisfaction of a dense clause

A finite bit sequence $a = (a_0, \dots, a_{n-1})$ satisfies
a clause $c$ when there are an index $j$ and a Boolean $b$ such that slot $j$ of $c$ holds the
literal $x_j = b$, $j < n$, and $a_j = b$. Variables $x_j$ with $j \ge n$ are unassigned and
satisfy no literal.

Formalized by `Cslib.Complexity.DenseSAT.clauseSat`, a definition declared in [CSLibExt/Computability/Complexity/DenseSAT.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseSAT.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#clause-sat).

## Satisfaction of a dense CNF formula

A finite bit sequence $a$ satisfies a CNF formula
$\varphi$ when $a$ satisfies every clause of $\varphi$.

Formalized by `Cslib.Complexity.DenseSAT.cnfSat`, a definition declared in [CSLibExt/Computability/Complexity/DenseSAT.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseSAT.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#cnf-sat).

## Dense decoding with an accumulator

Given a bit string $w$ and the list $c$ of slots read so
far for the current clause, stored in reverse order, the result is the CNF formula obtained by
reading $w$ two bits at a time: $00$ outputs the current clause in reading order and continues
with no slots read; $01$ adds an empty slot to the current clause; and $1s$, for a bit $s$, adds a
slot holding the Boolean $\lnot s$, so $10$ adds a positive and $11$ a negative literal. When
fewer than two bits remain, decoding stops and outputs no further clauses, so a trailing
unterminated clause and a dangling odd bit are ignored and decoding is total.

Formalized by `Cslib.Complexity.DenseSAT.decodeAux`, a definition declared in [CSLibExt/Computability/Complexity/DenseSAT.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseSAT.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#decode-aux).

## Dense decoding of CNF formulas

The CNF formula decoded from a bit string $w$ is the
result of the accumulator decoding of $w$ started with no slots read for the current clause:
$w$ is read two bits at a time, $00$ ends a clause, $01$ is an empty slot, $10$ a positive and
$11$ a negative literal, and a trailing unterminated clause and a dangling odd bit are ignored.

Formalized by `Cslib.Complexity.DenseSAT.decodeCNF`, a definition declared in [CSLibExt/Computability/Complexity/DenseSAT.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseSAT.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#decode-cnf).

## Two-bit code of a slot

Slot $j$ of a dense clause is empty (variable $x_j$ is absent),
holds the positive literal $x_j$, or holds the negative literal $\neg x_j$. Its code is $01$ when
empty, $10$ for the positive literal and $11$ for the negative literal.

Formalized by `Cslib.Complexity.DenseSAT.encodeSlot`, a definition declared in [CSLibExt/Computability/Complexity/DenseSAT.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseSAT.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#encode-slot).

## Dense encoding of a clause

The bit string encoding a clause is the concatenation of the
two-bit codes of its slots, in order (empty slot $01$, positive literal $10$, negative literal
$11$), followed by the terminator $00$.

Formalized by `Cslib.Complexity.DenseSAT.encodeClause`, a definition declared in [CSLibExt/Computability/Complexity/DenseSAT.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseSAT.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#encode-clause).

## Dense encoding of a CNF formula

The dense encoding of a CNF formula $\varphi$ is the bit
string obtained by concatenating, in order, the encodings of the clauses of $\varphi$, where a
clause is encoded as the two-bit codes of its slots followed by the terminator $00$.

Formalized by `Cslib.Complexity.DenseSAT.encodeCNF`, a definition declared in [CSLibExt/Computability/Complexity/DenseSAT.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseSAT.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#encode-cnf).

## Decoding inverts the dense encoding

For every CNF formula $\varphi$, decoding the bit
string that encodes $\varphi$ gives back $\varphi$. In particular, every CNF formula is the
decoding of some bit string.

Formalized by `Cslib.Complexity.DenseSAT.decodeCNF_encodeCNF`, a theorem declared in [CSLibExt/Computability/Complexity/DenseSAT.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseSAT.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#decode-cnf-encode-cnf).

## Dense CNF-SAT

A bit string $w$ belongs to dense CNF-SAT when the CNF formula obtained by
decoding $w$ in the dense clause encoding is satisfiable, that is, some assignment (a list of
booleans) satisfies every clause of the decoded formula.

Formalized by `Cslib.Complexity.DenseSAT.SAT`, a definition declared in [CSLibExt/Computability/Complexity/DenseSAT.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseSAT.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#sat).

## Single-pass evaluation of a dense CNF encoding

The scan $E(r, u, v, f)$ takes the formula
bits $r$ still to be read, the assignment bits $u$ not yet used by the current clause, the bits
$v$ already used by it (most recent first) and a boolean $f$ recording whether the current clause
is already satisfied; write $x u'$ for the list with first bit $x$ followed by the list $u'$. It
reads $r$ two bits at a time; let $r'$ be the bits after the pair read. On $00$ (end of clause)
the result is $f \wedge E(r', \overline{v}\,u, [\,], \mathrm{false})$, where $\overline{v}\,u$ is
the reversal of $v$ followed by $u$. On $01$ (an empty slot) the result is $E(r', u', x v, f)$
when $u = x u'$, and $E(r', [\,], v, f)$ when $u$ is empty. On $1s$ (a literal with sign bit $s$)
the result is $E(r', u', x v, f \vee (x = \neg s))$ when $u = x u'$, and $E(r', [\,], v, f)$
when $u$ is empty. When fewer than two bits remain, the result is true.

The scan mirrors the verifier machine step by step.

Formalized by `Cslib.Complexity.DenseSAT.evalCNF`, a definition declared in [CSLibExt/Computability/Complexity/DenseSAT.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseSAT.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#eval-cnf).

## Indexed evaluation of a dense CNF encoding

The scan $I(r, a, j, f)$ takes the formula
bits $r$ still to be read, an assignment $a$ (a list of booleans), the position $j$ of the next
slot in the current clause and a boolean $f$ recording whether the current clause is already
satisfied. It reads $r$ two bits at a time; let $r'$ be the bits after the pair read. On $00$
(end of clause) the result is $f \wedge I(r', a, 0, \mathrm{false})$. On $01$ (an empty slot) the
result is $I(r', a, j + 1, f)$. On $1s$ (a literal with sign bit $s$) the result is
$I(r', a, j + 1, f')$, where $f'$ is true when $f$ is true, or when $j < |a|$ and the entry $a_j$
of $a$ (counting from $0$) equals $\neg s$.
When fewer than two bits remain, the result is true.

Formalized by `Cslib.Complexity.DenseSAT.evalIdx`, a definition declared in [CSLibExt/Computability/Complexity/DenseSAT.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseSAT.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#eval-idx).

## Dense CNF-SAT certificate check

For bit strings $w$ (the encoded formula) and $y$ (the
certificate), the check of $y$ against $w$ is the Boolean result of the verifier's left-to-right
scan of the formula bits $w$, started with $y$ as the assignment bits not yet used by the current
clause, no used bits, and the current clause not yet satisfied.

Formalized by `Cslib.Complexity.DenseSAT.check`, a definition declared in [CSLibExt/Computability/Complexity/DenseSAT.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseSAT.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#check).

## Decoded clauses are no longer than the input

For every bit string $r$ and every clause
$c_0$, every clause produced by the auxiliary decoder run on $r$ with accumulated partial clause
$c_0$ has length at most $|c_0| + |r|$.

Formalized by `Cslib.Complexity.DenseSAT.length_le_of_mem_decodeAux`, a theorem declared in [CSLibExt/Computability/Complexity/DenseSAT.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseSAT.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#length-le-of-mem-decode-aux).

## Truncating a satisfying assignment

Let $w$ be a bit string and $\varphi$ the CNF formula
decoded from $w$. If a finite bit sequence $a$ satisfies $\varphi$, then so does the prefix of $a$
of length $|w|$ (all of $a$ when $a$ has at most $|w|$ bits).

Formalized by `Cslib.Complexity.DenseSAT.cnfSat_take`, a theorem declared in [CSLibExt/Computability/Complexity/DenseSAT.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseSAT.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#cnf-sat-take).

## Certificate characterization of dense CNF-SAT

A bit string $w$ belongs to dense CNF-SAT
if and only if there is a bit string $y$ with $|y| \le |w|$ that the certificate check accepts
on formula bits $w$ and assignment bits $y$.

Formalized by `Cslib.Complexity.DenseSAT.sat_iff_check`, a theorem declared in [CSLibExt/Computability/Complexity/DenseSAT.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseSAT.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#sat-iff-check).

## Work stacks of the dense CNF-SAT verifier

The verifier has four work stacks: the input
stack, a stack $F$ that stashes the formula, and two stacks $A$ and $B$ for the assignment.

Formalized by `Cslib.Complexity.DenseSAT.Verifier.W`, an inductive type declared in [CSLibExt/Computability/Complexity/DenseSATVerifier.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseSATVerifier.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#w).

## Work alphabet of the dense-SAT verifier

The work alphabet $G$ is the disjoint union of
the Booleans and the optional Booleans. Its elements are the left symbols $\mathrm{inl}(b)$ and
the right symbols $\mathrm{inr}(o)$, where $b$ is a Boolean and $o$ is either
$\mathrm{some}\ b$ or $\mathrm{none}$. This is the alphabet of the pair encoding, in which
$\mathrm{inr}(\mathrm{none})$ is the separator $\#$.

Formula and assignment bits are stored on the work stacks as left symbols $\mathrm{inl}(b)$.

Formalized by `Cslib.Complexity.DenseSAT.Verifier.G`, an abbreviation declared in [CSLibExt/Computability/Complexity/DenseSATVerifier.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseSATVerifier.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#g).

## Pair encoding $w \# y$

For bit strings $w$ and $y$, the word over the pair alphabet
$G = \mathrm{Bool} \oplus \mathrm{Option}\,\mathrm{Bool}$ consisting of the bits $b$ of $w$ in
order, each tagged on the left as $\mathrm{inl}\,b$, then the separator
$\# = \mathrm{inr}\,\mathrm{none}$, then the bits $b$ of $y$ in order, each tagged on the right as
$\mathrm{inr}(\mathrm{some}\,b)$. This is the input of the dense CNF-SAT verifier.

Formalized by `Cslib.Complexity.DenseSAT.Verifier.pairEncode`, a definition declared in [CSLibExt/Computability/Complexity/DenseSATVerifier.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseSATVerifier.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#pair-encode).

## Stack alphabets of the dense CNF-SAT verifier

The stacks of the verifier are the output
stack and one stack for each work stack name (input, formula stash $F$, assignment stacks $A$
and $B$). The output stack has the Booleans as alphabet, and every work stack has the alphabet
$G$, the disjoint union of the Booleans and the Booleans extended by a separator $\#$.

Formalized by `Cslib.Complexity.DenseSAT.Verifier.Γ`, a definition declared in [CSLibExt/Computability/Complexity/DenseSATVerifier.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseSATVerifier.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#untitled).

## Labels of the dense-SAT verifier

The labels of the verifier's program are
$\mathrm{read1}$, $\mathrm{read2}$, $\mathrm{back1}$ and $\mathrm{back2}$; $\mathrm{c0}(f)$ and
$\mathrm{c1}(f, b)$ for Booleans $f$ and $b$; $\mathrm{adv}(f, o)$ for a Boolean $f$ and an
optional Boolean $o$; $\mathrm{restore}(f)$ for a Boolean $f$; and $\mathrm{drainI}(a)$,
$\mathrm{drainA}(a)$, $\mathrm{drainB}(a)$ and $\mathrm{finish}(a)$ for a Boolean $a$. There are
finitely many labels, and equality of labels is decidable.

The labels $\mathrm{c0}(f)$ and $\mathrm{c1}(f, b)$ read the two bits of a token, with $f$
recording whether the current clause is already satisfied. $\mathrm{adv}(f, o)$ moves one
assignment bit from stack $B$ to stack $A$ ($o = \mathrm{some}\ s$ for the literal token $1s$),
and $\mathrm{restore}(f)$ moves the used assignment bits back from $A$ to $B$.

Formalized by `Cslib.Complexity.DenseSAT.Verifier.Lab`, an inductive type declared in [CSLibExt/Computability/Complexity/DenseSATVerifier.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseSATVerifier.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#lab).

## Machine states of the verifier

The machine state of the dense CNF-SAT verifier is an
element of $\mathrm{Option}\,G$: either nothing or a work symbol in $G$.

The program uses it to hold the last popped symbol.

Formalized by `Cslib.Complexity.DenseSAT.Verifier.St`, an abbreviation declared in [CSLibExt/Computability/Complexity/DenseSATVerifier.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseSATVerifier.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#st).

## Statements of the dense CNF-SAT verifier

The statements of the verifier are the
statements of Mathlib's multi-stack Turing machine model with stack alphabets $\Gamma$, labels in
the verifier's label type and machine states in $\mathrm{Option}\,G$.

Formalized by `Cslib.Complexity.DenseSAT.Verifier.Stmt`, an abbreviation declared in [CSLibExt/Computability/Complexity/DenseSATVerifier.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseSATVerifier.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#stmt).

## Configurations of the dense-SAT verifier

A configuration of the verifier is a
configuration of the multi-stack Turing machine model with the verifier's labels, states and
stack alphabets. It consists of an optional current label (absent once the machine has halted),
a state, which is either a symbol of the work alphabet $G$ or nothing, and for each stack the
list of symbols on it: Booleans on the output stack and symbols of $G$ on each of the four work
stacks.

Formalized by `Cslib.Complexity.DenseSAT.Verifier.Cfg`, an abbreviation declared in [CSLibExt/Computability/Complexity/DenseSATVerifier.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseSATVerifier.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#cfg).

## Generic copy loop of the dense-SAT verifier

For a work stack $s$, a partial map $g$ on
the work alphabet $G$, an optional target work stack $t$, and labels $\ell$ (the loop's own
label) and $\ell'$ (its exit), the generic loop is the program statement that does the following.
It pops the top of $s$ and stores the popped symbol $x$ as the machine state (nothing if $s$ is
empty). If $x$ exists and $g(x) = y$ is defined, it pushes $y$ onto $t$ (or pushes nothing when
there is no target stack) and jumps to $\ell$. Otherwise, when $s$ was empty or $g$ is undefined
at $x$, it jumps to $\ell'$.

Formalized by `Cslib.Complexity.DenseSAT.Verifier.loop`, a definition declared in [CSLibExt/Computability/Complexity/DenseSATVerifier.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseSATVerifier.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#loop).

## Formula filter of the dense-SAT verifier

The partial map on the work alphabet $G$ that
sends each left symbol $\mathrm{inl}(b)$ to itself and is undefined on every right symbol
$\mathrm{inr}(o)$, including the separator $\mathrm{inr}(\mathrm{none})$, written $\#$.

The verifier's first copying loop uses it, so on the pair encoding of a formula and a
certificate it stops at the separator $\#$.

Formalized by `Cslib.Complexity.DenseSAT.Verifier.gRead1`, a definition declared in [CSLibExt/Computability/Complexity/DenseSATVerifier.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseSATVerifier.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#g-read1).

## Certificate filter of the dense-SAT verifier

The partial map on the work alphabet $G$
that sends each right symbol $\mathrm{inr}(\mathrm{some}\ b)$ to the left symbol
$\mathrm{inl}(b)$ and is undefined on every other symbol, that is on the left symbols and on the
separator $\mathrm{inr}(\mathrm{none})$.

Formalized by `Cslib.Complexity.DenseSAT.Verifier.gRead2`, a definition declared in [CSLibExt/Computability/Complexity/DenseSATVerifier.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseSATVerifier.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#g-read2).

## The dense CNF-SAT verifier program

The program assigns a statement to each label. Every
pop stores the popped symbol, or nothing if the stack was empty, as the machine state.

* $\mathsf{read1}$: pop the input stack; while the popped symbol is some $\mathrm{inl}\,b$, push
  $\mathrm{inl}\,b$ onto $F$ and pop again; otherwise go to $\mathsf{read2}$.
* $\mathsf{read2}$: pop the input stack; while the popped symbol is some
  $\mathrm{inr}(\mathrm{some}\,b)$, push $\mathrm{inl}\,b$ onto $A$ and pop again; otherwise go
  to $\mathsf{back1}$.
* $\mathsf{back1}$: pop $F$ and push each popped symbol onto the input stack until $F$ is empty,
  then go to $\mathsf{back2}$.
* $\mathsf{back2}$: pop $A$ and push each popped symbol onto $B$ until $A$ is empty, then go to
  $\mathsf{c0}(\mathrm{false})$.
* $\mathsf{c0}(fl)$: pop the input stack; if the popped symbol is $\mathrm{inl}\,b$, go to
  $\mathsf{c1}(fl, b)$, otherwise go to $\mathsf{drainI}(\mathrm{true})$.
* $\mathsf{c1}(fl, \mathrm{false})$: pop the input stack; on $\mathrm{inl}\,\mathrm{false}$ go to
  $\mathsf{restore}(fl)$, on $\mathrm{inl}\,\mathrm{true}$ go to
  $\mathsf{adv}(fl, \mathrm{none})$, otherwise go to $\mathsf{drainI}(\mathrm{true})$.
* $\mathsf{c1}(fl, \mathrm{true})$: pop the input stack; on $\mathrm{inl}\,s$ go to
  $\mathsf{adv}(fl, \mathrm{some}\,s)$, otherwise go to $\mathsf{drainI}(\mathrm{true})$.
* $\mathsf{adv}(fl, o)$: pop $B$; if a symbol $x$ was popped, push $x$ onto $A$ and go to
  $\mathsf{c0}(fl')$, where $fl'$ is true when $fl$ is true, or when $o = \mathrm{some}\,s$ for a
  bit $s$ with $x = \mathrm{inl}(\lnot s)$; if $B$ was empty, go to $\mathsf{c0}(fl)$.
* $\mathsf{restore}(fl)$: pop $A$ and push each popped symbol onto $B$ until $A$ is empty, then
  go to $\mathsf{c0}(\mathrm{false})$ if $fl$ is true and to $\mathsf{drainI}(\mathrm{false})$
  otherwise.
* $\mathsf{drainI}(ans)$, $\mathsf{drainA}(ans)$, $\mathsf{drainB}(ans)$: pop and discard the
  input stack, $A$, $B$ respectively until it is empty, then go to $\mathsf{drainA}(ans)$,
  $\mathsf{drainB}(ans)$, $\mathsf{finish}(ans)$ respectively.
* $\mathsf{finish}(ans)$: push $ans$ onto the output stack, clear the machine state and halt.

Formalized by `Cslib.Complexity.DenseSAT.Verifier.prog`, a definition declared in [CSLibExt/Computability/Complexity/DenseSATVerifier.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseSATVerifier.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#prog).

## The dense CNF-SAT verifier machine

The finite multi-stack Turing machine with an output
stack over the Booleans and four work stacks (the input stack, a formula stash $F$ and two
assignment stacks $A$ and $B$) over the alphabet $G$, the disjoint union of the Booleans and the
Booleans extended by a separator $\#$. It reads its input from the input stack, writes its
result to the output stack, starts at the first label of the verifier program with empty
internal state, and runs that program: on input $w \# y$ it moves the formula bits $w$ onto $F$
and the assignment bits $y$ onto $A$, moves them back so that $w$ is on the input stack and $y$
on $B$, then scans $w$ clause by clause, moving assignment bits from $B$ to $A$ to test the
literals of a clause and back from $A$ to $B$ at the end of the clause, and finally empties the
work stacks and pushes the computed bit onto the output stack.

Formalized by `Cslib.Complexity.DenseSAT.Verifier.tm`, a definition declared in [CSLibExt/Computability/Complexity/DenseSATVerifier.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseSATVerifier.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#tm).

## All stacks of the verifier from work stacks and output

Given work-stack contents $V$ (a
list $V(s)$ of work symbols for each work stack $s$) and a list $o$ of bits, the stack contents of
the verifier that give the output stack $o$ and each work stack $s$ the list $V(s)$.

Formalized by `Cslib.Complexity.DenseSAT.Verifier.stk`, a definition declared in [CSLibExt/Computability/Complexity/DenseSATVerifier.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseSATVerifier.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#stk).

## Work stacks from four lists

Given four lists $i$, $f$, $a$, $b$ of work symbols in $G$,
the contents of the verifier's work stacks in which the input stack holds $i$, the formula stash
$F$ holds $f$, and the assignment stacks $A$ and $B$ hold $a$ and $b$.

Formalized by `Cslib.Complexity.DenseSAT.Verifier.mkV`, a definition declared in [CSLibExt/Computability/Complexity/DenseSATVerifier.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseSATVerifier.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#mk-v).

## Pushing a list onto a verifier work stack

Given an optional work stack $t$, a list $ys$
of work symbols and work-stack contents $V$ (a list $V(s)$ of symbols for each work stack $s$),
the contents obtained by pushing the elements of $ys$ one at a time onto $t$: if $t$ is a work
stack, $V(t)$ is replaced by the reverse of $ys$ followed by $V(t)$ and every other stack is
unchanged; if $t$ is none, the result is $V$.

Formalized by `Cslib.Complexity.DenseSAT.Verifier.pushAll`, a definition declared in [CSLibExt/Computability/Complexity/DenseSATVerifier.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseSATVerifier.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#push-all).

## Running the generic copy loop of the dense-SAT verifier

Let $s$ be a work stack, $g$ a
partial map on the work alphabet $G$, $t$ an optional target work stack other than $s$, and
$\ell$, $\ell'$ labels such that the verifier's program at $\ell$ is the generic loop with source
$s$, map $g$, target $t$, own label $\ell$ and exit $\ell'$. Let $o$ be a list of output bits.
Let $x = x_1 \dots x_n$, $y = y_1 \dots y_n$ and $r$ be lists of symbols of $G$ with
$g(x_j) = y_j$ defined for every $j$, and with $r$ empty or $g$ undefined at the first symbol of
$r$. Let $V$ be work-stack contents with $V(s) = x r$, and let $v$ be any state. Started at
$\ell$ in state $v$ with work stacks $V$ and output stack $o$, the program runs for exactly
$n + 1$ steps and reaches the label $\ell'$. Its state is then the first symbol of $r$ (nothing
if $r$ is empty) and its output stack is still $o$. Its work stacks are obtained from $V$ by
replacing stack $s$ with $r$ minus its first symbol (empty if $r$ is empty) and then, if $t$ is
a stack, pushing $y_1, \dots, y_n$ onto $t$ one at a time.

Formalized by `Cslib.Complexity.DenseSAT.Verifier.loop_run`, a theorem declared in [CSLibExt/Computability/Complexity/DenseSATVerifier.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseSATVerifier.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#loop-run).

## Draining the work stacks of the dense-SAT verifier

Let $\mathit{ans}$ be a Boolean, let
$i$, $a$, $b$ be lists of symbols of the work alphabet $G$, and let $v$ be any state. Start the
verifier's program at the label $\mathrm{drainI}(\mathit{ans})$ in state $v$, with the input
stack holding $i$, the formula stash empty, the assignment stacks $A$ and $B$ holding $a$ and
$b$, and the output stack empty. It then runs for exactly $|i| + |a| + |b| + 3$ steps and reaches
the label $\mathrm{finish}(\mathit{ans})$ with no symbol in its state, all four work stacks empty
and the output stack still empty.

Formalized by `Cslib.Complexity.DenseSAT.Verifier.drain_run`, a theorem declared in [CSLibExt/Computability/Complexity/DenseSATVerifier.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseSATVerifier.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#drain-run).

## Left-tagged encoding of a bit list

For a list $l$ of bits, its encoding on a work stack
of the dense-SAT verifier is the list of symbols of the work alphabet $G$ obtained by replacing
each bit $b$ of $l$ with the left symbol $\mathrm{inl}(b)$.

Formalized by `Cslib.Complexity.DenseSAT.Verifier.enc`, a definition declared in [CSLibExt/Computability/Complexity/DenseSATVerifier.lean, line 287](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseSATVerifier.lean#L287). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#enc).

## Step count of the verifier's main scan

The number $T(r, bs, as, fl) \in \mathbb{N}$, for
bit strings $r$, $bs$, $as$ and a flag $fl$, is defined by recursion on $r$, where $0$ is false
and $1$ is true, juxtaposition denotes concatenation (so $b\,r$ is $r$ with the bit $b$
prepended), $[\,]$ is the empty string, $\mathrm{rev}$ reverses a string and $|\cdot|$ is length:

* $T(0\,0\,r, bs, as, fl) = |as| + 3 + T(r, \mathrm{rev}(as)\,bs, [\,], \mathrm{false})$ if $fl$
  is true, and $|as| + 3 + (|r| + (|as| + |bs|) + 3)$ otherwise;
* $T(0\,1\,r, [\,], as, fl) = 3 + T(r, [\,], as, fl)$;
* $T(0\,1\,r, x\,bs, as, fl) = 3 + T(r, bs, x\,as, fl)$;
* $T(1\,s\,r, [\,], as, fl) = 3 + T(r, [\,], as, fl)$;
* $T(1\,s\,r, x\,bs, as, fl) = 3 + T(r, bs, x\,as, fl \lor (x = \lnot s))$;
* $T(r, bs, as, fl) = |r| + |as| + |bs| + 4$ when $r$ has fewer than two bits.

The recursion mirrors the dense CNF evaluation scan.

Formalized by `Cslib.Complexity.DenseSAT.Verifier.T`, a definition declared in [CSLibExt/Computability/Complexity/DenseSATVerifier.lean, line 363](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseSATVerifier.lean#L363). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#t).

## The verifier's main scan

For all bit strings $r$, $bs$, $as$, every flag $fl$ and every
machine state $v$, the verifier program leads in exactly $T(r, bs, as, fl)$ steps from the
configuration at label $\mathsf{c0}(fl)$ with machine state $v$, the input stack holding the bits
of $r$, the stack $A$ holding the bits of $as$ and the stack $B$ holding the bits of $bs$ (each bit
$b$ stored as $\mathrm{inl}\,b$, from the top in order), and the stack $F$ and the output stack
empty, to the configuration at label $\mathsf{finish}(\operatorname{evalCNF}(r, bs, as, fl))$
with empty machine state and all stacks empty.

Formalized by `Cslib.Complexity.DenseSAT.Verifier.scan`, a theorem declared in [CSLibExt/Computability/Complexity/DenseSATVerifier.lean, line 385](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseSATVerifier.lean#L385). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#scan).

## Right-tagged encoding of a certificate

For a list $y$ of bits, its right-tagged encoding
is the list of symbols of the work alphabet $G$ obtained by replacing each bit $b$ of $y$ with
the right symbol $\mathrm{inr}(\mathrm{some}\ b)$. This is how the certificate appears after the
separator in the pair encoding of a formula and a certificate.

Formalized by `Cslib.Complexity.DenseSAT.Verifier.encR`, a definition declared in [CSLibExt/Computability/Complexity/DenseSATVerifier.lean, line 472](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseSATVerifier.lean#L472). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#enc-r).

## Splitting the verifier input

For all bit strings $w$ and $y$, the verifier program
leads in exactly $(|w| + 1) + (|y| + 1) + (|w| + 1) + (|y| + 1)$ steps from the configuration at
label $\mathsf{read1}$ with empty machine state, the input stack holding (from the top) the bits
$b$ of $w$ as $\mathrm{inl}\,b$, the separator $\mathrm{inr}\,\mathrm{none}$ and the bits $b$ of
$y$ as $\mathrm{inr}(\mathrm{some}\,b)$, and all other stacks empty, to the configuration at label
$\mathsf{c0}(\mathrm{false})$ with empty machine state, the input stack holding the bits $b$ of
$w$ as $\mathrm{inl}\,b$, the stack $B$ holding the bits $b$ of $y$ as $\mathrm{inl}\,b$ (both from
the top in order), and the stacks $F$, $A$ and the output stack empty.

The four phases stash $w$ on $F$ and $y$ on $A$, then move them back onto the input stack and
$B$.

Formalized by `Cslib.Complexity.DenseSAT.Verifier.prefix_run`, a theorem declared in [CSLibExt/Computability/Complexity/DenseSATVerifier.lean, line 475](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseSATVerifier.lean#L475). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#prefix-run).

## Step count of the dense CNF-SAT verifier

For bit lists $w$ (a formula) and $y$ (an
assignment), the number $(|w| + 1) + (|y| + 1) + (|w| + 1) + (|y| + 1) + T + 1$, where $T$ is
the step count of the main scan on $w$ started with all of $y$ unused, no assignment bits used
and the clause flag false.

This is the exact number of steps of the verifier machine on input $w \# y$: four passes that
stash and restore $w$ and $y$, the main scan, and one output step.

Formalized by `Cslib.Complexity.DenseSAT.Verifier.totalSteps`, a definition declared in [CSLibExt/Computability/Complexity/DenseSATVerifier.lean, line 513](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseSATVerifier.lean#L513). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#total-steps).

## Time bound of the dense CNF-SAT verifier

The polynomial $2(n + 5)^2$ over $\mathbb{N}$
in one variable $n$. It bounds the running time of the verifier on inputs of length $n$; for a
formula $w$ and an assignment $y$, the input $w \# y$ has length $n = |w| + 1 + |y|$.

Formalized by `Cslib.Complexity.DenseSAT.Verifier.time`, a definition declared in [CSLibExt/Computability/Complexity/DenseSATVerifier.lean, line 517](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseSATVerifier.lean#L517). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#time).

## Polynomial-time verifier for dense CNF-SAT

The verifier machine computes, in polynomial
time, the map sending a pair $(w, y)$ of bit lists to the Boolean $\mathrm{check}(w, y)$, which
is true exactly when $y$ satisfies the CNF formula decoded from $w$. The pair is given as the
input $w \# y$ (the bits of $w$, a separator $\#$, then the bits of $y$), the output is the
single bit $\mathrm{check}(w, y)$, and the machine halts within $2(n + 5)^2$ steps on an input
of length $n$.

Formalized by `Cslib.Complexity.DenseSAT.Verifier.verifier`, a definition declared in [CSLibExt/Computability/Complexity/DenseSATVerifier.lean, line 521](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseSATVerifier.lean#L521). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#verifier).

## Dense CNF-SAT as a decision problem

The decision problem of dense CNF-SAT accepts a bit
string $w$ exactly when $w$ belongs to dense CNF-SAT, that is, when the formula decoded from $w$
in the dense clause encoding has a satisfying assignment.

Formalized by `Cslib.Complexity.DenseSAT.denseSatDec`, a definition declared in [CSLibExt/Computability/Complexity/DenseSATInNP.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseSATInNP.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#dense-sat-dec).

## The dense certificate check runs in polynomial time

The map sending a pair $(w, y)$ of bit
strings to the result of the certificate check on formula bits $w$ and assignment bits $y$ is
polynomial-time computable, where pairs of bit strings carry their canonical bitstring encoding.

Formalized by `Cslib.Complexity.DenseSAT.isPolyTime_check`, a theorem declared in [CSLibExt/Computability/Complexity/DenseSATInNP.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseSATInNP.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#is-poly-time-check).

## Dense CNF-SAT is in NP

**Dense CNF-SAT is in NP.**

Formalized by `Cslib.Complexity.DenseSAT.denseSatDec_mem_NP`, a theorem declared in [CSLibExt/Computability/Complexity/DenseSATInNP.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseSATInNP.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#dense-sat-dec-mem-np).

## The binary code of $2^k - 1$

For every natural number $k$, the binary code of
$2^k - 1$ (Mathlib's encoding of natural numbers as bit lists, least significant bit first) is
the list of $k$ ones.

Formalized by `Cslib.Complexity.DenseSAT.ToBinary.encodeNat_two_pow_sub_one`, a theorem declared in [CSLibExt/Computability/Complexity/DenseToBinary.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseToBinary.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#encode-nat-two-pow-sub-one).

## Self-delimiting code of a block of ones

For every $k \in \mathbb{N}$, the self-delimiting
form of the bit string of $k$ ones is $k$ copies of $11$ followed by a single $0$.

Formalized by `Cslib.Complexity.DenseSAT.ToBinary.delimit_replicate`, a theorem declared in [CSLibExt/Computability/Complexity/DenseToBinary.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseToBinary.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#delimit-replicate).

## Binary codes of literals on variables one less than a power of two

For every
$k \in \mathbb{N}$ and every truth value $b$, the binary code of the literal of polarity $b$ on
variable $2^k - 1$ is $k$ copies of $11$, followed by $0$, followed by the bit $b$.

Formalized by `Cslib.Complexity.DenseSAT.ToBinary.encodeLit_two_pow`, a theorem declared in [CSLibExt/Computability/Complexity/DenseToBinary.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseToBinary.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#encode-lit-two-pow).

## Binary-index translation of a dense clause

Let $k_0 \in \mathbb{N}$ and let $c$ be a dense
clause with slots $s_0, \dots, s_{L-1}$. Its binary-index translation with offset $k_0$ is the
clause that has, for each slot $j$ holding a literal of polarity $b$, the literal of polarity $b$
on variable $2^{k_0 + L - 1 - j} - 1$, listed in increasing order of $j$; absent slots contribute
no literal.

Formalized by `Cslib.Complexity.DenseSAT.ToBinary.binClause`, a definition declared in [CSLibExt/Computability/Complexity/DenseToBinary.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseToBinary.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#bin-clause).

## Binary-index translation of a dense formula

The translation of a dense CNF formula
$\varphi$ replaces each clause $c$ of $\varphi$, keeping their order, by its binary-index
translation with offset $0$: if $c$ has length $L$, each slot $j$ of $c$ holding a literal of
polarity $b$ becomes the literal of polarity $b$ on variable $2^{L - 1 - j} - 1$, and absent slots
are dropped.

Formalized by `Cslib.Complexity.DenseSAT.ToBinary.binCNF`, a definition declared in [CSLibExt/Computability/Complexity/DenseToBinary.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseToBinary.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#bin-cnf).

## The binary-index translation preserves satisfiability when all clauses have equal length

Let $\varphi$ be a dense CNF formula all of whose clauses have the same length $V$. Then the
binary-index translation of $\varphi$ is satisfiable (some assignment of truth values to the
variables satisfies every clause) if and only if some finite list of truth values satisfies
$\varphi$.

Formalized by `Cslib.Complexity.DenseSAT.ToBinary.cnfSat_binCNF_iff`, a theorem declared in [CSLibExt/Computability/Complexity/DenseToBinary.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseToBinary.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#cnf-sat-bin-cnf-iff).

## Closing a clause in the translated output

For a natural number $n$ and a bit string
$o$, closing a clause with $n$ literals in front of $o$ gives the bit string consisting of $n$
ones, then a zero, then $o$; that is, the unary count of $n$ is prepended to $o$.

In the translation, $o$ starts with the codes of the clause's $n$ literals, already emitted.

Formalized by `Cslib.Complexity.DenseSAT.ToBinary.endClause`, a definition declared in [CSLibExt/Computability/Complexity/DenseToBinary.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseToBinary.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#end-clause).

## The dense-to-binary translation on the reversed bit string

The function
$\mathrm{conv}(w, \iota, n, k, m, o)$ consumes the bit string $w$ two bits at a time and prepends
to the output bit string $o$. The truth value $\iota$ records whether a clause is open, $n$ counts
the literals of the open clause, $k$ counts slots and $m$ counts clauses. Juxtaposition of bit
strings is concatenation, $1^n$ is $n$ ones, $(11)^k$ is $k$ copies of $11$, $\bar s$ is the
negation of a bit $s$, and $C$ is $1^n 0\, o$ if $\iota$ is true and $o$ otherwise. For every bit
$s$ and bit string $r$:

* $\mathrm{conv}(00\, r, \iota, n, k, m, o) = \mathrm{conv}(r, \mathrm{true}, 0, 0, m + 1, C)$;
* $\mathrm{conv}(10\, r, \iota, n, k, m, o) = \mathrm{conv}(r, \iota, n, k + 1, m, o)$;
* $\mathrm{conv}(s1\, r, \iota, n, k, m, o)$ is
  $\mathrm{conv}(r, \mathrm{true}, n + 1, k + 1, m, (11)^k 0 \bar s\, o)$ if $\iota$ is true and
  $\mathrm{conv}(r, \mathrm{false}, n, k, m, o)$ otherwise;
* if $w$ has fewer than two bits, $\mathrm{conv}(w, \iota, n, k, m, o) = 1^m 0\, C$.

On the reversed dense encoding a slot $s_1 s_2$ is read as $s_2 s_1$: $00$ is a terminator, which
closes the open clause and opens the next, $10$ is an absent slot, and $s1$ is a present slot,
whose literal $(2^k - 1, \bar s)$ is emitted (its binary code is $(11)^k 0 \bar s$) inside a
clause and skipped outside one. At the end the open clause is closed and the unary clause count
is emitted.

Formalized by `Cslib.Complexity.DenseSAT.ToBinary.conv`, a definition declared in [CSLibExt/Computability/Complexity/DenseToBinary.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseToBinary.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#conv).

## The translation on the slots of a clause

Write $\mathrm{conv}(w, \iota, n, k, m, o)$ for
the reversed-string translation run on the bit string $w$ with open-clause flag $\iota$, literal
count $n$, slot count $k$, clause count $m$ and output $o$; juxtaposition of bit strings is
concatenation, $w^R$ is the reversal of $w$ and $|x|$ is the length of a list $x$. Let $c$ be a
dense clause, $r$ and $o$ bit strings and $n, k, m \in \mathbb{N}$. Let $s(c)$ be the
concatenation of the two-bit codes of the slots of $c$, let $c'$ be the binary-index translation
of $c$ with offset $k$, and let $e$ be the concatenation of the binary codes of the literals of
$c'$. Then
$\mathrm{conv}(s(c)^R r, \mathrm{true}, n, k, m, o) =
\mathrm{conv}(r, \mathrm{true}, n + |c'|, k + |c|, m, e\, o)$.

Formalized by `Cslib.Complexity.DenseSAT.ToBinary.conv_slots`, a theorem declared in [CSLibExt/Computability/Complexity/DenseToBinary.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseToBinary.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#conv-slots).

## The translation on a whole clause

Write $\mathrm{conv}(w, \iota, n, k, m, o)$ for the
reversed-string translation run on the bit string $w$ with open-clause flag $\iota$, literal count
$n$, slot count $k$, clause count $m$ and output $o$; juxtaposition of bit strings is
concatenation, $w^R$ is the reversal of $w$, $1^n$ is $n$ ones and $|x|$ is the length of a list
$x$. Let $c$ be a dense clause, $r$ and $o$ bit strings, $\iota$ a truth value and
$n, k, m \in \mathbb{N}$. Let $E(c)$ be the dense encoding of $c$ (its slot codes followed by the
terminator $00$), $c'$ the binary-index translation of $c$ with offset $0$, and $e$ the
concatenation of the binary codes of the literals of $c'$. Put $o' = 1^n 0\, o$ if $\iota$ is true
and $o' = o$ otherwise. Then
$\mathrm{conv}(E(c)^R r, \iota, n, k, m, o) =
\mathrm{conv}(r, \mathrm{true}, |c'|, |c|, m + 1, e\, o')$.

Formalized by `Cslib.Complexity.DenseSAT.ToBinary.conv_clause`, a theorem declared in [CSLibExt/Computability/Complexity/DenseToBinary.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseToBinary.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#conv-clause).

## The translation on the remaining clauses

Write $\mathrm{conv}(w, \iota, n, k, m, o)$ for
the reversed-string translation run on the bit string $w$ with open-clause flag $\iota$, literal
count $n$, slot count $k$, clause count $m$ and output $o$; juxtaposition of bit strings is
concatenation, $w^R$ is the reversal of $w$, $1^n$ is $n$ ones and $|x|$ is the length of a list
$x$. For a dense clause $c$, let $E(c)$ be its dense encoding, $c'$ its binary-index translation
with offset $0$, $e(c)$ the concatenation of the binary codes of the literals of $c'$, and $B(c)$
the binary code of the clause $c'$. Let $p, k, m \in \mathbb{N}$, let $c_0, c_1, \dots, c_p$ be
dense clauses and let $D$ be a bit string. Then
$\mathrm{conv}(E(c_1)^R \cdots E(c_p)^R, \mathrm{true}, |c_0'|, k, m, e(c_0)\, D) =
1^{m + p} 0\, B(c_p) \cdots B(c_1) B(c_0) D$.

Formalized by `Cslib.Complexity.DenseSAT.ToBinary.conv_clauses`, a theorem declared in [CSLibExt/Computability/Complexity/DenseToBinary.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseToBinary.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#conv-clauses).

## The translation computes the binary encoding

Let $\varphi$ be a dense CNF formula. Run the
reversed-string translation on the reversal of the dense encoding of $\varphi$, starting with no
clause open, literal count $0$, slot count $0$, clause count $0$ and empty output. The result is
the binary encoding of the binary-index translation of $\varphi$.

Formalized by `Cslib.Complexity.DenseSAT.ToBinary.conv_encodeCNF`, a theorem declared in [CSLibExt/Computability/Complexity/DenseToBinary.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseToBinary.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#conv-encode-cnf).

## SAT accepts the code of a formula exactly when it is satisfiable

For every CNF formula
$\psi$, the SAT decision problem returns true on the length-prefixed binary code of $\psi$ if and
only if $\psi$ is satisfiable.

Formalized by `Cslib.Complexity.DenseSAT.ToBinary.satDec_encodeCNF`, a theorem declared in [CSLibExt/Computability/Complexity/DenseToBinary.lean, line 257](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseToBinary.lean#L257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#sat-dec-encode-cnf).

## Unparsable input is not in SAT

If the decoder for binary-encoded CNF formulas fails on
a bit string $x$, then the SAT decision problem rejects $x$.

Formalized by `Cslib.Complexity.DenseSAT.ToBinary.satDec_of_decodeCNF_eq_none`, a theorem declared in [CSLibExt/Computability/Complexity/DenseToBinary.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseToBinary.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#sat-dec-of-decode-cnf-eq-none).

## The dense-to-binary translation on bit strings

The translation of a bit string $w$ is the
backwards dense-to-binary translation applied to the reversal of $w$, started with no clause open,
with its literal, slot and clause counters all equal to $0$, and with empty output.

Formalized by `Cslib.Complexity.DenseSAT.ToBinary.binConv`, a definition declared in [CSLibExt/Computability/Complexity/DenseToBinaryConverter.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseToBinaryConverter.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#bin-conv).

## Stacks of the dense-to-binary machine

The stack names of the Turing machine for the
dense-to-binary translation form a type with exactly seven elements: the input, a stash, the
output, the three counters $n$, $k$ and $m$, and a scratch stack $t$.

Formalized by `Cslib.Complexity.DenseSAT.ToBinary.Stk`, an inductive type declared in [CSLibExt/Computability/Complexity/DenseToBinaryConverter.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseToBinaryConverter.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#stk-2).

## Labels of the dense-to-binary converter

The labels of the dense-to-binary converter
program are the moving label $\mathrm{mv}$; the reading label $\mathrm{rd}(\iota)$ for a Boolean
$\iota$; the second-read label $\mathrm{rd2}(\iota, s)$ for Booleans $\iota$ and $s$; the two
literal labels $\mathrm{litA}$ and $\mathrm{litB}$; the two closing labels $\mathrm{eN}$ and
$\mathrm{eK}$; the clearing label $\mathrm{fK}(\iota)$ for a Boolean $\iota$; the literal-count
label $\mathrm{fN}$; and the clause-count label $\mathrm{fM}$. Equality of labels is decidable.

Here $\iota$ records whether a clause is open, and $s$ is the first bit read of a slot.

Formalized by `Cslib.Complexity.DenseSAT.ToBinary.Lab`, an inductive type declared in [CSLibExt/Computability/Complexity/DenseToBinaryConverter.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseToBinaryConverter.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#lab-2).

## Stack contents of the converter

For bit strings $i$, $a$, $o$ and natural numbers
$n, k, m, t$, this stack assignment gives the input stack $i$, the stash $a$, the output stack $o$,
and the counter stacks $N$, $K$, $M$ and the scratch stack $T$ respectively $n$, $k$, $m$ and $t$
copies of $1$ (true).

Formalized by `Cslib.Complexity.DenseSAT.ToBinary.stk`, a definition declared in [CSLibExt/Computability/Complexity/DenseToBinaryConverter.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseToBinaryConverter.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#stk-3).

## The dense-to-binary converter program

The program uses an input stack, a stash, an
output stack, unary counter stacks $N$, $K$, $M$ and a scratch stack $T$; each label first pops
one stack and keeps the popped bit (or nothing, if the stack was empty) as its internal state.
Below, $\iota$ says whether a clause is open, $0$ is false and $1$ is true.

Moving: pop the input; if a bit $b$ was popped, push $b$ onto the stash and repeat, otherwise go to
reading with $\iota$ false.

Reading with $\iota$: pop the stash; if a bit $s$ was popped, go to the second read with $\iota$
and $s$, otherwise go to clearing with $\iota$.

Second read with $\iota$ and $s$: pop the stash. If it was empty, go to clearing with $\iota$. If
it gave $0$: when $s = 1$, push $1$ onto $K$ and go to reading with $\iota$; when $s = 0$ and
$\iota$ is true, push $0$ onto the output and go to the first closing label; when $s = 0$ and
$\iota$ is false, go to the second closing label. If it gave $1$: when $\iota$ is true, push
$\lnot s$ and then $0$ onto the output and go to the first literal label; otherwise go to reading
with $\iota$ false.

First literal label: pop $K$; if a bit was popped, push $1$ twice onto the output and $1$ onto $T$
and repeat, otherwise go to the second literal label.

Second literal label: pop $T$; if a bit was popped, push $1$ onto $K$ and repeat, otherwise push
$1$ onto $N$, then $1$ onto $K$, and go to reading with $\iota$ true.

First closing label: pop $N$; if a bit was popped, push $1$ onto the output and repeat, otherwise
go to the second closing label.

Second closing label: pop $K$; if a bit was popped, repeat, otherwise push $1$ onto $M$ and go to
reading with $\iota$ true.

Clearing with $\iota$: pop $K$; if a bit was popped, repeat, otherwise push $0$ onto the output and
go to the literal-count label if $\iota$ is true and to the clause-count label otherwise.

Literal-count label: pop $N$; if a bit was popped, push $1$ onto the output and repeat, otherwise
push $0$ onto the output and go to the clause-count label.

Clause-count label: pop $M$; if a bit was popped, push $1$ onto the output and repeat, otherwise
halt.

Formalized by `Cslib.Complexity.DenseSAT.ToBinary.prog`, a definition declared in [CSLibExt/Computability/Complexity/DenseToBinaryConverter.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseToBinaryConverter.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#prog-2).

## Exact runs of the dense-to-binary converter

For a natural number $n$ and configurations
$c$ and $d$ of the converter program, $c$ leads to $d$ in exactly $n$ steps when the program,
started at $c$, is at configuration $d$ after exactly $n$ steps.

Formalized by `Cslib.Complexity.DenseSAT.ToBinary.Run`, an abbreviation declared in [CSLibExt/Computability/Complexity/DenseToBinaryConverter.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseToBinaryConverter.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#run).

## Moving the input onto the stash

Let $l$, $a$, $o$ be bit strings and $v$ an optional
bit, and list stacks top first. Started at the moving label with internal state $v$, input stack
$l$, stash $a$, output stack $o$, empty counter stacks $N$, $K$, $M$ and empty scratch stack $T$,
the dense-to-binary converter reaches, in exactly $|l| + 1$ steps, the label for reading with no
clause open, with no internal state, an empty input stack, the reversal of $l$ followed by $a$ on
the stash, output stack $o$, and $N$, $K$, $M$, $T$ still empty.

Formalized by `Cslib.Complexity.DenseSAT.ToBinary.mv_run`, a theorem declared in [CSLibExt/Computability/Complexity/DenseToBinaryConverter.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseToBinaryConverter.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#mv-run).

## The converter's final phase

Write $0$ for false, $1$ for true and $1^j$ for $j$ copies
of $1$. Let $o$ be a bit string, $\iota$ a flag saying whether a clause is open, and $n, k, m$
natural numbers with $n = 0$ if no clause is open; let $c = n + 1$ if a clause is open and $c = 0$
otherwise. Started at the label that clears the slot counter at the end, for the flag $\iota$, with
empty internal state, empty input and stash, output $o$, literal, slot and clause counter stacks
holding $n$, $k$ and $m$ ones respectively, and an empty scratch stack, the converter reaches in
exactly $(k + 1) + c + (m + 1)$ steps the halting configuration with empty internal state, every
stack but the output empty, and output $1^m 0 1^n 0 o$ if a clause is open and $1^m 0 o$ otherwise
(listed from the top of the stack).

Formalized by `Cslib.Complexity.DenseSAT.ToBinary.fin_run`, a theorem declared in [CSLibExt/Computability/Complexity/DenseToBinaryConverter.lean, line 258](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseToBinaryConverter.lean#L258). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#fin-run).

## Step count of the main loop

Write $0$ for false, $1$ for true, and $xyr$ for the bit
string whose first two bits are $x, y$ followed by $r$. For a bit string $l$, a flag $\iota$
(whether a clause is open) and natural numbers $n, k, m$, let $c = n + 1$ if $\iota$ is true and
$c = 0$ otherwise. The step count $T(l, \iota, n, k, m)$ is defined by recursion on $l$:
$T(00r, \iota, n, k, m) = 2 + c + (k + 1) + T(r, 1, 0, 0, m + 1)$;
$T(10r, \iota, n, k, m) = 2 + T(r, \iota, n, k + 1, m)$;
for every bit $s$, $T(s1r, \iota, n, k, m)$ is $2 + 2(k + 1) + T(r, 1, n + 1, k + 1, m)$ if $\iota$
is true and $2 + T(r, 0, n, k, m)$ otherwise; on a one-bit string $T = 2 + (k + 1) + c + (m + 1)$;
and on the empty string $T = 1 + (k + 1) + c + (m + 1)$.

Formalized by `Cslib.Complexity.DenseSAT.ToBinary.convT`, a definition declared in [CSLibExt/Computability/Complexity/DenseToBinaryConverter.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseToBinaryConverter.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#conv-t).

## Step bound for the main loop

For every bit string $l$, whether or not a clause is open, and
all natural numbers $n, k, m, Q$ with $|l| + n + k + m \le Q$, the exact step count of the main loop
on stash $l$ with literal, slot and clause counters $n, k, m$ is at most
$(|l| + 1)(2Q + 6) + Q + 4$.

Formalized by `Cslib.Complexity.DenseSAT.ToBinary.convT_le`, a theorem declared in [CSLibExt/Computability/Complexity/DenseToBinaryConverter.lean, line 362](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseToBinaryConverter.lean#L362). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#conv-t-le).

## The dense-to-binary machine

The multi-stack Turing machine whose stacks are indexed by
the stack names (input, stash, output, the counters $n$, $k$, $m$ and the scratch $t$), each
with the Booleans as alphabet. It reads its input from the input stack and leaves its output on
the output stack; its labels are the program labels, starting at the label that moves the input
onto the stash; its internal state is an optional Boolean, initially empty; and each label runs
the corresponding statement of the program.

Formalized by `Cslib.Complexity.DenseSAT.ToBinary.tm`, a definition declared in [CSLibExt/Computability/Complexity/DenseToBinaryConverter.lean, line 406](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseToBinaryConverter.lean#L406). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#tm-2).

## The dense-to-binary translation on raw bits is polynomial-time

There is a finite
multi-stack Turing machine whose input and output alphabets are the bits such that, for every bit
string $w$ of length $L$, the machine started on input $w$ halts within $2L^2 + 10L + 11$ steps with
the dense-to-binary translation of $w$ on its output stack and all other stacks empty.

Formalized by `Cslib.Complexity.DenseSAT.ToBinary.computable`, a definition declared in [CSLibExt/Computability/Complexity/DenseToBinaryConverter.lean, line 432](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/DenseToBinaryConverter.lean#L432). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html#computable).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Dense CNF encoding of SAT](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/cook-levin/dense-cnf-encoding-of-sat)
