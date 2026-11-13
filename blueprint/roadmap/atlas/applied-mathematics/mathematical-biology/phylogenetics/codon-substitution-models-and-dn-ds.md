---
declaration: section
origin: cited
lean: MathlibExt.Biology.Phylogenetics.CodonModel.Codon, MathlibExt.Biology.Phylogenetics.CodonModel.diffPositions, MathlibExt.Biology.Phylogenetics.CodonModel.IsSingleChange, MathlibExt.Biology.Phylogenetics.CodonModel.IsTransitionChange, MathlibExt.Biology.Phylogenetics.CodonModel.isSingleChange_comm, MathlibExt.Biology.Phylogenetics.CodonModel.isTransitionChange_comm, MathlibExt.Biology.Phylogenetics.CodonModel.gyExchange, MathlibExt.Biology.Phylogenetics.CodonModel.gyExchange_symm
statement: formalized
proof: formalized
---

# Codon substitution models and dN/dS

25 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/codon-substitution-models-and-dn-ds/index.html).

## Codon as a triple of nucleotides

A codon: three nucleotides, each in `Fin 4` (order `A, C, G, T`).

Formalized by `MathlibExt.Biology.Phylogenetics.CodonModel.Codon`, an abbreviation declared in [MathlibExt/Biology/Phylogenetics/CodonOmega.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/CodonOmega.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/codon-substitution-models-and-dn-ds/index.html#codon).

## Positions at which two codons differ

The positions at which two codons differ.

Formalized by `MathlibExt.Biology.Phylogenetics.CodonModel.diffPositions`, a definition declared in [MathlibExt/Biology/Phylogenetics/CodonOmega.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/CodonOmega.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/codon-substitution-models-and-dn-ds/index.html#diff-positions).

## Codons differing at exactly one position

Two codons differ at exactly one position.

Formalized by `MathlibExt.Biology.Phylogenetics.CodonModel.IsSingleChange`, a definition declared in [MathlibExt/Biology/Phylogenetics/CodonOmega.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/CodonOmega.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/codon-substitution-models-and-dn-ds/index.html#is-single-change).

## Codon change consisting of transitions

Every differing position is a transition (same parity: `A ↔ G` or `C ↔ T`).

Formalized by `MathlibExt.Biology.Phylogenetics.CodonModel.IsTransitionChange`, a definition declared in [MathlibExt/Biology/Phylogenetics/CodonOmega.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/CodonOmega.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/codon-substitution-models-and-dn-ds/index.html#is-transition-change).

## Symmetry of single-position codon changes

Differing at exactly one position is symmetric.

Formalized by `MathlibExt.Biology.Phylogenetics.CodonModel.isSingleChange_comm`, a theorem declared in [MathlibExt/Biology/Phylogenetics/CodonOmega.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/CodonOmega.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/codon-substitution-models-and-dn-ds/index.html#is-single-change-comm).

## Symmetry of transition codon changes

Being a transition change is symmetric.

Formalized by `MathlibExt.Biology.Phylogenetics.CodonModel.isTransitionChange_comm`, a theorem declared in [MathlibExt/Biology/Phylogenetics/CodonOmega.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/CodonOmega.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/codon-substitution-models-and-dn-ds/index.html#is-transition-change-comm).

## Goldman–Yang codon exchangeability

The **Goldman–Yang exchangeability** between codons `i` and `j`: `0` unless they differ at
one position; otherwise `κ` for a transition (`1` for a transversion), times `ω` if the amino
acid changes.

Formalized by `MathlibExt.Biology.Phylogenetics.CodonModel.gyExchange`, a definition declared in [MathlibExt/Biology/Phylogenetics/CodonOmega.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/CodonOmega.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/codon-substitution-models-and-dn-ds/index.html#gy-exchange).

## Symmetry of Goldman–Yang exchangeabilities

The Goldman–Yang exchangeabilities are symmetric.

Formalized by `MathlibExt.Biology.Phylogenetics.CodonModel.gyExchange_symm`, a theorem declared in [MathlibExt/Biology/Phylogenetics/CodonOmega.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/CodonOmega.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/codon-substitution-models-and-dn-ds/index.html#gy-exchange-symm).

## Dependence of Goldman–Yang exchangeabilities on ω

The nonsynonymous exchangeabilities are linear in `ω`, the synonymous ones do not
involve it.

Formalized by `MathlibExt.Biology.Phylogenetics.CodonModel.gyExchange_eq`, a theorem declared in [MathlibExt/Biology/Phylogenetics/CodonOmega.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/CodonOmega.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/codon-substitution-models-and-dn-ds/index.html#gy-exchange-eq).

## Goldman–Yang codon rate matrix

The **Goldman–Yang rate matrix** (Goldman & Yang 1994): the GTR matrix with codon
frequencies `π` and exchangeabilities `gyExchange`.

Formalized by `MathlibExt.Biology.Phylogenetics.CodonModel.gyRate`, a definition declared in [MathlibExt/Biology/Phylogenetics/CodonOmega.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/CodonOmega.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/codon-substitution-models-and-dn-ds/index.html#gy-rate).

## Stationary rate of synonymous substitutions

The stationary **rate of synonymous substitutions** per codon,
`ρ_S = ∑_{i ≠ j, aa i = aa j} π_i Q_ij`. This is the stationary rate when
`∑ i, π i = 1`; for unnormalized weights it is scaled by `(∑ i, π i) ^ 2`.

Formalized by `MathlibExt.Biology.Phylogenetics.CodonModel.synRate`, a definition declared in [MathlibExt/Biology/Phylogenetics/CodonOmega.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/CodonOmega.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/codon-substitution-models-and-dn-ds/index.html#syn-rate).

## Stationary rate of nonsynonymous substitutions

The stationary **rate of nonsynonymous substitutions** per codon,
`ρ_N = ∑_{aa i ≠ aa j} π_i Q_ij`. This is the stationary rate when
`∑ i, π i = 1`; for unnormalized weights it is scaled by `(∑ i, π i) ^ 2`.

Formalized by `MathlibExt.Biology.Phylogenetics.CodonModel.nonsynRate`, a definition declared in [MathlibExt/Biology/Phylogenetics/CodonOmega.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/CodonOmega.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/codon-substitution-models-and-dn-ds/index.html#nonsyn-rate).

## Number of synonymous sites per codon

The number of **synonymous sites** per codon, counted under `ω = 1`:
`S = 3 ρ_S(1) / (ρ_S(1) + ρ_N(1))`.

Formalized by `MathlibExt.Biology.Phylogenetics.CodonModel.synSites`, a definition declared in [MathlibExt/Biology/Phylogenetics/CodonOmega.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/CodonOmega.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/codon-substitution-models-and-dn-ds/index.html#syn-sites).

## Number of nonsynonymous sites per codon

The number of **nonsynonymous sites** per codon, counted under `ω = 1`:
`N = 3 ρ_N(1) / (ρ_S(1) + ρ_N(1))`.

Formalized by `MathlibExt.Biology.Phylogenetics.CodonModel.nonsynSites`, a definition declared in [MathlibExt/Biology/Phylogenetics/CodonOmega.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/CodonOmega.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/codon-substitution-models-and-dn-ds/index.html#nonsyn-sites).

## Synonymous substitution rate per synonymous site (dS)

The synonymous rate per synonymous site, `dS = ρ_S(ω) / S`.

Formalized by `MathlibExt.Biology.Phylogenetics.CodonModel.dS`, a definition declared in [MathlibExt/Biology/Phylogenetics/CodonOmega.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/CodonOmega.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/codon-substitution-models-and-dn-ds/index.html#d-s).

## Nonsynonymous substitution rate per nonsynonymous site (dN)

The nonsynonymous rate per nonsynonymous site, `dN = ρ_N(ω) / N`.

Formalized by `MathlibExt.Biology.Phylogenetics.CodonModel.dN`, a definition declared in [MathlibExt/Biology/Phylogenetics/CodonOmega.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/CodonOmega.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/codon-substitution-models-and-dn-ds/index.html#d-n).

## Off-diagonal entries of the Goldman–Yang rate matrix

Off the diagonal the Goldman–Yang rate is `gyExchange i j * π j`.

Formalized by `MathlibExt.Biology.Phylogenetics.CodonModel.gyRate_of_ne`, a theorem declared in [MathlibExt/Biology/Phylogenetics/CodonOmega.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/CodonOmega.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/codon-substitution-models-and-dn-ds/index.html#gy-rate-of-ne).

## Goldman–Yang matrix is a rate matrix

With nonnegative frequencies, `κ ≥ 0` and `ω ≥ 0`, the Goldman–Yang matrix is a rate
matrix.

Formalized by `MathlibExt.Biology.Phylogenetics.CodonModel.isRateMatrix_gyRate`, a theorem declared in [MathlibExt/Biology/Phylogenetics/CodonOmega.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/CodonOmega.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/codon-substitution-models-and-dn-ds/index.html#is-rate-matrix-gy-rate).

## The Goldman–Yang chain is reversible

It is in detailed balance with its codon
frequencies.

Formalized by `MathlibExt.Biology.Phylogenetics.CodonModel.isDetailedBalance_gyRate`, a theorem declared in [MathlibExt/Biology/Phylogenetics/CodonOmega.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/CodonOmega.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/codon-substitution-models-and-dn-ds/index.html#is-detailed-balance-gy-rate).

## Synonymous rate does not depend on ω

The synonymous rate does not depend on `ω`: `ρ_S(ω) = ρ_S(1)`.

Formalized by `MathlibExt.Biology.Phylogenetics.CodonModel.synRate_eq`, a theorem declared in [MathlibExt/Biology/Phylogenetics/CodonOmega.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/CodonOmega.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/codon-substitution-models-and-dn-ds/index.html#syn-rate-eq).

## Nonsynonymous rate is linear in ω

The nonsynonymous rate is linear in `ω`: `ρ_N(ω) = ω ρ_N(1)`.

Formalized by `MathlibExt.Biology.Phylogenetics.CodonModel.nonsynRate_eq`, a theorem declared in [MathlibExt/Biology/Phylogenetics/CodonOmega.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/CodonOmega.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/codon-substitution-models-and-dn-ds/index.html#nonsyn-rate-eq).

## Synonymous and nonsynonymous sites sum to three

There are three sites per codon: `S + N = 3` when `ρ_S(1) + ρ_N(1) ≠ 0`.

Formalized by `MathlibExt.Biology.Phylogenetics.CodonModel.synSites_add_nonsynSites`, a theorem declared in [MathlibExt/Biology/Phylogenetics/CodonOmega.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/CodonOmega.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/codon-substitution-models-and-dn-ds/index.html#syn-sites-add-nonsyn-sites).

## `dN / dS = ω`

**`dN / dS = ω`** in the Goldman–Yang model with sites counted under `ω = 1` (derived;
see the module docstring for the site definition), provided `ρ_S(1) > 0` and `ρ_N(1) > 0`.

Formalized by `MathlibExt.Biology.Phylogenetics.CodonModel.dN_div_dS`, a theorem declared in [MathlibExt/Biology/Phylogenetics/CodonOmega.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/CodonOmega.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/codon-substitution-models-and-dn-ds/index.html#d-n-div-d-s).

## Positivity of the synonymous rate

`ρ_S(1) > 0` if the frequencies are nonnegative, `κ > 0`, and some synonymous single
change joins two codons of positive frequency.

Formalized by `MathlibExt.Biology.Phylogenetics.CodonModel.synRate_pos_of_mem`, a theorem declared in [MathlibExt/Biology/Phylogenetics/CodonOmega.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/CodonOmega.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/codon-substitution-models-and-dn-ds/index.html#syn-rate-pos-of-mem).

## Positivity of the nonsynonymous rate

`ρ_N(1) > 0` if the frequencies are nonnegative, `κ > 0`, and some nonsynonymous single
change joins two codons of positive frequency.

Formalized by `MathlibExt.Biology.Phylogenetics.CodonModel.nonsynRate_pos_of_mem`, a theorem declared in [MathlibExt/Biology/Phylogenetics/CodonOmega.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/CodonOmega.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/codon-substitution-models-and-dn-ds/index.html#nonsyn-rate-pos-of-mem).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Codon substitution models and dN/dS](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/codon-substitution-models-and-dn-ds/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/phylogenetics/codon-substitution-models-and-dn-ds)
