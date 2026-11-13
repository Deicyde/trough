---
declaration: section
origin: cited
lean: Cslib.Language.leftQuotient_acceptsFrom, Cslib.Language.minimizedState, Cslib.Language.leftQuotientEquivReachableResiduals, Cslib.Language.minimizedDFA, Cslib.Language.toDFA_eval_val, Cslib.Language.minimizedDFA_eval_equiv, Cslib.Language.minimizedDFA_eval, Cslib.Language.minimizedDFA_step_val
statement: formalized
proof: formalized
---

# Minimal deterministic automaton

35 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/minimal-deterministic-automaton/index.html).

## Left quotients of continuation languages

Let $M$ be a DFA, write $\delta^*(q, x)$ for
the state $M$ reaches from the state $q$ by reading the word $x$, and let $L_M(q)$ be the
language of words accepted by $M$ when started in $q$. For every state $q$ and every word $x$,
the left quotient $\{z : xz \in L_M(q)\}$ of $L_M(q)$ by $x$ equals $L_M(\delta^*(q, x))$.

Formalized by `Cslib.Language.leftQuotient_acceptsFrom`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Minimization.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Minimization.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/minimal-deterministic-automaton/index.html#left-quotient-accepts-from).

## Residual reached by a word

For a DFA $M$ and a word $x$, the minimized state of $x$ is the
language accepted by $M$ starting from the state that $M$ reaches on reading $x$ from its start
state, viewed as an element of the reachable residuals of $M$.

Formalized by `Cslib.Language.minimizedState`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Minimization.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Minimization.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/minimal-deterministic-automaton/index.html#minimized-state).

## Left quotients as reachable residuals

Let $M$ be a DFA accepting the language $L$. The
set of left quotients $\{z : xz \in L\}$ of $L$ by words $x$ equals the set of reachable
residuals of $M$ (the languages accepted by $M$ from the states it reaches from its start
state). The bijection from the first set to the second sends each language to itself.

Formalized by `Cslib.Language.leftQuotientEquivReachableResiduals`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Minimization.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Minimization.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/minimal-deterministic-automaton/index.html#left-quotient-equiv-reachable-residuals).

## Minimized DFA

Let $M$ be a DFA accepting the language $L$. The minimized DFA of $M$
has as states the reachable residuals of $M$, that is, the languages accepted by $M$ from the
states it reaches from its start state. Its start state is $L$; on a letter $a$ it moves from
a state $K$ to the left quotient $\{z : az \in K\}$; and its accepting states are those that
contain the empty word.

It is the canonical automaton of $L$, whose states are the left quotients of $L$, with each
state renamed to the same language viewed as a reachable residual of $M$.

Formalized by `Cslib.Language.minimizedDFA`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Minimization.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Minimization.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/minimal-deterministic-automaton/index.html#minimized-dfa).

## States reached in the residual-language DFA

For every language $L$ and every word $x$, the
state that the residual-language DFA of $L$ reaches on reading $x$ is the left quotient
$x^{-1}L = \{z : xz \in L\}$. This automaton has the left quotients of $L$ as states, start state
$L$, transition from $K$ on a letter $a$ to $a^{-1}K$, and accepts $K$ when $K$ contains the empty
word.

Formalized by `Cslib.Language.toDFA_eval_val`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Minimization.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Minimization.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/minimal-deterministic-automaton/index.html#to-dfa-eval-val).

## Evaluation in the minimized DFA agrees with the left-quotient automaton

Let $M$ be a
DFA accepting the language $L$, and consider the automaton whose states are the left quotients
of $L$, with start state $L$, moving from $K$ on a letter $a$ to $\{z : az \in K\}$. For every
word $x$, the state that the minimized DFA of $M$ reaches on $x$, carried to the left quotients
of $L$ by the bijection that sends each language to itself, is the state that this automaton
reaches on $x$.

Formalized by `Cslib.Language.minimizedDFA_eval_equiv`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Minimization.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Minimization.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/minimal-deterministic-automaton/index.html#minimized-dfa-eval-equiv).

## States reached in the minimized DFA

For every DFA $M$ and every word $x$, the state that
the minimized DFA of $M$ reaches on $x$ is the language accepted by $M$ from the state that $M$
reaches on $x$.

Formalized by `Cslib.Language.minimizedDFA_eval`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Minimization.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Minimization.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/minimal-deterministic-automaton/index.html#minimized-dfa-eval).

## Transitions of the minimized DFA

Let $M$ be a DFA. For every reachable residual $K$ of
$M$ (a state of the minimized DFA of $M$) and every letter $a$, the minimized DFA of $M$ moves
from $K$ on input $a$ to the left quotient $\{z : az \in K\}$ of $K$ by $a$.

Formalized by `Cslib.Language.minimizedDFA_step_val`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Minimization.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Minimization.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/minimal-deterministic-automaton/index.html#minimized-dfa-step-val).

## Transitions of the minimized DFA on reached states

Let $M$ be a DFA, and for a word $x$
let $[x]$ be the language accepted by $M$ from the state that $M$ reaches on $x$. For every word
$x$ and every letter $a$, the minimized DFA of $M$ moves from the state $[x]$ on input $a$ to the
state $[xa]$.

Formalized by `Cslib.Language.minimizedDFA_step_minimizedState`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Minimization.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Minimization.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/minimal-deterministic-automaton/index.html#minimized-dfa-step-minimized-state).

## The minimized DFA accepts the same language

For every DFA $M$, the minimized DFA of $M$
accepts exactly the language accepted by $M$.

Formalized by `Cslib.Language.minimizedDFA_accepts`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Minimization.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Minimization.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/minimal-deterministic-automaton/index.html#minimized-dfa-accepts).

## The residual-language DFA is accessible

For every language $L$, the residual-language DFA
of $L$ is accessible. This automaton has as states the left quotients $x^{-1}L = \{z : xz \in L\}$
for words $x$, start state $L$, transition from $K$ on a letter $a$ to $a^{-1}K$, and accepts $K$
when $K$ contains the empty word.

Formalized by `Cslib.Language.toDFA_accessible`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Minimization.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Minimization.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/minimal-deterministic-automaton/index.html#to-dfa-accessible).

## The minimized DFA is accessible

For every DFA $M$, every state of the minimized DFA of
$M$ is reached from its start state by reading some word.

Formalized by `Cslib.Language.minimizedDFA_accessible`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Minimization.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Minimization.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/minimal-deterministic-automaton/index.html#minimized-dfa-accessible).

## Nerode classes and reachable residuals

For a DFA $M$ accepting the language $L$, there is a
bijection from the Nerode classes of $L$ to the reachable residuals of $M$; it sends the class of a
word $x$ to the left quotient $x^{-1}L = \{z : xz \in L\}$.

Formalized by `Cslib.Language.nerodeClassEquivMinimizedState`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Minimization.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Minimization.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/minimal-deterministic-automaton/index.html#nerode-class-equiv-minimized-state).

## Reachable residuals of the minimized DFA

Let $M$ be a DFA accepting the language $L$.
The reachable residuals of the minimized DFA of $M$ and the reachable residuals of $M$ both form
the set of left quotients $x^{-1}L = \{z : xz \in L\}$ of $L$ by words $x$, and this is the
bijection from the first set to the second that sends each language to itself.

It is built as the composite of the bijections from the Nerode classes of $L$ to both sets, each
sending the class of a word $x$ to $x^{-1}L$; so minimizing the minimized DFA again gives the
same state space.

Formalized by `Cslib.Language.minimizedStateEquivIterated`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Minimization.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Minimization.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/minimal-deterministic-automaton/index.html#minimized-state-equiv-iterated).

## When finite, the minimized DFA has as many states as there are Nerode classes

Let $M$
be a DFA accepting the language $L$. If the set of reachable residuals of $M$ (the states of the
minimized DFA of $M$) and the set of Nerode classes of $L$ are both finite, then they have the
same number of elements.

Formalized by `Cslib.Language.minimizedDFA_card_eq_nerode`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Minimization.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Minimization.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/minimal-deterministic-automaton/index.html#minimized-dfa-card-eq-nerode).

## CSLib automata as Mathlib DFAs

A CSLib deterministic automaton $M$ on finite words is
viewed as a Mathlib DFA with the same states, the same transition function, the same start state
and the same set of accepting states as $M$.

Formalized by `Cslib.Automata.DA.FinAcc.toDFA`, a definition declared in [CSLibExt/Computability/Automata/DA/MathlibDFA.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Automata/DA/MathlibDFA.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/minimal-deterministic-automaton/index.html#to-dfa).

## Mathlib DFAs as CSLib automata

A Mathlib DFA $M$ is viewed as a CSLib deterministic
automaton on finite words with the same states, the same transition function, the same start state
and the same set of accepting states as $M$.

Formalized by `Cslib.Automata.DA.FinAcc.ofDFA`, a definition declared in [CSLibExt/Computability/Automata/DA/MathlibDFA.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Automata/DA/MathlibDFA.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/minimal-deterministic-automaton/index.html#of-dfa).

## Converting a CSLib automaton to a Mathlib DFA preserves its language

For every
deterministic automaton $M$ on finite words, the DFA with the same states, transition function,
start state and accepting states as $M$ accepts exactly the language of $M$.

Formalized by `Cslib.Automata.DA.FinAcc.language_toDFA`, a theorem declared in [CSLibExt/Computability/Automata/DA/MathlibDFA.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Automata/DA/MathlibDFA.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/minimal-deterministic-automaton/index.html#language-to-dfa).

## The Nerode congruence relates words with equal left quotients

Let $L$ be a language
over an alphabet $\Sigma$ and let $x, y \in \Sigma^*$. Then $x$ and $y$ are related by the Nerode
congruence of $L$, that is, $xz \in L \iff yz \in L$ for every word $z$, if and only if they are
Nerode equivalent for $L$, that is, their left quotients $x^{-1}L = \{z : xz \in L\}$ and
$y^{-1}L$ are equal.

Formalized by `Cslib.Automata.DA.FinAcc.nerodeCongruence_r_iff`, a theorem declared in [CSLibExt/Computability/Automata/DA/MathlibDFA.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Automata/DA/MathlibDFA.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/minimal-deterministic-automaton/index.html#nerode-congruence-r-iff).

## The residual language of a Nerode class

Let $L$ be a language over an alphabet
$\Sigma$, and write $x^{-1}L = \{z : xz \in L\}$ for the left quotient of $L$ by a word $x$. This
is the map from the classes of the Nerode congruence of $L$ to the set
$\{w^{-1}L : w \in \Sigma^*\}$ of residual languages of $L$ that sends the class of each word $x$
to $x^{-1}L$; it is well defined because Nerode-congruent words have the same left quotient.

Formalized by `Cslib.Automata.DA.FinAcc.nerodeResidual`, a definition declared in [CSLibExt/Computability/Automata/DA/MathlibDFA.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Automata/DA/MathlibDFA.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/minimal-deterministic-automaton/index.html#nerode-residual).

## Nerode classes are the residual languages

Let $L$ be a language over an alphabet
$\Sigma$, and write $x^{-1}L = \{z : xz \in L\}$ for the left quotient of $L$ by a word $x$. This
is the bijection from the classes of the Nerode congruence of $L$ onto the set
$\{x^{-1}L : x \in \Sigma^*\}$ of residual languages of $L$ that sends the class of each word $x$
to $x^{-1}L$.

The residual languages are the states of Mathlib's residual-language DFA of $L$.

Formalized by `Cslib.Automata.DA.FinAcc.nerodeQuotientEquivResidual`, a definition declared in [CSLibExt/Computability/Automata/DA/MathlibDFA.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Automata/DA/MathlibDFA.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/minimal-deterministic-automaton/index.html#nerode-quotient-equiv-residual).

## The Nerode automaton is the residual-language automaton

Let $L$ be a language over an
alphabet $\Sigma$, and write $x^{-1}L = \{z : xz \in L\}$ for the left quotient of $L$ by a word
$x$. Consider the canonical automaton of $L$ as a DFA: its states are the classes $[x]$ of the
Nerode congruence of $L$, its start state is the class of the empty word, on a letter $a$ it goes
from $[x]$ to $[xa]$, and its accepting states are the classes of words of $L$. Renaming each
class $[x]$ to $x^{-1}L$ gives exactly Mathlib's residual-language DFA of $L$: its states are the
residual languages $x^{-1}L$ for $x \in \Sigma^*$, its start state is $L$, on a letter $a$ it goes
from $K$ to $a^{-1}K$, and its accepting states are the residual languages that contain the empty
word.

Formalized by `Cslib.Automata.DA.FinAcc.reindex_nerodeCongruenceDA`, a theorem declared in [CSLibExt/Computability/Automata/DA/MathlibDFA.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Automata/DA/MathlibDFA.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/minimal-deterministic-automaton/index.html#reindex-nerode-congruence-da).

## The canonical automaton of a DFA's language is its minimized DFA

Let $M$ be a DFA over
an alphabet $\Sigma$ accepting the language $L$, and write $x^{-1}L = \{z : xz \in L\}$ for the
left quotient of $L$ by a word $x$. Consider the canonical automaton of $L$ as a DFA: its states
are the classes $[x]$ of the Nerode congruence of $L$, its start state is the class of the empty
word, on a letter $a$ it goes from $[x]$ to $[xa]$, and its accepting states are the classes of
words of $L$. Renaming each class $[x]$ to $x^{-1}L$, regarded as one of the languages accepted
from the states of $M$ reachable from its start state, gives exactly the minimized DFA of $M$.

Formalized by `Cslib.Automata.DA.FinAcc.reindex_nerodeCongruenceDA_eq_minimizedDFA`, a theorem declared in [CSLibExt/Computability/Automata/DA/MathlibDFA.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Automata/DA/MathlibDFA.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/minimal-deterministic-automaton/index.html#reindex-nerode-congruence-da-eq-minimize).

## Morphisms of DFAs

Let $M$ and $N$ be DFAs over the same alphabet with transition
functions $\delta_M$ and $\delta_N$. A morphism from $M$ to $N$ is a map $f$ from the states of
$M$ to the states of $N$ that sends the start state of $M$ to the start state of $N$, satisfies
$f(\delta_M(q, a)) = \delta_N(f(q), a)$ for every state $q$ of $M$ and every symbol $a$, and
such that each state $q$ of $M$ is accepting if and only if $f(q)$ is accepting in $N$.

Formalized by `Cslib.Language.DFAHom`, a structure declared in [CSLibExt/Computability/Languages/Congruences/Universal.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Universal.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/minimal-deterministic-automaton/index.html#dfahom).

## DFA morphisms commute with evaluation from a state

If $f$ is a morphism from a DFA $M$
to a DFA $N$, then for every state $q$ of $M$ and every word $x$, running $N$ on $x$ from $f(q)$
ends in the image under $f$ of the state reached by running $M$ on $x$ from $q$.

Formalized by `Cslib.Language.DFAHom.map_evalFrom`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Universal.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Universal.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/minimal-deterministic-automaton/index.html#map-eval-from).

## DFA morphisms commute with evaluation

If $f$ is a morphism from a DFA $M$ to a DFA $N$,
then for every word $x$, the state that $N$ reaches on input $x$ from its start state is the
image under $f$ of the state that $M$ reaches on input $x$ from its start state.

Formalized by `Cslib.Language.DFAHom.map_eval`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Universal.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Universal.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/minimal-deterministic-automaton/index.html#map-eval).

## DFA morphisms preserve the accepted language

If $f$ is a morphism from a DFA $M$ to a DFA
$N$ over the same alphabet, then $M$ and $N$ accept the same language.

Formalized by `Cslib.Language.DFAHom.accepts_eq`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Universal.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Universal.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/minimal-deterministic-automaton/index.html#accepts-eq).

## Identity DFA morphism

For every DFA $M$, the identity map on the states of $M$ is a DFA
morphism from $M$ to itself.

Formalized by `Cslib.Language.DFAHom.refl`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Universal.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Universal.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/minimal-deterministic-automaton/index.html#refl).

## Composition of DFA morphisms

If $f$ is a DFA morphism from $M$ to $N$ and $g$ is a DFA
morphism from $N$ to $P$, where $M$, $N$, $P$ are DFAs over the same alphabet, then the composite
of $g$ and $f$ is the DFA morphism from $M$ to $P$ whose state map is $g \circ f$.

Formalized by `Cslib.Language.DFAHom.comp`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Universal.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Universal.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/minimal-deterministic-automaton/index.html#comp).

## State-separated DFA

A DFA $M$ is state-separated when any two equivalent states of $M$
are equal: if $p \ne q$, then the languages of words accepted by $M$ starting from $p$ and from
$q$ are different.

Formalized by `Cslib.Language.StateSeparated`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Universal.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Universal.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/minimal-deterministic-automaton/index.html#state-separated).

## The canonical residual map

Let $M$ be an accessible DFA accepting the language $L$. The
residual-language DFA of $L$ has as states the left quotients $x^{-1}L = \{y \mid xy \in L\}$
for words $x$, start state $L$, transitions $K \mapsto a^{-1}K$ on a symbol $a$, and a state $K$
is accepting when it contains the empty word. The canonical residual map is the DFA morphism from
$M$ to this DFA that sends each state $q$ of $M$ to its continuation language, the set of words
$z$ such that running $M$ from $q$ on $z$ ends in an accepting state.

Formalized by `Cslib.Language.canonicalResidualHom`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Universal.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Universal.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/minimal-deterministic-automaton/index.html#canonical-residual-hom).

## The canonical residual map is surjective

For an accessible DFA $M$, every state of the
residual-language DFA of the language accepted by $M$ is the image of some state of $M$ under
the canonical residual map.

Formalized by `Cslib.Language.canonicalResidualHom_surjective`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Universal.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Universal.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/minimal-deterministic-automaton/index.html#canonical-residual-hom-surjective).

## Injectivity of the canonical residual map

For an accessible DFA $M$, the canonical
residual map from $M$ to the residual-language DFA of its accepted language is injective if and
only if $M$ is state-separated, that is, any two states of $M$ with the same continuation
language are equal.

Formalized by `Cslib.Language.canonicalResidualHom_injective_iff`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Universal.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Universal.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/minimal-deterministic-automaton/index.html#canonical-residual-hom-injective-iff).

## States of an accessible, state-separated DFA correspond to residuals

Let $M$ be a DFA
that is accessible and state-separated, and let $L$ be the language it accepts. The map sending
each state $q$ of $M$ to the language of words accepted by $M$ starting from $q$ is a bijection
from the states of $M$ onto the set of left quotients $\{z : xz \in L\}$ of $L$ by words $x$.

Formalized by `Cslib.Language.stateEquivResidualsOfSeparated`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Universal.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Universal.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/minimal-deterministic-automaton/index.html#state-equiv-residuals-of-separated).

## Uniqueness of the canonical residual map

For an accessible DFA $M$ accepting the
language $L$, every DFA morphism from $M$ to the residual-language DFA of $L$ equals the
canonical residual map.

Formalized by `Cslib.Language.canonicalResidualHom_unique`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Universal.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Universal.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/minimal-deterministic-automaton/index.html#canonical-residual-hom-unique).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Minimal deterministic automaton](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/minimal-deterministic-automaton/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/regular-languages/minimization/minimal-deterministic-automaton)
