---
declaration: lemma
origin: cited
lean: close_smooth_approx_periodic
statement: formalized
proof: formalized
---

# smooth approximation

The function $f_0$ is $2\pi$-periodic. The function $f_0$ is smooth (and therefore measurable). The function $f_0$ satisfies for all $x\in {\mathbb{R}}$:

$$
|f(x)-f_0(x)|\le \epsilon' \, ,\qquad\text{(3)}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Periodicity follows directly from the definitions. The other properties are part of the Lean library.

## Lean

Formalized as [`close_smooth_approx_periodic`](https://fpvandoorn.github.io/carleson/docs/find/#doc/close_smooth_approx_periodic).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 8174](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L8174)
