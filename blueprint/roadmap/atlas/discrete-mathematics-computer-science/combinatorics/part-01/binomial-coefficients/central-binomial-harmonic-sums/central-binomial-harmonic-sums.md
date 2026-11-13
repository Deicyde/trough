---
declaration: section
origin: cited
lean: MetaMathlibExt.aeratedCentralBinomialNumber, MetaMathlibExt.central_binom_power_sum_stirling
statement: formalized
proof: formalized
---

# Central binomial coefficients and harmonic sums: its own results

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/index.html).

Finite sums and power series involving central binomial coefficients or their reciprocals, often weighted by harmonic or odd harmonic numbers, including arcsin-type series and Kollár's incomplete binomial sums.

## Aerated central binomial numbers

For a natural number $n$, the $n$-th aerated central
binomial number is $\binom{n}{n/2}$ if $n$ is even and $0$ if $n$ is odd. The sequence begins
$1, 0, 2, 0, 6, 0, 20, \dots$.

Formalized by `MetaMathlibExt.aeratedCentralBinomialNumber`, a definition declared in [MathlibExt/Combinatorics/Enumerative/AeratedCentralBinomialNumber.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/AeratedCentralBinomialNumber.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/index.html#aerated-central-binomial-number).

## Central binomial power sums via Stirling numbers

For every natural number $m$ and every
real $x$ with $|x| < 1/4$,

$$\sum_{n=0}^{\infty} \binom{2n}{n} n^m x^n =
\frac{1}{\sqrt{1-4x}} \sum_{k=0}^{m} S(m,k) \binom{2k}{k}\, k! \left(\frac{x}{1-4x}\right)^k,$$

where $S(m,k)$ denotes the Stirling numbers of the second kind (and $n^0 = 1$ for every $n$).

The source asks for positive $m$; the identity also holds at $m = 0$, where both sides are the
generating function of the central binomial coefficients.

## Sources

- Khristo N. Boyadzhiev, "Series with Central Binomial Coefficients, Catalan Numbers, and Harmonic Numbers," Journal of Integer Sequences 15 (2012), Article 12.1.7, Theorem (equation 8), lines 155–160, https://cs.uwaterloo.ca/journals/JIS/VOL15/Boyadzhiev/boyadzhiev6.tex

Formalized by `MetaMathlibExt.central_binom_power_sum_stirling`, a theorem declared in [MathlibExt/Analysis/Series/CentralBinomPowerSum.lean, line 586](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Series/CentralBinomPowerSum.lean#L586). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/index.html#central-binom-power-sum-stirling).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Central binomial coefficients and harmonic sums](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums)
