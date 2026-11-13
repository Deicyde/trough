---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.GapState, Cslib.Algorithms.Lean.gapCost, Cslib.Algorithms.Lean.affineScoreAux, Cslib.Algorithms.Lean.affineScore, Cslib.Algorithms.Lean.gotohAux, Cslib.Algorithms.Lean.gotohContNone, Cslib.Algorithms.Lean.gotohContGapX, Cslib.Algorithms.Lean.gotohContGapY
statement: formalized
proof: formalized
---

# Gotoh affine-gap alignment

45 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/gotoh-affine-gap-alignment/index.html).

## Gap states

A gap state is one of three values: $\mathrm{none}$, $\mathrm{gapX}$ and
$\mathrm{gapY}$. The affine-gap score and the Gotoh recursion carry one as the kind of the previous
column: $\mathrm{gapX}$ after a column pairing an element of the first sequence with a gap,
$\mathrm{gapY}$ after a column pairing a gap with an element of the second sequence, and
$\mathrm{none}$ otherwise, including before the first column.

Formalized by `Cslib.Algorithms.Lean.GapState`, an inductive type declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/gotoh-affine-gap-alignment/index.html#gap-state).

## Gap cost

Given an integer gap-open cost $o$, an integer gap-extend cost $e$ and gap states
$p$ (of the previous column) and $c$ (of the current gap column), the cost of the current column
is $e$ if $p = c$ (the column continues a run) and $o$ otherwise (it opens a run).

Formalized by `Cslib.Algorithms.Lean.gapCost`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/gotoh-affine-gap-alignment/index.html#gap-cost).

## Affine-gap score from a gap state

Fix an integer substitution score $\sigma$, an integer
gap-open cost $o$ and an integer gap-extend cost $e$. The affine-gap score of an alignment started
from a gap state $p$ is the sum of its column scores, computed left to right while carrying a gap
state that starts at $p$ and is updated after each column. The empty alignment scores $0$. A
column pairing an element $a$ of the first sequence with an element $b$ of the second scores
$\sigma(a, b)$ and sets the state to $\mathrm{none}$. A column pairing an element of the first
sequence with a gap has kind $\mathrm{gapX}$, and a column pairing a gap with an element of the
second sequence has kind $\mathrm{gapY}$; such a column scores $e$ if the carried state equals its
kind and $o$ otherwise, and sets the state to its kind. A column of two gaps scores $0$ and sets
the state to $\mathrm{none}$.

The column of two gaps cannot occur in a valid alignment; it is scored as a no-op.

Formalized by `Cslib.Algorithms.Lean.affineScoreAux`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/gotoh-affine-gap-alignment/index.html#affine-score-aux).

## Affine-gap alignment score

Given an integer substitution score $\sigma$, an integer
gap-open cost $o$ and an integer gap-extend cost $e$, the affine-gap score of an alignment is its
affine-gap score from a gap state, started from the state $\mathrm{none}$ (no open gap run).

Formalized by `Cslib.Algorithms.Lean.affineScore`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/gotoh-affine-gap-alignment/index.html#affine-score).

## Fuel-bounded Gotoh recursion

Fix an integer-valued scoring function $\sigma$ on pairs of
letters and integer gap-open and gap-extend penalties $g_o$ and $g_e$. A gap state records what
the previous alignment column was: a match ($\mathrm{none}$), a gap in the second sequence
($\mathrm{gapX}$) or a gap in the first sequence ($\mathrm{gapY}$). For gap states $p$, $q$ let
$c(p, q)$ be the gap cost, $g_e$ if $p = q$ and $g_o$ otherwise. Write $\varepsilon$ for the
empty sequence and $a \cdot u$ for the sequence with first letter $a$ followed by $u$. For fuel
$n \in \mathbb{N}$, sequences $u$, $v$ and a gap state $p$, the integer $G_n(u, v, p)$ is defined
by recursion on $n$: $G_0(u, v, p) = 0$, $G_{n+1}(\varepsilon, \varepsilon, p) = 0$,
$G_{n+1}(\varepsilon, b \cdot v, p) = c(p, \mathrm{gapY}) + G_n(\varepsilon, v, \mathrm{gapY})$,
$G_{n+1}(a \cdot u, \varepsilon, p) = c(p, \mathrm{gapX}) + G_n(u, \varepsilon, \mathrm{gapX})$,
and $G_{n+1}(a \cdot u, b \cdot v, p)$ is the maximum of $\sigma(a, b) + G_n(u, v, \mathrm{none})$,
$c(p, \mathrm{gapX}) + G_n(u, b \cdot v, \mathrm{gapX})$ and
$c(p, \mathrm{gapY}) + G_n(a \cdot u, v, \mathrm{gapY})$.

With fuel at least the sum of the two lengths this is the Gotoh dynamic program; with less fuel
the base case $G_0 = 0$ cuts the recursion short.

Formalized by `Cslib.Algorithms.Lean.gotohAux`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/gotoh-affine-gap-alignment/index.html#gotoh-aux).

## Gotoh value with no open gap run

Given a substitution score $\sigma$, a gap-open score
$g_o$ and a gap-extend score $g_e$, this is the value of the Gotoh dynamic program on sequences
$x$ and $y$ when no gap run is open (the previous column was a match, or there is no previous
column): the best affine-gap score of an alignment of $x$ and $y$, where a match column pairing
$a$ with $b$ scores $\sigma(a, b)$ and a gap column scores $g_e$ if it continues a run of gaps in
the same sequence and $g_o$ otherwise.

It is a continuation value, not an endpoint-restricted matrix: the first column may be a match
or either gap.

Formalized by `Cslib.Algorithms.Lean.gotohContNone`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/gotoh-affine-gap-alignment/index.html#gotoh-cont-none).

## Gotoh continuation value after a gap in the second sequence

Fix an integer-valued
scoring function $\sigma$ on pairs of letters and integer gap-open and gap-extend penalties $g_o$
and $g_e$. For sequences $u$ and $v$, the value $X(u, v)$ is the fuel-bounded Gotoh recursion on
$u$ and $v$, run with fuel equal to the sum of their lengths and started in the gap state where
the previous column was a gap in $v$.

It is the best affine-gap score of an alignment of $u$ with $v$ scored from that state. It is a
continuation value, not an endpoint-restricted matrix: the next column may be a match or either
gap, and the previous state only makes a next gap in $v$ cost $g_e$ instead of $g_o$.

Formalized by `Cslib.Algorithms.Lean.gotohContGapX`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/gotoh-affine-gap-alignment/index.html#gotoh-cont-gap-x).

## Gotoh continuation value after a gap in the first sequence

Fix an integer-valued
scoring function $\sigma$ on pairs of letters and integer gap-open and gap-extend penalties $g_o$
and $g_e$. For sequences $u$ and $v$, the value $Y(u, v)$ is the fuel-bounded Gotoh recursion on
$u$ and $v$, run with fuel equal to the sum of their lengths and started in the gap state where
the previous column was a gap in $u$.

It is the best affine-gap score of an alignment of $u$ with $v$ scored from that state. It is a
continuation value, not an endpoint-restricted matrix: the next column may be a match or either
gap, and the previous state only makes a next gap in $u$ cost $g_e$ instead of $g_o$.

Formalized by `Cslib.Algorithms.Lean.gotohContGapY`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/gotoh-affine-gap-alignment/index.html#gotoh-cont-gap-y).

## Gotoh score

For a substitution score $\sigma$ and gap-open and gap-extend scores $g_o$
and $g_e$, the Gotoh score of sequences $x$ and $y$ is the Gotoh value of $x$ against $y$ with no
open gap run, since no gap run is open before the first column.

It is the optimal affine-gap alignment score of $x$ and $y$.

Formalized by `Cslib.Algorithms.Lean.gotohScore`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/gotoh-affine-gap-alignment/index.html#gotoh-score).

## Cost of a gap run

Given an integer gap-open cost $o$, an integer gap-extend cost $e$, gap
states $p$ (of the column before the run) and $c$ (of the run's columns) and a length
$k \in \mathbb{N}$, the cost of a run of $k$ gap columns is $k e$ if $p = c$ (the run continues
an open run); otherwise it is $0$ for $k = 0$ and $o + (k - 1) e$ for $k \ge 1$.

Formalized by `Cslib.Algorithms.Lean.gapRunCost`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/gotoh-affine-gap-alignment/index.html#gap-run-cost).

## Adding a column to a gap run

For an integer gap-open cost $o$, an integer gap-extend cost
$e$, gap states $p$ and $c$ and $k \in \mathbb{N}$, the gap cost of a column in state $c$ after
state $p$, plus the cost of a run of $k$ columns in state $c$ that follows state $c$, equals the
cost of a run of $k + 1$ columns in state $c$ that follows state $p$.

Formalized by `Cslib.Algorithms.Lean.gapRunCost_succ`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/gotoh-affine-gap-alignment/index.html#gap-run-cost-succ).

## Removing a leading match column from a valid alignment

Let $a$ and $b$ be elements,
let $xs$ and $ys$ be sequences, and let $A$ be an alignment. If the alignment whose first column
is the match column $(a, b)$, followed by the columns of $A$, is a valid alignment of the
sequence $a$ followed by $xs$ and the sequence $b$ followed by $ys$, then $A$ is a valid
alignment of $xs$ and $ys$.

Formalized by `Cslib.Algorithms.Lean.isAlignment_of_cons_match`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/gotoh-affine-gap-alignment/index.html#is-alignment-of-cons-match).

## Removing a leading column with a gap in the second sequence

Let $A$ be an alignment, $a$
an element and $x$, $y$ sequences. If prepending to $A$ the column that pairs $a$ with a gap gives
a valid alignment of $a x$ (the sequence $x$ with $a$ prepended) and $y$, then $A$ is a valid
alignment of $x$ and $y$.

Formalized by `Cslib.Algorithms.Lean.isAlignment_of_cons_gapX`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/gotoh-affine-gap-alignment/index.html#is-alignment-of-cons-gap-x).

## Removing a leading column with a gap in the first sequence

Let $A$ be an alignment, $b$
an element and $x$, $y$ sequences. If prepending to $A$ the column that pairs a gap with $b$ gives
a valid alignment of $x$ and $b y$ (the sequence $y$ with $b$ prepended), then $A$ is a valid
alignment of $x$ and $y$.

Formalized by `Cslib.Algorithms.Lean.isAlignment_of_cons_gapY`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/gotoh-affine-gap-alignment/index.html#is-alignment-of-cons-gap-y).

## Prepending a match column

If $A$ is a valid alignment of sequences $x$ and $y$, then for
all elements $a$ and $b$, the alignment obtained by prepending to $A$ the column that pairs $a$
with $b$ is a valid alignment of $a x$ and $b y$ (the sequences $x$ and $y$ with $a$ and $b$
prepended).

Formalized by `Cslib.Algorithms.Lean.isAlignment_cons_match`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean, line 266](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean#L266). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/gotoh-affine-gap-alignment/index.html#is-alignment-cons-match).

## Prepending a column with a gap in the second sequence

If $A$ is a valid alignment of
sequences $x$ and $y$, then for every element $a$, the alignment obtained by prepending to $A$ the
column that pairs $a$ with a gap is a valid alignment of $a x$ (the sequence $x$ with $a$
prepended) and $y$.

Formalized by `Cslib.Algorithms.Lean.isAlignment_cons_gapX`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean, line 278](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean#L278). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/gotoh-affine-gap-alignment/index.html#is-alignment-cons-gap-x).

## Prepending a column with a gap in the first sequence

If $A$ is a valid alignment of
sequences $x$ and $y$, then for every element $b$, the alignment obtained by prepending to $A$ the
column that pairs a gap with $b$ is a valid alignment of $x$ and $b y$ (the sequence $y$ with $b$
prepended).

Formalized by `Cslib.Algorithms.Lean.isAlignment_cons_gapY`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean, line 290](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean#L290). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/gotoh-affine-gap-alignment/index.html#is-alignment-cons-gap-y).

## Gotoh is optimal

Let $\sigma$ be an integer substitution score, $o$ an integer gap-open
cost and $e$ an integer gap-extend cost. For all sequences $x$ and $y$ and every valid alignment
$A$ of $x$ and $y$, the affine-gap score of $A$ is at most the Gotoh score of $x$ and $y$, both
taken with $\sigma$, $o$ and $e$.

Formalized by `Cslib.Algorithms.Lean.affineScore_le_gotohScore`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean, line 502](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean#L502). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/gotoh-affine-gap-alignment/index.html#affine-score-le-gotoh-score).

## Gotoh is attained

Let $\sigma$ be an integer substitution score, $o$ an integer gap-open
cost and $e$ an integer gap-extend cost. For all sequences $x$ and $y$ there is a valid alignment
$A$ of $x$ and $y$ whose affine-gap score equals the Gotoh score of $x$ and $y$, both taken with
$\sigma$, $o$ and $e$.

Formalized by `Cslib.Algorithms.Lean.exists_affineScore_eq_gotohScore`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean, line 508](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean#L508). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/gotoh-affine-gap-alignment/index.html#exists-affine-score-eq-gotoh-score).

## First-column recurrence for the continuation after a match

Fix an
integer-valued scoring function $\sigma$ on pairs of letters and integer gap-open and gap-extend
penalties $g_o$ and $g_e$. For sequences $u$, $v$ let $N(u, v)$, $X(u, v)$ and $Y(u, v)$ be the
Gotoh continuation values when the previous column was a match, a gap in $v$ and a gap in $u$
respectively, and write $a \cdot u$ for the sequence with first letter $a$ followed by $u$. For
all letters $a$, $b$ and sequences $u$, $v$, the value $N(a \cdot u, b \cdot v)$ is the maximum
of $N(u, v) + \sigma(a, b)$, $X(u, b \cdot v) + g_o$ and $Y(a \cdot u, v) + g_o$.

Formalized by `Cslib.Algorithms.Lean.gotohContNone_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean, line 516](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean#L516). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/gotoh-affine-gap-alignment/index.html#gotoh-cont-none-eq).

## First-column recurrence for the continuation after a gap in the second sequence

Fix an
integer-valued scoring function $\sigma$ on pairs of letters and integer gap-open and gap-extend
penalties $g_o$ and $g_e$. For sequences $u$, $v$ let $N(u, v)$, $X(u, v)$ and $Y(u, v)$ be the
Gotoh continuation values when the previous column was a match, a gap in $v$ and a gap in $u$
respectively, and write $a \cdot u$ for the sequence with first letter $a$ followed by $u$. For
all letters $a$, $b$ and sequences $u$, $v$, the value $X(a \cdot u, b \cdot v)$ is the maximum
of $N(u, v) + \sigma(a, b)$, $X(u, b \cdot v) + g_e$ and $Y(a \cdot u, v) + g_o$.

Formalized by `Cslib.Algorithms.Lean.gotohContGapX_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean, line 531](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean#L531). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/gotoh-affine-gap-alignment/index.html#gotoh-cont-gap-x-eq).

## First-column recurrence for the continuation after a gap in the first sequence

Fix an
integer-valued scoring function $\sigma$ on pairs of letters and integer gap-open and gap-extend
penalties $g_o$ and $g_e$. For sequences $u$, $v$ let $N(u, v)$, $X(u, v)$ and $Y(u, v)$ be the
Gotoh continuation values when the previous column was a match, a gap in $v$ and a gap in $u$
respectively, and write $a \cdot u$ for the sequence with first letter $a$ followed by $u$. For
all letters $a$, $b$ and sequences $u$, $v$, the value $Y(a \cdot u, b \cdot v)$ is the maximum
of $N(u, v) + \sigma(a, b)$, $X(u, b \cdot v) + g_o$ and $Y(a \cdot u, v) + g_e$.

Formalized by `Cslib.Algorithms.Lean.gotohContGapY_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean, line 546](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean#L546). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/gotoh-affine-gap-alignment/index.html#gotoh-cont-gap-y-eq).

## Gotoh value against an empty first sequence

Let $g_o$ and $g_e$ be the gap-open and
gap-extend scores. For every sequence $y$ of length $n$, the Gotoh value with no open gap run of
the empty sequence against $y$ equals the score of a freshly opened run of $n$ gaps in the first
sequence: $0$ if $n = 0$, and $g_o + (n - 1) g_e$ if $n \ge 1$.

Formalized by `Cslib.Algorithms.Lean.gotohContNone_nil_left`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean, line 561](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean#L561). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/gotoh-affine-gap-alignment/index.html#gotoh-cont-none-nil-left).

## Gotoh value against an empty second sequence

Let $g_o$ and $g_e$ be the gap-open and
gap-extend scores. For every sequence $x$ of length $n$, the Gotoh value with no open gap run of
$x$ against the empty sequence equals the score of a freshly opened run of $n$ gaps in the second
sequence: $0$ if $n = 0$, and $g_o + (n - 1) g_e$ if $n \ge 1$.

Formalized by `Cslib.Algorithms.Lean.gotohContNone_nil_right`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean, line 567](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean#L567). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/gotoh-affine-gap-alignment/index.html#gotoh-cont-none-nil-right).

## Continuation after a gap in the second sequence, empty first sequence

Fix a scoring
function $\sigma$ on pairs of letters and integer gap-open and gap-extend penalties $g_o$ and
$g_e$, and let $X(u, v)$ be the Gotoh continuation value of sequences $u$, $v$ when the previous
column was a gap in $v$. For every sequence $v$ of length $k$, the value $X(\varepsilon, v)$,
where $\varepsilon$ is the empty sequence, is the cost of one freshly opened gap run of length
$k$: it is $0$ if $k = 0$ and $g_o + (k - 1) g_e$ if $k \ge 1$.

Formalized by `Cslib.Algorithms.Lean.gotohContGapX_nil_left`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean, line 573](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean#L573). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/gotoh-affine-gap-alignment/index.html#gotoh-cont-gap-x-nil-left).

## Continuation after a gap in the second sequence, empty second sequence

Fix a scoring
function $\sigma$ on pairs of letters and integer gap-open and gap-extend penalties $g_o$ and
$g_e$, and let $X(u, v)$ be the Gotoh continuation value of sequences $u$, $v$ when the previous
column was a gap in $v$. For every sequence $u$ of length $k$, the value $X(u, \varepsilon)$,
where $\varepsilon$ is the empty sequence, equals $k \, g_e$: the open gap run is extended by
$k$ columns.

Formalized by `Cslib.Algorithms.Lean.gotohContGapX_nil_right`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean, line 579](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean#L579). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/gotoh-affine-gap-alignment/index.html#gotoh-cont-gap-x-nil-right).

## Continuation after a gap in the first sequence, empty first sequence

Fix a scoring
function $\sigma$ on pairs of letters and integer gap-open and gap-extend penalties $g_o$ and
$g_e$, and let $Y(u, v)$ be the Gotoh continuation value of sequences $u$, $v$ when the previous
column was a gap in $u$. For every sequence $v$ of length $k$, the value $Y(\varepsilon, v)$,
where $\varepsilon$ is the empty sequence, equals $k \, g_e$: the open gap run is extended by
$k$ columns.

Formalized by `Cslib.Algorithms.Lean.gotohContGapY_nil_left`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean, line 585](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean#L585). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/gotoh-affine-gap-alignment/index.html#gotoh-cont-gap-y-nil-left).

## Continuation after a gap in the first sequence, empty second sequence

Fix a scoring
function $\sigma$ on pairs of letters and integer gap-open and gap-extend penalties $g_o$ and
$g_e$, and let $Y(u, v)$ be the Gotoh continuation value of sequences $u$, $v$ when the previous
column was a gap in $u$. For every sequence $u$ of length $k$, the value $Y(u, \varepsilon)$,
where $\varepsilon$ is the empty sequence, is the cost of one freshly opened gap run of length
$k$: it is $0$ if $k = 0$ and $g_o + (k - 1) g_e$ if $k \ge 1$.

Formalized by `Cslib.Algorithms.Lean.gotohContGapY_nil_right`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean, line 591](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean#L591). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/gotoh-affine-gap-alignment/index.html#gotoh-cont-gap-y-nil-right).

## Linear gaps as affine gaps, from any gap state

Let $\sigma$ be an integer substitution
score and $g$ an integer. If the gap-open cost and the gap-extend cost both equal $g$, then for
every alignment $A$ and every gap state $p$, the affine-gap score of $A$ started from state $p$,
with substitution score $\sigma$, equals the alignment score of $A$ with substitution score
$\sigma$ and gap penalty $g$.

Formalized by `Cslib.Algorithms.Lean.affineScoreAux_eq_alignmentScore`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean, line 598](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean#L598). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/gotoh-affine-gap-alignment/index.html#affine-score-aux-eq-alignment-score).

## Linear gaps are affine gaps with equal costs

Let $\sigma$ be an integer substitution
score and $g$ an integer. If the gap-open cost and the gap-extend cost both equal $g$, then for
every alignment $A$, the affine-gap score of $A$ with substitution score $\sigma$ equals the
alignment score of $A$ with substitution score $\sigma$ and gap penalty $g$.

Formalized by `Cslib.Algorithms.Lean.affineScore_eq_alignmentScore`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean, line 642](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean#L642). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/gotoh-affine-gap-alignment/index.html#affine-score-eq-alignment-score).

## Gotoh with equal gap scores is Needleman–Wunsch

Let $\sigma$ be a substitution score
and $g$ an integer. If the gap-open and gap-extend scores both equal $g$, then for all sequences
$x$ and $y$ the Gotoh score (optimal affine-gap alignment score) of $x$ and $y$ equals the
Needleman–Wunsch score of $x$ and $y$ with substitution score $\sigma$ and gap score $g$.

Formalized by `Cslib.Algorithms.Lean.gotohScore_eq_nwScore`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean, line 649](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/AffineAlignment.lean#L649). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/gotoh-affine-gap-alignment/index.html#gotoh-score-eq-nw-score).

## Specification of a Gotoh table cell

The specification of a cell: the three continuation values `(M, X, Y)` of the suffix pair
`(xs, ys)`, given that the previous column was a match, a gap in `ys`, or a gap in `xs`.

Formalized by `Cslib.Bioinformatics.Alignment.Gotoh.cellSpec`, a definition declared in [CSLibExt/Bioinformatics/Alignment/GotohTable.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Alignment/GotohTable.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/gotoh-affine-gap-alignment/index.html#cell-spec).

## Gotoh cell recurrence from diagonal, upper and left cells

The cell of `(a :: xs, b :: ys)` from the cells `diag` of `(xs, ys)`, `up` of `(xs, b :: ys)`
and `left` of `(a :: xs, ys)`: a match continues from `M`, a gap in `ys` from `X` (extending if
the previous column was one), a gap in `xs` from `Y`.

Formalized by `Cslib.Bioinformatics.Alignment.Gotoh.step`, a definition declared in [CSLibExt/Bioinformatics/Alignment/GotohTable.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Alignment/GotohTable.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/gotoh-affine-gap-alignment/index.html#step).

## Gotoh cell recurrence against an empty second suffix

The cell of `(a :: xs, [])` from the cell `o` of `(xs, [])`: one more gap column in `ys`.

Formalized by `Cslib.Bioinformatics.Alignment.Gotoh.stepX`, a definition declared in [CSLibExt/Bioinformatics/Alignment/GotohTable.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Alignment/GotohTable.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/gotoh-affine-gap-alignment/index.html#step-x).

## Gotoh table row of the empty first suffix

The row of the suffix `[]` of `xs`: the cells of `([], t)` for the suffixes `t` of `ys`,
longest first, each one gap column in `xs` more than the next.

Formalized by `Cslib.Bioinformatics.Alignment.Gotoh.firstRow`, a definition declared in [CSLibExt/Bioinformatics/Alignment/GotohTable.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Alignment/GotohTable.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/gotoh-affine-gap-alignment/index.html#first-row).

## Gotoh table row from the previous row

The row of `a :: xs` from the row `prev` of `xs`, over the remaining suffixes of `ys`, longest
first; each cell uses the cell to its right in the same row. A row `prev` that is too short gives
junk cells (this does not happen for rows of the table, `nextRow_eq`).

Formalized by `Cslib.Bioinformatics.Alignment.Gotoh.nextRow`, a definition declared in [CSLibExt/Bioinformatics/Alignment/GotohTable.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Alignment/GotohTable.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/gotoh-affine-gap-alignment/index.html#next-row).

## Gotoh table row of a suffix of the first sequence

The row of the suffix `xs` (of the first sequence) of the table, computed from the rows of
its shorter suffixes.

Formalized by `Cslib.Bioinformatics.Alignment.Gotoh.gotohRows`, a definition declared in [CSLibExt/Bioinformatics/Alignment/GotohTable.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Alignment/GotohTable.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/gotoh-affine-gap-alignment/index.html#gotoh-rows).

## The Gotoh table

The `M` value of the cell `(xs, ys)`.

Formalized by `Cslib.Bioinformatics.Alignment.Gotoh.gotohTab`, a definition declared in [CSLibExt/Bioinformatics/Alignment/GotohTable.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Alignment/GotohTable.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/gotoh-affine-gap-alignment/index.html#gotoh-tab).

## The first row

`firstRow ys` holds the cells of `([], t)` for the suffixes `t` of `ys`.

Formalized by `Cslib.Bioinformatics.Alignment.Gotoh.firstRow_eq`, a theorem declared in [CSLibExt/Bioinformatics/Alignment/GotohTable.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Alignment/GotohTable.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/gotoh-affine-gap-alignment/index.html#first-row-eq).

## One row of the table

From the row of the suffix `xs`, `nextRow` computes the row of
`a :: xs`: the cells `cellSpec (a :: xs) t` for the suffixes `t` of `ys`, longest first.

Formalized by `Cslib.Bioinformatics.Alignment.Gotoh.nextRow_eq`, a theorem declared in [CSLibExt/Bioinformatics/Alignment/GotohTable.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Alignment/GotohTable.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/gotoh-affine-gap-alignment/index.html#next-row-eq).

## The rows of the table

The row of `xs` holds `cellSpec xs t` for every suffix `t` of
`ys`, longest first.

Formalized by `Cslib.Bioinformatics.Alignment.Gotoh.gotohRows_eq`, a theorem declared in [CSLibExt/Bioinformatics/Alignment/GotohTable.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Alignment/GotohTable.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/gotoh-affine-gap-alignment/index.html#gotoh-rows-eq).

## The table computes the optimal affine-gap score

**The table computes the optimal affine-gap score** (Gotoh 1982): `gotohTab = gotohScore`.

Formalized by `Cslib.Bioinformatics.Alignment.Gotoh.gotohTab_eq_gotohScore`, a theorem declared in [CSLibExt/Bioinformatics/Alignment/GotohTable.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Alignment/GotohTable.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/gotoh-affine-gap-alignment/index.html#gotoh-tab-eq-gotoh-score).

## The table is an upper bound

Every alignment of `xs` and `ys` has affine-gap score at
most `gotohTab`.

Formalized by `Cslib.Bioinformatics.Alignment.Gotoh.affineScore_le_gotohTab`, a theorem declared in [CSLibExt/Bioinformatics/Alignment/GotohTable.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Alignment/GotohTable.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/gotoh-affine-gap-alignment/index.html#affine-score-le-gotoh-tab).

## The table is attained

Some alignment of `xs` and `ys` has affine-gap score `gotohTab`.

Formalized by `Cslib.Bioinformatics.Alignment.Gotoh.exists_affineScore_eq_gotohTab`, a theorem declared in [CSLibExt/Bioinformatics/Alignment/GotohTable.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Alignment/GotohTable.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/gotoh-affine-gap-alignment/index.html#exists-affine-score-eq-gotoh-tab).

## Gotoh table with equal gap costs gives the Needleman–Wunsch score

With `gapOpen = gapExtend = gap`, the Gotoh table computes the linear-gap Needleman–Wunsch
score.

Formalized by `Cslib.Bioinformatics.Alignment.Gotoh.gotohTab_eq_nwScore`, a theorem declared in [CSLibExt/Bioinformatics/Alignment/GotohTable.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Alignment/GotohTable.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/gotoh-affine-gap-alignment/index.html#gotoh-tab-eq-nw-score).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Gotoh affine-gap alignment](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/gotoh-affine-gap-alignment/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/bioinformatics/sequence-alignment/gotoh-affine-gap-alignment)
