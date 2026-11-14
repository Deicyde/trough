# Comparing the two endings

The L²/Koopman ending ([Conditional independence extension](thm-condindep-extension.md), in `CommonEnding.lean`) and the martingale ending ([Finite product formula](../../main-implication-contractable-implies-conditiona/via-martingale-aldous-proof/lem-finite-product-formula.md), in `ViaMartingale/FiniteProduct.lean`) are similar in total length and both finish with a rectangle $\pi$-system extension via `MeasureTheory.ext_of_generate_finite`. The substantive difference is the *shape of the bridge condition* each accepts about the directing kernel $\nu$.

| **Route** | **Bridge shape** | **How the route produces it** |
| --- | --- | --- |
| Martingale | Per-coordinate conditional-expectation equality: $(\omega \mapsto \nu(\omega)(B).\mathrm{toReal}) \, =^{\mathrm{a.e.}} \, \mathbb{E}[\mathbf{1}_B \circ X_n \mid \mathcal{T}]$ for every $n$, $B$ (see [Conditional law of $X_n$ equals directing measure](../../main-implication-contractable-implies-conditiona/via-martingale-aldous-proof/lem-conditional-law-eq-directingmeasure.md)). | Falls out directly from mathlib's `condExpKernel` applied to the tail $\sigma$-algebra. |
| [0.7em] L²/Koopman | Joint integral equality on the whole $m$-tuple: for every injective $k : \mathrm{Fin}\,m \to \mathbb{N}$ and rectangle $B$, $\int^- \prod_i \mathbf{1}_{X_{k\,i} \in B_i}\,d\mu = \int^- \prod_i \nu(\omega)(B_i)\,d\mu.$ | Falls out of Cesàro / ergodic averaging — both sides are limits of the same averaged sequence. |

Why this matters. Each route's directing-measure construction naturally produces the bridge shape its own ending expects, so the routes pick the ending that matches what they already have. The martingale route's per-coordinate bridge is “smaller” (one σ-algebra-relative equality per index) and is what `condExpKernel` delivers without extra work; the common ending's joint integral bridge is what limit-of-averages arguments deliver without extra work, but would be wasteful if you already had per-coordinate CE equalities. At the stitching level both routes compress to a short top-level theorem that hands a 4-tuple $(\nu, h_{\nu\text{-prob}}, h_{\nu\text{-meas}}, h_{\text{bridge}})$ to the chosen ending — the choice of ending is what differs, not the amount of stitching.

- [$\pi$-system uniqueness](lem-pi-system.md)
- [Monotone class theorem](thm-monotone-class.md)
- [Conditional independence extension](thm-condindep-extension.md)
