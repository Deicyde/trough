# Facts from Fourier analysis

Recall the definition of a Fourier transform.

- [Fourier-Transform](def-fourier-transform.md)

The following computational result will be of use later on.

Of great interest to us will be a specific family of functions, known as Schwartz Functions. The Fourier transform behaves particularly well when acting on Schwartz functions. We elaborate in the following subsections.

## On Schwartz Functions

- [Schwartz-Space](def-schwartz-space.md)
- [Fourier-transform-is-automorphism](lemma-fourier-transform-is-automorphism.md)

Another reason we are interested in Schwartz Functions is that they behave well under infinite sums. This will be useful to us when proving the Cohn-Elkies linear programming bound.

## On the Summability of Schwartz Functions

We begin by stating a general summability result over specific subsets of $\mathbb{R}^d$.

The decaying property of Schwartz functions means that they can be compared to the absolutely convergent power series above.

We end with a crucial result on Schwartz functions, the statement of which only makes sense because of the above result.

- [Poisson summation formula](thm-poisson-summation-formula.md)

While the Poisson Summation Formula over lattices can be stated in greater generality (and probably should be formalised as such in Mathlib due to the many applications it admits), we stick with Schwartz functions because that should be sufficient for our purposes.

Later, we will use Theorem [Poisson summation formula](thm-poisson-summation-formula.md) to prove that the certain functions $a(x)$ and $b(x)$ that will be defined later are eigenfunctions of the Fourier transform. To apply the theorem, we need to show that these functions are Schwartz functions. We will do so by verifying the following sufficient condition.
