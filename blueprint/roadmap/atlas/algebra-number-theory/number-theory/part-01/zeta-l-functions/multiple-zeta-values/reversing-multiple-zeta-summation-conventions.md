---
declaration: section
origin: cited
lean: MetaMathlibExt.MultipleZeta.Index.reverse, MetaMathlibExt.MultipleZeta.StrictIncreasingTuple, MetaMathlibExt.MultipleZeta.Index.IsIncreasingAdmissible, MetaMathlibExt.MultipleZeta.Index.isIncreasingAdmissible_iff_reverse_isAdmissible, MetaMathlibExt.MultipleZeta.Index.reverse_entry, MetaMathlibExt.MultipleZeta.increasingSummand, MetaMathlibExt.MultipleZeta.increasingValue, MetaMathlibExt.MultipleZeta.increasingEquivDecreasing
statement: formalized
proof: formalized
---

# Reversing multiple-zeta summation conventions

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/reversing-multiple-zeta-summation-conventions/index.html).

## Reversed index

The reverse of an index $(k_0, \dots, k_{d-1})$ is the index
$(k_{d-1}, \dots, k_0)$ with the same entries in the opposite order.

Formalized by `MetaMathlibExt.MultipleZeta.Index.reverse`, a definition declared in [MathlibExt/NumberTheory/MultipleZeta/Reversal.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/MultipleZeta/Reversal.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/reversing-multiple-zeta-summation-conventions/index.html#reverse).

## Strictly increasing tuples

For a natural number $d$, a strictly increasing tuple of
length $d$ is a tuple $(m_0, \dots, m_{d-1})$ of positive natural numbers with
$m_0 < m_1 < \cdots < m_{d-1}$. These are the summation variables of the increasing
multiple-zeta convention.

Formalized by `MetaMathlibExt.MultipleZeta.StrictIncreasingTuple`, an abbreviation declared in [MathlibExt/NumberTheory/MultipleZeta/Reversal.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/MultipleZeta/Reversal.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/reversing-multiple-zeta-summation-conventions/index.html#strict-increasing-tuple).

## Admissibility in the increasing convention

An index $(k_0, \dots, k_{d-1})$ is
admissible in the increasing convention when its list of entries read in reverse order,
$(k_{d-1}, \dots, k_0)$, is admissible: it is nonempty, its first element $k_{d-1}$ is at least
two, and its other elements are positive. Since the entries of an index are positive, this says
that the index is nonempty and its last entry is at least two.

This is the convention in arXiv:2304.08722 and arXiv:2608.10675.

Formalized by `MetaMathlibExt.MultipleZeta.Index.IsIncreasingAdmissible`, a definition declared in [MathlibExt/NumberTheory/MultipleZeta/Reversal.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/MultipleZeta/Reversal.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/reversing-multiple-zeta-summation-conventions/index.html#is-increasing-admissible).

## Increasing admissibility is admissibility of the reverse

An index is admissible in the
increasing convention (nonempty with last entry at least two) if and only if its reverse is
admissible (nonempty with first entry at least two).

Formalized by `MetaMathlibExt.MultipleZeta.Index.isIncreasingAdmissible_iff_reverse_isAdmissible`, a theorem declared in [MathlibExt/NumberTheory/MultipleZeta/Reversal.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/MultipleZeta/Reversal.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/reversing-multiple-zeta-summation-conventions/index.html#is-increasing-admissible-iff-reverse-is).

## Entries of the reversed index

Let $k = (k_0, \dots, k_{d-1})$ be an index of depth $d$;
its reverse also has depth $d$. For every $i < d$, the $i$-th entry of the reverse of $k$ is
$k_{d-1-i}$.

Formalized by `MetaMathlibExt.MultipleZeta.Index.reverse_entry`, a theorem declared in [MathlibExt/NumberTheory/MultipleZeta/Reversal.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/MultipleZeta/Reversal.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/reversing-multiple-zeta-summation-conventions/index.html#reverse-entry).

## Summand of the increasing multiple-zeta series

Let $k = (k_0, \dots, k_{d-1})$ be an
index of depth $d$. To a strictly increasing tuple $m = (m_0, \dots, m_{d-1})$ of positive
natural numbers it attaches the real number

$$\Bigl(\prod_{i=0}^{d-1} m_i^{k_i}\Bigr)^{-1}.$$

This is the convention in arXiv:2304.08722 and arXiv:2608.10675.

Formalized by `MetaMathlibExt.MultipleZeta.increasingSummand`, a definition declared in [MathlibExt/NumberTheory/MultipleZeta/Reversal.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/MultipleZeta/Reversal.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/reversing-multiple-zeta-summation-conventions/index.html#increasing-summand).

## Multiple zeta value in the increasing convention

Let $k = (k_0, \dots, k_{d-1})$ be an
index of depth $d$ that is admissible in the increasing convention. Its value in the increasing
convention is the real number

$$\sum_{0 < m_0 < \cdots < m_{d-1}} \prod_{i=0}^{d-1} m_i^{-k_i},$$

the unconditional sum over all strictly increasing tuples of positive natural numbers (taken to
be $0$ if the family is not summable).

This is the convention in arXiv:2304.08722 and arXiv:2608.10675.

Formalized by `MetaMathlibExt.MultipleZeta.increasingValue`, a definition declared in [MathlibExt/NumberTheory/MultipleZeta/Reversal.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/MultipleZeta/Reversal.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/reversing-multiple-zeta-summation-conventions/index.html#increasing-value).

## Reversal of strictly increasing tuples

Let $k$ be an index of depth $d$; its reverse
also has depth $d$. Sending a strictly increasing tuple $(m_0, \dots, m_{d-1})$ of positive
natural numbers to the reversed tuple $(m_{d-1}, \dots, m_0)$ is a bijection from the strictly
increasing tuples of length $d$ onto the strictly decreasing tuples of length $d$, whose inverse
again reverses the order of the coordinates.

Formalized by `MetaMathlibExt.MultipleZeta.increasingEquivDecreasing`, a definition declared in [MathlibExt/NumberTheory/MultipleZeta/Reversal.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/MultipleZeta/Reversal.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/reversing-multiple-zeta-summation-conventions/index.html#increasing-equiv-decreasing).

## Reversal preserves each summand

Let $k = (k_0, \dots, k_{d-1})$ be an index of depth
$d$ and let $m = (m_0, \dots, m_{d-1})$ be a strictly increasing tuple of positive natural
numbers. Then the summand of the increasing multiple-zeta series of $k$ at $m$ equals the
summand of the strict multiple-zeta series of the reversed index $(k_{d-1}, \dots, k_0)$ at the
strictly decreasing tuple $(m_{d-1}, \dots, m_0)$.

Formalized by `MetaMathlibExt.MultipleZeta.increasingSummand_eq_strictSummand_reverse`, a theorem declared in [MathlibExt/NumberTheory/MultipleZeta/Reversal.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/MultipleZeta/Reversal.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/reversing-multiple-zeta-summation-conventions/index.html#increasing-summand-eq-strict-summand-rev).

## Increasing values agree with strict values of the reverse

Let
$k = (k_0, \dots, k_{d-1})$ be an index of depth $d$ that is admissible in the increasing
convention, so that its reverse $(k_{d-1}, \dots, k_0)$ is admissible. Then the value of $k$ in
the increasing convention equals the strict multiple zeta value of the reverse of $k$:

$$\sum_{0 < m_0 < \cdots < m_{d-1}} \prod_{i=0}^{d-1} m_i^{-k_i}
= \sum_{n_0 > \cdots > n_{d-1} > 0} \prod_{i=0}^{d-1} n_i^{-k_{d-1-i}},$$

where both sides are unconditional sums of real numbers (taken to be $0$ for a non-summable
family).

Formalized by `MetaMathlibExt.MultipleZeta.increasingValue_eq_strictValue_reverse`, a theorem declared in [MathlibExt/NumberTheory/MultipleZeta/Reversal.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/MultipleZeta/Reversal.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/reversing-multiple-zeta-summation-conventions/index.html#increasing-value-eq-strict-value-reverse).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Reversing multiple-zeta summation conventions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/reversing-multiple-zeta-summation-conventions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/reversing-multiple-zeta-summation-conventions)
