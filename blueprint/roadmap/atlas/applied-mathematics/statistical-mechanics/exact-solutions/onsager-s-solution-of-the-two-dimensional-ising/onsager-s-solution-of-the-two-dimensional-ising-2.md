---
declaration: section
origin: cited
lean: StatMech.Onsager.main_high_temperature_expansion, StatMech.Onsager.main_finite_pressure_decomposition, StatMech.Onsager.main_critical_beta_value, StatMech.Onsager.main_critical_beta_unique, StatMech.Onsager.main_pressure_continuous_at_critical, StatMech.Onsager.main_torus_pressure_decomposition, StatMech.Onsager.main_free_energy_from_spin_kacWard, StatMech.Onsager.main_spin_kacWard_from_weighted_root
statement: formalized
proof: formalized
---

# Onsager's solution of the two-dimensional Ising model

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/onsager-s-solution-of-the-two-dimensional-ising/index.html).

## A. Finite volume

## High-temperature expansion

**High-temperature expansion** (van der Waerden 1941). On a finite graph,
`Z(β) = 2^|V| (cosh β)^|E| X(tanh β)` with `X` the even-subgraph generating function.

Formalized by `StatMech.Onsager.main_high_temperature_expansion`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/OnsagerFormula.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/OnsagerFormula.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/onsager-s-solution-of-the-two-dimensional-ising/index.html#main-high-temperature-expansion).

## Finite-volume pressure decomposition for $\beta \ge 0$

The finite-volume pressure as `log 2 + (|E|/|V|) log cosh β + log X(tanh β) / |V|`, for `β ≥ 0`.

Formalized by `StatMech.Onsager.main_finite_pressure_decomposition`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/OnsagerFormula.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/OnsagerFormula.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/onsager-s-solution-of-the-two-dimensional-ising/index.html#main-finite-pressure-decomposition).

## Kramers-Wannier critical point

`β_c = ½ log (1 + √2)` satisfies `sinh 2β_c = 1` (H. A.
Kramers and G. H. Wannier, *Statistics of the two-dimensional ferromagnet. Part I*, 1941).

Formalized by `StatMech.Onsager.main_critical_beta_value`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/OnsagerFormula.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/OnsagerFormula.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/onsager-s-solution-of-the-two-dimensional-ising/index.html#main-critical-beta-value).

## $\beta_c$ is the unique positive root of $\sinh 2\beta = 1$

`β_c` is the only positive `β` with `sinh 2β = 1`.

Formalized by `StatMech.Onsager.main_critical_beta_unique`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/OnsagerFormula.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/OnsagerFormula.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/onsager-s-solution-of-the-two-dimensional-ising/index.html#main-critical-beta-unique).

## Continuity of Onsager's pressure at the critical point

Onsager's pressure is continuous at `β_c`. Its non-analyticity there is not part of the statement.

Formalized by `StatMech.Onsager.main_pressure_continuous_at_critical`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/OnsagerFormula.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/OnsagerFormula.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/onsager-s-solution-of-the-two-dimensional-ising/index.html#main-pressure-continuous-at-critical).

## Pressure decomposition on the $L \times L$ torus for $\beta \ge 0$

On the `L × L` torus, `p_L(β) = log 2 + 2 log cosh β + log X_L(tanh β) / L²` for `β ≥ 0`.

Formalized by `StatMech.Onsager.main_torus_pressure_decomposition`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/OnsagerFormula.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/OnsagerFormula.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/onsager-s-solution-of-the-two-dimensional-ising/index.html#main-torus-pressure-decomposition).

## Onsager's formula from the spin Kac-Ward identities

Onsager's formula follows from the spin Kac-Ward identities at all `β`.

Formalized by `StatMech.Onsager.main_free_energy_from_spin_kacWard`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/OnsagerFormula.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/OnsagerFormula.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/onsager-s-solution-of-the-two-dimensional-ising/index.html#main-free-energy-from-spin-kac-ward).

## Spin Kac-Ward identities from the edge-weighted root identity

The spin Kac-Ward identities follow from the edge-weighted root identity on all tori.

Formalized by `StatMech.Onsager.main_spin_kacWard_from_weighted_root`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/OnsagerFormula.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/OnsagerFormula.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/onsager-s-solution-of-the-two-dimensional-ising/index.html#main-spin-kac-ward-from-weighted-root).

## Edge-weighted root identity from the decorated-torus formal identity

The edge-weighted root identity follows from the formal Kac-Ward identity on the decorated
torus.

Formalized by `StatMech.Onsager.main_weighted_root_from_decorated_formal`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/OnsagerFormula.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/OnsagerFormula.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/onsager-s-solution-of-the-two-dimensional-ising/index.html#main-weighted-root-from-decorated-formal).

## Spin Kac-Ward identities from the decorated-torus formal identity

The spin Kac-Ward identities follow from the formal Kac-Ward identity on all decorated tori.

Formalized by `StatMech.Onsager.main_spin_kacWard_from_decorated_formal`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/OnsagerFormula.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/OnsagerFormula.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/onsager-s-solution-of-the-two-dimensional-ising/index.html#main-spin-kac-ward-from-decorated-formal).

## Onsager's formula

**Onsager's formula** (L. Onsager, *Crystal statistics. I. A two-dimensional model with an
order-disorder transition*, Phys. Rev. 65, 1944). For the zero-field nearest-neighbor Ising model
with unit coupling on the `L × L` torus, the pressure `log Z_L(β) / L²` converges, for every
`β ≥ 0`, to `log 2 + (1 / 8π²) ∫∫_{[-π, π]²} log (cosh² 2β - sinh 2β (cos k₁ + cos k₂))`.

The limit runs over all `L` (the sequence is `0` for `L ≤ 2`, which does not affect it). Negative
`β` (antiferromagnetic coupling) is not covered: the right-hand side is even in `β`, but on odd tori the corresponding limit involves frustrated configurations.
Non-analyticity at `β_c` is not part of the statement.

Formalized by `StatMech.Onsager.main_free_energy`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/OnsagerFormula.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/OnsagerFormula.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/onsager-s-solution-of-the-two-dimensional-ising/index.html#main-free-energy).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Onsager's solution of the two-dimensional Ising model](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/onsager-s-solution-of-the-two-dimensional-ising/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/onsager-s-solution-of-the-two-dimensional-ising)
