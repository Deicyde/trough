---
declaration: lemma
origin: cited
lean: ProbabilityTheory.isProjectiveMeasureFamily_gaussianProjectiveFamily
statement: formalized
proof: formalized
---

# isProjectiveMeasureFamily_gaussianProjectiveFamily

The projective family of the Brownian motion is a projective family of measures.

## Depends on

- [Projective family of the Brownian motion](def-gaussianprojectivefamily.md)
- [Projective family](../kolmogorov-extension-theorem/def-isprojectivemeasurefamily.md)

## Proof depends on

- [isGaussian_multivariateGaussian](../../gaussian-distributions/gaussian-measures/part-02/lem-isgaussian-multivariategaussian.md)
- [covMatrix_map](../../characteristic-function-and-covariance/covariance/lem-covmatrix-map.md)
- [integral_id_multivariateGaussian](../../gaussian-distributions/gaussian-measures/part-02/lem-integral-id-multivariategaussian.md)
- [covMatrix_multivariateGaussian](../../gaussian-distributions/gaussian-measures/part-02/lem-covmatrix-multivariategaussian.md)
- [IsGaussian.ext_iff](../../gaussian-distributions/gaussian-measures/part-01/lem-isgaussian-ext-iff.md)

## Proof

Let $J \subseteq I$ be finite subsets of $\mathbb{R}_+$. We need to show that the restriction from $\mathbb{R}^I$ to $\mathbb{R}^J$ (denote it by $\pi_{IJ}$) maps $P^B_I$ to $P^B_J$.

The restriction is a continuous linear map from $\mathbb{R}^I$ to $\mathbb{R}^J$. The map of a Gaussian measure by a continuous linear map is Gaussian (Lemma [isGaussian_map](../../gaussian-distributions/gaussian-measures/part-01/lem-isgaussian-map.md)). It thus suffices to show that the mean and covariance matrix of the map are equal to the ones of $P^B_J$ by Lemma [IsGaussian.ext_iff](../../gaussian-distributions/gaussian-measures/part-01/lem-isgaussian-ext-iff.md).

The mean of the map is $0$, since the mean of $P^B_I$ is $0$ and the map is linear.

Let us turn to the covariance matrix. For any $i \in J$, the map $x : \mathbb{R}^I \mapsto \pi_{IJ}(x) i$ is equal to $x : \mathbb{R}^I \mapsto x i$. Let $i, j \in J$. The covariance of $x : \mathbb{R}^J \mapsto x i$ and $x : \mathbb{R}^J \mapsto x j$ with respect to ${\pi_{IJ}}_*P^B_J$ is equal to the covariance of $x : \mathbb{R}^I \mapsto \pi_{IJ}(x) i$ and $x : \mathbb{R}^I \mapsto \pi_{IJ}(x) j$ with respect to $P^B_I$, which is equal to the covariance of $x : \mathbb{R}^I \mapsto x i$ and $x : \mathbb{R}^I \mapsto x i$ with respect to $P^B_I$, which is equal to $t_i \land t_j$. But this is also the covariance of $x : \mathbb{R}^J \mapsto x i$ and $x : \mathbb{R}^J \mapsto x j$ with respect to $P^B_J$, so we are done.

## Lean

Formalized as [`ProbabilityTheory.isProjectiveMeasureFamily_gaussianProjectiveFamily`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.isProjectiveMeasureFamily_gaussianProjectiveFamily).

## Sources

- [Brownian motion blueprint: chapters/projective_family.tex, line 123](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/projective_family.tex#L123)
