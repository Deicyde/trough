---
declaration: theorem
origin: cited
lean: IsCompactSystem.fst_image_iInter
statement: formalized
proof: formalized
---

# fst_iInter_of_supClosure_image2_prod_of_antitone

Let $S$ be a paving of $\mathcal{X}$ and $T$ be a compact system of $\mathcal{K}$. Let $(B_n)_{n \in \mathbb{N}}$ be a monotone decreasing sequence of sets in $(S \times T)^{\cup f}$. Let $\pi_{\mathcal{X}} : \mathcal{X} \times \mathcal{K} \to \mathcal{X}$ be the projection on $\mathcal{X}$. Then

$$
\begin{aligned}
\pi_{\mathcal{X}}\left(\bigcap_{n\in\mathbb{N}} B_n\right) = \bigcap_{n\in\mathbb{N}} \pi_{\mathcal{X}}(B_n).
\end{aligned}
$$

## Depends on

- [IsCompactSystem](def-iscompactsystem.md)
- [supClosure](def-supclosure.md)

## Proof depends on

- [IsCompactSystem.supClosure](lem-iscompactsystem-supclosure.md)

## Lean

Formalized as [`IsCompactSystem.fst_image_iInter`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/IsCompactSystem.fst_image_iInter).

## Sources

- [Brownian motion blueprint: chapters/debut.tex, line 202](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/debut.tex#L202)
