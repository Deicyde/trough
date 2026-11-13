---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.HardyWeinberg.transmit, MathlibExt.Biology.PopulationGenetics.HardyWeinberg.gamete, MathlibExt.Biology.PopulationGenetics.HardyWeinberg.offspring, MathlibExt.Biology.PopulationGenetics.HardyWeinberg.transmit_apply, MathlibExt.Biology.PopulationGenetics.HardyWeinberg.gamete_apply, MathlibExt.Biology.PopulationGenetics.HardyWeinberg.offspring_apply, MathlibExt.Biology.PopulationGenetics.HardyWeinberg.gamete_offspring, MathlibExt.Biology.PopulationGenetics.HardyWeinberg.offspring_offspring
statement: formalized
proof: formalized
---

# Hardy–Weinberg law

14 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/hardy-weinberg-law/index.html).

## Mendel's law of segregation

Mendel's law of segregation: a parent with genotype `g` transmits its maternal allele `g.1`
or its paternal allele `g.2`, each with probability `1/2`.

Formalized by `MathlibExt.Biology.PopulationGenetics.HardyWeinberg.transmit`, a definition declared in [MathlibExt/Biology/PopulationGenetics/HardyWeinberg.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/HardyWeinberg.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/hardy-weinberg-law/index.html#transmit).

## Law of a random gamete

The law of a random gamete of a generation with genotype law `G`: pick a parent from `G`,
then one of its two alleles by `transmit`. Its mass at `a` is the frequency of allele `a`
(`gamete_apply`).

Formalized by `MathlibExt.Biology.PopulationGenetics.HardyWeinberg.gamete`, a definition declared in [MathlibExt/Biology/PopulationGenetics/HardyWeinberg.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/HardyWeinberg.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/hardy-weinberg-law/index.html#gamete).

## Offspring genotype law under random union of gametes

The offspring genotype law under random union of gametes: the maternal and paternal
alleles are independent gametes of the parental generation.

Formalized by `MathlibExt.Biology.PopulationGenetics.HardyWeinberg.offspring`, a definition declared in [MathlibExt/Biology/PopulationGenetics/HardyWeinberg.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/HardyWeinberg.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/hardy-weinberg-law/index.html#offspring).

## Allele transmission law of a parental genotype

`transmit g` puts mass `1/2` on each of the two alleles of `g` (mass `1` on `a` for a
homozygote `g = (a, a)`).

Formalized by `MathlibExt.Biology.PopulationGenetics.HardyWeinberg.transmit_apply`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/HardyWeinberg.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/HardyWeinberg.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/hardy-weinberg-law/index.html#transmit-apply).

## Gamete law equals the allele frequency

The gamete law is the allele frequency: `gamete G a = ½ ∑ b, G (a, b) + ½ ∑ b, G (b, a)`,
half the expected number of copies of `a` in a parental genotype.

Formalized by `MathlibExt.Biology.PopulationGenetics.HardyWeinberg.gamete_apply`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/HardyWeinberg.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/HardyWeinberg.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/hardy-weinberg-law/index.html#gamete-apply).

## Hardy–Weinberg proportions

**Hardy–Weinberg proportions** (Hardy 1908, Weinberg 1908): after one generation of random
mating the genotype law is the product `p ⊗ p` of the parental allele frequencies
`p = gamete G`.

Formalized by `MathlibExt.Biology.PopulationGenetics.HardyWeinberg.offspring_apply`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/HardyWeinberg.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/HardyWeinberg.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/hardy-weinberg-law/index.html#offspring-apply).

## Allele frequencies are conserved

**Allele frequencies are conserved** under random mating: the gamete law of the offspring
equals that of the parents.

Formalized by `MathlibExt.Biology.PopulationGenetics.HardyWeinberg.gamete_offspring`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/HardyWeinberg.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/HardyWeinberg.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/hardy-weinberg-law/index.html#gamete-offspring).

## Hardy–Weinberg equilibrium

The Hardy–Weinberg proportions reached after one generation
of random mating are a fixed point of random mating.

Formalized by `MathlibExt.Biology.PopulationGenetics.HardyWeinberg.offspring_offspring`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/HardyWeinberg.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/HardyWeinberg.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/hardy-weinberg-law/index.html#offspring-offspring).

## The two allele frequencies sum to one

The two allele frequencies sum to one: `p + q = 1`.

Formalized by `MathlibExt.Biology.PopulationGenetics.HardyWeinberg.freq_true_add_freq_false`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/HardyWeinberg.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/HardyWeinberg.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/hardy-weinberg-law/index.html#freq-true-add-freq-false).

## Hardy–Weinberg frequency $p^2$ of the AA homozygote

After one generation of random mating the homozygote `AA` has frequency `p²`.

Formalized by `MathlibExt.Biology.PopulationGenetics.HardyWeinberg.offspring_true_true`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/HardyWeinberg.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/HardyWeinberg.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/hardy-weinberg-law/index.html#offspring-true-true).

## Hardy–Weinberg frequency $q^2$ of the aa homozygote

After one generation of random mating the homozygote `aa` has frequency `q²`.

Formalized by `MathlibExt.Biology.PopulationGenetics.HardyWeinberg.offspring_false_false`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/HardyWeinberg.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/HardyWeinberg.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/hardy-weinberg-law/index.html#offspring-false-false).

## Hardy–Weinberg frequency $2pq$ of the heterozygote

After one generation of random mating the (unordered) heterozygote `Aa`, i.e. the two
ordered genotypes `(A, a)` and `(a, A)`, has frequency `2pq`.

Formalized by `MathlibExt.Biology.PopulationGenetics.HardyWeinberg.offspring_heterozygote`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/HardyWeinberg.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/HardyWeinberg.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/hardy-weinberg-law/index.html#offspring-heterozygote).

## Deviation from Hardy–Weinberg proportions

The deviation `D = P(AA) - p²` of a biallelic genotype law from Hardy–Weinberg
proportions, where `p` is the frequency of allele `A` (`true`).

Formalized by `MathlibExt.Biology.PopulationGenetics.HardyWeinberg.hwDeviation`, a definition declared in [MathlibExt/Biology/PopulationGenetics/HardyWeinberg.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/HardyWeinberg.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/hardy-weinberg-law/index.html#hw-deviation).

## Hardy–Weinberg proportions after one generation of random mating

The deviation from Hardy–Weinberg proportions vanishes after one generation of random
mating, whatever the parental genotype law.

Formalized by `MathlibExt.Biology.PopulationGenetics.HardyWeinberg.hwDeviation_offspring`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/HardyWeinberg.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/HardyWeinberg.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/hardy-weinberg-law/index.html#hw-deviation-offspring).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hardy–Weinberg law](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/hardy-weinberg-law/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/population-genetics/hardy-weinberg-law)
