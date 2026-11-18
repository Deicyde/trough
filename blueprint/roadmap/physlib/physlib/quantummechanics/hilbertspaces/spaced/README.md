# SpaceD

The folder [Physlib/QuantumMechanics/HilbertSpaces/SpaceD/](https://github.com/leanprover-community/physlib/tree/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD): 8 modules, an article each, in path order with Basic.lean first in its folder.

The repository's API map for this folder, *Hilbert spaces on Space* ([Physlib/QuantumMechanics/HilbertSpaces/SpaceD/API-map.md](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/API-map.md)): its Content section, with the sentences it marks as not yet formalized left out (…). A citation \[n\] links the module its n-th Lean reference names.

*Content (Alpha)*

> The Hilbert space on space \{1} with respect to a measure is the space of square-integrable complex functions modulo equality almost everywhere, and the volume is the default measure. [\[1\]](basic.md) A function can be read as an element of such a Hilbert space exactly when it is almost everywhere strongly measurable and square-integrable. [\[2\]](basic.md)
>
> Several subspaces carry the extra regularity that differential operators need. The complex Schwartz maps on space form a subspace, and a map passes in either direction between a Schwartz map and the class it represents. [\[3\]](schwartzsubmodule.md) … The Fourier transform is a unitary map from the Hilbert space to itself. [\[4\]](fourier.md)
>
> Restricting attention to a region of space gives further structure. The functions supported in a given subset of space form a Hilbert space of their own, with an inclusion into the full space and a projection onto it. [\[5\]](basic.md) The elements satisfying homogeneous Dirichlet boundary conditions on a subset of space form a subspace. [\[6\]](dirichletsubmodule.md) …
>
> Operators on these spaces come in two families. Any complex function of position gives a multiplication operator with maximal domain [\[7\]](../../operators/multiplication.md) , and the position operators are such multiplication operators. [\[8\]](../../operators/position.md) … The general theory of these operators lives in the operator algebra \{2}.

Its references:

> - \{1\} Space API map — [Physlib/SpaceAndTime/Space/API-map.md](../../../spaceandtime/space/README.md)
> - \{2\} Operator algebra API map — [Physlib/QuantumMechanics/Operators/API-map.md](../../operators/README.md)

- [Hilbert spaces for quantum mechanics on `Space d`](basic.md)
- [Dirichlet submodule](dirichletsubmodule.md)
- [The Fourier transform on `SpaceDHilbertSpace`](fourier.md)
- [Momentum states](momentumstates.md)
- [Polynomially-bounded Schwartz submodules](polybddschwartzsubmodule.md)
- [Position states (SpaceD/PositionStates)](positionstates.md)
- [Schwartz submodule](schwartzsubmodule.md)
- [Sobolev submodules of `SpaceDHilbertSpace`](sobolevsubmodule.md)
