# DampedHarmonicOscillator

The folder [Physlib/ClassicalMechanics/DampedHarmonicOscillator/](https://github.com/leanprover-community/physlib/tree/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator): 2 modules, an article each, in path order with Basic.lean first in its folder.

The repository's API map for this folder, *Damped harmonic oscillator* ([Physlib/ClassicalMechanics/DampedHarmonicOscillator/API-map.md](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/API-map.md)), with the sentences it marks as not yet formalized left out (…). A citation \[n\] links the module its n-th Lean reference names.

*Content (Alpha)*

> A damped harmonic oscillator \{1}\{2} is specified by its mass, its spring constant and its damping coefficient. [\[1\]](basic.md) Its equation of motion, for a trajectory from time \{3} into one-dimensional Euclidean space, is m ẍ + γ ẋ + k x = 0. [\[2\]](basic.md) The force on the mass is −k x − γ ẋ, and the equation of motion is Newton's second law for that force. [\[3\]](basic.md) With no damping the system is the undamped harmonic oscillator, and the two equations of motion agree. [\[6\]](basic.md)
>
> The kinetic energy is ½ m ‖ẋ‖², that of the underlying undamped oscillator. [\[10\]](../harmonicoscillator/basic.md) The potential energy is ½ k ‖x‖². [\[11\]](../harmonicoscillator/basic.md) Along a solution the mechanical energy dissipates at the rate −γ ‖ẋ‖², and strictly decreases whenever the velocity is nonzero and the damping is positive. [\[4\]](basic.md)
>
> The discriminant γ² − 4 m k classifies the motion: it is underdamped when the discriminant is negative, critically damped when it vanishes, and overdamped when it is positive, and each regime has a decay rate γ/(2m) and an angular frequency. [\[5\]](basic.md) The initial conditions of the oscillator are an initial position and an initial velocity. [\[7\]](solution.md) The trajectory with those initial conditions has a closed form appropriate to the damping regime — trigonometric, polynomial or hyperbolic, each multiplied by an exponential decay. [\[8\]](solution.md) That trajectory satisfies the equation of motion. [\[9\]](solution.md) It is the unique solution of the equation of motion with the given initial conditions. [\[14\]](solution.md)
>
> The Caldirola–Kanai Lagrangian is the undamped Lagrangian multiplied by the growing exponential exp(γ t / m). [\[12\]](basic.md) Its variational gradient reduces to the Euler–Lagrange equations, and vanishes exactly on solutions of the equation of motion. [\[13\]](basic.md) This Lagrangian goes back to Caldirola \{4} and Kanai \{5}.

Its references:

> - \{1\} Landau & Lifshitz, *Mechanics*, page 76, Section 25.
> - \{2\} Goldstein, *Classical Mechanics*, Chapter 2.
> - \{3\} Time API map — [Physlib/SpaceAndTime/Time/API-map.md](../../spaceandtime/time/README.md)
> - \{4\} Caldirola, *Nuovo Cimento* 18 (1941) 393.
> - \{5\} Kanai, *Progress of Theoretical Physics* 3 (1948) 440.

- [The damped harmonic oscillator](basic.md)
- [Solutions to the damped harmonic oscillator](solution.md)
