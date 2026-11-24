---
declaration: proposition
origin: cited
lean: MagicFunction.FourierEigenfunctions.a
statement: formalized
---

# a-schwartz

$a(x)$ is a Schwartz function.

## Depends on

- [a-definition](def-a-definition.md)

## Proof depends on

- [bound-I1-I3-I5](lem-bound-i1-i3-i5.md)
- [bound-I2-I4-I6](lem-bound-i2-i4-i6.md)

## Proof

By Lemma [Ij-smooth](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/construct-a-b.tex#L280), $a_\mathrm{rad} = I_1 + \cdots + I_6$ is smooth on $(-2, \infty)$ and all its derivatives decay rapidly on $[0, \infty)$. Corollary [schwartz-of-nonneg-decay](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/fourier-analysis.tex#L187) (with $\theta = -2$) shows that $x \mapsto a_\mathrm{rad}(\|x\|^2) = a(x)$ is a Schwartz function on $\mathbb{R}^8$.

In the formalisation, this is implemented by realising each product $\Theta_{-2} \cdot I_j$ as a term of type $\mathcal{S}(\mathbb{R}, \mathbb{C})$, transporting it to $\mathcal{S}(\mathbb{R}^8, \mathbb{C})$ via Lemma [schwartz-comp-normsq](../../facts-from-fourier-analysis/lemma-schwartz-comp-normsq.md), and summing; since $\Theta_{-2} = 1$ on $[0, \infty)$, the resulting Schwartz function is equal to the function $a$ of Definition [a-definition](def-a-definition.md).

## Lean

Stated as [`MagicFunction.FourierEigenfunctions.a`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/MagicFunction.FourierEigenfunctions.a); the blueprint marks no proof of it as formalized.

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/construct-a-b.tex, line 291](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/construct-a-b.tex#L291)
