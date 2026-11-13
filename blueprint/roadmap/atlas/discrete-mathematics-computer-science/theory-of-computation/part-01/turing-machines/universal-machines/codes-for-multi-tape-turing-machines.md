---
declaration: section
origin: cited
lean: Cslib.Turing.MultiTapeTM.decodeMove, Cslib.Turing.MultiTapeTM.CodeAction, Cslib.Turing.MultiTapeTM.CodeAction.equivProd, Cslib.Turing.MultiTapeTM.CodeAction.toAction, Cslib.Turing.MultiTapeTM.CodeAction.halt, Cslib.Turing.MultiTapeTM.CodeKey, Cslib.Turing.MultiTapeTM.Code, Cslib.Turing.MultiTapeTM.Code.equivTable
statement: formalized
proof: formalized
---

# Codes for multi-tape Turing machines

59 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html).

## Decoding a Turing machine head move

Decode a head move: `0` moves left, `1` stays, anything else moves right.

Formalized by `Cslib.Turing.MultiTapeTM.decodeMove`, a definition declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#decode-move).

## Coded actions

A coded action for a machine with $k$ work tapes consists of a coded
input-head move; for each of the $k$ work tapes, an optional symbol to write, the symbol being a
bit or the blank (so a blank can be written), together with a coded head move; an optional
output bit; and an optional next state in $\mathbb{N}$, where no next state means halting. A
head move is coded by a natural number: $0$ moves left, $1$ stays, and any other number moves
right.

Formalized by `Cslib.Turing.MultiTapeTM.CodeAction`, a structure declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#code-action).

## Coded actions as tuples

The bijection between coded actions and tuples $(m, w, b, q)$
that sends an action to its coded input head move $m \in \mathbb{N}$, its work tape instructions
$w$ (for each of the $k$ work tapes, an optional symbol to write and a coded head move), its
optional output bit $b$ and its optional next state $q$.

Formalized by `Cslib.Turing.MultiTapeTM.CodeAction.equivProd`, a definition declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#equiv-prod).

## Decoding a coded action

A coded action $a$ stands for the action of CSLib's multi-tape
model that moves the input head by the decoded input move of $a$, on each work tape writes the
optional symbol that $a$ gives for that tape and moves its head by the decoded move, emits the
optional output bit of $a$, and enters the next state of $a$ (halting when there is none).

Formalized by `Cslib.Turing.MultiTapeTM.CodeAction.toAction`, a definition declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#to-action).

## Halting action

The default action of a missing table entry: halt without moving any
head, writing any symbol or emitting an output bit.

Formalized by `Cslib.Turing.MultiTapeTM.CodeAction.halt`, a definition declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#halt).

## Keys of a code's table

A key of a table entry for a machine with $k$ work tapes is a
triple $(q, a, w)$ of a state $q \in \mathbb{N}$, the symbol $a$ under the input head and the
symbols $w = (w_i)_{i < k}$ under the $k$ work heads, where each symbol is a bit or the blank.

Formalized by `Cslib.Turing.MultiTapeTM.CodeKey`, an abbreviation declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#code-key).

## Codes for multi-tape machines

A code for a machine with $k$ work tapes over the binary
alphabet, with states in $\mathbb{N}$, is a finite list of table entries, each a key (a state
together with the symbols under the input head and the $k$ work heads) paired with a coded
action. The table is looked up by key, the first matching entry wins, and a missing key halts
the machine.

Formalized by `Cslib.Turing.MultiTapeTM.Code`, a structure declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#code).

## Multi-tape codes as tables

The bijection between codes for machines with $k$ work tapes
and finite lists of table entries, each a pair of a key and a coded action, that sends a code to
its table.

Formalized by `Cslib.Turing.MultiTapeTM.Code.equivTable`, a definition declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#equiv-table).

## Numeric coding of codes

The natural number coding a code $c$: its encoding under the
standard primitive recursive coding of codes, which identifies a code with its table, a list of
pairs of a key and a coded action.

Formalized by `Cslib.Turing.MultiTapeTM.Code.encode`, a definition declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#encode).

## Decoding numbers to codes

The code coded by a natural number $n$, if any: decoding
under the standard primitive recursive coding of codes, which identifies a code with its table,
a list of pairs of a key and a coded action. The result is empty when $n$ codes no code.

Formalized by `Cslib.Turing.MultiTapeTM.Code.decode`, a definition declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#decode).

## Code round-trip

For every code $c$ with $k$ work tapes, decoding the natural number
$\operatorname{encode}(c)$ returns $c$: $\operatorname{decode}(\operatorname{encode}(c))$ is
defined and equals $c$.

Formalized by `Cslib.Turing.MultiTapeTM.Code.decode_encode`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#decode-encode).

## Injectivity of the numeric coding of codes

If two codes $c$ and $c'$ with the same
number of work tapes have the same numeric code, then $c = c'$.

Formalized by `Cslib.Turing.MultiTapeTM.Code.encode_injective`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#encode-injective).

## Action of a code at a key

For a code $c$ with $k$ work tapes, a state
$q \in \mathbb{N}$, a symbol $a$ under the input head and symbols $w = (w_i)_{i < k}$ under the
work heads (each symbol a bit or the blank), the action of $c$ at $(q, a, w)$ is the coded action
of the first table entry of $c$ whose key is $(q, a, w)$, or, if there is no such entry, the
halting action, which moves no head, writes and emits nothing, and has no next state.

Formalized by `Cslib.Turing.MultiTapeTM.Code.act`, a definition declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#act).

## Transition function of a code

The transition function of a code $c$ sends a state $q$,
the symbol $a$ under the input head and the symbols $w$ under the work heads (each a bit or
blank) to the action of CSLib's multi-tape model that the coded action of $c$ at $(q, a, w)$
stands for. That coded action is the one of the first table entry of $c$ with key $(q, a, w)$,
or, if there is none, the one that halts without moving, writing or emitting.

Formalized by `Cslib.Turing.MultiTapeTM.Code.tr`, a definition declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#tr).

## The multi-tape machine of a code

The machine of a code $c$ for $k$ work tapes is the
machine of CSLib's multi-tape model with $k$ work tapes, the binary alphabet and states in
$\mathbb{N}$ whose initial state is $0$ and whose transition function is the transition function
of $c$.

Formalized by `Cslib.Turing.MultiTapeTM.Code.toTM`, a definition declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#to-tm).

## Step of the machine of a code

For a code $c$, a binary input $x$ and a configuration $C$
of the machine of $c$ on $x$, the step of the machine of $c$ sends $C$ to its successor under
the transition function of $c$: $C$ itself if it has halted, and otherwise the result of
applying to $C$ the action that the transition function of $c$ selects for the state of $C$ and
the symbols under its heads.

Formalized by `Cslib.Turing.MultiTapeTM.Code.step_toTM`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#step-to-tm).

## States of a multi-tape code

The states of a code $c$ for machines with $k$ work tapes
form the finite set of natural numbers consisting of the initial state $0$ and the next state of
every table entry of $c$ that does not halt.

Formalized by `Cslib.Turing.MultiTapeTM.Code.states`, a definition declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#states).

## Next states of a code lie in its state set

For a code $c$, a state $q$, an input symbol
$a$ and work tape symbols $w$, if the action of $c$ at $(q, a, w)$ has a next state $q'$ (rather
than halting), then $q'$ belongs to the set of states of $c$.

Formalized by `Cslib.Turing.MultiTapeTM.Code.next_act_mem_states`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#next-act-mem-states).

## Codes denote finite-state machines

Let $c$ be a code for a machine with $k$ work tapes.
For every binary input $x$ and every number of steps $t$, if the machine of $c$, run for $t$
steps from its initial configuration on $x$, has not halted and is in state $q$, then $q$ lies
in the finite set of states of $c$.

Formalized by `Cslib.Turing.MultiTapeTM.Code.state_runFrom_mem_states`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#state-run-from-mem-states).

## Work tapes as zippers

A work tape is a pair of finite lists of cells, each cell a bit or
blank: the cells left of the head, nearest first, and the cells from the head rightwards; cells
beyond both lists are blank.

Formalized by `Cslib.Turing.MultiTapeTM.Code.Tape`, an abbreviation declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#tape).

## Symbol under the head of a zipper tape

The symbol read from a work tape given as a zipper
$(l, r)$ is the first cell of $r$, or the blank if $r$ is empty.

Formalized by `Cslib.Turing.MultiTapeTM.Code.Tape.read`, a definition declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#read).

## Writing on a zipper tape

Writing an optional symbol on a work tape leaves the tape
unchanged when no symbol is given; given a symbol $s$ (a bit or blank), it replaces the cell
under the head by $s$ and keeps all other cells.

Formalized by `Cslib.Turing.MultiTapeTM.Code.Tape.write`, a definition declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#write).

## Moving the head of a zipper tape

For a coded move $m$ and a work tape given as a zipper
$(l, r)$: if $m = 0$ the head moves one cell left, removing the first cell of $l$ (the blank if $l$
is empty) and putting it in front of $r$; if $m = 1$ the tape is unchanged; otherwise the head
moves one cell right, removing the first cell of $r$ (the blank if $r$ is empty) and putting it in
front of $l$.

Formalized by `Cslib.Turing.MultiTapeTM.Code.Tape.move`, a definition declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#move).

## Cell of a zipper tape

For a work tape $t$ in zipper form and an integer $j$, the cell of
$t$ at $j$ is the symbol at offset $j$ from the head: for $j = n \ge 0$ it is entry $n$ (counting
from $0$) of the list of cells from the head rightwards, and for $j = -(n + 1)$ it is entry $n$ of
the list of cells left of the head, nearest first; in either case it is the blank when the list
has no entry $n$.

Formalized by `Cslib.Turing.MultiTapeTM.Code.Tape.cell`, a definition declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#cell).

## Explicit configurations of the code evaluator

An explicit configuration for a machine
with $k$ work tapes consists of an optional state in $\mathbb{N}$ (none when the machine has
halted); the input head position, a natural number shifted by one, so that position $0$ is the
cell left of the input; the $k$ work tapes, each a zipper (the cells left of the head, nearest
first, and the cells from the head rightwards, all further cells blank); and the output written
so far, a binary word.

Formalized by `Cslib.Turing.MultiTapeTM.Code.Config`, a structure declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean, line 308](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean#L308). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#config).

## Explicit configurations as tuples

The bijection between explicit configurations and
tuples $(q, p, t, o)$ that sends a configuration to its optional state $q$ (empty when halted),
its shifted input head position $p \in \mathbb{N}$, its family $t$ of $k$ work tapes (each a
zipper) and its output $o$ so far, a list of bits.

Formalized by `Cslib.Turing.MultiTapeTM.Code.Config.equivProd`, a definition declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean, line 321](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean#L321). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#equiv-prod-2).

## Initial configuration of the clocked evaluator

The initial explicit configuration has
state $0$, the input head on the first input cell (position $1$, positions being shifted by one),
every work tape blank (both halves of its zipper empty), and empty output.

Formalized by `Cslib.Turing.MultiTapeTM.Code.Config.init`, a definition declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean, line 331](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean#L331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#init).

## Input symbol under the input head

For an input $x$ and a shifted input head position
$p$, the input symbol is the blank if $p = 0$; otherwise it is the entry of $x$ at index $p - 1$
(counting from $0$) if $p - 1 < |x|$, and the blank if $p - 1 \ge |x|$.

Formalized by `Cslib.Turing.MultiTapeTM.Code.Config.inputSym`, a definition declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean, line 334](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean#L334). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#input-sym).

## Input head move of the clocked evaluator

For an input of length $n$, a shifted input head
position $p$ and a coded move $m$, the new position is $p - 1$ (truncated at $0$) if $m = 0$, $p$
if $m = 1$, and $\min(p + 1, n + 1)$ otherwise, so a move right never passes position $n + 1$,
one cell beyond the input.

Formalized by `Cslib.Turing.MultiTapeTM.Code.Config.moveInput`, a definition declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean, line 337](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean#L337). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#move-input).

## Applying a coded action

Given an input word $x$, a coded action $a$ and an explicit
configuration $e$, applying $a$ to $e$ gives the configuration whose state is the next state of
$a$; whose input head position is that of $e$, say $p$, moved by the coded input move of $a$,
where a left move gives $p - 1$ (truncated at $0$), staying gives $p$, and a right move gives
$\min(p + 1, |x| + 1)$; whose work tape $i$ is work tape $i$ of $e$ after writing the optional
symbol of $a$ for tape $i$ under the head and then moving the head by the coded move of $a$ for
tape $i$; and whose output is the output of $e$ followed by the output bit of $a$, if any.

Formalized by `Cslib.Turing.MultiTapeTM.Code.Config.apply`, a definition declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean, line 340](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean#L340). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#apply).

## Evaluator step

One step of the evaluator for a code $c$ on a binary input $x$ leaves an
explicit configuration $e$ unchanged if $e$ has halted; if $e$ is in state $q$, it applies to
$e$ the coded action of $c$ at $q$, the input symbol at the input head position of $e$ and the
symbols under the heads of the work tapes of $e$.

Formalized by `Cslib.Turing.MultiTapeTM.Code.Config.step`, a definition declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean, line 347](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean#L347). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#step).

## Clocked evaluator

The clocked evaluator runs a code $c$ on a binary input $x$ for $T$
steps: it applies the evaluator's step $T$ times to the initial explicit configuration. If the
resulting configuration is halted, it returns that configuration's output; otherwise it
returns no result.

Formalized by `Cslib.Turing.MultiTapeTM.Code.evalSteps`, a definition declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean, line 356](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean#L356). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#eval-steps).

## Explicit configurations representing machine configurations

An explicit configuration $e$
represents a configuration $C$ of CSLib's multi-tape model on input $x$ when they have the same
state, the same shifted input head position and the same output, and for every work tape $i$ and
every cell $z \in \mathbb{Z}$, the content of cell $z$ of tape $i$ in $C$ equals the cell of tape
$i$ of $e$ at offset $z - p_i$ from its head, where $p_i$ is the head position of tape $i$
in $C$.

Formalized by `Cslib.Turing.MultiTapeTM.Code.Represents`, a structure declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean, line 366](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean#L366). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#represents).

## The evaluator simulates the machine step for step

Let $c$ be a code and $x$ a binary
input. If an explicit configuration $e$ represents a configuration $C$ of the machine of $c$ on
$x$, then the evaluator's step of $e$ for $c$ on $x$ represents the successor of $C$ under the
machine of $c$.

Formalized by `Cslib.Turing.MultiTapeTM.Code.Represents.step`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean, line 425](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean#L425). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#step-2).

## The evaluator tracks the machine run

For a code $c$, an input $x$ and every $t$, the
explicit configuration obtained from the initial one by $t$ steps of the evaluator for $c$ on $x$
represents the configuration that the machine of $c$ reaches after $t$ steps from its initial
configuration on $x$.

Formalized by `Cslib.Turing.MultiTapeTM.Code.represents_iterate`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean, line 463](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean#L463). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#represents-iterate).

## Evaluator agreement

For every code $c$, binary input $x$, clock $T \in \mathbb{N}$
and binary word $o$, the clocked evaluator of $c$ on $x$ with clock $T$ returns $o$ if and
only if the machine of $c$, run for $T$ steps from its initial configuration on $x$, has
halted and its output is $o$.

Formalized by `Cslib.Turing.MultiTapeTM.Code.evalSteps_eq_some_iff`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean, line 473](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean#L473). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#eval-steps-eq-some-iff).

## The evaluator returns within the clock exactly when the machine runs in time

For a code
$c$, an input $x$ and a clock $T$, the clocked evaluator of $c$ on $x$ with clock $T$ returns an
output if and only if the machine of $c$ runs in time $T$ on $x$, that is, every computation path
of that machine on $x$ with at least $T$ steps ends in a halted configuration.

Formalized by `Cslib.Turing.MultiTapeTM.Code.isSome_evalSteps_iff_runsInTime`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean, line 483](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean#L483). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#is-some-eval-steps-iff-runs-in-time).

## Monotonicity of the clocked evaluator for multi-tape codes

For a code $c$ for machines
with $k$ work tapes, a binary input $x$, a binary word $o$ and clocks $T \le T'$ in $\mathbb{N}$,
if the clocked evaluator of $c$ on $x$ returns $o$ with clock $T$, then it also returns $o$ with
clock $T'$.

Formalized by `Cslib.Turing.MultiTapeTM.Code.evalSteps_mono`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean, line 490](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean#L490). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#eval-steps-mono).

## A code computes exactly what its clocked evaluator returns

For a code $c$ with $k$ work
tapes and binary words $x$ and $o$, the machine of $c$ computes $o$ on input $x$, that is, it
eventually halts on $x$ with output $o$, if and only if there is a clock $T \in \mathbb{N}$ such
that the clocked evaluator of $c$ run on $x$ for $T$ steps returns $o$.

Formalized by `Cslib.Turing.MultiTapeTM.Code.computes_iff_exists_evalSteps`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean, line 497](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean#L497). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#computes-iff-exists-eval-steps).

## The evaluator is primitive recursive

**The evaluator is primitive recursive** in the code, the input and the clock.

Formalized by `Cslib.Turing.MultiTapeTM.Code.primrec_evalSteps`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean, line 629](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/Code.lean#L629). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#primrec-eval-steps).

## Coding head moves

A head move is coded as a natural number: left is $0$, stay is $1$
and right is $2$. Decoding a move code recovers the move.

Formalized by `Cslib.Turing.MultiTapeTM.encodeMove`, a definition declared in [CSLibExt/Computability/Machines/Turing/MultiTape/CodeCompleteness.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/CodeCompleteness.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#encode-move).

## Coding an action

Let $e : Q \to \mathbb{N}$ number the states $Q$ of a binary multi-tape
machine with $k$ work tapes. The coded action of an action $a$ of the machine under $e$ records as
its input-head move the code of the input-head move of $a$ (left $0$, stay $1$, right $2$); for
each work tape it records what $a$ writes there and the code of the head move of $a$ there; it
records the output bit of $a$, if any; and its next state is $e(q)$ when $a$ enters the state $q$,
and it halts when $a$ halts.

Formalized by `Cslib.Turing.MultiTapeTM.encodeAction`, a definition declared in [CSLibExt/Computability/Machines/Turing/MultiTape/CodeCompleteness.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/CodeCompleteness.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#encode-action).

## Decoding the coding of an action

Let $Q$ be a type, $e : Q \to \mathbb{N}$ a map and $a$
an action of a binary machine with $k$ work tapes and states in $Q$. The action that the coded
action of $a$, with its successor state numbered by $e$, stands for is $a$ with its successor
state relabelled by $e$.

Formalized by `Cslib.Turing.MultiTapeTM.toAction_encodeAction`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/CodeCompleteness.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/CodeCompleteness.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#to-action-encode-action).

## State bound of a code

The states of a code $c$ are the initial state $0$ and every
successor state named in its table. The state bound of $c$ is one more than the largest of them;
it is a strict upper bound on the states of $c$.

Formalized by `Cslib.Turing.MultiTapeTM.Code.stateBound`, a definition declared in [CSLibExt/Computability/Machines/Turing/MultiTape/CodeCompleteness.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/CodeCompleteness.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#state-bound).

## A number as a bounded state

For natural numbers $N$ and $q$, this is $q$ as an element
of $\{0, \dots, N - 1\}$ if $q < N$, and no value otherwise.

Formalized by `Cslib.Turing.MultiTapeTM.Code.finState`, a definition declared in [CSLibExt/Computability/Machines/Turing/MultiTape/CodeCompleteness.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/CodeCompleteness.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#fin-state).

## Transition function of a code on bounded states

Let $c$ be a code with $k$ work tapes
and let $N$ be its state bound. For a state $q < N$, a symbol $a$ under the input head and
symbols $w$ under the $k$ work heads (each a bit or blank), this is the action of $c$ at
$(q, a, w)$ with the same input-head move, work-tape writes and moves, and output, and with its
successor state read as a state below $N$; a successor state that is not below $N$ is replaced
by halting.

Formalized by `Cslib.Turing.MultiTapeTM.Code.finTr`, a definition declared in [CSLibExt/Computability/Machines/Turing/MultiTape/CodeCompleteness.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/CodeCompleteness.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#fin-tr).

## The finite-state machine of a code

For a code $c$ with $k$ work tapes and state bound
$N$, this is the binary machine with $k$ work tapes and states $0, 1, \dots, N - 1$ that starts
in state $0$ and, in a state $q < N$ reading $a$ under the input head and $w$ under the work
heads, takes the action of $c$ at $(q, a, w)$, with a successor state not below $N$ replaced by
halting. Since every state the machine of $c$ can enter is below $N$, it is the machine of $c$
with its states restricted to those below $N$.

Formalized by `Cslib.Turing.MultiTapeTM.Code.toFinTM`, a definition declared in [CSLibExt/Computability/Machines/Turing/MultiTape/CodeCompleteness.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/CodeCompleteness.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#to-fin-tm).

## A code's machine simulates its finite-state machine

For every code $c$, the machine of
$c$ simulates the finite-state machine of $c$ up to the relabelling that sends each state
$q < N$, where $N$ is the state bound of $c$, to the natural number $q$.

Formalized by `Cslib.Turing.MultiTapeTM.Code.isRelabelling_toFinTM`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/CodeCompleteness.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/CodeCompleteness.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#is-relabelling-to-fin-tm).

## Computation by a code is finite-state computation

Let $c$ be a code with $k$ work tapes,
let $g : \alpha \to \beta$ be a function, let inputs in $\alpha$ and outputs in $\beta$ be encoded
by injective maps into binary words, and let $t, s : \alpha \to \mathbb{N}$. If the machine of $c$,
started on the encoding of any input $x$, halts with the encoding of $g(x)$ as output, halts
within $t(x)$ steps, and visits at most $s(x)$ work-tape cells, then some binary multi-tape
machine with finitely many states computes $g$ within the same bounds in the same sense.

Formalized by `Cslib.Turing.MultiTapeTM.Code.computableInTimeAndSpace`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/CodeCompleteness.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/CodeCompleteness.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#computable-in-time-and-space).

## Deciding by a code is finite-state decidability

Let $c$ be a code with $k$ work tapes,
let $L$ be a set of binary words, and let $t$ and $s$ map binary words to natural numbers. If
the machine of $c$ decides $L$, that is, started on any binary word $w$ it halts with the one-bit
output $\mathrm{true}$ if $w \in L$ and $\mathrm{false}$ otherwise, and if on every binary word
$w$ it halts within $t(w)$ steps and visits at most $s(w)$ work-tape cells, then some binary
multi-tape machine with finitely many states decides $L$ within the same bounds.

Formalized by `Cslib.Turing.MultiTapeTM.Code.decidableInTimeAndSpace`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/CodeCompleteness.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/CodeCompleteness.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#decidable-in-time-and-space).

## The code of a finite-state binary machine

Let $M$ be a machine over the binary alphabet
with $k$ work tapes and a finite set of states $Q$, and let $e : Q \to \mathbb{N}$. The code of
$M$ with states numbered by $e$ has one table entry for each state $q \in Q$, symbol $a$ under
the input head and symbols $w$ under the $k$ work heads (each a bit or blank): its key is
$(e(q), a, w)$ and its value is the coded action of $M$ in state $q$ reading $a$ and $w$, with
the successor state numbered by $e$. The entries are listed in an unspecified order.

When $e$ is injective and sends the initial state of $M$ to $0$, the machine of this code
simulates $M$ up to the relabelling $e$.

Formalized by `Cslib.Turing.MultiTapeTM.Code.ofTM`, a definition declared in [CSLibExt/Computability/Machines/Turing/MultiTape/CodeCompleteness.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/CodeCompleteness.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#of-tm).

## The code of a machine takes its coded actions

Let $M$ be a binary multi-tape machine
with $k$ work tapes and a finite set of states $Q$, and let $e : Q \to \mathbb{N}$ be injective.
For every state $q \in Q$, every symbol $a$ under the input head and every tuple $w$ of symbols
under the $k$ work heads (each a bit or blank), the coded action of the code of $M$ under $e$ at
state $e(q)$ and symbols $a$, $w$ is the coding, with successor states numbered by $e$, of the
action of $M$ in state $q$ on $a$ and $w$.

Formalized by `Cslib.Turing.MultiTapeTM.Code.act_ofTM`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/CodeCompleteness.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/CodeCompleteness.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#act-of-tm).

## The code of a machine simulates it

Let $M$ be a machine over the binary alphabet with
$k$ work tapes, a finite set of states $Q$ and initial state $q_0$, and let $e : Q \to \mathbb{N}$
be injective with $e(q_0) = 0$. Then the machine of the code of $M$ with states numbered by $e$
simulates $M$ up to the relabelling $e$.

Formalized by `Cslib.Turing.MultiTapeTM.Code.isRelabelling_ofTM`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/CodeCompleteness.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/CodeCompleteness.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#is-relabelling-of-tm).

## Numbering a finite type from a chosen element

For every finite type $Q$ and every
$q_0 \in Q$ there is an injective map $e : Q \to \mathbb{N}$ with $e(q_0) = 0$.

Formalized by `Cslib.Turing.MultiTapeTM.Code.exists_injective_nat_eq_zero`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/CodeCompleteness.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/CodeCompleteness.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#exists-injective-nat-eq-zero).

## Every finite-state machine has a code

A binary machine with finitely many states is
simulated, up to an injective state relabelling, by the machine of some code.

Formalized by `Cslib.Turing.MultiTapeTM.Code.exists_code_isRelabelling`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/CodeCompleteness.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/CodeCompleteness.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#exists-code-is-relabelling).

## Computability over codes

Let $g : \alpha \to \beta$ be a function, let inputs in $\alpha$
and outputs in $\beta$ be encoded by injective maps into binary words, and let
$t, s : \alpha \to \mathbb{N}$. Say a machine computes $g$ within $t$ and $s$ when, started on the
encoding of any input $x$, it halts with the encoding of $g(x)$ as output, halts within $t(x)$
steps, and visits at most $s(x)$ work-tape cells. Then some binary multi-tape machine with
finitely many states computes $g$ within $t$ and $s$ if and only if, for some number $k$ of work
tapes, the machine of some code with $k$ work tapes computes $g$ within $t$ and $s$.

Formalized by `Cslib.Turing.MultiTapeTM.computableInTimeAndSpace_iff_exists_code`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/CodeCompleteness.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/CodeCompleteness.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#computable-in-time-and-space-iff-exists).

## Decidability over codes

Let $L$ be a set of binary words and let $t$ and $s$ map binary
words to natural numbers. Say a machine decides $L$ within $t$ and $s$ when, started on any
binary word $w$, it halts with the one-bit output $\mathrm{true}$ if $w \in L$ and
$\mathrm{false}$ otherwise, halts within $t(w)$ steps, and visits at most $s(w)$ work-tape cells.
Then some binary multi-tape machine with finitely many states decides $L$ within $t$ and $s$ if
and only if, for some number $k$ of work tapes, the machine of some code with $k$ work tapes
decides $L$ within $t$ and $s$.

Formalized by `Cslib.Turing.MultiTapeTM.decidableInTimeAndSpace_iff_exists_code`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/CodeCompleteness.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/CodeCompleteness.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#decidable-in-time-and-space-iff-exists-c).

## DTIME over codes

For every $t : \mathbb{N} \to \mathbb{N}$ and every language $L$ of
binary words, $L \in \mathsf{DTIME}(t)$ if and only if there are natural numbers $c_1, c_2, k$
and a code $c$ with $k$ work tapes such that the machine of $c$ decides $L$, on every input $w$
runs in time $c_1 t(|w|) + c_2$, and for some $s : \mathbb{N} \to \mathbb{N}$ on every input
$w$ runs in space $s(|w|)$.

Formalized by `Cslib.Turing.MultiTapeTM.mem_DTIME_iff_exists_code`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/CodeCompleteness.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/CodeCompleteness.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#mem-dtime-iff-exists-code).

## DSPACE over codes

For every $s : \mathbb{N} \to \mathbb{N}$ and every language $L$ of
binary words, $L \in \mathsf{DSPACE}(s)$ if and only if there are natural numbers $c_1, c_2, k$
and a code $c$ with $k$ work tapes such that the machine of $c$ decides $L$, on every input $w$
runs in space $c_1 s(|w|) + c_2$, and for some $t : \mathbb{N} \to \mathbb{N}$ on every input
$w$ runs in time $t(|w|)$.

Formalized by `Cslib.Turing.MultiTapeTM.mem_DSPACE_iff_exists_code`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/CodeCompleteness.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/MultiTape/CodeCompleteness.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html#mem-dspace-iff-exists-code).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Codes for multi-tape Turing machines](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-multi-tape-turing-machines)
