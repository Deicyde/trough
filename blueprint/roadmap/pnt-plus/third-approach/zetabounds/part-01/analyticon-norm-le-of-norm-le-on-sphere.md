---
declaration: lemma
origin: cited
lean: AnalyticOn.norm_le_of_norm_le_on_sphere
statement: formalized
proof: formalized
---

# AnalyticOn.norm-le-of-norm-le-on-sphere

An application of the maximum modulus principle.

Let $r\leq R$. If $f$ is analytic on $\overline{\mathbb{D}_R}$ and $\|f(z)\|\leq C$ for all $z$ on the boundary of $\overline{\mathbb{D}_r}$, then $\|f(z)\|\leq C$ for all $z$ in $\overline{\mathbb{D}_r}$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

By the mean value theorem for holomorphic functions, we know that for any $z$ in $\overline{\mathbb{D}_r}$, one has

$$
f(z)=\frac{1}{2\pi}\int_0^{2\pi}f(z+re^{i\theta})\,d\theta.
$$

Thus,

$$
|f(z)|\leq\frac{1}{2\pi}\int_0^{2\pi}|f(z+re^{i\theta})|\,d\theta
\leq\max_{\theta\in[0,2\pi)}|f(z+re^{i\theta})|\leq C.
$$

## Lean

Formalized as [`AnalyticOn.norm_le_of_norm_le_on_sphere`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/AnalyticOn.norm_le_of_norm_le_on_sphere).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/StrongPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/StrongPNT.lean)
