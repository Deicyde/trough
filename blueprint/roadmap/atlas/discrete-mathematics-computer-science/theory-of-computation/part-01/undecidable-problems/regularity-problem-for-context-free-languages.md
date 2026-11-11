---
declaration: section
origin: cited
lean: Cslib.Decidability.Regularity.Letter, Cslib.Decidability.Regularity.sep, Cslib.Decidability.Regularity.tl, Cslib.Decidability.Regularity.bl, Cslib.Decidability.Regularity.zeroOne, Cslib.Decidability.Regularity.regLang, Cslib.Decidability.Regularity.eq_of_map_tl_append_sep, Cslib.Decidability.Regularity.not_isRegular_zeroOne
statement: formalized
proof: formalized
---

# Regularity problem for context-free languages

29 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/regularity-problem-for-context-free-languages/index.html).

## The languages

## Alphabet of the reduction from universality to regularity

For a type $T$, the alphabet
$T \sqcup \{\#, 0, 1\}$ consists of the letters of $T$, a separator $\#$ and two bits $0$ and $1$,
all distinct.

Formalized by `Cslib.Decidability.Regularity.Letter`, an abbreviation declared in [CSLibExt/Computability/Decidability/CFGRegularity.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CFGRegularity.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/regularity-problem-for-context-free-languages/index.html#letter).

## The separator letter

For an alphabet $T$, among the letters of the reduction (the letters
of $T$, a separator and two bits), this is the separator, written $\#$.

Formalized by `Cslib.Decidability.Regularity.sep`, a definition declared in [CSLibExt/Computability/Decidability/CFGRegularity.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CFGRegularity.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/regularity-problem-for-context-free-languages/index.html#sep).

## Alphabet letters in the extended alphabet

For an alphabet $T$, each letter $t \in T$ is
sent to the corresponding letter among the letters of the reduction (the letters of $T$, a
separator and two bits).

Formalized by `Cslib.Decidability.Regularity.tl`, a definition declared in [CSLibExt/Computability/Decidability/CFGRegularity.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CFGRegularity.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/regularity-problem-for-context-free-languages/index.html#tl).

## Bits as letters

Each boolean $b$ (with false read as $0$ and true as $1$) is sent to the
corresponding bit letter of the alphabet consisting of the letters of $T$, a separator $\#$ and
two bits $0$ and $1$.

Formalized by `Cslib.Decidability.Regularity.bl`, a definition declared in [CSLibExt/Computability/Decidability/CFGRegularity.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CFGRegularity.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/regularity-problem-for-context-free-languages/index.html#bl).

## The language $\{0^n 1^n\}$

The language over the two bits $0$ and $1$ (the Booleans
false and true) consisting of the words $0^n 1^n$ for $n \in \mathbb{N}$, that is, $n$ zeros
followed by $n$ ones.

Formalized by `Cslib.Decidability.Regularity.zeroOne`, a definition declared in [CSLibExt/Computability/Decidability/CFGRegularity.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CFGRegularity.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/regularity-problem-for-context-free-languages/index.html#zero-one).

## The target language of the regularity reduction

For a language $L$ over an alphabet
$T$, this is the language over the letters of $T$, a separator $\#$ and the two bits $0, 1$
consisting of the words $u \# v$ with $u \in T^*$ and $v \in \{0,1\}^*$ such that $u \in L$ or
$v = 0^n 1^n$ for some $n \in \mathbb{N}$; that is,
$L \# \{0,1\}^* \cup T^* \# \{0^n 1^n : n \in \mathbb{N}\}$.

Formalized by `Cslib.Decidability.Regularity.regLang`, a definition declared in [CSLibExt/Computability/Decidability/CFGRegularity.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CFGRegularity.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/regularity-problem-for-context-free-languages/index.html#reg-lang).

## Unique decomposition at the separator

Over the alphabet consisting of the letters of
$T$, a separator $\#$ and two bits $0$ and $1$, let $u, u'$ be words over $T$ and $v, v'$ words
over the bits. If $u \# v = u' \# v'$, then $u = u'$ and $v = v'$.

Formalized by `Cslib.Decidability.Regularity.eq_of_map_tl_append_sep`, a theorem declared in [CSLibExt/Computability/Decidability/CFGRegularity.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CFGRegularity.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/regularity-problem-for-context-free-languages/index.html#eq-of-map-tl-append-sep).

## `{0ⁿ1ⁿ}` is not regular

The words `0ⁱ` are pairwise inequivalent for the Nerode
congruence.

Formalized by `Cslib.Decidability.Regularity.not_isRegular_zeroOne`, a theorem declared in [CSLibExt/Computability/Decidability/CFGRegularity.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CFGRegularity.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/regularity-problem-for-context-free-languages/index.html#not-is-regular-zero-one).

## Words over $T$ in the reduction alphabet

This is the language $T^*$ over the alphabet
$T \sqcup \{\#, 0, 1\}$ of the reduction from universality to regularity: the words, including the
empty word, all of whose letters lie in $T$.

Formalized by `Cslib.Decidability.Regularity.letterWords`, a definition declared in [CSLibExt/Computability/Decidability/CFGRegularity.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CFGRegularity.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/regularity-problem-for-context-free-languages/index.html#letter-words).

## Bit words

Over the alphabet consisting of the letters of $T$, a separator $\#$ and two
bits $0$ and $1$, the bit words form the language $\{0, 1\}^*$ of all finite words, including
the empty word, all of whose letters are bits.

Formalized by `Cslib.Decidability.Regularity.bitWords`, a definition declared in [CSLibExt/Computability/Decidability/CFGRegularity.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CFGRegularity.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/regularity-problem-for-context-free-languages/index.html#bit-words).

## One-letter words over $T$

This is the language over the alphabet $T \sqcup \{\#, 0, 1\}$
of the reduction from universality to regularity consisting of the one-letter words $t$ with
$t \in T$.

Formalized by `Cslib.Decidability.Regularity.letterSet`, a definition declared in [CSLibExt/Computability/Decidability/CFGRegularity.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CFGRegularity.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/regularity-problem-for-context-free-languages/index.html#letter-set).

## Single-bit words

Over the alphabet consisting of the letters of $T$, a separator $\#$
and two bits $0$ and $1$, the single-bit words form the language $\{0, 1\}$ whose only words are
the one-letter words $0$ and $1$.

Formalized by `Cslib.Decidability.Regularity.bitSet`, a definition declared in [CSLibExt/Computability/Decidability/CFGRegularity.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CFGRegularity.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/regularity-problem-for-context-free-languages/index.html#bit-set).

## The reduction language of a universal language is regular

Let $T$ be a finite alphabet
and $L$ a language over $T$ that contains every word over $T$. Over the letters of $T$, a
separator $\#$ and two bits $0$ and $1$, the language
$L \# \{0,1\}^* \cup T^* \# \{0^n 1^n : n \ge 0\}$, which here equals $T^* \# \{0,1\}^*$, is
regular.

Formalized by `Cslib.Decidability.Regularity.isRegular_regLang_top`, a theorem declared in [CSLibExt/Computability/Decidability/CFGRegularity.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CFGRegularity.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/regularity-problem-for-context-free-languages/index.html#is-regular-reg-lang-top).

## Non-universality makes the reduction language non-regular

Let $L$ be a language over an
alphabet $T$, let $T \sqcup \{\#, 0, 1\}$ extend $T$ by a separator $\#$ and two bits, and let
$R(L) = L\,\#\,\{0,1\}^* \cup T^*\,\#\,\{0^n1^n : n \in \mathbb{N}\}$ over this alphabet. If some
word $u$ over $T$ is not in $L$, then $R(L)$ is not regular.

The words $v$ over the bits with $u\,\#\,v \in R(L)$ are exactly the words $0^n1^n$.

Formalized by `Cslib.Decidability.Regularity.not_isRegular_regLang`, a theorem declared in [CSLibExt/Computability/Decidability/CFGRegularity.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CFGRegularity.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/regularity-problem-for-context-free-languages/index.html#not-is-regular-reg-lang).

## Regularity of the reduction language characterises universality

Let $T$ be a finite
alphabet and $L$ a language over $T$. Over the letters of $T$, a separator $\#$ and two bits $0$
and $1$, the language $L \# \{0,1\}^* \cup T^* \# \{0^n 1^n : n \ge 0\}$, of the words $u \# v$
with $u$ a word over $T$, $v$ a word over the bits, and $u \in L$ or $v = 0^n 1^n$ for some $n$,
is regular if and only if $L$ contains every word over $T$.

Formalized by `Cslib.Decidability.Regularity.isRegular_regLang_iff`, a theorem declared in [CSLibExt/Computability/Decidability/CFGRegularity.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CFGRegularity.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/regularity-problem-for-context-free-languages/index.html#is-regular-reg-lang-iff).

## Shifting a symbol into the regularity grammar

Let $T$ be a finite alphabet with decidable
equality, and consider the alphabet $T \sqcup \{\#, 0, 1\}$ of the letters of $T$, a separator
$\#$ and two bits $0$ and $1$. A symbol of an encoded grammar over $T$, that is, a nonterminal
$n \in \mathbb{N}$ or a letter $t \in T$, is sent to a symbol of an encoded grammar over
$T \sqcup \{\#, 0, 1\}$: the nonterminal $n$ goes to the nonterminal $n + 4$, and the letter $t$
goes to the letter $t$ of $T \sqcup \{\#, 0, 1\}$.

Formalized by `Cslib.Decidability.Regularity.shiftSym`, a definition declared in [CSLibExt/Computability/Decidability/CFGRegularity.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CFGRegularity.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/regularity-problem-for-context-free-languages/index.html#shift-sym).

## Shifting a production into the regularity grammar

Let $T$ be a finite alphabet with
decidable equality, and consider the alphabet $T \sqcup \{\#, 0, 1\}$ of the letters of $T$, a
separator $\#$ and two bits $0$ and $1$. An encoded production $(n, \alpha)$ over $T$, with
left-hand side the nonterminal $n$ and right-hand side $\alpha$, is sent to the encoded production
$(n + 4, \alpha')$ over $T \sqcup \{\#, 0, 1\}$, where $\alpha'$ is $\alpha$ with each nonterminal
$k$ replaced by the nonterminal $k + 4$ and each letter of $T$ read as the same letter of
$T \sqcup \{\#, 0, 1\}$.

Formalized by `Cslib.Decidability.Regularity.shiftRule`, a definition declared in [CSLibExt/Computability/Decidability/CFGRegularity.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CFGRegularity.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/regularity-problem-for-context-free-languages/index.html#shift-rule).

## The auxiliary productions of the regularity grammar

For a natural number $s$, these are
the following productions over the nonterminals $\mathbb{N}$ and the alphabet consisting of the
letters of the finite alphabet $T$, a separator $\#$ and two bits $0$ and $1$, where $A_n$
denotes nonterminal $n$: $A_0 \to A_{s+4} \# A_1$, $A_0 \to A_2 \# A_3$, $A_1 \to \varepsilon$,
$A_1 \to 0 A_1$, $A_1 \to 1 A_1$, $A_2 \to \varepsilon$, $A_3 \to \varepsilon$,
$A_3 \to 0 A_3 1$, and $A_2 \to t A_2$ for each letter $t$ of $T$.

In the regularity grammar of a grammar $g$, $s$ is the start nonterminal of $g$, and these
productions are added to those of $g$ with every nonterminal $n$ renamed $n + 4$.

Formalized by `Cslib.Decidability.Regularity.fixedRules`, a definition declared in [CSLibExt/Computability/Decidability/CFGRegularity.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CFGRegularity.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/regularity-problem-for-context-free-languages/index.html#fixed-rules).

## Grammar of the reduction from universality to regularity

Let $g$ be an encoded
context-free grammar over a finite alphabet $T$ with start nonterminal $s$, and write $N_k$ for
nonterminal $k \in \mathbb{N}$ and $\varepsilon$ for the empty word. The reduction grammar of $g$
is the encoded grammar over $T \sqcup \{\#, 0, 1\}$ (the letters of $T$, a separator $\#$ and two
bits $0$ and $1$) with start nonterminal $N_0$ and the productions $N_0 \to N_{s+4}\,\#\,N_1$,
$N_0 \to N_2\,\#\,N_3$, $N_1 \to \varepsilon$, $N_1 \to 0\,N_1$, $N_1 \to 1\,N_1$,
$N_2 \to \varepsilon$, $N_2 \to t\,N_2$ for each $t \in T$, $N_3 \to \varepsilon$ and
$N_3 \to 0\,N_3\,1$, together with the production $N_{n+4} \to \alpha'$ for each production
$N_n \to \alpha$ of $g$, where $\alpha'$ is $\alpha$ with each nonterminal $N_k$ replaced by
$N_{k+4}$ and each letter of $T$ kept.

Its language is $L(g)\,\#\,\{0,1\}^* \cup T^*\,\#\,\{0^n1^n : n \in \mathbb{N}\}$, where $L(g)$
is the language of $g$.

Formalized by `Cslib.Decidability.Regularity.regGrammar`, a definition declared in [CSLibExt/Computability/Decidability/CFGRegularity.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CFGRegularity.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/regularity-problem-for-context-free-languages/index.html#reg-grammar).

## Languages assigned to the nonterminals of the regularity grammar

Let $g$ be an encoded
context-free grammar over a finite alphabet $T$ with decidable equality, let $L(g)$ be its
language and $L_g(n)$ the language $g$ generates from nonterminal $n$. Over the alphabet
$T \sqcup \{\#, 0, 1\}$ (the letters of $T$, a separator $\#$ and two bits $0$ and $1$), write
$\bar u$ for a word $u$ over $T$ read in this alphabet. This assigns to each $m \in \mathbb{N}$
the language $V(m)$ over $T \sqcup \{\#, 0, 1\}$ given by
$V(0) = L(g)\,\#\,\{0,1\}^* \cup T^*\,\#\,\{0^k1^k : k \in \mathbb{N}\}$, $V(1) = \{0,1\}^*$,
$V(2) = T^*$, $V(3) = \{0^k1^k : k \in \mathbb{N}\}$ and $V(n + 4) = \{\bar u : u \in L_g(n)\}$.

These are the intended languages of the nonterminals of the regularity grammar of $g$.

Formalized by `Cslib.Decidability.Regularity.regVal`, a definition declared in [CSLibExt/Computability/Decidability/CFGRegularity.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CFGRegularity.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/regularity-problem-for-context-free-languages/index.html#reg-val).

## Shifted right-hand sides denote images of words of $g$

Let $g$ be an encoded context-free
grammar over $T$, let $L_g(n)$ be the language $g$ generates from nonterminal $n$ and $L(g)$ its
language. For a word $u$ over $T$ write $\bar u$ for the same word over $T \sqcup \{\#, 0, 1\}$.
Let $V$ assign to each $m \in \mathbb{N}$ the language $V(m)$ over $T \sqcup \{\#, 0, 1\}$ given by
$V(0) = L(g)\,\#\,\{0,1\}^* \cup T^*\,\#\,\{0^k1^k : k \in \mathbb{N}\}$, $V(1) = \{0,1\}^*$,
$V(2) = T^*$, $V(3) = \{0^k1^k : k \in \mathbb{N}\}$ and $V(n + 4) = \{\bar u : u \in L_g(n)\}$.
Let $\alpha$ be a right-hand side over nonterminals in $\mathbb{N}$ and terminals in $T$, and let
$\alpha'$ be $\alpha$ with each nonterminal $n$ replaced by $n + 4$ and each terminal read in
$T \sqcup \{\#, 0, 1\}$. If $w$ lies in the language that $\alpha'$ denotes when each nonterminal
$m$ is read as $V(m)$, then $w = \bar u$ for some $u$ in the language that $\alpha$ denotes when
each nonterminal $n$ is read as $L_g(n)$.

Formalized by `Cslib.Decidability.Regularity.mem_evalForm_shift`, a theorem declared in [CSLibExt/Computability/Decidability/CFGRegularity.lean, line 269](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CFGRegularity.lean#L269). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/regularity-problem-for-context-free-languages/index.html#mem-eval-form-shift).

## Every production of the regularity grammar is sound for its intended languages

Let $g$
be an encoded context-free grammar over a finite alphabet $T$ with decidable equality, and let
$G$ be the regularity grammar of $g$, over the letters of $T$, a separator $\#$ and two bits $0$
and $1$; words over $T$ are read as words over this alphabet. Assign to the nonterminals of $G$
the languages $V(0) = L(g) \# \{0,1\}^* \cup T^* \# \{0^n 1^n : n \ge 0\}$, where $L(g)$ is the
language of $g$, $V(1) = \{0,1\}^*$, $V(2) = T^*$, $V(3) = \{0^n 1^n : n \ge 0\}$, and for each
$n$, $V(n + 4)$ the set of words that $g$ generates from its nonterminal $n$. Then $V$ is a
valuation of $G$: for every production $A \to \alpha$ of $G$, the language obtained from $\alpha$
by replacing each nonterminal $B$ by $V(B)$ and each letter $a$ by $\{a\}$, and concatenating, is
contained in $V(A)$.

Formalized by `Cslib.Decidability.Regularity.isValuation_regVal`, a theorem declared in [CSLibExt/Computability/Decidability/CFGRegularity.lean, line 288](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CFGRegularity.lean#L288). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/regularity-problem-for-context-free-languages/index.html#is-valuation-reg-val).

## Productions of the regularity grammar preserve generated languages

Let $g$ be an
encoded context-free grammar over a finite alphabet $T$ with decidable equality, let $G$ be the
regularity grammar of $g$, over the letters of $T$, a separator $\#$ and two bits $0$ and $1$,
and for a nonterminal $B$ let $L_G(B)$ be the language that the grammar denoted by $G$ generates
from $B$. If $(A, \alpha)$ is an encoded production of $G$ and $w$ is a word in the language that
the decoded right-hand side $\alpha$ denotes when each nonterminal $B$ is read as $L_G(B)$, each
letter $a$ as $\{a\}$, and these languages are concatenated in order, then $w \in L_G(A)$.

Formalized by `Cslib.Decidability.Regularity.mem_languageFrom_of_mem_rules`, a theorem declared in [CSLibExt/Computability/Decidability/CFGRegularity.lean, line 361](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CFGRegularity.lean#L361). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/regularity-problem-for-context-free-languages/index.html#mem-language-from-of-mem-rules).

## Shifted right-hand sides generate the images of words

Let $g$ be an encoded context-free
grammar over a finite alphabet $T$, let $G$ be the grammar over $T \sqcup \{\#, 0, 1\}$ that the
reduction from universality to regularity builds from $g$, and let $L_G(m)$ be the language $G$
generates from nonterminal $m$. For a word $u$ over $T$ write $\bar u$ for the same word over
$T \sqcup \{\#, 0, 1\}$. Let $W$ assign to each $n \in \mathbb{N}$ a language $W(n)$ over $T$ with
$\bar u \in L_G(n + 4)$ for every $u \in W(n)$. Let $\alpha$ be a right-hand side over nonterminals
in $\mathbb{N}$ and terminals in $T$, and let $\alpha'$ be $\alpha$ with each nonterminal $n$
replaced by $n + 4$ and each terminal read in $T \sqcup \{\#, 0, 1\}$. If $u$ lies in the language
that $\alpha$ denotes when each nonterminal $n$ is read as $W(n)$, then $\bar u$ lies in the
language that $\alpha'$ denotes when each nonterminal $m$ is read as $L_G(m)$.

Formalized by `Cslib.Decidability.Regularity.mem_evalForm_shift_of`, a theorem declared in [CSLibExt/Computability/Decidability/CFGRegularity.lean, line 410](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CFGRegularity.lean#L410). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/regularity-problem-for-context-free-languages/index.html#mem-eval-form-shift-of).

## Shifted derivations in the regularity grammar

Let $g$ be an encoded context-free grammar
over a finite alphabet $T$, and let $n$ be a nonterminal of $g$. If $g$ derives a word $u$ over
$T$ from $n$, then the regularity grammar of $g$ derives from its nonterminal $n + 4$ the word $u$
read over the extended alphabet, each letter $t$ of $T$ replaced by the corresponding letter.

Formalized by `Cslib.Decidability.Regularity.shift_mem`, a theorem declared in [CSLibExt/Computability/Decidability/CFGRegularity.lean, line 428](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CFGRegularity.lean#L428). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/regularity-problem-for-context-free-languages/index.html#shift-mem).

## The language of the regularity grammar

Let $g$ be an encoded context-free grammar over a
finite alphabet $T$ with decidable equality, with language $L(g)$. Over the letters of $T$, a
separator $\#$ and two bits $0$ and $1$, the regularity grammar of $g$ generates exactly
$L(g) \# \{0,1\}^* \cup T^* \# \{0^n 1^n : n \ge 0\}$, the set of words $u \# v$ with $u$ a word
over $T$, $v$ a word over the bits, and $u \in L(g)$ or $v = 0^n 1^n$ for some $n$.

Formalized by `Cslib.Decidability.Regularity.language_regGrammar`, a theorem declared in [CSLibExt/Computability/Decidability/CFGRegularity.lean, line 447](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CFGRegularity.lean#L447). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/regularity-problem-for-context-free-languages/index.html#language-reg-grammar).

## A grammar is universal iff its regularity grammar generates a regular language

Let $g$
be an encoded context-free grammar over a finite alphabet $T$. Then $g$ generates every word over
$T$ if and only if the regularity grammar of $g$ generates a regular language.

Formalized by `Cslib.Decidability.Regularity.univ_iff_isRegular`, a theorem declared in [CSLibExt/Computability/Decidability/CFGRegularity.lean, line 465](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CFGRegularity.lean#L465). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/regularity-problem-for-context-free-languages/index.html#univ-iff-is-regular).

## Universality many-one reduces to regularity of context-free languages

Let $T$ be a
finite alphabet with decidable equality and a primitive recursive coding, and let
$T \sqcup \{\#, 0, 1\}$ extend $T$ by a separator $\#$ and two bits. There is a computable map $f$
from encoded context-free grammars over $T$ to encoded context-free grammars over
$T \sqcup \{\#, 0, 1\}$ such that a grammar $g$ generates every word over $T$ if and only if the
language generated by $f(g)$ is regular.

Formalized by `Cslib.Decidability.Regularity.manyOneReducible_univ_isRegular`, a theorem declared in [CSLibExt/Computability/Decidability/CFGRegularity.lean, line 497](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CFGRegularity.lean#L497). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/regularity-problem-for-context-free-languages/index.html#many-one-reducible-univ-is-regular).

## Regularity of context-free languages is undecidable

There is a finite alphabet $T$,
with a primitive recursive encoding and decidable equality, such that no multi-stack Turing
machine decides, for an encoded context-free grammar $g$ over $T$, whether the language of $g$
is regular.

Formalized by `Cslib.Decidability.exists_not_tm2Decidable_isRegular`, a theorem declared in [CSLibExt/Computability/Decidability/CFGRegularity.lean, line 512](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/CFGRegularity.lean#L512). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/regularity-problem-for-context-free-languages/index.html#exists-not-tm2-decidable-is-regular).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Regularity problem for context-free languages](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/regularity-problem-for-context-free-languages/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/undecidable-problems/regularity-problem-for-context-free-languages)
