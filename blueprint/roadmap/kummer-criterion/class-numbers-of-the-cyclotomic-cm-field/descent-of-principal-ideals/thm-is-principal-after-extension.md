---
declaration: theorem
origin: cited
lean: KummerCriterion.isPrincipal_of_isPrincipal_map_Kplus
statement: formalized
proof: formalized
---

# is-principal-after-extension

Let $K$ be the $p$th cyclotomic field, with $p$ odd. If an ideal of $\mathcal O_{K^+}$ becomes principal after extension to $\mathcal O_K$, then it was already principal.

## Depends on

- [is-principal-map-span-singleton](thm-is-principal-map-span-singleton.md)
- [ideal-map-conj](thm-ideal-map-conj.md)
- [conj-generator-associated](thm-conj-generator-associated.md)
- [conj-unit-mul-one](thm-conj-unit-mul-one.md)
- [antisymmetric-unit-classification](thm-antisymmetric-unit-classification.md)
- [conj-fixed-associate](thm-conj-fixed-associate.md)
- [mem-ring-of-integers-conj-self](thm-mem-ring-of-integers-conj-self.md)

## Proof

Let $I$ be such an ideal; we may assume $I \ne 0$. Choose a generator $a$ of $I\mathcal O_K$. The extended ideal is conjugation-stable ([Theorem ideal-map-conj](thm-ideal-map-conj.md)), so [Theorem conj-generator-associated](thm-conj-generator-associated.md) produces a unit $u$ with $\overline a = ua$, and [Theorem conj-unit-mul-one](thm-conj-unit-mul-one.md) shows $u\overline u = 1$. The classification of such units ([Theorem antisymmetric-unit-classification](thm-antisymmetric-unit-classification.md)) lets us replace $a$ by a conjugation-fixed associate $b$ with $(b) = I\mathcal O_K$ ([Theorem conj-fixed-associate](thm-conj-fixed-associate.md)). By [Theorem mem-ring-of-integers-conj-self](thm-mem-ring-of-integers-conj-self.md), $b$ descends to an element $b_0 \in \mathcal O_{K^+}$, and [Theorem is-principal-map-span-singleton](thm-is-principal-map-span-singleton.md) contracts the equality $I\mathcal O_K = (b_0)$ to $I = (b_0)$.

## Lean

Formalized as [`KummerCriterion.isPrincipal_of_isPrincipal_map_Kplus`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.isPrincipal_of_isPrincipal_map_Kplus).

## Sources

- [Kummer's criterion blueprint: subsections/cm-splitting.tex, line 182](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/cm-splitting.tex#L182)
