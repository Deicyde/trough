# Facts from Fourier analysis

Recall the definition of a Fourier transform.

- [Fourier-Transform](def-fourier-transform.md)

The following computational result will be of use later on.

Of great interest to us will be a specific family of functions, known as Schwartz Functions. The Fourier transform behaves particularly well when acting on Schwartz functions. We elaborate in the following subsections.

## On Schwartz Functions

- [Schwartz-Space](def-schwartz-space.md)
- [Fourier-transform-is-automorphism](lemma-fourier-transform-is-automorphism.md)

## Radial Functions and Fourier Eigenfunctions

The functions we construct in Section [Fourier eigenfunctions with double zeroes at lattice points](../fourier-eigenfunctions-with-double-zeroes-at-lat/README.md) will be *radial*, and we record here the elementary facts about radial Schwartz functions that drive that construction.

- [fourier-involution](lemma-fourier-involution.md)
- [radial-fourier-inversion](lemma-radial-fourier-inversion.md)

Lemma [radial-fourier-inversion](lemma-radial-fourier-inversion.md) says that $\mathcal{F}$ is an involution on radial Schwartz functions, so such functions decompose into eigenfunctions of $\mathcal{F}$ with eigenvalues $\pm 1$.

This decomposition reduces the construction of the magic function in Section [Proof of Theorem g](../proof-of-theorem-g/README.md) to the construction of one $+1$- and one $-1$-eigenfunction of $\mathcal{F}$, which is carried out in Section [Fourier eigenfunctions with double zeroes at lattice points](../fourier-eigenfunctions-with-double-zeroes-at-lat/README.md).

Another reason we are interested in Schwartz Functions is that they behave well under infinite sums. This will be useful to us when proving the Cohn-Elkies linear programming bound.

## On the Summability of Schwartz Functions

We begin by stating a general summability result over specific subsets of $\mathbb{R}^d$.

The decaying property of Schwartz functions means that they can be compared to the absolutely convergent power series above.

We end with a crucial result on Schwartz functions, the statement of which only makes sense because of the above result.

- [Poisson summation formula](thm-poisson-summation-formula.md)

While the Poisson Summation Formula over lattices can be stated in greater generality (and probably should be formalised as such in Mathlib due to the many applications it admits), we stick with Schwartz functions because that should be sufficient for our purposes.

## Radial Schwartz Functions from One-Dimensional Data

Later, we will use Theorem [Poisson summation formula](thm-poisson-summation-formula.md) to prove that certain functions $a(x)$ and $b(x)$, defined in Section [Fourier eigenfunctions with double zeroes at lattice points](../fourier-eigenfunctions-with-double-zeroes-at-lat/README.md), are eigenfunctions of the Fourier transform. To apply the theorem, we need to show that these functions are Schwartz. Both are of the form $x \mapsto f(\|x\|^2)$ for a function $f : \mathbb{R} \to \mathbb{C}$ given by contour integrals, so we want a criterion for Schwartzness of such compositions purely in terms of $f$. This subsection provides one.

The first ingredient is a composition theorem already in Mathlib.

- [schwartz-comp-normsq](lemma-schwartz-comp-normsq.md)

Lemma [schwartz-comp-normsq](lemma-schwartz-comp-normsq.md) is not directly applicable to the functions of Section [Fourier eigenfunctions with double zeroes at lattice points](../fourier-eigenfunctions-with-double-zeroes-at-lat/README.md): the one-dimensional integrals defining them are *not* Schwartz on all of $\mathbb{R}$ — they grow exponentially as $r \to -\infty$, and some of them are not even given by convergent integrals far to the left of the origin. However, only their behaviour on $[0, \infty)$ matters, since $\|x\|^2 \geq 0$. The remedy is to multiply by a smooth cutoff before composing.

Note that, being smooth and constant on both $(-\infty, -1]$ and $[0, \infty)$, the function $\Theta$ has all of its derivatives supported in the compact interval $[-1, 0]$; in particular $\Theta$ and all of its derivatives are (individually) bounded. Rescaling, for any $\theta < 0$ we obtain a smooth cutoff $\Theta_\theta(x) := \Theta\left(\frac{2x}{-\theta}\right)$ which vanishes for $x \leq \theta/2$, equals $1$ for $x \geq 0$, and transitions on $[\theta/2, 0]$; for $\theta = -2$ this is $\Theta$ itself.

In the formalisation, the Schwartz structures on $a$ and $b$ are built exactly this way: the one-dimensional integrals are multiplied by a smooth cutoff (with $\theta = -2$ for $a$ and $\theta = -1$ for $b$, matching the regions where the corresponding integrals converge; see Section [Fourier eigenfunctions with double zeroes at lattice points](../fourier-eigenfunctions-with-double-zeroes-at-lat/README.md)), and the resulting Schwartz functions on $\mathbb{R}$ are transported to $\mathbb{R}^8$ via Lemma [schwartz-comp-normsq](lemma-schwartz-comp-normsq.md). The cutoff is invisible after composing with $\|\cdot\|^2$, so the resulting Schwartz functions are *equal* to the radial functions defined in Section [Fourier eigenfunctions with double zeroes at lattice points](../fourier-eigenfunctions-with-double-zeroes-at-lat/README.md).
