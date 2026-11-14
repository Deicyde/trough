# Kernel Radon-Nikodym derivative

In standard Borel spaces, we can define a Radon-Nikodym derivative for finite kernels. This is a measurable function $\frac{d \kappa}{d \eta} : \mathcal X \times \mathcal Y \to \mathbb{R}_{+, \infty}$ with $\kappa = \frac{d \kappa}{d \eta} \cdot \eta + \kappa_{\perp \eta}$, where for all $x$, $\kappa_{\perp \eta}(x) \perp \eta(x)$. The hypothesis that the spaces are standard Borel is used to ensure the measurability of the function on the product space. Taking for all $x$ the ratio $\frac{d \kappa(x)}{d \eta(x)}$ would give us measurable function $\mathcal Y \to \mathbb{R}_{+, \infty}$ for all $x \in \mathcal X$, but not necessarily a jointly measurable function.

- [kernel_rnDeriv](def-kernel-rnderiv.md)
- [rnDeriv_unique](lem-rnderiv-unique.md)
- [rnDeriv_value](cor-rnderiv-value.md)
