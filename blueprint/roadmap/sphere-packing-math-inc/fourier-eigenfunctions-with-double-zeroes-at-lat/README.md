# Fourier eigenfunctions with double zeroes at lattice points

In this section we construct two radial Schwartz functions $a,b:\mathbb{R}^8\to i\mathbb{R}$ such that

$$
\begin{aligned}\mathcal{F}(a)&=a\qquad\text{(1)}\\
\mathcal{F}(b)&=-b\qquad\text{(2)}\end{aligned}
$$

which double zeroes at all $\Lambda_8$-vectors of length greater than $\sqrt{2}$. Recall that each vector of $\Lambda_8$ has length $\sqrt{2n}$ for some $n\in\mathbb{N}_{\geq 0}$. We define $a$ and $b$ so that their values are purely imaginary because this simplifies some of our computations. We will show in Section [Proof of Theorem g](../proof-of-theorem-g/README.md) that an appropriate linear combination of functions $a$ and $b$ satisfies conditions [(5)](../cohn-elkies-linear-programming-bounds/thm-g.md)–[(7)](../cohn-elkies-linear-programming-bounds/thm-g.md).

Both of the functions will be defined via certain integrals of (quasi)modular forms. Then the eigenfunction property mainly follows from the Poisson summation formula (Theorem [Poisson summation formula](../facts-from-fourier-analysis/thm-poisson-summation-formula.md)) and the transformation laws of (quasi)modular forms. To apply Theorem [Poisson summation formula](../facts-from-fourier-analysis/thm-poisson-summation-formula.md), we will show that $a(x)$ and $b(x)$ are Schwartz functions, and this can be proved by verifying fast decay of the integrals.

First, we will define function $a$. To this end we consider the following functions:

## [phi4-phi2-phi0 to b-double-zeros](part-01/README.md)

- [phi4-phi2-phi0](part-01/def-phi4-phi2-phi0.md)
- [phi0-transform](part-01/lemma-phi0-transform.md)
- [a-definition](part-01/def-a-definition.md)
- [mod-div-disc-bound](part-01/lemma-mod-div-disc-bound.md)
- [phi0-bound](part-01/cor-phi0-bound.md)
- [phi2-bound](part-01/cor-phi2-bound.md)
- [phi4-bound](part-01/cor-phi4-bound.md)
- [a-schwartz](part-01/prop-a-schwartz.md)
- [a-fourier](part-01/prop-a-fourier.md)
- [a-double-zeros](part-01/prop-a-double-zeros.md)
- [a-another-integral](part-01/prop-a-another-integral.md)
- [a0](part-01/prop-a0.md)
- [ h](part-01/def-h.md)
- [psiI-psiT-psiS](part-01/def-psii-psit-psis.md)
- [psi-new](part-01/lemma-psi-new.md)
- [b-definition](part-01/def-b-definition.md)
- [psi-bound](part-01/lemma-psi-bound.md)
- [b-schwartz](part-01/prop-b-schwartz.md)
- [b-fourier](part-01/prop-b-fourier.md)
- [b-double-zeros](part-01/prop-b-double-zeros.md)

## [b-another-integral to b0](part-02/README.md)

- [b-another-integral](part-02/prop-b-another-integral.md)
- [b0](part-02/prop-b0.md)
