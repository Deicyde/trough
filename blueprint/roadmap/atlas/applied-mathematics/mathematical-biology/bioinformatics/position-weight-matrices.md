---
declaration: section
origin: cited
lean: Cslib.Bioinformatics.Motifs.PWM.score, Cslib.Bioinformatics.Motifs.PWM.siteLik, Cslib.Bioinformatics.Motifs.PWM.bgLik, Cslib.Bioinformatics.Motifs.PWM.logOdds, Cslib.Bioinformatics.Motifs.PWM.score_logOdds, Cslib.Bioinformatics.Motifs.PWM.sum_siteLik, Cslib.Bioinformatics.Motifs.PWM.sum_bgLik, Cslib.Bioinformatics.Motifs.PWM.sum_mul_siteLik_le_of_sum_mul_bgLik_le
statement: formalized
proof: formalized
---

# Position weight matrices

68 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html).

## Score of a site under a position weight matrix

The score `∑ᵢ W i (s i)` of a site `s` of width `w` under a position weight matrix `W`.

Formalized by `Cslib.Bioinformatics.Motifs.PWM.score`, a definition declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#score).

## Site likelihood under a column-independent model

The likelihood `∏ᵢ p i (s i)` of a site under the product (column-independent) site model
`p`.

Formalized by `Cslib.Bioinformatics.Motifs.PWM.siteLik`, a definition declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#site-lik).

## Background likelihood of a sequence

The likelihood `∏ₖ q (x k)` of a sequence of length `m` under the background of independent
letters with law `q`.

Formalized by `Cslib.Bioinformatics.Motifs.PWM.bgLik`, a definition declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#bg-lik).

## Log-odds matrix of a site model

The log-odds matrix `log (p i b / q b)` of a site model against a background (natural
logarithm).

Formalized by `Cslib.Bioinformatics.Motifs.PWM.logOdds`, a definition declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#log-odds).

## The log-odds score is a log-likelihood ratio

**The log-odds score is a log-likelihood ratio** (Staden 1989; Stormo 2000): for positive
site model and background, `score (logOdds p q) s = log (siteLik p s / bgLik q s)`.

Formalized by `Cslib.Bioinformatics.Motifs.PWM.score_logOdds`, a theorem declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#score-log-odds).

## Product site likelihoods form a distribution

A product of column distributions is a distribution on sites.

Formalized by `Cslib.Bioinformatics.Motifs.PWM.sum_siteLik`, a theorem declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#sum-site-lik).

## Background likelihoods form a distribution

The background law of independent letters is a distribution on sequences.

Formalized by `Cslib.Bioinformatics.Motifs.PWM.sum_bgLik`, a theorem declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#sum-bg-lik).

## Thresholding the log-odds score is most powerful

**Thresholding the log-odds score is most powerful** (Neyman–Pearson): a test `φ` of the
background (null) against the site model whose background size is at most that of the
threshold test `score > t` has at most its power.

Formalized by `Cslib.Bioinformatics.Motifs.PWM.sum_mul_siteLik_le_of_sum_mul_bgLik_le`, a theorem declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#sum-mul-site-lik-le-of-sum-mul-bg-lik-le).

## Information content of a position weight matrix column

The information content `∑_b p b log₂ (p b / q b)` (in bits) of a PWM column `p` against
the background `q` (Schneider et al. 1986). Letters with `p b = 0` contribute `0`.

Formalized by `Cslib.Bioinformatics.Motifs.PWM.infoContent`, a definition declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#info-content).

## Information content is a Kullback–Leibler divergence

For laws `P ≪ Q`, the information
content of `P` against `Q` is `KL(P ‖ Q) / log 2`, Mathlib's `klDiv` in bits.

Formalized by `Cslib.Bioinformatics.Motifs.PWM.infoContent_eq_klDiv`, a theorem declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#info-content-eq-kl-div).

## Information content is nonnegative

**Information content is nonnegative** (Gibbs' inequality) for a column distribution and a
positive background distribution.

Formalized by `Cslib.Bioinformatics.Motifs.PWM.infoContent_nonneg`, a theorem declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#info-content-nonneg).

## Information content against the uniform background

**Information content against the uniform background** (Schneider et al. 1986):
`log₂ |α| - H(p)`, the maximal entropy minus the column entropy.

Formalized by `Cslib.Bioinformatics.Motifs.PWM.infoContent_uniform`, a theorem declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#info-content-uniform).

## Information content is at most the log of the alphabet size

Against the uniform background, a column carries at most `log₂ |α|` bits.

Formalized by `Cslib.Bioinformatics.Motifs.PWM.infoContent_uniform_le`, a theorem declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#info-content-uniform-le).

## A DNA column carries at most two bits

For a four-letter alphabet (DNA) and the uniform background, a column carries between `0`
and `2` bits.

Formalized by `Cslib.Bioinformatics.Motifs.PWM.infoContent_uniform_le_two`, a theorem declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#info-content-uniform-le-two).

## The expected log-odds score is the total information content

Under the site model,
`E[score] = log 2 · ∑ᵢ IC(pᵢ ‖ q)`. This is an identity for every `q` (both sides use the same
logarithms); it is an expected log-likelihood ratio for a positive background.

Formalized by `Cslib.Bioinformatics.Motifs.PWM.sum_siteLik_mul_score_logOdds`, a theorem declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#sum-site-lik-mul-score-log-odds).

## One column step of the score-distribution recursion

One column of the score-distribution recursion: from the distribution `d` of the score of
the first columns, the distribution after adding a column `c` with background `q`,
`∑_b q b · (d shifted by c b)`.

Formalized by `Cslib.Bioinformatics.Motifs.PWM.scoreStep`, a definition declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 287](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L287). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#score-step).

## Background score distribution of an integer matrix

The background distribution of the score of an integer matrix `M`, computed column by column
from the point mass at `0` (Staden 1989; Touzet and Varré 2007).

Formalized by `Cslib.Bioinformatics.Motifs.PWM.scoreDist`, a definition declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 292](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L292). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#score-dist).

## The column recursion computes the exact score distribution

`scoreDist q M t` is
`∑_{s : score M s = t} ∏ᵢ q (s i)`, for every `q`. When `q` is a distribution this is the
background probability of the score `t` (the weights sum to `1` by `sum_bgLik`).

Formalized by `Cslib.Bioinformatics.Motifs.PWM.scoreDist_apply`, a theorem declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 321](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L321). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#score-dist-apply).

## Exact p-value of a score threshold

The exact p-value of the score threshold `t`, summed over the computed distribution.

Formalized by `Cslib.Bioinformatics.Motifs.PWM.pValue`, a definition declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 331](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#p-value).

## Exact p-values

`pValue q M t = ∑_{s : score M s ≥ t} ∏ᵢ q (s i)`, the background
probability `P_q(score M ≥ t)` when `q` is a distribution.

Formalized by `Cslib.Bioinformatics.Motifs.PWM.pValue_eq`, a theorem declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 336](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L336). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#p-value-eq).

## Scaling and rounding error

Rounding `c · W` to integers changes the rescaled score of
every site by at most `w / (2c)`.

Formalized by `Cslib.Bioinformatics.Motifs.PWM.abs_score_sub_score_round_le`, a theorem declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 366](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L366). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#abs-score-sub-score-round-le).

## Column partition function of an energy matrix

The column partition function `Z = ∑_b q b e^{-λ ε b}` of energies `ε` at inverse
temperature `λ`.

Formalized by `Cslib.Bioinformatics.Motifs.PWM.partitionFn`, a definition declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 388](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L388). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#partition-fn).

## Boltzmann position weight matrix

The Boltzmann PWM `q b e^{-λ ε i b} / Zᵢ` of an energy matrix `ε`.

Formalized by `Cslib.Bioinformatics.Motifs.PWM.boltzmannPWM`, a definition declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 391](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L391). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#boltzmann-pwm).

## Law of energy-selected background sites

The law of background sites selected with weight `e^{-λ E(s)}` for the additive energy
`E s = score ε s = ∑ᵢ ε i (s i)`: `q(s) e^{-λ E(s)} / ∑_{s'} q(s') e^{-λ E(s')}`.

Formalized by `Cslib.Bioinformatics.Motifs.PWM.selectedLaw`, a definition declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 396](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L396). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#selected-law).

## Positivity of the column partition function

The partition function of a positive background is positive.

Formalized by `Cslib.Bioinformatics.Motifs.PWM.partitionFn_pos`, a theorem declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 400](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L400). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#partition-fn-pos).

## Columns of the Boltzmann matrix are distributions

Each column of the Boltzmann PWM is a distribution.

Formalized by `Cslib.Bioinformatics.Motifs.PWM.isDist_boltzmannPWM`, a theorem declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 405](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L405). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#is-dist-boltzmann-pwm).

## Berg–von Hippel

Boltzmann selection of background sites with an additive energy yields
the product site model with columns `boltzmannPWM`. This is an identity for every `q`
(both sides vanish when some `Zᵢ = 0`); it is a statement about laws for positive `q`.

Formalized by `Cslib.Bioinformatics.Motifs.PWM.selectedLaw_eq_siteLik`, a theorem declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 416](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L416). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#selected-law-eq-site-lik).

## Log-odds are affine in the energies

`log (p i b / q b) = -λ ε i b - log Zᵢ` for the
Boltzmann PWM.

Formalized by `Cslib.Bioinformatics.Motifs.PWM.logOdds_boltzmannPWM`, a theorem declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 431](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L431). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#log-odds-boltzmann-pwm).

## Log-odds score of a selected site is its scaled energy up to a constant

The log-odds score of a selected site is `-λ E(s)` up to the constant `∑ᵢ log Zᵢ`.

Formalized by `Cslib.Bioinformatics.Motifs.PWM.score_logOdds_boltzmannPWM`, a theorem declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 441](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L441). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#score-log-odds-boltzmann-pwm).

## Sequence position of a motif column

The position `j + i` of motif column `i` for a motif starting at `j`, in a sequence of
length `n + w` (so `n + 1` possible starts).

Formalized by `Cslib.Bioinformatics.Motifs.PWM.sitePos`, a definition declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 456](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L456). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#site-pos).

## Window of a sequence at a given start

The window of width `w` of `x` starting at `j`.

Formalized by `Cslib.Bioinformatics.Motifs.PWM.window`, a definition declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 459](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L459). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#window).

## Likelihood ratio of a motif window

The likelihood ratio of the window at `j` under the site model `θ` against the background
`q`, and `1` when there is no motif occurrence.

Formalized by `Cslib.Bioinformatics.Motifs.PWM.windowRatio`, a definition declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 463](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L463). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#window-ratio).

## Joint likelihood of a sequence and a motif occurrence

The joint likelihood of a sequence `x` and a latent occurrence `z` with prior `prior z` and
start `start z` (`none`: no occurrence): background letters outside the window, site-model letters
inside. One occurrence per sequence (OOPS) is `Z = Fin (n + 1)`, `start = some`, `prior` uniform;
zero or one (ZOOPS) is `Z = Option (Fin (n + 1))`, `start = id`, `prior none = 1 - γ` and
`prior (some j) = γ / (n + 1)` for a fixed `γ`. The background `q` is a fixed parameter.

Formalized by `Cslib.Bioinformatics.Motifs.PWM.motifJoint`, a definition declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 473](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L473). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#motif-joint).

## The joint is the window model

For a positive background and an occurrence at `j`, the
joint is the prior times the product of `θ (k - j)` inside the window and `q` outside.

Formalized by `Cslib.Bioinformatics.Motifs.PWM.motifJoint_of_start_eq_some`, a theorem declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 480](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L480). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#motif-joint-of-start-eq-some).

## Joint likelihood with no motif occurrence

With no occurrence, the joint is the prior times the background likelihood.

Formalized by `Cslib.Bioinformatics.Motifs.PWM.motifJoint_of_start_eq_none`, a theorem declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 520](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L520). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#motif-joint-of-start-eq-none).

## Positive position weight matrices

PWMs with positive entries and columns summing to `1`: the EM parameter space.

Formalized by `Cslib.Bioinformatics.Motifs.PWM.PosPWM`, an abbreviation declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 526](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L526). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#pos-pwm).

## Motif model as an EM model

The motif model as an EM model on `PosPWM`.

Formalized by `Cslib.Bioinformatics.Motifs.PWM.motifModel`, a definition declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 530](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L530). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#motif-model).

## Positivity of the motif model

The motif model is positive for a positive background and a positive prior.

Formalized by `Cslib.Bioinformatics.Motifs.PWM.motifModel_pos`, a theorem declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 536](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L536). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#motif-model-pos).

## The E-step in closed form

The posterior of the occurrence `z` is proportional to its
prior times the likelihood ratio of its window (Lawrence and Reilly 1990; Bailey and Elkan
1995).

Formalized by `Cslib.Bioinformatics.Motifs.PWM.posterior_motifModel`, a theorem declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 551](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L551). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#posterior-motif-model).

## Expected letter counts in motif columns

The expected count of letter `b` in motif column `i` under the posteriors at `θ`:
`∑ₘ ∑_z P(z | xₘ, θ) [start z = some j ∧ xₘ (j + i) = b]`.

Formalized by `Cslib.Bioinformatics.Motifs.PWM.expectedCounts`, a definition declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 567](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L567). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#expected-counts).

## Coverage condition for motif columns

Every letter can occur in every motif column: for each column `i` and letter `b` some
sequence has `b` at offset `i` of some possible occurrence. This keeps the M-step positive.

Formalized by `Cslib.Bioinformatics.Motifs.PWM.Covers`, a definition declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 576](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L576). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#covers).

## Positivity of expected motif counts

Under `Covers`, every expected count is positive.

Formalized by `Cslib.Bioinformatics.Motifs.PWM.expectedCounts_pos`, a theorem declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 580](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L580). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#expected-counts-pos).

## M-step for position weight matrices

The M-step: normalized expected letter counts, `θ' i b = c i b / ∑_{b'} c i b'`.

Formalized by `Cslib.Bioinformatics.Motifs.PWM.mStep`, a definition declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 603](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L603). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#m-step).

## The M-step maximizes the EM objective

**The M-step maximizes the EM objective** over PWMs with positive entries and normalized
columns: for every `θ'`, `Q(θ' | θ) ≤ Q(mStep θ | θ)` (Gibbs' inequality per column).

Formalized by `Cslib.Bioinformatics.Motifs.PWM.emQ_le_emQ_mStep`, a theorem declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 682](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L682). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#em-q-le-em-q-m-step).

## The motif likelihood is nondecreasing along the EM iterates

**The motif likelihood is nondecreasing along the EM iterates.**

Formalized by `Cslib.Bioinformatics.Motifs.PWM.logLik_iterate_mStep_monotone`, a theorem declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 695](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L695). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#log-lik-iterate-m-step-monotone).

## Moment generating function of a pair score

The moment generating function `∑ₐ ∑_b pₐ p_b e^{λ s_{ab}}` of a pair score under independent
letters with law `p`.

Formalized by `Cslib.Bioinformatics.Motifs.PWM.pairMGF`, a definition declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 708](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L708). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#pair-mgf).

## Karlin–Altschul `λ`

**Karlin–Altschul `λ`** (Karlin and Altschul 1990): if the expected score under a positive
background distribution is negative and some score is positive, there is a unique `λ > 0` with
`∑ pₐ p_b e^{λ s_{ab}} = 1`.

Formalized by `Cslib.Bioinformatics.Motifs.PWM.existsUnique_pairMGF_eq_one`, a theorem declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 764](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L764). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#exists-unique-pair-mgf-eq-one).

## Implicit target frequencies of a score matrix

The implicit target frequencies `q_{ab} = pₐ p_b e^{λ s_{ab}}` of a score matrix.

Formalized by `Cslib.Bioinformatics.Motifs.PWM.targetFreq`, a definition declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 820](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L820). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#target-freq).

## Target frequencies form a distribution on pairs

At a root of `pairMGF p s λ = 1` the target frequencies form a distribution on pairs.

Formalized by `Cslib.Bioinformatics.Motifs.PWM.isDist_targetFreq`, a theorem declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 824](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L824). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#is-dist-target-freq).

## Every such score matrix is a log-odds matrix

**Every such score matrix is a log-odds matrix** (Karlin and Altschul 1990):
`s_{ab} = log (q_{ab} / (pₐ p_b)) / λ` for every `λ > 0`; at the Karlin–Altschul root the
`q_{ab}` form a distribution (`isDist_targetFreq`), the implicit target frequencies.

Formalized by `Cslib.Bioinformatics.Motifs.PWM.score_eq_log_targetFreq`, a theorem declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 834](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L834). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#score-eq-log-target-freq).

## The relative entropy of the target frequencies

**The relative entropy of the target frequencies** (Altschul 1991):
`λ ∑ q_{ab} s_{ab} = ∑ q_{ab} log (q_{ab} / (pₐ p_b))`, which is nonnegative.

Formalized by `Cslib.Bioinformatics.Motifs.PWM.relEntropy_eq_and_nonneg`, a theorem declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 842](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L842). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#rel-entropy-eq-and-nonneg).

## The target score is positive

At the Karlin–Altschul root `λ > 0`, the expected score
`∑ q_{ab} s_{ab}` under the target frequencies is positive.

Formalized by `Cslib.Bioinformatics.Motifs.PWM.sum_targetFreq_mul_pos`, a theorem declared in [CSLibExt/Bioinformatics/Motifs/PWM.lean, line 877](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Motifs/PWM.lean#L877). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#sum-target-freq-mul-pos).

## One-hot encoding of a letter

The one-hot encoding of a letter: `oneHot a b = 1` if `b = a` and `0` otherwise.

Formalized by `Cslib.Bioinformatics.Regulatory.ConvolutionPWM.oneHot`, a definition declared in [CSLibExt/Bioinformatics/Regulatory/ConvolutionPWM.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Regulatory/ConvolutionPWM.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#one-hot).

## Convolution filter response at a window

The response of a convolution (cross-correlation) filter `W` of width `w` on the one-hot
encoded sequence `x` at the window starting at `i`:
`∑ k, ∑ b, W k b * oneHot (x (i + k)) b`.

Formalized by `Cslib.Bioinformatics.Regulatory.ConvolutionPWM.conv`, a definition declared in [CSLibExt/Bioinformatics/Regulatory/ConvolutionPWM.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Regulatory/ConvolutionPWM.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#conv).

## Window of a sequence starting at a position

The window of length `w` of `x` starting at `i`.

Formalized by `Cslib.Bioinformatics.Regulatory.ConvolutionPWM.window`, a definition declared in [CSLibExt/Bioinformatics/Regulatory/ConvolutionPWM.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Regulatory/ConvolutionPWM.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#window-2).

## The convolution response is the PWM score of the window

**The convolution response is the PWM score of the window.**

Formalized by `Cslib.Bioinformatics.Regulatory.ConvolutionPWM.conv_eq_pwmScore`, a theorem declared in [CSLibExt/Bioinformatics/Regulatory/ConvolutionPWM.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Regulatory/ConvolutionPWM.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#conv-eq-pwm-score).

## Global max pooling

**Global max pooling** over the `m + 1` windows of a sequence of length `m + w`.

Formalized by `Cslib.Bioinformatics.Regulatory.ConvolutionPWM.maxPool`, a definition declared in [CSLibExt/Bioinformatics/Regulatory/ConvolutionPWM.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Regulatory/ConvolutionPWM.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#max-pool).

## Every window's PWM score is at most the max-pooled output

Every window's PWM score is at most the max-pooled output.

Formalized by `Cslib.Bioinformatics.Regulatory.ConvolutionPWM.le_maxPool`, a theorem declared in [CSLibExt/Bioinformatics/Regulatory/ConvolutionPWM.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Regulatory/ConvolutionPWM.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#le-max-pool).

## Max pooling returns the best PWM hit

Some window attains the max-pooled output.

Formalized by `Cslib.Bioinformatics.Regulatory.ConvolutionPWM.exists_eq_maxPool`, a theorem declared in [CSLibExt/Bioinformatics/Regulatory/ConvolutionPWM.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Regulatory/ConvolutionPWM.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#exists-eq-max-pool).

## Bias and ReLU commute with max pooling

Pooling `max (conv + β) 0` over the windows
gives `max (maxPool + β) 0`.

Formalized by `Cslib.Bioinformatics.Regulatory.ConvolutionPWM.maxPool_relu`, a theorem declared in [CSLibExt/Bioinformatics/Regulatory/ConvolutionPWM.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Regulatory/ConvolutionPWM.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#max-pool-relu).

## Translation equivariance

Dropping the first letter shifts the responses by one
window.

Formalized by `Cslib.Bioinformatics.Regulatory.ConvolutionPWM.conv_shift`, a theorem declared in [CSLibExt/Bioinformatics/Regulatory/ConvolutionPWM.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Regulatory/ConvolutionPWM.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#conv-shift).

## Reverse complement of a sequence prefix

The reverse complement of the length-`L` prefix of `x`: position `j < L` holds the complement
of `x (L - 1 - j)`.

Formalized by `Cslib.Bioinformatics.Regulatory.ConvolutionPWM.rcSeq`, a definition declared in [CSLibExt/Bioinformatics/Regulatory/ConvolutionPWM.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Regulatory/ConvolutionPWM.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#rc-seq).

## Reverse-complement filter

The reverse-complement filter: `rcFilter W k b = W (Fin.rev k) (comp b)`.

Formalized by `Cslib.Bioinformatics.Regulatory.ConvolutionPWM.rcFilter`, a definition declared in [CSLibExt/Bioinformatics/Regulatory/ConvolutionPWM.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Regulatory/ConvolutionPWM.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#rc-filter).

## The reverse-complement filter scans the other strand

On a sequence of length `m + w`,
its response at window `i ≤ m` is the response of `W` on the reverse complement at window
`m - i`.

Formalized by `Cslib.Bioinformatics.Regulatory.ConvolutionPWM.conv_rcFilter`, a theorem declared in [CSLibExt/Bioinformatics/Regulatory/ConvolutionPWM.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Regulatory/ConvolutionPWM.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#conv-rc-filter).

## Max pooling the reverse-complement filter equals max pooling `W` on the reverse complement

**Max pooling the reverse-complement filter equals max pooling `W` on the reverse
complement.**

Formalized by `Cslib.Bioinformatics.Regulatory.ConvolutionPWM.maxPool_rcFilter`, a theorem declared in [CSLibExt/Bioinformatics/Regulatory/ConvolutionPWM.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Regulatory/ConvolutionPWM.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#max-pool-rc-filter).

## Filter responses read only positions within the sequence length

The responses only read the positions `< m + w` of a sequence of length `m + w`.

Formalized by `Cslib.Bioinformatics.Regulatory.ConvolutionPWM.maxPool_congr`, a theorem declared in [CSLibExt/Bioinformatics/Regulatory/ConvolutionPWM.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Regulatory/ConvolutionPWM.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#max-pool-congr).

## Both-strand convolution score

The both-strand score: the larger of the max-pooled responses of `W` and of its reverse
complement.

Formalized by `Cslib.Bioinformatics.Regulatory.ConvolutionPWM.bothStrands`, a definition declared in [CSLibExt/Bioinformatics/Regulatory/ConvolutionPWM.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Regulatory/ConvolutionPWM.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#both-strands).

## The both-strand score is invariant under reverse complementing the sequence

**The both-strand score is invariant under reverse complementing the sequence**, for an
involutive complement.

Formalized by `Cslib.Bioinformatics.Regulatory.ConvolutionPWM.bothStrands_rcSeq`, a theorem declared in [CSLibExt/Bioinformatics/Regulatory/ConvolutionPWM.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Regulatory/ConvolutionPWM.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html#both-strands-rc-seq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Position weight matrices](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/position-weight-matrices/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/bioinformatics/position-weight-matrices)
