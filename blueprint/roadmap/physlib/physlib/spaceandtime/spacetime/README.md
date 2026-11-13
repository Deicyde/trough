# SpaceTime

The folder [Physlib/SpaceAndTime/SpaceTime/](https://github.com/leanprover-community/physlib/tree/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime): 10 modules, an article each, in path order with Basic.lean first in its folder.

The repository's API map for this folder, *SpaceTime* ([Physlib/SpaceAndTime/SpaceTime/API-map.md](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/API-map.md)), with the sentences it marks as not yet formalized left out (…). A citation \[n\] links the module its n-th Lean reference names.

*Content (Alpha)*

> ### Points of space-time
>
> A point of Minkowski space-time is a Lorentz vector \{1} of coordinates, for an arbitrary but fixed choice of units and origin. [\[1\]](basic.md) Space-time maps onto space \{2} and onto time \{3}, and is equivalent to their product. [\[2\]](basic.md)
>
> The Lorentz group \{4} acts on space-time, and through it on Schwartz maps and distributions on space-time. [\[8\]](lorentzaction.md) A rotation about the coordinate origin acts on space-time through the Lorentz group and on space through the Euclidean group, and the spatial projection intertwines these two actions of one and the same special orthogonal rotation. [\[3\]](basic.md)
>
> ### Integration and slicing
>
> Space-time carries the measure-space structure that integration over it uses: a Borel measurable space with an additive Haar volume measure. [\[9\]](basic.md) An integral over space-time splits into an integral over space and an integral over time, in either order. [\[7\]](basic.md) A function or a distribution on space-time can be sliced at a fixed instant. [\[10\]](timeslice.md)
>
> ### Derivatives
>
> A function from space-time into a normed space can be differentiated along a coordinate, and its derivatives assemble into a tensor. [\[4\]](derivatives.md) A function from space-time into a manifold can be differentiated along a coordinate too, giving a tangent vector at its value. [\[5\]](derivatives.md) A distribution on space-time valued in a normed space can be differentiated. [\[6\]](derivatives.md) …

Its references:

> - \{1\} Lorentz tensors API map — [Physlib/Relativity/Tensors/API-map.md](../../relativity/tensors/README.md)
> - \{2\} Space API map — [Physlib/SpaceAndTime/Space/API-map.md](../space/README.md)
> - \{3\} Time API map — [Physlib/SpaceAndTime/Time/API-map.md](../time/README.md)
> - \{4\} Lorentz group API map — [Physlib/Relativity/LorentzGroup/API-map.md](../../relativity/lorentzgroup/README.md)

- [Spacetime](basic.md)
- [Boosts of space time](boosts.md)
- [Derivatives on SpaceTime](derivatives.md)
- [Lorentz group actions related to SpaceTime](lorentzaction.md)
- [Time slice](timeslice.md)

Modules in [SpaceTimeAlgebra/](https://github.com/leanprover-community/physlib/tree/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeAlgebra):

- [The spacetime algebra](spacetimealgebra-basic.md)
- [Complex conjugation in the spacetime algebra](spacetimealgebra-star.md)
- [Taylor series of functions on spacetime](spacetimealgebra-taylorseries.md)

Modules in [SpaceTimeDerivAlgebra/](https://github.com/leanprover-community/physlib/tree/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra):

- [The spacetime derivative algebra](spacetimederivalgebra-basic.md)
- [The action of spacetime series on derivative symbols](spacetimederivalgebra-action.md)
