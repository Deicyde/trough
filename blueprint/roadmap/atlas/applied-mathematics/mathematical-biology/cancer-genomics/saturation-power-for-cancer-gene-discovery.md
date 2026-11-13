---
declaration: section
origin: cited
lean: MathlibExt.Biology.CancerGenomics.SaturationPower.saturationPower, MathlibExt.Biology.CancerGenomics.SaturationPower.lawrenceP0, MathlibExt.Biology.CancerGenomics.SaturationPower.lawrenceP1, MathlibExt.Biology.CancerGenomics.SaturationPower.tendsto_saturationPower, MathlibExt.Biology.CancerGenomics.SaturationPower.eventually_le_saturationPower, MathlibExt.Biology.CancerGenomics.SaturationPower.lawrenceP0_mem, MathlibExt.Biology.CancerGenomics.SaturationPower.lawrenceP0_lt_lawrenceP1
statement: formalized
proof: formalized
---

# Saturation power for cancer gene discovery

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/saturation-power-for-cancer-gene-discovery/index.html).

## Saturation power of the binomial gene discovery test

Power of the one-sided binomial test of Lawrence et al. (2014): the probability, when each
of `N` patients is mutated with probability `p₁`, of observing a count `x` whose background
p-value `ℙ_{p₀}(X ≥ x)` is at most `γ`.

Formalized by `MathlibExt.Biology.CancerGenomics.SaturationPower.saturationPower`, a definition declared in [MathlibExt/Biology/CancerGenomics/SaturationPower.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/CancerGenomics/SaturationPower.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/saturation-power-for-cancer-gene-discovery/index.html#saturation-power).

## Background mutation probability per patient

Background probability `p₀ = 1 - (1 - μ f_g)^(3L/4)` that a patient carries at least one
non-silent background mutation in a gene of `L` coding bases (Lawrence et al. 2014).

Formalized by `MathlibExt.Biology.CancerGenomics.SaturationPower.lawrenceP0`, a definition declared in [MathlibExt/Biology/CancerGenomics/SaturationPower.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/CancerGenomics/SaturationPower.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/saturation-power-for-cancer-gene-discovery/index.html#lawrence-p0).

## Signal mutation probability per patient

Signal probability `p₁ = p₀ + r (1 - m)` for a gene mutated in a fraction `r` of patients
above background, with miss rate `m` (Lawrence et al. 2014).

Formalized by `MathlibExt.Biology.CancerGenomics.SaturationPower.lawrenceP1`, a definition declared in [MathlibExt/Biology/CancerGenomics/SaturationPower.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/CancerGenomics/SaturationPower.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/saturation-power-for-cancer-gene-discovery/index.html#lawrence-p1).

## Power tends to one

For `0 ≤ p₀ < p₁ ≤ 1` and any level `γ > 0`, the power of the
binomial test tends to `1` as the number of patients grows.

Formalized by `MathlibExt.Biology.CancerGenomics.SaturationPower.tendsto_saturationPower`, a theorem declared in [MathlibExt/Biology/CancerGenomics/SaturationPower.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/CancerGenomics/SaturationPower.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/saturation-power-for-cancer-gene-discovery/index.html#tendsto-saturation-power).

## `N_β` exists

For every target power `β < 1` there is a cohort size beyond which the
power is at least `β` (Lawrence et al. 2014 take `β = 0.9`).

Formalized by `MathlibExt.Biology.CancerGenomics.SaturationPower.eventually_le_saturationPower`, a theorem declared in [MathlibExt/Biology/CancerGenomics/SaturationPower.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/CancerGenomics/SaturationPower.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/saturation-power-for-cancer-gene-discovery/index.html#eventually-le-saturation-power).

## Background mutation probability lies in (0, 1)

The background probability is a probability below one: `0 ≤ p₀ < 1` for
`0 ≤ μ f_g < 1` and `L ≥ 0`.

Formalized by `MathlibExt.Biology.CancerGenomics.SaturationPower.lawrenceP0_mem`, a theorem declared in [MathlibExt/Biology/CancerGenomics/SaturationPower.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/CancerGenomics/SaturationPower.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/saturation-power-for-cancer-gene-discovery/index.html#lawrence-p0-mem).

## Driver genes raise the per-patient mutation probability

A driver mutated above background raises the per-patient probability:
`p₀ < p₀ + r (1 - m)` for `r > 0` and `m < 1`.

Formalized by `MathlibExt.Biology.CancerGenomics.SaturationPower.lawrenceP0_lt_lawrenceP1`, a theorem declared in [MathlibExt/Biology/CancerGenomics/SaturationPower.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/CancerGenomics/SaturationPower.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/saturation-power-for-cancer-gene-discovery/index.html#lawrence-p0-lt-lawrence-p1).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Saturation power for cancer gene discovery](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/saturation-power-for-cancer-gene-discovery/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/cancer-genomics/saturation-power-for-cancer-gene-discovery)
