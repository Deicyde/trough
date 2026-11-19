---
declaration: theorem
origin: cited
lean: KummerCriterion.conj_generator_associated
statement: formalized
proof: formalized
---

# conj-generator-associated

Suppose $I \ne 0$ and $I\mathcal O_K=(a)$. Then, by [Theorem ideal-map-conj](thm-ideal-map-conj.md), also $I\mathcal O_K=(\overline a)$, and the two generators are associated: there is a unit $u\in\mathcal O_K^\times$ with

$$
\overline a = u a.
$$

## Depends on

- [ideal-map-conj](thm-ideal-map-conj.md)

## Proof

Two generators of the same nonzero principal ideal in a domain differ by a unit: from $(a) = (\overline a)$ we get $\overline a = ua$ and $a = v \overline a$ for some $u, v \in \mathcal O_K$, whence $a = vua$ and, since $a \ne 0$, $vu = 1$.

## Lean

Formalized as [`KummerCriterion.conj_generator_associated`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.conj_generator_associated).

## Sources

- [Kummer's criterion blueprint: subsections/cm-splitting.tex, line 97](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/cm-splitting.tex#L97)
