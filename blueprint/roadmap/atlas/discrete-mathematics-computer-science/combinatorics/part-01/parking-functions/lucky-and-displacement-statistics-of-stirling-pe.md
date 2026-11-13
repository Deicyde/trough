---
declaration: section
origin: cited
lean: MetaMathlibExt.stirlingPref, MetaMathlibExt.stirlingParkSpot, MetaMathlibExt.stirlingLuckySet, MetaMathlibExt.stirlingDisplacement, MetaMathlibExt.stirlingTotalDisplacement, MetaMathlibExt.IsAdmissibleLuckySet, MetaMathlibExt.stirlingLuckySet_small, MetaMathlibExt.stirlingDisplacement_small
statement: formalized
---

# Lucky and displacement statistics of Stirling permutations

32 results, 8 proved and 24 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-and-displacement-statistics-of-stirling-pe/index.html).

## Zero-based preferences of a word

Let $w = w_1 \cdots w_{2n}$ be a word of natural
numbers, read as the preferences of $2n$ cars for spots numbered $0, \dots, 2n - 1$. Car
$i \in \{1, \dots, 2n\}$ prefers the spot $(w_i - 1) \bmod 2n$, where $w_i - 1$ is truncated at
$0$. When every $w_i$ lies in $\{1, \dots, 2n\}$, for example when $w$ is a Stirling permutation
of order $n$, this is the spot $w_i - 1$, which is spot $w_i$ in the one-based numbering.

## Sources

- L. Colmenarejo et al., *On the Lucky and Displacement Statistics of Stirling Permutations*, Journal of Integer Sequences 27 (2024), Article 24.6.7, Section 1 (Stirling permutations read as parking functions of length `2n`).

Formalized by `MetaMathlibExt.stirlingPref`, a definition declared in [WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-and-displacement-statistics-of-stirling-pe/index.html#stirling-pref).

## Parking spot of a car

Let $w = w_1 \cdots w_{2n}$ be a word of natural numbers. Car $i$
prefers spot $q_i = ((w_i - 1) \bmod 2n) + 1$, where $w_i - 1$ is truncated at $0$; when every
$w_i$ lies in $\{1, \dots, 2n\}$, this is $q_i = w_i$. Cars $1, \dots, 2n$ arrive in order, and
car $i$ parks in the least spot $p(i) \in \{q_i, \dots, 2n\}$ not taken by an earlier car, or in
$p(i) = q_i$ if there is no such spot. The parking spot of car $i \in \{1, \dots, 2n\}$ is $p(i)$.

## Sources

- L. Colmenarejo et al., *On the Lucky and Displacement Statistics of Stirling Permutations*, Journal of Integer Sequences 27 (2024), Article 24.6.7, Definition 5.1.

Formalized by `MetaMathlibExt.stirlingParkSpot`, a definition declared in [WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-and-displacement-statistics-of-stirling-pe/index.html#stirling-park-spot).

## The lucky set of a word

Let $w = w_1 \cdots w_{2n}$ be a word of natural numbers. Car
$i$ prefers spot $q_i = ((w_i - 1) \bmod 2n) + 1$, where $w_i - 1$ is truncated at $0$; when
every $w_i$ lies in $\{1, \dots, 2n\}$, this is $q_i = w_i$. Cars $1, \dots, 2n$ arrive in
order, and car $i$ parks in the least spot $p(i) \in \{q_i, \dots, 2n\}$ not taken by an
earlier car, or in $p(i) = q_i$ if there is no such spot. The lucky set $\mathrm{Lucky}(w)$
is the set of cars $i \in \{1, \dots, 2n\}$ with $p(i) = w_i$; when every $w_i$ lies in
$\{1, \dots, 2n\}$, these are the cars that park in their preferred spot.

## Sources

- L. Colmenarejo et al., *On the Lucky and Displacement Statistics of Stirling Permutations*, Journal of Integer Sequences 27 (2024), Article 24.6.7, Definition 1.2.

Formalized by `MetaMathlibExt.stirlingLuckySet`, a definition declared in [WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-and-displacement-statistics-of-stirling-pe/index.html#stirling-lucky-set).

## Displacement of a car

Let $w = w_1 \cdots w_{2n}$ be a word of natural numbers. Car
$i$ prefers spot $q_i = ((w_i - 1) \bmod 2n) + 1$, where $w_i - 1$ is truncated at $0$; when
every $w_i$ lies in $\{1, \dots, 2n\}$, this is $q_i = w_i$. Cars $1, \dots, 2n$ arrive in
order, and car $i$ parks in the least spot $p(i) \in \{q_i, \dots, 2n\}$ not taken by an
earlier car, or in $p(i) = q_i$ if there is no such spot. The displacement of car $i$ is
$d(i) = p(i) - w_i$, where the subtraction is truncated at $0$.

## Sources

- L. Colmenarejo et al., *On the Lucky and Displacement Statistics of Stirling Permutations*, Journal of Integer Sequences 27 (2024), Article 24.6.7, Definition 5.1; the tuple `i ↦ d(i + 1)` is the displacement composition `dis(w)` (Definition 5.4).

Formalized by `MetaMathlibExt.stirlingDisplacement`, a definition declared in [WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-and-displacement-statistics-of-stirling-pe/index.html#stirling-displacement).

## Total displacement of a word

Let $w = w_1 \cdots w_{2n}$ be a word of natural numbers,
and for $i \in \{1, \dots, 2n\}$ let $d(i)$ be the displacement of car $i$ in $w$. The total
displacement of $w$ is $d(w) = \sum_{i=1}^{2n} d(i)$.

## Sources

- L. Colmenarejo et al., *On the Lucky and Displacement Statistics of Stirling Permutations*, Journal of Integer Sequences 27 (2024), Article 24.6.7, Definition 5.1.

Formalized by `MetaMathlibExt.stirlingTotalDisplacement`, a definition declared in [WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-and-displacement-statistics-of-stirling-pe/index.html#stirling-total-displacement).

## Admissible lucky sets

Let $n$ be a natural number. A finite set $S$ of natural numbers
is an $n$-admissible lucky set if $S = \mathrm{Lucky}(w)$ for some Stirling permutation $w$ of
order $n$, where $\mathrm{Lucky}(w)$ is the set of lucky cars of $w$.

## Sources

- L. Colmenarejo et al., *On the Lucky and Displacement Statistics of Stirling Permutations*, Journal of Integer Sequences 27 (2024), Article 24.6.7, Definition 3.1.

Formalized by `MetaMathlibExt.IsAdmissibleLuckySet`, a definition declared in [WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-and-displacement-statistics-of-stirling-pe/index.html#is-admissible-lucky-set).

## Lucky sets of 1122 and 1221

Read as parking functions of length $4$, the Stirling
permutation $1122$ has car $1$ as its only lucky car, and $1221$ has exactly cars $1$ and $2$
lucky: $\mathrm{Lucky}(1122) = \{1\}$ and $\mathrm{Lucky}(1221) = \{1, 2\}$.

## Sources

- L. Colmenarejo et al., *On the Lucky and Displacement Statistics of Stirling Permutations*, Journal of Integer Sequences 27 (2024), Article 24.6.7, Definitions 1.2 and 3.1.

Formalized by `MetaMathlibExt.stirlingLuckySet_small`, a theorem declared in [WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-and-displacement-statistics-of-stirling-pe/index.html#stirling-lucky-set-small).

## Displacement compositions of 1122 and 11244233

The displacement composition of a word
$w = w_1 \cdots w_{2n}$ is $\mathrm{dis}(w) = (d(1), \dots, d(2n))$, where $d(i)$ is the
displacement of car $i$. For the Stirling permutations $1122$ of order $2$ and $11244233$ of
order $4$, $\mathrm{dis}(1122) = (0, 1, 1, 2)$ and
$\mathrm{dis}(11244233) = (0, 1, 1, 0, 1, 4, 4, 5)$ (the paper's Example 5.5).

## Sources

- L. Colmenarejo et al., *On the Lucky and Displacement Statistics of Stirling Permutations*, Journal of Integer Sequences 27 (2024), Article 24.6.7, Definition 5.4 and Example 5.5.

Formalized by `MetaMathlibExt.stirlingDisplacement_small`, a theorem declared in [WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-and-displacement-statistics-of-stirling-pe/index.html#stirling-displacement-small).

## Basic properties of lucky cars

Let $n \ge 1$ and let $w$ be a Stirling permutation of
order $n$, read as a parking function of length $2n$. Then (a) car $1$ is lucky; (b) the first
car $i$ with $w_i = 1$ is lucky; (c) the number of lucky cars of $w$ is at least $1$ and at
most $n$.

The hypothesis $n \ge 1$ is added: the only Stirling permutation of order $0$ is the empty
word, which has no cars.

## Sources

- L. Colmenarejo et al., *On the Lucky and Displacement Statistics of Stirling Permutations*, Journal of Integer Sequences 27 (2024), Article 24.6.7, Lemma 2.1 (`jis-2024-24.6.7-lem-5`).

Stated but not proved: `MetaMathlibExt.stirlingLuckySet_basic` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-and-displacement-statistics-of-stirling-pe/index.html#stirling-lucky-set-basic).

## Characterization of extremely unlucky Stirling permutations

Let $n \ge 1$ and let $w$
be a Stirling permutation of order $n$, read as a parking function of length $2n$. Then car $1$
is the only lucky car of $w$ if and only if for every $x \in \{2, \dots, n\}$ and every
position $i \le x$, we have $w_i < x$.

The hypothesis $n \ge 1$ is added: the empty word, the only Stirling permutation of order $0$,
has no lucky cars, while the right-hand side holds vacuously.

## Sources

- L. Colmenarejo et al., *On the Lucky and Displacement Statistics of Stirling Permutations*, Journal of Integer Sequences 27 (2024), Article 24.6.7, Corollary 2.5 (`jis-2024-24.6.7-cor-11`).

Stated but not proved: `MetaMathlibExt.stirlingLuckySet_eq_singleton_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-and-displacement-statistics-of-stirling-pe/index.html#stirling-lucky-set-eq-singleton-iff).

## Counting extremely unlucky Stirling permutations

For every integer $n \ge 1$, the number
of Stirling permutations $w$ of order $n$ that are extremely unlucky, that is, whose only lucky
car is car $1$ ($\mathrm{Lucky}(w) = \{1\}$), is $(n - 1)!$.

## Sources

- L. Colmenarejo et al., *On the Lucky and Displacement Statistics of Stirling Permutations*, Journal of Integer Sequences 27 (2024), Article 24.6.7, Theorem 2.7 (`jis-2024-24.6.7-thm-13`).

Stated but not proved: `MetaMathlibExt.card_extremely_unlucky_stirling` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-and-displacement-statistics-of-stirling-pe/index.html#card-extremely-unlucky-stirling).

## Characterization of extremely lucky Stirling permutations

Let $w$ be a Stirling
permutation of order $n$, read as a parking function of length $2n$. Then $w$ has exactly $n$
lucky cars if and only if the second occurrences of the letters of $w$ appear in decreasing
order: for all positions $a < b$ such that $w_a$ also occurs before position $a$ and $w_b$ also
occurs before position $b$, we have $w_b < w_a$.

## Sources

- L. Colmenarejo et al., *On the Lucky and Displacement Statistics of Stirling Permutations*, Journal of Integer Sequences 27 (2024), Article 24.6.7, Proposition 2.11 (`jis-2024-24.6.7-prop-17`).

Stated but not proved: `MetaMathlibExt.stirlingLuckySet_card_eq_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-and-displacement-statistics-of-stirling-pe/index.html#stirling-lucky-set-card-eq-iff).

## Extremely lucky Stirling permutations and Dyck words

For every natural number $n$, there
is a bijection between the Stirling permutations $w$ of order $n$ that are extremely lucky, that
is, whose set $\mathrm{Lucky}(w)$ of lucky cars has exactly $n$ elements, and the Dyck words of
semilength $n$ (valid parenthesizations of $n$ pairs of parentheses).

## Sources

- L. Colmenarejo et al., *On the Lucky and Displacement Statistics of Stirling Permutations*, Journal of Integer Sequences 27 (2024), Article 24.6.7, Theorem 2.12 (`jis-2024-24.6.7-thm-18`).

Stated but not proved: `MetaMathlibExt.extremely_lucky_stirling_equiv_dyckWord` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-and-displacement-statistics-of-stirling-pe/index.html#extremely-lucky-stirling-equiv-dyck-word).

## Extremely lucky Stirling permutations are counted by the Catalan numbers

For every
positive integer $n$, the number of Stirling permutations $w$ of order $n$ that are extremely
lucky, that is, whose set $\mathrm{Lucky}(w)$ of lucky cars has exactly $n$ elements, is the
Catalan number $C_n$.

## Sources

- L. Colmenarejo et al., *On the Lucky and Displacement Statistics of Stirling Permutations*, Journal of Integer Sequences 27 (2024), Article 24.6.7, Corollary 2.14 (`jis-2024-24.6.7-cor-20`).

Stated but not proved: `MetaMathlibExt.card_extremely_lucky_stirling` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-and-displacement-statistics-of-stirling-pe/index.html#card-extremely-lucky-stirling).

## Extending admissible lucky sets

Let $n \ge 1$. If $S$ is an $n$-admissible lucky set,
then both $S$ and $S \cup \{2n + 1\}$ are $(n + 1)$-admissible lucky sets.

The hypothesis $n \ge 1$ is added: the empty set is $0$-admissible but not $1$-admissible.

## Sources

- L. Colmenarejo et al., *On the Lucky and Displacement Statistics of Stirling Permutations*, Journal of Integer Sequences 27 (2024), Article 24.6.7, Theorem 3.3 (`jis-2024-24.6.7-thm-23`).

Stated but not proved: `MetaMathlibExt.IsAdmissibleLuckySet.succ` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-and-displacement-statistics-of-stirling-pe/index.html#succ).

## Necessary conditions for admissible lucky sets

Let $n \ge 1$. If $S$ is an
$n$-admissible lucky set, then $1 \in S$ and $2n \notin S$.

## Sources

- L. Colmenarejo et al., *On the Lucky and Displacement Statistics of Stirling Permutations*, Journal of Integer Sequences 27 (2024), Article 24.6.7, Corollary 3.4 (`jis-2024-24.6.7-cor-24`).

Stated but not proved: `MetaMathlibExt.IsAdmissibleLuckySet.one_mem_and_two_mul_not_mem` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-and-displacement-statistics-of-stirling-pe/index.html#one-mem-and-two-mul-not-mem).

## Parking before the second lucky car

Let $w = w_1 \cdots w_{2n}$ be a Stirling permutation
of order $n$, read as a parking function of length $2n$, and let $x$ be a lucky car of $w$ such
that exactly one lucky car of $w$ is smaller than $x$, so that $x$ is the second-smallest element
of the lucky set $\mathrm{Lucky}(w)$. Then every car $c$ with $2 \le c \le x - 1$ parks in spot
$w_1 + c - 1$.

## Sources

- L. Colmenarejo et al., *On the Lucky and Displacement Statistics of Stirling Permutations*, Journal of Integer Sequences 27 (2024), Article 24.6.7, Lemma 3.5 (`jis-2024-24.6.7-lem-25`).

Stated but not proved: `MetaMathlibExt.stirlingParkSpot_before_second_lucky` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-and-displacement-statistics-of-stirling-pe/index.html#stirling-park-spot-before-second-lucky).

## Left-to-right minima of a Stirling permutation sit at odd positions

Let
$w = w_1 \cdots w_{2n}$ be a Stirling permutation of order $n$ and let $j \in \{1, \dots, 2n\}$.
If $w_j < w_i$ for every $i < j$, then $j$ is odd.

In the paper, $j$ is the first car preferring spot $w_j$; the hypothesis $w_j < w_i$ for all
$i < j$ already implies this, and $w_j \in \{1, \dots, n\}$ holds for every Stirling permutation.

## Sources

- L. Colmenarejo et al., *On the Lucky and Displacement Statistics of Stirling Permutations*, Journal of Integer Sequences 27 (2024), Article 24.6.7, Lemma 3.7 (`jis-2024-24.6.7-lem-27`).

Stated but not proved: `MetaMathlibExt.stirling_odd_of_lt_all_before` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-and-displacement-statistics-of-stirling-pe/index.html#stirling-odd-of-lt-all-before).

## A second lucky car beyond $n$ is odd

Let $w = w_1 \cdots w_{2n}$ be a Stirling
permutation of order $n$, read as a parking function of length $2n$, and let $x$ be a lucky car
of $w$ such that exactly one lucky car of $w$ is smaller than $x$, so that $x$ is the
second-smallest element of the lucky set $\mathrm{Lucky}(w)$. If $x > n$, then $x$ is odd.

## Sources

- L. Colmenarejo et al., *On the Lucky and Displacement Statistics of Stirling Permutations*, Journal of Integer Sequences 27 (2024), Article 24.6.7, Proposition 3.8 (`jis-2024-24.6.7-prop-28`).

Stated but not proved: `MetaMathlibExt.stirling_second_lucky_odd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-and-displacement-statistics-of-stirling-pe/index.html#stirling-second-lucky-odd).

## Preference of the second lucky car

Let $w = w_1 \cdots w_{2n}$ be a Stirling permutation
of order $n$, read as a parking function of length $2n$, and let $x$ be a lucky car of $w$ such
that exactly one lucky car of $w$ is smaller than $x$, so that $x$ is the second-smallest element
of the lucky set $\mathrm{Lucky}(w)$. If $w_1 = 1$, then $x \le w_x \le n$.

## Sources

- L. Colmenarejo et al., *On the Lucky and Displacement Statistics of Stirling Permutations*, Journal of Integer Sequences 27 (2024), Article 24.6.7, Lemma 3.9 (`jis-2024-24.6.7-lem-29`).

Stated but not proved: `MetaMathlibExt.stirling_second_lucky_pref` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-and-displacement-statistics-of-stirling-pe/index.html#stirling-second-lucky-pref).

## The first preference bounds the lucky cars

Let $w$ be a Stirling permutation of
order $n$, read as a parking function of length $2n$, with at least $3$ lucky cars, and let $x$
be the second-smallest lucky car of $w$. If $x \ge n$, then the number of lucky cars of $w$ is
at most $w_1$, and every lucky car parks in one of the spots $1, \dots, w_1$.

## Sources

- L. Colmenarejo et al., *On the Lucky and Displacement Statistics of Stirling Permutations*, Journal of Integer Sequences 27 (2024), Article 24.6.7, Lemma 3.10 (`jis-2024-24.6.7-lem-30`).

Stated but not proved: `MetaMathlibExt.stirling_first_pref_ge_lucky` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-and-displacement-statistics-of-stirling-pe/index.html#stirling-first-pref-ge-lucky).

## When the penultimate car is lucky

Let $n \ge 1$ and let $w = w_1 \cdots w_{2n}$ be a
Stirling permutation of order $n$, read as a parking function of length $2n$. Then car $2n - 1$
is lucky, that is, belongs to the lucky set $\mathrm{Lucky}(w)$, if and only if $w_{2n-1} = 1$.

## Sources

- L. Colmenarejo et al., *On the Lucky and Displacement Statistics of Stirling Permutations*, Journal of Integer Sequences 27 (2024), Article 24.6.7, Theorem 3.11 (`jis-2024-24.6.7-thm-31`).

Stated but not proved: `MetaMathlibExt.stirling_penultimate_lucky_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-and-displacement-statistics-of-stirling-pe/index.html#stirling-penultimate-lucky-iff).

## Admissible lucky sets with two elements

Let $n$, $h$ and $i$ be natural numbers with
$h < i \le 2n$. The set $\{h, i\}$ is an $n$-admissible lucky set if and only if $h = 1$ and
either $i > n$ and $i$ is odd, or $i \le n$.

The bound $i \le 2n$ is the paper's standing assumption that lucky sets lie in
$\{1, \dots, 2n\}$; without it $\{1, 2n + 1\}$ would satisfy the right-hand side.

## Sources

- L. Colmenarejo et al., *On the Lucky and Displacement Statistics of Stirling Permutations*, Journal of Integer Sequences 27 (2024), Article 24.6.7, Theorem 4.1 (`jis-2024-24.6.7-thm-32`).

Stated but not proved: `MetaMathlibExt.isAdmissibleLuckySet_pair_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean, line 285](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean#L285). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-and-displacement-statistics-of-stirling-pe/index.html#is-admissible-lucky-set-pair-iff).

## Counting admissible lucky sets with two elements

For every integer $n \ge 1$, the number
of $n$-admissible lucky sets with exactly two elements is $n - 1 + \lceil (n - 1)/2 \rceil$.

## Sources

- L. Colmenarejo et al., *On the Lucky and Displacement Statistics of Stirling Permutations*, Journal of Integer Sequences 27 (2024), Article 24.6.7, Corollary 4.2 (`jis-2024-24.6.7-cor-33`).

Stated but not proved: `MetaMathlibExt.ncard_admissibleLuckySet_card_two` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean, line 294](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean#L294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-and-displacement-statistics-of-stirling-pe/index.html#ncard-admissible-lucky-set-card-two).

## Stirling permutations whose second lucky car is $n$

Let $w = w_1 \cdots w_{2n}$ be a
Stirling permutation of order $n$, read as a parking function of length $2n$, such that car $n$
is lucky and exactly one lucky car of $w$ is smaller than $n$, so that $n$ is the second-smallest
element of the lucky set $\mathrm{Lucky}(w)$. (a) If $n$ is even, then $w_1 = 1$, $w_n = n$ and
$\mathrm{Lucky}(w)$ has exactly $2$ elements. (b) If $n$ is odd and $w_1 = 1$, then $w_n = n$ and
$\mathrm{Lucky}(w)$ has exactly $2$ elements.

The paper states this for an admissible lucky set $S$ and a Stirling permutation $w$ with
$\mathrm{Lucky}(w) = S$; here it holds for every such $w$.

## Sources

- L. Colmenarejo et al., *On the Lucky and Displacement Statistics of Stirling Permutations*, Journal of Integer Sequences 27 (2024), Article 24.6.7, Lemma 4.3 (`jis-2024-24.6.7-lem-34`).

Stated but not proved: `MetaMathlibExt.stirling_second_lucky_eq_n` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean, line 306](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean#L306). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-and-displacement-statistics-of-stirling-pe/index.html#stirling-second-lucky-eq-n).

## When $\{1, n - 1, 2n - 2\}$ is an admissible lucky set

For every integer $n \ge 4$, the
set $\{1, n - 1, 2n - 2\}$ is an $n$-admissible lucky set if and only if $n$ is even.

As printed the claim covers all $n$, but it fails at $n = 3$: $w = 133221$ is a Stirling
permutation of order $3$ with $\mathrm{Lucky}(w) = \{1, 2, 4\} = \{1, n - 1, 2n - 2\}$ (its cars
park in spots $1, 3, 4, 2, 5, 6$). The paper's proof assumes $n > 3$.

## Sources

- L. Colmenarejo et al., *On the Lucky and Displacement Statistics of Stirling Permutations*, Journal of Integer Sequences 27 (2024), Article 24.6.7, Proposition 4.4 (`jis-2024-24.6.7-prop-35`).

Stated but not proved: `MetaMathlibExt.isAdmissibleLuckySet_one_pred_two_mul_sub_two_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean, line 321](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean#L321). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-and-displacement-statistics-of-stirling-pe/index.html#is-admissible-lucky-set-one-pred-two-mul).

## Total displacement of a Stirling permutation is invariant under rearrangement

Let
$w = w_1 \cdots w_{2n}$ be a Stirling permutation of order $n$ and let $\sigma$ be a permutation
of $\{1, \dots, 2n\}$. Read words of length $2n$ as parking functions, and let $d(v)$ denote the
total displacement of a word $v$, the sum of the displacements of its cars. Then the rearranged
word $w \circ \sigma = w_{\sigma(1)} \cdots w_{\sigma(2n)}$ satisfies $d(w \circ \sigma) = d(w)$.

The rearranged word $w \circ \sigma$ need not be a Stirling permutation.

## Sources

- L. Colmenarejo et al., *On the Lucky and Displacement Statistics of Stirling Permutations*, Journal of Integer Sequences 27 (2024), Article 24.6.7, Lemma 5.2 (`jis-2024-24.6.7-lem-37`), quoting Elder, Harris, Kretschmann, and Martínez Mori, Lemma 3.1.

Stated but not proved: `MetaMathlibExt.stirlingTotalDisplacement_comp_perm` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean, line 332](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean#L332). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-and-displacement-statistics-of-stirling-pe/index.html#stirling-total-displacement-comp-perm).

## Total displacement of a Stirling permutation

Let $w = w_1 \cdots w_{2n}$ be a Stirling
permutation of order $n$, read as a parking function of length $2n$. Then the total displacement
of $w$, the sum $d(1) + \dots + d(2n)$ of the displacements of its cars, is $n^2$.

## Sources

- L. Colmenarejo et al., *On the Lucky and Displacement Statistics of Stirling Permutations*, Journal of Integer Sequences 27 (2024), Article 24.6.7, Corollary 5.3 (`jis-2024-24.6.7-cor-38`).

Stated but not proved: `MetaMathlibExt.stirlingTotalDisplacement_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean, line 341](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean#L341). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-and-displacement-statistics-of-stirling-pe/index.html#stirling-total-displacement-eq).

## Number of cars with zero displacement

Let $n \ge 1$ and let $w$ be a Stirling
permutation of order $n$, read as a parking function of length $2n$. The number of cars
$i \in \{1, \dots, 2n\}$ with displacement $d(i) = 0$ is at least $1$ and at most $n$.

## Sources

- L. Colmenarejo et al., *On the Lucky and Displacement Statistics of Stirling Permutations*, Journal of Integer Sequences 27 (2024), Article 24.6.7, Corollary 5.6 (`jis-2024-24.6.7-cor-41`).

Stated but not proved: `MetaMathlibExt.stirling_card_zero_displacement` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean, line 349](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean#L349). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-and-displacement-statistics-of-stirling-pe/index.html#stirling-card-zero-displacement).

## Unlucky cars of an extremely lucky Stirling permutation

Let $w = w_1 \cdots w_{2n}$ be a
Stirling permutation of order $n$ that is extremely lucky, that is, its set $\mathrm{Lucky}(w)$
of lucky cars has exactly $n$ elements, and let $1 \le i \le n$. If car $j$ is unlucky and
exactly $i - 1$ of the cars $1, \dots, j - 1$ are unlucky, then car $j$ prefers spot
$w_j = n - i + 1$ and has displacement $d(j) = 2i - 1$.

## Sources

- L. Colmenarejo et al., *On the Lucky and Displacement Statistics of Stirling Permutations*, Journal of Integer Sequences 27 (2024), Article 24.6.7, Lemma 5.7 (`jis-2024-24.6.7-lem-42`).

Stated but not proved: `MetaMathlibExt.extremely_lucky_unlucky_car` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean, line 361](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean#L361). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-and-displacement-statistics-of-stirling-pe/index.html#extremely-lucky-unlucky-car).

## Extremely lucky Stirling permutations are determined by their displacements

Let $w$ and
$w'$ be Stirling permutations of order $n$, and suppose that $w$ is extremely lucky, that is, its
set $\mathrm{Lucky}(w)$ of lucky cars has exactly $n$ elements. If every car has the same
displacement in $w'$ as in $w$ (that is, $\mathrm{dis}(w') = \mathrm{dis}(w)$), then $w' = w$.

## Sources

- L. Colmenarejo et al., *On the Lucky and Displacement Statistics of Stirling Permutations*, Journal of Integer Sequences 27 (2024), Article 24.6.7, Theorem 5.8 (`jis-2024-24.6.7-thm-43`).

Stated but not proved: `MetaMathlibExt.extremely_lucky_eq_of_displacement_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean, line 374](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean#L374). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-and-displacement-statistics-of-stirling-pe/index.html#extremely-lucky-eq-of-displacement-eq).

## Stirling permutations with $n$ nonzero displacements

For every natural number $n$, the
number of Stirling permutations $w$ of order $n$ in which exactly $n$ cars have nonzero
displacement (equivalently, whose displacement composition $\mathrm{dis}(w)$ has exactly $n$
nonzero parts) is the Catalan number $C_n$.

## Sources

- L. Colmenarejo et al., *On the Lucky and Displacement Statistics of Stirling Permutations*, Journal of Integer Sequences 27 (2024), Article 24.6.7, Corollary 5.9 (`jis-2024-24.6.7-cor-45`).

Stated but not proved: `MetaMathlibExt.card_stirling_displacement_nonzero_parts` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean, line 385](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/StirlingLuckyDisplacementWanted.lean#L385). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-and-displacement-statistics-of-stirling-pe/index.html#card-stirling-displacement-nonzero-parts).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Lucky and displacement statistics of Stirling permutations](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-and-displacement-statistics-of-stirling-pe/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/parking-functions/lucky-and-displacement-statistics-of-stirling-pe)
