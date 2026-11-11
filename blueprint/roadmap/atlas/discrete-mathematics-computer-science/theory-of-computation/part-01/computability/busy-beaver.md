---
declaration: section
origin: cited
lean: Cslib.BusyBeaver.Move, Cslib.BusyBeaver.Move.shift, Cslib.BusyBeaver.Machine, Cslib.BusyBeaver.Config, Cslib.BusyBeaver.step, Cslib.BusyBeaver.initialState, Cslib.BusyBeaver.initial, Cslib.BusyBeaver.run
statement: formalized
---

# Busy beaver

50 results, 44 proved and 6 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html).

## Head movement

A head movement is one of exactly two directions: left or right.

Formalized by `Cslib.BusyBeaver.Move`, an inductive type declared in [CSLibExt/Computability/BusyBeaver.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/BusyBeaver.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#move).

## Head displacement

The displacement of a head movement is $-1$ for a move to the left
and $1$ for a move to the right.

Formalized by `Cslib.BusyBeaver.Move.shift`, a definition declared in [CSLibExt/Computability/BusyBeaver.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/BusyBeaver.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#shift).

## Busy Beaver machine

A Busy Beaver machine with $n$ working states is a transition table
that assigns to each of the $n$ working states and each read symbol in $\{0, 1\}$ a symbol in
$\{0, 1\}$ to write, a head movement (left or right), and a next state, which is either one of
the $n$ working states or the halt state.

The write and move of a halting transition are still performed, and the halting step counts
toward the runtime.

Formalized by `Cslib.BusyBeaver.Machine`, an abbreviation declared in [CSLibExt/Computability/BusyBeaver.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/BusyBeaver.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#machine).

## Busy Beaver machine configuration

A configuration of an $n$-state machine consists of a
current state, which is either one of the $n$ working states or the halt state, an integer head
position, and a tape assigning a symbol in $\{0, 1\}$ to every integer cell.

Formalized by `Cslib.BusyBeaver.Config`, a structure declared in [CSLibExt/Computability/BusyBeaver.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/BusyBeaver.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#config).

## One step of a Busy Beaver machine

Let $M$ be a machine with $n$ working states and let
$c$ be a configuration with head position $h$. If $c$ is halted, the step leaves $c$ unchanged.
Otherwise let $q$ be the current state, let $a$ be the symbol in cell $h$, and let
$M(q, a) = (b, d, q')$. The step writes $b$ in cell $h$, leaving every other cell unchanged, moves
the head to $h - 1$ if $d$ is left and to $h + 1$ if $d$ is right, and passes to the state $q'$,
which may be the halt state.

Formalized by `Cslib.BusyBeaver.step`, a definition declared in [CSLibExt/Computability/BusyBeaver.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/BusyBeaver.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#step).

## Initial state

For a machine with $n$ working states, the initial state is state $0$ when
$n > 0$, and the halt state when $n = 0$.

Formalized by `Cslib.BusyBeaver.initialState`, a definition declared in [CSLibExt/Computability/BusyBeaver.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/BusyBeaver.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#initial-state).

## Initial configuration of a Busy Beaver machine

The initial configuration of a machine
with $n$ working states is in the initial state (state $0$, or the halt state when $n = 0$), with
the head at position $0$ and every tape cell blank, that is, holding the symbol $0$.

Formalized by `Cslib.BusyBeaver.initial`, a definition declared in [CSLibExt/Computability/BusyBeaver.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/BusyBeaver.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#initial).

## Configuration after $t$ steps

For a Busy Beaver machine $M$ and $t \in \mathbb{N}$,
the configuration of $M$ after $t$ steps is the result of applying the one-step map of $M$
$t$ times to the initial configuration on the blank tape.

Formalized by `Cslib.BusyBeaver.run`, a definition declared in [CSLibExt/Computability/BusyBeaver.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/BusyBeaver.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#run).

## Halting within $t$ steps

A Busy Beaver machine $M$ with $n$ working states halts within
$t$ steps when the configuration reached after running $M$ for $t$ steps from the initial
blank-tape configuration is in the halt state.

Formalized by `Cslib.BusyBeaver.HaltsWithin`, a definition declared in [CSLibExt/Computability/BusyBeaver.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/BusyBeaver.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#halts-within).

## Halting on the blank tape

A Busy Beaver machine $M$ halts when there is a number of steps
$t$ such that $M$ halts within $t$ steps, that is, when $M$ started from the initial
blank-tape configuration eventually reaches the halt state.

Formalized by `Cslib.BusyBeaver.Halts`, a definition declared in [CSLibExt/Computability/BusyBeaver.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/BusyBeaver.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#halts).

## Halting time

For an $n$-state machine $M$ that halts on the blank tape, its
halting time is the least $t$ such that $M$, started on the blank tape, is in the halt
state after $t$ steps.

Formalized by `Cslib.BusyBeaver.haltTime`, a definition declared in [CSLibExt/Computability/BusyBeaver.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/BusyBeaver.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#halt-time).

## Head displacement bound

For every $n$-state Busy Beaver machine $M$ and every
$t \in \mathbb{N}$, if $h \in \mathbb{Z}$ is the head position after $M$ has run for $t$ steps
from the initial configuration on the blank tape, then $|h| \le t$.

Formalized by `Cslib.BusyBeaver.abs_head_le`, a theorem declared in [CSLibExt/Computability/BusyBeaver.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/BusyBeaver.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#abs-head-le).

## Cells far from the origin stay blank

Let $M$ be a machine with $n$ working states,
started in cell $0$ on the blank tape. For every $t \in \mathbb{N}$ and every cell
$i \in \mathbb{Z}$ with $|i| > t$, the symbol in cell $i$ after $t$ steps is $0$.

Formalized by `Cslib.BusyBeaver.tape_eq_zero_of_abs_gt`, a theorem declared in [CSLibExt/Computability/BusyBeaver.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/BusyBeaver.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#tape-eq-zero-of-abs-gt).

## Number of ones after $t$ steps

For a Busy Beaver machine $M$ and $t \in \mathbb{N}$,
the number of ones of $M$ after $t$ steps is the number of cells $i \in \mathbb{Z}$ with
$-t \le i \le t$ that hold the symbol $1$ in the configuration of $M$ after $t$ steps, started
on the blank tape.

Every one on the tape after $t$ steps lies in this window, since the head moves at most one
cell per step.

Formalized by `Cslib.BusyBeaver.onesAt`, a definition declared in [CSLibExt/Computability/BusyBeaver.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/BusyBeaver.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#ones-at).

## After $t$ steps, every one lies within distance $t$ of the origin

For every Busy Beaver
machine $M$, every $t \in \mathbb{N}$ and every cell $i \in \mathbb{Z}$, if cell $i$ holds the
symbol $1$ after $M$ runs for $t$ steps from the initial blank-tape configuration, then
$-t \le i \le t$.

Formalized by `Cslib.BusyBeaver.mem_window_of_tape_eq_one`, a theorem declared in [CSLibExt/Computability/BusyBeaver.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/BusyBeaver.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#mem-window-of-tape-eq-one).

## The number of ones grows by at most one per step

For every Busy Beaver machine $M$
and every $t \in \mathbb{N}$, the number of ones of $M$ after $t + 1$ steps is at most the
number of ones of $M$ after $t$ steps plus $1$.

Formalized by `Cslib.BusyBeaver.onesAt_succ_le`, a theorem declared in [CSLibExt/Computability/BusyBeaver.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/BusyBeaver.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#ones-at-succ-le).

## At most $t$ ones after $t$ steps

For every Busy Beaver machine $M$ and every
$t \in \mathbb{N}$, the number of ones of $M$ after $t$ steps is at most $t$.

Formalized by `Cslib.BusyBeaver.onesAt_le_steps`, a theorem declared in [CSLibExt/Computability/BusyBeaver.lean, line 328](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/BusyBeaver.lean#L328). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#ones-at-le-steps).

## Runtime of a Busy Beaver machine

For a machine $M$ with $n$ working states, the runtime
of $M$ is its halting time on the blank tape if $M$ halts, and $0$ if $M$ does not halt. This is
the quantity whose maximum over all $n$-state machines is the shift function $S(n)$.

Formalized by `Cslib.BusyBeaver.stepsOf`, a definition declared in [CSLibExt/Computability/BusyBeaver.lean, line 337](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/BusyBeaver.lean#L337). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#steps-of).

## Score of a machine

For a Busy Beaver machine $M$: if $M$ halts on the blank tape,
with halting time $T$, its score is the number of ones of $M$ after $T$ steps; if $M$ does not
halt, its score is $0$.

Formalized by `Cslib.BusyBeaver.scoreOf`, a definition declared in [CSLibExt/Computability/BusyBeaver.lean, line 343](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/BusyBeaver.lean#L343). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#score-of).

## Busy Beaver shift function

For $n \in \mathbb{N}$, Rado's shift function $S(n)$ is the
largest halting time of an $n$-state two-symbol machine that halts when started on the blank
tape; machines that do not halt contribute $0$.

Formalized by `Cslib.BusyBeaver.busyBeaverSteps`, a definition declared in [CSLibExt/Computability/BusyBeaver.lean, line 349](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/BusyBeaver.lean#L349). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#busy-beaver-steps).

## Busy Beaver score function

For $n \in \mathbb{N}$, Rado's score function $\Sigma(n)$ is
the largest number of ones left on the tape, at its halting time, by an $n$-state two-symbol
machine that halts when started on the blank tape; machines that do not halt contribute $0$.

Formalized by `Cslib.BusyBeaver.busyBeaverOnes`, a definition declared in [CSLibExt/Computability/BusyBeaver.lean, line 354](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/BusyBeaver.lean#L354). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#busy-beaver-ones).

## The Busy Beaver score is at most the shift

For every $n \in \mathbb{N}$, Rado's score
function $\Sigma$ and Rado's shift function $S$ satisfy $\Sigma(n) \le S(n)$: the largest number
of ones left on the tape by a halting $n$-state two-symbol machine started on the blank tape is
at most the largest halting time of such a machine.

Formalized by `Cslib.BusyBeaver.busyBeaverOnes_le_steps`, a theorem declared in [CSLibExt/Computability/BusyBeaver.lean, line 391](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/BusyBeaver.lean#L391). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#busy-beaver-ones-le-steps).

## The shift function is attained

Let $S(n)$ be Rado's shift function, the largest
runtime of an $n$-state machine, where the runtime of a machine is its halting time on the
blank tape if it halts and $0$ otherwise. For every $n$, some $n$-state machine $M$ has
runtime equal to $S(n)$. Thus $S(n)$ is the halting time of a halting $n$-state machine,
or $S(n) = 0$.

Formalized by `Cslib.BusyBeaver.exists_stepsOf_eq`, a theorem declared in [CSLibExt/Computability/BusyBeaver.lean, line 399](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/BusyBeaver.lean#L399). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#exists-steps-of-eq).

## The score function is attained

Let $\Sigma(n)$ be the busy beaver score function,
the largest score of an $n$-state machine, where the score of a machine is the number of
ones on its final tape if it halts on the blank tape and $0$ otherwise. For every $n$, some
$n$-state machine $M$ has score equal to $\Sigma(n)$. Thus $\Sigma(n)$ is the number of
ones left by a halting $n$-state machine, or $\Sigma(n) = 0$.

Formalized by `Cslib.BusyBeaver.exists_scoreOf_eq`, a theorem declared in [CSLibExt/Computability/BusyBeaver.lean, line 408](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/BusyBeaver.lean#L408). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#exists-score-of-eq).

## Embedding a machine into one more state

An $n$-state machine $M$ is embedded
into $n + 1$ states as follows. In a working state $q < n$ reading a symbol $s$, the new
machine writes the symbol, makes the move and enters the next state that $M$ prescribes
in state $q$ on $s$, halting when $M$ halts. In the new state $n$ it writes $0$, moves
left and halts, whatever it reads.

No transition enters state $n$. So for $n \ge 1$, where the machine starts in state
$0 < n$, the new state is never reached; for $n = 0$ the new state is the start state.

Formalized by `Cslib.BusyBeaver.embedMachine`, a definition declared in [CSLibExt/Computability/BusyBeaver.lean, line 418](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/BusyBeaver.lean#L418). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#embed-machine).

## Embedding a configuration into one more state

For a configuration $c$ of an
$n$-state machine, its embedding is the configuration for $n + 1$ states with the same
head position and the same tape as $c$. Its state is the state of $c$, where a working
state $q \in \{0, \dots, n - 1\}$ stays $q$ and the halt state stays the halt state.

Formalized by `Cslib.BusyBeaver.embedConfig`, a definition declared in [CSLibExt/Computability/BusyBeaver.lean, line 426](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/BusyBeaver.lean#L426). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#embed-config).

## A one-state machine that stays in its state on a blank never halts

Let $M$ be a Busy Beaver
machine with a single working state $0$. If the transition of $M$ from state $0$ on reading the
blank symbol $0$ has next state $0$, then $M$ does not halt.

Such a machine marches in one direction forever: at every step the head is on a previously
unvisited blank cell.

Formalized by `Cslib.BusyBeaver.not_halts_of_one_state_march`, a theorem declared in [CSLibExt/Computability/BusyBeaver.lean, line 604](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/BusyBeaver.lean#L604). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#not-halts-of-one-state-march).

## One-state machines halt within one step

Every halting one-state machine halts
within one step.

Formalized by `Cslib.BusyBeaver.haltsWithin_one_of_halts`, a theorem declared in [CSLibExt/Computability/BusyBeaver.lean, line 677](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/BusyBeaver.lean#L677). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#halts-within-one-of-halts).

## Machine code

The code of a machine $M$ with $n$ working states is the natural number that
encodes the pair $(n, i)$ under a fixed pairing bijection
$\mathbb{N} \times \mathbb{N} \to \mathbb{N}$, where $i$ is the index of $M$ in a fixed enumeration
of the finitely many machines with $n$ working states.

Formalized by `Cslib.BusyBeaver.machineCode`, a definition declared in [CSLibExt/Computability/BusyBeaver.lean, line 747](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/BusyBeaver.lean#L747). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#machine-code).

## Sentence codes

The sentence code with tag $a$ and payload $p$ is the natural number
$4p + a$. The tags in use are $0$ (the coded machine halts), $1$ (the coded machine does not
halt), $2$ (the false sentence), and $3$ with payload the pairing code of $n$ and $B$ (every
halting $n$-state machine halts within $B$ steps).

Sentences are natural numbers rather than propositions, so provability does not collapse under
propositional extensionality.

Formalized by `Cslib.BusyBeaver.sentenceCode`, a definition declared in [CSLibExt/Computability/BusyBeaver.lean, line 756](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/BusyBeaver.lean#L756). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#sentence-code).

## Halting sentence of a machine

For an $n$-state machine $M$, the halting sentence
of $M$ is the sentence code with tag $0$ and payload the code of $M$. It stands for
"$M$ halts on the blank tape"; this meaning comes from soundness hypotheses on a
theory, not from the code itself.

Formalized by `Cslib.BusyBeaver.haltsSentence`, a definition declared in [CSLibExt/Computability/BusyBeaver.lean, line 760](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/BusyBeaver.lean#L760). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#halts-sentence).

## Non-halting sentence of a machine

For a Busy Beaver machine $M$, the non-halting
sentence of $M$ is the sentence code with tag $1$ whose payload is the code of $M$; it stands
for "$M$ does not halt on the blank tape".

Formalized by `Cslib.BusyBeaver.notHaltsSentence`, a definition declared in [CSLibExt/Computability/BusyBeaver.lean, line 764](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/BusyBeaver.lean#L764). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#not-halts-sentence).

## The false sentence

The false sentence is the sentence code with tag $2$ and
payload $0$, that is, the natural number $2$.

Formalized by `Cslib.BusyBeaver.falseSentence`, a definition declared in [CSLibExt/Computability/BusyBeaver.lean, line 768](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/BusyBeaver.lean#L768). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#false-sentence).

## Runtime-bound sentence

For natural numbers $n$ and $B$, the runtime-bound sentence is
the sentence code with tag $3$ and payload $\langle n, B \rangle$, the pairing of $n$ and $B$;
as a number it equals $4 \langle n, B \rangle + 3$.

Its intended reading is "every halting $n$-state machine halts within $B$ steps"; this meaning
is assigned only through separate soundness hypotheses.

Formalized by `Cslib.BusyBeaver.boundSentence`, a definition declared in [CSLibExt/Computability/BusyBeaver.lean, line 773](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/BusyBeaver.lean#L773). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#bound-sentence).

## Formal theory

A formal theory is given by a provability predicate on sentence
codes, which are natural numbers: for each natural number it specifies whether that
sentence code is provable in the theory.

The theory is an abstract parameter, with ZFC as the intended instance. No meaning is
attached to sentence codes here; the halting, non-halting, false and runtime-bound
sentences receive their meaning through separate soundness hypotheses.

Formalized by `Cslib.BusyBeaver.FormalTheory`, a structure declared in [CSLibExt/Computability/BusyBeaver.lean, line 798](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/BusyBeaver.lean#L798). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#formal-theory).

## Consistent formal theory

A formal theory $T$ is consistent when $T$ does not prove the
false sentence.

Formalized by `Cslib.BusyBeaver.Consistent`, a definition declared in [CSLibExt/Computability/BusyBeaver.lean, line 803](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/BusyBeaver.lean#L803). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#consistent).

## Soundness for halting sentences

A formal theory $T$ is sound for halting sentences
when, for every $n$ and every Busy Beaver machine $M$ with $n$ states, if $T$ proves the
halting sentence of $M$ then $M$ halts on the blank tape, and if $T$ proves the non-halting
sentence of $M$ then $M$ does not halt on the blank tape.

Formalized by `Cslib.BusyBeaver.SoundForHalting`, a definition declared in [CSLibExt/Computability/BusyBeaver.lean, line 809](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/BusyBeaver.lean#L809). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#sound-for-halting).

## Theories deciding halting at a state count

A formal theory $T$ decides halting for
$n$-state machines when, for every $n$-state machine $M$, $T$ proves the halting sentence of $M$
or $T$ proves the non-halting sentence of $M$.

Formalized by `Cslib.BusyBeaver.DecidesHalting`, a definition declared in [CSLibExt/Computability/BusyBeaver.lean, line 816](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/BusyBeaver.lean#L816). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#decides-halting).

## First undecidable number of states

For a formal theory $T$, the first
undecidable number of states is the least $n$ such that $T$ does not decide halting for
all $n$-state machines, that is, there is an $n$-state machine $M$ for which $T$ proves
neither the halting sentence nor the non-halting sentence of $M$. It is $0$ when there
is no such $n$.

For ZFC this is catalogue constant 14a; the junk value $0$ covers a theory that decides
halting at every number of states.

Formalized by `Cslib.BusyBeaver.firstUndecidable`, a definition declared in [CSLibExt/Computability/BusyBeaver.lean, line 824](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/BusyBeaver.lean#L824). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#first-undecidable).

## Decidability through five states and the first undecidable size

If a formal theory
$T$ decides halting for $n$-state machines for every $n \le 5$, and fails to decide halting for
$n$-state machines for some $n$, then the first undecidable size of $T$ is at least $6$.

This is the shape of the catalogue lower bound from the determination of the five-state Busy
Beaver value.

Formalized by `Cslib.BusyBeaver.six_le_firstUndecidable_of_decides_le_five`, a theorem declared in [CSLibExt/Computability/BusyBeaver.lean, line 840](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/BusyBeaver.lean#L840). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#six-le-first-undecidable-of-decides-le-f).

## A consistency-search machine blocks decidability at its size

Let $T$ be a formal theory
and $M$ a Busy Beaver machine with $n$ working states. Suppose that $M$ halts if and only if $T$
proves the false sentence, that $M$ halts whenever $T$ proves the halting sentence of $M$, that
$T$ is consistent, and that $T$ does not prove the non-halting sentence of $M$. Then $T$ does not
decide halting for all machines with $n$ working states.

The last hypothesis is the Gödel second-incompleteness content when $T$ is ZFC.

Formalized by `Cslib.BusyBeaver.not_decides_of_consistency_machine`, a theorem declared in [CSLibExt/Computability/BusyBeaver.lean, line 855](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/BusyBeaver.lean#L855). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#not-decides-of-consistency-machine).

## Decidability of halting passes to fewer states

Let $T$ be a formal theory such that, for
every $m$ and every Busy Beaver machine $M$ with $m$ working states, if $T$ proves the halting
sentence of the embedding of $M$ into $m + 1$ states then $T$ proves the halting sentence of $M$,
and if $T$ proves the non-halting sentence of the embedding of $M$ into $m + 1$ states then $T$
proves the non-halting sentence of $M$. Then for every $n$, if $T$ decides halting for machines
with $n + 1$ working states, it decides halting for machines with $n$ working states.

The transport hypotheses are where a real theory would rewrite a proof about the embedded machine
into a proof about the original machine; they are stated explicitly because provability of one
sentence code does not formally imply provability of another.

Formalized by `Cslib.BusyBeaver.decidesHalting_of_succ`, a theorem declared in [CSLibExt/Computability/BusyBeaver.lean, line 873](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/BusyBeaver.lean#L873). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#decides-halting-of-succ).

## Proof-checker presentation of a ZFC-like theory

A ZFC-like presentation consists of a
formal theory $T$, given by a provability predicate on sentence codes in $\mathbb{N}$, together
with a Boolean proof checker $\mathrm{check}(p, s)$ on pairs of natural numbers, such that the
following hold. A sentence code $s$ is provable in $T$ if and only if $\mathrm{check}(p, s)$ is true
for some $p \in \mathbb{N}$. $T$ is sound for halting: for every machine $M$, if $T$ proves the
halting sentence of $M$ then $M$ halts on the blank tape, and if $T$ proves the non-halting
sentence of $M$ then $M$ does not halt. For every machine $M$, if $M$ has halted within $t$ steps
for some $t$, then $T$ proves the halting sentence of $M$. Write $S(n)$ for the Busy Beaver shift
function, the largest halting time of a halting machine with $n$ working states, and call the
bound sentence for $n$ and $B$ the sentence code saying that every halting machine with $n$
working states halts within $B$ steps. For every $n \le 5$, $T$ proves the bound sentence for $n$
and $S(n)$. Whenever $T$ proves the bound sentence for $n$ and $B$, every halting machine with $n$
working states halts within $B$ steps. Whenever $T$ proves the bound sentence for $n$ and $B$ and a
machine $M$ with $n$ working states has not halted within $B$ steps, $T$ proves the non-halting
sentence of $M$.

No concrete syntax or proof checker for ZFC is given, and no presentation of ZFC is constructed;
the intended instance is ZFC with its standard proof checker. The state counts for
consistency-search machines in the literature depend on specific checker implementations and are
not asserted for arbitrary presentations.

Formalized by `Cslib.BusyBeaver.ZFCPresentation`, a structure declared in [CSLibExt/Computability/BusyBeaver.lean, line 900](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/BusyBeaver.lean#L900). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#zfcpresentation).

## ZFC-like theories decide halting through five states

For every ZFC-like presentation
$Z$ and every $n \le 5$, the theory presented by $Z$ decides halting for $n$-state machines: for
every $n$-state machine it proves the machine's halting sentence or its non-halting sentence.

Proof idea: let $S$ be Rado's shift function; $Z$ proves the runtime bound $S(n)$ for
halting $n$-state machines. Run each machine for $S(n)$ steps; if it has halted, the
computation verifies, and if it has not, the bound derives its non-halting sentence.

Formalized by `Cslib.BusyBeaver.ZFCPresentation.decidesHalting_le_five`, a theorem declared in [CSLibExt/Computability/BusyBeaver.lean, line 933](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/BusyBeaver.lean#L933). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#decides-halting-le-five).

## Three-state Busy Beaver shift value

Rado's shift function $S$ satisfies $S(3) = 21$:
among the two-symbol Busy Beaver machines with $3$ working states that halt when started on the
blank tape, the largest halting time is $21$.

## Sources

- Lin--Radó (1965), determination of `S(3) = 21`.

Stated but not proved: `Cslib.BusyBeaverWanted.busyBeaverSteps_three_wanted` is written with `theorem_wanted` in [WantedExt/TheoryOfComputation/BusyBeaverWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/TheoryOfComputation/BusyBeaverWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#busy-beaver-steps-three-wanted).

## Three-state Busy Beaver score value

Rado's score function $\Sigma$ satisfies
$\Sigma(3) = 6$: among the two-symbol Busy Beaver machines with $3$ working states that halt when
started on the blank tape, the largest number of ones left on the tape at the halting time is $6$.

## Sources

- Lin--Radó (1965), determination of `Σ(3) = 6`.

Stated but not proved: `Cslib.BusyBeaverWanted.busyBeaverOnes_three_wanted` is written with `theorem_wanted` in [WantedExt/TheoryOfComputation/BusyBeaverWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/TheoryOfComputation/BusyBeaverWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#busy-beaver-ones-three-wanted).

## Four-state Busy Beaver shift value

Rado's shift function $S$ satisfies $S(4) = 107$:
among the two-symbol Busy Beaver machines with $4$ working states that halt when started on the
blank tape, the largest halting time is $107$.

## Sources

- Brady (1983), determination of `S(4) = 107`.

Stated but not proved: `Cslib.BusyBeaverWanted.busyBeaverSteps_four_wanted` is written with `theorem_wanted` in [WantedExt/TheoryOfComputation/BusyBeaverWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/TheoryOfComputation/BusyBeaverWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#busy-beaver-steps-four-wanted).

## Four-state Busy Beaver score value

Rado's score function $\Sigma$ satisfies
$\Sigma(4) = 13$: among the two-symbol Busy Beaver machines with $4$ working states that halt when
started on the blank tape, the largest number of ones left on the tape at the halting time is $13$.

## Sources

- Brady (1983), determination of `Σ(4) = 13`.

Stated but not proved: `Cslib.BusyBeaverWanted.busyBeaverOnes_four_wanted` is written with `theorem_wanted` in [WantedExt/TheoryOfComputation/BusyBeaverWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/TheoryOfComputation/BusyBeaverWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#busy-beaver-ones-four-wanted).

## Five-state Busy Beaver shift value

Rado's shift function $S$ satisfies
$S(5) = 47176870$: among the two-symbol Busy Beaver machines with $5$ working states that halt
when started on the blank tape, the largest halting time is $47176870$.

## Sources

- Busy Beaver Challenge (2025), determination of `S(5) = 47176870`.

Stated but not proved: `Cslib.BusyBeaverWanted.busyBeaverSteps_five_wanted` is written with `theorem_wanted` in [WantedExt/TheoryOfComputation/BusyBeaverWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/TheoryOfComputation/BusyBeaverWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#busy-beaver-steps-five-wanted).

## Five-state Busy Beaver score value

Rado's score function $\Sigma$ satisfies
$\Sigma(5) = 4098$: among the two-symbol Busy Beaver machines with $5$ working states that halt
when started on the blank tape, the largest number of ones left on the tape at the halting time
is $4098$.

## Sources

- Busy Beaver Challenge (2025), determination of `Σ(5) = 4098`.

Stated but not proved: `Cslib.BusyBeaverWanted.busyBeaverOnes_five_wanted` is written with `theorem_wanted` in [WantedExt/TheoryOfComputation/BusyBeaverWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/TheoryOfComputation/BusyBeaverWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html#busy-beaver-ones-five-wanted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Busy beaver](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/busy-beaver/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/computability/busy-beaver)
