---
declaration: section
origin: cited
lean: Cslib.Language.mapSymbol_mapSymbol, Cslib.Language.language_eq_of_maps, Cslib.Language.EncodedCFG, Cslib.Language.EncodedCFG.decodeSymbol, Cslib.Language.EncodedCFG.encodeSymbol, Cslib.Language.EncodedCFG.decodeRule, Cslib.Language.EncodedCFG.encodeRule, Cslib.Language.EncodedCFG.toCFG
statement: formalized
proof: formalized
---

# Encodings of context-free grammars

19 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encodings-of-context-free-grammars/index.html).

## Renaming the nonterminals of a symbol twice

For maps $f : N_1 \to N_2$ and
$b : N_2 \to N_3$ and a grammar symbol $s$ with terminals in $T$ and nonterminals in $N_1$,
renaming the nonterminals of $s$ by $f$ and then by $b$ gives the same symbol as renaming them by
$b \circ f$.

Formalized by `Cslib.Language.mapSymbol_mapSymbol`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Encoded.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Encoded.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encodings-of-context-free-grammars/index.html#map-symbol-map-symbol).

## Grammars with renamings in both directions generate the same language

Let $g$ and $G$
be context-free grammars over the same terminals. Suppose there are maps $f$ from the
nonterminals of $g$ to those of $G$ and $b$ from the nonterminals of $G$ to those of $g$ such
that renaming the nonterminals of any production of $g$ by $f$ gives a production of $G$,
renaming the nonterminals of any production of $G$ by $b$ gives a production of $g$, $f$ sends
the start nonterminal of $g$ to that of $G$, and $b$ sends the start nonterminal of $G$ to that
of $g$. Then $g$ and $G$ generate the same language. The renamings need not be inverse to each
other.

Formalized by `Cslib.Language.language_eq_of_maps`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Encoded.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Encoded.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encodings-of-context-free-grammars/index.html#language-eq-of-maps).

## Encoded context-free grammars

An encoded context-free grammar over a terminal type $T$
consists of a start nonterminal, which is a natural number, and a list of productions. Each
production is a pair of a left-hand side, a natural number, and a right-hand side, a list of
elements of the disjoint union $\mathbb{N} \sqcup T$, in which a number $i$ from the left summand
stands for nonterminal $i$ and an element $a$ of $T$ for terminal $a$.

Unlike a general context-free grammar, whose type of nonterminals is part of its data, an
encoded grammar is a concrete object that computable functions can take and return.

Formalized by `Cslib.Language.EncodedCFG`, a structure declared in [CSLibExt/Computability/Languages/ContextFree/Encoded.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Encoded.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encodings-of-context-free-grammars/index.html#encoded-cfg).

## Decoding a grammar symbol

Decoding sends an element of the disjoint union
$\mathbb{N} \sqcup T$ to a grammar symbol with terminals $T$ and nonterminals $\mathbb{N}$:
a natural number $i$ from the left summand goes to the nonterminal $i$, and an element $a$ of
$T$ from the right summand goes to the terminal $a$.

Formalized by `Cslib.Language.EncodedCFG.decodeSymbol`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/Encoded.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Encoded.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encodings-of-context-free-grammars/index.html#decode-symbol).

## Encoding a grammar symbol

Encoding sends a grammar symbol with terminals $T$ and
nonterminals $\mathbb{N}$ to an element of the disjoint union $\mathbb{N} \sqcup T$: the
terminal $a$ goes to $a$ in the right summand $T$, and the nonterminal $i$ goes to $i$ in the
left summand $\mathbb{N}$.

Formalized by `Cslib.Language.EncodedCFG.encodeSymbol`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/Encoded.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Encoded.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encodings-of-context-free-grammars/index.html#encode-symbol).

## Decoding a production

Decoding a pair $(A, s)$ of a natural number $A$ and a list $s$
of elements of the disjoint union $\mathbb{N} \sqcup T$ gives the production, with terminals
$T$ and nonterminals $\mathbb{N}$, whose left-hand side is the nonterminal $A$ and whose
right-hand side is $s$ with each entry decoded as a symbol: a number $i$ from the left summand
becomes the nonterminal $i$ and an element $a$ of $T$ becomes the terminal $a$.

Formalized by `Cslib.Language.EncodedCFG.decodeRule`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/Encoded.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Encoded.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encodings-of-context-free-grammars/index.html#decode-rule).

## Encoding a production

Encoding a production with terminals $T$ and nonterminals
$\mathbb{N}$ gives the pair $(A, s)$ where $A \in \mathbb{N}$ is its left-hand side and $s$ is
its right-hand side with each symbol encoded as an element of the disjoint union
$\mathbb{N} \sqcup T$: the terminal $a$ becomes $a$ in the right summand and the nonterminal
$i$ becomes $i$ in the left summand.

Formalized by `Cslib.Language.EncodedCFG.encodeRule`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/Encoded.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Encoded.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encodings-of-context-free-grammars/index.html#encode-rule).

## Grammar denoted by an encoding

For an encoded context-free grammar $g$ over $T$, the
context-free grammar over $T$ whose nonterminals are the natural numbers, whose initial
nonterminal is the start nonterminal of $g$, and whose productions are the decodings of the
encoded productions of $g$: an encoded production $(i, u)$ becomes the production rewriting the
nonterminal $i$ to the word obtained from $u$ by reading each entry $\mathrm{inl}\, j$ as the
nonterminal $j$ and each entry $\mathrm{inr}\, a$ as the terminal $a$.

Formalized by `Cslib.Language.EncodedCFG.toCFG`, an abbreviation declared in [CSLibExt/Computability/Languages/ContextFree/Encoded.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Encoded.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encodings-of-context-free-grammars/index.html#to-cfg).

## Language of an encoded grammar

The language of an encoded context-free grammar $g$ over
$T$ is the language generated by the context-free grammar that $g$ denotes, whose nonterminals
are the natural numbers, whose initial nonterminal is the start nonterminal of $g$ and whose
productions are the decoded productions of $g$.

Formalized by `Cslib.Language.EncodedCFG.language`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/Encoded.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Encoded.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encodings-of-context-free-grammars/index.html#language).

## Encoded grammars generate context-free languages

The language of an encoded grammar is
context-free.

Formalized by `Cslib.Language.EncodedCFG.language_isContextFree`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Encoded.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Encoded.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encodings-of-context-free-grammars/index.html#language-is-context-free).

## Nonterminal of a symbol

The partial map from grammar symbols with terminals in $T$ and
nonterminals in $N$ to $N$ that sends a nonterminal $A$ to $A$ and has no value on terminals.

Formalized by `Cslib.Language.EncodedCFG.ntOf`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/Encoded.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Encoded.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encodings-of-context-free-grammars/index.html#nt-of).

## List of nonterminals mentioned by a grammar

For a context-free grammar $G$, the list
consisting of the initial nonterminal of $G$ followed, for each production of $G$ in turn (in some
fixed order of its finite set of productions), by the left-hand side of the production and then
the nonterminals of its right-hand side in order. Nonterminals may occur more than once.

Formalized by `Cslib.Language.EncodedCFG.usedNT`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/Encoded.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Encoded.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encodings-of-context-free-grammars/index.html#used-nt).

## Numbering of nonterminals

For a context-free grammar $G$, the number of a nonterminal $A$
of $G$ is the position, counting from $0$, of the first occurrence of $A$ in the list of
nonterminals that $G$ mentions (its initial nonterminal first); if $A$ does not occur in that
list, its number is the length of the list.

Formalized by `Cslib.Language.EncodedCFG.ntIndex`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/Encoded.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Encoded.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encodings-of-context-free-grammars/index.html#nt-index).

## Nonterminal with a given number

For a context-free grammar $G$ and a natural number $n$,
the nonterminal of $G$ with number $n$ is the entry at position $n$, counting from $0$, of the
list of nonterminals that $G$ mentions (its initial nonterminal first); if the list has no entry
at position $n$, it is the initial nonterminal of $G$.

Formalized by `Cslib.Language.EncodedCFG.ntOfIndex`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/Encoded.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Encoded.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encodings-of-context-free-grammars/index.html#nt-of-index).

## Numbering the nonterminals of a production and back recovers it

Let $G$ be a context-free
grammar over $T$ and $r$ a production of $G$. Replacing each nonterminal $A$ of $r$ by its number,
the position, counting from $0$, of the first occurrence of $A$ in the list of nonterminals that
$G$ mentions, and then replacing each number $n$ by the nonterminal of $G$ with number $n$ (the
entry at position $n$ of that list, or the initial nonterminal of $G$ if the list has no such
entry) gives $r$ again.

Formalized by `Cslib.Language.EncodedCFG.mapRule_ntOfIndex_ntIndex`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Encoded.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Encoded.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encodings-of-context-free-grammars/index.html#map-rule-nt-of-index-nt-index).

## Encoding of a context-free grammar

For a context-free grammar $G$ over $T$, the encoded
grammar whose start nonterminal is the number of the initial nonterminal of $G$ and whose
productions are the productions of $G$, listed in some fixed order, with every nonterminal $A$
replaced by its number, the position, counting from $0$, of the first occurrence of $A$ in the
list of nonterminals that $G$ mentions (its initial nonterminal first).

Formalized by `Cslib.Language.EncodedCFG.ofCFG`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/Encoded.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Encoded.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encodings-of-context-free-grammars/index.html#of-cfg).

## The encoding of a grammar generates the same language

**The encoding of a grammar generates the same language.**

Formalized by `Cslib.Language.EncodedCFG.language_ofCFG`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Encoded.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Encoded.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encodings-of-context-free-grammars/index.html#language-of-cfg).

## A language is context-free exactly when an encoded grammar generates it

**A language is context-free exactly when an encoded grammar generates
it.**

Formalized by `Cslib.Language.EncodedCFG.isContextFree_iff`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Encoded.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Encoded.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encodings-of-context-free-grammars/index.html#is-context-free-iff).

## Encoded grammars as pairs

Sending an encoded grammar over $T$ to the pair of its start
nonterminal and its list of productions is a bijection from encoded grammars over $T$ onto
pairs $(s, R)$ of a natural number $s$ and a list $R$ of pairs of a natural number and a list
of elements of the disjoint union $\mathbb{N} \sqcup T$.

Formalized by `Cslib.Language.EncodedCFG.equivProd`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/Encoded.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Encoded.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encodings-of-context-free-grammars/index.html#equiv-prod).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Encodings of context-free grammars](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/encodings-of-context-free-grammars/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/decision-procedures/encodings-of-context-free-grammars)
