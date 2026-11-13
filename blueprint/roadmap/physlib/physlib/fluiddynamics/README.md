# FluidDynamics

The folder [Physlib/FluidDynamics/](https://github.com/leanprover-community/physlib/tree/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics): 1 module, an article each, in path order with Basic.lean first in its folder; then 4 folders below it, a page each, 17 modules in all.

The repository's API map for this folder, *Fluid* ([Physlib/FluidDynamics/API-map.md](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/API-map.md)), with the sentences it marks as not yet formalized left out (…). A citation \[n\] links the module its n-th Lean reference names.

*Content (Alpha)*

> The mass flux density is the momentum density ρ u, the product of the density and the velocity, whose divergence enters the continuity equation; the convective momentum flux is ρ u ⊗ u. [\[2\]](fluidflow/momentum.md) The equation of continuity, ∂ₜρ + ∇ · (ρ u) = 0, expresses the local conservation of mass, in a pointwise classical form, through its residual, and in a smooth form that implies the classical one. [\[3\]](fluidflow/continuity.md)
>
> An ideal, inviscid fluid has Cauchy stress −p I, whose divergence is −∇p. [\[5\]](cauchyflow/inviscid.md) Euler's equation is the equation of motion of an ideal fluid: continuity, Cauchy momentum balance and inviscid stress, with the conservative and convective forms equivalent for differentiable fields. [\[4\]](euler/basic.md) Bernoulli's equation states that the Bernoulli function ½ |u|² + h + Φ, with h the specific enthalpy and Φ the potential of the body force, is spatially constant, locally that its spatial gradient vanishes. [\[6\]](thermodynamiccauchyflow/bernoulli.md)

Its references:

> - \{1\} Landau, L. D. and Lifshitz, E. M., *Fluid Mechanics* (Course of Theoretical Physics, vol. 6), 2nd ed., Chapter 1 (continuity, Euler equation, Bernoulli equation, energy and momentum flux).
> - \{2\} Space API map — [Physlib/SpaceAndTime/Space/API-map.md](../spaceandtime/space/README.md)
> - \{3\} Time API map — [Physlib/SpaceAndTime/Time/API-map.md](../spaceandtime/time/README.md)

- [Basic field types for fluid dynamics](basic.md)
- [CauchyFlow](cauchyflow/README.md)
- [Euler](euler/README.md)
- [FluidFlow](fluidflow/README.md)
- [ThermodynamicCauchyFlow](thermodynamiccauchyflow/README.md)
