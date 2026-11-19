---
declaration: lemma
origin: cited
lean: MeasureTheory.Capacity.compFst
statement: formalized
proof: formalized
---

# Capacity.compFst_aux

Let $F$ be a set of sets of $\mathcal{X}$ and let $I$ be an $F$-capacity. Suppose that $\emptyset \in F$ and $F$ is closed under pairwise unions. Let $K$ be a compact system of $\mathcal{K}$. Let $\pi_{\mathcal{X}} : \mathcal{X} \times \mathcal{K} \to \mathcal{X}$ be the projection on the first coordinate. Then the function $I_{\mathcal{X}}(u) = I(\pi_{\mathcal{X}}(u))$ is a capacity for $(F \times K)^{\cup f}$.

## Depends on

- [Capacity](def-capacity.md)
- [IsCompactSystem](../part-01/def-iscompactsystem.md)

## Proof depends on

- [fst_iInter_of_supClosure_image2_prod_of_antitone](../part-01/thm-fst-iinter-of-supclosure-image2-prod-of-anti.md)

## Lean

Formalized as [`MeasureTheory.Capacity.compFst`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Capacity.compFst).

## Sources

- [Brownian motion blueprint: chapters/debut.tex, line 495](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/debut.tex#L495)
