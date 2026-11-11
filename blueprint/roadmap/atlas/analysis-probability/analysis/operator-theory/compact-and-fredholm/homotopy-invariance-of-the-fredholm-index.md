---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Normed.Operator.FredholmIndexHomotopy.index_eq_of_preconnected, MathlibExt.Analysis.Normed.Operator.FredholmIndexHomotopy.index_eq_of_continuousOn_Icc, MathlibExt.Analysis.Normed.Operator.FredholmIndexHomotopy.index_eq_of_continuous_path, MathlibExt.Analysis.Normed.Operator.FredholmIndexHomotopy.hasFiniteRange_smulRight, MathlibExt.Analysis.Normed.Operator.FredholmIndexHomotopy.index_add_hasFiniteRange, MathlibExt.Analysis.Normed.Operator.FredholmIndexHomotopy.index_hasFiniteRange_add, MathlibExt.Analysis.Normed.Operator.FredholmIndexHomotopy.index_sub_hasFiniteRange
statement: formalized
proof: formalized
---

# Homotopy invariance of the Fredholm index

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/homotopy-invariance-of-the-fredholm-index/index.html).

## Fredholm index is constant on preconnected families

The Fredholm index is constant along a continuous family of Fredholm
operators indexed by a preconnected set, because the index is locally
constant (Mathlib) and takes values in the discrete space `ℤ`.

Formalized by `MathlibExt.Analysis.Normed.Operator.FredholmIndexHomotopy.index_eq_of_preconnected`, a theorem declared in [MathlibExt/Analysis/Normed/Operator/FredholmIndexHomotopy.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Operator/FredholmIndexHomotopy.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/homotopy-invariance-of-the-fredholm-index/index.html#index-eq-of-preconnected).

## Fredholm index is constant along a path continuous on (0, 1)

The Fredholm index is constant along a continuous path of Fredholm
operators on `[0, 1]`.

Formalized by `MathlibExt.Analysis.Normed.Operator.FredholmIndexHomotopy.index_eq_of_continuousOn_Icc`, a theorem declared in [MathlibExt/Analysis/Normed/Operator/FredholmIndexHomotopy.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Operator/FredholmIndexHomotopy.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/homotopy-invariance-of-the-fredholm-index/index.html#index-eq-of-continuous-on-icc).

## Fredholm index is constant along a globally continuous path

The Fredholm index is constant along a globally continuous path of
Fredholm operators on `[0, 1]`.

Formalized by `MathlibExt.Analysis.Normed.Operator.FredholmIndexHomotopy.index_eq_of_continuous_path`, a theorem declared in [MathlibExt/Analysis/Normed/Operator/FredholmIndexHomotopy.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Operator/FredholmIndexHomotopy.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/homotopy-invariance-of-the-fredholm-index/index.html#index-eq-of-continuous-path).

## Rank-one operators have finite range

A rank-one operator has finite range.

Formalized by `MathlibExt.Analysis.Normed.Operator.FredholmIndexHomotopy.hasFiniteRange_smulRight`, a theorem declared in [MathlibExt/Analysis/Normed/Operator/FredholmIndexHomotopy.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Operator/FredholmIndexHomotopy.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/homotopy-invariance-of-the-fredholm-index/index.html#has-finite-range-smul-right).

## Finite-rank perturbation preserves the Fredholm index

Adding a finite-rank operator does not change the Fredholm index.
The proof follows the segment `T + t • F`, `t ∈ [0, 1]`, which is a
continuous path of Fredholm operators.

Formalized by `MathlibExt.Analysis.Normed.Operator.FredholmIndexHomotopy.index_add_hasFiniteRange`, a theorem declared in [MathlibExt/Analysis/Normed/Operator/FredholmIndexHomotopy.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Operator/FredholmIndexHomotopy.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/homotopy-invariance-of-the-fredholm-index/index.html#index-add-has-finite-range).

## Left finite-rank perturbation preserves the Fredholm index

Adding a finite-rank operator on the left does not change the
Fredholm index.

Formalized by `MathlibExt.Analysis.Normed.Operator.FredholmIndexHomotopy.index_hasFiniteRange_add`, a theorem declared in [MathlibExt/Analysis/Normed/Operator/FredholmIndexHomotopy.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Operator/FredholmIndexHomotopy.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/homotopy-invariance-of-the-fredholm-index/index.html#index-has-finite-range-add).

## Subtracting a finite-rank operator preserves the Fredholm index

Subtracting a finite-rank operator does not change the Fredholm
index.

Formalized by `MathlibExt.Analysis.Normed.Operator.FredholmIndexHomotopy.index_sub_hasFiniteRange`, a theorem declared in [MathlibExt/Analysis/Normed/Operator/FredholmIndexHomotopy.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Operator/FredholmIndexHomotopy.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/homotopy-invariance-of-the-fredholm-index/index.html#index-sub-has-finite-range).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Homotopy invariance of the Fredholm index](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/homotopy-invariance-of-the-fredholm-index/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/operator-theory/compact-and-fredholm/homotopy-invariance-of-the-fredholm-index)
