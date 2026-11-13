# Kinematics

The folder [Physlib/Electromagnetism/Kinematics/](https://github.com/leanprover-community/physlib/tree/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics): 8 modules, an article each, in path order with Basic.lean first in its folder.

The repository's API map for this folder, *Electromagnetic Potential* ([Physlib/Electromagnetism/Kinematics/API-map.md](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/API-map.md)), with the sentences it marks as not yet formalized left out (…). A citation \[n\] links the module its n-th Lean reference names.

*Content (Alpha)*

> ### The potential
>
> An electromagnetic potential is a map from spacetime \{1} to contravariant Lorentz vectors \{2}; it is determined by its values, and potentials add, negate, subtract and scale by reals pointwise. [\[1\]](empotential.md) A distributional electromagnetic potential is a tempered distribution on spacetime valued in Lorentz vectors, and it arises from distributional scalar and vector potentials. [\[2\]](../tempereddistributional/basic.md)
>
> A potential arises from a scalar potential, from a vector potential, and from a pair of non-relativistic potentials \{3}, each with a static variant, and the potential of a pair is the sum of the potentials of its two members. [\[3\]](empotential.md) …
>
> ### Fields and Lagrangian
>
> The electric field is determined by the potential, both for functions [\[4\]](electricfield.md) and for distributions. [\[5\]](../tempereddistributional/electricfield.md) The magnetic field is determined by the potential as a vector field and as an antisymmetric matrix field for functions [\[6\]](magneticfield.md) , and as an antisymmetric matrix field for distributions. [\[7\]](../tempereddistributional/magneticfield.md) The field-strength term of the Lagrangian is built from the potential, with its gradient, for functions [\[8\]](../dynamics/kineticterm.md) , and its gradient exists for distributions too. [\[9\]](../tempereddistributional/dynamics-kineticterm.md) The electromagnetic Lagrangian is built from the potential, together with the coupling to a free current, and both have gradients for functions [\[10\]](../dynamics/lagrangian.md) and for distributions. [\[11\]](../tempereddistributional/dynamics-lagrangian.md)

Its references:

> - \{1\} Spacetime API map — [Physlib/SpaceAndTime/SpaceTime/API-map.md](../../spaceandtime/spacetime/README.md)
> - \{2\} Lorentz group API map — [Physlib/Relativity/LorentzGroup/API-map.md](../../relativity/lorentzgroup/README.md)
> - \{3\} J. D. Jackson, *Classical Electrodynamics*, 3rd ed., Sections 6.2-6.3, on vector and scalar potentials and gauge transformations.

- [Boosts on the electric and magnetic fields](boosts.md)
- [The Electric Field (Kinematics/ElectricField)](electricfield.md)
- [The Electromagnetic Potential (EMPotential)](empotential.md)
- [The Field Strength Tensor (Kinematics/FieldStrength)](fieldstrength.md)
- [Gauge Transformations of the Electromagnetic Potential](gaugetransformation.md)
- [The Magnetic Field (Kinematics/MagneticField)](magneticfield.md)
- [The Scalar Potential (Kinematics/ScalarPotential)](scalarpotential.md)
- [The vector Potential (Kinematics/VectorPotential)](vectorpotential.md)
