---
declaration: section
origin: cited
lean: MathlibExt.MeasureTheory.Geometry.BesicovitchKakeyaWanted.besicovitch_kakeya_compact_measure_zero, MathlibExt.Analysis.WangZahlKakeyaWanted.Analysis.WangZahlKakeya.Space, MathlibExt.Analysis.WangZahlKakeyaWanted.Analysis.WangZahlKakeya.IsKakeya, MathlibExt.Analysis.WangZahlKakeyaWanted.Analysis.WangZahlKakeya.wang_zahl_kakeya_dimH
statement: formalized
---

# Kakeya sets

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/kakeya-sets/index.html).

## Besicovitch's Kakeya set of measure zero

There is a compact set $K \subseteq \mathbb{R}^2$
of Lebesgue measure zero that contains a unit segment in every direction: $K$ is measurable,
and for every unit vector $v \in \mathbb{R}^2$ there is a point $a \in \mathbb{R}^2$ with
$a + t v \in K$ for all $t \in [0, 1]$.

The proof here follows T. W. Körner, "Besicovitch via Baire", Studia Math. 158 (2003): a
Baire-category argument in the Hausdorff metric space of compact sets, not a Perron-tree
construction.

## Sources

- A. S. Besicovitch, Math. Z. 27 (1928) 312–320 and S. Kakeya, Tohoku Rep. 6 (1917); Perron-tree gives compact measure-zero Kakeya set; Lean states compact Lebesgue-null oriented version in ℝ² with segments `a+t•v`, `t∈[0, 1]`.

Formalized by `MathlibExt.MeasureTheory.Geometry.BesicovitchKakeyaWanted.besicovitch_kakeya_compact_measure_zero`, a theorem declared in [MathlibExt/MeasureTheory/Geometry/BesicovitchKakeya.lean, line 1034](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/MeasureTheory/Geometry/BesicovitchKakeya.lean#L1034). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/kakeya-sets/index.html#besicovitch-kakeya-compact-measure-zero).

## Three-dimensional Euclidean space

The space $\mathbb{R}^3$ with the Euclidean inner
product.

Formalized by `MathlibExt.Analysis.WangZahlKakeyaWanted.Analysis.WangZahlKakeya.Space`, an abbreviation declared in [WantedExt/Analysis/WangZahlKakeyaWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/WangZahlKakeyaWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/kakeya-sets/index.html#space).

## Kakeya set

A Kakeya set is a compact subset $K$ of three-dimensional Euclidean space
that contains a unit line segment in every direction: for every unit vector $v$ there is a
point $x$ with $x + t v \in K$ for all $t \in [0, 1]$.

Formalized by `MathlibExt.Analysis.WangZahlKakeyaWanted.Analysis.WangZahlKakeya.IsKakeya`, a definition declared in [WantedExt/Analysis/WangZahlKakeyaWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/WangZahlKakeyaWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/kakeya-sets/index.html#is-kakeya).

## Wang–Zahl theorem: the Kakeya conjecture in three dimensions

Every Kakeya set in
three-dimensional Euclidean space has Hausdorff dimension $3$.

## Sources

- H. Wang and J. Zahl, 'Volume estimates for unions of convex sets, and the Kakeya set conjecture in three dimensions', Theorem 1.1, arXiv:2502.17655 (2025), https://arxiv.org/abs/2502.17655. The proof builds on their 'Sticky Kakeya sets and the sticky Kakeya conjecture', arXiv:2210.09581, and 'The Assouad dimension of Kakeya sets in R^3', arXiv:2401.12337. Problem `wang_zahl_kakeya_dimH` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.WangZahlKakeyaWanted.Analysis.WangZahlKakeya.wang_zahl_kakeya_dimH` is written with `theorem_wanted` in [WantedExt/Analysis/WangZahlKakeyaWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/WangZahlKakeyaWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/kakeya-sets/index.html#wang-zahl-kakeya-dim-h).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Kakeya sets](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/kakeya-sets/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/harmonic-analysis/fourier-transform/kakeya-sets)
