---
declaration: section
origin: cited
lean: MetaMathlibExt.card_add_le_card_sub_of_card_lt_six, MetaMathlibExt.no_small_sum_dominant
statement: formalized
proof: formalized
---

# Minimum size of a sum-dominant set

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/minimum-size-of-a-sum-dominant-set/index.html).

## Chu's theorem for arbitrary finite sets of integers

Let $A$ be a finite set of integers with
$|A| < 6$. Then $|A + A| \le |A - A|$, where $A + A = \{a + b : a, b \in A\}$ is the sumset and
$A - A = \{a - b : a, b \in A\}$ is the difference set of $A$.

This is Chu's theorem without the assumption that the elements of $A$ are nonnegative.

Formalized by `MetaMathlibExt.card_add_le_card_sub_of_card_lt_six`, a theorem declared in [MathlibExt/Combinatorics/Additive/NoSmallSumDominantSet.lean, line 1116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Additive/NoSmallSumDominantSet.lean#L1116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/minimum-size-of-a-sum-dominant-set/index.html#card-add-le-card-sub-of-card-lt-six).

## Chu's theorem: sets with fewer than six elements are not sum-dominant

Let $A$ be a finite
set of nonnegative integers with $|A| < 6$. Then $|A + A| \le |A - A|$, where
$A + A = \{a + b : a, b \in A\}$ is the sumset and $A - A = \{a - b : a, b \in A\}$ is the
difference set of $A$; that is, $A$ is not sum-dominant.

The nonnegativity assumption follows the source's normalization and is not needed: the same
bound holds for every finite set of integers with fewer than six elements.

## Sources

- Hùng Việt Chu, "When Sets Are Not Sum-Dominant," Journal of Integer Sequences 22 (2019), Article 19.3.7, Theorem, lines 126–128, https://cs.uwaterloo.ca/journals/JIS/VOL22/Chu/chu5.tex

Formalized by `MetaMathlibExt.no_small_sum_dominant`, a theorem declared in [MathlibExt/Combinatorics/Additive/NoSmallSumDominantSet.lean, line 1140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Additive/NoSmallSumDominantSet.lean#L1140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/minimum-size-of-a-sum-dominant-set/index.html#no-small-sum-dominant).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Minimum size of a sum-dominant set](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/minimum-size-of-a-sum-dominant-set/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/minimum-size-of-a-sum-dominant-set)
