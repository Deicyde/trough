# Via L$^2$ (Elementary proof)

The L$^2$ approach uses elementary contractability bounds on block averages. This is Kallenberg's “second proof” and has the lightest dependencies.

**Note:** This proof applies to *real-valued* sequences ($X : \mathbb{N} \to \Omega \to \mathbb{R}$) with $L^2$ integrability (i.e., $\mathbb{E}[X_i^2] < \infty$ for all $i$).

## Block Averages and Covariance Structure

- [Block average (L$^2$ version)](def-blockavg-l2.md)
- [Contractable covariance structure](lem-covariance-structure.md)
- [L$^2$ contractability bound](lem-l2-bound.md)

## Cesaro Convergence

Recorded Kallenberg L$^2$ bound. Kallenberg's Lemma 1.2 gives an L$^2$ distance bound for weighted averages of an *exchangeable* sequence. It is recorded in the Lean library as `Exchangeability.DeFinetti.ViaL2.kallenberg_L2_bound` for completeness, but it is not on the active proof path — the route below uses the contractability-only variant [L$^2$ contractability bound](lem-l2-bound.md) so that the proof of Contractable $\Rightarrow$ Conditionally i.i.d. does not assume exchangeability.

- [Block averages are Cauchy in L$^2$](lem-blockavg-cauchy-in-l2.md)
- [Cesaro to conditional expectation (L$^2$)](lem-cesaro-l2.md)
- [Cesaro to conditional expectation (L$^1$)](lem-cesaro-l1.md)

## Directing Measure Construction

The L$^2$ route now goes through mathlib's `condExpKernel` machinery: the Stieltjes construction supplies the candidate directing measure $\omega \mapsto \nu(\omega)$, and a pair of bridge lemmas identifies its push-forward and integral with the kernel coming from mathlib's `condExpKernel` on the tail $\sigma$-algebra. The shared common-ending theorem then lifts the indicator-level identity to the full product $\sigma$-algebra.

- [Directing measure is probability (L$^2$ version)](lem-directing-measure-isprob-l2.md)
- [Directing measure equals condExpKernel push-forward](thm-directing-measure-ae-eq-condexpkernel-map.md)
- [Directing-measure integral equals conditional expectation](lem-directing-measure-integral-eq-condexp.md)
- [Weighted sums converge in L$^1$](thm-weighted-sums-l1.md)
- [Contractable implies Conditionally i.i.d. (via L$^2$)](thm-conditionallyiid-of-contractable-l2.md)
