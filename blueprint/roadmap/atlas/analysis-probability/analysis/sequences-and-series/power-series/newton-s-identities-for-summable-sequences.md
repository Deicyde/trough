---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry11CorollaryNewtonGirard.ramanujan_part1_ch3_entry11_corollary_newton_girard_general, MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry11CorollaryNewtonGirard.ramanujan_part1_ch3_entry11_corollary_newton_girard, MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry11CorollaryPowerSummable.ramanujan_part1_ch3_entry11_corollary_power_summable
statement: formalized
proof: formalized
---

# Newton's identities for summable sequences

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/newton-s-identities-for-summable-sequences/index.html).

## Newton's identities for summable families

Let $(a_j)_{j \ge 0}$ be a sequence of complex
numbers, and let $(e_n)_{n \ge 0}$ and $(p_k)_{k \ge 1}$ be complex numbers such that for every
$n$ the family $\prod_{j \in s} a_j$, indexed by the $n$-element finite sets $s$ of natural
numbers, is summable with sum $e_n$, and for every $k \ge 1$ the series $\sum_{j \ge 0} a_j^k$
is summable with sum $p_k$. Then for every natural number $n$,

$$n e_n = \sum_{k=1}^{n} (-1)^{k-1} p_k e_{n-k}.$$

No absolute summability of $(a_j)$ is assumed, and the case $n = 0$, where both sides vanish,
is included.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry11CorollaryNewtonGirard.ramanujan_part1_ch3_entry11_corollary_newton_girard_general`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry11CorollaryNewtonGirard.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry11CorollaryNewtonGirard.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/newton-s-identities-for-summable-sequences/index.html#ramanujan-part1-ch3-entry11-corollary-ne).

## Newton's identities for absolutely summable sequences

Let $(a_j)_{j \ge 0}$ be a sequence
of complex numbers with $\sum_j |a_j| < \infty$. Let $(e_n)_{n \ge 0}$ and $(p_k)_{k \ge 1}$ be
complex numbers such that for every $n$ the family $\prod_{j \in s} a_j$, indexed by the
$n$-element finite sets $s$ of natural numbers, is summable with sum $e_n$, and for every
$k \ge 1$ the series $\sum_{j \ge 0} a_j^k$ is summable with sum $p_k$. Then for every $n \ge 1$,

$$n e_n = \sum_{k=1}^{n} (-1)^{k-1} p_k e_{n-k}.$$

## Sources

- Berndt, Ramanujan's Notebooks Part I, Chapter 3, Corollary to Entry 11, printed p. 66 / PDF p. 76.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry11CorollaryNewtonGirard.ramanujan_part1_ch3_entry11_corollary_newton_girard`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry11CorollaryNewtonGirard.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry11CorollaryNewtonGirard.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/newton-s-identities-for-summable-sequences/index.html#ramanujan-part1-ch3-entry11-corollary-ne-2).

## Powers of an absolutely summable sequence are absolutely summable

Let $(a_j)_{j \ge 0}$
be a sequence of complex numbers with $\sum_j |a_j| < \infty$, and let $n \ge 1$ be an integer.
Then $\sum_j |a_j^n| < \infty$.

## Sources

- Berndt, Ramanujan's Notebooks Part I, Chapter 3, Corollary to Entry 11, printed p. 66 / PDF p. 76.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry11CorollaryPowerSummable.ramanujan_part1_ch3_entry11_corollary_power_summable`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry11CorollaryPowerSummable.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry11CorollaryPowerSummable.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/newton-s-identities-for-summable-sequences/index.html#ramanujan-part1-ch3-entry11-corollary-po).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Newton's identities for summable sequences](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/newton-s-identities-for-summable-sequences/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/sequences-and-series/power-series/newton-s-identities-for-summable-sequences)
