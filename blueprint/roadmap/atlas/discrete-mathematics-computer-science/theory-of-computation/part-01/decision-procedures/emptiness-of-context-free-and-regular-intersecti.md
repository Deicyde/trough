---
declaration: section
origin: cited
lean: Cslib.Language.EncodedCFG.dfaSymFits, Cslib.Language.EncodedCFG.dfaStarts, Cslib.Language.EncodedCFG.dfaStep, Cslib.Language.EncodedCFG.dfaItems, Cslib.Language.EncodedCFG.dfaFound, Cslib.Language.EncodedCFG.interEmptyB, Cslib.Language.EncodedCFG.dfaStarts_subset, Cslib.Language.EncodedCFG.DfaSoundItem
statement: formalized
proof: formalized
---

# Emptiness of context-free and regular intersections

14 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-and-regular-intersecti/index.html).

## The procedure

## Whether a symbol fits at a DFA state

Let $D$ be an encoded DFA, $R$ and $S$ lists of
natural numbers (the items found so far and the states where the rest of a right-hand side can
start), $X$ a grammar symbol and $p \in \mathbb{N}$. The test is true exactly when either $X$ is a
terminal $a$ and the step of $D$ from $p$ on $a$ lies in $S$, or $X$ is a nonterminal $B$ and some
$k$ in $S$ has $\langle B, \langle p, k \rangle \rangle$ in $R$, where
$\langle \cdot, \cdot \rangle$ is the natural-number pairing.

Formalized by `Cslib.Language.EncodedCFG.dfaSymFits`, a definition declared in [CSLibExt/Computability/Decidability/ContextFreeRegular.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFreeRegular.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-and-regular-intersecti/index.html#dfa-sym-fits).

## Start states of a right-hand side in a DFA

Let $D$ be an encoded DFA, $R$ a list of
natural numbers (the items found so far) and $q \in \mathbb{N}$. The start states of a right-hand
side $\beta$, a list of grammar symbols, for $q$ given $R$ are defined by recursion on $\beta$: for
the empty right-hand side they are the one-element list $[q]$, and for a symbol $X$ followed by
$\beta'$ they are the states of $D$, in order, at which $X$ fits given $R$ and the start states of
$\beta'$ for $q$ given $R$.

Formalized by `Cslib.Language.EncodedCFG.dfaStarts`, a definition declared in [CSLibExt/Computability/Decidability/ContextFreeRegular.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFreeRegular.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-and-regular-intersecti/index.html#dfa-starts).

## One round of the item search against a DFA

For an encoded grammar $g$, an encoded DFA
$D$ and a list $R$ of natural numbers (the items found so far), one round produces the list of the
codes $\langle A, \langle p, q \rangle \rangle$, where $\langle \cdot, \cdot \rangle$ is the
natural-number pairing, for every production $A \to \beta$ of $g$, every state $q$ of $D$ and
every start state $p$ of $\beta$ for $q$ given $R$.

Formalized by `Cslib.Language.EncodedCFG.dfaStep`, a definition declared in [CSLibExt/Computability/Decidability/ContextFreeRegular.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFreeRegular.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-and-regular-intersecti/index.html#dfa-step).

## Candidate items for a grammar and a DFA

For an encoded grammar $g$ and an encoded DFA
$D$, the candidate items form the list of the codes $\langle A, \langle p, q \rangle \rangle$, where
$\langle \cdot, \cdot \rangle$ is the natural-number pairing, for every left-hand side $A$ of a
production of $g$ (listed once per production) and all states $p$ and $q$ of $D$.

Formalized by `Cslib.Language.EncodedCFG.dfaItems`, a definition declared in [CSLibExt/Computability/Decidability/ContextFreeRegular.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFreeRegular.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-and-regular-intersecti/index.html#dfa-items).

## Items found for a grammar and a DFA

For an encoded grammar $g$ and an encoded DFA $D$,
the found items are the list obtained from the empty list by applying one round of the item
search of $g$ and $D$ as many times as the length of the list of candidate items of $g$ and
$D$.

Formalized by `Cslib.Language.EncodedCFG.dfaFound`, a definition declared in [CSLibExt/Computability/Decidability/ContextFreeRegular.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFreeRegular.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-and-regular-intersecti/index.html#dfa-found).

## The intersection-emptiness test for a grammar and a DFA

Let $g$ be an encoded grammar with
start nonterminal $S$, let $D$ be an encoded DFA with start state $s$, and write
$\langle \cdot, \cdot \rangle$ for the natural-number pairing. The test of $g$ and $D$ is true
exactly when there is no accepting state $f$ of $D$ that is also one of the states of $D$ and for
which the code $\langle S, \langle s, f \rangle \rangle$ is among the found items of $g$ and
$D$.

Formalized by `Cslib.Language.EncodedCFG.interEmptyB`, a definition declared in [CSLibExt/Computability/Decidability/ContextFreeRegular.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFreeRegular.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-and-regular-intersecti/index.html#inter-empty-b).

## Start states of a right-hand side are states of the DFA

Let $D$ be an encoded DFA, $R$ a
list of natural numbers and $q$ one of the states of $D$. Then for every right-hand side $\beta$,
every start state of $\beta$ for $q$ given $R$ is one of the states of $D$.

Formalized by `Cslib.Language.EncodedCFG.dfaStarts_subset`, a theorem declared in [CSLibExt/Computability/Decidability/ContextFreeRegular.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFreeRegular.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-and-regular-intersecti/index.html#dfa-starts-subset).

## Sound items for a grammar and a DFA

For an encoded grammar $g$ and an encoded DFA $D$, a
natural number $x$ is a sound item when there are natural numbers $A$, $p$, $q$ and a word $w$
such that $x = \langle A, \langle p, q \rangle \rangle$, where $\langle \cdot, \cdot \rangle$ is the
natural-number pairing, the nonterminal $A$ yields $w$ in the grammar denoted by $g$, and the
automaton denoted by $D$, run on $w$ from state $p$, ends in state $q$.

Formalized by `Cslib.Language.EncodedCFG.DfaSoundItem`, a definition declared in [CSLibExt/Computability/Decidability/ContextFreeRegular.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFreeRegular.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-and-regular-intersecti/index.html#dfa-sound-item).

## Completeness of the start states in a DFA

Let $g$ be an encoded context-free grammar and
$D$ an encoded DFA over an alphabet $T$ with decidable equality, and let $\rho$ be an encoded
right-hand side whose decoding yields a word $u$ in the grammar that $g$ denotes. If $p$ is one
of the states of $D$ and the automaton that $D$ denotes, run on $u$ from state $p$, ends in state
$q$, then $p$ is a start state of $\rho$ for $q$ given the items found for $g$ and $D$.

Formalized by `Cslib.Language.EncodedCFG.mem_dfaStarts_of_yields`, a theorem declared in [CSLibExt/Computability/Decidability/ContextFreeRegular.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFreeRegular.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-and-regular-intersecti/index.html#mem-dfa-starts-of-yields).

## Correctness of the intersection-emptiness test

For every encoded grammar $g$ and every
encoded DFA $D$, the intersection-emptiness test of $g$ and $D$ returns true if and only if the
intersection of the language of $g$ and the language of $D$ is empty.

Formalized by `Cslib.Language.EncodedCFG.interEmptyB_iff`, a theorem declared in [CSLibExt/Computability/Decidability/ContextFreeRegular.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFreeRegular.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-and-regular-intersecti/index.html#inter-empty-b-iff).

## The inclusion test for a grammar and a DFA

For an encoded context-free grammar $g$ and an
encoded DFA $D$ over the same alphabet $T$, where $T$ has decidable equality, the inclusion test on
$g$ and $D$ is the Boolean value of the emptiness test on $g$ and the complement of $D$.

Formalized by `Cslib.Language.EncodedCFG.subsetB`, a definition declared in [CSLibExt/Computability/Decidability/ContextFreeRegular.lean, line 291](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFreeRegular.lean#L291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-and-regular-intersecti/index.html#subset-b).

## Correctness of the inclusion test

For every alphabet $T$ with decidable equality, every
encoded context-free grammar $g$ over $T$ and every encoded DFA $D$ over $T$, the inclusion test
on $g$ and $D$ returns true if and only if the language of $g$ is contained in the language of
$D$.

Formalized by `Cslib.Language.EncodedCFG.subsetB_iff`, a theorem declared in [CSLibExt/Computability/Decidability/ContextFreeRegular.lean, line 295](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFreeRegular.lean#L295). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-and-regular-intersecti/index.html#subset-b-iff).

## Emptiness of the intersection of a context-free and a regular language is decidable

For
every alphabet $T$ with decidable equality and a primitive recursive encoding, the property of a
pair $(g, D)$, where $g$ is an encoded context-free grammar over $T$ and $D$ is an encoded DFA
over $T$, that the intersection of the language of $g$ and the language of $D$ is empty is
decidable by a multi-stack machine.

Formalized by `Cslib.Language.EncodedCFG.tm2Decidable_inter_eq_zero`, a theorem declared in [CSLibExt/Computability/Decidability/ContextFreeRegular.lean, line 402](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFreeRegular.lean#L402). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-and-regular-intersecti/index.html#tm2-decidable-inter-eq-zero).

## Inclusion of a context-free language in a regular language is decidable

For every
alphabet $T$ with decidable equality and a primitive recursive encoding, the property of a pair
$(g, D)$, where $g$ is an encoded context-free grammar over $T$ and $D$ is an encoded DFA over
$T$, that the language of $g$ is contained in the language of $D$ is decidable by a multi-stack
machine.

Formalized by `Cslib.Language.EncodedCFG.tm2Decidable_language_le`, a theorem declared in [CSLibExt/Computability/Decidability/ContextFreeRegular.lean, line 409](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFreeRegular.lean#L409). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-and-regular-intersecti/index.html#tm2-decidable-language-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Emptiness of context-free and regular intersections](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-and-regular-intersecti/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-and-regular-intersecti)
