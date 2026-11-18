# TwoHDM

The folder [Physlib/Particles/BeyondTheStandardModel/TwoHDM/](https://github.com/leanprover-community/physlib/tree/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM): 3 modules, an article each, in path order with Basic.lean first in its folder.

The repository's API map for this folder, *Two Higgs Doublet Model* ([Physlib/Particles/BeyondTheStandardModel/TwoHDM/API-map.md](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/API-map.md)): its Content section, with the sentences it marks as not yet formalized left out (…). A citation \[n\] links the module its n-th Lean reference names.

*Content (Alpha)*

> ### Configurations and the gauge action
>
> A configuration of the two Higgs doublet model is a pair of Higgs vectors \{1}. [\[1\]](basic.md) The global gauge group of the Standard Model acts on such a pair. [\[2\]](basic.md) …
>
> ### Gram matrix and Gram vector
>
> The Gram matrix of a configuration is self-adjoint, with nonnegative determinant and trace. [\[3\]](grammatrix.md) Two configurations lie in the same gauge orbit exactly when they have the same Gram matrix. [\[4\]](grammatrix.md) Conversely, every self-adjoint matrix with nonnegative determinant and trace is the Gram matrix of some configuration. [\[5\]](grammatrix.md) Expanding the Gram matrix in the basis of Pauli matrices gives the Gram vector, which likewise characterizes gauge orbits and is surjective onto the vectors satisfying the corresponding constraints. [\[6\]](grammatrix.md)
>
> ### The potential and its stability
>
> The potential is parameterized following the convention of \{2}; these parameters are related to the reparameterization adapted to the Gram vector used in \{3}. [\[7\]](potential.md) The potential of the two Higgs doublets is the sum of a mass term and a quartic term. [\[8\]](potential.md) The potential, and each of its two terms, is invariant under the global gauge group. [\[9\]](potential.md) Each of them is a function of the Gram vector alone. [\[10\]](potential.md)
>
> The potential is stable when it is bounded below. Stability is characterized through the reduced mass and quartic terms, functions on the unit ball of normalized Gram-vector directions: the reduced quartic term is nonnegative there and, wherever the reduced mass term is negative, its square is bounded by a fixed multiple of the reduced quartic term. [\[11\]](potential.md) Strong stability, the positivity of the reduced quartic term, implies stability. [\[12\]](potential.md) The stability arguments follow, in part, those of \{3}, but one of its steps is false: there is an unstable potential whose reduced quartic term is nonnegative, and whose reduced mass term is nonnegative wherever the reduced quartic term vanishes. [\[13\]](potential.md)

Its references:

> - \{1\} Higgs field API map — [Physlib/Particles/StandardModel/HiggsBoson/API-map.md](../../standardmodel/higgsboson/README.md)
> - \{2\} arXiv:1605.03237, https://arxiv.org/abs/1605.03237
> - \{3\} arXiv:hep-ph/0605184, https://arxiv.org/abs/hep-ph/0605184

- [The Two Higgs Doublet Model](basic.md)
- [The gram matrix for the two Higgs doublet model](grammatrix.md)
- [The potential of the Two Higgs doublet model](potential.md)
