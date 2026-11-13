---
declaration: section
origin: cited
lean: MetaMathlibExt.unsignedCharlierOrder0, MetaMathlibExt.unsignedCharlierCoeff, MetaMathlibExt.unsignedCharlier_coeff_eq
statement: formalized
proof: formalized
---

# Charlier polynomials

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/charlier-polynomials/index.html).

## Unsigned Charlier polynomials of order 0

For a semiring $R$ and a natural number $n$,
the $n$-th unsigned Charlier polynomial of order $0$ is

$$\sum_{k=0}^{n} \binom{n}{k}\, x^{\overline{k}} \in R[x],$$

where $x^{\overline{k}} = x(x+1)\cdots(x+k-1)$ is the rising factorial polynomial.

It is the terminating hypergeometric series ${}_2F_0(-n, x; ; -1)$, an unsigned version of the
Charlier polynomials of order 0, and its coefficient array is the exponential Riordan array
$[e^x, \ln(1/(1-x))]$.

Formalized by `MetaMathlibExt.unsignedCharlierOrder0`, a definition declared in [MathlibExt/Algebra/Polynomial/UnsignedCharlierPolynomialsOfOrder0.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Polynomial/UnsignedCharlierPolynomialsOfOrder0.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/charlier-polynomials/index.html#unsigned-charlier-order0).

## Unsigned Charlier coefficient

For natural numbers $n$ and $m$, the unsigned Charlier
coefficient is the natural number

$$c(n, m) = \sum_{k=0}^{n} \binom{n}{k}\, [x^m]\, x^{\overline{k}},$$

where $x^{\overline{k}} = x(x+1)\cdots(x+k-1)$ is the rising factorial polynomial over
$\mathbb{N}$ and $[x^m]$ denotes the coefficient of $x^m$.

Formalized by `MetaMathlibExt.unsignedCharlierCoeff`, a definition declared in [MathlibExt/Algebra/Polynomial/UnsignedCharlierPolynomialsOfOrder0.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Polynomial/UnsignedCharlierPolynomialsOfOrder0.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/charlier-polynomials/index.html#unsigned-charlier-coeff).

## Coefficients of the unsigned Charlier polynomials

For all natural numbers $n$ and $m$,
the coefficient of $x^m$ in the $n$-th unsigned Charlier polynomial of order $0$ over $\mathbb{N}$
equals the unsigned Charlier coefficient $c(n, m)$.

Formalized by `MetaMathlibExt.unsignedCharlier_coeff_eq`, a theorem declared in [MathlibExt/Algebra/Polynomial/UnsignedCharlierPolynomialsOfOrder0.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Polynomial/UnsignedCharlierPolynomialsOfOrder0.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/charlier-polynomials/index.html#unsigned-charlier-coeff-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Charlier polynomials](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/charlier-polynomials/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Algebra/orthogonal-polynomials/charlier-polynomials)
