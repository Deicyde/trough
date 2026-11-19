---
declaration: definition
origin: cited
lean: Combine.combine
statement: formalized
---

# combine

Given target degree $d^*\in\mathbb{N}$, shifting parameter $r\in\mathbb{F}$, functions $f_0,\ldots,f_{m-1}:\mathcal{L}\rightarrow\mathbb{F}$, and degrees $0\leq d_0,\ldots,d_{m-1}\leq {d}^*$, we define $\mathsf{Combine}(d^*,r,(f_0,d_0),\ldots,(f_{m-1},d_{m-1})):\mathcal{L}\rightarrow\mathbb{F}$ as follows:

$$
\begin{array}{rcl}
\mathsf{Combine}(d^*, r, (f_0, d_0), \ldots, (f_{m-1}, d_{m-1}))(x)
& := & \displaystyle\sum_{i=0}^{m-1} r_i \cdot f_i(x) \cdot \left( \sum_{l=0}^{d^* - d_i} (r \cdot x)^l \right) \\[10pt]
& = & \left\{
\begin{array}{ll}
\displaystyle\sum_{i=0}^{m-1} r_i \cdot f_i(x) \cdot \left( \dfrac{1 - (x r)^{d^* - d_i + 1}}{1 - x r} \right)
& \text{if } x \cdot r \neq 1 \\[8pt]
\displaystyle\sum_{i=0}^{m-1} r_i \cdot f_i(x) \cdot (d^* - d_i + 1)
& \text{if } x \cdot r = 1
\end{array}
\right.
\end{array}
$$

Above, $r_i:=r^{i+\sum_{j\lt i}(d^*-d_j)}$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`Combine.combine`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Combine.combine).

## Sources

- [ArkLib blueprint: proof_systems/stir.tex, line 210](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/stir.tex#L210)
