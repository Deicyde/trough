# Space

The folder [Physlib/SpaceAndTime/Space/](https://github.com/leanprover-community/physlib/tree/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space): 30 modules, an article each, in path order with Basic.lean first in its folder.

The repository's API map for this folder, *Space* ([Physlib/SpaceAndTime/Space/API-map.md](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/API-map.md)), with the sentences it marks as not yet formalized left out (…). A citation \[n\] links the module its n-th Lean reference names.

*Content (Alpha)*

> ### Points of space and their structure
>
> A point of space is given by its d real coordinates. [\[1\]](part-01/basic.md) Space is a type of its own, distinct from the Euclidean space of the same dimension although closely related to it, a choice discussed on the Lean Zulip \{1}. Subtracting two points of space gives a vector of Euclidean space. [\[8\]](part-01/basic.md) Space is a normed torsor over Euclidean space of the same dimension. [\[9\]](part-01/basic.md)
>
> Space has a choice of origin, the zero of its vector space structure, and a standard affine-isometry chart onto Euclidean space of the same dimension. [\[5\]](part-01/origin.md) Once the origin is taken as its zero, space is a real vector space. [\[2\]](part-01/module.md) It carries a norm, an inner product and a metric, making it a finite-dimensional real inner-product space and a metric space. [\[3\]](part-01/module.md)[\[4\]](part-01/basic.md) It has basis vectors, one for each coordinate direction, forming an orthonormal basis. [\[7\]](part-01/module.md)
>
> Space is a smooth manifold, charted over Euclidean space of the same dimension through a homeomorphism with it. [\[6\]](part-01/basic.md)
>
> ### Dimensions, units and the cross product
>
> Spaces of different dimensions are related: one dimension of space splits off as a real factor, and one-dimensional space is isometrically the reals. [\[14\]](part-01/slice.md)[\[15\]](part-01/module.md) A choice of length unit rescales lengths, and concrete units such as the metre are available. [\[16\]](part-01/lengthunit.md)
>
> Three-dimensional Euclidean space carries the cross product. Taking the cross product with a fixed vector commutes with the time derivative, and the cross product of a vector with another is orthogonal to it. [\[17\]](part-01/crossproduct.md)
>
> ### Translations and rotations
>
> Points of space can be translated, and so can distributions on space. [\[10\]](part-01/basic.md)[\[11\]](part-01/translations.md) The group of rotations acts on space, and that action agrees with multiplying coordinates by the rotation matrix. [\[12\]](part-02/euclideangroup-basic.md)[\[13\]](part-02/euclideangroup-action.md)
>
> ### Derivatives and distributions
>
> A function from space into a normed space can be differentiated along a coordinate direction. [\[18\]](part-01/derivatives-basic.md) …
>
> A function bounded in the appropriate sense determines a distribution on space; the constant function and the constant slice are such distributions. [\[19\]](part-01/isdistbounded.md)[\[20\]](part-01/distoffunction.md)[\[21\]](part-01/distconst.md)[\[22\]](part-01/constantslicedist.md) A distribution on space valued in a normed space can be differentiated, giving also its gradient, its divergence and its curl. [\[23\]](part-01/derivatives-basic.md)[\[24\]](part-01/derivatives-grad.md)[\[25\]](part-01/derivatives-div.md)[\[26\]](part-01/derivatives-curl.md) …

Its references:

> - \{1\} Lean Zulip, #PhysLean > Space vs EuclideanSpace, https://leanprover.zulipchat.com/#narrow/channel/479953-PhysLean/topic/Space.20vs.20EuclideanSpace/with/575938877

## [Space to Matrix divergence on Space](part-01/README.md)

- [Space](part-01/basic.md)
- [Constant slice distributions](part-01/constantslicedist.md)
- [The cross product on Euclidean vectors in three dimensions](part-01/crossproduct.md)
- [The constant distribution on space](part-01/distconst.md)
- [Distributions from functions on space](part-01/distoffunction.md)
- [Functions on `Space d` which can be made into distributions](part-01/isdistbounded.md)
- [Units on Length](part-01/lengthunit.md)
- [The structure of a module on Space](part-01/module.md)
- [The origin of `Space` and the Euclidean chart](part-01/origin.md)
- [Slices of space](part-01/slice.md)
- [Smooth real-valued functions on space](part-01/smoothfunctions.md)
- [Translations on space](part-01/translations.md)
- [Derivatives on Space](part-01/derivatives-basic.md)
- [Curl on Space](part-01/derivatives-curl.md)
- [Bounded derivative indices](part-01/derivatives-derivativeindex.md)
- [Divergence on Space](part-01/derivatives-div.md)
- [Gradient of functions and distributions on `Space d`](part-01/derivatives-grad.md)
- [Iterated derivatives on `Space d`](part-01/derivatives-iterated.md)
- [The Laplacian operator on `Space d`](part-01/derivatives-laplacian.md)
- [Matrix divergence on Space](part-01/derivatives-matrixdiv.md)

## [Multi-indices to Regularized powers of the norm…](part-02/README.md)

- [Multi-indices](part-02/derivatives-multiindex.md)
- [Euclidean group](part-02/euclideangroup-basic.md)
- [The action of the Euclidean group on `Space`](part-02/euclideangroup-action.md)
- [The inclusion of the Euclidean group into the affine automorphism group](part-02/euclideangroup-affinegroup.md)
- [Integrals in Space](part-02/integrals-basic.md)
- [Integrability of norm powers on subsets of Space](part-02/integrals-normpow.md)
- [The radial angular measure on Space](part-02/integrals-radialangularmeasure.md)
- [The norm on space](part-02/norm-basic.md)
- [Iterated Laplacians of norm distributions](part-02/norm-iteratedlaplacian.md)
- [Regularized powers of the norm on space](part-02/norm-regularized.md)
