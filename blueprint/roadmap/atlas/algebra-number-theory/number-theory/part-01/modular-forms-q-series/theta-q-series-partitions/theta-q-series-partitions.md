---
declaration: section
origin: cited
lean: MetaMathlibExt.QPochhammer.jacobi_cube_euler_product_hasSum
statement: formalized
proof: formalized
---

# Theta functions and q-series: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/index.html).

Jacobi and Ramanujan theta functions, q-Pochhammer symbols and Euler products, Rogers–Ramanujan and related continued fractions, mock theta functions, Lambert series and q-series identities.

## Jacobi's identity for the cube of Euler's product

For every complex number $q$ with
$|q| < 1$, the series $\sum_{n=0}^{\infty} (-1)^n (2n+1) q^{n(n+1)/2}$ converges
unconditionally to $(q;q)_\infty^3$, the cube of the infinite q-Pochhammer symbol
$(q;q)_\infty = \prod_{n=0}^{\infty} (1 - q^{n+1})$.

## Sources

- Robson da Silva and James A. Sellers, "Parity Considerations for the Mex-Related Partition Functions of Andrews and Newman", <https://cs.uwaterloo.ca/journals/JIS/VOL23/Sellers/sellers52.tex>, lines 150-161 (equation `Jacobi` of the lemma; Eq. (1.3.24) of Berndt).

Formalized by `MetaMathlibExt.QPochhammer.jacobi_cube_euler_product_hasSum`, a theorem declared in [MathlibExt/NumberTheory/ModularForms/JacobiTheta/JacobiCubeEulerProduct.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ModularForms/JacobiTheta/JacobiCubeEulerProduct.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/index.html#jacobi-cube-euler-product-has-sum).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Theta functions and q-series](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions)
