---
declaration: theorem
origin: cited
lean: KummerCriterion.CyclotomicUnits.vandermonde_teichmuller_even_sub_one_det_ne_zero
statement: formalized
proof: formalized
---

# vandermonde-nonzero

The Teichmüller Vandermonde determinant occurring in [Theorem kummer-log-vandermonde](thm-kummer-log-vandermonde.md) is nonzero.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

The nodes are the values $\eta_a^2$ for $2 \le a \le (p-1)/2$; they are pairwise distinct and distinct from $1$, because the Teichmüller character is injective on $(\mathbb{Z}/p\mathbb{Z})^\times$ and squaring is two-to-one with the representatives $a$ chosen in a half-system. A Vandermonde determinant in distinct nodes is a product of nonzero differences, hence nonzero.

## Lean

Formalized as [`KummerCriterion.CyclotomicUnits.vandermonde_teichmuller_even_sub_one_det_ne_zero`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.CyclotomicUnits.vandermonde_teichmuller_even_sub_one_det_ne_zero).

## Sources

- [Kummer's criterion blueprint: subsections/cyclotomic-units.tex, line 248](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/cyclotomic-units.tex#L248)
