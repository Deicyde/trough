---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.KernelOperator.KernelSpace, MathlibExt.Analysis.FunctionalAnalysis.KernelOperator.KernelType, MathlibExt.Analysis.FunctionalAnalysis.KernelOperator.kernelExtend, MathlibExt.Analysis.FunctionalAnalysis.KernelOperator.kernelExtend_continuous, MathlibExt.Analysis.FunctionalAnalysis.KernelOperator.kernelExtend_apply_of_mem, MathlibExt.Analysis.FunctionalAnalysis.KernelOperator.norm_kernelExtend_le, MathlibExt.Analysis.FunctionalAnalysis.KernelOperator.kernelIntegrand, MathlibExt.Analysis.FunctionalAnalysis.KernelOperator.continuous_kernelIntegrand_uncurry
statement: formalized
proof: formalized
---

# Integral operators with continuous kernels

23 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/integral-operators-with-continuous-kernels/index.html).

## Continuous functions on the unit interval

$C([0, 1], \mathbb{R})$ denotes the space of
bounded continuous functions $[0, 1] \to \mathbb{R}$, with the supremum norm
$\|f\| = \sup_{x \in [0, 1]} |f(x)|$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.KernelOperator.KernelSpace`, an abbreviation declared in [MathlibExt/Analysis/FunctionalAnalysis/KernelOperator.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/KernelOperator.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/integral-operators-with-continuous-kernels/index.html#kernel-space).

## Continuous kernels on the unit square

A continuous kernel is a bounded continuous
function $k : [0, 1] \times [0, 1] \to \mathbb{R}$. These kernels form a normed space under the
supremum norm $\|k\| = \sup_{x, y \in [0, 1]} |k(x, y)|$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.KernelOperator.KernelType`, an abbreviation declared in [MathlibExt/Analysis/FunctionalAnalysis/KernelOperator.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/KernelOperator.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/integral-operators-with-continuous-kernels/index.html#kernel-type).

## Clamped extension

For a bounded continuous function $f$ on $[0, 1]$, its clamped extension
is the function $\tilde f : \mathbb{R} \to \mathbb{R}$ given by
$\tilde f(t) = f(\max(0, \min(1, t)))$. Thus $\tilde f(t) = f(0)$ for $t < 0$,
$\tilde f(t) = f(t)$ for $t \in [0, 1]$, and $\tilde f(t) = f(1)$ for $t > 1$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.KernelOperator.kernelExtend`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/KernelOperator.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/KernelOperator.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/integral-operators-with-continuous-kernels/index.html#kernel-extend).

## Continuity of the clamped extension

For every bounded continuous function $f$ on
$[0, 1]$, the clamped extension $t \mapsto f(\max(0, \min(1, t)))$ is continuous on $\mathbb{R}$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.KernelOperator.kernelExtend_continuous`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/KernelOperator.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/KernelOperator.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/integral-operators-with-continuous-kernels/index.html#kernel-extend-continuous).

## The clamped extension agrees with the function on $(0, 1)$

Let $f$ be a bounded continuous
function on $[0, 1]$ and let $\tilde f(s) = f(\max(0, \min(1, s)))$ for real $s$ be its clamped
extension. Then $\tilde f(t) = f(t)$ for every $t \in [0, 1]$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.KernelOperator.kernelExtend_apply_of_mem`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/KernelOperator.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/KernelOperator.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/integral-operators-with-continuous-kernels/index.html#kernel-extend-apply-of-mem).

## The clamped extension is bounded by the supremum norm

Let
$\pi(t) = \max(0, \min(1, t))$ be the projection of $\mathbb{R}$ onto $[0, 1]$. For every
$f \in C([0, 1], \mathbb{R})$ and every $t \in \mathbb{R}$, the clamped extension
$f \circ \pi$ of $f$ satisfies $|f(\pi(t))| \le \|f\|$, where $\|f\|$ is the supremum norm.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.KernelOperator.norm_kernelExtend_le`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/KernelOperator.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/KernelOperator.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/integral-operators-with-continuous-kernels/index.html#norm-kernel-extend-le).

## Kernel integrand

Let $\pi(t) = \max(0, \min(1, t))$ clamp a real number $t$ to $[0, 1]$.
For a continuous kernel $k$ on $[0, 1] \times [0, 1]$, a bounded continuous function $f$ on
$[0, 1]$ and a point $x \in [0, 1]$, the kernel integrand is the function
$\mathbb{R} \to \mathbb{R}$, $t \mapsto k(x, \pi(t)) \, f(\pi(t))$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.KernelOperator.kernelIntegrand`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/KernelOperator.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/KernelOperator.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/integral-operators-with-continuous-kernels/index.html#kernel-integrand).

## Joint continuity of the kernel integrand

Let $\pi(t) = \max(0, \min(1, t))$ clamp a
real number $t$ to $[0, 1]$. For every continuous kernel $k$ on $[0, 1] \times [0, 1]$ and every
bounded continuous function $f$ on $[0, 1]$, the kernel integrand
$(x, t) \mapsto k(x, \pi(t)) \, f(\pi(t))$ is jointly continuous on $[0, 1] \times \mathbb{R}$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.KernelOperator.continuous_kernelIntegrand_uncurry`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/KernelOperator.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/KernelOperator.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/integral-operators-with-continuous-kernels/index.html#continuous-kernel-integrand-uncurry).

## Continuity of the kernel integrand in $t$

Let $\pi(t) = \max(0, \min(1, t))$ clamp a real
number $t$ to $[0, 1]$. For every continuous kernel $k$ on $[0, 1] \times [0, 1]$, every bounded
continuous function $f$ on $[0, 1]$ and every $x \in [0, 1]$, the function
$t \mapsto k(x, \pi(t)) \, f(\pi(t))$ is continuous on $\mathbb{R}$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.KernelOperator.kernelIntegrand_continuous`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/KernelOperator.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/KernelOperator.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/integral-operators-with-continuous-kernels/index.html#kernel-integrand-continuous).

## Kernel value

Let $\pi(t) = \max(0, \min(1, t))$ be the projection of $\mathbb{R}$ onto
$[0, 1]$. For a continuous kernel $k$ on $[0, 1] \times [0, 1]$, a function
$f \in C([0, 1], \mathbb{R})$ and a point $x \in [0, 1]$, the kernel value is the real number

$$\int_0^1 k(x, \pi(t))\, f(\pi(t))\, dt.$$

Since $\pi(t) = t$ for $t \in [0, 1]$, it equals $\int_0^1 k(x, t)\, f(t)\, dt$, the value at
$x$ of the integral operator with kernel $k$ applied to $f$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.KernelOperator.kernelValue`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/KernelOperator.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/KernelOperator.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/integral-operators-with-continuous-kernels/index.html#kernel-value).

## Continuity of the kernel value

For every continuous kernel $k$ on
$[0, 1] \times [0, 1]$ and every $f \in C([0, 1], \mathbb{R})$, the kernel value of $k$ and
$f$, the function $x \mapsto \int_0^1 k(x, t)\, f(t)\, dt$ on $[0, 1]$, is continuous.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.KernelOperator.kernelValue_continuous`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/KernelOperator.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/KernelOperator.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/integral-operators-with-continuous-kernels/index.html#kernel-value-continuous).

## Pointwise bound for a kernel integral

Let $k$ be a continuous kernel on
$[0, 1] \times [0, 1]$ and let $f \in C([0, 1], \mathbb{R})$. For every $x \in [0, 1]$, the integral
$\int_0^1 k(x, t) \, f(t) \, dt$ has absolute value at most $\|k\|_\infty \, \|f\|_\infty$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.KernelOperator.norm_kernelValue_le`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/KernelOperator.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/KernelOperator.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/integral-operators-with-continuous-kernels/index.html#norm-kernel-value-le).

## The integral operator with continuous kernel, as a linear map

For a continuous kernel $k$
on $[0, 1] \times [0, 1]$, this is the $\mathbb{R}$-linear map $K$ from the space of bounded
continuous real functions on $[0, 1]$ to itself given by $(Kf)(x) = \int_0^1 k(x, t) f(t) \, dt$
for $x \in [0, 1]$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.KernelOperator.kernelLinearMap`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/KernelOperator.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/KernelOperator.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/integral-operators-with-continuous-kernels/index.html#kernel-linear-map).

## Sup-norm bound for the integral operator with continuous kernel

Write $\|\cdot\|$ for the
sup norm. For every continuous kernel $k$ on $[0, 1] \times [0, 1]$ and every bounded continuous
function $f$ on $[0, 1]$, the function $Kf$ given by $(Kf)(x) = \int_0^1 k(x, t) f(t) \, dt$
satisfies $\|Kf\| \le \|k\| \, \|f\|$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.KernelOperator.kernelLinearMap_norm_le`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/KernelOperator.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/KernelOperator.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/integral-operators-with-continuous-kernels/index.html#kernel-linear-map-norm-le).

## Integral operator with a continuous kernel

For a continuous kernel $k$ on
$[0, 1] \times [0, 1]$, the integral operator $T_k$ with kernel $k$ is the continuous linear
operator on $C([0, 1], \mathbb{R})$ given, for $f \in C([0, 1], \mathbb{R})$ and $x \in [0, 1]$, by
$(T_k f)(x) = \int_0^1 k(x, t)\, f(t)\, dt$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.KernelOperator.kernelOperator`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/KernelOperator.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/KernelOperator.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/integral-operators-with-continuous-kernels/index.html#kernel-operator).

## Evaluation formula for the integral operator

Let $\pi(t) = \max(0, \min(1, t))$ be the
projection of $\mathbb{R}$ onto $[0, 1]$. For a continuous kernel $k$ on $[0, 1] \times [0, 1]$,
write $T_k$ for the integral operator with kernel $k$ on $C([0, 1], \mathbb{R})$. For every
$f \in C([0, 1], \mathbb{R})$ and every $x \in [0, 1]$,

$$(T_k f)(x) = \int_0^1 k(x, \pi(t))\, f(\pi(t))\, dt,$$

the integral over $[0, 1]$ of the kernel integrand. Since $\pi(t) = t$ for $t \in [0, 1]$, this
is $\int_0^1 k(x, t)\, f(t)\, dt$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.KernelOperator.kernelOperator_apply`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/KernelOperator.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/KernelOperator.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/integral-operators-with-continuous-kernels/index.html#kernel-operator-apply).

## Norm bound for a kernel integral operator

For every continuous kernel $k$ on
$[0, 1] \times [0, 1]$, the integral operator $K$ with kernel $k$ on $C([0, 1], \mathbb{R})$ has
operator norm $\|K\| \le \|k\|_\infty$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.KernelOperator.norm_kernelOperator_le`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/KernelOperator.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/KernelOperator.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/integral-operators-with-continuous-kernels/index.html#norm-kernel-operator-le).

## Difference bound for the values of a kernel operator

Let $k$ be a continuous kernel on
$[0, 1] \times [0, 1]$, let $K$ be the integral operator with kernel $k$ on $C([0, 1], \mathbb{R})$,
let $f \in C([0, 1], \mathbb{R})$, and let $x, x' \in [0, 1]$ and $\delta \in \mathbb{R}$. If
$|k(x, y) - k(x', y)| \le \delta$ for every $y \in [0, 1]$, then
$|(Kf)(x) - (Kf)(x')| \le \delta \, \|f\|_\infty$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.KernelOperator.norm_kernelOperator_apply_sub_le`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/KernelOperator.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/KernelOperator.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/integral-operators-with-continuous-kernels/index.html#norm-kernel-operator-apply-sub-le).

## Integral operators with continuous kernels are compact

For every continuous kernel $k$ on
$[0, 1] \times [0, 1]$, the integral operator $K$ on the space of bounded continuous real functions
on $[0, 1]$, given by $(Kf)(x) = \int_0^1 k(x, t) f(t) \, dt$, is a compact operator.

The proof uses Arzelà–Ascoli: the image of the unit ball is equicontinuous by uniform continuity
of the kernel.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.KernelOperator.isCompactOperator_kernelOperator`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/KernelOperator.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/KernelOperator.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/integral-operators-with-continuous-kernels/index.html#is-compact-operator-kernel-operator).

## Separable kernels give finite-rank integral operators

Let $s$ be a finite set of indices
and, for $i \in s$, let $\varphi_i$ and $\psi_i$ be bounded continuous functions on $[0, 1]$. If a
continuous kernel $k$ on $[0, 1] \times [0, 1]$ satisfies
$k(x, y) = \sum_{i \in s} \varphi_i(x) \psi_i(y)$ for all $x, y \in [0, 1]$, then the range of the
integral operator $K$ on the space of bounded continuous real functions on $[0, 1]$, given by
$(Kf)(x) = \int_0^1 k(x, t) f(t) \, dt$, is a finite-dimensional real vector space.

The proof shows that the range lies in the span of the functions $\varphi_i$, $i \in s$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.KernelOperator.finiteDimensional_range_kernelOperator_of_separable`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/KernelOperator.lean, line 287](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/KernelOperator.lean#L287). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/integral-operators-with-continuous-kernels/index.html#finite-dimensional-range-kernel-operator).

## The integral operator is additive in the kernel

For a continuous kernel $k$ on
$[0, 1] \times [0, 1]$, write $T_k$ for the integral operator with kernel $k$ on
$C([0, 1], \mathbb{R})$. For all continuous kernels $k_1$ and $k_2$, the operator with the
pointwise sum kernel is the sum of the operators: $T_{k_1 + k_2} = T_{k_1} + T_{k_2}$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.KernelOperator.kernelOperator_add`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/KernelOperator.lean, line 344](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/KernelOperator.lean#L344). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/integral-operators-with-continuous-kernels/index.html#kernel-operator-add).

## The integral operator is homogeneous in the kernel

For a continuous kernel $k$ on
$[0, 1] \times [0, 1]$, write $T_k$ for the integral operator with kernel $k$ on
$C([0, 1], \mathbb{R})$. For every real number $c$ and every continuous kernel $k$,
$T_{c k} = c\, T_k$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.KernelOperator.kernelOperator_smul`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/KernelOperator.lean, line 361](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/KernelOperator.lean#L361). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/integral-operators-with-continuous-kernels/index.html#kernel-operator-smul).

## The zero kernel gives the zero operator

The integral operator on
$C([0, 1], \mathbb{R})$ whose kernel is the zero function on $[0, 1] \times [0, 1]$ is the
zero operator.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.KernelOperator.kernelOperator_zero`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/KernelOperator.lean, line 374](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/KernelOperator.lean#L374). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/integral-operators-with-continuous-kernels/index.html#kernel-operator-zero).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Integral operators with continuous kernels](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/integral-operators-with-continuous-kernels/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/operator-theory/integral-and-multiplication/integral-operators-with-continuous-kernels)
