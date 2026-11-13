---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.HuffmanTree, Cslib.Algorithms.Lean.HuffmanTree.weightedLeaves, Cslib.Algorithms.Lean.HuffmanTree.symbols, Cslib.Algorithms.Lean.HuffmanTree.totalWeight, Cslib.Algorithms.Lean.HuffmanTree.weightedPathLength, Cslib.Algorithms.Lean.HuffmanTree.weightedPathLength_fork, Cslib.Algorithms.Lean.HuffmanTree.encodedLength, Cslib.Algorithms.Lean.HuffmanTree.encodedLength_fork
statement: formalized
proof: formalized
---

# Huffman coding

81 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html).

## Huffman tree

A Huffman tree over an alphabet $\alpha$ is either a leaf, which carries a
symbol $a \in \alpha$ and a natural-number weight $w$, or a fork, which joins a left and a right
Huffman tree over $\alpha$.

Formalized by `Cslib.Algorithms.Lean.HuffmanTree`, an inductive type declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#huffman-tree).

## Weighted leaves of a Huffman tree

The list of pairs $(s, w)$, one for each leaf of a
Huffman tree, where $s$ is the symbol and $w$ the weight at that leaf, read from left to
right.

Formalized by `Cslib.Algorithms.Lean.HuffmanTree.weightedLeaves`, a definition declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#weighted-leaves).

## List of leaf symbols of a Huffman tree

The list of the symbols at the leaves of a
Huffman tree, read from left to right, with one entry per leaf.

Formalized by `Cslib.Algorithms.Lean.HuffmanTree.symbols`, a definition declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#symbols).

## Total weight of a Huffman tree

The sum of the weights at all leaves of a Huffman tree,
counted once per leaf.

Formalized by `Cslib.Algorithms.Lean.HuffmanTree.totalWeight`, a definition declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#total-weight).

## Weighted path length

The weighted path length of a Huffman tree is defined recursively:
a single leaf has weighted path length $0$, and the tree with left subtree $L$ and right subtree
$R$ has weighted path length equal to the weighted path length of $L$ plus that of $R$ plus the
total weight of $L$ plus the total weight of $R$.

Equivalently, it is the sum over the leaves of each leaf's weight times its depth, with the root
at depth zero (the standard weighted external path length).

Formalized by `Cslib.Algorithms.Lean.HuffmanTree.weightedPathLength`, a definition declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#weighted-path-length).

## Weighted path length of a merged tree

For Huffman trees $L$ and $R$, the weighted path
length of the tree with left subtree $L$ and right subtree $R$ equals the weighted path length of
$L$ plus the weighted path length of $R$ plus the total weight of $L$ plus the total weight of
$R$.

Formalized by `Cslib.Algorithms.Lean.HuffmanTree.weightedPathLength_fork`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#weighted-path-length-fork).

## Encoded length of a coding tree

The encoded length of a leaf of weight $w$ is $w$ (its
lone symbol receives a one-bit codeword). The encoded length of the tree with left subtree $L$
and right subtree $R$ is $P(L) + P(R) + W(L) + W(R)$, where $P$ is the weighted path length and
$W$ the total weight; this is the weighted path length of that tree.

When the leaf symbols are distinct, the encoded length equals the encoder's emitted cost, the
sum over the weighted leaves of weight times codeword length. When symbols repeat, the encoder
resolves each symbol to its first leaf, so on such trees the encoded length is the structural
path cost rather than the emitted cost.

Formalized by `Cslib.Algorithms.Lean.HuffmanTree.encodedLength`, a definition declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#encoded-length).

## Encoded length of a fork

For any two coding trees $L$ and $R$, the encoded length of the
tree with left subtree $L$ and right subtree $R$ equals its weighted path length.

Formalized by `Cslib.Algorithms.Lean.HuffmanTree.encodedLength_fork`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#encoded-length-fork).

## Root-to-leaf path code

For a Huffman tree $T$ and a symbol $s$, the path code of $s$
in $T$ records the edges on the path from the root of $T$ to the leftmost leaf labelled $s$,
writing false for a left edge and true for a right edge. If $T$ is a single leaf labelled $s$,
the path code is empty; if no leaf of $T$ is labelled $s$, there is no path code.

Formalized by `Cslib.Algorithms.Lean.HuffmanTree.pathCode?`, a definition declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#path-code).

## Codeword lookup in a Huffman tree

Let $T$ be a Huffman tree and $a$ a symbol, and write
$0$ for the bit false and $1$ for the bit true. If $T$ is a single leaf labelled $s$, the codeword
of $a$ is the one-bit word $0$ when $a = s$ and is undefined otherwise. Otherwise the codeword of
$a$ records the edges from the root of $T$ to the leftmost leaf labelled $a$, with $0$ for a left
edge and $1$ for a right edge; it is undefined when no leaf of $T$ is labelled $a$.

Formalized by `Cslib.Algorithms.Lean.HuffmanTree.code?`, a definition declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#code).

## Following a path in a Huffman tree

Let $T$ be a Huffman tree and $w$ a bit string, and
write $0$ for the bit false and $1$ for the bit true. Following $w$ in $T$ starts at the root
and reads the bits of $w$ one at a time, moving to the left subtree on $0$ and to the right
subtree on $1$, until it reaches a leaf; it then returns the label of that leaf together with
the unread bits of $w$. It fails if $w$ runs out before a leaf is reached. In particular, if
$T$ is a single leaf, it returns its label and all of $w$.

Formalized by `Cslib.Algorithms.Lean.HuffmanTree.decodePath?`, a definition declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#decode-path).

## Decoding one codeword

Let $T$ be a Huffman tree and $w$ a bit string, and write $0$ for
the bit false and $1$ for the bit true. If $T$ is a single leaf labelled $s$, decoding one
codeword from $w$ returns $s$ together with the rest of $w$ when $w$ starts with $0$, and fails
otherwise. If $T$ is a fork with left subtree $L$ and right subtree $R$, it fails when $w$ is
empty; when $w$ is a bit $b$ followed by $w'$, it follows $w'$ from the root of $R$ if $b = 1$
and from the root of $L$ if $b = 0$, reading one bit at a time, moving to the left subtree on
$0$ and to the right subtree on $1$, until it reaches a leaf. It then returns the label of that
leaf together with the unread bits, and fails if $w'$ runs out before a leaf is reached.

Formalized by `Cslib.Algorithms.Lean.HuffmanTree.decodeOne?`, a definition declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#decode-one).

## Decoding a bit string

Let $T$ be a Huffman tree. Decoding the empty bit string with $T$
returns the empty sequence of symbols. To decode a nonempty bit string $w$, decode one codeword
from $w$ with $T$, obtaining a symbol $s$ and the unread bits $w'$, and return $s$ followed by
the decoding of $w'$; decoding fails if decoding one codeword from $w$ fails or if decoding
$w'$ fails.

Formalized by `Cslib.Algorithms.Lean.HuffmanTree.decode?`, a definition declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#decode).

## Huffman encoding of a message

Given a coding tree $T$, the empty message encodes to the
empty bit string, and a message $s_1 s_2 \cdots s_n$ encodes to the concatenation, in order, of
the codewords of $s_1, \dots, s_n$ in $T$. If some $s_i$ has no codeword in $T$, the message has
no encoding.

Formalized by `Cslib.Algorithms.Lean.HuffmanTree.encode?`, a definition declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#encode).

## Type of leaf symbols of a Huffman tree

For a Huffman tree $T$ over an alphabet
$\alpha$, the type of leaf symbols of $T$ is the subtype of those $a \in \alpha$ that occur in
the list of leaf symbols of $T$.

Formalized by `Cslib.Algorithms.Lean.HuffmanTree.LeafSymbol`, an abbreviation declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#leaf-symbol).

## Codeword of a leaf symbol

For a Huffman tree $T$ and a symbol $s$ occurring at a
leaf of $T$, the codeword of $s$ is the word that the codeword lookup of $T$ returns for $s$,
or the empty word if the lookup fails.

The lookup never fails on a leaf symbol, so the empty-word default is never used.

Formalized by `Cslib.Algorithms.Lean.HuffmanTree.codeOfLeaf`, a definition declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#code-of-leaf).

## Every leaf symbol has a codeword

Let $T$ be a Huffman tree and $s$ a symbol occurring at
a leaf of $T$. Then the codeword lookup of $s$ in $T$ succeeds.

Formalized by `Cslib.Algorithms.Lean.HuffmanTree.code?_isSome_of_mem_symbols`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#code-is-some-of-mem-symbols).

## Codeword lookup agrees with the leaf code

Let $T$ be a Huffman tree and $s$ a symbol
occurring at a leaf of $T$. Then the codeword lookup of $s$ in $T$ succeeds and returns the
codeword of $s$ as a leaf symbol of $T$.

Formalized by `Cslib.Algorithms.Lean.HuffmanTree.code?_codeOfLeaf`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#code-code-of-leaf).

## Huffman tree codes are prefix-free

For every Huffman tree $T$, the codeword map on the
symbols occurring as leaves of $T$ is prefix-free: if $a$ and $b$ are distinct leaf symbols of
$T$, then the codeword of $a$ is not a prefix of the codeword of $b$.

Formalized by `Cslib.Algorithms.Lean.HuffmanTree.prefixFree`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 305](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L305). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#prefix-free).

## Decoding inverts the leaf code

Let $T$ be a Huffman tree and let $s_1, \dots, s_n$
($n \ge 0$) be symbols occurring at leaves of $T$, with codewords $c(s_1), \dots, c(s_n)$ as
leaf symbols of $T$. Decoding the concatenation $c(s_1) c(s_2) \cdots c(s_n)$ with $T$ succeeds
and returns the sequence $s_1, \dots, s_n$.

Formalized by `Cslib.Algorithms.Lean.HuffmanTree.decode_codeOfLeaf`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 332](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L332). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#decode-code-of-leaf).

## Encoding concatenates leaf codewords

Let $T$ be a Huffman tree and let
$s_1, \dots, s_n$ ($n \ge 0$) be symbols occurring at leaves of $T$, with codewords
$c(s_1), \dots, c(s_n)$ as leaf symbols of $T$. Encoding $s_1, \dots, s_n$ with $T$ succeeds
and returns the concatenation $c(s_1) c(s_2) \cdots c(s_n)$.

Formalized by `Cslib.Algorithms.Lean.HuffmanTree.encode_codeOfLeaf`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 344](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L344). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#encode-code-of-leaf).

## Decoding inverts encoding

Let $T$ be a Huffman tree and let $s_1, \dots, s_n$
($n \ge 0$) be symbols occurring at leaves of $T$. Encoding $s_1, \dots, s_n$ with $T$ and then
decoding the resulting bit string with $T$, failing if the encoding fails, returns
$s_1, \dots, s_n$. In particular, the encoding succeeds.

Formalized by `Cslib.Algorithms.Lean.HuffmanTree.decode_encode_leafSymbols`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 356](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L356). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#decode-encode-leaf-symbols).

## A symbol has a path code exactly when it labels a leaf

For a Huffman tree $T$ over an
alphabet $\alpha$ with decidable equality and a symbol $a \in \alpha$, the root-to-leaf path code
of $a$ in $T$ is undefined exactly when $a$ is not among the leaf symbols of $T$.

Formalized by `Cslib.Algorithms.Lean.HuffmanTree.pathCode?_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 366](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L366). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#path-code-eq-none-iff).

## Weighted path length as a sum over leaves

Let $T$ be a Huffman tree whose leaf symbols
are pairwise distinct. Then the weighted path length of $T$ equals the sum, over the leaves of
$T$ with symbol $s$ and weight $w$, of $w$ times the length of the root-to-leaf path of $s$ in
$T$ (the depth of that leaf, with the root at depth zero).

Formalized by `Cslib.Algorithms.Lean.HuffmanTree.weightedPathLength_eq_sum_pathLengths`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 421](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L421). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#weighted-path-length-eq-sum-path-lengths).

## Encoded length is the total weighted codeword length

Let $T$ be a coding tree whose leaf
symbols are pairwise distinct. For a symbol $s$, let $\ell(s)$ be the length of the codeword of
$s$ in $T$, or $0$ if $s$ has no codeword. Then the encoded length of $T$ equals
$\sum_{(s, w)} w \cdot \ell(s)$, the sum over the weighted leaves $(s, w)$ of $T$.

Without distinct symbols, the encoder resolves a repeated symbol to its first leaf, and the
encoded length remains the structural weighted path cost.

Formalized by `Cslib.Algorithms.Lean.HuffmanTree.encodedLength_eq_sum_codeLengths`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 476](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L476). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#encoded-length-eq-sum-code-lengths).

## Huffman priority

A Huffman priority is a pair $(w, s)$ of natural numbers: a weight $w$
and a serial number $s$.

Priorities are ordered lexicographically, first by weight and then by serial number, so serial
numbers break ties between equal weights deterministically.

Formalized by `Cslib.Algorithms.Lean.HuffmanPriority`, a structure declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 529](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L529). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#huffman-priority).

## Huffman work item

A work item over an alphabet $\alpha$ pairs a Huffman priority, that
is, a natural-number weight and a natural-number serial, with a Huffman tree over $\alpha$.

The serial is used to find the tree again after its priority is extracted from the heap.

Formalized by `Cslib.Algorithms.Lean.HuffmanWorkItem`, a structure declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 547](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L547). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#huffman-work-item).

## Result of a two-minimum extraction

A record consisting of two Huffman priorities, the
first and the second, together with a binary min-heap of Huffman priorities, the rest.

The two-minimum extraction fills it with the two successive minima of a heap and the heap left
after removing them.

Formalized by `Cslib.Algorithms.Lean.HuffmanTwoMin`, a structure declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 555](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L555). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#huffman-two-min).

## Extracting two minima from a Huffman heap

Given a binary min-heap $h$ of Huffman
priorities, extract the minimum of $h$, obtaining a priority $p_1$ and a heap $h_1$, then extract
the minimum of $h_1$, obtaining a priority $p_2$ and a heap $h_2$. The result is the triple
$(p_1, p_2, h_2)$; if either extraction meets an empty heap, there is no result.

Formalized by `Cslib.Algorithms.Lean.extractTwoMin?`, a definition declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 564](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L564). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#extract-two-min).

## Extracting two minima preserves the heap's elements

If extracting two minima from a
binary min-heap $h$ of Huffman priorities succeeds with first priority $p_1$, second priority
$p_2$ and remaining heap $h'$, then the multiset of elements of $h$ equals the multiset of
elements of $h'$ with $p_1$ and $p_2$ added, counted with multiplicity.

Formalized by `Cslib.Algorithms.Lean.extractTwoMin_cons_elements`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 573](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L573). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#extract-two-min-cons-elements).

## Two-minimum extraction is greedy

Order Huffman priorities lexicographically by weight and
then serial number. If extracting two minima from a binary min-heap $h$ of Huffman priorities
succeeds with first priority $p_1$, second priority $p_2$ and remaining heap $h'$, then
$p_1 \le q$ for every element $q$ of $h$, and $p_2 \le q$ for every $q$ that is $p_2$ or an
element of $h'$.

Formalized by `Cslib.Algorithms.Lean.extractTwoMin_greedy`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 595](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L595). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#extract-two-min-greedy).

## Work forest of a table

For a table $T$ whose cells each hold at most one work item, the
work forest of $T$ is the list of the work items held in the cells of $T$, in increasing cell
order; empty cells are skipped.

In the Huffman loop these are the work items still available to merge.

Formalized by `Cslib.Algorithms.Lean.huffmanTableForest`, a definition declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 619](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L619). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#huffman-table-forest).

## Removing a work item by serial

Given a serial number $s$ and a table $t$ of optional
Huffman work items, look up the entry of $t$ at index $s$. If that entry is a work item whose
serial number is $s$, the result is its tree together with the table obtained from $t$ by
emptying the entry at $s$; otherwise (the index is out of bounds, the entry is empty, or it
holds an item with a different serial number) the removal fails.

The table is indexed directly by serial, so this is one indexed lookup and one indexed update
rather than a scan of the work forest.

Formalized by `Cslib.Algorithms.Lean.takeSerial?`, a definition declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 626](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L626). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#take-serial).

## Weighted leaves of a Huffman work forest

The weighted leaves of a list of Huffman work
items are the concatenation, in list order, of the weighted leaves of the items' trees.

Formalized by `Cslib.Algorithms.Lean.huffmanForestLeaves`, a definition declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 638](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L638). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#huffman-forest-leaves).

## Removing a serial removes one work item from the forest

Let $t$ be a table of optional
Huffman work items, and call the list of work items present in a table its work forest. If
removing serial number $s$ from $t$ succeeds and returns a tree $T$ and an updated table $t'$,
then there is a work item $w$ with tree $T$ and serial number $s$ such that $w$ followed by the
work forest of $t'$ is a permutation of the work forest of $t$.

Formalized by `Cslib.Algorithms.Lean.takeSerial?_item`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 668](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L668). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#take-serial-item).

## Removing a serial preserves the table size

Let $t$ be a table of optional Huffman work
items. If removing serial number $s$ from $t$ succeeds and returns a tree together with an
updated table $t'$, then $t'$ has the same size as $t$.

Formalized by `Cslib.Algorithms.Lean.takeSerial?_size`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 691](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L691). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#take-serial-size).

## Removing a serial leaves the other table entries unchanged

Let $t$ be a table of
optional Huffman work items. If removing serial number $s$ from $t$ succeeds and returns a tree
together with an updated table $t'$, then for every index $j \ne s$ the entry of $t'$ at $j$
equals the entry of $t$ at $j$ (both are absent when $j$ is out of bounds).

Formalized by `Cslib.Algorithms.Lean.takeSerial?_getElem?_of_ne`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 709](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L709). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#take-serial-get-elem-of-ne).

## A stored work item can be removed by its serial

Let $t$ be a table of optional Huffman
work items and let $w$ be a work item with serial number $s$. If the entry of $t$ at index $s$
is $w$, then removing serial $s$ from $t$ succeeds and returns the tree of $w$ together with an
updated table.

Formalized by `Cslib.Algorithms.Lean.takeSerial?_isSome_of_stored`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 729](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L729). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#take-serial-is-some-of-stored).

## Numbered leaf work items

Given a starting serial number $s$ and a list of pairs
$(a_0, w_0), \dots, (a_{k-1}, w_{k-1})$ of symbols and natural-number weights, this is the list
of $k$ Huffman work items whose $i$-th entry has priority (weight $w_i$, serial $s + i$) and whose
tree is the leaf with symbol $a_i$ and weight $w_i$.

Formalized by `Cslib.Algorithms.Lean.initialHuffmanForestFrom`, a definition declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 746](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L746). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#initial-huffman-forest-from).

## Initial Huffman forest

For a list of pairs $(a_0, w_0), \dots, (a_{k-1}, w_{k-1})$ of
symbols and natural-number weights, the initial forest is the list of $k$ Huffman work items
whose $i$-th entry has priority (weight $w_i$, serial $i$) and whose tree is the leaf with symbol
$a_i$ and weight $w_i$.

Formalized by `Cslib.Algorithms.Lean.initialHuffmanForest`, a definition declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 754](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L754). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#initial-huffman-forest).

## Initial Huffman table

For a list of $k$ pairs $(a_0, w_0), \dots, (a_{k-1}, w_{k-1})$ of
symbols and natural-number weights, the initial table is the array of length $k$ of optional
Huffman work items whose cell $i$ is present and holds the work item with priority (weight $w_i$,
serial $i$) and tree the leaf with symbol $a_i$ and weight $w_i$; that is, it is the initial
Huffman forest with every entry marked present.

Formalized by `Cslib.Algorithms.Lean.initialHuffmanTable`, a definition declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 759](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L759). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#initial-huffman-table).

## The initial table holds the initial forest

For every list of weighted symbols, the work
forest read off the initial serial-indexed table of the list is exactly the initial leaf forest
of the list, in the same order.

Formalized by `Cslib.Algorithms.Lean.huffmanTableForest_initial`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 764](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L764). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#huffman-table-forest-initial).

## Appending to the table appends to the forest

For every table $T$ whose cells each hold at
most one work item and every work item $x$, the work forest of the table obtained from $T$ by
appending a new last cell holding $x$ is the work forest of $T$ followed by $x$.

Formalized by `Cslib.Algorithms.Lean.huffmanTableForest_push_some`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 769](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L769). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#huffman-table-forest-push-some).

## Heap of a Huffman work forest

The heap of a list of Huffman work items is obtained from
the empty binary min-heap by inserting the priorities of the items one at a time, in list
order.

Formalized by `Cslib.Algorithms.Lean.huffmanHeapOfForest`, a definition declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 776](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L776). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#huffman-heap-of-forest).

## Bounded Huffman merge loop

The loop takes a fuel $n$, a next serial number $s$, a binary
min-heap $H$ of Huffman priorities, ordered lexicographically by weight and then serial number,
and a table $T$ whose cells each hold at most one work item. Taking serial $i$ from a table
succeeds when cell $i$ holds a work item whose priority has serial number $i$, and returns that
item's tree together with the table with cell $i$ emptied. With fuel $0$, the loop extracts the
minimum $p$ of $H$, leaving a heap $H'$, and takes the serial number of $p$ from $T$, obtaining a
tree $t$ and a table $T'$; it returns $t$ if $H'$ is empty and no cell of $T'$ holds a work item,
and fails otherwise. With fuel $n + 1$, it extracts the minimum $p_1 = (w_1, s_1)$ of $H$ and then
the minimum $p_2 = (w_2, s_2)$ of the remaining heap, leaving a heap $H'$; it takes $s_1$ from $T$
and then $s_2$ from the resulting table, obtaining trees $t_1$, $t_2$ and a table $T'$. It then
runs with fuel $n$, next serial number $s + 1$, the heap $H'$ with the priority
$p = (w_1 + w_2, s)$ inserted, and the table $T'$ with a new last cell holding the work item of
priority $p$ whose tree has left subtree $t_1$ and right subtree $t_2$. If any extraction or take
fails, the loop fails.

Formalized by `Cslib.Algorithms.Lean.huffmanLoop`, a definition declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 781](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L781). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#huffman-loop).

## Huffman loop with an accumulated lookup count

The loop takes a fuel $n$, a next serial
number $s$, a binary min-heap $H$ of Huffman priorities, ordered lexicographically by weight and
then serial number, a table $T$ whose cells each hold at most one work item, and a counter $c$.
Taking serial $i$ from a table succeeds when cell $i$ holds a work item whose priority has serial
number $i$, and returns that item's tree together with the table with cell $i$ emptied. With fuel
$0$, the loop extracts the minimum $p$ of $H$, leaving a heap $H'$, and takes the serial number of
$p$ from $T$, obtaining a tree $t$ and a table $T'$; it returns $(t, c + 1)$ if $H'$ is empty and
no cell of $T'$ holds a work item, and fails otherwise. With fuel $n + 1$, it extracts the minimum
$p_1 = (w_1, s_1)$ of $H$ and then the minimum $p_2 = (w_2, s_2)$ of the remaining heap, leaving a
heap $H'$; it takes $s_1$ from $T$ and then $s_2$ from the resulting table, obtaining trees $t_1$,
$t_2$ and a table $T'$. It then runs with fuel $n$, next serial number $s + 1$, the heap $H'$ with
the priority $p = (w_1 + w_2, s)$ inserted, the table $T'$ with a new last cell holding the work
item of priority $p$ whose tree has left subtree $t_1$ and right subtree $t_2$, and counter
$c + 2$. If any extraction or take fails, the loop fails.

The counter thus grows by one for each work item taken from the table. The Huffman loop with
lookup count is the case $c = 0$.

Formalized by `Cslib.Algorithms.Lean.huffmanLoopWithLookupCountAux`, a definition declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 815](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L815). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#huffman-loop-with-lookup-count-aux).

## Huffman loop with lookup count

For a fuel $n$, a next serial number $s$, a binary min-heap
$H$ of Huffman priorities and a table $T$ whose cells each hold at most one work item, the Huffman
loop with lookup count on $(n, s, H, T)$ is the Huffman loop with an accumulated lookup count on
$(n, s, H, T)$ started with counter $0$. It runs the bounded sequence of Huffman merges and counts
indexed table lookups, one for each work item taken from the table: two per merge and one at the
final step. On success it returns the resulting tree together with the count; otherwise it fails.

The count excludes heap operations, table writes (emptying cells and appending merged work items)
and the final check that the table holds no work item.

Formalized by `Cslib.Algorithms.Lean.huffmanLoopWithLookupCount`, a definition declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 849](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L849). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#huffman-loop-with-lookup-count).

## Lookup count of the instrumented Huffman loop

For every fuel $n$, next serial number $s$,
binary min-heap $H$ of Huffman priorities and table $T$ whose cells each hold at most one work
item, the Huffman loop with lookup count on $(n, s, H, T)$ fails exactly when the bounded Huffman
merge loop on $(n, s, H, T)$ fails, and returns $(t, 2n + 1)$ when the merge loop returns the tree
$t$: two indexed table reads for each of the $n$ merges and one for the final step.

Formalized by `Cslib.Algorithms.Lean.huffmanLoopWithLookupCount_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 908](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L908). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#huffman-loop-with-lookup-count-eq).

## Discarding the lookup count recovers the Huffman loop

For every fuel $n$, next serial
number $s$, binary min-heap $H$ of Huffman priorities and table $T$ whose cells each hold at most
one work item, discarding the count from the result of the Huffman loop with lookup count on
$(n, s, H, T)$ gives the result of the bounded Huffman merge loop on $(n, s, H, T)$: the two fail
together, and otherwise they return the same tree.

Formalized by `Cslib.Algorithms.Lean.huffmanLoopWithLookupCount_map_fst`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 916](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L916). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#huffman-loop-with-lookup-count-map-fst).

## Indexed reads of a successful Huffman loop

Let $k$ be a merge budget, $n$ a next serial
number, $h$ a binary min-heap of Huffman priorities and $t$ a serial-indexed table of optional
Huffman work items. If the Huffman loop with budget $k$ on $n$, $h$ and $t$ returns a tree $T$,
then the Huffman loop with lookup counting on the same arguments returns $T$ together with the
count $2k + 1$ of indexed payload-table reads.

Formalized by `Cslib.Algorithms.Lean.huffmanLoop_lookupCount`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 924](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L924). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#huffman-loop-lookup-count).

## Huffman's algorithm

Let $L$ be a list of $n$ pairs $(a_0, w_0), \dots, (a_{n-1}, w_{n-1})$
of symbols and natural-number weights, with decidable equality on symbols. The construction
fails when $L$ is empty or two pairs share a symbol. Otherwise it starts from $n$ leaves, the
leaf for $(a_i, w_i)$ having priority (weight $w_i$, serial $i$), and performs $n - 1$ merges:
each merge removes the two trees whose priorities are least in the lexicographic order on
(weight, serial), and adds the fork with the first removed tree on the left, with priority the
sum of the two weights and the next unused serial $n, n + 1, \dots$. If exactly one tree then
remains, it is returned; otherwise the construction fails.

Ties between equal weights are broken by serial: leaves come before merged trees, leaves in input
order and merged trees in creation order.

Formalized by `Cslib.Algorithms.Lean.huffman`, a definition declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 1023](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L1023). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#huffman).

## Huffman's construction keeps the weighted leaves

Let $L$ be a list of pairs $(a, w)$ of
a symbol $a$ and a natural-number weight $w$, with decidable equality on symbols. If the Huffman
construction on $L$ succeeds with a tree $T$, then the list of weighted leaves of $T$, read left
to right, is a permutation of $L$.

Formalized by `Cslib.Algorithms.Lean.huffman_weightedLeaves_perm`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 1033](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L1033). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#huffman-weighted-leaves-perm).

## Huffman codes are prefix-free

If the Huffman construction succeeds on a list of weighted
symbols and returns a tree $T$, then the code of $T$ on its leaf symbols is prefix-free: for any
two distinct leaf symbols of $T$, neither codeword is a prefix of the other.

Formalized by `Cslib.Algorithms.Lean.huffman_prefixFree`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/Huffman.lean, line 1044](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/Huffman.lean#L1044). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#huffman-prefix-free).

## Huffman weight tree

A Huffman weight tree is a full binary tree whose leaves carry only
real weights: it is either a leaf with a weight $w \in \mathbb{R}$, or a fork joining a left and a
right Huffman weight tree.

Formalized by `Cslib.Algorithms.Lean.HuffmanWeightTree`, an inductive type declared in [CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#huffman-weight-tree).

## Multiset of leaf weights

The leaf weights of a Huffman weight tree form a multiset of
reals that forgets where the leaves sit: a leaf of weight $w$ gives $\{w\}$, and a tree with
subtrees $L$ and $R$ gives the multiset sum of the leaf weights of $L$ and those of $R$.

Formalized by `Cslib.Algorithms.Lean.HuffmanWeightTree.weights`, a definition declared in [CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#weights).

## Total leaf weight of a Huffman weight tree

The total weight of a Huffman weight tree is
the sum of its leaf weights: a leaf of weight $w$ has total weight $w$, and a tree with subtrees
$L$ and $R$ has total weight equal to the total weight of $L$ plus that of $R$.

Formalized by `Cslib.Algorithms.Lean.HuffmanWeightTree.totalWeight`, a definition declared in [CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#total-weight-2).

## Weighted external path length of a Huffman weight tree

For a Huffman weight tree $T$,
write $w(T)$ for its total leaf weight. The weighted external path length $P(T)$ of $T$ is
defined by the merge recurrence: a leaf $T$ has $P(T) = 0$, and a tree $T$ with subtrees $L$
and $R$ has $P(T) = P(L) + P(R) + w(L) + w(R)$.

Formalized by `Cslib.Algorithms.Lean.HuffmanWeightTree.pathCost`, a definition declared in [CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#path-cost).

## Height of a weight tree

The height of a weight tree is the number of edges on a longest
path from the root to a leaf: a leaf has height $0$, and a fork with subtrees $L$ and $R$ has
height $1 + \max(\mathrm{height}(L), \mathrm{height}(R))$.

Formalized by `Cslib.Algorithms.Lean.HuffmanWeightTree.height`, a definition declared in [CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#height).

## Weight at a given depth

For a real number $v$, a weight tree $T$ and a natural number
$d$, the relation "$T$ contains $v$ at depth $d$" is defined inductively: the leaf of weight $v$
contains $v$ at depth $0$, and if $L$ contains $v$ at depth $d$ or $R$ contains $v$ at depth $d$,
then the fork with left subtree $L$ and right subtree $R$ contains $v$ at depth $d + 1$. Thus it
holds exactly when some leaf of $T$ of weight $v$ lies at depth $d$, the root being at depth $0$.

Formalized by `Cslib.Algorithms.Lean.HuffmanWeightTree.ContainsAt`, an inductive type declared in [CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#contains-at).

## Reweighting one leaf occurrence

Suppose a leaf of weight $v$ occurs at depth $d$ in a
Huffman weight tree $T$, and let $r$ be a real number. Then there are a multiset $R$ of reals and
a Huffman weight tree $T'$ such that the multiset of leaf weights of $T$ is $\{v\} + R$, that of
$T'$ is $\{r\} + R$, the total leaf weight of $T'$ is that of $T$ plus $r - v$, the weighted
external path length of $T'$ is that of $T$ plus $d(r - v)$, and $T'$ has the same height as
$T$.

Formalized by `Cslib.Algorithms.Lean.HuffmanWeightTree.ContainsAt.reweight`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#reweight).

## Raising one leaf weight in a bounded-height tree

Let $T$ be a Huffman weight tree whose
height is at most a natural number $B$, and write $W(T)$ for its multiset of leaf weights. Let
$v \le r$ be real numbers and let $S$ be a multiset of reals with $\{r\} + W(T) = \{v\} + S$.
Then there is a Huffman weight tree $T'$ with multiset of leaf weights $S$ and height at most
$B$ whose weighted external path length is at most that of $T$ plus $B(r - v)$.

Formalized by `Cslib.Algorithms.Lean.HuffmanWeightTree.raiseBounded`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#raise-bounded).

## Raising two leaf weights in a bounded-height tree

Let $T$ be a Huffman weight tree whose
height is at most a natural number $B$, and write $W(T)$ for its multiset of leaf weights. Let
$f, s, \ell, n$ be real numbers with $\ell \le n$, $\ell \le f$ and $n \le s$, and let $S$ be a
multiset of reals with $\{f, s\} + W(T) = \{\ell, n\} + S$. Then there is a Huffman weight tree
$T'$ with multiset of leaf weights $S$ whose weighted external path length is at most that of
$T$ plus $B(f - \ell) + B(s - n)$.

Formalized by `Cslib.Algorithms.Lean.HuffmanWeightTree.raisePair`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean, line 291](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean#L291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#raise-pair).

## Contracting a deepest sibling pair

Let $T$ be a weight tree of height $h \ge 1$. Then
there are real numbers $x$ and $y$, a multiset $M$ of real numbers and a real number $c$ such that
the multiset of leaf weights of $T$ is $\{x, y\} + M$, the path cost of $T$ is $c + hx + hy$, and
for every real number $z$ there is a weight tree $T'$ of height at most $h$ whose multiset of leaf
weights is $\{z\} + M$ and whose path cost is $c + (h - 1)z$.

In the proof, $x$ and $y$ are the weights of a deepest pair of sibling leaves of $T$, and $T'$
replaces that pair by a single leaf of weight $z$.

Formalized by `Cslib.Algorithms.Lean.HuffmanWeightTree.exists_cherry_contraction`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean, line 327](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean#L327). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#exists-cherry-contraction).

## Contracting the two least weights

Let $T$ be a weight tree, let $a$ and $b$ be real
numbers and let $M$ be a multiset of real numbers such that the multiset of leaf weights of $T$ is
$\{a, b\} + M$, $a \le b$, and $b \le w$ for every $w \in M$. Then there is a weight tree $T'$
whose multiset of leaf weights is $\{a + b\} + M$ and whose path cost satisfies
$\mathrm{cost}(T') + a + b \le \mathrm{cost}(T)$, where $\mathrm{cost}$ denotes path cost.

The proof is a sibling exchange argument on the structural path cost.

Formalized by `Cslib.Algorithms.Lean.HuffmanWeightTree.contractLeastPair`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean, line 512](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean#L512). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#contract-least-pair).

## Two-minimum merge trace

The relation "$c$ is a two-minimum merge cost of the multiset $W$
of real weights" is defined inductively by two rules. A singleton multiset $\{w\}$ has merge cost
$0$. If $a \le b$, every element of the multiset $R$ is at least $b$, and $c$ is a merge cost of
$\{a + b\} + R$, then $a + b + c$ is a merge cost of $\{a, b\} + R$. Thus a merge cost is the total
cost of repeatedly replacing two smallest weights by their sum until one weight remains, each
merge costing the sum of the two merged weights.

Formalized by `Cslib.Algorithms.Lean.HuffmanWeightTree.MergeTrace`, an inductive type declared in [CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean, line 597](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean#L597). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#merge-trace).

## Two-minimum merge costs lower-bound weighted path length

Let $W$ be a multiset of real
weights and let $c$ be a merge cost of $W$ certified by a two-minimum merge trace. Then every
Huffman weight tree whose multiset of leaf weights is $W$ has weighted external path length at
least $c$.

Formalized by `Cslib.Algorithms.Lean.HuffmanWeightTree.MergeTrace.le_pathCost`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean, line 607](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean#L607). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#le-path-cost).

## Erasing symbols from a Huffman tree

Erasing the symbols of a Huffman tree gives the
weight tree of the same shape: a leaf with symbol $s$ and natural-number weight $w$ becomes the
leaf of real weight $w$, and a fork with subtrees $L$ and $R$ becomes the fork whose subtrees are
the erasures of $L$ and $R$.

Formalized by `Cslib.Algorithms.Lean.HuffmanTree.eraseSymbols`, a definition declared in [CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean, line 631](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean#L631). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#erase-symbols).

## Erasing symbols preserves leaf weights

For every Huffman tree $T$, the multiset of leaf
weights of the weight tree obtained from $T$ by erasing its symbols is the multiset of the weights
$w$, viewed as real numbers, over the weighted leaves $(s, w)$ of $T$.

Formalized by `Cslib.Algorithms.Lean.HuffmanTree.eraseSymbols_weights`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean, line 636](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean#L636). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#erase-symbols-weights).

## Erasing symbols preserves total weight

For every Huffman tree $T$, the total weight of
the weight tree obtained from $T$ by erasing its symbols equals the total weight of $T$, viewed as
a real number.

Formalized by `Cslib.Algorithms.Lean.HuffmanTree.eraseSymbols_totalWeight`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean, line 645](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean#L645). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#erase-symbols-total-weight).

## Erasing symbols preserves weighted path length

For every Huffman tree $T$, the path cost
of the weight tree obtained from $T$ by erasing its symbols equals the weighted path length of $T$,
viewed as a real number.

Formalized by `Cslib.Algorithms.Lean.HuffmanTree.eraseSymbols_pathCost`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean, line 653](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean#L653). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#erase-symbols-path-cost).

## Priorities of a Huffman work forest

The priorities of a list of Huffman work items form
the multiset consisting of the priority of each item in the list, counted with multiplicity.

Formalized by `Cslib.Algorithms.Lean.huffmanForestPriorities`, a definition declared in [CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean, line 662](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean#L662). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#huffman-forest-priorities).

## Weights of a Huffman work forest

The weights of a list of Huffman work items form the
multiset consisting of the total leaf weight of each item's tree, taken as a real number, counted
with multiplicity.

Formalized by `Cslib.Algorithms.Lean.huffmanForestWeights`, a definition declared in [CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean, line 667](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean#L667). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#huffman-forest-weights).

## Cost of a Huffman work forest

The cost of a list of Huffman work items is the real
number obtained by summing, over the items in the list, the weighted path length of each item's
tree.

Formalized by `Cslib.Algorithms.Lean.huffmanForestCost`, a definition declared in [CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean, line 672](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean#L672). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#huffman-forest-cost).

## Huffman loop invariant

Let $n$ be a natural number, $H$ a binary min-heap of Huffman
priorities and $T$ an array of optional Huffman work items, and let $F$ be the list of work
items stored in $T$, in array order. The invariant holds when the multiset of elements of $H$
equals the multiset of priorities of the items of $F$; the serial numbers of the items of $F$ are
pairwise distinct; every item of $F$ has serial number less than $n$; every item of $F$ has
priority weight equal to the total leaf weight of its tree; $T$ has exactly $n$ cells; and every
item of $F$ is stored in the cell of $T$ whose index is its serial number.

Formalized by `Cslib.Algorithms.Lean.HuffmanLoopInvariant`, a structure declared in [CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean, line 677](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean#L677). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#huffman-loop-invariant).

## Huffman's construction follows a two-minimum merge trace

Let $L$ be a list of
symbol–weight pairs with natural-number weights, over a symbol type with decidable equality,
and suppose the Huffman construction returns the tree $t$ on $L$. Then the weighted path length
of $t$, as a real number, is the cost of a two-minimum merge trace for the multiset of the
weights of $L$, taken as reals: starting from that multiset, repeatedly replace two weights
$x \le y$ such that every other weight is at least $y$ by their sum $x + y$, until a single
weight remains; the cost is the sum of all the sums $x + y$ formed.

Formalized by `Cslib.Algorithms.Lean.huffman_mergeTrace`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean, line 1399](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean#L1399). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#huffman-merge-trace).

## Huffman's construction succeeds on nonempty inputs with distinct symbols

Let $L$ be a
nonempty list of symbol–weight pairs with natural-number weights, over a symbol type with
decidable equality. If no symbol occurs in $L$ more than once, then the Huffman construction
returns a tree on $L$.

Formalized by `Cslib.Algorithms.Lean.huffman_isSome`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean, line 1417](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean#L1417). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#huffman-is-some).

## Huffman's construction fails exactly on empty or repeated-symbol inputs

Let $L$ be a
list of symbol–weight pairs with natural-number weights, over a symbol type with decidable
equality. The Huffman construction returns no tree on $L$ if and only if $L$ is empty or some
symbol occurs in $L$ more than once.

Formalized by `Cslib.Algorithms.Lean.huffman_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean, line 1441](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean#L1441). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#huffman-eq-none-iff).

## Admissible Huffman trees

Given an input list of symbols with natural-number weights, a
Huffman tree is admissible for the input when its list of weighted leaves, read from left to right,
is a permutation of the input list: the leaves of the tree carry exactly the input's (symbol,
weight) pairs, with the same multiplicities.

Every Huffman tree is a full binary tree, so admissibility imposes no further shape condition.

Formalized by `Cslib.Algorithms.Lean.HuffmanTree.Admissible`, a definition declared in [CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean, line 1460](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean#L1460). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#admissible).

## A two-minimum merge trace gives a minimum weighted path length

Let $L$ be a list of
symbol–weight pairs with natural-number weights, and let $t$ and $t'$ be coding trees with
symbols of the same type. Suppose the weighted path length of $t$, as a real number, is the cost
of a two-minimum merge trace for the multiset of the weights of $L$, taken as reals (repeatedly
replace two weights $x \le y$, with every other weight at least $y$, by $x + y$ until one weight
remains, the cost being the sum of the sums formed), and that the weighted leaves of $t'$, listed
left to right, are a permutation of $L$. Then the weighted path length of $t$ is at most that of
$t'$.

Formalized by `Cslib.Algorithms.Lean.huffman_optimal_of_mergeTrace`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean, line 1466](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean#L1466). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#huffman-optimal-of-merge-trace).

## Optimality of Huffman coding

Let $L$ be a list of symbol–weight pairs with
natural-number weights, over a symbol type with decidable equality, and suppose the Huffman
construction returns the tree $t$ on $L$. Then every coding tree $t'$ (a full binary tree whose
leaves carry symbols and weights) whose weighted leaves, listed left to right, form a permutation
of $L$ has weighted path length at least that of $t$.

Formalized by `Cslib.Algorithms.Lean.huffman_optimal`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean, line 1484](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean#L1484). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#huffman-optimal).

## Huffman's algorithm minimizes the encoded length

Let $L$ be a list of symbol–weight
pairs with natural-number weights, over a symbol type with decidable equality, and suppose
Huffman's algorithm returns the tree $t$ on $L$. Then every Huffman tree $t'$ that is admissible
for $L$, that is, whose weighted leaves listed from left to right form a permutation of $L$, has
encoded length at least that of $t$.

The encoded length charges a lone leaf for a one-bit codeword; when the leaf symbols of a tree
are distinct, it equals the encoder's emitted cost, the total weighted codeword length.

Formalized by `Cslib.Algorithms.Lean.huffman_encodedLength_optimal`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean, line 1495](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/HuffmanOptimality.lean#L1495). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html#huffman-encoded-length-optimal).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Huffman coding](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/huffman-coding/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/InformationTheory/source-coding/huffman-coding)
