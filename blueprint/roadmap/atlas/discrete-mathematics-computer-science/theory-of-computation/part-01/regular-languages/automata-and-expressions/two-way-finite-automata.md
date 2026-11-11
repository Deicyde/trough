---
declaration: section
origin: cited
lean: Cslib.Automata.TwoWayDFA, Cslib.Automata.TwoWayDFA.toTwoWayNA, Cslib.Automata.TwoWayDFA.tr_iff, Cslib.Automata.TwoWayDFA.tr_functional, Cslib.Automata.TwoWayDFA.language, Cslib.Automata.TwoWayDFA.mem_language, Cslib.Automata.TwoWayDFA.language_isRegular, Cslib.Automata.TwoWayDFA.ofDFA
statement: formalized
proof: formalized
---

# Two-way finite automata

13 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/two-way-finite-automata/index.html).

## Automata

## Deterministic two-way automaton

A deterministic two-way automaton with state set $Q$
over the alphabet $\Sigma$ consists of a partial transition function, which assigns to each
state $q \in Q$ and input symbol $a \in \Sigma$ at most one pair of a successor state and a head
move (left, stay or right), together with a single start state and a set of accepting states.

Formalized by `Cslib.Automata.TwoWayDFA`, a structure declared in [CSLibExt/Computability/Automata/TwoWayNA/TwoWayDFA.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/TwoWayNA/TwoWayDFA.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/two-way-finite-automata/index.html#two-way-dfa).

## A deterministic two-way automaton as a nondeterministic one

A deterministic two-way
automaton $A$ is viewed as the nondeterministic two-way automaton with the same states and
accepting states, whose only start state is the start state of $A$, and which can go from state
$q$ reading a symbol $a$ to state $q'$ with head move $m$ exactly when the step function of $A$
at $q$ and $a$ returns $q'$ and $m$.

Formalized by `Cslib.Automata.TwoWayDFA.toTwoWayNA`, a definition declared in [CSLibExt/Computability/Automata/TwoWayNA/TwoWayDFA.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/TwoWayNA/TwoWayDFA.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/two-way-finite-automata/index.html#to-two-way-na).

## Transition relation of a deterministic two-way automaton

Let $A$ be a deterministic
two-way automaton, viewed as a nondeterministic two-way automaton. On reading the symbol $x$ in
state $q$, it has a transition to state $q'$ with head move $m$ if and only if the transition
function of $A$ sends $(q, x)$ to the pair $(q', m)$.

Formalized by `Cslib.Automata.TwoWayDFA.tr_iff`, a theorem declared in [CSLibExt/Computability/Automata/TwoWayNA/TwoWayDFA.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/TwoWayNA/TwoWayDFA.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/two-way-finite-automata/index.html#tr-iff).

## Deterministic two-way automata have unique transitions

Let $A$ be a deterministic
two-way automaton, viewed as a nondeterministic two-way automaton. If, on reading the symbol
$x$ in state $q$, it has a transition to state $q'$ with head move $m$ and a transition to
state $q''$ with head move $m'$, then $m = m'$ and $q' = q''$.

Formalized by `Cslib.Automata.TwoWayDFA.tr_functional`, a theorem declared in [CSLibExt/Computability/Automata/TwoWayNA/TwoWayDFA.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/TwoWayNA/TwoWayDFA.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/two-way-finite-automata/index.html#tr-functional).

## Language of a deterministic two-way automaton

The language of a deterministic two-way
automaton $A$ is the set of words accepted by $A$ viewed as a nondeterministic two-way
automaton: a word $w$ belongs to it when, starting in the start state with the head at the
first position of $w$ and following the step function of $A$ (which moves the head one
position left, keeps it in place, or moves it one position right, and gets stuck when it is
undefined or would move the head left of the first position), the automaton reaches an
accepting state with the head just past the last symbol of $w$.

Formalized by `Cslib.Automata.TwoWayDFA.language`, a definition declared in [CSLibExt/Computability/Automata/TwoWayNA/TwoWayDFA.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/TwoWayNA/TwoWayDFA.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/two-way-finite-automata/index.html#language).

## Membership in the language of a two-way deterministic automaton

For every
deterministic two-way automaton $A$ and every word $w$, $w$ belongs to the language of $A$ if
and only if $w$ is accepted by $A$ viewed as a nondeterministic two-way automaton.

Formalized by `Cslib.Automata.TwoWayDFA.mem_language`, a theorem declared in [CSLibExt/Computability/Automata/TwoWayNA/TwoWayDFA.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/TwoWayNA/TwoWayDFA.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/two-way-finite-automata/index.html#mem-language).

## Finite two-way deterministic automata accept regular languages

The language of every
deterministic two-way automaton with finitely many states is regular.

Formalized by `Cslib.Automata.TwoWayDFA.language_isRegular`, a theorem declared in [CSLibExt/Computability/Automata/TwoWayNA/TwoWayDFA.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/TwoWayNA/TwoWayDFA.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/two-way-finite-automata/index.html#language-is-regular).

## A DFA as a two-way deterministic automaton

For a DFA $M$ with transition function
$\delta$, this is the deterministic two-way automaton with the same states, start state and
accepting states as $M$ which, in state $q$ reading a symbol $a$, goes to state $\delta(q, a)$
and moves its head one symbol to the right.

Formalized by `Cslib.Automata.TwoWayDFA.ofDFA`, a definition declared in [CSLibExt/Computability/Automata/TwoWayNA/TwoWayDFA.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/TwoWayNA/TwoWayDFA.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/two-way-finite-automata/index.html#of-dfa).

## The two-way simulation of a DFA agrees with that of its NFA

For every DFA $M$, the
deterministic two-way automaton that simulates $M$, viewed as a nondeterministic two-way
automaton, equals the nondeterministic two-way automaton obtained by viewing $M$ as an NFA and
letting that NFA always move its head one symbol to the right.

Formalized by `Cslib.Automata.TwoWayDFA.toTwoWayNA_ofDFA`, a theorem declared in [CSLibExt/Computability/Automata/TwoWayNA/TwoWayDFA.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/TwoWayNA/TwoWayDFA.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/two-way-finite-automata/index.html#to-two-way-na-of-dfa).

## The two-way simulation of a DFA accepts the same language

For every DFA $M$, the
deterministic two-way automaton that simulates $M$ by always moving its head one symbol to the
right has exactly the language accepted by $M$.

Formalized by `Cslib.Automata.TwoWayDFA.language_ofDFA`, a theorem declared in [CSLibExt/Computability/Automata/TwoWayNA/TwoWayDFA.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/TwoWayNA/TwoWayDFA.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/two-way-finite-automata/index.html#language-of-dfa).

## Regular languages are accepted by two-way deterministic automata

For every regular
language $L$ over an alphabet, there is a deterministic two-way automaton with finitely many
states whose language is exactly $L$.

Formalized by `Cslib.Automata.TwoWayDFA.exists_ofDFA_of_isRegular`, a theorem declared in [CSLibExt/Computability/Automata/TwoWayNA/TwoWayDFA.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/TwoWayNA/TwoWayDFA.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/two-way-finite-automata/index.html#exists-of-dfa-of-is-regular).

## Finite two-way nondeterministic automata accept regular languages

Every
nondeterministic two-way automaton with finitely many states accepts a regular language.

A run of such an automaton on a word starts in a start state with the head at the first
position; each step reads the symbol under the head, changes the state and moves the head one
position left, keeps it in place, or moves it one position right, and the run is stuck if the
head would move left of the first position. A word is accepted when some run ends in an
accepting state with the head just past the last symbol.

Formalized by `Cslib.Automata.TwoWayNA.language_isRegular`, a theorem declared in [CSLibExt/Computability/Automata/TwoWayNA/TwoWayDFA.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/TwoWayNA/TwoWayDFA.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/two-way-finite-automata/index.html#language-is-regular-2).

## Regular languages are accepted by two-way nondeterministic automata

For every
regular language $L$ over an alphabet, there is a nondeterministic two-way automaton with
finitely many states that accepts exactly the words of $L$.

A run of such an automaton on a word starts in a start state with the head at the first
position; each step reads the symbol under the head, changes the state and moves the head one
position left, keeps it in place, or moves it one position right, and the run is stuck if the
head would move left of the first position. A word is accepted when some run ends in an
accepting state with the head just past the last symbol.

Formalized by `Cslib.Automata.exists_twoWayNA_of_isRegular`, a theorem declared in [CSLibExt/Computability/Automata/TwoWayNA/TwoWayDFA.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/TwoWayNA/TwoWayDFA.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/two-way-finite-automata/index.html#exists-two-way-na-of-is-regular).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Two-way finite automata](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/two-way-finite-automata/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/two-way-finite-automata)
