---
declaration: theorem
origin: cited
lean: KummerCriterion.CyclotomicUnits.completedLog_relation_of_CPlus_product_mem_powers
statement: formalized
proof: formalized
---

# completed-log-relation

If an exponent product in $C^+$ is a $p$th power in the full unit group, then its completed logarithm is divisible by $p$ in the Dwork fixed subalgebra.

## Depends on

- [CPlusExponentProduct](../exact-p-saturation/def-cplusexponentproduct.md)
- [pPowerSubgroup](../exact-p-saturation/def-ppowersubgroup.md)

## Proof

The completed logarithm is a homomorphism on the relevant units: it turns the exponent product into the corresponding integer combination of the logarithms of the generators, and it sends a $p$th power $y^p$ to $p\log y$. Equating the two expressions exhibits the combination $\sum_a e_a \log \varepsilon_a$ as $p$ times an element of the fixed subalgebra. (The sign $(-1)^s$ is killed by the logarithm.)

## Lean

Formalized as [`KummerCriterion.CyclotomicUnits.completedLog_relation_of_CPlus_product_mem_powers`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.CyclotomicUnits.completedLog_relation_of_CPlus_product_mem_powers).

## Sources

- [Kummer's criterion blueprint: subsections/cyclotomic-units.tex, line 311](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/cyclotomic-units.tex#L311)
