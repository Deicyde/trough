---
declaration: lemma
origin: cited
lean: Combine.geometric_sum_units
statement: formalized
---

# geometric_sum

Let $\mathbb{F}$ be a field, $r\in\mathbb{F}^\times$ be a nonzero field element, $a\in\mathbb{N}$ be a natural number. Then

$$
\sum_{i=0}^{a} r^i :=
\left\{
\begin{array}{ll}
\displaystyle\left(\frac{1 - r^{a+1}}{1 - r}\right)
& \text{if } r \neq 1 \\[6pt]
a + 1
& \text{if } r = 1
\end{array}
\right.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Stated as [`Combine.geometric_sum_units`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Combine.geometric_sum_units); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/stir.tex, line 192](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/stir.tex#L192)
