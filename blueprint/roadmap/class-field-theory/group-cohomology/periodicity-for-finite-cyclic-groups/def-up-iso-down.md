---
declaration: definition
origin: cited
lean: Representation.map₁, Representation.map₁_ker, Representation.map₂_range, Rep.upIsoDown
statement: formalized
---

# up iso down

We have a commutative square with vertical isomorphisms:

$$
\begin{matrix}
\mathrm{ind}_1'(M) & \stackrel{\mathrm{map}_2}\to & \mathrm{ind}_1'(M) \\
\downarrow && \downarrow \\
\mathrm{coind}_1'(M) & \stackrel{\mathrm{map}_1}\to & \mathrm{coind}_1'(M) \\
\end{matrix}.
$$

It follows that $\mathrm{im}(\mathrm{map}_1) \cong \mathrm{im}(\mathrm{map}_2)$, i.e.

$$
\mathrm{up}(M) \cong \mathrm{down}(M).
$$

This is an isomorphism of functors; i.e. for each map $f : M \to N$ in $\mathbf{Rep}(R,G)$ we have a commuting square:

$$
\begin{matrix}
\mathrm{up}(M) & \stackrel{\mathrm{up}(f)}\to & \mathrm{up}(N) \\[2mm]
\downarrow && \downarrow \\
\mathrm{down}(M) & \stackrel{\mathrm{down}(f)}\to & \mathrm{down}(N)
\end{matrix}.
$$

## Depends on

- [up](../dimension-shifting/def-up.md)
- [down](../dimension-shifting/def-down.md)
- [map2 image](lem-map2-image.md)

## Lean

Formalized as [`Representation.map₁`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Representation.map₁), [`Representation.map₁_ker`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Representation.map₁_ker), [`Representation.map₂_range`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Representation.map₂_range), [`Rep.upIsoDown`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.upIsoDown).

## Sources

- [Class field theory blueprint: _2_cohomology.tex, line 1557](https://github.com/kbuzzard/ClassFieldTheory/blob/629ae9ed781748980bb51ab6f5f338ad9d6db3e8/blueprint/src/_2_cohomology.tex#L1557)
