---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.bandedFrom, Cslib.Algorithms.Lean.IsBanded, Cslib.Algorithms.Lean.abs_le_of_between, Cslib.Algorithms.Lean.abs_le_of_between_add, Cslib.Algorithms.Lean.bandedFrom_final, Cslib.Algorithms.Lean.isBanded_length_diff, Cslib.Algorithms.Lean.diagAlign, Cslib.Algorithms.Lean.isAlignment_diagAlign
statement: formalized
proof: formalized
---

# Banded sequence alignment

23 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/banded-sequence-alignment/index.html).

## Band check from a starting offset

Let $w \in \mathbb{N}$ be a band width. For natural
numbers $i$, $j$ and an alignment $A$, the band check of $A$ with width $w$ from offset $(i, j)$
is true exactly when every prefix $P$ of $A$ (including the empty prefix and $A$ itself)
satisfies $|(i + p) - (j + q)| \le w$, where $p$ and $q$ are the numbers of columns of $P$
whose first, respectively second, entry is present.

Formalized by `Cslib.Algorithms.Lean.bandedFrom`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/BandedAlignment.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/BandedAlignment.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/banded-sequence-alignment/index.html#banded-from).

## Banded alignments

Let $w \in \mathbb{N}$. An alignment $A$ is banded with width $w$ when,
for every prefix of $A$ (including the empty prefix and $A$ itself), the number of columns of
that prefix with a letter in the first row and the number with a letter in the second row
differ by at most $w$.

Formalized by `Cslib.Algorithms.Lean.IsBanded`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/BandedAlignment.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/BandedAlignment.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/banded-sequence-alignment/index.html#is-banded).

## Bound at an intermediate point, difference form

For integers $a$, $d$, $t$ and $w$,
if $|a| \le w$, $|a - d| \le w$ and $0 \le t \le d$, then $|a - t| \le w$.

Used for the gap phases of an alignment, where the offset difference interpolates between its
start and end values.

Formalized by `Cslib.Algorithms.Lean.abs_le_of_between`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/BandedAlignment.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/BandedAlignment.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/banded-sequence-alignment/index.html#abs-le-of-between).

## Bound at an intermediate point, sum form

For integers $a$, $d$, $t$ and $w$, if
$|a| \le w$, $|a + d| \le w$ and $0 \le t \le d$, then $|a + t| \le w$.

Used for runs of alignment columns that consume only letters of the first sequence, where the
offset difference grows.

Formalized by `Cslib.Algorithms.Lean.abs_le_of_between_add`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/BandedAlignment.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/BandedAlignment.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/banded-sequence-alignment/index.html#abs-le-of-between-add).

## A passing band check bounds the final offset

Let $w, i, j \in \mathbb{N}$ and let
$A$ be an alignment. If the band check of $A$ with width $w$ from offset $(i, j)$ is true, then
$|(i + p) - (j + q)| \le w$, where $p$ and $q$ are the numbers of columns of $A$ whose first,
respectively second, entry is present.

Formalized by `Cslib.Algorithms.Lean.bandedFrom_final`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/BandedAlignment.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/BandedAlignment.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/banded-sequence-alignment/index.html#banded-from-final).

## Banded alignments force close lengths

Let $w \in \mathbb{N}$. If $A$ is a valid alignment
of sequences $x$ and $y$ and $A$ is banded with width $w$, then the lengths of $x$ and $y$ differ
by at most $w$, that is $\bigl| |x| - |y| \bigr| \le w$.

Formalized by `Cslib.Algorithms.Lean.isBanded_length_diff`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/BandedAlignment.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/BandedAlignment.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/banded-sequence-alignment/index.html#is-banded-length-diff).

## Diagonal alignment

For sequences $x = x_1 \dots x_m$ and $y = y_1 \dots y_n$, let
$k = \min(m, n)$. The diagonal alignment of $x$ and $y$ consists of the columns
$(x_1, y_1), \dots, (x_k, y_k)$, which pair letters by position whether or not they are equal,
followed by one column for each remaining letter of the longer sequence, in order, pairing that
letter with a gap.

Formalized by `Cslib.Algorithms.Lean.diagAlign`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/BandedAlignment.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/BandedAlignment.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/banded-sequence-alignment/index.html#diag-align).

## The diagonal alignment is a valid alignment

For all sequences $x$ and $y$, the diagonal
alignment of $x$ and $y$ is a valid alignment of $x$ and $y$: none of its columns consists of two
gaps, and deleting the gaps from its first and second rows gives $x$ and $y$ respectively.

Formalized by `Cslib.Algorithms.Lean.isAlignment_diagAlign`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/BandedAlignment.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/BandedAlignment.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/banded-sequence-alignment/index.html#is-alignment-diag-align).

## Columns using only the second sequence stay in the band

Let $w, i, j \in \mathbb{N}$,
let $y$ be a list of length $n$, and let $A$ be the alignment with one column for each element
$b$ of $y$, in order, with empty first entry and second entry $b$. If $|i - j| \le w$ and
$|i - (j + n)| \le w$, then the band check of $A$ with width $w$ from offset
$(i, j)$ is true.

Formalized by `Cslib.Algorithms.Lean.bandedFrom_map_gapY`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/BandedAlignment.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/BandedAlignment.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/banded-sequence-alignment/index.html#banded-from-map-gap-y).

## Columns using only the first sequence stay in the band

Let $w, i, j \in \mathbb{N}$,
let $x$ be a list of length $n$, and let $A$ be the alignment with one column for each element
$a$ of $x$, in order, with first entry $a$ and empty second entry. If $|i - j| \le w$ and
$|(i + n) - j| \le w$, then the band check of $A$ with width $w$ from offset
$(i, j)$ is true.

Formalized by `Cslib.Algorithms.Lean.bandedFrom_map_gapX`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/BandedAlignment.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/BandedAlignment.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/banded-sequence-alignment/index.html#banded-from-map-gap-x).

## The diagonal alignment stays in the band

Let $w, i, j \in \mathbb{N}$ and let $x$, $y$
be lists of lengths $m$ and $n$. If $|i - j| \le w$ and $|(i + m) - (j + n)| \le w$, then the
band check of the diagonal alignment of $x$ and $y$ with width $w$ from offset $(i, j)$ is true.

The match phase keeps the offset difference and the gap phases interpolate it.

Formalized by `Cslib.Algorithms.Lean.bandedFrom_diagAlign`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/BandedAlignment.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/BandedAlignment.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/banded-sequence-alignment/index.html#banded-from-diag-align).

## The diagonal alignment is banded

Let $w \in \mathbb{N}$. If two sequences $x$ and $y$
have lengths differing by at most $w$, that is $\bigl| |x| - |y| \bigr| \le w$, then the diagonal
alignment of $x$ and $y$ is banded with width $w$.

Formalized by `Cslib.Algorithms.Lean.isBanded_diagAlign`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/BandedAlignment.lean, line 283](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/BandedAlignment.lean#L283). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/banded-sequence-alignment/index.html#is-banded-diag-align).

## Banded alignment score

Fix a substitution score $\sigma$, assigning an integer
$\sigma(a, b)$ to each pair of letters $a$, $b$, an integer gap score $g$ and a band width
$w \in \mathbb{N}$. The banded alignment score of two sequences $x$ and $y$ is the maximum, over
all valid alignments of $x$ and $y$ that are banded with width $w$, of the (integer) alignment
score with respect to $\sigma$ and $g$. It has no value (it is the empty optional value) when no
such alignment exists.

Formalized by `Cslib.Algorithms.Lean.bandedScore`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/BandedAlignment.lean, line 292](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/BandedAlignment.lean#L292). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/banded-sequence-alignment/index.html#banded-score).

## The banded score is at most the Needleman–Wunsch score

Let $\sigma$ be an integer
substitution score on an alphabet, $g$ an integer gap score and $w \in \mathbb{N}$ a band
width. For sequences $x$ and $y$ over the alphabet and an integer $s$, if the banded score of
$x$ and $y$ (under $\sigma$, $g$ and width $w$) is defined and equals $s$, then $s$ is at most
the Needleman–Wunsch score of $x$ and $y$.

Formalized by `Cslib.Algorithms.Lean.bandedScore_le_nwScore`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/BandedAlignment.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/BandedAlignment.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/banded-sequence-alignment/index.html#banded-score-le-nw-score).

## Banded alignment is exact when some optimal alignment is banded

Let $\sigma$ be an
integer substitution score on an alphabet, $g$ an integer gap score and $w \in \mathbb{N}$ a
band width. For sequences $x$ and $y$ over the alphabet, if some alignment of $x$ and $y$ is
banded with width $w$ and has score (under $\sigma$ and $g$) equal to the Needleman–Wunsch
score of $x$ and $y$, then the banded score of $x$ and $y$ (under $\sigma$, $g$ and width $w$)
is defined and equals their Needleman–Wunsch score.

Formalized by `Cslib.Algorithms.Lean.bandedScore_eq_nwScore_of_banded_optimal`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/BandedAlignment.lean, line 311](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/BandedAlignment.lean#L311). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/banded-sequence-alignment/index.html#banded-score-eq-nw-score-of-banded-optim).

## No banded score when the lengths differ by more than the band width

Let $\sigma$ be
an integer substitution score on an alphabet, $g$ an integer gap score and $w \in \mathbb{N}$ a
band width. For sequences $x$ and $y$ over the alphabet, of lengths $m$ and $n$, with
$w < |m - n|$, the banded score of $x$ and $y$ (under $\sigma$, $g$ and width $w$) is undefined:
no alignment of $x$ and $y$ is banded with width $w$.

Formalized by `Cslib.Algorithms.Lean.bandedScore_none_of_length_diff_gt`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/BandedAlignment.lean, line 349](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/BandedAlignment.lean#L349). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/banded-sequence-alignment/index.html#banded-score-none-of-length-diff-gt).

## The banded score is defined when the lengths are close

Fix a substitution score
$\sigma$, assigning an integer $\sigma(a, b)$ to each pair of letters $a$, $b$, an integer gap
score $g$ and a band width $w \in \mathbb{N}$. If two sequences $x$ and $y$ have lengths differing
by at most $w$, that is $\bigl| |x| - |y| \bigr| \le w$, then the banded alignment score of $x$
and $y$ (for $\sigma$, $g$ and $w$) is defined: it equals some integer $s$.

Formalized by `Cslib.Algorithms.Lean.bandedScore_some_of_length_diff_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/BandedAlignment.lean, line 368](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/BandedAlignment.lean#L368). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/banded-sequence-alignment/index.html#banded-score-some-of-length-diff-le).

## Number of gap columns of an alignment

The number of gap columns of an alignment: columns with exactly one letter.

Formalized by `Cslib.Algorithms.Lean.gapColumns`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/BandLemma.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/BandLemma.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/banded-sequence-alignment/index.html#gap-columns).

## An alignment with few gap columns stays in the band from its start

Along every prefix, the offset difference is at most the starting difference plus the number
of gap columns: an alignment starting at `(i, j)` stays in the band of width `w` as soon as
`|i - j| + gapColumns A ≤ w`.

Formalized by `Cslib.Algorithms.Lean.bandedFrom_of_abs_add_gapColumns_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/BandLemma.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/BandLemma.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/banded-sequence-alignment/index.html#banded-from-of-abs-add-gap-columns-le).

## An alignment with at most w gap columns is w-banded

An alignment with at most `w` gap columns is `w`-banded.

Formalized by `Cslib.Algorithms.Lean.isBanded_of_gapColumns_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/BandLemma.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/BandLemma.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/banded-sequence-alignment/index.html#is-banded-of-gap-columns-le).

## Alignment score is at most minus the number of gap columns

With nonpositive substitution scores and gap score at most `-1`, an alignment scores at most
minus its number of gap columns.

Formalized by `Cslib.Algorithms.Lean.alignmentScore_le_neg_gapColumns`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/BandLemma.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/BandLemma.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/banded-sequence-alignment/index.html#alignment-score-le-neg-gap-columns).

## The band lemma

**The band lemma** (Ukkonen 1985): with nonpositive substitution scores and gap score at
most `-1`, every alignment scoring at least `-w` (cost at most `w`) is `w`-banded.

Formalized by `Cslib.Algorithms.Lean.isBanded_of_neg_le_alignmentScore`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/BandLemma.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/BandLemma.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/banded-sequence-alignment/index.html#is-banded-of-neg-le-alignment-score).

## The banded optimum is exact

**The banded optimum is exact** when the optimal score is at least `-w` (optimal cost at
most `w`), for nonpositive substitution scores and gap score at most `-1`: some optimal
alignment exists and, by the band lemma, it is `w`-banded.

Formalized by `Cslib.Algorithms.Lean.bandedScore_eq_nwScore_of_neg_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/BandLemma.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/BandLemma.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/banded-sequence-alignment/index.html#banded-score-eq-nw-score-of-neg-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Banded sequence alignment](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/banded-sequence-alignment/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/bioinformatics/sequence-alignment/banded-sequence-alignment)
