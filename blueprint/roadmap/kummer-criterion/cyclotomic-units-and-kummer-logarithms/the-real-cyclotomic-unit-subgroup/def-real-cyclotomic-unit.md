---
declaration: definition
origin: cited
lean: KummerCriterion.realCyclotomicUnit
statement: formalized
---

# real-cyclotomic-unit

For $2\le a\le (p-1)/2$, the *real cyclotomic unit* $\varepsilon_a$ is the unit of $\mathcal O_{K^+}$ obtained by descending the product of the cyclotomic unit $(1-\zeta_p^a)/(1-\zeta_p)$ of $\mathcal O_K$ with its complex conjugate:

$$
\varepsilon_a
\;=\;
\frac{(1-\zeta_p^a)\,(1-\zeta_p^{-a})}{(1-\zeta_p)\,(1-\zeta_p^{-1})} .
$$

This element is fixed by complex conjugation, hence lies in $(\mathcal O_{K^+})^\times$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`KummerCriterion.realCyclotomicUnit`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.realCyclotomicUnit).

## Sources

- [Kummer's criterion blueprint: subsections/cyclotomic-units.tex, line 17](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/cyclotomic-units.tex#L17)
