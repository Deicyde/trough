---
declaration: section
origin: cited
lean: MetaMathlibExt.IsMPTQSet, MetaMathlibExt.not_isMPTQSet_singleton, MetaMathlibExt.not_isMPTQSet_of_zero_mem, MetaMathlibExt.not_isMSTDSet_int_of_card_eq_seven, MetaMathlibExt.isMSTDSet_int_of_card_eq_eight_iff, MetaMathlibExt.eight_le_card_of_isMPTQSet_of_pos, MetaMathlibExt.five_le_card_of_isMPTQSet_of_neg, MetaMathlibExt.not_isMPTQSet_insert_of_le
statement: formalized
---

# Sets with more products than quotients

15 results, 3 proved and 12 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/sets-with-more-products-than-quotients/index.html).

## MPTQ set

A finite set $A$ of real numbers is an MPTQ (more products than quotients) set
when $0 \notin A$ and $|A/A| < |A \cdot A|$, where $A \cdot A = \{ab : a, b \in A\}$ is the
product set, $A/A = \{a/b : a, b \in A\}$ is the quotient set, and $|X|$ is the number of
elements of $X$.

## Sources

- Anupriya Shetty and B. R. Shankar, *On The Minimum Cardinality of MPTQ Sets*, INTEGERS 24 (2024), Article A96, Definition 1.

Formalized by `MetaMathlibExt.IsMPTQSet`, a definition declared in [WantedExt/Combinatorics/Additive/MPTQSetsWanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/MPTQSetsWanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/sets-with-more-products-than-quotients/index.html#is-mptqset).

## A singleton is not an MPTQ set

For every real number $a$, the one-element set $\{a\}$
is not an MPTQ set.

## Sources

- Anupriya Shetty and B. R. Shankar, *On The Minimum Cardinality of MPTQ Sets*, INTEGERS 24 (2024), Article A96, Definition 1.

Formalized by `MetaMathlibExt.not_isMPTQSet_singleton`, a theorem declared in [WantedExt/Combinatorics/Additive/MPTQSetsWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/MPTQSetsWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/sets-with-more-products-than-quotients/index.html#not-is-mptqset-singleton).

## Sets containing zero are not MPTQ sets

If $A$ is a finite set of real numbers with
$0 \in A$, then $A$ is not an MPTQ set.

## Sources

- Anupriya Shetty and B. R. Shankar, *On The Minimum Cardinality of MPTQ Sets*, INTEGERS 24 (2024), Article A96, Definition 1.

Formalized by `MetaMathlibExt.not_isMPTQSet_of_zero_mem`, a theorem declared in [WantedExt/Combinatorics/Additive/MPTQSetsWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/MPTQSetsWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/sets-with-more-products-than-quotients/index.html#not-is-mptqset-of-zero-mem).

## Hegarty: no seven-element MSTD set of integers

No set of seven integers, viewed as a set
of real numbers, is an MSTD set.

## Sources

- Anupriya Shetty and B. R. Shankar, *On The Minimum Cardinality of MPTQ Sets*, INTEGERS 24 (2024), Article A96, Theorem 1.

Stated but not proved: `MetaMathlibExt.not_isMSTDSet_int_of_card_eq_seven` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/MPTQSetsWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/MPTQSetsWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/sets-with-more-products-than-quotients/index.html#not-is-mstdset-int-of-card-eq-seven).

## Hegarty's classification of MSTD sets of size eight

Let $A$ be a set of eight integers,
regarded as a set of real numbers, and let $S = \{0, 2, 3, 4, 7, 11, 12, 14\}$. Then $A$ is an
MSTD set if and only if $A = \{as + b : s \in S\}$ for some integers $a \neq 0$ and $b$.

## Sources

- Anupriya Shetty and B. R. Shankar, *On The Minimum Cardinality of MPTQ Sets*, INTEGERS 24 (2024), Article A96, Theorem 1.

Stated but not proved: `MetaMathlibExt.isMSTDSet_int_of_card_eq_eight_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/MPTQSetsWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/MPTQSetsWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/sets-with-more-products-than-quotients/index.html#is-mstdset-int-of-card-eq-eight-iff).

## Chu's bound for MPTQ sets of positive reals

Every MPTQ set whose elements are all
positive real numbers has at least $8$ elements.

## Sources

- Anupriya Shetty and B. R. Shankar, *On The Minimum Cardinality of MPTQ Sets*, INTEGERS 24 (2024), Article A96, Theorem 2.

Stated but not proved: `MetaMathlibExt.eight_le_card_of_isMPTQSet_of_pos` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/MPTQSetsWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/MPTQSetsWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/sets-with-more-products-than-quotients/index.html#eight-le-card-of-is-mptqset-of-pos).

## Chu's bound for MPTQ sets with a negative element

Every MPTQ set of real numbers that
contains a negative number has at least $5$ elements.

## Sources

- Anupriya Shetty and B. R. Shankar, *On The Minimum Cardinality of MPTQ Sets*, INTEGERS 24 (2024), Article A96, Theorem 2.

Stated but not proved: `MetaMathlibExt.five_le_card_of_isMPTQSet_of_neg` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/MPTQSetsWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/MPTQSetsWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/sets-with-more-products-than-quotients/index.html#five-le-card-of-is-mptqset-of-neg).

## Adjoining an element that adds no more products than quotients

Let $A$ be a finite set
of real numbers that is not an MPTQ set, let $x$ be a real number, let $n \le m$ be natural
numbers, and write $A' = A \cup \{x\}$. If $|A' \cdot A'| \le |A \cdot A| + n$ and
$|A/A| + m \le |A'/A'|$, where $X \cdot X$ and $X/X$ denote the product set and quotient set of
$X$, then $A'$ is not an MPTQ set.

## Sources

- Anupriya Shetty and B. R. Shankar, *On The Minimum Cardinality of MPTQ Sets*, INTEGERS 24 (2024), Article A96, Lemma 1.

Stated but not proved: `MetaMathlibExt.not_isMPTQSet_insert_of_le` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/MPTQSetsWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/MPTQSetsWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/sets-with-more-products-than-quotients/index.html#not-is-mptqset-insert-of-le).

## One equal pairing of products excludes the other two

Let $a$, $b$, $c$, $d$ be pairwise
distinct positive real numbers with $ab = cd$. Then $ad \neq bc$ and $ac \neq bd$.

## Sources

- Anupriya Shetty and B. R. Shankar, *On The Minimum Cardinality of MPTQ Sets*, INTEGERS 24 (2024), Article A96, Lemma 2.

Stated but not proved: `MetaMathlibExt.mul_ne_of_mul_eq_of_distinct` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/MPTQSetsWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/MPTQSetsWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/sets-with-more-products-than-quotients/index.html#mul-ne-of-mul-eq-of-distinct).

## At most one square is the product of the other two

Let $a$, $b$, $c$ be pairwise
distinct positive real numbers. Then at most one of the equations $a^2 = bc$, $b^2 = ac$ and
$c^2 = ab$ holds; that is, no two of them hold simultaneously.

## Sources

- Anupriya Shetty and B. R. Shankar, *On The Minimum Cardinality of MPTQ Sets*, INTEGERS 24 (2024), Article A96, Lemma 3.

Stated but not proved: `MetaMathlibExt.at_most_one_sq_eq_mul_of_distinct` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/MPTQSetsWanted.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/MPTQSetsWanted.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/sets-with-more-products-than-quotients/index.html#at-most-one-sq-eq-mul-of-distinct).

## Five-element sets with one negative element are not MPTQ sets

If $A$ is a set of five
real numbers exactly one of which is negative, then $A$ is not an MPTQ set.

The source assumes the elements are nonzero; this is not needed, since a set containing $0$ is
never an MPTQ set.

## Sources

- Anupriya Shetty and B. R. Shankar, *On The Minimum Cardinality of MPTQ Sets*, INTEGERS 24 (2024), Article A96, Lemma 4.

Stated but not proved: `MetaMathlibExt.not_isMPTQSet_of_card_five_one_neg` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/MPTQSetsWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/MPTQSetsWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/sets-with-more-products-than-quotients/index.html#not-is-mptqset-of-card-five-one-neg).

## Five-element sets with two negative elements are not MPTQ sets

If $A$ is a set of five
real numbers exactly two of which are negative, then $A$ is not an MPTQ set.

The source assumes the elements are nonzero; this is not needed, since a set containing $0$ is
never an MPTQ set.

## Sources

- Anupriya Shetty and B. R. Shankar, *On The Minimum Cardinality of MPTQ Sets*, INTEGERS 24 (2024), Article A96, Lemma 5.

Stated but not proved: `MetaMathlibExt.not_isMPTQSet_of_card_five_two_neg` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/MPTQSetsWanted.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/MPTQSetsWanted.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/sets-with-more-products-than-quotients/index.html#not-is-mptqset-of-card-five-two-neg).

## Adjoining negatives preserves the MPTQ property

Let $A$ be a finite set of positive real
numbers and $-A = \{-a : a \in A\}$. Then $A \cup (-A)$ is an MPTQ set if and only if $A$ is an
MPTQ set.

## Sources

- Anupriya Shetty and B. R. Shankar, *On The Minimum Cardinality of MPTQ Sets*, INTEGERS 24 (2024), Article A96, Proposition 1.

Stated but not proved: `MetaMathlibExt.isMPTQSet_union_neg_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/MPTQSetsWanted.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/MPTQSetsWanted.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/sets-with-more-products-than-quotients/index.html#is-mptqset-union-neg-iff).

## No MPTQ set has five elements

No set of five real numbers is an MPTQ set.

## Sources

- Anupriya Shetty and B. R. Shankar, *On The Minimum Cardinality of MPTQ Sets*, INTEGERS 24 (2024), Article A96, Theorem 3.

Stated but not proved: `MetaMathlibExt.not_isMPTQSet_of_card_eq_five` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/MPTQSetsWanted.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/MPTQSetsWanted.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/sets-with-more-products-than-quotients/index.html#not-is-mptqset-of-card-eq-five).

## Adjoining multiples by a coprime prime preserves the MPTQ property

Let $A$ be a finite
set of integers and $p$ a prime number such that every element of $A$ is coprime to $p$, and let
$pA = \{pa : a \in A\}$. Regarding sets of integers as sets of real numbers, $A \cup pA$ is an
MPTQ set if and only if $A$ is an MPTQ set.

## Sources

- Anupriya Shetty and B. R. Shankar, *On The Minimum Cardinality of MPTQ Sets*, INTEGERS 24 (2024), Article A96, Theorem 4.

Stated but not proved: `MetaMathlibExt.isMPTQSet_union_prime_mul_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/MPTQSetsWanted.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/MPTQSetsWanted.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/sets-with-more-products-than-quotients/index.html#is-mptqset-union-prime-mul-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sets with more products than quotients](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/sets-with-more-products-than-quotients/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/sets-with-more-products-than-quotients)
