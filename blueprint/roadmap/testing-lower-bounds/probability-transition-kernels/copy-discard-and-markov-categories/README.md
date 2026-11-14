# Copy-discard and Markov categories

Measurable spaces and s-finite kernels are a copy-discard category (and in particular a symmetric monoidal category) with the following data:

- Objects: measurable spaces
- Morphisms: s-finite kernels, with identity kernels and composition of kernels
- Tensor product of objects: product of measurable spaces $\mathcal X \times \mathcal Y$
- Tensor product of morphisms: parallel product $\kappa \parallel \eta$
- Unit: measurable space with one element (denoted by $*$)
- The associator, left and right unitors and braiding are given by the deterministic kernels of the corresponding equivalences between measurable spaces
- Copy morphism: $c_{\mathcal X}: \mathcal X \rightsquigarrow \mathcal X \times \mathcal X$
- Delete morphism: $d_{\mathcal X} : \mathcal X \rightsquigarrow *$

If we restrict the morphisms to Markov kernels, we get a Markov category (TODO ref), which is a copy-discard category in which for every morphism $\kappa$, $d_{\mathcal Y} \circ \kappa = d_{\mathcal X}$.

In that view of transition kernels, the following operations are not primitive, but derived from others:

- Product: for $\kappa : \mathcal X \rightsquigarrow \mathcal Y$ and $\eta : \mathcal X \rightsquigarrow \mathcal Z$, $\kappa \times \eta = (\kappa \parallel \eta) \circ c_{\mathcal X}$
- Composition-product: for $\kappa : \mathcal X \rightsquigarrow \mathcal Y$ and $\eta : \mathcal X \times \mathcal Y \rightsquigarrow \mathcal Z$, $\kappa \otimes \eta = \mathrm{swap_{\mathcal Z, \mathcal Y}} \circ (\eta \parallel \mathrm{id}) \circ \alpha_{\mathcal X, \mathcal Y, \mathcal Y} \circ (\mathrm{id} \parallel c_{\mathcal Y}) \circ (\mathrm{id} \parallel \kappa) \circ c_{\mathcal X}$ (where $\alpha$ is the associator and $\mathrm{swap}$ is the braiding).
