---
declaration: section
origin: cited
lean: MetaMathlibExt.quadraticGaussSum5, MetaMathlibExt.quadraticGaussSum5_eval
statement: formalized
proof: formalized
---

# Quadratic Gauss sums

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/quadratic-gauss-sums/index.html).

## Quadratic Gauss sum modulo $5$

For an integer $k$, the quadratic Gauss sum $g(k; 5)$ is
the complex number $g(k; 5) = \sum_{n=0}^{4} e^{2\pi i k n^2 / 5}$.

Formalized by `MetaMathlibExt.quadraticGaussSum5`, a definition declared in [MathlibExt/NumberTheory/QuadraticGaussSumFive.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/QuadraticGaussSumFive.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/quadratic-gauss-sums/index.html#quadratic-gauss-sum5).

## Evaluation of the quadratic Gauss sum modulo $5$

For every integer $k$ not divisible by
$5$, the quadratic Gauss sum $g(k; 5) = \sum_{n=0}^{4} e^{2\pi i k n^2 / 5}$ equals
$\left(\frac{k}{5}\right)\sqrt{5}$, where $\left(\frac{k}{5}\right)$ is the Legendre symbol.

## Sources

- the classical evaluation recorded in Dresden–Li, Journal of Integer Sequences 26 (2023), citing Berndt, Evans, and Williams, Theorem 1.5.2.

Formalized by `MetaMathlibExt.quadraticGaussSum5_eval`, a theorem declared in [MathlibExt/NumberTheory/QuadraticGaussSumFive.lean, line 551](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/QuadraticGaussSumFive.lean#L551). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/quadratic-gauss-sums/index.html#quadratic-gauss-sum5-eval).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Quadratic Gauss sums](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/quadratic-gauss-sums/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/exponential-sums/quadratic-gauss-sums)
