---
declaration: section
origin: cited
lean: Cslib.Decidability.exists_not_tm2Decidable_overlap, Cslib.Decidability.exists_not_tm2Decidable_disjoint, Cslib.Decidability.exists_not_tm2Decidable_isAmbiguous, Cslib.Decidability.exists_not_tm2Decidable_univ, Cslib.Decidability.allWordsCFG, Cslib.Decidability.exists_not_tm2Decidable_language_eq, Cslib.Decidability.exists_not_tm2Decidable_language_le, Cslib.Decidability.not_tm2Recognizable_not_of
statement: formalized
proof: formalized
---

# Undecidable problems for context-free grammars

18 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/undecidable-problems-for-context-free-grammars/index.html).

## Whether two context-free languages intersect is undecidable

There is an alphabet $T$,
with decidable equality and a primitive recursive encoding into $\mathbb{N}$, such that no
multi-stack machine decides (in the sense of TM2-decidability), for a pair $(G_1, G_2)$ of
encoded context-free grammars over $T$, whether some word lies in both $L(G_1)$ and $L(G_2)$,
where $L(G)$ is the language of $G$.

$T$ is not required to be finite. This is Sipser's problem $\mathit{OVERLAP}_{\mathit{CFG}}$.

Formalized by `Cslib.Decidability.exists_not_tm2Decidable_overlap`, a theorem declared in [CSLibExt/Computability/Decidability/PCPApplications.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPApplications.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/undecidable-problems-for-context-free-grammars/index.html#exists-not-tm2-decidable-overlap).

## Whether two context-free languages are disjoint is undecidable

There is an alphabet $T$,
with decidable equality and a primitive recursive encoding into $\mathbb{N}$, such that no
multi-stack machine decides (in the sense of TM2-decidability), for a pair $(G_1, G_2)$ of
encoded context-free grammars over $T$, whether no word lies in both $L(G_1)$ and $L(G_2)$,
where $L(G)$ is the language of $G$.

$T$ is not required to be finite.

Formalized by `Cslib.Decidability.exists_not_tm2Decidable_disjoint`, a theorem declared in [CSLibExt/Computability/Decidability/PCPApplications.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPApplications.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/undecidable-problems-for-context-free-grammars/index.html#exists-not-tm2-decidable-disjoint).

## Whether a context-free grammar is ambiguous is undecidable

There is an alphabet $T$,
with decidable equality and a primitive recursive encoding into $\mathbb{N}$, such that no
multi-stack machine decides (in the sense of TM2-decidability), for an encoded context-free
grammar $G$ over $T$, whether $G$ is ambiguous, that is, whether some word has two different
leftmost derivations from the start nonterminal of $G$.

$T$ is not required to be finite. This is Sipser's problem $\mathit{AMBIG}_{\mathit{CFG}}$.

Formalized by `Cslib.Decidability.exists_not_tm2Decidable_isAmbiguous`, a theorem declared in [CSLibExt/Computability/Decidability/PCPApplications.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPApplications.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/undecidable-problems-for-context-free-grammars/index.html#exists-not-tm2-decidable-is-ambiguous).

## Whether a context-free grammar generates every word is undecidable

There is a finite
alphabet $T$, with decidable equality and a primitive recursive encoding into $\mathbb{N}$, such
that no multi-stack machine decides (in the sense of TM2-decidability), for an encoded
context-free grammar $G$ over $T$, whether every word over $T$ lies in the language of $G$.

This is Sipser's problem $\mathit{ALL}_{\mathit{CFG}}$.

Formalized by `Cslib.Decidability.exists_not_tm2Decidable_univ`, a theorem declared in [CSLibExt/Computability/Decidability/PCPApplications.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPApplications.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/undecidable-problems-for-context-free-grammars/index.html#exists-not-tm2-decidable-univ).

## Grammar of all words

For a finite alphabet $T$, the encoded context-free grammar over $T$
whose start nonterminal is $S = 0$ and whose productions are $S \to \varepsilon$ and $S \to a S$
for every letter $a \in T$.

It generates every word over $T$.

Formalized by `Cslib.Decidability.allWordsCFG`, a definition declared in [CSLibExt/Computability/Decidability/PCPApplications.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPApplications.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/undecidable-problems-for-context-free-grammars/index.html#all-words-cfg).

## Equivalence of context-free grammars is undecidable

There is a finite alphabet $T$, with
decidable equality and a primitive recursive encoding into $\mathbb{N}$, such that no multi-stack
machine decides (in the sense of TM2-decidability), for a pair $(G_1, G_2)$ of encoded
context-free grammars over $T$, whether $L(G_1) = L(G_2)$, where $L(G)$ is the language of $G$.

This is Sipser's problem $\mathit{EQ}_{\mathit{CFG}}$.

Formalized by `Cslib.Decidability.exists_not_tm2Decidable_language_eq`, a theorem declared in [CSLibExt/Computability/Decidability/PCPApplications.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPApplications.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/undecidable-problems-for-context-free-grammars/index.html#exists-not-tm2-decidable-language-eq).

## Inclusion of context-free languages is undecidable

There is a finite alphabet $T$, with
decidable equality and a primitive recursive encoding into $\mathbb{N}$, such that no multi-stack
machine decides (in the sense of TM2-decidability), for a pair $(G_1, G_2)$ of encoded
context-free grammars over $T$, whether $L(G_1) \subseteq L(G_2)$, where $L(G)$ is the language
of $G$.

Formalized by `Cslib.Decidability.exists_not_tm2Decidable_language_le`, a theorem declared in [CSLibExt/Computability/Decidability/PCPApplications.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPApplications.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/undecidable-problems-for-context-free-grammars/index.html#exists-not-tm2-decidable-language-le).

## Post's theorem, contrapositive

A recognizable undecidable predicate has an
unrecognizable complement.

Formalized by `Cslib.Decidability.not_tm2Recognizable_not_of`, a theorem declared in [CSLibExt/Computability/Decidability/CFGRecognizability.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CFGRecognizability.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/undecidable-problems-for-context-free-grammars/index.html#not-tm2-recognizable-not-of).

## The complement of PCP is not recognizable

**The complement of PCP is not recognizable**, over some finite alphabet.

Formalized by `Cslib.Decidability.exists_not_tm2Recognizable_not_pcp`, a theorem declared in [CSLibExt/Computability/Decidability/CFGRecognizability.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CFGRecognizability.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/undecidable-problems-for-context-free-grammars/index.html#exists-not-tm2-recognizable-not-pcp).

## Membership in the first grammar of a pair is computable

Let $T$ be an alphabet with a
primcodable encoding and decidable equality. The predicate that holds of a pair
$((g_1, g_2), w)$, where $g_1, g_2$ are encoded context-free grammars over $T$ and $w$ is a word
over $T$, exactly when $w$ lies in the language of $g_1$, is a computable predicate.

Formalized by `Cslib.Decidability.computablePred_mem_fst`, a theorem declared in [CSLibExt/Computability/Decidability/CFGRecognizability.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CFGRecognizability.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/undecidable-problems-for-context-free-grammars/index.html#computable-pred-mem-fst).

## The overlap problem for context-free grammars is recognizable

Let $T$ be an alphabet
with a primitive recursive coding into the natural numbers and decidable equality. For an
encoded context-free grammar $G$ over $T$, write $L(G)$ for the language it generates. The
problem $\mathrm{OVERLAP}_{\mathrm{CFG}}$, the set of pairs $(G, H)$ of encoded context-free
grammars over $T$ such that some word $w$ over $T$ lies in both $L(G)$ and $L(H)$, is
recognizable by a multi-stack machine.

The proof searches for a common word, using that membership in a context-free language is
decidable.

Formalized by `Cslib.Decidability.tm2Recognizable_overlap`, a theorem declared in [CSLibExt/Computability/Decidability/CFGRecognizability.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CFGRecognizability.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/undecidable-problems-for-context-free-grammars/index.html#tm2-recognizable-overlap).

## Universality of context-free grammars is co-recognizable

For every alphabet $T$ with a
primcodable encoding and decidable equality, the set of encoded context-free grammars over $T$
whose language contains every word over $T$ is co-recognizable by a multi-stack Turing machine.

A recognizer for the complement searches for a word outside the language.

Formalized by `Cslib.Decidability.tm2CoRecognizable_univ`, a theorem declared in [CSLibExt/Computability/Decidability/CFGRecognizability.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CFGRecognizability.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/undecidable-problems-for-context-free-grammars/index.html#tm2-co-recognizable-univ).

## Equivalence of context-free grammars is co-recognizable

For every alphabet $T$ with a
primcodable encoding and decidable equality, the set of pairs $(g_1, g_2)$ of encoded
context-free grammars over $T$ whose languages are equal is co-recognizable by a multi-stack
Turing machine.

A recognizer for the complement searches for a word in exactly one of the two languages.

Formalized by `Cslib.Decidability.tm2CoRecognizable_language_eq`, a theorem declared in [CSLibExt/Computability/Decidability/CFGRecognizability.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CFGRecognizability.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/undecidable-problems-for-context-free-grammars/index.html#tm2-co-recognizable-language-eq).

## Inclusion of context-free languages is co-recognizable

For every alphabet $T$ with a
primcodable encoding and decidable equality, the set of pairs $(g_1, g_2)$ of encoded
context-free grammars over $T$ for which the language of $g_1$ is contained in the language of
$g_2$ is co-recognizable by a multi-stack Turing machine.

Formalized by `Cslib.Decidability.tm2CoRecognizable_language_le`, a theorem declared in [CSLibExt/Computability/Decidability/CFGRecognizability.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CFGRecognizability.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/undecidable-problems-for-context-free-grammars/index.html#tm2-co-recognizable-language-le).

## Disjointness of context-free languages is not recognizable

There is an alphabet $T$,
with a primcodable encoding and decidable equality, such that the set of pairs $(g_1, g_2)$ of
encoded context-free grammars over $T$ whose languages are disjoint (no word lies in both) is not
recognizable by a multi-stack Turing machine.

Formalized by `Cslib.Decidability.exists_not_tm2Recognizable_disjoint`, a theorem declared in [CSLibExt/Computability/Decidability/CFGRecognizability.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CFGRecognizability.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/undecidable-problems-for-context-free-grammars/index.html#exists-not-tm2-recognizable-disjoint).

## Universality of context-free grammars is not recognizable

There is a finite alphabet
$T$, with a primcodable encoding and decidable equality, such that the set of encoded
context-free grammars over $T$ whose language contains every word over $T$ is not recognizable by
a multi-stack Turing machine.

The complement of the Post correspondence problem reduces to this problem.

Formalized by `Cslib.Decidability.exists_not_tm2Recognizable_univ`, a theorem declared in [CSLibExt/Computability/Decidability/CFGRecognizability.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CFGRecognizability.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/undecidable-problems-for-context-free-grammars/index.html#exists-not-tm2-recognizable-univ).

## Equivalence of context-free grammars is not recognizable

There is a finite alphabet
$T$, with a primcodable encoding and decidable equality, such that the set of pairs $(g_1, g_2)$
of encoded context-free grammars over $T$ whose languages are equal is not recognizable by a
multi-stack Turing machine.

Formalized by `Cslib.Decidability.exists_not_tm2Recognizable_language_eq`, a theorem declared in [CSLibExt/Computability/Decidability/CFGRecognizability.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CFGRecognizability.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/undecidable-problems-for-context-free-grammars/index.html#exists-not-tm2-recognizable-language-eq).

## Inclusion of context-free languages is not recognizable

There is a finite alphabet $T$,
with a primcodable encoding and decidable equality, such that the set of pairs $(g_1, g_2)$ of
encoded context-free grammars over $T$ for which the language of $g_1$ is contained in the
language of $g_2$ is not recognizable by a multi-stack Turing machine.

Formalized by `Cslib.Decidability.exists_not_tm2Recognizable_language_le`, a theorem declared in [CSLibExt/Computability/Decidability/CFGRecognizability.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CFGRecognizability.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/undecidable-problems-for-context-free-grammars/index.html#exists-not-tm2-recognizable-language-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Undecidable problems for context-free grammars](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/undecidable-problems-for-context-free-grammars/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/undecidable-problems/undecidable-problems-for-context-free-grammars)
