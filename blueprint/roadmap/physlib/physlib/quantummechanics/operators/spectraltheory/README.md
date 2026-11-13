# SpectralTheory

The folder [Physlib/QuantumMechanics/Operators/SpectralTheory/](https://github.com/leanprover-community/physlib/tree/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory): 4 modules, an article each, in path order with Basic.lean first in its folder.

The repository's API map for this folder, *Spectral theory of unbounded operators* ([Physlib/QuantumMechanics/Operators/SpectralTheory/API-map.md](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/API-map.md)), with the sentences it marks as not yet formalized left out (…). A citation \[n\] links the module its n-th Lean reference names.

*Content (Alpha)*

> ### Resolvent and spectrum
>
> A complex number z lies in the resolvent set of an operator T \{1} when T - z has a bounded inverse, the resolvent; the resolvent set is open, and for a closed operator it is exactly the set of z for which T - z is a bijection from the domain onto the space. [\[1\]](basic.md) The spectrum is the complement of the resolvent set; it is closed, and splits into the point, residual and continuous spectra. [\[2\]](basic.md) Resolvents satisfy the two resolvent identities, relating resolvents at two points and of two operators. [\[3\]](basic.md) The treatment follows the standard references of Hall \{2}, Reed and Simon \{3}, and Schmüdgen \{4}.
>
> ### Regularity domain and numerical range
>
> A point z is a point of regularity when T - z is bounded below. The regularity domain is open, the deficiency subspace at z is the orthogonal complement of the range of T - z, and its dimension is the defect number; for a closable operator it is constant on each connected component of the regularity domain. [\[4\]](basic.md) The numerical range is the set of values of the pairing of a unit vector with its image; it is convex by the Toeplitz-Hausdorff theorem, and the exterior of its closure consists of points of regularity. [\[5\]](basic.md)
>
> ### Symmetric operators
>
> The numerical range of a symmetric operator is real, and so is described by its projection to the real axis. [\[6\]](symmetric.md) Every point off the real axis is therefore a point of regularity, and the regularity domain is connected when the operator is bounded above or below. [\[7\]](symmetric.md) A symmetric operator whose defect numbers at i and -i both vanish is essentially self-adjoint. [\[8\]](symmetric.md) The eigenvalues of a symmetric operator are real. [\[9\]](symmetric.md)
>
> ### Self-adjoint operators
>
> For a self-adjoint operator the resolvent set and the regularity domain coincide, and every complex number with non-zero imaginary part lies in the resolvent set, with T - z onto. [\[10\]](selfadjoint.md) The spectrum of a self-adjoint operator lies in the real axis and its residual spectrum is empty. [\[11\]](selfadjoint.md) Conjugation by a unitary preserves self-adjointness, so an observable keeps its status under a change of representation. [\[12\]](selfadjoint.md)
>
> ### Spectral measures and the spectral theorem
>
> A spectral measure is a vector measure valued in the bounded operators whose values are star projections and which sends the whole outcome space to the identity. [\[13\]](spectralmeasure.md) The projections of two measurable sets compose to the projection of their intersection, disjoint sets give orthogonal projections, and all of them commute. [\[14\]](spectralmeasure.md)

Its references:

> - \{1\} Operator algebra API map — [Physlib/QuantumMechanics/Operators/API-map.md](../README.md)
> - \{2\} B. C. Hall, *Quantum Theory for Mathematicians*, Springer (2013), Chapters 9 and 10 (unbounded self-adjoint operators, the spectral theorem).
> - \{3\} M. Reed and B. Simon, *Methods of Modern Mathematical Physics I. Functional Analysis*, Academic Press (1980), Chapters VII and VIII (the spectral theorem, unbounded operators).
> - \{4\} K. Schmüdgen, *Unbounded Self-Adjoint Operators on Hilbert Space*, Springer (2012), Chapters 1 to 3 (closed, symmetric and self-adjoint operators, defect numbers, the spectrum).

- [Spectral theory for closed operators](basic.md)
- [Spectral theory for self-adjoint operators](selfadjoint.md)
- [Spectral measures](spectralmeasure.md)
- [Spectral theory for symmetric operators](symmetric.md)
