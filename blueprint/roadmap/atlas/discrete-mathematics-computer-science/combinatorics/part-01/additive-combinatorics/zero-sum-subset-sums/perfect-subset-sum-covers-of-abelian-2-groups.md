---
declaration: section
origin: cited
lean: MetaMathlibExt.PerfectSubsetSumCover.coverCount, MetaMathlibExt.PerfectSubsetSumCover.IsPerfectMCover, MetaMathlibExt.PerfectSubsetSumCover.IsPerfectCover, MetaMathlibExt.PerfectSubsetSumCover.count, MetaMathlibExt.PerfectSubsetSumCover.count_eq_card_filter, MetaMathlibExt.PerfectSubsetSumCover.count_small, MetaMathlibExt.PerfectSubsetSumCover.isPerfectCover_zmod_four, MetaMathlibExt.PerfectSubsetSumCover.oddCombinations
statement: formalized
---

# Perfect subset-sum covers of abelian 2-groups

37 results, 11 proved and 26 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/perfect-subset-sum-covers-of-abelian-2-groups/index.html).

## Perfect Subset Sum Cover

## Cover count

Let $G$ be an abelian group, $s = (s_i)_{i \in \iota}$ a family in $G$
indexed by a finite type $\iota$ (a colored multiset), and $g \in G$. The cover count of $g$ by
$s$ is the number of index sets $I \subseteq \iota$ with $\sum_{i \in I} s_i = g$: the number of
times $s$ covers $g$ by its subset sums (the empty set covers $0$).

## Sources

- John Greene and Clayton Higgins, *Maximal Subset Sums in a Group of Order a Power of 2*, Journal of Integer Sequences 28 (2025), Article 25.7.8, Section 1 (subset sums, "covered `m` times", Lemma 8).

Formalized by `MetaMathlibExt.PerfectSubsetSumCover.coverCount`, a definition declared in [WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/perfect-subset-sum-covers-of-abelian-2-groups/index.html#cover-count).

## Perfect $m$-cover

Let $G$ be an abelian group, $m$ a natural number and
$s = (s_i)_{i \in \iota}$ a family of elements of $G$ indexed by a finite set $\iota$ (a colored
multiset: repeated values count separately). The family $s$ is a perfect $m$-cover of $G$ when
every $g \in G$ equals $\sum_{i \in I} s_i$ for exactly $m$ subsets $I \subseteq \iota$ (the
empty subset has sum $0$).

## Sources

- John Greene and Clayton Higgins, *Maximal Subset Sums in a Group of Order a Power of 2*, Journal of Integer Sequences 28 (2025), Article 25.7.8, Section 1 (perfect `m`-covers, Lemmas 5 and 8).

Formalized by `MetaMathlibExt.PerfectSubsetSumCover.IsPerfectMCover`, a definition declared in [WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/perfect-subset-sum-covers-of-abelian-2-groups/index.html#is-perfect-mcover).

## Perfect cover

Let $G$ be an abelian group. A finite set $S \subseteq G$ is a perfect cover
of $G$ when every element of $G$ is the sum of exactly one subset of $S$ (the empty subset has
sum $0$); that is, the family of the elements of $S$ is a perfect $1$-cover of $G$.

## Sources

- John Greene and Clayton Higgins, *Maximal Subset Sums in a Group of Order a Power of 2*, Journal of Integer Sequences 28 (2025), Article 25.7.8, Section 1 (perfect covers, Lemma 16).

Formalized by `MetaMathlibExt.PerfectSubsetSumCover.IsPerfectCover`, a definition declared in [WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/perfect-subset-sum-covers-of-abelian-2-groups/index.html#is-perfect-cover).

## Number of perfect covers

For an abelian group $G$, $C(G)$ is the number of perfect
covers of $G$: finite subsets $S \subseteq G$ such that every element of $G$ is the sum of
exactly one subset of $S$ (the empty subset has sum $0$).

## Sources

- John Greene and Clayton Higgins, *Maximal Subset Sums in a Group of Order a Power of 2*, Journal of Integer Sequences 28 (2025), Article 25.7.8, Section 1 (`C(G)`).

Formalized by `MetaMathlibExt.PerfectSubsetSumCover.count`, a definition declared in [WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/perfect-subset-sum-covers-of-abelian-2-groups/index.html#count).

## Perfect cover count as a finset cardinality

For a finite abelian group $G$, the number
$C(G)$ of perfect covers of $G$ equals the number of elements of the finite set of all subsets of
$G$ that are perfect covers.

## Sources

- John Greene and Clayton Higgins, *Maximal Subset Sums in a Group of Order a Power of 2*, Journal of Integer Sequences 28 (2025), Article 25.7.8, Section 1 (`C(G)`).

Formalized by `MetaMathlibExt.PerfectSubsetSumCover.count_eq_card_filter`, a theorem declared in [WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/perfect-subset-sum-covers-of-abelian-2-groups/index.html#count-eq-card-filter).

## Small values of the perfect cover count

Writing $C(K)$ for the number of perfect covers
of a group $K$, we have $C(\mathbb{Z}_2) = 1$, $C(\mathbb{Z}_4) = 2$ and
$C(\mathbb{Z}_2 \oplus \mathbb{Z}_2) = 3$.

The two perfect covers of $\mathbb{Z}_4$ are $\{1, 2\}$ and $\{2, 3\}$.

## Sources

- John Greene and Clayton Higgins, *Maximal Subset Sums in a Group of Order a Power of 2*, Journal of Integer Sequences 28 (2025), Article 25.7.8, Theorems 2 and 4 at `n = 1, 2` and `m = 2`.

Formalized by `MetaMathlibExt.PerfectSubsetSumCover.count_small`, a theorem declared in [WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/perfect-subset-sum-covers-of-abelian-2-groups/index.html#count-small).

## Perfect covers of ℤ₄: an example and a non-example

In the cyclic group
$\mathbb{Z}_4 = \mathbb{Z}/4\mathbb{Z}$, the set $\{1, 2\}$ is a perfect cover and the set
$\{1, 3\}$ is not, since $1 + 3 = 0$.

## Sources

- John Greene and Clayton Higgins, *Maximal Subset Sums in a Group of Order a Power of 2*, Journal of Integer Sequences 28 (2025), Article 25.7.8, Section 1 (perfect covers).

Formalized by `MetaMathlibExt.PerfectSubsetSumCover.isPerfectCover_zmod_four`, a theorem declared in [WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/perfect-subset-sum-covers-of-abelian-2-groups/index.html#is-perfect-cover-zmod-four).

## Odd combinations

For a finite subset $A$ of an abelian group $G$, $\mathcal{T}(A)$ is the
set of all sums $\sum_{x \in A} c_x x$ with integer coefficients $c_x$ such that every $c_x$ is
either $0$ or odd.

## Sources

- John Greene and Clayton Higgins, *Maximal Subset Sums in a Group of Order a Power of 2*, Journal of Integer Sequences 28 (2025), Article 25.7.8, Section 3 (the operator `𝒯`).

Formalized by `MetaMathlibExt.PerfectSubsetSumCover.oddCombinations`, a definition declared in [WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/perfect-subset-sum-covers-of-abelian-2-groups/index.html#odd-combinations).

## Zero is an odd combination

For every finite subset $A$ of an abelian group $G$, $0$ lies
in the set $\mathcal{T}(A)$ of odd combinations of $A$ (take every coefficient equal to $0$).

## Sources

- John Greene and Clayton Higgins, *Maximal Subset Sums in a Group of Order a Power of 2*, Journal of Integer Sequences 28 (2025), Article 25.7.8, Section 3 (the operator `𝒯`).

Formalized by `MetaMathlibExt.PerfectSubsetSumCover.zero_mem_oddCombinations`, a theorem declared in [WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/perfect-subset-sum-covers-of-abelian-2-groups/index.html#zero-mem-odd-combinations).

## Elements of a finite set are odd combinations of it

Let $G$ be an abelian group and $A$ a
finite subset of $G$, and let $\mathcal{T}(A)$ be the set of combinations $\sum_{y \in A} c_y y$
in which every integer coefficient $c_y$ is $0$ or odd. Every $x \in A$ lies in $\mathcal{T}(A)$:
take $c_x = 1$ and $c_y = 0$ for $y \neq x$.

## Sources

- John Greene and Clayton Higgins, *Maximal Subset Sums in a Group of Order a Power of 2*, Journal of Integer Sequences 28 (2025), Article 25.7.8, Section 3 (the operator `𝒯`).

Formalized by `MetaMathlibExt.PerfectSubsetSumCover.mem_oddCombinations_of_mem`, a theorem declared in [WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/perfect-subset-sum-covers-of-abelian-2-groups/index.html#mem-odd-combinations-of-mem).

## Odd combinations of the empty set

Let $G$ be an abelian group and, for a finite
$A \subseteq G$, let $\mathcal{T}(A)$ be the set of combinations $\sum_{x \in A} c_x x$ in which
every integer coefficient $c_x$ is $0$ or odd. Then $\mathcal{T}(\emptyset) = \{0\}$.

## Sources

- John Greene and Clayton Higgins, *Maximal Subset Sums in a Group of Order a Power of 2*, Journal of Integer Sequences 28 (2025), Article 25.7.8, Section 3 (the operator `𝒯`).

Formalized by `MetaMathlibExt.PerfectSubsetSumCover.oddCombinations_empty`, a theorem declared in [WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/perfect-subset-sum-covers-of-abelian-2-groups/index.html#odd-combinations-empty).

## Existence of perfect covers

Every finite abelian group $G$ of order $2^n$ has a perfect
cover, and every nonzero $x \in G$ lies in some perfect cover of $G$.

## Sources

- John Greene and Clayton Higgins, *Maximal Subset Sums in a Group of Order a Power of 2*, Journal of Integer Sequences 28 (2025), Article 25.7.8, Theorem 1 (`jis-2025-25.7.8-thm-1`).

Stated but not proved: `MetaMathlibExt.exists_isPerfectCover_mem` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/perfect-subset-sum-covers-of-abelian-2-groups/index.html#exists-is-perfect-cover-mem).

## Number of perfect covers of a cyclic 2-group

For every $n \ge 0$, the cyclic group
$\mathbb{Z}_{2^n}$ has exactly $2^{n(n-1)/2}$ perfect covers.

## Sources

- John Greene and Clayton Higgins, *Maximal Subset Sums in a Group of Order a Power of 2*, Journal of Integer Sequences 28 (2025), Article 25.7.8, Theorem 2 (`jis-2025-25.7.8-thm-2`).

Stated but not proved: `MetaMathlibExt.count_zmod_two_pow` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/perfect-subset-sum-covers-of-abelian-2-groups/index.html#count-zmod-two-pow).

## Perfect covers of a product of two cyclic 2-groups

Write $C(K)$ for the number of
perfect covers of a group $K$, and $a_{m,n} = C(\mathbb{Z}_{2^m} \oplus \mathbb{Z}_{2^n})$.
For all $m \ge n \ge 1$,
$a_{m,n} = 2^{m+n-1} (a_{m-1,n} + 2 a_{m,n-1}) -
3 \cdot 2^{2m+2n-4} \, a_{m-1,n-1}$.
Moreover, for every $n \ge 0$ there is a polynomial $p$ of degree $n$ with rational coefficients
such that $a_{m,n} = 2^{(m-1)n} \, 2^{m(m-1)/2} \, p(m)$ for all $m \ge n$.

## Sources

- John Greene and Clayton Higgins, *Maximal Subset Sums in a Group of Order a Power of 2*, Journal of Integer Sequences 28 (2025), Article 25.7.8, Theorem 3 (`jis-2025-25.7.8-thm-3`).

Stated but not proved: `MetaMathlibExt.count_zmod_two_pow_prod_recurrence` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/perfect-subset-sum-covers-of-abelian-2-groups/index.html#count-zmod-two-pow-prod-recurrence).

## Perfect covers of $(\mathbb{Z}_2)^m \oplus \mathbb{Z}_{2^n}$

Write $C(K)$ for the number
of perfect covers of a group $K$, and for natural numbers $m$ and $n$ let
$b_{m,n} = C((\mathbb{Z}_2)^m \oplus \mathbb{Z}_{2^n})$. Then:
for every $m \ge 0$, $C((\mathbb{Z}_2)^m) \cdot m! = \prod_{i=0}^{m-1} (2^m - 2^i)$;
for all $m, n \ge 1$, writing $B_{m,k} = 2^m \prod_{i=0}^{k-1} (2^m - 2^i) / (k+1)!$ for
$1 \le k \le m$, we have $b_{m,n} = 2^{m+n-1} b_{m,n-1} +
\sum_{k=1}^{m} B_{m,k} \, 2^{k(m-k)} \, 2^{(k+1)(n-1)} \, b_{m-k,n-1}$;
and for every $m \ge 0$ there is a polynomial $q$ of degree $m$ with rational coefficients such
that $b_{m,n} = 2^{m(n-1)} \, 2^{n(n-1)/2} \, q(n)$ for all $n \ge 0$, where the power
$2^{m(n-1)}$ has an integer exponent (it is $2^{-m}$ at $n = 0$).

## Sources

- John Greene and Clayton Higgins, *Maximal Subset Sums in a Group of Order a Power of 2*, Journal of Integer Sequences 28 (2025), Article 25.7.8, Theorem 4 (`jis-2025-25.7.8-thm-4`).

Stated but not proved: `MetaMathlibExt.count_elementary_prod_zmod_two_pow` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/perfect-subset-sum-covers-of-abelian-2-groups/index.html#count-elementary-prod-zmod-two-pow).

## Perfect covers of a cyclic 2-group times a cyclic group of order 2, 4 or 8

Write
$C(K)$ for the number of perfect covers of a group $K$. For every $n \ge 0$,
$C(\mathbb{Z}_{2^n} \oplus \mathbb{Z}_2) = 2^{n-1} \, 2^{n(n-1)/2} \, (n + 2)$, where $2^{n-1}$
is an integer power of $2$ (equal to $1/2$ at $n = 0$). For every $n \ge 1$,
$C(\mathbb{Z}_{2^n} \oplus \mathbb{Z}_4) = 2^{2n-2} \, 2^{n(n-1)/2} \, (n^2 + 11n + 4)$.
For every $n \ge 2$,
$C(\mathbb{Z}_{2^n} \oplus \mathbb{Z}_8) =
2^{3n-3} \, 2^{n(n-1)/2} \, (4n^3 + 108n^2 + 512n - 384)/3$.

## Sources

- John Greene and Clayton Higgins, *Maximal Subset Sums in a Group of Order a Power of 2*, Journal of Integer Sequences 28 (2025), Article 25.7.8, Corollary 25 (`jis-2025-25.7.8-cor-25`). The record gives no range; the second identity fails at `n = 0` (`C(ℤ₄) = 2`, formula `1`) and the third at `n = 0, 1` (`C(ℤ₈) = 8`, formula `-16`; `C(ℤ₂ ⊕ ℤ₈) = 160`, formula `80`), matching Theorem 3's range `m ≥ n`.

Stated but not proved: `MetaMathlibExt.count_zmod_two_pow_prod_small_special` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/perfect-subset-sum-covers-of-abelian-2-groups/index.html#count-zmod-two-pow-prod-small-special).

## Perfect covers of an elementary abelian group of order 4 or 8 times a cyclic 2-group

Write $C(K)$ for the number of perfect covers of a group $K$. For every $n \ge 0$,
$C((\mathbb{Z}_2)^2 \oplus \mathbb{Z}_{2^n}) = 2^{2n-2} \, 2^{n(n-1)/2} \, (3n^2 + 13n + 12)$
and
$C((\mathbb{Z}_2)^3 \oplus \mathbb{Z}_{2^n}) =
2^{3n-3} \, 2^{n(n-1)/2} \, (28n^3 + 196n^2 + 392n + 224)$,
where $2^{2n-2}$ and $2^{3n-3}$ are integer powers of $2$ (fractional at $n = 0$).

## Sources

- John Greene and Clayton Higgins, *Maximal Subset Sums in a Group of Order a Power of 2*, Journal of Integer Sequences 28 (2025), Article 25.7.8, Corollary 26 (`jis-2025-25.7.8-cor-26`). The record's third identity, for `(ℤ₂)^4 ⊕ ℤ_{2^n}`, is omitted: it fails as printed at `n = 1` (`C((ℤ₂)^5) = 83328`, formula `72328`).

Stated but not proved: `MetaMathlibExt.count_elementary_two_three_prod_zmod` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/perfect-subset-sum-covers-of-abelian-2-groups/index.html#count-elementary-two-three-prod-zmod).

## Adjoining an element doubles the multiplicity of a perfect cover

Let $G$ be an abelian
group and let $s = (s_1, \dots, s_k)$ be a perfect $m$-cover of $G$. For every $g \in G$, the
family $(g, s_1, \dots, s_k)$ is a perfect $2m$-cover of $G$.

## Sources

- John Greene and Clayton Higgins, *Maximal Subset Sums in a Group of Order a Power of 2*, Journal of Integer Sequences 28 (2025), Article 25.7.8, Lemma 5 (`jis-2025-25.7.8-lem-5`).

Stated but not proved: `MetaMathlibExt.isPerfectMCover_cons` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/perfect-subset-sum-covers-of-abelian-2-groups/index.html#is-perfect-mcover-cons).

## Projections of a perfect cover of a direct sum

Let $H$ and $K$ be finite abelian groups
with $|H| = 2^m$ and $|K| = 2^n$, and let $s = (s_i)_{i \in \iota}$, indexed by a finite set
$\iota$, be a perfect $l$-cover of $H \oplus K$. Then the first coordinates of the $s_i$ form a
perfect $2^n l$-cover of $H$, and the second coordinates form a perfect $2^m l$-cover of $K$.

## Sources

- John Greene and Clayton Higgins, *Maximal Subset Sums in a Group of Order a Power of 2*, Journal of Integer Sequences 28 (2025), Article 25.7.8, Lemma 6 (`jis-2025-25.7.8-lem-6`).

Stated but not proved: `MetaMathlibExt.isPerfectMCover_fst_snd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean, line 266](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean#L266). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/perfect-subset-sum-covers-of-abelian-2-groups/index.html#is-perfect-mcover-fst-snd).

## Removing one element from a perfect cover

Let $G$ be a finite abelian group of order $2^n$,
let $S$ be a perfect cover of $G$, let $z \in S$ and let $S_1 = S \setminus \{z\}$. Then (a) every
element of $G$ is the sum of at most one subset of $S_1$, and exactly half of the $2^n$ elements
of $G$ are the sum of a subset of $S_1$; (b) if $g \in G$ is the sum of a subset of $S_1$ and $j$
is an integer with $j \ge 1$, then $g + 2jz$ is the sum of a subset of $S_1$ and $g + (2j-1)z$ is
not.

## Sources

- John Greene and Clayton Higgins, *Maximal Subset Sums in a Group of Order a Power of 2*, Journal of Integer Sequences 28 (2025), Article 25.7.8, Lemma 7 (`jis-2025-25.7.8-lem-7`).

Stated but not proved: `MetaMathlibExt.perfectCover_erase_coverCount` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean, line 281](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean#L281). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/perfect-subset-sum-covers-of-abelian-2-groups/index.html#perfect-cover-erase-cover-count).

## Removing the last element of a perfect $2^j$-cover

Let $G$ be an abelian group, let
$s = (x_1, \dots, x_{k+1})$ be a family in $G$ that is a perfect $2^j$-cover of $G$, and let
$S_1 = (x_1, \dots, x_k)$. For every $a \in G$, if $S_1$ covers $a$ exactly $c$ times, then
$S_1$ covers $a + x_{k+1}$ exactly $2^j - c$ times.

## Sources

- John Greene and Clayton Higgins, *Maximal Subset Sums in a Group of Order a Power of 2*, Journal of Integer Sequences 28 (2025), Article 25.7.8, Lemma 8 (`jis-2025-25.7.8-lem-8`). The paper's `|G| = 2^n` and `k + 1 = j + n` are not needed.

Stated but not proved: `MetaMathlibExt.coverCount_init_add_last` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/perfect-subset-sum-covers-of-abelian-2-groups/index.html#cover-count-init-add-last).

## Shifting by multiples of the last element of a perfect $2^j$-cover

Let $G$ be an
abelian group, let $s = (x_1, \dots, x_{k+1})$ be a family in $G$ that is a perfect $2^j$-cover
of $G$, and let $S_1 = (x_1, \dots, x_k)$. For every $b \in G$, if $S_1$ covers $b$ exactly $c$
times, then for every integer $t$ it covers $b + 2t\,x_{k+1}$ exactly $c$ times and
$b + (2t + 1)\,x_{k+1}$ exactly $2^j - c$ times.

## Sources

- John Greene and Clayton Higgins, *Maximal Subset Sums in a Group of Order a Power of 2*, Journal of Integer Sequences 28 (2025), Article 25.7.8, Corollary 9 (`jis-2025-25.7.8-cor-9`). `t` ranges over `ℤ`.

Stated but not proved: `MetaMathlibExt.coverCount_init_add_zsmul_last` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean, line 309](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean#L309). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/perfect-subset-sum-covers-of-abelian-2-groups/index.html#cover-count-init-add-zsmul-last).

## Odd multiples and replacement in perfect covers

Let $G$ be a finite abelian group of order
$2^n$ and let $a, b \in G$ be nonzero. Then $b = (2j+1)a$ for some integer $j$ if and only if, for
every perfect cover $S$ of $G$ with $a \in S$, the set $(S \setminus \{a\}) \cup \{b\}$ is again a
perfect cover of $G$. If moreover $a \ne b$, then $b = (2j+1)a$ for some integer $j$ if and only if
no perfect cover of $G$ contains both $a$ and $b$.

## Sources

- John Greene and Clayton Higgins, *Maximal Subset Sums in a Group of Order a Power of 2*, Journal of Integer Sequences 28 (2025), Article 25.7.8, Theorem 10 (`jis-2025-25.7.8-thm-10`). `a, b ≠ 0` added and `a ≠ b` added for (3): for `a = 0, b ≠ 0` conditions (2) and (3) hold vacuously while (1) fails, and for `a = b ≠ 0` condition (3) fails (Theorem 1 puts `a` in a perfect cover) while (1) holds.

Stated but not proved: `MetaMathlibExt.oddMultiple_iff_perfectCover_replace` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean, line 327](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean#L327). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/perfect-subset-sum-covers-of-abelian-2-groups/index.html#odd-multiple-iff-perfect-cover-replace).

## Replacing an entry of a perfect $2^k$-cover by an odd multiple

Let $G$ be an abelian
group, let $k$ and $N$ be natural numbers, and let $a, b, s_1, \dots, s_N \in G$. If the family
$(a, s_1, \dots, s_N)$ is a perfect $2^k$-cover of $G$ and $b = (2j + 1)a$ for some integer $j$,
then the family $(b, s_1, \dots, s_N)$ is also a perfect $2^k$-cover of $G$.

## Sources

- John Greene and Clayton Higgins, *Maximal Subset Sums in a Group of Order a Power of 2*, Journal of Integer Sequences 28 (2025), Article 25.7.8, Lemma 11 (`jis-2025-25.7.8-lem-11`). The paper's `|G| = 2^n` and length `n + k` are not needed.

Stated but not proved: `MetaMathlibExt.isPerfectMCover_cons_oddMultiple` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean, line 341](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean#L341). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/perfect-subset-sum-covers-of-abelian-2-groups/index.html#is-perfect-mcover-cons-odd-multiple).

## Which families are perfect $m$-covers of $\mathbb{Z}_{2^n}$

Let $s = (s_i)_{i \in \iota}$
be a family in $\mathbb{Z}_{2^n}$ indexed by a finite type $\iota$ (a colored multiset). Then $s$
is a perfect $m$-cover of $\mathbb{Z}_{2^n}$ for some $m$ if and only if for every $j$ with
$1 \le j \le n$ some $s_i$ has additive order $2^j$.

## Sources

- John Greene and Clayton Higgins, *Maximal Subset Sums in a Group of Order a Power of 2*, Journal of Integer Sequences 28 (2025), Article 25.7.8, Theorem 12 (`jis-2025-25.7.8-thm-12`). The multiplicity `m` is existentially quantified.

Stated but not proved: `MetaMathlibExt.exists_isPerfectMCover_zmod_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean, line 353](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean#L353). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/perfect-subset-sum-covers-of-abelian-2-groups/index.html#exists-is-perfect-mcover-zmod-iff).

## Perfect $m$-covers of $\mathbb{Z}_{2^n}$ contain perfect covers

Let
$s = (s_i)_{i \in \iota}$ be a family in $\mathbb{Z}_{2^n}$ indexed by a finite type $\iota$. If
$s$ is a perfect $m$-cover of $\mathbb{Z}_{2^n}$, then there is a finite set $T \subseteq \iota$
such that the subfamily $(s_i)_{i \in T}$ is a perfect $1$-cover of $\mathbb{Z}_{2^n}$.

## Sources

- John Greene and Clayton Higgins, *Maximal Subset Sums in a Group of Order a Power of 2*, Journal of Integer Sequences 28 (2025), Article 25.7.8, Corollary 13 (`jis-2025-25.7.8-cor-13`).

Stated but not proved: `MetaMathlibExt.exists_perfectCover_subfamily_zmod` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean, line 364](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean#L364). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/perfect-subset-sum-covers-of-abelian-2-groups/index.html#exists-perfect-cover-subfamily-zmod).

## Orders of second coordinates in perfect $m$-covers

Let $H$ be a finite abelian group of
order $2^r$ and let $s = (s_i)_{i \in \iota}$ be a family in $H \oplus \mathbb{Z}_{2^n}$ indexed by
a finite type $\iota$. If $s$ is a perfect $m$-cover of $H \oplus \mathbb{Z}_{2^n}$, then for
every $j$ with $1 \le j \le n$ the second coordinate of some $s_i$ has additive order $2^j$.

## Sources

- John Greene and Clayton Higgins, *Maximal Subset Sums in a Group of Order a Power of 2*, Journal of Integer Sequences 28 (2025), Article 25.7.8, Corollary 14 (`jis-2025-25.7.8-cor-14`). The family has any finite index type (the record reuses `n` for its length).

Stated but not proved: `MetaMathlibExt.exists_snd_addOrderOf_of_isPerfectMCover` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean, line 375](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean#L375). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/perfect-subset-sum-covers-of-abelian-2-groups/index.html#exists-snd-add-order-of-of-is-perfect-mc).

## Odd combinations of disjoint parts of a perfect cover

Let $G$ be an abelian group of
order $2^n$ and $S$ a perfect cover of $G$. For a finite $A \subseteq G$, let $\mathcal{T}(A)$ be
the set of combinations $\sum_{x \in A} c_x x$ in which every integer coefficient $c_x$ is $0$
or odd. Then: (a) for disjoint $A, B \subseteq S$, $\mathcal{T}(A) \cap \mathcal{T}(B) = \{0\}$;
(b) if $A \subseteq S$ and $s \in S \setminus A$, then $s \notin \mathcal{T}(A)$.

## Sources

- John Greene and Clayton Higgins, *Maximal Subset Sums in a Group of Order a Power of 2*, Journal of Integer Sequences 28 (2025), Article 25.7.8, Theorem 15 (a), (b) (`jis-2025-25.7.8-thm-15`).

Stated but not proved: `MetaMathlibExt.oddCombinations_inter_of_isPerfectCover` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean, line 386](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean#L386). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/perfect-subset-sum-covers-of-abelian-2-groups/index.html#odd-combinations-inter-of-is-perfect-cov).

## Odd combinations are closed under odd multiples

Let $A$ be a finite subset of an abelian
group $G$. If $g$ lies in the set $\mathcal{T}(A)$ of odd combinations of $A$, then
$(2j+1)g \in \mathcal{T}(A)$ for every integer $j$.

## Sources

- John Greene and Clayton Higgins, *Maximal Subset Sums in a Group of Order a Power of 2*, Journal of Integer Sequences 28 (2025), Article 25.7.8, Theorem 15 (c) (`jis-2025-25.7.8-thm-15`). "Union of equivalence classes" is stated as closure under odd multiples (`0 ∈ 𝒯(A)` is `zero_mem_oddCombinations`).

Stated but not proved: `MetaMathlibExt.zsmul_mem_oddCombinations` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean, line 400](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean#L400). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/perfect-subset-sum-covers-of-abelian-2-groups/index.html#zsmul-mem-odd-combinations).

## Distinct subset sums from the odd-combination condition

Let $G$ be an abelian group,
and for a finite set $A \subseteq G$ write $\mathcal{T}(A)$ for the set of odd combinations of
$A$. Let $x = (x_1, \dots, x_m)$ be a family in $G$ such that
$x_i \notin \mathcal{T}(\{x_1, \dots, x_{i-1}\})$ for every $i$ (for $i = 1$ this says
$x_1 \ne 0$, and for $i \ge 2$ it forces $x_i \ne 0$). Then $x$ covers every element of $G$ at
most once, that is, all subset sums of $x$ are distinct; if moreover $|G| = 2^m$, then $x$ is a
perfect $1$-cover of $G$.

## Sources

- John Greene and Clayton Higgins, *Maximal Subset Sums in a Group of Order a Power of 2*, Journal of Integer Sequences 28 (2025), Article 25.7.8, Lemma 16 (`jis-2025-25.7.8-lem-16`). The paper's "nonzero" hypothesis is the `i = 1` case of `hx`; distinctness needs no finiteness, and "`m = n`" is `Nat.card G = 2 ^ m`.

Stated but not proved: `MetaMathlibExt.coverCount_le_one_of_not_mem_oddCombinations` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean, line 412](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean#L412). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/perfect-subset-sum-covers-of-abelian-2-groups/index.html#cover-count-le-one-of-not-mem-odd-combin).

## Perfect covers containing a perfect cover of a subgroup

Let $G$ be an abelian group of
order $2^n$ and $H$ a subgroup of order $2^m$. Then the number of perfect covers of $G$ that
contain a perfect cover of $H$ is $2^{m(n-m)} \cdot C(G/H) \cdot C(H)$, where $C(K)$ denotes the
number of perfect covers of a group $K$.

## Sources

- John Greene and Clayton Higgins, *Maximal Subset Sums in a Group of Order a Power of 2*, Journal of Integer Sequences 28 (2025), Article 25.7.8, Lemma 17 (`jis-2025-25.7.8-lem-17`).

Stated but not proved: `MetaMathlibExt.card_perfectCover_superset_subgroup` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean, line 423](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean#L423). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/perfect-subset-sum-covers-of-abelian-2-groups/index.html#card-perfect-cover-superset-subgroup).

## Elements of order two among odd combinations of part of a perfect cover

Let $G$ be an
abelian group of order $2^n$, let $S$ be a perfect cover of $G$, and let $A \subseteq S$ contain
no element of order $2$. Let $\mathcal{T}(A)$ be the set of combinations $\sum_{x \in A} c_x x$ in
which every integer coefficient $c_x$ is $0$ or odd. Then $\mathcal{T}(A)$ does not contain
exactly one element of order $2$: it contains none or at least two.

## Sources

- John Greene and Clayton Higgins, *Maximal Subset Sums in a Group of Order a Power of 2*, Journal of Integer Sequences 28 (2025), Article 25.7.8, Lemma 18 (`jis-2025-25.7.8-lem-18`). "No elements of order `2`, or at least two" is stated as "not exactly one".

Stated but not proved: `MetaMathlibExt.not_existsUnique_addOrderOf_two_mem_oddCombinations` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean, line 437](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean#L437). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/perfect-subset-sum-covers-of-abelian-2-groups/index.html#not-exists-unique-add-order-of-two-mem-o).

## Elements of order $2$ in perfect covers of $\mathbb{Z}_{2^m} \oplus \mathbb{Z}_{2^n}$

Let $m, n$ be natural numbers with $m + n > 0$. Every perfect cover of
$\mathbb{Z}_{2^m} \oplus \mathbb{Z}_{2^n}$ contains an element of order $2$.

## Sources

- John Greene and Clayton Higgins, *Maximal Subset Sums in a Group of Order a Power of 2*, Journal of Integer Sequences 28 (2025), Article 25.7.8, Lemma 19 (`jis-2025-25.7.8-lem-19`). Hypothesis `0 < m + n` added: the trivial group's perfect cover is empty.

Stated but not proved: `MetaMathlibExt.exists_addOrderOf_eq_two_of_isPerfectCover` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean, line 449](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean#L449). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/perfect-subset-sum-covers-of-abelian-2-groups/index.html#exists-add-order-of-eq-two-of-is-perfect).

## Perfect covers with a prescribed number of odd last coordinates

Let $H$ be a finite
abelian group of order $2^m$, let $n \ge 1$, and let $G = H \oplus \mathbb{Z}_{2^n}$. For every
$k$ with $1 \le k \le m + 1$, some perfect cover $S$ of $G$ has exactly $k$ elements $(h, y)$
whose coordinate $y \in \mathbb{Z}_{2^n}$ is odd.

## Sources

- John Greene and Clayton Higgins, *Maximal Subset Sums in a Group of Order a Power of 2*, Journal of Integer Sequences 28 (2025), Article 25.7.8, Lemma 20 (`jis-2025-25.7.8-lem-20`). The setting `G = H ⊕ ℤ_{2^n}`, `|H| = 2^m`, is the one fixed before the lemma in Section 5; `y` odd means `y.val` odd; `n ≥ 1` added (for `n = 0` no `y` is odd).

Stated but not proved: `MetaMathlibExt.exists_isPerfectCover_card_odd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean, line 461](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean#L461). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/perfect-subset-sum-covers-of-abelian-2-groups/index.html#exists-is-perfect-cover-card-odd).

## Perfect covers with exactly one odd element

Let $H$ be an abelian group of order $2^m$,
let $n \ge 1$ and let $G = H \oplus \mathbb{Z}_{2^n}$. Call an element of $G$ odd when its
$\mathbb{Z}_{2^n}$-coordinate, taken as a representative in $\{0, 1, \dots, 2^n - 1\}$, is odd.
Then the number of perfect covers of $G$ with exactly one odd element is
$2^m \cdot 2^{n-1} \cdot C(H \oplus \mathbb{Z}_{2^{n-1}})$, where $C(K)$ denotes the number of
perfect covers of a group $K$.

## Sources

- John Greene and Clayton Higgins, *Maximal Subset Sums in a Group of Order a Power of 2*, Journal of Integer Sequences 28 (2025), Article 25.7.8, Lemma 21 (`jis-2025-25.7.8-lem-21`). "`y_1` odd, all other `y_i` even" is read as "exactly one odd `y`" for the unordered set; `y` odd means `y.val` odd; `n ≥ 1` added (`ℤ_{2^{n-1}}`).

Stated but not proved: `MetaMathlibExt.card_perfectCover_one_odd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean, line 473](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean#L473). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/perfect-subset-sum-covers-of-abelian-2-groups/index.html#card-perfect-cover-one-odd).

## Spans of the odd and even entries of a perfect cover

Let $m$, $n$ and $k$ be natural
numbers with $k + 1 \le m + n$, and let $s = (s_1, \dots, s_{m+n})$, $s_i = (x_i, y_i)$, be a
family in $(\mathbb{Z}_2)^m \oplus \mathbb{Z}_{2^n}$ that is a perfect $1$-cover: every element of
the group is the sum of the $s_i$ over exactly one set of indices. Suppose that $y_i$, read as an
integer in $\{0, \dots, 2^n - 1\}$, is odd exactly when $i \le k + 1$. Let $U$ be the
$\mathbb{Z}_2$-span of $x_1 + x_2, \dots, x_1 + x_{k+1}$ and $V$ the $\mathbb{Z}_2$-span of
$x_{k+2}, \dots, x_{m+n}$ in $(\mathbb{Z}_2)^m$. Then $\dim U = k$, $\dim V = m - k$,
$U \cap V = 0$ and $U + V = (\mathbb{Z}_2)^m$.

## Sources

- John Greene and Clayton Higgins, *Maximal Subset Sums in a Group of Order a Power of 2*, Journal of Integer Sequences 28 (2025), Article 25.7.8, Lemma 23 (`jis-2025-25.7.8-lem-23`). Indices are `0`-based (`i < k + 1` are the odd ones, and `k + 1 ≤ m + n` makes `y_1, …, y_{k+1}` exist); the perfect cover is an indexed family (perfect covers have distinct entries); `(ℤ₂)^m = U ⊕ V` is stated as `U ⊔ V = ⊤`.

Stated but not proved: `MetaMathlibExt.perfectCover_odd_even_span` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean, line 489](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean#L489). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/perfect-subset-sum-covers-of-abelian-2-groups/index.html#perfect-cover-odd-even-span).

## The even tail of a perfect cover

Let $s = (s_1, \dots, s_{m+n})$, $s_i = (x_i, y_i)$, be a
family in $(\mathbb{Z}_2)^m \oplus \mathbb{Z}_{2^n}$ that is a perfect $1$-cover: every element of
the group is the sum of the $s_i$ over exactly one set of indices. Let $k + 1 \le m + n$ and suppose
that $y_i$, read as an integer in $\{0, \dots, 2^n - 1\}$, is odd exactly when $i \le k + 1$. Let
$V$ be the $\mathbb{Z}_2$-span of $x_{k+2}, \dots, x_{m+n}$ in $(\mathbb{Z}_2)^m$. Then every
$(x, y)$ with $x \in V$ and $y$ even (again read in $\{0, \dots, 2^n - 1\}$) is the sum of the
$s_i$ over exactly one set of indices taken from $\{k+2, \dots, m+n\}$.

## Sources

- John Greene and Clayton Higgins, *Maximal Subset Sums in a Group of Order a Power of 2*, Journal of Integer Sequences 28 (2025), Article 25.7.8, Lemma 24 (`jis-2025-25.7.8-lem-24`). The family's elements lie in `V ⊕ 2ℤ_{2^n}` by hypothesis and by definition of `V`; only the covering statement is stated.

Stated but not proved: `MetaMathlibExt.perfectCover_even_tail_coverCount` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean, line 505](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/PerfectSubsetSumCoverWanted.lean#L505). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/perfect-subset-sum-covers-of-abelian-2-groups/index.html#perfect-cover-even-tail-cover-count).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Perfect subset-sum covers of abelian 2-groups](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/perfect-subset-sum-covers-of-abelian-2-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/perfect-subset-sum-covers-of-abelian-2-groups)
