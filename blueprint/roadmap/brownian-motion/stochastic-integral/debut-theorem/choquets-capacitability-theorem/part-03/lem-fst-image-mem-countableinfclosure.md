---
declaration: lemma
origin: cited
lean: MeasureTheory.fst_image_mem_countableInfClosure
statement: formalized
proof: formalized
---

# fst_image_mem_countableInfClosure

Suppose that $F$ contains the empty set and is closed under pairwise intersections and unions, and let $I$ be an $F$-capacity. Let $K$ be a compact system which is also closed under pairwise intersections. Let $s \in ((F \times K)^{\cup f})_\delta$. Then $\pi_{\mathcal{X}}(s) \in F_\delta$.

## Depends on

- [countableInfClosure](../part-01/def-countableinfclosure.md)
- [IsCompactSystem](../part-01/def-iscompactsystem.md)

## Proof depends on

- [fst_iInter_of_supClosure_image2_prod_of_antitone](../part-01/thm-fst-iinter-of-supclosure-image2-prod-of-anti.md)
- [InfClosed.mem_countableInfClosure_iff](../part-01/lem-infclosed-mem-countableinfclosure-iff.md)

## Lean

Formalized as [`MeasureTheory.fst_image_mem_countableInfClosure`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.fst_image_mem_countableInfClosure).

## Sources

- [Brownian motion blueprint: chapters/debut.tex, line 559](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/debut.tex#L559)
