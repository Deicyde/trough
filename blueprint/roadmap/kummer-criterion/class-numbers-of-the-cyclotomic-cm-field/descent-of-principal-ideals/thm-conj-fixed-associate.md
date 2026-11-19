---
declaration: theorem
origin: cited
lean: KummerCriterion.exists_conj_fixed_associate_of_classification
statement: formalized
proof: formalized
---

# conj-fixed-associate

In the situation of [Theorem conj-generator-associated](thm-conj-generator-associated.md), the generator $a$ may be replaced by an associate $b$ such that

$$
\overline b=b
\qquad\text{and}\qquad
(b)=(a).
$$

## Depends on

- [antisymmetric-unit-classification](thm-antisymmetric-unit-classification.md)

## Proof

By [Theorem antisymmetric-unit-classification](thm-antisymmetric-unit-classification.md), the unit $u = \overline a / a$ has the form $(-1)^n \zeta_p^m$. Since $p$ is odd, every power of $\zeta_p$ is a square in $\langle\zeta_p\rangle$, and the sign can be absorbed: write $u = w/\overline w$ for a suitable root of unity $w$ (concretely, a power of $\zeta_p$ chosen so that $w^2$ accounts for $\zeta_p^m$, possibly times $-1$). Then $b := w a$ satisfies $\overline b = \overline w\,\overline a = \overline w u a = w a = b$, and $b$ is an associate of $a$, so it generates the same ideal.

## Lean

Formalized as [`KummerCriterion.exists_conj_fixed_associate_of_classification`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.exists_conj_fixed_associate_of_classification).

## Sources

- [Kummer's criterion blueprint: subsections/cm-splitting.tex, line 148](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/cm-splitting.tex#L148)
