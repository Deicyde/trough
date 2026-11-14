# CanonicalEnsemble

The folder [Physlib/StatisticalMechanics/CanonicalEnsemble/](https://github.com/leanprover-community/physlib/tree/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble): 4 modules, an article each, in path order with Basic.lean first in its folder.

The repository's API map for this folder, *Canonical ensemble* ([Physlib/StatisticalMechanics/CanonicalEnsemble/API-map.md](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/API-map.md)): its Content section, with the sentences it marks as not yet formalized left out (…). A citation \[n\] links the module its n-th Lean reference names.

*Content (Alpha)*

> ### Ensembles and their measures
>
> A canonical ensemble \{1} is given by its microstates, its energy function, its degrees of freedom, its phase-space unit and a σ-finite measure; independent ensembles add, a system has several non-interacting copies, and an ensemble transports along a measurable equivalence. [\[1\]](basic.md) The temperature enters through the inverse temperature \{2}. An ensemble carries an unnormalized Boltzmann measure and a normalized probability measure, together with pointwise mathematical and physical probability densities. [\[2\]](basic.md) The mathematical partition function is the integral of the Boltzmann factor, and the physical one is that divided by the phase-space unit raised to the degrees of freedom; both are positive. [\[3\]](basic.md)
>
> ### Thermodynamic quantities
>
> An ensemble has a mean energy, a mean square energy and an energy variance, [\[4\]](basic.md) and the variance is the mean square minus the square of the mean. [\[5\]](lemmas.md) The Helmholtz free energy comes from the partition function. [\[6\]](basic.md) An ensemble has a differential entropy and an absolute thermodynamic entropy, [\[7\]](basic.md) and for finitely many microstates the thermodynamic entropy is the Shannon entropy. [\[8\]](finite.md)
>
> The fundamental thermodynamic identity holds: the free energy is the mean energy less the temperature times the entropy. [\[9\]](lemmas.md) The mean energy is minus the derivative of the logarithm of the partition function with respect to the inverse temperature. [\[10\]](lemmas.md) The heat capacity is the derivative of the mean energy with respect to temperature, and whenever the energy variance is minus the derivative of the mean energy with respect to the inverse temperature, the heat capacity is the energy variance divided by the Boltzmann constant times the square of the temperature. [\[11\]](lemmas.md) For a finite ensemble at positive temperature this fluctuation–dissipation theorem holds outright. [\[12\]](finite.md) These identities are developed in Tong's lectures \{3}.
>
> ### Finite ensembles and the two-state system
>
> For systems with finitely many discrete microstates the integral definitions reduce to finite sums. [\[13\]](finite.md) The two-state ensemble has closed forms for its partition function, its state probabilities and its mean energy. [\[14\]](twostate.md) …

Its references:

> - \{1\} L. D. Landau and E. M. Lifshitz, *Statistical Physics, Part 1*, §31.
> - \{2\} Temperature API map — [Physlib/Thermodynamics/Temperature/API-map.md](../../thermodynamics/temperature/README.md)
> - \{3\} D. Tong, *Lectures on Statistical Physics* (Cambridge), https://www.damtp.cam.ac.uk/user/tong/statphys/one.pdf and https://www.damtp.cam.ac.uk/user/tong/statphys/two.pdf

- [Canonical Ensemble: Core Definitions](basic.md)
- [Finite Canonical Ensemble](finite.md)
- [Canonical Ensemble: Thermodynamic Identities and Relations](lemmas.md)
- [Two-state canonical ensemble](twostate.md)
