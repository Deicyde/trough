---
declaration: section
origin: cited
lean: Cslib.Turing.Universal.Code.DecidesWithin, Cslib.Turing.Universal.CodeTime, Cslib.Turing.Universal.Code.DecidesWithin.mono, Cslib.Turing.Universal.codeTime_mono, Cslib.Turing.Universal.Code.constFalse, Cslib.Turing.Universal.Code.constFalse_decidesWithin, Cslib.Turing.Universal.const_false_mem_codeTime, Cslib.Turing.Universal.codeTime_eq_empty
statement: formalized
---

# Time hierarchy theorem

70 results, 68 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html).

## Deciding within a time bound

A code $c$ decides a decision problem $L$ within the time
bound $t : \mathbb{N} \to \mathbb{N}$ when, on every bit list $x$, the machine of $c$ started on the
input word of $x$ halts within $t(|x|)$ steps, and its tape from the head rightwards, without
trailing blanks, is the single symbol of the answer $L(x)$: $2$ for true and $1$ for false.

Formalized by `Cslib.Turing.Universal.Code.DecidesWithin`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#decides-within).

## Time classes on codes

For $t : \mathbb{N} \to \mathbb{N}$, $\mathrm{CodeTime}(t)$ is
the class of decision problems $L$ such that some code decides $L$ within $t(|x|)$ steps on
every input $x$.

Formalized by `Cslib.Turing.Universal.CodeTime`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#code-time).

## Deciding within a larger time bound

If a code $c$ decides a decision problem $L$
within a time bound $t : \mathbb{N} \to \mathbb{N}$, and $t' : \mathbb{N} \to \mathbb{N}$
satisfies $t(n) \le t'(n)$ for every $n$, then $c$ decides $L$ within $t'$.

Formalized by `Cslib.Turing.Universal.Code.DecidesWithin.mono`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#mono).

## Monotonicity of time classes on codes

Let $t, t' : \mathbb{N} \to \mathbb{N}$ with
$t(n) \le t'(n)$ for every $n$. Then every decision problem that some code decides within
$t(|x|)$ steps on every input $x$ is decided by some code within $t'(|x|)$ steps on every
input $x$: $\mathrm{CodeTime}(t) \subseteq \mathrm{CodeTime}(t')$.

Formalized by `Cslib.Turing.Universal.codeTime_mono`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#code-time-mono).

## The constant-false code

The code whose table has a single row, for state $0$: on the
blank $0$ it writes the symbol $1$, the symbol of the bit false, and enters state $1$; on the input
symbols $1$ and $2$ it moves right and stays in state $0$; on every other symbol it halts. State $1$
has no row, so the machine halts there. This code answers false on every input.

Formalized by `Cslib.Turing.Universal.Code.constFalse`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#const-false).

## The constant-false code decides the empty language

Let $c$ be the code whose table has
one row, for state $0$: on the input symbols $1$ and $2$ it moves right and stays in state $0$,
and on the blank $0$ it writes $1$, the symbol of the bit $\mathrm{false}$, and enters state
$1$, which has no row, so that $c$ halts. Then $c$ decides the empty language within $n + 1$
steps on every input of length $n$.

Formalized by `Cslib.Turing.Universal.Code.constFalse_decidesWithin`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#const-false-decides-within).

## Time classes are not empty once the bound exceeds the input length

Let
$f : \mathbb{N} \to \mathbb{N}$ satisfy $n + 1 \le f(n)$ for every $n$. Then the empty language, the
decision problem that answers false on every bit list, belongs to the time class of $f$: some code
decides it within $f(|x|)$ steps on every input $x$, where $|x|$ is the length of $x$.

Formalized by `Cslib.Turing.Universal.const_false_mem_codeTime`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#const-false-mem-code-time).

## Some step is needed

Let $f : \mathbb{N} \to \mathbb{N}$ with $f(0) = 0$. Then no
decision problem is decided by a code within $f(|x|)$ steps on every input $x$: the time class
$\mathrm{CodeTime}(f)$ is empty. With no step on the empty input, the tape stays blank and
holds no answer bit.

Formalized by `Cslib.Turing.Universal.codeTime_eq_empty`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#code-time-eq-empty).

## The code stack determines the table lookups

If two codes $c$ and $c'$ have the same
code stack, then for every state $q$ and every symbol $a$, the table entry of $c$ at $(q, a)$
equals the table entry of $c'$ at $(q, a)$.

Formalized by `Cslib.Turing.Universal.Code.lookup_eq_of_codeCells_eq`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#lookup-eq-of-code-cells-eq).

## The code stack determines the clocked semantics

Codes with the same code stack have the
same clocked evaluator.

Formalized by `Cslib.Turing.Universal.Code.evalSteps_eq_of_codeCells_eq`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#eval-steps-eq-of-code-cells-eq).

## Reading a unary length prefix reads one cell

For bit lists $x$ and $r$ and a natural
number $n$, reading a unary length prefix of $x$ returns $n$ together with the rest $r$ if and
only if $x$ is the cell of $n$ (that is, $n$ copies of $\mathrm{true}$ followed by
$\mathrm{false}$) followed by $r$.

Formalized by `Cslib.Turing.Universal.Diag.readUnaryLength_eq_some_iff_cell`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#read-unary-length-eq-some-iff-cell).

## Decoding a list of cells

For a bit list $x$, the list of natural numbers $l$ whose
cells are $x$, if there is one, and nothing otherwise. Here the cells of $l$ are its numbers
written in order, each number $n$ as $n$ copies of $\mathrm{true}$ followed by one
$\mathrm{false}$; distinct lists have distinct cells. The decoder reads one cell at a time
with the unary length reader.

Formalized by `Cslib.Turing.Universal.Diag.cellsDecode`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#cells-decode).

## Reading entries from numbers

A list of natural numbers is read as a list of entries
$(q, a, q', s)$, four consecutive numbers per entry, if possible: the empty list gives no entries;
a list that starts with $q, a, q', s$ and continues with $l$ gives the entry $(q, a, q', s)$
followed by the entries read from $l$, if that succeeds; and the reading fails when the length of
the list is not a multiple of $4$.

Formalized by `Cslib.Turing.Universal.Diag.entriesOfNums`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean, line 291](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean#L291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#entries-of-nums).

## Ascending keys of a list of entries

For natural numbers $p_q$, $p_a$ and a list of
entries $(q, a, q', s) \in \mathbb{N}^4$, this Boolean test is true exactly when the keys
$(q, a)$ of the entries strictly increase in lexicographic order and the first key, if there is
one, is at least $(p_q, p_a)$ in that order.

Formalized by `Cslib.Turing.Universal.Diag.keysAscendFrom`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean, line 298](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean#L298). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#keys-ascend-from).

## The code of a list of entries

Let $E$ be a list of entries $(q, a, q', s)$ of natural
numbers, and let $Q$ and $M$ be the sums, over the entries of $E$ counted with multiplicity, of
$q + 1$ and of $a + 1$ respectively. The code of $E$ has a table with $Q$ rows and $M$
columns, and for $q < Q$ and $a < M$ its position $(q, a)$ holds $(q', s)$ for the first entry
$(q, a, q', s)$ of $E$ with key $(q, a)$, and is empty (halting) if $E$ has no entry with that
key.

Formalized by `Cslib.Turing.Universal.Diag.codeOfEntries`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean, line 305](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean#L305). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#code-of-entries).

## Decoding a code stack

For a bit list $x$, the decoding of $x$ as a code is defined as
follows. Write the cell of a number $n$ for the $n$ bits true followed by one bit false, and the
cells of a list of numbers for the cells of its numbers in order. If $x$ is the cells of a list
$l$ of natural numbers (such an $l$ is unique), the length of $l$ is a multiple of $4$, and the
keys $(q, a)$ of the entries $(q, a, q', s)$ formed by the consecutive groups of four numbers of
$l$ strictly increase in lexicographic order, then the decoding of $x$ is the code of these
entries. Otherwise the decoding returns no code.

The code stack of a code is the cells of the numbers $q, a, q', s$ of its entries
$(q, a, q', s)$, listed by increasing key $(q, a)$; codes with the same code stack have the same
clocked evaluator.

Formalized by `Cslib.Turing.Universal.decodeCodeCells`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean, line 508](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean#L508). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#decode-code-cells).

## The diagonal language

For $f : \mathbb{N} \to \mathbb{N}$, the diagonal language of $f$
holds at a bit list $x$ iff $x$ encodes a code $c$ and the clocked evaluator, running $c$ on $x$
for at most $f(|x|)$ steps, does not return the output $[2]$, the symbol of the answer true:
either $c$ does not halt on $x$ within $f(|x|)$ steps, or it halts with another output. Bit lists
that encode no code are not in the language. This is the diagonal language of the proof of
Sipser's Theorem 9.10.

Formalized by `Cslib.Turing.Universal.diag`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean, line 515](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean#L515). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#diag).

## Decoding inverts the code stack

For every bit list $x$ and every code $c$, if $x$
decodes to $c$, then the code stack of $c$ is $x$.

Formalized by `Cslib.Turing.Universal.codeCells_of_decodeCodeCells_eq_some`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean, line 521](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean#L521). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#code-cells-of-decode-code-cells-eq-some).

## Code stacks are recognized

For every bit list $x$, the decoding of $x$ as a code
succeeds iff $x$ is the code stack of some code.

Formalized by `Cslib.Turing.Universal.isSome_decodeCodeCells_iff`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean, line 531](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean#L531). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#is-some-decode-code-cells-iff).

## Code stacks, entry by entry

A bit list $x$ encodes a code (its decoding succeeds) iff
there is a list of entries $(q, a, q', s)$ of natural numbers whose keys $(q, a)$ strictly
increase in lexicographic order, such that $x$ is the list of cells of the numbers of these
entries, four numbers per entry.

Formalized by `Cslib.Turing.Universal.isSome_decodeCodeCells_iff_entries`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean, line 550](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean#L550). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#is-some-decode-code-cells-iff-entries).

## Code stacks decode to codes with the same code stack

For every code $c$, decoding the code
stack of $c$ succeeds and returns a code $c'$ whose code stack equals the code stack of $c$.

Formalized by `Cslib.Turing.Universal.decodeCodeCells_codeCells`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean, line 565](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean#L565). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#decode-code-cells-code-cells).

## The diagonal language on a code stack

For every time bound
$f : \mathbb{N} \to \mathbb{N}$ and every code $c$ with code stack $x$, the bit list $x$ belongs to
the diagonal language for $f$ iff it is not the case that $c$, run on $x$, halts within $f(|x|)$
steps with output the single symbol $2$ of the bit true.

Formalized by `Cslib.Turing.Universal.diag_codeCells`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean, line 572](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean#L572). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#diag-code-cells).

## Bit lists that encode no code are outside the diagonal language

For every
$f : \mathbb{N} \to \mathbb{N}$ and every bit list $x$ that is the code stack of no code, $x$ is not
in the diagonal language of $f$.

Formalized by `Cslib.Turing.Universal.diag_eq_false`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean, line 579](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean#L579). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#diag-eq-false).

## The diagonal language through the universal machine

For every time bound
$f : \mathbb{N} \to \mathbb{N}$ and every code $c$ with code stack $x$, the bit list $x$ belongs to
the diagonal language for $f$ iff the output encoding of the result of running $c$ on $x$ for at
most $f(|x|)$ steps differs from the output encoding of the result whose output is the single
symbol $2$ of the bit true.

The clocked universal machine reads the input encoding of a code, an input and a clock $T$ and
writes the output encoding of the result of running the code on the input for at most $T$ steps,
so the condition is read from its output on $c$, $x$ and $f(|x|)$.

Formalized by `Cslib.Turing.Universal.diag_codeCells_eq_encOut`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean, line 591](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean#L591). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#diag-code-cells-eq-enc-out).

## The diagonal argument

For every $f : \mathbb{N} \to \mathbb{N}$, the diagonal language of
$f$ is not in the time class of $f$ on codes: no code decides it on every input $x$ within
$f(|x|)$ steps. This is the argument from the proof of Sipser's Theorem 9.10: a code $c$ deciding
it would, on its own code stack, answer the opposite of the diagonal language of $f$.

Formalized by `Cslib.Turing.Universal.diag_not_mem_codeTime`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean, line 601](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean#L601). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#diag-not-mem-code-time).

## A hierarchy within codes, given an upper bound

Let $f, g : \mathbb{N} \to \mathbb{N}$
with $f(n) \le g(n)$ for every $n$, and for a time bound $t$ let $\mathrm{CodeTime}(t)$ be the
class of decision problems that some code decides within $t(|x|)$ steps on every input $x$.
If the diagonal language $\mathrm{diag}(f)$ belongs to $\mathrm{CodeTime}(g)$, then
$\mathrm{CodeTime}(f)$ is a proper subclass of $\mathrm{CodeTime}(g)$.

Formalized by `Cslib.Turing.Universal.codeTime_ssubset_of_diag_mem`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean, line 616](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean#L616). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#code-time-ssubset-of-diag-mem).

## The universal machine's argument for the diagonal language

For a time bound
$f : \mathbb{N} \to \mathbb{N}$ and a bit list $x$, the argument is a triple of a code, an input and
a clock. If $x$ decodes to a code $c$, it is $(c, x, f(|x|))$. Otherwise it is the code with the
empty table, the input consisting of the single bit true, and the clock $0$; that code halts at
once with the answer true, so that the diagonal answer is false there.

Formalized by `Cslib.Turing.Universal.diagArg`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean, line 625](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean#L625). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#diag-arg).

## The reformatting function in bits

For $f : \mathbb{N} \to \mathbb{N}$ and a bit list $x$,
the input bits of the clocked universal machine on its argument for the diagonal language of $f$
on $x$ are, when $x$ encodes a code, the cell of $f(|x|)$, then the cells of the input symbols of
$x$, then the bit false, then $x$ reversed; when $x$ encodes no code, they are the fixed list
$[\mathrm{false}, \mathrm{true}, \mathrm{true}, \mathrm{false}, \mathrm{false}]$.

Formalized by `Cslib.Turing.Universal.encIn_diagArg`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean, line 633](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean#L633). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#enc-in-diag-arg).

## The diagonal answer

For a clocked result $o$, either a timeout or the output of a halted
run, the diagonal answer of $o$ is false if $o$ is the output consisting of the single symbol $2$,
the symbol of the bit true, and true otherwise, including on a timeout.

Formalized by `Cslib.Turing.Universal.diagAnswer`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean, line 646](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean#L646). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#diag-answer).

## The diagonal answer read from the encoded output

For every clocked result $o$, either a
timeout or the output of a halted run, the diagonal answer of $o$ is true exactly when the output
encoding of $o$ differs from the output encoding of the result whose output is the single symbol
$2$ of the bit true, which is the bit list true, true, true, false.

Formalized by `Cslib.Turing.Universal.diagAnswer_eq_decide_encOut`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean, line 650](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean#L650). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#diag-answer-eq-decide-enc-out).

## The diagonal language through the clocked evaluator

For every
$f : \mathbb{N} \to \mathbb{N}$ and every bit list $x$, let $(c, y, T)$ be the universal machine's
argument for the diagonal language of $f$ on $x$. Then the diagonal language of $f$ holds at $x$
iff the clocked evaluator, running $c$ on $y$ for at most $T$ steps, does not return the output
$[2]$, the symbol of the answer true.

Formalized by `Cslib.Turing.Universal.diag_eq_comp`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean, line 656](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean#L656). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#diag-eq-comp).

## Stacks of the readout machine

The readout machine, which reads the answer of the
diagonal language off the output of the clocked universal machine, has exactly two stacks: the
input stack $X$ and the output stack $O$.

Formalized by `Cslib.Turing.Universal.Diag.Readout.K`, an inductive type declared in [CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean, line 668](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean#L668). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#k-3).

## Labels of the readout machine

The readout machine has eight labels: $r_0$, $r_1$,
$r_2$ and $r_3$ read in turn the bits $\mathrm{true}, \mathrm{true}, \mathrm{true},
\mathrm{false}$, which encode, at the output of the clocked universal machine, a halt whose
output is the single symbol of the bit $\mathrm{true}$; $r_4$ checks that no bit follows;
$\mathrm{hit}$ and $\mathrm{miss}$ write the answer; and $\mathrm{done}$ stops.

Formalized by `Cslib.Turing.Universal.Diag.Readout.Lab`, an inductive type declared in [CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean, line 678](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean#L678). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#lab-3).

## Stack alphabet of the readout machine

Every stack of the readout machine, namely
the input stack $X$ and the output stack $O$, has the alphabet of bits.

Formalized by `Cslib.Turing.Universal.Diag.Readout.Γ`, an abbreviation declared in [CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean, line 687](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean#L687). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#untitled-3).

## Expecting a bit in the readout machine

For a bit $b$ and a label $\ell$, the statement
that pops the top of the input stack $X$ and goes to $\ell$ if the popped symbol is $b$, and to the
label miss otherwise, including when $X$ is empty.

Formalized by `Cslib.Turing.Universal.Diag.Readout.expect`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean, line 690](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean#L690). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#expect).

## Program of the readout machine

The readout machine pops the bits of its input stack
$X$ one at a time and compares them with $\mathrm{true}, \mathrm{true}, \mathrm{true},
\mathrm{false}$, which encode, at the output of the clocked universal machine, a halt whose
output is the single symbol of the bit $\mathrm{true}$. If the input is exactly this list, it
pushes $\mathrm{false}$ onto its output stack $O$; otherwise (at the first bit that differs,
when the input ends early, or when a fifth bit follows) it pushes $\mathrm{true}$. Then it
halts.

Formalized by `Cslib.Turing.Universal.Diag.Readout.prog`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean, line 695](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean#L695). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#prog-3).

## The readout machine as a host component

The component machine whose stacks are the
input $X$ and the output $O$, each over the alphabet of bits, whose labels and program are
those of the readout machine, which checks whether $X$ holds exactly
$(\mathrm{true}, \mathrm{true}, \mathrm{true}, \mathrm{false})$ and pushes $\mathrm{false}$ on
$O$ if so and $\mathrm{true}$ otherwise, and whose list of stacks is $(X, O)$.

Formalized by `Cslib.Turing.Universal.Diag.Readout.comp`, an abbreviation declared in [CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean, line 706](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean#L706). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#comp-3).

## The readout run

Let $l$ be a bit list, and start the readout machine at the label
$r_0$ with its internal Boolean variable set to $\mathrm{false}$, $l$ on the input stack $X$ and
the output stack $O$ empty. Then the machine reaches the label $\mathrm{done}$ within $6$ steps,
and $O$ then holds exactly one bit, which is $\mathrm{true}$ if and only if
$l \ne [\mathrm{true}, \mathrm{true}, \mathrm{true}, \mathrm{false}]$, the list that encodes, at
the output of the clocked universal machine, a halt whose output is the single symbol of the bit
$\mathrm{true}$.

Formalized by `Cslib.Turing.Universal.Diag.Readout.run`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean, line 718](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean#L718). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#run-3).

## The readout on raw bits in polynomial time

A finite multi-stack Turing machine, whose
input and output alphabets are identified with the bits, together with a polynomial time bound,
such that for every bit list $l$, given $l$ as its input, it halts within the bound, evaluated at
$|l|$, with output the one-bit list $[b]$, where $b$ is true if and only if $l$ differs from the
output encoding of the result whose output is the single symbol $2$ of the bit true, that is,
from the list true, true, true, false.

Formalized by `Cslib.Turing.Universal.Diag.Readout.bitsPolyTime`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean, line 730](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean#L730). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#bits-poly-time).

## The readout in polynomial time

A finite multi-stack Turing machine, given the output
encoding $\mathrm{encOut}(o)$ of a result $o$ of the clocked universal function (a list of
symbols, or a timeout), outputs the one-bit list $[\mathrm{diagAnswer}(o)]$ within a number
of steps polynomial in the length of $\mathrm{encOut}(o)$. Here $\mathrm{diagAnswer}(o)$ is
$\mathrm{true}$ unless $o$ is a halt whose output is the single symbol of the bit
$\mathrm{true}$.

Formalized by `Cslib.Turing.Universal.Diag.Readout.polyTime`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean, line 740](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean#L740). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#poly-time-3).

## The diagonal language in polynomial time, given the reformatting machine

Let
$f : \mathbb{N} \to \mathbb{N}$. Suppose that a finite multi-stack Turing machine, the
reformatting machine, computes in polynomial time, from a bit list $x$ given as itself, the
input $\mathrm{encIn}(c, y, T)$ of the clocked universal machine, where
$(c, y, T) = \mathrm{diagArg}_f(x)$ is the argument of the clocked universal function for the
diagonal language $\mathrm{diag}_f$ on $x$. Then a finite multi-stack Turing machine computes
$\mathrm{diag}_f$ in polynomial time: on every bit list $x$, given as itself, it outputs the
one-bit list $[\mathrm{diag}_f(x)]$.

The machine runs the reformatting machine, then the clocked universal machine, then the
readout machine.

Formalized by `Cslib.Turing.Universal.nonempty_diag_polyTime`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean, line 754](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/Diagonalization.lean#L754). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#nonempty-diag-poly-time).

## Cell-by-cell check of a code stack

The check of a bit list $x$ from a key $(p_q, p_a)$
of natural numbers is defined as follows. The empty list passes. Otherwise, calling the cell of a
number $n$ the $n$ bits $\mathrm{true}$ followed by one bit $\mathrm{false}$, read four cells off
the front of $x$, those of $q$, $a$, $q'$ and $s$ in this order, leaving the rest $r$. The check
fails if one of these cells cannot be read because what remains contains no bit
$\mathrm{false}$, or if the key $(q, a)$ is lexicographically below $(p_q, p_a)$, that is,
unless $p_q < q$, or $p_q = q$ and $p_a \le a$. Otherwise its result is the check of $r$ from
the key $(q, a + 1)$.

The reformatting machine checks its input this way.

Formalized by `Cslib.Turing.Universal.Diag.chkFrom`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#chk-from).

## The cell-by-cell check recognizes code stacks

For all natural numbers $p_q, p_a$ and
every bit list $x$, the cell-by-cell check of $x$ from the key $(p_q, p_a)$ succeeds if and only
if there is a list of $m \ge 0$ entries $(q_1, a_1, q'_1, s_1), \dots, (q_m, a_m, q'_m, s_m)$ of
natural numbers such that $x$ is the concatenation of the cells of
$q_1, a_1, q'_1, s_1, \dots, q_m, a_m, q'_m, s_m$, in this order, and the keys $(q_i, a_i)$
strictly increase in lexicographic order, starting at $(p_q, p_a)$ or above. Here the cell of a
number $n$ is $n$ bits $\mathrm{true}$ followed by one bit $\mathrm{false}$.

Formalized by `Cslib.Turing.Universal.Diag.chkFrom_iff`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#chk-from-iff).

## Stacks of the checking machine

The checking machine has twelve stacks, named
$X, Y, W, V, Q, A, P_Q, P_A, T_1, T_2, J, O$.

Formalized by `Cslib.Turing.Universal.Diag.Check.K`, an inductive type declared in [CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean, line 390](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean#L390). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#k).

## Labels of the checking machine

The labels of the checking machine: 23 labels without
arguments and four families of labels indexed by the outcome of a comparison ($<$, $=$ or $>$),
35 distinct labels in all.

Formalized by `Cslib.Turing.Universal.Diag.Check.Lab`, an inductive type declared in [CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean, line 399](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean#L399). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#lab).

## Stack alphabet of the layout machine

Every stack of the layout machine holds bits: the
alphabet of each stack is the type of Booleans.

Formalized by `Cslib.Turing.Universal.Diag.Check.Γ`, an abbreviation declared in [CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean, line 417](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean#L417). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#untitled).

## Branch after comparing states

The label the checking machine goes to after comparing the
bound $p$ for the state (the state of the previous key, or $0$ at the first entry) with the
state $q$ of the current key: if $p < q$, the label $\mathsf{sk0}$, where it starts skipping the
rest of the entry; if $p = q$, the label $\mathsf{ca}$, where it compares the symbols; if
$p > q$, the label $\mathsf{bad}$, where it rejects.

Formalized by `Cslib.Turing.Universal.Diag.Check.outQ`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean, line 420](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean#L420). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#out-q).

## Branch after comparing symbols

The label the checking machine goes to after comparing
the bound $p$ for the symbol with the symbol $a$ of the current key: if $p > a$, the label
$\mathsf{bad}$, where it rejects; if $p < a$ or $p = a$, the label $\mathsf{sk0}$, where it starts
skipping the rest of the entry.

Formalized by `Cslib.Turing.Universal.Diag.Check.outA`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean, line 426](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean#L426). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#out-a).

## Program of the checking machine

Writing $1$ for true and $0$ for false, this is the
program of a multi-stack machine whose stacks $X, Y, W, V, Q, A, P_Q, P_A, T_1, T_2, J, O$ all
hold bits. To read a cell from $V$ onto a stack $S$ means to pop the leading $1$s of $V$, pushing
a $1$ on $S$ for each, and then to pop the $0$ that follows; if $V$ is empty at that point, the
machine rejects. From its first label the program pops the bits of $X$ one at a time, pushing
each onto both $Y$ and $W$, and then pops the bits of $W$ one at a time onto $V$. Then it loops.
If $V$ is empty, it pops the bits of $Y$ one at a time onto $O$, pushes a $1$ on $O$ and halts.
Otherwise it reads a cell from $V$ onto $Q$ and then one onto $A$. With $p_Q$, $q$, $p_A$, $a$
the numbers of bits on $P_Q$, $Q$, $P_A$, $A$, it compares $p_Q$ with $q$ and, if they are
equal, $p_A$ with $a$, afterwards pushing back as many $1$s as it popped from each. If
$p_Q > q$, or $p_Q = q$ and $p_A > a$, it rejects; otherwise it reads two more cells from $V$
onto $J$, empties $P_Q$ and $P_A$, moves $Q$ onto $P_Q$ and $A$ onto $P_A$ (pushing a $1$ for
each bit popped), pushes one more $1$ on $P_A$ and loops again. Rejecting pushes a single $0$ on
$O$ and halts.

Formalized by `Cslib.Turing.Universal.Diag.Check.prog`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean, line 431](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean#L431). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#prog).

## Answer of the checking machine

For a bit list $x$, the answer is the list $x$ with
the bit $\mathrm{true}$ put in front if the cell-by-cell check of $x$ from the key $(0, 0)$
succeeds, and the one-bit list $[\mathrm{false}]$ otherwise.

Formalized by `Cslib.Turing.Universal.Diag.Check.answer`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean, line 685](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean#L685). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#answer).

## The checking run

For every bit list $x$, the checking machine, started at the label
$\mathsf{dupP}$ with internal state false, with $x$ on its input stack $X$ and every other stack
empty, reaches the label $\mathsf{done}$ within $33(|x| + 1)^2$ steps, with some internal state
and stacks in which the output stack $O$ holds the answer of the checking machine on $x$.

Formalized by `Cslib.Turing.Universal.Diag.Check.run`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean, line 689](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean#L689). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#run).

## The checking machine as a host component

The component machine with the twelve stacks
$X, Y, W, V, Q, A, P_Q, P_A, T_1, T_2, J, O$ of the checking machine, each holding bits, with
the labels and the program of the checking machine, and with its stacks listed in the order
$X, Y, W, V, Q, A, P_Q, P_A, T_1, T_2, J, O$.

Formalized by `Cslib.Turing.Universal.Diag.Check.comp`, an abbreviation declared in [CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean, line 731](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean#L731). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#comp).

## The checking machine in polynomial time

A finite multi-stack Turing machine with a
polynomial time bound that computes the checking answer: given a bit list $x$ as its input, it
halts within the bound, evaluated at $|x|$, with the checking answer on $x$ as its output.

Formalized by `Cslib.Turing.Universal.Diag.Check.polyTime`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean, line 742](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean#L742). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#poly-time).

## Stacks of the layout machine

The layout machine has twelve stacks, named
$X, Z, P, P_2, U, N, A_2, B_2, D, C, T, O$.

Formalized by `Cslib.Turing.Universal.Diag.Layout.K`, an inductive type declared in [CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean, line 760](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean#L760). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#k-2).

## Labels of the layout machine

The layout machine has 17 labels, named $\mathsf{s0}$,
$\mathsf{mvZ}$, $\mathsf{cp0}$, $\mathsf{cp1}$, $\mathsf{lo0}$, $\mathsf{lo1}$, $\mathsf{lo2}$,
$\mathsf{lo3}$, $\mathsf{lo4}$, $\mathsf{mh}$, $\mathsf{mb}$, $\mathsf{mk}$, $\mathsf{mr}$,
$\mathsf{lo5}$, $\mathsf{lo6}$, $\mathsf{bad}$ and $\mathsf{done}$.

Formalized by `Cslib.Turing.Universal.Diag.Layout.Lab`, an inductive type declared in [CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean, line 769](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean#L769). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#lab-2).

## Stack symbols of the layout machine

Every stack of the layout machine holds bits: the
alphabet of each of its stacks is the type of Booleans.

Formalized by `Cslib.Turing.Universal.Diag.Layout.Γ`, an abbreviation declared in [CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean, line 780](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean#L780). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#untitled-2).

## Program of the layout machine

Writing $1$ for true and $0$ for false, this is the
program of a multi-stack machine whose stacks $X, Z, P, P_2, U, N, A_2, B_2, D, C, T, O$ all hold
bits. To move a stack $S$ onto a stack $S'$ means to pop the bits of $S$ one at a time, pushing
each onto $S'$, until $S$ is empty; to transfer $S$ to some stacks means to pop $S$ until it is
empty, pushing a $1$ on each of these stacks for every bit popped. From the label $\mathsf{s0}$
the program pops $X$. If $X$ was empty or the popped bit is $0$, it pushes $0, 0, 1, 1, 0$ on $O$
in this order and halts. Otherwise it moves $X$ onto $Z$, and then, as long as $Z$ is nonempty,
it pops a bit $b$ from $Z$, pushes $b$ on $U$ and a $1$ on $N$, and pushes $0, 1, 1$ on $P$ in
this order if $b = 1$ and $0, 1$ if $b = 0$. Then it moves $U$ onto $O$, pushes a $0$ on $O$,
moves $P$ onto $P_2$ and then $P_2$ onto $O$, and transfers $N$ to $A_2$ and $B_2$. Then it
loops: it pops $A_2$; if a bit was popped, it pushes a $1$ on $D$, transfers $B_2$ to $C$ and
$T$, transfers $T$ to $B_2$ and loops again; if $A_2$ was empty, it transfers $D$ to $A_2$.
Finally it pushes $0, 1$ on $O$ in this order, transfers $C$ to $O$ and halts.

Formalized by `Cslib.Turing.Universal.Diag.Layout.prog`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean, line 784](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean#L784). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#prog-2).

## The layout function

Write $\mathrm{cell}(n)$ for the bit list of $n$ bits
$\mathrm{true}$ followed by one bit $\mathrm{false}$. On a bit list $\mathrm{true} :: x$, the
layout function returns $\mathrm{cell}(|x|^2 + 1)$, then the cells $\mathrm{cell}(s)$ of the
symbols $s$ of the input word of $x$ (the symbol $2$ for each bit $\mathrm{true}$ and $1$ for
each bit $\mathrm{false}$), then the bit $\mathrm{false}$, then the reverse of $x$. On every other
bit list, that is, the empty list or a list starting with $\mathrm{false}$, it returns the list
$[\mathrm{false}, \mathrm{true}, \mathrm{true}, \mathrm{false}, \mathrm{false}]$.

Formalized by `Cslib.Turing.Universal.Diag.Layout.layout`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean, line 850](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean#L850). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#layout).

## The layout run

For every bit list $y$, the layout machine, started at the label
$\mathsf{s0}$ with internal state false, with $y$ on its input stack $X$ and every other stack
empty, reaches the label $\mathsf{done}$ within $18(|y| + 1)^2$ steps, with some internal state
and stacks in which the output stack $O$ holds the layout of $y$.

Formalized by `Cslib.Turing.Universal.Diag.Layout.run`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean, line 856](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean#L856). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#run-2).

## The cell-by-cell check agrees with code-stack decoding

For every bit list $x$, the
cell-by-cell check of $x$ from the key $(0, 0)$ succeeds if and only if the decoding of $x$ as a
code stack returns a code.

Formalized by `Cslib.Turing.Universal.Diag.chkFrom_zero`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean, line 962](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean#L962). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#chk-from-zero).

## The layout machine as a host component

The component machine with the twelve stacks
$X, Z, P, P_2, U, N, A_2, B_2, D, C, T, O$ of the layout machine, each holding bits, with the
labels and the program of the layout machine, and with its stacks listed in the order
$X, Z, P, P_2, U, N, A_2, B_2, D, C, T, O$.

Formalized by `Cslib.Turing.Universal.Diag.Layout.comp`, an abbreviation declared in [CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean, line 968](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean#L968). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#comp-2).

## The layout in polynomial time

A finite multi-stack Turing machine, whose input and
output alphabets are identified with the bits, together with a polynomial time bound, that
computes the layout function: given a bit list $y$ as its input, it halts within the bound,
evaluated at $|y|$, with the layout of $y$ as its output.

Formalized by `Cslib.Turing.Universal.Diag.Layout.polyTime`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean, line 979](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean#L979). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#poly-time-2).

## Layout after checking gives the universal machine's input

For every bit list $x$, let
$(c, y, T)$ be the universal machine's argument for the diagonal language of $f(n) = n^2 + 1$ on
$x$. Then the layout function applied to the checking machine's answer on $x$ equals the input
bit list of the clocked universal machine for the code $c$, the input $y$ and the clock $T$.

Formalized by `Cslib.Turing.Universal.Diag.layout_answer`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean, line 992](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean#L992). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#layout-answer).

## The reformatting machine for $n \mapsto n^2 + 1$

Let $f(n) = n^2 + 1$. This is a
finite multi-stack Turing machine whose input and output alphabets are identified with the bits,
together with a polynomial $p$, such that for every bit list $x$, started with $x$ on its input
stack it halts within $p(|x|)$ steps with output the clocked universal machine's input bits for
the universal machine's argument $(c, w, T)$ for the diagonal language of $f$ at $x$: the clock
$T$ as a cell, the cells of the input symbols of $w$, a blank cell and the code stack of $c$
reversed. It runs the checking machine and then the layout machine.

Formalized by `Cslib.Turing.Universal.Diag.reformat`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean, line 1002](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean#L1002). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#reformat).

## Deciding the diagonal language on raw bits in polynomial time

Let $D$ be the diagonal
language for the time bound $f(n) = n^2 + 1$. There is a finite multi-stack Turing machine that,
given a bit list $x$ as its input, halts within a number of steps polynomial in $|x|$ with the
single bit $D(x)$ as its output.

Formalized by `Cslib.Turing.Universal.nonempty_diag_sq_add_one_polyTime`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean, line 1017](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean#L1017). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#nonempty-diag-sq-add-one-poly-time).

## The quadratic diagonal language is in P

The diagonal language for the time bound
$f(n) = n^2 + 1$, the set of bit lists $x$ that encode a code which does not halt on $x$ within
$|x|^2 + 1$ steps with the answer $\mathrm{true}$, is in the class P of decision problems
decidable in polynomial time.

The decider decodes the canonical encoding of bit lists and then runs a polynomial-time decider
on the raw bits.

Formalized by `Cslib.Turing.Universal.diag_sq_add_one_mem_P`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean, line 1025](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean#L1025). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#diag-sq-add-one-mem-p).

## Diagonalization across models

There is a decision problem in the class P that no code
decides within $n^2 + 1$ steps: no code halts on every input $x$ within $|x|^2 + 1$ steps with
the answer for $x$ as its output.

The diagonal language for the time bound $n \mapsto n^2 + 1$ is such a problem. The class of
problems that codes decide within $n^2 + 1$ steps is not empty: it contains the problem whose
answer is always $\mathrm{false}$.

Formalized by `Cslib.Turing.Universal.exists_mem_P_not_mem_codeTime_sq_add_one`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean, line 1034](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean#L1034). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#exists-mem-p-not-mem-code-time-sq-add-on).

## Polynomial time is not contained in code time $n^2 + 1$

Some decision problem in
$\mathsf{P}$ is decided by no code within $n^2 + 1$ steps on every input of length $n$; that is,
$\mathsf{P}$ is not a subset of the class $\mathrm{CodeTime}(n \mapsto n^2 + 1)$.

Formalized by `Cslib.Turing.Universal.not_P_subset_codeTime_sq_add_one`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean, line 1039](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/Universal/DiagonalDecider.lean#L1039). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#not-p-subset-code-time-sq-add-one).

## There is an EXP language outside P (time-hierarchy separation)

There is a decision
problem that belongs to the class EXP but not to the complexity class P.

Only this separation is stated; the containment of P in EXP is not part of the statement.

## Sources

- J. Hartmanis and R. E. Stearns, "On the computational complexity of algorithms", Transactions of the American Mathematical Society 117 (1965), 285-306; S. Arora and B. Barak, Computational Complexity: A Modern Approach, 2009, Corollary 3.5.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.PneqEXP.p_ne_exp` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/PneqEXPWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/PneqEXPWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#p-ne-exp).

## Deterministic time hierarchy: quadratic versus linear time

There is a language $L$ of
bitstrings that lies in the multi-tape deterministic time class $\mathrm{DTIME}(n^2)$ but not in
$\mathrm{DTIME}(n)$.

## Sources

- J. Hartmanis and R. E. Stearns, "On the computational complexity of algorithms", Transactions of the American Mathematical Society 117 (1965), 285-306.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.TimeHierarchy.time_hierarchy` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/TimeHierarchyWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/TimeHierarchyWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html#time-hierarchy).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Time hierarchy theorem](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/time-hierarchy-theorem)
