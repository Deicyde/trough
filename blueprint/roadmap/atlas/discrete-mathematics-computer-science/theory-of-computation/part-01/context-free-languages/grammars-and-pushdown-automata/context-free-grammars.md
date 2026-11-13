---
declaration: section
origin: cited
lean: Cslib.Language.evalSymbol, Cslib.Language.evalForm, Cslib.Language.evalForm_append, Cslib.Language.evalForm_map_terminal, Cslib.Language.IsValuation, Cslib.Language.evalForm_le_of_produces, Cslib.Language.evalForm_le_of_derives, Cslib.Language.language_le_of_valuation
statement: formalized
proof: formalized
---

# Context-free grammars

30 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/context-free-grammars/index.html).

## Interpretation of a grammar symbol

Under an assignment $V$ of languages to nonterminals, a
terminal $a$ denotes the language containing only the one-letter word $a$, and a nonterminal $A$
denotes its assigned language $V(A)$.

Formalized by `Cslib.Language.evalSymbol`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/Basic.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/Basic.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/context-free-grammars/index.html#eval-symbol).

## Interpretation of a sentential form

Under an assignment $V$ of languages to nonterminals, a
sentential form denotes the concatenation, in order, of the languages its symbols denote: a
terminal $a$ denotes the language containing only the one-letter word $a$, and a nonterminal $A$
denotes $V(A)$. The empty sentential form denotes the language containing only the empty word.

Formalized by `Cslib.Language.evalForm`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/Basic.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/Basic.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/context-free-grammars/index.html#eval-form).

## Interpretation of a concatenation

For every assignment $V$ of languages to nonterminals and
all sentential forms $u$ and $v$, the language that $uv$ denotes under $V$ is the concatenation of
the languages that $u$ and $v$ denote under $V$.

Formalized by `Cslib.Language.evalForm_append`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Basic.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/Basic.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/context-free-grammars/index.html#eval-form-append).

## A terminal word denotes its singleton

Under every assignment of languages to
nonterminals, a terminal word $w$, read as a sentential form, denotes the singleton language
$\{w\}$.

Formalized by `Cslib.Language.evalForm_map_terminal`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Basic.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/Basic.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/context-free-grammars/index.html#eval-form-map-terminal).

## Valuation of a grammar

Let $g$ be a context-free grammar with terminals $T$, and let $V$
assign a language over $T$ to each nonterminal of $g$. Interpret a sentential form under $V$ by
sending each terminal $a$ to the language $\{a\}$ of the one-letter word $a$ and each nonterminal
$B$ to $V(B)$, and concatenating these languages in order (the empty form is interpreted as
$\{\varepsilon\}$). Then $V$ is a *valuation* of $g$ when, for every production $A \to u$
of $g$, the interpretation of $u$ under $V$ is contained in $V(A)$.

Formalized by `Cslib.Language.IsValuation`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/Basic.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/Basic.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/context-free-grammars/index.html#is-valuation).

## A production step shrinks interpretations under a valuation

Let $g$ be a context-free
grammar and $V$ a valuation of $g$. If a sentential form $u$ rewrites to $v$ by one production of
$g$, then the language that $v$ denotes under $V$ is contained in the language that $u$ denotes
under $V$.

Formalized by `Cslib.Language.evalForm_le_of_produces`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Basic.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/Basic.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/context-free-grammars/index.html#eval-form-le-of-produces).

## Derivations shrink interpretations under a valuation

Let $g$ be a context-free grammar and
$V$ a valuation of $g$. If a sentential form $u$ derives $v$ in $g$ (in zero or more steps), then
the language that $v$ denotes under $V$ is contained in the language that $u$ denotes under $V$.

Formalized by `Cslib.Language.evalForm_le_of_derives`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Basic.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/Basic.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/context-free-grammars/index.html#eval-form-le-of-derives).

## Valuations bound the language of a grammar

For every context-free grammar $g$ and every
valuation $V$ of $g$, the language generated by $g$ is contained in $V(S)$, where $S$ is the
initial nonterminal of $g$.

Formalized by `Cslib.Language.language_le_of_valuation`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Basic.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/Basic.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/context-free-grammars/index.html#language-le-of-valuation).

## Concatenating derivations

Let $g$ be a context-free grammar and let $u$, $u'$, $v$, $v'$
be sentential forms of $g$. If $u$ derives $u'$ and $v$ derives $v'$ in $g$ (each in zero or more
steps), then the concatenation $uv$ derives $u'v'$ in $g$.

Formalized by `Cslib.Language.derives_append`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Basic.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/Basic.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/context-free-grammars/index.html#derives-append).

## Renaming the nonterminals of a symbol

Given a map $f$ from nonterminals $N$ to
nonterminals $N'$, renaming a grammar symbol by $f$ leaves a terminal $a$ unchanged and sends a
nonterminal $A$ to the nonterminal $f(A)$.

Formalized by `Cslib.Language.mapSymbol`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/Basic.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/Basic.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/context-free-grammars/index.html#map-symbol).

## Renaming the nonterminals of a production

Given a map $f$ from nonterminals $N$ to
nonterminals $N'$, the renaming by $f$ of a production $A \to u$ is the production
$f(A) \to u'$, where $u'$ is obtained from $u$ by replacing each nonterminal $B$ with $f(B)$ and
leaving each terminal unchanged.

Formalized by `Cslib.Language.mapRule`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/Basic.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/Basic.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/context-free-grammars/index.html#map-rule).

## Interpretation after renaming nonterminals

Let $f \colon N \to N'$ be a map of
nonterminals, extended to sentential forms by renaming each nonterminal and keeping each terminal,
and let $V$ assign a language to each nonterminal in $N'$. For every sentential form $u$ over $N$,
the language that $f(u)$ denotes under $V$ equals the language that $u$ denotes under the
assignment $V \circ f$.

Formalized by `Cslib.Language.evalForm_map`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Basic.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/Basic.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/context-free-grammars/index.html#eval-form-map).

## Derivations transfer along a renaming of nonterminals

Let $g$ and $G$ be context-free
grammars over the same terminal alphabet, and let $f$ map the nonterminals of $g$ to those of $G$.
Extend $f$ to symbols and sentential forms by renaming each nonterminal and keeping each terminal.
Suppose that for every production $A \to \alpha$ of $g$, the renamed production $f(A) \to f(\alpha)$
is a production of $G$. Then whenever a sentential form $u$ derives $v$ in $g$ (in zero or more
steps), $f(u)$ derives $f(v)$ in $G$.

No injectivity of $f$ is needed for this direction.

Formalized by `Cslib.Language.derives_map_of_forall_mem`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Basic.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/Basic.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/context-free-grammars/index.html#derives-map-of-forall-mem).

## Language generated from a nonterminal

For a context-free grammar $g$ and a nonterminal
$A$ of $g$, the language generated by $g$ from $A$ is the set of words $w$ over the terminals of
$g$ such that $g$ derives $w$ from the one-symbol sentential form $A$. It is the language of $g$
with $A$ in place of the initial nonterminal.

Formalized by `Cslib.Language.languageFrom`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/Basic.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/Basic.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/context-free-grammars/index.html#language-from).

## Words of the canonical interpretation are derivable

Let $g$ be a context-free grammar and
assign to each nonterminal $A$ of $g$ the language of terminal words that $g$ derives from $A$. If a
terminal word $w$ lies in the language that a sentential form $u$ of $g$ denotes under this
assignment, then $u$ derives $w$ in $g$.

Formalized by `Cslib.Language.derives_of_mem_evalForm_languageFrom`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Basic.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/Basic.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/context-free-grammars/index.html#derives-of-mem-eval-form-language-from).

## The languages generated from each nonterminal form a valuation

For every context-free
grammar $g$, the assignment that sends each nonterminal $A$ of $g$ to the language generated by
$g$ from $A$ is a valuation of $g$.

Formalized by `Cslib.Language.isValuation_languageFrom`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Basic.lean, line 258](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/Basic.lean#L258). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/context-free-grammars/index.html#is-valuation-language-from).

## Injective renamings are injective on symbols

If $f$ is an injective map from
nonterminals $N$ to nonterminals $N'$, then renaming grammar symbols by $f$, which fixes each
terminal and sends each nonterminal $A$ to $f(A)$, is injective.

Formalized by `Cslib.Language.mapSymbol_injective`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Basic.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/Basic.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/context-free-grammars/index.html#map-symbol-injective).

## Injective renamings are injective on productions

If $f$ is an injective map from
nonterminals $N$ to nonterminals $N'$, then renaming the nonterminals of productions over $N$ by
$f$ is injective: two productions with the same renaming are equal.

In particular, renaming a finite set of productions by $f$ merges none of them.

Formalized by `Cslib.Language.mapRule_injective`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Basic.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/Basic.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/context-free-grammars/index.html#map-rule-injective).

## Renaming nonterminals fixes terminal words

Let $f$ map nonterminals $N$ to nonterminals
$N'$, and let $w$ be a word over the terminals. Reading $w$ as a sentential form over $N$ and
renaming its nonterminals by $f$ gives $w$ read as a sentential form over $N'$.

Formalized by `Cslib.Language.map_mapSymbol_terminal`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Basic.lean, line 287](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/Basic.lean#L287). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/context-free-grammars/index.html#map-map-symbol-terminal).

## The empty language is context-free

The empty language over any alphabet is
context-free: take a grammar with no productions.

Formalized by `Cslib.Language.IsContextFree.zero`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Basic.lean, line 292](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/Basic.lean#L292). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/context-free-grammars/index.html#zero).

## The language of the empty word is context-free

For every alphabet $T$, the language
over $T$ whose only word is the empty word is context-free: a grammar with one nonterminal and
a single production erasing it generates this language.

Formalized by `Cslib.Language.IsContextFree.one`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Basic.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/Basic.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/context-free-grammars/index.html#one).

## Singleton languages are context-free

For every word $w$ over an alphabet $T$, the
language $\{w\}$ consisting of $w$ alone is context-free: one production spells the word out.

Formalized by `Cslib.Language.IsContextFree.singleton_word`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Basic.lean, line 315](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/Basic.lean#L315). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/context-free-grammars/index.html#singleton-word).

## Yield of a sentential form

For a context-free grammar $g$ with terminal alphabet
$T$, the relation "the sentential form $u$ yields the terminal word $w$" is the smallest
relation such that: the empty form yields the empty word; if $u$ yields $w$, then for every
terminal $a$ the form $a u$ yields $a w$; and if $A \to \alpha$ is a production of $g$,
$\alpha$ yields $w_1$ and $u$ yields $w_2$, then the form $A u$ yields $w_1 w_2$.

Formalized by `Cslib.Language.Yields`, an inductive type declared in [CSLibExt/Computability/Languages/ContextFree/Yields.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/Yields.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/context-free-grammars/index.html#yields).

## Concatenation of yields

Let $g$ be a context-free grammar. If the sentential form
$u$ yields the terminal word $w_1$ and the sentential form $v$ yields the terminal word
$w_2$, then the concatenated form $u v$ yields $w_1 w_2$.

Formalized by `Cslib.Language.Yields.append`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Yields.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/Yields.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/context-free-grammars/index.html#append).

## Splitting a yield over a concatenation

Let $g$ be a context-free grammar. If the
concatenated sentential form $u v$ yields the terminal word $w$, then there are terminal
words $w_1$ and $w_2$ with $w = w_1 w_2$ such that $u$ yields $w_1$ and $v$ yields $w_2$.

Formalized by `Cslib.Language.Yields.append_inv`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Yields.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/Yields.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/context-free-grammars/index.html#append-inv).

## Yield through one production

Let $g$ be a context-free grammar and $A \to \alpha$ a
production of $g$. If $\alpha$ yields the terminal word $w$, then the one-symbol sentential
form $A$ yields $w$.

Formalized by `Cslib.Language.yields_of_rule`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Yields.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/Yields.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/context-free-grammars/index.html#yields-of-rule).

## Yields are derivable

Let $g$ be a context-free grammar. If the sentential form $u$
yields the terminal word $w$, then $u$ derives $w$, read as a string of terminal symbols,
in $g$: that is, $u \Rightarrow^* w$ in zero or more rewriting steps.

Formalized by `Cslib.Language.derives_of_yields`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Yields.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/Yields.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/context-free-grammars/index.html#derives-of-yields).

## Derivable terminal words are yields

Let $g$ be a context-free grammar. If the
sentential form $u$ derives the terminal word $w$, read as a string of terminal symbols,
in $g$, then $u$ yields $w$.

The proof is the valuation argument: the languages yielded by the nonterminals form a
valuation.

Formalized by `Cslib.Language.yields_of_derives`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Yields.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/Yields.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/context-free-grammars/index.html#yields-of-derives).

## Yields coincide with derivations of terminal words

Let $g$ be a context-free grammar,
$u$ a sentential form of $g$ and $w$ a word of terminals. Then $u$ yields $w$ in $g$ if and only
if $u$ derives in $g$, by zero or more rewriting steps, the sentential form consisting of the
letters of $w$ read as terminals.

Formalized by `Cslib.Language.yields_iff_derives`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Yields.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/Yields.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/context-free-grammars/index.html#yields-iff-derives).

## Language membership through yields

Let $g$ be a context-free grammar with initial
nonterminal $S$. A terminal word $w$ belongs to the language of $g$ if and only if the
one-symbol sentential form $S$ yields $w$.

Formalized by `Cslib.Language.mem_language_iff_yields`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Yields.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/Yields.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/context-free-grammars/index.html#mem-language-iff-yields).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Context-free grammars](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/context-free-grammars/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/context-free-grammars)
