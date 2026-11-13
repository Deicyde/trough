# Operators

The folder [Physlib/QuantumMechanics/Operators/](https://github.com/leanprover-community/physlib/tree/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators): 17 modules, an article each, in path order with Basic.lean first in its folder; then 1 folder below it, a page each, 21 modules in all.

The repository's API map for this folder, *Operator algebra* ([Physlib/QuantumMechanics/Operators/API-map.md](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/API-map.md)), with the sentences it marks as not yet formalized left out (…). A citation \[n\] links the module its n-th Lean reference names.

*Content (Alpha)*

> ### Unbounded operators
>
> An operator on a Hilbert space is a partially defined linear map. It has a dense domain when its domain is a dense subspace, and it is unbounded, in the technical sense used here, when it is densely defined and closable. [\[1\]](unbounded.md) It is symmetric when the inner-product pairing is symmetric on its domain, which happens exactly when the pairing of each vector with its own image is real. [\[2\]](unbounded.md) Symmetry is stable under sums, powers and closures, and a self-adjoint operator is symmetric and closed. [\[3\]](unbounded.md) An operator is essentially self-adjoint when its closure is self-adjoint; such an operator is unbounded, and its closure is its only self-adjoint extension. [\[4\]](unbounded.md)
>
> The adjoint is antitone and conjugate-linear in non-zero scalars, the sum of two adjoints is a restriction of the adjoint of the sum, and likewise for compositions; the adjoint of an unbounded operator is again unbounded, and its second adjoint is its closure. [\[5\]](unbounded.md) A symmetric densely defined operator for which T + i and T - i both have the whole space as range is self-adjoint. [\[6\]](unbounded.md) Conjugation by a unitary preserves formal adjoints, dense domains and surjectivity of T - z. [\[7\]](unbounded.md) … These definitions follow the standard treatments of unbounded operators by Hall \{1}, Reed and Simon \{2}, and Schmüdgen \{3}. The spectrum, the resolvent, the numerical range and spectral measures of these operators belong to spectral theory \{4}.
>
> ### Multiplication operators
>
> A complex function on space \{5} gives a multiplication operator on the Hilbert space on space \{6}, defined on its maximal domain, the vectors whose product with the function is still square-integrable; for an almost everywhere strongly measurable multiplier the operator is densely defined. [\[8\]](multiplication.md) For a bounded multiplier the domain is the whole space, and for a multiplier of temperate growth it contains the Schwartz maps. [\[9\]](multiplication.md) The adjoint of a multiplication operator is multiplication by the conjugate function, so a real multiplier gives a self-adjoint operator; multiplication operators are closed and unbounded. [\[10\]](multiplication.md) They behave predictably under scalar multiples, sums and composition. [\[11\]](multiplication.md)
>
> ### Position and momentum
>
> Each component of the position operator is multiplication by a coordinate, first on Schwartz maps and then as a partially defined operator on the Hilbert space, where it is densely defined, self-adjoint and unbounded. [\[12\]](position.md) Multiplication by a power of the radius, and by its smooth regularization, supplies the multipliers of central potentials; the product stays square-integrable under an explicit condition, and the regularized operators converge to the unregularized one. [\[13\]](position.md)
>
> Each component of the momentum operator is -iℏ∂ᵢ, first on Schwartz maps and then as a partially defined operator, which is densely defined, symmetric and unbounded on the Schwartz submodule; the momentum squared acts on the same domain. [\[14\]](momentum.md) …
>
> ### Commutation relations
>
> Position and momentum satisfy the canonical commutation relation [xᵢ, pⱼ] = iℏ δᵢⱼ on Schwartz maps, and Leibniz rules reduce a commutator of products to commutators of the factors. [\[15\]](commutation.md) The position components commute among themselves, as do the momentum components, and the commutator of a position component with the momentum squared is 2iℏ pᵢ. [\[16\]](commutation.md) A regularized power of the radius commutes with itself and with each position component, and its commutators with a momentum component and with the momentum squared are explicit. [\[17\]](commutation.md)
>
> ### Angular momentum
>
> The components 𝐋ᵢⱼ = xᵢpⱼ - xⱼpᵢ of the angular momentum operator and the scalar 𝐋² act on Schwartz maps; the components are antisymmetric in the two indices and vanish for a repeated index, and the one-, two- and three-dimensional cases each have their own description. [\[18\]](angularmomentum.md) Position and momentum transform as vectors under the angular momenta, which close into the Lie algebra of rotations. [\[19\]](angularmomentum.md) The scalar 𝐋² commutes with every angular momentum component, with the momentum squared and with any regularized power of the radius. [\[20\]](angularmomentum.md)
>
> Each angular momentum component acts on the Hilbert space with dense Schwartz domain, agrees almost everywhere with its action on Schwartz maps, preserves the Schwartz submodule, and is symmetric and closable. [\[21\]](angularmomentum.md) Angular momentum squared acts on the Hilbert space with invariant dense Schwartz domain, equals half the sum of the squares of the components, and is symmetric and closable. [\[22\]](angularmomentum.md) In three dimensions the right-handed Cartesian components act on the invariant Schwartz domain, satisfy the Levi-Civita and cyclic commutation relations, and their three squares sum to angular momentum squared. [\[23\]](angularmomentum-dimthree.md) The ladder operators L± = Lx ± i Ly act on Schwartz maps and on the Hilbert space with invariant dense Schwartz domain, where [Lz, L±] = ±ℏ L± and [L², L±] = 0. [\[24\]](angularmomentum-dimthree.md)
>
> ### Statistics of observables
>
> The expectation value of an observable T in a state ψ is ⟨T⟩ = re ⟪ψ, T ψ⟫, and the centered vector is T ψ - ⟨T⟩ψ; for a symmetric operator the pairing is already real. [\[25\]](stateobservables-expectedvalue.md) The variance is ‖T ψ - ⟨T⟩ψ‖², given for a unit vector and a symmetric operator by the second-order formula ⟨T²⟩ - ⟨T⟩², and the standard deviation is its square root; for a unit vector the variance vanishes exactly when the vector is an eigenvector. [\[26\]](stateobservables-variance.md) A vector is an eigenvector of a partially defined operator when it is a non-zero element of the domain sent to a multiple of itself. [\[27\]](stateobservables-iseigenvector.md) The covariance of two observables in a state is symmetric and reduces to the variance on a single observable. [\[28\]](covariance.md)
>
> The product of the standard deviations of two observables is at least half the size of their expected commutator, in both the Robertson and the Robertson-Schrödinger forms, stated for both a centered and a raw commutator identity. [\[29\]](uncertainty.md) …
>
> These are the textbook notions of Sakurai and Napolitano \{7}, Griffiths and Schroeter \{8}, and Hall \{1}. The uncertainty bounds go back to Robertson \{9} and Schrödinger \{10}.

Its references:

> - \{1\} B. C. Hall, *Quantum Theory for Mathematicians*, Springer (2013), Chapters 9 and 10 (unbounded self-adjoint operators) and Chapter 12 (position, momentum, expectation values and the uncertainty principle).
> - \{2\} M. Reed and B. Simon, *Methods of Modern Mathematical Physics I. Functional Analysis*, Academic Press (1980), Chapter VIII (unbounded operators).
> - \{3\} K. Schmüdgen, *Unbounded Self-Adjoint Operators on Hilbert Space*, Springer (2012), Chapters 1 to 3 (closed, symmetric and self-adjoint operators, and examples 1.3 and 3.8 on multiplication operators).
> - \{4\} Spectral theory API map — [Physlib/QuantumMechanics/Operators/SpectralTheory/API-map.md](spectraltheory/README.md)
> - \{5\} Space API map — [Physlib/SpaceAndTime/Space/API-map.md](../../spaceandtime/space/README.md)
> - \{6\} Hilbert space on space API map — [Physlib/QuantumMechanics/HilbertSpaces/SpaceD/API-map.md](../hilbertspaces/spaced/README.md)
> - \{7\} J. J. Sakurai and J. Napolitano, *Modern Quantum Mechanics*, 2nd ed., Cambridge University Press (2017), Chapter 1 (observables, expectation values, the canonical commutation relation, the uncertainty relation) and Chapter 3 (angular momentum).
> - \{8\} D. J. Griffiths and D. F. Schroeter, *Introduction to Quantum Mechanics*, 3rd ed., Cambridge University Press (2018), Chapter 3 (observables, eigenfunctions of hermitian operators, the generalized uncertainty principle) and Chapter 4 (angular momentum).
> - \{9\} H. P. Robertson, *The Uncertainty Principle*, Phys. Rev. 34, 163 (1929).
> - \{10\} E. Schrödinger, *Zum Heisenbergschen Unschärfeprinzip*, Sitzungsberichte der Preussischen Akademie der Wissenschaften 19, 296 (1930).

- [Angular momentum operator](angularmomentum.md)
- [Commutation relations](commutation.md)
- [Covariance](covariance.md)
- [Momentum operators](momentum.md)
- [Multiplication operators on `SpaceDHilbertSpace`](multiplication.md)
- [Position operators](position.md)
- [Unbounded operators](unbounded.md)
- [Uncertainty bounds for partial linear maps](uncertainty.md)

Modules in [AngularMomentum/](https://github.com/leanprover-community/physlib/tree/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum):

- [Three-dimensional angular momentum](angularmomentum-dimthree.md)

Modules in [OneDimension/](https://github.com/leanprover-community/physlib/tree/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/OneDimension):

- [Commutation relations](onedimension-commutation.md)
- [Momentum operator](onedimension-momentum.md)
- [Parity operator](onedimension-parity.md)
- [Position operator](onedimension-position.md)
- [Unbounded operators](onedimension-unbounded.md)

Modules in [StateObservables/](https://github.com/leanprover-community/physlib/tree/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/StateObservables):

- [Expectation values and centered vectors](stateobservables-expectedvalue.md)
- [Eigenvectors of partial linear maps](stateobservables-iseigenvector.md)
- [Variance and standard deviation](stateobservables-variance.md)
- [SpectralTheory](spectraltheory/README.md)
