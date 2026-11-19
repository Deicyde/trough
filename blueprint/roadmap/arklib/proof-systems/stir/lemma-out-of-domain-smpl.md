---
declaration: lemma
origin: cited
lean: OutOfDomSmpl.out_of_dom_smpl_1, OutOfDomSmpl.out_of_dom_smpl_2
statement: formalized
---

# out_of_domain_smpl

Let $\mathbb{F}$ be a finite field and $\mathcal{L}\subseteq\mathbb{F}$ an evaluation domain with $|\mathcal{L}|<|\mathbb{F}|$, so that $\mathbb{F}\setminus\mathcal{L}$ is nonempty. Let $f:\mathcal{L}\rightarrow\mathbb{F}$ be a function, $d\in\mathbb{N}$ be a degree parameter, $s\in\mathbb{N}$ be a repetition parameter, $\delta\ge0$ be a distance parameter and $l\ge0$ a real list-size bound. If $\mathrm{RS}[\mathbb{F},\mathcal{L},d]$ is $(\delta,l)$-list decodable, then

$$
\begin{array}{rcl}
\Pr_{\substack{r_0, \ldots, r_{s-1} \gets \mathbb{F} \setminus \mathcal{L}}}
\left[
\begin{array}{c}
\exists \text{ distinct } u, u' \in \mathsf{List}(f, d, \delta): \\
\forall i \in [s],\ \hat{u}(r_i) = \hat{u}'(r_i)
\end{array}
\right]
& \leq & \frac{l\,(l-1)}{2} \cdot \left( \frac{d - 1}{|\mathbb{F}| - |\mathcal{L}|} \right)^s \\
& \leq & \left( \frac{l^2}{2} \right) \cdot \left( \frac{d}{|\mathbb{F}| - |\mathcal{L}|} \right)^s
\end{array}
$$

Here $l-1$ is truncated at $0$, and the $r_i$ are independent and uniform on $\mathbb{F}\setminus\mathcal{L}$.

## Depends on

- [Reed-Solomon Code](../../supporting-theories/coding-theory/def-reed-solomon-code.md)
- [List Decodability](../../supporting-theories/coding-theory/def-list-decodable.md)
- [List of Close Codewords](../../supporting-theories/coding-theory/def-list-close-codewords.md)

## Lean

Stated as [`OutOfDomSmpl.out_of_dom_smpl_1`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/OutOfDomSmpl.out_of_dom_smpl_1), [`OutOfDomSmpl.out_of_dom_smpl_2`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/OutOfDomSmpl.out_of_dom_smpl_2); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/stir.tex, line 102](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/stir.tex#L102)
