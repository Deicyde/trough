---
declaration: section
origin: cited
lean: MetaMathlibExt.brent_osborn_binomial_absolute_moment, MetaMathlibExt.double_binomial_sum_eq_single_binomial_sum
statement: formalized
proof: formalized
---

# Binomial sums involving absolute values

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/binomial-sums-involving-absolute-values/index.html).

## Brent–Osborn binomial absolute moment identity

For every natural number $n$,

$$\sum_{k=0}^{2n} \sum_{\ell=0}^{2n} \binom{2n}{k} \binom{2n}{\ell} \,
\bigl| (k-n)^2 - (\ell-n)^2 \bigr| = 2n^2 \binom{2n}{n}^2.$$

In centered form this says
$\sum_{k,\ell} \binom{2n}{n+k} \binom{2n}{n+\ell} \, |k^2 - \ell^2| = 2n^2 \binom{2n}{n}^2$,
the sum running over all integers $k, \ell$, since the binomial coefficients vanish for $|k| > n$.

## Sources

- Richard P. Brent, Hideyuki Ohtsuka, Judy-anne H. Osborn, and Helmut Prodinger, "Some Binomial Sums Involving Absolute Values," Journal of Integer Sequences 19 (2016), Article 16.3.7, Theorem [Brent and Osborn], lines 377–383 (with the `W_β` definition at lines 345–349), https://cs.uwaterloo.ca/journals/JIS/VOL19/Brent/brent9.tex

Formalized by `MetaMathlibExt.brent_osborn_binomial_absolute_moment`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/BrentOsbornBinomialAbsoluteMoment.lean, line 400](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/BrentOsbornBinomialAbsoluteMoment.lean#L400). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/binomial-sums-involving-absolute-values/index.html#brent-osborn-binomial-absolute-moment).

## Reduction of a double binomial absolute-value sum

For all natural numbers $\beta$, $m$ and
$n$,

$$\sum_{i=0}^{2m} \sum_{j=0}^{2n} \binom{2m}{i} \binom{2n}{j} \lvert (i-m)-(j-n) \rvert^{\beta}
= \sum_{k=0}^{2(m+n)} \binom{2(m+n)}{k} \lvert k-m-n \rvert^{\beta},$$

with the convention $0^0 = 1$.

In the source's notation, $S_\beta(n) = \sum_k \binom{2n}{n+k} \lvert k \rvert^\beta$ and
$T_\beta(m,n) = \sum_{k,\ell} \binom{2m}{m+k} \binom{2n}{n+\ell} \lvert k-\ell \rvert^\beta$, and
the identity reads $T_\beta(m,n) = S_\beta(m+n)$, after the shift $i = m + k$, $j = n + \ell$.

## Sources

- Richard P. Brent, Hideyuki Ohtsuka, Judy-anne H. Osborn, and Helmut Prodinger, "Some Binomial Sums Involving Absolute Values," Journal of Integer Sequences 19 (2016), Article 16.3.7, Theorem, lines 278–283 (with `S_β` defined at lines 245–247 and `T_β` at 271–274), https://cs.uwaterloo.ca/journals/JIS/VOL19/Brent/brent9.tex

Formalized by `MetaMathlibExt.double_binomial_sum_eq_single_binomial_sum`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/DoubleBinomialSumReduction.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/DoubleBinomialSumReduction.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/binomial-sums-involving-absolute-values/index.html#double-binomial-sum-eq-single-binomial-s).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Binomial sums involving absolute values](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/binomial-sums-involving-absolute-values/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/binomial-coefficients/binomial-sums/binomial-sums-involving-absolute-values)
