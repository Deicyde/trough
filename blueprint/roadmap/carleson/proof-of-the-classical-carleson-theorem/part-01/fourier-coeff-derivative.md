---
declaration: lemma
origin: cited
lean: fourierCoeffOn_of_hasDerivAt
statement: formalized
proof: formalized
---

# fourier-coeff-derivative

Let $f:{\mathbb{R}} \to {\mathbb{C}}$ be $2\pi$-periodic and continuously differentiable, and let $n \in {\mathbb{Z}} \setminus \{0\}$. Then

$$
\widehat{f}_n = \frac{1}{i n} \widehat{f'}_n.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

This is part of the Lean library.

## Lean

Formalized as [`fourierCoeffOn_of_hasDerivAt`](https://fpvandoorn.github.io/carleson/docs/find/#doc/fourierCoeffOn_of_hasDerivAt).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 8511](https://github.com/fpvandoorn/carleson/blob/f7487cc9da4d1e73f009dc0280cd5b958f3e2c78/blueprint/src/chapter/main.tex#L8511)
