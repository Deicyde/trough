# Lagrangian

The folder [Physlib/ClassicalMechanics/Lagrangian/](https://github.com/leanprover-community/physlib/tree/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Lagrangian): 4 modules, an article each, in path order with Basic.lean first in its folder.

The repository's API map for this folder, *Lagrangian mechanics* ([Physlib/ClassicalMechanics/Lagrangian/API-map.md](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Lagrangian/API-map.md)), with the sentences it marks as not yet formalized left out (…). A citation \[n\] links the module its n-th Lean reference names.

*Content (Alpha)*

> ### Lagrangian systems and the action
>
> A Lagrangian system on a configuration space M \{1} is a smooth function L : Time × TM → ℝ of time \{2} and of the positions and velocities, depending on first derivatives only. [\[1\]](basic.md) A smooth variation of a curve γ on [t₀, t₁] is a smooth family of curves starting at γ and fixing γ(t₀) and γ(t₁). [\[2\]](../configurationspace/variation.md) The action of γ is ∫ L(t, γ, γ̇) dt over [t₀, t₁], and γ is a critical point of the action when it is smooth and every variation has zero first variation of the action \{3}. [\[3\]](basic.md) On a normed space, the action is the integral of L(t, q, q̇) along the coordinate curve. \[4\]
>
> ### Equations of motion
>
> On a normed space, a smooth curve is a critical point of the action over [t₀, t₁] with t₀ ≠ t₁ if and only if the Euler–Lagrange equations hold. \[5\] …

Its references:

> - \{1\} Configuration Space API map — [Physlib/ClassicalMechanics/ConfigurationSpace/API-map.md](../configurationspace/README.md)
> - \{2\} Time API map — [Physlib/SpaceAndTime/Time/API-map.md](../../spaceandtime/time/README.md)
> - \{3\} Ivo Terek, *Introductory Variational Calculus on Manifolds*.
> - \{4\} V. I. Arnold, *Mathematical Methods of Classical Mechanics*.
> - \{5\} L. D. Landau and E. M. Lifshitz, *Mechanics*.

- [Lagrangian systems](basic.md)
- [Critical points and Euler-Lagrange equations](criticalpoint.md)
- [First variation of the action](firstvariation.md)
- [Equivalent Lagrangians under Total Derivatives](totalderivativeequivalence.md)
