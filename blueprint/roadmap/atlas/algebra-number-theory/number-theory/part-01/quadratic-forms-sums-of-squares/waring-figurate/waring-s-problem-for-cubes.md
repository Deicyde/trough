---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.WieferichNineCubesWanted.NumberTheory.IsSumOfCubes, MathlibExt.NumberTheory.WieferichNineCubesWanted.NumberTheory.wieferich_g_three
statement: formalized
---

# Waring's problem for cubes

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/waring-s-problem-for-cubes/index.html).

## Sum of $k$ cubes

A natural number $n$ is a sum of $k$ cubes if there are natural numbers
$x_1, \dots, x_k$ with $n = x_1^3 + \dots + x_k^3$.

Formalized by `MathlibExt.NumberTheory.WieferichNineCubesWanted.NumberTheory.IsSumOfCubes`, a definition declared in [WantedExt/NumberTheory/WieferichNineCubesWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/WieferichNineCubesWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/waring-s-problem-for-cubes/index.html#is-sum-of-cubes).

## Wieferich's nine cubes theorem

Every natural number is a sum of $9$ cubes of natural
numbers, and $9$ cannot be replaced by $8$: some natural number is not a sum of $8$ cubes of
natural numbers.

## Sources

- A. Wieferich, *Beweis des Satzes, daß sich eine jede ganze Zahl als Summe von höchstens neun positiven Kuben darstellen läßt*, Math. Ann. 66 (1909); A. Kempner, *Über das Waringsche Problem und einige Verallgemeinerungen*, Math. Ann. 72 (1912). Knill, *Some fundamental theorems in mathematics*, §76. Problem `wieferich_g_three` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.NumberTheory.WieferichNineCubesWanted.NumberTheory.wieferich_g_three` is written with `theorem_wanted` in [WantedExt/NumberTheory/WieferichNineCubesWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/WieferichNineCubesWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/waring-s-problem-for-cubes/index.html#wieferich-g-three).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Waring's problem for cubes](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/waring-s-problem-for-cubes/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/waring-s-problem-for-cubes)
