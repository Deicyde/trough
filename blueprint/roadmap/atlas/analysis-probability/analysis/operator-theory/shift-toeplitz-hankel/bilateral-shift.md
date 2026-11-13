---
declaration: section
origin: cited
lean: MathlibExt.Analysis.InnerProductSpace.BilateralShiftOperator.bilateralShiftFun, MathlibExt.Analysis.InnerProductSpace.BilateralShiftOperator.bilateralBackwardFun, MathlibExt.Analysis.InnerProductSpace.BilateralShiftOperator.bilateralShiftLinMap, MathlibExt.Analysis.InnerProductSpace.BilateralShiftOperator.bilateralBackwardLinMap, MathlibExt.Analysis.InnerProductSpace.BilateralShiftOperator.bilateralShiftCLM, MathlibExt.Analysis.InnerProductSpace.BilateralShiftOperator.bilateralBackwardCLM, MathlibExt.Analysis.InnerProductSpace.BilateralShiftSpectrum.mul_star_eq_one_of_norm_eq_one, MathlibExt.Analysis.InnerProductSpace.BilateralShiftSpectrum.star_ne_zero_of_norm_eq_one
statement: formalized
proof: formalized
---

# Bilateral shift

18 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/bilateral-shift/index.html).

## Bilateral shift of a sequence

For a function $x : \mathbb{Z} \to K$ with values in any
set $K$, the bilateral (forward) shift of $x$ is the function $Sx : \mathbb{Z} \to K$ given by
$(Sx)(n) = x(n - 1)$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BilateralShiftOperator.bilateralShiftFun`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/BilateralShiftOperator.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/BilateralShiftOperator.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/bilateral-shift/index.html#bilateral-shift-fun).

## Bilateral backward shift of a sequence

For a function $x : \mathbb{Z} \to K$ with values
in any set $K$, the bilateral backward shift of $x$ is the function $Bx : \mathbb{Z} \to K$
given by $(Bx)(n) = x(n + 1)$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BilateralShiftOperator.bilateralBackwardFun`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/BilateralShiftOperator.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/BilateralShiftOperator.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/bilateral-shift/index.html#bilateral-backward-fun).

## Bilateral shift as a linear map

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$ and let
$\ell^2(\mathbb{Z}, \mathbb{K})$ be the space of square-summable functions
$\mathbb{Z} \to \mathbb{K}$. The bilateral shift is the $\mathbb{K}$-linear map
$S : \ell^2(\mathbb{Z}, \mathbb{K}) \to \ell^2(\mathbb{Z}, \mathbb{K})$ given by
$(Sx)(n) = x(n - 1)$ for all $n \in \mathbb{Z}$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BilateralShiftOperator.bilateralShiftLinMap`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/BilateralShiftOperator.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/BilateralShiftOperator.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/bilateral-shift/index.html#bilateral-shift-lin-map).

## Bilateral backward shift as a linear map

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$
and let $\ell^2(\mathbb{Z}, \mathbb{K})$ be the space of square-summable functions
$\mathbb{Z} \to \mathbb{K}$. The bilateral backward shift is the $\mathbb{K}$-linear map
$B : \ell^2(\mathbb{Z}, \mathbb{K}) \to \ell^2(\mathbb{Z}, \mathbb{K})$ given by
$(Bx)(n) = x(n + 1)$ for all $n \in \mathbb{Z}$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BilateralShiftOperator.bilateralBackwardLinMap`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/BilateralShiftOperator.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/BilateralShiftOperator.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/bilateral-shift/index.html#bilateral-backward-lin-map).

## Bilateral shift operator

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$ and let
$\ell^2(\mathbb{Z}, \mathbb{K})$ be the Hilbert space of square-summable functions
$\mathbb{Z} \to \mathbb{K}$. The bilateral shift is the bounded $\mathbb{K}$-linear operator $S$
on $\ell^2(\mathbb{Z}, \mathbb{K})$ given by $(Sx)(n) = x(n - 1)$ for all $n \in \mathbb{Z}$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BilateralShiftOperator.bilateralShiftCLM`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/BilateralShiftOperator.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/BilateralShiftOperator.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/bilateral-shift/index.html#bilateral-shift-clm).

## Bilateral backward shift operator

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$ and
let $\ell^2(\mathbb{Z}, \mathbb{K})$ be the Hilbert space of square-summable functions
$\mathbb{Z} \to \mathbb{K}$. The bilateral backward shift is the bounded $\mathbb{K}$-linear
operator $B$ on $\ell^2(\mathbb{Z}, \mathbb{K})$ given by $(Bx)(n) = x(n + 1)$ for all
$n \in \mathbb{Z}$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BilateralShiftOperator.bilateralBackwardCLM`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/BilateralShiftOperator.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/BilateralShiftOperator.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/bilateral-shift/index.html#bilateral-backward-clm).

## A unit scalar times its conjugate is one

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$. If $\mu \in \mathbb{K}$ satisfies $|\mu| = 1$, then $\mu \bar{\mu} = 1$, where
$\bar{\mu}$ is the complex conjugate of $\mu$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BilateralShiftSpectrum.mul_star_eq_one_of_norm_eq_one`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/BilateralShiftSpectrum.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/BilateralShiftSpectrum.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/bilateral-shift/index.html#mul-star-eq-one-of-norm-eq-one).

## Conjugates of unimodular scalars are nonzero

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$. If $\mu \in \mathbb{K}$ satisfies $|\mu| = 1$, then its conjugate $\bar{\mu}$ is
nonzero.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BilateralShiftSpectrum.star_ne_zero_of_norm_eq_one`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/BilateralShiftSpectrum.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/BilateralShiftSpectrum.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/bilateral-shift/index.html#star-ne-zero-of-norm-eq-one).

## Multiplying a power of the conjugate by a unit scalar

Let $\mathbb{K}$ be $\mathbb{R}$
or $\mathbb{C}$, and write $\bar{\mu}$ for the complex conjugate of $\mu \in \mathbb{K}$. If
$|\mu| = 1$, then for every integer $n$, $\mu \bar{\mu}^{\,n} = \bar{\mu}^{\,n-1}$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BilateralShiftSpectrum.mul_star_zpow`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/BilateralShiftSpectrum.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/BilateralShiftSpectrum.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/bilateral-shift/index.html#mul-star-zpow).

## Truncated approximate eigenfunction of the bilateral shift

Let $\mathbb{K}$ be
$\mathbb{R}$ or $\mathbb{C}$, let $\mu \in \mathbb{K}$ and $N \in \mathbb{N}$, and write
$\bar{\mu}$ for the complex conjugate of $\mu$. This is the function
$f_{\mu,N} : \mathbb{Z} \to \mathbb{K}$ with $f_{\mu,N}(n) = \bar{\mu}^{\,n}$ for
$-N \le n \le N$ and $f_{\mu,N}(n) = 0$ otherwise (negative powers are inverses, with the
convention $0^{n} = 0$ for $n < 0$).

It is used for $\mu$ on the unit circle, where it gives approximate eigenvectors of the
bilateral shift.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BilateralShiftSpectrum.approxEigenFun`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/BilateralShiftSpectrum.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/BilateralShiftSpectrum.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/bilateral-shift/index.html#approx-eigen-fun).

## Truncated approximate eigenvector of the bilateral shift

Let $\mathbb{K}$ be
$\mathbb{R}$ or $\mathbb{C}$, let $\mu \in \mathbb{K}$ and $N \in \mathbb{N}$, and write
$\bar{\mu}$ for the complex conjugate of $\mu$. This is the vector
$v_{\mu,N} \in \ell^2(\mathbb{Z}, \mathbb{K})$ whose $n$-th coordinate is the truncated
approximate eigenfunction $f_{\mu,N}(n)$, that is, $\bar{\mu}^{\,n}$ for $-N \le n \le N$ and
$0$ otherwise; it lies in $\ell^2$ because it has finite support.

It is used for $\mu$ on the unit circle, where it is an approximate eigenvector of the
bilateral shift.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BilateralShiftSpectrum.approxEigenVec`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/BilateralShiftSpectrum.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/BilateralShiftSpectrum.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/bilateral-shift/index.html#approx-eigen-vec).

## Norm of the truncated approximate eigenvector

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$, let $\mu \in \mathbb{K}$ with $|\mu| = 1$, and let $N \in \mathbb{N}$. The
truncated approximate eigenvector $v_{\mu,N} \in \ell^2(\mathbb{Z}, \mathbb{K})$, whose $n$-th
coordinate is $\bar{\mu}^{\,n}$ for $-N \le n \le N$ and $0$ otherwise ($\bar{\mu}$ the complex
conjugate of $\mu$), satisfies $\|v_{\mu,N}\|^2 = 2N + 1$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BilateralShiftSpectrum.norm_sq_approxEigenVec`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/BilateralShiftSpectrum.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/BilateralShiftSpectrum.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/bilateral-shift/index.html#norm-sq-approx-eigen-vec).

## Applying $\mu I - T$ on $\ell^2(\mathbb{Z})$

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$, let $T$ be a bounded linear operator on $\ell^2(\mathbb{Z}, \mathbb{K})$, let
$\mu \in \mathbb{K}$, and let $\mu I$ be the image of $\mu$ under the algebra map from $\mathbb{K}$
to the bounded operators on $\ell^2(\mathbb{Z}, \mathbb{K})$, that is, $\mu$ times the identity.
Then for every $x \in \ell^2(\mathbb{Z}, \mathbb{K})$, $(\mu I - T)x = \mu x - Tx$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BilateralShiftSpectrum.algebraMap_sub_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/BilateralShiftSpectrum.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/BilateralShiftSpectrum.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/bilateral-shift/index.html#algebra-map-sub-apply).

## Coordinates of the residual of the truncated approximate eigenvector

Let $\mathbb{K}$ be
$\mathbb{R}$ or $\mathbb{C}$, let $S$ be the bilateral shift on $\ell^2(\mathbb{Z}, \mathbb{K})$,
and let $\mu \in \mathbb{K}$, $N \in \mathbb{N}$ and $n \in \mathbb{Z}$. Let $f_{\mu,N}$ be the
truncated approximate eigenfunction and $v_{\mu,N} \in \ell^2(\mathbb{Z}, \mathbb{K})$ the
corresponding truncated approximate eigenvector. Then the $n$-th coordinate of
$(\mu I - S)v_{\mu,N}$ is $\mu f_{\mu,N}(n) - f_{\mu,N}(n - 1)$, where $\mu I$ is $\mu$ times
the identity operator.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BilateralShiftSpectrum.residual_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/BilateralShiftSpectrum.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/BilateralShiftSpectrum.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/bilateral-shift/index.html#residual-apply).

## Residual of the truncated approximate eigenvector

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$, let $S$ be the bilateral shift on $\ell^2(\mathbb{Z}, \mathbb{K})$, let
$\mu \in \mathbb{K}$ with $|\mu| = 1$, and let $N \in \mathbb{N}$. The truncated approximate
eigenvector $v_{\mu,N}$ satisfies $\|(\mu I - S)v_{\mu,N}\|^2 = 2$, where $\mu I$ is $\mu$ times
the identity operator.

The only nonzero coordinates of $(\mu I - S)v_{\mu,N}$ are those at $n = -N$ and $n = N + 1$,
each of absolute value $1$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BilateralShiftSpectrum.norm_sq_residual_approxEigenVec`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/BilateralShiftSpectrum.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/BilateralShiftSpectrum.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/bilateral-shift/index.html#norm-sq-residual-approx-eigen-vec).

## Every point of the unit circle lies in the spectrum of the bilateral shift

Let
$\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$ and let $S$ be the bilateral shift on
$\ell^2(\mathbb{Z}, \mathbb{K})$. Every $\mu \in \mathbb{K}$ with $|\mu| = 1$ lies in the
spectrum of $S$ in the algebra of bounded operators on $\ell^2(\mathbb{Z}, \mathbb{K})$, that
is, $\mu I - S$ is not invertible there, where $\mu I$ is $\mu$ times the identity operator.

If $\mu I - S$ were invertible it would be bounded below, but the truncated approximate
eigenvectors $v_{\mu,N}$ satisfy $\|v_{\mu,N}\| = \sqrt{2N + 1}$ and
$\|(\mu I - S)v_{\mu,N}\| = \sqrt{2}$ for every $N \in \mathbb{N}$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BilateralShiftSpectrum.mem_spectrum_bilateralShiftCLM_of_norm_eq_one`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/BilateralShiftSpectrum.lean, line 258](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/BilateralShiftSpectrum.lean#L258). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/bilateral-shift/index.html#mem-spectrum-bilateral-shift-clm-of-norm).

## Spectrum of the bilateral shift

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$. The
spectrum of the bilateral shift, as a bounded operator on $\ell^2(\mathbb{Z}, \mathbb{K})$, is the
set of scalars $\mu \in \mathbb{K}$ with $|\mu| = 1$; for $\mathbb{K} = \mathbb{C}$ this is the
unit circle.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BilateralShiftSpectrum.spectrum_bilateralShiftCLM`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/BilateralShiftSpectrum.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/BilateralShiftSpectrum.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/bilateral-shift/index.html#spectrum-bilateral-shift-clm).

## Spectrum of the bilateral backward shift

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$ and let $B$ be the bilateral backward shift on $\ell^2(\mathbb{Z}, \mathbb{K})$.
The spectrum of $B$ in the algebra of bounded operators on $\ell^2(\mathbb{Z}, \mathbb{K})$ is
the unit circle $\{\mu \in \mathbb{K} : |\mu| = 1\}$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BilateralShiftSpectrum.spectrum_bilateralBackwardCLM`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/BilateralShiftSpectrum.lean, line 295](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/BilateralShiftSpectrum.lean#L295). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/bilateral-shift/index.html#spectrum-bilateral-backward-clm).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bilateral shift](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/bilateral-shift/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/bilateral-shift)
