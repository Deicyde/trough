# Definition

- [Giry monad](../../../mathlib/overview/analysis/measures-and-integral-calculus/part-01/giry-monad.md)

It then makes sense to talk about a measurable function from a measurable space $\mathcal X$ to the measures on another measurable space $\mathcal Y$. We now write more explicitly what it means for such a function to be measurable.

- [measurable_measure_fun](lem-measurable-measure-fun.md)

We now have the tools needed to define probability transition kernels.

- [Kernel](def-kernel.md)

Measures and measurable functions are special cases of kernels. A measure on $\mathcal Y$ can be seen as a constant kernel from any space to $\mathcal Y$ (for example from a space with 1 element to $\mathcal Y$). A measurable function can be represented by a *deterministic* kernel.

- [Deterministic kernel](def-deterministic-kernel.md)

A few deterministic kernels are particularly useful.

- The identity kernel, deterministic kernel given by the identity function.
- The copy kernel $c_{\mathcal X} : \mathcal X \rightsquigarrow \mathcal X \times \mathcal X$, from the function $x \mapsto (x, x)$.
- The discard kernel $d_{\mathcal X}$ (TODO: conflicts with deterministic kernel notation). This is a kernel from $\mathcal X$ to $*$, the space with one point, corresponding to the constant function.

Kernels can be described by the integrals of measurable functions, as demonstrated in the following extensionality theorem.

- [kernel_ext](thm-kernel-ext.md)
