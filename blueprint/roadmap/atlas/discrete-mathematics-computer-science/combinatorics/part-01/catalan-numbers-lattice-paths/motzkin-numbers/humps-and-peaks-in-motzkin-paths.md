---
declaration: section
origin: cited
lean: MetaMathlibExt.motzkin_hump_peak_height_distribution, MetaMathlibExt.motzkinStep, MetaMathlibExt.IsMotzkinPrefix, MetaMathlibExt.IsMotzkinHump, MetaMathlibExt.isMotzkinPrefix_iff, MetaMathlibExt.IsMotzkinPrefixFinite, MetaMathlibExt.isMotzkinPrefixFinite_iff, MetaMathlibExt.isMotzkinHump_iff
statement: formalized
---

# Humps and peaks in Motzkin paths

40 results, 33 proved and 7 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/humps-and-peaks-in-motzkin-paths/index.html).

## Humps and peaks at a given height in Motzkin paths

Let $n \ge 2$ and $k \ge 1$. A Motzkin
path of length $n$ is a sequence of $n$ steps, each up ($+1$), flat ($0$) or down ($-1$), whose
partial sums are all nonnegative and whose total is $0$. A hump at height $k$ of such a path is
a pair of positions $i < j$ such that step $i$ is up, step $j$ is down, every step strictly
between them is flat, and the sum of the steps up to and including step $i$ equals $k$; a peak
at height $k$ is such a hump with $j = i + 1$. Let $H_{n,k}$ be the number of pairs consisting
of a Motzkin path of length $n$ and a hump at height $k$ of it, and let $P_{n,k}$ be the same
count for peaks. Then, as rational numbers,

$$H_{n,k} = \sum_{j} \frac{4k}{n - j + 2k} \binom{n}{j} \binom{n - j - 1}{(n - j)/2 + k - 1}$$

and

$$P_{n,k} = \sum_{j} \frac{4k}{n - j + 2k} \binom{n - 1}{j} \binom{n - j - 1}{(n - j)/2 + k - 1},$$

where both sums run over the integers $0 \le j \le n - 2k$ with $j \equiv n \pmod 2$.

## Sources

- Xiaomei Chen, "Humps in Motzkin Paths and Standard Young Tableaux in a $(2,1)$-Hook", Journal of Integer Sequences 28 (2025), Article 25.8.1, Theorem `thm:22`, lines 147-156, <https://cs.uwaterloo.ca/journals/JIS/VOL28/Chen/chen36.tex>.

Formalized by `MetaMathlibExt.motzkin_hump_peak_height_distribution`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/MotzkinHumpPeakHeight.lean, line 1583](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MotzkinHumpPeakHeight.lean#L1583). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/humps-and-peaks-in-motzkin-paths/index.html#motzkin-hump-peak-height-distribution).

## Height change of a Motzkin step

The three Motzkin steps are encoded as $0 = D$ (down),
$1 = F$ (flat) and $2 = U$ (up). The height change of the step encoded by $s \in \{0, 1, 2\}$
is the integer $s - 1$; thus $D$ changes the height by $-1$, $F$ by $0$ and $U$ by $+1$.

## Sources

- Xiaomei Chen, *Humps in Motzkin Paths and Standard Young Tableaux in a (2,1)-Hook*, Journal of Integer Sequences 28 (2025), Article 25.8.1, Section 1 (definitions).

Formalized by `MetaMathlibExt.motzkinStep`, a definition declared in [WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/humps-and-peaks-in-motzkin-paths/index.html#motzkin-step).

## Motzkin prefix

Let $p = p_0 p_1 \cdots p_{n-1}$ be a word of length $n$ in the steps $D$,
$F$, $U$ (encoded as $0$, $1$, $2$), whose vertical displacements are $-1$, $0$ and $+1$, and let
$h \in \mathbb{Z}$. The word $p$ is a Motzkin prefix ending at height $h$ when, for every natural
number $m \le n$, the sum of the displacements of $p_0, \dots, p_{m-1}$ is nonnegative, and the
sum of the displacements of all $n$ steps is $h$.

## Sources

- Xiaomei Chen, *Humps in Motzkin Paths and Standard Young Tableaux in a (2,1)-Hook*, Journal of Integer Sequences 28 (2025), Article 25.8.1, Section 1 (definitions).

Formalized by `MetaMathlibExt.IsMotzkinPrefix`, a definition declared in [WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/humps-and-peaks-in-motzkin-paths/index.html#is-motzkin-prefix).

## Motzkin hump

Let $p = p_0 p_1 \cdots p_{n-1}$ be a word of length $n$ in the steps $D$,
$F$, $U$ (encoded as $0$, $1$, $2$), whose vertical displacements are $-1$, $0$ and $+1$. For
$k \in \mathbb{N}$ and positions $i, j \in \{0, \dots, n-1\}$, the pair $(i, j)$ is a hump of
height $k$ in $p$ when $i < j$, $p_i = U$, $p_j = D$, every $p_r$ with $i < r < j$ is $F$, and the
height after step $i$, that is, the sum of the displacements of $p_0, \dots, p_i$, equals $k$.

## Sources

- Xiaomei Chen, *Humps in Motzkin Paths and Standard Young Tableaux in a (2,1)-Hook*, Journal of Integer Sequences 28 (2025), Article 25.8.1, Section 1 (definitions).

Formalized by `MetaMathlibExt.IsMotzkinHump`, a definition declared in [WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/humps-and-peaks-in-motzkin-paths/index.html#is-motzkin-hump).

## Unfolding the Motzkin prefix condition

Let $p = p_0 p_1 \cdots p_{n-1}$ be a word of
length $n$ in the steps $D$, $F$, $U$, whose vertical displacements are $-1$, $0$ and $+1$, and let
$h \in \mathbb{Z}$. Then $p$ is a Motzkin prefix ending at height $h$ if and only if, for every
natural number $m \le n$, the sum of the displacements of $p_0, \dots, p_{m-1}$ is nonnegative,
and the sum of the displacements of all $n$ steps is $h$.

## Sources

- Xiaomei Chen, *Humps in Motzkin Paths and Standard Young Tableaux in a (2,1)-Hook*, Journal of Integer Sequences 28 (2025), Article 25.8.1, Section 1 (definitions).

Formalized by `MetaMathlibExt.isMotzkinPrefix_iff`, a theorem declared in [WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/humps-and-peaks-in-motzkin-paths/index.html#is-motzkin-prefix-iff).

## Bounded Motzkin prefix condition

Let $p = p_0 p_1 \cdots p_{n-1}$ be a word of length $n$
in the steps $D$, $F$, $U$ (encoded as $0$, $1$, $2$), whose vertical displacements are $-1$, $0$
and $+1$, and let $h \in \mathbb{Z}$. The word $p$ satisfies the bounded Motzkin prefix condition
for $h$ when, for every $m \in \{0, 1, \dots, n\}$, the sum of the displacements of
$p_0, \dots, p_{m-1}$ is nonnegative, and the sum of the displacements of all $n$ steps is $h$.

## Sources

- Xiaomei Chen, *Humps in Motzkin Paths and Standard Young Tableaux in a (2,1)-Hook*, Journal of Integer Sequences 28 (2025), Article 25.8.1, Section 1 (definitions).

Formalized by `MetaMathlibExt.IsMotzkinPrefixFinite`, a definition declared in [WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/humps-and-peaks-in-motzkin-paths/index.html#is-motzkin-prefix-finite).

## Bounded form of the Motzkin prefix condition

Let $p$ be a word of length $n$ in the steps
$D$, $F$, $U$ and let $h \in \mathbb{Z}$. Then $p$ satisfies the bounded Motzkin prefix condition
for $h$, in which the prefix length $m$ ranges over $\{0, 1, \dots, n\}$, if and only if $p$ is
a Motzkin prefix ending at height $h$, in which $m$ ranges over all natural numbers with
$m \le n$.

## Sources

- Xiaomei Chen, *Humps in Motzkin Paths and Standard Young Tableaux in a (2,1)-Hook*, Journal of Integer Sequences 28 (2025), Article 25.8.1, Section 1 (definitions).

Formalized by `MetaMathlibExt.isMotzkinPrefixFinite_iff`, a theorem declared in [WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/humps-and-peaks-in-motzkin-paths/index.html#is-motzkin-prefix-finite-iff).

## Characterization of Motzkin humps

Write a path of length $n$ as a sequence of steps
$p_0, \dots, p_{n-1}$, and let $s(p_r) \in \{-1, 0, 1\}$ be the vertical displacement of the
step $p_r$ (down, flat or up). For a natural number $k$ and positions $i, j < n$, the pair
$(i, j)$ is a hump of height $k$ if and only if $i < j$, $s(p_i) = 1$, $s(p_j) = -1$,
$s(p_r) = 0$ for every $r$ with $i < r < j$, and $\sum_{r \le i} s(p_r) = k$.

## Sources

- Xiaomei Chen, *Humps in Motzkin Paths and Standard Young Tableaux in a (2,1)-Hook*, Journal of Integer Sequences 28 (2025), Article 25.8.1, Section 1 (definitions).

Formalized by `MetaMathlibExt.isMotzkinHump_iff`, a theorem declared in [WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/humps-and-peaks-in-motzkin-paths/index.html#is-motzkin-hump-iff).

## Motzkin peak

Let $p$ be a word of length $n$ in the steps $D$, $F$, $U$, let
$k \in \mathbb{N}$, and let $i, j \in \{0, \dots, n-1\}$. The pair $(i, j)$ is a peak of height
$k$ in $p$ when it is a hump of height $k$ in $p$ and $j = i + 1$, that is, when the down step
$p_j$ immediately follows the up step $p_i$.

## Sources

- Xiaomei Chen, *Humps in Motzkin Paths and Standard Young Tableaux in a (2,1)-Hook*, Journal of Integer Sequences 28 (2025), Article 25.8.1, Section 1 (definitions).

Formalized by `MetaMathlibExt.IsMotzkinPeak`, a definition declared in [WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/humps-and-peaks-in-motzkin-paths/index.html#is-motzkin-peak).

## Peaks are humps with adjacent endpoints

Let $p$ be a word of length $n$ in the steps $D$,
$F$, $U$, let $k \in \mathbb{N}$, and let $i, j \in \{0, \dots, n-1\}$. Then $(i, j)$ is a peak of
height $k$ in $p$ if and only if $(i, j)$ is a hump of height $k$ in $p$ and $j = i + 1$.

## Sources

- Xiaomei Chen, *Humps in Motzkin Paths and Standard Young Tableaux in a (2,1)-Hook*, Journal of Integer Sequences 28 (2025), Article 25.8.1, Section 1 (definitions).

Formalized by `MetaMathlibExt.isMotzkinPeak_iff`, a theorem declared in [WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/humps-and-peaks-in-motzkin-paths/index.html#is-motzkin-peak-iff).

## Paths whose last non-flat step is up

A word $p = p_0 p_1 \cdots p_{n-1}$ of length $n$
in the steps $U$ (up), $F$ (flat) and $D$ (down) has last non-flat step up when some position
$i$ has $p_i = U$ and every later step $p_j$ with $j > i$ is $F$. In particular, such a word
contains an up step.

Among the Motzkin prefixes of length $n$ ending at height $h$ (words that never go below height
$0$ and end at height $h$), these words form the paper's set $\mathcal{M}^{*U}_{n,h}$.

## Sources

- Xiaomei Chen, *Humps in Motzkin Paths and Standard Young Tableaux in a (2,1)-Hook*, Journal of Integer Sequences 28 (2025), Article 25.8.1, Section 1 (definitions).

Formalized by `MetaMathlibExt.LastNonflatStepUp`, a definition declared in [WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/humps-and-peaks-in-motzkin-paths/index.html#last-nonflat-step-up).

## Characterization of words whose last non-flat step is up

Let $p = p_0 p_1 \cdots p_{n-1}$
be a word of length $n$ in the steps $D$, $F$, $U$. Then the last non-flat step of $p$ is $U$ if
and only if there is a position $i$ with $p_i = U$ such that $p_j = F$ for every position $j > i$.

## Sources

- Xiaomei Chen, *Humps in Motzkin Paths and Standard Young Tableaux in a (2,1)-Hook*, Journal of Integer Sequences 28 (2025), Article 25.8.1, Section 1 (definitions).

Formalized by `MetaMathlibExt.lastNonflatStepUp_iff`, a theorem declared in [WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/humps-and-peaks-in-motzkin-paths/index.html#last-nonflat-step-up-iff).

## Paths whose first non-up step is down

Write a path of length $n$ as a sequence of steps
$p_0, \dots, p_{n-1}$, each $D$ (down), $F$ (flat) or $U$ (up), encoded as $0$, $1$, $2$. The
path has first non-up step down when there is a position $i$ with $p_i = D$ and $p_j = U$ for
every $j < i$. In particular, a path all of whose steps are up steps, including the empty path,
does not qualify.

For a Motzkin prefix ending at height $h$, this is membership in the paper's set
$\mathcal{M}^{D*}_{n,h}$.

## Sources

- Xiaomei Chen, *Humps in Motzkin Paths and Standard Young Tableaux in a (2,1)-Hook*, Journal of Integer Sequences 28 (2025), Article 25.8.1, Section 1 (definitions).

Formalized by `MetaMathlibExt.FirstNonupStepDown`, a definition declared in [WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/humps-and-peaks-in-motzkin-paths/index.html#first-nonup-step-down).

## Characterization of paths whose first non-up step is down

Write a path of length $n$ as
a sequence of steps $p_0, \dots, p_{n-1}$, each $D$ (down), $F$ (flat) or $U$ (up), encoded as
$0$, $1$, $2$. The path has first non-up step $D$ if and only if there is a position $i$ with
$p_i = D$ and $p_j = U$ for every $j < i$.

## Sources

- Xiaomei Chen, *Humps in Motzkin Paths and Standard Young Tableaux in a (2,1)-Hook*, Journal of Integer Sequences 28 (2025), Article 25.8.1, Section 1 (definitions).

Formalized by `MetaMathlibExt.firstNonupStepDown_iff`, a theorem declared in [WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/humps-and-peaks-in-motzkin-paths/index.html#first-nonup-step-down-iff).

## Paths ending with an up step

Write a path of length $n$ as a sequence of steps
$p_0, \dots, p_{n-1}$, each $D$ (down), $F$ (flat) or $U$ (up), encoded as $0$, $1$, $2$. The
path ends with an up step when it has a last position, that is, some $i < n$ with $i + 1 = n$,
and $p_i = U$.

## Sources

- Xiaomei Chen, *Humps in Motzkin Paths and Standard Young Tableaux in a (2,1)-Hook*, Journal of Integer Sequences 28 (2025), Article 25.8.1, Lemma 3 (`jis-2025-25.8.1-lem-3`).

Formalized by `MetaMathlibExt.EndsWithUp`, a definition declared in [WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/humps-and-peaks-in-motzkin-paths/index.html#ends-with-up).

## Characterization of paths ending with an up step

Write a path of length $n$ as a
sequence of steps $p_0, \dots, p_{n-1}$, each $D$ (down), $F$ (flat) or $U$ (up), encoded as
$0$, $1$, $2$. The path ends with an up step if and only if there is a position $i < n$ with
$i + 1 = n$ and $p_i = U$.

## Sources

- Xiaomei Chen, *Humps in Motzkin Paths and Standard Young Tableaux in a (2,1)-Hook*, Journal of Integer Sequences 28 (2025), Article 25.8.1, Lemma 3 (`jis-2025-25.8.1-lem-3`).

Formalized by `MetaMathlibExt.endsWithUp_iff`, a theorem declared in [WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/humps-and-peaks-in-motzkin-paths/index.html#ends-with-up-iff).

## Number of humps of a given height in Motzkin paths

A Motzkin path of length $n$ is a
word of $n$ steps $U = (1,1)$, $F = (1,0)$ and $D = (1,-1)$ that ends at height $0$ and never
goes below height $0$. A hump of height $k$ in such a path is a pair consisting of an up step
and a later down step with only flat steps between them, where the up step ends at height $k$.
For natural numbers $n$ and $k$, $H_{n,k}$ is the number of pairs $(P, h)$ with $P$ a Motzkin
path of length $n$ and $h$ a hump of height $k$ in $P$, that is, the number of Motzkin paths of
length $n$ with one distinguished hump of height $k$.

## Sources

- Xiaomei Chen, *Humps in Motzkin Paths and Standard Young Tableaux in a (2,1)-Hook*, Journal of Integer Sequences 28 (2025), Article 25.8.1, Section 1 (definitions).

Formalized by `MetaMathlibExt.motzkinHumpCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/humps-and-peaks-in-motzkin-paths/index.html#motzkin-hump-count).

## Motzkin generating function

The Motzkin series is the formal power series
$M(x) = \sum_{n \ge 0} m_n x^n$ in $\mathbb{Z}[[x]]$, where $m_n$ is the $n$-th Motzkin number.

## Sources

- Xiaomei Chen, *Humps in Motzkin Paths and Standard Young Tableaux in a (2,1)-Hook*, Journal of Integer Sequences 28 (2025), Article 25.8.1, Section 1 (definitions).

Formalized by `MetaMathlibExt.motzkinSeries`, a definition declared in [WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/humps-and-peaks-in-motzkin-paths/index.html#motzkin-series).

## Standard Young tableau

A standard Young tableau of order $n$ is encoded by a map $T$ that
assigns to each entry $i \in \{0, \dots, n-1\}$ a cell $T(i) = (r_i, c_i)$ with row and column
indices in $\{0, \dots, n-1\}$. The map $T$ is a standard Young tableau when it is injective
and, for every entry $i$ and every cell $(r, c)$ with $r \le r_i$ and $c \le c_i$, there is an
entry $j \le i$ with $T(j) = (r, c)$.

It follows that for every $m \le n$ the cells of the entries $0, \dots, m-1$ form a Young
diagram, and that entries increase strictly along rows and down columns.

## Sources

- Xiaomei Chen, *Humps in Motzkin Paths and Standard Young Tableaux in a (2,1)-Hook*, Journal of Integer Sequences 28 (2025), Article 25.8.1, Section 1 (definitions).

Formalized by `MetaMathlibExt.IsStandardYoungTableau`, a definition declared in [WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/humps-and-peaks-in-motzkin-paths/index.html#is-standard-young-tableau).

## Unfolding the standard Young tableau condition

Let $T$ assign to each entry
$i \in \{0, \dots, n-1\}$ a cell $T(i) = (r_i, c_i)$ with row and column indices in
$\{0, \dots, n-1\}$. Then $T$ is a standard Young tableau of order $n$ if and only if $T$ is
injective and, for every entry $i$ and every cell $(r, c)$ with $r \le r_i$ and $c \le c_i$,
there is an entry $j \le i$ with $T(j) = (r, c)$.

## Sources

- Xiaomei Chen, *Humps in Motzkin Paths and Standard Young Tableaux in a (2,1)-Hook*, Journal of Integer Sequences 28 (2025), Article 25.8.1, Section 1 (definitions).

Formalized by `MetaMathlibExt.isStandardYoungTableau_iff`, a theorem declared in [WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/humps-and-peaks-in-motzkin-paths/index.html#is-standard-young-tableau-iff).

## Tableaux in the $(2,1)$-hook

Let $T$ assign to each entry $i < n$ a cell $(r_i, c_i)$
with zero-based row $r_i < n$ and column $c_i < n$. Then $T$ lies in the $(2,1)$-hook when no
entry occupies a cell whose row is at least $2$ and whose column is at least $1$, that is, when
no $i$ has both $r_i \ge 2$ and $c_i \ge 1$.

## Sources

- Xiaomei Chen, *Humps in Motzkin Paths and Standard Young Tableaux in a (2,1)-Hook*, Journal of Integer Sequences 28 (2025), Article 25.8.1, Section 1 (definitions).

Formalized by `MetaMathlibExt.IsInTwoOneHook`, a definition declared in [WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/humps-and-peaks-in-motzkin-paths/index.html#is-in-two-one-hook).

## Characterization of tableaux in the $(2,1)$-hook

Let $T$ assign to each entry $i < n$ a
cell $(r_i, c_i)$ with zero-based row $r_i < n$ and column $c_i < n$. Then $T$ lies in the
$(2,1)$-hook if and only if for no entry $i$ do both $r_i \ge 2$ and $c_i \ge 1$ hold.

## Sources

- Xiaomei Chen, *Humps in Motzkin Paths and Standard Young Tableaux in a (2,1)-Hook*, Journal of Integer Sequences 28 (2025), Article 25.8.1, Section 1 (definitions).

Formalized by `MetaMathlibExt.isInTwoOneHook_iff`, a theorem declared in [WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean, line 266](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean#L266). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/humps-and-peaks-in-motzkin-paths/index.html#is-in-two-one-hook-iff).

## Row length of a tableau

For a natural number $n$, let $T$ assign to each entry
$i \in \{0, \dots, n-1\}$ a cell $T(i)$, given by a zero-based row index and a zero-based column
index, both in $\{0, \dots, n-1\}$. For a natural number $r$, the length of row $r$ is the number
of entries $i$ whose cell $T(i)$ lies in row $r$.

## Sources

- Xiaomei Chen, *Humps in Motzkin Paths and Standard Young Tableaux in a (2,1)-Hook*, Journal of Integer Sequences 28 (2025), Article 25.8.1, Section 1 (definitions).

Formalized by `MetaMathlibExt.tableauRowLength`, a definition declared in [WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean, line 283](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean#L283). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/humps-and-peaks-in-motzkin-paths/index.html#tableau-row-length).

## First-two-row difference of a tableau

Let $T$ assign to each entry $i < n$ a cell
$(r_i, c_i)$ with zero-based row $r_i < n$ and column $c_i < n$, and let $\lambda_1$ and
$\lambda_2$ be the numbers of entries $i$ with $r_i = 0$ and with $r_i = 1$ respectively. For a
natural number $k$, $T$ has first-two-row difference $k$ when $\lambda_1 = \lambda_2 + k$, that
is, when $\lambda_1 - \lambda_2 = k$.

## Sources

- Xiaomei Chen, *Humps in Motzkin Paths and Standard Young Tableaux in a (2,1)-Hook*, Journal of Integer Sequences 28 (2025), Article 25.8.1, Section 1 (definitions).

Formalized by `MetaMathlibExt.HasFirstTwoRowDifference`, a definition declared in [WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean, line 291](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean#L291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/humps-and-peaks-in-motzkin-paths/index.html#has-first-two-row-difference).

## Characterization of the first-two-row difference

Let $T$ assign to each entry $i < n$ a
cell $(r_i, c_i)$ with zero-based row $r_i < n$ and column $c_i < n$, and let $\lambda_1$ and
$\lambda_2$ be the numbers of entries $i$ with $r_i = 0$ and with $r_i = 1$ respectively. For a
natural number $k$, $T$ has first-two-row difference $k$ if and only if
$\lambda_1 = \lambda_2 + k$.

## Sources

- Xiaomei Chen, *Humps in Motzkin Paths and Standard Young Tableaux in a (2,1)-Hook*, Journal of Integer Sequences 28 (2025), Article 25.8.1, Section 1 (definitions).

Formalized by `MetaMathlibExt.hasFirstTwoRowDifference_iff`, a theorem declared in [WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean, line 298](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean#L298). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/humps-and-peaks-in-motzkin-paths/index.html#has-first-two-row-difference-iff).

## Standard Young tableaux in the $(2,1)$-hook with given row difference

For natural numbers
$n$ and $k$, $\mathrm{SYT}_k(2,1;n)$ is the number of standard Young tableaux of order $n$ whose
shape $\lambda$ lies in the $(2,1)$-hook, that is $\lambda_3 \le 1$, and whose first two row
lengths satisfy $\lambda_1 = \lambda_2 + k$ (a missing row has length $0$).

## Sources

- Xiaomei Chen, *Humps in Motzkin Paths and Standard Young Tableaux in a (2,1)-Hook*, Journal of Integer Sequences 28 (2025), Article 25.8.1, Section 1 (definitions).

Formalized by `MetaMathlibExt.sytHookCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean, line 317](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean#L317). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/humps-and-peaks-in-motzkin-paths/index.html#syt-hook-count).

## Motzkin paths with a marked hump, over all heights

For a natural number $n$, this is
the set of triples $(k, P, h)$ where $k$ is a natural number with
$1 \le k \le \lfloor n/2 \rfloor$, $P$ is a Motzkin path of length $n$ (a word of $n$ steps
$U = (1,1)$, $F = (1,0)$ and $D = (1,-1)$ that ends at height $0$ and never goes below height
$0$), and $h$ is a hump of height $k$ in $P$: an up step and a later down step with only flat
steps between them, where the up step ends at height $k$, recorded by the positions of its two
steps.

This is the paper's disjoint union $\bigcup_{1 \le k \le \lfloor n/2 \rfloor} \mathcal{H}_{n,k}$,
keeping the height index $k$ with each marked path.

## Sources

- Xiaomei Chen, *Humps in Motzkin Paths and Standard Young Tableaux in a (2,1)-Hook*, Journal of Integer Sequences 28 (2025), Article 25.8.1, Lemma 3 (`jis-2025-25.8.1-lem-3`).

Formalized by `MetaMathlibExt.MotzkinHumpFamily`, a definition declared in [WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean, line 385](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean#L385). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/humps-and-peaks-in-motzkin-paths/index.html#motzkin-hump-family).

## Motzkin prefixes of even height whose last non-flat step is up

Use the steps
$U = (1,1)$, $F = (1,0)$ and $D = (1,-1)$, and call a word in these steps a Motzkin prefix if
none of its initial segments ends below height $0$. For a natural number $n$, this is the set
of pairs $(k, p)$ where $k$ is a natural number with $1 \le k \le \lfloor n/2 \rfloor$ and $p$
is a Motzkin prefix of length $n$ ending at height $2k$ that contains a $U$ after which every
step is $F$.

This is the paper's disjoint union
$\bigcup_{1 \le k \le \lfloor n/2 \rfloor} \mathcal{M}^{*U}_{n,2k}$, keeping the index $k$ with
each path.

## Sources

- Xiaomei Chen, *Humps in Motzkin Paths and Standard Young Tableaux in a (2,1)-Hook*, Journal of Integer Sequences 28 (2025), Article 25.8.1, Lemma 3 (`jis-2025-25.8.1-lem-3`).

Formalized by `MetaMathlibExt.MotzkinLastUpEvenFamily`, a definition declared in [WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean, line 395](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean#L395). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/humps-and-peaks-in-motzkin-paths/index.html#motzkin-last-up-even-family).

## Motzkin prefixes whose first non-up step is down

Use the steps $U = (1,1)$,
$F = (1,0)$ and $D = (1,-1)$, and call a word in these steps a Motzkin prefix if none of its
initial segments ends below height $0$. For a natural number $n$, this is the set of pairs
$(k, p)$ where $k$ is a natural number with $k \le n - 2$ and $p$ is a Motzkin prefix of length
$n$ ending at height $k$ whose first step other than $U$ exists and is $D$.

This is the paper's disjoint union $\bigcup_{0 \le k \le n-2} \mathcal{M}^{D*}_{n,k}$, keeping
the index $k$ with each path.

## Sources

- Xiaomei Chen, *Humps in Motzkin Paths and Standard Young Tableaux in a (2,1)-Hook*, Journal of Integer Sequences 28 (2025), Article 25.8.1, Lemma 6 (`jis-2025-25.8.1-lem-6`).

Formalized by `MetaMathlibExt.MotzkinFirstDownFamily`, a definition declared in [WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean, line 406](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean#L406). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/humps-and-peaks-in-motzkin-paths/index.html#motzkin-first-down-family).

## Hook tableaux of order 3 with row difference 1

The number $\mathrm{SYT}_1(2,1;3)$ of
standard Young tableaux of order $3$ in the $(2,1)$-hook whose first row is longer than its
second row by exactly $1$ equals $2$.

## Sources

- Xiaomei Chen, *Humps in Motzkin Paths and Standard Young Tableaux in a (2,1)-Hook*, Journal of Integer Sequences 28 (2025), Article 25.8.1, Initial-values table.

Formalized by `MetaMathlibExt.sytHookCount_three_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean, line 414](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean#L414). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/humps-and-peaks-in-motzkin-paths/index.html#syt-hook-count-three-one).

## Hook tableaux of order 3 with row difference 0

The number $\mathrm{SYT}_0(2,1;3)$ of
standard Young tableaux of order $3$ in the $(2,1)$-hook whose first two rows have the same
length equals $1$.

## Sources

- Xiaomei Chen, *Humps in Motzkin Paths and Standard Young Tableaux in a (2,1)-Hook*, Journal of Integer Sequences 28 (2025), Article 25.8.1, Initial-values table.

Formalized by `MetaMathlibExt.sytHookCount_three_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean, line 422](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean#L422). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/humps-and-peaks-in-motzkin-paths/index.html#syt-hook-count-three-zero).

## Hook tableaux of order 2 with row difference 1

The number $\mathrm{SYT}_1(2,1;2)$ of
standard Young tableaux of order $2$ in the $(2,1)$-hook whose first row is longer than its
second row by exactly $1$ equals $0$.

## Sources

- Xiaomei Chen, *Humps in Motzkin Paths and Standard Young Tableaux in a (2,1)-Hook*, Journal of Integer Sequences 28 (2025), Article 25.8.1, Initial-values table.

Formalized by `MetaMathlibExt.sytHookCount_two_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean, line 430](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean#L430). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/humps-and-peaks-in-motzkin-paths/index.html#syt-hook-count-two-one).

## Humps of height one in Motzkin paths of length four

Let $H_{n,k}$ be the number of
pairs $(P, h)$ where $P$ is a Motzkin path of length $n$ and $h$ is a hump of height $k$ in $P$,
that is, an up step and a later down step with only flat steps between them, where the up step
ends at height $k$. Then $H_{4,1} = 8$.

## Sources

- Xiaomei Chen, *Humps in Motzkin Paths and Standard Young Tableaux in a (2,1)-Hook*, Journal of Integer Sequences 28 (2025), Article 25.8.1, Hump-count table.

Formalized by `MetaMathlibExt.motzkinHumpCount_four_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean, line 438](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean#L438). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/humps-and-peaks-in-motzkin-paths/index.html#motzkin-hump-count-four-one).

## Closed formula for hook tableau counts

For natural numbers $n$ and $k$ with
$k + 2 \le n$, let $\mathrm{SYT}_k(2,1;n)$ be the number of standard Young tableaux of order $n$
in the $(2,1)$-hook whose first row is longer than its second row by exactly $k$. Then, as an
identity of rational numbers,

$$
\mathrm{SYT}_k(2,1;n) = (-1)^{n+k} + \sum_{i=0}^{\lfloor (n-k-1)/2 \rfloor}
\sum_{\substack{0 \le j \le n-k-1-2i \\ j \equiv n+k-1 \pmod 2}}
\frac{2k+2}{n+k+1-2i-j} \binom{n-2i-2}{j} \binom{n-2i-j-1}{\frac{n+k-j-1}{2} - i}.
$$

When $k = 0$ and $2i = n - 1$, the upper argument $n - 2i - 2$ would be $-1$; it is read as $0$,
so the only term of that inner sum, $j = 0$, has binomial factor $\binom{0}{0} = 1$.

## Sources

- Xiaomei Chen, *Humps in Motzkin Paths and Standard Young Tableaux in a (2,1)-Hook*, Journal of Integer Sequences 28 (2025), Article 25.8.1, Theorem 2 (`jis-2025-25.8.1-thm-2`).

Stated but not proved: `MetaMathlibExt.sytHookCount_closedForm` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean, line 451](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean#L451). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/humps-and-peaks-in-motzkin-paths/index.html#syt-hook-count-closed-form).

## Humps correspond to last-up prefixes of twice the height

Use the steps $U = (1,1)$,
$F = (1,0)$ and $D = (1,-1)$. A Motzkin prefix of length $n$ ending at height $h$ is a word of
$n$ steps that never goes below height $0$ and ends at height $h$; a Motzkin path is a Motzkin
prefix ending at height $0$. A hump of height $k$ in a path is a pair of an up step and a later
down step with only flat steps between them, where the up step ends at height $k$; the hump is
a peak when the down step immediately follows the up step. For every natural number $n$ there
is a bijection from the set of triples $(k, P, h)$ with $1 \le k \le \lfloor n/2 \rfloor$, $P$
a Motzkin path of length $n$ and $h$ a hump of height $k$ in $P$, to the set of pairs $(k, p)$
with $1 \le k \le \lfloor n/2 \rfloor$ and $p$ a Motzkin prefix of length $n$ ending at height
$2k$ that contains a $U$ after which every step is $F$. This bijection keeps the index $k$, and
the hump $h$ is a peak exactly when the image path $p$ ends with an up step.

## Sources

- Xiaomei Chen, *Humps in Motzkin Paths and Standard Young Tableaux in a (2,1)-Hook*, Journal of Integer Sequences 28 (2025), Article 25.8.1, Lemma 3 (`jis-2025-25.8.1-lem-3`).

Stated but not proved: `MetaMathlibExt.motzkinHumpFamily_equiv_lastUpEvenFamily` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean, line 468](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean#L468). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/humps-and-peaks-in-motzkin-paths/index.html#motzkin-hump-family-equiv-last-up-even-f).

## Generating function for humps of a fixed height

Let $H_{n,k}$ be the number of pairs
$(P, h)$ where $P$ is a Motzkin path of length $n$ and $h$ is a hump of height $k$ in $P$ (an up
step and a later down step with only flat steps between them, the up step ending at height
$k$), and let $M(x) = \sum_{n \ge 0} m_n x^n$, where $m_n$ is the $n$-th Motzkin number. For
every integer $k \ge 1$, in the ring $\mathbb{Z}[[x]]$ of formal power series,

$$(1 - x) \sum_{n \ge 2k} H_{n,k} \, x^n = x^{2k} M(x)^{2k}.$$

The source also states this result in Riordan-array form.

## Sources

- Xiaomei Chen, *Humps in Motzkin Paths and Standard Young Tableaux in a (2,1)-Hook*, Journal of Integer Sequences 28 (2025), Article 25.8.1, Corollary 5 (`jis-2025-25.8.1-cor-5`).

Stated but not proved: `MetaMathlibExt.motzkinHumpCount_generatingFunction` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean, line 480](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean#L480). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/humps-and-peaks-in-motzkin-paths/index.html#motzkin-hump-count-generating-function).

## A bijection between first-down and even-height last-up Motzkin prefixes

Use the steps
$U = (1,1)$, $F = (1,0)$ and $D = (1,-1)$, and call a word in these steps a Motzkin prefix if
none of its initial segments ends below height $0$. For every natural number $n$ there is a
bijection between the set of pairs $(k, p)$, where $k$ is a natural number with $k + 2 \le n$ and
$p$ is a Motzkin prefix of length $n$ ending at height $k$ whose first step other than $U$ exists
and is $D$, and the set of pairs $(k, p)$, where $k$ is a natural number with
$1 \le k \le \lfloor n/2 \rfloor$ and $p$ is a Motzkin prefix of length $n$ ending at height $2k$
that contains a $U$ after which every step is $F$.

## Sources

- Xiaomei Chen, *Humps in Motzkin Paths and Standard Young Tableaux in a (2,1)-Hook*, Journal of Integer Sequences 28 (2025), Article 25.8.1, Lemma 6 (`jis-2025-25.8.1-lem-6`).

Stated but not proved: `MetaMathlibExt.motzkinFirstDownFamily_equiv_lastUpEvenFamily` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean, line 492](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean#L492). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/humps-and-peaks-in-motzkin-paths/index.html#motzkin-first-down-family-equiv-last-up).

## Generating function for the adjusted $(2,1)$-hook tableau counts

Let $k$ be a natural
number, and let $\mathrm{SYT}_k(2,1;n)$ be the number of standard Young tableaux with $n$ cells
in the $(2,1)$-hook whose first two rows differ in length by $k$. Set
$T_{n,k} = \mathrm{SYT}_k(2,1;n) + (-1)^{n+k+1}$ for $n \ge k$ and $T_{n,k} = 0$ for $n < k$, and
let $M(x) = \sum_{n \ge 0} m_n x^n$ be the generating function of the Motzkin numbers $m_n$.
Then in the ring $\mathbb{Z}[[x]]$ of formal power series

$$(1 + x) \sum_{n \ge 0} T_{n,k} x^n = (x M(x))^{k+1}.$$

Equivalently, $\sum_{n \ge k} T_{n,k} x^n = x^{k+1} M(x)^{k+1} / (1 + x)$; the identity is
stated without division.

## Sources

- Xiaomei Chen, *Humps in Motzkin Paths and Standard Young Tableaux in a (2,1)-Hook*, Journal of Integer Sequences 28 (2025), Article 25.8.1, Lemma 7 (`jis-2025-25.8.1-lem-7`).

Stated but not proved: `MetaMathlibExt.adjustedSytHookCount_generatingFunction` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean, line 501](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean#L501). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/humps-and-peaks-in-motzkin-paths/index.html#adjusted-syt-hook-count-generating-funct).

## Generating function for hook tableau counts

For a natural number $k$, let
$\mathrm{SYT}_k(2,1;n)$ be the number of standard Young tableaux of order $n$ in the
$(2,1)$-hook whose first row is longer than its second row by exactly $k$, and let
$M(x) = \sum_{n \ge 0} m_n x^n$ be the generating function of the Motzkin numbers $m_n$. Then,
in the ring of formal power series with integer coefficients,

$$
(1 + x) \sum_{n \ge k} \mathrm{SYT}_k(2,1;n)\, x^n = x^k \bigl(1 + x\, M(x)^{k+1}\bigr).
$$

The factor $1 + x$ is cleared, so the identity involves no division.

## Sources

- Xiaomei Chen, *Humps in Motzkin Paths and Standard Young Tableaux in a (2,1)-Hook*, Journal of Integer Sequences 28 (2025), Article 25.8.1, Corollary 9 (`jis-2025-25.8.1-cor-9`).

Stated but not proved: `MetaMathlibExt.sytHookCount_generatingFunction` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean, line 513](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean#L513). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/humps-and-peaks-in-motzkin-paths/index.html#syt-hook-count-generating-function).

## Hook tableau counts as differences of hump counts

For natural numbers $m$ and $j$, let
$\mathrm{SYT}_j(2,1;m)$ be the number of standard Young tableaux of order $m$ in the
$(2,1)$-hook whose first row is longer than its second row by exactly $j$, and let $H_{m,j}$ be
the number of Motzkin paths of length $m$ with one distinguished hump of height $j$ (a hump is
an up step followed by flat steps and then a down step; its height is the height reached by the
up step). For natural numbers $n$ and $k$ with $1 \le k \le \lfloor n/2 \rfloor$,

$$
\mathrm{SYT}_{2k-1}(2,1;n+1) + \mathrm{SYT}_{2k-1}(2,1;n) = H_{n+1,k} - H_{n,k},
$$

where the subtraction is taken in the integers.

## Sources

- Xiaomei Chen, *Humps in Motzkin Paths and Standard Young Tableaux in a (2,1)-Hook*, Journal of Integer Sequences 28 (2025), Article 25.8.1, Corollary 10 (`jis-2025-25.8.1-cor-10`).

Stated but not proved: `MetaMathlibExt.sytHookCount_add_eq_humpCount_sub` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean, line 524](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/MotzkinHumpsYoungTableauxWanted.lean#L524). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/humps-and-peaks-in-motzkin-paths/index.html#syt-hook-count-add-eq-hump-count-sub).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Humps and peaks in Motzkin paths](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/humps-and-peaks-in-motzkin-paths/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/humps-and-peaks-in-motzkin-paths)
