---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.Alignment, Cslib.Algorithms.Lean.IsAlignment, Cslib.Algorithms.Lean.columnScore, Cslib.Algorithms.Lean.alignmentScore, Cslib.Algorithms.Lean.isAlignment_append, Cslib.Algorithms.Lean.nwScoreAux, Cslib.Algorithms.Lean.nwScore, Cslib.Algorithms.Lean.nwScore_nil_left
statement: formalized
proof: formalized
---

# Pairwise sequence alignment

59 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html).

## Alignment

An alignment over an alphabet $\alpha$ is a finite list of columns, where
each column is a pair $(u, v)$ and each of $u$ and $v$ is either a letter of $\alpha$ or a gap.

Whether an alignment is valid for two given sequences is a separate condition.

Formalized by `Cslib.Algorithms.Lean.Alignment`, an abbreviation declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#alignment).

## Valid alignment of two sequences

A list $A$ of columns, each a pair of optional letters,
is an alignment of sequences $x$ and $y$ when no column has both entries empty, the letters
present in the first entries of the columns, read in order, form $x$, and the letters present in
the second entries, read in order, form $y$.

Formalized by `Cslib.Algorithms.Lean.IsAlignment`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#is-alignment).

## Score of an alignment column

Given a substitution score $\sigma$, which assigns an
integer $\sigma(a, b)$ to all letters $a, b \in \alpha$, and a gap score $g \in \mathbb{Z}$, a
column pairing letters $a$ and $b$ scores $\sigma(a, b)$, a column pairing a letter with a gap
(on either side) scores $g$, and a column with a gap on both sides scores $0$.

Formalized by `Cslib.Algorithms.Lean.columnScore`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#column-score).

## Score of an alignment

Given a substitution score $\sigma$, which assigns an integer
$\sigma(a, b)$ to all letters $a, b \in \alpha$, and a gap score $g \in \mathbb{Z}$, the score of
an alignment $A$ over $\alpha$ is the sum, over all columns of $A$, of the score of the column
with respect to $\sigma$ and $g$.

Formalized by `Cslib.Algorithms.Lean.alignmentScore`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#alignment-score).

## Concatenation of alignments

If $A_1$ is an alignment of sequences $x_1$ and $y_1$, and
$A_2$ is an alignment of sequences $x_2$ and $y_2$, then the concatenation of $A_1$ and $A_2$ is
an alignment of the concatenation of $x_1$ and $x_2$ and the concatenation of $y_1$ and $y_2$.

Formalized by `Cslib.Algorithms.Lean.isAlignment_append`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#is-alignment-append).

## Fuel-bounded Needleman–Wunsch recursion

Fix a substitution score
$\sigma : \alpha \to \alpha \to \mathbb{Z}$ and a gap score $g \in \mathbb{Z}$, and write $|x|$ for
the length of a sequence $x$ and $ax$ for the sequence with first element $a$ followed by $x$.
For a fuel $n \in \mathbb{N}$ and sequences $x, y$ over $\alpha$, the value
$N_n(x, y) \in \mathbb{Z}$ is defined by $N_0(x, y) = 0$, by $N_{n+1}(x, y) = g\,|y|$ if $x$ is
empty and $N_{n+1}(x, y) = g\,|x|$ if $y$ is empty, and by

$$N_{n+1}(ax, by) = \max\bigl(N_n(x, y) + \sigma(a, b),\ N_n(x, by) + g,\ N_n(ax, y) + g\bigr).$$

The Needleman–Wunsch score of $x$ and $y$ is $N_{|x|+|y|}(x, y)$; this fuel suffices because every
recursive call shortens the pair. This is an exponential-time specification, not a memoized
table.

Formalized by `Cslib.Algorithms.Lean.nwScoreAux`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#nw-score-aux).

## Needleman–Wunsch score

Given a type $\alpha$, a substitution score
$\sigma : \alpha \to \alpha \to \mathbb{Z}$ and a gap score $g \in \mathbb{Z}$, the
Needleman–Wunsch score $\mathrm{NW}(xs, ys)$ of two lists over $\alpha$ is defined by recursion
on their total length: if one of the lists is empty, it is $g$ times the length of the other;
and for lists $a\,xs$ and $b\,ys$ with heads $a$, $b$ and tails $xs$, $ys$,

$$\mathrm{NW}(a\,xs, b\,ys) = \max\bigl(\mathrm{NW}(xs, ys) + \sigma(a, b),
\ \mathrm{NW}(xs, b\,ys) + g,\ \mathrm{NW}(a\,xs, ys) + g\bigr).$$

By the Needleman–Wunsch optimality theorem, this is the optimal global alignment score of the
two lists.

Formalized by `Cslib.Algorithms.Lean.nwScore`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#nw-score).

## Aligning the empty sequence with a sequence

For every substitution score
$\sigma : \alpha \to \alpha \to \mathbb{Z}$, gap score $g \in \mathbb{Z}$ and sequence $y$ over
$\alpha$ of length $|y|$, the Needleman–Wunsch score of the empty sequence and $y$ with respect to
$\sigma$ and $g$ is $g\,|y|$: one gap per letter.

Formalized by `Cslib.Algorithms.Lean.nwScore_nil_left`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#nw-score-nil-left).

## Aligning a sequence with the empty sequence

For every substitution score
$\sigma : \alpha \to \alpha \to \mathbb{Z}$, gap score $g \in \mathbb{Z}$ and sequence $x$ over
$\alpha$ of length $|x|$, the Needleman–Wunsch score of $x$ and the empty sequence with respect to
$\sigma$ and $g$ is $g\,|x|$: one gap per letter.

Formalized by `Cslib.Algorithms.Lean.nwScore_nil_right`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#nw-score-nil-right).

## The Needleman–Wunsch recurrence

Let $\sigma : \alpha \to \alpha \to \mathbb{Z}$ be a
substitution score and $g \in \mathbb{Z}$ a gap score, and write $N(x, y)$ for the
Needleman–Wunsch score of sequences $x, y$ over $\alpha$ with respect to $\sigma$ and $g$. For all
letters $a, b \in \alpha$ and sequences $x, y$, writing $ax$ for the sequence with first element
$a$ followed by $x$,

$$N(ax, by) = \max\bigl(N(x, y) + \sigma(a, b),\ N(x, by) + g,\ N(ax, y) + g\bigr).$$

Formalized by `Cslib.Algorithms.Lean.nwScore_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#nw-score-eq).

## Fuel-bounded enumeration of alignments

Given a fuel $n \in \mathbb{N}$ and sequences
$x$ and $y$ over $\alpha$, this lists alignments column by column from the front. With fuel $0$
the list is empty. With fuel $n + 1$: two empty sequences give the single empty alignment; if
only $y$ is nonempty, with first letter $b$ and rest $y'$, each alignment of $x$ and $y'$ with
fuel $n$ is preceded by the column pairing a gap with $b$; if only $x$ is nonempty, with first
letter $a$ and rest $x'$, each alignment of $x'$ and $y$ with fuel $n$ is preceded by the
column pairing $a$ with a gap; and if both are nonempty, $x$ with first letter $a$ and rest $x'$
and $y$ with first letter $b$ and rest $y'$, the list consists of the alignments of $x'$ and
$y'$ preceded by the column $(a, b)$, then those of $x'$ and $y$ preceded by the column pairing
$a$ with a gap, then those of $x$ and $y'$ preceded by the column pairing a gap with $b$, each
computed with fuel $n$.

With fuel at least $|x| + |y| + 1$ the fuel never runs out before both sequences are used up;
with less fuel some alignments are missing from the list.

Formalized by `Cslib.Algorithms.Lean.alignmentsAux`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#alignments-aux).

## The list of all alignments

For sequences $x$ and $y$ over $\alpha$, this is the list
produced by the fuel-bounded enumeration of alignments of $x$ and $y$ with fuel
$|x| + |y| + 1$.

This fuel suffices: an alignment belongs to the list exactly when it is a valid alignment of
$x$ and $y$.

Formalized by `Cslib.Algorithms.Lean.alignments`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#alignments).

## The enumerated alignments are exactly the valid ones

For sequences $x$ and $y$ and a
list $A$ of columns, $A$ occurs in the enumerated list of all alignments of $x$ and $y$ if and
only if $A$ is an alignment of $x$ and $y$.

Formalized by `Cslib.Algorithms.Lean.mem_alignments`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 563](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L563). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#mem-alignments).

## Needleman–Wunsch is optimal

Let $\sigma : \alpha \to \alpha \to \mathbb{Z}$ be a
substitution score and $g \in \mathbb{Z}$ a gap score. For all sequences $x$ and $y$ over
$\alpha$ and every valid alignment $A$ of $x$ and $y$, the score of $A$ with respect to
$\sigma$ and $g$ is at most the Needleman–Wunsch score of $x$ and $y$.

Formalized by `Cslib.Algorithms.Lean.alignmentScore_le_nwScore`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 953](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L953). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#alignment-score-le-nw-score).

## Needleman–Wunsch is attained

Let $\sigma : \alpha \to \alpha \to \mathbb{Z}$ be a
substitution score and $g \in \mathbb{Z}$ a gap score. For all sequences $x$ and $y$ over
$\alpha$ there is a valid alignment $A$ of $x$ and $y$ whose score with respect to $\sigma$ and
$g$ equals the Needleman–Wunsch score of $x$ and $y$.

Formalized by `Cslib.Algorithms.Lean.exists_alignmentScore_eq_nwScore`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 959](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L959). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#exists-alignment-score-eq-nw-score).

## Fuel-bounded Smith–Waterman recursion

Fix a substitution score
$\sigma : \alpha \to \alpha \to \mathbb{Z}$ and a gap score $g \in \mathbb{Z}$, and write $ax$ for
the sequence with first element $a$ followed by $x$. For a fuel $n \in \mathbb{N}$ and sequences
$x, y$ over $\alpha$, the value $F_n(x, y) \in \mathbb{Z}$ is defined by $F_0(x, y) = 0$, by
$F_{n+1}(x, y) = 0$ if $x$ or $y$ is empty, and by

$$F_{n+1}(ax, by) = \max\bigl(0,\ F_n(x, y) + \sigma(a, b),\ F_n(x, by) + g,
\ F_n(ax, y) + g\bigr).$$

This is an exponential-time specification, not a memoized table.

Formalized by `Cslib.Algorithms.Lean.swCellFront`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 973](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L973). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#sw-cell-front).

## The terminal Smith–Waterman cell

Given a substitution score $\sigma(a, b) \in \mathbb{Z}$
for letters $a, b$ and a gap score $g \in \mathbb{Z}$, and writing $sc$ for a sequence $s$
followed by a letter $c$, the terminal Smith–Waterman cell $H(x, y)$ of two sequences $x$ and
$y$ is the integer defined by $H(x, y) = 0$ when $x$ or $y$ is empty, and

$$H(xa, yb) = \max\bigl(0,\ H(x, y) + \sigma(a, b),\ H(x, yb) + g,\ H(xa, y) + g\bigr)$$

for all sequences $x, y$ and letters $a, b$. It is the entry $H(|x|, |y|)$ of the
Smith–Waterman dynamic-programming table.

For $g \le 0$ it equals the maximum Needleman–Wunsch score over pairs of suffixes of $x$ and $y$;
for $g > 0$ it can be strictly smaller (for one-letter sequences with $\sigma = -100$ and
$g = 1$ the cell is $1$, while the alignment with two gap columns scores $2$). It is not the
optimal local alignment score over all positions; that is the Smith–Waterman score, the maximum
of this cell over all pairs of prefixes.

Formalized by `Cslib.Algorithms.Lean.swCellScore`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 988](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L988). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#sw-cell-score).

## The terminal Smith–Waterman cell is nonnegative

For every substitution score $\sigma$,
every gap score $g$ and all sequences $x$ and $y$, the terminal Smith–Waterman cell $H(x, y)$
satisfies $H(x, y) \ge 0$.

Formalized by `Cslib.Algorithms.Lean.swCellScore_nonneg`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 1036](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L1036). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#sw-cell-score-nonneg).

## The terminal cell vanishes when the first sequence is empty

For a substitution score
$\sigma$, a gap score $g$ and every sequence $y$, the terminal Smith–Waterman cell of the empty
sequence and $y$ is $0$.

Formalized by `Cslib.Algorithms.Lean.swCellScore_nil_left`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 1055](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L1055). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#sw-cell-score-nil-left).

## The terminal cell vanishes when the second sequence is empty

For a substitution score
$\sigma$, a gap score $g$ and every sequence $x$, the terminal Smith–Waterman cell of $x$ and the
empty sequence is $0$.

Formalized by `Cslib.Algorithms.Lean.swCellScore_nil_right`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 1061](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L1061). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#sw-cell-score-nil-right).

## The Smith–Waterman recurrence

Let $\sigma$ be a substitution score and $g$ a gap score,
and for a sequence $s$ and a letter $c$ write $sc$ for $s$ followed by $c$. For all sequences
$x$ and $y$ and all letters $a$ and $b$, the terminal Smith–Waterman cell $H$ satisfies

$$H(xa, yb) = \max\bigl(0,\ H(x, y) + \sigma(a, b),\ H(x, yb) + g,\ H(xa, y) + g\bigr).$$

Formalized by `Cslib.Algorithms.Lean.swCellScore_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 1067](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L1067). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#sw-cell-score-eq).

## Suffixes of a list with an element appended

If $s$ is a suffix of the list obtained by
appending an element $a$ at the end of a list $xs$, then either $s$ is empty, or there is a
suffix $s'$ of $xs$ such that $s$ is $s'$ with $a$ appended at the end.

Formalized by `Cslib.Algorithms.Lean.suffix_of_snoc`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 1106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L1106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#suffix-of-snoc).

## Appending an element preserves suffixes

If a list $s$ is a suffix of a list $xs$,
then for every element $a$, the list $s$ with $a$ appended at the end is a suffix of $xs$ with
$a$ appended at the end.

Formalized by `Cslib.Algorithms.Lean.suffix_append_snoc`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 1119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L1119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#suffix-append-snoc).

## Reversing an alignment

For a list of columns $A$ and sequences $x$ and $y$, $A$ is an
alignment of the reversal of $x$ and the reversal of $y$ if and only if the reversal of $A$ (its
columns in reverse order) is an alignment of $x$ and $y$.

Formalized by `Cslib.Algorithms.Lean.isAlignment_reverse`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 1124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L1124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#is-alignment-reverse).

## Reversal preserves alignment score

For every substitution score
$\sigma : \alpha \to \alpha \to \mathbb{Z}$, gap score $g \in \mathbb{Z}$ and alignment $A$, the
alignment obtained by listing the columns of $A$ in reverse order has the same score as $A$.

Formalized by `Cslib.Algorithms.Lean.alignmentScore_reverse`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 1141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L1141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#alignment-score-reverse).

## Needleman–Wunsch is reversal-invariant

Reversing both sequences preserves the
optimal global score.

Formalized by `Cslib.Algorithms.Lean.nwScore_reverse`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 1147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L1147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#nw-score-reverse).

## The Needleman–Wunsch recurrence, end-peeling

Let
$\sigma : \alpha \to \alpha \to \mathbb{Z}$ be a substitution score and $g \in \mathbb{Z}$ a gap
score, and write $N(x, y)$ for the Needleman–Wunsch score of sequences $x, y$ over $\alpha$ with
respect to $\sigma$ and $g$. For all sequences $x, y$ and letters $a, b \in \alpha$, writing $xa$
for the sequence $x$ followed by the letter $a$,

$$N(xa, yb) = \max\bigl(N(x, y) + \sigma(a, b),\ N(x, yb) + g,\ N(xa, y) + g\bigr).$$

Formalized by `Cslib.Algorithms.Lean.nwScore_snoc`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 1161](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L1161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#nw-score-snoc).

## Maximum of an integer list with floor zero

For a list $l$ of integers, this is the
largest of $0$ and the entries of $l$; in particular the empty list gives $0$.

It is used to define the suffix maximum, the local score and the Smith–Waterman score.

Formalized by `Cslib.Algorithms.Lean.listMax`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 1187](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L1187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#list-max).

## Pairs of suffixes

For lists $xs$ and $ys$, the list of all pairs $(u, v)$ where $u$ is
a suffix of $xs$ and $v$ is a suffix of $ys$, the empty lists and $xs$, $ys$ themselves
included.

Formalized by `Cslib.Algorithms.Lean.suffixPairs`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 1222](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L1222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#suffix-pairs).

## Suffix maximum of Needleman–Wunsch scores

Given a substitution score $\sigma$ and an
integer gap score $g$, the suffix maximum of lists $xs$ and $ys$ is the maximum of the
Needleman–Wunsch scores of all pairs $(u, v)$ with $u$ a suffix of $xs$ and $v$ a suffix of
$ys$.

The maximum is taken with floor $0$, which changes nothing, since the pair of empty suffixes
scores $0$.

Formalized by `Cslib.Algorithms.Lean.suffixMax`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 1230](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L1230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#suffix-max).

## Suffix pairs score at most the suffix maximum

Let
$\sigma : \alpha \to \alpha \to \mathbb{Z}$ be a substitution score and $g \in \mathbb{Z}$ a gap
score. If $(x', y')$ is a suffix pair of sequences $x$ and $y$ over $\alpha$, that is, $x'$ is a
suffix of $x$ and $y'$ is a suffix of $y$, then the Needleman–Wunsch score of $x'$ and $y'$ is at
most the suffix maximum of $x$ and $y$, both with respect to $\sigma$ and $g$.

Formalized by `Cslib.Algorithms.Lean.nwScore_le_suffixMax`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 1234](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L1234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#nw-score-le-suffix-max).

## Upper bounds on the suffix maximum

Let $\sigma$ be a substitution score, $g$ an integer
gap score, $xs$ and $ys$ lists and $y$ an integer. If every pair $(u, v)$ with $u$ a suffix of
$xs$ and $v$ a suffix of $ys$ has Needleman–Wunsch score at most $y$, then the maximum
Needleman–Wunsch score over all such suffix pairs is at most $y$.

Formalized by `Cslib.Algorithms.Lean.suffixMax_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 1242](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L1242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#suffix-max-le).

## The suffix maximum is attained

For a substitution score
$\sigma : \alpha \to \alpha \to \mathbb{Z}$, a gap score $g \in \mathbb{Z}$ and sequences $x$
and $y$ over $\alpha$, there is a suffix pair $(x', y')$ of $x$ and $y$, that is, a suffix $x'$
of $x$ and a suffix $y'$ of $y$, whose Needleman–Wunsch score equals the suffix maximum of $x$
and $y$.

Formalized by `Cslib.Algorithms.Lean.exists_nwScore_eq_suffixMax`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 1256](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L1256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#exists-nw-score-eq-suffix-max).

## The suffix maximum is nonnegative

For every scoring function
$\sigma : \alpha \to \alpha \to \mathbb{Z}$, every gap score $g \in \mathbb{Z}$ and all lists
$x$ and $y$ over $\alpha$, the suffix maximum of $x$ and $y$ (the largest Needleman–Wunsch score,
under $\sigma$ and $g$, of a suffix of $x$ against a suffix of $y$) is at least $0$, since the
pair of empty suffixes scores $0$.

Formalized by `Cslib.Algorithms.Lean.zero_le_suffixMax`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 1272](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L1272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#zero-le-suffix-max).

## Extending an alignment by a letter of the first sequence

If $A$ is an alignment of
sequences $x$ and $y$ and $a$ is a letter, then $A$ followed by the column with $a$ in the
first row and a gap in the second row is an alignment of $x$ followed by $a$ and of $y$.

Formalized by `Cslib.Algorithms.Lean.isAlignment_append_some_none`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 1279](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L1279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#is-alignment-append-some-none).

## Extending an alignment by a letter of the second sequence

If $A$ is an alignment of
sequences $x$ and $y$ and $b$ is a letter, then $A$ followed by the column with a gap in the
first row and $b$ in the second row is an alignment of $x$ and of $y$ followed by $b$.

Formalized by `Cslib.Algorithms.Lean.isAlignment_append_none_some`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 1293](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L1293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#is-alignment-append-none-some).

## Appending to the first sequence loses at most one gap

Let
$\sigma : \alpha \to \alpha \to \mathbb{Z}$ be a substitution score, $g \in \mathbb{Z}$ a gap
score, and write $N(x, y)$ for the Needleman–Wunsch score of sequences $x, y$ over $\alpha$ with
respect to $\sigma$ and $g$. For all sequences $x, y$ and every letter $a \in \alpha$, writing
$xa$ for $x$ with $a$ appended at the end, $N(x, y) + g \le N(xa, y)$.

An optimal alignment of $x$ and $y$ followed by the gap column pairing $a$ with nothing is an
alignment of $xa$ and $y$.

Formalized by `Cslib.Algorithms.Lean.nwScore_le_nwScore_snoc_left`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 1307](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L1307). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#nw-score-le-nw-score-snoc-left).

## Appending to the second sequence loses at most one gap

Let
$\sigma : \alpha \to \alpha \to \mathbb{Z}$ be a substitution score, $g \in \mathbb{Z}$ a gap
score, and write $N(x, y)$ for the Needleman–Wunsch score of sequences $x, y$ over $\alpha$ with
respect to $\sigma$ and $g$. For all sequences $x, y$ and every letter $b \in \alpha$, writing
$yb$ for $y$ with $b$ appended at the end, $N(x, y) + g \le N(x, yb)$.

An optimal alignment of $x$ and $y$ followed by the gap column pairing nothing with $b$ is an
alignment of $x$ and $yb$.

Formalized by `Cslib.Algorithms.Lean.nwScore_le_nwScore_snoc_right`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 1319](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L1319). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#nw-score-le-nw-score-snoc-right).

## Suffix pairs score at most the terminal Smith–Waterman cell

Let
$\sigma : \alpha \to \alpha \to \mathbb{Z}$ be a substitution score and $g \le 0$ a gap score. If
$x'$ is a suffix of a sequence $x$ and $y'$ is a suffix of a sequence $y$ over $\alpha$, then the
Needleman–Wunsch score of $x'$ and $y'$ is at most the terminal Smith–Waterman cell score of $x$
and $y$, both with respect to $\sigma$ and $g$.

Formalized by `Cslib.Algorithms.Lean.nwScore_le_swCellScore_of_suffix`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 1331](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L1331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#nw-score-le-sw-cell-score-of-suffix).

## The terminal cell is at most the suffix maximum

For every substitution score $\sigma$,
every gap score $g$ of either sign and all sequences $x$ and $y$, the terminal Smith–Waterman
cell $H(x, y)$ is at most the maximum Needleman–Wunsch score over all pairs of a suffix of $x$
and a suffix of $y$.

Only the reverse inequality needs $g \le 0$.

Formalized by `Cslib.Algorithms.Lean.swCellScore_le_suffixMax`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 1400](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L1400). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#sw-cell-score-le-suffix-max).

## The suffix maximum is at most the terminal Smith–Waterman cell

Let $\sigma$ be a
substitution score and $g \le 0$ an integer gap score. For all lists $xs$ and $ys$, the
maximum Needleman–Wunsch score over all pairs of a suffix of $xs$ and a suffix of $ys$ is at
most the terminal Smith–Waterman cell score of $xs$ and $ys$.

Formalized by `Cslib.Algorithms.Lean.suffixMax_le_swCellScore`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 1493](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L1493). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#suffix-max-le-sw-cell-score).

## For nonpositive gaps, the terminal Smith–Waterman cell is the best suffix-pair score

For a substitution score $\sigma$, a gap score $g \le 0$ and all sequences $x$ and $y$, the
terminal Smith–Waterman cell $H(x, y)$ equals the maximum Needleman–Wunsch score over all pairs
of a suffix of $x$ and a suffix of $y$ (the empty suffixes included).

Formalized by `Cslib.Algorithms.Lean.swCellScore_eq_suffixMax`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 1502](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L1502). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#sw-cell-score-eq-suffix-max).

## Pairs of prefixes

For lists $xs$ and $ys$, the list of all pairs $(p, q)$ where $p$ is
a prefix of $xs$ and $q$ is a prefix of $ys$, the empty lists and $xs$, $ys$ themselves
included.

Formalized by `Cslib.Algorithms.Lean.prefixPairs`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 1508](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L1508). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#prefix-pairs).

## Infix pairs

For sequences $x$ and $y$ over $\alpha$, the list of infix pairs of $x$ and
$y$ is obtained by going through each prefix $p$ of $x$ and each prefix $q$ of $y$ and, for each
such $(p, q)$, listing all pairs $(x', y')$ of a suffix $x'$ of $p$ and a suffix $y'$ of $q$.

So $(x', y')$ occurs in the list exactly when $x'$ is a contiguous block of $x$ and $y'$ is a
contiguous block of $y$; a pair may occur more than once.

Formalized by `Cslib.Algorithms.Lean.infixPairs`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 1516](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L1516). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#infix-pairs).

## Local alignment score

For an integer substitution score $\sigma$, an integer gap score
$g$ and sequences $x$ and $y$, the local score of $x$ and $y$ is the maximum of the
Needleman–Wunsch score of $(x', y')$ over all pairs of an infix $x'$ of $x$ and an infix $y'$ of
$y$ (contiguous and possibly empty).

Formalized by `Cslib.Algorithms.Lean.localScore`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 1539](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L1539). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#local-score).

## Infix pairs score at most the local score

Let $\sigma : \alpha \to \alpha \to \mathbb{Z}$
be a substitution score and $g \in \mathbb{Z}$ a gap score. If $(x', y')$ is an infix pair of
sequences $x$ and $y$ over $\alpha$, that is, $x'$ is a suffix of a prefix of $x$ and $y'$ is a
suffix of a prefix of $y$, then the Needleman–Wunsch score of $x'$ and $y'$ is at most the local
score of $x$ and $y$, both with respect to $\sigma$ and $g$.

Formalized by `Cslib.Algorithms.Lean.nwScore_le_localScore`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 1543](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L1543). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#nw-score-le-local-score).

## Upper bounds on the local score

Let $\sigma$ be an integer substitution score, $g$ an
integer gap score, $x$ and $y$ sequences and $c$ an integer. If the Needleman–Wunsch score of
every pair $(x', y')$ with $x'$ an infix of $x$ and $y'$ an infix of $y$ is at most $c$, then the
local score of $x$ and $y$ is at most $c$.

Formalized by `Cslib.Algorithms.Lean.localScore_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 1551](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L1551). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#local-score-le).

## The Smith–Waterman score

Given a substitution score $\sigma$ and a gap score $g$, the
Smith–Waterman score of two sequences $x$ and $y$ is the maximum of the terminal Smith–Waterman
cell $H(p, q)$ over all pairs of a prefix $p$ of $x$ and a prefix $q$ of $y$ (the empty prefixes
included).

For $g \le 0$ this is the optimal local alignment score, the maximum Needleman–Wunsch score over
pairs of infixes; for $g > 0$ it can be smaller.

Formalized by `Cslib.Algorithms.Lean.swScore`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 1568](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L1568). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#sw-score).

## Each prefix-pair cell is at most the Smith–Waterman score

For a substitution score
$\sigma$, a gap score $g$, sequences $x$ and $y$, a prefix $p$ of $x$ and a prefix $q$ of $y$,
the terminal Smith–Waterman cell $H(p, q)$ is at most the Smith–Waterman score of $x$ and $y$.

Formalized by `Cslib.Algorithms.Lean.swCellScore_le_swScore`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 1572](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L1572). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#sw-cell-score-le-sw-score).

## Bounding the Smith–Waterman score by its cells

For a substitution score $\sigma$, a gap
score $g$, sequences $x$ and $y$ and an integer $c$, if the terminal Smith–Waterman cell $H(p, q)$
is at most $c$ for every prefix $p$ of $x$ and every prefix $q$ of $y$, then the Smith–Waterman
score of $x$ and $y$ is at most $c$.

Formalized by `Cslib.Algorithms.Lean.swScore_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 1580](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L1580). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#sw-score-le).

## The local score equals the Smith–Waterman score

Let $\sigma$ be an integer-valued
substitution score on letters and let $g$ be an integer gap score with $g \le 0$. Then for all
sequences $x$ and $y$, the local score of $x$ and $y$ (the maximum Needleman–Wunsch score over
pairs of infixes) equals their Smith–Waterman score (the maximum terminal-cell score over pairs
of prefixes).

The proof uses that an infix is a suffix of a prefix and that the terminal cell is a maximum
over pairs of suffixes.

Formalized by `Cslib.Algorithms.Lean.localScore_eq_swScore`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean, line 1595](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/SequenceAlignment.lean#L1595). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#local-score-eq-sw-score).

## Remaining cells of a Needleman–Wunsch table row

The cells `F[i+1][j+1], F[i+1][j+2], …` of a row from the remaining letters `b :: ys` of the
second sequence, the remaining cells `up :: prev` of the previous row, the previous row's cell
`diag` to the upper left and the cell `left` just computed. A previous row that is too short ends
the row early (this does not happen for rows of the table, `nextRow_eq`).

Formalized by `Cslib.Bioinformatics.Alignment.NeedlemanWunsch.nextRowAux`, a definition declared in [CSLibExt/Bioinformatics/Alignment/NeedlemanWunschTable.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Alignment/NeedlemanWunschTable.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#next-row-aux).

## Next row of the Needleman–Wunsch table

The row of the table for the prefix extended by `a`, from the previous row: the first cell is
one more gap than the previous row's first cell, then the recurrence left to right.

Formalized by `Cslib.Bioinformatics.Alignment.NeedlemanWunsch.nextRow`, a definition declared in [CSLibExt/Bioinformatics/Alignment/NeedlemanWunschTable.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Alignment/NeedlemanWunschTable.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#next-row).

## Row-by-row filling of the Needleman–Wunsch table

The rows of the table, filled top to bottom over the letters of the first sequence; the
result is the last row. Row `0` is `F[0][j] = j * gap`.

Formalized by `Cslib.Bioinformatics.Alignment.NeedlemanWunsch.nwRowsAux`, a definition declared in [CSLibExt/Bioinformatics/Alignment/NeedlemanWunschTable.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Alignment/NeedlemanWunschTable.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#nw-rows-aux).

## Last row of the Needleman–Wunsch table

The last row `F[|xs|][·]` of the Needleman–Wunsch table.

Formalized by `Cslib.Bioinformatics.Alignment.NeedlemanWunsch.nwRows`, a definition declared in [CSLibExt/Bioinformatics/Alignment/NeedlemanWunschTable.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Alignment/NeedlemanWunschTable.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#nw-rows).

## The Needleman–Wunsch table

Its last cell `F[|xs|][|ys|]`.

Formalized by `Cslib.Bioinformatics.Alignment.NeedlemanWunsch.nwTab`, a definition declared in [CSLibExt/Bioinformatics/Alignment/NeedlemanWunschTable.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Alignment/NeedlemanWunschTable.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#nw-tab).

## One row of the table

From the row of the prefix `px`, `nextRow` computes the row of
`px ++ [a]`: the cells `nwScore (px ++ [a]) py` for the prefixes `py` of `ys`, shortest first.

Formalized by `Cslib.Bioinformatics.Alignment.NeedlemanWunsch.nextRow_eq`, a theorem declared in [CSLibExt/Bioinformatics/Alignment/NeedlemanWunschTable.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Alignment/NeedlemanWunschTable.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#next-row-eq).

## The last row of the table

**The last row of the table** is `F[|xs|][j] = nwScore xs (ys.take j)`: the cells
`nwScore xs py` over the prefixes `py` of `ys`, shortest first.

Formalized by `Cslib.Bioinformatics.Alignment.NeedlemanWunsch.nwRows_eq`, a theorem declared in [CSLibExt/Bioinformatics/Alignment/NeedlemanWunschTable.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Alignment/NeedlemanWunschTable.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#nw-rows-eq).

## The table computes the optimal global alignment score

**The table computes the optimal global alignment score** (Needleman–Wunsch 1970), for every
substitution score `σ` and gap score `gap`.

Formalized by `Cslib.Bioinformatics.Alignment.NeedlemanWunsch.nwTab_eq_nwScore`, a theorem declared in [CSLibExt/Bioinformatics/Alignment/NeedlemanWunschTable.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Alignment/NeedlemanWunschTable.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html#nw-tab-eq-nw-score).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Pairwise sequence alignment](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/bioinformatics/sequence-alignment/pairwise-sequence-alignment)
