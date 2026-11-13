---
declaration: section
origin: cited
lean: MetaMathlibExt.lambertSeriesSummand, MetaMathlibExt.lambertSeries, MetaMathlibExt.lambertFSummand, MetaMathlibExt.lambertF, MetaMathlibExt.lambertGSummand, MetaMathlibExt.lambertG, MetaMathlibExt.lambertFMuSummand, MetaMathlibExt.lambertFMu
statement: formalized
proof: formalized
---

# Lambert series

21 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/lambert-series/index.html).

## Lambert series summand

For a complex number $q$ with $|q| < 1$ and a natural number $k$,
the $k$-th summand of the basic Lambert series is $q^{k+1} / (1 - q^{k+1})$, that is, the term
$q^n / (1 - q^n)$ with $n = k + 1$.

Formalized by `MetaMathlibExt.lambertSeriesSummand`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/LambertSeries.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/LambertSeries.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/lambert-series/index.html#lambert-series-summand).

## Lambert series

For a complex number $q$ with $|q| < 1$, the basic Lambert series is
$L(q) = \sum_{n \ge 1} q^n / (1 - q^n)$.

Formalized by `MetaMathlibExt.lambertSeries`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/LambertSeries.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/LambertSeries.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/lambert-series/index.html#lambert-series).

## Terms of the weighted Lambert series $f$

For a complex number $q$ with $|q| < 1$ and a
natural number $k$, the term of index $k$ is $n q^n / (1 - q^n)$ with $n = k + 1$. These are the
terms of the weighted Lambert series $f(q) = \sum_{n \ge 1} n q^n / (1 - q^n)$.

Formalized by `MetaMathlibExt.lambertFSummand`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/LambertSeries.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/LambertSeries.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/lambert-series/index.html#lambert-fsummand).

## The weighted Lambert series $f$

For a complex number $q$ with $|q| < 1$, the weighted
Lambert series is $f(q) = \sum_{n \ge 1} n q^n / (1 - q^n)$.

Formalized by `MetaMathlibExt.lambertF`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/LambertSeries.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/LambertSeries.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/lambert-series/index.html#lambert-f).

## Terms of the weighted Lambert series $g$

For a complex number $q$ with $|q| < 1$ and a
natural number $k$, the term of index $k$ is $n q^n / (1 + q^n)$ with $n = k + 1$. These are the
terms of the weighted Lambert series $g(q) = \sum_{n \ge 1} n q^n / (1 + q^n)$.

Formalized by `MetaMathlibExt.lambertGSummand`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/LambertSeries.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/LambertSeries.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/lambert-series/index.html#lambert-gsummand).

## The weighted Lambert series $g$

For a complex number $q$ with $|q| < 1$, the weighted
Lambert series is $g(q) = \sum_{n \ge 1} n q^n / (1 + q^n)$.

Formalized by `MetaMathlibExt.lambertG`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/LambertSeries.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/LambertSeries.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/lambert-series/index.html#lambert-g).

## Terms of the power-weighted Lambert series $f_\mu$

For a complex number $q$ with
$|q| < 1$, an integer $\mu \ge 1$ and a natural number $k$, the term of index $k$ is
$n^\mu q^n / (1 - q^n)$ with $n = k + 1$. These are the terms of the power-weighted Lambert series
$f_\mu(q) = \sum_{n \ge 1} n^\mu q^n / (1 - q^n)$.

Formalized by `MetaMathlibExt.lambertFMuSummand`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/LambertSeries.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/LambertSeries.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/lambert-series/index.html#lambert-fmu-summand).

## The power-weighted Lambert series $f_\mu$

For a complex number $q$ with $|q| < 1$ and an
integer $\mu \ge 1$, the power-weighted Lambert series is
$f_\mu(q) = \sum_{n \ge 1} n^\mu q^n / (1 - q^n)$.

Formalized by `MetaMathlibExt.lambertFMu`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/LambertSeries.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/LambertSeries.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/lambert-series/index.html#lambert-fmu).

## Terms of the power-weighted Lambert series $g_\mu$

For a complex number $q$ with
$|q| < 1$, an integer $\mu \ge 1$ and a natural number $k$, the term of index $k$ is
$n^\mu q^n / (1 + q^n)$ with $n = k + 1$. These are the terms of the power-weighted Lambert series
$g_\mu(q) = \sum_{n \ge 1} n^\mu q^n / (1 + q^n)$.

Formalized by `MetaMathlibExt.lambertGMuSummand`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/LambertSeries.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/LambertSeries.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/lambert-series/index.html#lambert-gmu-summand).

## The power-weighted Lambert series $g_\mu$

For a complex number $q$ with $|q| < 1$ and an
integer $\mu \ge 1$, the power-weighted Lambert series is
$g_\mu(q) = \sum_{n \ge 1} n^\mu q^n / (1 + q^n)$.

Formalized by `MetaMathlibExt.lambertGMu`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/LambertSeries.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/LambertSeries.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/lambert-series/index.html#lambert-gmu).

## Terms of the Lambert family $L_m$

For a complex number $q$ with $|q| < 1$, an integer
$m \ge 1$ and a natural number $k$, the term of index $k$ is $q^{mn} / (1 - q^{2n})^m$ with
$n = k + 1$. These are the terms of $L_m(q) = \sum_{n \ge 1} q^{mn} / (1 - q^{2n})^m$.

Formalized by `MetaMathlibExt.lambertLmSummand`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/LambertSeries.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/LambertSeries.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/lambert-series/index.html#lambert-lm-summand).

## The Lambert family $L_m$

For a complex number $q$ with $|q| < 1$ and an integer $m \ge 1$,
the Lambert family is $L_m(q) = \sum_{n \ge 1} q^{mn} / (1 - q^{2n})^m$.

Formalized by `MetaMathlibExt.lambertLm`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/LambertSeries.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/LambertSeries.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/lambert-series/index.html#lambert-lm).

## Terms of the Lambert-type series $\tilde L_m$

For a complex number $q$ with $|q| < 1$,
an integer $m \ge 1$ and a natural number $k$, the term of index $k$ is
$q^{(2k+1)m} / (1 + q^{2k+1})^{2m}$, that is, $q^{(2n-1)m} / (1 + q^{2n-1})^{2m}$ with $n = k + 1$.

## Sources

- Gerhold.

Formalized by `MetaMathlibExt.tildeLMSummand`, a definition declared in [MathlibExt/NumberTheory/LambertSeriesVariants.lean, line 21](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LambertSeriesVariants.lean#L21). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/lambert-series/index.html#tilde-lmsummand).

## Summability of the Lambert-type series $\tilde L_m$

For a complex number $q$ with
$|q| < 1$ and an integer $m \ge 1$, this predicate holds when the series
$\sum_{n \ge 1} q^{(2n-1)m} / (1 + q^{2n-1})^{2m}$ is summable in $\mathbb{C}$.

## Sources

- Gerhold.

Formalized by `MetaMathlibExt.tildeLMSummable`, a definition declared in [MathlibExt/NumberTheory/LambertSeriesVariants.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LambertSeriesVariants.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/lambert-series/index.html#tilde-lmsummable).

## The Lambert-type series $\tilde L_m$

For a complex number $q$ with $|q| < 1$ and an
integer $m \ge 1$, $\tilde L_m(q) = \sum_{n \ge 1} q^{(2n-1)m} / (1 + q^{2n-1})^{2m}$, where the
sum is taken to be $0$ if the series is not summable.

## Sources

- Gerhold.

Formalized by `MetaMathlibExt.tildeLM`, a definition declared in [MathlibExt/NumberTheory/LambertSeriesVariants.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LambertSeriesVariants.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/lambert-series/index.html#tilde-lm).

## Terms of the Lambert-type series $\hat L_m$

For a complex number $q$ with $|q| < 1$,
an integer $m \ge 1$ and a natural number $k$, the term of index $k$ is
$q^{m(k+1)} / (1 + q^{2(k+1)})^m$, that is, $q^{mn} / (1 + q^{2n})^m$ with $n = k + 1$.

## Sources

- Gerhold.

Formalized by `MetaMathlibExt.hatLMSummand`, a definition declared in [MathlibExt/NumberTheory/LambertSeriesVariants.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LambertSeriesVariants.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/lambert-series/index.html#hat-lmsummand).

## Summability of the Lambert-type series $\hat L_m$

For a complex number $q$ with
$|q| < 1$ and an integer $m \ge 1$, this predicate holds when the series
$\sum_{n \ge 1} q^{mn} / (1 + q^{2n})^m$ is summable in $\mathbb{C}$.

## Sources

- Gerhold.

Formalized by `MetaMathlibExt.hatLMSummable`, a definition declared in [MathlibExt/NumberTheory/LambertSeriesVariants.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LambertSeriesVariants.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/lambert-series/index.html#hat-lmsummable).

## The Lambert-type series $\hat L_m$

For a complex number $q$ with $|q| < 1$ and an
integer $m \ge 1$, $\hat L_m(q) = \sum_{n \ge 1} q^{mn} / (1 + q^{2n})^m$, where the sum is
taken to be $0$ if the series is not summable.

## Sources

- Gerhold.

Formalized by `MetaMathlibExt.hatLM`, a definition declared in [MathlibExt/NumberTheory/LambertSeriesVariants.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LambertSeriesVariants.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/lambert-series/index.html#hat-lm).

## Terms of the Lambert-type series $L_m^*$

**Terms of the Lambert-type series $L_m^*$.** For a complex number $q$ with $|q| < 1$, an
integer $m \ge 1$ and a natural number $k$, the term of index $k$ is
$q^{(2k+1)m} / (1 - q^{2k+1})^{2m}$, that is, $q^{(2n-1)m} / (1 - q^{2n-1})^{2m}$ with $n = k + 1$.

## Sources

- Gerhold.

Formalized by `MetaMathlibExt.starLMSummand`, a definition declared in [MathlibExt/NumberTheory/LambertSeriesVariants.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LambertSeriesVariants.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/lambert-series/index.html#star-lmsummand).

## Summability of the Lambert-type series $L_m^*$

**Summability of the Lambert-type series $L_m^*$.** For a complex number $q$ with $|q| < 1$
and an integer $m \ge 1$, this predicate holds when the series
$\sum_{n \ge 1} q^{(2n-1)m} / (1 - q^{2n-1})^{2m}$ is summable in $\mathbb{C}$.

## Sources

- Gerhold.

Formalized by `MetaMathlibExt.starLMSummable`, a definition declared in [MathlibExt/NumberTheory/LambertSeriesVariants.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LambertSeriesVariants.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/lambert-series/index.html#star-lmsummable).

## The Lambert-type series $L_m^*$

**The Lambert-type series $L_m^*$.** For a complex number $q$ with $|q| < 1$ and an integer
$m \ge 1$, $L_m^*(q) = \sum_{n \ge 1} q^{(2n-1)m} / (1 - q^{2n-1})^{2m}$, where the sum is taken
to be $0$ if the series is not summable.

## Sources

- Gerhold.

Formalized by `MetaMathlibExt.starLM`, a definition declared in [MathlibExt/NumberTheory/LambertSeriesVariants.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LambertSeriesVariants.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/lambert-series/index.html#star-lm).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Lambert series](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/lambert-series/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/lambert-series)
