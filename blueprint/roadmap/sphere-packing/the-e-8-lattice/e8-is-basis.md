---
declaration: lemma
origin: cited
lean: span_E8Matrix_eq_top
statement: formalized
proof: formalized
---

# E8-is-basis

$B_8$ is a $\mathbb{R}$-basis of $\mathbb{R}^8$.

## Depends on

- [E8-Matrix](e8-matrix.md)

## Proof

It suffices to prove that $\mathcal{B}_8 \in \mathrm{GL}_8(\mathbb{R})$. We prove this by explicitly defining the inverse matrix $\mathcal{B}_8^{-1}$ and proving $\mathcal{B}_8 \mathcal{B}_8^{-1} = I_8$, which implies that $\det(\mathcal{B}_8)$ is nonzero. See the Lean code for more details.,

## Lean

Formalized as [`span_E8Matrix_eq_top`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/span_E8Matrix_eq_top).

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/E8-defs.tex, line 59](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/E8-defs.tex#L59)
