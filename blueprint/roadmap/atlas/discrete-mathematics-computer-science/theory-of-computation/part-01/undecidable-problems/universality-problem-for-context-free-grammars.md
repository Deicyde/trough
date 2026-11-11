---
declaration: section
origin: cited
lean: Cslib.Decidability.Grammar.bitCode, Cslib.Decidability.Grammar.bitCodes, Cslib.Decidability.Grammar.listWord, Cslib.Decidability.Grammar.listLang, Cslib.Decidability.Grammar.bitCodes_injective, Cslib.Decidability.Grammar.pcp_iff_exists_mem_listLang, Cslib.Decidability.Grammar.uNt, Cslib.Decidability.Grammar.uLetter
statement: formalized
proof: formalized
---

# Universality problem for context-free grammars

36 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/universality-problem-for-context-free-grammars/index.html).

## Index codes and list languages

## Unary code of an index

The code of an index $i \in \mathbb{N}$ is the bit word
$\mathbf{t}\,\mathbf{f}^i$ of length $i + 1$: the bit $\mathbf{t}$ (true) followed by $i$ copies
of the bit $\mathbf{f}$ (false); with $|$ for true and $1$ for false, it is the word $|\,1^i$.

Formalized by `Cslib.Decidability.Grammar.bitCode`, a definition declared in [CSLibExt/Computability/Decidability/PCPUniversality.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUniversality.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/universality-problem-for-context-free-grammars/index.html#bit-code).

## Concatenated code of an index sequence

For a finite sequence $I = (i_1, \dots, i_n)$
of natural numbers, its code is the bit word $c(i_1)\,c(i_2) \cdots c(i_n)$, the concatenation of
the unary codes $c(i) = \mathbf{t}\,\mathbf{f}^i$ of its entries; the empty sequence has the
empty code.

Formalized by `Cslib.Decidability.Grammar.bitCodes`, a definition declared in [CSLibExt/Computability/Decidability/PCPUniversality.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUniversality.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/universality-problem-for-context-free-grammars/index.html#bit-codes).

## List word of an index sequence

Let $P = (d_0, \dots, d_{m-1})$ be a list of dominoes over
$\alpha$, let $s$ be a function sending each domino to a word over $\alpha$, and set
$w_i = s(d_i)$ for $i < m$ and $w_i = s(\varepsilon, \varepsilon)$ for $i \ge m$, where
$(\varepsilon, \varepsilon)$ is the domino with empty top and bottom. The list word of an index
sequence $i_1, \dots, i_n$ is the word $w_{i_1} \cdots w_{i_n}\, c(i_n) \cdots c(i_1)$ over
$\alpha \oplus \mathrm{Bool}$, where $c(i)$ is the unary code of $i$: the bit $\mathrm{true}$
followed by $i$ bits $\mathrm{false}$.

Formalized by `Cslib.Decidability.Grammar.listWord`, a definition declared in [CSLibExt/Computability/Decidability/PCPUniversality.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUniversality.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/universality-problem-for-context-free-grammars/index.html#list-word).

## List language of a PCP instance

Let $P = (d_0, \dots, d_{m-1})$ be a list of dominoes
over $\alpha$, let $s$ be a function sending each domino to a word over $\alpha$ (for instance its
top word), and write $w_i = s(d_i)$. The list language of $s$ and $P$ is the language over
$\alpha \oplus \mathrm{Bool}$ of all words $w_{i_1} \cdots w_{i_n}\, c(i_n) \cdots c(i_1)$ with
$n \ge 1$ and $i_1, \dots, i_n < m$, where $c(i)$ is the unary code of $i$: the bit
$\mathrm{true}$ followed by $i$ bits $\mathrm{false}$.

Formalized by `Cslib.Decidability.Grammar.listLang`, a definition declared in [CSLibExt/Computability/Decidability/PCPUniversality.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUniversality.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/universality-problem-for-context-free-grammars/index.html#list-lang).

## Concatenated index codes are uniquely decodable

For a finite sequence
$I = (i_1, \dots, i_n)$ of natural numbers write $c(I) = c(i_1) \cdots c(i_n)$, where
$c(i) = \mathbf{t}\,\mathbf{f}^i$ is the unary code of $i$. If $I$ and $J$ are finite sequences of
natural numbers with $c(I) = c(J)$, then $I = J$.

Formalized by `Cslib.Decidability.Grammar.bitCodes_injective`, a theorem declared in [CSLibExt/Computability/Decidability/PCPUniversality.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUniversality.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/universality-problem-for-context-free-grammars/index.html#bit-codes-injective).

## A PCP instance is solvable exactly when its top and bottom list languages meet

A list $P$
of dominoes has a PCP solution if and only if some word belongs both to the list language of the
top words of $P$ and to the list language of the bottom words of $P$.

Formalized by `Cslib.Decidability.Grammar.pcp_iff_exists_mem_listLang`, a theorem declared in [CSLibExt/Computability/Decidability/PCPUniversality.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUniversality.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/universality-problem-for-context-free-grammars/index.html#pcp-iff-exists-mem-list-lang).

## Encoded nonterminal

For a type $\alpha$ and a natural number $A$, the nonterminal $A$ as a
symbol of an encoded grammar over the alphabet $\alpha \oplus \mathrm{Bool}$, that is, the element
$\mathrm{inl}\, A$ of $\mathbb{N} \oplus (\alpha \oplus \mathrm{Bool})$.

Formalized by `Cslib.Decidability.Grammar.uNt`, a definition declared in [CSLibExt/Computability/Decidability/PCPUniversality.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUniversality.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/universality-problem-for-context-free-grammars/index.html#u-nt).

## Encoded letter terminal

For a letter $a \in \alpha$, the terminal $a$ of the alphabet
$\alpha \oplus \mathrm{Bool}$ as a symbol of an encoded grammar, that is, the element
$\mathrm{inr}(\mathrm{inl}\, a)$ of $\mathbb{N} \oplus (\alpha \oplus \mathrm{Bool})$.

Formalized by `Cslib.Decidability.Grammar.uLetter`, a definition declared in [CSLibExt/Computability/Decidability/PCPUniversality.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUniversality.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/universality-problem-for-context-free-grammars/index.html#u-letter).

## Encoded bit terminal

For a type $\alpha$ and a bit $b$, the terminal $b$ of the alphabet
$\alpha \oplus \mathrm{Bool}$ as a symbol of an encoded grammar, that is, the element
$\mathrm{inr}(\mathrm{inr}\, b)$ of $\mathbb{N} \oplus (\alpha \oplus \mathrm{Bool})$.

Formalized by `Cslib.Decidability.Grammar.uBit`, a definition declared in [CSLibExt/Computability/Decidability/PCPUniversality.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUniversality.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/universality-problem-for-context-free-grammars/index.html#u-bit).

## List of all letters

For a finite alphabet $\alpha$, the list of all letters of $\alpha$,
each appearing exactly once, in some fixed but unspecified order.

Formalized by `Cslib.Decidability.Grammar.allLetters`, a definition declared in [CSLibExt/Computability/Decidability/PCPUniversality.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUniversality.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/universality-problem-for-context-free-grammars/index.html#all-letters).

## The letters other than a given letter

For a letter $a$ of a finite alphabet with decidable
equality, the list of all letters $b$ of the alphabet with $b \ne a$, in the order of a fixed
enumeration of the alphabet.

Formalized by `Cslib.Decidability.Grammar.others`, a definition declared in [CSLibExt/Computability/Decidability/PCPUniversality.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUniversality.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/universality-problem-for-context-free-grammars/index.html#others).

## Domino-independent productions of the universality grammar

For a finite alphabet
$\alpha$ and $k \in \mathbb{N}$, this is a list of productions whose nonterminals $N_0, N_1, \dots$
are encoded as natural numbers and whose terminals are the letters $a \in \alpha$ and the two bits
$\mathbf{t}$ (true) and $\mathbf{f}$ (false). Writing $c(i) = \mathbf{t}\,\mathbf{f}^i$ for the
unary code of an index $i$, the list consists of the productions $N_3 \to \varepsilon$,
$N_5 \to \varepsilon$, $N_6 \to \varepsilon$, $N_7 \to \varepsilon$; $N_5 \to \mathbf{t}\,N_5$,
$N_5 \to \mathbf{f}\,N_5$, $N_6 \to \mathbf{t}\,N_6$, $N_6 \to \mathbf{f}\,N_6$;
$N_0 \to N_3$, $N_0 \to N_3\,\mathbf{f}\,N_5$, $N_0 \to N_6\,c(k)\,N_6$, $N_0 \to N_1$,
$N_0 \to N_2$; for each letter $a \in \alpha$, the productions $N_3 \to a\,N_3$,
$N_4 \to a\,N_3$, $N_6 \to a\,N_6$, $N_0 \to N_6\,\mathbf{t}\,a\,N_6$ and
$N_0 \to N_6\,\mathbf{f}\,a\,N_6$; and for each $i < k$, the production $N_7 \to c(i)\,N_7$.

The nonterminal $N_0$ is the start symbol. The intended languages are: for $N_3$ the words of
letters, for $N_4$ the nonempty words of letters, for $N_5$ the words of bits, for $N_6$ all
words, and for $N_7$ the concatenated codes of indices below $k$. The start productions (those
with left side $N_0$) generate the malformed words and the two mismatch nonterminals $N_1$ and
$N_2$.

Formalized by `Cslib.Decidability.Grammar.baseRules`, a definition declared in [CSLibExt/Computability/Decidability/PCPUniversality.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUniversality.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/universality-problem-for-context-free-grammars/index.html#base-rules).

## The mismatch productions

**The mismatch productions** of a nonterminal $A$ for one side of a list $P$ of dominoes over a
finite alphabet. Let $s$ be a map from dominoes to words (in use, the top or the bottom). For each
index $i < |P|$ write $w = s(d_i)$ for the $i$-th domino $d_i$ of $P$ and $\mathrm{code}(i)$ for
the unary code of $i$ as bits. With letters and bits as terminals and $N_3$, $N_4$, $N_7$ the
nonterminals $3$, $4$, $7$ (meant to generate words of letters, nonempty words of letters and
codes of indices), the productions are $A \to w\,A\,\mathrm{code}(i)$ and
$A \to w\,N_4\,\mathrm{code}(i)$, which peel $w$ off, and, for each proper prefix $u$ of $w$,
$A \to u\,N_7\,\mathrm{code}(i)$ and $A \to u\,a\,N_3\,N_7\,\mathrm{code}(i)$ for every letter $a$
other than the letter of $w$ following $u$, which stop matching.

Formalized by `Cslib.Decidability.Grammar.mismatchRules`, a definition declared in [CSLibExt/Computability/Decidability/PCPUniversality.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUniversality.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/universality-problem-for-context-free-grammars/index.html#mismatch-rules).

## The universality grammar

For a finite alphabet $\alpha$ with decidable equality and a list
$P$ of dominoes over $\alpha$, the encoded context-free grammar over $\alpha \oplus \mathrm{Bool}$
with start nonterminal $0$ whose productions are the base productions for $k = |P|$, followed by
the mismatch productions of the top words of $P$ with nonterminal $1$, followed by the mismatch
productions of the bottom words of $P$ with nonterminal $2$.

Its language is the union of the complements of the top and bottom list languages of $P$.

Formalized by `Cslib.Decidability.Grammar.univGrammar`, a definition declared in [CSLibExt/Computability/Decidability/PCPUniversality.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUniversality.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/universality-problem-for-context-free-grammars/index.html#univ-grammar).

## Words of letters

For an alphabet $\alpha$, the language of words of letters is the set of
all words over $\alpha \oplus \mathrm{Bool}$ whose symbols all lie in $\alpha$, that is, the words
over $\alpha$ (including the empty word) viewed as words over $\alpha \oplus \mathrm{Bool}$.

Formalized by `Cslib.Decidability.Grammar.lettersLang`, a definition declared in [CSLibExt/Computability/Decidability/PCPUniversality.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUniversality.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/universality-problem-for-context-free-grammars/index.html#letters-lang).

## Nonempty words of letters

For an alphabet $\alpha$, the language of nonempty words of
letters is the set of all nonempty words over $\alpha \oplus \mathrm{Bool}$ whose symbols all lie
in $\alpha$, that is, the nonempty words over $\alpha$ viewed as words over
$\alpha \oplus \mathrm{Bool}$.

Formalized by `Cslib.Decidability.Grammar.letters1Lang`, a definition declared in [CSLibExt/Computability/Decidability/PCPUniversality.lean, line 258](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUniversality.lean#L258). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/universality-problem-for-context-free-grammars/index.html#letters1-lang).

## Words of bits

For an alphabet $\alpha$, the language over the disjoint union of $\alpha$
and the bits $\{\mathbf{t}, \mathbf{f}\}$ consisting of the words in which every symbol is a bit,
including the empty word.

Formalized by `Cslib.Decidability.Grammar.bitsLang`, a definition declared in [CSLibExt/Computability/Decidability/PCPUniversality.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUniversality.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/universality-problem-for-context-free-grammars/index.html#bits-lang).

## Codes of index sequences below $k$

For an alphabet $\alpha$ and $k \in \mathbb{N}$, the
language over the disjoint union of $\alpha$ and the bits $\{\mathbf{t}, \mathbf{f}\}$ consisting of
the bit words $c(j_1) \cdots c(j_n)$ with $n \ge 0$ and $j_1, \dots, j_n < k$, where
$c(j) = \mathbf{t}\,\mathbf{f}^j$ is the unary code of $j$. In particular it contains the empty
word.

Formalized by `Cslib.Decidability.Grammar.codesLang`, a definition declared in [CSLibExt/Computability/Decidability/PCPUniversality.lean, line 264](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUniversality.lean#L264). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/universality-problem-for-context-free-grammars/index.html#codes-lang).

## The mismatch language

**The mismatch language** of one side of a list $P$ of dominoes. Let $s$ be a map from dominoes
to words (in use, the top or the bottom), write $w_i = s(d_i)$ for the $i$-th domino $d_i$ of $P$
and $\mathrm{code}(i)$ for the unary code of $i$ as bits. The language, over letters and bits,
consists of the words $x\,\mathrm{code}(i_n) \cdots \mathrm{code}(i_1)$ where $x$ is a word of
letters and $i_1, \dots, i_n$ with $n \ge 1$ are indices below $|P|$ such that
$x \ne w_{i_1} \cdots w_{i_n}$.

Formalized by `Cslib.Decidability.Grammar.mismatchLang`, a definition declared in [CSLibExt/Computability/Decidability/PCPUniversality.lean, line 268](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUniversality.lean#L268). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/universality-problem-for-context-free-grammars/index.html#mismatch-lang).

## Malformed words

Consider words over $\alpha \oplus \mathrm{Bool}$, whose symbols are
letters from $\alpha$ and bits, and read the bit $\mathrm{true}$ as the separator $|$ and the bit
$\mathrm{false}$ as $1$. For $k \in \mathbb{N}$, a word is malformed with bound $k$ when at least
one of the following holds: it consists of letters only (possibly none); it is a word of letters
followed by a nonempty word of bits whose first bit is $1$; some bit is immediately followed by a
letter; or it contains the block $|\,1^k$ (the bit $|$ followed by $k$ bits $1$) as a contiguous
factor.

Formalized by `Cslib.Decidability.Grammar.malformedLang`, a definition declared in [CSLibExt/Computability/Decidability/PCPUniversality.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUniversality.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/universality-problem-for-context-free-grammars/index.html#malformed-lang).

## Intended languages of the nonterminals of the universality grammar

For a list $P$ of
dominoes over $\alpha$, the assignment of a language over $\alpha \oplus \mathrm{Bool}$ to each
natural number that sends $0$ to the union of the malformed language for $k = |P|$ and the
mismatch languages of the top words and of the bottom words of $P$; $1$ to the mismatch language
of the top words of $P$; $2$ to the mismatch language of the bottom words of $P$; $3$ to the words
of letters; $4$ to the nonempty words of letters; $5$ to the words of bits; $6$ to the set of all
words; $7$ to the codes of index sequences with all indices below $|P|$; and every other number
to the empty language.

Formalized by `Cslib.Decidability.Grammar.univVal`, a definition declared in [CSLibExt/Computability/Decidability/PCPUniversality.lean, line 281](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUniversality.lean#L281). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/universality-problem-for-context-free-grammars/index.html#univ-val).

## Evaluating a form with one nonterminal

Let $V$ assign a language over $T$ to each
nonterminal. For terminal words $u$ and $v$, a nonterminal $A$ and a word $w$, the word $w$ lies
in the language that $V$ assigns to the sentential form $u\,A\,v$ if and only if $w = u z v$ for
some $z \in V(A)$.

Formalized by `Cslib.Decidability.Grammar.mem_evalForm_one`, a theorem declared in [CSLibExt/Computability/Decidability/PCPUniversality.lean, line 315](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUniversality.lean#L315). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/universality-problem-for-context-free-grammars/index.html#mem-eval-form-one).

## Evaluating a form with two nonterminals

Let $V$ assign a language over $T$ to each
nonterminal. For terminal words $u$, $v$ and $x$, nonterminals $A$ and $B$ and a word $w$, the
word $w$ lies in the language that $V$ assigns to the sentential form $u\,A\,v\,B\,x$ if and
only if $w = u z_1 v z_2 x$ for some $z_1 \in V(A)$ and $z_2 \in V(B)$.

Formalized by `Cslib.Decidability.Grammar.mem_evalForm_two`, a theorem declared in [CSLibExt/Computability/Decidability/PCPUniversality.lean, line 327](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUniversality.lean#L327). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/universality-problem-for-context-free-grammars/index.html#mem-eval-form-two).

## The intended languages form a valuation of the universality grammar

Let $\alpha$ be a
finite alphabet with decidable equality and let $P$ be a list of dominoes over $\alpha$. The
assignment of intended languages to the nonterminals of the universality grammar of $P$ is a
valuation of that grammar: for every production $A \to \gamma$, the language that $\gamma$ denotes
under the assignment is contained in the language assigned to $A$.

Formalized by `Cslib.Decidability.Grammar.isValuation_univVal`, a theorem declared in [CSLibExt/Computability/Decidability/PCPUniversality.lean, line 525](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUniversality.lean#L525). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/universality-problem-for-context-free-grammars/index.html#is-valuation-univ-val).

## A word that does not start with $w$ leaves $w$ at some position

Let $w$ and $x$ be words over an alphabet $\alpha$ such that $w$ is not a prefix of $x$. Then
there is a position $m < |w|$ with the following property: writing $w = u\,c\,r$ with $|u| = m$
and $c \in \alpha$, either $x = u$, or $x = u\,a\,y$ for some letter $a \ne c$ and some word $y$.

Formalized by `Cslib.Decidability.Grammar.exists_mismatch_of_not_prefix`, a theorem declared in [CSLibExt/Computability/Decidability/PCPUniversality.lean, line 540](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUniversality.lean#L540). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/universality-problem-for-context-free-grammars/index.html#exists-mismatch-of-not-prefix).

## Membership in the mismatch productions

Let $P$ be a list of dominoes over a finite
alphabet with decidable equality, $A$ a nonterminal, $s$ a map from dominoes to words (in use, the
top or the bottom), $i < |P|$ an index, $w = s(d_i)$ for the $i$-th domino $d_i$ of $P$, and
$\mathrm{code}(i)$ the unary code of $i$ as bits. Write letters and bits as terminals and $N_3$,
$N_4$, $N_7$ for the nonterminals $3$, $4$ and $7$. Each of the following encoded productions
belongs to the mismatch productions of $A$ for $s$ and $P$: $A \to w\,A\,\mathrm{code}(i)$;
$A \to w\,N_4\,\mathrm{code}(i)$; for each $m < |w|$, with $u$ the prefix of $w$ of length $m$,
$A \to u\,N_7\,\mathrm{code}(i)$; and, for each such $m$ and each letter $a$ different from the
letter of $w$ following $u$, $A \to u\,a\,N_3\,N_7\,\mathrm{code}(i)$.

Formalized by `Cslib.Decidability.Grammar.mem_mismatchRules`, a theorem declared in [CSLibExt/Computability/Decidability/PCPUniversality.lean, line 654](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUniversality.lean#L654). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/universality-problem-for-context-free-grammars/index.html#mem-mismatch-rules).

## Every mismatched word is derivable from the mismatch nonterminal

Let $P$ be a list of
dominoes over a finite alphabet, $s$ a map from dominoes to words (in use, the top or the bottom),
$w_i = s(d_i)$ for the $i$-th domino $d_i$ of $P$, and $\mathrm{code}(i)$ the unary code of $i$ as
bits. Let $A$ be a nonterminal such that every mismatch production of $A$ for $s$ and $P$ is a
production of the universality grammar of $P$. Then for every nonempty sequence
$i_1, \dots, i_n$ of indices below $|P|$ and every word $x$ of letters with
$x \ne w_{i_1} \cdots w_{i_n}$, the word $x\,\mathrm{code}(i_n) \cdots \mathrm{code}(i_1)$ is
derivable from $A$ in the universality grammar of $P$.

Formalized by `Cslib.Decidability.Grammar.mismatch_mem`, a theorem declared in [CSLibExt/Computability/Decidability/PCPUniversality.lean, line 673](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUniversality.lean#L673). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/universality-problem-for-context-free-grammars/index.html#mismatch-mem).

## The language of the universality grammar

Let $\alpha$ be a finite alphabet with decidable
equality, let $P$ be a list of dominoes over $\alpha$ of length $m$, and for $i < m$ let $t_i$ and
$b_i$ be the top and bottom words of the domino of $P$ at position $i$, counting from $0$. Read the
bit $\mathrm{true}$ as the separator $|$ and the bit $\mathrm{false}$ as $1$, and let $c(i)$ be the
unary code of $i$: the bit $|$ followed by $i$ bits $1$. The language of the universality grammar
of $P$ equals the intended language of its start nonterminal $0$: a word over
$\alpha \oplus \mathrm{Bool}$ belongs to it exactly when at least one of the following holds: it
consists of letters from $\alpha$ only (possibly none); it is a word of letters followed by a
nonempty word of bits whose first bit is $1$; some bit is immediately followed by a letter; it
contains $c(m)$ as a contiguous factor; or it equals $x\, c(i_n) \cdots c(i_1)$ for a word $x$
over $\alpha$ and indices $i_1, \dots, i_n < m$ with $n \ge 1$ such that
$x \ne t_{i_1} \cdots t_{i_n}$ or $x \ne b_{i_1} \cdots b_{i_n}$.

Formalized by `Cslib.Decidability.Grammar.language_univGrammar`, a theorem declared in [CSLibExt/Computability/Decidability/PCPUniversality.lean, line 765](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUniversality.lean#L765). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/universality-problem-for-context-free-grammars/index.html#language-univ-grammar).

## No right symbol directly precedes a left symbol in a left-then-right word

Let $\alpha$
and $\beta$ be types and consider words over the disjoint union $\alpha \sqcup \beta$. For all
words $u, v$ over $\alpha \sqcup \beta$, all $b \in \beta$ and $a \in \alpha$, all words $X$ over
$\alpha$ and all words $Y$ over $\beta$, we have $u\,b\,a\,v \ne X\,Y$: a word over $\alpha$
followed by a word over $\beta$ never has a symbol of $\beta$ immediately followed by a symbol of
$\alpha$.

Formalized by `Cslib.Decidability.Grammar.append_inr_inl_ne`, a theorem declared in [CSLibExt/Computability/Decidability/PCPUniversality.lean, line 776](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUniversality.lean#L776). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/universality-problem-for-context-free-grammars/index.html#append-inr-inl-ne).

## A bit inside a word of letters followed by bits starts a suffix of the bits

Let $\alpha$
and $\beta$ be types, call the elements of $\alpha$ letters and those of $\beta$ bits, and regard
words over $\alpha$ and over $\beta$ as words over the disjoint union $\alpha \oplus \beta$. If
$u\,b\,z = X\,Y$ for words $u, z$ over $\alpha \oplus \beta$, a bit $b$, a word $X$ of letters and a
word $Y$ of bits, then there are words $Y_1, Y_2$ of bits with $Y = Y_1 Y_2$ and $b\,z = Y_2$.

Formalized by `Cslib.Decidability.Grammar.exists_suffix_of_inr`, a theorem declared in [CSLibExt/Computability/Decidability/PCPUniversality.lean, line 804](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUniversality.lean#L804). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/universality-problem-for-context-free-grammars/index.html#exists-suffix-of-inr).

## Codes of indices below $k$ contain no code of $k$

Let $k \in \mathbb{N}$ and let
$J = (j_1, \dots, j_n)$ be a finite sequence of natural numbers with $j_1, \dots, j_n < k$. Write
$c(i) = \mathbf{t}\,\mathbf{f}^i$ for the unary code of $i$ and $c(J) = c(j_1) \cdots c(j_n)$. Then
there are no bit words $Y$ and $Z$ with $c(J) = Y\,c(k)\,Z$.

Formalized by `Cslib.Decidability.Grammar.bitCodes_ne_append_bitCode`, a theorem declared in [CSLibExt/Computability/Decidability/PCPUniversality.lean, line 843](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUniversality.lean#L843). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/universality-problem-for-context-free-grammars/index.html#bit-codes-ne-append-bit-code).

## Malformed words are in no list language

Let $P$ be a list of dominoes and $s$ a map from
dominoes to words (in use, the top or the bottom). Write the code of an index $i$ as the bits
$|\,1^i$, where $|$ stands for the bit true and $1$ for the bit false. A word over letters and
bits that is malformed with respect to $|P|$ (it has no bits, its first bit is a $1$, a bit is
followed by a letter, or it contains the factor $|\,1^{|P|}$) does not belong to the list
language of $s$ for $P$.

Formalized by `Cslib.Decidability.Grammar.not_mem_listLang_of_malformed`, a theorem declared in [CSLibExt/Computability/Decidability/PCPUniversality.lean, line 872](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUniversality.lean#L872). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/universality-problem-for-context-free-grammars/index.html#not-mem-list-lang-of-malformed).

## Mismatched words are not in the list language

Let $P$ be a list of dominoes and $s$ a map
from dominoes to words (in use, the top or the bottom). No word of the mismatch language of $s$
for $P$ belongs to the list language of $s$ for $P$.

Formalized by `Cslib.Decidability.Grammar.not_mem_listLang_of_mismatch`, a theorem declared in [CSLibExt/Computability/Decidability/PCPUniversality.lean, line 900](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUniversality.lean#L900). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/universality-problem-for-context-free-grammars/index.html#not-mem-list-lang-of-mismatch).

## Every word is malformed or well formed

Let $k \in \mathbb{N}$ and let $w$ be a word over
$\alpha \oplus \mathrm{Bool}$. Then $w$ is malformed with bound $k$, or
$w = x\, c(j_1) \cdots c(j_n)$ for a word $x$ over $\alpha$ and a nonempty sequence of indices
$j_1, \dots, j_n < k$, where $c(j)$ is the unary code of $j$: the bit $\mathrm{true}$ followed by
$j$ bits $\mathrm{false}$.

Formalized by `Cslib.Decidability.Grammar.malformed_or_wellFormed`, a theorem declared in [CSLibExt/Computability/Decidability/PCPUniversality.lean, line 933](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUniversality.lean#L933). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/universality-problem-for-context-free-grammars/index.html#malformed-or-well-formed).

## The universality grammar generates every word exactly when PCP has no solution

Let
$\alpha$ be a finite alphabet with decidable equality and let $P$ be a list of dominoes over
$\alpha$. The universality grammar of $P$ generates every word over $\alpha \oplus \mathrm{Bool}$
if and only if the Post correspondence problem $P$ has no solution.

Formalized by `Cslib.Decidability.Grammar.forall_mem_language_univGrammar_iff`, a theorem declared in [CSLibExt/Computability/Decidability/PCPUniversality.lean, line 979](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUniversality.lean#L979). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/universality-problem-for-context-free-grammars/index.html#forall-mem-language-univ-grammar-iff).

## The complement of PCP many-one reduces to universality of context-free grammars

Let
$\alpha$ be a finite alphabet with decidable equality and a primitive recursive encoding. There
is a computable map sending each PCP instance $P$ (a list of dominoes over $\alpha$) to an
encoded context-free grammar $G_P$ over the alphabet $\alpha \oplus \mathrm{Bool}$ (the letters
of $\alpha$ together with two bits) such that $P$ has no PCP solution if and only if $G_P$
generates every word over $\alpha \oplus \mathrm{Bool}$.

Formalized by `Cslib.Decidability.Grammar.manyOneReducible_not_pcp_univ`, a theorem declared in [CSLibExt/Computability/Decidability/PCPUniversality.lean, line 1095](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUniversality.lean#L1095). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/universality-problem-for-context-free-grammars/index.html#many-one-reducible-not-pcp-univ).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Universality problem for context-free grammars](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/universality-problem-for-context-free-grammars/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/undecidable-problems/universality-problem-for-context-free-grammars)
