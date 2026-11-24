# Fourier eigenfunctions with double zeroes at lattice points

In this section we construct two radial Schwartz functions $a,b:\mathbb{R}^8\to i\mathbb{R}$ such that

$$
\begin{aligned}\mathcal{F}(a)&=a\qquad\text{(1)}\\
\mathcal{F}(b)&=-b\qquad\text{(2)}\end{aligned}
$$

with double zeroes at all $\Lambda_8$-vectors of length greater than $\sqrt{2}$. Recall that each vector of $\Lambda_8$ has length $\sqrt{2n}$ for some $n\in\mathbb{N}_{\geq 0}$. We define $a$ and $b$ so that their values are purely imaginary because this simplifies some of our computations. We will show in Section [Proof of Theorem g](../proof-of-theorem-g/README.md) that an appropriate linear combination of functions $a$ and $b$ satisfies conditions [Theorem g](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/cohn-elkies.tex#L53)–[Theorem g](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/cohn-elkies.tex#L53).

Both functions are defined as $x \mapsto f(\|x\|^2)$, where $f : \mathbb{R} \to \mathbb{C}$ is a sum of six contour integrals of (quasi)modular forms against the Gaussian $e^{\pi i r z}$. The programme of this section is as follows. Bounds on the relevant (quasi)modular forms (obtained from Lemma [mod-div-disc-bound](part-01/lemma-mod-div-disc-bound.md)) yield rapid decay of the integrals and their derivatives on $[0, \infty)$; smoothness on a neighbourhood of $[0,\infty)$ follows by differentiation under the integral sign; Schwartzness of $a$ and $b$ is then obtained from the smooth-cutoff criterion of Corollary [schwartz-of-nonneg-decay](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/fourier-analysis.tex#L187). The eigenfunction properties (1) and (2) follow from the Fourier transform of the Gaussian (Lemma [Gaussian-Fourier](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/fourier-analysis.tex#L15)) and the transformation laws of the integrands, and the double zeroes are exhibited by deforming contours.

## The Integrands for $a$

To define the function $a$, we consider the following functions:

## [phi4-phi2-phi0 to perm-J12](part-01/README.md)

- [phi4-phi2-phi0](part-01/def-phi4-phi2-phi0.md)
- [phi0-transform](part-01/lemma-phi0-transform.md)
- [a-definition](part-01/def-a-definition.md)
- [mod-div-disc-bound](part-01/lemma-mod-div-disc-bound.md)
- [bound-I1-I3-I5](part-01/lem-bound-i1-i3-i5.md)
- [bound-I2-I4-I6](part-01/lem-bound-i2-i4-i6.md)
- [a-schwartz](part-01/prop-a-schwartz.md)
- [perm-I12](part-01/lemma-perm-i12.md)
- [perm-I56](part-01/lemma-perm-i56.md)
- [perm-I-reverse](part-01/lemma-perm-i-reverse.md)
- [a-fourier](part-01/prop-a-fourier.md)
- [Cauchy–Goursat for unbounded rectangular contours](part-01/lem-cg-unbounded.md)
- [a0](part-01/prop-a0.md)
- [ h](part-01/def-h.md)
- [psiI-psiT-psiS](part-01/def-psii-psit-psis.md)
- [psi-explicit](part-01/lemma-psi-explicit.md)
- [psi-slash-relations](part-01/lemma-psi-slash-relations.md)
- [b-definition](part-01/def-b-definition.md)
- [b-schwartz](part-01/prop-b-schwartz.md)
- [perm-J12](part-01/lemma-perm-j12.md)

## [perm-J56 to b0](part-02/README.md)

- [perm-J56](part-02/lemma-perm-j56.md)
- [perm-J-reverse](part-02/lemma-perm-j-reverse.md)
- [b-fourier](part-02/prop-b-fourier.md)
- [b0](part-02/prop-b0.md)
