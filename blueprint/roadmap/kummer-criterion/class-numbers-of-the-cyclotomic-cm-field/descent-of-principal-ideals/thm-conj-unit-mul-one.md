---
declaration: theorem
origin: cited
lean: KummerCriterion.conj_unit_mul_eq_one
statement: formalized
proof: formalized
---

# conj-unit-mul-one

The unit $u$ obtained from $\overline a=ua$ in [Theorem conj-generator-associated](thm-conj-generator-associated.md) satisfies

$$
u\overline u=1.
$$

## Depends on

- [conj-generator-associated](thm-conj-generator-associated.md)

## Proof

Apply complex conjugation to $\overline a=ua$: since conjugation is an involution, $a = \overline u\,\overline a = \overline u u a$. As $a\ne0$, cancellation in the domain $\mathcal O_K$ gives $u\overline u=1$.

## Lean

Formalized as [`KummerCriterion.conj_unit_mul_eq_one`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.conj_unit_mul_eq_one).

## Sources

- [Kummer's criterion blueprint: subsections/cm-splitting.tex, line 114](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/cm-splitting.tex#L114)
