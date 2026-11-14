---
declaration: theorem
origin: cited
lean: KummerCriterion.classGroupMap_injective
statement: formalized
proof: formalized
---

# class-group-map-injective

For an odd prime cyclotomic field, the map

$$
\mathrm{Cl}(\mathcal O_{K^+})\longrightarrow \mathrm{Cl}(\mathcal O_K)
$$

is injective.

## Depends on

- [class-group-map](def-class-group-map.md)
- [is-principal-after-extension](../descent-of-principal-ideals/thm-is-principal-after-extension.md)

## Proof

A group homomorphism is injective when its kernel is trivial. If an ideal class of $\mathcal O_{K^+}$ maps to the trivial class, a representative ideal becomes principal after extension to $\mathcal O_K$; by [Theorem is-principal-after-extension](../descent-of-principal-ideals/thm-is-principal-after-extension.md) the representative was already principal, so the class is trivial.

## Lean

Formalized as [`KummerCriterion.classGroupMap_injective`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.classGroupMap_injective).

## Sources

- [Kummer's criterion blueprint: subsections/cm-splitting.tex, line 218](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/cm-splitting.tex#L218)
