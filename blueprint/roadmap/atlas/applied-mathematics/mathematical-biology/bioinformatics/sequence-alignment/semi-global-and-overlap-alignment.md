---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.zero_le_listMax, Cslib.Algorithms.Lean.overlapPairs, Cslib.Algorithms.Lean.overlapScore, Cslib.Algorithms.Lean.nwScore_le_overlapScore, Cslib.Algorithms.Lean.overlapScore_le, Cslib.Algorithms.Lean.exists_nwScore_eq_overlapScore, Cslib.Algorithms.Lean.overlapScore_nonneg, Cslib.Algorithms.Lean.infixes
statement: formalized
proof: formalized
---

# Semi-global and overlap alignment

14 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/semi-global-and-overlap-alignment/index.html).

## The floored list maximum is nonnegative

For every list $L$ of integers, the maximum of
$L$ with floor $0$ (which is $0$ for the empty list) is at least $0$.

Formalized by `Cslib.Algorithms.Lean.zero_le_listMax`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SemiGlobalAlignment.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/SemiGlobalAlignment.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/semi-global-and-overlap-alignment/index.html#zero-le-list-max).

## Overlap pairs

The overlap pairs of sequences $x$ and $y$ are the pairs $(x', y')$ in
which $x'$ is a suffix of $x$ and $y'$ is a prefix of $y$, or $x'$ is a prefix of $x$ and
$y'$ is a suffix of $y$. Prefixes and suffixes include the empty sequence and the whole
sequence; the pairs are listed with the suffix–prefix pairs first, and the list can contain
repetitions.

Formalized by `Cslib.Algorithms.Lean.overlapPairs`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SemiGlobalAlignment.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/SemiGlobalAlignment.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/semi-global-and-overlap-alignment/index.html#overlap-pairs).

## Overlap alignment score

Given a substitution score $\sigma$ and a gap score $g$, the
overlap score of sequences $s$ and $t$ is the maximum, with floor $0$, of the Needleman–Wunsch
scores of the overlap pairs of $s$ and $t$: the pairs $(s', t')$ where $s'$ is a suffix of $s$
and $t'$ a prefix of $t$, or $s'$ is a prefix of $s$ and $t'$ a suffix of $t$.

The pair of two empty sequences is an overlap pair with score $0$, so the floor never changes
the value: this is the best alignment score of a suffix of one sequence against a prefix of the
other.

Formalized by `Cslib.Algorithms.Lean.overlapScore`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SemiGlobalAlignment.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/SemiGlobalAlignment.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/semi-global-and-overlap-alignment/index.html#overlap-score).

## Overlap-pair scores are at most the overlap score

Let $\sigma$ be a substitution
score and $g$ a gap score. If $(x', y')$ is an overlap pair of sequences $x$ and $y$, then the
Needleman–Wunsch score of $x'$ against $y'$ is at most the overlap score of $x$ and $y$, both
taken with $\sigma$ and $g$.

Formalized by `Cslib.Algorithms.Lean.nwScore_le_overlapScore`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SemiGlobalAlignment.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/SemiGlobalAlignment.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/semi-global-and-overlap-alignment/index.html#nw-score-le-overlap-score).

## Upper bounds for the overlap score

Fix a substitution score $\sigma$ and a gap score
$g$, and sequences $s$ and $t$. If an integer $b$ is at least the Needleman–Wunsch score of
every overlap pair of $s$ and $t$ (a suffix of $s$ with a prefix of $t$, or a prefix of $s$
with a suffix of $t$), then the overlap score of $s$ and $t$ is at most $b$.

Formalized by `Cslib.Algorithms.Lean.overlapScore_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SemiGlobalAlignment.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/SemiGlobalAlignment.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/semi-global-and-overlap-alignment/index.html#overlap-score-le).

## The overlap score is attained

Let $\sigma$ be a substitution score and $g$ a gap
score. For all sequences $x$ and $y$ there is an overlap pair $(x', y')$ of $x$ and $y$ such
that the Needleman–Wunsch score of $x'$ against $y'$ (with $\sigma$ and $g$) equals the
overlap score of $x$ and $y$.

Formalized by `Cslib.Algorithms.Lean.exists_nwScore_eq_overlapScore`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SemiGlobalAlignment.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/SemiGlobalAlignment.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/semi-global-and-overlap-alignment/index.html#exists-nw-score-eq-overlap-score).

## The overlap score is nonnegative

For every substitution score $\sigma$, gap
score $g$ and sequences $s$ and $t$, the overlap score of $s$ and $t$ is at least $0$.

The pair of two empty sequences is an overlap pair, and its score is $0$.

Formalized by `Cslib.Algorithms.Lean.overlapScore_nonneg`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SemiGlobalAlignment.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/SemiGlobalAlignment.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/semi-global-and-overlap-alignment/index.html#overlap-score-nonneg).

## Infixes

The infixes of a sequence $y$ are its contiguous substrings: the sequences
$l$ such that $y$ is the concatenation of $s$, $l$ and $t$ for some sequences $s$ and $t$,
including the empty sequence and $y$ itself. They are listed as the suffixes of the prefixes
of $y$, so the list can contain repetitions.

Formalized by `Cslib.Algorithms.Lean.infixes`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SemiGlobalAlignment.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/SemiGlobalAlignment.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/semi-global-and-overlap-alignment/index.html#infixes).

## Fitting score

Let $\sigma$ be a substitution score and $g$ a gap score. The fitting
score of a sequence $x$ against a sequence $y$ is the maximum, over all infixes $l$ of $y$
(including the empty one), of the Needleman–Wunsch score of $x$ against $l$ with $\sigma$ and
$g$: the best global alignment score of $x$ against a substring of $y$.

The empty infix is always a candidate, so the maximum is attained. Unlike the overlap score,
the fitting score is not floored at $0$: it can be negative when every fitting alignment
scores negatively.

Formalized by `Cslib.Algorithms.Lean.fittingScore`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SemiGlobalAlignment.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/SemiGlobalAlignment.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/semi-global-and-overlap-alignment/index.html#fitting-score).

## Infix scores are at most the fitting score

Let $\sigma$ be a substitution score and
$g$ a gap score. If $l$ is an infix of a sequence $y$, then for every sequence $x$ the
Needleman–Wunsch score of $x$ against $l$ is at most the fitting score of $x$ against $y$,
both taken with $\sigma$ and $g$.

Formalized by `Cslib.Algorithms.Lean.nwScore_le_fittingScore`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SemiGlobalAlignment.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/SemiGlobalAlignment.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/semi-global-and-overlap-alignment/index.html#nw-score-le-fitting-score).

## Upper bounds on the fitting score

Let $\sigma$ be a substitution score, $g$ a gap
score, $x$ and $y$ sequences and $b$ an integer. If the Needleman–Wunsch score of $x$ against
every infix of $y$ (with $\sigma$ and $g$) is at most $b$, then the fitting score of $x$
against $y$ is at most $b$.

Formalized by `Cslib.Algorithms.Lean.fittingScore_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SemiGlobalAlignment.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/SemiGlobalAlignment.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/semi-global-and-overlap-alignment/index.html#fitting-score-le).

## The fitting score is attained

Let $\sigma$ be a substitution score and $g$ a gap
score. For all sequences $x$ and $y$ there is an infix $l$ of $y$ such that the
Needleman–Wunsch score of $x$ against $l$ (with $\sigma$ and $g$) equals the fitting score of
$x$ against $y$.

Formalized by `Cslib.Algorithms.Lean.exists_nwScore_eq_fittingScore`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SemiGlobalAlignment.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/SemiGlobalAlignment.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/semi-global-and-overlap-alignment/index.html#exists-nw-score-eq-fitting-score).

## The overlap score is at most the local score

Let $\sigma$ be a substitution score
and $g$ a gap score. For all sequences $x$ and $y$, the overlap score of $x$ and $y$ is at
most the local score of $x$ and $y$, both taken with $\sigma$ and $g$.

Every overlap pair is an infix pair.

Formalized by `Cslib.Algorithms.Lean.overlapScore_le_localScore`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SemiGlobalAlignment.lean, line 271](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/SemiGlobalAlignment.lean#L271). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/semi-global-and-overlap-alignment/index.html#overlap-score-le-local-score).

## The fitting score is at most the local score

Let $\sigma$ be a substitution score
and $g$ a gap score. For all sequences $x$ and $y$, the fitting score of $x$ against $y$ is at
most the local score of $x$ and $y$, both taken with $\sigma$ and $g$.

Every fitting candidate, all of $x$ against an infix of $y$, is an infix pair.

Formalized by `Cslib.Algorithms.Lean.fittingScore_le_localScore`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/SemiGlobalAlignment.lean, line 285](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/SemiGlobalAlignment.lean#L285). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/semi-global-and-overlap-alignment/index.html#fitting-score-le-local-score).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Semi-global and overlap alignment](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/semi-global-and-overlap-alignment/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/bioinformatics/sequence-alignment/semi-global-and-overlap-alignment)
