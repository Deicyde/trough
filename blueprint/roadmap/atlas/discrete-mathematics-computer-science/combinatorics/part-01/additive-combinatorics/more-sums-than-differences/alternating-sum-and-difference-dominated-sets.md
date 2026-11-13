---
declaration: section
origin: cited
lean: MetaMathlibExt.interval_erase_add_sub, MetaMathlibExt.alternating_sequence_of_copies, MetaMathlibExt.nathanson_mstd_construction, MetaMathlibExt.alternating_sequence_from_nathanson
statement: formalized
---

# Alternating sum- and difference-dominated sets

4 results, 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/alternating-sum-and-difference-dominated-sets/index.html).

## Sums and differences of an interval with one point removed

Let $m$ and $r$ be integers
with $m \ge 4$ and $2 \le r \le m - 3$, and let $B = \{0, 1, \dots, m - 1\} \setminus \{r\}$. Then
the sumset $B + B = \{b + b' : b, b' \in B\}$ is $\{0, 1, \dots, 2m - 2\}$ and the difference set
$B - B = \{b - b' : b, b' \in B\}$ is the set of integers from $-(m - 1)$ to $m - 1$.

## Sources

- Yorick Herrmann, Connor Hill, Merlin Phillips, Daniel Flores, Steven J. Miller and Steven Senger, *Additional Constructions of Sequences of Alternating Sum and Difference Dominated Sets*, INTEGERS 26 (2026), Article A88, Lemma 1.

Stated but not proved: `MetaMathlibExt.interval_erase_add_sub` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/AlternatingSumDifferenceDominatedWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/AlternatingSumDifferenceDominatedWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/alternating-sum-and-difference-dominated-sets/index.html#interval-erase-add-sub).

## Alternating sum- and difference-dominated sets from shifted copies

For a set $S$ of
integers write $S + S = \{s + s' : s, s' \in S\}$ and $S - S = \{s - s' : s, s' \in S\}$. Let $A_1$
be a finite set of integers with $|A_1 - A_1| < |A_1 + A_1|$ and $0 \in A_1$, and let $n$ be an
integer with $0 \le a < n$ for every $a \in A_1$. Suppose that (a) $A_1 + A_1$ and $A_1 - A_1$
meet the same number of residue classes modulo $n$, and (b) with
$x = \#\{a \in A_1 : n + a \notin A_1 + A_1\}$ and $y = \#\{b \in A_1 : n - b \notin A_1 - A_1\}$
we have $2y - x - 1 > |A_1 + A_1| - |A_1 - A_1|$. Let $A_1, A_2, A_3, \dots$ be finite sets of
integers, starting with this $A_1$, such that for every $l \ge 1$, $A_{2l} = A_{2l-1} \cup \{ln\}$
and $A_{2l+1} = A_{2l-1} \cup \{a + ln : a \in A_1\}$. Then for every $l \ge 1$,
$|A_{2l} + A_{2l}| < |A_{2l} - A_{2l}|$, $|A_{2l+1} - A_{2l+1}| < |A_{2l+1} + A_{2l+1}|$ and
$A_{2l-1} \subsetneq A_{2l} \subsetneq A_{2l+1}$.

## Sources

- Yorick Herrmann, Connor Hill, Merlin Phillips, Daniel Flores, Steven J. Miller and Steven Senger, *Additional Constructions of Sequences of Alternating Sum and Difference Dominated Sets*, INTEGERS 26 (2026), Article A88, Theorem 1.

Stated but not proved: `MetaMathlibExt.alternating_sequence_of_copies` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/AlternatingSumDifferenceDominatedWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/AlternatingSumDifferenceDominatedWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/alternating-sum-and-difference-dominated-sets/index.html#alternating-sequence-of-copies).

## Nathanson's sum-dominated set

For a set $S$ of integers write
$S + S = \{s + s' : s, s' \in S\}$ and $S - S = \{s - s' : s, s' \in S\}$. Let $m$, $d$, $k$ be
integers with $m \ge 4$, $1 \le d \le m - 1$ and $2d \ne m$, and suppose $k \ge 3$ if $2d < m$
and $k \ge 4$ if $2d > m$. Let $B = \{0, 1, \dots, m - 1\} \setminus \{d\}$,
$L = \{jm - d : 1 \le j \le k\}$, $A^* = B \cup L \cup \{(k + 1)m - 2d - b : b \in B\}$ and
$A = A^* \cup \{m\}$. Then $|A - A| < |A + A|$, $2m \in A + A$, $2m \notin A^* + A^*$, and
$\{a - m : a \in A^*\} \subseteq A^* - A^*$.

## Sources

- Yorick Herrmann, Connor Hill, Merlin Phillips, Daniel Flores, Steven J. Miller and Steven Senger, *Additional Constructions of Sequences of Alternating Sum and Difference Dominated Sets*, INTEGERS 26 (2026), Article A88, Theorem 2.

Stated but not proved: `MetaMathlibExt.nathanson_mstd_construction` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/AlternatingSumDifferenceDominatedWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/AlternatingSumDifferenceDominatedWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/alternating-sum-and-difference-dominated-sets/index.html#nathanson-mstd-construction).

## Alternating sum- and difference-dominated sets from Nathanson's construction

For a set
$S$ of integers write $S + S = \{s + s' : s, s' \in S\}$, $S - S = \{s - s' : s, s' \in S\}$,
$c + S = \{c + s : s \in S\}$ and $c - S = \{c - s : s \in S\}$. Let $m$, $d$, $k$ be integers with
$m \ge 4$, $m \equiv 0 \pmod 4$ and $4d = m$ or $4d = 3m$, and suppose $k \ge 3$ if $2d < m$ and
$k \ge 4$ if $2d > m$. Let $B = \{0, 1, \dots, m - 1\} \setminus \{d\}$,
$L = \{jm - d : 1 \le j \le k\}$ and $A^* = B \cup L \cup \{(k + 1)m - 2d - b : b \in B\}$. Let
$A_1, A_2, A_3, \dots$ be finite sets of integers with $A_1 = A^* \cup \{m, -d, (k + 1)m - d\}$
and, for every $r \ge 1$, $A_{2r} = A_{2r-1} \cup \{(k + r + 1)m - d\}$ and
$A_{2r+1} = A_{2r-1} \cup \{-rm - d, (k + r + 1)m - d\}$. Then $|A_1 - A_1| < |A_1 + A_1|$, and
for every $r \ge 1$, writing $A'_{2r-1} = A_{2r-1} \setminus \{m\}$: we have
$|A_{2r} + A_{2r}| < |A_{2r} - A_{2r}|$ and $|A_{2r+1} - A_{2r+1}| < |A_{2r+1} + A_{2r+1}|$;
$A_{2r-1} \subsetneq A_{2r} \subsetneq A_{2r+1}$; $m + A'_{2r-1} \subseteq A'_{2r-1} + A'_{2r-1}$
and $m - A'_{2r-1} \subseteq A'_{2r-1} - A'_{2r-1}$;
$|A_{2r-1} + A_{2r-1}| = |A_{2r-1} - A_{2r-1}| + 1$; and
$|A_{2r} + A_{2r}| \le |A_{2r} - A_{2r}| - m + 3$.

## Sources

- Yorick Herrmann, Connor Hill, Merlin Phillips, Daniel Flores, Steven J. Miller and Steven Senger, *Additional Constructions of Sequences of Alternating Sum and Difference Dominated Sets*, INTEGERS 26 (2026), Article A88, Theorem 3.

Stated but not proved: `MetaMathlibExt.alternating_sequence_from_nathanson` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/AlternatingSumDifferenceDominatedWanted.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/AlternatingSumDifferenceDominatedWanted.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/alternating-sum-and-difference-dominated-sets/index.html#alternating-sequence-from-nathanson).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Alternating sum- and difference-dominated sets](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/alternating-sum-and-difference-dominated-sets/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/alternating-sum-and-difference-dominated-sets)
