---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.bestArgmax, Cslib.Algorithms.Lean.bestArgmax_le, Cslib.Algorithms.Lean.bestArgmax_spec, Cslib.Algorithms.Lean.splitScore_le_nwScore_ys, Cslib.Algorithms.Lean.splitScore_le_nwScore_xs, Cslib.Algorithms.Lean.exists_split_eq_nwScore_ys, Cslib.Algorithms.Lean.exists_split_eq_nwScore_xs, Cslib.Algorithms.Lean.nwScore_eq_bestSplit_ys
statement: formalized
proof: formalized
---

# Hirschberg's linear-space alignment

22 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/hirschberg-s-linear-space-alignment/index.html).

## Argmax over an initial segment

For a function $f : \mathbb{N} \to \mathbb{Z}$ and
$n \in \mathbb{N}$, the argmax of $f$ over $\{0, \dots, n\}$ is the least $k \le n$ such that
$f(j) \le f(k)$ for all $j \le n$.

It is computed as the first maximizer of $f$ on the list $[0, 1, \dots, n]$, which is never
empty.

Formalized by `Cslib.Algorithms.Lean.bestArgmax`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/HirschbergAlignment.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/HirschbergAlignment.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/hirschberg-s-linear-space-alignment/index.html#best-argmax).

## The argmax over $\{0, \dots, n\}$ is at most $n$

For every function
$f : \mathbb{N} \to \mathbb{Z}$ and every $n \in \mathbb{N}$, the argmax of $f$ over
$\{0, \dots, n\}$ is at most $n$.

Formalized by `Cslib.Algorithms.Lean.bestArgmax_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/HirschbergAlignment.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/HirschbergAlignment.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/hirschberg-s-linear-space-alignment/index.html#best-argmax-le).

## The argmax over $\{0, \dots, n\}$ maximizes the function there

Let
$f : \mathbb{N} \to \mathbb{Z}$, let $n \in \mathbb{N}$ and let $m$ be the argmax of $f$ over
$\{0, \dots, n\}$. Then $f(k) \le f(m)$ for every $k \le n$.

Formalized by `Cslib.Algorithms.Lean.bestArgmax_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/HirschbergAlignment.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/HirschbergAlignment.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/hirschberg-s-linear-space-alignment/index.html#best-argmax-spec).

## A split of the second sequence scores at most the Needleman–Wunsch optimum

Let
$\sigma$ be an integer-valued substitution score on an alphabet, let $g$ be an integer gap
score, and write $\mathrm{NW}(x, y)$ for the optimal Needleman–Wunsch global alignment score
of sequences $x$ and $y$ under $\sigma$ and $g$. For sequences $x$, $y$ and natural numbers
$k$, $m$, let $x_{\lt k}$ be the first $k$ letters of $x$ (all of $x$ if $k$ is at least its
length) and $x_{\ge k}$ the remaining letters, and define $y_{\lt m}$ and $y_{\ge m}$ likewise.
Then $\mathrm{NW}(x_{\lt k}, y_{\lt m}) + \mathrm{NW}(x_{\ge k}, y_{\ge m}) \le \mathrm{NW}(x, y)$.

The bound holds because optimal alignments of the two halves concatenate to an alignment of
$x$ and $y$.

Formalized by `Cslib.Algorithms.Lean.splitScore_le_nwScore_ys`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/HirschbergAlignment.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/HirschbergAlignment.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/hirschberg-s-linear-space-alignment/index.html#split-score-le-nw-score-ys).

## A split of the first sequence scores at most the Needleman–Wunsch optimum

Let
$\sigma$ be an integer-valued substitution score on an alphabet, let $g$ be an integer gap
score, and write $\mathrm{NW}(x, y)$ for the optimal Needleman–Wunsch global alignment score
of sequences $x$ and $y$ under $\sigma$ and $g$. For sequences $x$, $y$ and natural numbers
$m$, $k$, let $x_{\lt m}$ be the first $m$ letters of $x$ (all of $x$ if $m$ is at least its
length) and $x_{\ge m}$ the remaining letters, and define $y_{\lt k}$ and $y_{\ge k}$ likewise.
Then $\mathrm{NW}(x_{\lt m}, y_{\lt k}) + \mathrm{NW}(x_{\ge m}, y_{\ge k}) \le \mathrm{NW}(x, y)$.

Formalized by `Cslib.Algorithms.Lean.splitScore_le_nwScore_xs`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/HirschbergAlignment.lean, line 266](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/HirschbergAlignment.lean#L266). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/hirschberg-s-linear-space-alignment/index.html#split-score-le-nw-score-xs).

## Every cut of the second list extends to an optimal split

Fix a type $\alpha$, a
substitution score $\sigma : \alpha \to \alpha \to \mathbb{Z}$ and a gap score $g \in \mathbb{Z}$.
Write $S(u, v)$ for the Needleman–Wunsch score of lists $u$, $v$, and $u_{\lt m}$ for the first
$m$ elements of $u$ and $u_{\ge m}$ for the rest. For all lists $xs$, $ys$ over $\alpha$ and
every $m \le |ys|$, there is $k \le |xs|$ with
$S(xs_{\lt k}, ys_{\lt m}) + S(xs_{\ge k}, ys_{\ge m}) = S(xs, ys)$.

Formalized by `Cslib.Algorithms.Lean.exists_split_eq_nwScore_ys`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/HirschbergAlignment.lean, line 279](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/HirschbergAlignment.lean#L279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/hirschberg-s-linear-space-alignment/index.html#exists-split-eq-nw-score-ys).

## Every cut of the first list extends to an optimal split

Fix a type $\alpha$, a
substitution score $\sigma : \alpha \to \alpha \to \mathbb{Z}$ and a gap score $g \in \mathbb{Z}$.
Write $S(u, v)$ for the Needleman–Wunsch score of lists $u$, $v$, and $u_{\lt m}$ for the first
$m$ elements of $u$ and $u_{\ge m}$ for the rest. For all lists $xs$, $ys$ over $\alpha$ and
every $m \le |xs|$, there is $k \le |ys|$ with
$S(xs_{\lt m}, ys_{\lt k}) + S(xs_{\ge m}, ys_{\ge k}) = S(xs, ys)$.

Formalized by `Cslib.Algorithms.Lean.exists_split_eq_nwScore_xs`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/HirschbergAlignment.lean, line 294](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/HirschbergAlignment.lean#L294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/hirschberg-s-linear-space-alignment/index.html#exists-split-eq-nw-score-xs).

## Hirschberg split identity, splitting the second sequence

Fix a substitution score
$\sigma$ assigning an integer to each pair of letters and an integer gap score $g$, and write
$\mathrm{NW}$ for the Needleman–Wunsch score. For a sequence $s$, write $s_{\lt j}$ for its first
$j$ letters and $s_{\ge j}$ for the remaining letters. Let $x$, $y$ be sequences and
$m \le |y|$, and let $k$ be the first index $j \in \{0, \dots, |x|\}$ that maximizes
$\mathrm{NW}(x_{\lt j}, y_{\lt m}) + \mathrm{NW}(x_{\ge j}, y_{\ge m})$. Then
$\mathrm{NW}(x_{\lt k}, y_{\lt m}) + \mathrm{NW}(x_{\ge k}, y_{\ge m}) = \mathrm{NW}(x, y)$.

Formalized by `Cslib.Algorithms.Lean.nwScore_eq_bestSplit_ys`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/HirschbergAlignment.lean, line 309](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/HirschbergAlignment.lean#L309). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/hirschberg-s-linear-space-alignment/index.html#nw-score-eq-best-split-ys).

## Hirschberg split identity, splitting the first sequence

Fix a substitution score
$\sigma$ assigning an integer to each pair of letters and an integer gap score $g$, and write
$\mathrm{NW}$ for the Needleman–Wunsch score. For a sequence $s$, write $s_{\lt j}$ for its first
$j$ letters and $s_{\ge j}$ for the remaining letters. Let $x$, $y$ be sequences and
$m \le |x|$, and let $k$ be the first index $j \in \{0, \dots, |y|\}$ that maximizes
$\mathrm{NW}(x_{\lt m}, y_{\lt j}) + \mathrm{NW}(x_{\ge m}, y_{\ge j})$. Then
$\mathrm{NW}(x_{\lt m}, y_{\lt k}) + \mathrm{NW}(x_{\ge m}, y_{\ge k}) = \mathrm{NW}(x, y)$.

Formalized by `Cslib.Algorithms.Lean.nwScore_eq_bestSplit_xs`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/HirschbergAlignment.lean, line 338](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/HirschbergAlignment.lean#L338). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/hirschberg-s-linear-space-alignment/index.html#nw-score-eq-best-split-xs).

## Needleman–Wunsch score of two single letters

For every substitution score $\sigma$
assigning an integer to each pair of letters, integer gap score $g$ and letters $a$, $b$, the
Needleman–Wunsch score of the one-letter sequences $[a]$ and $[b]$ is
$\max(\sigma(a, b), g + g)$: the better of matching $a$ with $b$ and gapping both.

Formalized by `Cslib.Algorithms.Lean.nwScore_singleton_singleton`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/HirschbergAlignment.lean, line 368](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/HirschbergAlignment.lean#L368). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/hirschberg-s-linear-space-alignment/index.html#nw-score-singleton-singleton).

## Base-case alignment for Hirschberg

Fix a substitution score $\sigma$ assigning an
integer to each pair of letters and an integer gap score $g$, and write a column as a pair
whose missing entry, a gap, is marked $\bot$. The base-case alignment of sequences $x$ and $y$
is the empty alignment if both are empty; the single column $(\bot, b)$ if $x$ is empty and
$y = [b]$; the single column $(a, \bot)$ if $x = [a]$ and $y$ is empty; if $x = [a]$ and
$y = [b]$, it is the single column $(a, b)$ when $\sigma(a, b) \ge 2g$ and the two columns
$(a, \bot)$, $(\bot, b)$ otherwise; and it is the empty alignment when $x$ or $y$ has length
at least $2$.

Formalized by `Cslib.Algorithms.Lean.smallAlign`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/HirschbergAlignment.lean, line 376](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/HirschbergAlignment.lean#L376). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/hirschberg-s-linear-space-alignment/index.html#small-align).

## The base-case alignment is valid

For every substitution score $\sigma$ assigning an
integer to each pair of letters, integer gap score $g$ and sequences $x$, $y$ with
$|x| \le 1$ and $|y| \le 1$, the base-case alignment of $x$ and $y$ is a valid alignment of
$x$ and $y$.

Formalized by `Cslib.Algorithms.Lean.isAlignment_smallAlign`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/HirschbergAlignment.lean, line 385](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/HirschbergAlignment.lean#L385). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/hirschberg-s-linear-space-alignment/index.html#is-alignment-small-align).

## The base-case alignment is optimal

Fix a type $\alpha$, a substitution score
$\sigma : \alpha \to \alpha \to \mathbb{Z}$ and a gap score $g \in \mathbb{Z}$. For all lists
$xs$, $ys$ over $\alpha$ with $|xs| \le 1$ and $|ys| \le 1$, the alignment score of the
base-case alignment of $xs$ and $ys$ equals the Needleman–Wunsch score of $xs$ and $ys$.

Formalized by `Cslib.Algorithms.Lean.alignmentScore_smallAlign_eq_nwScore`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/HirschbergAlignment.lean, line 432](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/HirschbergAlignment.lean#L432). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/hirschberg-s-linear-space-alignment/index.html#alignment-score-small-align-eq-nw-score).

## Hirschberg reconstruction with fuel

Fix a substitution score $\sigma$ assigning an
integer to each pair of letters and an integer gap score $g$, and write $\mathrm{NW}$ for the
Needleman–Wunsch score. For a sequence $s$, write $s_{\lt j}$ for its first $j$ letters and
$s_{\ge j}$ for the remaining letters. The Hirschberg reconstruction of sequences $x$ and $y$
with fuel $n$ is the alignment defined by recursion on $n$. With fuel $0$ it is the empty
alignment. With fuel $n + 1$: if $|x| \le 1$ and $|y| \le 1$, it is the base-case alignment
of $x$ and $y$; otherwise, if $|y| \ge |x|$, let $m = \lfloor |y|/2 \rfloor$ and let $k$ be
the first index $j \in \{0, \dots, |x|\}$ that maximizes
$\mathrm{NW}(x_{\lt j}, y_{\lt m}) + \mathrm{NW}(x_{\ge j}, y_{\ge m})$, and the result is the
concatenation of the reconstructions with fuel $n$ of $x_{\lt k}$ and $y_{\lt m}$ and of $x_{\ge k}$
and $y_{\ge m}$; otherwise, let $m = \lfloor |x|/2 \rfloor$ and let $k$ be the first index
$j \in \{0, \dots, |y|\}$ that maximizes
$\mathrm{NW}(x_{\lt m}, y_{\lt j}) + \mathrm{NW}(x_{\ge m}, y_{\ge j})$, and the result is the
concatenation of the reconstructions with fuel $n$ of $x_{\lt m}$ and $y_{\lt k}$ and of $x_{\ge m}$
and $y_{\ge k}$.

Hirschberg's alignment algorithm runs this reconstruction with fuel $|x| + |y|$.

Formalized by `Cslib.Algorithms.Lean.hirschbergAlign`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/HirschbergAlignment.lean, line 487](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/HirschbergAlignment.lean#L487). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/hirschberg-s-linear-space-alignment/index.html#hirschberg-align).

## Hirschberg reconstruction on lists of length at most one

Fix a type $\alpha$, a
substitution score $\sigma : \alpha \to \alpha \to \mathbb{Z}$ and a gap score $g \in \mathbb{Z}$.
For every $n \in \mathbb{N}$ and all lists $xs$, $ys$ over $\alpha$ with $|xs| \le 1$ and
$|ys| \le 1$, the Hirschberg reconstruction of $xs$ and $ys$ with fuel $n + 1$ is the
base-case alignment of $xs$ and $ys$.

Formalized by `Cslib.Algorithms.Lean.hirschbergAlign_small`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/HirschbergAlignment.lean, line 516](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/HirschbergAlignment.lean#L516). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/hirschberg-s-linear-space-alignment/index.html#hirschberg-align-small).

## Hirschberg recursion step splitting the second sequence

Fix a substitution score
$\sigma$ assigning an integer to each pair of letters and an integer gap score $g$, and write
$\mathrm{NW}$ for the Needleman–Wunsch score. For a sequence $s$, write $s_{\lt j}$ for its first
$j$ letters and $s_{\ge j}$ for the remaining letters. Let $x$, $y$ be sequences with
$|y| \ge |x|$ that do not both have length at most $1$, let $m = \lfloor |y|/2 \rfloor$, and
let $k$ be the first index $j \in \{0, \dots, |x|\}$ that maximizes
$\mathrm{NW}(x_{\lt j}, y_{\lt m}) + \mathrm{NW}(x_{\ge j}, y_{\ge m})$. Then for every natural
number $n$, the Hirschberg reconstruction of $x$ and $y$ with fuel $n + 1$ is the
concatenation of the Hirschberg reconstruction of $x_{\lt k}$ and $y_{\lt m}$ with fuel $n$ and the
Hirschberg reconstruction of $x_{\ge k}$ and $y_{\ge m}$ with fuel $n$.

Formalized by `Cslib.Algorithms.Lean.hirschbergAlign_split_ys`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/HirschbergAlignment.lean, line 526](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/HirschbergAlignment.lean#L526). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/hirschberg-s-linear-space-alignment/index.html#hirschberg-align-split-ys).

## Hirschberg reconstruction splits the longer first list

Fix a type $\alpha$, a
substitution score $\sigma : \alpha \to \alpha \to \mathbb{Z}$ and a gap score $g \in \mathbb{Z}$.
Write $H_n(u, v)$ for the Hirschberg reconstruction of lists $u$, $v$ with fuel $n$, $S(u, v)$
for their Needleman–Wunsch score, and $u_{\lt m}$, $u_{\ge m}$ for the first $m$ elements of $u$
and the rest. Let $xs$, $ys$ be lists over $\alpha$ that are not both of length at most $1$,
with $|ys| < |xs|$. Put $h = \lfloor |xs| / 2 \rfloor$ and let $k$ be the least maximizer over
$\{0, \dots, |ys|\}$ of $j \mapsto S(xs_{\lt h}, ys_{\lt j}) + S(xs_{\ge h}, ys_{\ge j})$. Then
for every $n \in \mathbb{N}$, $H_{n+1}(xs, ys)$ is the concatenation of
$H_n(xs_{\lt h}, ys_{\lt k})$ and $H_n(xs_{\ge h}, ys_{\ge k})$.

Formalized by `Cslib.Algorithms.Lean.hirschbergAlign_split_xs`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/HirschbergAlignment.lean, line 549](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/HirschbergAlignment.lean#L549). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/hirschberg-s-linear-space-alignment/index.html#hirschberg-align-split-xs).

## Hirschberg reconstruction with enough fuel is valid

For every substitution score
$\sigma$ assigning an integer to each pair of letters, integer gap score $g$, natural number
$n$ and sequences $x$, $y$ with $|x| + |y| \le n$, the Hirschberg reconstruction of $x$ and
$y$ with fuel $n$ is a valid alignment of $x$ and $y$.

Formalized by `Cslib.Algorithms.Lean.isAlignment_hirschbergAlign`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/HirschbergAlignment.lean, line 574](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/HirschbergAlignment.lean#L574). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/hirschberg-s-linear-space-alignment/index.html#is-alignment-hirschberg-align).

## Hirschberg reconstruction with enough fuel attains the optimum

Fix a type $\alpha$, a
substitution score $\sigma : \alpha \to \alpha \to \mathbb{Z}$ and a gap score $g \in \mathbb{Z}$.
For every fuel $n \in \mathbb{N}$ and all lists $xs$, $ys$ over $\alpha$ with
$|xs| + |ys| \le n$, the alignment score of the Hirschberg reconstruction of $xs$ and $ys$ with
fuel $n$ equals the Needleman–Wunsch score of $xs$ and $ys$.

Formalized by `Cslib.Algorithms.Lean.alignmentScore_hirschbergAlign`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/HirschbergAlignment.lean, line 631](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/HirschbergAlignment.lean#L631). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/hirschberg-s-linear-space-alignment/index.html#alignment-score-hirschberg-align).

## Hirschberg's alignment algorithm

Fix a substitution score $\sigma$ assigning an integer
to each pair of letters and an integer gap score $g$. The Hirschberg alignment of sequences $x$
and $y$ is the Hirschberg reconstruction of $x$ and $y$ with fuel $|x| + |y|$.

Formalized by `Cslib.Algorithms.Lean.hirschberg`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/HirschbergAlignment.lean, line 689](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/HirschbergAlignment.lean#L689). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/hirschberg-s-linear-space-alignment/index.html#hirschberg).

## Hirschberg reconstruction is valid

For every substitution score $\sigma$ assigning an
integer to each pair of letters, integer gap score $g$ and sequences $x$, $y$, the Hirschberg
alignment of $x$ and $y$ is a valid alignment of $x$ and $y$.

Formalized by `Cslib.Algorithms.Lean.isAlignment_hirschberg`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/HirschbergAlignment.lean, line 693](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/HirschbergAlignment.lean#L693). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/hirschberg-s-linear-space-alignment/index.html#is-alignment-hirschberg).

## Hirschberg reconstruction attains the Needleman–Wunsch optimum

Fix a type $\alpha$, a
substitution score $\sigma : \alpha \to \alpha \to \mathbb{Z}$ and a gap score $g \in \mathbb{Z}$.
For all lists $xs$, $ys$ over $\alpha$, the alignment score of the Hirschberg alignment of $xs$
and $ys$ equals the Needleman–Wunsch score of $xs$ and $ys$.

Formalized by `Cslib.Algorithms.Lean.alignmentScore_hirschberg`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/HirschbergAlignment.lean, line 698](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/HirschbergAlignment.lean#L698). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/hirschberg-s-linear-space-alignment/index.html#alignment-score-hirschberg).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hirschberg's linear-space alignment](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/hirschberg-s-linear-space-alignment/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/bioinformatics/sequence-alignment/hirschberg-s-linear-space-alignment)
