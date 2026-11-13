---
declaration: section
origin: cited
lean: Cslib.Decidability.Grammar.letterSym, Cslib.Decidability.Grammar.indexSym, Cslib.Decidability.Grammar.ntSym, Cslib.Decidability.Grammar.domino, Cslib.Decidability.Grammar.contRule, Cslib.Decidability.Grammar.termRule, Cslib.Decidability.Grammar.sideRules, Cslib.Decidability.Grammar.sideGrammar
statement: formalized
proof: formalized
---

# Intersection problem for context-free languages

18 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/intersection-problem-for-context-free-languages/index.html).

## The grammars

## The encoded letter terminal

For a letter $a \in \alpha$, this is $a$ as an encoded
terminal over the alphabet $\alpha \oplus \mathbb{N}$: the element $\mathrm{inr}(\mathrm{inl}\, a)$
of $\mathbb{N} \oplus (\alpha \oplus \mathbb{N})$, whose left summand $\mathbb{N}$ holds the
nonterminals and whose right summand holds the terminals.

Formalized by `Cslib.Decidability.Grammar.letterSym`, a definition declared in [CSLibExt/Computability/Decidability/CFGUndecidable.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/CFGUndecidable.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/intersection-problem-for-context-free-languages/index.html#letter-sym).

## The encoded index terminal

For $i \in \mathbb{N}$, this is the index $i$ as an encoded
terminal over the alphabet $\alpha \oplus \mathbb{N}$: the element $\mathrm{inr}(\mathrm{inr}\, i)$
of $\mathbb{N} \oplus (\alpha \oplus \mathbb{N})$, whose left summand $\mathbb{N}$ holds the
nonterminals and whose right summand holds the terminals.

Formalized by `Cslib.Decidability.Grammar.indexSym`, a definition declared in [CSLibExt/Computability/Decidability/CFGUndecidable.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/CFGUndecidable.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/intersection-problem-for-context-free-languages/index.html#index-sym).

## Encoded nonterminal symbol

For a natural number $A$, the nonterminal $A$ as a symbol of
the right-hand side of an encoded production over the terminals $\alpha \sqcup \mathbb{N}$: the
left injection of $A$ into $\mathbb{N} \sqcup (\alpha \sqcup \mathbb{N})$.

Formalized by `Cslib.Decidability.Grammar.ntSym`, a definition declared in [CSLibExt/Computability/Decidability/CFGUndecidable.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/CFGUndecidable.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/intersection-problem-for-context-free-languages/index.html#nt-sym).

## The $i$-th domino of a list

For a list $P$ of dominoes and $i \in \mathbb{N}$, this is the
$i$-th domino of $P$ (counting from $0$) when $i$ is less than the length of $P$, and the domino
whose top and bottom words are both empty otherwise.

Formalized by `Cslib.Decidability.Grammar.domino`, a definition declared in [CSLibExt/Computability/Decidability/CFGUndecidable.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/CFGUndecidable.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/intersection-problem-for-context-free-languages/index.html#domino).

## The continuation production

For a list $P$ of dominoes, a map $\sigma$ assigning a word
over $\alpha$ to each domino, a nonterminal $A \in \mathbb{N}$ and an index $i \in \mathbb{N}$,
this is the production $A \to w_i\, A\, i$ in encoded form, where $w_i$ is $\sigma$ applied to the
$i$-th domino of $P$ (the domino with both words empty when $i$ is past the end of $P$): its
right-hand side is the letters of $w_i$ as terminals, then the nonterminal $A$, then the index
terminal $i$.

Formalized by `Cslib.Decidability.Grammar.contRule`, a definition declared in [CSLibExt/Computability/Decidability/CFGUndecidable.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/CFGUndecidable.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/intersection-problem-for-context-free-languages/index.html#cont-rule).

## The terminating production of a side grammar

Let $P = (d_0, \dots, d_{k-1})$ be a list
of dominoes over $\alpha$, set $d_i = (\varepsilon, \varepsilon)$ for $i \ge k$, let $\sigma$
assign a word over $\alpha$ to each domino, and write $w_i = \sigma(d_i)$. For a nonterminal $A$
and a natural number $i$, this is the encoded production $A \to w_i \, i$, whose right-hand side
is the letters of $w_i$ as terminals followed by the index terminal $i$.

Formalized by `Cslib.Decidability.Grammar.termRule`, a definition declared in [CSLibExt/Computability/Decidability/CFGUndecidable.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/CFGUndecidable.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/intersection-problem-for-context-free-languages/index.html#term-rule).

## The productions of a side grammar

Let $P = (d_0, \dots, d_{k-1})$ be a list of dominoes
over $\alpha$, let $\sigma$ assign a word over $\alpha$ to each domino, write $w_i = \sigma(d_i)$,
and let $A$ be a nonterminal. The side productions are the list of encoded productions
$A \to w_i \, A \, i$ and $A \to w_i \, i$ for $i = 0, 1, \dots, k - 1$, where the letters of
$w_i$ are terminals and $i$ is an index terminal.

Formalized by `Cslib.Decidability.Grammar.sideRules`, a definition declared in [CSLibExt/Computability/Decidability/CFGUndecidable.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/CFGUndecidable.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/intersection-problem-for-context-free-languages/index.html#side-rules).

## The side grammar of a PCP instance

Let $P = (d_0, \dots, d_{k-1})$ be a list of dominoes
over $\alpha$, let $\sigma$ assign a word over $\alpha$ to each domino, and write
$w_i = \sigma(d_i)$. The side grammar of $\sigma$ and $P$ is the encoded context-free grammar
whose terminals are the letters of $\alpha$ and the index terminals $0, 1, 2, \dots$, whose start
nonterminal is $S = 0$, and whose productions are $S \to w_i \, S \, i$ and $S \to w_i \, i$ for
each $i < k$. Taking for $\sigma$ the top word of a domino gives the top grammar of $P$, and the
bottom word the bottom grammar.

Formalized by `Cslib.Decidability.Grammar.sideGrammar`, a definition declared in [CSLibExt/Computability/Decidability/CFGUndecidable.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/CFGUndecidable.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/intersection-problem-for-context-free-languages/index.html#side-grammar).

## The letter part of an index sequence

For a list $P$ of dominoes, a map $\sigma$ assigning
a word over $\alpha$ to each domino, and a sequence $i_1, \dots, i_n$ of natural numbers, this is
the word $w_{i_1} w_{i_2} \cdots w_{i_n}$ over $\alpha$, where $w_i$ is $\sigma$ applied to the
$i$-th domino of $P$ (the domino with both words empty when $i$ is past the end of $P$).

Formalized by `Cslib.Decidability.Grammar.flat`, a definition declared in [CSLibExt/Computability/Decidability/CFGUndecidable.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/CFGUndecidable.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/intersection-problem-for-context-free-languages/index.html#flat).

## The side word of an index sequence

Let $P = (d_0, \dots, d_{k-1})$ be a list of dominoes
over $\alpha$, set $d_i = (\varepsilon, \varepsilon)$ for $i \ge k$, let $\sigma$ assign a word
over $\alpha$ to each domino, and write $w_i = \sigma(d_i)$. The side word of a sequence
$i_1, \dots, i_n$ of natural numbers is the word $w_{i_1} \cdots w_{i_n} \, i_n \cdots i_1$ over
the letters of $\alpha$ and the index terminals $0, 1, 2, \dots$: the letters of
$w_{i_1}, \dots, w_{i_n}$ followed by the indices in reverse order.

Formalized by `Cslib.Decidability.Grammar.sideWord`, a definition declared in [CSLibExt/Computability/Decidability/CFGUndecidable.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/CFGUndecidable.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/intersection-problem-for-context-free-languages/index.html#side-word).

## A terminal word derives only itself

Let $g$ be a context-free grammar with terminal
alphabet $\alpha \oplus \mathbb{N}$ and let $u$ be a word over $\alpha \oplus \mathbb{N}$. If $g$
derives a sentential form $v$ from $u$, read as a string of terminals, then $v = u$.

Formalized by `Cslib.Decidability.Grammar.eq_of_derives_terminal`, a theorem declared in [CSLibExt/Computability/Decidability/CFGUndecidable.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/CFGUndecidable.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/intersection-problem-for-context-free-languages/index.html#eq-of-derives-terminal).

## Splitting a sentential form at its single nonterminal

Let $N$ be a type of nonterminals,
$u, v$ words over $\alpha \oplus \mathbb{N}$, $A, B \in N$, and $p, q$ strings of terminals in
$\alpha \oplus \mathbb{N}$ and nonterminals in $N$. If $u\, A\, v = p\, B\, q$, where $u$ and $v$
are read as strings of terminals, then $p = u$, $B = A$ and $q = v$.

Formalized by `Cslib.Decidability.Grammar.eq_of_terminal_append_nonterminal`, a theorem declared in [CSLibExt/Computability/Decidability/CFGUndecidable.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/CFGUndecidable.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/intersection-problem-for-context-free-languages/index.html#eq-of-terminal-append-nonterminal).

## The analysis of derivations

Let $P$ be a list of dominoes, $\sigma$ a map assigning a word
over $\alpha$ to each domino, and $G$ the context-free grammar of the side grammar of $P$ for
$\sigma$, with start nonterminal $S$ and terminals $\alpha \oplus \mathbb{N}$ (letters and
indices). Let $u, v, x$ be words over $\alpha \oplus \mathbb{N}$. If $G$ derives the terminal word
$x$ from the sentential form $u\, S\, v$, then there is a nonempty sequence $i_1, \dots, i_n$ of
indices, each less than the length of $P$, such that
$x = u\, w_{i_1} \cdots w_{i_n}\, i_n \cdots i_1\, v$, where $w_i$ is $\sigma$ applied to the
$i$-th domino of $P$.

Such a derivation applies $S \to w_i\, S\, i$ for each index but the last and then
$S \to w_i\, i$.

Formalized by `Cslib.Decidability.Grammar.eq_sideWord_of_derives`, a theorem declared in [CSLibExt/Computability/Decidability/CFGUndecidable.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/CFGUndecidable.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/intersection-problem-for-context-free-languages/index.html#eq-side-word-of-derives).

## The construction of derivations

Let $P$ be a list of dominoes, $\sigma$ a map assigning a
word over $\alpha$ to each domino, and $G$ the context-free grammar of the side grammar of $P$ for
$\sigma$, with start nonterminal $S$ and terminals $\alpha \oplus \mathbb{N}$ (letters and
indices). For every nonempty sequence $i_1, \dots, i_n$ of indices, each less than the length of
$P$, and all words $u, v$ over $\alpha \oplus \mathbb{N}$, $G$ derives the terminal word
$u\, w_{i_1} \cdots w_{i_n}\, i_n \cdots i_1\, v$ from the sentential form $u\, S\, v$, where
$w_i$ is $\sigma$ applied to the $i$-th domino of $P$.

Formalized by `Cslib.Decidability.Grammar.derives_sideWord`, a theorem declared in [CSLibExt/Computability/Decidability/CFGUndecidable.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/CFGUndecidable.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/intersection-problem-for-context-free-languages/index.html#derives-side-word).

## The language of a side grammar

Let $\alpha$ be an alphabet with decidable equality,
let $P = (d_0, \dots, d_{k-1})$ be a list of dominoes over $\alpha$, let $\sigma$ assign a word
over $\alpha$ to each domino, and write $w_i = \sigma(d_i)$. A word $u$ over the letters of
$\alpha$ and the index terminals $0, 1, 2, \dots$ lies in the language of the side grammar of
$\sigma$ and $P$ if and only if there is a nonempty sequence of indices $i_1, \dots, i_n$, each
less than $k$, with $u = w_{i_1} \cdots w_{i_n} \, i_n \cdots i_1$.

Formalized by `Cslib.Decidability.Grammar.mem_language_sideGrammar`, a theorem declared in [CSLibExt/Computability/Decidability/CFGUndecidable.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/CFGUndecidable.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/intersection-problem-for-context-free-languages/index.html#mem-language-side-grammar).

## Unique splitting of letters followed by markers

Let $A, C$ be words over $\alpha$ and
$B, D$ words over $\beta$, all viewed as words over the disjoint union $\alpha \oplus \beta$. If
$AB = CD$ as words over $\alpha \oplus \beta$, then $A = C$ and $B = D$.

Formalized by `Cslib.Decidability.Grammar.eq_of_map_inl_append_map_inr`, a theorem declared in [CSLibExt/Computability/Decidability/CFGUndecidable.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/CFGUndecidable.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/intersection-problem-for-context-free-languages/index.html#eq-of-map-inl-append-map-inr).

## A PCP instance is solvable exactly when its top and bottom grammars share a word

Let
$P$ be a list of dominoes over an alphabet $\alpha$ with decidable equality. Then $P$ has a PCP
solution if and only if some word lies both in the language of the side grammar of $P$ for the
top words and in the language of the side grammar of $P$ for the bottom words.

Formalized by `Cslib.Decidability.Grammar.pcp_iff_exists_mem_inter`, a theorem declared in [CSLibExt/Computability/Decidability/CFGUndecidable.lean, line 307](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/CFGUndecidable.lean#L307). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/intersection-problem-for-context-free-languages/index.html#pcp-iff-exists-mem-inter).

## PCP many-one reduces to nonemptiness of the intersection of two context-free languages

**PCP many-one reduces to nonemptiness of the intersection of two context-free
languages.** Let $\alpha$ be an alphabet with a primitive recursive encoding and decidable
equality. The Post correspondence problem over $\alpha$ is many-one reducible to the problem of
deciding, for a pair $(G_1, G_2)$ of encoded context-free grammars whose terminals are the letters
of $\alpha$ together with the natural numbers, whether some word lies in both the language of
$G_1$ and the language of $G_2$: there is a computable map sending each list $P$ of dominoes over
$\alpha$ to such a pair, with $P$ having a PCP solution if and only if the two languages share a
word.

Formalized by `Cslib.Decidability.Grammar.manyOneReducible_pcp_inter`, a theorem declared in [CSLibExt/Computability/Decidability/CFGUndecidable.lean, line 356](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/CFGUndecidable.lean#L356). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/intersection-problem-for-context-free-languages/index.html#many-one-reducible-pcp-inter).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Intersection problem for context-free languages](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/intersection-problem-for-context-free-languages/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/undecidable-problems/intersection-problem-for-context-free-languages)
