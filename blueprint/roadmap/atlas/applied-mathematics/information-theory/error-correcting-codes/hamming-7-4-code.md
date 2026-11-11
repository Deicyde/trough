---
declaration: section
origin: cited
lean: Cslib.CodingTheory.Hamming74.G, Cslib.CodingTheory.Hamming74.H, Cslib.CodingTheory.Hamming74.code, Cslib.CodingTheory.Hamming74.encode, Cslib.CodingTheory.Hamming74.message, Cslib.CodingTheory.Hamming74.errorPos, Cslib.CodingTheory.Hamming74.table, Cslib.CodingTheory.Hamming74.decode
statement: formalized
proof: formalized
---

# Hamming (7,4) code

22 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/hamming-7-4-code/index.html).

## Generator matrix of the Hamming (7,4) code

$G$ is the $4 \times 7$ matrix over
$\mathbb{F}_2$, with columns indexed by the positions $1, \dots, 7$, whose $k$-th row encodes the
$k$-th message bit: if $p$ is the $k$-th of the message positions $3, 5, 6, 7$, the row has
entry $1$ at position $p$ and at each of the parity positions $1, 2, 4$ that occurs in the
binary expansion of $p$, and entry $0$ elsewhere.

Explicitly, its rows are $1110000$, $1001100$, $0101010$ and $1101001$.

Formalized by `Cslib.CodingTheory.Hamming74.G`, a definition declared in [CSLibExt/Coding/Hamming74.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Coding/Hamming74.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/hamming-7-4-code/index.html#g).

## Parity-check matrix of the Hamming (7,4) code

$H$ is the $3 \times 7$ matrix over
$\mathbb{F}_2$, with columns indexed by the positions $1, \dots, 7$, whose column at position $p$
is the binary expansion of $p$, least significant bit first: its entry in row $i$, for
$i = 0, 1, 2$, is the $i$-th binary digit of $p$.

Formalized by `Cslib.CodingTheory.Hamming74.H`, a definition declared in [CSLibExt/Coding/Hamming74.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Coding/Hamming74.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/hamming-7-4-code/index.html#h).

## The Hamming (7,4) code

Let $H$ be the $3 \times 7$ matrix over $\mathbb{F}_2$ whose
column $j$, for $j = 1, \dots, 7$, is the binary expansion of $j$, least significant bit first.
The Hamming code is the binary linear code of length $7$ with parity-check matrix $H$: the words
$c \in \mathbb{F}_2^7$ with $Hc = 0$.

Formalized by `Cslib.CodingTheory.Hamming74.code`, a definition declared in [CSLibExt/Coding/Hamming74.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Coding/Hamming74.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/hamming-7-4-code/index.html#code).

## Encoder of the Hamming code

Let $G$ be the $4 \times 7$ generator matrix over
$\mathbb{F}_2$ with rows $(1,1,1,0,0,0,0)$, $(1,0,0,1,1,0,0)$, $(0,1,0,1,0,1,0)$ and
$(1,1,0,1,0,0,1)$. A message $m \in \mathbb{F}_2^4$ is encoded as the word
$mG \in \mathbb{F}_2^7$, the combination of the rows of $G$ with coefficients $m$.

Formalized by `Cslib.CodingTheory.Hamming74.encode`, a definition declared in [CSLibExt/Coding/Hamming74.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Coding/Hamming74.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/hamming-7-4-code/index.html#encode).

## Message bits of a word

The message of a word $y = (y_1, \dots, y_7) \in \mathbb{F}_2^7$ is
$(y_3, y_5, y_6, y_7) \in \mathbb{F}_2^4$, its bits at the positions that are not powers of two.

Formalized by `Cslib.CodingTheory.Hamming74.message`, a definition declared in [CSLibExt/Coding/Hamming74.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Coding/Hamming74.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/hamming-7-4-code/index.html#message).

## Error position of a syndrome

For a syndrome $s = (s_0, s_1, s_2) \in \mathbb{F}_2^3$,
read its entries as bits of the number $p = s_0 + 2s_1 + 4s_2 \in \{0, \dots, 7\}$. If $p = 0$
there is no error position; otherwise the error position is $p - 1 \in \{0, \dots, 6\}$.

Formalized by `Cslib.CodingTheory.Hamming74.errorPos`, a definition declared in [CSLibExt/Coding/Hamming74.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Coding/Hamming74.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/hamming-7-4-code/index.html#error-pos).

## Syndrome table of the Hamming (7,4) code

Number the positions of a word in
$\mathbb{F}_2^7$ as $1, \dots, 7$. For a syndrome $s = (s_0, s_1, s_2) \in \mathbb{F}_2^3$,
read each $s_i$ as $0$ or $1$ and let $p = s_0 + 2 s_1 + 4 s_2$. The table sends $s$ to the zero
word if $p = 0$, and otherwise to the word whose only nonzero entry is a $1$ at position $p$.

The Hamming decoder subtracts from a received word the table entry of its syndrome; over
$\mathbb{F}_2$ this flips the bit at the position the syndrome names.

Formalized by `Cslib.CodingTheory.Hamming74.table`, a definition declared in [CSLibExt/Coding/Hamming74.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Coding/Hamming74.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/hamming-7-4-code/index.html#table).

## Syndrome decoder of the Hamming code

Let $H$ be the $3 \times 7$ parity-check matrix of
the Hamming code over $\mathbb{F}_2$, whose column $j$, for $j = 1, \dots, 7$, is the binary
expansion of $j$, least significant bit first. Given a word $y \in \mathbb{F}_2^7$, compute its
syndrome $s = (s_0, s_1, s_2) = Hy \in \mathbb{F}_2^3$. If $s = 0$, return $y$. Otherwise read
the entries of $s$ as bits of the number $p = s_0 + 2s_1 + 4s_2 \in \{1, \dots, 7\}$ and return
$y$ with its $p$-th bit flipped, counting positions from $1$.

Formalized by `Cslib.CodingTheory.Hamming74.decode`, a definition declared in [CSLibExt/Coding/Hamming74.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Coding/Hamming74.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/hamming-7-4-code/index.html#decode).

## The syndrome of a single-bit error locates it

Let $H$ be the parity-check matrix of the
Hamming (7,4) code, and index the coordinates of words in $\mathbb{F}_2^7$ by $0, \dots, 6$, so
that index $i$ is position $i + 1$. For each index $i$, let $e_i \in \mathbb{F}_2^7$ be the word
with entry $1$ at index $i$ and $0$ elsewhere. Then the error position of the syndrome $He_i$ is
defined and equals $i$.

Formalized by `Cslib.CodingTheory.Hamming74.errorPos_syndrome_single`, a theorem declared in [CSLibExt/Coding/Hamming74.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Coding/Hamming74.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/hamming-7-4-code/index.html#error-pos-syndrome-single).

## The Hamming decoder's syndrome table is correct

Let $H$ be the parity-check matrix of the
Hamming (7,4) code and $T$ the syndrome table of its decoder. Then $T$ is a correct syndrome
table up to radius $1$ for $H$: for every word $e \in \mathbb{F}_2^7$ of Hamming weight at most
$1$, the word $T(He)$ has Hamming weight at most $1$ and the same syndrome as $e$, that is,
$H \, T(He) = He$.

Formalized by `Cslib.CodingTheory.Hamming74.isSyndromeTable_table`, a theorem declared in [CSLibExt/Coding/Hamming74.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Coding/Hamming74.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/hamming-7-4-code/index.html#is-syndrome-table-table).

## The generator matrix is orthogonal to the parity-check matrix

Let $G$ be the generator
matrix and $H$ the parity-check matrix of the Hamming (7,4) code over $\mathbb{F}_2$. Then
$G H^{\mathsf{T}} = 0$, the $4 \times 3$ zero matrix: every row of $G$ is orthogonal to every
row of $H$, so every row of $G$ satisfies the parity checks given by $H$.

Formalized by `Cslib.CodingTheory.Hamming74.G_mul_H_transpose`, a theorem declared in [CSLibExt/Coding/Hamming74.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Coding/Hamming74.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/hamming-7-4-code/index.html#g-mul-h-transpose).

## The Hamming generator matrix generates the Hamming code

The code generated by the
generator matrix $G$, that is, the set of words $mG$ for $m \in \mathbb{F}_2^4$, equals the
Hamming (7,4) code, the set of words $c \in \mathbb{F}_2^7$ with $Hc = 0$ for the parity-check
matrix $H$.

Formalized by `Cslib.CodingTheory.Hamming74.ofGenerator_G_eq_code`, a theorem declared in [CSLibExt/Coding/Hamming74.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Coding/Hamming74.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/hamming-7-4-code/index.html#of-generator-g-eq-code).

## The Hamming (7,4) code has minimum weight at least 3

Every nonzero codeword of the
Hamming (7,4) code over $\mathbb{F}_2$ has at least $3$ nonzero coordinates; that is, the minimum
weight of the code is at least $3$.

Formalized by `Cslib.CodingTheory.Hamming74.three_le_minWeight_code`, a theorem declared in [CSLibExt/Coding/Hamming74.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Coding/Hamming74.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/hamming-7-4-code/index.html#three-le-min-weight-code).

## Minimum distance of the Hamming (7,4) code

The minimum distance of the Hamming (7,4)
code is $3$.

Formalized by `Cslib.CodingTheory.Hamming74.minDist_code`, a theorem declared in [CSLibExt/Coding/Hamming74.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Coding/Hamming74.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/hamming-7-4-code/index.html#min-dist-code).

## The decoder corrects every error of weight at most 1

For every codeword $c$ of the
Hamming code and every word $e \in \mathbb{F}_2^7$ of Hamming weight at most $1$, decoding
$c + e$ returns $c$.

Formalized by `Cslib.CodingTheory.Hamming74.decode_add`, a theorem declared in [CSLibExt/Coding/Hamming74.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Coding/Hamming74.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/hamming-7-4-code/index.html#decode-add).

## Every single-bit error is corrected

For every message $m \in \mathbb{F}_2^4$ and every
position $i$ among the $7$, flipping bit $i$ of the encoding of $m$ and then decoding returns
the encoding of $m$.

Formalized by `Cslib.CodingTheory.Hamming74.decode_encode_add_single`, a theorem declared in [CSLibExt/Coding/Hamming74.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Coding/Hamming74.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/hamming-7-4-code/index.html#decode-encode-add-single).

## The decoder always outputs a codeword

For every word $y \in \mathbb{F}_2^7$, the
decoding of $y$ belongs to the Hamming code.

Formalized by `Cslib.CodingTheory.Hamming74.decode_mem_code`, a theorem declared in [CSLibExt/Coding/Hamming74.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Coding/Hamming74.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/hamming-7-4-code/index.html#decode-mem-code).

## The Hamming decoder changes at most one bit

Let $D$ be the Hamming (7,4) decoder. For
every word $y \in \mathbb{F}_2^7$, the Hamming distance between $y$ and $D(y)$ is at most $1$.

Formalized by `Cslib.CodingTheory.Hamming74.hammingDist_decode_le_one`, a theorem declared in [CSLibExt/Coding/Hamming74.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Coding/Hamming74.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/hamming-7-4-code/index.html#hamming-dist-decode-le-one).

## The Hamming code is perfect

Every word lies within distance 1 of exactly one codeword.

Formalized by `Cslib.CodingTheory.Hamming74.existsUnique_hammingDist_le_one`, a theorem declared in [CSLibExt/Coding/Hamming74.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Coding/Hamming74.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/hamming-7-4-code/index.html#exists-unique-hamming-dist-le-one).

## No codeword is closer than the Hamming decoder's output

Let $D$ be the Hamming (7,4)
decoder and $C \subseteq \mathbb{F}_2^7$ the Hamming code. For every word $y \in \mathbb{F}_2^7$
and every codeword $c \in C$, the Hamming distance between $y$ and $D(y)$ is at most the
Hamming distance between $y$ and $c$.

Since $D(y)$ is itself a codeword, the decoder returns a nearest codeword.

Formalized by `Cslib.CodingTheory.Hamming74.hammingDist_decode_le`, a theorem declared in [CSLibExt/Coding/Hamming74.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Coding/Hamming74.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/hamming-7-4-code/index.html#hamming-dist-decode-le).

## Hamming bound for the Hamming (7,4) code

Let $k$ be the dimension of the Hamming (7,4)
code over $\mathbb{F}_2$. Then $2^k \cdot \sum_{i=0}^{1} \binom{7}{i} (2 - 1)^i \le 2^7$.

This is the Hamming bound for codes correcting one error, obtained from the general Hamming
bound for linear codes, which applies because the minimum distance $3$ exceeds $2$.

Formalized by `Cslib.CodingTheory.Hamming74.pow_finrank_mul_sum_le`, a theorem declared in [CSLibExt/Coding/Hamming74.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Coding/Hamming74.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/hamming-7-4-code/index.html#pow-finrank-mul-sum-le).

## The Hamming bound is attained

Let $k$ be the dimension of the Hamming (7,4) code over
$\mathbb{F}_2$. Then $2^k \cdot \sum_{i=0}^{1} \binom{7}{i} (2 - 1)^i = 2^7$: the Hamming bound
for one error holds with equality.

Since $k = 4$, this reads $2^4 \cdot (1 + 7) = 2^7$, so the radius-$1$ Hamming balls around the
codewords fill $\mathbb{F}_2^7$.

Formalized by `Cslib.CodingTheory.Hamming74.pow_finrank_mul_sum_eq`, a theorem declared in [CSLibExt/Coding/Hamming74.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Coding/Hamming74.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/hamming-7-4-code/index.html#pow-finrank-mul-sum-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hamming (7,4) code](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/hamming-7-4-code/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/InformationTheory/error-correcting-codes/hamming-7-4-code)
