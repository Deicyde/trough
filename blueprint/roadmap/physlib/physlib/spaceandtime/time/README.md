# Time

The folder [Physlib/SpaceAndTime/Time/](https://github.com/leanprover-community/physlib/tree/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time): 7 modules, an article each, in path order with Basic.lean first in its folder.

The repository's API map for this folder, *Time* ([Physlib/SpaceAndTime/Time/API-map.md](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/API-map.md)): its Content section, with the sentences it marks as not yet formalized left out (…). A citation \[n\] links the module its n-th Lean reference names.

*Content (Alpha)*

> ### Instants and their structure
>
> An instant of time is a single real number, for an arbitrary but fixed choice of unit and orientation. [\[1\]](basic.md) Instants form an affine space over the reals: a real number translates an instant to another instant, and any two instants differ by a real elapsed time. [\[2\]](basic.md) No instant is canonically zero.
>
> Given the implicit origin, the instant whose real number is zero, time is a real vector space of dimension one. It has an orthonormal basis and continuous linear and isometric equivalences to the reals. [\[3\]](innerproductspace.md) Instants are ordered, so that one instant comes no later than another. [\[4\]](innerproductspace.md) Time carries a norm, and an inner product making it a one-dimensional real inner-product space. [\[5\]](innerproductspace.md) It is a Borel measurable space whose volume measure is the Haar measure of the basis, and the identification with the reals preserves that measure. [\[6\]](innerproductspace.md) …
>
> Time with no structure beyond its orientation is a manifold in its own right, with its topology, its charted-space and manifold structures, and a diffeomorphism to the reals. [\[10\]](timeman.md)
>
> ### Derivatives in time
>
> A function from time into a normed space has a time derivative. The derivative is compatible with scalar multiplication and with quotients, kills constants, and preserves smoothness. Differentiating a function valued in Euclidean space, or in Lorentz vectors \{1}, agrees with differentiating its components one at a time. [\[7\]](derivatives.md) The time derivative of a product of square-matrix-valued functions obeys the product rule, and the time derivative commutes with the transpose. [\[9\]](matrixderivatives.md)
>
> A function from time into a manifold has a time derivative too, and for a target that is both a normed space and a manifold the two derivatives agree. [\[8\]](derivatives.md)
>
> ### Units of time
>
> A choice of time unit is a positive real number. Two units have a ratio, and a unit rescales an elapsed time. The concrete units run from seconds up to weeks, with the relations between them, such as the number of seconds in an hour. [\[11\]](timeunit.md)

Its references:

> - \{1\} Lorentz tensors API map — [Physlib/Relativity/Tensors/API-map.md](../../relativity/tensors/README.md)

- [Time](basic.md)
- [Time Derivatives](derivatives.md)
- [Time as an inner product space](innerproductspace.md)
- [Curves in normed spaces over `Time`](manifoldcurves.md)
- [Time derivatives of matrix-valued functions](matrixderivatives.md)
- [The time manifold](timeman.md)
- [Units on time](timeunit.md)
