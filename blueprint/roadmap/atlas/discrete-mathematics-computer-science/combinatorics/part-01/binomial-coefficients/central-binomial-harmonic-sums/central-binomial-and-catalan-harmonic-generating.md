---
declaration: section
origin: cited
lean: MetaMathlibExt.catalan_harmonic_generating_function_canonical, MetaMathlibExt.catalan_harmonic_generating_function, MetaMathlibExt.hasSum_centralBinomial_harmonic
statement: formalized
proof: formalized
---

# Central binomial and Catalan–harmonic generating functions

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/central-binomial-and-catalan-harmonic-generating/index.html).

## Generating function of Catalan–harmonic products

Let $C_n$ be the $n$th Catalan number and
$H_n = \sum_{k=1}^{n} 1/k$ the $n$th harmonic number, so that $H_0 = 0$. For every real number
$x$ with $|x| < 1/4$,

$$
\sum_{n=0}^{\infty} C_n H_n x^{n+1} = \log 2 + \sqrt{1-4x}\,\log\bigl(2\sqrt{1-4x}\bigr) -
\bigl(1 + \sqrt{1-4x}\bigr)\log\bigl(1 + \sqrt{1-4x}\bigr).
$$

Formalized by `MetaMathlibExt.catalan_harmonic_generating_function_canonical`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/CatalanHarmonicGeneratingFunction.lean, line 964](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/CatalanHarmonicGeneratingFunction.lean#L964). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/central-binomial-and-catalan-harmonic-generating/index.html#catalan-harmonic-generating-function-can).

## Catalan–harmonic generating function with explicit coefficients

For every real number $x$
with $|x| < 1/4$,

$$
\sum_{n=1}^{\infty} \frac{\binom{2n}{n}}{n+1} \Bigl(\sum_{k=1}^{n} \frac{1}{k}\Bigr) x^{n+1} =
\log 2 + \sqrt{1-4x}\,\log\bigl(2\sqrt{1-4x}\bigr) -
\bigl(1 + \sqrt{1-4x}\bigr)\log\bigl(1 + \sqrt{1-4x}\bigr).
$$

Here $\binom{2n}{n}/(n+1)$ is the $n$th Catalan number (the division is exact) and
$\sum_{k=1}^{n} 1/k$ is the $n$th harmonic number.

## Sources

- Hongwei Chen, "Interesting Series Associated with Central Binomial Coefficients, Catalan Numbers and Harmonic Numbers," Journal of Integer Sequences 19 (2016), Article 16.1.5, Corollary, lines 156–160, https://cs.uwaterloo.ca/journals/JIS/VOL19/Chen/chen21.tex; obtained there by integrating the central-binomial harmonic generating function.

Formalized by `MetaMathlibExt.catalan_harmonic_generating_function`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/CatalanHarmonicGeneratingFunction.lean, line 998](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/CatalanHarmonicGeneratingFunction.lean#L998). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/central-binomial-and-catalan-harmonic-generating/index.html#catalan-harmonic-generating-function).

## Central binomial–harmonic generating function

Let $H_n = \sum_{k=1}^{n} 1/k$ be the $n$th
harmonic number. For every real number $x$ with $|x| < 1/4$, the series
$\sum_{n=1}^{\infty} \binom{2n}{n} H_n x^n$ converges unconditionally, with sum

$$
\sum_{n=1}^{\infty} \binom{2n}{n} H_n x^n =
\frac{2}{\sqrt{1-4x}} \log \frac{1 + \sqrt{1-4x}}{2\sqrt{1-4x}}.
$$

## Sources

- Hongwei Chen, "Interesting Series Associated with Central Binomial Coefficients, Catalan Numbers and Harmonic Numbers," Journal of Integer Sequences 19 (2016), Article 16.1.5, Theorem, lines 147–151, https://cs.uwaterloo.ca/journals/JIS/VOL19/Chen/chen21.tex.

Formalized by `MetaMathlibExt.hasSum_centralBinomial_harmonic`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/CentralBinomialHarmonicGeneratingFunction.lean, line 757](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/CentralBinomialHarmonicGeneratingFunction.lean#L757). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/central-binomial-and-catalan-harmonic-generating/index.html#has-sum-central-binomial-harmonic).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Central binomial and Catalan–harmonic generating functions](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/central-binomial-and-catalan-harmonic-generating/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/central-binomial-and-catalan-harmonic-generating)
