---
declaration: lemma
origin: cited
lean: Representation.map₂_range
statement: formalized
proof: formalized
---

# map2 image

The image of $\mathrm{map}_2 : \mathrm{ind}_1'(M) \to \mathrm{ind}_1'(M)$ is precisely the set of functions $G \to_0 M$ which sum to zero. This is the kernel of the map $\mathrm{ind}_1'(M) \to M$, which we are calling $\mathrm{down}(M)$.

## Depends on

- [ind'](../dimension-shifting/def-ind.md)

## Proof

It's clear that the values of $\mathrm{map}_2(f)$ sum to $0$, so the image of $\mathrm{map}_2$ is contained in the kernel. Conversely suppose $h : G \to_0 M$ satisfies $\sum_{i=0}^{n-1} h(\mathrm{gen}^i) = 0$. Then we have

$$
\begin{aligned}
h
& = \sum_{i=0}^{n-1} \mathrm{single}(\mathrm{gen}^i, h(\mathrm{gen}^i))\\
& = \sum_{i=0}^{n-1} (\mathrm{single}(\mathrm{gen}^i, h(\mathrm{gen}^i)) - \mathrm{single}(1, h(\mathrm{gen}^i))).
\end{aligned}
$$

Furthermore each of the terms $\mathrm{single}(\mathrm{gen}^i, m) - \mathrm{single}(1, m)$ is in the image of $\mathrm{map}_2$:

$$
\begin{aligned}
\mathrm{map}_2 (\mathrm{single}(1,m) + \cdots + \mathrm{single}(\mathrm{gen}^{i-1},m))
&=\mathrm{single}(1,m) - \mathrm{single}(\mathrm{gen}^i,m).
\end{aligned}
$$

## Lean

Formalized as [`Representation.map₂_range`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Representation.map₂_range).

## Sources

- [Class field theory blueprint: _2_cohomology.tex, line 1529](https://github.com/kbuzzard/ClassFieldTheory/blob/629ae9ed781748980bb51ab6f5f338ad9d6db3e8/blueprint/src/_2_cohomology.tex#L1529)
