---
declaration: section
origin: cited
lean: MetaMathlibExt.kadiri_zero_free_region, MetaMathlibExt.kadiri_zero_free_region_refined
statement: formalized
---

# Zero-free regions for the Riemann zeta function

2 results, 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/zero-free-regions-for-the-riemann-zeta-function/index.html).

## Kadiri's zero-free region for the Riemann zeta function

Let $\zeta$ be the Riemann zeta
function and $\log$ the natural logarithm. For every complex number $s = \sigma + it$ with
$|t| \ge 2$ and $\sigma \ge 1 - \frac{1}{5.70176 \log |t|}$, we have $\zeta(s) \ne 0$.

Stated but not proved: `MetaMathlibExt.kadiri_zero_free_region` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/KadiriZeroFreeRegionWanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PrimeCounting/KadiriZeroFreeRegionWanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/zero-free-regions-for-the-riemann-zeta-function/index.html#kadiri-zero-free-region).

## Kadiri's refined zero-free region for the Riemann zeta function

Let $\zeta$ be the Riemann
zeta function and $\log$ the natural logarithm. For every complex number $s = \sigma + it$ with
$|t| \ge 2$ and $\sigma \ge 1 - \frac{1}{5.69693 \log |t|}$, we have $\zeta(s) \ne 0$.

## Sources

- Kadiri's refined constant as cited in Dusart 2016; this is the region required by `dusart2016_tail_theorem`.

Stated but not proved: `MetaMathlibExt.kadiri_zero_free_region_refined` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/KadiriZeroFreeRegionWanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PrimeCounting/KadiriZeroFreeRegionWanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/zero-free-regions-for-the-riemann-zeta-function/index.html#kadiri-zero-free-region-refined).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Zero-free regions for the Riemann zeta function](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/zero-free-regions-for-the-riemann-zeta-function/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/zero-free-regions-for-the-riemann-zeta-function)
