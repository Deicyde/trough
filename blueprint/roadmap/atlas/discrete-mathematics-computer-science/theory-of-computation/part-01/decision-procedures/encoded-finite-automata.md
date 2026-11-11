---
declaration: section
origin: cited
lean: Cslib.Automata.EncodedDFA, Cslib.Automata.EncodedDFA.step, Cslib.Automata.EncodedDFA.toDFA, Cslib.Automata.EncodedDFA.language, Cslib.Automata.EncodedDFA.letters, Cslib.Automata.EncodedDFA.states, Cslib.Automata.EncodedDFA.step_eq_self, Cslib.Automata.EncodedDFA.step_eq_of_forall
statement: formalized
proof: formalized
---

# Encoded finite automata

42 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encoded-finite-automata/index.html).

## Encoded DFA

An encoded deterministic finite automaton over an alphabet $\alpha$ is a
deterministic finite automaton given as data with natural-number states: a start state in
$\mathbb{N}$, a list of accepting states in $\mathbb{N}$, and a list of transitions $((s, a), t)$
with $s, t \in \mathbb{N}$ and $a \in \alpha$, read as "on letter $a$, state $s$ moves to $t$".

Formalized by `Cslib.Automata.EncodedDFA`, a structure declared in [CSLibExt/Computability/Automata/DA/EncodedDFA.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/DA/EncodedDFA.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encoded-finite-automata/index.html#encoded-dfa).

## Transition function of an encoded DFA

For an encoded DFA $D$, a state $s \in \mathbb{N}$
and a letter $a$, the step of $D$ from $s$ on $a$ is the target of the first transition that $D$
lists from $s$ on $a$, or $s$ itself when $D$ lists no such transition.

Formalized by `Cslib.Automata.EncodedDFA.step`, a definition declared in [CSLibExt/Computability/Automata/DA/EncodedDFA.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/DA/EncodedDFA.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encoded-finite-automata/index.html#step).

## The automaton denoted by an encoded DFA

An encoded DFA $D$ over an alphabet $\alpha$
denotes the deterministic automaton over $\alpha$ with state set $\mathbb{N}$ whose start state is
the start state of $D$, whose transition function is the transition function of $D$, and whose
accepting states are the states in the accepting list of $D$.

Formalized by `Cslib.Automata.EncodedDFA.toDFA`, a definition declared in [CSLibExt/Computability/Automata/DA/EncodedDFA.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/DA/EncodedDFA.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encoded-finite-automata/index.html#to-dfa).

## Language of an encoded DFA

The language of an encoded DFA $D$ is the set of words $w$
such that the state reached by running $D$ on $w$ from its start state, following its transition
function, is one of its accepting states.

Formalized by `Cslib.Automata.EncodedDFA.language`, a definition declared in [CSLibExt/Computability/Automata/DA/EncodedDFA.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/DA/EncodedDFA.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encoded-finite-automata/index.html#language).

## Letters of an encoded DFA

The letters of an encoded DFA $D$ form the list of the letters
$a$ of its listed transitions $((s, a), t)$, in the order the transitions are listed.

Formalized by `Cslib.Automata.EncodedDFA.letters`, a definition declared in [CSLibExt/Computability/Automata/DA/EncodedDFA.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/DA/EncodedDFA.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encoded-finite-automata/index.html#letters).

## States of an encoded DFA

The states of an encoded DFA $D$ form the list consisting of its
start state followed by the targets of its listed transitions, in the order they are listed.

Formalized by `Cslib.Automata.EncodedDFA.states`, a definition declared in [CSLibExt/Computability/Automata/DA/EncodedDFA.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/DA/EncodedDFA.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encoded-finite-automata/index.html#states).

## Unlisted transitions fix the state

Let $D$ be an encoded DFA, $s \in \mathbb{N}$ a state
and $a$ a letter. If $D$ lists no transition from $s$ on $a$, then the transition function of $D$
takes $s$ on $a$ to $s$.

Formalized by `Cslib.Automata.EncodedDFA.step_eq_self`, a theorem declared in [CSLibExt/Computability/Automata/DA/EncodedDFA.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/DA/EncodedDFA.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encoded-finite-automata/index.html#step-eq-self).

## A step determined by its listed transitions

Let $D$ be an encoded DFA, let
$s, t \in \mathbb{N}$ be states and let $a$ be a letter. If $D$ lists at least one transition from
$s$ on $a$, and every transition listed from $s$ on $a$ has target $t$, then the transition
function of $D$ takes $s$ on $a$ to $t$.

Formalized by `Cslib.Automata.EncodedDFA.step_eq_of_forall`, a theorem declared in [CSLibExt/Computability/Automata/DA/EncodedDFA.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/DA/EncodedDFA.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encoded-finite-automata/index.html#step-eq-of-forall).

## Letters without listed transitions fix every state

Let $D$ be an encoded DFA and let $a$
be a letter that is not among the letters of $D$, that is, no listed transition of $D$ is labelled
$a$. Then for every state $s \in \mathbb{N}$ the transition function of $D$ takes $s$ on $a$ to
$s$.

Formalized by `Cslib.Automata.EncodedDFA.step_of_not_mem_letters`, a theorem declared in [CSLibExt/Computability/Automata/DA/EncodedDFA.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/DA/EncodedDFA.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encoded-finite-automata/index.html#step-of-not-mem-letters).

## Where a step can lead

For every encoded DFA $D$, state $s \in \mathbb{N}$ and letter $a$,
the transition function of $D$ takes $s$ on $a$ either to the target of some listed transition of
$D$ or to $s$ itself.

Formalized by `Cslib.Automata.EncodedDFA.step_mem_or_eq`, a theorem declared in [CSLibExt/Computability/Automata/DA/EncodedDFA.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/DA/EncodedDFA.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encoded-finite-automata/index.html#step-mem-or-eq).

## The listed states are closed under transitions

Let $D$ be an encoded DFA and let $s$ be
one of its states, that is, its start state or the target of one of its listed transitions. Then
for every letter $a$ the transition function of $D$ takes $s$ on $a$ to one of the states of $D$.

Formalized by `Cslib.Automata.EncodedDFA.step_mem_states`, a theorem declared in [CSLibExt/Computability/Automata/DA/EncodedDFA.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/DA/EncodedDFA.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encoded-finite-automata/index.html#step-mem-states).

## Complement of an encoded DFA

The complement of an encoded DFA $D$ has the same start
state and the same transitions as $D$, and its accepting states are those states of $D$ (its
start state and the targets of its listed transitions) that $D$ does not accept.

Formalized by `Cslib.Automata.EncodedDFA.compl`, a definition declared in [CSLibExt/Computability/Automata/DA/EncodedDFA.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/DA/EncodedDFA.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encoded-finite-automata/index.html#compl).

## The complement DFA accepts the complement language

For every encoded DFA $D$ and every
word $w$, the complement of $D$ accepts $w$ if and only if $D$ does not accept $w$.

Formalized by `Cslib.Automata.EncodedDFA.mem_language_compl`, a theorem declared in [CSLibExt/Computability/Automata/DA/EncodedDFA.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/DA/EncodedDFA.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encoded-finite-automata/index.html#mem-language-compl).

## Every finite DFA has an encoding

A DFA over a finite alphabet with finitely many states
has an encoded DFA with the same language.

Formalized by `Cslib.Automata.EncodedDFA.exists_language_eq`, a theorem declared in [CSLibExt/Computability/Automata/DA/EncodedDFA.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/DA/EncodedDFA.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encoded-finite-automata/index.html#exists-language-eq).

## Encoded DFAs as triples

Sending an encoded DFA over $\alpha$ to the triple of its start
state, its list of accepting states and its list of transitions is an equivalence (a bijection
with explicit inverse) between encoded DFAs over $\alpha$ and the set
$\mathbb{N} \times \mathrm{List}\,\mathbb{N} \times \mathrm{List}((\mathbb{N} \times \alpha) \times
\mathbb{N})$.

Formalized by `Cslib.Automata.EncodedDFA.equivProd`, a definition declared in [CSLibExt/Computability/Automata/DA/EncodedDFA.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/DA/EncodedDFA.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encoded-finite-automata/index.html#equiv-prod).

## Assembling an encoded DFA is primitive recursive

Let $\alpha$ be an alphabet with a
primitive recursive encoding, and encode encoded DFAs over $\alpha$ through their start state,
accepting states and transitions. The map sending a triple $(s, F, T)$, where $s \in \mathbb{N}$,
$F$ is a list of natural numbers and $T$ is a list of pairs $((q, a), t)$ with $q, t \in \mathbb{N}$
and $a \in \alpha$, to the encoded DFA over $\alpha$ with start state $s$, accepting states $F$
and transitions $T$ is primitive recursive.

Formalized by `Cslib.Automata.EncodedDFA.primrec_mk`, a theorem declared in [CSLibExt/Computability/Automata/DA/EncodedDFA.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/DA/EncodedDFA.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encoded-finite-automata/index.html#primrec-mk).

## The transition function of encoded DFAs is primitive recursive

Let $\alpha$ be an
alphabet with a primitive recursive encoding and decidable equality, and encode encoded DFAs over
$\alpha$ through their start state, accepting states and transitions. The map sending an encoded
DFA $D$ over $\alpha$, a state $s \in \mathbb{N}$ and a letter $a \in \alpha$ to the state that
$D$ moves to from $s$ on $a$ (the target of the first transition listed for $(s, a)$, or $s$ if
there is none) is primitive recursive.

Formalized by `Cslib.Automata.EncodedDFA.primrec_step`, a theorem declared in [CSLibExt/Computability/Automata/DA/EncodedDFA.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/DA/EncodedDFA.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encoded-finite-automata/index.html#primrec-step).

## Running an encoded DFA is primitive recursive

Let $\alpha$ be an alphabet with a
primitive recursive encoding and decidable equality, and encode encoded DFAs over $\alpha$
through their start state, accepting states and transitions. The map sending an encoded DFA $D$
and a word $w$ over $\alpha$ to the state reached by running $D$ on $w$ from its start state is
primitive recursive.

Formalized by `Cslib.Automata.EncodedDFA.primrec₂_eval`, a theorem declared in [CSLibExt/Computability/Automata/DA/EncodedDFA.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/DA/EncodedDFA.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encoded-finite-automata/index.html#primrec-eval).

## Encoded NFA

An encoded NFA over an alphabet $\alpha$ is a nondeterministic finite
automaton with ε-moves given as data, with natural numbers as states: a list of start states, a
list of accepting states, a list of transitions $((s, a), t)$, meaning that on the letter $a$ the
state $s$ may move to $t$, and a list of ε-moves $(s, t)$, meaning that the state $s$ may move to
$t$ without reading a letter.

Formalized by `Cslib.Automata.EncodedNFA`, a structure declared in [CSLibExt/Computability/Automata/NA/EncodedNFA.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/EncodedNFA.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encoded-finite-automata/index.html#encoded-nfa).

## The ε-NFA of an encoded NFA

An encoded NFA $N$ over $\alpha$ denotes the ε-NFA over
$\alpha$ with state set $\mathbb{N}$ whose start states are the start states listed in $N$, whose
accepting states are the accepting states listed in $N$, and in which a state $s$ may move to $t$
on a letter $a$ exactly when $((s, a), t)$ is a transition of $N$, and without reading a letter
exactly when $(s, t)$ is an ε-move of $N$.

Formalized by `Cslib.Automata.EncodedNFA.toεNFA`, a definition declared in [CSLibExt/Computability/Automata/NA/EncodedNFA.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/EncodedNFA.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encoded-finite-automata/index.html#to-nfa).

## Language of an encoded NFA

The language of an encoded NFA $N$ over an alphabet $\alpha$
is the language accepted by the ε-NFA that $N$ denotes, whose states are the natural numbers:
the words $w$ over $\alpha$ such that some accepting state of $N$ is among the states reached on
$w$ from the start states of $N$, with ε-moves allowed before, between and after the letters.

Formalized by `Cslib.Automata.EncodedNFA.language`, a definition declared in [CSLibExt/Computability/Automata/NA/EncodedNFA.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/EncodedNFA.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encoded-finite-automata/index.html#language-2).

## States an encoded NFA mentions as start states or targets

For an encoded NFA $N$, this is
the list of the start states of $N$, followed by the targets $t$ of its transitions $((s, a), t)$,
followed by the targets $t$ of its ε-moves $(s, t)$.

Formalized by `Cslib.Automata.EncodedNFA.states`, a definition declared in [CSLibExt/Computability/Automata/NA/EncodedNFA.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/EncodedNFA.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encoded-finite-automata/index.html#states-2).

## ε-move relation

For an encoded NFA $N$, the ε-move relation holds between states $s$ and
$t$ exactly when $(s, t)$ is one of the ε-moves of $N$.

Formalized by `Cslib.Automata.EncodedNFA.EpsRel`, a definition declared in [CSLibExt/Computability/Automata/NA/EncodedNFA.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/EncodedNFA.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encoded-finite-automata/index.html#eps-rel).

## The ε-closure is reachability along ε-moves

For an encoded NFA $N$, a set $X$ of natural
numbers and a natural number $t$, $t$ lies in the ε-closure of $X$ in the ε-NFA that $N$ denotes
if and only if $t$ is reachable from some $u \in X$ by a sequence of zero or more ε-moves of $N$.

Formalized by `Cslib.Automata.EncodedNFA.mem_εClosure_iff`, a theorem declared in [CSLibExt/Computability/Automata/NA/EncodedNFA.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/EncodedNFA.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encoded-finite-automata/index.html#mem-closure-iff).

## ε-successors of a state

For an encoded NFA $N$ and a state $s$, the ε-successors of $s$
are the list of the targets $t$ of the ε-moves $(s, t)$ of $N$, in the order in which these
ε-moves are listed.

Formalized by `Cslib.Automata.EncodedNFA.epsNext`, a definition declared in [CSLibExt/Computability/Automata/NA/EncodedNFA.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/EncodedNFA.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encoded-finite-automata/index.html#eps-next).

## ε-closure of a list of states

For an encoded NFA $N$ and a list $S$ of states, the
ε-closure of $S$ is a list whose members are exactly the states reachable from some state of $S$
by finitely many ε-moves of $N$ (zero moves included), computed by a search from each state of
$S$.

Formalized by `Cslib.Automata.EncodedNFA.closure`, a definition declared in [CSLibExt/Computability/Automata/NA/EncodedNFA.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/EncodedNFA.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encoded-finite-automata/index.html#closure).

## Letter step of an encoded NFA

For an encoded NFA $N$, a list $S$ of states and a letter
$a$, the letter step lists the target $t$ of every transition $((s, a), t)$ of $N$ with $s \in S$,
in the order of the transition list of $N$, without taking the ε-closure.

Formalized by `Cslib.Automata.EncodedNFA.letterStep`, a definition declared in [CSLibExt/Computability/Automata/NA/EncodedNFA.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/EncodedNFA.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encoded-finite-automata/index.html#letter-step).

## One step of an encoded NFA on a list of states

For an encoded NFA $N$, a list $S$ of
states and a letter $a$, the list of states reached from $S$ on $a$: the ε-closure, computed as a
list, of the list of states $t$ such that $((s, a), t)$ is a transition of $N$ for some $s$ in
$S$.

Formalized by `Cslib.Automata.EncodedNFA.stepList`, a definition declared in [CSLibExt/Computability/Automata/NA/EncodedNFA.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/EncodedNFA.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encoded-finite-automata/index.html#step-list).

## Run of an encoded NFA

For an encoded NFA $N$ and a word $w = a_1 \cdots a_n$, the run of
$N$ on $w$ is the list of states obtained by starting from the ε-closure of the start states of
$N$ and, for each letter $a_i$ in turn, taking the letter step on $a_i$ and then the ε-closure.

Formalized by `Cslib.Automata.EncodedNFA.run`, a definition declared in [CSLibExt/Computability/Automata/NA/EncodedNFA.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/EncodedNFA.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encoded-finite-automata/index.html#run).

## Membership test for encoded NFAs

For an encoded NFA $N$ and a word $w$, the membership
test is the Boolean that is true exactly when some state reached on $w$ is an accepting state of
$N$. The states reached on $w$ are computed from the ε-closure of the start states by, for each
letter of $w$ in turn, following the transitions on that letter and taking the ε-closure.

Formalized by `Cslib.Automata.EncodedNFA.acceptsB`, a definition declared in [CSLibExt/Computability/Automata/NA/EncodedNFA.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/EncodedNFA.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encoded-finite-automata/index.html#accepts-b).

## The run of an encoded NFA agrees with ε-NFA evaluation

For an encoded NFA $N$, a word $w$
and a natural number $t$, $t$ is among the states in the run of $N$ on $w$ if and only if $t$ is
among the states that the ε-NFA denoted by $N$ reaches on $w$ from its start states, with ε-moves
allowed before, between and after the letters.

Formalized by `Cslib.Automata.EncodedNFA.mem_run_iff`, a theorem declared in [CSLibExt/Computability/Automata/NA/EncodedNFA.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/EncodedNFA.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encoded-finite-automata/index.html#mem-run-iff).

## Correctness of the NFA membership test

For an encoded NFA $N$ and a word $w$, the
membership test returns true on $w$ if and only if $w$ belongs to the language of $N$.

Formalized by `Cslib.Automata.EncodedNFA.acceptsB_iff`, a theorem declared in [CSLibExt/Computability/Automata/NA/EncodedNFA.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/EncodedNFA.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encoded-finite-automata/index.html#accepts-b-iff).

## The states reached on a word are closed under ε-moves

Let $N$ be an encoded NFA and $w$ a
word. If $u$ is one of the states that the ε-NFA denoted by $N$ can be in after reading $w$, and
$N$ has an ε-move from $u$ to $v$, then $v$ is also one of these states.

Formalized by `Cslib.Automata.EncodedNFA.eval_epsRel`, a theorem declared in [CSLibExt/Computability/Automata/NA/EncodedNFA.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/EncodedNFA.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encoded-finite-automata/index.html#eval-eps-rel).

## Successors of a state in an encoded NFA

For an encoded NFA $N$ and a state $s$, this is the
list of the targets $t$ of the transitions $((s, a), t)$ of $N$ on any letter $a$, followed by the
targets $t$ of the ε-moves $(s, t)$ of $N$, each in the order of the corresponding list of $N$.

Formalized by `Cslib.Automata.EncodedNFA.next`, a definition declared in [CSLibExt/Computability/Automata/NA/EncodedNFA.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/EncodedNFA.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encoded-finite-automata/index.html#next).

## Reachable states of an encoded NFA

For an encoded NFA $N$, this is the list, found by a
search from each start state of $N$ in turn through the start states of $N$ and the targets of
its transitions and ε-moves, of the states reachable from a start state of $N$ by zero or more
moves, each a transition of $N$ on some letter or an ε-move of $N$.

Formalized by `Cslib.Automata.EncodedNFA.reachable`, a definition declared in [CSLibExt/Computability/Automata/NA/EncodedNFA.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/EncodedNFA.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encoded-finite-automata/index.html#reachable).

## The reachable states are those some word can lead to

For an encoded NFA $N$ and a natural
number $t$, $t$ is among the reachable states of $N$ if and only if there is a word $w$ such that
$t$ is among the states that the ε-NFA denoted by $N$ reaches on $w$ from its start states, with
ε-moves allowed before, between and after the letters.

Formalized by `Cslib.Automata.EncodedNFA.mem_reachable_iff`, a theorem declared in [CSLibExt/Computability/Automata/NA/EncodedNFA.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/EncodedNFA.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encoded-finite-automata/index.html#mem-reachable-iff).

## Emptiness test for encoded NFAs

For an encoded NFA $N$, the emptiness test is the
Boolean that is true exactly when no state in the list of reachable states of $N$ is an
accepting state of $N$; the reachable states are those reachable from a start state of $N$ by
zero or more moves, each a transition on some letter or an ε-move.

Formalized by `Cslib.Automata.EncodedNFA.isEmptyB`, a definition declared in [CSLibExt/Computability/Automata/NA/EncodedNFA.lean, line 290](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/EncodedNFA.lean#L290). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encoded-finite-automata/index.html#is-empty-b).

## Every finite ε-NFA has an encoding

An `εNFA` over a finite alphabet with finitely many
states has an encoded NFA with the same language.

Formalized by `Cslib.Automata.EncodedNFA.exists_language_eq_εNFA`, a theorem declared in [CSLibExt/Computability/Automata/NA/EncodedNFA.lean, line 317](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/EncodedNFA.lean#L317). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encoded-finite-automata/index.html#exists-language-eq-nfa).

## Every finite NFA has an encoding

An NFA over a finite alphabet with finitely many states
has an encoded NFA with the same language.

Formalized by `Cslib.Automata.EncodedNFA.exists_language_eq`, a theorem declared in [CSLibExt/Computability/Automata/NA/EncodedNFA.lean, line 394](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/EncodedNFA.lean#L394). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encoded-finite-automata/index.html#exists-language-eq-2).

## Encoded NFAs as tuples

The bijection between encoded NFAs over $\alpha$ and quadruples
consisting of a list of natural numbers, a list of natural numbers, a list of elements of
$(\mathbb{N} \times \alpha) \times \mathbb{N}$ and a list of pairs of natural numbers, which sends
an encoded NFA to its start states, accepting states, transitions and ε-moves.

Formalized by `Cslib.Automata.EncodedNFA.equivProd`, a definition declared in [CSLibExt/Computability/Automata/NA/EncodedNFA.lean, line 404](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/EncodedNFA.lean#L404). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encoded-finite-automata/index.html#equiv-prod-2).

## Membership for NFAs is decidable

For every alphabet $\alpha$ with a primitive recursive
encoding, the property of a pair $(N, w)$, where $N$ is an encoded NFA (with ε-moves) over
$\alpha$ and $w$ is a word over $\alpha$, that $w$ is in the language of $N$ is decidable by a
multi-stack machine. This is Sipser, Theorem 4.2: the problem $A_{\mathrm{NFA}}$ is decidable.

Formalized by `Cslib.Automata.EncodedNFA.tm2Decidable_mem_language`, a theorem declared in [CSLibExt/Computability/Automata/NA/EncodedNFA.lean, line 503](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/EncodedNFA.lean#L503). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encoded-finite-automata/index.html#tm2-decidable-mem-language).

## Emptiness of NFAs is decidable

For every alphabet $\alpha$ with a primitive recursive
encoding, the property of an encoded NFA $N$ (with ε-moves) over $\alpha$ that its language is
empty is decidable by a multi-stack machine. This is the problem $E_{\mathrm{NFA}}$.

Formalized by `Cslib.Automata.EncodedNFA.tm2Decidable_language_eq_zero`, a theorem declared in [CSLibExt/Computability/Automata/NA/EncodedNFA.lean, line 511](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/EncodedNFA.lean#L511). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encoded-finite-automata/index.html#tm2-decidable-language-eq-zero).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Encoded finite automata](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encoded-finite-automata/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/decision-procedures/encoded-finite-automata)
