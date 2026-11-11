---
declaration: section
origin: cited
lean: MetaMathlibExt.carlemanGeomMean, MetaMathlibExt.carlemanGeomMean_sum_add_mul_le, MetaMathlibExt.carlemanGeomMean_sum_le, MetaMathlibExt.carleman_inequality
statement: formalized
proof: formalized
---

# Carleman's inequality

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/carleman-s-inequality/index.html).

## Geometric mean of the initial terms of a sequence

The geometric mean of the first `n + 1` terms of a sequence `a`.

Formalized by `MetaMathlibExt.carlemanGeomMean`, a definition declared in [MathlibExt/Analysis/Series/CarlemanInequality.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Series/CarlemanInequality.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/carleman-s-inequality/index.html#carleman-geom-mean).

## Strengthened finite Carleman inequality

Strengthened finite Carleman inequality: the partial sum of the geometric
means plus `(M + 1)` times the last geometric mean is bounded by `e` times the
partial sum of the terms.

Formalized by `MetaMathlibExt.carlemanGeomMean_sum_add_mul_le`, a theorem declared in [MathlibExt/Analysis/Series/CarlemanInequality.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Series/CarlemanInequality.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/carleman-s-inequality/index.html#carleman-geom-mean-sum-add-mul-le).

## Finite Carleman inequality

Finite Carleman inequality: the partial sum of the geometric means is
bounded by `e` times the partial sum of the terms.

Formalized by `MetaMathlibExt.carlemanGeomMean_sum_le`, a theorem declared in [MathlibExt/Analysis/Series/CarlemanInequality.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Series/CarlemanInequality.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/carleman-s-inequality/index.html#carleman-geom-mean-sum-le).

## Carleman's inequality

Carleman's inequality (sharp form): for a summable nonnegative sequence,
the series of geometric means of the initial products is summable and bounded
by `e` times the series of the terms.

Formalized by `MetaMathlibExt.carleman_inequality`, a theorem declared in [MathlibExt/Analysis/Series/CarlemanInequality.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Series/CarlemanInequality.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/carleman-s-inequality/index.html#carleman-inequality).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Carleman's inequality](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/carleman-s-inequality/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/inequalities/carleman-s-inequality)
