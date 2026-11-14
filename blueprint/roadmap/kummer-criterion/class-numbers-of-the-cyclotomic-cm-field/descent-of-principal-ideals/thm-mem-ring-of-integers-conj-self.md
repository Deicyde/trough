---
declaration: theorem
origin: cited
lean: KummerCriterion.mem_ringOfIntegers_of_conj_eq_self
statement: formalized
proof: formalized
---

# mem-ring-of-integers-conj-self

If $b\in\mathcal O_K$ is fixed by complex conjugation, then it is the image of an element of $\mathcal O_{K^+}$.

## Depends on

- [cm-real-subfield](../the-real-subfield-and-the-class-numbers/def-cm-real-subfield.md)

## Proof

For a CM field, $K^+$ is exactly the fixed field of conjugation, so the element $b$ lies in $K^+$. Being integral over $\mathbb{Z}$, it lies in $K^+ \cap \mathcal O_K = \mathcal O_{K^+}$.

## Lean

Formalized as [`KummerCriterion.mem_ringOfIntegers_of_conj_eq_self`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.mem_ringOfIntegers_of_conj_eq_self).

## Sources

- [Kummer's criterion blueprint: subsections/cm-splitting.tex, line 170](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/cm-splitting.tex#L170)
