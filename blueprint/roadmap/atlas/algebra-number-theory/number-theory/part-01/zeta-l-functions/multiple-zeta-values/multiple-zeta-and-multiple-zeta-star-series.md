---
declaration: section
origin: cited
lean: MetaMathlibExt.MultipleZeta.Index.empty, MetaMathlibExt.MultipleZeta.Index.entry, MetaMathlibExt.MultipleZeta.StrictDecreasingTuple, MetaMathlibExt.MultipleZeta.StrictDecreasingTuple.empty, MetaMathlibExt.MultipleZeta.strictSummand, MetaMathlibExt.MultipleZeta.Index.IsAdmissibleOrEmpty, MetaMathlibExt.MultipleZeta.strictValue, MetaMathlibExt.MultipleZeta.WeaklyDecreasingTuple
statement: formalized
proof: formalized
---

# Multiple-zeta and multiple-zeta-star series

16 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/multiple-zeta-and-multiple-zeta-star-series/index.html).

## Empty multiple-zeta index

The empty multiple-zeta index, which has no entries and weight
zero.

## Sources

- arXiv:2307.09867, empty-index convention.

Formalized by `MetaMathlibExt.MultipleZeta.Index.empty`, a definition declared in [MathlibExt/NumberTheory/MultipleZeta/Series.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/MultipleZeta/Series.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/multiple-zeta-and-multiple-zeta-star-series/index.html#empty).

## Entry of a multiple-zeta index

For a multiple-zeta index $k = (k_0, \dots, k_{d-1})$ of
depth $d$ and $0 \le i < d$, the entry of $k$ at $i$ is the positive natural number $k_i$.

Formalized by `MetaMathlibExt.MultipleZeta.Index.entry`, a definition declared in [MathlibExt/NumberTheory/MultipleZeta/Series.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/MultipleZeta/Series.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/multiple-zeta-and-multiple-zeta-star-series/index.html#entry).

## Strictly decreasing tuples

For a natural number $r$, a strictly decreasing $r$-tuple is a
tuple $(m_0, \dots, m_{r-1})$ of positive integers with $m_0 > m_1 > \dots > m_{r-1}$.

## Sources

- arXiv:2307.09867, lines 60–63, and arXiv:2309.07569, lines 76–80.

Formalized by `MetaMathlibExt.MultipleZeta.StrictDecreasingTuple`, an abbreviation declared in [MathlibExt/NumberTheory/MultipleZeta/Series.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/MultipleZeta/Series.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/multiple-zeta-and-multiple-zeta-star-series/index.html#strict-decreasing-tuple).

## Empty strictly decreasing tuple

The unique strictly decreasing tuple of positive natural
numbers of length zero, namely the empty tuple.

Formalized by `MetaMathlibExt.MultipleZeta.StrictDecreasingTuple.empty`, a definition declared in [MathlibExt/NumberTheory/MultipleZeta/Series.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/MultipleZeta/Series.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/multiple-zeta-and-multiple-zeta-star-series/index.html#empty-2).

## Multiple zeta summand

Let $\mathbf{k} = (k_0, \dots, k_{r-1})$ be an index of depth $r$
and let $(m_0, \dots, m_{r-1})$ be a strictly decreasing $r$-tuple of positive integers. The
summand attached to $\mathbf{k}$ and this tuple is the real number
$\left(\prod_{i=0}^{r-1} m_i^{k_i}\right)^{-1}$.

## Sources

- arXiv:2307.09867, lines 60–63, and arXiv:2309.07569, lines 76–80.

Formalized by `MetaMathlibExt.MultipleZeta.strictSummand`, a definition declared in [MathlibExt/NumberTheory/MultipleZeta/Series.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/MultipleZeta/Series.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/multiple-zeta-and-multiple-zeta-star-series/index.html#strict-summand).

## Admissible or empty index

A multiple-zeta index is admissible or empty when it is
admissible (nonempty with first entry at least two) or has depth zero, that is, has no entries.

The strict multiple-zeta value and the multiple-zeta-star value are defined on these indices.

Formalized by `MetaMathlibExt.MultipleZeta.Index.IsAdmissibleOrEmpty`, a definition declared in [MathlibExt/NumberTheory/MultipleZeta/Series.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/MultipleZeta/Series.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/multiple-zeta-and-multiple-zeta-star-series/index.html#is-admissible-or-empty).

## Multiple zeta value

Let $\mathbf{k} = (k_0, \dots, k_{r-1})$ be an index of depth $r$
that is admissible ($r \ge 1$ and $k_0 \ge 2$) or empty. Its multiple zeta value is the real
number

$$\zeta(\mathbf{k}) = \sum_{m_0 > m_1 > \dots > m_{r-1} \ge 1} \prod_{i=0}^{r-1} m_i^{-k_i}$$

where the sum runs over all strictly decreasing $r$-tuples $(m_0, \dots, m_{r-1})$ of positive
integers. The sum is unconditional, with value $0$ by convention when the family is not
summable.

## Sources

- arXiv:2307.09867, lines 60–63, and arXiv:2309.07569, lines 76–80.

Formalized by `MetaMathlibExt.MultipleZeta.strictValue`, a definition declared in [MathlibExt/NumberTheory/MultipleZeta/Series.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/MultipleZeta/Series.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/multiple-zeta-and-multiple-zeta-star-series/index.html#strict-value).

## Weakly decreasing tuples

For a natural number $r$, a weakly decreasing $r$-tuple is a
tuple $(m_0, \dots, m_{r-1})$ of positive integers with $m_0 \ge m_1 \ge \dots \ge m_{r-1}$.

## Sources

- arXiv:2307.09867, lines 61–65, and arXiv:2309.07569v2, lines 84–87.

Formalized by `MetaMathlibExt.MultipleZeta.WeaklyDecreasingTuple`, an abbreviation declared in [MathlibExt/NumberTheory/MultipleZeta/Series.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/MultipleZeta/Series.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/multiple-zeta-and-multiple-zeta-star-series/index.html#weakly-decreasing-tuple).

## Empty weakly decreasing tuple

The unique weakly decreasing tuple of positive natural
numbers of length zero, namely the empty tuple.

Formalized by `MetaMathlibExt.MultipleZeta.WeaklyDecreasingTuple.empty`, a definition declared in [MathlibExt/NumberTheory/MultipleZeta/Series.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/MultipleZeta/Series.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/multiple-zeta-and-multiple-zeta-star-series/index.html#empty-3).

## Strictly decreasing tuples as weakly decreasing tuples

For a natural number $r$, every
strictly decreasing $r$-tuple $(m_0, \dots, m_{r-1})$ of positive integers is weakly decreasing;
this map sends it to the same tuple, regarded as a weakly decreasing $r$-tuple.

Formalized by `MetaMathlibExt.MultipleZeta.StrictDecreasingTuple.toWeaklyDecreasing`, a definition declared in [MathlibExt/NumberTheory/MultipleZeta/Series.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/MultipleZeta/Series.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/multiple-zeta-and-multiple-zeta-star-series/index.html#to-weakly-decreasing).

## Multiple-zeta-star summand

For a multiple-zeta index $k = (k_0, \dots, k_{d-1})$ of
depth $d$ and a weakly decreasing tuple $m = (m_0, \dots, m_{d-1})$ of positive natural numbers,
the star summand of $k$ at $m$ is the real number $\left(\prod_{i\lt d} m_i^{k_i}\right)^{-1}$.

## Sources

- arXiv:2307.09867, lines 61–65, and arXiv:2309.07569v2, lines 84–87.

Formalized by `MetaMathlibExt.MultipleZeta.starSummand`, a definition declared in [MathlibExt/NumberTheory/MultipleZeta/Series.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/MultipleZeta/Series.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/multiple-zeta-and-multiple-zeta-star-series/index.html#star-summand).

## Star and strict summands agree on strictly decreasing tuples

For a multiple-zeta index
$k$ of depth $d$ and a strictly decreasing tuple $m$ of $d$ positive natural numbers, the star
summand of $k$ at $m$, with $m$ regarded as a weakly decreasing tuple, equals the strict summand
of $k$ at $m$.

Formalized by `MetaMathlibExt.MultipleZeta.starSummand_toWeaklyDecreasing`, a theorem declared in [MathlibExt/NumberTheory/MultipleZeta/Series.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/MultipleZeta/Series.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/multiple-zeta-and-multiple-zeta-star-series/index.html#star-summand-to-weakly-decreasing).

## Multiple zeta-star value

Let $\mathbf{k} = (k_0, \dots, k_{r-1})$ be an index of depth
$r$ that is admissible ($r \ge 1$ and $k_0 \ge 2$) or empty. Its multiple zeta-star value is the
real number

$$\zeta^\star(\mathbf{k}) = \sum_{m_0 \ge \dots \ge m_{r-1} \ge 1} \prod_{i=0}^{r-1} m_i^{-k_i}$$

where the sum runs over all weakly decreasing $r$-tuples $(m_0, \dots, m_{r-1})$ of positive
integers. The sum is unconditional, with value $0$ by convention when the family is not
summable.

## Sources

- arXiv:2307.09867, lines 61–65, and arXiv:2309.07569v2, lines 84–87.

Formalized by `MetaMathlibExt.MultipleZeta.starValue`, a definition declared in [MathlibExt/NumberTheory/MultipleZeta/Series.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/MultipleZeta/Series.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/multiple-zeta-and-multiple-zeta-star-series/index.html#star-value).

## Multiple-zeta-star value of the empty index

The multiple-zeta-star value of the empty
index is $1$.

## Sources

- arXiv:2307.09867, lines 166–167.

Formalized by `MetaMathlibExt.MultipleZeta.starValue_empty`, a theorem declared in [MathlibExt/NumberTheory/MultipleZeta/Series.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/MultipleZeta/Series.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/multiple-zeta-and-multiple-zeta-star-series/index.html#star-value-empty).

## Repeated index

For a natural number $k$ and a positive natural number $e$, the index
$\{e\}^k = (e, \dots, e)$ consisting of $k$ entries all equal to $e$, so of weight $ke$.

For $e = 2$ its multiple-zeta-star value is $\zeta^\star(\{2\}^k)$.

## Sources

- Serge Iovleff, *About Some Nested Sums of Reciprocal Squared Numbers*, INTEGERS 26 (2026), Article A114, Section 1 (notation `ζ*({2}^k)` and `ζ({2}^k)`).

Formalized by `MetaMathlibExt.MultipleZeta.Index.replicate`, a definition declared in [MathlibExt/NumberTheory/MultipleZeta/Series.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/MultipleZeta/Series.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/multiple-zeta-and-multiple-zeta-star-series/index.html#replicate).

## Repeated indices with entry at least two are admissible or empty

For every natural
number $k$ and every positive natural number $e \ge 2$, the index $\{e\}^k$ consisting of $k$
entries all equal to $e$ is admissible or empty.

## Sources

- Iovleff, INTEGERS 26 (2026), Article A114, Section 1 (`ζ*({2}^k)`).

Formalized by `MetaMathlibExt.MultipleZeta.Index.replicate_isAdmissibleOrEmpty`, a theorem declared in [MathlibExt/NumberTheory/MultipleZeta/Series.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/MultipleZeta/Series.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/multiple-zeta-and-multiple-zeta-star-series/index.html#replicate-is-admissible-or-empty).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Multiple-zeta and multiple-zeta-star series](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/multiple-zeta-and-multiple-zeta-star-series/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/multiple-zeta-and-multiple-zeta-star-series)
