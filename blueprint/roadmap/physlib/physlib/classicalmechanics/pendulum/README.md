# Pendulum

The folder [Physlib/ClassicalMechanics/Pendulum/](https://github.com/leanprover-community/physlib/tree/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum): 1 module, with an article; then 1 folder below it, a page each, 12 modules in all.

The repository's API map for this folder, *Configuration space for pendulum* ([Physlib/ClassicalMechanics/Pendulum/API-map.md](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/API-map.md)): its Content section, with the sentences it marks as not yet formalized left out (…). A citation \[n\] links the module its n-th Lean reference names.

*Content (Alpha)*

> The configuration space \{1} of the sliding pendulum \{2} is given by two generalized coordinates: the horizontal position of the support and the angle the string makes with the vertical. [\[1\]](slidingpendulum.md)
>
> The configuration space of the simple pendulum \{3} is a manifold. [\[2\]](simplependulum/geometric-basic.md) It maps into physical space \{4}, giving the position of the bob there. [\[3\]](simplependulum/geometric-basic.md) A trajectory of the simple pendulum is a curve in its configuration space, and every lift of the angle to the real line describes one. [\[4\]](simplependulum/geometric-trajectory.md) The Lagrangian of the simple pendulum is a function of the lifted angle and angular velocity, and along a differentiable lift it agrees with the constrained Lagrangian of the bob moving in physical space. [\[5\]](simplependulum/basic.md)[\[6\]](simplependulum/geometric-physicalspace.md)

Its references:

> - \{1\} Configuration Space API map — [Physlib/ClassicalMechanics/Lagrangian/API-map.md](../lagrangian/README.md)
> - \{2\} Landau & Lifshitz, *Mechanics*, 3rd Edition, Chapter 1 (The Equations of motion), Section 5 (The Lagrangian for a system of particles).
> - \{3\} Simple pendulum API map — [Physlib/ClassicalMechanics/Pendulum/SimplePendulum/API-map.md](simplependulum/README.md)
> - \{4\} Space API map — [Physlib/SpaceAndTime/Space/API-map.md](../../spaceandtime/space/README.md)

- [Sliding Pendulum](slidingpendulum.md)
- [SimplePendulum](simplependulum/README.md)
