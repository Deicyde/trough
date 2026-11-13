---
declaration: section
origin: cited
lean: Cslib.Language.syntacticRel, Cslib.Language.syntacticRel_prefix, Cslib.Language.syntacticRel_suffix, Cslib.Language.syntacticRel_append, Cslib.Language.syntacticCon, Cslib.Language.SyntacticMonoid, Cslib.Language.syntacticMorphism, Cslib.Language.syntacticRel_mem_iff
statement: formalized
proof: formalized
---

# Syntactic monoid

45 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/syntactic-monoid/index.html).

## Syntactic equivalence

Let $L$ be a language over an alphabet $\Sigma$. Two words
$x, y \in \Sigma^*$ are syntactically equivalent for $L$ when, for all words $u, v \in \Sigma^*$,
$uxv \in L$ if and only if $uyv \in L$.

Formalized by `Cslib.Language.syntacticRel`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Syntactic.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Syntactic.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/syntactic-monoid/index.html#syntactic-rel).

## Syntactic equivalence is stable under left multiplication

Let $L$ be a language over an
alphabet $\Sigma$. If two words $x, y \in \Sigma^*$ are syntactically equivalent for $L$, then
for every word $w \in \Sigma^*$ the words $wx$ and $wy$ are syntactically equivalent for $L$.

Formalized by `Cslib.Language.syntacticRel_prefix`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Syntactic.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Syntactic.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/syntactic-monoid/index.html#syntactic-rel-prefix).

## Syntactic equivalence is stable under right multiplication

Let $L$ be a language over an
alphabet $\Sigma$. If two words $x, y \in \Sigma^*$ are syntactically equivalent for $L$, then
for every word $w \in \Sigma^*$ the words $xw$ and $yw$ are syntactically equivalent for $L$.

Formalized by `Cslib.Language.syntacticRel_suffix`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Syntactic.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Syntactic.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/syntactic-monoid/index.html#syntactic-rel-suffix).

## Syntactic equivalence is compatible with concatenation

Let $L$ be a language over an
alphabet $\Sigma$ and let $w, x, y, z \in \Sigma^*$ be words. If $w$ and $x$ are syntactically
equivalent for $L$, and $y$ and $z$ are syntactically equivalent for $L$, then $wy$ and $xz$ are
syntactically equivalent for $L$.

Formalized by `Cslib.Language.syntacticRel_append`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Syntactic.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Syntactic.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/syntactic-monoid/index.html#syntactic-rel-append).

## Syntactic congruence

For a language $L$ over an alphabet $\Sigma$, the syntactic
congruence of $L$ is the monoid congruence on the free monoid $\Sigma^*$ that relates words $x$
and $y$ when, for all words $u$ and $v$, $uxv \in L$ if and only if $uyv \in L$.

Formalized by `Cslib.Language.syntacticCon`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Syntactic.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Syntactic.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/syntactic-monoid/index.html#syntactic-con).

## Syntactic monoid

For a language $L$ over an alphabet $\Sigma$, the syntactic monoid of
$L$ is the quotient of the free monoid $\Sigma^*$ of words by the syntactic congruence of $L$,
which relates words $x$ and $y$ when $uxv \in L \iff uyv \in L$ for all words $u$ and $v$.

Formalized by `Cslib.Language.SyntacticMonoid`, an abbreviation declared in [CSLibExt/Computability/Languages/Congruences/Syntactic.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Syntactic.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/syntactic-monoid/index.html#syntactic-monoid).

## Syntactic morphism

For a language $L$ over an alphabet $\Sigma$, the syntactic morphism
of $L$ is the monoid homomorphism from the free monoid $\Sigma^*$ of words to the syntactic
monoid of $L$ that sends each word to its class under the syntactic congruence of $L$.

Formalized by `Cslib.Language.syntacticMorphism`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Syntactic.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Syntactic.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/syntactic-monoid/index.html#syntactic-morphism).

## Syntactically equivalent words agree on membership

Let $L$ be a language over an
alphabet $\Sigma$. If two words $x, y \in \Sigma^*$ are syntactically equivalent for $L$, then
$x \in L$ if and only if $y \in L$.

Formalized by `Cslib.Language.syntacticRel_mem_iff`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Syntactic.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Syntactic.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/syntactic-monoid/index.html#syntactic-rel-mem-iff).

## Accepting set of the syntactic monoid

For a language $L$, the accepting set of the
syntactic monoid of $L$ is the set of syntactic classes of words of $L$: a class belongs to it
when its representatives lie in $L$, which does not depend on the representative chosen.

Formalized by `Cslib.Language.syntacticAccept`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Syntactic.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Syntactic.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/syntactic-monoid/index.html#syntactic-accept).

## The syntactic morphism recognizes the language

Let $L$ be a language over an alphabet
$\Sigma$. For every word $x \in \Sigma^*$, $x \in L$ if and only if the image of $x$ under the
syntactic morphism of $L$ lies in the accepting set of the syntactic monoid of $L$, the set of
syntactic classes of words of $L$.

Formalized by `Cslib.Language.mem_iff_syntacticMorphism_mem`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Syntactic.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Syntactic.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/syntactic-monoid/index.html#mem-iff-syntactic-morphism-mem).

## Syntactic equivalence refines Nerode equivalence

Let $L$ be a language over an alphabet
$\Sigma$. If two words $x, y \in \Sigma^*$ are syntactically equivalent for $L$, then they are
Nerode equivalent for $L$: the sets $\{z : xz \in L\}$ and $\{z : yz \in L\}$ are equal.

Formalized by `Cslib.Language.syntacticRel_nerodeRel`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Syntactic.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Syntactic.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/syntactic-monoid/index.html#syntactic-rel-nerode-rel).

## Equal syntactic classes give equal Nerode classes

Let $L$ be a language. For all words
$x$ and $y$, if the syntactic morphism of $L$ sends $x$ and $y$ to the same element of the
syntactic monoid of $L$, then $x$ and $y$ have the same Nerode class with respect to $L$.

Formalized by `Cslib.Language.nerodeClass_eq_of_syntacticMorphism_eq`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Syntactic.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Syntactic.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/syntactic-monoid/index.html#nerode-class-eq-of-syntactic-morphism-eq).

## Transition action of a word

For a DFA $M$ and a word $x$, the transition action of $x$ is
the map sending each state $q$ of $M$ to the state that $M$ reaches by reading $x$ starting
from $q$.

Formalized by `Cslib.Language.transitionAction`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Syntactic.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Syntactic.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/syntactic-monoid/index.html#transition-action).

## Words with the same transition action are syntactically equivalent

Let $M$ be a DFA over
an alphabet $\Sigma$ and let $L$ be the language accepted by $M$. If two words
$x, y \in \Sigma^*$ have the same transition action on $M$, that is, for every state $q$, running
$M$ from $q$ on $x$ ends in the same state as running $M$ from $q$ on $y$, then $x$ and $y$ are
syntactically equivalent for $L$.

Formalized by `Cslib.Language.syntacticRel_of_transitionAction_eq`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Syntactic.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Syntactic.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/syntactic-monoid/index.html#syntactic-rel-of-transition-action-eq).

## Syntactically equivalent words act identically

Let $M$ be a DFA that is accessible
(every state is reachable from the start state) and state-separated (two states with the same
continuation language are equal). If two words $x$ and $y$ are syntactically equivalent for the
language accepted by $M$, then $x$ and $y$ have the same transition action on $M$: for every
state $q$, reading $x$ from $q$ and reading $y$ from $q$ lead to the same state.

Formalized by `Cslib.Language.transitionAction_eq_of_syntacticRel`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Syntactic.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Syntactic.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/syntactic-monoid/index.html#transition-action-eq-of-syntactic-rel).

## Syntactic equivalence via transition actions

Let $M$ be a DFA over an alphabet $\Sigma$
that is accessible (every state is reached from the start state by some word) and
state-separated (distinct states have distinct continuation languages), and let $L$ be the
language accepted by $M$. Then two words $x, y \in \Sigma^*$ are syntactically equivalent for $L$
if and only if they have the same transition action on $M$: for every state $q$, running $M$
from $q$ on $x$ ends in the same state as running $M$ from $q$ on $y$.

Formalized by `Cslib.Language.syntacticRel_iff_transitionAction_eq`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Syntactic.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Syntactic.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/syntactic-monoid/index.html#syntactic-rel-iff-transition-action-eq).

## State transformation monoid

For a type $Q$ of states, the state transformation monoid
of $Q$ consists of all functions $Q \to Q$, multiplied by composition in the opposite order: the
product $fg$ first applies $f$ and then $g$, so $(fg)(q) = g(f(q))$, and the unit is the
identity function.

Formalized by `Cslib.Language.StateTransformation`, an abbreviation declared in [CSLibExt/Computability/Languages/Congruences/Syntactic.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Syntactic.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/syntactic-monoid/index.html#state-transformation).

## State transformations as functions

For a type $Q$ of states, the bijection from the
state transformations of $Q$ to the functions $Q \to Q$ that sends each transformation to its
underlying function; it forgets the multiplication of state transformations.

Formalized by `Cslib.Language.stateTransformationEquiv`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Syntactic.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Syntactic.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/syntactic-monoid/index.html#state-transformation-equiv).

## Transition transformation of a word

For a DFA $M$ and a word $x$, the transition
transformation of $x$ is the transition action of $x$, the map sending each state $q$ to the
state that $M$ reaches by reading $x$ from $q$, regarded as an element of the monoid of state
transformations of $M$ (multiplied in reading order: $fg$ applies $f$ first, then $g$).

Formalized by `Cslib.Language.transitionTransformation`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Syntactic.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Syntactic.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/syntactic-monoid/index.html#transition-transformation).

## Transition morphism of a DFA

For a DFA $M$, the transition morphism is the monoid
homomorphism from the free monoid of words to the state transformations of $M$ that sends each
word $x$ to its transition action, the map taking each state $q$ to the state that $M$ reaches
by reading $x$ from $q$. State transformations are multiplied in reading order, so the product
$fg$ applies $f$ first and then $g$; with this order, the word $xy$ is sent to the product of
the images of $x$ and $y$.

Formalized by `Cslib.Language.transitionMorphism`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Syntactic.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Syntactic.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/syntactic-monoid/index.html#transition-morphism).

## Transition monoid of a DFA

The transition monoid of a DFA $M$ is the image of the
transition morphism of $M$: the submonoid of state transformations of $M$ consisting of the
transition actions of all words, where a word $x$ acts by sending each state $q$ to the state
that $M$ reaches by reading $x$ from $q$. State transformations are multiplied in reading
order, so the product $fg$ applies $f$ first and then $g$.

Formalized by `Cslib.Language.TransitionMonoid`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Syntactic.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Syntactic.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/syntactic-monoid/index.html#transition-monoid).

## Transition monoid element of a word

Let $M$ be a DFA over an alphabet $\Sigma$. Each word
$x \in \Sigma^*$ determines the element of the transition monoid of $M$ given by the state
transformation that sends each state $q$ to the state $M$ reaches from $q$ after reading $x$.

Formalized by `Cslib.Language.toTransitionMonoid`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Syntactic.lean, line 265](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Syntactic.lean#L265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/syntactic-monoid/index.html#to-transition-monoid).

## Syntactic congruence as a kernel

Let $M$ be an accessible, state-separated DFA and let
$L$ be the language $M$ accepts. The syntactic congruence of $L$ equals the kernel of the
transition morphism of $M$: two words are syntactically equivalent for $L$ if and only if they
induce the same transformation of the states of $M$.

Formalized by `Cslib.Language.syntacticCon_eq_transitionMorphism_ker`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Syntactic.lean, line 299](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Syntactic.lean#L299). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/syntactic-monoid/index.html#syntactic-con-eq-transition-morphism-ker).

## Action of the syntactic monoid on states

Let $M$ be an accessible, state-separated DFA
with state type $Q$, and let $L$ be the language $M$ accepts. This is the monoid homomorphism
from the syntactic monoid of $L$ to the state transformation monoid of $Q$ that sends the
syntactic class of each word $x$ to the map taking each state $q$ to the state $M$ reaches from
$q$ by reading $x$. It is well defined because syntactically equivalent words act identically on
the states of such a DFA.

Formalized by `Cslib.Language.syntacticActionHom`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Syntactic.lean, line 309](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Syntactic.lean#L309). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/syntactic-monoid/index.html#syntactic-action-hom).

## Image of the syntactic action

Let $M$ be an accessible, state-separated DFA and let $L$
be the language $M$ accepts. The image of the action of the syntactic monoid of $L$ on the states
of $M$, the monoid homomorphism sending the syntactic class of each word $x$ to the state
transformation induced by reading $x$, is exactly the transition monoid of $M$.

Formalized by `Cslib.Language.syntacticActionHom_range`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Syntactic.lean, line 337](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Syntactic.lean#L337). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/syntactic-monoid/index.html#syntactic-action-hom-range).

## Recognition of a language by a monoid morphism

Let $L$ be a language over an alphabet
$\Sigma$, let $\varphi : \Sigma^* \to M$ be a monoid morphism from the free monoid on $\Sigma$
into a monoid $M$, and let $A \subseteq M$. Then $\varphi$ recognizes $L$ through $A$ when, for
every word $w \in \Sigma^*$, $w \in L$ if and only if $\varphi(w) \in A$.

Formalized by `Cslib.Language.Recognizes`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Recognition.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Recognition.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/syntactic-monoid/index.html#recognizes).

## The syntactic morphism recognizes its language

For every language $L$ over an alphabet
$\Sigma$, the syntactic morphism of $L$, from the free monoid $\Sigma^*$ to the syntactic monoid
of $L$, recognizes $L$ through the accepting subset of the syntactic monoid, namely the set of
syntactic classes of words in $L$.

Formalized by `Cslib.Language.recognizes_syntacticMorphism`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Recognition.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Recognition.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/syntactic-monoid/index.html#recognizes-syntactic-morphism).

## Recognition pulls back along a factorization

Let $L$ be a language over an
alphabet $\Sigma$ and let $\varphi : \Sigma^* \to C$ be a monoid morphism from the free monoid
$\Sigma^*$ that recognizes $L$ through a subset $A \subseteq C$. If $\varphi = f \circ \psi$ for
monoid morphisms $\psi : \Sigma^* \to T$ and $f : T \to C$, then $\psi$ recognizes $L$ through the
preimage $f^{-1}(A)$.

Formalized by `Cslib.Language.Recognizes.comp`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Recognition.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Recognition.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/syntactic-monoid/index.html#comp).

## Words with equal recognizer images are syntactically equivalent

Let
$\varphi : \Sigma^* \to M$ be a monoid morphism from the free monoid on an alphabet $\Sigma$ into
a monoid $M$ that recognizes a language $L$ over $\Sigma$ through a set $A \subseteq M$. If two
words $x, y \in \Sigma^*$ satisfy $\varphi(x) = \varphi(y)$, then $x$ and $y$ are syntactically
equivalent for $L$: for all words $u, v \in \Sigma^*$, $uxv \in L$ if and only if $uyv \in L$.

Formalized by `Cslib.Language.syntacticRel_of_recognizer_eq`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Recognition.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Recognition.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/syntactic-monoid/index.html#syntactic-rel-of-recognizer-eq).

## Recognizer kernels refine the syntactic congruence

If a monoid morphism $\varphi$ from the
free monoid $\Sigma^*$ recognizes a language $L$ over $\Sigma$ through a subset $A$ of its
codomain, then the kernel congruence of $\varphi$ is contained in the syntactic congruence of $L$:
any words $x, y$ with $\varphi(x) = \varphi(y)$ are syntactically equivalent for $L$.

Formalized by `Cslib.Language.recognizer_ker_le_syntacticCon`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Recognition.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Recognition.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/syntactic-monoid/index.html#recognizer-ker-le-syntactic-con).

## Canonical map from a recognizer's kernel quotient to the syntactic monoid

Let $L$ be a
language over an alphabet $\Sigma$, let $\varphi : \Sigma^* \to M$ be a monoid morphism from the
free monoid on $\Sigma$ into a monoid $M$, and let $A \subseteq M$ be such that $\varphi$
recognizes $L$ through $A$. Since the kernel congruence of $\varphi$ (words $x, y$ with
$\varphi(x) = \varphi(y)$) is contained in the syntactic congruence of $L$, there is a monoid
morphism from the quotient of $\Sigma^*$ by the kernel of $\varphi$ to the syntactic monoid of
$L$ sending the class of each word $w$ to the syntactic class of $w$.

This is the algebraic minimality map before identifying the kernel quotient with the image of
the recognizer.

Formalized by `Cslib.Language.recognizerQuotientToSyntactic`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Recognition.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Recognition.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/syntactic-monoid/index.html#recognizer-quotient-to-syntactic).

## The kernel quotient of a recognizer maps onto the syntactic monoid

If a monoid morphism
$\varphi$ from the free monoid $\Sigma^*$ recognizes a language $L$ over $\Sigma$ through a subset
$A$ of its codomain, then the canonical monoid morphism from the quotient of $\Sigma^*$ by the
kernel congruence of $\varphi$ to the syntactic monoid of $L$, which sends the class of a word
$x$ to its syntactic class, is surjective.

Formalized by `Cslib.Language.recognizerQuotientToSyntactic_surjective`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Recognition.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Recognition.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/syntactic-monoid/index.html#recognizer-quotient-to-syntactic-surject).

## Map from a recognizer's image to the syntactic monoid

Let $\varphi : \Sigma^* \to M$ be a
monoid morphism from the free monoid $\Sigma^*$ that recognizes a language $L$ over $\Sigma$
through a subset $A \subseteq M$. This is the monoid morphism from the image $\varphi(\Sigma^*)$
to the syntactic monoid of $L$ that sends $\varphi(x)$ to the syntactic class of $x$ for every
word $x$. It is well defined because words with the same image under $\varphi$ are syntactically
equivalent for $L$.

Formalized by `Cslib.Language.recognizerImageToSyntactic`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Recognition.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Recognition.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/syntactic-monoid/index.html#recognizer-image-to-syntactic).

## The image of a recognizer maps onto the syntactic monoid

Let $\varphi : \Sigma^* \to M$ be
a monoid morphism from the free monoid $\Sigma^*$ that recognizes a language $L$ over $\Sigma$
through a subset $A \subseteq M$. Then the canonical monoid morphism from the image
$\varphi(\Sigma^*)$ to the syntactic monoid of $L$, which sends $\varphi(x)$ to the syntactic class
of $x$, is surjective.

Formalized by `Cslib.Language.recognizerImageToSyntactic_surjective`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Recognition.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Recognition.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/syntactic-monoid/index.html#recognizer-image-to-syntactic-surjective).

## Finite recognizers give finite syntactic monoids

If a monoid morphism from the free monoid
$\Sigma^*$ to a finite monoid $M$ recognizes a language $L$ over $\Sigma$ through some subset of
$M$, then the syntactic monoid of $L$ is finite.

Formalized by `Cslib.Language.finite_syntacticMonoid_of_recognizer`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Recognition.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Recognition.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/syntactic-monoid/index.html#finite-syntactic-monoid-of-recognizer).

## Recognition as an inverse image

Let $L$ be a language over an alphabet $\Sigma$, let
$\varphi : \Sigma^* \to M$ be a monoid morphism from the free monoid on $\Sigma$ into a monoid
$M$, and let $A \subseteq M$. Then $\varphi$ recognizes $L$ through $A$ if and only if the set
of words of $\Sigma^*$ that belong to $L$ equals $\varphi^{-1}(A)$.

Formalized by `Cslib.Language.recognizes_iff_preimage`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Recognition.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Recognition.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/syntactic-monoid/index.html#recognizes-iff-preimage).

## Changing the accepting set off the image of a recognizer

Let $\varphi : \Sigma^* \to M$ be
a monoid morphism from the free monoid $\Sigma^*$ that recognizes a language $L$ over $\Sigma$
through a subset $A_1 \subseteq M$. If $A_2 \subseteq M$ satisfies
$\varphi(x) \in A_1 \iff \varphi(x) \in A_2$ for every word $x$, then $\varphi$ also recognizes $L$
through $A_2$.

Formalized by `Cslib.Language.Recognizes.congr_accept`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Recognition.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Recognition.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/syntactic-monoid/index.html#congr-accept).

## The syntactic DFA

Let $L$ be a language over an alphabet $\Sigma$. The syntactic DFA of
$L$ has the syntactic monoid of $L$ as its set of states, the identity $1$ as start state, and
the syntactic classes of the words of $L$ as accepting states; from a state $q$, reading a
letter $a \in \Sigma$ leads to $q \cdot [a]$, where $[a]$ is the syntactic class of the
one-letter word $a$.

It is the direct automata-theoretic presentation of the canonical syntactic recognizer.

Formalized by `Cslib.Language.syntacticDFA`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Recognition.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Recognition.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/syntactic-monoid/index.html#syntactic-dfa).

## Runs of the syntactic DFA

Let $L$ be a language over an alphabet $\Sigma$. For every
state $q$ of the syntactic DFA of $L$ (an element of the syntactic monoid of $L$) and every word
$x \in \Sigma^*$, the state reached from $q$ by reading $x$ is $q \cdot [x]$, where $[x]$ is the
image of $x$ under the syntactic morphism of $L$.

Formalized by `Cslib.Language.syntacticDFA_evalFrom`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Recognition.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Recognition.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/syntactic-monoid/index.html#syntactic-dfa-eval-from).

## The syntactic DFA accepts its language

For every language $L$, the syntactic DFA of $L$
accepts exactly $L$.

Formalized by `Cslib.Language.syntacticDFA_accepts`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Recognition.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Recognition.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/syntactic-monoid/index.html#syntactic-dfa-accepts).

## The syntactic DFA is accessible

For every language $L$, every state of the syntactic DFA
of $L$ is reachable: some word leads to it from the start state.

Formalized by `Cslib.Language.syntacticDFA_accessible`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Recognition.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Recognition.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/syntactic-monoid/index.html#syntactic-dfa-accessible).

## Finite syntactic monoid implies regularity

Every language whose syntactic monoid is
finite is regular.

Formalized by `Cslib.Language.isRegular_of_finite_syntacticMonoid`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Recognition.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Recognition.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/syntactic-monoid/index.html#is-regular-of-finite-syntactic-monoid).

## The syntactic DFA of a language with finite syntactic monoid

If the syntactic monoid of a
language $L$ is finite, then the syntactic DFA of $L$ has finitely many states and accepts exactly
$L$.

This gives a specific finite recognizer, the syntactic DFA, rather than merely the existence of
some finite DFA.

Formalized by `Cslib.Language.exists_finite_syntacticDFA`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Recognition.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Recognition.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/syntactic-monoid/index.html#exists-finite-syntactic-dfa).

## The transition morphism of a DFA recognizes its language

Let $M$ be a DFA over an
alphabet $\Sigma$ with state set $Q$, start state $q_0$ and set of accepting states $F$. The
transition morphism of $M$, from the free monoid $\Sigma^*$ to the monoid of state
transformations of $Q$, recognizes the language accepted by $M$ through the set of
transformations $f$ with $f(q_0) \in F$.

No accessibility or state-separation hypothesis on $M$ is needed.

Formalized by `Cslib.Language.recognizes_transitionMorphism`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Recognition.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Recognition.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/syntactic-monoid/index.html#recognizes-transition-morphism).

## Languages of finite automata have finite syntactic monoids

Every language accepted by a
DFA with finitely many states has a finite syntactic monoid.

Formalized by `Cslib.Language.finite_syntacticMonoid_of_finite_dfa`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Recognition.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Recognition.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/syntactic-monoid/index.html#finite-syntactic-monoid-of-finite-dfa).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Syntactic monoid](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/syntactic-monoid/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/syntactic-monoid)
