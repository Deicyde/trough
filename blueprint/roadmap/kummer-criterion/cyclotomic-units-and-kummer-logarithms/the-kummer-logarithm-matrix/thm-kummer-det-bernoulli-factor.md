---
declaration: theorem
origin: cited
lean: KummerCriterion.CyclotomicUnits.concreteKummerLogMatrix_det_ne_zero_iff_forall_bernoulliFactor_ne_zero
statement: formalized
proof: formalized
---

# kummer-det-bernoulli-factor

$\det M \ne 0$ if and only if every diagonal Bernoulli factor is nonzero.

## Depends on

- [kummer-log-vandermonde](thm-kummer-log-vandermonde.md)
- [vandermonde-nonzero](thm-vandermonde-nonzero.md)

## Proof

By [Theorem kummer-log-vandermonde](thm-kummer-log-vandermonde.md), $\det M = \det D \cdot \det V$, and $\det V \ne 0$ by [Theorem vandermonde-nonzero](thm-vandermonde-nonzero.md). Hence $\det M \ne 0$ exactly when $\det D = \prod_j D_{jj} \ne 0$, i.e. when every diagonal entry is nonzero.

## Lean

Formalized as [`KummerCriterion.CyclotomicUnits.concreteKummerLogMatrix_det_ne_zero_iff_forall_bernoulliFactor_ne_zero`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.CyclotomicUnits.concreteKummerLogMatrix_det_ne_zero_iff_forall_bernoulliFactor_ne_zero).

## Sources

- [Kummer's criterion blueprint: subsections/cyclotomic-units.tex, line 262](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/cyclotomic-units.tex#L262)
