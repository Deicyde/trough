---
declaration: section
origin: cited
lean: MeasureTheory.exists_gt_not_mem_of_volume_lt_top, MathlibExt.MeasureTheory.PositiveMeasureThreeTermProgressionWanted.exists_add_mem_and_sub_mem_of_volume_pos
statement: formalized
---

# Lebesgue measure: its own results

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lebesgue-measure/index.html).

Lebesgue measure on the real line and Euclidean space: volumes of concrete bodies, null sets and density phenomena.

## Sets of finite Lebesgue measure contain no right half-line

Let $E \subseteq \mathbb{R}$
have finite Lebesgue outer measure ($E$ need not be measurable). Then for every real $X$ there
is a real $x > X$ with $x \notin E$; that is, $E$ contains no half-line $(X, \infty)$.

Formalized by `MeasureTheory.exists_gt_not_mem_of_volume_lt_top`, a theorem declared in [MathlibExt/MeasureTheory/Measure/Lebesgue/Finite.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/MeasureTheory/Measure/Lebesgue/Finite.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lebesgue-measure/index.html#exists-gt-not-mem-of-volume-lt-top).

## Sets of positive measure contain three-term arithmetic progressions

For every Borel set
$A \subseteq \mathbb{R}$ of positive Lebesgue measure there exist $x \in A$ and $y > 0$ such that
$x + y \in A$ and $x - y \in A$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Measure and integration; Classical measure theory), problem `ma_proofbench_l2_75`.

Stated but not proved: `MathlibExt.MeasureTheory.PositiveMeasureThreeTermProgressionWanted.exists_add_mem_and_sub_mem_of_volume_pos` is written with `theorem_wanted` in [WantedExt/MeasureTheory/PositiveMeasureThreeTermProgressionWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/MeasureTheory/PositiveMeasureThreeTermProgressionWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lebesgue-measure/index.html#exists-add-mem-and-sub-mem-of-volume-pos).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Lebesgue measure](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lebesgue-measure/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/MeasureTheory/lebesgue-measure)
