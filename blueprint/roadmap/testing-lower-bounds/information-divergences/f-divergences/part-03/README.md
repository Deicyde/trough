---
navigation: transparent
---

# fDiv_statInfoFun_eq_statInfo to tv_eq_fDiv

- [fDiv_statInfoFun_eq_statInfo](cor-fdiv-statinfofun-eq-statinfo.md)
- [fDiv_phi_data_proc](lem-fdiv-phi-data-proc.md)
- [Data-processing](thm-fdiv-data-proc-2.md)

## Sigma-algebras

For $\mathcal A$ a sub-$\sigma$-algebra and $\mu$ a measure, we write $\mathcal \mu_{| \mathcal A}$ for the measure restricted to the $\sigma$-algebra. The measure $\mathcal \mu_{| \mathcal A}$ is equal to the map of $\mu$ by the identity, seen as a function to $\mathcal X$ with the $\sigma$-algebra $\mathcal A$. We can thus get a DPI for sub-sigma-algebras by using the DPI for maps.

- [fDiv_trim_le](thm-fdiv-trim-le.md)
- [fDiv_map_eq_fDiv_trim_of_ac](lem-fdiv-map-eq-fdiv-trim-of-ac.md)

## Consequences of the data-processing inequality

### Direct applications

- [fDiv_le_compProd_2](thm-fdiv-le-compprod-2.md)
- [fDiv_comp_le_compProd_2](thm-fdiv-comp-le-compprod-2.md)
- [Conditioning increases f-divergence](thm-fdiv-comp-le-condfdiv-2.md)
- [Marginals](thm-fdiv-fst-le-2.md)
- [fDiv_compProd_prod_eq](lem-fdiv-compprod-prod-eq.md)

### Data-processing and mean values

In this section $d_f(p, q)$ denotes the $f$-divergence between two Bernoulli distributions with means $p$ and $q$.

- [data_proc_event](cor-data-proc-event.md)

## Convexity

- [Joint convexity](thm-fdiv-convex.md)

## Variational representations

TODO

## Comparisons between divergences

We collate here general tools that can be used to compare $D_f$ and $D_g$ for two functions $f$ and $g$. Specific divergences are discussed in the next sections.

- [fDiv_mono_fun](lem-fdiv-mono-fun.md)

Remark: if $\mathcal X$ does not have two disjoint non-empty measurable sets then its measurable sets are only $\{\emptyset, \mathcal X\}$ and the ratio on the left is $0/0$.

Bretagnolle-Huber inequalities

- [bh_fDiv](thm-bh-fdiv.md)
- [Bretagnolle-Huber inequality](cor-bh-kl.md)

Joint range

TODO (Harremoës and Vajda 2011)

## Statistical divergences

- [statInfo_eq_fDiv](lem-statinfo-eq-fdiv.md)
- [tv_eq_fDiv](lem-tv-eq-fdiv.md)
