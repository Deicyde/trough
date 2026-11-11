---
declaration: section
origin: cited
lean: MetaMathlibExt.FastVanDerWaerdenGame.ContainsCopy, MetaMathlibExt.FastVanDerWaerdenGame.MakerWinsWithin, MetaMathlibExt.FastVanDerWaerdenGame.IsRatCopy, MetaMathlibExt.FastVanDerWaerdenGame.IsRatReflection, MetaMathlibExt.FastVanDerWaerdenGame.IsSymmetricOfType, MetaMathlibExt.FastVanDerWaerdenGame.IsSymmetric, MetaMathlibExt.FastVanDerWaerdenGame.zeroGeometricSet, MetaMathlibExt.FastVanDerWaerdenGame.containsCopy_empty
statement: formalized
---

# Fast van der Waerden game

22 results, 12 proved and 10 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/fast-van-der-waerden-game/index.html).

## Containing a homothetic copy

Let $S$ and $M$ be finite sets of natural numbers. $M$
contains a homothetic copy of $S$ if there are a natural number $a > 0$ and an integer $b$ such
that $as + b \in M$ for every $s \in S$, that is, $aS + b \subseteq M$. This is Maker's winning
condition.

## Sources

- Alpert, Barham, Freidin, Tan, and Weiner, *Fast Winning Strategies in a Generalized van der Waerden Game*, INTEGERS 26 (2026), Article A40, Section 1.

Formalized by `MetaMathlibExt.FastVanDerWaerdenGame.ContainsCopy`, a definition declared in [WantedExt/Combinatorics/FastVanDerWaerdenGameWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/FastVanDerWaerdenGameWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/fast-van-der-waerden-game/index.html#contains-copy).

## Maker wins within $p$ moves

Let $S$ be a finite set of natural numbers. In the
$S$-game, Maker and Breaker alternately claim unclaimed natural numbers, and Maker wins once the
numbers Maker has claimed contain a copy $aS + b = \{as + b : s \in S\}$ of $S$, where $a$ is a
positive integer and $b$ is an integer. Let $M$ and $B$ be finite sets of natural numbers
(claimed by Maker and by Breaker) and $p$ a natural number, with Maker to move. Maker wins
within $p$ moves if $M$ already contains such a copy of $S$, or if $p \ge 1$ and there is a
number $x \notin M \cup B$ such that for every number $y \ne x$ with $y \notin M \cup B$, Maker
wins within $p - 1$ moves from the position where Maker has claimed $M \cup \{x\}$ and Breaker
has claimed $B \cup \{y\}$.

## Sources

- Alpert, Barham, Freidin, Tan, and Weiner, *Fast Winning Strategies in a Generalized van der Waerden Game*, INTEGERS 26 (2026), Article A40, Sections 1 and 5 (`p`-move strategy).

Formalized by `MetaMathlibExt.FastVanDerWaerdenGame.MakerWinsWithin`, a definition declared in [WantedExt/Combinatorics/FastVanDerWaerdenGameWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/FastVanDerWaerdenGameWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/fast-van-der-waerden-game/index.html#maker-wins-within).

## Copies of finite sets of rationals

Let $A$ and $B$ be finite sets of rational numbers.
$B$ is a copy of $A$ if there are rationals $a > 0$ and $b$ such that
$B = aA + b = \{ax + b : x \in A\}$.

## Sources

- Alpert, Barham, Freidin, Tan, and Weiner, *Fast Winning Strategies in a Generalized van der Waerden Game*, INTEGERS 26 (2026), Article A40, Section 5.

Formalized by `MetaMathlibExt.FastVanDerWaerdenGame.IsRatCopy`, a definition declared in [WantedExt/Combinatorics/FastVanDerWaerdenGameWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/FastVanDerWaerdenGameWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/fast-van-der-waerden-game/index.html#is-rat-copy).

## Reflections of finite sets of rationals

Let $A$ and $B$ be finite sets of rational
numbers. $B$ is a reflection of $A$ if there are rationals $a < 0$ and $b$ such that
$B = aA + b = \{ax + b : x \in A\}$.

## Sources

- Alpert, Barham, Freidin, Tan, and Weiner, *Fast Winning Strategies in a Generalized van der Waerden Game*, INTEGERS 26 (2026), Article A40, Section 6.

Formalized by `MetaMathlibExt.FastVanDerWaerdenGame.IsRatReflection`, a definition declared in [WantedExt/Combinatorics/FastVanDerWaerdenGameWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/FastVanDerWaerdenGameWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/fast-van-der-waerden-game/index.html#is-rat-reflection).

## Symmetric sets of a given type

Let $S = \{s_0 < s_1 < \dots < s_{n-1}\}$ be a finite
set of $n$ rational numbers and let $i, j < n$. Then $S$ is called symmetric of type $(i, j)$ if
$i < j$ and $S \setminus \{s_i\}$ is a copy of $S \setminus \{s_j\}$.

Positions are counted from $0$, so the paper's type $(i + 1, j + 1)$ is the type $(i, j)$ here.

## Sources

- Alpert, Barham, Freidin, Tan, and Weiner, *Fast Winning Strategies in a Generalized van der Waerden Game*, INTEGERS 26 (2026), Article A40, Definition 2.

Formalized by `MetaMathlibExt.FastVanDerWaerdenGame.IsSymmetricOfType`, a definition declared in [WantedExt/Combinatorics/FastVanDerWaerdenGameWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/FastVanDerWaerdenGameWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/fast-van-der-waerden-game/index.html#is-symmetric-of-type).

## Symmetric sets of rationals

A finite set $S$ of rational numbers is symmetric if it is
symmetric of some type $(i, j)$ with $i, j < |S|$.

## Sources

- Alpert, Barham, Freidin, Tan, and Weiner, *Fast Winning Strategies in a Generalized van der Waerden Game*, INTEGERS 26 (2026), Article A40, Definition 2.

Formalized by `MetaMathlibExt.FastVanDerWaerdenGame.IsSymmetric`, a definition declared in [WantedExt/Combinatorics/FastVanDerWaerdenGameWanted.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/FastVanDerWaerdenGameWanted.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/fast-van-der-waerden-game/index.html#is-symmetric).

## The zero-geometric set $S_2(n, k)$

For a natural number $n$ and a rational number $k$,
$S_2(n, k)$ is the finite set of rationals $\{0\} \cup \{k^i : 0 \le i < n - 1\}$, that is,
$\{0, 1, k, \dots, k^{n-2}\}$ when $n \ge 2$ and $\{0\}$ when $n \le 1$.

## Sources

- Alpert, Barham, Freidin, Tan, and Weiner, *Fast Winning Strategies in a Generalized van der Waerden Game*, INTEGERS 26 (2026), Article A40, Definition 3.

Formalized by `MetaMathlibExt.FastVanDerWaerdenGame.zeroGeometricSet`, a definition declared in [WantedExt/Combinatorics/FastVanDerWaerdenGameWanted.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/FastVanDerWaerdenGameWanted.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/fast-van-der-waerden-game/index.html#zero-geometric-set).

## Every finite set contains a copy of the empty set

Every finite set $M$ of natural
numbers contains a homothetic copy of the empty set.

## Sources

- Alpert, Barham, Freidin, Tan, and Weiner, *Fast Winning Strategies in a Generalized van der Waerden Game*, INTEGERS 26 (2026), Article A40, Section 1.

Formalized by `MetaMathlibExt.FastVanDerWaerdenGame.containsCopy_empty`, a theorem declared in [WantedExt/Combinatorics/FastVanDerWaerdenGameWanted.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/FastVanDerWaerdenGameWanted.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/fast-van-der-waerden-game/index.html#contains-copy-empty).

## Winning within zero moves

Let $S$ be a finite set of natural numbers, and let $M$ and
$B$ be finite sets of natural numbers. Maker wins the $S$-game within $0$ moves from the position
where Maker has claimed $M$ and Breaker has claimed $B$ if and only if $M$ contains a copy
$aS + b = \{as + b : s \in S\}$ of $S$, where $a$ is a positive integer and $b$ is an integer.

## Sources

- Alpert, Barham, Freidin, Tan, and Weiner, *Fast Winning Strategies in a Generalized van der Waerden Game*, INTEGERS 26 (2026), Article A40, Section 5.

Formalized by `MetaMathlibExt.FastVanDerWaerdenGame.makerWinsWithin_zero`, a theorem declared in [WantedExt/Combinatorics/FastVanDerWaerdenGameWanted.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/FastVanDerWaerdenGameWanted.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/fast-van-der-waerden-game/index.html#maker-wins-within-zero).

## Every finite set of rationals is a copy of itself

For every finite set $A$ of rational
numbers, $A$ is a copy of $A$.

## Sources

- Alpert, Barham, Freidin, Tan, and Weiner, *Fast Winning Strategies in a Generalized van der Waerden Game*, INTEGERS 26 (2026), Article A40, Section 5.

Formalized by `MetaMathlibExt.FastVanDerWaerdenGame.isRatCopy_refl`, a theorem declared in [WantedExt/Combinatorics/FastVanDerWaerdenGameWanted.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/FastVanDerWaerdenGameWanted.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/fast-van-der-waerden-game/index.html#is-rat-copy-refl).

## The zero-geometric set $S_2(1, k)$ is $\{0\}$

For every rational number $k$, the
zero-geometric set $S_2(1, k)$ equals $\{0\}$.

## Sources

- Alpert, Barham, Freidin, Tan, and Weiner, *Fast Winning Strategies in a Generalized van der Waerden Game*, INTEGERS 26 (2026), Article A40, Definition 3.

Formalized by `MetaMathlibExt.FastVanDerWaerdenGame.zeroGeometricSet_one`, a theorem declared in [WantedExt/Combinatorics/FastVanDerWaerdenGameWanted.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/FastVanDerWaerdenGameWanted.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/fast-van-der-waerden-game/index.html#zero-geometric-set-one).

## The zero-geometric set $S_2(n + 2, k)$

For every natural number $n$ and every rational
$k$, $S_2(n + 2, k) = \{0\} \cup \{k^i : 0 \le i \le n\} = \{0, 1, k, \dots, k^n\}$.

## Sources

- Alpert, Barham, Freidin, Tan, and Weiner, *Fast Winning Strategies in a Generalized van der Waerden Game*, INTEGERS 26 (2026), Article A40, Definition 3.

Formalized by `MetaMathlibExt.FastVanDerWaerdenGame.zeroGeometricSet_add_two`, a theorem declared in [WantedExt/Combinatorics/FastVanDerWaerdenGameWanted.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/FastVanDerWaerdenGameWanted.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/fast-van-der-waerden-game/index.html#zero-geometric-set-add-two).

## Maker wins the $S$-game in $|S|$ moves when $|S| \le 3$

If $S$ is a finite set of
natural numbers with $|S| \le 3$, then, starting from the position where no number has been
claimed, Maker wins the $S$-game within $|S|$ moves.

## Sources

- Alpert, Barham, Freidin, Tan, and Weiner, *Fast Winning Strategies in a Generalized van der Waerden Game*, INTEGERS 26 (2026), Article A40, Corollary 1.

Stated but not proved: `MetaMathlibExt.FastVanDerWaerdenGame.makerWinsWithin_card_of_card_le_three` is written with `theorem_wanted` in [WantedExt/Combinatorics/FastVanDerWaerdenGameWanted.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/FastVanDerWaerdenGameWanted.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/fast-van-der-waerden-game/index.html#maker-wins-within-card-of-card-le-three).

## A fast Maker win forces symmetry

Let $S$ be a finite set of natural numbers with at
least two elements. If Maker, moving first with no numbers claimed, can force a win in the
game on $S$ within $|S|$ selections, then $S$, viewed as a set of rational numbers, is
symmetric.

## Sources

- Alpert, Barham, Freidin, Tan, and Weiner, *Fast Winning Strategies in a Generalized van der Waerden Game*, INTEGERS 26 (2026), Article A40, Lemma 1.

Stated but not proved: `MetaMathlibExt.FastVanDerWaerdenGame.isSymmetric_of_makerWinsWithin_card` is written with `theorem_wanted` in [WantedExt/Combinatorics/FastVanDerWaerdenGameWanted.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/FastVanDerWaerdenGameWanted.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/fast-van-der-waerden-game/index.html#is-symmetric-of-maker-wins-within-card).

## Possible types of a symmetric set

Let $S$ be a finite set of rational numbers with
$n \ge 4$ elements. If $S$ is symmetric of type $(i, j)$, with positions counted from $0$, then
$(i, j)$ is $(0, n - 1)$, $(1, n - 1)$ or $(0, n - 2)$. In the paper's one-based numbering these
are the types $(1, n)$, $(2, n)$ and $(1, n - 1)$.

## Sources

- Alpert, Barham, Freidin, Tan, and Weiner, *Fast Winning Strategies in a Generalized van der Waerden Game*, INTEGERS 26 (2026), Article A40, Lemma 2.

Stated but not proved: `MetaMathlibExt.FastVanDerWaerdenGame.isSymmetricOfType_cases` is written with `theorem_wanted` in [WantedExt/Combinatorics/FastVanDerWaerdenGameWanted.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/FastVanDerWaerdenGameWanted.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/fast-van-der-waerden-game/index.html#is-symmetric-of-type-cases).

## Zero-geometric copies of symmetric sets

Let $S = \{s_0 < s_1 < \dots < s_{n-1}\}$ be a
finite set of $n$ rational numbers, and let $i, j < n$ be such that $S$ is symmetric of type
$(i, j)$, with positions counted from $0$. If $i = 1$ and $j = n - 1$, then there is a rational
number $k > 1$ such that the zero-geometric set $S_2(n, k)$ is a copy of $S$. If $i = 0$ and
$j = n - 2$, then there is a rational number $k > 1$ such that $S_2(n, k)$ is a reflection of $S$.

In the paper's one-based numbering these are the types $(2, n)$ and $(1, n - 1)$.

## Sources

- Alpert, Barham, Freidin, Tan, and Weiner, *Fast Winning Strategies in a Generalized van der Waerden Game*, INTEGERS 26 (2026), Article A40, Lemma 4.

Stated but not proved: `MetaMathlibExt.FastVanDerWaerdenGame.zeroGeometricSet_of_isSymmetricOfType` is written with `theorem_wanted` in [WantedExt/Combinatorics/FastVanDerWaerdenGameWanted.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/FastVanDerWaerdenGameWanted.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/fast-van-der-waerden-game/index.html#zero-geometric-set-of-is-symmetric-of-ty).

## Uniqueness of the symmetry type

A finite set $S$ of rational numbers with at least
four elements is symmetric of at most one type: if $S$ is symmetric of types $(i, j)$ and
$(i', j')$, then $i = i'$ and $j = j'$.

## Sources

- Alpert, Barham, Freidin, Tan, and Weiner, *Fast Winning Strategies in a Generalized van der Waerden Game*, INTEGERS 26 (2026), Article A40, Lemma 5.

Stated but not proved: `MetaMathlibExt.FastVanDerWaerdenGame.isSymmetricOfType_unique` is written with `theorem_wanted` in [WantedExt/Combinatorics/FastVanDerWaerdenGameWanted.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/FastVanDerWaerdenGameWanted.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/fast-van-der-waerden-game/index.html#is-symmetric-of-type-unique).

## Hales–Jewett bound for the $S$-game

Let $S$ be a finite set of natural numbers with
$|S| = n$, and let $N$ be a natural number such that every 2-coloring of $S^N$ has a
monochromatic combinatorial line. Then, starting from the position where no number has been
claimed, Maker wins the $S$-game within $\lceil n^N / 2 \rceil$ moves.

## Sources

- Alpert, Barham, Freidin, Tan, and Weiner, *Fast Winning Strategies in a Generalized van der Waerden Game*, INTEGERS 26 (2026), Article A40, Theorem 4.

Stated but not proved: `MetaMathlibExt.FastVanDerWaerdenGame.makerWinsWithin_of_halesJewett` is written with `theorem_wanted` in [WantedExt/Combinatorics/FastVanDerWaerdenGameWanted.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/FastVanDerWaerdenGameWanted.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/fast-van-der-waerden-game/index.html#maker-wins-within-of-hales-jewett).

## Maker cannot win the $S$-game in $|S|$ moves when $|S| \ge 5$

If $S$ is a finite
set of natural numbers with $|S| \ge 5$, then, starting from the position where no number has
been claimed, Maker does not win the $S$-game within $|S|$ moves.

## Sources

- Alpert, Barham, Freidin, Tan, and Weiner, *Fast Winning Strategies in a Generalized van der Waerden Game*, INTEGERS 26 (2026), Article A40, Theorem 5.

Stated but not proved: `MetaMathlibExt.FastVanDerWaerdenGame.not_makerWinsWithin_card_of_five_le` is written with `theorem_wanted` in [WantedExt/Combinatorics/FastVanDerWaerdenGameWanted.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/FastVanDerWaerdenGameWanted.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/fast-van-der-waerden-game/index.html#not-maker-wins-within-card-of-five-le).

## Four-element sets with a four-move win are the symmetric ones

If $S$ is a set of four
natural numbers, then, starting from the position where no number has been claimed, Maker wins
the $S$-game within $4$ moves if and only if $S$, viewed as a set of rationals, is symmetric.

## Sources

- Alpert, Barham, Freidin, Tan, and Weiner, *Fast Winning Strategies in a Generalized van der Waerden Game*, INTEGERS 26 (2026), Article A40, Theorem 6.

Stated but not proved: `MetaMathlibExt.FastVanDerWaerdenGame.makerWinsWithin_four_iff_isSymmetric` is written with `theorem_wanted` in [WantedExt/Combinatorics/FastVanDerWaerdenGameWanted.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/FastVanDerWaerdenGameWanted.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/fast-van-der-waerden-game/index.html#maker-wins-within-four-iff-is-symmetric).

## Maker wins the $S$-game in five moves when $|S| = 4$

If $S$ is a set of four natural
numbers, then, starting from the position where no number has been claimed, Maker wins the
$S$-game within $5$ moves.

## Sources

- Alpert, Barham, Freidin, Tan, and Weiner, *Fast Winning Strategies in a Generalized van der Waerden Game*, INTEGERS 26 (2026), Article A40, Theorem 7.

Stated but not proved: `MetaMathlibExt.FastVanDerWaerdenGame.makerWinsWithin_five_of_card_eq_four` is written with `theorem_wanted` in [WantedExt/Combinatorics/FastVanDerWaerdenGameWanted.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/FastVanDerWaerdenGameWanted.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/fast-van-der-waerden-game/index.html#maker-wins-within-five-of-card-eq-four).

## Tree criterion for fast wins

Let $S$ be a finite set of natural numbers and $p$ a
natural number. Let $T$ be a finite rooted tree with root $r$ whose vertices are pairwise
distinct rationals, such that every path from $r$ down to a vertex has at most $p$ vertices and
some such path has exactly $p$ vertices (so $T$ has height $p - 1$). Suppose that for every leaf
$v$ the set of vertices on the path from $r$ to $v$ contains a copy $aS + b$ of $S$ with
rationals $a > 0$ and $b$, and that every vertex other than the root that is not a leaf has at
least two children. Then, starting from the position where no number has been claimed, Maker
wins the $S$-game within $p$ moves.

The tree is given by the finite set of its root-to-vertex paths, each recorded as the list of
rationals along it.

## Sources

- Alpert, Barham, Freidin, Tan, and Weiner, *Fast Winning Strategies in a Generalized van der Waerden Game*, INTEGERS 26 (2026), Article A40, Proposition 1.

Stated but not proved: `MetaMathlibExt.FastVanDerWaerdenGame.makerWinsWithin_of_tree` is written with `theorem_wanted` in [WantedExt/Combinatorics/FastVanDerWaerdenGameWanted.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/FastVanDerWaerdenGameWanted.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/fast-van-der-waerden-game/index.html#maker-wins-within-of-tree).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fast van der Waerden game](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/fast-van-der-waerden-game/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GameTheory/combinatorial-games/fast-van-der-waerden-game)
