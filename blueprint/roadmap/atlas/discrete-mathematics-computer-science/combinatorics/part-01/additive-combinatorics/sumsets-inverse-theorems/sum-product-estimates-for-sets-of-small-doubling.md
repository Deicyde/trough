---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.ErdosProblem818Wanted.conjecture, MathlibExt.NumberTheory.ErdosProblem818Wanted.conjecture_holds
statement: formalized
---

# Sum-product estimates for sets of small doubling

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sum-product-estimates-for-sets-of-small-doubling/index.html).

## Erdős Problem 818

The statement that for every real $K > 0$ there are reals $C > 0$ and
$c > 0$ such that every finite set $A$ of integers with $|A| \ge 2$ and $|A + A| \le K|A|$
satisfies $c|A|^2 / (\log |A|)^C \le |A \cdot A|$. Here $A + A = \{a + b : a, b \in A\}$,
$A \cdot A = \{ab : a, b \in A\}$ and $\log$ is the natural logarithm.

Formalized by `MathlibExt.NumberTheory.ErdosProblem818Wanted.conjecture`, a definition declared in [WantedExt/NumberTheory/ErdosProblem818Wanted.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosProblem818Wanted.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sum-product-estimates-for-sets-of-small-doubling/index.html#conjecture).

## Erdős Problem 818 is true

For every real $K > 0$ there are reals $C > 0$ and $c > 0$ such
that every finite set $A$ of integers with $|A| \ge 2$ and $|A + A| \le K|A|$ satisfies
$c|A|^2 / (\log |A|)^C \le |A \cdot A|$. Here $A + A = \{a + b : a, b \in A\}$,
$A \cdot A = \{ab : a, b \in A\}$ and $\log$ is the natural logarithm.

József Solymosi proved a stronger bound, with a single logarithm in the denominator.

## Sources

- József Solymosi, Bounding multiplicative energy by the sumset, Advances in Mathematics 222 (2009), 402–408, https://doi.org/10.1016/j.aim.2009.04.006.

Stated but not proved: `MathlibExt.NumberTheory.ErdosProblem818Wanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosProblem818Wanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosProblem818Wanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sum-product-estimates-for-sets-of-small-doubling/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sum-product estimates for sets of small doubling](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sum-product-estimates-for-sets-of-small-doubling/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sum-product-estimates-for-sets-of-small-doubling)
