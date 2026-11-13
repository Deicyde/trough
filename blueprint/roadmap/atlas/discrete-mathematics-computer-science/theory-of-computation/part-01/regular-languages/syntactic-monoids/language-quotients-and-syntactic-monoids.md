---
declaration: section
origin: cited
lean: Cslib.Language.contextQuotient, Cslib.Language.contextQuotient_contextQuotient, Cslib.Language.contextAccept, Cslib.Language.Recognizes.contextQuotient, Cslib.Language.contextQuotientToSyntactic, Cslib.Language.card_syntacticMonoid_contextQuotient_le_mrange, Cslib.Language.finite_syntacticMonoid_contextQuotient, Cslib.Language.IsRegular.contextQuotient
statement: formalized
proof: formalized
---

# Language quotients and syntactic monoids

20 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/language-quotients-and-syntactic-monoids/index.html).

## Context quotient

Let $L$ be a language over an alphabet $A$ and let $u, v$ be words over
$A$. The context quotient of $L$ by $(u, v)$ is the language
$u^{-1} L v^{-1} = \{x \in A^* \mid uxv \in L\}$ of words that land in $L$ when placed between
$u$ and $v$.

Formalized by `Cslib.Language.contextQuotient`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Contexts.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Contexts.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/language-quotients-and-syntactic-monoids/index.html#context-quotient).

## Composing context quotients

Let $L$ be a language over an alphabet $A$, and for words
$u, v$ over $A$ write $u^{-1} L v^{-1} = \{x \mid uxv \in L\}$. Then for all words
$u_1, v_1, u_2, v_2$ over $A$,
$u_2^{-1} (u_1^{-1} L v_1^{-1}) v_2^{-1} = (u_1 u_2)^{-1} L (v_2 v_1)^{-1}$.

Formalized by `Cslib.Language.contextQuotient_contextQuotient`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Contexts.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Contexts.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/language-quotients-and-syntactic-monoids/index.html#context-quotient-context-quotient).

## Accepting set for a context quotient

Let $\varphi \colon A^* \to M$ be a monoid morphism
from the free monoid on an alphabet $A$ to a monoid $M$, let $P \subseteq M$, and let $u, v$ be
words over $A$. The accepting set for the context $(u, v)$ is
$\{m \in M \mid \varphi(u)\, m\, \varphi(v) \in P\}$.

Formalized by `Cslib.Language.contextAccept`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Contexts.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Contexts.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/language-quotients-and-syntactic-monoids/index.html#context-accept).

## Recognizers recognize context quotients

Let $\varphi \colon A^* \to M$ be a monoid
morphism from the free monoid on an alphabet $A$ to a monoid $M$ that recognizes a language $L$
over $A$ through $P \subseteq M$, that is, a word $x$ lies in $L$ exactly when $\varphi(x) \in P$.
Then for all words $u, v$ over $A$, $\varphi$ recognizes the context quotient
$\{x \mid uxv \in L\}$ through the set $\{m \in M \mid \varphi(u)\, m\, \varphi(v) \in P\}$.

Formalized by `Cslib.Language.Recognizes.contextQuotient`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Contexts.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Contexts.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/language-quotients-and-syntactic-monoids/index.html#context-quotient-2).

## The canonical map to the syntactic monoid of a context quotient

Let $L$ be a language
over an alphabet $A$, let $u, v$ be words over $A$, and write
$u^{-1} L v^{-1} = \{x \mid uxv \in L\}$. Let $\eta$ be the syntactic morphism of $L$ and
$\eta'$ the syntactic morphism of $u^{-1} L v^{-1}$. This is the monoid morphism from the image
of $\eta$ to the syntactic monoid of $u^{-1} L v^{-1}$ that sends $\eta(x)$ to $\eta'(x)$ for
every word $x$ over $A$.

Formalized by `Cslib.Language.contextQuotientToSyntactic`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Contexts.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Contexts.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/language-quotients-and-syntactic-monoids/index.html#context-quotient-to-syntactic).

## Size bound for the syntactic monoid of a context quotient

Let $L$ be a language over an
alphabet $A$, let $u, v$ be words over $A$, and write $u^{-1} L v^{-1} = \{x \mid uxv \in L\}$
for the context quotient. If the image of the syntactic morphism of $L$ and the syntactic monoid
of $u^{-1} L v^{-1}$ are both finite, then the syntactic monoid of $u^{-1} L v^{-1}$ has at most
as many elements as the image of the syntactic morphism of $L$.

Formalized by `Cslib.Language.card_syntacticMonoid_contextQuotient_le_mrange`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Contexts.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Contexts.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/language-quotients-and-syntactic-monoids/index.html#card-syntactic-monoid-context-quotient-l).

## Context quotients preserve finiteness of the syntactic monoid

Let $L$ be a language over
an alphabet $A$ whose syntactic monoid is finite. Then for all words $u, v$ over $A$, the
syntactic monoid of the context quotient $u^{-1} L v^{-1} = \{x \mid uxv \in L\}$ is finite.

Formalized by `Cslib.Language.finite_syntacticMonoid_contextQuotient`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Contexts.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Contexts.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/language-quotients-and-syntactic-monoids/index.html#finite-syntactic-monoid-context-quotient).

## Regular languages are closed under context quotients

If $L$ is a regular language over
an alphabet $A$, then for all words $u, v$ over $A$, the context quotient
$u^{-1} L v^{-1} = \{x \mid uxv \in L\}$ is regular.

Formalized by `Cslib.Language.IsRegular.contextQuotient`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Contexts.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Contexts.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/language-quotients-and-syntactic-monoids/index.html#context-quotient-3).

## Syntactic equivalence via context quotients

Let $L$ be a language over an alphabet $A$.
Two words $x, y$ over $A$ are syntactically equivalent for $L$ if and only if, for all words
$u, v$ over $A$, $x$ lies in the context quotient $u^{-1} L v^{-1} = \{w \mid uwv \in L\}$
exactly when $y$ does.

Formalized by `Cslib.Language.syntacticRel_iff_mem_contextQuotient`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Contexts.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Contexts.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/language-quotients-and-syntactic-monoids/index.html#syntactic-rel-iff-mem-context-quotient).

## Right quotient of a language by a word

For a language $L$ over an alphabet $\Sigma$ and a
word $w \in \Sigma^*$, the right quotient of $L$ by $w$ is the language
$\{x \in \Sigma^* : xw \in L\}$ of all words $x$ whose concatenation $xw$ with $w$ lies in $L$.

Formalized by `Cslib.Language.rightQuotient`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Quotients.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Quotients.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/language-quotients-and-syntactic-monoids/index.html#right-quotient).

## Accepting set for a left quotient

Let $\varphi \colon A^* \to M$ be a monoid morphism
from the free monoid on an alphabet $A$ to a monoid $M$, let $P \subseteq M$, and let $u$ be a
word over $A$. The accepting set for the left quotient by $u$ is
$\{m \in M \mid \varphi(u)\, m \in P\}$.

Formalized by `Cslib.Language.leftQuotientAccept`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Quotients.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Quotients.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/language-quotients-and-syntactic-monoids/index.html#left-quotient-accept).

## Accepting set for a right quotient

Let $\varphi \colon A^* \to M$ be a monoid morphism
from the free monoid on an alphabet $A$ to a monoid $M$, let $P \subseteq M$, and let $u$ be a
word over $A$. The accepting set for the right quotient by $u$ is
$\{m \in M \mid m\, \varphi(u) \in P\}$.

Formalized by `Cslib.Language.rightQuotientAccept`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Quotients.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Quotients.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/language-quotients-and-syntactic-monoids/index.html#right-quotient-accept).

## Recognizers recognize left quotients

Let $\varphi \colon A^* \to M$ be a monoid morphism
from the free monoid on an alphabet $A$ to a monoid $M$ that recognizes a language $L$ over $A$
through $P \subseteq M$, that is, a word $x$ lies in $L$ exactly when $\varphi(x) \in P$. Then
for every word $u$ over $A$, $\varphi$ recognizes the left quotient $\{x \mid ux \in L\}$ through
the set $\{m \in M \mid \varphi(u)\, m \in P\}$.

Formalized by `Cslib.Language.Recognizes.leftQuotient`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Quotients.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Quotients.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/language-quotients-and-syntactic-monoids/index.html#left-quotient).

## Recognizers recognize right quotients

Let $\varphi \colon A^* \to M$ be a monoid
morphism from the free monoid on an alphabet $A$ to a monoid $M$ that recognizes a language $L$
over $A$ through $P \subseteq M$, that is, a word $x$ lies in $L$ exactly when $\varphi(x) \in P$.
Then for every word $u$ over $A$, $\varphi$ recognizes the right quotient $\{x \mid xu \in L\}$
through the set $\{m \in M \mid m\, \varphi(u) \in P\}$.

Formalized by `Cslib.Language.Recognizes.rightQuotient`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Quotients.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Quotients.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/language-quotients-and-syntactic-monoids/index.html#right-quotient-2).

## The canonical map to the syntactic monoid of a left quotient

Let $L$ be a language over
an alphabet $A$, let $u$ be a word over $A$, and write $u^{-1} L = \{x \mid ux \in L\}$. Let
$\eta$ be the syntactic morphism of $L$ and $\eta'$ the syntactic morphism of $u^{-1} L$. This
is the monoid morphism from the image of $\eta$ to the syntactic monoid of $u^{-1} L$ that sends
$\eta(x)$ to $\eta'(x)$ for every word $x$ over $A$.

Formalized by `Cslib.Language.leftQuotientToSyntactic`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Quotients.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Quotients.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/language-quotients-and-syntactic-monoids/index.html#left-quotient-to-syntactic).

## The canonical map to the syntactic monoid of a right quotient

Let $L$ be a language over
an alphabet $A$, let $u$ be a word over $A$, and write $L u^{-1} = \{x \mid xu \in L\}$. Let
$\eta$ be the syntactic morphism of $L$ and $\eta'$ the syntactic morphism of $L u^{-1}$. This
is the monoid morphism from the image of $\eta$ to the syntactic monoid of $L u^{-1}$ that sends
$\eta(x)$ to $\eta'(x)$ for every word $x$ over $A$.

Formalized by `Cslib.Language.rightQuotientToSyntactic`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Quotients.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Quotients.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/language-quotients-and-syntactic-monoids/index.html#right-quotient-to-syntactic).

## Left quotients preserve finiteness of the syntactic monoid

Let $L$ be a language over an
alphabet $A$ whose syntactic monoid is finite. Then for every word $u$ over $A$, the syntactic
monoid of the left quotient $u^{-1} L = \{x \mid ux \in L\}$ is finite.

Formalized by `Cslib.Language.finite_syntacticMonoid_leftQuotient`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Quotients.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Quotients.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/language-quotients-and-syntactic-monoids/index.html#finite-syntactic-monoid-left-quotient).

## Right quotients preserve finiteness of the syntactic monoid

Let $L$ be a language over
an alphabet $A$ whose syntactic monoid is finite. Then for every word $u$ over $A$, the syntactic
monoid of the right quotient $L u^{-1} = \{x \mid xu \in L\}$ is finite.

Formalized by `Cslib.Language.finite_syntacticMonoid_rightQuotient`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Quotients.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Quotients.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/language-quotients-and-syntactic-monoids/index.html#finite-syntactic-monoid-right-quotient).

## Regular languages are closed under right quotients by fixed words

If $L$ is a regular
language over an alphabet $A$, then for every word $u$ over $A$, the right quotient
$L u^{-1} = \{x \mid xu \in L\}$ is regular.

Formalized by `Cslib.Language.IsRegular.rightQuotient'`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Quotients.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Quotients.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/language-quotients-and-syntactic-monoids/index.html#right-quotient-3).

## Regular languages are closed under left quotients by fixed words

If $L$ is a regular
language over an alphabet $A$, then for every word $u$ over $A$, the left quotient
$u^{-1} L = \{x \mid ux \in L\}$ is regular.

The proof starts a DFA for $L$ in the state it reaches on $u$.

Formalized by `Cslib.Language.IsRegular.leftQuotient`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Quotients.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Quotients.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/language-quotients-and-syntactic-monoids/index.html#left-quotient-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Language quotients and syntactic monoids](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/language-quotients-and-syntactic-monoids/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/language-quotients-and-syntactic-monoids)
