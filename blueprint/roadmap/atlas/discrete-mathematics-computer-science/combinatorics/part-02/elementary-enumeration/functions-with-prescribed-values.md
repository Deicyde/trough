---
declaration: section
origin: cited
lean: Fintype.piFinsetOn, Fintype.mem_piFinsetOn, Fintype.card_piFinsetOn, Fintype.sum_piFinsetOn_prod, Fintype.prod_sum_eq_sum_piFinsetOn_mul, Fintype.existsUnique_piFinsetOn, Fintype.card_filter_piFinset_eqOn_of_mem, Fintype.card_filter_univ_eqOn
statement: formalized
proof: formalized
---

# Functions with prescribed values

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/functions-with-prescribed-values/index.html).

## Finite tuples with prescribed default values

Finite tuples constrained on `P` and equal to a prescribed default elsewhere.

Formalized by `Fintype.piFinsetOn`, a definition declared in [MathlibExt/Data/Fintype/PiFinsetOn.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Data/Fintype/PiFinsetOn.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/functions-with-prescribed-values/index.html#pi-finset-on).

## Membership in default-padded finite tuples

Membership gives the allowed values on the active indices and the default off them.

Formalized by `Fintype.mem_piFinsetOn`, a theorem declared in [MathlibExt/Data/Fintype/PiFinsetOn.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Data/Fintype/PiFinsetOn.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/functions-with-prescribed-values/index.html#mem-pi-finset-on).

## Number of default-padded finite tuples

Inactive coordinates contribute one choice, so only active coordinates enter the product.

Formalized by `Fintype.card_piFinsetOn`, a theorem declared in [MathlibExt/Data/Fintype/PiFinsetOn.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Data/Fintype/PiFinsetOn.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/functions-with-prescribed-values/index.html#card-pi-finset-on).

## Product of sums over default-padded tuples

Distribute a product of finite sums over the default-padded tuples of choices.

Formalized by `Fintype.sum_piFinsetOn_prod`, a theorem declared in [MathlibExt/Data/Fintype/PiFinsetOn.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Data/Fintype/PiFinsetOn.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/functions-with-prescribed-values/index.html#sum-pi-finset-on-prod).

## Products of factorized functions over label tuples

Products of factorized functions factor through the tuples of their labels.

Formalized by `Fintype.prod_sum_eq_sum_piFinsetOn_mul`, a theorem declared in [MathlibExt/Data/Fintype/PiFinsetOn.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Data/Fintype/PiFinsetOn.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/functions-with-prescribed-values/index.html#prod-sum-eq-sum-pi-finset-on-mul).

## Unique default completion of active coordinates

Prescribed active coordinates have exactly one completion with the chosen default.

Formalized by `Fintype.existsUnique_piFinsetOn`, a theorem declared in [MathlibExt/Data/Fintype/PiFinsetOn.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Data/Fintype/PiFinsetOn.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/functions-with-prescribed-values/index.html#exists-unique-pi-finset-on).

## Number of dependent functions with prescribed values

The number of dependent functions in `piFinset s` with prescribed values on `S` is the
product of the numbers of choices outside `S`.

Formalized by `Fintype.card_filter_piFinset_eqOn_of_mem`, a theorem declared in [MathlibExt/Data/Fintype/PrescribedFunctions.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Data/Fintype/PrescribedFunctions.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/functions-with-prescribed-values/index.html#card-filter-pi-finset-eq-on-of-mem).

## Number of functions agreeing with a given one on a set

The number of functions agreeing with `f` on `S` is the number of unrestricted choices on
the remaining coordinates.

Formalized by `Fintype.card_filter_univ_eqOn`, a theorem declared in [MathlibExt/Data/Fintype/PrescribedFunctions.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Data/Fintype/PrescribedFunctions.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/functions-with-prescribed-values/index.html#card-filter-univ-eq-on).

## Division-free count of functions with prescribed values

Division-free count of finite functions with prescribed values on a set of coordinates.

Formalized by `Fintype.card_filter_univ_eqOn_mul_pow_card`, a theorem declared in [MathlibExt/Data/Fintype/PrescribedFunctions.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Data/Fintype/PrescribedFunctions.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/functions-with-prescribed-values/index.html#card-filter-univ-eq-on-mul-pow-card).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Functions with prescribed values](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/functions-with-prescribed-values/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/elementary-enumeration/functions-with-prescribed-values)
