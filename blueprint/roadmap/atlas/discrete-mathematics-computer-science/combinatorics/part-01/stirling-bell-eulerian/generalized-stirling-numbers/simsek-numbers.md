---
declaration: section
origin: cited
lean: MetaMathlibExt.simsekNumber, MetaMathlibExt.simsekNumber_eq_sum, MetaMathlibExt.simsekNumber_zero_k, MetaMathlibExt.simsekNumber_zero_zero
statement: formalized
proof: formalized
---

# Simsek numbers

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/simsek-numbers/index.html).

## Simsek numbers

For natural numbers $n$ and $k$ and a complex number $\lambda$, the Simsek
number $y_1(n, k; \lambda)$ is the complex number

$$y_1(n, k; \lambda) = \frac{1}{k!} \sum_{j=0}^{k} \binom{k}{j} j^n \lambda^j,$$

where $0^0 = 1$.

## Sources

- equation (snmf1) of https://cs.uwaterloo.ca/journals/JIS/VOL26/Oussi/oussi9.tex.

Formalized by `MetaMathlibExt.simsekNumber`, a definition declared in [MathlibExt/NumberTheory/SimsekNumber.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SimsekNumber.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/simsek-numbers/index.html#simsek-number).

## Finite-sum formula for Simsek numbers

For all natural numbers $n$ and $k$ and every
complex number $\lambda$, the Simsek number satisfies
$y_1(n, k; \lambda) = \frac{1}{k!} \sum_{j=0}^{k} \binom{k}{j} j^n \lambda^j$, where $0^0 = 1$.

Formalized by `MetaMathlibExt.simsekNumber_eq_sum`, a theorem declared in [MathlibExt/NumberTheory/SimsekNumber.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SimsekNumber.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/simsek-numbers/index.html#simsek-number-eq-sum).

## Simsek numbers with second index zero

For every natural number $n$ and every complex
number $\lambda$, the Simsek number $y_1(n, 0; \lambda)$ equals $0^n$; that is, it equals $1$
when $n = 0$ and $0$ otherwise.

Formalized by `MetaMathlibExt.simsekNumber_zero_k`, a theorem declared in [MathlibExt/NumberTheory/SimsekNumber.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SimsekNumber.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/simsek-numbers/index.html#simsek-number-zero-k).

## Simsek numbers with both indices zero

For every complex number $\lambda$, the Simsek
number $y_1(0, 0; \lambda)$ equals $1$.

Formalized by `MetaMathlibExt.simsekNumber_zero_zero`, a theorem declared in [MathlibExt/NumberTheory/SimsekNumber.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SimsekNumber.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/simsek-numbers/index.html#simsek-number-zero-zero).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Simsek numbers](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/simsek-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/simsek-numbers)
