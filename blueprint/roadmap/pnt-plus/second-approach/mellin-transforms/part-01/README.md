---
navigation: transparent
---

# PartialIntegration to Smooth1ContinuousAt

- [PartialIntegration](partialintegration.md)

In this section, we define the Mellin transform (already in Mathlib, thanks to David Loeffler), prove its inversion formula, and derive a number of important properties of some special functions and bumpfunctions.

Def: (Already in Mathlib) Let $f$ be a function from $\mathbb{R}_{>0}$ to $\mathbb{C}$. We define the Mellin transform of $f$ to be the function $\mathcal{M}(f)$ from $\mathbb{C}$ to $\mathbb{C}$ defined by

$$
\mathcal{M}(f)(s) = \int_0^\infty f(x)x^{s-1}dx.
$$

[Note: My preferred way to think about this is that we are integrating over the multiplicative group $\mathbb{R}_{>0}$, multiplying by a (not necessarily unitary!) character $|\cdot|^s$, and integrating with respect to the invariant Haar measure $dx/x$. This is very useful in the kinds of calculations carried out below. But may be more difficult to formalize as things now stand. So we might have clunkier calculations, which “magically” turn out just right - of course they're explained by the aforementioned structure...]

Finally, we need Mellin Convolutions and properties thereof.

- [MellinConvolution](mellinconvolution.md)

Let us start with a simple property of the Mellin convolution.

- [MellinConvolutionSymmetric](mellinconvolutionsymmetric.md)

The Mellin transform of a convolution is the product of the Mellin transforms.

- [MellinConvolutionTransform](mellinconvolutiontransform.md)

The $\nu$ function has Mellin transform $\mathcal{M}(\nu)(s)$ which is entire and decays (at least) like $1/|s|$.

[Of course it decays faster than any power of $|s|$, but it turns out that we will just need one power.]

- [MellinOfPsi](mellinofpsi.md)

We can make a delta spike out of this bumpfunction, as follows.

- [DeltaSpike](deltaspike.md)

This spike still has mass one:

- [DeltaSpikeMass](deltaspikemass.md)

The Mellin transform of the delta spike is easy to compute.

- [MellinOfDeltaSpike](mellinofdeltaspike.md)

In particular, for $s=1$, we have that the Mellin transform of $\nu_\epsilon$ is $1+O(\epsilon)$.

- [MellinOfDeltaSpikeAt1](mellinofdeltaspikeat1.md)
- [MellinOfDeltaSpikeAt1-asymp](mellinofdeltaspikeat1-asymp.md)

Let $1_{(0,1]}$ be the function from $\mathbb{R}_{>0}$ to $\mathbb{C}$ defined by

$$
1_{(0,1]}(x) = \begin{cases}
1 & \text{ if }x\leq 1\\
0 & \text{ if }x>1
\end{cases}.
$$

This has Mellin transform: [Note: this already exists in mathlib]

- [MellinOf1](mellinof1.md)

What will be essential for us is properties of the smooth version of $1_{(0,1]}$, obtained as the Mellin convolution of $1_{(0,1]}$ with $\nu_\epsilon$.

- [Smooth1](smooth1.md)

In particular, we have the following two properties.

- [Smooth1Properties-below](smooth1properties-below.md)
- [Smooth1Properties-above](smooth1properties-above.md)
- [Smooth1Nonneg](smooth1nonneg.md)
- [Smooth1LeOne](smooth1leone.md)

Combining the above, we have the following three Main Lemmata of this section on the Mellin transform of $\widetilde{1_{\epsilon}}$.

- [MellinOfSmooth1a](mellinofsmooth1a.md)
- [MellinOfSmooth1b](mellinofsmooth1b.md)
- [MellinOfSmooth1c](mellinofsmooth1c.md)
- [Smooth1ContinuousAt](smooth1continuousat.md)
