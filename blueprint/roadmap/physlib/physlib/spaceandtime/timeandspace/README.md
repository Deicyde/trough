# TimeAndSpace

The folder [Physlib/SpaceAndTime/TimeAndSpace/](https://github.com/leanprover-community/physlib/tree/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace): 4 modules, an article each, in path order with Basic.lean first in its folder.

The repository's API map for this folder, *TimeAndSpace* ([Physlib/SpaceAndTime/TimeAndSpace/API-map.md](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/API-map.md)), with the sentences it marks as not yet formalized left out (…). A citation \[n\] links the module its n-th Lean reference names.

*Content (Alpha)*

> A point of Euclidean space-time is a pair of an instant of time \{1} and a point of d-dimensional space \{2}. [\[1\]](basic.md) Space-time projects onto its time and its space factor, continuously and linearly, and each projection moves a pair of points no further apart than they were. [\[2\]](basic.md)
>
> The Euclidean group of space acts on space-time, each element as an isometry which splits into a linear part and a translation. [\[3\]](euclideangroup-action.md) That action carries over to the Schwartz maps out of space-time, where each element acts injectively and surjectively. [\[4\]](euclideangroup-schwartzaction.md)
>
> Differentiating a function on space-time in time and differentiating it in space commute, and the time derivative commutes with the curl. [\[5\]](basic.md) A function on space-time whose time derivative vanishes depends only on the point of space, one whose space derivative vanishes depends only on the instant, and one with both vanishing is constant. [\[6\]](basic.md)

Its references:

> - \{1\} Time API map — [Physlib/SpaceAndTime/Time/API-map.md](../time/README.md)
> - \{2\} Space API map — [Physlib/SpaceAndTime/Space/API-map.md](../space/README.md)

- [Functions and distributions on Time and Space d](basic.md)
- [Distributions which are constant in time](constanttimedist.md)

Modules in [EuclideanGroup/](https://github.com/leanprover-community/physlib/tree/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/EuclideanGroup):

- [The action of the Euclidean group on `TimeAndSpace`](euclideangroup-action.md)
- [The Euclidean group action on Schwartz maps over `TimeAndSpace`](euclideangroup-schwartzaction.md)
