---
declaration: section
origin: cited
lean: MetaMathlibExt.morganVoyceCoeff, MetaMathlibExt.morganVoycePolynomial
statement: formalized
proof: formalized
---

# Morgan–Voyce polynomials

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/morgan-voyce-polynomials/index.html).

## Morgan–Voyce coefficients

For natural numbers $n$ and $k$, the Morgan–Voyce coefficient
$d(n, k)$ is the binomial coefficient $\binom{n + k}{n - k}$ if $k \le n$, and $0$ if $k > n$.

These numbers form the lower-triangular Riordan array
$\left(\frac{1}{1 - x}, \frac{x}{(1 - x)^2}\right)$, OEIS A085478.

Formalized by `MetaMathlibExt.morganVoyceCoeff`, a definition declared in [MathlibExt/RingTheory/Polynomial/MorganVoycePolynomial.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/Polynomial/MorganVoycePolynomial.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/morgan-voyce-polynomials/index.html#morgan-voyce-coeff).

## Morgan–Voyce polynomials

For a semiring $R$ and a natural number $n$, the Morgan–Voyce
polynomial of index $n$ over $R$ is

$$b_n(x) = \sum_{k=0}^{n} d(n, k)\, x^k \in R[x],$$

where $d(n, k) = \binom{n + k}{n - k}$ is the Morgan–Voyce coefficient, read in $R$ through the
map from the natural numbers.

The coefficients of $b_n$ form row $n$ of the Riordan array
$\left(\frac{1}{1 - x}, \frac{x}{(1 - x)^2}\right)$, OEIS A085478.

## Sources

- OEIS A085478.

Formalized by `MetaMathlibExt.morganVoycePolynomial`, a definition declared in [MathlibExt/RingTheory/Polynomial/MorganVoycePolynomial.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/Polynomial/MorganVoycePolynomial.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/morgan-voyce-polynomials/index.html#morgan-voyce-polynomial).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Morgan–Voyce polynomials](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/morgan-voyce-polynomials/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/morgan-voyce-polynomials)
