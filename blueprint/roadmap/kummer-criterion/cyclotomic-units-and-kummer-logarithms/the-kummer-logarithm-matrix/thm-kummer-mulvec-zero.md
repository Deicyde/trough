---
declaration: theorem
origin: cited
lean: KummerCriterion.CyclotomicUnits.concreteKummerLogMatrix_mulVec_exponents_eq_zero
statement: formalized
proof: formalized
---

# kummer-mulvec-zero

In the situation of [Theorem completed-log-relation](thm-completed-log-relation.md),

$$
M e=0
\quad\text{over } \mathbb{F}_p,
$$

where $e$ is the vector of exponents $e_a$ reduced modulo $p$.

## Depends on

- [concreteKummerLogMatrix](def-concretekummerlogmatrix.md)
- [completed-log-relation](thm-completed-log-relation.md)

## Proof

Take coordinates in the Dwork basis. The $j$th coordinate of the combination $\sum_a e_a \log\varepsilon_a$ is the $j$th entry of the matrix-vector product $Me$ (before reduction). Divisibility by $p$ of the combination makes every coordinate divisible by $p$, i.e. every entry of $Me$ vanishes after reduction modulo $p$.

## Lean

Formalized as [`KummerCriterion.CyclotomicUnits.concreteKummerLogMatrix_mulVec_exponents_eq_zero`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.CyclotomicUnits.concreteKummerLogMatrix_mulVec_exponents_eq_zero).

## Sources

- [Kummer's criterion blueprint: subsections/cyclotomic-units.tex, line 327](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/cyclotomic-units.tex#L327)
