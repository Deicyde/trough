---
declaration: section
origin: cited
lean: Cslib.Language.IsChomskyNormalForm, Cslib.Language.grammarTerminals, Cslib.Language.toCnfNT, Cslib.Language.fromCnfNT, Cslib.Language.cnfHead, Cslib.Language.cnfGrammar, Cslib.Language.cnfValuation, Cslib.Language.cnfGrammar_language_le_of_reduced
statement: formalized
proof: formalized
---

# Chomsky normal form

18 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/chomsky-normal-form/index.html).

## Chomsky normal form

A grammar is in Chomsky normal form when every production has
output either two nonterminals, a single terminal, or the empty word with the initial
nonterminal on the left; and either the initial nonterminal occurs in no output (so an empty
production cannot leak the empty word to other nonterminals) or there are no empty outputs at
all.

Formalized by `Cslib.Language.IsChomskyNormalForm`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/ChomskyNormalForm.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/ChomskyNormalForm.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/chomsky-normal-form/index.html#is-chomsky-normal-form).

## Terminals of a grammar

For a context-free grammar $G$, the list of terminals occurring
in the outputs of its productions: going through the productions of $G$ in a fixed but
unspecified order, list the terminals of each output from left to right. A terminal may appear
more than once.

Formalized by `Cslib.Language.grammarTerminals`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/ChomskyNormalForm.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/ChomskyNormalForm.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/chomsky-normal-form/index.html#grammar-terminals).

## Encoding symbols as basic nonterminals of the binarized grammar

Let $G$ be a
context-free grammar with nonterminals $N$, and let $t_0, \dots, t_{k-1}$ be the list of
terminals occurring in the production outputs of $G$. This map sends a symbol of $G$ to an
element of $N \sqcup \mathbb{N}$: a nonterminal $A$ goes to $A$, and a terminal $a$ goes to the
least index $i$ with $t_i = a$, or to $k$ if $a$ does not occur in the list.

Formalized by `Cslib.Language.toCnfNT`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/ChomskyNormalForm.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/ChomskyNormalForm.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/chomsky-normal-form/index.html#to-cnf-nt).

## Decoding basic nonterminals of the binarized grammar

Let $G$ be a context-free
grammar with nonterminals $N$ and initial nonterminal $S$, and let $t_0, \dots, t_{k-1}$ be
the list of terminals occurring in the production outputs of $G$. This map sends an element of
$N \sqcup \mathbb{N}$ (a basic nonterminal of the binarized grammar) to a symbol of $G$: a
nonterminal $A \in N$ goes to $A$, an index $i < k$ goes to the terminal $t_i$, and an index
$i \ge k$ goes to the nonterminal $S$.

Indices $i \ge k$ never arise from encoding nonterminals of $G$ or terminals occurring in the
production outputs of $G$.

Formalized by `Cslib.Language.fromCnfNT`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/ChomskyNormalForm.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/ChomskyNormalForm.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/chomsky-normal-form/index.html#from-cnf-nt).

## Head of a binarized output

Let $g$ be a context-free grammar and let
$a_0, a_1, \dots$ be its list of terminals occurring in production outputs. For a list
$\sigma$ of basic symbols (each a nonterminal of $g$ or a natural number, a terminal wrapper),
the head $h(\sigma)$ is the following form over the nonterminals of the binarized grammar
(basic symbols and chain nonterminals $\langle\tau\rangle$ for lists $\tau$ of basic symbols):
$h(XY) = XY$ for two basic symbols $X, Y$; $h(XYZ\tau) = X\langle YZ\tau\rangle$ for basic
symbols $X, Y, Z$ and a list $\tau$; $h(i) = a_i$ for a single natural number $i$ less than
the length of the list; and $h(\sigma)$ is empty in every other case (the empty list, a single
nonterminal of $g$, or a single out-of-range index).

Formalized by `Cslib.Language.cnfHead`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/ChomskyNormalForm.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/ChomskyNormalForm.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/chomsky-normal-form/index.html#cnf-head).

## Binarization of a grammar

Let $g$ be a context-free grammar with nonterminals $N$ and
initial nonterminal $S$, and let $t_0, \dots, t_{k-1}$ be the list of terminals occurring in the
production outputs of $g$. Encode each symbol of a production output of $g$ as a basic symbol in
$N \sqcup \mathbb{N}$: a nonterminal $A$ as $A$, and a terminal $a$ as the least index $i$ with
$t_i = a$. The binarized grammar of $g$ has as nonterminals the basic symbols together with a
chain nonterminal $\langle\tau\rangle$ for every list $\tau$ of basic symbols, and its initial
nonterminal is $S$. For a list $\sigma$ of basic symbols, its head $h(\sigma)$ is defined by
$h(XY) = XY$ and $h(XYZ\tau) = X\langle YZ\tau\rangle$ for basic symbols $X, Y, Z$ and a list
$\tau$, $h(i) = t_i$ for a single index $i < k$, and $h(\sigma)$ empty in every other case. For
every production $A \to \alpha$ of $g$, with $\sigma$ the encoding of $\alpha$ symbol by symbol,
the binarized grammar has the production $A \to h(\sigma)$, the production
$\langle\tau\rangle \to h(\tau)$ for every suffix $\tau$ of $\sigma$ (including $\sigma$ itself)
with at least two entries, and the production $i \to a$ for every terminal $a$ occurring in
$\alpha$, where $i$ is the encoding of $a$; it has no other productions.

This construction is meant for reduced grammars, which have no empty outputs and no outputs
consisting of a single nonterminal: on other grammars such outputs get the empty head, and in
general neither the language nor Chomsky normal form is preserved.

Formalized by `Cslib.Language.cnfGrammar`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/ChomskyNormalForm.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/ChomskyNormalForm.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/chomsky-normal-form/index.html#cnf-grammar).

## Valuation of the binarized grammar by yields

Let $g$ be a context-free grammar and let
$a_0, a_1, \dots$ be its list of terminals occurring in production outputs. A basic symbol is a
nonterminal of $g$ or a natural number (a terminal wrapper); the nonterminals of the binarized
grammar are the basic symbols together with a chain nonterminal $\langle\sigma\rangle$ for every
list $\sigma$ of basic symbols. Decode a basic symbol as a symbol of $g$: a nonterminal $A$ of
$g$ as $A$, a natural number $i$ less than the length of the list as the terminal $a_i$, and any
other natural number as the initial nonterminal of $g$. The valuation assigns to a basic symbol
$X$ the set of words that the decoding of $X$ yields in $g$, and to a chain nonterminal
$\langle\sigma\rangle$ the set of words that the symbolwise decoding of $\sigma$ yields in $g$.

Formalized by `Cslib.Language.cnfValuation`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/ChomskyNormalForm.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/ChomskyNormalForm.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/chomsky-normal-form/index.html#cnf-valuation).

## Binarization adds no words

If a context-free grammar $g$ is reduced, then every word
generated by the binarization of $g$ is generated by $g$.

Formalized by `Cslib.Language.cnfGrammar_language_le_of_reduced`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/ChomskyNormalForm.lean, line 382](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/ChomskyNormalForm.lean#L382). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/chomsky-normal-form/index.html#cnf-grammar-language-le-of-reduced).

## Binarization has no empty productions

If a context-free grammar $g$ is reduced, then
no production of the binarization of $g$ has the empty word as output.

Formalized by `Cslib.Language.cnfGrammar_output_ne_nil`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/ChomskyNormalForm.lean, line 406](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/ChomskyNormalForm.lean#L406). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/chomsky-normal-form/index.html#cnf-grammar-output-ne-nil).

## Binarization of a reduced grammar is in Chomsky normal form

If a context-free
grammar $g$ is reduced, then the binarization of $g$ is in Chomsky normal form.

Formalized by `Cslib.Language.cnfGrammar_isChomskyNormalForm`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/ChomskyNormalForm.lean, line 426](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/ChomskyNormalForm.lean#L426). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/chomsky-normal-form/index.html#cnf-grammar-is-chomsky-normal-form).

## Binarization preserves the language

If a context-free grammar $g$ is reduced, then
the binarization of $g$ generates exactly the language of $g$.

Formalized by `Cslib.Language.cnfGrammar_language_of_reduced`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/ChomskyNormalForm.lean, line 561](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/ChomskyNormalForm.lean#L561). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/chomsky-normal-form/index.html#cnf-grammar-language-of-reduced).

## Grammar with a fresh nullable start symbol

Given a context-free grammar $G$ with
nonterminals $N$ and initial nonterminal $S$, this is the grammar with nonterminals
$N \cup \{S_0\}$ for a fresh symbol $S_0$, initial nonterminal $S_0$, and the following
productions: every production of $G$; the empty production $S_0 \to \varepsilon$; and
$S_0 \to \alpha$ for every production $S \to \alpha$ of $G$.

The new grammar generates the language of $G$ plus the empty word, and stays in Chomsky normal
form when $G$ is in Chomsky normal form and has no empty outputs.

Formalized by `Cslib.Language.epsStartGrammar`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/ChomskyNormalForm.lean, line 584](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/ChomskyNormalForm.lean#L584). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/chomsky-normal-form/index.html#eps-start-grammar).

## Language of the grammar with a fresh nullable start symbol

For every context-free
grammar $G$, the grammar obtained from $G$ by adding a fresh initial nonterminal (with an empty
production and copies of the productions of the old initial nonterminal) generates exactly
$L(G) \cup \{\varepsilon\}$, where $L(G)$ is the language of $G$ and $\varepsilon$ is the
empty word.

Formalized by `Cslib.Language.epsStartGrammar_language`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/ChomskyNormalForm.lean, line 667](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/ChomskyNormalForm.lean#L667). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/chomsky-normal-form/index.html#eps-start-grammar-language).

## The fresh start symbol occurs in no output

For every context-free grammar $g$, the
fresh initial nonterminal of the fresh-start grammar of $g$ occurs in no production output of
the fresh-start grammar.

Formalized by `Cslib.Language.epsStartGrammar_initial_not_mem_output`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/ChomskyNormalForm.lean, line 707](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/ChomskyNormalForm.lean#L707). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/chomsky-normal-form/index.html#eps-start-grammar-initial-not-mem-output).

## A fresh start symbol is harmless when the empty word is generated

If the empty word
belongs to the language of a context-free grammar $g$, then the fresh-start grammar of $g$
generates exactly the language of $g$.

Formalized by `Cslib.Language.epsStartGrammar_language_of_mem_nil`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/ChomskyNormalForm.lean, line 728](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/ChomskyNormalForm.lean#L728). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/chomsky-normal-form/index.html#eps-start-grammar-language-of-mem-nil).

## Adding a fresh start symbol preserves Chomsky normal form

If a context-free grammar
$g$ is in Chomsky normal form and no production of $g$ has empty output, then the fresh-start
grammar of $g$ is in Chomsky normal form.

The no-empty-outputs hypothesis is essential: an existing empty production would be embedded
with the old initial nonterminal, not the fresh one, on the left.

Formalized by `Cslib.Language.epsStartGrammar_isChomskyNormalForm`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/ChomskyNormalForm.lean, line 738](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/ChomskyNormalForm.lean#L738). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/chomsky-normal-form/index.html#eps-start-grammar-is-chomsky-normal-form).

## Chomsky normal form theorem

For every context-free grammar $G$ there is a
context-free grammar in Chomsky normal form that generates the same language as $G$.

Formalized by `Cslib.Language.exists_chomskyNormalForm`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/ChomskyNormalForm.lean, line 767](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/ChomskyNormalForm.lean#L767). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/chomsky-normal-form/index.html#exists-chomsky-normal-form).

## Chomsky normal form for context-free languages

Every context-free language $L$ is
generated by some context-free grammar in Chomsky normal form.

Formalized by `Cslib.Language.IsContextFree.exists_chomskyNormalForm`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/ChomskyNormalForm.lean, line 800](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/ChomskyNormalForm.lean#L800). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/chomsky-normal-form/index.html#exists-chomsky-normal-form-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Chomsky normal form](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/chomsky-normal-form/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/chomsky-normal-form)
