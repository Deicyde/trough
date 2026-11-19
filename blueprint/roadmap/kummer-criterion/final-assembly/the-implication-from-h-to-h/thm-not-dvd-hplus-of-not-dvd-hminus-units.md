---
declaration: theorem
origin: cited
lean: KummerCriterion.not_dvd_hPlus_of_not_dvd_hMinus_units
statement: formalized
proof: formalized
---

# not-dvd-hplus-of-not-dvd-hminus-units

If $p\nmid h^-(K)$, then $p\nmid h^+(K)$.

## Depends on

- [hminus-nondiv-to-bernoulli-nondiv](../../the-minus-class-number-criterion/from-h-to-bernoulli-numerators/thm-hminus-nondiv-to-bernoulli-nondiv.md)
- [bernoulli-nonzero-index](thm-bernoulli-nonzero-index.md)
- [sinnott-index-pprimary](../../cyclotomic-units-and-kummer-logarithms/the-prime-conductor-index-theorem/thm-sinnott-index-pprimary.md)
- [CPlus-normalized-index](../../cyclotomic-units-and-kummer-logarithms/the-real-cyclotomic-unit-subgroup/thm-cplus-normalized-index.md)

## Proof

By [Theorem hminus-nondiv-to-bernoulli-nondiv](../../the-minus-class-number-criterion/from-h-to-bernoulli-numerators/thm-hminus-nondiv-to-bernoulli-nondiv.md), the hypothesis $p\nmid h^-(K)$ implies that no Bernoulli numerator in Kummer's range is divisible by $p$, so [Theorem bernoulli-nonzero-index](thm-bernoulli-nonzero-index.md) gives

$$
p\nmid[(\mathcal O_{K^+})^\times:C^+].
$$

Suppose for contradiction that $p\mid h^+(K)$. The prime-conductor index theorem ([Theorem sinnott-index-pprimary](../../cyclotomic-units-and-kummer-logarithms/the-prime-conductor-index-theorem/thm-sinnott-index-pprimary.md)) then gives $p \mid [(\mathcal O_{K^+})^\times:C^+_{\mathrm{norm}}]$, and by [Theorem CPlus-normalized-index](../../cyclotomic-units-and-kummer-logarithms/the-real-cyclotomic-unit-subgroup/thm-cplus-normalized-index.md) this is equivalent to $p$ dividing the ordinary $C^+$ index — a contradiction.

## Lean

Formalized as [`KummerCriterion.not_dvd_hPlus_of_not_dvd_hMinus_units`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.not_dvd_hPlus_of_not_dvd_hMinus_units).

## Sources

- [Kummer's criterion blueprint: subsections/final.tex, line 38](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/final.tex#L38)
