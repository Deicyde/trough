---
declaration: theorem
origin: cited
lean: ArithmeticFunction.abscissa_powR_le
statement: formalized
proof: formalized
---

# abscissa powR le

The abscissa of absolute convergence of $L(\text{pow}^R(\nu), s)$ is at most $\Re(\nu) + 1$.

## Depends on

- [powR](powr.md)

## Proof

We apply LSeries.abscissaOfAbsConv_le_of_le_const_mul_rpow which states that if there exists a constant $C$ such that $\|f(n)\| \leq C \cdot n^r$ for all $n$ sufficiently large, then the abscissa of absolute convergence of $L(f, s)$ is at most $r + 1$. In our case, we can take $f(n) = n^\nu$ and observe that $\|n^\nu\| = n^{\Re(\nu)}$. Thus, we can choose $C = 1$ and $r = \Re(\nu)$, which gives us the desired result that the abscissa of absolute convergence of $L(\text{pow}^R(\nu), s)$ is at most $\Re(\nu) + 1$.

## Lean

Formalized as [`ArithmeticFunction.abscissa_powR_le`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.abscissa_powR_le).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
