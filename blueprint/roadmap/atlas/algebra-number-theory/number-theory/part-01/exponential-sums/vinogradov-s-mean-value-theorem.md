---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.VinogradovMeanValueWanted.NumberTheory.VinogradovMeanValue.J, MathlibExt.NumberTheory.VinogradovMeanValueWanted.NumberTheory.VinogradovMeanValue.vinogradov_mean_value
statement: formalized
---

# Vinogradov's mean value theorem

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/vinogradov-s-mean-value-theorem/index.html).

## The Vinogradov mean value count

For natural numbers $s$, $k$ and $X$, $J_{s,k}(X)$ is the
number of pairs of tuples $(x_1, \dots, x_s)$ and $(y_1, \dots, y_s)$ of integers in
$\{1, \dots, X\}$ such that $x_1^j + \dots + x_s^j = y_1^j + \dots + y_s^j$ for every natural
number $j \le k$, regarded as a real number.

Formalized by `MathlibExt.NumberTheory.VinogradovMeanValueWanted.NumberTheory.VinogradovMeanValue.J`, a definition declared in [WantedExt/NumberTheory/VinogradovMeanValueWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/VinogradovMeanValueWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/vinogradov-s-mean-value-theorem/index.html#j).

## Vinogradov's mean value theorem

For all natural numbers $s$ and $k$ and every real
$\varepsilon > 0$ there is a constant $C$ such that
$J_{s,k}(X) \le C (X^{s + \varepsilon} + X^{2s - k(k+1)/2 + \varepsilon})$ for all sufficiently
large natural numbers $X$, where $J_{s,k}(X)$ is the number of pairs of tuples
$(x_1, \dots, x_s)$ and $(y_1, \dots, y_s)$ of integers in $\{1, \dots, X\}$ with
$x_1^j + \dots + x_s^j = y_1^j + \dots + y_s^j$ for every natural number $j \le k$.

## Sources

- J. Bourgain, C. Demeter, and L. Guth, `Proof of the main conjecture in Vinogradov's Mean Value Theorem for degrees higher than three`, Ann. of Math. 184 (2) 2016, 633–682; T. D. Wooley, `Nested efficient congruencing and relatives of Vinogradov's mean value theorem`, Proc. London Math. Soc. 118 (4) 2019, 942–1016. Problem `vinogradov_mean_value` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.NumberTheory.VinogradovMeanValueWanted.NumberTheory.VinogradovMeanValue.vinogradov_mean_value` is written with `theorem_wanted` in [WantedExt/NumberTheory/VinogradovMeanValueWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/VinogradovMeanValueWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/vinogradov-s-mean-value-theorem/index.html#vinogradov-mean-value).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Vinogradov's mean value theorem](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/vinogradov-s-mean-value-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/exponential-sums/vinogradov-s-mean-value-theorem)
