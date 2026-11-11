---
declaration: section
origin: cited
lean: Cslib.Language.projRight, Cslib.Language.insSymbol, Cslib.Language.markedForm, Cslib.Language.insGrammar, Cslib.Language.insGrammar_derives_flatMap, Cslib.Language.insGrammar_derives_markedForm, Cslib.Language.insValuation, Cslib.Language.insGrammar_language
statement: formalized
proof: formalized
---

# Inverse homomorphic images of context-free languages

13 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/inverse-homomorphic-images-of-context-free-langu/index.html).

## Right letters

## Right projection of a word

For a word $u$ over the disjoint union $T \oplus T'$ of two
alphabets, its right projection is the word over $T'$ obtained from $u$ by deleting every letter
from $T$ and reading each remaining letter as a letter of $T'$, keeping their order.

Formalized by `Cslib.Language.projRight`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/InverseHom.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/InverseHom.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/inverse-homomorphic-images-of-context-free-langu/index.html#proj-right).

## Marker translation of a symbol

Let $g$ be a context-free grammar over $T'$ and let $T$ be
an alphabet. Each symbol of $g$ is translated to a string of symbols with terminals in
$T \sqcup T'$ and nonterminals those of $g$ together with two new nonterminals $S$ and $D$: a
terminal $b \in T'$ becomes the marker $D$ followed by $b$, and a nonterminal $A$ of $g$ becomes
$A$.

Formalized by `Cslib.Language.insSymbol`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/InverseHom.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/InverseHom.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/inverse-homomorphic-images-of-context-free-langu/index.html#ins-symbol).

## Marked form of a word

Let $g$ be a context-free grammar over $T'$, let $T$ be an
alphabet, and let $u$ be a word over $T \sqcup T'$. The marked form of $u$ is the sentential form,
with terminals in $T \sqcup T'$ and nonterminals those of $g$ together with two new nonterminals
$S$ and $D$, that lists the letters of $u$ from $T'$ in order, each preceded by the marker $D$,
followed by one more $D$.

Formalized by `Cslib.Language.markedForm`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/InverseHom.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/InverseHom.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/inverse-homomorphic-images-of-context-free-langu/index.html#marked-form).

## Marker-insertion grammar

Let $g$ be a context-free grammar over $T'$ with start symbol
$A_0$, and let $T$ be a finite alphabet. The marker-insertion grammar of $g$ is the context-free
grammar over $T \sqcup T'$ whose nonterminals are those of $g$ together with a new start symbol
$S$ and a marker $D$, and whose rules are: for each rule $A \to \alpha$ of $g$, the rule
$A \to \alpha'$, where $\alpha'$ is $\alpha$ with $D$ inserted in front of each terminal; the
rule $S \to A_0 D$; the rule $D \to \varepsilon$; and the rule $D \to a D$ for each $a \in T$.

Formalized by `Cslib.Language.insGrammar`, an abbreviation declared in [CSLibExt/Computability/Languages/ContextFree/InverseHom.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/InverseHom.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/inverse-homomorphic-images-of-context-free-langu/index.html#ins-grammar).

## The marker-insertion grammar simulates the original grammar

Let $g$ be a context-free
grammar over $T'$ and let $T$ be a finite alphabet. If $g$ derives a sentential form $y$ from a
sentential form $x$, then the marker-insertion grammar of $g$ over $T \sqcup T'$ derives the
translation of $y$ from the translation of $x$, where a sentential form is translated by
replacing each of its symbols by its marker translation.

Formalized by `Cslib.Language.insGrammar_derives_flatMap`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/InverseHom.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/InverseHom.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/inverse-homomorphic-images-of-context-free-langu/index.html#ins-grammar-derives-flat-map).

## Marker loops fill in the left letters

Let $g$ be a context-free grammar over $T'$ and
let $T$ be a finite alphabet. For every word $u$ over $T \sqcup T'$, the marker-insertion grammar
of $g$ derives $u$ from the marked form of $u$, the sentential form that lists the letters of $u$
from $T'$ in order, each preceded by the marker nonterminal $D$, followed by one more $D$.

Formalized by `Cslib.Language.insGrammar_derives_markedForm`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/InverseHom.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/InverseHom.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/inverse-homomorphic-images-of-context-free-langu/index.html#ins-grammar-derives-marked-form).

## Valuation for the marker-insertion grammar

Let $g$ be a context-free grammar over $T'$
and let $T$ be an alphabet. This valuation assigns a language over $T \sqcup T'$ to each
nonterminal of $g$ and to the two new nonterminals $S$ and $D$ of the marker-insertion grammar
of $g$: to the marker $D$ the words with no letter from $T'$; to the new start symbol $S$ the
words whose letters from $T'$ form a word of the language of $g$; and to a nonterminal $A$ of $g$
the words whose letters from $T'$ form a word that $g$ derives from $A$.

Formalized by `Cslib.Language.insValuation`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/InverseHom.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/InverseHom.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/inverse-homomorphic-images-of-context-free-langu/index.html#ins-valuation).

## Language of the marker-insertion grammar

Let $g$ be a context-free grammar over $T'$
and let $T$ be a finite alphabet. The marker-insertion grammar of $g$ generates exactly the
words $u$ over $T \sqcup T'$ whose letters from $T'$, read in order, form a word of the language
of $g$.

Formalized by `Cslib.Language.insGrammar_language`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/InverseHom.lean, line 258](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/InverseHom.lean#L258). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/inverse-homomorphic-images-of-context-free-langu/index.html#ins-grammar-language).

## Context-free languages are closed under inserting letters

Let $T$ be a finite alphabet
and let $L$ be a context-free language over an alphabet $T'$. Then the language of words $u$ over
the disjoint union $T \oplus T'$ whose letters from $T'$, read in order, form a word of $L$ is
context-free.

Formalized by `Cslib.Language.IsContextFree.preimage_projRight`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/InverseHom.lean, line 285](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/InverseHom.lean#L285). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/inverse-homomorphic-images-of-context-free-langu/index.html#preimage-proj-right).

## Block of a letter

For a map $\varphi$ from $T$ to words over $T'$ and a letter
$a \in T$, the block of $a$ is the word over the disjoint union $T \sqcup T'$ that consists of
$a$, as a letter of $T$, followed by the letters of $\varphi(a)$, as letters of $T'$.

Formalized by `Cslib.Language.block`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/InverseHom.lean, line 294](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/InverseHom.lean#L294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/inverse-homomorphic-images-of-context-free-langu/index.html#block).

## Erasing right letters

Erasing right letters is the map from letters of the disjoint
union $T \sqcup T'$ to words over $T$ that sends a letter $a$ of $T$ to the one-letter word $a$
and every letter of $T'$ to the empty word.

Formalized by `Cslib.Language.eraseRight`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/InverseHom.lean, line 298](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/InverseHom.lean#L298). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/inverse-homomorphic-images-of-context-free-langu/index.html#erase-right).

## Context-free languages are closed under inverse homomorphisms

**Context-free languages are closed under inverse homomorphisms** from a finite alphabet.

Formalized by `Cslib.Language.IsContextFree.preimage_hom`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/InverseHom.lean, line 330](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/InverseHom.lean#L330). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/inverse-homomorphic-images-of-context-free-langu/index.html#preimage-hom).

## Context-free languages are closed under inverse free-monoid morphisms

Let $T$ be a
finite alphabet, $T'$ an alphabet, $\sigma \colon T^* \to {T'}^*$ a morphism of free monoids and
$L$ a context-free language over $T'$. Then the inverse image
$\sigma^{-1}(L) = \{x \in T^* \mid \sigma(x) \in L\}$ is a context-free language over $T$.

Formalized by `Cslib.Language.IsContextFree.preimage_wordMorphism`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/InverseHom.lean, line 371](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/InverseHom.lean#L371). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/inverse-homomorphic-images-of-context-free-langu/index.html#preimage-word-morphism).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Inverse homomorphic images of context-free languages](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/inverse-homomorphic-images-of-context-free-langu/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/inverse-homomorphic-images-of-context-free-langu)
