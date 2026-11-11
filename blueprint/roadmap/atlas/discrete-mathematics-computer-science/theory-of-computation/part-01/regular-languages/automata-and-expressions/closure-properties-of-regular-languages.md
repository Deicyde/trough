---
declaration: section
origin: cited
lean: Cslib.Language.HomImage.bound, Cslib.Language.HomImage.State, Cslib.Language.HomImage.advance, Cslib.Language.HomImage.εnfa, Cslib.Language.HomImage.code, Cslib.Language.HomImage.isPath_advance, Cslib.Language.HomImage.isPath_code, Cslib.Language.HomImage.exists_of_isPath
statement: formalized
proof: formalized
---

# Closure properties of regular languages

26 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/closure-properties-of-regular-languages/index.html).

## Maximal length of the image of a letter

For a map $\varphi$ from a finite alphabet $T$ to
words over $T'$, the bound is the maximum of the lengths $|\varphi(a)|$ over all letters $a \in T$
(and $0$ when $T$ is empty).

Formalized by `Cslib.Language.HomImage.bound`, a definition declared in [CSLibExt/Computability/Languages/RegularHomImage.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/RegularHomImage.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/closure-properties-of-regular-languages/index.html#bound).

## States of the homomorphic-image ε-NFA

Let $T$ be a finite alphabet, let $\varphi$ map
letters of $T$ to words over $T'$, let $\sigma$ be a set (the states of a DFA), and let $N$ be the
maximum of the lengths $|\varphi(a)|$ over $a \in T$. The states of the ε-NFA form the disjoint
union of $\sigma$ and the set of triples $(q, a, i)$ with $q \in \sigma$, $a \in T$ and
$0 \le i < N$.

Formalized by `Cslib.Language.HomImage.State`, an abbreviation declared in [CSLibExt/Computability/Languages/RegularHomImage.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/RegularHomImage.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/closure-properties-of-regular-languages/index.html#state).

## Next state while spelling out a letter's image

Let $M$ be a DFA over a finite alphabet $T$
with transition function $\delta$, and let $\varphi$ map each letter of $T$ to a word over $T'$. For
a state $q$ of $M$, a letter $a$ and a natural number $i$, the state reached after emitting position
$i$ (counted from $0$) of $\varphi(a)$ from $q$ is the intermediate state $(q, a, i + 1)$ of the
ε-NFA if $i + 1 < |\varphi(a)|$, and the state $\delta(q, a)$ of $M$ otherwise.

Formalized by `Cslib.Language.HomImage.advance`, a definition declared in [CSLibExt/Computability/Languages/RegularHomImage.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/RegularHomImage.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/closure-properties-of-regular-languages/index.html#advance).

## The ε-NFA for the homomorphic image

Let $M$ be a DFA over a finite alphabet $T$ with start
state $q_0$, transition function $\delta$ and accepting states $F$, let $\varphi$ map letters of $T$
to words over $T'$, and let $N$ be the maximum of the lengths $|\varphi(a)|$ over $a \in T$. The
ε-NFA over $T'$ has as states the states of $M$ together with the triples $(q, a, i)$ with $q$ a
state of $M$, $a \in T$ and $0 \le i < N$. Write $\mathrm{next}(q, a, i)$ for $(q, a, i + 1)$ if
$i + 1 < |\varphi(a)|$ and for $\delta(q, a)$ otherwise. From a state $q$ of $M$, reading $b$ leads
to $\mathrm{next}(q, a, 0)$ for each letter $a$ whose image starts with $b$, and an ε-move leads to
$\delta(q, a)$ for each letter $a$ with $\varphi(a)$ empty. From $(q, a, i)$, reading $b$ leads to
$\mathrm{next}(q, a, i)$ if the letter of $\varphi(a)$ at position $i$ (counted from $0$) is $b$,
and there are no ε-moves. The only start state is $q_0$ and the accepting states are those in
$F$.

Formalized by `Cslib.Language.HomImage.εnfa`, a definition declared in [CSLibExt/Computability/Languages/RegularHomImage.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/RegularHomImage.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/closure-properties-of-regular-languages/index.html#nfa).

## Edge labels for a letter's image

For a map $\varphi$ from letters of $T$ to words over $T'$
and a letter $a$, the label sequence of $a$ is a single ε-label when $\varphi(a)$ is empty, and
otherwise the letters of $\varphi(a)$ in order, each as a non-ε label.

Formalized by `Cslib.Language.HomImage.code`, a definition declared in [CSLibExt/Computability/Languages/RegularHomImage.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/RegularHomImage.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/closure-properties-of-regular-languages/index.html#code).

## Finishing a letter's image in the image ε-NFA

Let $M$ be a DFA over a finite alphabet $T$
with transition function $\delta$, and let $\varphi$ map letters of $T$ to words over $T'$. For
every state $q$ of $M$, letter $a$ and natural number $i$, the ε-NFA of $M$ and $\varphi$ has a path
to the state $\delta(q, a)$ of $M$ from the state $(q, a, i + 1)$ if $i + 1 < |\varphi(a)|$, and
from $\delta(q, a)$ otherwise, whose labels are the letters of $\varphi(a)$ after position $i$
(positions counted from $0$), in order and all non-ε.

Formalized by `Cslib.Language.HomImage.isPath_advance`, a theorem declared in [CSLibExt/Computability/Languages/RegularHomImage.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/RegularHomImage.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/closure-properties-of-regular-languages/index.html#is-path-advance).

## Spelling out a letter's image in the image ε-NFA

Let $M$ be a DFA over a finite alphabet
$T$ with transition function $\delta$, and let $\varphi$ map letters of $T$ to words over $T'$. For
every state $q$ of $M$ and letter $a$, the ε-NFA of $M$ and $\varphi$ has a path from the state $q$
to the state $\delta(q, a)$ whose label sequence is a single ε-label if $\varphi(a)$ is empty, and
the letters of $\varphi(a)$ in order, all non-ε, otherwise.

Formalized by `Cslib.Language.HomImage.isPath_code`, a theorem declared in [CSLibExt/Computability/Languages/RegularHomImage.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/RegularHomImage.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/closure-properties-of-regular-languages/index.html#is-path-code).

## Soundness of the homomorphic-image ε-NFA

Let $M$ be a DFA over a finite alphabet $T$ with
start state $q_0$, and let $\varphi$ map letters of $T$ to words over $T'$; for a word $w$ over $T$,
write $\varphi(w)$ for the concatenation of the images of its letters. Suppose the ε-NFA of $M$ and
$\varphi$ has a path from the state $q_0$ of $M$ to a state $u$, with label sequence $x$, and let
$\bar x$ be the word formed by the non-ε labels of $x$. If $u$ is a state $q$ of $M$, then there is
a word $w$ over $T$ on which $M$ reaches $q$ from $q_0$ and $\varphi(w) = \bar x$. If $u$ is the
intermediate state $(q, a, i)$, then there is a word $w$ over $T$ on which $M$ reaches $q$ from
$q_0$ and $\varphi(w)$ followed by the first $i$ letters of $\varphi(a)$ (all of $\varphi(a)$ if it
is shorter) equals $\bar x$.

Formalized by `Cslib.Language.HomImage.exists_of_isPath`, a theorem declared in [CSLibExt/Computability/Languages/RegularHomImage.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/RegularHomImage.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/closure-properties-of-regular-languages/index.html#exists-of-is-path).

## Homomorphic images of regular languages over finite alphabets are regular

Let $T$ be a
finite alphabet, $T'$ an arbitrary (possibly infinite) alphabet, and $\varphi$ a map from $T$ to
words over $T'$, extended to words by $\varphi(a_1 \cdots a_n) = \varphi(a_1) \cdots \varphi(a_n)$.
If $L$ is a regular language over $T$, then its image $\{\varphi(w) : w \in L\}$ is a regular
language over $T'$.

Formalized by `Cslib.Language.IsRegular.homImage`, a theorem declared in [CSLibExt/Computability/Languages/RegularHomImage.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/RegularHomImage.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/closure-properties-of-regular-languages/index.html#hom-image).

## DFA for the right quotient by a language

Given a DFA $M$ over an alphabet $T$ with state
set $\sigma$ and a language $R$ over $T$, this is the DFA with the same states, transition function
and start state as $M$, whose accepting states are the states $q$ from which some word of $R$
leads $M$ to an accepting state of $M$.

The accepting set is defined by quantifying over $R$, so it is not computable in general.

Formalized by `Cslib.Language.RegularQuotient.rightDFA`, a definition declared in [CSLibExt/Computability/Languages/RegularQuotient.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/RegularQuotient.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/closure-properties-of-regular-languages/index.html#right-dfa).

## NFA for the left quotient by a language

Given a DFA $M$ over an alphabet $T$ with state
set $\sigma$ and a language $R$ over $T$, this is the NFA with state set $\sigma$ and the same
accepting states as $M$, in which from a state $q$ on a letter $a$ the only possible move is to
the state $M$ reaches from $q$ on $a$, and whose start states are the states that $M$ reaches from
its start state on the words of $R$.

The set of start states is defined by quantifying over $R$, so it is not computable in general.

Formalized by `Cslib.Language.RegularQuotient.leftNFA`, a definition declared in [CSLibExt/Computability/Languages/RegularQuotient.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/RegularQuotient.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/closure-properties-of-regular-languages/index.html#left-nfa).

## Regular languages are closed under right quotients by arbitrary languages

If $L$ is a
regular language over an alphabet $T$ and $R$ is any language over $T$, then the right quotient
$\{x \mid \exists y \in R,\ xy \in L\}$ of $L$ by $R$ is regular.

Formalized by `Cslib.Language.IsRegular.rightQuotientSet`, a theorem declared in [CSLibExt/Computability/Languages/RegularQuotient.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/RegularQuotient.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/closure-properties-of-regular-languages/index.html#right-quotient-set).

## Regular languages are closed under left quotients by arbitrary languages

If $L$ is a
regular language over an alphabet $T$ and $R$ is any language over $T$, then the left quotient
$\{y \mid \exists x \in R,\ xy \in L\}$ of $L$ by $R$ is regular.

Formalized by `Cslib.Language.IsRegular.leftQuotientSet`, a theorem declared in [CSLibExt/Computability/Languages/RegularQuotient.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/RegularQuotient.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/closure-properties-of-regular-languages/index.html#left-quotient-set).

## Shuffle of two words

The relation "$w$ is a shuffle of $u$ and $v$" on words over $\alpha$
is defined inductively: the empty word is a shuffle of the empty word and the empty word, and if
$w$ is a shuffle of $u$ and $v$, then for every letter $a$ the word $aw$ is a shuffle of $au$ and
$v$, and a shuffle of $u$ and $av$. Thus $w$ interleaves the letters of $u$ and of $v$, keeping
their order within each word.

Formalized by `Cslib.Language.IsShuffle`, an inductive type declared in [CSLibExt/Computability/Languages/RegularShuffle.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/RegularShuffle.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/closure-properties-of-regular-languages/index.html#is-shuffle).

## Shuffle of two languages

For languages $L$ and $M$ over $\alpha$, the shuffle of $L$ and
$M$ is the language of all words $w$ over $\alpha$ such that $w$ is a shuffle of some word $u \in L$
and some word $v \in M$, that is, $w$ interleaves $u$ and $v$.

Formalized by `Cslib.Language.shuffle`, a definition declared in [CSLibExt/Computability/Languages/RegularShuffle.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/RegularShuffle.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/closure-properties-of-regular-languages/index.html#shuffle).

## Cyclic shift of a language

For a language $L$ over $\alpha$, the cyclic shift of $L$ is
the language of all words $yx$ over $\alpha$ such that $xy \in L$ for some words $x$ and $y$; that
is, the language of all rotations of the words of $L$.

Formalized by `Cslib.Language.cyclicShift`, a definition declared in [CSLibExt/Computability/Languages/RegularShuffle.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/RegularShuffle.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/closure-properties-of-regular-languages/index.html#cyclic-shift).

## Shuffle automaton of two DFAs

Let $M$ and $N$ be DFAs over $\alpha$ with state types
$\sigma$ and $\tau$, start states $s_M$ and $s_N$, sets of accepting states $F_M$ and $F_N$, and
transition functions $\delta_M$ and $\delta_N$. Their shuffle automaton is the NFA over $\alpha$
with state type $\sigma \times \tau$, the single start state $(s_M, s_N)$ and accepting states
$F_M \times F_N$, which on a letter $a$ moves from a state $(p, q)$ to the two states
$(\delta_M(p, a), q)$ and $(p, \delta_N(q, a))$.

Formalized by `Cslib.Language.RegularShuffle.shuffleNFA`, a definition declared in [CSLibExt/Computability/Languages/RegularShuffle.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/RegularShuffle.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/closure-properties-of-regular-languages/index.html#shuffle-nfa).

## Words leading a DFA from a state into a set of states

For a DFA $M$ over $\alpha$ with
state type $\sigma$, a state $p \in \sigma$ and a set $S \subseteq \sigma$ of states, this is the
language of all words $w$ over $\alpha$ such that the run of $M$ started in $p$ on $w$ ends in a
state of $S$.

Formalized by `Cslib.Language.RegularShuffle.fromTo`, a definition declared in [CSLibExt/Computability/Languages/RegularShuffle.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/RegularShuffle.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/closure-properties-of-regular-languages/index.html#from-to).

## The shuffle of two regular languages is regular

**The shuffle of two regular languages is regular.**

Formalized by `Cslib.Language.IsRegular.shuffle`, a theorem declared in [CSLibExt/Computability/Languages/RegularShuffle.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/RegularShuffle.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/closure-properties-of-regular-languages/index.html#shuffle-2).

## The cyclic shifts of the words of a regular language form a regular language

**The cyclic shifts of the words of a regular language form a regular language.**

Formalized by `Cslib.Language.IsRegular.cyclicShift`, a theorem declared in [CSLibExt/Computability/Languages/RegularShuffle.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/RegularShuffle.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/closure-properties-of-regular-languages/index.html#cyclic-shift-2).

## Substitution of languages for letters

Let $L$ be a language over an alphabet $T$, and let
$s$ assign to each letter $a \in T$ a language $s(a)$ over an alphabet $T'$. The substitution of
$s$ into $L$ is the language over $T'$ of all words $y_1 y_2 \cdots y_n$ for which there is a word
$a_1 a_2 \cdots a_n \in L$ with $y_i \in s(a_i)$ for every $i$.

Formalized by `Cslib.Language.substitution`, a definition declared in [CSLibExt/Computability/Languages/Substitution.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/Substitution.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/closure-properties-of-regular-languages/index.html#substitution-2).

## The ε-NFA for a substitution

Let $M$ be a DFA over $T$ with states $\sigma$, and for each
letter $a \in T$ let $N_a$ be a DFA over $T'$ with states $\tau_a$. This ε-NFA over $T'$ has as
states the states $q$ of $M$ and the triples $(q, a, p)$ with $q$ a state of $M$, $a \in T$ and
$p$ a state of $N_a$, read as the state $p$ of the copy of $N_a$ entered from $q$. A state $q$ of
$M$ has an ε-move to $(q, a, s_a)$ for every $a \in T$, where $s_a$ is the start state of $N_a$,
and no letter moves. A state $(q, a, p)$ moves on a letter $b$ to $(q, a, \delta_a(p, b))$, where
$\delta_a$ is the transition function of $N_a$, and has an ε-move, to the state $\delta_M(q, a)$
of $M$, exactly when $p$ is an accepting state of $N_a$; here $\delta_M$ is the transition
function of $M$. The start state is the start state of $M$, and the accepting states are the
accepting states of $M$.

Formalized by `Cslib.Language.RegularSubstitution.εnfa`, a definition declared in [CSLibExt/Computability/Languages/RegularSubstitution.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/RegularSubstitution.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/closure-properties-of-regular-languages/index.html#nfa-2).

## Paths inside one copy of a letter automaton

Let $M$ be a DFA over $T$, and for each
letter $a \in T$ let $N_a$ be a DFA over $T'$. For every state $q$ of $M$, letter $a \in T$,
state $p$ of $N_a$ and word $y$ over $T'$, the ε-NFA built from $M$ and the $N_a$ has a path
reading the letters of $y$, with no ε-moves, from the state $p$ of the copy of $N_a$ entered from
$q$ to the state of the same copy that $N_a$ reaches from $p$ on $y$.

Formalized by `Cslib.Language.RegularSubstitution.isPath_run`, a theorem declared in [CSLibExt/Computability/Languages/RegularSubstitution.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/RegularSubstitution.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/closure-properties-of-regular-languages/index.html#is-path-run).

## Detour labels

For a word $y = b_1 \cdots b_n$ over $T'$, the detour labels of $y$ are
the sequence of ε-NFA labels $\varepsilon, b_1, \ldots, b_n, \varepsilon$: an ε-move, the letters
of $y$ in order, and a final ε-move.

They label the detour that the substitution ε-NFA takes through a copy of the automaton for one
letter.

Formalized by `Cslib.Language.RegularSubstitution.detour`, a definition declared in [CSLibExt/Computability/Languages/RegularSubstitution.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/RegularSubstitution.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/closure-properties-of-regular-languages/index.html#detour).

## Soundness of the paths of the substitution ε-NFA

Let $M$ be a DFA over $T$ with start
state $q_0$, and for each letter $a \in T$ let $N_a$ be a DFA over $T'$, with accepted language
$L(N_a)$; for a word $w = a_1 \cdots a_n$ over $T$ write $L_w = L(N_{a_1}) \cdots L(N_{a_n})$,
which is $\{\varepsilon\}$ when $w$ is empty. Let $x$ be a sequence of labels, each a letter of
$T'$ or $\varepsilon$, let $\bar x$ be the word over $T'$ obtained from $x$ by deleting the
$\varepsilon$'s, and suppose the ε-NFA built from $M$ and the $N_a$ has a path reading $x$ from
the state $q_0$ of $M$ to a state $u$. If $u$ is a state $q$ of $M$, then there is a word $w$
over $T$ such that $M$ reaches $q$ from $q_0$ on $w$ and $\bar x \in L_w$. If $u$ is the state
$p$ of the copy of $N_a$ entered from the state $q$ of $M$, then there are a word $w$ over $T$
such that $M$ reaches $q$ from $q_0$ on $w$, a word $y_1 \in L_w$ and a word $y_2$ over $T'$
such that $\bar x = y_1 y_2$ and $N_a$ reaches $p$ from its start state on $y_2$.

Formalized by `Cslib.Language.RegularSubstitution.exists_of_isPath`, a theorem declared in [CSLibExt/Computability/Languages/RegularSubstitution.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/RegularSubstitution.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/closure-properties-of-regular-languages/index.html#exists-of-is-path-2).

## Regular languages are closed under substitution over a finite alphabet

Let $T$ be a
finite alphabet and $T'$ any alphabet. If $L$ is a regular language over $T$ and $s(a)$ is a
regular language over $T'$ for every letter $a \in T$, then the substitution of $s$ into $L$ is a
regular language over $T'$.

Formalized by `Cslib.Language.IsRegular.substitution`, a theorem declared in [CSLibExt/Computability/Languages/RegularSubstitution.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/RegularSubstitution.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/closure-properties-of-regular-languages/index.html#substitution).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Closure properties of regular languages](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/closure-properties-of-regular-languages/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/closure-properties-of-regular-languages)
