---
declaration: section
origin: cited
lean: MetaMathlibExt.nExpansionDigit, MetaMathlibExt.nExpansionMap, MetaMathlibExt.nExpansionDigit_of_ne, MetaMathlibExt.nExpansionMap_mem_Ico_of_ne, MetaMathlibExt.nExpansionMap_self_of_int, MetaMathlibExt.idealPeriodWord, MetaMathlibExt.idealPeriodWord_five, MetaMathlibExt.idealPeriodWord_flatten_length_small
statement: formalized
---

# N-continued fraction expansions

13 results, 8 proved and 5 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/low-dimensional-dynamics/n-continued-fraction-expansions/index.html).

## Digit of the N-expansion map

Let $N$ be a natural number and $\alpha$ a real number, and
write $I_\alpha = [\alpha, \alpha + 1]$. The digit of a real number $x$ is
$d(x) = \lfloor N/x - \alpha \rfloor$, except that when $N/\alpha - \alpha$ is an integer, the
digit of $\alpha$ itself is $d(\alpha) = N/\alpha - \alpha - 1$.

With this choice the $N$-expansion map $T_\alpha(x) = N/x - d(x)$ sends $\alpha$ to $\alpha + 1$
in the integer case, every other point of $I_\alpha$ lands in $[\alpha, \alpha + 1)$, and no
cylinder is a single point.

## Sources

- Jaap de Jonge, *Intervals of N-Expansions with Many Gaps*, INTEGERS 26 (2026), Article A75, Definition 1.

Formalized by `MetaMathlibExt.nExpansionDigit`, a definition declared in [WantedExt/Dynamics/NExpansionGapsWanted.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Dynamics/NExpansionGapsWanted.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/low-dimensional-dynamics/n-continued-fraction-expansions/index.html#n-expansion-digit).

## The $N$-expansion map

For a natural number $N$ and a real number $\alpha$, the
$N$-expansion map is $T_\alpha(x) = N/x - d_\alpha(x)$ for real $x$, where $d_\alpha(x)$ is the
$N$-expansion digit: $d_\alpha(x) = \lfloor N/x - \alpha \rfloor$, except that
$d_\alpha(\alpha) = \lfloor N/\alpha - \alpha \rfloor - 1$ when $N/\alpha - \alpha$ is an integer.
The map is meant to act on the interval $I_\alpha = [\alpha, \alpha + 1]$, but it is defined for
every real $x$, with the convention $N/0 = 0$.

## Sources

- Jaap de Jonge, *Intervals of N-Expansions with Many Gaps*, INTEGERS 26 (2026), Article A75, Definition 1.

Formalized by `MetaMathlibExt.nExpansionMap`, a definition declared in [WantedExt/Dynamics/NExpansionGapsWanted.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Dynamics/NExpansionGapsWanted.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/low-dimensional-dynamics/n-continued-fraction-expansions/index.html#n-expansion-map).

## The digit away from the left endpoint

Let $N$ be a natural number and let $\alpha$ and
$x$ be real numbers with $x \ne \alpha$. Then the digit of $x$ for the $N$-expansion map on
$[\alpha, \alpha + 1]$ is $\lfloor N/x - \alpha \rfloor$.

## Sources

- Jaap de Jonge, *Intervals of N-Expansions with Many Gaps*, INTEGERS 26 (2026), Article A75, Definition 1.

Formalized by `MetaMathlibExt.nExpansionDigit_of_ne`, a theorem declared in [WantedExt/Dynamics/NExpansionGapsWanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Dynamics/NExpansionGapsWanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/low-dimensional-dynamics/n-continued-fraction-expansions/index.html#n-expansion-digit-of-ne).

## The N-expansion map away from the left endpoint

Let $N$ be a natural number and let
$\alpha$ and $x$ be real numbers with $x \ne \alpha$. Then the $N$-expansion map $T_\alpha$
satisfies $\alpha \le T_\alpha(x) < \alpha + 1$.

Indeed $T_\alpha(x) = \alpha + \{N/x - \alpha\}$, where $\{\cdot\}$ denotes the fractional part.

## Sources

- Jaap de Jonge, *Intervals of N-Expansions with Many Gaps*, INTEGERS 26 (2026), Article A75, Definition 1.

Formalized by `MetaMathlibExt.nExpansionMap_mem_Ico_of_ne`, a theorem declared in [WantedExt/Dynamics/NExpansionGapsWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Dynamics/NExpansionGapsWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/low-dimensional-dynamics/n-continued-fraction-expansions/index.html#n-expansion-map-mem-ico-of-ne).

## The left endpoint goes to the right endpoint when $N/\alpha - \alpha$ is an integer

Let
$N$ be a natural number and $\alpha$ a real number such that $N/\alpha - \alpha$ is an integer,
with the convention $N/0 = 0$. Then the $N$-expansion map $T_\alpha$ satisfies
$T_\alpha(\alpha) = \alpha + 1$.

## Sources

- Jaap de Jonge, *Intervals of N-Expansions with Many Gaps*, INTEGERS 26 (2026), Article A75, Definition 1.

Formalized by `MetaMathlibExt.nExpansionMap_self_of_int`, a theorem declared in [WantedExt/Dynamics/NExpansionGapsWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Dynamics/NExpansionGapsWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/low-dimensional-dynamics/n-continued-fraction-expansions/index.html#n-expansion-map-self-of-int).

## Ideal period words

For $n \ge 1$, the ideal period word $d_n$ is a finite list of blocks
of partial quotients, each block being $a = 2, 1, 1$ or $b = 2, 2$. Writing lists of blocks by
juxtaposition, with commas between parts, $d_1 = [ab]$, $d_2 = [abb]$, $d_3 = [abb, ab, ab]$ and
$d_4 = [abb, ab, ab, abb, abb]$; for $n \ge 5$, if $d_{n-1} = [j, ab, ab]$ for a list $j$ then
$d_n = [j, ab, ab, j, abb]$, and if $d_{n-1} = [j, abb]$ then $d_n = [j, abb, j, ab, ab]$. The
digit string of $d_n$ is the concatenation of its blocks. For $n = 0$ the list is empty, a
placeholder.

## Sources

- Jaap de Jonge, *Intervals of N-Expansions with Many Gaps*, INTEGERS 26 (2026), Article A75, Definition 7.

Formalized by `MetaMathlibExt.idealPeriodWord`, a definition declared in [WantedExt/Dynamics/NExpansionGapsWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Dynamics/NExpansionGapsWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/low-dimensional-dynamics/n-continued-fraction-expansions/index.html#ideal-period-word).

## The fifth ideal period word

Writing $a$ for the block $2, 1, 1$ and $b$ for the block
$2, 2$ of partial quotients, the ideal period word $d_5$ is $d_4$ followed by the blocks
$abb\,ab\,ab\,abb\,ab\,ab$, in this order.

This is the second recursion rule applied to $d_4 = [j, abb]$ with $j = [abb, ab, ab, abb]$.

## Sources

- Jaap de Jonge, *Intervals of N-Expansions with Many Gaps*, INTEGERS 26 (2026), Article A75, Definition 7.

Formalized by `MetaMathlibExt.idealPeriodWord_five`, a theorem declared in [WantedExt/Dynamics/NExpansionGapsWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Dynamics/NExpansionGapsWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/low-dimensional-dynamics/n-continued-fraction-expansions/index.html#ideal-period-word-five).

## Lengths of the first ideal period words

The digit strings of the ideal period words
$d_1, d_2, d_3, d_4, d_5$ have lengths $5, 7, 17, 31, 65$ respectively.

## Sources

- Jaap de Jonge, *Intervals of N-Expansions with Many Gaps*, INTEGERS 26 (2026), Article A75, Definition 7.

Formalized by `MetaMathlibExt.idealPeriodWord_flatten_length_small`, a theorem declared in [WantedExt/Dynamics/NExpansionGapsWanted.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Dynamics/NExpansionGapsWanted.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/low-dimensional-dynamics/n-continued-fraction-expansions/index.html#ideal-period-word-flatten-length-small).

## Orbits with the same digits alternate in order

Let $N$ be a positive integer and let
$0 < \alpha < \alpha'$ be real numbers. Write $T_\alpha$ for the $N$-expansion map and $d_\alpha$
for the $N$-expansion digit with parameter $\alpha$, and let $m$ be a natural number. If the
orbits $\alpha_j = T_\alpha^j(\alpha)$ and $\alpha'_j = T_{\alpha'}^j(\alpha')$ satisfy
$d_\alpha(\alpha_j) = d_{\alpha'}(\alpha'_j)$ for all $j \in \{0, \dots, m\}$, then
$\alpha'_m < \alpha_m$ if and only if $m$ is odd. Likewise, if the orbits
$\beta_j = T_\alpha^j(\alpha + 1)$ and $\beta'_j = T_{\alpha'}^j(\alpha' + 1)$ satisfy
$d_\alpha(\beta_j) = d_{\alpha'}(\beta'_j)$ for all $j \in \{0, \dots, m\}$, then
$\beta'_m < \beta_m$ if and only if $m$ is odd.

The paper assumes $\alpha$ and $\alpha'$ in Phase I (so in particular $\alpha' \le \sqrt N - 1$);
for $N > 0$ neither assumption is needed (the orbits stay in $[\alpha, \alpha + 1]$ and
$[\alpha', \alpha' + 1]$, where $x \mapsto N/x$ is strictly decreasing), so both are replaced by
$N > 0$. For $N = 0$ the claim fails ($\alpha = 1/5$, $\alpha' = 3/10$, $m = 1$).

## Sources

- Jaap de Jonge, *Intervals of N-Expansions with Many Gaps*, INTEGERS 26 (2026), Article A75, Lemma 2.

Stated but not proved: `MetaMathlibExt.nExpansion_orbit_gt_iff_odd` is written with `theorem_wanted` in [WantedExt/Dynamics/NExpansionGapsWanted.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Dynamics/NExpansionGapsWanted.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/low-dimensional-dynamics/n-continued-fraction-expansions/index.html#n-expansion-orbit-gt-iff-odd).

## The ideal periodic points decrease

Let $N$ be a natural number, let $\alpha$ be a real
number with $0 < \alpha \le \sqrt N - 1$, and let $T_\alpha$ be the $N$-expansion map on
$I_\alpha = [\alpha, \alpha + 1]$. For $m \ge 1$ write $|d_m|$ for the length of the digit string
of the ideal period word $d_m$. Let $k, \ell \ge 1$ and let $x, y \in I_\alpha$ be such that for
every $i \ge 0$ the digit of $T_\alpha^i(x)$ is entry $i \bmod |d_k|$ (counting from $0$) of the
digit string of $d_k$, and the digit of $T_\alpha^i(y)$ is entry $i \bmod |d_\ell|$ of the digit
string of $d_\ell$; that is, the expansions of $x$ and $y$ are purely periodic with period words
$d_k$ and $d_\ell$. Then $x < y$ if and only if $\ell < k$.

The source works in Phase I; only the assumption $0 < \alpha \le \sqrt N - 1$ is kept here, which
makes $T_\alpha$ expanding, so that a digit sequence determines its point.

## Sources

- Jaap de Jonge, *Intervals of N-Expansions with Many Gaps*, INTEGERS 26 (2026), Article A75, Lemma 4.

Stated but not proved: `MetaMathlibExt.idealPeriodWord_point_lt_iff` is written with `theorem_wanted` in [WantedExt/Dynamics/NExpansionGapsWanted.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Dynamics/NExpansionGapsWanted.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/low-dimensional-dynamics/n-continued-fraction-expansions/index.html#ideal-period-word-point-lt-iff).

## The ideal periodic point is the least point of its orbit

Let $N$ be a natural number,
let $\alpha$ be a real number with $0 < \alpha \le \sqrt N - 1$, and let $T_\alpha$ be the
$N$-expansion map on $I_\alpha = [\alpha, \alpha + 1]$. Let $n \ge 1$, write $|d_n|$ for the
length of the digit string of the ideal period word $d_n$, and let $x \in I_\alpha$ be such that
for every $i \ge 0$ the digit of $T_\alpha^i(x)$ is entry $i \bmod |d_n|$ (counting from $0$) of
that digit string, so that the expansion of $x$ is purely periodic with period word $d_n$. Then
$x \le T_\alpha^j(x)$ for every $j \ge 0$.

The source assumes Phase I; only the assumption $0 < \alpha \le \sqrt N - 1$ is kept here.

## Sources

- Jaap de Jonge, *Intervals of N-Expansions with Many Gaps*, INTEGERS 26 (2026), Article A75, Lemma 5.

Stated but not proved: `MetaMathlibExt.idealPeriodWord_point_le_orbit` is written with `theorem_wanted` in [WantedExt/Dynamics/NExpansionGapsWanted.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Dynamics/NExpansionGapsWanted.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/low-dimensional-dynamics/n-continued-fraction-expansions/index.html#ideal-period-word-point-le-orbit).

## Length of the ideal period words

For every $n \ge 1$, the digit string of the ideal
period word $d_n$ (the concatenation of its blocks of partial quotients) has length
$|d_n| = 2^{n+1} - (-1)^n$.

The source derives this from the recursion $|d_n| = 2|d_{n-1}| - 3(-1)^n$.

## Sources

- Jaap de Jonge, *Intervals of N-Expansions with Many Gaps*, INTEGERS 26 (2026), Article A75, Lemma 7.

Stated but not proved: `MetaMathlibExt.idealPeriodWord_flatten_length` is written with `theorem_wanted` in [WantedExt/Dynamics/NExpansionGapsWanted.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Dynamics/NExpansionGapsWanted.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/low-dimensional-dynamics/n-continued-fraction-expansions/index.html#ideal-period-word-flatten-length).

## Block counts of the ideal period words

For every $n \ge 1$, the ideal period word $d_n$
contains exactly $2^{n-1}$ blocks $2, 2$, and the number $c_n$ of its blocks $2, 1, 1$ satisfies
$3 c_n = 2^n - (-1)^n$; that is, $c_n = (2^n + 1)/3$ for odd $n$ and $c_n = (2^n - 1)/3$ for even
$n$.

In this lemma the source names the blocks $a = 2, 2$ and $b = 2, 1, 1$, the reverse of its
Definition 7; the counts are stated by block, so the naming does not matter.

## Sources

- Jaap de Jonge, *Intervals of N-Expansions with Many Gaps*, INTEGERS 26 (2026), Article A75, Lemma 8.

Stated but not proved: `MetaMathlibExt.idealPeriodWord_count_blocks` is written with `theorem_wanted` in [WantedExt/Dynamics/NExpansionGapsWanted.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Dynamics/NExpansionGapsWanted.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/low-dimensional-dynamics/n-continued-fraction-expansions/index.html#ideal-period-word-count-blocks).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: N-continued fraction expansions](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/low-dimensional-dynamics/n-continued-fraction-expansions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Dynamics/low-dimensional-dynamics/n-continued-fraction-expansions)
