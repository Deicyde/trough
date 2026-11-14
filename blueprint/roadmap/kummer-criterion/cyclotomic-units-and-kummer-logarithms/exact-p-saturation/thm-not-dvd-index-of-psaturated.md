---
declaration: theorem
origin: cited
lean: KummerCriterion.not_dvd_index_of_pSaturated
statement: formalized
proof: formalized
---

# not-dvd-index-of-pSaturated

If $C^+$ is $p$-saturated in $E^+$, then

$$
p\nmid[E^+:C^+].
$$

## Depends on

- [pSaturated](def-psaturated.md)
- [CPlus](../the-real-cyclotomic-unit-subgroup/def-cplus.md)
- [EPlus](def-eplus.md)

## Proof

The group-theoretic statement is: a finite-index $p$-saturated subgroup $H \le E$ whose inclusion captures the $p$-torsion of $E/H$ has index prime to $p$. Indeed, if $p$ divided the index, the finite abelian quotient $E/H$ would contain an element of order exactly $p$, say the class of $x$; then $x^p \in H$ is a $p$th power in $E$, so by saturation $x^p = y^p$ with $y\in H$, and $x/y$ is a $p$-torsion unit of $E$ not in $H$. For $E = E^+$, torsion units of the totally real field $K^+$ are $\pm1$, and $-1 \in C^+$ by construction, so no such element exists — a contradiction. Finiteness of the index is supplied by the cyclotomic-unit index theory (the units $\varepsilon_a$ are a full-rank family).

## Lean

Formalized as [`KummerCriterion.not_dvd_index_of_pSaturated`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.not_dvd_index_of_pSaturated).

## Sources

- [Kummer's criterion blueprint: subsections/cyclotomic-units.tex, line 184](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/cyclotomic-units.tex#L184)
