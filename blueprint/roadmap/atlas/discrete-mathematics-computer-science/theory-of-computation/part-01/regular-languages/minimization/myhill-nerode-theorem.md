---
declaration: section
origin: cited
lean: Cslib.Language.nerodeRel, Cslib.Language.nerodeSetoid, Cslib.Language.NerodeClass, Cslib.Language.nerodeRel_iff, Cslib.Language.nerodeRel.mem_iff, Cslib.Language.nerodeRel_append_right, Cslib.Language.nerodeRel_append_singleton, Cslib.Language.nerodeRel_append_nil
statement: formalized
proof: formalized
---

# Myhill–Nerode theorem

34 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/myhill-nerode-theorem/index.html).

## Nerode equivalence

Let $L$ be a language over an alphabet $\Sigma$. Two words
$x, y \in \Sigma^*$ are Nerode equivalent for $L$ when they have the same left quotient, that is,
$\{z \in \Sigma^* \mid xz \in L\} = \{z \in \Sigma^* \mid yz \in L\}$.

Formalized by `Cslib.Language.nerodeRel`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Nerode.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Nerode.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/myhill-nerode-theorem/index.html#nerode-rel).

## The Nerode setoid

For a language $L$ over an alphabet $\Sigma$, the Nerode setoid of $L$
is the set $\Sigma^*$ of words equipped with Nerode equivalence for $L$, which is reflexive,
symmetric and transitive.

Formalized by `Cslib.Language.nerodeSetoid`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Nerode.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Nerode.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/myhill-nerode-theorem/index.html#nerode-setoid).

## Nerode classes

For a language $L$ over an alphabet $\Sigma$, the Nerode classes of $L$
are the elements of the quotient of the set of words over $\Sigma$ by Nerode equivalence for
$L$, under which two words $x$ and $y$ are equivalent when they have the same left quotient,
that is, when for every word $z$ we have $xz \in L$ if and only if $yz \in L$.

Formalized by `Cslib.Language.NerodeClass`, an abbreviation declared in [CSLibExt/Computability/Languages/Congruences/Nerode.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Nerode.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/myhill-nerode-theorem/index.html#nerode-class).

## Continuation characterization of Nerode equivalence

Let $L$ be a language over an
alphabet $\Sigma$. Two words $x, y \in \Sigma^*$ are Nerode equivalent for $L$ if and only if,
for every word $z \in \Sigma^*$, $xz \in L$ holds exactly when $yz \in L$.

Formalized by `Cslib.Language.nerodeRel_iff`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Nerode.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Nerode.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/myhill-nerode-theorem/index.html#nerode-rel-iff).

## Nerode equivalent words agree on membership

Let $L$ be a language. If two words $x$ and
$y$ are Nerode equivalent for $L$, then $x \in L$ if and only if $y \in L$.

Formalized by `Cslib.Language.nerodeRel.mem_iff`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Nerode.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Nerode.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/myhill-nerode-theorem/index.html#mem-iff).

## Nerode equivalence is a right congruence

Let $L$ be a language over an alphabet
$\Sigma$. If two words $x, y \in \Sigma^*$ are Nerode equivalent for $L$, then for every word
$z \in \Sigma^*$ the words $xz$ and $yz$ are Nerode equivalent for $L$.

Formalized by `Cslib.Language.nerodeRel_append_right`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Nerode.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Nerode.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/myhill-nerode-theorem/index.html#nerode-rel-append-right).

## Appending a symbol preserves Nerode equivalence

Let $L$ be a language over an alphabet
$\Sigma$. If two words $x, y \in \Sigma^*$ are Nerode equivalent for $L$, then for every symbol
$a \in \Sigma$ the words $xa$ and $ya$ are Nerode equivalent for $L$.

Formalized by `Cslib.Language.nerodeRel_append_singleton`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Nerode.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Nerode.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/myhill-nerode-theorem/index.html#nerode-rel-append-singleton).

## Appending the empty word preserves the Nerode class

Let $L$ be a language over an
alphabet $\Sigma$. For every word $x \in \Sigma^*$, the word $x\varepsilon$ obtained by appending
the empty word $\varepsilon$ is Nerode equivalent to $x$ for $L$.

Formalized by `Cslib.Language.nerodeRel_append_nil`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Nerode.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Nerode.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/myhill-nerode-theorem/index.html#nerode-rel-append-nil).

## Nerode class of a word

For a language $L$ and a word $x$, the Nerode class $[x]$ of $x$
is the equivalence class of $x$ under Nerode equivalence for $L$.

Formalized by `Cslib.Language.nerodeClass`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Nerode.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Nerode.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/myhill-nerode-theorem/index.html#nerode-class-2).

## Residual map on Nerode classes

Let $L$ be a language. The residual map sends the Nerode
class $[x]$ of a word $x$ to the left quotient $x^{-1}L = \{ y \mid xy \in L \}$, viewed as an
element of the set $\{ w^{-1}L \mid w \text{ a word} \}$ of left quotients of $L$. It is
well-defined because Nerode equivalent words have the same left quotient.

Formalized by `Cslib.Language.classResidual`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Nerode.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Nerode.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/myhill-nerode-theorem/index.html#class-residual).

## Bijection between Nerode classes and left quotients

For every language $L$, the map
sending the Nerode class $[x]$ of a word $x$ to the left quotient
$x^{-1}L = \{ y \mid xy \in L \}$ is a bijection from the set of Nerode classes of $L$ onto the
set $\{ w^{-1}L \mid w \text{ a word} \}$ of left quotients of $L$.

Formalized by `Cslib.Language.nerodeClassEquivResidual`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Nerode.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Nerode.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/myhill-nerode-theorem/index.html#nerode-class-equiv-residual).

## Transition on Nerode classes

Let $L$ be a language over an alphabet $\Sigma$ and
$a \in \Sigma$ a symbol. Appending $a$ sends the Nerode class of a word $x$ to the Nerode class
of $xa$; this is well defined because Nerode equivalence is preserved by appending a symbol.

Formalized by `Cslib.Language.NerodeClass.step`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Nerode.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Nerode.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/myhill-nerode-theorem/index.html#step).

## Accepting Nerode classes

Let $L$ be a language. The accepting Nerode classes of $L$ are
those whose words belong to $L$: the Nerode class $[x]$ of a word $x$ is accepting if and only if
$x \in L$. This is well-defined because Nerode equivalent words are either both in $L$ or both
outside $L$.

Formalized by `Cslib.Language.NerodeClass.Accepting`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Nerode.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Nerode.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/myhill-nerode-theorem/index.html#accepting).

## The Nerode automaton

Let $L$ be a language over an alphabet $\Sigma$. The Nerode
automaton of $L$ is the deterministic automaton over $\Sigma$, not necessarily finite, whose
states are the Nerode classes of words for $L$, whose start state is the class of the empty
word, which on reading a symbol $a \in \Sigma$ moves from the class of a word $x$ to the class
of $xa$, and whose accepting states are the classes of the words in $L$.

Formalized by `Cslib.Language.nerodeDFA`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Nerode.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Nerode.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/myhill-nerode-theorem/index.html#nerode-dfa).

## The Nerode automaton recognizes its language

For every language $L$, the language accepted
by the Nerode automaton of $L$ is exactly $L$.

Formalized by `Cslib.Language.accepts_nerodeDFA`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Nerode.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Nerode.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/myhill-nerode-theorem/index.html#accepts-nerode-dfa).

## Every state of the Nerode automaton is reachable

For every language $L$ and every
Nerode class $q$ of $L$, there is a word $x$ such that the Nerode automaton of $L$, started in
its start state and reading $x$, ends in the state $q$.

Formalized by `Cslib.Language.nerodeDFA_state_reachable`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Nerode.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Nerode.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/myhill-nerode-theorem/index.html#nerode-dfa-state-reachable).

## Finitely many Nerode classes iff finitely many left quotients

For every language $L$,
writing $x^{-1}L = \{ y \mid xy \in L \}$ for the left quotient of $L$ by a word $x$, there are
finitely many Nerode classes of $L$ if and only if the set $\{ x^{-1}L \mid x \text{ a word} \}$
of left quotients of $L$ is finite.

This is the quotient formulation of the Myhill--Nerode criterion.

Formalized by `Cslib.Language.finite_nerodeClass_iff`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Nerode.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Nerode.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/myhill-nerode-theorem/index.html#finite-nerode-class-iff).

## Myhill–Nerode theorem, quotient form

A language $L$ is regular, that is, accepted by some
deterministic finite automaton, if and only if $L$ has finitely many Nerode classes.

Formalized by `Cslib.Language.isRegular_iff_finite_nerodeClass`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Nerode.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Nerode.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/myhill-nerode-theorem/index.html#is-regular-iff-finite-nerode-class).

## Distinguishable words

Let $L$ be a language over an alphabet $\Sigma$. Two words $x$ and
$y$ over $\Sigma$ are distinguishable by $L$ when there is a word $z$ over $\Sigma$ such that
exactly one of $xz$ and $yz$ belongs to $L$.

Formalized by `Cslib.Language.Distinguishable`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Minimality.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Minimality.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/myhill-nerode-theorem/index.html#distinguishable).

## Words reaching the same DFA state are Nerode equivalent

Let $M$ be a DFA and let $L$ be
the language it accepts. If $M$ reaches the same state from its start state on reading the words
$x$ and $y$, then $x$ and $y$ are Nerode equivalent for $L$.

Formalized by `Cslib.Language.nerodeRel_of_eval_eq`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Minimality.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Minimality.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/myhill-nerode-theorem/index.html#nerode-rel-of-eval-eq).

## Distinguishable words reach different DFA states

Let $L$ be a language and let $M$ be
a DFA that accepts exactly $L$. If two words $x$ and $y$ are distinguishable by $L$, then the
states that $M$ reaches from its start state on reading $x$ and on reading $y$ are different.

Formalized by `Cslib.Language.eval_ne_of_distinguishable`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Minimality.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Minimality.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/myhill-nerode-theorem/index.html#eval-ne-of-distinguishable).

## Equivalent states of a DFA

Two states $p$ and $q$ of a DFA $M$ are equivalent when
they accept the same continuation language: for every word $z$, running $M$ from $p$ on $z$
ends in an accepting state if and only if running $M$ from $q$ on $z$ does.

Formalized by `Cslib.Language.StateEquivalent`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Minimality.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Minimality.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/myhill-nerode-theorem/index.html#state-equivalent).

## Nerode equivalence is equivalence of the reached states

Let $M$ be a DFA and let $L$ be
the language it accepts. Two words $x$ and $y$ are Nerode equivalent for $L$ if and only if the
states that $M$ reaches from its start state on reading $x$ and on reading $y$ are
observationally equivalent, that is, $M$ accepts the same language from both states.

Formalized by `Cslib.Language.nerodeRel_iff_stateEquivalent`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Minimality.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Minimality.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/myhill-nerode-theorem/index.html#nerode-rel-iff-state-equivalent).

## Residual languages of reachable states

For a DFA $M$ and a state $q$ of $M$, let $L_q$
be the language of words $z$ such that running $M$ from $q$ on $z$ ends in an accepting state.
The reachable residuals of $M$ form the set of the languages $L_q$ over all states $q$ that $M$
reaches from its start state on some input word.

This semantic state space forgets duplicate DFA states that accept the same continuations.

Formalized by `Cslib.Language.reachableResiduals`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Minimality.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Minimality.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/myhill-nerode-theorem/index.html#reachable-residuals).

## Nerode classes correspond to reachable residuals

Let $L$ be a language and let $M$ be
a DFA that accepts exactly $L$. This is the bijection from the Nerode classes of $L$ to the
reachable residuals of $M$, the languages accepted by $M$ from states it reaches from its start
state. It sends the Nerode class of a word $x$ to the left quotient $\{z \mid xz \in L\}$, which
is the language $M$ accepts from the state it reaches on reading $x$.

Formalized by `Cslib.Language.nerodeClassEquivReachableResiduals`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Minimality.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Minimality.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/myhill-nerode-theorem/index.html#nerode-class-equiv-reachable-residuals).

## Representative of a Nerode class

For a language $L$ and a Nerode class $q$ of $L$,
the representative of $q$ is a word whose Nerode class is $q$, chosen once and for all.

Formalized by `Cslib.Language.NerodeClass.representative`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Minimality.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Minimality.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/myhill-nerode-theorem/index.html#representative).

## Nerode classes to DFA states

For a language $L$ and a DFA $M$ over the same alphabet,
this map sends each Nerode class $q$ of $L$ to the state that $M$ reaches from its start
state on the chosen representative of $q$.

Unlike the canonical map from words to states, this does not claim that equivalent words reach
equal states in a nonminimal DFA.

Formalized by `Cslib.Language.NerodeClass.toDFAState`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Minimality.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Minimality.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/myhill-nerode-theorem/index.html#to-dfastate).

## Distinct Nerode classes reach distinct states

Let $M$ be a DFA that accepts exactly
the language $L$. Then the map sending each Nerode class of $L$ to the state that $M$ reaches
from its start state on the chosen representative of the class is injective. In particular, $M$
has at least one distinct state for each Nerode class.

Formalized by `Cslib.Language.NerodeClass.toDFAState_injective`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Minimality.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Minimality.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/myhill-nerode-theorem/index.html#to-dfastate-injective).

## Nerode classes bound the number of DFA states

Let $L$ be a language with finitely many
Nerode classes, and let $M$ be a DFA with a finite set of states $Q$ that accepts exactly $L$.
Then the number of Nerode classes of $L$ is at most $|Q|$.

Formalized by `Cslib.Language.card_nerodeClass_le_card_state`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Minimality.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Minimality.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/myhill-nerode-theorem/index.html#card-nerode-class-le-card-state).

## Myhill–Nerode lower bound via left quotients

Let $L$ be a language and let $M$ be a DFA
with a finite set of states $Q$ that accepts exactly $L$. For a word $x$, the left quotient of
$L$ by $x$ is the language $\{z \mid xz \in L\}$. Then the number of distinct left quotients of
$L$ is at most $|Q|$.

Formalized by `Cslib.Language.natCard_range_leftQuotient_le_natCard_state`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Minimality.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Minimality.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/myhill-nerode-theorem/index.html#nat-card-range-left-quotient-le-nat-card).

## Equality case of the Nerode state bound

Let $L$ be a language with finitely many
Nerode classes, and let $M$ be a DFA with a finite set of states $Q$ that accepts exactly $L$.
Send each Nerode class of $L$ to the state that $M$ reaches from its start state on the chosen
representative word of the class. Then the number of Nerode classes of $L$ equals $|Q|$ if and
only if every state in $Q$ is the image of some Nerode class under this map.

Formalized by `Cslib.Language.card_nerodeClass_eq_card_state_iff`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Minimality.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Minimality.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/myhill-nerode-theorem/index.html#card-nerode-class-eq-card-state-iff).

## Strict Nerode state bound

Let $L$ be a language with finitely many Nerode classes, and
let $M$ be a DFA with a finite set of states $Q$ that accepts exactly $L$. Send each Nerode
class of $L$ to the state that $M$ reaches from its start state on the chosen representative
word of the class. If some state in $Q$ is not the image of any Nerode class under this map,
then the number of Nerode classes of $L$ is strictly less than $|Q|$.

Formalized by `Cslib.Language.card_nerodeClass_lt_card_state`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Minimality.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Minimality.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/myhill-nerode-theorem/index.html#card-nerode-class-lt-card-state).

## Reachable state of a DFA

A state is reachable when some input word reaches it from the start state.

Formalized by `Cslib.Language.ReachableState`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Minimality.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Minimality.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/myhill-nerode-theorem/index.html#reachable-state).

## Accessible DFA

A DFA is accessible when every state is reachable.

Formalized by `Cslib.Language.Accessible`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Minimality.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Minimality.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/myhill-nerode-theorem/index.html#accessible).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Myhill–Nerode theorem](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/myhill-nerode-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/regular-languages/minimization/myhill-nerode-theorem)
