---
declaration: section
origin: cited
lean: MetaMathlibExt.ramanujanThetaTerm, MetaMathlibExt.ramanujanThetaRaw, MetaMathlibExt.ramanujanTheta, MetaMathlibExt.not_summable_ramanujanThetaTerm_one_one, MetaMathlibExt.ramanujanThetaRaw_one_one, MetaMathlibExt.ramanujanTheta_summable
statement: formalized
proof: formalized
---

# Ramanujan's theta function

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/ramanujan-s-theta-function/index.html).

## Summand of Ramanujan's general theta function

For complex numbers $a$, $b$ and an
integer $n$, this is the term $a^{n(n+1)/2} b^{n(n-1)/2}$ of index $n$ in Ramanujan's general
theta function $f(a,b) = \sum_{k \in \mathbb{Z}} a^{k(k+1)/2} b^{k(k-1)/2}$.

Both exponents $n(n+1)/2$ and $n(n-1)/2$ are nonnegative integers for every integer $n$, so
the term is a product of ordinary powers with natural-number exponents.

## Sources

- the common definition in arXiv:2305.14988, arXiv:2309.06689, arXiv:2312.15513, arXiv:2502.17312, and arXiv:2607.26471.

Formalized by `MetaMathlibExt.ramanujanThetaTerm`, a definition declared in [MathlibExt/NumberTheory/ModularForms/JacobiTheta/Ramanujan.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ModularForms/JacobiTheta/Ramanujan.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/ramanujan-s-theta-function/index.html#ramanujan-theta-term).

## Raw Ramanujan theta sum

For complex numbers $a$ and $b$, the raw Ramanujan theta sum is
$\sum_{n \in \mathbb{Z}} a^{n(n+1)/2} b^{n(n-1)/2}$ when this series is summable, and $0$
otherwise.

The value $0$ for a non-summable series is a convention. Ramanujan's general theta function,
which requires the series to be summable, is the intended object.

Formalized by `MetaMathlibExt.ramanujanThetaRaw`, a definition declared in [MathlibExt/NumberTheory/ModularForms/JacobiTheta/Ramanujan.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ModularForms/JacobiTheta/Ramanujan.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/ramanujan-s-theta-function/index.html#ramanujan-theta-raw).

## Ramanujan's general theta function

For complex numbers $a$ and $b$ such that the series
$\sum_{n \in \mathbb{Z}} a^{n(n+1)/2} b^{n(n-1)/2}$ is summable, Ramanujan's general theta
function is its sum $f(a,b) = \sum_{n \in \mathbb{Z}} a^{n(n+1)/2} b^{n(n-1)/2}$.

Formalized by `MetaMathlibExt.ramanujanTheta`, a definition declared in [MathlibExt/NumberTheory/ModularForms/JacobiTheta/Ramanujan.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ModularForms/JacobiTheta/Ramanujan.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/ramanujan-s-theta-function/index.html#ramanujan-theta).

## Ramanujan's theta series diverges at $a = b = 1$

The series
$\sum_{n \in \mathbb{Z}} a^{n(n+1)/2} b^{n(n-1)/2}$ of Ramanujan's general theta function is
not summable at $a = b = 1$, since every one of its terms equals $1$.

Formalized by `MetaMathlibExt.not_summable_ramanujanThetaTerm_one_one`, a theorem declared in [MathlibExt/NumberTheory/ModularForms/JacobiTheta/Ramanujan.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ModularForms/JacobiTheta/Ramanujan.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/ramanujan-s-theta-function/index.html#not-summable-ramanujan-theta-term-one-on).

## The raw Ramanujan theta sum vanishes at $a = b = 1$

The raw Ramanujan theta sum
$\sum_{n \in \mathbb{Z}} a^{n(n+1)/2} b^{n(n-1)/2}$, which is assigned the value $0$ whenever
the series is not summable, equals $0$ at $a = b = 1$, because there every term equals $1$ and
the series is not summable.

Formalized by `MetaMathlibExt.ramanujanThetaRaw_one_one`, a theorem declared in [MathlibExt/NumberTheory/ModularForms/JacobiTheta/Ramanujan.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ModularForms/JacobiTheta/Ramanujan.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/ramanujan-s-theta-function/index.html#ramanujan-theta-raw-one-one).

## Absolute convergence of Ramanujan's general theta series

For all complex numbers $a$
and $b$ with $|ab| < 1$, the series $\sum_{n \in \mathbb{Z}} |a^{n(n+1)/2} b^{n(n-1)/2}|$ of
the absolute values of the terms of Ramanujan's general theta function converges.

## Sources

- arXiv:2607.26471, `Oliver_identities.tex` ll. 127-130.

Formalized by `MetaMathlibExt.ramanujanTheta_summable`, a theorem declared in [MathlibExt/NumberTheory/ModularForms/JacobiTheta/RamanujanSummability.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ModularForms/JacobiTheta/RamanujanSummability.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/ramanujan-s-theta-function/index.html#ramanujan-theta-summable).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ramanujan's theta function](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/ramanujan-s-theta-function/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/ramanujan-s-theta-function)
