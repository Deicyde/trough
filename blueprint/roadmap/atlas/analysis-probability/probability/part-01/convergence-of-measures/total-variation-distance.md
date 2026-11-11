---
declaration: section
origin: cited
lean: MathlibExt.Probability.TotalVariationDistance.totalVariationDist, MathlibExt.Probability.TotalVariationDistance.totalVariationDist_nonneg, MathlibExt.Probability.TotalVariationDistance.totalVariationDist_self, MathlibExt.Probability.TotalVariationDistance.totalVariationDist_comm, MathlibExt.Probability.TotalVariationDistance.totalVariationDist_triangle, MathlibExt.Probability.TotalVariationDistance.totalVariationDist_le_one, MathlibExt.Probability.TotalVariationDistance.totalVariationDist_eq_zero_iff, MathlibExt.Probability.TotalVariationDistance.totalVariationDist_dirac
statement: formalized
proof: formalized
---

# Total variation distance

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/convergence-of-measures/total-variation-distance/index.html).

## Total variation distance between finite measures

For finite measures $\mu$ and $\nu$ on a
measurable space $\Omega$, the total variation distance $d_{TV}(\mu, \nu)$ is the real number
$\sup_B |\mu(B) - \nu(B)|$, where the supremum runs over all measurable sets $B \subseteq \Omega$
and the masses $\mu(B)$ and $\nu(B)$ are taken as real numbers.

## Sources

- the probability-measure specialization is the Lecture 12 definition. The inline finiteness binders are part of this public interface.

Formalized by `MathlibExt.Probability.TotalVariationDistance.totalVariationDist`, a definition declared in [MathlibExt/Probability/TotalVariationDistance.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/TotalVariationDistance.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/convergence-of-measures/total-variation-distance/index.html#total-variation-dist).

## Total variation distance is nonnegative

For finite measures $\mu$ and $\nu$ on a measurable
space, the total variation distance satisfies $0 \le d_{TV}(\mu, \nu)$.

Formalized by `MathlibExt.Probability.TotalVariationDistance.totalVariationDist_nonneg`, a theorem declared in [MathlibExt/Probability/TotalVariationDistance.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/TotalVariationDistance.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/convergence-of-measures/total-variation-distance/index.html#total-variation-dist-nonneg).

## Total variation distance from a measure to itself

For every finite measure $\mu$ on a
measurable space, the total variation distance $d_{TV}(\mu, \mu)$ is $0$.

Formalized by `MathlibExt.Probability.TotalVariationDistance.totalVariationDist_self`, a theorem declared in [MathlibExt/Probability/TotalVariationDistance.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/TotalVariationDistance.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/convergence-of-measures/total-variation-distance/index.html#total-variation-dist-self).

## Symmetry of total variation distance

For finite measures $\mu$ and $\nu$ on a measurable
space, the total variation distances satisfy $d_{TV}(\mu, \nu) = d_{TV}(\nu, \mu)$.

Formalized by `MathlibExt.Probability.TotalVariationDistance.totalVariationDist_comm`, a theorem declared in [MathlibExt/Probability/TotalVariationDistance.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/TotalVariationDistance.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/convergence-of-measures/total-variation-distance/index.html#total-variation-dist-comm).

## Triangle inequality for total variation distance

For finite measures $\mu$, $\nu$ and
$\rho$ on a measurable space, the total variation distance satisfies
$d_{TV}(\mu, \rho) \le d_{TV}(\mu, \nu) + d_{TV}(\nu, \rho)$.

Formalized by `MathlibExt.Probability.TotalVariationDistance.totalVariationDist_triangle`, a theorem declared in [MathlibExt/Probability/TotalVariationDistance.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/TotalVariationDistance.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/convergence-of-measures/total-variation-distance/index.html#total-variation-dist-triangle).

## Total variation distance between probability measures is at most one

For probability
measures $\mu$ and $\nu$ on a measurable space, the total variation distance satisfies
$d_{TV}(\mu, \nu) \le 1$.

Formalized by `MathlibExt.Probability.TotalVariationDistance.totalVariationDist_le_one`, a theorem declared in [MathlibExt/Probability/TotalVariationDistance.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/TotalVariationDistance.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/convergence-of-measures/total-variation-distance/index.html#total-variation-dist-le-one).

## Total variation distance vanishes only for equal measures

For finite measures $\mu$ and
$\nu$ on a measurable space, the total variation distance $d_{TV}(\mu, \nu)$ is $0$ if and only
if $\mu = \nu$.

Formalized by `MathlibExt.Probability.TotalVariationDistance.totalVariationDist_eq_zero_iff`, a theorem declared in [MathlibExt/Probability/TotalVariationDistance.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/TotalVariationDistance.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/convergence-of-measures/total-variation-distance/index.html#total-variation-dist-eq-zero-iff).

## Total variation distance between Dirac measures

Let $\Omega$ be a measurable space in which
every singleton is measurable, and let $a, b \in \Omega$. The total variation distance between the
Dirac measures $\delta_a$ and $\delta_b$ is $0$ if $a = b$ and $1$ if $a \neq b$.

Formalized by `MathlibExt.Probability.TotalVariationDistance.totalVariationDist_dirac`, a theorem declared in [MathlibExt/Probability/TotalVariationDistance.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/TotalVariationDistance.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/convergence-of-measures/total-variation-distance/index.html#total-variation-dist-dirac).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Total variation distance](https://deicyde.github.io/atlas-lean/roadmap/Probability/convergence-of-measures/total-variation-distance/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/convergence-of-measures/total-variation-distance)
