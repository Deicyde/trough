# Via Koopman (Mean Ergodic Theorem)

The Koopman approach uses the Mean Ergodic Theorem via the shift operator on L$^2$. This is Kallenberg's “first proof” and uses disjoint-block averaging.

**Scope note:** the Koopman route is currently stated for real-valued sequences (the Mean Ergodic Theorem is invoked through L$^2(\mu; \mathbb{R})$ on path space). Generalising to standard Borel targets would require an L$^2$-valued ergodic infrastructure beyond what is presently formalised. The default project export ([de Finetti–Ryll-Nardzewski equivalence (martingale route)](../../main-theorem/thm-definetti.md)) handles general standard Borel spaces via the martingale route.

## Block Averages and Ergodic Theory

- [Block average](def-blockavg.md)
- [Koopman-condexp commutation](lem-koopman-condexp-comm.md)
- [Birkhoff averages converge to condexp](thm-birkhoff-condexp.md)
- [Block averages converge in $L^1$](lem-blockavg-tendsto.md)

## Contractability and Factorization

- [Conditional expectation lag constancy from exchangeability](lem-condexp-lag-const.md)
- [Integral product equals block average product](lem-integral-prod-blockavg.md)
- [Product block average L$^1$ convergence](lem-product-blockavg-l1.md)
- [Conditional expectation product factorization](thm-condexp-product-factorization.md)
- [Bridge from contractability](lem-indicator-product-bridge-contractable.md)
- [Contractable implies Conditionally i.i.d. (via Koopman)](thm-conditionallyiid-of-contractable-koopman.md)
