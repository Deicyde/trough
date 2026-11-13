---
declaration: section
origin: cited
lean: MetaMathlibExt.knuth_catalan_log_sq_canonical, MetaMathlibExt.knuth_catalan_log_sq
statement: formalized
proof: formalized
---

# Knuth's identity for central binomial coefficients

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/knuth-s-identity-for-central-binomial-coefficien/index.html).

## Knuth's identity in harmonic-number notation

Let $x$ be a real number with
$|x| \le 1/4$. Write $H_k = \sum_{j=1}^{k} \frac{1}{j}$ for the $k$-th harmonic number and $C_n$
for the $n$-th Catalan number. Then the series

$$\sum_{n=1}^{\infty} \binom{2n}{n} \left(H_{2n-1} - H_n\right) \frac{x^n}{n}$$

converges absolutely, and its sum is $\left(\log \sum_{n=0}^{\infty} C_n x^n\right)^2$.

Formalized by `MetaMathlibExt.knuth_catalan_log_sq_canonical`, a theorem declared in [MathlibExt/Analysis/Series/KnuthCatalanLogSq.lean, line 1763](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Series/KnuthCatalanLogSq.lean#L1763). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/knuth-s-identity-for-central-binomial-coefficien/index.html#knuth-catalan-log-sq-canonical).

## Knuth's identity for central binomial coefficients and harmonic numbers

Let $x$ be a real
number with $|x| \le 1/4$, and let $C_n$ denote the $n$-th Catalan number. Then the series

$$\sum_{n=1}^{\infty} \binom{2n}{n}
\left(\sum_{j=1}^{2n-1} \frac{1}{j} - \sum_{j=1}^{n} \frac{1}{j}\right) \frac{x^n}{n}$$

converges absolutely, and its sum is $\left(\log \sum_{n=0}^{\infty} C_n x^n\right)^2$.

## Sources

- Hongwei Chen, "Interesting Series Associated with Central Binomial Coefficients, Catalan Numbers and Harmonic Numbers", Journal of Integer Sequences 19 (2016), Article 16.1.5, Theorem `eq:k_gf`, lines 229-234, <https://cs.uwaterloo.ca/journals/JIS/VOL19/Chen/chen21.tex>.

Formalized by `MetaMathlibExt.knuth_catalan_log_sq`, a theorem declared in [MathlibExt/Analysis/Series/KnuthCatalanLogSq.lean, line 1782](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Series/KnuthCatalanLogSq.lean#L1782). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/knuth-s-identity-for-central-binomial-coefficien/index.html#knuth-catalan-log-sq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Knuth's identity for central binomial coefficients](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/knuth-s-identity-for-central-binomial-coefficien/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/knuth-s-identity-for-central-binomial-coefficien)
