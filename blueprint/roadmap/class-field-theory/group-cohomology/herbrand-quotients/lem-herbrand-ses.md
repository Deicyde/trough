---
declaration: lemma
origin: cited
lean: Rep.herbrandQuotient_ne_zero_of_shortExact₁, Rep.herbrandQuotient_ne_zero_of_shortExact₂, Rep.herbrandQuotient_ne_zero_of_shortExact₃, Rep.herbrandQuotient_eq_of_shortExact
statement: formalized
proof: formalized
---

# herbrand ses

Suppose we have a short exact sequence of representations of a finite cyclic group $G$:

$$
0 \to A \to B \to C \to 0.
$$

If two of the representations $A$, $B$, $C$ have non-zero Herbrand quotient then so does the third, and $h(G,B) = h(G,A) \cdot h(G,C)$.

## Depends on

- [herbrand quotient](def-herbrand-quotient.md)

## Proof depends on

- [periodic cohomology](../periodicity-for-finite-cyclic-groups/cor-periodic-cohomology.md)

## Proof

It follows from the long exact sequence that if two of the representations $A,B,C$ have finite cohomology groups then so does the third. Also, by periodicity ([periodic cohomology](../periodicity-for-finite-cyclic-groups/cor-periodic-cohomology.md)), the long exact sequence reduces to an exact hexagon:

$$
\begin{matrix}
&& H^0_{\mathrm{Tate}}(G,B) \\
&\nearrow && \searrow \\
H^0_{\mathrm{Tate}}(G,A)  && && H^0_{\mathrm{Tate}}(G,C) \\
\uparrow & & & & \downarrow \\
H^1_{\mathrm{Tate}}(G,C) &&&& H^1_{\mathrm{Tate}}(G,A) \\
& \nwarrow && \swarrow\\
&& H^1_{\mathrm{Tate}}(G,B)
\end{matrix}.
$$

The result follows because the alternating product of the finite group orders in the hexagon is $1$.

## Lean

Formalized as [`Rep.herbrandQuotient_ne_zero_of_shortExact₁`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.herbrandQuotient_ne_zero_of_shortExact₁), [`Rep.herbrandQuotient_ne_zero_of_shortExact₂`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.herbrandQuotient_ne_zero_of_shortExact₂), [`Rep.herbrandQuotient_ne_zero_of_shortExact₃`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.herbrandQuotient_ne_zero_of_shortExact₃), [`Rep.herbrandQuotient_eq_of_shortExact`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.herbrandQuotient_eq_of_shortExact).

## Sources

- [Class field theory blueprint: _2_cohomology.tex, line 1736](https://github.com/kbuzzard/ClassFieldTheory/blob/629ae9ed781748980bb51ab6f5f338ad9d6db3e8/blueprint/src/_2_cohomology.tex#L1736)
