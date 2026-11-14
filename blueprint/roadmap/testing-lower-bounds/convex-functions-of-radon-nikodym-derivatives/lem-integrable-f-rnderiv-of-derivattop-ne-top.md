---
declaration: lemma
origin: cited
lean: MeasureTheory.integrable_f_rnDeriv_of_derivAtTop_ne_top
statement: formalized
proof: formalized
---

# integrable_f_rnDeriv_of_derivAtTop_ne_top

If $\mu$ and $\nu$ are two finite measures and $f'(\infty) < \infty$, then $x \mapsto f\left(\frac{d\mu}{d\nu}(x)\right)$ is $\nu$-integrable.

## Depends on

- [derivAtTop](def-derivattop.md)

## Proof

By convexity and $f(0) < \infty$, $f'(\infty)\lt \infty$, we can sandwich $f$ between two affine functions of $\frac{d\mu}{d\nu}$. Those functions are integrable since the measures are finite.

## Lean

Formalized as [`MeasureTheory.integrable_f_rnDeriv_of_derivAtTop_ne_top`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/MeasureTheory.integrable_f_rnDeriv_of_derivAtTop_ne_top).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/convex.tex, line 13](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/convex.tex#L13)
