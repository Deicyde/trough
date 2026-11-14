---
declaration: lemma
origin: cited
lean: groupCohomology.rest, groupCohomology.infl, groupCohomology.rest_δ_naturality, groupCohomology.infl_δ_naturality
statement: formalized
proof: formalized
---

# inflation restriction naturality

Let $S$ be a subgroup of $G$ and suppose we have a short exact sequence $0 \to A \to B \to C \to 0$ in $\mathbf{Rep}(R,G)$. Then the sequence the sequence $0 \to A \downarrow S \to B \downarrow S \to C \downarrow S \to 0$ is exact in $\mathbf{Rep}(R,S)$. The following diagram commutes, where the rows are the long exact sequences for $0 \to A \to B \to C \to 0$ and for its restriction to $S$, and the vertical maps are restriction.

$$
\begin{array}{ccccccc}
H^n(G,A) & \to & H^n(G,B) &\to &H^n(G,C)& \to& H^{n+1}(G,A)\\
\downarrow&&\downarrow&&\downarrow&&\downarrow \\
H^n(S,A) & \to & H^n(S,B) &\to &H^n(S,C)& \to& H^{n+1}(S,A)
\end{array}
$$

Suppose now that $S$ is a normal subgroup of $G$. Then we have for every map $f : A \to B$ in $\mathbf{Rep}(R,G)$ a commuting square in which the vertical maps are inflation.

$$
\begin{array}{ccccccc}
H^n(G/S,A^S) & \stackrel{H^n(\mathbf{invar}(f))}\to & H^n(G/S,B^S)\\
\downarrow&&\downarrow \\
H^n(G,A) & \stackrel{H^n(f)}\to & H^n(G,B)
\end{array}.
$$

If $0 \to A \to B \to C \to 0$ is exact in $\mathbf{Rep}(R,G)$ and its inflation $0 \to A^S \to B^S \to C^S \to 0$ is also exact in $Rep(R,G/S)$, then we have a commutative diagram in which the rows are the corresponding long exact sequences and the vertical maps are inflation:

$$
\begin{array}{ccccccc}
H^n(G/S,A^S) & \to & H^n(G/S,B^S) &\to &H^n(G/S,C^S)& \stackrel{\delta}\to& H^{n+1}(G/S,A^S)\\
\downarrow&&\downarrow&&\downarrow&&\downarrow \\
H^n(G,A) & \to & H^n(G,B) &\to &H^n(G,C)& \stackrel{\delta}\to& H^{n+1}(G,A)
\end{array}.
$$

## Depends on

- [restriction map](def-restriction-map.md)
- [inflation map](def-inflation-map.md)
- [cohomology long exact sequence](def-cohomology-long-exact-sequence.md)
- [inflation restriction functors](def-inflation-restriction-functors.md)

## Proof

Most of the commuting squares have already been proved if inflation and restriction are defined as morphisms of functors. The remaining two squares are:

$$
\begin{matrix}
H^n(G,C)& \stackrel{\delta}\to& H^{n+1}(G,A)\\
\mathrm{rest}\downarrow&&\downarrow\mathrm{rest} \\
H^n(S,C)& \stackrel{\delta} \to& H^{n+1}(S,A)
\end{matrix}
\qquad\textrm{ and }\qquad
\begin{matrix}
H^n(G/S,C^S)& \stackrel{\delta}\to& H^{n+1}(G/S,A^S)\\
\mathrm{infl}\downarrow&&\downarrow\mathrm{infl}\\
H^n(G,C)& \stackrel{\delta}\to& H^{n+1}(G,A)
\end{matrix} .
$$

Both of these can be deduced from the following statement in Mathlib:

> `HomologicalComplex.HomologySequence.$\delta$_naturality`

## Lean

Formalized as [`groupCohomology.rest`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/groupCohomology.rest), [`groupCohomology.infl`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/groupCohomology.infl), [`groupCohomology.rest_δ_naturality`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/groupCohomology.rest_δ_naturality), [`groupCohomology.infl_δ_naturality`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/groupCohomology.infl_δ_naturality).

## Sources

- [Class field theory blueprint: _2_cohomology.tex, line 244](https://github.com/kbuzzard/ClassFieldTheory/blob/629ae9ed781748980bb51ab6f5f338ad9d6db3e8/blueprint/src/_2_cohomology.tex#L244)
