---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: groupCohomology.δ
---

# cohomology long exact sequence

Given a short exact sequence $0 \to A \stackrel{f}\to B \stackrel{g}\to C \to 0$ in $\mathbf{Rep}(R,G)$, the corresponding sequence of cochain complexes is exact: $0 \to C^n(G,A) \to C^n(G,B) \to C^n(G,C) \to 0$. This implies that there exist “connecting homomorphisms” $\delta : H^n(G,C) \to H^{n+1}(G,A)$, such that the following is a long exact sequence:

$$
0 \to H^0(G,A) \stackrel{H^0(f)}\to H^0(G,B) \stackrel{H^0(g)}\to H^0(G,C) \stackrel{\delta}\to
H^1(G,A) \stackrel{H^1(f)}\to H^1(G,B) \stackrel{H^1(g)} \to H^1(G,C) \stackrel{\delta}\to \cdots.
$$

## Depends on

- [cochainsFunctor exact](lem-cochainsfunctor-exact.md)

## Lean

Formalized as [`groupCohomology.δ`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/groupCohomology.δ).

## Sources

- [Class field theory blueprint: _2_cohomology.tex, line 227](https://github.com/kbuzzard/ClassFieldTheory/blob/629ae9ed781748980bb51ab6f5f338ad9d6db3e8/blueprint/src/_2_cohomology.tex#L227)
