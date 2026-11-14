---
declaration: theorem
origin: cited
lean: TouchingSimplices.zaks
statement: formalized
proof: formalized
---

# ch16theorem1

For every $d\ge 2$, there is a family of $2^d$ pairwise touching $d$-simplices in $\mathbb{R}^d$ together with a transversal line that hits the interior of every single one of them.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Start with four touching triangles in the plane with a common transversal. For the induction step, an affine transformation puts short segments inside all simplices into a half-square. Reflect the configuration in $x_1=x_2$, then form pyramids over the two configurations with apexes on opposite sides of $\mathbb{R}^d$. This doubles the number of simplices. A slightly tilted antidiagonal meets the interior of each pyramid.

## Lean

Formalized as [`TouchingSimplices.zaks`](https://mo271.github.io/FormalBook/docs/find/#doc/TouchingSimplices.zaks).

## Sources

- [Formal Book blueprint: chapter/chapter16.tex, line 10](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter16.tex#L10)
