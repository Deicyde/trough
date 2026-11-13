---
declaration: section
origin: cited
lean: MetaMathlibExt.chebyshevU_coeff_eq_binomial_sum, MetaMathlibExt.GeneralizedChebyshevSecondKind.P, MetaMathlibExt.GeneralizedChebyshevSecondKind.Q, MetaMathlibExt.GeneralizedChebyshevSecondKind.Q_recurrence
statement: formalized
proof: formalized
---

# Chebyshev polynomials of the second kind

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/chebyshev-polynomials-of-the-second-kind/index.html).

## Coefficients of the Chebyshev polynomials of the second kind

Let $U_n \in \mathbb{Z}[x]$
denote the $n$-th Chebyshev polynomial of the second kind, and let $k \le n$ be natural numbers.
If $n$ and $k$ have the same parity, the coefficient of $x^k$ in $U_n$ is
$(-1)^{(n-k)/2} \sum_{i=0}^{k} \binom{(n+k)/2}{i} \binom{(n+k)/2 - i}{(n-k)/2}$;
otherwise it is $0$.

## Sources

- Milan Janjić, "On a Class of Polynomials with Integer Coefficients", Journal of Integer Sequences 11 (2008), Article 08.5.2, Corollary lines 441-446, <https://cs.uwaterloo.ca/journals/JIS/VOL11/Janjic/janjic19.tex>.

Formalized by `MetaMathlibExt.chebyshevU_coeff_eq_binomial_sum`, a theorem declared in [MathlibExt/Algebra/Polynomial/ChebyshevUCoefficients.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Polynomial/ChebyshevUCoefficients.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/chebyshev-polynomials-of-the-second-kind/index.html#chebyshev-u-coeff-eq-binomial-sum).

## Modified Chebyshev base polynomials of the second kind

For a commutative ring $R$ and
$r, s \in R$, the polynomials $P_n \in R[x]$, $n \ge 0$, are defined by $P_0 = 1$,
$P_1 = x - r$ and $P_{n+2} = (x - r) P_{n+1} - s P_n$ for every $n \ge 0$.

Formalized by `MetaMathlibExt.GeneralizedChebyshevSecondKind.P`, a definition declared in [MathlibExt/Algebra/Polynomial/GeneralizedChebyshevSecondKind.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Polynomial/GeneralizedChebyshevSecondKind.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/chebyshev-polynomials-of-the-second-kind/index.html#p).

## Generalized Chebyshev polynomials of the second kind

For a commutative ring $R$ and
$r, s, \lambda, \mu \in R$, let $P_n \in R[x]$ be the modified Chebyshev base polynomials
with parameters $r, s$. The polynomials $Q_n \in R[x]$ are defined by $Q_0 = 1$,
$Q_1 = P_1 - \lambda P_0$ and $Q_{n+2} = P_{n+2} - \lambda P_{n+1} - \mu P_n$
for every $n \ge 0$.

Formalized by `MetaMathlibExt.GeneralizedChebyshevSecondKind.Q`, a definition declared in [MathlibExt/Algebra/Polynomial/GeneralizedChebyshevSecondKind.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Polynomial/GeneralizedChebyshevSecondKind.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/chebyshev-polynomials-of-the-second-kind/index.html#q).

## Three-term recurrence for generalized Chebyshev polynomials

For a commutative ring $R$,
all $r, s, \lambda, \mu \in R$ and every $n \ge 0$, the generalized Chebyshev polynomials of
the second kind $Q_n \in R[x]$ with parameters $r, s, \lambda, \mu$ satisfy
$Q_{n+3} = (x - r) Q_{n+2} - s Q_{n+1}$.

No hypothesis on $\mu$ is needed because the recurrence starts at $Q_3$; the analogous
identity $Q_2 = (x - r) Q_1 - s Q_0$ holds only when $\mu = 0$.

Formalized by `MetaMathlibExt.GeneralizedChebyshevSecondKind.Q_recurrence`, a theorem declared in [MathlibExt/Algebra/Polynomial/GeneralizedChebyshevSecondKind.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Polynomial/GeneralizedChebyshevSecondKind.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/chebyshev-polynomials-of-the-second-kind/index.html#q-recurrence).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Chebyshev polynomials of the second kind](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/chebyshev-polynomials-of-the-second-kind/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Algebra/orthogonal-polynomials/chebyshev-polynomials-of-the-second-kind)
