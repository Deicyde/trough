---
declaration: theorem
origin: cited
lean: KummerCriterion.weakReflection_dvd_hMinus_of_dvd_hPlus_units
statement: formalized
proof: formalized
---

# hplus-to-hminus-units

If $p\mid h^+(K)$, then $p\mid h^-(K)$.

## Depends on

- [not-dvd-hplus-of-not-dvd-hminus-units](thm-not-dvd-hplus-of-not-dvd-hminus-units.md)

## Proof

Contrapositive of [Theorem not-dvd-hplus-of-not-dvd-hminus-units](thm-not-dvd-hplus-of-not-dvd-hminus-units.md): if $p\nmid h^-(K)$, that theorem gives $p\nmid h^+(K)$.

## Lean

Formalized as [`KummerCriterion.weakReflection_dvd_hMinus_of_dvd_hPlus_units`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.weakReflection_dvd_hMinus_of_dvd_hPlus_units).

## Sources

- [Kummer's criterion blueprint: subsections/final.tex, line 58](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/final.tex#L58)
