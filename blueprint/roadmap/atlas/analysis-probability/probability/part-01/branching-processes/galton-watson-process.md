---
declaration: section
origin: cited
lean: MathlibExt.Probability.GaltonWatson.law, MathlibExt.Probability.GaltonWatson.mean, MathlibExt.Probability.GaltonWatson.extinctionProb, MathlibExt.Probability.GaltonWatson.iterate_pgf_mem_Icc, MathlibExt.Probability.GaltonWatson.monotone_iterate_pgf_zero, MathlibExt.Probability.GaltonWatson.isLeast_iSup_iterate_pgf_zero, MathlibExt.Probability.GaltonWatson.iSup_iterate_pgf_zero_eq_one_iff, MathlibExt.Probability.GaltonWatson.pgf_law
statement: formalized
proof: formalized
---

# Galton–Watson process

14 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/branching-processes/galton-watson-process/index.html).

## Generation-size law of a Galton–Watson process

The law of the generation size `Z_n` of the Galton–Watson process with offspring law `ν`
started from one individual: `Z_0 = 1` and, given `Z_n = z`, `Z_{n+1}` has law `ν^{∗z}`
(`Measure.convPow ν z`).

Formalized by `MathlibExt.Probability.GaltonWatson.law`, a definition declared in [MathlibExt/Probability/BranchingProcess/GaltonWatson.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BranchingProcess/GaltonWatson.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/branching-processes/galton-watson-process/index.html#law).

## Mean offspring number

The mean offspring number `m = E ξ = ∑ k ν{k} ∈ [0, ∞]`.

Formalized by `MathlibExt.Probability.GaltonWatson.mean`, a definition declared in [MathlibExt/Probability/BranchingProcess/GaltonWatson.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BranchingProcess/GaltonWatson.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/branching-processes/galton-watson-process/index.html#mean).

## Extinction probability of a Galton–Watson process

The extinction probability `q = sup_n P(Z_n = 0)`, the limit of the probabilities of
extinction by generation `n` (`tendsto_law_real_zero`). On a path space carrying the process the
events `{Z_n = 0}` increase with `n` (`0` is absorbing), so `q` is the probability of eventual
extinction; this file describes the process through its generation laws and does not construct
the path space.

Formalized by `MathlibExt.Probability.GaltonWatson.extinctionProb`, a definition declared in [MathlibExt/Probability/BranchingProcess/GaltonWatson.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BranchingProcess/GaltonWatson.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/branching-processes/galton-watson-process/index.html#extinction-prob).

## Iterates of the offspring generating function stay in (0, 1)

The iterates `f^[n]&#40;s)` of the offspring generating function stay in `[0, 1]` for
`s ∈ [0, 1]`.

Formalized by `MathlibExt.Probability.GaltonWatson.iterate_pgf_mem_Icc`, a theorem declared in [MathlibExt/Probability/BranchingProcess/GaltonWatson.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BranchingProcess/GaltonWatson.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/branching-processes/galton-watson-process/index.html#iterate-pgf-mem-icc).

## Iterates of the generating function at zero are nondecreasing

The iterates `f^[n]&#40;0)` of the offspring generating function are non-decreasing.

Formalized by `MathlibExt.Probability.GaltonWatson.monotone_iterate_pgf_zero`, a theorem declared in [MathlibExt/Probability/BranchingProcess/GaltonWatson.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BranchingProcess/GaltonWatson.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/branching-processes/galton-watson-process/index.html#monotone-iterate-pgf-zero).

## Limit of generating-function iterates is the least fixed point

`sup_n f^[n]&#40;0)` is the least fixed point of `f` in `[0, 1]`
(Athreya–Ney 1972, ch. I).

Formalized by `MathlibExt.Probability.GaltonWatson.isLeast_iSup_iterate_pgf_zero`, a theorem declared in [MathlibExt/Probability/BranchingProcess/GaltonWatson.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BranchingProcess/GaltonWatson.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/branching-processes/galton-watson-process/index.html#is-least-i-sup-iterate-pgf-zero).

## Least fixed point equals one iff mean offspring is at most one

The least fixed point is `1` iff the mean offspring number is at most `1`, provided the
offspring number is not almost surely `1` (Athreya–Ney 1972, ch. I).

Formalized by `MathlibExt.Probability.GaltonWatson.iSup_iterate_pgf_zero_eq_one_iff`, a theorem declared in [MathlibExt/Probability/BranchingProcess/GaltonWatson.lean, line 307](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BranchingProcess/GaltonWatson.lean#L307). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/branching-processes/galton-watson-process/index.html#i-sup-iterate-pgf-zero-eq-one-iff).

## Generating function of the n-th generation size

The generating function of `Z_n` is the `n`-th iterate of the offspring generating
function on `[0, 1]` (Athreya–Ney 1972, ch. I).

Formalized by `MathlibExt.Probability.GaltonWatson.pgf_law`, a theorem declared in [MathlibExt/Probability/BranchingProcess/GaltonWatson.lean, line 384](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BranchingProcess/GaltonWatson.lean#L384). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/branching-processes/galton-watson-process/index.html#pgf-law).

## Probability of extinction by generation n

`P(Z_n = 0) = f^[n]&#40;0)`.

Formalized by `MathlibExt.Probability.GaltonWatson.law_real_zero`, a theorem declared in [MathlibExt/Probability/BranchingProcess/GaltonWatson.lean, line 391](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BranchingProcess/GaltonWatson.lean#L391). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/branching-processes/galton-watson-process/index.html#law-real-zero).

## Mean generation size of a Galton–Watson process

The mean generation size is `E Z_n = m ^ n` (Athreya–Ney 1972, ch. I).

Formalized by `MathlibExt.Probability.GaltonWatson.lintegral_law`, a theorem declared in [MathlibExt/Probability/BranchingProcess/GaltonWatson.lean, line 410](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BranchingProcess/GaltonWatson.lean#L410). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/branching-processes/galton-watson-process/index.html#lintegral-law).

## Extinction by generation n is nondecreasing in n

`P(Z_n = 0)` is non-decreasing in `n`.

Formalized by `MathlibExt.Probability.GaltonWatson.monotone_law_real_zero`, a theorem declared in [MathlibExt/Probability/BranchingProcess/GaltonWatson.lean, line 423](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BranchingProcess/GaltonWatson.lean#L423). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/branching-processes/galton-watson-process/index.html#monotone-law-real-zero).

## Extinction by generation n converges to the extinction probability

`P(Z_n = 0)` converges to the extinction probability.

Formalized by `MathlibExt.Probability.GaltonWatson.tendsto_law_real_zero`, a theorem declared in [MathlibExt/Probability/BranchingProcess/GaltonWatson.lean, line 433](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BranchingProcess/GaltonWatson.lean#L433). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/branching-processes/galton-watson-process/index.html#tendsto-law-real-zero).

## Extinction probability is the least fixed point

The extinction probability is the least fixed point of the offspring generating function
in `[0, 1]` (Athreya–Ney 1972, ch. I).

Formalized by `MathlibExt.Probability.GaltonWatson.isLeast_extinctionProb`, a theorem declared in [MathlibExt/Probability/BranchingProcess/GaltonWatson.lean, line 441](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BranchingProcess/GaltonWatson.lean#L441). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/branching-processes/galton-watson-process/index.html#is-least-extinction-prob).

## Galton–Watson extinction criterion

Extinction is certain iff the mean offspring number is at most `1`, provided the offspring
number is not almost surely `1` (Athreya–Ney 1972, ch. I).

Formalized by `MathlibExt.Probability.GaltonWatson.extinctionProb_eq_one_iff`, a theorem declared in [MathlibExt/Probability/BranchingProcess/GaltonWatson.lean, line 448](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BranchingProcess/GaltonWatson.lean#L448). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/branching-processes/galton-watson-process/index.html#extinction-prob-eq-one-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Galton–Watson process](https://deicyde.github.io/atlas-lean/roadmap/Probability/branching-processes/galton-watson-process/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/branching-processes/galton-watson-process)
