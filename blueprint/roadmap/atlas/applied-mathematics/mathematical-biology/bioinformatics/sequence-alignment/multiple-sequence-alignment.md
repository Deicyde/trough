---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.MSAlignment, Cslib.Algorithms.Lean.IsMSAlignment, Cslib.Algorithms.Lean.inducedPair, Cslib.Algorithms.Lean.inducedPair_ne_none_none, Cslib.Algorithms.Lean.inducedPair_filterMap_fst, Cslib.Algorithms.Lean.inducedPair_filterMap_snd, Cslib.Algorithms.Lean.inducedPair_isAlignment, Cslib.Algorithms.Lean.pairFinset
statement: formalized
proof: formalized
---

# Multiple sequence alignment

14 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/multiple-sequence-alignment/index.html).

## Multiple alignments

A multiple alignment with $k$ rows over an alphabet $\alpha$ is a
finite list of columns, each of which assigns to every row $i \in \{0, \dots, k-1\}$ either a
letter of $\alpha$ or a gap. No condition ties the rows to given sequences.

Formalized by `Cslib.Algorithms.Lean.MSAlignment`, an abbreviation declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleSequenceAlignment.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleSequenceAlignment.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/multiple-sequence-alignment/index.html#msalignment).

## Valid multiple alignment

A multiple alignment $A$ of $k$ rows is a valid multiple
alignment of sequences $s_0, \dots, s_{k-1}$ when no column of $A$ consists only of gaps and, for
every $i < k$, deleting the gaps from row $i$ of $A$ gives $s_i$.

Formalized by `Cslib.Algorithms.Lean.IsMSAlignment`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleSequenceAlignment.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleSequenceAlignment.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/multiple-sequence-alignment/index.html#is-msalignment).

## Induced pairwise alignment

Given a multiple alignment $A$ of $k$ sequences and rows
$i, j < k$, the pairwise alignment induced by $A$ on rows $i$ and $j$ is obtained by keeping, for
each column $c$ of $A$ in order, the pair $(c_i, c_j)$, and dropping the columns in which both
$c_i$ and $c_j$ are gaps.

Formalized by `Cslib.Algorithms.Lean.inducedPair`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleSequenceAlignment.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleSequenceAlignment.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/multiple-sequence-alignment/index.html#induced-pair).

## Induced alignments have no all-gap column

For a multiple alignment $A$ of $k$ sequences
and rows $i, j < k$, no column of the pairwise alignment induced by $A$ on rows $i$ and $j$ is a
gap in both rows.

Formalized by `Cslib.Algorithms.Lean.inducedPair_ne_none_none`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleSequenceAlignment.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleSequenceAlignment.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/multiple-sequence-alignment/index.html#induced-pair-ne-none-none).

## Letters of the first row of an induced alignment

For a multiple alignment $A$ of $k$
sequences and rows $i, j < k$, deleting the gaps from the first row of the pairwise alignment
induced by $A$ on rows $i$ and $j$ gives the same sequence as deleting the gaps from row $i$ of
$A$.

Formalized by `Cslib.Algorithms.Lean.inducedPair_filterMap_fst`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleSequenceAlignment.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleSequenceAlignment.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/multiple-sequence-alignment/index.html#induced-pair-filter-map-fst).

## Letters of the second row of an induced alignment

For a multiple alignment $A$ of $k$
sequences and rows $i, j < k$, deleting the gaps from the second row of the pairwise alignment
induced by $A$ on rows $i$ and $j$ gives the same sequence as deleting the gaps from row $j$ of
$A$.

Formalized by `Cslib.Algorithms.Lean.inducedPair_filterMap_snd`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleSequenceAlignment.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleSequenceAlignment.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/multiple-sequence-alignment/index.html#induced-pair-filter-map-snd).

## Induced pairwise alignments are valid

Let $A$ be a valid multiple alignment of sequences
$s_0, \dots, s_{k-1}$. Then for all rows $i, j < k$, the pairwise alignment induced by $A$ on rows
$i$ and $j$ is a valid pairwise alignment of $s_i$ and $s_j$.

Formalized by `Cslib.Algorithms.Lean.inducedPair_isAlignment`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleSequenceAlignment.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleSequenceAlignment.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/multiple-sequence-alignment/index.html#induced-pair-is-alignment).

## Pairs of rows

For $k \in \mathbb{N}$, the finite set of all pairs $(i, j)$ with
$i, j \in \{0, \dots, k-1\}$ and $i < j$, so that each unordered pair of distinct rows appears
exactly once.

Formalized by `Cslib.Algorithms.Lean.pairFinset`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleSequenceAlignment.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleSequenceAlignment.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/multiple-sequence-alignment/index.html#pair-finset).

## Sum-of-pairs score of a column

Let $\sigma$ assign an integer score to each pair of
letters and let $g$ be an integer gap score. For a column $c$ of a multiple alignment of $k$
sequences, which gives each row $r < k$ either a letter or a gap $c_r$, the sum-of-pairs score of
$c$ is $\sum_{i < j < k} s(c_i, c_j)$, where $s$ is the pairwise column score: $\sigma(a, b)$ for
letters $a$ and $b$, $g$ for a letter against a gap, and $0$ for two gaps.

Formalized by `Cslib.Algorithms.Lean.columnSP`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleSequenceAlignment.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleSequenceAlignment.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/multiple-sequence-alignment/index.html#column-sp).

## Sum-of-pairs score

Fix a score $\sigma(a, b) \in \mathbb{Z}$ for each pair of letters
$a, b$ and a gap score $g \in \mathbb{Z}$. For two entries $x, y$, each a letter or a gap, let
$s(x, y) = \sigma(x, y)$ if both are letters, $s(x, y) = g$ if exactly one is a gap, and
$s(x, y) = 0$ if both are gaps. The sum-of-pairs score of a multiple alignment $A$ of $k$
sequences is the sum, over the columns $c$ of $A$, of $\sum_{0 \le i < j < k} s(c_i, c_j)$,
where $c_i$ is the entry of $c$ in row $i$.

Formalized by `Cslib.Algorithms.Lean.msaScore`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleSequenceAlignment.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleSequenceAlignment.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/multiple-sequence-alignment/index.html#msa-score).

## Score of an induced pairwise alignment

Let $\sigma$ assign an integer score to each
pair of letters and let $g$ be an integer gap score. For a multiple alignment $A$ of $k$
sequences and rows $i, j < k$, the score (with respect to $\sigma$ and $g$) of the pairwise
alignment induced by $A$ on rows $i$ and $j$ equals the sum, over all columns $c$ of $A$, of the
column score of the pair $(c_i, c_j)$.

Formalized by `Cslib.Algorithms.Lean.alignmentScore_inducedPair`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleSequenceAlignment.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleSequenceAlignment.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/multiple-sequence-alignment/index.html#alignment-score-induced-pair).

## The SP score is the sum of the induced pairwise scores

Let $\sigma$ assign an integer
score to each pair of letters and let $g$ be an integer gap score. For every multiple alignment
$A$ of $k$ sequences, the sum-of-pairs score of $A$ equals the sum, over all pairs of rows
$i < j < k$, of the score of the pairwise alignment induced by $A$ on rows $i$ and $j$.

Formalized by `Cslib.Algorithms.Lean.msaScore_eq_sum_induced`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleSequenceAlignment.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleSequenceAlignment.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/multiple-sequence-alignment/index.html#msa-score-eq-sum-induced).

## The sum-of-pairs score is bounded by the pairwise optima

Fix a score
$\sigma(a, b) \in \mathbb{Z}$ for each pair of letters $a, b$ of an alphabet $\alpha$ and a gap
score $g \in \mathbb{Z}$. Let $s_0, \dots, s_{k-1}$ be sequences over $\alpha$ and let $A$ be a
valid multiple alignment of them: no column of $A$ consists only of gaps, and deleting the gaps
from row $i$ of $A$ leaves $s_i$. Then the sum-of-pairs score of $A$ under $\sigma$ and $g$ is at
most $\sum_{0 \le i < j < k} \mathrm{NW}(s_i, s_j)$, where $\mathrm{NW}(s_i, s_j)$ is the optimal
global (Needleman–Wunsch) alignment score of $s_i$ and $s_j$ under $\sigma$ and $g$.

Formalized by `Cslib.Algorithms.Lean.msaScore_le_sum_nwScore`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleSequenceAlignment.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleSequenceAlignment.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/multiple-sequence-alignment/index.html#msa-score-le-sum-nw-score).

## Every family of sequences has a multiple alignment

For every natural number $n$ and
every family of $k$ sequences $s_0, \dots, s_{k-1}$ whose lengths sum to at most $n$, there is a
valid multiple alignment of $s_0, \dots, s_{k-1}$.

The bound $n$ is the parameter of the induction in the proof, which removes the first letter of
one nonempty sequence; taking $n$ to be the total length shows that every finite family of
sequences has a valid multiple alignment.

Formalized by `Cslib.Algorithms.Lean.exists_isMSAlignment`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleSequenceAlignment.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/MultipleSequenceAlignment.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/multiple-sequence-alignment/index.html#exists-is-msalignment).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Multiple sequence alignment](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/multiple-sequence-alignment/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/bioinformatics/sequence-alignment/multiple-sequence-alignment)
