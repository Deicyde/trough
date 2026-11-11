---
declaration: section
origin: cited
lean: Cslib.Language.transitionAccept, Cslib.Language.recognizes_transitionAccept, Cslib.Language.recognizes_toTransitionMonoid, Cslib.Language.finite_stateTransformation, Cslib.Language.finite_transitionMonoid, Cslib.Language.finite_syntacticMonoid_of_isRegular, Cslib.Language.isRegular_iff_finite_syntacticMonoid, Cslib.Language.transitionMonoidToSyntactic
statement: formalized
proof: formalized
---

# Transition monoids and regularity

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/transition-monoids-and-regularity/index.html).

## Accepting transformations of a DFA

For a DFA $M$ with set of states $Q$, start state
$q_0$ and accepting states $F$, the accepting transformations of $M$ are the state
transformations $f$ of $Q$ with $f(q_0) \in F$.

Formalized by `Cslib.Language.transitionAccept`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Regularity.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/Congruences/Regularity.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/transition-monoids-and-regularity/index.html#transition-accept).

## The transition morphism recognizes through accepting transformations

Let $M$ be a DFA
with start state $q_0$ and accepting states $F$. The transition morphism of $M$, from words to
state transformations, recognizes the language accepted by $M$ through the accepting
transformations of $M$: a word is accepted by $M$ exactly when the transformation it induces
sends $q_0$ into $F$.

Formalized by `Cslib.Language.recognizes_transitionAccept`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Regularity.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/Congruences/Regularity.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/transition-monoids-and-regularity/index.html#recognizes-transition-accept).

## The transition monoid recognizes the accepted language

Let $M$ be a DFA with start
state $q_0$ and accepting states $F$. The map sending each word to the element of the transition
monoid of $M$ that it induces recognizes the language accepted by $M$, with accepting set the
elements $f$ of the transition monoid such that $f(q_0) \in F$: a word is accepted by $M$ exactly
when the transformation it induces sends $q_0$ into $F$.

Formalized by `Cslib.Language.recognizes_toTransitionMonoid`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Regularity.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/Congruences/Regularity.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/transition-monoids-and-regularity/index.html#recognizes-to-transition-monoid).

## Finitely many state transformations

If $Q$ is a finite set, then the monoid of state
transformations of $Q$, consisting of all functions $Q \to Q$ multiplied in diagrammatic order,
is finite.

Formalized by `Cslib.Language.finite_stateTransformation`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Regularity.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/Congruences/Regularity.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/transition-monoids-and-regularity/index.html#finite-state-transformation).

## Transition monoids of finite automata are finite

For every DFA $M$ with a finite set of
states, the transition monoid of $M$ is finite.

Formalized by `Cslib.Language.finite_transitionMonoid`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Regularity.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/Congruences/Regularity.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/transition-monoids-and-regularity/index.html#finite-transition-monoid).

## Regular languages have finite syntactic monoids

If $L$ is a regular language, then the
syntactic monoid of $L$ is finite.

Formalized by `Cslib.Language.finite_syntacticMonoid_of_isRegular`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Regularity.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/Congruences/Regularity.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/transition-monoids-and-regularity/index.html#finite-syntactic-monoid-of-is-regular).

## Regular languages are those with finite syntactic monoid

A language $L$ is regular if
and only if the syntactic monoid of $L$ is finite.

Formalized by `Cslib.Language.isRegular_iff_finite_syntacticMonoid`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Regularity.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/Congruences/Regularity.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/transition-monoids-and-regularity/index.html#is-regular-iff-finite-syntactic-monoid).

## The transition monoid maps to the syntactic monoid

For a DFA $M$ accepting the language
$L$, this is the monoid homomorphism from the transition monoid of $M$ to the syntactic monoid of
$L$ that sends the transformation induced by each word $w$ to the syntactic class of $w$.

Formalized by `Cslib.Language.transitionMonoidToSyntactic`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Regularity.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/Congruences/Regularity.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/transition-monoids-and-regularity/index.html#transition-monoid-to-syntactic).

## The syntactic monoid is no larger than the transition monoid

Let $M$ be a DFA
accepting the language $L$, and suppose that the transition monoid of $M$ and the syntactic
monoid of $L$ are both finite. Then the syntactic monoid of $L$ has at most as many elements as
the transition monoid of $M$.

Formalized by `Cslib.Language.card_syntacticMonoid_le_card_transitionMonoid`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Regularity.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/Congruences/Regularity.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/transition-monoids-and-regularity/index.html#card-syntactic-monoid-le-card-transition).

## Endofunction bound for the syntactic monoid

Let $M$ be a DFA with a finite
set of states $Q$, and suppose the syntactic monoid of the language accepted by $M$ is
finite. Then that syntactic monoid has at most $|Q|^{|Q|}$ elements.

Formalized by `Cslib.Language.card_syntacticMonoid_le_card_endofunction`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Regularity.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/Congruences/Regularity.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/transition-monoids-and-regularity/index.html#card-syntactic-monoid-le-card-endofuncti).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Transition monoids and regularity](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/transition-monoids-and-regularity/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/transition-monoids-and-regularity)
