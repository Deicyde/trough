---
declaration: section
origin: cited
lean: MetaMathlibExt.polynomialQuadrinomialCoeff, MetaMathlibExt.zhangVSum, MetaMathlibExt.quadrinomialCoeff, MetaMathlibExt.quadrinomialCoeff_eq_zhangVSum
statement: formalized
proof: formalized
---

# Quadrinomial coefficients

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/quadrinomial-coefficients/index.html).

## Quadrinomial coefficient triangle

For natural numbers $n$ and $k$, the quadrinomial
coefficient $\binom{n}{k}_4$ is the coefficient of $x^k$ in the polynomial
$(1 + x + x^2 + x^3)^n$ with natural-number coefficients. These numbers form the triangle
OEIS A008287.

Formalized by `MetaMathlibExt.polynomialQuadrinomialCoeff`, a definition declared in [MathlibExt/Combinatorics/Enumerative/QuadrinomialCoefficient.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/QuadrinomialCoefficient.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/quadrinomial-coefficients/index.html#polynomial-quadrinomial-coeff).

## Zhang's six-parameter binomial sum

For natural numbers $n$, $r_1$, $r_2$, $s$, $t$, $u$,
Zhang's binomial sum is

$$
V(n, r_1, r_2, s, t, u) = \sum_{k=0}^{n} \binom{n}{k}^{r_1} \binom{n}{2k}^{r_2}
\binom{n+k}{k}^{s} \binom{2k}{k}^{t} \binom{2(n-k)}{n-k}^{u}.
$$

The source uses the convention $0^0 = 1$, which is also Lean's convention for natural-number
powers.

Formalized by `MetaMathlibExt.zhangVSum`, a definition declared in [MathlibExt/Combinatorics/Enumerative/QuadrinomialCoefficients.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/QuadrinomialCoefficients.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/quadrinomial-coefficients/index.html#zhang-vsum).

## Quadrinomial sequence A005725

For a natural number $n$, the quadrinomial number is
$Q(n) = \sum_{k=0}^{n} \binom{n}{k} \binom{n}{2k}$. This is OEIS sequence A005725.

Formalized by `MetaMathlibExt.quadrinomialCoeff`, a definition declared in [MathlibExt/Combinatorics/Enumerative/QuadrinomialCoefficients.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/QuadrinomialCoefficients.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/quadrinomial-coefficients/index.html#quadrinomial-coeff).

## Quadrinomial numbers as a specialization of Zhang's V-sum

For every natural number $n$,
the quadrinomial number $Q(n) = \sum_{k=0}^{n} \binom{n}{k} \binom{n}{2k}$ equals Zhang's
six-parameter binomial sum $V(n, 1, 1, 0, 0, 0)$.

Formalized by `MetaMathlibExt.quadrinomialCoeff_eq_zhangVSum`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/QuadrinomialCoefficients.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/QuadrinomialCoefficients.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/quadrinomial-coefficients/index.html#quadrinomial-coeff-eq-zhang-vsum).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Quadrinomial coefficients](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/quadrinomial-coefficients/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/quadrinomial-coefficients)
