---
declaration: section
origin: cited
lean: Cslib.Automata.SequentialTransducer, Cslib.Automata.SequentialTransducer.runFrom, Cslib.Automata.SequentialTransducer.runState, Cslib.Automata.SequentialTransducer.runOut, Cslib.Automata.SequentialTransducer.runState_cons, Cslib.Automata.SequentialTransducer.runOut_cons, Cslib.Automata.SequentialTransducer.runState_append, Cslib.Automata.SequentialTransducer.runOut_append
statement: formalized
proof: formalized
---

# Sequential transducers, Mealy and Moore machines

50 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html).

## Automata

## Sequential transducer

A sequential transducer with states in a type $Q$, input letters in
a type $\Sigma$ and output letters in a type $\Gamma$ consists of a transition function assigning
to each state $q \in Q$ and input letter $a \in \Sigma$ a successor state in $Q$ and an output
word over $\Gamma$, a start state in $Q$, a set of accepting states $F \subseteq Q$, an initial
output word over $\Gamma$, and, for each state in $Q$, a final output word over $\Gamma$.

No finiteness is assumed of $Q$, $\Sigma$ or $\Gamma$.

Formalized by `Cslib.Automata.SequentialTransducer`, a structure declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#sequential-transducer).

## Run of a sequential transducer

The run of a sequential transducer $S$ from a state $q$
on an input word $a_1 \cdots a_n$ is the pair $(q_n, w_1 w_2 \cdots w_n)$, where $q_0 = q$ and,
for each $1 \le i \le n$, $S$ moves from $q_{i-1}$ on $a_i$ to $q_i$ emitting the word $w_i$.
The initial output and the final outputs of $S$ are not included.

Formalized by `Cslib.Automata.SequentialTransducer.runFrom`, a definition declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#run-from).

## Final state of a sequential transducer run

For a sequential transducer $S$, a state $q$
and an input word $w$, the final state of the run of $S$ from $q$ on $w$ is obtained by starting
in $q$, reading the letters of $w$ in order, moving at each letter to the successor state given
by the transition function of $S$, and taking the state reached at the end.

Formalized by `Cslib.Automata.SequentialTransducer.runState`, a definition declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#run-state).

## Output word of a sequential transducer run

For a sequential transducer $S$, a state $q$
and an input word $x$, the output word of the run from $q$ on $x$ is the concatenation of the
output words that $S$ emits on the successive letters of $x$, starting in $q$ and moving to the
successor state after each letter; the initial and final outputs are not included.

Formalized by `Cslib.Automata.SequentialTransducer.runOut`, a definition declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#run-out).

## Final state of a sequential transducer run on a nonempty word

Let $S$ be a sequential
transducer, $q$ a state, $a$ an input letter and $w$ an input word, and let $q'$ be the successor
state of $q$ on $a$ under the transition function of $S$. Then the final state of the run of $S$
from $q$ on the word $aw$ equals the final state of the run of $S$ from $q'$ on $w$.

Formalized by `Cslib.Automata.SequentialTransducer.runState_cons`, a theorem declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#run-state-cons).

## Output of a sequential transducer on a nonempty word

Let $S$ be a sequential
transducer, $q$ a state, $a$ an input letter and $x$ an input word, and let $q'$ and $w$ be the
successor state and the output word of $S$ in state $q$ on letter $a$. The output word of the
run of $S$ from $q$ on $ax$ is $w$ followed by the output word of the run from $q'$ on $x$.

Formalized by `Cslib.Automata.SequentialTransducer.runOut_cons`, a theorem declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#run-out-cons).

## Final state of a sequential transducer on a concatenation

For a sequential transducer
$S$, a state $q$ and input words $x$ and $y$, the final state of the run of $S$ from $q$ on $xy$
is the final state of the run on $y$ from the final state of the run from $q$ on $x$.

Formalized by `Cslib.Automata.SequentialTransducer.runState_append`, a theorem declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#run-state-append).

## Output of a sequential transducer on a concatenation

For a sequential transducer $S$,
a state $q$ and input words $x$ and $y$, the output word of the run of $S$ from $q$ on $xy$ is
the output word of the run from $q$ on $x$ followed by the output word of the run on $y$ from
the final state of the run from $q$ on $x$.

Formalized by `Cslib.Automata.SequentialTransducer.runOut_append`, a theorem declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#run-out-append).

## Translation by a sequential transducer

A sequential transducer $S$ translates an input
word $x$ to an output word $y$ when the run of $S$ on $x$ from its start state ends in an
accepting state $q$ and $y$ is the concatenation of the initial output of $S$, the output words
emitted by the transitions along the run, and the final output of $S$ at $q$.

Formalized by `Cslib.Automata.SequentialTransducer.Translates`, a definition declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#translates).

## Composition of sequential transducers

Let $S_1$ be a sequential transducer from $I$ to
$M$ with start state $s_1$, initial output $\iota_1$ and final output map $\phi_1$, and let $S_2$
be one from $M$ to $O$ with start state $s_2$, initial output $\iota_2$ and final output map
$\phi_2$. For a transducer $S$, a state $q$ and a word $w$, write $\delta_S(q, w)$ for the state
$S$ reaches by reading $w$ from $q$ and $\lambda_S(q, w)$ for the concatenation of the words it
emits along the way. The composition of $S_1$ and $S_2$ is the sequential transducer from $I$ to
$O$ whose states are the pairs $(q_1, q_2)$ of a state of $S_1$ and a state of $S_2$, where:
reading a letter $a$ in state $(q_1, q_2)$, if $S_1$ reading $a$ in $q_1$ moves to $q_1'$ and
emits $w$, the composition moves to $(q_1', \delta_{S_2}(q_2, w))$ and emits
$\lambda_{S_2}(q_2, w)$; the start state is $(s_1, \delta_{S_2}(s_2, \iota_1))$; the initial
output is $\iota_2$ followed by $\lambda_{S_2}(s_2, \iota_1)$; a state $(q_1, q_2)$ is accepting
when $q_1$ is accepting for $S_1$ and $\delta_{S_2}(q_2, \phi_1(q_1))$ is accepting for $S_2$; and
the final output at $(q_1, q_2)$ is $\lambda_{S_2}(q_2, \phi_1(q_1))$ followed by
$\phi_2(\delta_{S_2}(q_2, \phi_1(q_1)))$.

In words: run $S_1$ and feed its output, including its initial output (fed through $S_2$ before
any input is read) and its final output, through $S_2$.

Formalized by `Cslib.Automata.SequentialTransducer.comp`, a definition declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#comp).

## One step of a composite transducer: the successor state

Let $S_1$ be a sequential
transducer from $I$ to $M$, $S_2$ one from $M$ to $O$, and $C$ their composition. Let $q_1$ be a
state of $S_1$, $q_2$ a state of $S_2$ and $a \in I$ a letter, and suppose that $S_1$, reading
$a$ in state $q_1$, moves to $q_1'$ and emits the word $w$. Then $C$, reading $a$ in state
$(q_1, q_2)$, moves to $(q_1', q_2')$, where $q_2'$ is the state $S_2$ reaches by reading $w$
from $q_2$.

Formalized by `Cslib.Automata.SequentialTransducer.comp_step_fst`, a theorem declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#comp-step-fst).

## One step of a composite transducer: the output

Let $S_1$ be a sequential transducer from
$I$ to $M$, $S_2$ one from $M$ to $O$, and $C$ their composition. Let $q_1$ be a state of $S_1$,
$q_2$ a state of $S_2$ and $a \in I$ a letter, and let $w$ be the word $S_1$ emits when it reads
$a$ in state $q_1$. Then the word $C$ emits when it reads $a$ in state $(q_1, q_2)$ is the
concatenation of the words $S_2$ emits while reading $w$ from $q_2$.

Formalized by `Cslib.Automata.SequentialTransducer.comp_step_snd`, a theorem declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#comp-step-snd).

## States reached by a composite sequential transducer

Let $S_1$ be a sequential transducer
from $I$ to $M$, $S_2$ one from $M$ to $O$, and $C$ their composition. For a transducer $S$, a
state $q$ and a word $w$, write $\delta_S(q, w)$ for the state $S$ reaches by reading $w$ from
$q$ and $\lambda_S(q, w)$ for the concatenation of the words it emits along the way (without
initial or final output). Then for all states $q_1$ of $S_1$ and $q_2$ of $S_2$ and every word
$x$ over $I$,
$\delta_C((q_1, q_2), x) = (\delta_{S_1}(q_1, x), \delta_{S_2}(q_2, \lambda_{S_1}(q_1, x)))$.

Formalized by `Cslib.Automata.SequentialTransducer.comp_runState`, a theorem declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#comp-run-state).

## Output of a composite sequential transducer

Let $S_1$ be a sequential transducer from
$I$ to $M$, $S_2$ one from $M$ to $O$, and $C$ their composition. For a transducer $S$, a state
$q$ and a word $w$, write $\lambda_S(q, w)$ for the concatenation of the words $S$ emits while
reading $w$ from $q$ (without initial or final output). Then for all states $q_1$ of $S_1$ and
$q_2$ of $S_2$ and every word $x$ over $I$,
$\lambda_C((q_1, q_2), x) = \lambda_{S_2}(q_2, \lambda_{S_1}(q_1, x))$.

Formalized by `Cslib.Automata.SequentialTransducer.comp_runOut`, a theorem declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#comp-run-out).

## State of the second transducer after the first one's whole output

Let $S_1$ be a
sequential transducer from $I$ to $M$ and $S_2$ one from $M$ to $O$, with start states $s_1$ and
$s_2$. For a transducer $S$, a state $q$ and a word $w$, write $\delta_S(q, w)$ for the state $S$
reaches by reading $w$ from $q$ and $\lambda_S(q, w)$ for the concatenation of the words it emits
along the way (without initial or final output); juxtaposition of words is concatenation. For a
word $x$ over $I$, let $\iota$ be the initial output of $S_1$, let $u = \lambda_{S_1}(s_1, x)$,
and let $f$ be the final output of $S_1$ at $\delta_{S_1}(s_1, x)$. Then
$\delta_{S_2}(s_2, \iota u f) = \delta_{S_2}(\delta_{S_2}(\delta_{S_2}(s_2, \iota), u), f)$.

Formalized by `Cslib.Automata.SequentialTransducer.comp_runState_initOut`, a theorem declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#comp-run-state-init-out).

## Output of the second transducer on the first one's whole output

Let $S_1$ be a
sequential transducer from $I$ to $M$ and $S_2$ one from $M$ to $O$, with start states $s_1$ and
$s_2$. For a transducer $S$, a state $q$ and a word $w$, write $\delta_S(q, w)$ for the state $S$
reaches by reading $w$ from $q$ and $\lambda_S(q, w)$ for the concatenation of the words it emits
along the way (without initial or final output); juxtaposition of words is concatenation. For a
word $x$ over $I$, let $\iota$ be the initial output of $S_1$, let $u = \lambda_{S_1}(s_1, x)$,
let $f$ be the final output of $S_1$ at $\delta_{S_1}(s_1, x)$, and let
$r = \delta_{S_2}(s_2, \iota)$. Then
$\lambda_{S_2}(s_2, \iota u f) = \lambda_{S_2}(s_2, \iota) \, \lambda_{S_2}(r, u) \,
\lambda_{S_2}(\delta_{S_2}(r, u), f)$.

Formalized by `Cslib.Automata.SequentialTransducer.comp_runOut_initOut`, a theorem declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#comp-run-out-init-out).

## Total output of a composite sequential transducer

Let $S_1$ be a sequential transducer
from $I$ to $M$, $S_2$ one from $M$ to $O$, and $C$ their composition. For a sequential
transducer $S$ with start state $s$, initial output $\iota$ and final output map $\phi$, and a
word $x$, let $\delta_S(s, x)$ be the state $S$ reaches by reading $x$ from $s$ and
$\lambda_S(s, x)$ the concatenation of the words it emits along the way, and call the
concatenation $\iota \, \lambda_S(s, x) \, \phi(\delta_S(s, x))$ the whole output of $S$ on $x$
(acceptance plays no role). Then for every word $x$ over $I$, the whole output of $C$ on $x$
equals the whole output of $S_2$ on the whole output of $S_1$ on $x$.

Formalized by `Cslib.Automata.SequentialTransducer.comp_output_eq`, a theorem declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#comp-output-eq).

## Translations of a composite sequential transducer

Let $S_1$ be a sequential transducer
from an alphabet $A$ to an alphabet $B$, and $S_2$ one from $B$ to an alphabet $C$. For every word
$x$ over $A$ and every word $y$ over $C$, the composition of $S_1$ and $S_2$ translates $x$ to $y$
if and only if there is a word $z$ over $B$ such that $S_1$ translates $x$ to $z$ and $S_2$
translates $z$ to $y$.

Formalized by `Cslib.Automata.SequentialTransducer.translates_comp_iff`, a theorem declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#translates-comp-iff).

## Preimage of a language under a sequential transducer

Let $S$ be a sequential transducer
with input alphabet $\Sigma$ and output alphabet $\Gamma$, and let $L$ be a language over
$\Gamma$. The preimage of $L$ under $S$ is the language over $\Sigma$ consisting of the words $x$
for which there is a word $y \in L$ such that $S$ translates $x$ to $y$.

Formalized by `Cslib.Automata.SequentialTransducer.preimage`, a definition declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 292](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L292). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#preimage).

## Product DFA of a sequential transducer and a DFA

Let $S$ be a sequential transducer
with state type $Q$, input alphabet $\Sigma$ and output alphabet $\Gamma$, and let $M$ be a DFA
over $\Gamma$ with state type $P$. The product DFA of $S$ and $M$ is the DFA over $\Sigma$ with
state type $Q \times P$ defined as follows. In state $(q, r)$ on a letter $a$, if $S$ moves from
$q$ to $q'$ emitting the word $w$, it moves to $(q', r')$, where $r'$ is the state $M$ reaches
from $r$ on $w$. Its start state is $(q_0, r_0)$, where $q_0$ is the start state of $S$ and
$r_0$ is the state $M$ reaches from its start state on the initial output of $S$. A state
$(q, r)$ is accepting when $q$ is an accepting state of $S$ and the state $M$ reaches from $r$
on the final output of $S$ at $q$ is an accepting state of $M$.

Formalized by `Cslib.Automata.SequentialTransducer.preimageDFA`, a definition declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 298](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L298). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#preimage-dfa).

## Runs of the product DFA

Let $S$ be a sequential transducer and $M$ a DFA over the
output alphabet of $S$. For every input word $x$, state $q$ of $S$ and state $r$ of $M$, the
product DFA of $S$ and $M$, started in $(q, r)$ and run on $x$, ends in the state $(q', r')$,
where $q'$ is the final state of the run of $S$ from $q$ on $x$ and $r'$ is the state that $M$
reaches from $r$ on the output word of that run.

Formalized by `Cslib.Automata.SequentialTransducer.preimageDFA_evalFrom`, a theorem declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 309](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L309). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#preimage-dfa-eval-from).

## The product DFA recognizes the preimage

Let $S$ be a sequential transducer with output
alphabet $\Gamma$ and let $M$ be a DFA over $\Gamma$. The language accepted by the product DFA
of $S$ and $M$ equals the preimage under $S$ of the language accepted by $M$, that is, the set
of input words that $S$ translates to some word accepted by $M$.

Formalized by `Cslib.Automata.SequentialTransducer.preimageDFA_accepts`, a theorem declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 322](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L322). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#preimage-dfa-accepts).

## Inverse sequential transduction preserves regular languages

Let $S$ be a sequential
transducer with finitely many states, input alphabet $I$ and output alphabet $O$, and let $L$ be
a regular language over $O$. Then the preimage of $L$ under $S$, the set of words over $I$ that
$S$ translates to some word of $L$, is regular.

The proof is the product of $S$ with a DFA for $L$, started in the DFA state reached on the
initial output of $S$.

Formalized by `Cslib.Automata.SequentialTransducer.isRegular_preimage`, a theorem declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 371](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L371). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#is-regular-preimage).

## Mealy machine

A Mealy machine with state set $Q$, input alphabet $I$ and output
alphabet $O$ consists of a start state in $Q$ and a transition function that, given a state
$q \in Q$ and an input letter $a \in I$, returns a successor state in $Q$ and a single output
letter in $O$; thus the output of a transition depends on the state and the input letter.

Formalized by `Cslib.Automata.MealyMachine`, a structure declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 383](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L383). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#mealy-machine).

## Run of a Mealy machine

The run of a Mealy machine $M$ from a state $q$ on an input
word $a_1 \cdots a_n$ is the pair $(q_n, o_1 \cdots o_n)$, where $q_0 = q$ and, for each
$1 \le i \le n$, $M$ moves from $q_{i-1}$ on $a_i$ to $q_i$ emitting the output letter $o_i$.

Formalized by `Cslib.Automata.MealyMachine.runFrom`, a definition declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 392](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L392). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#run-from-2).

## Final state of a Mealy machine run

For a Mealy machine $M$, a state $q$ and an input
word $x$, the final state of the run from $q$ on $x$ is the state reached by starting in $q$
and moving, on each successive letter of $x$, to the successor state given by the transition
function of $M$; on the empty word it is $q$.

Formalized by `Cslib.Automata.MealyMachine.runState`, a definition declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 401](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L401). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#run-state-2).

## Output word of a Mealy machine run

For a Mealy machine $M$, a state $q$ and an input
word $x$, the output word of $M$ from $q$ on $x$ is the second component of the run of $M$ from
$q$ on $x$: the word of output letters emitted along that run, one per input letter.

Formalized by `Cslib.Automata.MealyMachine.runOut`, a definition declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 405](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L405). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#run-out-2).

## Final state of a Mealy machine on a nonempty word

Let $M$ be a Mealy machine, $q$ a
state, $a$ an input letter and $x$ an input word, and let $q'$ be the successor state of $M$ in
state $q$ on letter $a$. The final state of the run of $M$ from $q$ on $ax$ is the final state of
the run from $q'$ on $x$.

Formalized by `Cslib.Automata.MealyMachine.runState_cons`, a theorem declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 409](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L409). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#run-state-cons-2).

## Output of a Mealy machine on a nonempty word

Let $M$ be a Mealy machine, $q$ a state,
$a$ an input letter and $x$ an input word, and let $q'$ and $o$ be the successor state and the
output letter of $M$ in state $q$ on letter $a$. The output word of the run of $M$ from $q$ on
$ax$ is $o$ followed by the output word of the run from $q'$ on $x$.

Formalized by `Cslib.Automata.MealyMachine.runOut_cons`, a theorem declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 415](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L415). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#run-out-cons-2).

## Transduction of a Mealy machine

Let $M$ be a Mealy machine with start state $q_0$. On
an input word $a_1 a_2 \cdots a_n$, for each $i$ let $q_i$ and $b_i$ be the state that $M$ moves
to and the letter that it outputs when it reads $a_i$ in state $q_{i-1}$. The transduction of
$M$ on this word is the output word $b_1 b_2 \cdots b_n$.

Formalized by `Cslib.Automata.MealyMachine.transduce`, a definition declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 421](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L421). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#transduce).

## Mealy machine as a sequential transducer

The sequential transducer of a Mealy machine
$M$ has the states and the start state of $M$; on an input letter $a$ in a state $q$ it moves
to the state that $M$ moves to and emits the one-letter word consisting of the letter that $M$
outputs on this transition. Every state accepts, and the initial and final outputs are empty.

Formalized by `Cslib.Automata.MealyMachine.toSequential`, a definition declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 426](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L426). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#to-sequential).

## The sequential transducer of a Mealy machine has the same final states

For a Mealy
machine $M$, a state $q$ and an input word $w$, the final state of the run from $q$ on $w$ of the
sequential transducer associated with $M$ equals the final state of the run of $M$ from $q$ on
$w$.

Formalized by `Cslib.Automata.MealyMachine.seq_runState_eq`, a theorem declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 435](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L435). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#seq-run-state-eq).

## The sequential transducer of a Mealy machine has the same run outputs

For a Mealy
machine $M$, a state $q$ and an input word $w$, the output word of the run from $q$ on $w$ of the
sequential transducer associated with $M$ (excluding its initial and final outputs) equals the
output word of the run of $M$ from $q$ on $w$.

Formalized by `Cslib.Automata.MealyMachine.seq_runOut_eq`, a theorem declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 446](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L446). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#seq-run-out-eq).

## Every state of the sequential transducer of a Mealy machine is accepting

For a Mealy
machine $M$, the set of accepting states of the sequential transducer associated with $M$ is the
set of all states.

Formalized by `Cslib.Automata.MealyMachine.toSequential_accept`, a theorem declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 458](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L458). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#to-sequential-accept).

## Initial output of the sequential transducer of a Mealy machine

For every Mealy machine
$M$, the initial output of the sequential transducer of $M$ is the empty word.

Formalized by `Cslib.Automata.MealyMachine.toSequential_initOut`, a theorem declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 463](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L463). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#to-sequential-init-out).

## Final outputs of the sequential transducer of a Mealy machine

For every Mealy machine
$M$ and every state $q$, the final output of the sequential transducer of $M$ at $q$ is the
empty word.

Formalized by `Cslib.Automata.MealyMachine.toSequential_finalOut`, a theorem declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 468](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L468). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#to-sequential-final-out).

## The sequential transducer of a Mealy machine computes its transduction

For every Mealy
machine $M$, input word $x$ and output word $y$, the sequential transducer of $M$ translates $x$
to $y$ if and only if the transduction of $M$ on $x$ is $y$.

Formalized by `Cslib.Automata.MealyMachine.translates_toSequential_iff`, a theorem declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 473](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L473). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#translates-to-sequential-iff).

## Moore machine

A Moore machine with state type $Q$, input alphabet $\Sigma$ and output
alphabet $\Gamma$ consists of a transition function, assigning to each state $q$ and input
letter $a$ a successor state $\delta(q, a) \in Q$, an output function $\lambda : Q \to \Gamma$,
and a start state $q_0 \in Q$. The output depends only on the state.

Formalized by `Cslib.Automata.MooreMachine`, a structure declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 485](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L485). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#moore-machine).

## Run of a Moore machine

The run of a Moore machine $M$ with output function $\lambda$
from a state $q$ on an input word $a_1 \cdots a_n$ is the pair
$(q_n, \lambda(q_0) \lambda(q_1) \cdots \lambda(q_n))$, where $q_0 = q$ and, for each
$1 \le i \le n$, $q_i$ is the successor of $q_{i-1}$ on $a_i$. The output word has $n + 1$
letters and begins with the output of the starting state.

Formalized by `Cslib.Automata.MooreMachine.runFrom`, a definition declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 497](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L497). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#run-from-3).

## Final state of a Moore machine run

For a Moore machine $M$, a state $q$ and an input
word $x$, the final state of the run from $q$ on $x$ is the state reached by starting in $q$
and moving, on each successive letter of $x$, to the successor state given by the transition
function of $M$; on the empty word it is $q$.

Formalized by `Cslib.Automata.MooreMachine.runState`, a definition declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 506](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L506). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#run-state-3).

## Output word of a Moore machine run

For a Moore machine $M$, a state $q$ and an input
word $x$, the output word of $M$ from $q$ on $x$ is the second component of the run of $M$ from
$q$ on $x$: the outputs of the states visited along that run, starting with the output of $q$;
it has one more letter than $x$.

Formalized by `Cslib.Automata.MooreMachine.runOut`, a definition declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 510](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L510). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#run-out-3).

## Final state of a Moore machine run on a nonempty word

For a Moore machine $M$ with
transition function $\delta$, a state $q$, an input letter $a$ and an input word $w$, the final
state of the run of $M$ from $q$ on the word $aw$ equals the final state of the run of $M$ from
$\delta(q, a)$ on $w$.

Formalized by `Cslib.Automata.MooreMachine.runState_cons`, a theorem declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 514](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L514). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#run-state-cons-3).

## Output of a Moore machine on a nonempty word

Let $M$ be a Moore machine, $q$ a state,
$a$ an input letter and $x$ an input word, and let $q'$ be the successor state of $M$ in state
$q$ on letter $a$. The output word of the run of $M$ from $q$ on $ax$ is the output of $q$
followed by the output word of the run from $q'$ on $x$.

Formalized by `Cslib.Automata.MooreMachine.runOut_cons`, a theorem declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 520](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L520). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#run-out-cons-3).

## Transduction of a Moore machine

Let $M$ be a Moore machine with start state $q_0$, and
write $o(q)$ for the output of a state $q$. On an input word $a_1 a_2 \cdots a_n$, let $q_i$ be
the state that $M$ moves to from $q_{i-1}$ on $a_i$. The transduction of $M$ on this word is the
output word $o(q_0)\, o(q_1) \cdots o(q_n)$, of length $n + 1$.

Formalized by `Cslib.Automata.MooreMachine.transduce`, a definition declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 526](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L526). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#transduce-2).

## The sequential transducer of a Moore machine

Let $M$ be a Moore machine with transition
function $\delta$, output function $\lambda$ and start state $q_0$. Its sequential transducer has
the same states and the start state $q_0$; reading a letter $a$ in state $q$ it moves to
$\delta(q, a)$ and emits the one-letter word $\lambda(\delta(q, a))$; every state is accepting;
the initial output is the one-letter word $\lambda(q_0)$; and every final output is empty.

Formalized by `Cslib.Automata.MooreMachine.toSequential`, a definition declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 532](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L532). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#to-sequential-2).

## Moore machine output via its sequential rendering

For a Moore machine $M$, a state $q$
and an input word $x$, the output word of the run of $M$ from $q$ on $x$ is the output of $q$
followed by the output word of the run of the sequential rendering of $M$ from $q$ on $x$.

Formalized by `Cslib.Automata.MooreMachine.runOut_eq_cons`, a theorem declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 541](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L541). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#run-out-eq-cons).

## Every state of the sequential transducer of a Moore machine is accepting

For a Moore
machine $M$, the set of accepting states of the sequential transducer associated with $M$ is the
set of all states.

Formalized by `Cslib.Automata.MooreMachine.toSequential_accept`, a theorem declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 553](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L553). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#to-sequential-accept-2).

## Initial output of the sequential transducer of a Moore machine

For every Moore machine
$M$, the initial output of the sequential transducer of $M$ is the one-letter word consisting of
the output of the start state of $M$.

Formalized by `Cslib.Automata.MooreMachine.toSequential_initOut`, a theorem declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 559](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L559). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#to-sequential-init-out-2).

## Final outputs of the sequential transducer of a Moore machine

For a Moore machine $M$
and every state $q$, the final output word at $q$ of the sequential transducer associated with
$M$ is empty.

Formalized by `Cslib.Automata.MooreMachine.toSequential_finalOut`, a theorem declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 564](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L564). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#to-sequential-final-out-2).

## The sequential transducer of a Moore machine computes its transduction

For every Moore
machine $M$, input word $x$ and output word $y$, the sequential transducer of $M$ translates $x$
to $y$ if and only if the transduction of $M$ on $x$ is $y$.

Formalized by `Cslib.Automata.MooreMachine.translates_toSequential_iff`, a theorem declared in [CSLibExt/Computability/Automata/Transducers/Sequential.lean, line 569](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/Transducers/Sequential.lean#L569). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html#translates-to-sequential-iff-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sequential transducers, Mealy and Moore machines](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/sequential-transducers-mealy-and-moore-machines)
