# SimplePendulum

The folder [Physlib/ClassicalMechanics/Pendulum/SimplePendulum/](https://github.com/leanprover-community/physlib/tree/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum): 11 modules, an article each, in path order with Basic.lean first in its folder.

The repository's API map for this folder, *Simple pendulum* ([Physlib/ClassicalMechanics/Pendulum/SimplePendulum/API-map.md](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/API-map.md)), with the sentences it marks as not yet formalized left out (…). A citation \[n\] links the module its n-th Lean reference names.

*Content (Alpha)*

> ### Configuration space
>
> The configuration space of the simple pendulum, one of the pendulum configuration spaces \{1}, is the angle of the rod from the downward vertical modulo a full turn, homeomorphic to the circle. [\[1\]](geometric-basic.md) That configuration space is a manifold. [\[2\]](geometric-basic.md) Each real angle determines a configuration, with angles that differ by an integer multiple of 2π representing the same configuration. The map from real angles to configurations is therefore periodic with period 2π. [\[3\]](geometric-basic.md) The configuration space maps into physical space \{2}, sending an angle θ to the position (ℓ sin θ, −ℓ cos θ) of the bob, which lies at distance ℓ from the pivot. [\[4\]](geometric-basic.md)
>
> A trajectory is a time-parametrized curve in the configuration space. An angular lift of a given trajectory is a real-valued function θ(t) whose value modulo 2π gives the configuration at each time. Two angular lifts describe the same trajectory precisely when their angles differ by an integer multiple of 2π at each time. \[5\] Continuous and smooth angular lifts give rise to continuous and smooth trajectories, respectively. \[6\] Mapping a trajectory to physical space gives the position of the bob, which remains at distance |ℓ| from the pivot. \[7\]
>
> ### Dynamics
>
> The Lagrangian of the simple pendulum is the kinetic energy ½ m ℓ² θ̇² minus the gravitational potential energy \{3}. Its equation of motion m ℓ² θ̈ = −m g ℓ sin θ equates the rate of change of angular momentum with the gravitational torque, and is equivalent to the scalar form θ̈ + (g/ℓ) sin θ = 0. [\[8\]](basic.md) The equation of motion holds exactly when the variational gradient of the action vanishes, and energy is conserved along solutions. [\[9\]](basic.md) The Hamiltonian formulation \{4} is equivalent: the Newtonian, scalar, Hamiltonian and variational formulations agree. [\[10\]](hamiltonian.md)
>
> The hanging and the inverted positions are equilibria and solve the equation of motion. The separatrix energy 2 m g ℓ divides the motions: below it the pendulum never reaches the inverted position, and above it the angular velocity never vanishes. [\[11\]](equilibria.md) Shifting the angle by a whole number of turns leaves the lifted dynamics unchanged. [\[12\]](liftinvariance.md) The solution with a given initial angle and angular velocity is unique, the solutions are symmetric under time reversal, and a pendulum released from rest swings symmetrically in time. [\[13\]](solution.md) For any initial angle and angular velocity there is a curve with that initial data which satisfies the equation of motion within ε of the initial instant. [\[14\]](solution.md)
>
> ### Small oscillations and the period
>
> In the small-angle limit \{5} the pendulum is a harmonic oscillator of mass m ℓ² and spring constant m g ℓ: the linearized equation of motion is the oscillator's, its motions exist and are unique, and the period is 2π√(ℓ/g). [\[15\]](smallangle.md) The full and the linearized dynamics are related by the cubic bound m g ℓ |θ|³/6 on the error in the torque, and the difference of the variational gradients of the two actions is the difference of the torque and the linearized force. [\[16\]](smallangle.md)
>
> The period of a libration of amplitude θ₀ is 4√(ℓ/g) K(sin²(θ₀/2)) \{6}. This formula equals 2π√(ℓ/g) at zero amplitude, tends to the small-angle period as the amplitude goes to zero, increases with the amplitude on [0, π), and is bounded below by the small-angle period and above by the small-angle period divided by cos(θ₀/2). [\[17\]](periodformula.md) …

Its references:

> - \{1\} Configuration space for pendulum API map — [Physlib/ClassicalMechanics/Pendulum/API-map.md](../README.md)
> - \{2\} Space API map — [Physlib/SpaceAndTime/Space/API-map.md](../../../spaceandtime/space/README.md)
> - \{3\} Landau & Lifshitz, *Mechanics*, 3rd Edition, Chapter 1 (The Equations of motion), Section 5 (The Lagrangian for a system of particles).
> - \{4\} Landau & Lifshitz, *Mechanics*, 3rd Edition, Chapter 7 (The canonical equations), Section 40 (Hamilton's equations).
> - \{5\} Landau & Lifshitz, *Mechanics*, 3rd Edition, Chapter 5 (Small oscillations), Section 21 (Free oscillations in one dimension).
> - \{6\} Landau & Lifshitz, *Mechanics*, 3rd Edition, Chapter 3 (Integration of the equations of motion), Section 11 (Motion in one dimension), Problem 1.

- [The simple gravity pendulum](basic.md)
- [Equilibria and energy regimes of the simple pendulum](equilibria.md)
- [The Hamiltonian formulation of the simple pendulum](hamiltonian.md)
- [Independence of the lift for the simple pendulum](liftinvariance.md)
- [The period formula of the simple gravity pendulum](periodformula.md)
- [The simple pendulum released from rest](releasedfromrest.md)
- [Small-angle motion of the simple gravity pendulum](smallangle.md)
- [Existence and uniqueness of the solutions of the simple pendulum](solution.md)

Modules in [Geometric/](https://github.com/leanprover-community/physlib/tree/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric):

- [Configuration space of the simple pendulum](geometric-basic.md)
- [The simple pendulum in physical space](geometric-physicalspace.md)
- [Geometric trajectories of the simple pendulum](geometric-trajectory.md)
