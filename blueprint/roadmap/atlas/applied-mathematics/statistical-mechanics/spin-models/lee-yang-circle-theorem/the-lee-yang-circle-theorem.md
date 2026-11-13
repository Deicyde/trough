---
declaration: section
origin: cited
lean: StatMech.LeeYang.asano_quadratic_contraction, StatMech.LeeYang.IsMultiAffine, StatMech.LeeYang.PolydiscStable, StatMech.LeeYang.asanoContract, StatMech.LeeYang.asanoContract_stable, StatMech.LeeYang.leeYang_edgeFactor_ne_zero, StatMech.LeeYang.LeeYangVar, StatMech.LeeYang.leeYangAnchor
statement: formalized
proof: formalized
---

# The Lee–Yang circle theorem

33 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/lee-yang-circle-theorem/the-lee-yang-circle-theorem/index.html).

## A. Asano contraction

## Asano's lemma in one variable

Asano's lemma in one variable: if `A + E t + D t²` has no zero in the open unit disk, then
neither has `A + D t`.

Formalized by `StatMech.LeeYang.asano_quadratic_contraction`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/lee-yang-circle-theorem/the-lee-yang-circle-theorem/index.html#asano-quadratic-contraction).

## Multi-affine function of several complex variables

A function of finitely many complex variables is multi-affine if it is affine in each variable
separately.

Formalized by `StatMech.LeeYang.IsMultiAffine`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/lee-yang-circle-theorem/the-lee-yang-circle-theorem/index.html#is-multi-affine).

## Polydisc stability of a function of complex variables

A function of complex variables is polydisc stable if it has no zero when every variable lies in
the open unit disk.

Formalized by `StatMech.LeeYang.PolydiscStable`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/lee-yang-circle-theorem/the-lee-yang-circle-theorem/index.html#polydisc-stable).

## Asano contraction of two variables

The Asano contraction of the variables `i` and `j`: for `p = A + B z_i + C z_j + D z_i z_j` it
is `A + D z_i`, computed from the values of `p` at `z_i, z_j ∈ {0, 1}`.

Formalized by `StatMech.LeeYang.asanoContract`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/lee-yang-circle-theorem/the-lee-yang-circle-theorem/index.html#asano-contract).

## Asano's contraction lemma

Asano's contraction lemma: the Asano contraction of a multi-affine polydisc-stable polynomial is
polydisc stable (Asano, Phys. Rev. Lett. 24 (1970)).

Formalized by `StatMech.LeeYang.asanoContract_stable`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/lee-yang-circle-theorem/the-lee-yang-circle-theorem/index.html#asano-contract-stable).

## Edge factor has no zero in the open unit bidisk for 0 ≤ r ≤ 1

The two-variable edge factor `1 + ab + r (a + b)` with `0 ≤ r ≤ 1` has no zero in the open unit
bidisk.

Formalized by `StatMech.LeeYang.leeYang_edgeFactor_ne_zero`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/lee-yang-circle-theorem/the-lee-yang-circle-theorem/index.html#lee-yang-edge-factor-ne-zero).

## Variables of the half-edge polynomial

The variables of the half-edge polynomial: one anchor variable per vertex and one half-edge
variable per incidence `(v, e)`.

Formalized by `StatMech.LeeYang.LeeYangVar`, an abbreviation declared in [PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean, line 293](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean#L293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/lee-yang-circle-theorem/the-lee-yang-circle-theorem/index.html#lee-yang-var).

## Anchor variable of a vertex

The anchor variable of a vertex.

Formalized by `StatMech.LeeYang.leeYangAnchor`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean, line 296](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean#L296). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/lee-yang-circle-theorem/the-lee-yang-circle-theorem/index.html#lee-yang-anchor).

## Half-edge variable of an incidence

The half-edge variable of the incidence `(v, e)`.

Formalized by `StatMech.LeeYang.leeYangHalf`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean, line 299](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean#L299). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/lee-yang-circle-theorem/the-lee-yang-circle-theorem/index.html#lee-yang-half).

## Edge factor in half-edge variables

The edge factor `1 + w_u w_v + e^{-2β} (w_u + w_v)` of the edge `e = {u, v}`, in its half-edge
variables.

Formalized by `StatMech.LeeYang.leeYangNormalizedEdgeFactor`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean, line 303](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean#L303). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/lee-yang-circle-theorem/the-lee-yang-circle-theorem/index.html#lee-yang-normalized-edge-factor).

## Half-edge polynomial of a graph

The half-edge polynomial: the product of `1 + z_v` over the vertices and of the edge factors
over the edges.

Formalized by `StatMech.LeeYang.leeYangHalfEdgeProduct`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean, line 314](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean#L314). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/lee-yang-circle-theorem/the-lee-yang-circle-theorem/index.html#lee-yang-half-edge-product).

## Vertex part of the half-edge polynomial

The vertex part `∏_v (1 + z_v)` of the half-edge polynomial.

Formalized by `StatMech.LeeYang.leeYangAnchorProduct`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean, line 320](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean#L320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/lee-yang-circle-theorem/the-lee-yang-circle-theorem/index.html#lee-yang-anchor-product).

## Edge part of the half-edge polynomial

The edge part of the half-edge polynomial: the product of the edge factors.

Formalized by `StatMech.LeeYang.leeYangEdgeProduct`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean, line 324](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean#L324). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/lee-yang-circle-theorem/the-lee-yang-circle-theorem/index.html#lee-yang-edge-product).

## Successive Asano contraction along a list of incidences

Successive Asano contraction of the half-edge variable of each incidence in the list into the
anchor variable of its vertex.

Formalized by `StatMech.LeeYang.leeYangContractList`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean, line 536](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean#L536). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/lee-yang-circle-theorem/the-lee-yang-circle-theorem/index.html#lee-yang-contract-list).

## Vertex–edge incidences of a graph

The incidences `(v, e)` of `G`, with `v` an endpoint of `e`.

Formalized by `StatMech.LeeYang.leeYangIncidenceFinset`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean, line 567](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean#L567). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/lee-yang-circle-theorem/the-lee-yang-circle-theorem/index.html#lee-yang-incidence-finset).

## Half-edge polynomial with every incidence contracted

The half-edge polynomial after contracting every incidence.

Formalized by `StatMech.LeeYang.leeYangContractedProduct`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean, line 571](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean#L571). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/lee-yang-circle-theorem/the-lee-yang-circle-theorem/index.html#lee-yang-contracted-product).

## Monomial of a set of variables

The monomial `∏_{i ∈ S} z_i`.

Formalized by `StatMech.LeeYang.leeYangMonomial`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean, line 588](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean#L588). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/lee-yang-circle-theorem/the-lee-yang-circle-theorem/index.html#lee-yang-monomial).

## Chosen first endpoint of an edge

A chosen first endpoint of an edge.

Formalized by `StatMech.LeeYang.leeYangEndpoint0`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean, line 650](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean#L650). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/lee-yang-circle-theorem/the-lee-yang-circle-theorem/index.html#lee-yang-endpoint0).

## Other endpoint of an edge

The other endpoint of an edge.

Formalized by `StatMech.LeeYang.leeYangEndpoint1`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean, line 653](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean#L653). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/lee-yang-circle-theorem/the-lee-yang-circle-theorem/index.html#lee-yang-endpoint1).

## Term of a vertex factor selected by a Boolean choice

The term of `1 + z_v` selected by a Boolean choice.

Formalized by `StatMech.LeeYang.leeYangAnchorChoiceFactor`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean, line 670](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean#L670). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/lee-yang-circle-theorem/the-lee-yang-circle-theorem/index.html#lee-yang-anchor-choice-factor).

## Term of an edge factor selected by two Boolean choices

The term of the edge factor selected by a pair of Boolean choices, one per endpoint.

Formalized by `StatMech.LeeYang.leeYangEdgeChoiceFactor`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean, line 674](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean#L674). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/lee-yang-circle-theorem/the-lee-yang-circle-theorem/index.html#lee-yang-edge-choice-factor).

## Term of the expanded half-edge polynomial for a choice

The term of the expanded half-edge polynomial selected by a choice at every vertex and every
edge.

Formalized by `StatMech.LeeYang.leeYangChoiceTerm`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean, line 708](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean#L708). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/lee-yang-circle-theorem/the-lee-yang-circle-theorem/index.html#lee-yang-choice-term).

## Coefficient of a term of the expanded half-edge polynomial

The coefficient of a term of the expanded half-edge polynomial: `e^{-2β}` for every edge whose
two choices differ.

Formalized by `StatMech.LeeYang.leeYangChoiceWeight`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean, line 732](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean#L732). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/lee-yang-circle-theorem/the-lee-yang-circle-theorem/index.html#lee-yang-choice-weight).

## Selection indicator of a choice on the variables

Whether a choice selects each variable.

Formalized by `StatMech.LeeYang.leeYangChoiceSelected`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean, line 738](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean#L738). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/lee-yang-circle-theorem/the-lee-yang-circle-theorem/index.html#lee-yang-choice-selected).

## Set of variables selected by a choice

The set of variables selected by a choice, the support of its monomial.

Formalized by `StatMech.LeeYang.leeYangChoiceSupport`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean, line 748](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean#L748). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/lee-yang-circle-theorem/the-lee-yang-circle-theorem/index.html#lee-yang-choice-support).

## Removal of listed half-edge variables from a variable set

Remove from a set of variables the half-edge variables of the listed incidences.

Formalized by `StatMech.LeeYang.leeYangEraseHalves`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean, line 856](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean#L856). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/lee-yang-circle-theorem/the-lee-yang-circle-theorem/index.html#lee-yang-erase-halves).

## Consistency of a variable set with a list of incidences

A set of variables is consistent with a list of incidences if each listed half-edge variable is
selected exactly when the anchor variable of its vertex is.

Formalized by `StatMech.LeeYang.LeeYangConsistent`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean, line 862](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean#L862). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/lee-yang-circle-theorem/the-lee-yang-circle-theorem/index.html#lee-yang-consistent).

## Edge choices induced by a spin configuration

The edge choices induced by a spin configuration: each edge copies the spins of its
endpoints.

Formalized by `StatMech.LeeYang.leeYangTauOf`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean, line 942](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean#L942). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/lee-yang-circle-theorem/the-lee-yang-circle-theorem/index.html#lee-yang-tau-of).

## Anchor variables of the vertices with plus spin

The anchor variables of the vertices with spin `true`.

Formalized by `StatMech.LeeYang.leeYangAnchorSupport`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean, line 1020](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean#L1020). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/lee-yang-circle-theorem/the-lee-yang-circle-theorem/index.html#lee-yang-anchor-support).

## Diagonal point with anchors at q and half-edge variables at zero

The point with every anchor variable equal to `q` and every half-edge variable equal to `0`.

Formalized by `StatMech.LeeYang.leeYangDiagonal`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean, line 1101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean#L1101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/lee-yang-circle-theorem/the-lee-yang-circle-theorem/index.html#lee-yang-diagonal).

## Real disagreement weight of a spin configuration

The real weight `∏_e e^{-2β [σ_u ≠ σ_v]}` of a spin configuration.

Formalized by `StatMech.LeeYang.leeYangRealChoiceWeight`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean, line 1117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean#L1117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/lee-yang-circle-theorem/the-lee-yang-circle-theorem/index.html#lee-yang-real-choice-weight).

## Ferromagnetic Lee–Yang polynomial has no zero in the open unit disk

The Lee–Yang polynomial of a ferromagnetic Ising model has no zero in the open unit disk.

Formalized by `StatMech.LeeYang.leeYangComplexPolynomial_ne_zero_in_openUnitDisk`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean, line 1217](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean#L1217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/lee-yang-circle-theorem/the-lee-yang-circle-theorem/index.html#lee-yang-complex-polynomial-ne-zero-in-o).

## Lee–Yang circle theorem

For the Ising model on a finite graph with uniform ferromagnetic
coupling and `β ≥ 0`, every complex zero of the partition function in the fugacity `z =
e^{-2βh}` lies on the unit circle (Lee and Yang, *Statistical theory of equations of state and
phase transitions. II*, Phys. Rev. 87 (1952)).

Formalized by `StatMech.LeeYang.finiteGraph_hasLeeYangCircle`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean, line 1239](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/LeeYang/LeeYangAsano.lean#L1239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/lee-yang-circle-theorem/the-lee-yang-circle-theorem/index.html#finite-graph-has-lee-yang-circle).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The Lee–Yang circle theorem](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/lee-yang-circle-theorem/the-lee-yang-circle-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/StatisticalMechanics/spin-models/lee-yang-circle-theorem/the-lee-yang-circle-theorem)
