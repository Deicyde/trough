---
declaration: section
origin: cited
lean: MathlibExt.Analysis.InnerProductSpace.DouglasLemma.norm_adjoint, MathlibExt.Analysis.InnerProductSpace.DouglasLemma.eq_of_mem_orthogonal_and_apply, MathlibExt.Analysis.InnerProductSpace.DouglasLemma.exists_mem_orthogonal_apply, MathlibExt.Analysis.InnerProductSpace.DouglasLemma.douglasFactorFun, MathlibExt.Analysis.InnerProductSpace.DouglasLemma.douglasFactorFun_spec, MathlibExt.Analysis.InnerProductSpace.DouglasLemma.douglasFactorLin, MathlibExt.Analysis.InnerProductSpace.DouglasLemma.continuous_douglasFactorLin, MathlibExt.Analysis.InnerProductSpace.DouglasLemma.douglasFactor
statement: formalized
proof: formalized
---

# Douglas factorization lemma

17 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/douglas-factorization-lemma/index.html).

## Adjoint preserves the operator norm

Adjoints preserve operator norm.

Formalized by `MathlibExt.Analysis.InnerProductSpace.DouglasLemma.norm_adjoint`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/DouglasLemma.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/DouglasLemma.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/douglas-factorization-lemma/index.html#norm-adjoint).

## Injectivity of an operator on the orthogonal complement of its kernel

Two points of `(ker B)ᗮ` with the same image under `B` are equal, since
their difference lies in `ker B ∩ (ker B)ᗮ`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.DouglasLemma.eq_of_mem_orthogonal_and_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/DouglasLemma.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/DouglasLemma.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/douglas-factorization-lemma/index.html#eq-of-mem-orthogonal-and-apply).

## Preimages in the orthogonal complement of the kernel under range inclusion

If `A.range ≤ B.range`, every `A x` has a preimage under `B` in `(ker B)ᗮ`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.DouglasLemma.exists_mem_orthogonal_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/DouglasLemma.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/DouglasLemma.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/douglas-factorization-lemma/index.html#exists-mem-orthogonal-apply).

## Underlying function of the Douglas factor

The underlying function of the canonical factor: the chosen preimage of `A x`
in `(ker B)ᗮ`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.DouglasLemma.douglasFactorFun`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/DouglasLemma.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/DouglasLemma.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/douglas-factorization-lemma/index.html#douglas-factor-fun).

## Defining properties of the Douglas preimage

The defining properties of the chosen preimage.

Formalized by `MathlibExt.Analysis.InnerProductSpace.DouglasLemma.douglasFactorFun_spec`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/DouglasLemma.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/DouglasLemma.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/douglas-factorization-lemma/index.html#douglas-factor-fun-spec).

## Douglas factor as a linear map

The canonical factor as a linear map.

Formalized by `MathlibExt.Analysis.InnerProductSpace.DouglasLemma.douglasFactorLin`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/DouglasLemma.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/DouglasLemma.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/douglas-factorization-lemma/index.html#douglas-factor-lin).

## Continuity of the Douglas factor via the closed graph theorem

The canonical factor is continuous, by the (sequential) closed graph theorem:
if `u n → x` and `C (u n) → y`, then `y ∈ (ker B)ᗮ` (the orthogonal complement
is closed) and `B y = A x` (continuity of `A` and `B`), so `y = C x` by
uniqueness of the preimage in `(ker B)ᗮ`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.DouglasLemma.continuous_douglasFactorLin`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/DouglasLemma.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/DouglasLemma.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/douglas-factorization-lemma/index.html#continuous-douglas-factor-lin).

## Canonical factor in Douglas' lemma

The canonical factor in Douglas' lemma: for `x : E`, the unique element of
`(ker B)ᗮ` mapped by `B` to `A x`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.DouglasLemma.douglasFactor`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/DouglasLemma.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/DouglasLemma.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/douglas-factorization-lemma/index.html#douglas-factor).

## Douglas factor takes values in the kernel's orthogonal complement

The canonical factor lands in `(ker B)ᗮ`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.DouglasLemma.douglasFactor_mem_orthogonal`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/DouglasLemma.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/DouglasLemma.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/douglas-factorization-lemma/index.html#douglas-factor-mem-orthogonal).

## Douglas factor gives a preimage under B

The canonical factor is a preimage: `B (C x) = A x`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.DouglasLemma.apply_douglasFactor`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/DouglasLemma.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/DouglasLemma.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/douglas-factorization-lemma/index.html#apply-douglas-factor).

## Douglas factor factors A through B

The canonical factor factors `A` through `B`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.DouglasLemma.eq_comp_douglasFactor`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/DouglasLemma.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/DouglasLemma.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/douglas-factorization-lemma/index.html#eq-comp-douglas-factor).

## Uniqueness of the Douglas factor

The canonical factor is the unique operator with the two defining properties.

Formalized by `MathlibExt.Analysis.InnerProductSpace.DouglasLemma.douglasFactor_eq_of_mem_orthogonal_and_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/DouglasLemma.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/DouglasLemma.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/douglas-factorization-lemma/index.html#douglas-factor-eq-of-mem-orthogonal-and).

## Douglas' lemma: range inclusion iff factorization

Douglas' lemma, range form: `A.range ≤ B.range` iff `A = B ∘L C` for some
bounded `C`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.DouglasLemma.range_le_iff_exists_factorization`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/DouglasLemma.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/DouglasLemma.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/douglas-factorization-lemma/index.html#range-le-iff-exists-factorization).

## Factorization implies majorization

If `A = B ∘L C`, then majorization holds with constant `‖C‖`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.DouglasLemma.majorization_of_factorization`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/DouglasLemma.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/DouglasLemma.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/douglas-factorization-lemma/index.html#majorization-of-factorization).

## Douglas' lemma: majorization gives a norm-bounded factor

Douglas' lemma, factorization form with a norm bound: majorization with
constant `c` yields a factor `C` with `A = B ∘L C` and `‖C‖ ≤ c`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.DouglasLemma.exists_factorization_of_majorization`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/DouglasLemma.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/DouglasLemma.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/douglas-factorization-lemma/index.html#exists-factorization-of-majorization).

## Douglas' lemma: majorization iff factorization

Douglas' lemma, majorization form: majorization holds iff `A` factors
through `B`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.DouglasLemma.majorization_iff_exists_factorization`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/DouglasLemma.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/DouglasLemma.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/douglas-factorization-lemma/index.html#majorization-iff-exists-factorization).

## Douglas' lemma: range inclusion iff majorization

Douglas' lemma, range/majorization form: `A.range ≤ B.range` iff
majorization holds.

Formalized by `MathlibExt.Analysis.InnerProductSpace.DouglasLemma.range_le_iff_majorization`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/DouglasLemma.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/DouglasLemma.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/douglas-factorization-lemma/index.html#range-le-iff-majorization).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Douglas factorization lemma](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/douglas-factorization-lemma/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/operator-theory/bounded-operators/douglas-factorization-lemma)
