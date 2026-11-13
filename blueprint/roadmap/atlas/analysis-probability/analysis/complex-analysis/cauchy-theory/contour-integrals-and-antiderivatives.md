---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Complex.ContourIntegralWanted.contourIntegral_of_hasDerivAt, MathlibExt.Analysis.Complex.ContourIntegralWanted.norm_contourIntegral_le, MathlibExt.Analysis.Complex.InvNoAntiderivativeAnnulusWanted.not_exists_hasDerivAt_inv_on_annulus
statement: formalized
---

# Contour integrals and antiderivatives

3 results, 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/contour-integrals-and-antiderivatives/index.html).

## Fundamental theorem of contour integration

Let $U \subseteq \mathbb{C}$ be open and let
$F, f : \mathbb{C} \to \mathbb{C}$ be such that $F$ is complex-differentiable at every $z \in U$
with $F'(z) = f(z)$. Let $\gamma : [0, 1] \to \mathbb{C}$ be a path from $a$ to $b$ whose image
lies in $U$ and which is continuously differentiable on $[0, 1]$, with derivative $\gamma'$
(one-sided at the endpoints). If $t \mapsto f(\gamma(t))\,\gamma'(t)$ is integrable on $[0, 1]$,
then $\int_\gamma f(z)\,dz = F(b) - F(a)$, where
$\int_\gamma f(z)\,dz = \int_0^1 f(\gamma(t))\,\gamma'(t)\,dt$.

## Sources

- L. V. Ahlfors, Complex Analysis, 3rd ed., Ch. 4, §1.1 to §1.3 (line integrals).

Stated but not proved: `MathlibExt.Analysis.Complex.ContourIntegralWanted.contourIntegral_of_hasDerivAt` is written with `theorem_wanted` in [WantedExt/Analysis/Complex/ContourIntegralWanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Complex/ContourIntegralWanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/contour-integrals-and-antiderivatives/index.html#contour-integral-of-has-deriv-at).

## ML estimate for contour integrals

Let $f : \mathbb{C} \to \mathbb{C}$ and let
$\gamma : [0, 1] \to \mathbb{C}$ be a path from $a$ to $b$ which is continuously differentiable
on $[0, 1]$, with derivative $\gamma'$ (one-sided at the endpoints). Let $M$ and $L$ be real
numbers with $|f(\gamma(t))| \le M$ and $|\gamma'(t)| \le L$ for every $t \in [0, 1]$. If
$t \mapsto f(\gamma(t))\,\gamma'(t)$ is integrable on $[0, 1]$, then
$\left|\int_\gamma f(z)\,dz\right| \le ML$, where
$\int_\gamma f(z)\,dz = \int_0^1 f(\gamma(t))\,\gamma'(t)\,dt$.

The parameter interval has length one, so $L$ bounds the length of $\gamma$.

## Sources

- L. V. Ahlfors, Complex Analysis, 3rd ed., Ch. 4, §1.1 to §1.3 (line integrals).

Stated but not proved: `MathlibExt.Analysis.Complex.ContourIntegralWanted.norm_contourIntegral_le` is written with `theorem_wanted` in [WantedExt/Analysis/Complex/ContourIntegralWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Complex/ContourIntegralWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/contour-integrals-and-antiderivatives/index.html#norm-contour-integral-le).

## The reciprocal function has no antiderivative on an annulus

Let
$U = \{z \in \mathbb{C} : 1 < |z| < 2\}$. There is no function $F : \mathbb{C} \to \mathbb{C}$
that is complex differentiable at every $z \in U$ with $F'(z) = 1/z$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Functions of a complex variable; General properties of functions of one complex variable), problem `ma_proofbench_l1_67`.

Stated but not proved: `MathlibExt.Analysis.Complex.InvNoAntiderivativeAnnulusWanted.not_exists_hasDerivAt_inv_on_annulus` is written with `theorem_wanted` in [WantedExt/Analysis/Complex/InvNoAntiderivativeAnnulusWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Complex/InvNoAntiderivativeAnnulusWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/contour-integrals-and-antiderivatives/index.html#not-exists-has-deriv-at-inv-on-annulus).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Contour integrals and antiderivatives](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/contour-integrals-and-antiderivatives/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/complex-analysis/cauchy-theory/contour-integrals-and-antiderivatives)
