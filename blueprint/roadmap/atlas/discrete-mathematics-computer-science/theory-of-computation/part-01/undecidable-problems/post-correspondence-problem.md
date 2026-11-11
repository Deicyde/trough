---
declaration: section
origin: cited
lean: Cslib.Decidability.Post.Domino, Cslib.Decidability.Post.top, Cslib.Decidability.Post.bottom, Cslib.Decidability.Post.IsSolution, Cslib.Decidability.Post.PCP, Cslib.Decidability.Post.MPCP, Cslib.Decidability.Post.NonemptyWords, Cslib.Decidability.Post.Sym
statement: formalized
proof: formalized
---

# Post correspondence problem

79 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html).

## Domino (Post correspondence problem)

A domino over an alphabet $\alpha$ is a pair
$(t, b)$ of words over $\alpha$: its top word $t$ and its bottom word $b$.

Formalized by `Cslib.Decidability.Post.Domino`, an abbreviation declared in [CSLibExt/Computability/Decidability/PCP.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCP.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#domino).

## Top word of a sequence of dominoes

For a sequence of dominoes
$(t_1, b_1), \ldots, (t_n, b_n)$, its top word is the concatenation $t_1 t_2 \cdots t_n$ of their
top words; the empty sequence has the empty top word.

Formalized by `Cslib.Decidability.Post.top`, a definition declared in [CSLibExt/Computability/Decidability/PCP.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCP.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#top).

## Bottom word of a domino sequence

For a sequence $s = d_1, \dots, d_k$ of dominoes, the
bottom word of $s$ is the concatenation $b_1 b_2 \cdots b_k$, where $b_i$ is the bottom word of
$d_i$.

Formalized by `Cslib.Decidability.Post.bottom`, a definition declared in [CSLibExt/Computability/Decidability/PCP.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCP.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#bottom).

## PCP solution

Let $P$ be a finite list of dominoes. A solution of $P$ is a nonempty
sequence $d_1, \dots, d_k$ of dominoes, each occurring in $P$ (repetitions allowed), such that the
concatenation of the top words of $d_1, \dots, d_k$ equals the concatenation of their bottom
words.

Formalized by `Cslib.Decidability.Post.IsSolution`, a definition declared in [CSLibExt/Computability/Decidability/PCP.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCP.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#is-solution).

## The Post correspondence problem

A list $P$ of dominoes is a solvable instance of the
Post correspondence problem when it has a PCP solution: a nonempty sequence of dominoes from $P$,
repetitions allowed, whose top words and bottom words concatenate to the same word.

Formalized by `Cslib.Decidability.Post.PCP`, a definition declared in [CSLibExt/Computability/Decidability/PCP.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCP.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#pcp).

## The modified Post correspondence problem

A list $P$ of dominoes has an MPCP solution
when $P$ is nonempty and some PCP solution of $P$ starts with the first domino of $P$.

Formalized by `Cslib.Decidability.Post.MPCP`, a definition declared in [CSLibExt/Computability/Decidability/PCP.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCP.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#mpcp).

## Instances with nonempty words

A list $P$ of dominoes has nonempty words when every
domino of $P$ has a nonempty top word and a nonempty bottom word.

Formalized by `Cslib.Decidability.Post.NonemptyWords`, a definition declared in [CSLibExt/Computability/Decidability/PCP.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCP.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#nonempty-words).

## The extended alphabet of the MPCP-to-PCP reduction

For an alphabet $\alpha$, the extended
alphabet consists of the letters of $\alpha$ together with two new symbols: the star $\star$ and
the end marker $\diamond$.

It is represented so that it has a primitive recursive encoding whenever $\alpha$ has one.

Formalized by `Cslib.Decidability.Post.Sym`, an abbreviation declared in [CSLibExt/Computability/Decidability/PCP.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCP.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#sym).

## The alphabet inside the extended alphabet

Each letter $a$ of the alphabet $\alpha$ is
regarded as a symbol of the extended alphabet of the MPCP-to-PCP reduction, which consists of the
letters of $\alpha$, the star $\star$ and the end marker $\diamond$.

Formalized by `Cslib.Decidability.Post.letter`, an abbreviation declared in [CSLibExt/Computability/Decidability/PCP.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCP.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#letter).

## The star symbol

The star $\star$ is the new symbol of the extended alphabet that is
neither a letter of $\alpha$ nor the end marker $\diamond$.

Formalized by `Cslib.Decidability.Post.star`, an abbreviation declared in [CSLibExt/Computability/Decidability/PCP.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCP.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#star).

## End marker

The end marker $\diamond$ is the symbol of the extended alphabet of the
MPCP-to-PCP reduction that is neither a letter of $\alpha$ nor the star $\star$.

Formalized by `Cslib.Decidability.Post.endMark`, an abbreviation declared in [CSLibExt/Computability/Decidability/PCP.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCP.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#end-mark).

## A star before every letter

Let $\star$ be the star of the extended alphabet. For a word
$u = a_1 a_2 \cdots a_n$ over $\alpha$, the word $\star u$ over the extended alphabet is
$\star a_1 \star a_2 \cdots \star a_n$, obtained by putting a star before every letter of $u$; the
empty word gives the empty word.

Formalized by `Cslib.Decidability.Post.starBefore`, a definition declared in [CSLibExt/Computability/Decidability/PCP.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCP.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#star-before).

## A star after every letter

Let $\star$ be the star of the extended alphabet. For a word
$u = a_1 a_2 \cdots a_n$ over $\alpha$, the word $u\star$ over the extended alphabet is
$a_1 \star a_2 \star \cdots a_n \star$, obtained by putting a star after every letter of $u$; the
empty word gives the empty word.

Formalized by `Cslib.Decidability.Post.starAfter`, a definition declared in [CSLibExt/Computability/Decidability/PCP.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCP.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#star-after).

## Erasing stars and end markers

For a word $w$ over the extended alphabet of the
MPCP-to-PCP reduction, this is the word over $\alpha$ obtained from $w$ by deleting every star
$\star$ and every end marker $\diamond$, keeping the letters of $\alpha$ in their order.

Formalized by `Cslib.Decidability.Post.letters`, a definition declared in [CSLibExt/Computability/Decidability/PCP.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCP.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#letters).

## Starred image of a domino

For a word $u$ over $\alpha$, write $\star u$ for the word over
the extended alphabet obtained by putting a star $\star$ before every letter of $u$, and $u\star$
for the word obtained by putting a star after every letter. A domino $(t, b)$ over $\alpha$ is sent
to the domino $(\star t, b\star)$ over the extended alphabet.

Formalized by `Cslib.Decidability.Post.mapDomino`, a definition declared in [CSLibExt/Computability/Decidability/PCP.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCP.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#map-domino).

## The start domino of the MPCP-to-PCP reduction

For a domino $(t, b)$ over an alphabet
$\alpha$, its start domino is the domino $(\star t, \star b \star)$ over the extended alphabet,
where $\star t$ puts the star $\star$ before every letter of $t$ and $b \star$ puts a star after
every letter of $b$, so that the bottom word gets one extra star in front.

Formalized by `Cslib.Decidability.Post.startDomino`, a definition declared in [CSLibExt/Computability/Decidability/PCP.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCP.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#start-domino).

## End domino of the MPCP-to-PCP reduction

Over the alphabet $\alpha$ extended with the
star $\star$ and the end marker $\diamond$, the end domino is $(\star\diamond, \diamond)$: its top
word is $\star$ followed by $\diamond$, and its bottom word is $\diamond$.

Formalized by `Cslib.Decidability.Post.endDomino`, a definition declared in [CSLibExt/Computability/Decidability/PCP.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCP.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#end-domino).

## The reduction from MPCP to PCP

Write $\star$ for the star and $\diamond$ for the end
marker of the extended alphabet; for a word $u$ over $\alpha$, $\star u$ puts a star before every
letter of $u$ and $u \star$ puts a star after every letter of $u$. The empty list of dominoes is
sent to the empty list. A list $P = [d_0, d_1, \ldots, d_n]$ of dominoes over $\alpha$, with
$d_0 = (t_0, b_0)$, is sent to the following list of dominoes over the extended alphabet: first
the start domino $(\star t_0, \star b_0 \star)$, then the domino $(\star t, b \star)$ for each
domino $(t, b)$ of $P$ in order (including $d_0$), and last the end domino
$(\star \diamond, \diamond)$, whose top word is a star followed by the end marker.

Formalized by `Cslib.Decidability.Post.toPCP`, a definition declared in [CSLibExt/Computability/Decidability/PCP.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCP.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#to-pcp).

## Erasing the markers from a domino

For a domino $(t, b)$ over the extended alphabet, its
unmapping is the domino over $\alpha$ obtained by deleting every star $\star$ and every end marker
$\diamond$ from both $t$ and $b$, keeping the letters of $\alpha$ in order.

It reads a domino of the reduced PCP instance back as a domino over $\alpha$.

Formalized by `Cslib.Decidability.Post.unmap`, a definition declared in [CSLibExt/Computability/Decidability/PCP.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCP.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#unmap).

## An MPCP solution gives a PCP solution of the reduced instance

If a list $P$ of dominoes
has an MPCP solution, then the image of $P$ under the reduction from MPCP to PCP has a PCP
solution.

Formalized by `Cslib.Decidability.Post.pcp_toPCP_of_mpcp`, a theorem declared in [CSLibExt/Computability/Decidability/PCP.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCP.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#pcp-to-pcp-of-mpcp).

## On instances with nonempty words, a PCP solution of the reduced instance gives an MPCP solution

**On instances with nonempty words, a PCP solution of the reduced instance gives an MPCP
solution.** Let $P$ be a list of dominoes in which every domino has a nonempty top and a nonempty
bottom. If the image of $P$ under the reduction from MPCP to PCP has a PCP solution, then $P$ has
an MPCP solution.

Formalized by `Cslib.Decidability.Post.mpcp_of_pcp_toPCP`, a theorem declared in [CSLibExt/Computability/Decidability/PCP.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCP.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#mpcp-of-pcp-to-pcp).

## MPCP reduces to PCP on instances with nonempty words

Let $P$ be a list of dominoes over
an alphabet $\alpha$ in which every domino has a nonempty top and a nonempty bottom. Then $P$ has
an MPCP solution if and only if the image of $P$ under the reduction from MPCP to PCP, an
instance over $\alpha$ extended with a star and an end marker, has a PCP solution.

Formalized by `Cslib.Decidability.Post.mpcp_iff_pcp_toPCP`, a theorem declared in [CSLibExt/Computability/Decidability/PCP.lean, line 305](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCP.lean#L305). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#mpcp-iff-pcp-to-pcp).

## Boolean test for nonempty words

For a list $P$ of dominoes, this Boolean test returns
true exactly when every domino of $P$ has a nonempty top and a nonempty bottom.

Formalized by `Cslib.Decidability.Post.nonemptyWordsB`, a definition declared in [CSLibExt/Computability/Decidability/PCP.lean, line 312](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCP.lean#L312). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#nonempty-words-b).

## The total reduction from MPCP to PCP

For a list $P$ of dominoes, the total reduction
sends $P$ to its image under the reduction from MPCP to PCP when every domino of $P$ has a
nonempty top and a nonempty bottom, and to the empty instance, which has no PCP solution,
otherwise.

Formalized by `Cslib.Decidability.Post.reduce`, a definition declared in [CSLibExt/Computability/Decidability/PCP.lean, line 319](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCP.lean#L319). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#reduce).

## The nonempty-words test is primitive recursive

For an alphabet $\alpha$ with a
primitive recursive coding, the Boolean test of whether every domino of a list over $\alpha$ has
a nonempty top and a nonempty bottom is a primitive recursive function of the list.

Formalized by `Cslib.Decidability.Post.primrec_nonemptyWordsB`, a theorem declared in [CSLibExt/Computability/Decidability/PCP.lean, line 364](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCP.lean#L364). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#primrec-nonempty-words-b).

## MPCP many-one reduces to PCP

Let $\alpha$ be an alphabet with a primitive recursive
coding, and let $\alpha'$ be $\alpha$ extended with two new symbols, the star and the end marker.
There is a computable function $f$ from finite lists of dominoes over $\alpha$ to finite lists of
dominoes over $\alpha'$ such that, for every list $P$ of dominoes over $\alpha$, $f(P)$ has a PCP
solution if and only if both every domino of $P$ has a nonempty top word and a nonempty bottom
word, and $P$ has an MPCP solution.

Formalized by `Cslib.Decidability.Post.manyOneReducible_mpcp_pcp`, a theorem declared in [CSLibExt/Computability/Decidability/PCP.lean, line 385](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCP.lean#L385). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#many-one-reducible-mpcp-pcp).

## Boolean check for PCP solutions

Let $\alpha$ be an alphabet with a primitive recursive
coding and decidable equality, and let $P$ and $s$ be lists of dominoes over $\alpha$. The Boolean
solution check of $s$ for $P$ is true exactly when $s$ is nonempty, every domino of $s$ occurs in
$P$, and the top word of $s$ equals the bottom word of $s$, and it is false otherwise.

Formalized by `Cslib.Decidability.Post.isSolutionB`, a definition declared in [CSLibExt/Computability/Decidability/PCP.lean, line 399](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCP.lean#L399). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#is-solution-b).

## PCP is recursively enumerable

For an alphabet $\alpha$ with a primitive recursive
coding, the set of lists of dominoes over $\alpha$ that have a PCP solution is recursively
enumerable.

The proof searches all candidate sequences.

Formalized by `Cslib.Decidability.Post.rePred_pcp`, a theorem declared in [CSLibExt/Computability/Decidability/PCP.lean, line 435](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCP.lean#L435). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#re-pred-pcp).

## PCP is Turing-recognizable

For every alphabet $\alpha$ with a primitive recursive
encoding, there is a multi-stack Turing machine that, started on the binary encoding of a list
$P$ of dominoes over $\alpha$, halts exactly when $P$ has a PCP solution.

Formalized by `Cslib.Decidability.Post.tm2Recognizable_pcp`, a theorem declared in [CSLibExt/Computability/Decidability/PCP.lean, line 457](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCP.lean#L457). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#tm2-recognizable-pcp).

## Total length of dominoes that are at least as long on top

Write $|w|$ for the length of a
word $w$. Let $s$ be a finite sequence of dominoes over an alphabet. If every domino $(t, b)$ in
$s$ satisfies $|b| \le |t|$, then the concatenation of the bottom words of $s$ is no longer than
the concatenation of the top words of $s$.

Formalized by `Cslib.Decidability.Post.length_bottom_le_length_top`, a theorem declared in [CSLibExt/Computability/Decidability/PCPUnary.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUnary.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#length-bottom-le-length-top).

## Total length of dominoes that are strictly longer on top

Write $|w|$ for the length of a
word $w$. Let $s$ be a nonempty finite sequence of dominoes over an alphabet. If every domino
$(t, b)$ in $s$ satisfies $|b| < |t|$, then the concatenation of the bottom words of $s$ is strictly
shorter than the concatenation of the top words of $s$.

Formalized by `Cslib.Decidability.Post.length_bottom_lt_length_top`, a theorem declared in [CSLibExt/Computability/Decidability/PCPUnary.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUnary.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#length-bottom-lt-length-top).

## Swapping top and bottom

For a finite sequence $s$ of dominoes, the swapped sequence is
obtained from $s$ by exchanging the top and bottom word of every domino: each $(t, b)$ becomes
$(b, t)$, and the order of the dominoes is unchanged.

Formalized by `Cslib.Decidability.Post.swap`, a definition declared in [CSLibExt/Computability/Decidability/PCPUnary.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUnary.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#swap).

## The unary PCP criterion

Let $\alpha$ be an alphabet with at most one letter, and write
$|w|$ for the length of a word $w$. A finite list $P$ of dominoes over $\alpha$ has a PCP solution
if and only if either some domino $(t, b)$ in $P$ has $|t| = |b|$, or some domino $(t, b)$ in $P$
has $|t| < |b|$ and some domino $(t', b')$ in $P$ has $|b'| < |t'|$.

Formalized by `Cslib.Decidability.Post.pcp_iff_of_subsingleton`, a theorem declared in [CSLibExt/Computability/Decidability/PCPUnary.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUnary.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#pcp-iff-of-subsingleton).

## The unary PCP test

Let $\alpha$ be an alphabet with at most one letter, and write $|w|$
for the length of a word $w$. For a finite list $P$ of dominoes over $\alpha$, the unary test of
$P$ is the Boolean value that is true exactly when some domino $(t, b)$ in $P$ has $|t| = |b|$, or
some domino $(t, b)$ in $P$ has $|t| < |b|$ and some domino $(t', b')$ in $P$ has $|b'| < |t'|$.

Formalized by `Cslib.Decidability.Post.unaryTest`, a definition declared in [CSLibExt/Computability/Decidability/PCPUnary.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUnary.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#unary-test).

## PCP over a one-letter alphabet is decidable

Let $\alpha$ be an alphabet with at most one
letter whose elements have a computable encoding. Then the Post correspondence problem over
$\alpha$ is a computable predicate: some computable function decides, for every finite list $P$
of dominoes over $\alpha$, whether $P$ has a PCP solution.

Formalized by `Cslib.Decidability.Post.computablePred_pcp_of_subsingleton`, a theorem declared in [CSLibExt/Computability/Decidability/PCPUnary.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUnary.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#computable-pred-pcp-of-subsingleton).

## Unary PCP is decidable by a multi-stack machine

Let $\alpha$ be an alphabet with at most
one letter whose elements have a computable encoding. Then the Post correspondence problem over
$\alpha$ is decidable by a multi-stack machine: some multi-stack Turing machine decides, for every
finite list $P$ of dominoes over $\alpha$, whether $P$ has a PCP solution.

Formalized by `Cslib.Decidability.Post.tm2Decidable_pcp_of_subsingleton`, a theorem declared in [CSLibExt/Computability/Decidability/PCPUnary.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUnary.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#tm2-decidable-pcp-of-subsingleton).

## Symbols of the rewriting system of a single-tape machine

For a tape alphabet $\Gamma$ and
a set of states $\Lambda$, the symbols of the rewriting system simulating a single-tape machine are
a tape symbol $a$ for each $a \in \Gamma$, a state symbol $q$ for each $q \in \Lambda$, the left end
marker $\vdash$, the right end marker $\dashv$ and the halting symbol $H$.

Formalized by `Cslib.Decidability.TMRewriting.TMSym`, an inductive type declared in [CSLibExt/Computability/Decidability/PCPUndecidable.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUndecidable.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#tmsym).

## Control symbols

A symbol of the rewriting system simulating a single-tape Turing machine
is a control symbol if it is a state symbol or the halting symbol $H$; tape symbols and the end
markers $\vdash$ and $\dashv$ are not control symbols.

Formalized by `Cslib.Decidability.TMRewriting.IsCtl`, a definition declared in [CSLibExt/Computability/Decidability/PCPUndecidable.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUndecidable.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#is-ctl).

## Unique splitting at a marked letter

Let $P$ be a property of the elements of a type
$\alpha$, let $A$ and $B$ be lists over $\alpha$ none of whose elements satisfy $P$, and let
$y \in \alpha$. If $C$ and $D$ are lists over $\alpha$ and $x \in \alpha$ satisfies $P$ with
$C\,x\,D = A\,y\,B$ (concatenation), then $C = A$, $x = y$ and $D = B$.

Formalized by `Cslib.Decidability.TMRewriting.eq_of_append_cons_eq`, a theorem declared in [CSLibExt/Computability/Decidability/PCPUndecidable.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUndecidable.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#eq-of-append-cons-eq).

## Splitting a rewrite site at its control symbol

Let $A$, $B$, $u$, $v$, $p$, $s$ be words
over the symbols of the rewriting system simulating a single-tape machine, and let $x$ and $y$ be
symbols. If no symbol of $A$ or of $B$ is a control symbol (a state symbol or the halting symbol),
$x$ is a control symbol, and $u\,p\,x\,s\,v = A\,y\,B$, then $u\,p = A$, $x = y$ and $s\,v = B$.

Formalized by `Cslib.Decidability.TMRewriting.split_site`, a theorem declared in [CSLibExt/Computability/Decidability/PCPUndecidable.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUndecidable.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#split-site).

## The word of a configuration

For a state $q$, a tape symbol $h$ and words $L$, $R$ of
tape symbols, the word of the configuration in state $q$ with head symbol $h$, left part $L$
(in reading order, from left to right) and right part $R$ is $\vdash L\,q\,h\,R \dashv$, where
$\vdash$ and $\dashv$ are the end markers.

Formalized by `Cslib.Decidability.TMRewriting.spell`, a definition declared in [CSLibExt/Computability/Decidability/PCPUndecidable.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUndecidable.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#spell).

## The halting word

The halting word is the word $\vdash H \dashv$ made of the left end
marker, the halting symbol and the right end marker. It is the target word of the rewriting
simulation of a single-tape machine.

Formalized by `Cslib.Decidability.TMRewriting.haltWord`, a definition declared in [CSLibExt/Computability/Decidability/PCPUndecidable.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUndecidable.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#halt-word).

## Words spelling a configuration

A word $w$ spells a configuration $c$ of a single-tape
Turing machine if there are a state $q$, a tape symbol $h$ and words $L$, $R$ of tape symbols
such that $c$ is in state $q$, its head reads $h$, its tape reads $L$ immediately to the left of
the head and $R$ immediately to the right of it, with blanks beyond, and
$w = \vdash L\,q\,h\,R \dashv$.

Formalized by `Cslib.Decidability.TMRewriting.Spells`, a definition declared in [CSLibExt/Computability/Decidability/PCPUndecidable.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUndecidable.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#spells).

## The start word

For an input $l$ of tape symbols, the start word is
$\vdash q_0\, h\, R \dashv$, where $\vdash$ and $\dashv$ are the left and right end markers,
$q_0$ is the default state, $h$ is the first symbol of $l$ (the default tape symbol if $l$ is
empty) and $R$ is the rest of $l$. It spells the configuration in state $q_0$ with head symbol
$h$, empty left part and right part $R$.

Formalized by `Cslib.Decidability.TMRewriting.initWord`, a definition declared in [CSLibExt/Computability/Decidability/PCPUndecidable.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUndecidable.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#init-word).

## The rules for one transition

Let $M$ be a single-tape Turing machine with finitely many
states and tape symbols, let $\sqcup$ be its blank symbol, and write $\vdash$, $\dashv$ for the end
markers and $H$ for the halting symbol. The rules for a state $q$ reading a tape symbol $a$ are:
the rule $q\,a \to H$ if $M$ has no transition from $q$ reading $a$; the rule
$q\,a \to q'\,b$ if $M$ writes $b$ and enters $q'$; the rules
$q\,a \dashv \to a\,q'\,\sqcup \dashv$ and, for every tape symbol $c$, $q\,a\,c \to a\,q'\,c$ if
$M$ moves right and enters $q'$; and the rules ${\vdash}\,q\,a \to {\vdash}\,q'\,\sqcup\,a$ and,
for every tape symbol $c$, $c\,q\,a \to q'\,c\,a$ if $M$ moves left and enters $q'$.

Formalized by `Cslib.Decidability.TMRewriting.rulesFor`, a definition declared in [CSLibExt/Computability/Decidability/PCPUndecidable.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUndecidable.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#rules-for).

## Erasing rules

For a finite tape alphabet $\Gamma$, let $H$ be the halting symbol of the
rewriting system simulating a single-tape machine with tape alphabet $\Gamma$. The erasing rules
are the rewriting rules $c\,H \to H$ and $H\,c \to H$ for every tape symbol $c \in \Gamma$: the
halting symbol deletes the tape symbol on either side of it.

Formalized by `Cslib.Decidability.TMRewriting.eraseRules`, a definition declared in [CSLibExt/Computability/Decidability/PCPUndecidable.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUndecidable.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#erase-rules).

## The rewriting system simulating a Turing machine

Let $M$ be a single-tape Turing
machine with finitely many states and tape symbols, and write $H$ for the halting symbol. The
rewriting system simulating $M$ is the finite list of rules consisting of the rules for every
state $q$ reading every tape symbol $a$, followed by the erasing rules $c\,H \to H$ and
$H\,c \to H$ for every tape symbol $c$.

Formalized by `Cslib.Decidability.TMRewriting.rules`, a definition declared in [CSLibExt/Computability/Decidability/PCPUndecidable.lean, line 264](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUndecidable.lean#L264). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#rules).

## The eight kinds of rules of the machine-simulating rewriting system

Let $M$ be a
single-tape Turing machine with a finite tape alphabet $\Gamma$, a default (blank) symbol
$\beta \in \Gamma$ and finitely many states. The symbols are the tape symbols, the states, the end
markers $\vdash$ and $\dashv$, and the halting symbol $H$. Every rule $l \to r$ of the rewriting
system simulating $M$ has one of the following eight forms, where $q, q'$ are states and
$a, b, c$ are tape symbols. Either $M$ has no transition in state $q$ reading $a$, and $l = q\,a$,
$r = H$; or in state $q$ reading $a$ the machine $M$ goes to state $q'$ and writes $b$, and
$l = q\,a$, $r = q'\,b$; or in state $q$ reading $a$ it goes to $q'$ and moves the head right, and
either $l = q\,a \dashv$, $r = a\,q'\,\beta \dashv$ or $l = q\,a\,c$, $r = a\,q'\,c$; or in state
$q$ reading $a$ it goes to $q'$ and moves the head left, and either $l = \vdash q\,a$,
$r = \vdash q'\,\beta\,a$ or $l = c\,q\,a$, $r = q'\,c\,a$; or $l = c\,H$, $r = H$; or $l = H\,c$,
$r = H$.

Formalized by `Cslib.Decidability.TMRewriting.cases_of_mem_rules`, a theorem declared in [CSLibExt/Computability/Decidability/PCPUndecidable.lean, line 309](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUndecidable.lean#L309). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#cases-of-mem-rules).

## One machine step is one rewrite

Let $M$ be a single-tape Turing machine with finitely
many tape symbols and states. If the word $w$ spells the configuration $c$ and $M$ steps from
$c$ to $c'$, then $w$ rewrites in one step of the rewriting system simulating $M$ to a word
$w'$ that spells $c'$.

Formalized by `Cslib.Decidability.TMRewriting.exists_step_of_spells`, a theorem declared in [CSLibExt/Computability/Decidability/PCPUndecidable.lean, line 368](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUndecidable.lean#L368). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#exists-step-of-spells).

## The halting symbol erases the tape

Let $M$ be a single-tape Turing machine with finitely
many states and tape symbols, and let $\vdash$, $\dashv$ be the end markers and $H$ the halting
symbol of the rewriting system simulating $M$. For all words $X$ and $Y$ of tape symbols, the word
$\vdash X\,H\,Y \dashv$ rewrites in zero or more steps of this rewriting system to the halting
word $\vdash H \dashv$.

Formalized by `Cslib.Decidability.TMRewriting.derives_erase`, a theorem declared in [CSLibExt/Computability/Decidability/PCPUndecidable.lean, line 404](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUndecidable.lean#L404). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#derives-erase).

## A halted configuration rewrites to the halting word

Let $M$ be a single-tape Turing
machine with finitely many states and tape symbols, and let $\vdash$, $\dashv$ be the end markers
and $H$ the halting symbol of the rewriting system simulating $M$. Let $c$ be a configuration of
$M$ at which $M$ has no next step, and let $w$ be a word that spells $c$: for some state $q$, tape
symbol $h$ and lists $L$, $R$ of tape symbols, $c$ is in state $q$ with $h$ under the head, the
tape left of the head reads $L$ from left to right and the tape right of the head reads $R$, up to
blanks at the far ends, and $w = \vdash L\,q\,h\,R \dashv$. Then $w$ rewrites in zero or more steps
of this rewriting system to the halting word $\vdash H \dashv$.

Formalized by `Cslib.Decidability.TMRewriting.derives_of_spells_of_step_eq_none`, a theorem declared in [CSLibExt/Computability/Decidability/PCPUndecidable.lean, line 424](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUndecidable.lean#L424). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#derives-of-spells-of-step-eq-none).

## Invariant of the rewriting simulation of a single-tape machine

Let $M$ be a single-tape
machine with finitely many tape symbols and states, and $l$ an input. A word $w$ satisfies the
invariant for $l$ when either $w$ spells a configuration that $M$ reaches from its initial
configuration on $l$, or $M$ halts on $l$ and $w = \vdash X\, H\, Y \dashv$ for some words $X$
and $Y$ of tape symbols, where $\vdash$ and $\dashv$ are the left and right end markers and $H$
is the halting symbol. It serves as the invariant of the words reachable from the start word
of $l$.

Formalized by `Cslib.Decidability.TMRewriting.Inv`, a definition declared in [CSLibExt/Computability/Decidability/PCPUndecidable.lean, line 451](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUndecidable.lean#L451). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#inv).

## Every rewrite preserves the invariant of reachable words

Let $M$ be a single-tape machine
with finite tape alphabet and finite set of states, and let $l$ be an input word. Write $\vdash$
and $\dashv$ for the left and right end markers and $H$ for the halting symbol. A word $w$
satisfies the invariant for $M$ and $l$ when either $w$ spells a configuration that $M$ reaches from
its initial configuration on $l$ (the configuration with state $q$, head symbol $h$, left part $L$
and right part $R$, finite words of tape symbols read from left to right beyond which the tape is
blank, is spelled ${\vdash}\,L\,q\,h\,R\,{\dashv}$), or $M$ halts on $l$ and
$w = {\vdash}\,X\,H\,Y\,{\dashv}$ for words $X$ and $Y$ of tape symbols. If $w$ satisfies the
invariant and rewrites in one step to $w'$ under the rules of $M$, then $w'$ satisfies the
invariant.

Formalized by `Cslib.Decidability.TMRewriting.Inv.step`, a theorem declared in [CSLibExt/Computability/Decidability/PCPUndecidable.lean, line 464](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUndecidable.lean#L464). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#step).

## A single-tape machine halts iff its start word rewrites to the halting word

Let $M$ be a
single-tape machine with finite tape alphabet and finite set of states, and write $\vdash$ and
$\dashv$ for the left and right end markers and $H$ for the halting symbol. For every input word
$l$, $M$ halts on $l$ if and only if the start word ${\vdash}\,q_0\,h\,R\,{\dashv}$ of $l$
rewrites to the halting word ${\vdash}\,H\,{\dashv}$ in zero or more steps under the rules of $M$,
where $q_0$ is the default state, $h$ is the first letter of $l$ (the blank if $l$ is empty) and
$R$ is the rest of $l$.

Formalized by `Cslib.Decidability.TMRewriting.tm0HaltsOn_iff_derives`, a theorem declared in [CSLibExt/Computability/Decidability/PCPUndecidable.lean, line 603](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUndecidable.lean#L603). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#tm0-halts-on-iff-derives).

## Single-tape halting many-one reduces to string rewriting reachability

Let $M$ be a
single-tape Turing machine with finitely many states and tape symbols. Then the set of inputs on
which $M$ halts is many-one reducible to the set of instances $(R, x, y)$, where $R$ is a list of
rules and $x$, $y$ are words over the symbols of the rewriting system simulating $M$, such that
every rule of $R$ has a nonempty left side and a nonempty right side and $x$ rewrites to $y$ in
zero or more steps of $R$.

Formalized by `Cslib.Decidability.TMRewriting.manyOneReducible_tm0HaltsOn_sr`, a theorem declared in [CSLibExt/Computability/Decidability/PCPUndecidable.lean, line 636](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUndecidable.lean#L636). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#many-one-reducible-tm0-halts-on-sr).

## Reachability for string rewriting is undecidable

There is a finite alphabet $\alpha$,
with a primitive recursive coding of its letters by natural numbers, such that no multi-stack
Turing machine decides, for a finite list $R$ of rewriting rules over $\alpha$ and words $x$ and
$y$ over $\alpha$, whether every rule of $R$ has a nonempty left side and a nonempty right side
and $x$ rewrites to $y$ in zero or more steps of $R$.

Formalized by `Cslib.Decidability.exists_not_tm2Decidable_sr`, a theorem declared in [CSLibExt/Computability/Decidability/PCPUndecidable.lean, line 657](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUndecidable.lean#L657). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#exists-not-tm2-decidable-sr).

## MPCP is undecidable

There is a finite alphabet $\alpha$, with a primitive recursive
coding of its letters by natural numbers, such that no multi-stack Turing machine decides, for
a finite list $P$ of dominoes over $\alpha$, whether every domino of $P$ has a nonempty top and
a nonempty bottom and $P$ has a solution of the modified Post correspondence problem, that is,
a nonempty sequence of dominoes of $P$, repetitions allowed, that starts with the first domino
of $P$ and whose tops and bottoms concatenate to the same word.

Formalized by `Cslib.Decidability.exists_not_tm2Decidable_mpcp`, a theorem declared in [CSLibExt/Computability/Decidability/PCPUndecidable.lean, line 673](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUndecidable.lean#L673). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#exists-not-tm2-decidable-mpcp).

## The Post correspondence problem is undecidable

There is a finite alphabet $\alpha$, with
a primitive recursive coding of its letters by natural numbers, such that no multi-stack Turing
machine decides whether a finite list of dominoes over $\alpha$ has a solution, that is, a
nonempty sequence of dominoes of the list, repetitions allowed, whose tops and bottoms
concatenate to the same word.

Formalized by `Cslib.Decidability.exists_not_tm2Decidable_pcp`, a theorem declared in [CSLibExt/Computability/Decidability/PCPUndecidable.lean, line 681](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUndecidable.lean#L681). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#exists-not-tm2-decidable-pcp).

## Boolean test for control symbols

The Boolean function on the symbols of the rewriting
system simulating a single-tape Turing machine that is true on every state symbol and on the
halting symbol $H$, and false on every tape symbol and on the end markers $\vdash$ and $\dashv$.

Formalized by `Cslib.Decidability.TMRewriting.isCtlB`, a definition declared in [CSLibExt/Computability/Decidability/PCPUndecidable.lean, line 698](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUndecidable.lean#L698). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#is-ctl-b).

## Number of control symbols

The number of control symbols of a word $w$ over the symbols of
the rewriting system simulating a single-tape machine is the number of letters of $w$ that are
states or the halting symbol $H$.

Formalized by `Cslib.Decidability.TMRewriting.ctlCount`, a definition declared in [CSLibExt/Computability/Decidability/PCPUndecidable.lean, line 707](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUndecidable.lean#L707). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#ctl-count).

## A word with one control symbol splits at it

If a word $w$ over the symbols of the
rewriting system simulating a single-tape machine contains exactly one control symbol (a state
symbol or the halting symbol), then $w = p\,x\,s$ for a control symbol $x$ and words $p$ and
$s$ that contain no control symbol.

Formalized by `Cslib.Decidability.TMRewriting.exists_split_of_ctlCount_eq_one`, a theorem declared in [CSLibExt/Computability/Decidability/PCPUndecidable.lean, line 717](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUndecidable.lean#L717). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#exists-split-of-ctl-count-eq-one).

## Rewriting at a state symbol

Let $M$ be a single-tape Turing machine with finitely many
states and tape symbols, and let $\sqcup$ be its blank symbol. For words $u$, $v$ and a state $q$,
the successor of $u\,q\,v$ is defined as follows. If $v$ does not begin with a tape symbol, there
is none. If $v = a\,v'$ for a tape symbol $a$: when $M$ has no transition from $q$ reading $a$,
it is $u\,H\,v'$, where $H$ is the halting symbol; when $M$ writes $b$ and enters $q'$, it is
$u\,q'\,b\,v'$; when $M$ moves right and enters $q'$, it is $u\,a\,q'\,\sqcup \dashv v''$ if
$v' = {\dashv}\,v''$ for the right end marker $\dashv$, it is $u\,a\,q'\,c\,v''$ if
$v' = c\,v''$ for a tape symbol $c$, and there is none otherwise; when $M$ moves left and enters
$q'$, it is $u' \vdash q'\,\sqcup\,a\,v'$ if $u = u' \vdash$ for the left end marker $\vdash$, it
is $u'\,q'\,c\,a\,v'$ if $u = u'\,c$ for a tape symbol $c$, and there is none otherwise.

Formalized by `Cslib.Decidability.TMRewriting.nextState`, a definition declared in [CSLibExt/Computability/Decidability/PCPUndecidable.lean, line 739](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUndecidable.lean#L739). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#next-state).

## A rewrite at the control symbol

Let $M$ be a single-tape machine with finite tape
alphabet and finite set of states. Let $x$ be a control symbol (a state symbol or the halting
symbol $H$) and let $u$ and $v$ be words that contain no control symbol. If $u\,x\,v$ rewrites in
one step to $w'$ under the rules of $M$, then either $x$ is a state symbol $q$ and the successor of
$u\,q\,v$ under the rules for $q$ is defined and equals $w'$, or $x = H$ and either $u = u'\,c$ for
a word $u'$ and a tape symbol $c$ with $w' = u'\,H\,v$, or $v = c\,v'$ for a tape symbol $c$ and a
word $v'$ with $w' = u\,H\,v'$.

Formalized by `Cslib.Decidability.TMRewriting.step_result`, a theorem declared in [CSLibExt/Computability/Decidability/PCPUndecidable.lean, line 760](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUndecidable.lean#L760). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#step-result).

## Rewriting preserves the number of control symbols

Let $M$ be a single-tape Turing
machine with finitely many states and tape symbols, and call the states and the halting symbol
$H$ control symbols. If a word $w$ rewrites to $w'$ in one step of the rewriting system simulating
$M$, then $w$ and $w'$ contain the same number of control symbols.

Formalized by `Cslib.Decidability.TMRewriting.ctlCount_eq_of_step`, a theorem declared in [CSLibExt/Computability/Decidability/PCPUndecidable.lean, line 798](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUndecidable.lean#L798). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#ctl-count-eq-of-step).

## Local confluence on words with one control symbol

Let $M$ be a single-tape machine with
finite tape alphabet and finite set of states, and let $w$ be a word over the symbols of its
rewriting system that contains exactly one control symbol (a state symbol or the halting symbol).
If $w$ rewrites in one step to $w_1$ and in one step to $w_2$ under the rules of $M$, then there is
a word $d$ such that $w_1$ rewrites to $d$ in at most one step and $w_2$ rewrites to $d$ in zero or
more steps.

Rewriting at a state symbol is deterministic, and the two erasures at the halting symbol commute.

Formalized by `Cslib.Decidability.TMRewriting.step_confluent`, a theorem declared in [CSLibExt/Computability/Decidability/PCPUndecidable.lean, line 810](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUndecidable.lean#L810). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#step-confluent).

## The halting word is irreducible

Let $M$ be a single-tape Turing machine with finitely
many states and tape symbols. There is no word $w$ such that the halting word $\vdash H \dashv$
rewrites to $w$ in one step of the rewriting system simulating $M$.

Formalized by `Cslib.Decidability.TMRewriting.not_step_haltWord`, a theorem declared in [CSLibExt/Computability/Decidability/PCPUndecidable.lean, line 848](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUndecidable.lean#L848). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#not-step-halt-word).

## Rewrites from words with one control symbol

Let $M$ be a single-tape Turing machine with
finitely many states and tape symbols, and call the states and the halting symbol $H$ control
symbols. A word $w$ rewrites to $w'$ by a controlled step when $w$ contains exactly one control
symbol and $w$ rewrites to $w'$ in one step of the rewriting system simulating $M$.

Formalized by `Cslib.Decidability.TMRewriting.CtlStep`, a definition declared in [CSLibExt/Computability/Decidability/PCPUndecidable.lean, line 873](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUndecidable.lean#L873). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#ctl-step).

## Thue equivalence from a word with one control symbol uses only controlled steps

Let $M$ be
a single-tape Turing machine with finitely many states and tape symbols, and call the states and
the halting symbol $H$ control symbols. Suppose $w$ contains exactly one control symbol, and $w$
and $w'$ are equivalent under the equivalence relation generated by one-step rewriting in the
rewriting system simulating $M$. Then $w$ and $w'$ are equivalent under the equivalence relation
generated by the one-step rewrites from words with exactly one control symbol.

Formalized by `Cslib.Decidability.TMRewriting.eqvGen_ctlStep`, a theorem declared in [CSLibExt/Computability/Decidability/PCPUndecidable.lean, line 876](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUndecidable.lean#L876). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#eqv-gen-ctl-step).

## The rewrites from words with one control symbol are confluent

Let $M$ be a single-tape
Turing machine with finitely many states and tape symbols, and call the states and the halting
symbol $H$ control symbols. Consider the relation in which a word $w$ with exactly one control
symbol rewrites to $w'$ by one step of the rewriting system simulating $M$. This relation is
confluent: if $w$ rewrites in zero or more such steps to both $w_1$ and $w_2$, then $w_1$ and
$w_2$ both rewrite in zero or more such steps to a common word.

Formalized by `Cslib.Decidability.TMRewriting.confluent_ctlStep`, a theorem declared in [CSLibExt/Computability/Decidability/PCPUndecidable.lean, line 892](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUndecidable.lean#L892). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#confluent-ctl-step).

## A single-tape machine halts iff its start word is Thue equivalent to the halting word

Let
$M$ be a single-tape Turing machine with finitely many states and tape symbols, write $\vdash$ and
$\dashv$ for the left and right end markers and $H$ for the halting symbol, and let $l$ be an input
word of tape symbols. Then $M$ halts on $l$ if and only if the start word of $l$ and the halting
word ${\vdash}\,H\,{\dashv}$ are equivalent under the reflexive, symmetric and transitive closure
of one-step rewriting by the rewriting system simulating $M$.

Formalized by `Cslib.Decidability.TMRewriting.tm0HaltsOn_iff_eqvGen`, a theorem declared in [CSLibExt/Computability/Decidability/PCPUndecidable.lean, line 911](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUndecidable.lean#L911). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#tm0-halts-on-iff-eqv-gen).

## Single-tape halting many-one reduces to the word problem of a fixed Thue system

Let $M$
be a single-tape Turing machine with finitely many states and tape symbols, and let $R_M$ be the
rewriting system simulating $M$. Then the set of inputs on which $M$ halts is many-one reducible
to the set of pairs $(x, y)$ of words over the symbols of $R_M$ that are equivalent under the
reflexive, symmetric and transitive closure of one-step rewriting by $R_M$.

Formalized by `Cslib.Decidability.TMRewriting.manyOneReducible_tm0HaltsOn_eqvGen`, a theorem declared in [CSLibExt/Computability/Decidability/PCPUndecidable.lean, line 923](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUndecidable.lean#L923). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#many-one-reducible-tm0-halts-on-eqv-gen).

## Some finite Thue system has an undecidable word problem

(Post, Markov) There are a
finite alphabet $\alpha$, with a primitive recursive coding of its letters by natural numbers,
and a finite list $R$ of rewriting rules over $\alpha$ such that no multi-stack Turing machine
decides, for words $x$ and $y$ over $\alpha$, whether $x$ and $y$ are equivalent under the
reflexive, symmetric and transitive closure of one-step rewriting by $R$.

Formalized by `Cslib.Decidability.exists_not_tm2Decidable_eqvGen`, a theorem declared in [CSLibExt/Computability/Decidability/PCPUndecidable.lean, line 937](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUndecidable.lean#L937). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#exists-not-tm2-decidable-eqv-gen).

## The uniform word problem for Thue systems is undecidable

There is a finite alphabet
$\alpha$, with a primitive recursive coding of its letters by natural numbers, such that no
multi-stack Turing machine decides, for a finite list $R$ of rewriting rules over $\alpha$ and
words $x$ and $y$ over $\alpha$, whether $x$ and $y$ are equivalent under the reflexive,
symmetric and transitive closure of one-step rewriting by $R$.

Formalized by `Cslib.Decidability.exists_not_tm2Decidable_thueWP`, a theorem declared in [CSLibExt/Computability/Decidability/PCPUndecidable.lean, line 954](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPUndecidable.lean#L954). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#exists-not-tm2-decidable-thue-wp).

## Image of a PCP instance under a word map

Given a map $f$ from words over $\alpha$
to words over $\beta$ and a list $P$ of dominoes over $\alpha$, the image of $P$ under $f$ is the
list of dominoes over $\beta$ obtained by replacing each domino $(u, v)$ of $P$ by $(f(u), f(v))$,
in the same order.

Formalized by `Cslib.Decidability.Post.mapInstance`, a definition declared in [CSLibExt/Computability/Decidability/PCPBinary.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPBinary.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#map-instance).

## An injective word homomorphism preserves and reflects PCP solvability

Let $h$ map each
letter of $\alpha$ to a word over $\beta$, and extend it to words by
$h(a_1 \cdots a_n) = h(a_1) \cdots h(a_n)$. If this extension is injective on words over $\alpha$,
then for every list $P$ of dominoes over $\alpha$, the list obtained from $P$ by replacing each
domino $(u, v)$ by $(h(u), h(v))$ has a PCP solution if and only if $P$ has a PCP solution.

Formalized by `Cslib.Decidability.Post.pcp_map_iff`, a theorem declared in [CSLibExt/Computability/Decidability/PCPBinary.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPBinary.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#pcp-map-iff).

## Unary code of a letter

Given an indexing $e$ assigning a natural number to each letter of
$\alpha$, the unary code of a letter $a$ is the Boolean word consisting of $e(a)$ copies of
$\mathrm{true}$ followed by one $\mathrm{false}$; writing $1$ for true and $0$ for false, it is
$1^{e(a)} 0$.

Formalized by `Cslib.Decidability.Post.unaryCode`, a definition declared in [CSLibExt/Computability/Decidability/PCPBinary.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPBinary.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#unary-code).

## The unary code of an injective indexing is uniquely decodable

Let $e$ be an injective map
from $\alpha$ to the natural numbers, and let $c(a)$ be the unary code of a letter $a$: $e(a)$
copies of $\mathrm{true}$ followed by one $\mathrm{false}$. Then the map sending a word
$a_1 \cdots a_n$ over $\alpha$ to the Boolean word $c(a_1) \cdots c(a_n)$ is injective.

Formalized by `Cslib.Decidability.Post.unaryHom_injective`, a theorem declared in [CSLibExt/Computability/Decidability/PCPBinary.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPBinary.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#unary-hom-injective).

## PCP over a finite alphabet many-one reduces to PCP over the binary alphabet

Let $\alpha$
be a finite alphabet with a primitive recursive encoding of its letters as natural numbers. Then
the Post correspondence problem over $\alpha$ is many-one reducible to the Post correspondence
problem over the two-letter alphabet of Booleans $\mathrm{true}$ and $\mathrm{false}$: there is a
computable map $f$ sending each finite list $P$ of dominoes over $\alpha$ to a finite list $f(P)$
of dominoes over the Booleans such that $P$ has a PCP solution if and only if $f(P)$ has a PCP
solution.

Formalized by `Cslib.Decidability.Post.manyOneReducible_pcp_bool`, a theorem declared in [CSLibExt/Computability/Decidability/PCPBinary.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPBinary.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#many-one-reducible-pcp-bool).

## The Post correspondence problem is undecidable over the binary alphabet

The Post
correspondence problem over the two-letter alphabet of Booleans $\mathrm{true}$ and
$\mathrm{false}$, that is, the property of a finite list $P$ of dominoes over the Booleans of
having a PCP solution, is not decidable by a multi-stack Turing machine: no multi-stack machine
computes a total function $g : \mathbb{N} \to \mathbb{N}$ such that, for every such $P$ with
natural-number encoding $n_P$, $g(n_P) = 1$ exactly when $P$ has a PCP solution.

Formalized by `Cslib.Decidability.not_tm2Decidable_pcp_bool`, a theorem declared in [CSLibExt/Computability/Decidability/PCPBinary.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/PCPBinary.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html#not-tm2-decidable-pcp-bool).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Post correspondence problem](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/undecidable-problems/post-correspondence-problem)
