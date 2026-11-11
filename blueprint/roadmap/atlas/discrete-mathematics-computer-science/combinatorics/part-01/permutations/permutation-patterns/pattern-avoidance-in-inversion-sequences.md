---
declaration: section
origin: cited
lean: MetaMathlibExt.InvSeqContainsPattern, MetaMathlibExt.not_invSeqContainsPattern_of_lt, MetaMathlibExt.invSeqAvoidCount, MetaMathlibExt.invSeqAvoidCount_one, MetaMathlibExt.invSeqAvoidGF, MetaMathlibExt.coeff_invSeqAvoidGF, MetaMathlibExt.invSeq_wilf_000_010_100_120_101_110, MetaMathlibExt.invSeq_wilf_000_010_120_five_class
statement: formalized
---

# Pattern avoidance in inversion sequences

82 results, 16 proved and 66 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html).

## Containment of a length-3 pattern

A sequence $e = e_0 e_1 \cdots e_{n-1}$ of natural
numbers contains the length-3 pattern $p = p_0 p_1 p_2$ of natural numbers when there are
positions $i_0 < i_1 < i_2$ in $\{0, \dots, n - 1\}$ such that, for all $a, b \in \{0, 1, 2\}$,
$e_{i_a} < e_{i_b}$ if and only if $p_a < p_b$; that is, the subsequence $e_{i_0} e_{i_1} e_{i_2}$
is order-isomorphic to $p$.

## Sources

- Toufik Mansour, *Inversion Sequences Avoiding a Set of Length-3 Patterns*, INTEGERS 24 (2024), Article A76, Introduction.

Formalized by `MetaMathlibExt.InvSeqContainsPattern`, a definition declared in [WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#inv-seq-contains-pattern).

## Short sequences contain no length-3 pattern

If $n < 3$, then no sequence
$e_0 e_1 \cdots e_{n-1}$ of natural numbers contains a length-3 pattern $p$.

## Sources

- Toufik Mansour, *Inversion Sequences Avoiding a Set of Length-3 Patterns*, INTEGERS 24 (2024), Article A76, Introduction.

Formalized by `MetaMathlibExt.not_invSeqContainsPattern_of_lt`, a theorem declared in [WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#not-inv-seq-contains-pattern-of-lt).

## Number of inversion sequences avoiding a set of patterns

An inversion sequence of length
$n$ is a sequence $e = e_0 e_1 \cdots e_{n-1}$ of natural numbers with $e_i \le i$ for every $i$.
It contains a length-3 pattern $p = p_0 p_1 p_2$ (a triple of natural numbers) when some
subsequence $e_a e_b e_c$ with $a < b < c$ is order-isomorphic to $p$. For a set $B$ of length-3
patterns, $|I_n(B)|$ is the number of inversion sequences of length $n$ that contain no pattern
of $B$.

## Sources

- Toufik Mansour, *Inversion Sequences Avoiding a Set of Length-3 Patterns*, INTEGERS 24 (2024), Article A76, Introduction.

Formalized by `MetaMathlibExt.invSeqAvoidCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#inv-seq-avoid-count).

## One inversion sequence of length one

For every set $B$ of length-3 patterns, the number
$|I_1(B)|$ of inversion sequences of length one that avoid every pattern in $B$ equals $1$: the
only inversion sequence of length one is $0$, and it avoids every length-3 pattern.

## Sources

- Toufik Mansour, *Inversion Sequences Avoiding a Set of Length-3 Patterns*, INTEGERS 24 (2024), Article A76, Introduction.

Formalized by `MetaMathlibExt.invSeqAvoidCount_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#inv-seq-avoid-count-one).

## Generating function of inversion sequences avoiding a set of patterns

For a set $B$ of
length-3 patterns, $F_B(x) = \sum_{n \ge 1} |I_n(B)| x^n$ is the formal power series in
$\mathbb{Q}[[x]]$ with constant coefficient $0$ whose coefficient of $x^n$, for $n \ge 1$, is the
number $|I_n(B)|$ of inversion sequences of length $n$ that avoid every pattern in $B$.

## Sources

- Toufik Mansour, *Inversion Sequences Avoiding a Set of Length-3 Patterns*, INTEGERS 24 (2024), Article A76, Section 2.

Formalized by `MetaMathlibExt.invSeqAvoidGF`, a definition declared in [WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#inv-seq-avoid-gf).

## Coefficients of the generating function of pattern-avoiding inversion sequences

For
every set $B$ of length-3 patterns and every $n \ge 0$, the generating function
$F_B(x) = \sum_{m \ge 1} |I_m(B)| x^m \in \mathbb{Q}[[x]]$ has constant coefficient $0$, and its
coefficient of $x^{n+1}$ is $|I_{n+1}(B)|$, the number of inversion sequences of length $n + 1$
that avoid every pattern in $B$.

## Sources

- Toufik Mansour, *Inversion Sequences Avoiding a Set of Length-3 Patterns*, INTEGERS 24 (2024), Article A76, Section 2.

Formalized by `MetaMathlibExt.coeff_invSeqAvoidGF`, a theorem declared in [WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#coeff-inv-seq-avoid-gf).

## I-Wilf equivalence of $\{000, 010, 100, 101, 120\}$ and $\{000, 010, 100, 110, 120\}$

Write length-3 patterns as digit strings ($101$ is the pattern $(1, 0, 1)$) and let $|I_n(B)|$ be
the number of inversion sequences of length $n$ that avoid every pattern in the set $B$. Then for
every $n \ge 0$, $|I_n(\{000, 010, 100, 101, 120\})| = |I_n(\{000, 010, 100, 110, 120\})|$.

## Sources

- Toufik Mansour, *Inversion Sequences Avoiding a Set of Length-3 Patterns*, INTEGERS 24 (2024), Article A76, Theorem 4.

Stated but not proved: `MetaMathlibExt.invSeq_wilf_000_010_100_120_101_110` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#inv-seq-wilf-000-010-100-120-101-110).

## Three I-Wilf-equivalent sets of five patterns containing $000$, $010$ and $120$

Write
length-3 patterns as digit strings ($101$ is the pattern $(1, 0, 1)$) and let $|I_n(B)|$ be the
number of inversion sequences of length $n$ that avoid every pattern in the set $B$. For
$B_1 = \{000, 010, 101, 120, 201\}$, $B_2 = \{000, 010, 101, 120, 210\}$ and
$B_3 = \{000, 010, 110, 120, 210\}$, and for every $n \ge 0$,
$|I_n(B_1)| = |I_n(B_2)| = |I_n(B_3)|$.

## Sources

- Toufik Mansour, *Inversion Sequences Avoiding a Set of Length-3 Patterns*, INTEGERS 24 (2024), Article A76, Theorem 5.

Stated but not proved: `MetaMathlibExt.invSeq_wilf_000_010_120_five_class` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#inv-seq-wilf-000-010-120-five-class).

## Inversion sequences avoiding $\{011, 102, 120\}$

Let $B = \{011, 102, 120\}$, where a
pattern is written as a digit string ($101$ is the triple $(1, 0, 1)$), and let
$F_B(x) = \sum_{n \ge 1} |I_n(B)| x^n \in \mathbb{Q}[[x]]$ be the generating function of the
inversion sequences avoiding every pattern in $B$. Then

$$(1 - 2x)^2 F_B(x) = x(1 - x)^2.$$

Since $(1 - 2x)^2$ is a unit in $\mathbb{Q}[[x]]$, this says $F_B(x) = x(1 - x)^2/(1 - 2x)^2$.

## Sources

- Toufik Mansour, *Inversion Sequences Avoiding a Set of Length-3 Patterns*, INTEGERS 24 (2024), Article A76, Theorem 6.

Stated but not proved: `MetaMathlibExt.invSeqAvoidGF_011_102_120` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#inv-seq-avoid-gf-011-102-120).

## Three I-Wilf-equivalent sets of five patterns containing $000$, $102$ and $120$

Write
length-3 patterns as digit strings ($101$ is the pattern $(1, 0, 1)$) and let $|I_n(B)|$ be the
number of inversion sequences of length $n$ that avoid every pattern in the set $B$. For
$B_1 = \{000, 101, 102, 120, 201\}$, $B_2 = \{000, 101, 102, 120, 210\}$ and
$B_3 = \{000, 102, 110, 120, 210\}$, and for every $n \ge 0$,
$|I_n(B_1)| = |I_n(B_2)| = |I_n(B_3)|$.

## Sources

- Toufik Mansour, *Inversion Sequences Avoiding a Set of Length-3 Patterns*, INTEGERS 24 (2024), Article A76, Theorem 7.

Stated but not proved: `MetaMathlibExt.invSeq_wilf_000_102_120_five_class` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#inv-seq-wilf-000-102-120-five-class).

## Two I-Wilf equivalences exchanging $201$ and $210$ in five-pattern sets

Write
length-3 patterns as digit strings ($101$ is the pattern $(1, 0, 1)$) and let $|I_n(B)|$ be the
number of inversion sequences of length $n$ that avoid every pattern in the set $B$. For a pattern
$\tau$ let $A_\tau = \{000, 100, 101, 120, \tau\}$ and $B_\tau = \{000, 100, 110, 120, \tau\}$.
Then for every $n \ge 0$, $|I_n(A_{201})| = |I_n(A_{210})|$ and $|I_n(B_{201})| = |I_n(B_{210})|$.

## Sources

- Toufik Mansour, *Inversion Sequences Avoiding a Set of Length-3 Patterns*, INTEGERS 24 (2024), Article A76, Theorem 8.

Stated but not proved: `MetaMathlibExt.invSeq_wilf_000_100_120_201_210` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#inv-seq-wilf-000-100-120-201-210).

## I-Wilf equivalences among five-pattern sets containing $010$, $102$ and $120$

Write
length-3 patterns as digit strings ($101$ is the pattern $(1, 0, 1)$) and let $|I_n(B)|$ be the
number of inversion sequences of length $n$ that avoid every pattern in the set $B$. For a pattern
$\tau$ let $A_\tau = \{010, \tau, 102, 120, 201\}$ and $A'_\tau = \{010, \tau, 102, 120, 210\}$,
and let $B = \{010, 101, 102, 120, 201\}$. Then for every $n \ge 0$,
$|I_n(A_{100})| = |I_n(A_{110})|$ and
$|I_n(A'_{100})| = |I_n(A'_{101})| = |I_n(A'_{110})| = |I_n(B)|$.

## Sources

- Toufik Mansour, *Inversion Sequences Avoiding a Set of Length-3 Patterns*, INTEGERS 24 (2024), Article A76, Theorem 9.

Stated but not proved: `MetaMathlibExt.invSeq_wilf_010_102_120_five_classes` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#inv-seq-wilf-010-102-120-five-classes).

## I-Wilf equivalence of $\{010, 100, 101, 120, 201\}$ and $\{010, 100, 101, 120, 210\}$

Write length-3 patterns as digit strings ($101$ is the pattern $(1, 0, 1)$) and let $|I_n(B)|$ be
the number of inversion sequences of length $n$ that avoid every pattern in the set $B$. Then for
every $n \ge 0$, $|I_n(\{010, 100, 101, 120, 201\})| = |I_n(\{010, 100, 101, 120, 210\})|$.

## Sources

- Toufik Mansour, *Inversion Sequences Avoiding a Set of Length-3 Patterns*, INTEGERS 24 (2024), Article A76, Theorem 11.

Stated but not proved: `MetaMathlibExt.invSeq_wilf_010_100_101_120_201_210` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#inv-seq-wilf-010-100-101-120-201-210).

## Five I-Wilf-equivalent sets of six patterns containing $000$, $010$ and $120$

Write
length-3 patterns as digit strings ($101$ is the pattern $(1, 0, 1)$) and let $|I_n(B)|$ be the
number of inversion sequences of length $n$ that avoid every pattern in the set $B$. For a pattern
$\tau$ let $A_\tau = \{000, 010, 100, 101, 120, \tau\}$ and $B_\tau = \{000, 010, 100, 110, 120,
\tau\}$, and let $C = \{000, 010, 101, 110, 120, 201\}$. Then for every $n \ge 0$,
$|I_n(A_{201})| = |I_n(A_{210})| = |I_n(B_{201})| = |I_n(B_{210})| = |I_n(C)|$.

## Sources

- Toufik Mansour, *Inversion Sequences Avoiding a Set of Length-3 Patterns*, INTEGERS 24 (2024), Article A76, Theorem 13.

Stated but not proved: `MetaMathlibExt.invSeq_wilf_000_010_120_six_class` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#inv-seq-wilf-000-010-120-six-class).

## Three I-Wilf-equivalent six-pattern sets containing 102 and 110

Write a length-3 pattern
as the word of its values, so $101$ is the pattern $(1, 0, 1)$, and for a set $B$ of patterns let
$|I_n(B)|$ be the number of inversion sequences of length $n$ that avoid every pattern in $B$.
Let $A_\tau = \{011, 101, 102, 110, 120, \tau\}$ and $C = \{011, 021, 102, 110, 201, 210\}$.
Then $|I_n(A_{201})| = |I_n(A_{210})| = |I_n(C)|$ for every $n \ge 0$.

## Sources

- Toufik Mansour, *Inversion Sequences Avoiding a Set of Length-3 Patterns*, INTEGERS 24 (2024), Article A76, Theorem 14.

Stated but not proved: `MetaMathlibExt.invSeq_wilf_102_110_six_class` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#inv-seq-wilf-102-110-six-class).

## A common generating function for three sets of seven patterns

Let
$B_1 = \{010, 011, 100, 101, 102, 201, 210\}$, $B_2 = \{010, 011, 100, 102, 110, 201, 210\}$ and
$B_3 = \{010, 011, 101, 102, 110, 201, 210\}$, where a pattern is written as a digit string ($101$
is the triple $(1, 0, 1)$). For a set $B$ of patterns let
$F_B(x) = \sum_{n \ge 1} |I_n(B)| x^n \in \mathbb{Q}[[x]]$ be the generating function of the
inversion sequences avoiding every pattern in $B$. Then for each $j \in \{1, 2, 3\}$,

$$(1 - x)(1 - 2x)^2 F_{B_j}(x) = x(1 - 2x)^2 + x^2(1 - x)^2.$$

Since $(1 - x)(1 - 2x)^2$ is a unit in $\mathbb{Q}[[x]]$, this says
$F_{B_j}(x) = x/(1 - x) + x^2(1 - x)/(1 - 2x)^2$.

## Sources

- Toufik Mansour, *Inversion Sequences Avoiding a Set of Length-3 Patterns*, INTEGERS 24 (2024), Article A76, Theorem 16.

Stated but not proved: `MetaMathlibExt.invSeqAvoidGF_010_011_102_201_210_seven` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#inv-seq-avoid-gf-010-011-102-201-210-sev).

## Eight-pattern sets differing in 201 and 210: equivalence and generating function

Write a
length-3 pattern as the word of its values, so $101$ is the pattern $(1, 0, 1)$. For a set $B$ of
patterns let $|I_n(B)|$ be the number of inversion sequences of length $n$ that avoid every
pattern in $B$, and let $F_B(x) = \sum_{n \ge 1} |I_n(B)| x^n \in \mathbb{Q}[[x]]$. Let
$B_\tau = \{000, 010, 100, 101, 102, 110, 120, \tau\}$. Then $|I_n(B_{201})| = |I_n(B_{210})|$
for every $n \ge 0$, and for every power series $s \in \mathbb{Q}[[x]]$ with constant term $1$
and $s^2 = 1 - 2x - 3x^2$,

$$
2x^3 (1 + x)(x^2 + 2x + 2) F_{B_{201}}(x) =
1 - x^2 - 4x^3 - 7x^4 - 5x^5 - 2x^6 - (1 + x + 2x^2 + 2x^3 + x^4) s.
$$

This is the paper's closed form for $F_{B_{201}}$ with the denominator cleared, where $s$ plays
the role of $\sqrt{1 - 2x - 3x^2}$.

## Sources

- Toufik Mansour, *Inversion Sequences Avoiding a Set of Length-3 Patterns*, INTEGERS 24 (2024), Article A76, Theorem 17.

Stated but not proved: `MetaMathlibExt.invSeq_wilf_eight_201_210_and_gf` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#inv-seq-wilf-eight-201-210-and-gf).

## A common generating function for three sets of eight patterns

Let
$B_1 = \{000, 010, 100, 101, 102, 120, 201, 210\}$,
$B_2 = \{000, 010, 100, 102, 110, 120, 201, 210\}$ and
$B_3 = \{000, 010, 101, 102, 110, 120, 201, 210\}$, where a pattern is written as a digit string
($101$ is the triple $(1, 0, 1)$). For a set $B$ of patterns let
$F_B(x) = \sum_{n \ge 1} |I_n(B)| x^n \in \mathbb{Q}[[x]]$ be the generating function of the
inversion sequences avoiding every pattern in $B$. For each $j \in \{1, 2, 3\}$ and every power
series $s \in \mathbb{Q}[[x]]$ with constant term $1$ and $s^2 = 1 - 2x - 3x^2$,

$$x^2 F_{B_j}(x) = 1 - 2x - x^2 + x^3 - (1 - x) s.$$

This is the closed form $F_{B_j}(x) = (1 - 2x - x^2 + x^3 - (1 - x)\sqrt{1 - 2x - 3x^2}) / x^2$
with the denominator cleared, $s$ standing for $\sqrt{1 - 2x - 3x^2}$.

## Sources

- Toufik Mansour, *Inversion Sequences Avoiding a Set of Length-3 Patterns*, INTEGERS 24 (2024), Article A76, Theorem 18.

Stated but not proved: `MetaMathlibExt.invSeqAvoidGF_eight_radical_three` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#inv-seq-avoid-gf-eight-radical-three).

## Inversion sequences avoiding $\{000, 100, 101, 102, 110, 120, 201, 210\}$

Let
$B = \{000, 100, 101, 102, 110, 120, 201, 210\}$, where a pattern is written as a digit string
($101$ is the triple $(1, 0, 1)$), and let
$F_B(x) = \sum_{n \ge 1} |I_n(B)| x^n \in \mathbb{Q}[[x]]$ be the generating function of the
inversion sequences avoiding every pattern in $B$. For every power series $s \in \mathbb{Q}[[x]]$
with constant term $1$ and $s^2 = 1 - 2x - 3x^2$,

$$2x^2(1 + x) F_B(x) = 2 - 2x - 5x^2 - x^3 - (2 - x^2) s.$$

This is the closed form
$F_B(x) = (2 - 2x - 5x^2 - x^3 - (2 - x^2)\sqrt{1 - 2x - 3x^2}) / (2x^2(1 + x))$ with the
denominator cleared, $s$ standing for $\sqrt{1 - 2x - 3x^2}$.

## Sources

- Toufik Mansour, *Inversion Sequences Avoiding a Set of Length-3 Patterns*, INTEGERS 24 (2024), Article A76, Theorem 21.

Stated but not proved: `MetaMathlibExt.invSeqAvoidGF_000_100_101_102_110_120_201_210` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean, line 291](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean#L291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#inv-seq-avoid-gf-000-100-101-102-110-120).

## Inversion sequences avoiding nine patterns

Let
$B = \{000, 010, 100, 101, 102, 110, 120, 201, 210\}$, where a pattern is written as a digit
string ($101$ is the triple $(1, 0, 1)$), and let
$F_B(x) = \sum_{n \ge 1} |I_n(B)| x^n \in \mathbb{Q}[[x]]$ be the generating function of the
inversion sequences avoiding every pattern in $B$. For every power series $s \in \mathbb{Q}[[x]]$
with constant term $1$ and $s^2 = 1 - 2x - 3x^2$,

$$2x^2(1 + x) F_B(x) = 2 - 3x - 3x^2 + (x - 2) s.$$

This is the closed form
$F_B(x) = (2 - 3x - 3x^2 + (x - 2)\sqrt{1 - 2x - 3x^2}) / (2x^2(1 + x))$ with the denominator
cleared, $s$ standing for $\sqrt{1 - 2x - 3x^2}$.

## Sources

- Toufik Mansour, *Inversion Sequences Avoiding a Set of Length-3 Patterns*, INTEGERS 24 (2024), Article A76, Theorem 22.

Stated but not proved: `MetaMathlibExt.invSeqAvoidGF_nine_patterns` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean, line 306](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean#L306). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#inv-seq-avoid-gf-nine-patterns).

## Number of I-Wilf classes of sets of length-3 patterns

Let $P$ be the set of the thirteen
length-3 patterns $000, 001, 010, 011, 012, 021, 100, 101, 102, 110, 120, 201, 210$, each written
as the word of its values. For $B \subseteq P$ let $|I_n(B)|$ be the number of inversion sequences
of length $n$ that avoid every pattern in $B$, and let $w_d$ be the number of distinct sequences
$(|I_n(B)|)_{n \ge 0}$ as $B$ ranges over the $d$-element subsets of $P$ (the number of
I-Wilf-equivalence classes of such sets). Then $w_5 = 219$, $w_6 = 167$, $w_7 = 105$, $w_8 = 61$,
$w_9 = 35$, $w_{10} = 21$, $w_{11} = 10$, $w_{12} = 4$ and $w_{13} = 1$.

## Sources

- Toufik Mansour, *Inversion Sequences Avoiding a Set of Length-3 Patterns*, INTEGERS 24 (2024), Article A76, Theorem 1.

Stated but not proved: `MetaMathlibExt.invSeq_wilfClassCount` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean, line 321](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean#L321). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#inv-seq-wilf-class-count).

## Reducible sets of length-3 patterns for inversion sequences

An inversion sequence of
length $n$ is a sequence $e_0 e_1 \cdots e_{n-1}$ of natural numbers with $e_i \le i$ for all $i$;
write a length-3 pattern as a digit string ($101$ is the pattern $(1, 0, 1)$). For each pair
$(C, \tau)$ listed below and every $n$, every inversion sequence of length $n$ that avoids every
pattern in $C$ also avoids $\tau$, so $C \cup \{\tau\}$ and $C$ are avoided by the same inversion
sequences. The pairs are: $C = \{001\}$ with $\tau \in \{101, 102, 201\}$;
$C = \{011\}$ with $\tau \in \{101, 110\}$; $C = \{012\}$ with $\tau \in \{102, 120\}$;
$C = \{021\}$ with $\tau \in \{201, 210\}$; $C = \{000, 001\}$ with $\tau = 100$;
$C = \{000, 011\}$ with $\tau \in \{100, 201, 210\}$;
$C = \{000, 012\}$ with $\tau \in \{201, 210\}$; $C = \{000, 021\}$ with $\tau = 100$;
$C = \{001, 010\}$ with $\tau \in \{021, 100, 110, 120, 210\}$;
$C = \{001, 011\}$ with $\tau = 021$; $C = \{001, 012\}$ with $\tau = 021$;
$C = \{001, 110\}$ with $\tau = 210$; $C = \{001, 120\}$ with $\tau = 210$;
$C = \{010, 011\}$ with $\tau = 100$; $C = \{010, 012\}$ with $\tau \in \{101, 201\}$;
$C = \{010, 021\}$ with $\tau \in \{100, 101, 102, 110, 120\}$;
$C = \{001, 011, 012\}$ with $\tau = 210$; $C = \{001, 011, 100\}$ with $\tau = 210$; and
$C = \{001, 012, 100\}$ with $\tau = 210$.

## Sources

- Toufik Mansour, *Inversion Sequences Avoiding a Set of Length-3 Patterns*, INTEGERS 24 (2024), Article A76, Theorem 2.

Stated but not proved: `MetaMathlibExt.invSeq_reducible_pattern_sets` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean, line 337](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean#L337). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#inv-seq-reducible-pattern-sets).

## A Catalan generating function for two sets of five patterns

Let
$B = \{010, 101, 102, 201, 210\}$ and $B' = \{011, 101, 110, 201, 210\}$, where a pattern is
written as a digit string ($101$ is the triple $(1, 0, 1)$). For a set $A$ of patterns let
$F_A(x) = \sum_{n \ge 1} |I_n(A)| x^n \in \mathbb{Q}[[x]]$ be the generating function of the
inversion sequences avoiding every pattern in $A$, and let $C(x) = \sum_{n \ge 0} C_n x^n$ be the
generating function of the Catalan numbers $C_n = \binom{2n}{n}/(n + 1)$. Then $F_B = F_{B'}$
and

$$(1 - x)(2 - C(x)) F_B(x) = x.$$

Since $C(x) = (1 - \sqrt{1 - 4x})/(2x)$ and $(1 - x)(2 - C(x))$ is a unit in $\mathbb{Q}[[x]]$,
this says $F_B(x) = F_{B'}(x) = x / ((1 - x)(2 - (1 - \sqrt{1 - 4x})/(2x)))$.

## Sources

- Toufik Mansour, *Inversion Sequences Avoiding a Set of Length-3 Patterns*, INTEGERS 24 (2024), Article A76, Theorem 3.

Stated but not proved: `MetaMathlibExt.invSeqAvoidGF_010_101_102_201_210_catalan` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean, line 385](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean#L385). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#inv-seq-avoid-gf-010-101-102-201-210-cat).

## I-Wilf-equivalence of 101 and 110 alongside 102, 120, 210

Write a length-3 pattern as the
word of its values, so $101$ is the pattern $(1, 0, 1)$, and for a set $S$ of patterns let
$|I_n(S)|$ be the number of inversion sequences of length $n$ that avoid every pattern in $S$.
Let $B_\tau = \{100, \tau, 102, 120, 210\}$ and $C_\tau = \{\tau, 102, 120, 201, 210\}$. Then for
every $n \ge 0$, $|I_n(B_{101})| = |I_n(B_{110})|$ and $|I_n(C_{101})| = |I_n(C_{110})|$.

The paper's Theorem 10 also claims $|I_n(A_{101})| = |I_n(A_{110})|$ for all $n$, where
$A_\tau = \{100, \tau, 102, 120, 201\}$; that claim is false, since for $n = 6$ the two counts
are $206$ and $205$.

## Sources

- Toufik Mansour, *Inversion Sequences Avoiding a Set of Length-3 Patterns*, INTEGERS 24 (2024), Article A76, Theorem 10.

Stated but not proved: `MetaMathlibExt.invSeq_wilf_102_120_101_110_parts_B_C` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean, line 400](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean#L400). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#inv-seq-wilf-102-120-101-110-parts-b-c).

## I-Wilf-equivalence of 101 and 110 alongside 010, 120, 201, 210

Write a length-3 pattern
as the word of its values, so $101$ is the pattern $(1, 0, 1)$, and for a set $B$ of patterns let
$|I_n(B)|$ be the number of inversion sequences of length $n$ that avoid every pattern in $B$.
For every $n \ge 0$,

$$|I_n(\{010, 101, 120, 201, 210\})| = |I_n(\{010, 110, 120, 201, 210\})|.$$

The paper's Theorem 12 also claims this equality for $\{100, 101, 120, 201, 210\}$ and
$\{100, 110, 120, 201, 210\}$; that claim is false, since for $n = 5$ the two counts are $79$
and $81$.

## Sources

- Toufik Mansour, *Inversion Sequences Avoiding a Set of Length-3 Patterns*, INTEGERS 24 (2024), Article A76, Theorem 12.

Stated but not proved: `MetaMathlibExt.invSeq_wilf_010_120_201_210_101_110` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean, line 416](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean#L416). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#inv-seq-wilf-010-120-201-210-101-110).

## Exchanging $201$ and $210$ in $\{010, 100, 101, 102, 120, 201\}$

Write length-3
patterns as digit strings ($101$ is the pattern $(1, 0, 1)$) and let $|I_n(B)|$ be the number of
inversion sequences of length $n$ that avoid every pattern in the set $B$. For a pattern $\tau$
let $A_\tau = \{010, 100, 101, 102, 120, \tau\}$. Then for every $n \ge 0$,
$|I_n(A_{201})| = |I_n(A_{210})|$.

The source further claims $|I_n(A_{210})| = |I_n(B)| = |I_n(C)|$ for all $n$, with
$B = \{010, 100, 110, 102, 120, 201\}$ and $C = \{010, 101, 110, 102, 120, 210\}$; these claims are
false as printed ($|I_7| = 538, 537, 539$ for $A_{210}$, $B$, $C$) and are omitted.

## Sources

- Toufik Mansour, *Inversion Sequences Avoiding a Set of Length-3 Patterns*, INTEGERS 24 (2024), Article A76, Theorem 15.

Stated but not proved: `MetaMathlibExt.invSeq_wilf_010_100_101_102_120_201_210` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean, line 429](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/InversionSequencePatternSetsWanted.lean#L429). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#inv-seq-wilf-010-100-101-102-120-201-210).

## Length-2 signed pattern

A length-2 signed pattern is a word $\tau_1\tau_2$ whose
underlying word $|\tau_1||\tau_2|$ is $00$, $01$ or $10$ and each of whose letters may be barred,
for example $\bar10$ or $0\bar1$. It is given by the comparison of $|\tau_1|$ with $|\tau_2|$
(equal for $00$, less for $01$, greater for $10$) together with whether $\tau_1$ is barred and
whether $\tau_2$ is barred.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Introduction.

Formalized by `MetaMathlibExt.SignedPattern2`, a structure declared in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-pattern2).

## Number of length-2 signed patterns

There are exactly twelve length-2 signed patterns.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Section 5 (`binom 12 k` sets of `k` patterns).

Formalized by `MetaMathlibExt.card_signedPattern2`, a theorem declared in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#card-signed-pattern2).

## Containment of a length-2 signed pattern

Let $e = e_1 \cdots e_n$ be a sequence whose
entries are natural numbers $|e_i|$, each barred or not, and let $\tau_1\tau_2$ be a length-2
signed pattern. Then $e$ contains $\tau_1\tau_2$ if there are positions $i < j$ such that $|e_i|$
is equal to, smaller than or larger than $|e_j|$ exactly as $|\tau_1|$ is equal to, smaller than
or larger than $|\tau_2|$, and $e_i$ and $e_j$ are barred exactly when $\tau_1$ and $\tau_2$ are.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Introduction.

Formalized by `MetaMathlibExt.SignedInvSeqContains`, a definition declared in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-inv-seq-contains).

## Number of signed inversion sequences avoiding a set of patterns

A signed inversion
sequence of length $n$ is a word $e_1 \cdots e_n$ in which each entry $e_i$ is a natural number
$|e_i| \le i - 1$, either barred or not; that is, $e_i \in \lbrace 0, \bar 0, 1, \bar 1, \dots,
i - 1, \overline{i - 1} \rbrace$. For a finite set $B$ of length-2 signed patterns and $n \ge 0$,
$|\bar I_n(B)|$ is the number of signed inversion sequences of length $n$ that contain no pattern
of $B$.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Introduction.

Formalized by `MetaMathlibExt.signedInvAvoidCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-inv-avoid-count).

## Signed inversion sequences of length zero

The empty sequence is the only signed inversion
sequence of length $0$, and it contains no pattern, so for every finite set $B$ of length-2 signed
patterns the number $|\bar I_0(B)|$ of signed inversion sequences of length $0$ avoiding every
pattern of $B$ is $1$.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Introduction.

Formalized by `MetaMathlibExt.signedInvAvoidCount_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-inv-avoid-count-zero).

## Signed inversion sequences of length one

The signed inversion sequences of length $1$ are
$0$ and $\bar 0$, and neither contains a length-2 signed pattern, so for every finite set $B$ of
length-2 signed patterns the number $|\bar I_1(B)|$ of signed inversion sequences of length $1$
avoiding every pattern of $B$ is $2$.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Introduction.

Formalized by `MetaMathlibExt.signedInvAvoidCount_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-inv-avoid-count-one).

## Generating function of signed inversion sequences avoiding a set of patterns

For a finite
set $B$ of length-2 signed patterns, $F_B(x) = \sum_{n \ge 0} |\bar I_n(B)| x^n$ is the formal
power series with rational coefficients whose coefficient of $x^n$ is the number $|\bar I_n(B)|$
of signed inversion sequences of length $n$ avoiding every pattern of $B$.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Section 2.

Formalized by `MetaMathlibExt.signedInvAvoidGF`, a definition declared in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-inv-avoid-gf).

## Coefficients of the avoidance generating function

For a finite set $B$ of length-2
signed patterns and $m \ge 0$, let $|\bar I_m(B)|$ be the number of signed inversion sequences of
length $m$ avoiding every pattern of $B$, and let $F_B(x) = \sum_{m \ge 0} |\bar I_m(B)| x^m$ be
their generating function, a formal power series with rational coefficients. Then for every
$n \ge 0$ the coefficient of $x^n$ in $F_B(x)$ is $|\bar I_n(B)|$, viewed as a rational number.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Section 2.

Formalized by `MetaMathlibExt.coeff_signedInvAvoidGF`, a theorem declared in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#coeff-signed-inv-avoid-gf).

## Number of signed Wilf classes

For $k \ge 0$, $\mathrm{sw}_k$ is the number of
Wilf-equivalence classes among the sets of $k$ length-2 signed patterns, that is, the number of
distinct counting functions $n \mapsto |\bar{I}_n(B)|$ (for $n \ge 0$) over all sets $B$ of exactly
$k$ length-2 signed patterns, where $|\bar{I}_n(B)|$ is the number of signed inversion sequences of
length $n$ avoiding every pattern of $B$.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Theorem 1.

Formalized by `MetaMathlibExt.signedWilfClassCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-wilf-class-count).

## The empty pattern set forms one signed Wilf class

The number $\mathrm{sw}_0$ of
Wilf-equivalence classes among the sets of $0$ length-2 signed patterns is $1$: the empty set is
the only set of no patterns.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Theorem 1 (definition of `sw_k`).

Formalized by `MetaMathlibExt.signedWilfClassCount_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-wilf-class-count-zero).

## Mansour–Safadi Lemma 1 (signed patterns 0̄1̄, 0̄0, 01)

A signed inversion sequence of
length $n$ is a word $e_1 \cdots e_n$ with $e_k \in \{0, \bar 0, 1, \bar 1, \dots, k - 1,
\overline{k - 1}\}$. It avoids a length-2 signed pattern $\tau_1\tau_2$ (one of $00$, $01$, $10$,
each letter possibly barred) when no $i < j$ have $|e_i|$, $|e_j|$ in the same order as $|\tau_1|$,
$|\tau_2|$ with $e_i$, $e_j$ barred exactly when $\tau_1$, $\tau_2$ are. Write $\bar I_n(B)$ for the
set of signed inversion sequences of length $n$ that avoid every pattern in $B$, and
$F_B(x) = \sum_{n \ge 0} |\bar I_n(B)|\,x^n$ in $\mathbb{Q}[[x]]$. Let
$B_1 = \{\bar 0\bar 1, \bar 0 0, 01\}$ and $B_2 = \{\bar 0\bar 1, \bar 0 1, 01\}$. Then
$|\bar I_n(B_1)| = |\bar I_n(B_2)|$ for every $n \ge 0$, and $(1 - 3x + x^2)\,F_{B_1}(x) = 1 - x$,
that is, $F_{B_1}(x) = (1 - x)/(1 - 3x + x^2)$.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Lemma 1.

Stated but not proved: `MetaMathlibExt.signedInvSeq_wilf_and_gf_b0b1_b00_01` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-inv-seq-wilf-and-gf-b0b1-b00-01).

## Wilf-equivalence and count for \{0̄0̄, 0̄0, 01̄} (Lemma 2)

Write a length-2 signed pattern
as $\tau_1\tau_2$, where $00$, $01$ and $10$ record whether $|\tau_1|$ is equal to, smaller than
or larger than $|\tau_2|$ and a bar marks a barred letter, and write $|\bar I_n(B)|$ for the
number of signed inversion sequences of length $n$ avoiding every pattern of a set $B$ of such
patterns. Let $B = \lbrace \bar 0\bar 0, \bar 0 0, 0\bar 1 \rbrace$ and
$C = \lbrace \bar 0 0, \bar 0 1, 0\bar 1 \rbrace$. Then $B$ and $C$ are Wilf-equivalent, that is,
$|\bar I_n(B)| = |\bar I_n(C)|$ for every $n \ge 0$, and for every $n \ge 0$,

$$
|\bar I_n(B)| = 1 + \sum_{j=0}^{n-1} (2j + 1)\, j!.
$$

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Lemma 2.

Stated but not proved: `MetaMathlibExt.signedInvSeq_wilf_and_count_b0b0_b00_0b1` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-inv-seq-wilf-and-count-b0b0-b00-0).

## Mansour–Safadi Lemma 3 (signed patterns 0̄1̄, 0̄0̄, 01̄)

A signed inversion sequence of
length $n$ is a word $e_1 \cdots e_n$ with $e_k \in \{0, \bar 0, 1, \bar 1, \dots, k - 1,
\overline{k - 1}\}$. It avoids a length-2 signed pattern $\tau_1\tau_2$ (one of $00$, $01$, $10$,
each letter possibly barred) when no $i < j$ have $|e_i|$, $|e_j|$ in the same order as $|\tau_1|$,
$|\tau_2|$ with $e_i$, $e_j$ barred exactly when $\tau_1$, $\tau_2$ are. Write $\bar I_n(B)$ for the
set of signed inversion sequences of length $n$ that avoid every pattern in $B$. Let
$B_1 = \{\bar 0\bar 1, \bar 0\bar 0, 0\bar 1\}$, $B_2 = \{\bar 0\bar 1, \bar 0 0, 0\bar 1\}$ and
$B_3 = \{\bar 0\bar 1, 0\bar 1, 0\bar 0\}$. For every $n \ge 0$,
$|\bar I_n(B_1)| = |\bar I_n(B_2)| = |\bar I_n(B_3)| = n!\,(1 + H_n)$, where
$H_n = \sum_{k=1}^{n} 1/k$ is the $n$th harmonic number.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Lemma 3.

Stated but not proved: `MetaMathlibExt.signedInvSeq_wilf_and_count_b0b1_b0b0_0b1` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-inv-seq-wilf-and-count-b0b1-b0b0).

## Mansour–Safadi Lemma 4 (signed patterns 0̄1̄, 0̄0̄, 0̄1)

A signed inversion sequence of
length $n$ is a word $e_1 \cdots e_n$ with $e_k \in \{0, \bar 0, 1, \bar 1, \dots, k - 1,
\overline{k - 1}\}$. It avoids a length-2 signed pattern $\tau_1\tau_2$ (one of $00$, $01$, $10$,
each letter possibly barred) when no $i < j$ have $|e_i|$, $|e_j|$ in the same order as $|\tau_1|$,
$|\tau_2|$ with $e_i$, $e_j$ barred exactly when $\tau_1$, $\tau_2$ are. Write $\bar I_n(B)$ for the
set of signed inversion sequences of length $n$ that avoid every pattern in $B$. For every
$n \ge 0$, $|\bar I_n(\{\bar 0\bar 1, \bar 0\bar 0, \bar 0 1\})| =
|\bar I_n(\{\bar 0\bar 1, \bar 0 0, \bar 0 1\})| = \sum_{j=0}^{n} j!\,(j + 1)^{n - j}$.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Lemma 4.

Stated but not proved: `MetaMathlibExt.signedInvSeq_wilf_and_count_b0b1_b0b0_b01` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-inv-seq-wilf-and-count-b0b1-b0b0-2).

## Signed inversion sequences avoiding $\{\bar1\bar0, \bar0\bar1, 01\}$

For a set $B$ of
length-2 signed patterns (a bar marks a barred letter), let $|\bar I_n(B)|$ be the number of signed
inversion sequences of length $n$ avoiding every pattern of $B$, and let
$F_B(x) = \sum_{n \ge 0} |\bar I_n(B)| x^n \in \mathbb{Q}[[x]]$. Let
$B = \{\bar1\bar0, \bar0\bar1, 01\}$ and $C = \{\bar10, \bar0\bar1, 01\}$. Then
$|\bar I_n(B)| = |\bar I_n(C)|$ for every $n \ge 0$, and

$$
(1 - 2x)(1 - 3x + x^2)(1 - x)^2 F_B(x) = (1 - 2x)(1 - 3x + x^2)(1 - x)^2 + x(1 - x)^4 +
x(1 - x + x^2)(1 - 3x + x^2),
$$

that is,
$F_B(x) = 1 + \frac{x(1 - x)^2}{(1 - 2x)(1 - 3x + x^2)} + \frac{x(1 - x + x^2)}{(1 - 2x)(1 - x)^2}$.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Lemma 5.

Stated but not proved: `MetaMathlibExt.signedInvSeq_wilf_and_gf_b1b0_b0b1_01` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-inv-seq-wilf-and-gf-b1b0-b0b1-01).

## Mansour–Safadi Lemma 6

Write $\bar{I}_n(B)$ for the set of signed inversion
sequences of length $n$ that avoid every length-2 signed pattern in $B$, where a pattern is
one of $00$, $01$, $10$ with a bar over each barred letter. Then for every $n \ge 0$,
$|\bar{I}_n(\{\bar{1}\bar{0}, \bar{0}\bar{0}, \bar{0}1\})| =
|\bar{I}_n(\{\bar{1}\bar{0}, \bar{0}0, \bar{0}1\})|$.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Lemma 6.

Stated but not proved: `MetaMathlibExt.signedInvSeq_wilf_b1b0_b0b0_b01` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-inv-seq-wilf-b1b0-b0b0-b01).

## Mansour–Safadi Lemma 7

Write $\bar{I}_n(B)$ for the set of signed inversion
sequences of length $n$ that avoid every length-2 signed pattern in $B$, where a pattern is
one of $00$, $01$, $10$ with a bar over each barred letter. Then for every $n \ge 0$,
$|\bar{I}_n(\{\bar{1}0, \bar{0}\bar{1}, \bar{0}\bar{0}\})| =
|\bar{I}_n(\{\bar{1}0, \bar{0}\bar{1}, \bar{0}0\})|$.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Lemma 7.

Stated but not proved: `MetaMathlibExt.signedInvSeq_wilf_b10_b0b1_b0b0` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-inv-seq-wilf-b10-b0b1-b0b0).

## Eight signed-pattern triples with (n + 1)! avoiders (Lemma 8)

Write a length-2 signed
pattern as $\tau_1\tau_2$, where $00$, $01$ and $10$ record whether $|\tau_1|$ is equal to, smaller
than or larger than $|\tau_2|$ and a bar marks a barred letter, and write $|\bar I_n(B)|$ for the
number of signed inversion sequences of length $n$ avoiding every pattern of a set $B$ of such
patterns. For every $n \ge 0$ and each of the eight sets
$B = \lbrace \bar 1\bar 0, \bar 0\bar 1, \bar 0\bar 0 \rbrace$,
$\lbrace \bar 1\bar 0, \bar 0\bar 1, \bar 0 0 \rbrace$,
$\lbrace \bar 1\bar 0, \bar 0\bar 1, 0\bar 1 \rbrace$,
$\lbrace \bar 1 0, \bar 0\bar 1, 0\bar 1 \rbrace$,
$\lbrace \bar 1 0, \bar 0 0, \bar 0 1 \rbrace$,
$\lbrace \bar 1\bar 0, \bar 0\bar 1, 0\bar 0 \rbrace$,
$\lbrace \bar 1 0, \bar 0 0, 0\bar 1 \rbrace$ and
$\lbrace \bar 1 0, 0\bar 0, 0\bar 1 \rbrace$, we have $|\bar I_n(B)| = (n+1)!$.

The source prints an unbarred $I_n$ in parts (iii) and (iv); it is read as $\bar I_n$.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Lemma 8.

Stated but not proved: `MetaMathlibExt.signedInvAvoidCount_eq_factorial_succ` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-inv-avoid-count-eq-factorial-succ).

## Mansour–Safadi Lemma 9: a Wilf-equivalence of three-pattern sets

Length-2 signed
patterns are written as in the paper, a bar marking a barred letter, and $B \sim C$ means that
for every $n \ge 0$ the number $|\bar I_n(B)|$ of signed inversion sequences of length $n$
avoiding every pattern of $B$ equals $|\bar I_n(C)|$. Then
$\{\bar1\bar0, \bar10, \bar0\bar0\} \sim \{\bar1\bar0, \bar10, \bar00\}$.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Lemma 9.

Stated but not proved: `MetaMathlibExt.signedInvSeq_wilf_b1b0_b10_b0b0` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-inv-seq-wilf-b1b0-b10-b0b0).

## Mansour–Safadi Lemma 10

Write $\bar{I}_n(B)$ for the set of signed inversion
sequences of length $n$ that avoid every length-2 signed pattern in $B$, where a pattern is
one of $00$, $01$, $10$ with a bar over each barred letter. Then for every $n \ge 0$,
$|\bar{I}_n(\{\bar{1}\bar{0}, \bar{0}\bar{0}, 1\bar{0}\})| =
|\bar{I}_n(\{\bar{1}\bar{0}, 0\bar{0}, 1\bar{0}\})|$.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Lemma 10.

Stated but not proved: `MetaMathlibExt.signedInvSeq_wilf_b1b0_b0b0_1b0` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-inv-seq-wilf-b1b0-b0b0-1b0).

## Signed Wilf classes of sets of three to twelve patterns

Let $\mathrm{sw}_k$ be the number
of Wilf-equivalence classes among the sets of $k$ length-2 signed patterns. Then
$\mathrm{sw}_3 = 93$, $\mathrm{sw}_4 = 195$, $239 \le \mathrm{sw}_5 \le 240$, $\mathrm{sw}_6 = 190$,
$\mathrm{sw}_7 = 107$, $\mathrm{sw}_8 = 49$, $\mathrm{sw}_9 = 22$, $\mathrm{sw}_{10} = 8$,
$\mathrm{sw}_{11} = 3$ and $\mathrm{sw}_{12} = 1$.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Theorem 1.

Stated but not proved: `MetaMathlibExt.signedWilfClassCount_three_to_twelve` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-wilf-class-count-three-to-twelve).

## Mansour–Safadi Class 141 Wilf-equivalence

Length-2 signed patterns are written as in
the paper, a bar marking a barred letter, and $B \sim C$ means that for every $n \ge 0$ the
number $|\bar I_n(B)|$ of signed inversion sequences of length $n$ avoiding every pattern of $B$
equals $|\bar I_n(C)|$. Then
$\{\bar1\bar0, \bar10, \bar0\bar0, \bar00, 00\} \sim
\{\bar1\bar0, \bar10, \bar0\bar1, 0\bar1, 00\}$.

The paper leaves this equivalence (Class 141 of its Table 6) open; it is what remains to be shown
for the number of Wilf classes of five-pattern sets to be exactly $239$.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Theorem 1, closing remark.

Stated but not proved: `MetaMathlibExt.signedInvSeq_wilf_b1b0_b10_b0b0_b00_00` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-inv-seq-wilf-b1b0-b10-b0b0-b00-00).

## Signed Wilf classes of sets of three patterns

The number $\mathrm{sw}_3$ of
Wilf-equivalence classes among the sets of $3$ length-2 signed patterns is $93$.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Theorem 2.

Stated but not proved: `MetaMathlibExt.signedWilfClassCount_three` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-wilf-class-count-three).

## Signed Wilf classes of sets of four patterns

The number $\mathrm{sw}_4$ of
Wilf-equivalence classes among the sets of $4$ length-2 signed patterns is $195$.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Theorem 10.

Stated but not proved: `MetaMathlibExt.signedWilfClassCount_four` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 289](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L289). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-wilf-class-count-four).

## Signed Wilf classes of sets of five to twelve patterns

Let $\mathrm{sw}_k$ be the number
of Wilf-equivalence classes among the sets of $k$ length-2 signed patterns. Then
$239 \le \mathrm{sw}_5 \le 240$, $\mathrm{sw}_6 = 190$, $\mathrm{sw}_7 = 107$, $\mathrm{sw}_8 = 49$,
$\mathrm{sw}_9 = 22$, $\mathrm{sw}_{10} = 8$, $\mathrm{sw}_{11} = 3$ and $\mathrm{sw}_{12} = 1$.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Theorem 11.

Stated but not proved: `MetaMathlibExt.signedWilfClassCount_five_to_twelve` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-wilf-class-count-five-to-twelve).

## Mansour–Safadi Theorem 3, class C2 (signed patterns 0̄0̄, 0̄0, 0̄1, 01)

A signed inversion
sequence of length $n$ is a word $e_1 \cdots e_n$ with $e_k \in \{0, \bar 0, 1, \bar 1, \dots,
k - 1, \overline{k - 1}\}$. It avoids a length-2 signed pattern $\tau_1\tau_2$ (one of $00$, $01$,
$10$, each letter possibly barred) when no $i < j$ have $|e_i|$, $|e_j|$ in the same order as
$|\tau_1|$, $|\tau_2|$ with $e_i$, $e_j$ barred exactly when $\tau_1$, $\tau_2$ are. Write
$\bar I_n(B)$ for the set of signed inversion sequences of length $n$ that avoid every pattern in
$B$, and $F_B(x) = \sum_{n \ge 0} |\bar I_n(B)|\,x^n$ in $\mathbb{Q}[[x]]$. Let
$B_1 = \{\bar 0\bar 0, \bar 0 0, \bar 0 1, 01\}$ and
$B_2 = \{\bar 0\bar 0, \bar 0 1, 0\bar 0, 01\}$.
For every $n \ge 0$, $|\bar I_n(B_1)| = |\bar I_n(B_2)|$, and the coefficient of $x^n$ in
$F_{B_1}(x)$ equals the coefficient of $x^n$ in
$1 + 2\sum_{k=1}^{n} x^k \prod_{i=1}^{k} (1 - ix)^{-1}$.

Since the terms with $k > n$ contribute nothing to $x^n$, this says
$F_{B_1}(x) = 1 + 2\sum_{k \ge 1} x^k / \prod_{i=1}^{k} (1 - ix)$.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Theorem 3 (C2).

Stated but not proved: `MetaMathlibExt.signedInvSeq_wilf_and_gf_b0b0_b00_b01_01` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 309](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L309). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-inv-seq-wilf-and-gf-b0b0-b00-b01).

## Mansour–Safadi Theorem 3, class C3 (signed patterns 0̄1̄, 0̄0̄, 0̄1, 01̄)

A signed
inversion sequence of length $n$ is a word $e_1 \cdots e_n$ with $e_k \in \{0, \bar 0, 1, \bar 1,
\dots, k - 1, \overline{k - 1}\}$. It avoids a length-2 signed pattern $\tau_1\tau_2$ (one of $00$,
$01$, $10$, each letter possibly barred) when no $i < j$ have $|e_i|$, $|e_j|$ in the same order as
$|\tau_1|$, $|\tau_2|$ with $e_i$, $e_j$ barred exactly when $\tau_1$, $\tau_2$ are. Write
$\bar I_n(B)$ for the set of signed inversion sequences of length $n$ that avoid every pattern in
$B$. Let $B_1 = \{\bar 0\bar 1, \bar 0\bar 0, \bar 0 1, 0\bar 1\}$,
$B_2 = \{\bar 0\bar 1, \bar 0 0, \bar 0 1, 0\bar 1\}$ and
$B_3 = \{\bar 0\bar 0, \bar 0 0, 0\bar 1, 0\bar 0\}$. For every $n \ge 0$,
$|\bar I_n(B_1)| = |\bar I_n(B_2)| = |\bar I_n(B_3)| = \sum_{i=0}^{n} i!$.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Theorem 3 (C3).

Stated but not proved: `MetaMathlibExt.signedInvSeq_wilf_and_gf_b0b1_b0b0_b01_0b1` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 323](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L323). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-inv-seq-wilf-and-gf-b0b1-b0b0-b01).

## Mansour–Safadi Theorem 3, class C4 (signed patterns 0̄1̄, 0̄0̄, 0̄0, 01̄)

A signed
inversion sequence of length $n$ is a word $e_1 \cdots e_n$ with $e_k \in \{0, \bar 0, 1, \bar 1,
\dots, k - 1, \overline{k - 1}\}$. It avoids a length-2 signed pattern $\tau_1\tau_2$ (one of $00$,
$01$, $10$, each letter possibly barred) when no $i < j$ have $|e_i|$, $|e_j|$ in the same order as
$|\tau_1|$, $|\tau_2|$ with $e_i$, $e_j$ barred exactly when $\tau_1$, $\tau_2$ are. Write
$\bar I_n(B)$ for the set of signed inversion sequences of length $n$ that avoid every pattern in
$B$. Let $B_1 = \{\bar 0\bar 1, \bar 0\bar 0, \bar 0 0, 0\bar 1\}$,
$B_2 = \{\bar 0\bar 1, \bar 0\bar 0, 0\bar 1, 0\bar 0\}$,
$B_3 = \{\bar 0\bar 1, \bar 0 0, 0\bar 1, 0\bar 0\}$ and
$B_4 = \{\bar 0 0, \bar 0 1, 0\bar 1, 0\bar 0\}$. Then
$|\bar I_n(B_1)| = |\bar I_n(B_2)| = |\bar I_n(B_3)| = |\bar I_n(B_4)|$ for every $n \ge 0$, and
$|\bar I_n(B_1)| = 2\,n!$ for every $n \ge 1$.

Together with $|\bar I_0(B)| = 1$, which holds for every $B$, this says that
$\sum_{n \ge 0} |\bar I_n(B_1)|\,x^n = 1 + 2\sum_{k \ge 1} k!\,x^k$.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Theorem 3 (C4).

Stated but not proved: `MetaMathlibExt.signedInvSeq_wilf_and_gf_b0b1_b0b0_b00_0b1` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 342](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L342). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-inv-seq-wilf-and-gf-b0b1-b0b0-b00).

## Mansour–Safadi Theorem 3, class C12 (signed patterns 0̄1̄, 0̄0̄, 01̄, 01)

A signed
inversion sequence of length $n$ is a word $e_1 \cdots e_n$ with $e_k \in \{0, \bar 0, 1, \bar 1,
\dots, k - 1, \overline{k - 1}\}$. It avoids a length-2 signed pattern $\tau_1\tau_2$ (one of $00$,
$01$, $10$, each letter possibly barred) when no $i < j$ have $|e_i|$, $|e_j|$ in the same order as
$|\tau_1|$, $|\tau_2|$ with $e_i$, $e_j$ barred exactly when $\tau_1$, $\tau_2$ are. Write
$\bar I_n(B)$ for the set of signed inversion sequences of length $n$ that avoid every pattern in
$B$, and $F_B(x) = \sum_{n \ge 0} |\bar I_n(B)|\,x^n$ in $\mathbb{Q}[[x]]$. Let
$B_1 = \{\bar 0\bar 1, \bar 0\bar 0, 0\bar 1, 01\}$, $B_2 = \{\bar 0\bar 1, \bar 0 1, 0\bar 1, 00\}$
and $B_3 = \{\bar 0\bar 1, \bar 0 1, 0\bar 0, 00\}$. Then
$|\bar I_n(B_1)| = |\bar I_n(B_2)| = |\bar I_n(B_3)|$ for every $n \ge 0$, and
$(1 - x)^2\,F_{B_1}(x) = 1 + x^2$.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Theorem 3 (C12).

Stated but not proved: `MetaMathlibExt.signedInvSeq_wilf_and_gf_b0b1_b0b0_0b1_01` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 363](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L363). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-inv-seq-wilf-and-gf-b0b1-b0b0-0b1).

## Mansour–Safadi Theorem 3, class C15 (signed patterns 0̄1̄, 0̄0̄, 0̄1, 01)

A signed
inversion sequence of length $n$ is a word $e_1 \cdots e_n$ with $e_k \in \{0, \bar 0, 1, \bar 1,
\dots, k - 1, \overline{k - 1}\}$. It avoids a length-2 signed pattern $\tau_1\tau_2$ (one of $00$,
$01$, $10$, each letter possibly barred) when no $i < j$ have $|e_i|$, $|e_j|$ in the same order as
$|\tau_1|$, $|\tau_2|$ with $e_i$, $e_j$ barred exactly when $\tau_1$, $\tau_2$ are. Write
$\bar I_n(B)$ for the set of signed inversion sequences of length $n$ that avoid every pattern in
$B$, and $F_B(x) = \sum_{n \ge 0} |\bar I_n(B)|\,x^n$ in $\mathbb{Q}[[x]]$. Let
$B_1 = \{\bar 0\bar 1, \bar 0\bar 0, \bar 0 1, 01\}$,
$B_2 = \{\bar 0\bar 1, \bar 0 0, \bar 0 1, 00\}$,
$B_3 = \{\bar 0\bar 1, \bar 0\bar 0, 0\bar 1, 00\}$,
$B_4 = \{\bar 0\bar 1, \bar 0\bar 0, 0\bar 0, 00\}$,
$B_5 = \{\bar 0\bar 1, \bar 0 1, 0\bar 1, 01\}$, $B_6 = \{\bar 0\bar 0, \bar 0 0, 0\bar 1, 00\}$ and
$B_7 = \{\bar 0\bar 0, \bar 0 0, 0\bar 0, 00\}$. Then
$|\bar I_n(B_1)| = |\bar I_n(B_2)| = \cdots = |\bar I_n(B_7)|$ for every $n \ge 0$, and
$(1 - 2x)\,F_{B_1}(x) = 1$, that is, $F_{B_1}(x) = 1/(1 - 2x)$.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Theorem 3 (C15).

Stated but not proved: `MetaMathlibExt.signedInvSeq_wilf_and_gf_b0b1_b0b0_b01_01` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 382](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L382). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-inv-seq-wilf-and-gf-b0b1-b0b0-b01-2).

## Mansour–Safadi Theorem 3, class C16 (signed patterns 0̄1̄, 0̄0, 01̄, 01)

A signed inversion
sequence of length $n$ is a word $e_1 \cdots e_n$ with $e_k \in \{0, \bar 0, 1, \bar 1, \dots,
k - 1, \overline{k - 1}\}$. It avoids a length-2 signed pattern $\tau_1\tau_2$ (one of $00$, $01$,
$10$, each letter possibly barred) when no $i < j$ have $|e_i|$, $|e_j|$ in the same order as
$|\tau_1|$, $|\tau_2|$ with $e_i$, $e_j$ barred exactly when $\tau_1$, $\tau_2$ are. Write
$\bar I_n(B)$ for the set of signed inversion sequences of length $n$ that avoid every pattern in
$B$, and $F_B(x) = \sum_{n \ge 0} |\bar I_n(B)|\,x^n$ in $\mathbb{Q}[[x]]$. Let
$B_1 = \{\bar 0\bar 1, \bar 0 0, 0\bar 1, 01\}$ and $B_2 = \{\bar 0\bar 1, \bar 0 1, 0\bar 0, 01\}$.
Then $|\bar I_n(B_1)| = |\bar I_n(B_2)|$ for every $n \ge 0$, and
$(1 - x)^2 (1 - 3x + x^2)\,F_{B_1}(x) = 1 - 3x + 2x^2 - x^3$.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Theorem 3 (C16).

Stated but not proved: `MetaMathlibExt.signedInvSeq_wilf_and_gf_b0b1_b00_0b1_01` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 416](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L416). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-inv-seq-wilf-and-gf-b0b1-b00-0b1).

## Mansour–Safadi Theorem 3, class C21

Write $\bar{I}_n(B)$ for the set of signed inversion
sequences of length $n$ that avoid every length-2 signed pattern in $B$, where a pattern is
one of $00$, $01$, $10$ with a bar over each barred letter. Then for every $n \ge 0$,
$|\bar{I}_n(\{\bar{0}\bar{1}, \bar{0}1, 0\bar{1}, 0\bar{0}\})| =
|\bar{I}_n(\{\bar{0}\bar{0}, \bar{0}1, 0\bar{1}, 0\bar{0}\})|$.

The generating function printed in the paper, $1/(1 - x)^2 + \sum_{j \ge 0} j!\, x^j$, is false
(its constant term is $2$, while $|\bar{I}_0(B)| = 1$) and is omitted.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Theorem 3 (C21).

Stated but not proved: `MetaMathlibExt.signedInvSeq_wilf_b0b1_b01_0b1_0b0` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 431](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L431). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-inv-seq-wilf-b0b1-b01-0b1-0b0).

## Signed inversion sequences avoiding $\{\bar1\bar0, \bar0\bar1, \bar01, 00\}$

For a set $B$
of length-2 signed patterns (a bar marks a barred letter), let $|\bar I_n(B)|$ be the number of
signed inversion sequences of length $n$ avoiding every pattern of $B$, and let
$F_B(x) = \sum_{n \ge 0} |\bar I_n(B)| x^n \in \mathbb{Q}[[x]]$. Let
$B = \{\bar1\bar0, \bar0\bar1, \bar01, 00\}$ and $C = \{\bar10, \bar0\bar0, 0\bar1, 01\}$. Then
$|\bar I_n(B)| = |\bar I_n(C)|$ for every $n \ge 0$, and $(1 - x)^3 F_B(x) = 1 - x + 2x^2$, that is,
$F_B(x) = (1 - x + 2x^2)/(1 - x)^3$.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Theorem 3 (C23).

Stated but not proved: `MetaMathlibExt.signedInvSeq_wilf_and_gf_b1b0_b0b1_b01_00` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 442](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L442). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-inv-seq-wilf-and-gf-b1b0-b0b1-b01).

## Signed inversion sequences avoiding $\{\bar1\bar0, \bar0\bar0, 0\bar1, 01\}$

For a set $B$
of length-2 signed patterns (a bar marks a barred letter), let $|\bar I_n(B)|$ be the number of
signed inversion sequences of length $n$ avoiding every pattern of $B$, and let
$F_B(x) = \sum_{n \ge 0} |\bar I_n(B)| x^n \in \mathbb{Q}[[x]]$. Let
$B = \{\bar1\bar0, \bar0\bar0, 0\bar1, 01\}$ and $C = \{\bar10, \bar0\bar1, \bar01, 00\}$. Then
$|\bar I_n(B)| = |\bar I_n(C)|$ for every $n \ge 0$, and $(1 - x)(1 - 2x) F_B(x) = 1 - x + x^2$,
that is, $F_B(x) = (1 - x + x^2)/((1 - x)(1 - 2x))$.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Theorem 3 (C25).

Stated but not proved: `MetaMathlibExt.signedInvSeq_wilf_and_gf_b1b0_b0b0_0b1_01` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 456](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L456). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-inv-seq-wilf-and-gf-b1b0-b0b0-0b1).

## Signed inversion sequences avoiding $\{\bar1\bar0, \bar0\bar1, \bar0\bar0, 00\}$

For a set
$B$ of length-2 signed patterns (a bar marks a barred letter), let $|\bar I_n(B)|$ be the number of
signed inversion sequences of length $n$ avoiding every pattern of $B$, and let
$F_B(x) = \sum_{n \ge 0} |\bar I_n(B)| x^n \in \mathbb{Q}[[x]]$. Let
$B_1 = \{\bar1\bar0, \bar0\bar1, \bar0\bar0, 00\}$, $B_2 = \{\bar1\bar0, \bar0\bar1, \bar01, 01\}$,
$B_3 = \{\bar10, \bar0\bar1, \bar01, 01\}$, $B_4 = \{\bar10, \bar0\bar0, 0\bar1, 00\}$ and
$B_5 = \{\bar0\bar0, \bar01, 00, 1\bar0\}$. Then
$|\bar I_n(B_1)| = |\bar I_n(B_2)| = |\bar I_n(B_3)| = |\bar I_n(B_4)| = |\bar I_n(B_5)|$ for every
$n \ge 0$, and $(1 - x)^2(1 - 2x) F_{B_1}(x) = 1 - 2x + 2x^2$, that is,
$F_{B_1}(x) = (1 - 2x + 2x^2)/((1 - x)^2(1 - 2x))$.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Theorem 3 (C30).

Stated but not proved: `MetaMathlibExt.signedInvSeq_wilf_and_gf_b1b0_b0b1_b0b0_00` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 471](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L471). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-inv-seq-wilf-and-gf-b1b0-b0b1-b0b).

## Signed inversion sequences avoiding $\{\bar1\bar0, \bar0\bar1, \bar00, 01\}$

For a set $B$
of length-2 signed patterns (a bar marks a barred letter), let $|\bar I_n(B)|$ be the number of
signed inversion sequences of length $n$ avoiding every pattern of $B$, and let
$F_B(x) = \sum_{n \ge 0} |\bar I_n(B)| x^n \in \mathbb{Q}[[x]]$. Let
$B = \{\bar1\bar0, \bar0\bar1, \bar00, 01\}$ and $C = \{\bar10, \bar0\bar1, \bar00, 01\}$. Then
$|\bar I_n(B)| = |\bar I_n(C)|$ for every $n \ge 0$, and
$(1 - x)(1 - 2x)(1 - 3x + x^2) F_B(x) = 1 - 4x + 5x^2 - 3x^3$, that is,
$F_B(x) = (1 - 4x + 5x^2 - 3x^3)/((1 - x)(1 - 2x)(1 - 3x + x^2))$.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Theorem 3 (C32).

Stated but not proved: `MetaMathlibExt.signedInvSeq_wilf_and_gf_b1b0_b0b1_b00_01` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 498](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L498). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-inv-seq-wilf-and-gf-b1b0-b0b1-b00).

## Signed inversion sequences avoiding $\{\bar1\bar0, \bar0\bar1, 0\bar1, 01\}$

For a set $B$
of length-2 signed patterns (a bar marks a barred letter), let $|\bar I_n(B)|$ be the number of
signed inversion sequences of length $n$ avoiding every pattern of $B$, and let
$F_B(x) = \sum_{n \ge 0} |\bar I_n(B)| x^n \in \mathbb{Q}[[x]]$. Let
$B = \{\bar1\bar0, \bar0\bar1, 0\bar1, 01\}$ and $C = \{\bar10, \bar0\bar1, 0\bar1, 01\}$. Then
$|\bar I_n(B)| = |\bar I_n(C)|$ for every $n \ge 0$, and $(1 - 3x + x^2) F_B(x) = 1 - x$, that is,
$F_B(x) = (1 - x)/(1 - 3x + x^2)$.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Theorem 3 (C38).

Stated but not proved: `MetaMathlibExt.signedInvSeq_wilf_and_gf_b1b0_b0b1_0b1_01` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 512](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L512). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-inv-seq-wilf-and-gf-b1b0-b0b1-0b1).

## Signed inversion sequences avoiding $\{\bar1\bar0, \bar0\bar0, \bar00, 01\}$

For a set $B$
of length-2 signed patterns (a bar marks a barred letter), let $|\bar I_n(B)|$ be the number of
signed inversion sequences of length $n$ avoiding every pattern of $B$, and let
$F_B(x) = \sum_{n \ge 0} |\bar I_n(B)| x^n \in \mathbb{Q}[[x]]$. Let
$B = \{\bar1\bar0, \bar0\bar0, \bar00, 01\}$ and $C = \{\bar1\bar0, \bar01, 0\bar1, 01\}$. Then
$|\bar I_n(B)| = |\bar I_n(C)|$ for every $n \ge 0$, and for every power series
$S \in \mathbb{Q}[[x]]$ with constant term $1$ and $S^2 = 1 - 4x$,

$$
2x(1 - x)^2(1 - 2x) F_B(x) = 1 - 3x + 2x^2 + 2x^3 - (1 - 3x + 2x^2) S.
$$

This is the formula
$F_B(x) = \bigl(1 - 3x + 2x^2 + 2x^3 - (1 - 3x + 2x^2)\sqrt{1 - 4x}\bigr)/(2x(1 - x)^2(1 - 2x))$
multiplied by its denominator, with $S = \sqrt{1 - 4x}$.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Theorem 3 (C39).

Stated but not proved: `MetaMathlibExt.signedInvSeq_wilf_and_gf_b1b0_b0b0_b00_01` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 528](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L528). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-inv-seq-wilf-and-gf-b1b0-b0b0-b00).

## Mansour–Safadi Theorem 3, class C41 (signed patterns 1̄0̄, 0̄0̄, 01̄, 00)

A signed
inversion sequence of length $n$ is a word $e_1 \cdots e_n$ with $e_k \in \{0, \bar 0, 1, \bar 1,
\dots, k - 1, \overline{k - 1}\}$. It avoids a length-2 signed pattern $\tau_1\tau_2$ (one of $00$,
$01$, $10$, each letter possibly barred) when no $i < j$ have $|e_i|$, $|e_j|$ in the same order as
$|\tau_1|$, $|\tau_2|$ with $e_i$, $e_j$ barred exactly when $\tau_1$, $\tau_2$ are. Write
$\bar I_n(B)$ for the set of signed inversion sequences of length $n$ that avoid every pattern in
$B$, and $F_B(x) = \sum_{n \ge 0} |\bar I_n(B)|\,x^n$ in $\mathbb{Q}[[x]]$. Let
$B_1 = \{\bar 1\bar 0, \bar 0\bar 0, 0\bar 1, 00\}$ and
$B_2 = \{\bar 1 0, \bar 0\bar 0, \bar 0 0, 01\}$.
For every $n \ge 0$, $|\bar I_n(B_1)| = |\bar I_n(B_2)|$, and the coefficient of $x^n$ in
$F_{B_1}(x)$ equals the coefficient of $x^n$ in
$(1 - x)^{-1} + (1 - x)^{-1} \sum_{j=1}^{n} x^j (1 - (j + 1)x)^{-1}$.

Since the terms with $j > n$ contribute nothing to $x^n$, this says
$F_{B_1}(x) = \frac{1}{1 - x}\bigl(1 + \sum_{j \ge 1} x^j / (1 - (j + 1)x)\bigr)$.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Theorem 3 (C41).

Stated but not proved: `MetaMathlibExt.signedInvSeq_wilf_and_gf_b1b0_b0b0_0b1_00` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 544](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L544). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-inv-seq-wilf-and-gf-b1b0-b0b0-0b1-2).

## Mansour–Safadi Theorem 3, class C45

Write $\bar{I}_n(B)$ for the set of signed inversion
sequences of length $n$ that avoid every length-2 signed pattern in $B$, where a pattern is
one of $00$, $01$, $10$ with a bar over each barred letter. Then for every $n \ge 0$,
$|\bar{I}_n(\{\bar{1}\bar{0}, \bar{0}\bar{0}, \bar{0}1, 01\})| =
|\bar{I}_n(\{\bar{1}\bar{0}, \bar{0}0, \bar{0}1, 00\})|$.

The generating function $C(x)$ printed in the paper is not defined there and is omitted.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Theorem 3 (C45).

Stated but not proved: `MetaMathlibExt.signedInvSeq_wilf_b1b0_b0b0_b01_01` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 559](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L559). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-inv-seq-wilf-b1b0-b0b0-b01-01).

## Signed inversion sequences avoiding $\{\bar1\bar0, \bar0\bar1, \bar00, 00\}$

For a set $B$
of length-2 signed patterns (a bar marks a barred letter), let $|\bar I_n(B)|$ be the number of
signed inversion sequences of length $n$ avoiding every pattern of $B$, and let
$F_B(x) = \sum_{n \ge 0} |\bar I_n(B)| x^n \in \mathbb{Q}[[x]]$. Let
$B_1 = \{\bar1\bar0, \bar0\bar1, \bar00, 00\}$, $B_2 = \{\bar1\bar0, \bar0\bar1, 0\bar0, 00\}$ and
$B_3 = \{\bar10, \bar0\bar1, 0\bar0, 00\}$. Then
$|\bar I_n(B_1)| = |\bar I_n(B_2)| = |\bar I_n(B_3)|$ for every $n \ge 0$, and for every $n \ge 0$
the coefficient of $x^n$ in $F_{B_1}(x)$ equals the coefficient of $x^n$ in

$$
\frac{1}{1 - x} + \frac{1}{1 - x} \sum_{j=1}^{n} \frac{x^j (1 - jx)}{\prod_{i=1}^{j+1} (1 - ix)}.
$$

The terms with $j > n$ are divisible by $x^{n+1}$, so this says
$F_{B_1}(x) = \frac{1}{1 - x}\Bigl(1 + \sum_{j \ge 1} x^j (1 - jx) /
\prod_{i=1}^{j+1} (1 - ix)\Bigr)$.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Theorem 3 (C46).

Stated but not proved: `MetaMathlibExt.signedInvSeq_wilf_and_gf_b1b0_b0b1_b00_00` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 572](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L572). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-inv-seq-wilf-and-gf-b1b0-b0b1-b00-2).

## Signed inversion sequences avoiding $\{\bar1\bar0, \bar0\bar1, \bar01, 0\bar1\}$

For a set
$B$ of length-2 signed patterns (a bar marks a barred letter), let $|\bar I_n(B)|$ be the number of
signed inversion sequences of length $n$ avoiding every pattern of $B$, and let
$F_B(x) = \sum_{n \ge 0} |\bar I_n(B)| x^n \in \mathbb{Q}[[x]]$. Let
$B = \{\bar1\bar0, \bar0\bar1, \bar01, 0\bar1\}$ and $C = \{\bar10, \bar0\bar1, \bar01, 0\bar1\}$.
Then $|\bar I_n(B)| = |\bar I_n(C)|$ for every $n \ge 0$, and
$(1 - 2x) F_B(x) = (1 - x) \sum_{j \ge 0} j!\, x^j$, that is,
$F_B(x) = \frac{1 - x}{1 - 2x} \sum_{j \ge 0} j!\, x^j$.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Theorem 3 (C50).

Stated but not proved: `MetaMathlibExt.signedInvSeq_wilf_and_gf_b1b0_b0b1_b01_0b1` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 591](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L591). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-inv-seq-wilf-and-gf-b1b0-b0b1-b01-2).

## Signed inversion sequences avoiding $\{\bar1\bar0, \bar0\bar1, 0\bar1, 00\}$

For a set $B$
of length-2 signed patterns (a bar marks a barred letter), let $|\bar I_n(B)|$ be the number of
signed inversion sequences of length $n$ avoiding every pattern of $B$, and let
$F_B(x) = \sum_{n \ge 0} |\bar I_n(B)| x^n \in \mathbb{Q}[[x]]$. Let
$B = \{\bar1\bar0, \bar0\bar1, 0\bar1, 00\}$ and $C = \{\bar10, \bar0\bar1, 0\bar1, 00\}$. Then
$|\bar I_n(B)| = |\bar I_n(C)|$ for every $n \ge 0$, and for every $n \ge 0$ the coefficient of
$x^n$ in $F_B(x)$ equals the coefficient of $x^n$ in
$\sum_{j=0}^{n} x^j \prod_{i=1}^{j+1} (1 - ix)^{-1}$.

The terms with $j > n$ are divisible by $x^{n+1}$, so this says
$F_B(x) = \sum_{j \ge 0} x^j / \prod_{i=1}^{j+1} (1 - ix)$.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Theorem 3 (C60).

Stated but not proved: `MetaMathlibExt.signedInvSeq_wilf_and_gf_b1b0_b0b1_0b1_00` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 606](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L606). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-inv-seq-wilf-and-gf-b1b0-b0b1-0b1-2).

## Mansour–Safadi Theorem 4

Write $\bar{I}_n(B)$ for the set of signed inversion
sequences of length $n$ that avoid every length-2 signed pattern in $B$, where a pattern is
one of $00$, $01$, $10$ with a bar over each barred letter. Then for every $n \ge 0$,
$|\bar{I}_n(\{\bar{0}\bar{1}, \bar{0}\bar{0}, \bar{0}1, 0\bar{0}\})| =
|\bar{I}_n(\{\bar{0}\bar{1}, \bar{0}0, \bar{0}1, 0\bar{0}\})|$.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Theorem 4.

Stated but not proved: `MetaMathlibExt.signedInvSeq_wilf_b0b1_b0b0_b01_0b0` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 620](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L620). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-inv-seq-wilf-b0b1-b0b0-b01-0b0).

## Mansour–Safadi Theorem 5

Write $\bar{I}_n(B)$ for the set of signed inversion
sequences of length $n$ that avoid every length-2 signed pattern in $B$, where a pattern is
one of $00$, $01$, $10$ with a bar over each barred letter. Then for every $n \ge 0$,
$|\bar{I}_n(\{\bar{1}\bar{0}, \bar{0}\bar{0}, \bar{0}1, 0\bar{0}\})| =
|\bar{I}_n(\{\bar{1}\bar{0}, \bar{0}0, \bar{0}1, 0\bar{0}\})|$,
$|\bar{I}_n(\{\bar{1}0, \bar{0}\bar{1}, \bar{0}\bar{0}, 0\bar{0}\})| =
|\bar{I}_n(\{\bar{1}0, \bar{0}\bar{1}, \bar{0}0, 0\bar{0}\})|$, and
$|\bar{I}_n(\{\bar{1}\bar{0}, \bar{0}\bar{0}, \bar{0}1, 1\bar{0}\})| =
|\bar{I}_n(\{\bar{1}\bar{0}, \bar{0}0, \bar{0}1, 1\bar{0}\})|$.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Theorem 5.

Stated but not proved: `MetaMathlibExt.signedInvSeq_wilf_b1b0_b0b0_b01_0b0` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 631](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L631). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-inv-seq-wilf-b1b0-b0b0-b01-0b0).

## Mansour–Safadi Theorem 6

Write $\bar{I}_n(B)$ for the set of signed inversion
sequences of length $n$ that avoid every length-2 signed pattern in $B$, where a pattern is
one of $00$, $01$, $10$ with a bar over each barred letter. Then for every $n \ge 0$,
$|\bar{I}_n(\{\bar{1}0, \bar{0}0, 0\bar{1}, 00\})| =
|\bar{I}_n(\{\bar{1}0, 0\bar{1}, 0\bar{0}, 00\})|$.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Theorem 6.

Stated but not proved: `MetaMathlibExt.signedInvSeq_wilf_b10_b00_0b1_00` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 649](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L649). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-inv-seq-wilf-b10-b00-0b1-00).

## Mansour–Safadi Theorem 7: four Wilf-equivalent four-pattern sets

Length-2 signed
patterns are written as in the paper, a bar marking a barred letter, and $B \sim C$ means that
for every $n \ge 0$ the number $|\bar I_n(B)|$ of signed inversion sequences of length $n$
avoiding every pattern of $B$ equals $|\bar I_n(C)|$. Then
$\{\bar1\bar0, \bar0\bar1, \bar0\bar0, \bar00\} \sim \{\bar1\bar0, \bar0\bar1, \bar0\bar0, 0\bar0\}
\sim \{\bar1\bar0, \bar0\bar1, \bar00, 0\bar0\} \sim \{\bar10, \bar00, 0\bar1, 0\bar0\}$.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Theorem 7.

Stated but not proved: `MetaMathlibExt.signedInvSeq_wilf_b1b0_b0b1_b0b0_b00` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 660](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L660). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-inv-seq-wilf-b1b0-b0b1-b0b0-b00).

## Mansour–Safadi Theorem 8: two Wilf-equivalences of four-pattern sets

Length-2 signed
patterns are written as in the paper, a bar marking a barred letter, and $B \sim C$ means that
for every $n \ge 0$ the number $|\bar I_n(B)|$ of signed inversion sequences of length $n$
avoiding every pattern of $B$ equals $|\bar I_n(C)|$. Then
$\{\bar1\bar0, \bar0\bar1, \bar0\bar0, 1\bar0\} \sim \{\bar1\bar0, \bar0\bar1, 0\bar0, 1\bar0\}$
and $\{\bar1\bar0, \bar0\bar0, \bar00, 1\bar0\} \sim \{\bar1\bar0, \bar00, 0\bar0, 1\bar0\}$.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Theorem 8.

Stated but not proved: `MetaMathlibExt.signedInvSeq_wilf_b1b0_b0b1_b0b0_1b0` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 679](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L679). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-inv-seq-wilf-b1b0-b0b1-b0b0-1b0).

## Mansour–Safadi Theorem 9: a Wilf-equivalence of four-pattern sets

Length-2 signed
patterns are written as in the paper, a bar marking a barred letter, and $B \sim C$ means that
for every $n \ge 0$ the number $|\bar I_n(B)|$ of signed inversion sequences of length $n$
avoiding every pattern of $B$ equals $|\bar I_n(C)|$. Then
$\{\bar1\bar0, \bar10, \bar0\bar0, 0\bar0\} \sim \{\bar1\bar0, \bar10, \bar00, 0\bar0\}$.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Theorem 9.

Stated but not proved: `MetaMathlibExt.signedInvSeq_wilf_b1b0_b10_b0b0_0b0` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 693](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L693). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-inv-seq-wilf-b1b0-b10-b0b0-0b0).

## Mansour–Safadi Theorem 12: four Wilf-equivalences of five-pattern sets

Length-2 signed
patterns are written as in the paper, a bar marking a barred letter, and $B \sim C$ means that
for every $n \ge 0$ the number $|\bar I_n(B)|$ of signed inversion sequences of length $n$
avoiding every pattern of $B$ equals $|\bar I_n(C)|$. Then
$\{\bar1\bar0, \bar0\bar1, \bar00, \bar01, 0\bar0\} \sim
\{\bar1\bar0, \bar0\bar1, \bar0\bar0, \bar01, 0\bar0\}$,
$\{\bar1\bar0, \bar10, \bar0\bar1, \bar00, 0\bar0\} \sim
\{\bar1\bar0, \bar10, \bar0\bar1, \bar0\bar0, 0\bar0\}$,
$\{\bar1\bar0, \bar0\bar1, \bar0\bar0, \bar00, 1\bar0\} \sim
\{\bar1\bar0, \bar0\bar1, \bar00, 0\bar0, 1\bar0\}$ and
$\{\bar1\bar0, \bar10, \bar0\bar1, \bar00, 00\} \sim
\{\bar1\bar0, \bar10, \bar0\bar1, 0\bar0, 00\}$.

The paper prints a third set in the first equivalence,
$\{\bar1\bar0, \bar0\bar1, \bar01, 0\bar0, 1\bar0\}$; it is left out here because it has
$|\bar I_2| = 5$, against $4$ for the first two sets.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Theorem 12.

Stated but not proved: `MetaMathlibExt.signedInvSeq_wilf_b1b0_b0b1_b00_b01_0b0` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 707](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L707). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-inv-seq-wilf-b1b0-b0b1-b00-b01-0b).

## Mansour–Safadi Theorem 13: a Wilf-equivalence of five-pattern sets

Length-2 signed
patterns are written as in the paper, a bar marking a barred letter, and $B \sim C$ means that
for every $n \ge 0$ the number $|\bar I_n(B)|$ of signed inversion sequences of length $n$
avoiding every pattern of $B$ equals $|\bar I_n(C)|$. Then
$\{\bar1\bar0, \bar0\bar1, \bar00, \bar01, 1\bar0\} \sim
\{\bar1\bar0, \bar0\bar1, \bar0\bar0, \bar01, 1\bar0\}$.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Theorem 13.

Stated but not proved: `MetaMathlibExt.signedInvSeq_wilf_b1b0_b0b1_b00_b01_1b0` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 729](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L729). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-inv-seq-wilf-b1b0-b0b1-b00-b01-1b).

## Mansour–Safadi Theorem 14

Write $\bar{I}_n(B)$ for the set of signed inversion
sequences of length $n$ that avoid every length-2 signed pattern in $B$, where a pattern is
one of $00$, $01$, $10$ with a bar over each barred letter. Let
$B_1 = \{\bar{1}0, \bar{0}\bar{1}, 0\bar{1}, 0\bar{0}, 1\bar{0}\}$,
$B_2 = \{\bar{1}\bar{0}, \bar{0}\bar{1}, 0\bar{1}, 0\bar{0}, 1\bar{0}\}$,
$B_3 = \{\bar{1}\bar{0}, \bar{1}0, \bar{0}\bar{0}, \bar{0}0, 0\bar{0}\}$,
$B_4 = \{\bar{1}\bar{0}, \bar{0}\bar{0}, 0\bar{1}, 0\bar{0}, 1\bar{0}\}$,
$B_5 = \{\bar{1}\bar{0}, \bar{0}\bar{1}, \bar{0}\bar{0}, 0\bar{1}, 1\bar{0}\}$,
$B_6 = \{\bar{1}0, \bar{0}\bar{1}, \bar{0}\bar{0}, 0\bar{1}, 1\bar{0}\}$, and
$B_7 = \{\bar{1}\bar{0}, \bar{1}0, \bar{0}\bar{0}, \bar{0}0, \bar{0}1\}$.
Then for every $n \ge 0$,
$|\bar{I}_n(B_1)| = |\bar{I}_n(B_2)| = |\bar{I}_n(B_3)| = |\bar{I}_n(B_4)| = |\bar{I}_n(B_5)| =
|\bar{I}_n(B_6)| = |\bar{I}_n(B_7)|$.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Theorem 14.

Stated but not proved: `MetaMathlibExt.signedInvSeq_wilf_b10_b0b1_0b1_0b0_1b0` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 741](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L741). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-inv-seq-wilf-b10-b0b1-0b1-0b0-1b0).

## Mansour–Safadi Theorem 15

Write $\bar{I}_n(B)$ for the set of signed inversion
sequences of length $n$ that avoid every length-2 signed pattern in $B$, where a pattern is
one of $00$, $01$, $10$ with a bar over each barred letter. Then for every $n \ge 0$,
$|\bar{I}_n(\{\bar{1}\bar{0}, \bar{0}0, \bar{0}1, 0\bar{0}, 1\bar{0}\})| =
|\bar{I}_n(\{\bar{1}\bar{0}, \bar{0}\bar{0}, \bar{0}1, 0\bar{0}, 1\bar{0}\})|$.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Theorem 15.

Stated but not proved: `MetaMathlibExt.signedInvSeq_wilf_b1b0_b00_b01_0b0_1b0` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 771](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L771). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-inv-seq-wilf-b1b0-b00-b01-0b0-1b0).

## Mansour–Safadi Theorem 16: a Wilf-equivalence of six-pattern sets

Length-2 signed
patterns are written as in the paper, a bar marking a barred letter, and $B \sim C$ means that
for every $n \ge 0$ the number $|\bar I_n(B)|$ of signed inversion sequences of length $n$
avoiding every pattern of $B$ equals $|\bar I_n(C)|$. Then
$\{\bar1\bar0, \bar10, \bar0\bar1, \bar00, \bar01, 0\bar0\} \sim
\{\bar1\bar0, \bar10, \bar0\bar1, \bar0\bar0, \bar01, 0\bar0\}$.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Theorem 16.

Stated but not proved: `MetaMathlibExt.signedInvSeq_wilf_b1b0_b10_b0b1_b00_b01_0b0` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 781](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L781). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-inv-seq-wilf-b1b0-b10-b0b1-b00-b0).

## Three six-pattern sets with 2 · n! avoiders (Theorem 17)

Write a length-2 signed pattern
as $\tau_1\tau_2$, where $00$, $01$ and $10$ record whether $|\tau_1|$ is equal to, smaller than
or larger than $|\tau_2|$ and a bar marks a barred letter, and write $|\bar I_n(A)|$ for the
number of signed inversion sequences of length $n$ avoiding every pattern of a set $A$ of such
patterns. For every $n \ge 1$ and each of the three sets
$A = \lbrace \bar 1\bar 0, \bar 1 0, \bar 0\bar 1, \bar 0\bar 0, \bar 0 0, 0\bar 1 \rbrace$,
$\lbrace \bar 1\bar 0, \bar 1 0, \bar 0\bar 1, \bar 0\bar 0, \bar 0 0, 0\bar 0 \rbrace$ and
$\lbrace \bar 1\bar 0, \bar 0\bar 1, \bar 0\bar 0, \bar 0 0, \bar 0 1, 1\bar 0 \rbrace$, we have
$|\bar I_n(A)| = 2 \cdot n!$.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Theorem 17.

Stated but not proved: `MetaMathlibExt.signedInvAvoidCount_eq_two_mul_factorial` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 792](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L792). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-inv-avoid-count-eq-two-mul-factor).

## Mansour–Safadi Theorem 18: a Wilf-equivalence of seven-pattern sets

Length-2 signed
patterns are written as in the paper, a bar marking a barred letter, and $B \sim C$ means that
for every $n \ge 0$ the number $|\bar I_n(B)|$ of signed inversion sequences of length $n$
avoiding every pattern of $B$ equals $|\bar I_n(C)|$. Then
$\{\bar1\bar0, \bar10, \bar0\bar1, \bar0\bar0, \bar00, \bar01, 1\bar0\} \sim
\{\bar1\bar0, \bar10, \bar0\bar0, \bar00, \bar01, 0\bar0, 1\bar0\}$.

## Sources

- Toufik Mansour and Amir Safadi, *Signed Inversion Sequences Avoiding a Set of Length-2 Signed Patterns*, INTEGERS 26 (2026), Article A74, Theorem 18.

Stated but not proved: `MetaMathlibExt.signedInvSeq_wilf_b1b0_b10_b0b1_b0b0_b00_b01_1b0` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean, line 806](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SignedInversionSequenceLength2Wanted.lean#L806). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html#signed-inv-seq-wilf-b1b0-b10-b0b1-b0b0-b).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Pattern avoidance in inversion sequences](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-inversion-sequences)
