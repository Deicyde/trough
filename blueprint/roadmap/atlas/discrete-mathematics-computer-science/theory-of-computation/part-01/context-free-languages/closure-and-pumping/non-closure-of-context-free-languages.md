---
declaration: section
origin: cited
lean: Cslib.Language.mem_kstar_singleton, Cslib.Language.eqPowLang, Cslib.Language.eqPowGrammar, Cslib.Language.eqPowGrammar_language, Cslib.Language.eqPowLang_isContextFree, Cslib.Language.anbncnLang, Cslib.Language.anbncnLang_not_isContextFree, Cslib.Language.exists_isContextFree_inf_not_isContextFree
statement: formalized
proof: formalized
---

# Non-closure of context-free languages

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/non-closure-of-context-free-languages/index.html).

## The Kleene star of a one-letter word

For a letter $a$ of an alphabet, a word $w$ belongs
to the Kleene star of the language $\{a\}$ whose only word is the one-letter word $a$ if and only
if $w = a^k$ for some $k \in \mathbb{N}$.

Formalized by `Cslib.Language.mem_kstar_singleton`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/NonClosure.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/NonClosure.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/non-closure-of-context-free-languages/index.html#mem-kstar-singleton).

## The language $a^n b^n$

For letters $a$ and $b$ of an alphabet, this is the language of the
words $a^n b^n$ for $n \in \mathbb{N}$: $n$ copies of $a$ followed by $n$ copies of $b$.

Formalized by `Cslib.Language.eqPowLang`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/NonClosure.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/NonClosure.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/non-closure-of-context-free-languages/index.html#eq-pow-lang).

## The grammar $S \to aSb \mid \varepsilon$

For letters $a$ and $b$ of an alphabet with
decidable equality, this is the context-free grammar with a single nonterminal $S$, which is its
start symbol, and the two rules $S \to aSb$ and $S \to \varepsilon$.

Formalized by `Cslib.Language.eqPowGrammar`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/NonClosure.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/NonClosure.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/non-closure-of-context-free-languages/index.html#eq-pow-grammar).

## The grammar $S \to aSb \mid \varepsilon$ generates $a^n b^n$

For letters $a$ and $b$ of an
alphabet with decidable equality, the language of the context-free grammar with a single
nonterminal $S$, its start symbol, and the two rules $S \to aSb$ and $S \to \varepsilon$ is the
language of the words $a^n b^n$ for $n \in \mathbb{N}$.

Formalized by `Cslib.Language.eqPowGrammar_language`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/NonClosure.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/NonClosure.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/non-closure-of-context-free-languages/index.html#eq-pow-grammar-language).

## The language $a^n b^n$ is context-free

For any alphabet and any letters $a$ and $b$ of it,
the language of the words $a^n b^n$ for $n \in \mathbb{N}$ is context-free.

Formalized by `Cslib.Language.eqPowLang_isContextFree`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/NonClosure.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/NonClosure.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/non-closure-of-context-free-languages/index.html#eq-pow-lang-is-context-free).

## The language $a^n b^n c^n$

Over the three-letter alphabet $\{a, b, c\}$ (the letters
$0, 1, 2$), this is the language of the words $a^n b^n c^n$ for $n \in \mathbb{N}$: $n$ copies of
$a$, then $n$ copies of $b$, then $n$ copies of $c$.

Formalized by `Cslib.Language.anbncnLang`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/NonClosure.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/NonClosure.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/non-closure-of-context-free-languages/index.html#anbncn-lang).

## The language $a^n b^n c^n$ is not context-free

Over the three-letter alphabet $\{a, b, c\}$
(the letters $0, 1, 2$), the language of the words $a^n b^n c^n$ for $n \in \mathbb{N}$ is not
context-free.

Proof idea: by the pumping lemma, pumping $a^n b^n c^n$ down would keep the three letter counts
equal, so the pumped factor has equal counts of all letters, but a short factor misses $a$ or $c$,
forcing the factor to be empty.

Formalized by `Cslib.Language.anbncnLang_not_isContextFree`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/NonClosure.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/NonClosure.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/non-closure-of-context-free-languages/index.html#anbncn-lang-not-is-context-free).

## Context-free languages are not closed under intersection

There are context-free languages
$L$ and $M$ over the three-letter alphabet $\{0, 1, 2\}$ whose intersection $L \cap M$ is not
context-free.

Formalized by `Cslib.Language.exists_isContextFree_inf_not_isContextFree`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/NonClosure.lean, line 372](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/NonClosure.lean#L372). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/non-closure-of-context-free-languages/index.html#exists-is-context-free-inf-not-is-contex).

## Context-free languages are not closed under complement

There is a context-free language
$L$ over the three-letter alphabet $\{0, 1, 2\}$ whose complement is not context-free.

Closure under complement and union would give closure under intersection.

Formalized by `Cslib.Language.exists_isContextFree_compl_not_isContextFree`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/NonClosure.lean, line 380](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/NonClosure.lean#L380). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/non-closure-of-context-free-languages/index.html#exists-is-context-free-compl-not-is-cont).

## Intersections of context-free languages need not be context-free

Over the three-letter
alphabet $\{0, 1, 2\}$, it is not the case that for all context-free languages $L$ and $M$ the
intersection $L \cap M$ is context-free.

Formalized by `Cslib.Language.not_forall_isContextFree_inf`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/NonClosure.lean, line 408](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/NonClosure.lean#L408). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/non-closure-of-context-free-languages/index.html#not-forall-is-context-free-inf).

## Complements of context-free languages need not be context-free

It is not the case that
for every context-free language $L$ over the three-letter alphabet $\{0, 1, 2\}$, the complement
of $L$ is context-free.

Formalized by `Cslib.Language.not_forall_isContextFree_compl`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/NonClosure.lean, line 418](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/NonClosure.lean#L418). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/non-closure-of-context-free-languages/index.html#not-forall-is-context-free-compl).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Non-closure of context-free languages](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/non-closure-of-context-free-languages/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/non-closure-of-context-free-languages)
