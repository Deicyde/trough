---
declaration: theorem
origin: cited
lean: KummerCriterion.cyclotomicUnitIndexSubgroup_eq_CPlus
statement: formalized
proof: formalized
---

# index-subgroup-eq-CPlus

Up to the normalisation of [Theorem CPlus-normalized-index](../the-real-cyclotomic-unit-subgroup/thm-cplus-normalized-index.md), the subgroup used in the index theorem agrees with the subgroup $C^+$ used in the saturation argument: each contains representatives generating the other modulo $\{\pm1\}$ and squares.

## Depends on

- [cyclotomicUnitIndexSubgroup](def-cyclotomicunitindexsubgroup.md)
- [CPlus](../the-real-cyclotomic-unit-subgroup/def-cplus.md)

## Proof

Both inclusions are checked on generators. A normalised generator $\xi_a$ times a root of unity recovers the cyclotomic unit $(1-\zeta_p^a)/(1-\zeta_p)$, whose product with its conjugate is $\varepsilon_a = \xi_a^2$; conversely each $\varepsilon_a$ is the square of $\xi_a$, so the two subgroups generate each other up to squares and signs.

## Lean

Formalized as [`KummerCriterion.cyclotomicUnitIndexSubgroup_eq_CPlus`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.cyclotomicUnitIndexSubgroup_eq_CPlus).

## Sources

- [Kummer's criterion blueprint: subsections/cyclotomic-units.tex, line 390](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/cyclotomic-units.tex#L390)
