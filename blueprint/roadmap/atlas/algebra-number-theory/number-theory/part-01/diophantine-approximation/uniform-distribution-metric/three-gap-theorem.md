---
declaration: section
origin: cited
lean: MetaMathlibExt.IsThreeGapPoint, MetaMathlibExt.IsThreeGapLength, MetaMathlibExt.three_gap
statement: formalized
proof: formalized
---

# Three-gap theorem

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/three-gap-theorem/index.html).

## Points of the three-gap configuration

Let $n$ be a natural number and $\alpha$ a real
number, and write $\operatorname{frac}(t) = t - \lfloor t \rfloor$ for the fractional part of a
real number $t$. A real number $x$ is a three-gap point of $n$ and $\alpha$ if
$x = \operatorname{frac}(k\alpha)$ for some natural number $k < n$.

Formalized by `MetaMathlibExt.IsThreeGapPoint`, a definition declared in [MathlibExt/NumberTheory/DiophantineApproximation/ThreeGap.lean, line 435](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/DiophantineApproximation/ThreeGap.lean#L435). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/three-gap-theorem/index.html#is-three-gap-point).

## Gap lengths of the three-gap configuration

Let $n$ be a natural number and $\alpha$ a real
number. In this definition a point means a three-gap point of $n$ and $\alpha$, that is, a number
$\operatorname{frac}(k\alpha) = k\alpha - \lfloor k\alpha \rfloor$ for a natural number $k < n$.
A real number $d$ is a gap length of $n$ and $\alpha$ if either $d = y - x$ for points $x < y$
with no point strictly between $x$ and $y$, or there are a least point $x_{\min}$ and a greatest
point $x_{\max}$ and $d = 1 + x_{\min} - x_{\max}$.

Formalized by `MetaMathlibExt.IsThreeGapLength`, a definition declared in [MathlibExt/NumberTheory/DiophantineApproximation/ThreeGap.lean, line 458](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/DiophantineApproximation/ThreeGap.lean#L458). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/three-gap-theorem/index.html#is-three-gap-length).

## Three-gap theorem

Let $n \ge 1$ be a natural number and $\alpha$ an irrational real
number. Consider the points $\operatorname{frac}(k\alpha) = k\alpha - \lfloor k\alpha \rfloor$ for
$0 \le k < n$ on the circle $[0, 1)$. The set of gap lengths of $n$ and $\alpha$, that is, the
lengths of the gaps between cyclically consecutive points, including the gap that wraps around
from the greatest point to the least, is finite and has at most three elements. If it has exactly
three elements, the largest of them is the sum of the other two.

Proof: We formalize the standard successor argument of Sós (1958) and Świerczkowski (1959),
following Alessandri and Berthé, *Three distance theorems and combinatorics on words*, §2.

## Sources

- https://en.wikipedia.org/wiki/Three-gap_theorem.

Formalized by `MetaMathlibExt.three_gap`, a theorem declared in [MathlibExt/NumberTheory/DiophantineApproximation/ThreeGap.lean, line 610](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/DiophantineApproximation/ThreeGap.lean#L610). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/three-gap-theorem/index.html#three-gap).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Three-gap theorem](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/three-gap-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/three-gap-theorem)
