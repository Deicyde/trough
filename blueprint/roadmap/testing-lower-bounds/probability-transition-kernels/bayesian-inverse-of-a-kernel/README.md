# Bayesian inverse of a kernel

- [bayesInv](def-bayesinv.md)

The bayesian interpretation of this definition is that $\mu$ represents a prior over a parameter and $\kappa$ gives the distribution of data given the parameter. $\kappa \circ \mu$ is the distribution of the data, and $\kappa_\mu^\dagger$ gives the posterior distribution of the parameter given the data.

The measure $\rho = \mu \otimes \kappa$ is a joint probability distribution over $\mathcal X \times \mathcal Y$ with marginals $\rho_X = \mu$ and $\rho_Y = \kappa \circ \mu$ (if $\kappa$ is Markov). By construction, that joint probability distribution can be written as the composition-product of the first marginal $\rho_X$ and a kernel $\kappa$. The Bayesian inverse, if it exists, gives a way to write the joint as a composition-product of the second marginal $\rho_Y$ and a kernel.

If the joint space is such that every product distribution can be disintegrated (see Theorem [Disintegration in standard Borel spaces](../disintegration/thm-disintegration.md)), then the Bayesian inverse exists.

- [Existence of the Bayesian inverse](lem-exists-bayesinv.md)

See (Clerc et al. 2017) and (Dahlqvist et al. 2018) for a category theory point of view on Bayesian inversion.

- [a.e.-uniqueness of the Bayesian inverse](lem-eq-bayesinv-of-compprod-eq.md)
- [bayesInv_comp_self](lem-bayesinv-comp-self.md)
- [bayesInv_self](lem-bayesinv-self.md)
- [bayesInv_id](lem-bayesinv-id.md)
- [bayesInv_comp](lem-bayesinv-comp.md)
- [rnDeriv_bayesInv](lem-rnderiv-bayesinv.md)

If $\mathcal{X}$ is countable, then we do have $\kappa(x) \ll \kappa \circ \mu$ almost surely.

*The proof of [Lemma rnDeriv_bayesInv](lem-rnderiv-bayesinv.md) is shown with its statement.*
