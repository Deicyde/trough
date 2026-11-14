---
declaration: theorem
origin: cited
lean: KummerCriterion.cyclotomicUnitIndex_primeConductor_pPrimary_aux
statement: formalized
proof: formalized
---

# index-pprimary-aux

For $p\ge5$, the normalised cyclotomic-unit index has the same $p$-divisibility as $h^+$:

$$
p\mid[(\mathcal O_{K^+})^\times:C^+_{\mathrm{norm}}]
\Longleftrightarrow
p\mid h^+(K).
$$

## Depends on

- [index-subgroup-eq-CPlus](thm-index-subgroup-eq-cplus.md)
- [deleted-fourier-kummer-dirichlet](thm-deleted-fourier-kummer-dirichlet.md)
- [CPlus-normalized-index](../the-real-cyclotomic-unit-subgroup/thm-cplus-normalized-index.md)
- [class-number-hplus](../../class-numbers-of-the-cyclotomic-cm-field/the-real-subfield-and-the-class-numbers/def-class-number-hplus.md)

## Proof

This is Sinnott's prime-conductor index theorem: for prime conductor the index of the circular units in the full unit group equals $h^+$. The deleted-Fourier determinant of [Theorem deleted-fourier-kummer-dirichlet](thm-deleted-fourier-kummer-dirichlet.md) provides the determinant computation at the heart of the proof, [Theorem index-subgroup-eq-CPlus](thm-index-subgroup-eq-cplus.md) identifies the index subgroup with the one used here, and [Theorem CPlus-normalized-index](../the-real-cyclotomic-unit-subgroup/thm-cplus-normalized-index.md) transfers $p$-divisibility between the standard and normalised indices.

## Lean

Formalized as [`KummerCriterion.cyclotomicUnitIndex_primeConductor_pPrimary_aux`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.cyclotomicUnitIndex_primeConductor_pPrimary_aux).

## Sources

- [Kummer's criterion blueprint: subsections/cyclotomic-units.tex, line 424](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/cyclotomic-units.tex#L424)
