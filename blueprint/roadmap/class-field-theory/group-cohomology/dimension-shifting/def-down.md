---
declaration: definition
origin: cited
lean: Representation.ind₁'_π, Representation.ind₁'_π_comm, Rep.ind₁'_π, Rep.instEpiAppInd₁'_π, Rep.dimensionShift.down, Rep.dimensionShift.downSES, Rep.dimensionShift.shortExact_downSES, Rep.dimensionShift.shortExact_downSES_res
statement: formalized
---

# down

For any representation $M$, there is a surjective morphism $\mathrm{ind}_1'(M) \to M$, which takes a finitely supported function $f : G \to_0 M$ to the sum $\sum_{x \in G} f (x)$. We define $\mathrm{down}(M)$ to be the kernel of this map. There is therefore a short exact sequence

$$
0 \to \mathrm{down}(M) \to \mathrm{ind}_1'(M) \to M \to 0.
$$

Both $\mathrm{down}(M)$ and the short exact sequence are functors of $M$; in particular for every map $f : M \to N$ in $\mathbf{Rep}(R,G)$, we have a commutative diagram:

$$
\begin{matrix}
0 & \to & \mathrm{down}(M) &\to &\mathrm{ind}_1'(M)& \to& M & \to & 0 \\
&&\downarrow && \downarrow && \downarrow \\
0 & \to & \mathrm{down}(N) &\to &\mathrm{ind}_1'(N)& \to& N & \to & 0
\end{matrix} .
$$

## Depends on

- [ind'](def-ind.md)

## Lean

Formalized as [`Representation.ind₁'_π`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Representation.ind₁'_π), [`Representation.ind₁'_π_comm`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Representation.ind₁'_π_comm), [`Rep.ind₁'_π`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.ind₁'_π), [`Rep.instEpiAppInd₁'_π`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.instEpiAppInd₁'_π), [`Rep.dimensionShift.down`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.dimensionShift.down), [`Rep.dimensionShift.downSES`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.dimensionShift.downSES), [`Rep.dimensionShift.shortExact_downSES`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.dimensionShift.shortExact_downSES), [`Rep.dimensionShift.shortExact_downSES_res`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.dimensionShift.shortExact_downSES_res).

## Sources

- [Class field theory blueprint: _2_cohomology.tex, line 1135](https://github.com/kbuzzard/ClassFieldTheory/blob/629ae9ed781748980bb51ab6f5f338ad9d6db3e8/blueprint/src/_2_cohomology.tex#L1135)
