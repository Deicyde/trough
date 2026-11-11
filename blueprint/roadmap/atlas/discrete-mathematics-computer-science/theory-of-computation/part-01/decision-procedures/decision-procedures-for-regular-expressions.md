---
declaration: section
origin: cited
lean: Cslib.Language.RegexNode, Cslib.Language.EncodedRegex, Cslib.Language.EncodedRegex.node, Cslib.Language.EncodedRegex.regexAt, Cslib.Language.EncodedRegex.toRegex, Cslib.Language.EncodedRegex.regexAt_append, Cslib.Language.EncodedRegex.flattenAux, Cslib.Language.EncodedRegex.flatten
statement: formalized
proof: formalized
---

# Decision procedures for regular expressions

55 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html).

## Regular-expression node

A node of an encoded regular expression over an alphabet
$\alpha$ is one of six kinds: zero, epsilon, a letter $a \in \alpha$, a sum with arguments
$i, j \in \mathbb{N}$, a product (concatenation) with arguments $i, j \in \mathbb{N}$, or a star
with argument $i \in \mathbb{N}$, where the arguments are indices of nodes.

Formalized by `Cslib.Language.RegexNode`, an inductive type declared in [CSLibExt/Computability/Decidability/RegularExpression.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpression.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#regex-node).

## Encoded regular expressions

An encoded regular expression over an alphabet $\alpha$ is a
list of regular-expression nodes, each a constant ($0$, $1$ or a letter) or an operator (sum,
concatenation or star) whose arguments are node indices; the last node is the root. Any list is
allowed: in the semantics, an argument that is not the index of an earlier node reads as $0$,
and the empty list denotes $0$.

Formalized by `Cslib.Language.EncodedRegex`, a structure declared in [CSLibExt/Computability/Decidability/RegularExpression.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpression.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#encoded-regex).

## Node at an index

For an encoded regular expression $e$ and a natural number $k$, the
node of $e$ at index $k$ is the entry at position $k$ (counting from $0$) of its list of
nodes, or the zero node when $k$ is at least the length of the list.

Formalized by `Cslib.Language.EncodedRegex.node`, a definition declared in [CSLibExt/Computability/Decidability/RegularExpression.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpression.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#node).

## Regular expression at a node

For an encoded regular expression $e$ and $k \in \mathbb{N}$,
the regular expression at node $k$ is defined by recursion on $k$ from the node of $e$ at index
$k$ (a zero node when $k$ is past the end): a zero node gives $0$, an epsilon node gives $1$, a
node for a letter $a$ gives $a$, and a sum, product or star node gives the sum, product or star
of the regular expressions at its arguments, where an argument that is not smaller than $k$
reads as $0$.

Formalized by `Cslib.Language.EncodedRegex.regexAt`, a definition declared in [CSLibExt/Computability/Decidability/RegularExpression.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpression.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#regex-at).

## The regular expression denoted by an encoding

An encoded regular expression $e$ with $n$
nodes denotes the regular expression at its node $n - 1$, the last node. For $n = 0$ this is the
expression at node $0$, which lies past the end of the list and is the empty expression $0$.

Formalized by `Cslib.Language.EncodedRegex.toRegex`, a definition declared in [CSLibExt/Computability/Decidability/RegularExpression.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpression.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#to-regex).

## Appending nodes does not change earlier expressions

Let $l$ and $m$ be lists of
regular-expression nodes and let $k$ be smaller than the length of $l$. Then the regular
expression at node $k$ of the encoding with nodes $l$ followed by $m$ equals the regular
expression at node $k$ of the encoding with nodes $l$.

Formalized by `Cslib.Language.EncodedRegex.regexAt_append`, a theorem declared in [CSLibExt/Computability/Decidability/RegularExpression.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpression.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#regex-at-append).

## Postorder encoding after a prefix

For a regular expression $r$ and a list $l$ of nodes,
the nodes of $r$ are appended after $l$ in postorder, by recursion on $r$. For $0$, $1$ and a
letter $a$, append the single node $0$, $1$ or $a$. For a sum $s + t$ (respectively a
concatenation $st$), append the nodes of $s$ after $l$, giving $l_1$, then the nodes of $t$ after
$l_1$, giving $l_2$, then a sum (respectively concatenation) node with arguments $|l_1| - 1$ and
$|l_2| - 1$. For a star $s^*$, append the nodes of $s$ after $l$, giving $l_1$, then a star node
with argument $|l_1| - 1$. The root of $r$ is the last node.

Formalized by `Cslib.Language.EncodedRegex.flattenAux`, a definition declared in [CSLibExt/Computability/Decidability/RegularExpression.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpression.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#flatten-aux).

## Encoding of a regular expression

The encoding of a regular expression $r$ is the list of
nodes obtained by appending the nodes of $r$ in postorder after the empty list, so that the root
of $r$ is the last node.

Formalized by `Cslib.Language.EncodedRegex.flatten`, a definition declared in [CSLibExt/Computability/Decidability/RegularExpression.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpression.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#flatten).

## Every regular expression has an encoding

For every regular expression $r$ over an
alphabet $\alpha$, the encoded regular expression obtained by flattening $r$ (listing the nodes of
its subexpressions in postorder, so that the root of $r$ is the last node) denotes $r$.

Formalized by `Cslib.Language.EncodedRegex.toRegex_flatten`, a theorem declared in [CSLibExt/Computability/Decidability/RegularExpression.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpression.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#to-regex-flatten).

## Flags of the empty language

The flag triple of the empty language is
$(\mathrm{false}, \mathrm{false}, \mathrm{false})$; the three flags of a language say whether it is
nonempty, whether it has a nonempty word, and whether it is infinite. This triple is also read for
an argument of a node that is not an earlier node.

Formalized by `Cslib.Language.EncodedRegex.zeroFlags`, a definition declared in [CSLibExt/Computability/Decidability/RegularExpression.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpression.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#zero-flags).

## Flags of a sum

For triples of booleans $b = (b_1, b_2, b_3)$ and
$c = (c_1, c_2, c_3)$, the flags of the sum are $(b_1 \lor c_1, b_2 \lor c_2, b_3 \lor c_3)$.

If $b$ and $c$ record whether languages $L$ and $M$ are nonempty, contain a nonempty word and
are infinite, then the flags of the sum record the same for their union $L \cup M$.

Formalized by `Cslib.Language.EncodedRegex.plusFlags`, a definition declared in [CSLibExt/Computability/Decidability/RegularExpression.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpression.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#plus-flags).

## Flags of a concatenation

For triples of Booleans $b = (b_1, b_2, b_3)$ and
$c = (c_1, c_2, c_3)$, the flags of the product are
$(b_1 \land c_1,\ (b_2 \land c_1) \lor (b_1 \land c_2),\ (b_3 \land c_1) \lor (b_1 \land c_3))$.

If $b$ and $c$ record whether languages $L$ and $M$ are nonempty, contain a nonempty word,
and are infinite, the result records the same for $LM$: in particular $LM$ is infinite when
one factor is infinite and the other nonempty.

Formalized by `Cslib.Language.EncodedRegex.compFlags`, a definition declared in [CSLibExt/Computability/Decidability/RegularExpression.lean, line 264](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpression.lean#L264). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#comp-flags).

## Flags of a star

Given a triple of Booleans $(b_1, b_2, b_3)$, the flags of its star are
$(\mathrm{true}, b_2, b_2)$. Read as the flags (nonempty, has a nonempty word, infinite) of a
language, a star is always nonempty, and it has a nonempty word, and is infinite, exactly when
the argument has a nonempty word.

Formalized by `Cslib.Language.EncodedRegex.starFlags`, a definition declared in [CSLibExt/Computability/Decidability/RegularExpression.lean, line 268](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpression.lean#L268). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#star-flags).

## Flags of the next node

Given the list $A$ of flag triples of the nodes before it, the
flag triple of a node is $(\mathrm{false}, \mathrm{false}, \mathrm{false})$ for a zero node,
$(\mathrm{true}, \mathrm{false}, \mathrm{false})$ for an epsilon node and
$(\mathrm{true}, \mathrm{true}, \mathrm{false})$ for a letter node. For a sum, product or star
node it is the flags of a sum, product or star applied to the entries of $A$ at its arguments,
where an argument that is not an index of $A$ reads as
$(\mathrm{false}, \mathrm{false}, \mathrm{false})$.

Formalized by `Cslib.Language.EncodedRegex.stepFlags`, a definition declared in [CSLibExt/Computability/Decidability/RegularExpression.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpression.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#step-flags).

## Flags of all nodes

For a list of nodes $n_0, \dots, n_{m-1}$, the flags
$f_0, \dots, f_{m-1}$ are computed in one left-to-right pass: $f_k$ is the step flags of node
$n_k$ computed from the flags $f_0, \dots, f_{k-1}$ of the nodes before it.

Formalized by `Cslib.Language.EncodedRegex.flags`, a definition declared in [CSLibExt/Computability/Decidability/RegularExpression.lean, line 281](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpression.lean#L281). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#flags).

## Flags of a language

A triple of Booleans $(b_1, b_2, b_3)$ describes a language $L$ when
$b_1$ is true exactly when $L$ is nonempty, $b_2$ is true exactly when $L$ contains a nonempty
word, and $b_3$ is true exactly when $L$ is infinite.

Formalized by `Cslib.Language.EncodedRegex.FlagsOK`, a definition declared in [CSLibExt/Computability/Decidability/RegularExpression.lean, line 285](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpression.lean#L285). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#flags-ok).

## Correctness of the flag pass

For a list $l$ of nodes and a natural number $k$, let $f_k$
be the entry at position $k$ of the flags of $l$, or the zero flags
$(\mathrm{false}, \mathrm{false}, \mathrm{false})$ if $k$ is at least the length of $l$. Then
$f_k$ describes the language of the regular expression at node $k$ of the encoding $l$ when $k$
is less than the length of $l$, and describes the empty language otherwise.

Formalized by `Cslib.Language.EncodedRegex.flagsOK_flags`, a theorem declared in [CSLibExt/Computability/Decidability/RegularExpression.lean, line 409](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpression.lean#L409). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#flags-ok-flags).

## Infiniteness test for encoded regular expressions

Let $e$ be an encoded regular
expression with nodes $n_0, \dots, n_{m-1}$, and let $f_0, \dots, f_{m-1}$ be the flags of all
nodes of $e$, the triples of Booleans computed in one left-to-right pass over the nodes. The
infiniteness test of $e$ is the third component of $f_{m-1}$, the flag triple of the last node
(the root); when $e$ has no nodes it is false.

The three flags of a node say whether its language is nonempty, contains a nonempty word and is
infinite, so the test returns true exactly when the language of $e$ is infinite.

Formalized by `Cslib.Language.EncodedRegex.infiniteB`, a definition declared in [CSLibExt/Computability/Decidability/RegularExpression.lean, line 457](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpression.lean#L457). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#infinite-b).

## Productions of a sum node

For natural numbers $k$, $i$ and $j$, the productions of a
sum node $k$ with arguments $i$ and $j$ are the unit production $k \to i$ if $i < k$, followed
by the unit production $k \to j$ if $j < k$ (and nothing else). Nonterminals are node indices.

Formalized by `Cslib.Language.EncodedRegex.plusRules`, a definition declared in [CSLibExt/Computability/Decidability/RegularExpression.lean, line 472](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpression.lean#L472). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#plus-rules).

## Productions of a concatenation node

For natural numbers $k$, $i$ and $j$, the
productions of a concatenation node $k$ with arguments $i$ and $j$ are the single production
$k \to i\,j$ (nonterminal $i$ followed by nonterminal $j$) when $i < k$ and $j < k$, and there
are none otherwise.

Formalized by `Cslib.Language.EncodedRegex.compRules`, a definition declared in [CSLibExt/Computability/Decidability/RegularExpression.lean, line 476](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpression.lean#L476). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#comp-rules).

## Productions of a star node

For natural numbers $k$ and $i$, the productions of a star
node $k$ with argument $i$ are $k \to \varepsilon$, followed by $k \to i\,k$ if $i < k$ (and
nothing else). Nonterminals are node indices.

Formalized by `Cslib.Language.EncodedRegex.starRules`, a definition declared in [CSLibExt/Computability/Decidability/RegularExpression.lean, line 481](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpression.lean#L481). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#star-rules).

## Productions of a node

For a natural number $k$ and a node $n$, the productions of
node $k$ are the following encoded productions, all with left-hand side $k$, where nonterminal
$i$ stands for node $i$: none if $n$ is the zero node; $k \to \varepsilon$ if $n$ is the
empty-word node; $k \to a$ if $n$ is the character $a$; if $n$ is a sum with arguments $i$ and
$j$, the unit production $k \to i$ when $i < k$ and the unit production $k \to j$ when
$j < k$; if $n$ is a product with arguments $i$ and $j$, the production $k \to i\,j$ when
$i < k$ and $j < k$; if $n$ is a star with argument $i$, the production $k \to \varepsilon$
together with $k \to i\,k$ when $i < k$.

Formalized by `Cslib.Language.EncodedRegex.nodeRules`, a definition declared in [CSLibExt/Computability/Decidability/RegularExpression.lean, line 485](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpression.lean#L485). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#node-rules).

## The grammar of an encoded regular expression

For an encoded regular expression $e$ with
$n$ nodes, its grammar is the encoded context-free grammar with start nonterminal $n - 1$
(truncated subtraction, so $0$ when $n = 0$), in which nonterminal $k$ stands for node $k$. Its
productions are, for each node $k < n$: none if node $k$ is $0$; $k \to \varepsilon$ if it is
$\varepsilon$; if it is the letter $a$, the production $k \to a$; if it is the sum of nodes $i$
and $j$, the productions $k \to i$ (when $i < k$) and $k \to j$ (when $j < k$); if it is the
product of nodes $i$ and $j$, the production $k \to i\,j$ (when $i < k$ and $j < k$); and if it
is the star of node $i$, the productions $k \to \varepsilon$ and $k \to i\,k$ (when $i < k$).
There are no other productions.

Formalized by `Cslib.Language.EncodedRegex.toGrammar`, a definition declared in [CSLibExt/Computability/Decidability/RegularExpression.lean, line 495](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpression.lean#L495). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#to-grammar).

## Language of a sentential form

For an encoded regular expression $e$, the language of a
sentential form $X_1 \cdots X_n$ (terminals in $\alpha$, nonterminals in $\mathbb{N}$) is the
product $L_1 \cdots L_n$, where $L_i$ is $\{a\}$, the language of the one-letter word $a$, when
$X_i$ is the terminal $a$, and the language of the regular expression at node $k$ of $e$ when
$X_i$ is the nonterminal $k$. The empty form has language $\{\varepsilon\}$.

Formalized by `Cslib.Language.EncodedRegex.formLang`, a definition declared in [CSLibExt/Computability/Decidability/RegularExpression.lean, line 531](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpression.lean#L531). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#form-lang).

## A production of a node only produces words of its language

Let $e$ be an encoded
regular expression, $k$ a natural number and $x$ one of the productions of node $k$ built from
the node of $e$ at index $k$. If a word $w$ belongs to the language of the right-hand side of
$x$ (the concatenation, over its symbols, of $\{a\}$ for a terminal $a$ and of the language of
the regular expression at node $i$ for a nonterminal $i$), then $w$ belongs to the language of
the regular expression at node $k$.

Formalized by `Cslib.Language.EncodedRegex.mem_matches_of_mem_nodeRules`, a theorem declared in [CSLibExt/Computability/Decidability/RegularExpression.lean, line 546](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpression.lean#L546). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#mem-matches-of-mem-node-rules).

## Soundness of the grammar of a regular expression

Let $e$ be an encoded regular
expression. If a sentential form $u$ of the context-free grammar of $e$ yields a terminal word
$w$, then $w$ belongs to the language of $u$: the concatenation, over the symbols of $u$, of
$\{a\}$ for a terminal $a$ and of the language of the regular expression at node $k$ for a
nonterminal $k$.

Formalized by `Cslib.Language.EncodedRegex.mem_formLang_of_yields`, a theorem declared in [CSLibExt/Computability/Decidability/RegularExpression.lean, line 632](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpression.lean#L632). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#mem-form-lang-of-yields).

## Completeness of the grammar of an encoded regular expression

Let $\alpha$ be an alphabet
with decidable equality, $e$ an encoded regular expression over $\alpha$ and $k$ a natural number.
Every word in the language of the regular expression at node $k$ of $e$ is yielded by the
sentential form consisting of the single nonterminal $k$ in the context-free grammar of $e$.

Formalized by `Cslib.Language.EncodedRegex.yields_of_mem_matches`, a theorem declared in [CSLibExt/Computability/Decidability/RegularExpression.lean, line 644](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpression.lean#L644). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#yields-of-mem-matches).

## The grammar generates the language of the expression

For every encoded regular
expression $e$, the language of the context-free grammar of $e$ (one nonterminal per node, the
root as start symbol) equals the language of the regular expression that $e$ denotes.

Formalized by `Cslib.Language.EncodedRegex.language_toGrammar`, a theorem declared in [CSLibExt/Computability/Decidability/RegularExpression.lean, line 716](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpression.lean#L716). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#language-to-grammar).

## Membership test for regular expressions

For an encoded regular expression $e$ and a
word $w$, the test returns the answer of the membership test for encoded context-free grammars
on the word $w$ and the grammar of $e$, which has one nonterminal per node and the root as
start symbol.

Formalized by `Cslib.Language.EncodedRegex.memB`, a definition declared in [CSLibExt/Computability/Decidability/RegularExpression.lean, line 722](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpression.lean#L722). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#mem-b).

## Emptiness test for regular expressions

For an encoded regular expression $e$, the test
returns the answer of the emptiness test for encoded context-free grammars on the grammar of
$e$, which has one nonterminal per node and the root as start symbol.

Formalized by `Cslib.Language.EncodedRegex.isEmptyB`, a definition declared in [CSLibExt/Computability/Decidability/RegularExpression.lean, line 729](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpression.lean#L729). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#is-empty-b).

## Inclusion test

For an encoded regular expression $e$ and an encoded DFA $D$, the
inclusion test returns the Boolean computed by the CFG ⊆ DFA inclusion test on the grammar of
$e$ and the automaton $D$.

Formalized by `Cslib.Language.EncodedRegex.subsetB`, a definition declared in [CSLibExt/Computability/Decidability/RegularExpression.lean, line 738](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpression.lean#L738). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#subset-b).

## Regex nodes as a sum type

The bijection between the nodes of encoded regular
expressions over $\alpha$ and $1 \oplus 1 \oplus \alpha \oplus (\mathbb{N} \times \mathbb{N}) \oplus
(\mathbb{N} \times \mathbb{N}) \oplus \mathbb{N}$, where $1$ is the one-point type, that sends the
zero node and the empty-word node to the first and second copies of $1$, a character node $a$
to $a$, a sum node with arguments $i, j$ to $(i, j)$ in the first copy of
$\mathbb{N} \times \mathbb{N}$, a product node with arguments $i, j$ to $(i, j)$ in the second,
and a star node with argument $i$ to $i$.

Formalized by `Cslib.Language.EncodedRegex.nodeEquiv`, a definition declared in [CSLibExt/Computability/Decidability/RegularExpression.lean, line 750](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpression.lean#L750). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#node-equiv).

## Encodings are lists of nodes

The map sending an encoded regular expression over $\alpha$
to its list of nodes is a bijection onto the lists of regular-expression nodes over $\alpha$; its
inverse wraps a list of nodes as an encoding.

Formalized by `Cslib.Language.EncodedRegex.equivList`, a definition declared in [CSLibExt/Computability/Decidability/RegularExpression.lean, line 769](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpression.lean#L769). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#equiv-list).

## Membership for regular expressions is decidable

Let $\alpha$ be an alphabet with a
primitive recursive coding by natural numbers. The set of pairs $(e, w)$ of an encoded regular
expression $e$ over $\alpha$ and a word $w$ over $\alpha$ such that $w$ belongs to the language of
the regular expression denoted by $e$ is decidable by a multi-stack machine.

## Sources

- Sipser, Introduction to the Theory of Computation, Theorem 4.3 ($A_{\mathsf{REX}}$).

Formalized by `Cslib.Language.EncodedRegex.tm2Decidable_mem_matches`, a theorem declared in [CSLibExt/Computability/Decidability/RegularExpression.lean, line 882](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpression.lean#L882). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#tm2-decidable-mem-matches).

## Emptiness of regular expressions is decidable

For an alphabet $\alpha$ with a primitive
recursive encoding, the property of an encoded regular expression over $\alpha$ that the
language it denotes is empty (E_REX) is decidable by a multi-stack machine.

Formalized by `Cslib.Language.EncodedRegex.tm2Decidable_matches_eq_zero`, a theorem declared in [CSLibExt/Computability/Decidability/RegularExpression.lean, line 894](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpression.lean#L894). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#tm2-decidable-matches-eq-zero).

## Infiniteness of regular expressions is decidable

For an alphabet $\alpha$ with a
primitive recursive encoding, the property of an encoded regular expression over $\alpha$ that
the language it denotes is infinite is decidable by a multi-stack machine.

Formalized by `Cslib.Language.EncodedRegex.tm2Decidable_matches_infinite`, a theorem declared in [CSLibExt/Computability/Decidability/RegularExpression.lean, line 998](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpression.lean#L998). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#tm2-decidable-matches-infinite).

## Inclusion of a regular language in a DFA language is decidable

Let $\alpha$ be an
alphabet with decidable equality and a primitive recursive coding by natural numbers. The set of
pairs $(e, D)$ of an encoded regular expression $e$ over $\alpha$ and an encoded DFA $D$ over
$\alpha$ such that the language of the regular expression denoted by $e$ is contained in the
language of $D$ is decidable by a multi-stack machine.

Formalized by `Cslib.Language.EncodedRegex.tm2Decidable_matches_le`, a theorem declared in [CSLibExt/Computability/Decidability/RegularExpression.lean, line 1006](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpression.lean#L1006). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#tm2-decidable-matches-le).

## Short distinguishing words

Two regular expressions $r$ and $s$ denote the same language if
and only if every word of length less than $2^{n(r) + n(s)}$, where $n$ denotes the Thompson state
count, is matched by $r$ exactly when it is matched by $s$.

The bound is the number of states of the product of the subset-construction DFAs of the Thompson
automata.

Formalized by `Cslib.Automata.Thompson.matches'_eq_iff_forall_length_lt`, a theorem declared in [CSLibExt/Computability/Decidability/RegularExpressionEquiv.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpressionEquiv.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#matches-eq-iff-forall-length-lt).

## One step of the Thompson state count

Let $c = (c_0, \dots, c_{m-1})$ be a list of
natural numbers, and read $c_i$ as $0$ when $i \ge m$. The Thompson state count of a
regular-expression node from $c$ is $0$ for the node $0$, $1$ for the node $\varepsilon$, $2$ for
a letter, $c_i + c_j$ for a sum node and for a concatenation node with arguments $i$ and $j$, and
$c_i + 1$ for a star node with argument $i$.

When $c$ holds the counts of the nodes before the node, this is the number of states of
Thompson's automaton of its expression; an argument that is not an earlier node counts $0$, as
the expression $0$ does.

Formalized by `Cslib.Language.EncodedRegex.stepStates`, a definition declared in [CSLibExt/Computability/Decidability/RegularExpressionEquiv.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpressionEquiv.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#step-states).

## Thompson state counts of a node list

For a list $l$ of regular-expression nodes, the
list of Thompson state counts of $l$ is computed in one left-to-right pass: starting from the
empty list, each node $n$ of $l$ in turn appends the count of $n$ computed from the list of
counts built so far.

Formalized by `Cslib.Language.EncodedRegex.stateCounts`, a definition declared in [CSLibExt/Computability/Decidability/RegularExpressionEquiv.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpressionEquiv.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#state-counts).

## Thompson state count of an encoding

The number of Thompson states of an encoded regular
expression $e$ is the entry of the state counts of the nodes of $e$ at the last node, the root
(read as $0$ when $e$ has no nodes).

It equals the number of states of Thompson's automaton of the expression that $e$ denotes.

Formalized by `Cslib.Language.EncodedRegex.numThompsonStates`, a definition declared in [CSLibExt/Computability/Decidability/RegularExpressionEquiv.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpressionEquiv.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#num-thompson-states).

## One state count per node

For every list $l$ of nodes of encoded regular expressions, the
list of state counts of $l$ has the same length as $l$.

Formalized by `Cslib.Language.EncodedRegex.length_stateCounts`, a theorem declared in [CSLibExt/Computability/Decidability/RegularExpressionEquiv.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpressionEquiv.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#length-state-counts).

## Appending a node appends its count

For every list $l$ of regular-expression nodes and
every node $n$, let $l'$ be the list $l$ with $n$ appended at the end. Then the list of Thompson
state counts of $l'$ is the list of counts of $l$ followed by one more entry, the count of $n$
computed from the counts of $l$.

Formalized by `Cslib.Language.EncodedRegex.stateCounts_append_singleton`, a theorem declared in [CSLibExt/Computability/Decidability/RegularExpressionEquiv.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpressionEquiv.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#state-counts-append-singleton).

## The pass computes the Thompson state count of every node

For every list $l$ of nodes and
every index $k$, the entry at index $k$ of the state counts of $l$ (read as $0$ past the end of the
list) equals the Thompson state count of the regular expression at node $k$ of the encoding with
nodes $l$ when $k$ is less than the length of $l$, and $0$ otherwise.

Formalized by `Cslib.Language.EncodedRegex.getD_stateCounts`, a theorem declared in [CSLibExt/Computability/Decidability/RegularExpressionEquiv.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpressionEquiv.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#get-d-state-counts).

## The pass counts the states of Thompson's automaton

For every encoded regular expression
$e$, the number of Thompson states of $e$ computed by the pass over its nodes equals the Thompson
state count of the regular expression that $e$ denotes.

This holds even when the expression tree is exponentially larger than the node list.

Formalized by `Cslib.Language.EncodedRegex.numThompsonStates_eq`, a theorem declared in [CSLibExt/Computability/Decidability/RegularExpressionEquiv.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpressionEquiv.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#num-thompson-states-eq).

## Search bound for equivalence

For encoded regular expressions $e_1$ and $e_2$, the search
bound is $2^{m + n}$, where $m$ and $n$ are the numbers of Thompson states of $e_1$ and $e_2$, each
computed by one pass over the nodes of the encoding.

Formalized by `Cslib.Language.EncodedRegex.eqBound`, a definition declared in [CSLibExt/Computability/Decidability/RegularExpressionEquiv.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpressionEquiv.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#eq-bound).

## Short distinguishing words for encoded regular expressions

Let $e_1$ and $e_2$ be encoded
regular expressions over an alphabet $\alpha$, and let $B$ be their search bound for equivalence.
The regular expressions denoted by $e_1$ and $e_2$ match the same language if and only if every
word $w$ over $\alpha$ of length less than $B$ is matched by the expression denoted by $e_1$
exactly when it is matched by the expression denoted by $e_2$.

Formalized by `Cslib.Language.EncodedRegex.matches'_eq_iff_forall_length_lt`, a theorem declared in [CSLibExt/Computability/Decidability/RegularExpressionEquiv.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpressionEquiv.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#matches-eq-iff-forall-length-lt-2).

## Equivalence test

Over a finite alphabet with decidable equality and a fixed enumeration of
its letters, the equivalence test of two encoded regular expressions $e_1$ and $e_2$ returns true
exactly when, for every length $n$ less than the search bound of $e_1$ and $e_2$ and every word $w$
of length $n$, the membership test gives the same answer for $e_1$ on $w$ as for $e_2$ on $w$.

Formalized by `Cslib.Language.EncodedRegex.eqB`, a definition declared in [CSLibExt/Computability/Decidability/RegularExpressionEquiv.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpressionEquiv.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#eq-b).

## The equivalence test is correct

Over a finite alphabet with decidable equality and a fixed
enumeration of its letters, for all encoded regular expressions $e_1$ and $e_2$, the equivalence
test returns true on $e_1$ and $e_2$ if and only if the regular expressions that $e_1$ and $e_2$
denote have the same language.

Formalized by `Cslib.Language.EncodedRegex.eqB_iff`, a theorem declared in [CSLibExt/Computability/Decidability/RegularExpressionEquiv.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpressionEquiv.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#eq-b-iff).

## One step of the Thompson state count is primitive recursive

For an alphabet $\alpha$
with a primitive recursive encoding, the map sending a list $c$ of natural numbers and a
regular-expression node over $\alpha$ to the Thompson state count of the node computed from $c$
is primitive recursive.

Formalized by `Cslib.Language.EncodedRegex.primrec_stepStates`, a theorem declared in [CSLibExt/Computability/Decidability/RegularExpressionEquiv.lean, line 258](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpressionEquiv.lean#L258). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#primrec-step-states).

## The pass of Thompson state counts is primitive recursive

For an alphabet $\alpha$ with a
primitive recursive encoding, the map sending a list of regular-expression nodes over $\alpha$ to
the list of their Thompson state counts, computed in one left-to-right pass, is primitive
recursive.

Formalized by `Cslib.Language.EncodedRegex.primrec_stateCounts`, a theorem declared in [CSLibExt/Computability/Decidability/RegularExpressionEquiv.lean, line 300](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpressionEquiv.lean#L300). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#primrec-state-counts).

## The Thompson state count of an encoding is primitive recursive

For an alphabet $\alpha$
with a primitive recursive encoding, the number of states of Thompson's automaton of an encoded
regular expression over $\alpha$, computed by one pass over its nodes, is a primitive recursive
function of the encoding.

Formalized by `Cslib.Language.EncodedRegex.primrec_numThompsonStates`, a theorem declared in [CSLibExt/Computability/Decidability/RegularExpressionEquiv.lean, line 307](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpressionEquiv.lean#L307). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#primrec-num-thompson-states).

## The equivalence search bound is primitive recursive

For an alphabet $\alpha$ with a
primitive recursive encoding, the search bound $2^{m+n}$ for equivalence of two encoded regular
expressions over $\alpha$, where $m$ and $n$ are the numbers of states of Thompson's automata of
the two expressions, is a primitive recursive function of the pair of encoded expressions.

Formalized by `Cslib.Language.EncodedRegex.primrec_eqBound`, a theorem declared in [CSLibExt/Computability/Decidability/RegularExpressionEquiv.lean, line 313](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpressionEquiv.lean#L313). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#primrec-eq-bound).

## The equivalence test is primitive recursive

Over a primitively encodable finite alphabet
with decidable equality and a fixed enumeration of its letters, the equivalence test, as a function
of two encoded regular expressions, is primitive recursive.

Formalized by `Cslib.Language.EncodedRegex.primrec_eqB`, a theorem declared in [CSLibExt/Computability/Decidability/RegularExpressionEquiv.lean, line 320](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpressionEquiv.lean#L320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#primrec-eq-b).

## EQ_REX is decidable

Let $\alpha$ be a finite alphabet with a primitive recursive
encoding. Then equivalence of encoded regular expressions over $\alpha$ is decidable by a
multi-stack machine: some multi-stack machine decides, for a pair $(e_1, e_2)$ of encoded
regular expressions over $\alpha$, whether the regular expressions that $e_1$ and $e_2$ denote
have the same language.

This is the regular-expression analogue of Sipser, Theorem 4.5 (EQ_DFA). It is proved by
bounded search: the membership decider is run on both expressions for every word shorter than
a bound computed from them, and the answers are compared.

Formalized by `Cslib.Language.EncodedRegex.tm2Decidable_matches_eq`, a theorem declared in [CSLibExt/Computability/Decidability/RegularExpressionEquiv.lean, line 334](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RegularExpressionEquiv.lean#L334). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html#tm2-decidable-matches-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Decision procedures for regular expressions](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-regular-expressions)
