---
declaration: section
origin: cited
lean: MetaMathlibExt.BasicHypergeometric.basicHypergeometricCoefficient, MetaMathlibExt.BasicHypergeometric.basicHypergeometricSeries, MetaMathlibExt.BasicHypergeometric.basicHypergeometricCoefficient_phi_succ
statement: formalized
proof: formalized
---

# Basic hypergeometric series

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/hypergeometric-functions/basic-hypergeometric-series/index.html).

## Coefficients of the basic hypergeometric series

Let $r$ and $s$ be natural numbers, let
$a_1, \dots, a_r$, $b_1, \dots, b_s$ and $q$ be complex numbers, and write
$(x;q)_n = \prod_{j=0}^{n-1} (1 - x q^j)$ for the finite $q$-Pochhammer symbol, so that
$(q;q)_n = \prod_{j=0}^{n-1} (1 - q^{j+1})$. For a natural number $n$, the coefficient of $z^n$ in
the basic hypergeometric series ${}_r\phi_s(a_1, \dots, a_r; b_1, \dots, b_s; q, z)$ is

$$\frac{(a_1;q)_n \cdots (a_r;q)_n}{(q;q)_n\,(b_1;q)_n \cdots (b_s;q)_n}
\left((-1)^n q^{\binom{n}{2}}\right)^{1+s-r},$$

where the exponent $1 + s - r$ is an integer and may be negative. This is DLMF 17.4.1, which is
written for $r + 1$ upper parameters, restated for $r$ upper parameters.

No condition on the parameters is imposed: division by zero gives $0$, and so does every negative
power of $0$. Analytic applications must separately establish that the denominator does not
vanish.

Formalized by `MetaMathlibExt.BasicHypergeometric.basicHypergeometricCoefficient`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/BasicHypergeometric.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/BasicHypergeometric.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/hypergeometric-functions/basic-hypergeometric-series/index.html#basic-hypergeometric-coefficient).

## Basic hypergeometric series

Let $r$ and $s$ be natural numbers and let
$a_1, \dots, a_r$, $b_1, \dots, b_s$ and $q$ be complex numbers. The basic hypergeometric series
${}_r\phi_s(a_1, \dots, a_r; b_1, \dots, b_s; q, z)$ is the formal power series in $z$ over
$\mathbb{C}$ whose coefficient of $z^n$, for each natural number $n$, is the $n$-th basic
hypergeometric coefficient of these parameters.

Formalized by `MetaMathlibExt.BasicHypergeometric.basicHypergeometricSeries`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/BasicHypergeometric.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/BasicHypergeometric.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/hypergeometric-functions/basic-hypergeometric-series/index.html#basic-hypergeometric-series).

## Coefficients of the series ${}_{s+1}\phi_s$

Let $s$ be a natural number, let
$a_1, \dots, a_{s+1}$, $b_1, \dots, b_s$ and $q$ be complex numbers, and write
$(x;q)_n = \prod_{j=0}^{n-1} (1 - x q^j)$ for the finite $q$-Pochhammer symbol, so that
$(q;q)_n = \prod_{j=0}^{n-1} (1 - q^{j+1})$. For every natural number $n$, the coefficient of $z^n$
in the basic hypergeometric series ${}_{s+1}\phi_s(a_1, \dots, a_{s+1}; b_1, \dots, b_s; q, z)$ is

$$\frac{(a_1;q)_n \cdots (a_{s+1};q)_n}{(q;q)_n\,(b_1;q)_n \cdots (b_s;q)_n}.$$

With $r = s + 1$ upper parameters, the exponent $1 + s - r$ of the normalization factor
$\left((-1)^n q^{\binom{n}{2}}\right)^{1+s-r}$ is $0$, so the factor disappears. As in the
definition of the coefficient, division by zero gives $0$.

Formalized by `MetaMathlibExt.BasicHypergeometric.basicHypergeometricCoefficient_phi_succ`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/BasicHypergeometric.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/BasicHypergeometric.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/hypergeometric-functions/basic-hypergeometric-series/index.html#basic-hypergeometric-coefficient-phi-suc).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Basic hypergeometric series](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/hypergeometric-functions/basic-hypergeometric-series/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/special-functions/hypergeometric-functions/basic-hypergeometric-series)
