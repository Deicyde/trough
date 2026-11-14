# Composition and product

- [Composition-product](def-kernel-compprod.md)

As for all other kernel definitions in this section, we omit the proof that this indeed defines a kernel and refer the reader to the Mathlib implementation.

TODO: explanation of that composition-product on an example.

The name *composition-product* is not standard in the literature, where it can be called either composition or product depending on the source. We reserve the name *composition* for an operation that from kernels $\mathcal X \rightsquigarrow \mathcal Y$ and $\mathcal Y \rightsquigarrow \mathcal Z$ produces a kernel $\mathcal X \rightsquigarrow \mathcal Z$, and the name product for the one that takes kernels $\mathcal X \rightsquigarrow \mathcal Y$ and $\mathcal X \rightsquigarrow \mathcal Z$ and produces a kernel $\mathcal X \rightsquigarrow (\mathcal Y \times \mathcal Z)$. Both are special cases of the composition-product, which justifies that name.

The composition-product is defined for $\kappa : \mathcal X \rightsquigarrow \mathcal Y$ and $\eta : \mathcal X \times \mathcal Y \rightsquigarrow \mathcal Z$, but since a kernel $\mathcal Y \rightsquigarrow \mathcal Z$ can be seen as a kernel $\mathcal X \times \mathcal Y \rightsquigarrow \mathcal Z$ independent of the first coordinate, we abuse notation and also write $\kappa \otimes \xi$ for $\xi : \mathcal Y \rightsquigarrow \mathcal Z$.

Since a measure is a constant kernel from the space with one element, we can also define the composition-product of a measure and a kernel. Note that this definition uses the abuse of notation we just introduced.

- [Composition-product of a measure and a kernel](def-measure-compprod.md)
- [Composition](def-kernel-comp.md)

We can also define the composition of a measure and a kernel, by $\kappa \circ \mu = (\kappa \circ \mu_k) (u)$, where $\mathcal U$ is a measurable space with a unique element $u$ and $\mu_k : \mathcal U \rightsquigarrow \mathcal X$ is the constant kernel with value $\mu$.

- [Product](def-kernel-prod.md)

For $\kappa : \mathcal X \rightsquigarrow \mathcal Y$ and $\eta : \mathcal Y \rightsquigarrow \mathcal Z$ (independent of $\mathcal X$), the composition-product can be written as a composition: $\kappa \otimes \eta = (d_{\text{id}} \times \eta) \circ \kappa$ where $d_{\text{id}}$ is the deterministic kernel for the identity. In particular, the composition-product of a measure and a kernel $\kappa$ is the composition of that measure with the kernel $d_{\text{id}} \times \kappa$.

- [Parallel product](def-kernel-parallel-prod.md)
