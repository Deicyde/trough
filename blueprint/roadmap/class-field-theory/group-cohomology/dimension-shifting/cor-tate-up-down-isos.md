---
declaration: corollary
origin: cited
lean: groupCohomology.instIsIso_shortExact_upSES, groupCohomology.instIsIso_shortExact_downSES, groupCohomology.δUpIsoTate, groupCohomology.δDownIsoTate, groupCohomology.instIsIso_shortExact_upSES_res, groupCohomology.instIsIso_shortExact_downSES_res, groupCohomology.δUpResIsoTate, groupCohomology.δDownResIsoTate
statement: formalized
proof: formalized
---

# Tate up down isos

If the group $G$ is finite then for every subgroup $S$ of $G$ and every $n \in {\mathbb Z}$ we have isomorphisms

$$
H^n_{\mathrm{Tate}}(S, \mathrm{up}(M)) \cong H^{n+1}_{\mathrm{Tate}}(S,M),
\qquad
H^{n+1}_{\mathrm{Tate}}(S, \mathrm{down}(M)) \cong H^{n}_{\mathrm{Tate}}(S,M).
$$

## Depends on

- [up](def-up.md)
- [down](def-down.md)
- [induced' trivial Tate](lem-induced-trivial-tate.md)
- [Tate long exact sequence](../tate-cohomology/def-tate-long-exact-sequence.md)

## Proof

These are the connecting homomorphisms from the short exact sequences linking $\mathrm{up}(M)$ and $\mathrm{down}(M)$ to $M$. They are isomorphisms because $\mathrm{coind}_1'(M)$ and $\mathrm{ind}_1'(M)$ have trivial Tate cohomology.

## Lean

Formalized as [`groupCohomology.instIsIso_shortExact_upSES`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/groupCohomology.instIsIso_shortExact_upSES), [`groupCohomology.instIsIso_shortExact_downSES`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/groupCohomology.instIsIso_shortExact_downSES), [`groupCohomology.δUpIsoTate`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/groupCohomology.δUpIsoTate), [`groupCohomology.δDownIsoTate`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/groupCohomology.δDownIsoTate), [`groupCohomology.instIsIso_shortExact_upSES_res`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/groupCohomology.instIsIso_shortExact_upSES_res), [`groupCohomology.instIsIso_shortExact_downSES_res`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/groupCohomology.instIsIso_shortExact_downSES_res), [`groupCohomology.δUpResIsoTate`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/groupCohomology.δUpResIsoTate), [`groupCohomology.δDownResIsoTate`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/groupCohomology.δDownResIsoTate).

## Sources

- [Class field theory blueprint: _2_cohomology.tex, line 1208](https://github.com/kbuzzard/ClassFieldTheory/blob/629ae9ed781748980bb51ab6f5f338ad9d6db3e8/blueprint/src/_2_cohomology.tex#L1208)
