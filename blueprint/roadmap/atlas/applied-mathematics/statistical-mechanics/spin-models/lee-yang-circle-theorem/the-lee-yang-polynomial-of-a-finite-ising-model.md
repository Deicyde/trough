---
declaration: section
origin: cited
lean: StatMech.LeeYang.minusSpinCount, StatMech.LeeYang.zeroFieldInteractionWeight, StatMech.LeeYang.leeYangPolynomial, StatMech.LeeYang.leeYangComplexPolynomial
statement: formalized
proof: formalized
---

# The Lee–Yang polynomial of a finite Ising model

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/lee-yang-circle-theorem/the-lee-yang-polynomial-of-a-finite-ising-model/index.html).

## Number of minus spins of a configuration

The number of minus spins (sites with value `false`) of a configuration.

Formalized by `StatMech.LeeYang.minusSpinCount`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangPolynomial.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangPolynomial.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/lee-yang-circle-theorem/the-lee-yang-polynomial-of-a-finite-ising-model/index.html#minus-spin-count).

## Zero-field Boltzmann weight of a configuration

The zero-field Boltzmann weight `exp (β ∑_{e ∈ E(G)} σ_x σ_y)` of a configuration.

Formalized by `StatMech.LeeYang.zeroFieldInteractionWeight`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangPolynomial.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangPolynomial.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/lee-yang-circle-theorem/the-lee-yang-polynomial-of-a-finite-ising-model/index.html#zero-field-interaction-weight).

## Lee–Yang polynomial of a finite Ising model

The Lee–Yang polynomial `∑_σ exp (β ∑_e σ_x σ_y) X^k(σ)` of the Ising model on `G`, where `k(σ)`
is the number of minus spins; its variable is the fugacity `exp (-2βh)`.

Formalized by `StatMech.LeeYang.leeYangPolynomial`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangPolynomial.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangPolynomial.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/lee-yang-circle-theorem/the-lee-yang-polynomial-of-a-finite-ising-model/index.html#lee-yang-polynomial).

## Lee–Yang polynomial with complex coefficients

The Lee–Yang polynomial with complex coefficients, whose zeros the Lee–Yang circle theorem
locates.

Formalized by `StatMech.LeeYang.leeYangComplexPolynomial`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangPolynomial.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangPolynomial.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/lee-yang-circle-theorem/the-lee-yang-polynomial-of-a-finite-ising-model/index.html#lee-yang-complex-polynomial).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The Lee–Yang polynomial of a finite Ising model](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/lee-yang-circle-theorem/the-lee-yang-polynomial-of-a-finite-ising-model/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/StatisticalMechanics/spin-models/lee-yang-circle-theorem/the-lee-yang-polynomial-of-a-finite-ising-model)
