---
declaration: theorem
origin: cited
lean: ZetaBoxEval
statement: formalized
proof: formalized
---

# ZetaBoxEval

For all $\epsilon > 0$ sufficiently close to $0$, the rectangle integral over $[1-\delta,2] \times_{ℂ} [-T,T]$ of the integrand in $\psi_{\epsilon}$ is

$$
\frac{X^{1}}{1}\mathcal{M}(\widetilde{1_{\epsilon}})(1)
= X(1+O(\epsilon))
,
$$

where the implicit constant is independent of $X$.

## Depends on

- [Smooth1](../../mellin-transforms/part-01/smooth1.md)

## Proof depends on

- [MellinOfSmooth1c](../../mellin-transforms/part-01/mellinofsmooth1c.md)

## Proof

Unfold the definitions and apply Lemma [MellinOfSmooth1c](../../mellin-transforms/part-01/mellinofsmooth1c.md).

## Lean

Formalized as [`ZetaBoxEval`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ZetaBoxEval).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/MediumPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/MediumPNT.lean)
