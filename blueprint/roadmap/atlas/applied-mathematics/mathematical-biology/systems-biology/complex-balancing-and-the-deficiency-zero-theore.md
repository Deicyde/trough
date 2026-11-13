---
declaration: section
origin: cited
lean: MathlibExt.Biology.Dynamics.ComplexBalanced.ReactionNetwork, MathlibExt.Biology.Dynamics.ComplexBalanced.ReactionNetwork.stoichiometricSubspace, MathlibExt.Biology.Dynamics.ComplexBalanced.ReactionNetwork.massActionField, MathlibExt.Biology.Dynamics.ComplexBalanced.ReactionNetwork.rate, MathlibExt.Biology.Dynamics.ComplexBalanced.ReactionNetwork.IsComplexBalanced, MathlibExt.Biology.Dynamics.ComplexBalanced.ReactionNetwork.pseudoHelmholtz, MathlibExt.Biology.Dynamics.ComplexBalanced.ReactionNetwork.helmholtzRate, MathlibExt.Biology.Dynamics.ComplexBalanced.ReactionNetwork.sum_rate_mul_prod_eq
statement: formalized
---

# Complex balancing and the deficiency-zero theorem

27 results, 26 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/complex-balancing-and-the-deficiency-zero-theore/index.html).

## Chemical reaction network

A chemical reaction network on the species `S` with reactions indexed by `ρ`: reaction `r`
turns the source complex `src r` into the product complex `prod r` (stoichiometric
coefficients).

Formalized by `MathlibExt.Biology.Dynamics.ComplexBalanced.ReactionNetwork`, a structure declared in [MathlibExt/Biology/Dynamics/ComplexBalanced.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/ComplexBalanced.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/complex-balancing-and-the-deficiency-zero-theore/index.html#reaction-network).

## Stoichiometric subspace

The stoichiometric subspace: the span of the reaction vectors `prod r - src r`.

Formalized by `MathlibExt.Biology.Dynamics.ComplexBalanced.ReactionNetwork.stoichiometricSubspace`, a definition declared in [MathlibExt/Biology/Dynamics/ComplexBalanced.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/ComplexBalanced.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/complex-balancing-and-the-deficiency-zero-theore/index.html#stoichiometric-subspace).

## Mass-action vector field

The mass-action vector field with rate constants `k`:
`x ↦ ∑_r k r (∏_s x_s ^ (src r s)) (prod r - src r)`.

Formalized by `MathlibExt.Biology.Dynamics.ComplexBalanced.ReactionNetwork.massActionField`, a definition declared in [MathlibExt/Biology/Dynamics/ComplexBalanced.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/ComplexBalanced.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/complex-balancing-and-the-deficiency-zero-theore/index.html#mass-action-field).

## Mass-action reaction rate

The mass-action rate `k r * ∏_s c_s ^ (src r s)` of reaction `r` at concentrations `c`.

Formalized by `MathlibExt.Biology.Dynamics.ComplexBalanced.ReactionNetwork.rate`, a definition declared in [MathlibExt/Biology/Dynamics/ComplexBalanced.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/ComplexBalanced.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/complex-balancing-and-the-deficiency-zero-theore/index.html#rate).

## Complex-balanced concentrations

Concentrations `c` are complex balanced for the rate constants `k`: at every complex `z`,
the total rate of the reactions with source `z` equals the total rate of the reactions with
product `z`. (Complexes that occur in no reaction give `0 = 0`.)

## Sources

- Horn & Jackson (1972); Feinberg (2019), ch. 15.

Formalized by `MathlibExt.Biology.Dynamics.ComplexBalanced.ReactionNetwork.IsComplexBalanced`, a definition declared in [MathlibExt/Biology/Dynamics/ComplexBalanced.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/ComplexBalanced.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/complex-balancing-and-the-deficiency-zero-theore/index.html#is-complex-balanced).

## Pseudo-Helmholtz function

The pseudo-Helmholtz function `G(c) = ∑_s c_s (log c_s - log c*_s - 1)` relative to the
reference concentrations `cstar` (Horn & Jackson 1972). It is meaningful for positive `c`
and `cstar`; elsewhere `Real.log` takes junk values.

Formalized by `MathlibExt.Biology.Dynamics.ComplexBalanced.ReactionNetwork.pseudoHelmholtz`, a definition declared in [MathlibExt/Biology/Dynamics/ComplexBalanced.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/ComplexBalanced.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/complex-balancing-and-the-deficiency-zero-theore/index.html#pseudo-helmholtz).

## Rate of change of the pseudo-Helmholtz function

The rate of change of the pseudo-Helmholtz function along the mass-action vector field,
`∑_s (log c_s - log c*_s) f_s(c)`: the derivative of `pseudoHelmholtz cstar` at `c > 0`
applied to `massActionField k c` (`hasDerivAt_pseudoHelmholtz`).

Formalized by `MathlibExt.Biology.Dynamics.ComplexBalanced.ReactionNetwork.helmholtzRate`, a definition declared in [MathlibExt/Biology/Dynamics/ComplexBalanced.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/ComplexBalanced.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/complex-balancing-and-the-deficiency-zero-theore/index.html#helmholtz-rate).

## Complex balance exchanges source and product sums

Complex balance at `c` rewrites the rate-weighted sum of any function of the products as
the same sum over the sources (for all real `c` and `k`).

Formalized by `MathlibExt.Biology.Dynamics.ComplexBalanced.ReactionNetwork.sum_rate_mul_prod_eq`, a theorem declared in [MathlibExt/Biology/Dynamics/ComplexBalanced.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/ComplexBalanced.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/complex-balancing-and-the-deficiency-zero-theore/index.html#sum-rate-mul-prod-eq).

## Complex-balanced states are equilibria

A complex-balanced state is an equilibrium of the mass-action system (for all real `c`
and `k`). Source: Horn & Jackson (1972).

Formalized by `MathlibExt.Biology.Dynamics.ComplexBalanced.ReactionNetwork.massActionField_eq_zero_of_isComplexBalanced`, a theorem declared in [MathlibExt/Biology/Dynamics/ComplexBalanced.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/ComplexBalanced.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/complex-balancing-and-the-deficiency-zero-theore/index.html#mass-action-field-eq-zero-of-is-complex).

## Horn–Jackson inequality

If `c*` is a positive complex-balanced equilibrium for
positive rate constants, the pseudo-Helmholtz function does not increase along the
mass-action vector field at any positive `c`. Source: Horn & Jackson (1972);
Feinberg (2019), ch. 15.

Formalized by `MathlibExt.Biology.Dynamics.ComplexBalanced.ReactionNetwork.helmholtzRate_nonpos`, a theorem declared in [MathlibExt/Biology/Dynamics/ComplexBalanced.lean, line 269](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/ComplexBalanced.lean#L269). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/complex-balancing-and-the-deficiency-zero-theore/index.html#helmholtz-rate-nonpos).

## Equality in the Horn–Jackson inequality

Under the hypotheses of
`helmholtzRate_nonpos`, the rate of change of the pseudo-Helmholtz function vanishes at a
positive `c` exactly when `c` is an equilibrium. Source: Horn & Jackson (1972).

Formalized by `MathlibExt.Biology.Dynamics.ComplexBalanced.ReactionNetwork.helmholtzRate_eq_zero_iff`, a theorem declared in [MathlibExt/Biology/Dynamics/ComplexBalanced.lean, line 279](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/ComplexBalanced.lean#L279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/complex-balancing-and-the-deficiency-zero-theore/index.html#helmholtz-rate-eq-zero-iff).

## Horn–Jackson

If a mass-action system with positive rate constants has a positive
complex-balanced equilibrium, then every positive equilibrium is complex balanced.

## Sources

- Horn & Jackson (1972); Feinberg (2019), ch. 15.

Formalized by `MathlibExt.Biology.Dynamics.ComplexBalanced.ReactionNetwork.isComplexBalanced_of_massActionField_eq_zero`, a theorem declared in [MathlibExt/Biology/Dynamics/ComplexBalanced.lean, line 291](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/ComplexBalanced.lean#L291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/complex-balancing-and-the-deficiency-zero-theore/index.html#is-complex-balanced-of-mass-action-field).

## Horn–Jackson: the positive equilibria

If `c*` is a positive complex-balanced
equilibrium for positive rate constants, the positive equilibria are exactly the positive
`c` whose `log c - log c*` is orthogonal (for the dot product) to the stoichiometric
subspace. Source: Horn & Jackson (1972); Feinberg (2019), ch. 15.

Formalized by `MathlibExt.Biology.Dynamics.ComplexBalanced.ReactionNetwork.positiveEquilibria_eq`, a theorem declared in [MathlibExt/Biology/Dynamics/ComplexBalanced.lean, line 309](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/ComplexBalanced.lean#L309). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/complex-balancing-and-the-deficiency-zero-theore/index.html#positive-equilibria-eq).

## Birch's theorem, existence

For any subspace `W` of `S → ℝ` and positive `a`, `b`
there is a positive `c` with `c - b ∈ W` and `log c - log a` orthogonal to `W` (for the dot
product). Source: Birch (1963); Horn & Jackson (1972).

Formalized by `MathlibExt.Biology.Dynamics.ComplexBalanced.exists_pos_sub_mem_log_orthogonal`, a theorem declared in [MathlibExt/Biology/Dynamics/ComplexBalanced.lean, line 373](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/ComplexBalanced.lean#L373). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/complex-balancing-and-the-deficiency-zero-theore/index.html#exists-pos-sub-mem-log-orthogonal).

## Birch's theorem, uniqueness

Two positive vectors whose difference lies in a subspace
`W` and whose logarithms differ by a vector orthogonal to `W` are equal.

## Sources

- Birch (1963); Horn & Jackson (1972).

Formalized by `MathlibExt.Biology.Dynamics.ComplexBalanced.eq_of_sub_mem_log_orthogonal`, a theorem declared in [MathlibExt/Biology/Dynamics/ComplexBalanced.lean, line 449](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/ComplexBalanced.lean#L449). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/complex-balancing-and-the-deficiency-zero-theore/index.html#eq-of-sub-mem-log-orthogonal).

## Horn–Jackson: one equilibrium per compatibility class

If a mass-action system with
positive rate constants has a positive complex-balanced equilibrium, then each positive
stoichiometric compatibility class `(x₀ + 𝒮) ∩ ℝ_{>0}^S`, `x₀ > 0`, contains exactly one
positive equilibrium. Source: Horn & Jackson (1972); Feinberg (2019), ch. 15.

Formalized by `MathlibExt.Biology.Dynamics.ComplexBalanced.ReactionNetwork.existsUnique_equilibrium_of_isComplexBalanced`, a theorem declared in [MathlibExt/Biology/Dynamics/ComplexBalanced.lean, line 474](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/ComplexBalanced.lean#L474). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/complex-balancing-and-the-deficiency-zero-theore/index.html#exists-unique-equilibrium-of-is-complex).

## Pseudo-Helmholtz function along positive mass-action solutions

The pseudo-Helmholtz function has time derivative `helmholtzRate` along a solution of the
mass-action system, at any time where the solution is positive.

Formalized by `MathlibExt.Biology.Dynamics.ComplexBalanced.ReactionNetwork.hasDerivAt_pseudoHelmholtz`, a theorem declared in [MathlibExt/Biology/Dynamics/ComplexBalanced.lean, line 499](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/ComplexBalanced.lean#L499). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/complex-balancing-and-the-deficiency-zero-theore/index.html#has-deriv-at-pseudo-helmholtz).

## The pseudo-Helmholtz function does not increase along solutions

Along a solution of a
mass-action system with positive rate constants and a positive complex-balanced equilibrium
`c*`, positive and differentiable (two-sided) at every `t ≥ 0`, `G(x t)` is nonincreasing on
`[0, ∞)`.

## Sources

- Horn & Jackson (1972).

Formalized by `MathlibExt.Biology.Dynamics.ComplexBalanced.ReactionNetwork.antitoneOn_pseudoHelmholtz`, a theorem declared in [MathlibExt/Biology/Dynamics/ComplexBalanced.lean, line 516](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/ComplexBalanced.lean#L516). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/complex-balancing-and-the-deficiency-zero-theore/index.html#antitone-on-pseudo-helmholtz).

## Complexes of a chemical reaction network

The complexes of the network: the sources and products of its reactions.

Formalized by `MathlibExt.Biology.Dynamics.ComplexBalanced.ReactionNetwork.complexes`, a definition declared in [MathlibExt/Biology/Dynamics/DeficiencyZero/API.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/DeficiencyZero/API.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/complex-balancing-and-the-deficiency-zero-theore/index.html#complexes).

## Directed reaction relation on complexes

The directed reaction relation on complexes: `y ⟶ y'` if some reaction has source `y` and
product `y'`.

Formalized by `MathlibExt.Biology.Dynamics.ComplexBalanced.ReactionNetwork.Reacts`, a definition declared in [MathlibExt/Biology/Dynamics/DeficiencyZero/API.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/DeficiencyZero/API.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/complex-balancing-and-the-deficiency-zero-theore/index.html#reacts).

## Linkage graph of a reaction network

The undirected reaction graph on the complexes: distinct complexes are adjacent when one
reacts to the other.

Formalized by `MathlibExt.Biology.Dynamics.ComplexBalanced.ReactionNetwork.linkageGraph`, a definition declared in [MathlibExt/Biology/Dynamics/DeficiencyZero/API.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/DeficiencyZero/API.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/complex-balancing-and-the-deficiency-zero-theore/index.html#linkage-graph).

## Number of linkage classes of a reaction network

The number of linkage classes of a network with finitely many complexes: connected
components of the undirected reaction graph.

Formalized by `MathlibExt.Biology.Dynamics.ComplexBalanced.ReactionNetwork.numLinkageClasses`, a definition declared in [MathlibExt/Biology/Dynamics/DeficiencyZero/API.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/DeficiencyZero/API.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/complex-balancing-and-the-deficiency-zero-theore/index.html#num-linkage-classes).

## Deficiency of a chemical reaction network

The deficiency `δ = n - ℓ - s` (number of complexes, linkage classes, dimension of the
stoichiometric subspace) of a network with finitely many complexes.

Formalized by `MathlibExt.Biology.Dynamics.ComplexBalanced.ReactionNetwork.deficiency`, a definition declared in [MathlibExt/Biology/Dynamics/DeficiencyZero/API.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/DeficiencyZero/API.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/complex-balancing-and-the-deficiency-zero-theore/index.html#deficiency).

## Weakly reversible reaction network

The network is weakly reversible: for every reaction `y → y'` there is a directed path of
reactions from `y'` back to `y`.

Formalized by `MathlibExt.Biology.Dynamics.ComplexBalanced.ReactionNetwork.IsWeaklyReversible`, a definition declared in [MathlibExt/Biology/Dynamics/DeficiencyZero/API.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/DeficiencyZero/API.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/complex-balancing-and-the-deficiency-zero-theore/index.html#is-weakly-reversible).

## Horn–Feinberg: complex balancing for every choice of rate constants

A weakly
reversible mass-action network of deficiency zero has, for any positive rate constants, a
positive complex-balanced equilibrium. Together with
`existsUnique_equilibrium_of_isComplexBalanced` this gives `existsUnique_equilibrium`.

## Sources

- Horn (1972); Feinberg (1972); Feinberg (1987).

Formalized by `MathlibExt.Biology.Dynamics.ComplexBalanced.ReactionNetwork.exists_pos_isComplexBalanced`, a theorem declared in [MathlibExt/Biology/Dynamics/DeficiencyZero/Integration.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/DeficiencyZero/Integration.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/complex-balancing-and-the-deficiency-zero-theore/index.html#exists-pos-is-complex-balanced).

## Deficiency-zero theorem, weakly reversible case

A weakly reversible mass-action
network of deficiency zero has, for any positive rate constants, exactly one equilibrium in
each positive stoichiometric compatibility class.

## Sources

- Horn (1972); Horn & Jackson (1972); Feinberg (1987).

Formalized by `MathlibExt.Biology.Dynamics.ComplexBalanced.ReactionNetwork.existsUnique_equilibrium`, a theorem declared in [MathlibExt/Biology/Dynamics/DeficiencyZero/Integration.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/DeficiencyZero/Integration.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/complex-balancing-and-the-deficiency-zero-theore/index.html#exists-unique-equilibrium).

## Deficiency-zero theorem, non-weakly-reversible case

A mass-action network of
deficiency zero that is not weakly reversible has no positive equilibrium for any positive
rate constants.

## Sources

- Feinberg (1987).

Stated but not proved: `MathlibExt.Biology.Dynamics.ComplexBalanced.ReactionNetwork.not_exists_positive_equilibrium` is written with `theorem_wanted` in [WantedExt/Biology/Dynamics/DeficiencyZeroWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Biology/Dynamics/DeficiencyZeroWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/complex-balancing-and-the-deficiency-zero-theore/index.html#not-exists-positive-equilibrium).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Complex balancing and the deficiency-zero theorem](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/complex-balancing-and-the-deficiency-zero-theore/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/systems-biology/complex-balancing-and-the-deficiency-zero-theore)
