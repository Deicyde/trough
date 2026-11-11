---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.Matching.GaleShapley.StrictTotalOrder, MathlibExt.Combinatorics.Matching.GaleShapley.StrictTotalOrder.mk, MathlibExt.Combinatorics.Matching.GaleShapley.StrictTotalOrder.lt, MathlibExt.Combinatorics.Matching.GaleShapley.StrictTotalOrder.irrefl, MathlibExt.Combinatorics.Matching.GaleShapley.StrictTotalOrder.trans, MathlibExt.Combinatorics.Matching.GaleShapley.StrictTotalOrder.total, MathlibExt.Combinatorics.Matching.GaleShapley.StrictTotalOrder.ext, MathlibExt.Combinatorics.Matching.GaleShapley.MPrefs
statement: formalized
---

# Stable marriage problem

44 results, 33 proved and 11 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/stable-marriage-problem/index.html).

## Strict preference order

A strict total order on a type $\alpha$ is a binary relation
$<$ on $\alpha$ that is irreflexive ($a < a$ holds for no $a$), transitive ($a < b$ and $b < c$
imply $a < c$) and total on distinct elements ($a \ne b$ implies $a < b$ or $b < a$). In the
Gale–Shapley development it models strict preference.

Formalized by `MathlibExt.Combinatorics.Matching.GaleShapley.StrictTotalOrder`, an abbreviation declared in [MathlibExt/Combinatorics/Matching/GaleShapley.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Matching/GaleShapley.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/stable-marriage-problem/index.html#strict-total-order).

## Building a strict total order from a relation

A binary relation $<$ on a set $\alpha$
that is irreflexive ($a \not< a$ for all $a$), transitive ($a < b$ and $b < c$ imply $a < c$) and
total on distinct elements ($a \ne b$ implies $a < b$ or $b < a$) defines a strict total order on
$\alpha$ whose relation is $<$.

Formalized by `MathlibExt.Combinatorics.Matching.GaleShapley.StrictTotalOrder.mk`, an abbreviation declared in [MathlibExt/Combinatorics/Matching/GaleShapley.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Matching/GaleShapley.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/stable-marriage-problem/index.html#mk).

## Relation of a strict total order

The relation of a strict total order $T$ on a set
$\alpha$ is its underlying binary relation $\lt _T$ on $\alpha$, which is irreflexive, transitive,
and relates any two distinct elements in one direction or the other.

Formalized by `MathlibExt.Combinatorics.Matching.GaleShapley.StrictTotalOrder.lt`, an abbreviation declared in [MathlibExt/Combinatorics/Matching/GaleShapley.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Matching/GaleShapley.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/stable-marriage-problem/index.html#lt).

## Irreflexivity of a strict total order

Let $T$ be a strict total order on a set $\alpha$,
with relation $\lt _T$. Then $a \lt _T a$ fails for every $a \in \alpha$.

Formalized by `MathlibExt.Combinatorics.Matching.GaleShapley.StrictTotalOrder.irrefl`, an abbreviation declared in [MathlibExt/Combinatorics/Matching/GaleShapley.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Matching/GaleShapley.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/stable-marriage-problem/index.html#irrefl).

## Transitivity of a strict total order

Let $<$ be the relation of a strict total order on a
type $\alpha$. If $a, b, c \in \alpha$ satisfy $a < b$ and $b < c$, then $a < c$.

Formalized by `MathlibExt.Combinatorics.Matching.GaleShapley.StrictTotalOrder.trans`, an abbreviation declared in [MathlibExt/Combinatorics/Matching/GaleShapley.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Matching/GaleShapley.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/stable-marriage-problem/index.html#trans).

## Strict total orders are total on distinct elements

Let $<$ be the relation of a strict
total order on a type $\alpha$. If $a, b \in \alpha$ and $a \ne b$, then $a < b$ or $b < a$.

Formalized by `MathlibExt.Combinatorics.Matching.GaleShapley.StrictTotalOrder.total`, an abbreviation declared in [MathlibExt/Combinatorics/Matching/GaleShapley.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Matching/GaleShapley.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/stable-marriage-problem/index.html#total).

## Strict total orders are determined by their relation

Let $T$ and $T'$ be strict total
orders on a set $\alpha$, with relations $\lt _T$ and $\lt _{T'}$. If $x \lt _T y \iff x \lt _{T'} y$ for all
$x, y \in \alpha$, then $T = T'$.

Formalized by `MathlibExt.Combinatorics.Matching.GaleShapley.StrictTotalOrder.ext`, a theorem declared in [MathlibExt/Combinatorics/Matching/GaleShapley.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Matching/GaleShapley.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/stable-marriage-problem/index.html#ext).

## Men's preferences

For sets $M$ (men) and $W$ (women), a preference profile of the men
assigns to each $m \in M$ a strict total order on $W$, the preferences of $m$.

Formalized by `MathlibExt.Combinatorics.Matching.GaleShapley.MPrefs`, an abbreviation declared in [MathlibExt/Combinatorics/Matching/GaleShapley.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Matching/GaleShapley.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/stable-marriage-problem/index.html#mprefs).

## Women's preference profile

For types $M$ and $W$, a preference profile of $W$ over $M$
assigns to each $w \in W$ a strict total order on $M$, read as the strict preference of $w$
among the elements of $M$.

Formalized by `MathlibExt.Combinatorics.Matching.GaleShapley.WPrefs`, an abbreviation declared in [MathlibExt/Combinatorics/Matching/GaleShapley.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Matching/GaleShapley.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/stable-marriage-problem/index.html#wprefs).

## Perfect matching

A perfect matching between sets $M$ and $W$ is a bijection
$\mu \colon M \to W$, which matches each $m \in M$ with $\mu(m) \in W$.

Formalized by `MathlibExt.Combinatorics.Matching.GaleShapley.PerfectMatching`, an abbreviation declared in [MathlibExt/Combinatorics/Matching/GaleShapley.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Matching/GaleShapley.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/stable-marriage-problem/index.html#perfect-matching).

## Blocking pair

Let $M$ and $W$ be sets. Suppose that each $m \in M$ has a strict total
order $\lt _m$ of preference on $W$ and each $w \in W$ has a strict total order $\lt _w$ of preference
on $M$, where $x \lt _m y$ means that $m$ prefers $x$ to $y$, and likewise for $\lt _w$. For a perfect
matching $\mu$ between $M$ and $W$, a pair $(m, w) \in M \times W$ is a blocking pair when
$w \lt _m \mu(m)$ and $m \lt _w \mu^{-1}(w)$, that is, when $m$ prefers $w$ to $\mu(m)$ and $w$ prefers
$m$ to $\mu^{-1}(w)$.

Formalized by `MathlibExt.Combinatorics.Matching.GaleShapley.IsBlockingPair`, a definition declared in [MathlibExt/Combinatorics/Matching/GaleShapley.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Matching/GaleShapley.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/stable-marriage-problem/index.html#is-blocking-pair).

## Stable perfect matching

Let $M$ and $W$ be sets. Suppose that each $m \in M$ has a strict
total order of preference on $W$ and each $w \in W$ has a strict total order of preference on
$M$. A perfect matching $\mu$ between $M$ and $W$ is stable for these preferences when no pair
$(m, w) \in M \times W$ is a blocking pair for $\mu$.

Formalized by `MathlibExt.Combinatorics.Matching.GaleShapley.IsStable`, a definition declared in [MathlibExt/Combinatorics/Matching/GaleShapley.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Matching/GaleShapley.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/stable-marriage-problem/index.html#is-stable).

## Existence of stable perfect matchings

Let $M$ and $W$ be finite sets with the same
number of elements. Suppose that each $m \in M$ has a strict total order of preference on $W$ and
each $w \in W$ has a strict total order of preference on $M$. Then some perfect matching between
$M$ and $W$ is stable for these preferences.

This is the Gale–Shapley theorem, stated without decidability assumptions on $M$ and $W$.

Formalized by `MathlibExt.Combinatorics.Matching.GaleShapley.gale_shapley_exists_stable_matching_general`, a theorem declared in [MathlibExt/Combinatorics/Matching/GaleShapley.lean, line 584](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Matching/GaleShapley.lean#L584). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/stable-marriage-problem/index.html#gale-shapley-exists-stable-matching-gene).

## Gale–Shapley theorem

Let $M$ and $W$ be finite sets with the same number of elements.
Suppose that each $m \in M$ has a strict total order of preference on $W$ and each $w \in W$ has
a strict total order of preference on $M$. Then some perfect matching between $M$ and $W$ is
stable for these preferences.

## Sources

- D. Gale and L. S. Shapley, "College Admissions and the Stability of Marriage", American Mathematical Monthly 69 (1962), 9–15, DOI 10.2307/2312726. It follows from `gale_shapley_exists_stable_matching_general`; the instances `[DecidableEq M]` and `[DecidableEq W]` are unused and keep the source's shape.

Formalized by `MathlibExt.Combinatorics.Matching.GaleShapley.gale_shapley_exists_stable_matching`, a theorem declared in [MathlibExt/Combinatorics/Matching/GaleShapley.lean, line 706](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Matching/GaleShapley.lean#L706). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/stable-marriage-problem/index.html#gale-shapley-exists-stable-matching).

## Preference profile for $n$ men and $n$ women

For a natural number $n$, number $n$ men and
$n$ women by $0, \dots, n - 1$. A preference profile $P = (M, W)$ for them consists of a
permutation $M_i$ of $\{0, \dots, n - 1\}$ for each man $i$ and a permutation $W_j$ of
$\{0, \dots, n - 1\}$ for each woman $j$: $M_i(r)$ is the woman man $i$ ranks at zero-based
position $r$, and $W_j(r)$ is the man woman $j$ ranks at position $r$.

## Sources

- Borodin, Duncan, Litchev, Liu, Moroz, Qian, Raghavan, Rastogi, Voigt, and Khovanova, *Sequences of the Stable Matching Problem*, Journal of Integer Sequences 27 (2024), Article 24.2.2, Section 2.

Formalized by `MetaMathlibExt.StableMatchingSequences.PreferenceProfile`, an abbreviation declared in [WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/stable-marriage-problem/index.html#preference-profile).

## Rank of a woman for a man

For a preference profile of $n$ men and $n$ women, the rank of
woman $j$ for man $i$ is the zero-based position $r \in \{0, \dots, n-1\}$ at which $i$ ranks
$j$, so his favorite has rank $0$ and his least favorite has rank $n - 1$.

The paper's one-based ranking is this rank plus one.

## Sources

- Borodin et al., *Sequences of the Stable Matching Problem*, Journal of Integer Sequences 27 (2024), Article 24.2.2, Section 2.

Formalized by `MetaMathlibExt.StableMatchingSequences.manRank`, a definition declared in [WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/stable-marriage-problem/index.html#man-rank).

## A woman's rank of a man

For a preference profile for $n$ men and $n$ women, the rank
that woman $j$ gives man $i$ is the zero-based position at which she ranks him, that is, the
paper's ranking minus one.

## Sources

- Borodin et al., *Sequences of the Stable Matching Problem*, Journal of Integer Sequences 27 (2024), Article 24.2.2, Section 2.

Formalized by `MetaMathlibExt.StableMatchingSequences.womanRank`, a definition declared in [WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/stable-marriage-problem/index.html#woman-rank).

## Soulmate pair

For a preference profile of $n$ men and $n$ women, man $i$ and woman $j$
are soulmates when each ranks the other first: $j$ is the first choice of $i$ and $i$ is the
first choice of $j$.

## Sources

- Borodin et al., *Sequences of the Stable Matching Problem*, Journal of Integer Sequences 27 (2024), Article 24.2.2, Section 2.1.

Formalized by `MetaMathlibExt.StableMatchingSequences.IsSoulmatePair`, a definition declared in [WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/stable-marriage-problem/index.html#is-soulmate-pair).

## Number of soulmate pairs

The number of soulmate pairs of a preference profile $P$ for
$n$ men and $n$ women is the number of pairs $(i, j)$ of a man $i$ and a woman $j$ that are
soulmates in $P$, that is, each ranks the other first.

This is the paper's $k$ in $F(k, n)$, the number of profiles with exactly $k$ soulmate pairs.

## Sources

- Borodin et al., *Sequences of the Stable Matching Problem*, Journal of Integer Sequences 27 (2024), Article 24.2.2, Section 4.

Formalized by `MetaMathlibExt.StableMatchingSequences.soulmatePairCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/stable-marriage-problem/index.html#soulmate-pair-count).

## Men's preferences induced by rankings

For a preference profile of $n$ men and $n$
women, each man $i$ gets the strict total order on the women in which $i$ prefers woman $a$ to
woman $b$ exactly when he ranks $a$ at an earlier position than $b$.

## Sources

- Borodin et al., *Sequences of the Stable Matching Problem*, Journal of Integer Sequences 27 (2024), Article 24.2.2, Section 2.

Formalized by `MetaMathlibExt.StableMatchingSequences.manPrefs`, a definition declared in [WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/stable-marriage-problem/index.html#man-prefs).

## Women's preference orders of a profile

For a preference profile $P$ for $n$ men and $n$
women, each woman $j$ gets the strict total order on the men in which man $a$ comes before
(is preferred to) man $b$ exactly when woman $j$ ranks $a$ at an earlier position than $b$.

## Sources

- Borodin et al., *Sequences of the Stable Matching Problem*, Journal of Integer Sequences 27 (2024), Article 24.2.2, Section 2.

Formalized by `MetaMathlibExt.StableMatchingSequences.womanPrefs`, a definition declared in [WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/stable-marriage-problem/index.html#woman-prefs).

## Stable matching

For a preference profile of $n$ men and $n$ women, a matching $\mu$, in
which man $i$ marries woman $\mu(i)$, is stable when no man and woman both strictly prefer each
other to their own spouses. Equivalently, $\mu$ is a stable perfect matching for the strict
preferences induced by the men's and the women's rankings.

## Sources

- Borodin et al., *Sequences of the Stable Matching Problem*, Journal of Integer Sequences 27 (2024), Article 24.2.2, Section 2.

Formalized by `MetaMathlibExt.StableMatchingSequences.IsStableMatching`, an abbreviation declared in [WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/stable-marriage-problem/index.html#is-stable-matching).

## Stability in terms of ranks

For a preference profile of $n$ men and $n$ women, a
matching $\mu$, in which man $i$ marries woman $\mu(i)$, is stable if and only if there are no
man $i$ and woman $j$ such that $i$ ranks $j$ strictly above his wife $\mu(i)$ and $j$ ranks $i$
strictly above her husband $\mu^{-1}(j)$.

## Sources

- Borodin et al., *Sequences of the Stable Matching Problem*, Journal of Integer Sequences 27 (2024), Article 24.2.2, Section 2.

Formalized by `MetaMathlibExt.StableMatchingSequences.isStableMatching_iff`, a theorem declared in [WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/stable-marriage-problem/index.html#is-stable-matching-iff).

## Hell-couple

Let $P$ be a preference profile of $n$ men and $n$ women, and let $\mu$
be a matching in which man $i$ marries woman $\mu(i)$. Man $i$ and his wife $\mu(i)$ form a
hell-couple when each ranks the other last: $i$ ranks $\mu(i)$ in his last position and
$\mu(i)$ ranks $i$ in her last position.

## Sources

- Borodin et al., *Sequences of the Stable Matching Problem*, Journal of Integer Sequences 27 (2024), Article 24.2.2, Section 6.1.

Formalized by `MetaMathlibExt.StableMatchingSequences.IsHellCouple`, a definition declared in [WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/stable-marriage-problem/index.html#is-hell-couple).

## Number of Latin squares

For $n \in \mathbb{N}$, $L_n$ is the number of Latin squares of
order $n$: families $(M_0, \dots, M_{n-1})$ of permutations of $\{0, \dots, n-1\}$ (the rows)
such that for every position $r$ the entries $M_0(r), \dots, M_{n-1}(r)$ (column $r$) are
pairwise distinct.

## Sources

- Borodin et al., *Sequences of the Stable Matching Problem*, Journal of Integer Sequences 27 (2024), Article 24.2.2, Section 4.2 (OEIS A002860).

Formalized by `MetaMathlibExt.StableMatchingSequences.latinSquareCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/stable-marriage-problem/index.html#latin-square-count).

## Provisional engagement in the Gale–Shapley algorithm

Let $P$ be a preference profile for
$n$ men and $n$ women, with positions in each ranking numbered $0, \dots, n - 1$, and consider
the state of the men-proposing Gale–Shapley algorithm in which each man $i'$ has proposed to the
women at the positions $r' < p(i')$ of his ranking. Man $i$ is provisionally engaged in this
state if $1 \le p(i) \le n$ and the woman $w$ at his position $p(i) - 1$ (the last woman he
proposed to) ranks him weakly above every man who has proposed to her: her position for $i$ is
at most her position for every man $i'$ who has $w$ at some position $r' < p(i')$.

## Sources

- Borodin et al., *Sequences of the Stable Matching Problem*, Journal of Integer Sequences 27 (2024), Article 24.2.2, Section 2 (description of the Gale–Shapley algorithm).

Formalized by `MetaMathlibExt.StableMatchingSequences.GSEngaged`, a definition declared in [WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/stable-marriage-problem/index.html#gsengaged).

## Proposal counts in the Gale–Shapley algorithm

Let $P$ be a preference profile for $n$ men
and $n$ women. The number $p_t(i)$ of women man $i$ has proposed to after $t$ rounds of the
men-proposing Gale–Shapley algorithm on $P$ is defined by $p_0(i) = 0$ and, for every $t$,
$p_{t+1}(i) = p_t(i)$ if man $i$ is provisionally engaged in the state $p_t$ and
$p_{t+1}(i) = p_t(i) + 1$ otherwise: in each round every man who is not provisionally engaged
proposes to his next choice.

## Sources

- Borodin et al., *Sequences of the Stable Matching Problem*, Journal of Integer Sequences 27 (2024), Article 24.2.2, Section 2.

Formalized by `MetaMathlibExt.StableMatchingSequences.gsProposals`, a definition declared in [WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/stable-marriage-problem/index.html#gs-proposals).

## Number of Gale–Shapley rounds

For a preference profile $P$ for $n$ men and $n$ women,
the number of rounds of the men-proposing Gale–Shapley algorithm on $P$ is the least $t$ such
that every man is provisionally engaged after $t$ rounds (or $0$ if there is no such $t$).

## Sources

- Borodin et al., *Sequences of the Stable Matching Problem*, Journal of Integer Sequences 27 (2024), Article 24.2.2, Section 2.

Formalized by `MetaMathlibExt.StableMatchingSequences.galeShapleyRounds`, a definition declared in [WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/stable-marriage-problem/index.html#gale-shapley-rounds).

## No proposals before the first round

For every preference profile, after zero rounds of
the men-proposing Gale–Shapley algorithm every man has made zero proposals.

## Sources

- Borodin et al., *Sequences of the Stable Matching Problem*, Journal of Integer Sequences 27 (2024), Article 24.2.2, Section 2.

Formalized by `MetaMathlibExt.StableMatchingSequences.gsProposals_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/stable-marriage-problem/index.html#gs-proposals-zero).

## One round of the Gale–Shapley algorithm

Let $P$ be a preference profile for $n$ men and
$n$ women and let $t$ be a natural number. After $t + 1$ rounds of the men-proposing
Gale–Shapley algorithm on $P$, a man who is provisionally engaged after $t$ rounds has made as
many proposals as after $t$ rounds, and every other man has made one proposal more than after
$t$ rounds.

## Sources

- Borodin et al., *Sequences of the Stable Matching Problem*, Journal of Integer Sequences 27 (2024), Article 24.2.2, Section 2.

Formalized by `MetaMathlibExt.StableMatchingSequences.gsProposals_succ`, a theorem declared in [WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/stable-marriage-problem/index.html#gs-proposals-succ).

## Gale–Shapley rounds with no participants

For the preference profile with no men and no
women, the men-proposing Gale–Shapley algorithm takes zero rounds.

## Sources

- Borodin et al., *Sequences of the Stable Matching Problem*, Journal of Integer Sequences 27 (2024), Article 24.2.2, Section 2.

Formalized by `MetaMathlibExt.StableMatchingSequences.galeShapleyRounds_of_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/stable-marriage-problem/index.html#gale-shapley-rounds-of-zero).

## A profile has at most $n$ soulmate pairs

Every preference profile for $n$ men and $n$
women has at most $n$ soulmate pairs, since a man's soulmate is his first choice.

## Sources

- Borodin et al., *Sequences of the Stable Matching Problem*, Journal of Integer Sequences 27 (2024), Article 24.2.2, Section 4.

Formalized by `MetaMathlibExt.StableMatchingSequences.soulmatePairCount_le`, a theorem declared in [WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/stable-marriage-problem/index.html#soulmate-pair-count-le).

## Latin squares of order zero

There is exactly one Latin square of order $0$, that is,
$L_0 = 1$.

## Sources

- Borodin et al., *Sequences of the Stable Matching Problem*, Journal of Integer Sequences 27 (2024), Article 24.2.2, Section 4.2 (OEIS A002860).

Formalized by `MetaMathlibExt.StableMatchingSequences.latinSquareCount_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/stable-marriage-problem/index.html#latin-square-count-zero).

## Gale–Shapley rounds when all men have the same preferences

Let $P$ be a preference
profile for $n$ men and $n$ women in which all men rank the women in the same order. Then the
men-proposing Gale–Shapley algorithm on $P$ ends in exactly $n$ rounds.

## Sources

- Borodin, Duncan, Litchev, Liu, Moroz, Qian, Raghavan, Rastogi, Voigt, and Khovanova, *Sequences of the Stable Matching Problem*, Journal of Integer Sequences 27 (2024), Article 24.2.2, Proposition 1 (`jis-2024-24.2.2-prop-1`).

Stated but not proved: `MetaMathlibExt.StableMatchingSequences.galeShapleyRounds_of_same_taste` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/stable-marriage-problem/index.html#gale-shapley-rounds-of-same-taste).

## When the Gale–Shapley algorithm ends in one round

Let $n \ge 1$ and let $P$ be a
preference profile for $n$ men and $n$ women. The men-proposing Gale–Shapley algorithm on $P$ ends
in exactly one round if and only if every woman is the first choice of exactly one man.

## Sources

- Borodin et al., *Sequences of the Stable Matching Problem*, Journal of Integer Sequences 27 (2024), Article 24.2.2, Proposition 2 (`jis-2024-24.2.2-prop-2`).

Stated but not proved: `MetaMathlibExt.StableMatchingSequences.galeShapleyRounds_eq_one_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/stable-marriage-problem/index.html#gale-shapley-rounds-eq-one-iff).

## Counting disjoint preference profiles

Call a preference profile for $n$ men and $n$ women
disjoint if for every pair of positions $(r, s)$ there is exactly one man–woman pair in which the
man ranks the woman at position $r$ and the woman ranks the man at position $s$. For every natural
number $n$, the number of disjoint profiles is at most $(n^2)!$ and is divisible by $(n!)^2$.

## Sources

- Borodin et al., *Sequences of the Stable Matching Problem*, Journal of Integer Sequences 27 (2024), Article 24.2.2, Proposition 3 (`jis-2024-24.2.2-prop-3`).

Stated but not proved: `MetaMathlibExt.StableMatchingSequences.disjoint_profiles_card_le_and_dvd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean, line 270](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean#L270). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/stable-marriage-problem/index.html#disjoint-profiles-card-le-and-dvd).

## Outsiders without soulmate pairs

Let $n$ and $k$ be natural numbers, where $n - k$ is
read as $0$ when $k > n$. Consider the $n - k$ men $k, \dots, n - 1$ and the $n - k$ women
$k, \dots, n - 1$ among $n$ men and $n$ women numbered from $0$, where each of these men ranks all
$n$ women and each of these women ranks all $n$ men. The number of ways to choose these rankings
so that no man and woman among them each rank the other first is

$$\sum_{i=0}^{n-k} (-1)^i \binom{n-k}{i}^2 ((n-1)!)^{2i}\, i!\, (n!)^{2(n-k-i)}.$$

This number is the paper's $S(k, n)$: the preferences of the remaining $k$ men and $k$ women are
ignored.

## Sources

- Borodin et al., *Sequences of the Stable Matching Problem*, Journal of Integer Sequences 27 (2024), Article 24.2.2, Lemma 4 (`jis-2024-24.2.2-lem-4`).

Stated but not proved: `MetaMathlibExt.StableMatchingSequences.outside_no_soulmates_card` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/stable-marriage-problem/index.html#outside-no-soulmates-card).

## Number of profiles with exactly $k$ soulmate pairs

For natural numbers $n$ and $k$, the
number $F(k, n)$ of preference profiles for $n$ men and $n$ women with exactly $k$ soulmate pairs
is

$$
\binom{n}{k}^2 k!\, ((n-1)!)^{2k}
\sum_{i=0}^{n-k} (-1)^i \binom{n-k}{i}^2 ((n-1)!)^{2i}\, i!\, (n!)^{2(n-k-i)}.
$$

When $k > n$ both sides are $0$.

The sum is the paper's $S(k, n)$ of Lemma 4, which counts the preferences of the people outside
the $k$ soulmate couples that create no further soulmate pair.

## Sources

- Borodin et al., *Sequences of the Stable Matching Problem*, Journal of Integer Sequences 27 (2024), Article 24.2.2, Theorem 6 (`jis-2024-24.2.2-thm-6`).

Stated but not proved: `MetaMathlibExt.StableMatchingSequences.soulmate_profiles_card` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean, line 302](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean#L302). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/stable-marriage-problem/index.html#soulmate-profiles-card).

## Profiles with $n - 1$ soulmate pairs

Let $P$ be a preference profile for $n$ men and $n$
women with exactly $n - 1$ soulmate pairs (read as $0$ when $n = 0$). Then $P$ has exactly one
stable matching. Moreover, for every stable matching $\mu$ of $P$ and every man $i$ who has no
soulmate, the men-proposing Gale–Shapley algorithm on $P$ ends after $r + 1$ rounds, where $r$ is
the zero-based position at which man $i$ ranks his wife $\mu(i)$.

## Sources

- Borodin et al., *Sequences of the Stable Matching Problem*, Journal of Integer Sequences 27 (2024), Article 24.2.2, Proposition 7 (`jis-2024-24.2.2-prop-7`).

Stated but not proved: `MetaMathlibExt.StableMatchingSequences.unique_stable_matching_of_soulmatePairCount_eq_pred` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean, line 316](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean#L316). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/stable-marriage-problem/index.html#unique-stable-matching-of-soulmate-pair).

## Profiles with Latin-square men's preferences, counted by soulmate pairs

For all
$n, k \in \mathbb{N}$, the number of preference profiles of $n$ men and $n$ women in which, for
every position $r$, different men rank different women at position $r$ (the men's rankings form
a Latin square), and which have exactly $k$ soulmate pairs, is

$$L_n \binom{n}{k} (n-1)^{n-k} ((n-1)!)^n,$$

where $L_n$ is the number of Latin squares of order $n$.

Here $n - 1$ and $n - k$ are truncated subtractions in $\mathbb{N}$.

## Sources

- Borodin et al., *Sequences of the Stable Matching Problem*, Journal of Integer Sequences 27 (2024), Article 24.2.2, Theorem 8 (`jis-2024-24.2.2-thm-8`).

Stated but not proved: `MetaMathlibExt.StableMatchingSequences.men_latin_soulmate_profiles_card` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean, line 329](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean#L329). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/stable-marriage-problem/index.html#men-latin-soulmate-profiles-card).

## Mutually Latin profiles with $k$ soulmate pairs

Let $n$ and $k$ be natural numbers and
let $L_n$ be the number of Latin squares of order $n$. Call the men's preferences of a preference
profile for $n$ men and $n$ women Latin when, for every position $r$, distinct men rank distinct
women at position $r$, and likewise for the women's preferences. The number of preference
profiles whose men's and women's preferences are both Latin and that have exactly $k$ soulmate
pairs is

$$\frac{L_n^2}{n!} \binom{n}{k} \sum_{i=0}^{n-k} \frac{(-1)^i (n-k)!}{i!}.$$

When $k > n$ the binomial coefficient vanishes and both sides are $0$.

## Sources

- Borodin et al., *Sequences of the Stable Matching Problem*, Journal of Integer Sequences 27 (2024), Article 24.2.2, Theorem 9 (`jis-2024-24.2.2-thm-9`).

Stated but not proved: `MetaMathlibExt.StableMatchingSequences.mutually_latin_soulmate_profiles_card` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean, line 341](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean#L341). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/stable-marriage-problem/index.html#mutually-latin-soulmate-profiles-card).

## At most one hell-couple in a stable matching

Let $P$ be a preference profile of $n$
men and $n$ women, and let $\mu$ be a stable matching for $P$, in which man $i$ marries woman
$\mu(i)$. Then at most one man $i$ forms a hell-couple with his wife $\mu(i)$.

## Sources

- Borodin et al., *Sequences of the Stable Matching Problem*, Journal of Integer Sequences 27 (2024), Article 24.2.2, Proposition 12 (`jis-2024-24.2.2-prop-12`).

Stated but not proved: `MetaMathlibExt.StableMatchingSequences.hellCouple_subsingleton` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean, line 353](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean#L353). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/stable-marriage-problem/index.html#hell-couple-subsingleton).

## A hell-couple belongs to every stable matching

Let $P$ be a preference profile for $n$
men and $n$ women and let $\mu$ and $\nu$ be stable matchings for $P$. If man $i$ and his wife
$\mu(i)$ form a hell-couple in $\mu$ (each ranks the other last), then $\nu(i) = \mu(i)$.

## Sources

- Borodin et al., *Sequences of the Stable Matching Problem*, Journal of Integer Sequences 27 (2024), Article 24.2.2, Proposition 13 (`jis-2024-24.2.2-prop-13`).

Stated but not proved: `MetaMathlibExt.StableMatchingSequences.hellCouple_mem_all_stable` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean, line 363](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean#L363). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/stable-marriage-problem/index.html#hell-couple-mem-all-stable).

## Profiles with a pair of outcasts

In a preference profile for $n$ men and $n$ women, a man
$i$ and a woman $j$ form a pair of outcasts when every man other than $i$ ranks $j$ last and every
woman other than $j$ ranks $i$ last. The number of preference profiles with at least one pair of
outcasts is $14$ if $n = 2$ and $n^4 ((n-1)!)^{2n}$ if $n \ne 2$ (this is $0$ for $n = 0$).

## Sources

- Borodin et al., *Sequences of the Stable Matching Problem*, Journal of Integer Sequences 27 (2024), Article 24.2.2, Proposition 14 (`jis-2024-24.2.2-prop-14`).

Stated but not proved: `MetaMathlibExt.StableMatchingSequences.outcast_profiles_card` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean, line 375](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StableMatchingSequencesWanted.lean#L375). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/stable-marriage-problem/index.html#outcast-profiles-card).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Stable marriage problem](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/stable-marriage-problem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/matchings-and-flows/stable-marriage-problem)
