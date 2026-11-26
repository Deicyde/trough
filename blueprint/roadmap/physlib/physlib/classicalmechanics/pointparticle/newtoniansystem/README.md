# NewtonianSystem

The folder [Physlib/ClassicalMechanics/PointParticle/NewtonianSystem/](https://github.com/leanprover-community/physlib/tree/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/PointParticle/NewtonianSystem): 2 modules, an article each, in path order with Basic.lean first in its folder.

The repository's API map for this folder, *Newtonian systems of point particles* ([Physlib/ClassicalMechanics/PointParticle/NewtonianSystem/API-map.md](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/PointParticle/NewtonianSystem/API-map.md)): its Content section, with the sentences it marks as not yet formalized left out (…). A citation \[n\] links the module its n-th Lean reference names.

*Content (Alpha)*

> ### Particles and forces in an inertial frame
>
> A particle has a constant positive mass and a position that depends on time. In an inertial frame the position is twice differentiable. Its first derivative is the velocity and its second derivative is the acceleration. [\[1\]](../basic.md)
>
> A Newtonian system collects the particles and the forces acting on them in one inertial frame. Each force has a time-dependent vector value and a target particle. An internal force also has a source particle distinct from its target. The net force on a particle is the sum of all internal and external forces on that target, counting each occurrence. \[2\][\[3\]](../../force.md)
>
> Newton's second law identifies this net force with the particle's mass times its acceleration. Newton's third law pairs each internal force with its reverse, which swaps the source and target and negates the force. The two occur with the same multiplicity, so the sum of all internal forces vanishes at each time \{1}. \[2\][\[4\]](../../force.md)
>
> ### Total quantities and the center of mass
>
> Summing the particle masses gives the total mass M. Summing their momenta gives the total momentum P(t), and summing their individual kinetic energies gives the total kinetic energy. The net external force sums just the forces applied from outside the system. \[5\]
>
> For positive M, the center of mass R(t) is the mass-weighted average of the particle positions and its velocity is R′(t) = P(t) / M. \[6\] If the collection of external forces is empty, the center of mass moves at constant velocity. Its position at any time t is R(t) = R(t₀) + (t − t₀) P(t₀) / M for any reference time t₀ \{1}. \[7\]
>
> ### An isolated binary star
>
> Consider two stars of masses m₀ and m₁ at positions x₀(t) and x₁(t), interacting only through gravity. The gravitational forces on the two stars are equal and opposite. \[8\] Their center of mass R(t) = (m₀ x₀(t) + m₁ x₁(t)) / M, where M = m₀ + m₁, moves at constant velocity because there are no external forces. \[7\]\[9\] Let G be the gravitational constant and r(t) = x₁(t) − x₀(t) the relative displacement. Whenever r(t) ≠ 0, the relative motion satisfies the inverse-square equation r″(t) = −G M r(t) / ‖r(t)‖³ \{1}. \[10\]

Its references:

> - \{1\} H. Goldstein, C. P. Poole and J. L. Safko, *Classical Mechanics*, 3rd ed., Addison-Wesley, 2002, §§1.2, 3.1 and 3.7.

- [Newtonian point-particle systems](basic.md)
- [Center of mass of a Newtonian system](centerofmass.md)
