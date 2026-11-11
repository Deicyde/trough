---
declaration: section
origin: cited
lean: MetaMathlibExt.SkewDyckStep, MetaMathlibExt.IsSkewDyckWord, MetaMathlibExt.skewDyckWords, MetaMathlibExt.card_skewDyckWords_two, MetaMathlibExt.skewFactorCount, MetaMathlibExt.boxFactor, MetaMathlibExt.kBoxPaths, MetaMathlibExt.kBoxPaths_one_one
statement: formalized
---

# k-box paths and skew Dyck paths

35 results, 22 proved and 13 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/k-box-paths-and-skew-dyck-paths/index.html).

## Skew Dyck steps

A skew Dyck path is built from three kinds of step: the up step
$U = (1,1)$, the down step $D = (1,-1)$ and the left step $L = (-1,-1)$.

## Sources

- Zhang and Zhuang, *A Subfamily of Skew Dyck Paths Related to `k`-ary Trees*, Journal of Integer Sequences 27 (2024), Article 24.2.4, Section 1.

Formalized by `MetaMathlibExt.SkewDyckStep`, an inductive type declared in [WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/k-box-paths-and-skew-dyck-paths/index.html#skew-dyck-step).

## Skew Dyck words

A word $w$ in the steps $U$, $D$, $L$ is a skew Dyck word when neither
$UL$ nor $LU$ occurs in $w$ as two consecutive letters, the number of $U$s in $w$ equals the
number of $D$s and $L$s together, and no prefix of $w$ has more $D$s and $L$s together than
$U$s.

## Sources

- Zhang and Zhuang, *A Subfamily of Skew Dyck Paths Related to `k`-ary Trees*, Journal of Integer Sequences 27 (2024), Article 24.2.4, Section 1.

Formalized by `MetaMathlibExt.IsSkewDyckWord`, a definition declared in [WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/k-box-paths-and-skew-dyck-paths/index.html#is-skew-dyck-word).

## Skew Dyck paths of semilength $m$

For $m \in \mathbb{N}$, the skew Dyck paths of
semilength $m$ are the words of length $2m$ over $\{U, D, L\}$ that avoid the factors $UL$ and
$LU$, have as many $U$s as $D$s and $L$s together, and have no prefix with more $D$s and $L$s
together than $U$s.

## Sources

- Zhang and Zhuang, *A Subfamily of Skew Dyck Paths Related to `k`-ary Trees*, Journal of Integer Sequences 27 (2024), Article 24.2.4, Section 1.

Formalized by `MetaMathlibExt.skewDyckWords`, a definition declared in [WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/k-box-paths-and-skew-dyck-paths/index.html#skew-dyck-words).

## Three skew Dyck paths of semilength $2$

The number of skew Dyck paths of semilength
$2$ is $3$.

They are $UUDD$, $UDUD$ and $UUDL$.

## Sources

- Zhang and Zhuang, *A Subfamily of Skew Dyck Paths Related to `k`-ary Trees*, Journal of Integer Sequences 27 (2024), Article 24.2.4, Section 1.

Formalized by `MetaMathlibExt.card_skewDyckWords_two`, a theorem declared in [WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/k-box-paths-and-skew-dyck-paths/index.html#card-skew-dyck-words-two).

## Occurrences of a factor in a skew Dyck word

For words $f$ and $w$ over the skew Dyck
steps $U$, $D$, $L$, the factor count of $f$ in $w$ is the number of suffixes of $w$, including
$w$ itself and the empty suffix, that begin with $f$. Equivalently, it is the number of positions
of $w$ at which an occurrence of $f$ as a contiguous block starts, overlapping occurrences all
being counted; in particular the empty word has factor count $|w| + 1$ in $w$.

## Sources

- Zhang and Zhuang, *A Subfamily of Skew Dyck Paths Related to `k`-ary Trees*, Journal of Integer Sequences 27 (2024), Article 24.2.4, Section 1.

Formalized by `MetaMathlibExt.skewFactorCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/k-box-paths-and-skew-dyck-paths/index.html#skew-factor-count).

## The $k$-box factor

For $k \ge 0$, the $k$-box factor is the word $U D^k L$ in the skew
Dyck steps: one step $U$, then $k$ steps $D$, then one step $L$.

## Sources

- Zhang and Zhuang, *A Subfamily of Skew Dyck Paths Related to `k`-ary Trees*, Journal of Integer Sequences 27 (2024), Article 24.2.4, Section 3.

Formalized by `MetaMathlibExt.boxFactor`, a definition declared in [WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/k-box-paths-and-skew-dyck-paths/index.html#box-factor).

## $k$-box paths

For natural numbers $k$ and $n$, the set $B_n^{(k)}$ of $k$-box paths of
size $n$ consists of the skew Dyck paths of semilength $(k+2)n - 1$ that contain exactly $n$
occurrences of the factor $U D^k L$. The subtraction is truncated at $0$, so $B_0^{(k)}$
consists of the empty path alone.

## Sources

- Zhang and Zhuang, *A Subfamily of Skew Dyck Paths Related to `k`-ary Trees*, Journal of Integer Sequences 27 (2024), Article 24.2.4, Section 3.

Formalized by `MetaMathlibExt.kBoxPaths`, a definition declared in [WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/k-box-paths-and-skew-dyck-paths/index.html#k-box-paths).

## The $1$-box path of size $1$

The only $1$-box path of size $1$ is $UUDL$.

## Sources

- Zhang and Zhuang, *A Subfamily of Skew Dyck Paths Related to `k`-ary Trees*, Journal of Integer Sequences 27 (2024), Article 24.2.4, Section 3.

Formalized by `MetaMathlibExt.kBoxPaths_one_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/k-box-paths-and-skew-dyck-paths/index.html#k-box-paths-one-one).

## Box words

Let $k \ge 0$ and let $a = (a_1, \dots, a_n)$ be a list of natural numbers
with $n \ge 1$. The box word of $k$ and $a$ is the word in the skew Dyck steps

$$
U^{a_1} D^k L D \; U^{a_2} D^k L D \; \cdots \; U^{a_{n-1}} D^k L D \; U^{a_n} D^k L,
$$

that is, the blocks $U^{a_i} D^k L D$ for $i < n$ followed by $U^{a_n} D^k L$. For the empty
list it is $D^k L$.

## Sources

- Zhang and Zhuang, *A Subfamily of Skew Dyck Paths Related to `k`-ary Trees*, Journal of Integer Sequences 27 (2024), Article 24.2.4, Lemma 2.

Formalized by `MetaMathlibExt.boxWord`, a definition declared in [WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/k-box-paths-and-skew-dyck-paths/index.html#box-word).

## The box word for $k = 1$ and $a = (3, 2)$

For $k = 1$ and $a = (3, 2)$, the box word
$U^{a_1} D^k L D \, U^{a_2} D^k L$ equals $UUUDLDUUDL$.

## Sources

- Zhang and Zhuang, *A Subfamily of Skew Dyck Paths Related to `k`-ary Trees*, Journal of Integer Sequences 27 (2024), Article 24.2.4, Lemma 2.

Formalized by `MetaMathlibExt.boxWord_one_three_two`, a theorem declared in [WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/k-box-paths-and-skew-dyck-paths/index.html#box-word-one-three-two).

## $k$-Dyck words

A word $w$ over the Booleans is a $k$-Dyck word when the number of
letters $\mathrm{true}$ in $w$ is $k$ times the number of letters $\mathrm{false}$, and every
prefix of $w$ contains at least $k$ times as many letters $\mathrm{true}$ as letters
$\mathrm{false}$.

Reading $\mathrm{true}$ as the step $U = (1,1)$ and $\mathrm{false}$ as the step
$D^{(k)} = (k,-k)$, this says that the path ends on the $x$-axis and never goes below it.

## Sources

- Zhang and Zhuang, *A Subfamily of Skew Dyck Paths Related to `k`-ary Trees*, Journal of Integer Sequences 27 (2024), Article 24.2.4, Section 2.

Formalized by `MetaMathlibExt.IsKDyckWord`, a definition declared in [WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/k-box-paths-and-skew-dyck-paths/index.html#is-kdyck-word).

## $k$-Dyck paths of size $n$

Write $U = (1,1)$ and $D^{(k)} = (k,-k)$. The $k$-Dyck paths
of size $n$ are the words of length $(k+1)n$ over $\{U, D^{(k)}\}$ with exactly $n$ steps
$D^{(k)}$ that have $k$ times as many $U$s as $D^{(k)}$s and in which every prefix has at least
$k$ times as many $U$s as $D^{(k)}$s.

## Sources

- Zhang and Zhuang, *A Subfamily of Skew Dyck Paths Related to `k`-ary Trees*, Journal of Integer Sequences 27 (2024), Article 24.2.4, Section 2.

Formalized by `MetaMathlibExt.kDyckWords`, a definition declared in [WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/k-box-paths-and-skew-dyck-paths/index.html#k-dyck-words).

## Three $2$-Dyck paths of size $2$

The number of $2$-Dyck paths of size $2$ is $3$.

## Sources

- Zhang and Zhuang, *A Subfamily of Skew Dyck Paths Related to `k`-ary Trees*, Journal of Integer Sequences 27 (2024), Article 24.2.4, Section 2.

Formalized by `MetaMathlibExt.card_kDyckWords_two_two`, a theorem declared in [WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/k-box-paths-and-skew-dyck-paths/index.html#card-k-dyck-words-two-two).

## Augmentation of a $k$-Dyck word

Let $k \ge 0$ and let $w$ be a word in the letters
$U = (1,1)$ and $D^{(k)} = (k,-k)$, for example a $k$-Dyck path. The augmented path of $w$ is the
word in the skew Dyck steps $U$, $D$, $L$ obtained from $w$ by keeping each letter $U$ and
replacing each letter $D^{(k)}$ by $U D^{k-1} L D$, where $D^{k-1}$ means $k - 1$ copies of $D$
(none when $k \le 1$).

## Sources

- Zhang and Zhuang, *A Subfamily of Skew Dyck Paths Related to `k`-ary Trees*, Journal of Integer Sequences 27 (2024), Article 24.2.4, Section 2.

Formalized by `MetaMathlibExt.augmentKDyckWord`, a definition declared in [WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/k-box-paths-and-skew-dyck-paths/index.html#augment-kdyck-word).

## Augmented $k$-Dyck paths

For natural numbers $k$ and $n$, write $U = (1,1)$ and
$D^{(k)} = (k,-k)$. A $k$-Dyck path of size $n$ is a word of length $(k+1)n$ in the letters $U$
and $D^{(k)}$ that has exactly $n$ letters $D^{(k)}$ and $k$ times as many letters $U$ as letters
$D^{(k)}$, and in which every prefix has at least $k$ times as many letters $U$ as letters
$D^{(k)}$. The augmented path of such a word is the word in the skew Dyck steps $U$, $D$, $L$
obtained by keeping each letter $U$ and replacing each letter $D^{(k)}$ by $U D^{k-1} L D$, where
$D^{k-1}$ means $k - 1$ copies of $D$ (none when $k \le 1$). The set $\hat{D}_n^{(k)}$ of
augmented $k$-Dyck paths of size $n$ is the set of the augmented paths of the $k$-Dyck paths of
size $n$.

The definition is used for $k \ge 2$.

## Sources

- Zhang and Zhuang, *A Subfamily of Skew Dyck Paths Related to `k`-ary Trees*, Journal of Integer Sequences 27 (2024), Article 24.2.4, Section 2.

Formalized by `MetaMathlibExt.augmentedKDyckPaths`, a definition declared in [WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/k-box-paths-and-skew-dyck-paths/index.html#augmented-kdyck-paths).

## Returns of a skew Dyck word

Read a word $w$ over the skew Dyck steps $U = (1,1)$,
$D = (1,-1)$ and $L = (-1,-1)$ as a lattice path starting at the origin. The number of returns of
$w$ is the number of steps of $w$ that end on the $x$-axis, that is, the number of nonempty
prefixes of $w$ that contain as many $U$ steps as $D$ and $L$ steps together.

## Sources

- Zhang and Zhuang, *A Subfamily of Skew Dyck Paths Related to `k`-ary Trees*, Journal of Integer Sequences 27 (2024), Article 24.2.4, Section 3.

Formalized by `MetaMathlibExt.skewReturns`, a definition declared in [WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/k-box-paths-and-skew-dyck-paths/index.html#skew-returns).

## Long ascents of a skew Dyck word

A long ascent of a word $w$ over the skew Dyck steps
$U$, $D$, $L$ is a maximal run of consecutive $U$ steps of length at least $2$. The long ascent
count of $w$ is the number of long ascents of $w$.

## Sources

- Zhang and Zhuang, *A Subfamily of Skew Dyck Paths Related to `k`-ary Trees*, Journal of Integer Sequences 27 (2024), Article 24.2.4, Section 7.

Formalized by `MetaMathlibExt.skewLongAscents`, a definition declared in [WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/k-box-paths-and-skew-dyck-paths/index.html#skew-long-ascents).

## Returns and long ascents of an example skew Dyck path

The word $U D U^5 D L^2 D U D L$
over the skew Dyck steps has exactly two returns and exactly one long ascent.

This is the source's example of a skew Dyck path.

## Sources

- Zhang and Zhuang, *A Subfamily of Skew Dyck Paths Related to `k`-ary Trees*, Journal of Integer Sequences 27 (2024), Article 24.2.4, Figure 1.

Formalized by `MetaMathlibExt.skewReturns_skewLongAscents_example`, a theorem declared in [WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/k-box-paths-and-skew-dyck-paths/index.html#skew-returns-skew-long-ascents-example).

## Generating function of augmented $k$-Dyck paths

Let $k \ge 0$ and let $\hat D_n^{(k)}$
be the set of augmented $k$-Dyck paths of size $n$. Then $G_k(x)$ is the formal power series with
integer coefficients

$$
G_k(x) = \sum_{n \ge 0} |\hat D_n^{(k)}| \, x^n \in \mathbb{Z}[[x]].
$$

## Sources

- Zhang and Zhuang, *A Subfamily of Skew Dyck Paths Related to `k`-ary Trees*, Journal of Integer Sequences 27 (2024), Article 24.2.4, Section 6.

Formalized by `MetaMathlibExt.augmentedKDyckGF`, a definition declared in [WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/k-box-paths-and-skew-dyck-paths/index.html#augmented-kdyck-gf).

## Generating function of $k$-box paths by returns

For $k \in \mathbb{N}$, $F_k(t, x)$ is
the power series in $\mathbb{Z}[t][[x]]$ with constant term $0$ whose coefficient of $x^n$ for
$n \ge 1$ is the sum of $t^{\operatorname{ret}(\mu)}$ over the set $B_n^{(k)}$ of $k$-box paths
$\mu$ of size $n$, where $\operatorname{ret}(\mu)$ is the number of returns of $\mu$; that is,
$F_k(t, x) = \sum_{n \ge 1} \sum_{\mu \in B_n^{(k)}} t^{\operatorname{ret}(\mu)} x^n$.

## Sources

- Zhang and Zhuang, *A Subfamily of Skew Dyck Paths Related to `k`-ary Trees*, Journal of Integer Sequences 27 (2024), Article 24.2.4, Section 6.

Formalized by `MetaMathlibExt.kBoxReturnGF`, a definition declared in [WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/k-box-paths-and-skew-dyck-paths/index.html#k-box-return-gf).

## Long-ascent generating function of $k$-box paths

Let $B_n^{(k)}$ be the set of $k$-box
paths of size $n$, and let $\mathrm{la}(\mu)$ be the number of long ascents of a path $\mu$. The
long-ascent generating function of $k$-box paths is the power series

$$
\acute F_k(t, x) = \sum_{n \ge 1} \sum_{\mu \in B_n^{(k)}} t^{\mathrm{la}(\mu)} x^n
$$

in $\mathbb{Z}[t][[x]]$.

## Sources

- Zhang and Zhuang, *A Subfamily of Skew Dyck Paths Related to `k`-ary Trees*, Journal of Integer Sequences 27 (2024), Article 24.2.4, Section 7.

Formalized by `MetaMathlibExt.kBoxLongAscentGF`, a definition declared in [WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/k-box-paths-and-skew-dyck-paths/index.html#k-box-long-ascent-gf).

## Long-ascent generating function of augmented $k$-Dyck paths

Let $k \ge 0$, let
$\hat D_n^{(k)}$ be the set of augmented $k$-Dyck paths of size $n$, and for a path $\mu$ let
$\operatorname{asc}(\mu)$ be its number of long ascents. Then $\acute{G}_k(t, x)$ is the formal
power series

$$
\acute{G}_k(t, x) = \sum_{n \ge 0} \sum_{\mu \in \hat D_n^{(k)}} t^{\operatorname{asc}(\mu)} x^n
$$

in $\mathbb{Z}[t][[x]]$. Its constant term is $1$, coming from the empty path.

## Sources

- Zhang and Zhuang, *A Subfamily of Skew Dyck Paths Related to `k`-ary Trees*, Journal of Integer Sequences 27 (2024), Article 24.2.4, Section 7.

Formalized by `MetaMathlibExt.augmentedKDyckLongAscentGF`, a definition declared in [WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/k-box-paths-and-skew-dyck-paths/index.html#augmented-kdyck-long-ascent-gf).

## Minimal semilength of skew Dyck paths with $n$ box factors

Let $k \ge 1$ and $n \ge 1$.
Some skew Dyck path with exactly $n$ occurrences of the factor $U D^k L$ has semilength
(number of $U$ steps) $(k+2)n - 1$, and every skew Dyck path with exactly $n$ occurrences of
$U D^k L$ has semilength at least $(k+2)n - 1$.

## Sources

- Zhang and Zhuang, *A Subfamily of Skew Dyck Paths Related to `k`-ary Trees*, Journal of Integer Sequences 27 (2024), Article 24.2.4, Proposition 1 (`jis-2024-24.2.4-prop-1`).

Stated but not proved: `MetaMathlibExt.min_semilength_boxFactor` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/k-box-paths-and-skew-dyck-paths/index.html#min-semilength-box-factor).

## Structure of $k$-box paths

Let $k \ge 1$ and $n \ge 1$. For a list
$a = (a_1, \dots, a_n)$ of natural numbers write
$w_k(a) = U^{a_1} D^k L D \cdots U^{a_{n-1}} D^k L D\, U^{a_n} D^k L$. Every $k$-box path of
size $n$ equals $w_k(a)$ for some list $a$ of $n$ positive integers. Conversely, if $a$ is a
list of $n$ positive integers with $a_1 + \cdots + a_n = (k+2)n - 1$ and no prefix of $w_k(a)$
has more $D$s and $L$s together than $U$s, then $w_k(a)$ is a $k$-box path of size $n$.

## Sources

- Zhang and Zhuang, *A Subfamily of Skew Dyck Paths Related to `k`-ary Trees*, Journal of Integer Sequences 27 (2024), Article 24.2.4, Lemma 2 (`jis-2024-24.2.4-lem-2`).

Stated but not proved: `MetaMathlibExt.kBoxPaths_structure` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/k-box-paths-and-skew-dyck-paths/index.html#k-box-paths-structure).

## Decomposition of $k$-box paths

Let $k \ge 1$. A word $w$ in the steps $U$, $D$, $L$ is a
$k$-box path of some size $n \ge 1$ if and only if $w = \mu_1 U \mu_2 U \cdots \mu_{k+1} U D^k L$
for some augmented $(k+1)$-Dyck paths $\mu_1, \ldots, \mu_{k+1}$, each of some size.

## Sources

- Zhang and Zhuang, *A Subfamily of Skew Dyck Paths Related to `k`-ary Trees*, Journal of Integer Sequences 27 (2024), Article 24.2.4, Lemma 4 (`jis-2024-24.2.4-lem-4`).

Stated but not proved: `MetaMathlibExt.kBoxPaths_decomposition` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/k-box-paths-and-skew-dyck-paths/index.html#k-box-paths-decomposition).

## Number of $k$-box paths of size $n$

Let $k \ge 1$ and $n \ge 1$, and let $f_{k,n}$ be
the number of $k$-box paths of size $n$. Then

$$
((k+2)n - 1) \, f_{k,n} = \binom{(k+2)n - 1}{n},
$$

and if moreover $n \ge 2$, then

$$
(n - 1) \, f_{k,n} = (k+1) \binom{(k+2)n - 2}{n - 2}.
$$

The source also identifies $f_{k,n}$ with the number of $(k+1)$-tuples of $(k+2)$-ary trees
with $n - 1$ nodes; that identification is not part of this statement.

## Sources

- Zhang and Zhuang, *A Subfamily of Skew Dyck Paths Related to `k`-ary Trees*, Journal of Integer Sequences 27 (2024), Article 24.2.4, Theorem 5 (`jis-2024-24.2.4-thm-5`).

Stated but not proved: `MetaMathlibExt.card_kBoxPaths` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean, line 287](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean#L287). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/k-box-paths-and-skew-dyck-paths/index.html#card-k-box-paths).

## Counting tailed $k$-box paths

Let $k \ge 1$ and $n \ge 1$, and let $T$ be the number of
$k$-box paths of size $n$ that end with $U^{k+1} D^k L$. Then
$((k+2)(n-1)+1) \cdot T = \binom{(k+2)(n-1)+1}{n-1}$, and if $n \ge 2$ then also
$(n-1) \cdot T = \binom{(k+2)(n-1)}{n-2}$.

## Sources

- Zhang and Zhuang, *A Subfamily of Skew Dyck Paths Related to `k`-ary Trees*, Journal of Integer Sequences 27 (2024), Article 24.2.4, Proposition 7 (`jis-2024-24.2.4-prop-7`).

Stated but not proved: `MetaMathlibExt.card_tailed_kBoxPaths` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean, line 299](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean#L299). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/k-box-paths-and-skew-dyck-paths/index.html#card-tailed-k-box-paths).

## Functional equation for the returns generating function

Let $k \ge 1$, let
$F_k(t, x) \in \mathbb{Z}[t][[x]]$ be the generating function of $k$-box paths of size at least
$1$ by number of returns (exponent of $t$) and size (exponent of $x$), and let $G_{k+1}(x)$ be
the generating function of augmented $(k+1)$-Dyck paths by size, viewed in $\mathbb{Z}[t][[x]]$.
Then

$$\bigl(1 - t x G_{k+1}^{k+1}\bigr) F_k = t x G_{k+1}^k.$$

## Sources

- Zhang and Zhuang, *A Subfamily of Skew Dyck Paths Related to `k`-ary Trees*, Journal of Integer Sequences 27 (2024), Article 24.2.4, Lemma 8 (`jis-2024-24.2.4-lem-8`).

Stated but not proved: `MetaMathlibExt.kBoxReturnGF_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean, line 314](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean#L314). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/k-box-paths-and-skew-dyck-paths/index.html#k-box-return-gf-eq).

## Number of $k$-box paths with $j$ returns

Let $k \ge 1$ and $1 \le j \le n$, and let
$r_{k,n,j}$ be the number of $k$-box paths of size $n$ with exactly $j$ returns. Then

$$
((k+2)n - j - 1) \, r_{k,n,j} = (j(k+1) - 1) \binom{(k+2)n - j - 1}{n - j},
$$

and if moreover $j < n$, then

$$
(n - j) \, r_{k,n,j} = (j(k+1) - 1) \binom{(k+2)n - j - 2}{n - j - 1}.
$$

## Sources

- Zhang and Zhuang, *A Subfamily of Skew Dyck Paths Related to `k`-ary Trees*, Journal of Integer Sequences 27 (2024), Article 24.2.4, Theorem 9 (`jis-2024-24.2.4-thm-9`).

Stated but not proved: `MetaMathlibExt.card_kBoxPaths_returns` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean, line 326](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean#L326). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/k-box-paths-and-skew-dyck-paths/index.html#card-k-box-paths-returns).

## Mean and variance of the number of returns of $k$-box paths

Let $k \ge 1$ and $n \ge 1$,
and let $R(\mu)$ be the number of returns (steps ending on the $x$-axis) of a path $\mu$. The
average of $R$ over the $k$-box paths of size $n$ is

$$\frac{(k+2)((k+2)n-1)}{(k+1)((k+1)n+1)},$$

and the average of $R^2$ over these paths minus the square of the average of $R$ is

$$\frac{(k+2)((k+2)n-1)((2k+1)(k+1)n-2)(n-1)}{(k+1)^2((k+1)n+1)^2((k+1)n+2)}.$$

## Sources

- Zhang and Zhuang, *A Subfamily of Skew Dyck Paths Related to `k`-ary Trees*, Journal of Integer Sequences 27 (2024), Article 24.2.4, Corollary 11 (`jis-2024-24.2.4-cor-11`).

Stated but not proved: `MetaMathlibExt.kBoxPaths_returns_mean_variance` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean, line 340](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean#L340). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/k-box-paths-and-skew-dyck-paths/index.html#k-box-paths-returns-mean-variance).

## Long-ascent functional equations for $k$-box paths

Let $\acute F_k(t, x)$ be the
long-ascent generating function of $k$-box paths and $\acute G_k(t, x)$ that of augmented
$k$-Dyck paths, including the empty path, both in $\mathbb{Z}[t][[x]]$. Then for every $k \ge 1$

$$
\acute F_k = x \, \acute G_{k+1}^{k} \, (\acute G_{k+1} - 1 + t),
$$

and for every $k \ge 2$

$$
\acute G_k = 1 + x \, \acute G_k^{k} \, (\acute G_k - 1 + t).
$$

The source's displayed sum for $\acute G_k$ omits the empty path; here $\acute G_k$ includes it
(constant term $1$), as both equations require.

## Sources

- Zhang and Zhuang, *A Subfamily of Skew Dyck Paths Related to `k`-ary Trees*, Journal of Integer Sequences 27 (2024), Article 24.2.4, Lemma 12 (`jis-2024-24.2.4-lem-12`).

Stated but not proved: `MetaMathlibExt.kBoxLongAscentGF_functional_equations` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean, line 356](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean#L356). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/k-box-paths-and-skew-dyck-paths/index.html#k-box-long-ascent-gf-functional-equation).

## Number of $k$-box paths with $j$ long ascents

Let $k \ge 1$, $n \ge 1$ and $j \ge 1$,
and let $a_{k,n,j}$ be the number of $k$-box paths of size $n$ with exactly $j$ long ascents.
Then

$$
j \, a_{k,n,j} = \binom{(k+1)n - 2}{j - 1} \binom{n - 1}{j - 1}.
$$

For $j > n$ both sides vanish.

## Sources

- Zhang and Zhuang, *A Subfamily of Skew Dyck Paths Related to `k`-ary Trees*, Journal of Integer Sequences 27 (2024), Article 24.2.4, Theorem 13 (`jis-2024-24.2.4-thm-13`).

Stated but not proved: `MetaMathlibExt.card_kBoxPaths_longAscents` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean, line 370](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean#L370). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/k-box-paths-and-skew-dyck-paths/index.html#card-k-box-paths-long-ascents).

## Second polygonal numbers count box paths with two long ascents

Let $K \ge 4$ and
$n \ge 1$. Then $n\bigl((K-2)n + (K-4)\bigr)$ is twice the number of $(K-3)$-box paths of size
$n + 1$ with exactly two long ascents (maximal runs of at least two $U$ steps). Equivalently,
the $n$th second $K$-gonal number $n\bigl((K-2)n + (K-4)\bigr)/2$, the $K$-gonal formula
$m\bigl((K-2)m - (K-4)\bigr)/2$ at $m = -n$, equals this number of paths.

The source states this for $K \ge 3$, where the case $K = 3$ uses its convention for $0$-box
paths.

## Sources

- Zhang and Zhuang, *A Subfamily of Skew Dyck Paths Related to `k`-ary Trees*, Journal of Integer Sequences 27 (2024), Article 24.2.4, Theorem 15 (`jis-2024-24.2.4-thm-15`).

Stated but not proved: `MetaMathlibExt.second_polygonal_eq_card_kBoxPaths_two_longAscents` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean, line 384](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean#L384). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/k-box-paths-and-skew-dyck-paths/index.html#second-polygonal-eq-card-k-box-paths-two).

## Long ascents of box paths: sum and sum of squares

Let $k \ge 1$ and $n \ge 1$, let
$B_n^{(k)}$ be the set of $k$-box paths of size $n$, and for a path $w$ let $\mathrm{la}(w)$ be
its number of long ascents. Then

$$\sum_{w \in B_n^{(k)}} \mathrm{la}(w) = \binom{(k+2)n-3}{n-1}$$

and

$$\bigl((k+2)n-3\bigr) \sum_{w \in B_n^{(k)}} \mathrm{la}(w)^2 =
\bigl((k+1)n^2-n-1\bigr) \binom{(k+2)n-3}{n-1}.$$

The source states the second identity divided by $(k+2)n-3$, that is, with the sum of
$\mathrm{la}(w)^2$ equal to $\frac{(k+1)n^2-n-1}{(k+2)n-3}\binom{(k+2)n-3}{n-1}$; at $k = n = 1$
the cleared form reads $0 = 0$.

## Sources

- Zhang and Zhuang, *A Subfamily of Skew Dyck Paths Related to `k`-ary Trees*, Journal of Integer Sequences 27 (2024), Article 24.2.4, Lemma 17 (`jis-2024-24.2.4-lem-17`).

Stated but not proved: `MetaMathlibExt.sum_kBoxPaths_longAscents` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean, line 397](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean#L397). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/k-box-paths-and-skew-dyck-paths/index.html#sum-k-box-paths-long-ascents).

## Mean and variance of long ascents in $k$-box paths

Let $k \ge 1$ and $n \ge 1$. Over the
$k$-box paths of size $n$, taken with equal weight, the mean number of long ascents is

$$
\frac{n((k+1)n-1)}{(k+2)n-2}
$$

and the variance (the mean of the square minus the square of the mean) is

$$
\frac{((k+1)n-1)((k+1)n-2)\,n(n-1)}{((k+2)n-2)^2\,((k+2)n-3)}.
$$

When $k = n = 1$ the variance is $0$, and the last fraction reads $0/0$, which is taken to be $0$.

## Sources

- Zhang and Zhuang, *A Subfamily of Skew Dyck Paths Related to `k`-ary Trees*, Journal of Integer Sequences 27 (2024), Article 24.2.4, Proposition 18 (`jis-2024-24.2.4-prop-18`).

Stated but not proved: `MetaMathlibExt.kBoxPaths_longAscents_mean_variance` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean, line 410](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/KBoxPathsWanted.lean#L410). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/k-box-paths-and-skew-dyck-paths/index.html#k-box-paths-long-ascents-mean-variance).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: k-box paths and skew Dyck paths](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/k-box-paths-and-skew-dyck-paths/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/k-box-paths-and-skew-dyck-paths)
