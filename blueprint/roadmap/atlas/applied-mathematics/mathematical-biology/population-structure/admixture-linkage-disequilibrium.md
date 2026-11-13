---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.AdmixtureLD.alleleCount, MathlibExt.Biology.PopulationGenetics.AdmixtureLD.alleleCov, MathlibExt.Biology.PopulationGenetics.AdmixtureLD.genotypeCov, MathlibExt.Biology.PopulationGenetics.AdmixtureLD.alleleCov_eq_linkageDiseq, MathlibExt.Biology.PopulationGenetics.AdmixtureLD.genotypeCov_eq_two_mul, MathlibExt.Biology.PopulationGenetics.AdmixtureLD.bernFreq, MathlibExt.Biology.PopulationGenetics.AdmixtureLD.sourceMix, MathlibExt.Biology.PopulationGenetics.AdmixtureLD.sum_sourceMix
statement: formalized
proof: formalized
---

# Admixture linkage disequilibrium

25 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-linkage-disequilibrium/index.html).

## Haplotype and genotype covariances

## Allele count of a gamete at one locus

The `0/1` count of the `'1'` allele carried by a gamete at one locus.

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureLD.alleleCount`, a definition declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-linkage-disequilibrium/index.html#allele-count).

## Covariance of allele counts within a gamete

The covariance of the allele counts at the two loci of one gamete drawn from the gamete
frequencies `x`: `∑ g, x g a(g.1) a(g.2) - (∑ g, x g a(g.1)) (∑ g, x g a(g.2))`.

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureLD.alleleCov`, a definition declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-linkage-disequilibrium/index.html#allele-cov).

## Covariance of unphased diploid genotypes

The covariance of the unphased diploid genotypes `X = X₁ + X₂ ∈ {0, 1, 2}` at the first
locus and `Y = Y₁ + Y₂` at the second, for an individual made of two gametes `g`, `h` drawn
independently from `x` (random union of gametes). This is `z(x, y)` of Loh et al. (2013),
Eq. 1.

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureLD.genotypeCov`, a definition declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-linkage-disequilibrium/index.html#genotype-cov).

## Gamete allele covariance equals linkage disequilibrium

The covariance of the allele counts of one gamete is the linkage disequilibrium
`D = x_AB x_ab - x_Ab x_aB` (frequencies summing to `1`).

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureLD.alleleCov_eq_linkageDiseq`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-linkage-disequilibrium/index.html#allele-cov-eq-linkage-diseq).

## Diploid genotype covariance is twice the linkage disequilibrium

The diploid genotype covariance is twice the haplotype one, `z = 2 D`: the two
same-gamete terms each contribute `D` and the two cross-gamete terms vanish by independence
(Loh et al. 2013, Eqs. 2–3).

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureLD.genotypeCov_eq_two_mul`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-linkage-disequilibrium/index.html#genotype-cov-eq-two-mul).

## Bernoulli allele frequency

The frequency `p` of the `'1'` allele (`b = true`) or `1 - p` of the `'0'` allele.

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureLD.bernFreq`, a definition declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-linkage-disequilibrium/index.html#bern-freq).

## Gamete frequencies after an admixture pulse

Gamete frequencies right after the pulse: with probability `α` the gamete comes from `A`,
where the loci are in linkage equilibrium with `'1'` frequencies `pA` and `qA`, and otherwise
from `B` (frequencies `pB`, `qB`). The biological domain is `α, pA, qA, pB, qB ∈ [0, 1]`;
the identities below hold for all reals.

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureLD.sourceMix`, a definition declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-linkage-disequilibrium/index.html#source-mix).

## Pulse gamete frequencies sum to one

The pulse gamete frequencies sum to `1`.

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureLD.sum_sourceMix`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-linkage-disequilibrium/index.html#sum-source-mix).

## Admixture linkage disequilibrium right after the pulse

Admixture LD right after the pulse: `D₀ = α (1 - α) δ(x) δ(y)`, with
`δ(x) = pA - pB`, `δ(y) = qA - qB` (Chakraborty and Weiss 1988).

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureLD.linkageDiseq_sourceMix`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-linkage-disequilibrium/index.html#linkage-diseq-source-mix).

## Decay of admixture linkage disequilibrium over generations

Admixture LD after `n` generations of random mating with recombination fraction `r`:
`D_n = (1 - r)^n α (1 - α) δ(x) δ(y)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureLD.linkageDiseq_admixed`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-linkage-disequilibrium/index.html#linkage-diseq-admixed).

## Recombination preserves total gamete frequency

Recombination keeps gamete frequencies summing to `1` over any number of generations.

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureLD.sum_iterate_recombine`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-linkage-disequilibrium/index.html#sum-iterate-recombine).

## Diploid genotype covariance in an admixed population

The diploid genotype covariance in the admixed population `n` generations after the
pulse: `z(x, y) = 2 α (1 - α) (1 - r)^n δ(x) δ(y)` (Loh et al. 2013, Eq. 3, with the exact
discrete-generation factor `(1 - r)^n` in place of `e^{-n d}`).

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureLD.genotypeCov_admixed`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-linkage-disequilibrium/index.html#genotype-cov-admixed).

## Joint law of local ancestry after an admixture pulse

Joint law of the local-ancestry labels at the two loci right after the pulse
(`true` = descends from `A`): every gamete is entirely from `A` (probability `α`) or entirely
from `B`. This is `sourceMix` with perfectly differentiated markers (`pA = qA = 1`,
`pB = qB = 0`).

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureLD.ancestryPulse`, a definition declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-linkage-disequilibrium/index.html#ancestry-pulse).

## Covariance of local-ancestry indicators after pulse admixture

Pulse admixture: after `n` generations of random mating the local-ancestry indicators at
two loci with recombination fraction `r` have covariance `Cov(I_x, I_y) = α (1 - α) (1 - r)^n`
(for every real `α`, `r`; the biological domain is `0 ≤ α ≤ 1`, `0 ≤ r ≤ 1/2`). The
ancestry labels obey the two-locus random-mating recursion of `Linkage.recombine`
(Chakraborty and Weiss 1988).

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureLD.alleleCov_ancestryPulse`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-linkage-disequilibrium/index.html#allele-cov-ancestry-pulse).

## Haldane's map function: $1 - r = e^{-d}\cosh d$

With Haldane's map function, `1 - r = e^{-d} cosh d` for map length `d`.

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureLD.one_sub_haldane`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-linkage-disequilibrium/index.html#one-sub-haldane).

## Exact decay factor under Haldane's map function

Exact decay in Morgans: `(1 - r)^n = e^{-n d} (cosh d)^n` when `r = haldane d`.

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureLD.pow_one_sub_haldane`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-linkage-disequilibrium/index.html#pow-one-sub-haldane).

## Continuous decay is a lower bound for the exact factor under Haldane's map

The continuous decay `e^{-n d}` used by Chakraborty and Weiss (1988) and Loh et al.
(2013) is a lower bound for the exact factor `(1 - r)^n` under Haldane's map (all real
`d`; the biological domain is `0 ≤ d`).

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureLD.exp_neg_mul_le_pow_one_sub_haldane`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-linkage-disequilibrium/index.html#exp-neg-mul-le-pow-one-sub-haldane).

## Local-ancestry covariance in Morgans

Local-ancestry covariance in Morgans:
`Cov(I_x, I_y) = α (1 - α) e^{-n d} (cosh d)^n` for loci `d` Morgans apart.

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureLD.alleleCov_ancestryPulse_haldane`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-linkage-disequilibrium/index.html#allele-cov-ancestry-pulse-haldane).

## Expected ALDER weighted linkage disequilibrium

The expected ALDER two-site weighted-LD statistic `𝔼[z(x, y) w(x) w(y)]` (Loh et al.
2013, Appendix A, without distance binning). The loci `x` and `y` drift independently: `ω.1`
and `ω.2` are independent draws from `μ`, and `p X ω` is the frequency of the `'1'` allele in
population `X`. The covariance `z(x, y)` is that of the population formed `n` generations ago
as an `α : 1 - α` mixture of `A` and `B` (`genotypeCov_admixed`), and the weights are the
frequency differences `w = p R - p S` between two reference populations `R` and `S`.

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureLD.weightedLD`, a definition declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-linkage-disequilibrium/index.html#weighted-ld).

## Weighted linkage disequilibrium in terms of the f4 statistic

The expected weighted LD factors as `2 α (1 - α) (1 - r)^n (f4 A B R S)^2`: by
independence of the loci, `𝔼[δ(x) w(x) δ(y) w(y)] = 𝔼[δ w]^2` and `𝔼[δ w] = f4 A B R S`.
The identity holds with the Bochner-integral conventions as stated; it is meaningful when the
frequencies are square integrable, as in every `DriftModel`.

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureLD.weightedLD_eq`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean, line 257](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean#L257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-linkage-disequilibrium/index.html#weighted-ld-eq).

## Weighted LD amplitude with the true source populations

Weights from the true mixing populations (`R = A`, `S = B`): the amplitude is
`2 α β F2(A, B)^2` (Loh et al. 2013, Eq. 4).

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureLD.DriftModel.weightedLD_sources`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-linkage-disequilibrium/index.html#weighted-ld-sources).

## f4 equals f2 for references branching off the path

Branch points on the `A–B` path. Suppose that `A = A″ + uA`, `A′ = A″ + uA'`,
`B = B″ + uB`, `B′ = B″ + uB'` at the level of lineage weights, where `w A″ - w B″` is
disjoint in support from each of `uA`, `uB`, `uA'`, `uB'`, and each of `uA`, `uB` is disjoint
from each of `uA'`, `uB'`. On a tree this says that the paths `A″–B″`, `A″–A`, `B″–B`,
`A″–A′`, `B″–B′` share no edge (the vectors may be signed, so every rooting is allowed).
Then `f4 A B A′ B′ = f2 A″ B″`.

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureLD.DriftModel.f4_eq_f2_of_branch`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean, line 288](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean#L288). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-linkage-disequilibrium/index.html#f4-eq-f2-of-branch).

## Weighted LD amplitude with two diverged references

Two diverged references `A′`, `B′` branching off the `A–B` path at `A″` and `B″`: the
amplitude is `2 α β F2(A″, B″)^2` (Loh et al. 2013, Eq. 6).

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureLD.DriftModel.weightedLD_branch`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean, line 310](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean#L310). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-linkage-disequilibrium/index.html#weighted-ld-branch).

## Weighted LD amplitude with the admixed population as reference

One reference `A` and the admixed population `C` itself, with no drift in `C` after the
pulse (`w C = α w A + (1 - α) w B`): the weights are `p A - p C = β δ` and the amplitude is
`2 α β^3 F2(A, B)^2` (Loh et al. 2013, Eq. 7).

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureLD.DriftModel.weightedLD_admixedRef`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean, line 323](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean#L323). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-linkage-disequilibrium/index.html#weighted-ld-admixed-ref).

## Weighted LD amplitude with one diverged reference

One diverged reference `R′` branching off the `A–B` path at `R″` (so `A = R″ + uA`,
`B = R″ + uB`, `R′ = R″ + uR` with pairwise disjoint supports) and the admixed population `C`
with no post-pulse drift: the weights `p R′ - p C` give the amplitude
`2 α β (α F2(A, R″) - β F2(B, R″))^2` (Loh et al. 2013, Eq. 8).

Formalized by `MathlibExt.Biology.PopulationGenetics.AdmixtureLD.DriftModel.weightedLD_oneRef`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean, line 340](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/AdmixtureLD.lean#L340). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-linkage-disequilibrium/index.html#weighted-ld-one-ref).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Admixture linkage disequilibrium](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-linkage-disequilibrium/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/population-structure/admixture-linkage-disequilibrium)
