---
declaration: definition
origin: cited
lean: Combine.degCor
statement: formalized
---

# deg_corr

Given target degree $d^*\in\mathbb{N}$, shifting parameter $r\in\mathbb{F}$, function $f:\mathcal{L}\rightarrow\mathbb{F}$, and degree $0\leqd\leqd^*$, we define $\mathsf{DegCor}(d^*,r,f,d)$ as follows.

$$
\begin{array}{rcl}
\mathsf{DegCor}(d^*, r, f, d)(x)
& := & \displaystyle f(x) \cdot \left( \sum_{l=0}^{d^* - d} (r \cdot x)^l \right) \\[10pt]
& = & \left\{
\begin{array}{ll}
\displaystyle f(x) \cdot \left( \dfrac{1 - (x r)^{d^* - d + 1}}{1 - x r} \right)
& \text{if } x \cdot r \neq 1 \\[8pt]
\displaystyle f(x) \cdot (d^* - d + 1)
& \text{if } x \cdot r = 1
\end{array}
\right.
\end{array}
$$

(Observe that $\mathsf{DegCor}(d^*,r,f,d)=\mathsf{Combine}(d^*,r,(f,d))$.)

## Depends on

- [combine](def-combine.md)
- [Reed-Solomon Code](../../supporting-theories/coding-theory/def-reed-solomon-code.md)
- [Distance from a Code](../../supporting-theories/coding-theory/def-distance-from-code.md)

## Lean

Formalized as [`Combine.degCor`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Combine.degCor).

## Sources

- [ArkLib blueprint: proof_systems/stir.tex, line 232](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/stir.tex#L232)
