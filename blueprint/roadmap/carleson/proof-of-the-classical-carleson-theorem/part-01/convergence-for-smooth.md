---
declaration: lemma
origin: cited
lean: fourierConv_ofTwiceDifferentiable
statement: formalized
proof: formalized
---

# convergence for smooth

There exists some $N_0 \in {\mathbb{N}}$ such that for all $N>N_0$ and $x\in [0,2\pi]$ we have

$$
|S_N f_0 (x)- f_0(x)|\le \frac \epsilon 4\, .
$$

## Depends on

- [convergence-for-twice-contdiff](convergence-for-twice-contdiff.md)

## Proof

*Proof of convergence for smooth.* convergence for smooth now follows directly from the previous [Lemma convergence-for-twice-contdiff](convergence-for-twice-contdiff.md).

## Lean

Formalized as [`fourierConv_ofTwiceDifferentiable`](https://fpvandoorn.github.io/carleson/docs/find/#doc/fourierConv_ofTwiceDifferentiable).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 8192](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L8192)
