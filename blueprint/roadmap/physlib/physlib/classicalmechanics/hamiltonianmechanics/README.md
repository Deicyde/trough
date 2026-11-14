# HamiltonianMechanics

The folder [Physlib/ClassicalMechanics/HamiltonianMechanics/](https://github.com/leanprover-community/physlib/tree/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HamiltonianMechanics): 2 modules, an article each, in path order.

The repository's API map for this folder, *Hamiltonian mechanics* ([Physlib/ClassicalMechanics/HamiltonianMechanics/API-map.md](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HamiltonianMechanics/API-map.md)): its Content section, with the sentences it marks as not yet formalized left out (…). A citation \[n\] links the module its n-th Lean reference names.

*Content (Alpha)*

> ### Phase space and observables
>
> A configuration space Q is a smooth manifold without boundary \{1}. [\[1\]](../configurationspace/basic.md) … In the coordinate formulation on a complete real inner-product space X, states are pairs (p, q) in X × X, and observables are real-valued functions f(p, q), with momentum first. [\[2\]](poissonbracket.md) …
>
> ### Hamiltonians and Hamiltonian trajectories
>
> … In coordinates, curves p(t) and q(t) satisfy Hamilton's equations q̇ = ∇ₚH and ṗ = −∇qH exactly when the Hamilton equation operator vanishes. \[3\] … For a smooth Hamiltonian and a smooth phase-space curve, the variational gradient of the action ∫ (⟨p, q̇⟩ − H(t, p, q)) dt is that operator. \[4\]
>
> Taking E = ℝ, positive mass m and spring constant k gives the harmonic-oscillator Hamiltonian H(p, q) = p²/(2m) + k q²/2, which is smooth on the whole phase space. [\[12\]](../harmonicoscillator/basic.md) Taking E = ℝ³, positive mass m and a radial potential V smooth at positive radii gives the central-force Hamiltonian H(p, q) = ‖p‖²/(2m) + V(‖q‖), smooth on the open domain U = \{(p, q) | q ≠ 0}. [\[14\]](../../../physlibalpha/classicalmechanics/centralforce/basic.md) …
>
> ### Poisson brackets and observable evolution
>
> The coordinate Poisson bracket is \{f, g} = ⟨∇qf, ∇ₚg⟩ − ⟨∇ₚf, ∇qg⟩. [\[2\]](poissonbracket.md) It is antisymmetric, bilinear and satisfies the Leibniz rule, with the differentiability assumptions needed for the gradient rules. \[5\] Along a differentiable solution of Hamilton's equations, a time-independent observable differentiable at the current state satisfies d f(p(t), q(t))/dt = \{f, H(t)}(p(t), q(t)). \[6\] …
>
> ### Symmetries and conserved quantities
>
> For a time-independent differentiable observable along a differentiable Hamiltonian trajectory, a vanishing Poisson bracket with the Hamiltonian implies zero time derivative. \[6\] A smooth autonomous Hamiltonian Poisson-commutes with itself and has zero time derivative along its Hamiltonian trajectories. \[5\]\[6\] …
>
> On a finite-dimensional real symplectic vector space, an affine infinitesimally symplectic Lie algebra action has a moment map whose components generate the action's vector fields through their symplectic gradients. [\[7\]](../../../physlibalpha/classicalmechanics/momentmap/basic.md) If an autonomous Hamiltonian is invariant under a generator, the corresponding moment-map component is constant along its Hamiltonian trajectories. \[8\]
>
> ### Integrability
>
> For an autonomous Hamiltonian on a 2d-dimensional Euclidean phase space, Liouville integrability on an open dense domain U consists of d smooth observables, including the Hamiltonian, that pairwise Poisson-commute and whose phase-space gradients are linearly independent on U. [\[9\]](../../../physlibalpha/classicalmechanics/liouvilleintegrable/basic.md) Each has zero time derivative along a differentiable Hamiltonian trajectory at times when the state lies in U. \[10\] With one degree of freedom, the Hamiltonian alone gives integrability on any open dense domain where it is smooth and its phase-space gradient is nonzero. \[11\] …
>
> ### Existing examples and their connections
>
> The harmonic oscillator \{3} and simple pendulum \{4} have explicit canonical momenta and Hamiltonians, with Hamiltonian, Newtonian and variational descriptions agreeing for smooth trajectories. The pendulum is expressed using a real lift of its angle. [\[12\]](../harmonicoscillator/basic.md)[\[13\]](../pendulum/simplependulum/hamiltonian.md)
>
> Three-dimensional central-force systems have Hamiltonians smooth away from the centre. [\[14\]](../../../physlibalpha/classicalmechanics/centralforce/basic.md) Their angular-momentum observables L² and Lz Poisson-commute with each other and with the Hamiltonian away from the centre. [\[15\]](../../../physlibalpha/classicalmechanics/centralforce/angularmomentum.md) …

Its references:

> - \{1\} Configuration Space API map — [Physlib/ClassicalMechanics/ConfigurationSpace/API-map.md](../configurationspace/README.md)
> - \{2\} Physlib GitHub issue #2003, Foundations for Hamiltonian Systems, https://github.com/leanprover-community/physlib/issues/2003
> - \{3\} Configuration space of the harmonic oscillator API map — [Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/API-map.md](../harmonicoscillator/geometric/README.md)
> - \{4\} Simple pendulum API map — [Physlib/ClassicalMechanics/Pendulum/SimplePendulum/API-map.md](../pendulum/simplependulum/README.md)
> - \{5\} Lagrangian mechanics API map — [Physlib/ClassicalMechanics/Lagrangian/API-map.md](../lagrangian/README.md)
> - \{6\} V. I. Arnold, *Mathematical Methods of Classical Mechanics*.

- [Hamilton's equations](hamiltonsequations.md)
- [The Poisson bracket](poissonbracket.md)
