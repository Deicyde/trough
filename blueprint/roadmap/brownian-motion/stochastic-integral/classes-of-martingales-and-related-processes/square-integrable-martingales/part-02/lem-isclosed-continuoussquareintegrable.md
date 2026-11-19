---
declaration: lemma
origin: cited
lean: ProbabilityTheory.instIsClosedSquareIntegrableCoeSubmoduleRealContinuousSquareIntegrableOfIsCompleteOfOrderTopology
statement: formalized
proof: formalized
---

# isClosed_continuousSquareIntegrable

The submodule $\mathcal{M}^{2,c}$ is closed in the Hilbert space $\mathcal{M}^2$.

## Depends on

- [continuousSquareIntegrable](def-continuoussquareintegrable.md)

## Proof depends on

- [exists_subsequence_ae_tendsto_uniformly](lem-exists-subsequence-ae-tendsto-uniformly.md)

## Proof

Take $M^{(n)}$ a sequence of continuous square integrable martingales that converges to $N$ in $\mathcal{M}^2$. This means that $\|M^{(n)}_\infty - N_\infty\|$ goes to zero as $n$ goes to infinity, which means that there exists $\phi$ increasing such that, almost surely, $M^{(\phi(n))}_\cdot(\omega)$ converges uniformly to $N_\cdot(\omega)$ as $n$ goes to infinity (Lemma [exists_subsequence_ae_tendsto_uniformly](lem-exists-subsequence-ae-tendsto-uniformly.md)). As each $M^{(\phi(n))}(\omega)$ is continuous, $N(\omega)$ is also continuous.

## Lean

Formalized as [`ProbabilityTheory.instIsClosedSquareIntegrableCoeSubmoduleRealContinuousSquareIntegrableOfIsCompleteOfOrderTopology`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.instIsClosedSquareIntegrableCoeSubmoduleRealContinuousSquareIntegrableOfIsCompleteOfOrderTopology).

## Sources

- [Brownian motion blueprint: chapters/martingale_classes.tex, line 608](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/martingale_classes.tex#L608)
