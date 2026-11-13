# Geometric

The folder [Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/](https://github.com/leanprover-community/physlib/tree/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Geometric): 3 modules, an article each, in path order with Basic.lean first in its folder.

The repository's API map for this folder, *Configuration space of the harmonic oscillator* ([Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/API-map.md](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/API-map.md)), with the sentences it marks as not yet formalized left out (…). A citation \[n\] links the module its n-th Lean reference names.

*Content (Alpha)*

> ### The configuration space
>
> The configuration space of the classical harmonic oscillator, in the geometric setting of Terek \{1}, carries a single global coordinate valued in one-dimensional Euclidean space; two configurations are equal when their coordinates are, and a configuration can be applied like a function to read off its coordinate. [\[1\]](basic.md) The configuration space carries the topology induced by its global coordinate, and is equivalent and homeomorphic to the Euclidean model, which transports Hausdorffness and second countability across. [\[2\]](basic.md)
>
> The configuration space is a smooth manifold, charted by a single global chart, and that chart is an analytic diffeomorphism onto the Euclidean model. [\[3\]](basic.md) Each tangent space is a finite-dimensional normed real vector space, with a chart-induced continuous linear equivalence to the Euclidean coordinate model. [\[4\]](basic.md) The configuration space maps to the actual position of the particle in physical space \{2}, by reading off the underlying coordinate. [\[5\]](basic.md)
>
> ### Trajectories and kinetic energy
>
> A trajectory of the oscillator is a curve from time \{3} into the configuration space, with its coordinate curve and its curve of positions in physical space. [\[6\]](trajectory.md) A trajectory is smooth exactly when its coordinate curve is, and likewise differentiable; the geometric velocity is a tangent vector, and it is the time derivative of the coordinate curve. [\[7\]](trajectory.md)
>
> The configuration space carries the oscillator's mass Riemannian metric, the mass-scaled Euclidean inner product in global tangent coordinates, which is positive definite and computable in coordinates. [\[8\]](kineticenergy.md) The geometric kinetic energy of a tangent vector v is ½ g(v, v) for that metric g, and recovers the standard mass-scaled coordinate expression ½ m ‖v‖². [\[9\]](kineticenergy.md)

Its references:

> - \{1\} Ivo Terek, *Introductory Variational Calculus on Manifolds*, Section 1 (pages 1-2), Basic definitions and examples.
> - \{2\} Space API map — [Physlib/SpaceAndTime/Space/API-map.md](../../../spaceandtime/space/README.md)
> - \{3\} Time API map — [Physlib/SpaceAndTime/Time/API-map.md](../../../spaceandtime/time/README.md)

- [Configuration space of the harmonic oscillator](basic.md)
- [Geometric kinetic energy of the harmonic oscillator](kineticenergy.md)
- [Geometric trajectories of the harmonic oscillator](trajectory.md)
