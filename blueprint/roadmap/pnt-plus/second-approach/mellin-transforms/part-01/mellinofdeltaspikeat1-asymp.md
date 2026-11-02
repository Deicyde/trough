---
declaration: lemma
origin: cited
lean: MellinOfDeltaSpikeAt1_asymp
statement: formalized
proof: formalized
---

# MellinOfDeltaSpikeAt1-asymp

As $\epsilon\to 0$, we have

$$
\mathcal{M}(\nu_\epsilon)(1) = 1+O(\epsilon).
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

By Lemma [MellinOfDeltaSpikeAt1](mellinofdeltaspikeat1.md),

$$
\mathcal M(\nu_\epsilon)(1)=\mathcal M(\nu)(\epsilon)
$$

which by Definition MellinTransform is

$$
\mathcal M(\nu)(\epsilon)=\int_0^\infty\nu(x)x^{\epsilon-1}dx
.
$$

Since $\nu(x) x^{\epsilon-1}$ is integrable (because $\nu$ is continuous and compactly supported),

$$
\mathcal M(\nu)(\epsilon)-\int_0^\infty\nu(x)\frac{dx}x
=\int_0^\infty\nu(x)(x^{\epsilon-1}-x^{-1})dx
.
$$

By Taylor's theorem,

$$
x^{\epsilon-1}-x^{-1}=O(\epsilon)
$$

so, since $\nu$ is absolutely integrable,

$$
\mathcal M(\nu)(\epsilon)-\int_0^\infty\nu(x)\frac{dx}x=O(\epsilon)
.
$$

We conclude the proof using Theorem [SmoothExistence](../part-02/smoothexistence.md).

## Lean

Formalized as [`MellinOfDeltaSpikeAt1_asymp`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/MellinOfDeltaSpikeAt1_asymp).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/MellinCalculus.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/MellinCalculus.lean)
