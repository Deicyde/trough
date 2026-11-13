---
declaration: section
origin: cited
lean: Cslib.Turing.Universal.HaltsWithin, Cslib.Turing.Universal.HaltsWithin.mono, Cslib.Turing.Universal.dom_eval_iff_exists_haltsWithin, Cslib.Turing.Universal.Code, Cslib.Turing.Universal.decodeStmt, Cslib.Turing.Universal.bitSym, Cslib.Turing.Universal.input, Cslib.Turing.Universal.Code.equivTable
statement: formalized
proof: formalized
---

# Codes for single-tape Turing machines

35 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-single-tape-turing-machines/index.html).

## Halting within a number of steps

## Bounded halting of a single-tape machine

A single-tape Turing machine $M$ halts within
$T$ steps on a word $l$ when, started in its initial state with $l$ on the tape and the head on
the first letter of $l$ (on a blank if $l$ is empty), it reaches after some $j \le T$ steps a
configuration that has no successor.

Formalized by `Cslib.Turing.Universal.HaltsWithin`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Code.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Code.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-single-tape-turing-machines/index.html#halts-within).

## Halting within a bound is monotone in the bound

For a single-tape Turing machine $M$,
a list $l$ of symbols and numbers $T \le T'$, if $M$ started on $l$ halts within $T$ steps,
then $M$ started on $l$ halts within $T'$ steps.

Formalized by `Cslib.Turing.Universal.HaltsWithin.mono`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/Code.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Code.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-single-tape-turing-machines/index.html#mono).

## Halting is halting within some number of steps

For a single-tape Turing machine $M$ and
an input word $l$, the evaluation of $M$ on $l$ is defined (that is, $M$ halts on $l$) if and only
if there is $T \in \mathbb{N}$ such that $M$ halts on $l$ within $T$ steps.

Formalized by `Cslib.Turing.Universal.dom_eval_iff_exists_haltsWithin`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/Code.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Code.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-single-tape-turing-machines/index.html#dom-eval-iff-exists-halts-within).

## Codes for single-tape machines

A code is a transition table: a finite list of rows, row
$q$ belonging to the state $q \in \mathbb{N}$, each a finite list of entries, entry $a$ of a row
belonging to the symbol $a \in \mathbb{N}$. The entry in row $q$ and column $a$ is either empty,
meaning that the machine halts, or a pair $(q', s)$ of natural numbers, meaning that the machine
enters the state $q'$ and does the action coded by $s$: $0$ moves left, $1$ moves right and
$b + 2$ writes $b$. A state or symbol outside the table halts the machine.

Formalized by `Cslib.Turing.Universal.Code`, a structure declared in [CSLibExt/Computability/Machines/Turing/Universal/Code.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Code.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-single-tape-turing-machines/index.html#code).

## Decoding an action

A natural number codes a statement of a single-tape Turing machine
with symbols in $\mathbb{N}$: $0$ moves the head left, $1$ moves the head right, and $a + 2$ writes
the symbol $a$.

Formalized by `Cslib.Turing.Universal.decodeStmt`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Code.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Code.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-single-tape-turing-machines/index.html#decode-stmt).

## Symbol of an input bit

The tape symbol of a bit $b$ is $1$ if $b$ is false and $2$ if $b$
is true; the symbol $0$ is the blank.

Formalized by `Cslib.Turing.Universal.bitSym`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Code.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Code.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-single-tape-turing-machines/index.html#bit-sym).

## Input word of a list of bits

The input word of a list of bits $x$ is the list of natural
numbers obtained from $x$ by replacing each bit by its symbol: $1$ for false and $2$ for true.

Formalized by `Cslib.Turing.Universal.input`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Code.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Code.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-single-tape-turing-machines/index.html#input).

## Single-tape codes as tables

Codes for single-tape machines correspond bijectively to
transition tables, that is, to lists of rows, each a list of entries that are either empty or a
pair of natural numbers: a code corresponds to its table.

Formalized by `Cslib.Turing.Universal.Code.equivTable`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Code.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Code.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-single-tape-turing-machines/index.html#equiv-table).

## Table lookup of a code

For a code $c$ and numbers $q$ and $a$, the lookup of $c$ at
state $q$ and symbol $a$ is the entry in row $q$, column $a$ of the table of $c$: either a pair
$(q', s)$ of a next state and an action code, or no entry (halt). It is no entry when the
table has no row $q$ or that row has no column $a$.

Formalized by `Cslib.Turing.Universal.Code.lookup`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Code.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Code.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-single-tape-turing-machines/index.html#lookup).

## The machine of a single-tape code

The machine of a code $c$ is the single-tape Turing
machine with states and symbols in $\mathbb{N}$ that, in state $q$ reading symbol $a$, halts if
the table lookup of $c$ at state $q$ and symbol $a$ has no entry, and otherwise, if the entry is
$(q', s)$, enters state $q'$ and does the action coded by $s$: $0$ moves left, $1$ moves right
and $a' + 2$ writes $a'$.

Formalized by `Cslib.Turing.Universal.Code.machine`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Code.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Code.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-single-tape-turing-machines/index.html#machine).

## States of a single-tape code

The set of states of a code $c$ is the finite set of natural
numbers consisting of the initial state $0$ and every state $q'$ such that some entry of the
table of $c$ is a pair $(q', s)$.

Formalized by `Cslib.Turing.Universal.Code.states`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Code.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Code.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-single-tape-turing-machines/index.html#states).

## Codes denote finite machines

The decoded machine is supported by the finite set of
states of its code.

Formalized by `Cslib.Turing.Universal.Code.supports_machine`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/Code.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Code.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-single-tape-turing-machines/index.html#supports-machine).

## Explicit configurations

A configuration of the simulation consists of a state
$q \in \mathbb{N}$, the list of the cells left of the head (nearest first), the symbol in the cell
under the head, and the list of the cells right of the head (nearest first); states and symbols
are natural numbers.

Formalized by `Cslib.Turing.Universal.Code.Cfg`, a structure declared in [CSLibExt/Computability/Machines/Turing/Universal/Code.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Code.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-single-tape-turing-machines/index.html#cfg).

## Configurations as tuples

Configurations correspond bijectively to tuples in
$\mathbb{N} \times \mathrm{List}(\mathbb{N}) \times \mathbb{N} \times \mathrm{List}(\mathbb{N})$:
a configuration corresponds to the tuple of its state, its cells left of the head, its cell under
the head and its cells right of the head.

Formalized by `Cslib.Turing.Universal.Code.Cfg.equivProd`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Code.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Code.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-single-tape-turing-machines/index.html#equiv-prod).

## TM0 configuration of a simulation configuration

The TM0 configuration of a configuration
$k$ of the simulation has the state of $k$, the cell under the head of $k$ as its head cell, and
as the halves of its tape left and right of the head the cells of $k$ left and right of the head,
nearest first, followed by infinitely many blanks.

Formalized by `Cslib.Turing.Universal.Code.Cfg.toTM0`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Code.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Code.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-single-tape-turing-machines/index.html#to-tm0).

## Acting on a configuration

Let $k$ be a configuration with left cells $L$ (nearest
first), head cell $h$ and right cells $R$ (nearest first), let $q'$ be a state and let $s$ be an
action code. Acting on $k$ with $q'$ and $s$ gives a configuration with state $q'$, as follows.
For $s = 0$ (move left), its head cell is the first entry of $L$, or the blank $0$ if $L$ is
empty, its left cells are $L$ without its first entry, and its right cells are $h$ followed by
$R$. For $s = 1$ (move right), its head cell is the first entry of $R$, or $0$ if $R$ is empty,
its right cells are $R$ without its first entry, and its left cells are $h$ followed by $L$. For
$s = a + 2$ (write $a$), its head cell is $a$ and its left and right cells are $L$ and $R$.

Formalized by `Cslib.Turing.Universal.Code.Cfg.act`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Code.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Code.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-single-tape-turing-machines/index.html#act).

## Output of a configuration

The output of a configuration $k$ is the list consisting of the
symbol under the head of $k$ followed by the cells right of the head (nearest first), with all
trailing blanks $0$ removed.

Formalized by `Cslib.Turing.Universal.Code.Cfg.output`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Code.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Code.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-single-tape-turing-machines/index.html#output).

## Initial configuration of the code simulation

The initial configuration of the
simulation on a list of bits $x$ has state $0$, an empty list of cells left of the head, the
head on the first symbol of the input word of $x$ (the blank $0$ if $x$ is empty), and the
remaining symbols of the input word, in order, right of the head.

Formalized by `Cslib.Turing.Universal.Code.init`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Code.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Code.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-single-tape-turing-machines/index.html#init).

## One step of a code

For a code $c$ and a configuration $k$ of the simulation, look up the
table entry of $c$ at the state of $k$ and the symbol under the head of $k$. If there is no entry,
the step is undefined (the machine halts); if the entry is $(q', s)$, the step is the
configuration obtained from $k$ by entering the state $q'$ and doing the action coded by $s$.

Formalized by `Cslib.Turing.Universal.Code.step`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Code.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Code.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-single-tape-turing-machines/index.html#step).

## One step of a code, or stay when halted

For a code $c$ and a configuration $k$ of the
simulation, the configuration after one step of $c$ from $k$ if that step is defined, and $k$
itself if $c$ halts at $k$.

Formalized by `Cslib.Turing.Universal.Code.stepOrStay`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Code.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Code.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-single-tape-turing-machines/index.html#step-or-stay).

## Clocked configuration of a code

For a code $c$, a list of bits $x$ and $T \in \mathbb{N}$,
the configuration of $c$ on $x$ after $T$ steps is obtained from the initial configuration on $x$
by applying $T$ times the step of $c$, where a step leaves a halted configuration unchanged. It is
the configuration after $T$ steps, or the halting configuration if the machine halts earlier.

Formalized by `Cslib.Turing.Universal.Code.cfgAfter`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Code.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Code.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-single-tape-turing-machines/index.html#cfg-after).

## The clocked evaluator

Given a code $c$, a list of bits $x$ and a clock $T \in \mathbb{N}$,
run the simulation of $c$ on $x$ for at most $T$ steps. If it halts within $T$ steps, the result
is the output of the halting configuration: the tape from the head rightwards, with trailing
blanks dropped. Otherwise there is no result.

Formalized by `Cslib.Turing.Universal.Code.evalSteps`, a definition declared in [CSLibExt/Computability/Machines/Turing/Universal/Code.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Code.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-single-tape-turing-machines/index.html#eval-steps).

## Explicit steps agree with the decoded machine

For every code $c$ and every configuration
$k$ of the simulation, the decoded TM0 machine of $c$ halts at the TM0 configuration of $k$
exactly when the step of $c$ from $k$ is undefined, and otherwise its step from the TM0
configuration of $k$ is the TM0 configuration of the step of $c$ from $k$.

Formalized by `Cslib.Turing.Universal.Code.step_toTM0`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/Code.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Code.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-single-tape-turing-machines/index.html#step-to-tm0).

## The explicit initial configuration is the machine's

For a list of bits $x$, the initial
configuration of the simulation on $x$, read as a configuration of a single-tape machine, is the
initial configuration of a single-tape machine on the input word of $x$.

Formalized by `Cslib.Turing.Universal.Code.init_toTM0`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/Code.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Code.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-single-tape-turing-machines/index.html#init-to-tm0).

## The output of a configuration as a Mathlib half-tape

For every explicit configuration
$k$, the half-tape of the Mathlib configuration of $k$ from the head rightwards (the cell under
the head followed by the cells to its right) is the output of $k$, read with blanks beyond its
end.

Formalized by `Cslib.Turing.Universal.Code.right₀_toTM0`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/Code.lean, line 264](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Code.lean#L264). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-single-tape-turing-machines/index.html#right-to-tm0).

## Iterated steps of the decoded machine

Let $c$ be a code, $n \in \mathbb{N}$ and $k$
an explicit configuration. Run the machine of $c$ for $n$ steps from the Mathlib configuration
of $k$, and run the explicit simulation of $c$ for $n$ steps from $k$, where a run that reaches
a configuration without a successor before completing $n$ steps has no result. Then the first
run has a result exactly when the second does, and its result is the Mathlib configuration of
the result of the second.

Formalized by `Cslib.Turing.Universal.Code.iterate_step_toTM0`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/Code.lean, line 306](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Code.lean#L306). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-single-tape-turing-machines/index.html#iterate-step-to-tm0).

## Bounded halting of a decoded machine through its simulation

For a code $c$, a list of
bits $x$ and $T \in \mathbb{N}$, the decoded machine of $c$ halts within $T$ steps on the input
word of $x$ if and only if the explicit simulation of $c$, started from the initial configuration
on $x$, reaches after some $j \le T$ steps a configuration that has no successor step.

Formalized by `Cslib.Turing.Universal.Code.haltsWithin_machine_iff`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/Code.lean, line 313](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Code.lean#L313). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-single-tape-turing-machines/index.html#halts-within-machine-iff).

## Definedness of the clocked evaluator

For a code $c$, a list of bits $x$ and a clock
$T \in \mathbb{N}$, the clocked evaluator of $c$ on $x$ with clock $T$ returns a value if and
only if the simulation of $c$ has no step from the configuration after $T$ clocked steps on $x$
(the configuration after $T$ steps, or the halting configuration if the machine halts
earlier).

Formalized by `Cslib.Turing.Universal.Code.isSome_evalSteps_iff_step_eq_none`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/Code.lean, line 350](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Code.lean#L350). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-single-tape-turing-machines/index.html#is-some-eval-steps-iff-step-eq-none).

## Clocked halting

For a code $c$, a list of bits $x$ and a clock $T \in \mathbb{N}$,
the clocked evaluator of $c$ on $x$ with clock $T$ returns a value if and only if the machine
of $c$, started on the input word of $x$, halts within $T$ steps.

Formalized by `Cslib.Turing.Universal.Code.isSome_evalSteps_iff`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/Code.lean, line 357](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Code.lean#L357). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-single-tape-turing-machines/index.html#is-some-eval-steps-iff).

## Characterization of clocked results

For a code $c$, a list of bits $x$, a clock
$T \in \mathbb{N}$ and a list $l$ of natural numbers, the clocked evaluator returns $l$ on $c$,
$x$ and $T$ if and only if the configuration of $c$ after $T$ clocked steps on $x$ has no
successor step and its output is $l$.

Formalized by `Cslib.Turing.Universal.Code.evalSteps_eq_some_iff_output`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/Code.lean, line 375](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Code.lean#L375). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-single-tape-turing-machines/index.html#eval-steps-eq-some-iff-output).

## Monotonicity of the single-tape clocked evaluator

Let $c$ be a code for a single-tape
machine, $x$ a list of bits, $l$ a list of natural numbers and $T \le T'$ natural numbers. If the
clocked evaluator returns $l$ on $c$ and $x$ with clock $T$, then it also returns $l$ with clock
$T'$.

Formalized by `Cslib.Turing.Universal.Code.evalSteps_mono`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/Code.lean, line 381](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Code.lean#L381). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-single-tape-turing-machines/index.html#eval-steps-mono).

## Clocked results agree with the machine's semantics

Let $c$ be a code, $x$ a list of
bits, $T$ a natural number and $l$ a list of natural numbers. If the clocked evaluator, running
$c$ on $x$ for at most $T$ steps, returns $l$, then the decoded machine of $c$, started on the
input word of $x$, halts, and the tape from its head rightwards in the halting configuration is
$l$ followed by blanks.

Formalized by `Cslib.Turing.Universal.Code.eval_eq_some_of_evalSteps_eq_some`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/Code.lean, line 396](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Code.lean#L396). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-single-tape-turing-machines/index.html#eval-eq-some-of-eval-steps-eq-some).

## Unclocked halting

For a code $c$ and a list of bits $x$, the machine decoded from $c$ halts
on the input word of $x$ if and only if there is a clock $T \in \mathbb{N}$ for which the clocked
evaluator of $c$ on $x$ with clock $T$ returns a result.

Formalized by `Cslib.Turing.Universal.Code.dom_eval_iff_exists_isSome_evalSteps`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/Code.lean, line 415](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Code.lean#L415). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-single-tape-turing-machines/index.html#dom-eval-iff-exists-is-some-eval-steps).

## Universality of codes

**Universality of codes**, for machines that read bit inputs. Let $M$ be a single-tape
Turing machine with a finite alphabet $\Gamma$ and a finite set of states that contains the
initial state and is closed under the transitions of $M$, and let $\iota$ be an injective map
from the bits to $\Gamma$ whose values are not the blank. Then there are a code $c$ and an
injective map $f$ from $\Gamma$ to the natural numbers, sending the blank to $0$ and each
$\iota(b)$ to the symbol of the bit $b$, such that for every word $l$ over $\Gamma$, writing
$f(l)$ for the word obtained by applying $f$ to each letter: the decoded machine of $c$ halts on
$f(l)$ exactly when $M$ halts on $l$, and its result (the tape from the head rightwards when it
halts) is then the result of $M$ on $l$ with $f$ applied to each cell; and for every
$T \in \mathbb{N}$, the decoded machine of $c$ halts within $T$ steps on $f(l)$ if and only if
$M$ halts within $T$ steps on $l$.

(So the alphabet has at least three symbols; a machine over a smaller alphabet cannot read a bit
input.)

Formalized by `Cslib.Turing.Universal.Code.exists_code`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/Code.lean, line 447](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Code.lean#L447). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-single-tape-turing-machines/index.html#exists-code).

## The clocked evaluator is primitive recursive

The clocked evaluator is primitive
recursive in the code, the input and the clock.

Formalized by `Cslib.Turing.Universal.Code.primrec_evalSteps`, a theorem declared in [CSLibExt/Computability/Machines/Turing/Universal/Code.lean, line 632](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/Universal/Code.lean#L632). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-single-tape-turing-machines/index.html#primrec-eval-steps).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Codes for single-tape Turing machines](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-single-tape-turing-machines/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/turing-machines/universal-machines/codes-for-single-tape-turing-machines)
