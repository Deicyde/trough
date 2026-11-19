---
declaration: theorem
origin: cited
lean: KummerCriterion.CyclotomicUnits.CPlusGenerator_exponents_modP_zero_of_kummerLog_det_ne_zero
statement: formalized
proof: formalized
---

# kummer-log-exponents-zero

If $\det M \ne 0$, then every exponent product in $C^+$ which is a $p$th power in the full unit group has all exponents $e_a$ divisible by $p$.

## Depends on

- [completed-log-relation](thm-completed-log-relation.md)
- [kummer-mulvec-zero](thm-kummer-mulvec-zero.md)
- [kummer-linear-algebra](thm-kummer-linear-algebra.md)

## Proof

Apply [Theorem completed-log-relation](thm-completed-log-relation.md) to the $p$th-power relation, then [Theorem kummer-mulvec-zero](thm-kummer-mulvec-zero.md) converts the logarithmic divisibility into $Me=0$, and [Theorem kummer-linear-algebra](thm-kummer-linear-algebra.md) forces $e=0$ modulo $p$.

## Lean

Formalized as [`KummerCriterion.CyclotomicUnits.CPlusGenerator_exponents_modP_zero_of_kummerLog_det_ne_zero`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.CyclotomicUnits.CPlusGenerator_exponents_modP_zero_of_kummerLog_det_ne_zero).

## Sources

- [Kummer's criterion blueprint: subsections/cyclotomic-units.tex, line 355](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/cyclotomic-units.tex#L355)
