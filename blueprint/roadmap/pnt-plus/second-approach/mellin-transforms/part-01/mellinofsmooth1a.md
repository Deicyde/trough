---
declaration: lemma
origin: cited
lean: MellinOfSmooth1a
statement: formalized
proof: formalized
---

# MellinOfSmooth1a

Fix $\epsilon>0$. Then the Mellin transform of $\widetilde{1_{\epsilon}}$ is

$$
\mathcal{M}(\widetilde{1_{\epsilon}})(s) =
\frac{1}{s}\left(\mathcal{M}(\nu)\left(\epsilon s\right)\right).
$$

## Depends on

- [Smooth1](smooth1.md)

## Proof depends on

- [MellinOf1](mellinof1.md)
- [MellinOfDeltaSpike](mellinofdeltaspike.md)
- [DeltaSpike](deltaspike.md)
- [MellinConvolution](mellinconvolution.md)
- [MellinConvolutionTransform](mellinconvolutiontransform.md)
- [MellinConvolutionSymmetric](mellinconvolutionsymmetric.md)

## Proof

By Definition [Smooth1](smooth1.md),

$$
\mathcal M(\widetilde{1_\epsilon})(s)
=\mathcal M(1_{(0,1]}\ast\nu_\epsilon)(s)
.
$$

We wish to apply Theorem [MellinConvolutionTransform](mellinconvolutiontransform.md). To do so, we must prove that

$$
(x,y)\mapsto 1_{(0,1]}(y)\nu_\epsilon(x/y)/y
$$

is integrable on $[0,\infty)^2$. It is actually easier to do this for the convolution: $\nu_\epsilon\ast 1_{(0,1]}$, so we use Lemma [MellinConvolutionSymmetric](mellinconvolutionsymmetric.md): for $x\neq0$,

$$
1_{(0,1]}\ast\nu_\epsilon(x)=\nu_\epsilon\ast 1_{(0,1]}(x)
.
$$

Now, for $x=0$, both sides of the equation are 0, so the equation also holds for $x=0$. Therefore,

$$
\mathcal M(\widetilde{1_\epsilon})(s)
=\mathcal M(\nu_\epsilon\ast 1_{(0,1]})(s)
.
$$

Now,

$$
(x,y)\mapsto \nu_\epsilon(y)1_{(0,1]}(x/y)\frac{x^{s-1}}y
$$

has compact support that is bounded away from $y=0$ (specifically $y\in[2^{-\epsilon},2^\epsilon]$ and $x\in(0,y]$), so it is integrable. We can thus apply Theorem [MellinConvolutionTransform](mellinconvolutiontransform.md) and find

$$
\mathcal M(\widetilde{1_\epsilon})(s)
=\mathcal M(\nu_\epsilon)(s)\mathcal M(1_{(0,1]})(s)
.
$$

By Lemmas [MellinOf1](mellinof1.md) and [MellinOfDeltaSpike](mellinofdeltaspike.md),

$$
\mathcal M(\widetilde{1_\epsilon})(s)
=\frac1s\mathcal M(\nu)(\epsilon s)
.
$$

## Lean

Formalized as [`MellinOfSmooth1a`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/MellinOfSmooth1a).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/MellinCalculus.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/MellinCalculus.lean)
