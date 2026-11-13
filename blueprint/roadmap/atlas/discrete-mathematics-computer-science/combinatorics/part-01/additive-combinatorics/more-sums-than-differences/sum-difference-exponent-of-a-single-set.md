---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.SingleSetSumDifferenceExponentWanted.IsAdmissibleExponent, MathlibExt.Combinatorics.SingleSetSumDifferenceExponentWanted.singleSetSumDifferenceExponent, MathlibExt.Combinatorics.SingleSetSumDifferenceExponentWanted.singleSetSumDifferenceExponent_eq_two, MathlibExt.Combinatorics.SingleSetSumDifferenceExponentWanted.singleSetSumDifferenceExponent_eq_two_holds
statement: formalized
---

# Sum-difference exponent of a single set

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/sum-difference-exponent-of-a-single-set/index.html).

## Admissible exponents for sums and differences

A real number $\theta$ is an admissible
exponent when every nonempty finite set $A$ of integers satisfies
$|A+A|/|A| \le (|A-A|/|A|)^{\theta}$, where $A+A$ and $A-A$ are the sumset and the difference
set of $A$.

Formalized by `MathlibExt.Combinatorics.SingleSetSumDifferenceExponentWanted.IsAdmissibleExponent`, a definition declared in [WantedExt/Combinatorics/SingleSetSumDifferenceExponentWanted.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SingleSetSumDifferenceExponentWanted.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/sum-difference-exponent-of-a-single-set/index.html#is-admissible-exponent).

## The single-set sum-difference exponent

The single-set sum-difference exponent $C_{3d}$ is
the infimum of the admissible exponents, that is, of the set of real numbers $\theta$ such that
$|A+A|/|A| \le (|A-A|/|A|)^{\theta}$ for every nonempty finite set $A$ of integers, where $A+A$
and $A-A$ are the sumset and the difference set of $A$.

This is the source's equivalent formulation of $C_{3d}$ as a least admissible exponent, over
finite sets of integers.

Formalized by `MathlibExt.Combinatorics.SingleSetSumDifferenceExponentWanted.singleSetSumDifferenceExponent`, a definition declared in [WantedExt/Combinatorics/SingleSetSumDifferenceExponentWanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SingleSetSumDifferenceExponentWanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/sum-difference-exponent-of-a-single-set/index.html#single-set-sum-difference-exponent).

## The proposition that the single-set sum-difference exponent equals 2

This is the
statement that the single-set sum-difference exponent $C_{3d}$ is equal to $2$.

Formalized by `MathlibExt.Combinatorics.SingleSetSumDifferenceExponentWanted.singleSetSumDifferenceExponent_eq_two`, a definition declared in [WantedExt/Combinatorics/SingleSetSumDifferenceExponentWanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SingleSetSumDifferenceExponentWanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/sum-difference-exponent-of-a-single-set/index.html#single-set-sum-difference-exponent-eq-tw).

## The single-set sum-difference exponent equals 2

The single-set sum-difference exponent
$C_{3d}$ is equal to $2$.

Known constructions approach this value but do not attain it.

## Sources

- Haowei Lin and Shanda Li, Settling the optimal exponent relating sumsets and difference sets, arXiv:2607.27199v1 (2026), https://arxiv.org/abs/2607.27199v1.

Stated but not proved: `MathlibExt.Combinatorics.SingleSetSumDifferenceExponentWanted.singleSetSumDifferenceExponent_eq_two_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/SingleSetSumDifferenceExponentWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SingleSetSumDifferenceExponentWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/sum-difference-exponent-of-a-single-set/index.html#single-set-sum-difference-exponent-eq-tw-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sum-difference exponent of a single set](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/sum-difference-exponent-of-a-single-set/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/sum-difference-exponent-of-a-single-set)
