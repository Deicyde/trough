# Mertens' theorems

In this section we give explicit versions of Mertens' theorems:

- Mertens' first theorem (von Mangoldt form): $\sum_{n \leq x} \frac{\Lambda(n)}{n} = \log x + O(1)$.
- Mertens' first theorem (prime form): $\sum_{p \leq x} \frac{\log p}{p} = \log x + O(1)$.
- Mertens' second theorem (von Mangoldt form): $\sum_{n \leq x} \frac{\Lambda(n)}{n \log n} = \log \log x + \gamma + O(1/\log x)$.
- Mertens' second theorem (prime form): $\sum_{p \leq x} \frac{1}{p} = \log \log x + M + O(1/\log x)$, where $M$ is the Meissel-Mertens constant.
- Mertens' third theorem: $\prod_{p \leq x} (1 - \frac{1}{p}) = e^{-\gamma}/\log x + O(1/\log^2 x)$.

We aim to upstreaming these results to Mathlib. In particular, the arguments here should be self-contained and written for efficiency, coherency, and clarity. As such, extensive use of AI tools is *strongly discouraged* in this section.

The arguments here are drawn from Leo Goldmakher's “A quick proof of Mertens' theorem” from https://web.williams.edu/Mathematics/lg5/mertens.pdf

The unfinished formalization of Mertens' theorems by Arend Mellendijk in https://github.com/FLDutchmann/Analytic/blob/main/Analytic/Mertens.lean may also be relevant here.

## [Partial sum of logarithm… to Integral form for second error…](part-01/README.md)

- [Partial sum of logarithm identity](part-01/mertens-sum-log.md)
- [Partial sum of logarithm upper bound](part-01/mertens-sum-log-le.md)
- [Partial sum of logarithm lower bound](part-01/mertens-sum-log-ge.md)
- [Partial sum of logarithm as logarithm of factorial](part-01/mertens-sum-log-eq-log-factorial.md)
- [Partial sum of logarithm as sum of $\Lambda(d)/d$](part-01/mertens-sum-log-eq-sum-mangoldt.md)
- [The remainder term in Mertens first theorem (von Mangoldt form)](part-01/mertens-first-error-mangoldt.md)
- [Partial sum of $\Lambda(d)/d$ lower bound](part-01/mertens-first-error-mangoldt-ge.md)
- [Partial sum of $\Lambda(d)/d$ upper bound](part-01/mertens-first-error-mangoldt-le.md)
- [Mertens' first theorem (von Mangoldt form)](part-01/mertens-first-theorem-mangoldt.md)
- [The remainder term in Mertens first theorem (prime form)](part-01/mertens-first-error-prime.md)
- [Prime error for Mertens first theorem bounded by von Mangoldt error](part-01/mertens-first-error-prime-le-mangoldt.md)
- [Partial sum of $\frac{\log p}{p}$ upper bound](part-01/mertens-first-error-prime-le.md)
- [$E_1$ summable](part-01/e1-summable.md)
- [Upper bound on $E_1$](part-01/e1-bound.md)
- [Partial sum of $\frac{\log p}{p}$ lower bound](part-01/mertens-first-error-prime-ge.md)
- [Error term in Mertens' first theorem bounded (prime form)](part-01/mertens-first-theorem-prime-bounded.md)
- [Alternate Formula for Euler-Mascheroni constant](part-01/euler-mascheroni-const-alt.md)
- [The remainder term in Mertens second theorem (von Mangoldt form)](part-01/mertens-second-error-mangoldt.md)
- [Integral identity involving inverse log weight](part-01/mertens-integral-ident.md)
- [Integral form for second error (von Mangoldt form)](part-01/mertens-second-error-mangoldt-eq.md)

## [Bound for second Mertens error… to Mertens' third theorem error…](part-02/README.md)

- [Bound for second Mertens error (von Mangoldt form)](part-02/mertens-second-error-mangoldt-bound.md)
- [Dirichlet series for $\log \zeta(s)$](part-02/log-zeta-eq-1.md)
- [Integration by parts identity for $\log \zeta(s)$](part-02/log-zeta-eq-2.md)
- [First integral identity](part-02/log-zeta-eq-3.md)
- [Second integral identity](part-02/log-zeta-eq-4.md)
- [An identity for $\log \zeta(s)$](part-02/log-zeta-eq.md)
- [limiting behavior of log zeta](part-02/log-zeta-limit.md)
- [Compatibility with Mathlib Euler-Mascheroni constant](part-02/euler-mascheroni-eq.md)
- [Mertens' second theorem (weak von Mangoldt form)](part-02/mertens-second-theorem-mangoldt-weak.md)
- [The Meissel-Mertens constant](part-02/meissel-mertens-constant.md)
- [Upper bound for $M$](part-02/mertens-second-constant-prime-le.md)
- [Lower bound for $M$](part-02/mertens-second-constant-prime-ge.md)
- [Integral form for second error (prime form)](part-02/mertens-second-error-prime-eq.md)
- [Bound for second error (prime form)](part-02/mertens-second-error-prime-abs-le.md)
- [Mertens' second theorem (weak prime form)](part-02/mertens-second-theorem-prime-weak.md)
- [Formula for Meissel-Mertens constant](part-02/meissel-mertens-eq.md)
- [The remainder term in Mertens third theorem](part-02/mertens-third-error.md)
- [Mertens' third theorem error term](part-02/mertens-third-theorem-error.md)
- [Mertens' third theorem error bound](part-02/mertens-third-theorem-error-le.md)
