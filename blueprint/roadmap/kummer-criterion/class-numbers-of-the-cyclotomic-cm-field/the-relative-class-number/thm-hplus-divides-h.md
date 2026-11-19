---
declaration: theorem
origin: cited
lean: KummerCriterion.hPlus_dvd_h
statement: formalized
proof: formalized
---

# hplus-divides-h

The plus class number divides the full class number:

$$
h^+(K)\mid h(K).
$$

## Depends on

- [class-number-h](../the-real-subfield-and-the-class-numbers/def-class-number-h.md)
- [class-number-hplus](../the-real-subfield-and-the-class-numbers/def-class-number-hplus.md)
- [class-group-map-injective](thm-class-group-map-injective.md)

## Proof

By [Theorem class-group-map-injective](thm-class-group-map-injective.md), $\mathrm{Cl}(\mathcal O_{K^+})$ embeds as a subgroup of the finite group $\mathrm{Cl}(\mathcal O_K)$, and Lagrange's theorem gives the divisibility of cardinalities.

## Lean

Formalized as [`KummerCriterion.hPlus_dvd_h`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.hPlus_dvd_h).

## Sources

- [Kummer's criterion blueprint: subsections/cm-splitting.tex, line 235](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/cm-splitting.tex#L235)
