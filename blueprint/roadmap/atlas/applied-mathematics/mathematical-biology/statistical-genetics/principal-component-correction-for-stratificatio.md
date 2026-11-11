---
declaration: section
origin: cited
lean: MathlibExt.Biology.StatisticalGenetics.Eigenstrat.adjusted, MathlibExt.Biology.StatisticalGenetics.Eigenstrat.adjusted_mem_orthogonal, MathlibExt.Biology.StatisticalGenetics.Eigenstrat.inner_adjusted_eq_zero, MathlibExt.Biology.StatisticalGenetics.Eigenstrat.adjusted_eq_starProjection_orthogonal, MathlibExt.Biology.StatisticalGenetics.Eigenstrat.adjusted_add, MathlibExt.Biology.StatisticalGenetics.Eigenstrat.adjusted_smul, MathlibExt.Biology.StatisticalGenetics.Eigenstrat.adjusted_eq_zero_iff, MathlibExt.Biology.StatisticalGenetics.Eigenstrat.adjusted_add_of_mem
statement: formalized
proof: formalized
---

# Principal-component correction for stratification

34 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/principal-component-correction-for-stratificatio/index.html).

## Residualization on a span of axes

## Residualized vector after adjustment for a subspace

The adjusted (residualized) `y`: the residual of the least-squares regression of `y` on the
subspace `V` (`y` minus its orthogonal projection onto `V`).

Formalized by `MathlibExt.Biology.StatisticalGenetics.Eigenstrat.adjusted`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/principal-component-correction-for-stratificatio/index.html#adjusted).

## Residuals lie in the orthogonal complement

Residuals are orthogonal to the adjustment subspace.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Eigenstrat.adjusted_mem_orthogonal`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/principal-component-correction-for-stratificatio/index.html#adjusted-mem-orthogonal).

## Residuals are orthogonal to every axis

Residuals are orthogonal to every vector of the subspace, in particular to every axis.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Eigenstrat.inner_adjusted_eq_zero`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/principal-component-correction-for-stratificatio/index.html#inner-adjusted-eq-zero).

## Residual as projection onto the orthogonal complement

The residual is the orthogonal projection onto `Vᗮ`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Eigenstrat.adjusted_eq_starProjection_orthogonal`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/principal-component-correction-for-stratificatio/index.html#adjusted-eq-star-projection-orthogonal).

## Additivity of residualization

Residualization is additive.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Eigenstrat.adjusted_add`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/principal-component-correction-for-stratificatio/index.html#adjusted-add).

## Homogeneity of residualization

Residualization is homogeneous.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Eigenstrat.adjusted_smul`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/principal-component-correction-for-stratificatio/index.html#adjusted-smul).

## Residual vanishes exactly on the subspace

The residual vanishes exactly on the subspace.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Eigenstrat.adjusted_eq_zero_iff`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/principal-component-correction-for-stratificatio/index.html#adjusted-eq-zero-iff).

## Stratification within the axis span does not change the residual

Adding a vector of the subspace (stratification lying in the axis span) does not change the
residual.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Eigenstrat.adjusted_add_of_mem`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/principal-component-correction-for-stratificatio/index.html#adjusted-add-of-mem).

## Vectors orthogonal to the subspace are their own residuals

Vectors orthogonal to the subspace are their own residuals: stratification outside the axis
span is not removed.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Eigenstrat.adjusted_of_mem_orthogonal`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/principal-component-correction-for-stratificatio/index.html#adjusted-of-mem-orthogonal).

## Residual with respect to an orthonormal family of axes

Regressing on an orthonormal family of axes one axis at a time gives the joint residual:
`y - ∑ₖ ⟪aₖ, y⟫ aₖ`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Eigenstrat.adjusted_span_orthonormal`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/principal-component-correction-for-stratificatio/index.html#adjusted-span-orthonormal).

## Frisch–Waugh–Lovell theorem, uniqueness

Frisch–Waugh–Lovell, uniqueness: in any least-squares decomposition
`y = c + β g + e` with `c ∈ V` and `e ⊥ V ⊔ span {g}`, the coefficient `β` is the
coefficient of the regression of the residualized `y` on the residualized `g`, and the
residual `e` is the residual of that regression.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Eigenstrat.frischWaughLovell`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/principal-component-correction-for-stratificatio/index.html#frisch-waugh-lovell).

## Frisch–Waugh–Lovell theorem, existence

Frisch–Waugh–Lovell, existence: the coefficient of the residual-on-residual regression
gives a least-squares decomposition of `y` on `V ⊔ span {g}`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Eigenstrat.exists_frischWaughLovell`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/principal-component-correction-for-stratificatio/index.html#exists-frisch-waugh-lovell).

## EIGENSTRAT association statistic

The EIGENSTRAT association statistic `(N - K - 1) ⟪r_g, r_y⟫² / (‖r_g‖² ‖r_y‖²)` of the
adjusted genotype `r_g` and adjusted phenotype `r_y`: `(N - K - 1)` times their squared cosine,
which is their squared sample correlation when both are centered (Price et al. 2006). When either
adjusted vector is zero the ratio is the junk value `0`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Eigenstrat.chiSq`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/principal-component-correction-for-stratificatio/index.html#chi-sq).

## Stratification in the axis span is removed

Adding vectors of `V` to the phenotype and
the genotype does not change the EIGENSTRAT statistic.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Eigenstrat.chiSq_add_of_mem`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/principal-component-correction-for-stratificatio/index.html#chi-sq-add-of-mem).

## Nonnegativity of the EIGENSTRAT statistic

The EIGENSTRAT statistic is nonnegative when `K + 1 ≤ N`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Eigenstrat.chiSq_nonneg`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/principal-component-correction-for-stratificatio/index.html#chi-sq-nonneg).

## Genotypes in the axis span carry no signal after adjustment

A genotype lying in the axis span carries no signal after adjustment (its residual is zero,
and the statistic is the junk value `0` of the zero denominator).

Formalized by `MathlibExt.Biology.StatisticalGenetics.Eigenstrat.chiSq_of_mem`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/principal-component-correction-for-stratificatio/index.html#chi-sq-of-mem).

## Allele-frequency estimate of a marker

The allele-frequency estimate `p̂ⱼ = μⱼ / 2` of marker `j`, where `μⱼ` is the mean
variant-allele count of column `j` (autosomal diploid data, counts in `{0, 1, 2}`).

Formalized by `MathlibExt.Biology.StatisticalGenetics.Eigenstrat.alleleFreq`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/principal-component-correction-for-stratificatio/index.html#allele-freq).

## Patterson's normalized genotype matrix

Patterson's normalized genotype matrix `(C i j - μⱼ) / √(p̂ⱼ (1 - p̂ⱼ))`. For a
monomorphic marker (`p̂ⱼ ∈ {0, 1}`) the denominator is `0` and the column is the junk value `0`;
Patterson et al. use polymorphic markers only.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Eigenstrat.normalizedGenotype`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean, line 281](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean#L281). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/principal-component-correction-for-stratificatio/index.html#normalized-genotype).

## Patterson's relatedness matrix

Patterson's `N × N` matrix `Ψ = M Mᵀ / (number of markers)` of the normalized genotypes,
whose top eigenvectors are the axes of variation.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Eigenstrat.relatednessMatrix`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/principal-component-correction-for-stratificatio/index.html#relatedness-matrix).

## Patterson's relatedness matrix is positive semidefinite

Patterson's matrix `Ψ` is positive semidefinite.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Eigenstrat.relatednessMatrix_posSemidef`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean, line 290](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean#L290). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/principal-component-correction-for-stratificatio/index.html#relatedness-matrix-pos-semidef).

## All-ones vector lies in the kernel of the relatedness matrix

The all-ones vector is in the kernel of `Ψ` (columns of the normalized matrix are centered),
so at most `N - 1` eigenvalues are nonzero.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Eigenstrat.relatednessMatrix_mulVec_one`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean, line 299](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean#L299). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/principal-component-correction-for-stratificatio/index.html#relatedness-matrix-mul-vec-one).

## Axes of variation

The axes of variation: an orthonormal eigenbasis of `Ψ`, in decreasing eigenvalue order.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Eigenstrat.axes`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean, line 308](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean#L308). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/principal-component-correction-for-stratificatio/index.html#axes).

## Eigenvalues of the axes of variation

The eigenvalues of `Ψ` in decreasing order, matching `axes`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Eigenstrat.axisEigenvalues`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean, line 313](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean#L313). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/principal-component-correction-for-stratificatio/index.html#axis-eigenvalues).

## Span of the top axes of variation

The span of the top `K` axes of variation, the subspace EIGENSTRAT adjusts for.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Eigenstrat.topAxesSpan`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean, line 317](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean#L317). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/principal-component-correction-for-stratificatio/index.html#top-axes-span).

## Each top axis lies in the span of the top axes

Each of the top `K` axes lies in their span.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Eigenstrat.axes_mem_topAxesSpan`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean, line 322](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean#L322). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/principal-component-correction-for-stratificatio/index.html#axes-mem-top-axes-span).

## Dimension of the span of the top axes

The top `K` axes span a `K`-dimensional subspace.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Eigenstrat.finrank_topAxesSpan`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean, line 327](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean#L327). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/principal-component-correction-for-stratificatio/index.html#finrank-top-axes-span).

## Sequential count of significant axes

Patterson's sequential count of significant axes: among the first `K` statistics, the
length of the leading run of statistics exceeding the threshold `t` (testing stops at the first
non-significant one).

Formalized by `MathlibExt.Biology.StatisticalGenetics.Eigenstrat.numSignificant`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean, line 359](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean#L359). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/principal-component-correction-for-stratificatio/index.html#num-significant).

## At most K axes are declared significant

At most `K` axes are declared significant.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Eigenstrat.numSignificant_le`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean, line 365](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean#L365). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/principal-component-correction-for-stratificatio/index.html#num-significant-le).

## Characterization of the axes counted as significant

The first `numSignificant stat t K` indices are exactly those `k < K` whose statistics and
all earlier ones exceed the threshold.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Eigenstrat.lt_numSignificant_iff`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean, line 374](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean#L374). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/principal-component-correction-for-stratificatio/index.html#lt-num-significant-iff).

## Significant axes have statistics above the threshold

Every axis counted as significant has a statistic above the threshold.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Eigenstrat.lt_stat_of_lt_numSignificant`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean, line 400](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean#L400). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/principal-component-correction-for-stratificatio/index.html#lt-stat-of-lt-num-significant).

## Criterion for at least one significant axis

At least one axis is significant iff the leading statistic exceeds the threshold.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Eigenstrat.numSignificant_pos_iff`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean, line 405](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean#L405). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/principal-component-correction-for-stratificatio/index.html#num-significant-pos-iff).

## Count of significant axes decreases with the threshold

A higher threshold declares no more axes significant.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Eigenstrat.numSignificant_antitone`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean, line 411](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean#L411). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/principal-component-correction-for-stratificatio/index.html#num-significant-antitone).

## Significant-axis count for decreasing statistics

For decreasing statistics (such as ordered eigenvalues compared with a fixed threshold) the
sequential count is the number of statistics above the threshold.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Eigenstrat.numSignificant_eq_card_of_antitone`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean, line 420](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean#L420). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/principal-component-correction-for-stratificatio/index.html#num-significant-eq-card-of-antitone).

## Conditional error bound

If, under the null hypothesis, the `k`-th statistic exceeds `t`
with probability at most `1 - F t` (the Tracy–Widom approximation with `F` the TW₁ distribution
function, taken here as a hypothesis), then the rule declares more than `k` significant axes with
probability at most `1 - F t`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Eigenstrat.measure_lt_numSignificant_le`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean, line 434](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/Eigenstrat.lean#L434). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/principal-component-correction-for-stratificatio/index.html#measure-lt-num-significant-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Principal-component correction for stratification](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/principal-component-correction-for-stratificatio/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/statistical-genetics/principal-component-correction-for-stratificatio)
