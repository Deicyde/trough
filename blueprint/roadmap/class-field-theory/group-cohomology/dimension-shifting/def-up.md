---
declaration: definition
origin: cited
lean: Representation.coind₁'_ι, Rep.coind₁'_ι, Rep.dimensionShift.up, Rep.dimensionShift.upShortComplex, Rep.dimensionShift.shortExact_upSES, Rep.dimensionShift.shortExact_upSES_res
statement: formalized
---

# up

There is an injective morphism $M \to \mathrm{coind}_1'(M)$ which takes a vector $m \in M$ to the constant function on $G$ with value $m$. We define a representation $\mathrm{up}(M)$ to be the cokernel of this map, so that we have a short exact sequence

$$
0 \to M \to \mathrm{coind}_1'(M) \to \mathrm{up}(M) \to 0.
$$

This construction is functorial in $M$; in particular for every $f : M_1 \to M_2$ in $\mathbf{Rep}(R,G)$, there is a commutative diagram

$$
\begin{matrix}
0 & \to & M_1 & \to & \mathrm{coind}_1'(M_1) & \to& \mathrm{up}(M_1) \to 0 \\
&&\downarrow &&\downarrow&&\downarrow \\
0 & \to & M_2 & \to & \mathrm{coind}_1'(M_2) & \to& \mathrm{up}(M_2) \to 0 \\
\end{matrix}.
$$

## Depends on

- [coind₁'](def-coind1.md)

## Lean

Formalized as [`Representation.coind₁'_ι`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Representation.coind₁'_ι), [`Rep.coind₁'_ι`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.coind₁'_ι), [`Rep.dimensionShift.up`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.dimensionShift.up), [`Rep.dimensionShift.upShortComplex`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.dimensionShift.upShortComplex), [`Rep.dimensionShift.shortExact_upSES`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.dimensionShift.shortExact_upSES), [`Rep.dimensionShift.shortExact_upSES_res`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.dimensionShift.shortExact_upSES_res).

## Sources

- [Class field theory blueprint: _2_cohomology.tex, line 993](https://github.com/kbuzzard/ClassFieldTheory/blob/629ae9ed781748980bb51ab6f5f338ad9d6db3e8/blueprint/src/_2_cohomology.tex#L993)
