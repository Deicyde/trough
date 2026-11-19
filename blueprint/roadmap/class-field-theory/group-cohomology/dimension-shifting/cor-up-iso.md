---
declaration: corollary
origin: cited
lean: Rep.dimensionShift.δ_up_zero_epi, Rep.dimensionShift.δ_up_isIso, Rep.dimensionShift.δUpIso, Rep.dimensionShift.epi_δ_up_zero_res, Rep.dimensionShift.isIso_δ_up_res, Rep.dimensionShift.δUpResIso, Rep.dimensionShift.δUpNatIso
statement: formalized
proof: formalized
---

# up iso

Let $S$ be any subgroup of $G$ and let $n \ge 1$. Then the connecting map from the long exact sequence $H^{n}(S,\mathrm{up}(M)) \to H^{n+1}(S,M)$ is an isomorphism. The corresponding map $H^{0}(S,\mathrm{up}(M)) \to H^{1}(S,M)$ is surjective.

The isomorphism $H^{n}(S,\mathrm{up}(-)) \cong H^{n+1}(S,-)$ is an isomorphism of functors. This means that for every morphism $f : M \to N$ of representations, the following square commutes:

$$
\begin{matrix}
H^{n}(S,\mathrm{up}(M)) & \cong & H^{n+1}(S,M) \\
\downarrow && \downarrow \\
H^{n}(S,\mathrm{up}(N)) & \cong & H^{n+1}(S,N)
\end{matrix}.
$$

## Depends on

- [up](def-up.md)
- [coind₁' trivial cohomology](cor-coind1-trivial-cohomology.md)

## Proof

We have already shown in Corollary [coind₁' trivial cohomology](cor-coind1-trivial-cohomology.md) that $\mathrm{coind}_1'(M)$ has trivial cohomology, so $H^{r}(S,\mathrm{coind}_1'(M))=0$ for all $r>0$. This implies that the connecting maps are isomorphisms.

The commuting square follows from `HomologicalComplex.HomologySequence.$\delta$_naturality` because the short exact sequence $0 \to M \to \mathrm{coind}_1'(M) \to \mathrm{up}(M) \to 0$ is functorial in $M$.

## Lean

Formalized as [`Rep.dimensionShift.δ_up_zero_epi`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.dimensionShift.δ_up_zero_epi), [`Rep.dimensionShift.δ_up_isIso`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.dimensionShift.δ_up_isIso), [`Rep.dimensionShift.δUpIso`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.dimensionShift.δUpIso), [`Rep.dimensionShift.epi_δ_up_zero_res`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.dimensionShift.epi_δ_up_zero_res), [`Rep.dimensionShift.isIso_δ_up_res`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.dimensionShift.isIso_δ_up_res), [`Rep.dimensionShift.δUpResIso`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.dimensionShift.δUpResIso), [`Rep.dimensionShift.δUpNatIso`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.dimensionShift.δUpNatIso).

## Sources

- [Class field theory blueprint: _2_cohomology.tex, line 1021](https://github.com/kbuzzard/ClassFieldTheory/blob/629ae9ed781748980bb51ab6f5f338ad9d6db3e8/blueprint/src/_2_cohomology.tex#L1021)
