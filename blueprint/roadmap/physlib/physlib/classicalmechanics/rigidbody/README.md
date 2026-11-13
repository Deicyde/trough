# RigidBody

The folder [Physlib/ClassicalMechanics/RigidBody/](https://github.com/leanprover-community/physlib/tree/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody): 6 modules, an article each, in path order with Basic.lean first in its folder.

The repository's API map for this folder, *Rigid body* ([Physlib/ClassicalMechanics/RigidBody/API-map.md](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/API-map.md)), with the sentences it marks as not yet formalized left out (…). A citation \[n\] links the module its n-th Lean reference names.

*Content (Alpha)*

> ### Mass distribution and inertia
>
> A rigid body \{1} is specified by its mass distribution, a linear functional on the smooth functions on space \{2}. [\[1\]](basic.md) … The total mass of a rigid body is its mass distribution applied to the constant function one. [\[2\]](basic.md) The centre of mass is the mass-weighted average of the coordinate functions. [\[3\]](basic.md) The inertia tensor of a rigid body, I\_ij = ∫ (δ\_ij |x|² − x\_i x\_j) dm, is built from the second moments of its mass distribution about the origin. [\[4\]](basic.md) It is symmetric. [\[5\]](basic.md) The inertia tensor about an arbitrary point takes its moments about that point, and the parallel-axis theorem expresses it as the inertia tensor about the centre of mass plus that of a point mass at the centre of mass. [\[6\]](basic.md)
>
> The solid sphere of mass m and radius R > 0, with uniform density on the closed ball about the origin, is a rigid body whose total mass is m and whose centre of mass is the origin. [\[7\]](solidsphere.md) …
>
> ### Motion
>
> The angular velocity of a rotating rigid body is the skew-symmetric tensor Ω = Ṙ Rᵀ built from its orientation R, and in three dimensions it is the vector dual to that tensor under the hat map. [\[8\]](angularvelocity.md) The velocity of the centre of mass is the time derivative of the centre-of-mass trajectory. [\[9\]](motion.md) The rotational kinetic energy at angular velocity ω is ½ ω · (I ω), and the total kinetic energy of a moving body is half the mass integral of the squared speed of its points. [\[10\]](kineticenergy.md) …

Its references:

> - \{1\} Landau and Lifshitz, *Mechanics*, Section 32 (page 100).
> - \{2\} Space API map — [Physlib/SpaceAndTime/Space/API-map.md](../../spaceandtime/space/README.md)

- [Rigid bodies](basic.md)
- [Angular momentum of a rigid body](angularmomentum.md)
- [The angular velocity of a rigid body](angularvelocity.md)
- [Kinetic energy of a rigid body](kineticenergy.md)
- [Rigid body motion](motion.md)
- [The solid sphere as a rigid body](solidsphere.md)
