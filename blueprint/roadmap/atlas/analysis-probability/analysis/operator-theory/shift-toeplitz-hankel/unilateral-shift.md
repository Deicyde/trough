---
declaration: section
origin: cited
lean: MathlibExt.Analysis.InnerProductSpace.LpShiftOperator.shiftFun, MathlibExt.Analysis.InnerProductSpace.LpShiftOperator.backwardFun, MathlibExt.Analysis.InnerProductSpace.LpShiftOperator.memℓp_shiftFun, MathlibExt.Analysis.InnerProductSpace.LpShiftOperator.memℓp_backwardFun, MathlibExt.Analysis.InnerProductSpace.LpShiftOperator.shiftLinMap, MathlibExt.Analysis.InnerProductSpace.LpShiftOperator.backwardLinMap, MathlibExt.Analysis.InnerProductSpace.LpShiftOperator.shiftLinMap_apply, MathlibExt.Analysis.InnerProductSpace.LpShiftOperator.backwardLinMap_apply
statement: formalized
---

# Unilateral shift

108 results, 107 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html).

## Forward shift of a sequence

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$. The
forward shift of a sequence $x : \mathbb{N} \to \mathbb{K}$ is the sequence $S x$ with
$(S x)_0 = 0$ and $(S x)_{n+1} = x_n$ for every $n \in \mathbb{N}$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpShiftOperator.shiftFun`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#shift-fun).

## Backward shift of a sequence

For any type $K$, the backward shift of a sequence
$x \colon \mathbb{N} \to K$ is the sequence $n \mapsto x_{n+1}$: it drops the coordinate $x_0$
and shifts every other coordinate down by one.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpShiftOperator.backwardFun`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#backward-fun).

## The forward shift of a square-summable sequence is square-summable

Let $\mathbb{K}$ be
$\mathbb{R}$ or $\mathbb{C}$. For every square-summable sequence $x = (x_0, x_1, x_2, \dots)$ in
$\mathbb{K}$, the forward-shifted sequence $(0, x_0, x_1, \dots)$ is also square-summable, that is,
it belongs to $\ell^2(\mathbb{N}, \mathbb{K})$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpShiftOperator.memℓp_shiftFun`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#mem-p-shift-fun).

## The backward shift of an $\ell^2$ sequence is in $\ell^2$

Let $\mathbb{K}$ be
$\mathbb{R}$ or $\mathbb{C}$. For every $x \in \ell^2(\mathbb{N}, \mathbb{K})$, the backward
shift $n \mapsto x_{n+1}$ of the sequence $x$ is square-summable, that is, it lies in
$\ell^2(\mathbb{N}, \mathbb{K})$.

Its squared absolute values are a tail of the squared absolute values of $x$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpShiftOperator.memℓp_backwardFun`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#mem-p-backward-fun).

## Forward shift as a linear map

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$. The
forward shift is the $\mathbb{K}$-linear map
$\ell^2(\mathbb{N}, \mathbb{K}) \to \ell^2(\mathbb{N}, \mathbb{K})$ sending $x$ to the forward
shift of the sequence $x$, that is, to $(0, x_0, x_1, \dots)$, which is again
square-summable.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpShiftOperator.shiftLinMap`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#shift-lin-map).

## Backward shift as a linear map

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$. The
backward-shift linear map is the $\mathbb{K}$-linear map $B$ from $\ell^2(\mathbb{N}, \mathbb{K})$
to itself given by $(Bx)_n = x_{n+1}$ for all $x$ and all $n \in \mathbb{N}$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpShiftOperator.backwardLinMap`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#backward-lin-map).

## Coordinates of the forward-shift linear map

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$. For every $x \in \ell^2(\mathbb{N}, \mathbb{K})$ and every $i \in \mathbb{N}$,
the $i$-th coordinate of the forward-shift linear map applied to $x$ equals the $i$-th term
of the forward shift of the sequence $x$, namely $0$ for $i = 0$ and $x_{i-1}$ for
$i \ge 1$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpShiftOperator.shiftLinMap_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#shift-lin-map-apply).

## Coordinates of the backward-shift linear map

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$. For every $x \in \ell^2(\mathbb{N}, \mathbb{K})$ and every $i \in \mathbb{N}$, the
$i$-th coordinate of the image of $x$ under the backward-shift linear map $B$ is the $i$-th term
of the backward shift of the sequence $x$, that is, $(Bx)_i = x_{i+1}$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpShiftOperator.backwardLinMap_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#backward-lin-map-apply).

## Square sum of the forward shift

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$.
For every $x \in \ell^2(\mathbb{N}, \mathbb{K})$, the forward shift $S x = (0, x_0, x_1, \dots)$
of $x$ satisfies $\sum_{i=0}^{\infty} |(S x)_i|^2 = \sum_{i=0}^{\infty} |x_i|^2$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpShiftOperator.tsum_shiftFun_norm`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#tsum-shift-fun-norm).

## Square sum of the backward shift

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$.
For every $x \in \ell^2(\mathbb{N}, \mathbb{K})$, the backward shift $(x_1, x_2, \dots)$ of
$x$ satisfies $\sum_{i=0}^{\infty} |x_{i+1}|^2 \le \sum_{i=0}^{\infty} |x_i|^2$: the left
side is a tail of the right side.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpShiftOperator.tsum_backwardFun_norm_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#tsum-backward-fun-norm-le).

## The forward shift linear map preserves norms

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$, and let $S$ be the forward shift on the space $\ell^2(\mathbb{N}, \mathbb{K})$ of
square-summable sequences in $\mathbb{K}$, viewed as a linear map and given by
$S(x_0, x_1, \dots) = (0, x_0, x_1, \dots)$. Then $\|Sx\| = \|x\|$ for every
$x \in \ell^2(\mathbb{N}, \mathbb{K})$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpShiftOperator.norm_shiftLinMap_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#norm-shift-lin-map-apply).

## The backward shift linear map does not increase norms

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$, and let $B$ be the backward shift on the space $\ell^2(\mathbb{N}, \mathbb{K})$ of
square-summable sequences in $\mathbb{K}$, viewed as a linear map and given by
$(Bx)_n = x_{n+1}$. Then $\|Bx\| \le \|x\|$ for every $x \in \ell^2(\mathbb{N}, \mathbb{K})$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpShiftOperator.norm_backwardLinMap_apply_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#norm-backward-lin-map-apply-le).

## The unilateral shift operator

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$. The
unilateral shift is the bounded linear operator $S$ on the Hilbert space
$\ell^2(\mathbb{N}, \mathbb{K})$ of square-summable sequences in $\mathbb{K}$ given by
$S(x_0, x_1, x_2, \dots) = (0, x_0, x_1, \dots)$. It is bounded because $\|Sx\| = \|x\|$ for every
$x$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpShiftOperator.shiftCLM`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#shift-clm).

## Backward shift

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$. The backward shift is the
bounded linear operator $B$ on $\ell^2(\mathbb{N}, \mathbb{K})$ given by $(Bx)_n = x_{n+1}$ for
all $x \in \ell^2(\mathbb{N}, \mathbb{K})$ and $n \in \mathbb{N}$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpShiftOperator.backwardCLM`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#backward-clm).

## Coordinates of the unilateral shift

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$, and
let $S$ be the unilateral shift on the Hilbert space $\ell^2(\mathbb{N}, \mathbb{K})$ of
square-summable sequences in $\mathbb{K}$. For every $x \in \ell^2(\mathbb{N}, \mathbb{K})$ and
every $i \in \mathbb{N}$, the coordinate $(Sx)_i$ is the $i$-th term of the forward shift of $x$:
$(Sx)_0 = 0$ and $(Sx)_{n+1} = x_n$ for every $n \in \mathbb{N}$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpShiftOperator.shiftCLM_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#shift-clm-apply).

## Coordinates of the backward shift

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$. For
every $x \in \ell^2(\mathbb{N}, \mathbb{K})$ and every $i \in \mathbb{N}$, the $i$-th coordinate
of the backward shift $Bx$ is the $i$-th term of the backward shift of the sequence $x$,
that is, $(Bx)_i = x_{i+1}$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpShiftOperator.backwardCLM_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#backward-clm-apply).

## The unilateral shift preserves norms

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$, and
let $S$ be the unilateral shift on the Hilbert space $\ell^2(\mathbb{N}, \mathbb{K})$ of
square-summable sequences in $\mathbb{K}$, given by $S(x_0, x_1, \dots) = (0, x_0, x_1, \dots)$.
Then $\|Sx\| = \|x\|$ for every $x \in \ell^2(\mathbb{N}, \mathbb{K})$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpShiftOperator.norm_shiftCLM_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#norm-shift-clm-apply).

## The unilateral shift preserves distances

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$. The unilateral shift $S$ on $\ell^2(\mathbb{N}, \mathbb{K})$ is an isometry:
$\|Sx - Sy\| = \|x - y\|$ for all $x, y \in \ell^2(\mathbb{N}, \mathbb{K})$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpShiftOperator.isometry_shiftCLM`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#isometry-shift-clm).

## The unilateral shift has operator norm one

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$, and let $S$ be the unilateral shift on the Hilbert space
$\ell^2(\mathbb{N}, \mathbb{K})$ of square-summable sequences in $\mathbb{K}$, given by
$S(x_0, x_1, \dots) = (0, x_0, x_1, \dots)$. Then the operator norm of $S$ is $\|S\| = 1$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpShiftOperator.norm_shiftCLM`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#norm-shift-clm).

## The backward shift has operator norm at most one

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$, and let $B$ be the backward shift on the Hilbert space
$\ell^2(\mathbb{N}, \mathbb{K})$ of square-summable sequences in $\mathbb{K}$, given by
$(Bx)_n = x_{n+1}$. Then the operator norm of $B$ satisfies $\|B\| \le 1$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpShiftOperator.norm_backwardCLM_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#norm-backward-clm-le).

## Adjoint of the unilateral shift

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$. The
adjoint of the unilateral shift $S$ on $\ell^2(\mathbb{N}, \mathbb{K})$ is the backward shift
$B$: $S^* = B$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpShiftOperator.adjoint_shiftCLM`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#adjoint-shift-clm).

## Left inverse of the unilateral shift

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$.
The backward shift $B$ is a left inverse of the unilateral shift $S$ on
$\ell^2(\mathbb{N}, \mathbb{K})$: $BS = I$, where $I$ is the identity operator.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpShiftOperator.backward_comp_shift`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#backward-comp-shift).

## The unilateral shift is injective

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$. The
unilateral shift on $\ell^2(\mathbb{N}, \mathbb{K})$ is injective.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpShiftOperator.injective_shiftCLM`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#injective-shift-clm).

## Coordinates of the unilateral shift after the backward shift

Let $\mathbb{K}$ be
$\mathbb{R}$ or $\mathbb{C}$, and on the Hilbert space $\ell^2(\mathbb{N}, \mathbb{K})$ of
square-summable sequences in $\mathbb{K}$ let $S$ be the unilateral shift,
$S(x_0, x_1, \dots) = (0, x_0, x_1, \dots)$, and $B$ the backward shift, $(Bx)_n = x_{n+1}$.
Then for every $x \in \ell^2(\mathbb{N}, \mathbb{K})$ and every $i \in \mathbb{N}$, the coordinate
$(SBx)_i$ is $0$ if $i = 0$ and is $x_i$ if $i \ne 0$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpShiftOperator.shift_comp_backward_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#shift-comp-backward-apply).

## The unilateral shift composed with the backward shift

Let $\mathbb{K}$ be
$\mathbb{R}$ or $\mathbb{C}$, let $S$ be the unilateral (forward) shift and $B$ the
backward shift on $\ell^2(\mathbb{N}, \mathbb{K})$, and let $e_0$ be the first standard
basis vector. Then $S \circ B = 1 - P$, where $P$ is the rank-one operator
$P x = \langle e_0, x \rangle e_0 = x_0 e_0$.

Thus $S \circ B$ is the orthogonal projection onto $\{e_0\}^\perp$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpShiftOperator.shift_comp_backward`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#shift-comp-backward).

## The unilateral shift is not surjective

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$,
and let $S$ be the unilateral shift on the Hilbert space $\ell^2(\mathbb{N}, \mathbb{K})$ of
square-summable sequences in $\mathbb{K}$, given by $S(x_0, x_1, \dots) = (0, x_0, x_1, \dots)$.
Then $S$ is not surjective.

The first standard basis vector $e_0 = (1, 0, 0, \dots)$ is not in the range of $S$, since every
vector in the range has $0$ in coordinate $0$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpShiftOperator.not_surjective_shiftCLM`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/LpShiftOperator.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#not-surjective-shift-clm).

## Geometric sequences with ratio of norm less than one are square-summable

Let
$\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$ and let $c \in \mathbb{K}$ with $\|c\| < 1$. Then
the sequence $(c^i)_{i \in \mathbb{N}}$ lies in $\ell^2$, that is,
$\sum_{i} \|c^i\|^2 < \infty$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpShiftOperatorSpectrum.memℓp_geometric`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpShiftOperatorSpectrum.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/LpShiftOperatorSpectrum.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#mem-p-geometric).

## Geometric vector

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$ and let
$c \in \mathbb{K}$ with $\|c\| < 1$. The geometric vector of $c$ is the sequence
$(1, c, c^2, \dots)$, that is $i \mapsto c^i$, regarded as an element of the Hilbert space
$\ell^2(\mathbb{N}, \mathbb{K})$ of square-summable sequences.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpShiftOperatorSpectrum.geometricVec`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/LpShiftOperatorSpectrum.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/LpShiftOperatorSpectrum.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#geometric-vec).

## Coordinates of the geometric vector

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$ and
let $c \in \mathbb{K}$ with $\|c\| < 1$. For every $i \in \mathbb{N}$, the $i$-th coordinate of
the geometric vector of $c$ in $\ell^2(\mathbb{N}, \mathbb{K})$ is $c^i$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpShiftOperatorSpectrum.geometricVec_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpShiftOperatorSpectrum.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/LpShiftOperatorSpectrum.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#geometric-vec-apply).

## The geometric vector is nonzero

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$ and let
$c \in \mathbb{K}$ with $\|c\| < 1$. The geometric vector $(1, c, c^2, \dots)$ in
$\ell^2(\mathbb{N}, \mathbb{K})$ is nonzero, since its $0$-th coordinate is $1$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpShiftOperatorSpectrum.geometricVec_ne_zero`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpShiftOperatorSpectrum.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/LpShiftOperatorSpectrum.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#geometric-vec-ne-zero).

## Backward shift of the geometric vector

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$
and let $c \in \mathbb{K}$ with $\|c\| < 1$. Let $v = (1, c, c^2, \dots)$ be the geometric vector
of $c$ in $\ell^2(\mathbb{N}, \mathbb{K})$ and let $B$ be the backward shift on
$\ell^2(\mathbb{N}, \mathbb{K})$. Then $Bv = c\,v$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpShiftOperatorSpectrum.backwardCLM_geometricVec`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpShiftOperatorSpectrum.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/LpShiftOperatorSpectrum.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#backward-clm-geometric-vec).

## The identity on ℓ²(ℕ) has norm at most one

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$. The operator norm of the identity operator on $\ell^2(\mathbb{N}, \mathbb{K})$ is
at most $1$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpShiftOperatorSpectrum.norm_one_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpShiftOperatorSpectrum.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/LpShiftOperatorSpectrum.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#norm-one-le).

## Applying a scalar operator minus an operator on ℓ²(ℕ)

Let $\mathbb{K}$ be $\mathbb{R}$
or $\mathbb{C}$, let $T$ be a bounded linear operator on $\ell^2(\mathbb{N}, \mathbb{K})$, let
$\mu \in \mathbb{K}$, and let $\mu I$ be the image of $\mu$ under the algebra map from $\mathbb{K}$
into the bounded operators, i.e. $\mu$ times the identity $I$. Then $(\mu I - T)x = \mu x - Tx$
for every $x \in \ell^2(\mathbb{N}, \mathbb{K})$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpShiftOperatorSpectrum.algebraMap_sub_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpShiftOperatorSpectrum.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/LpShiftOperatorSpectrum.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#algebra-map-sub-apply).

## The open unit ball lies in the spectrum of the unilateral shift

Let $\mathbb{K}$ be
$\mathbb{R}$ or $\mathbb{C}$ and let $S$ be the unilateral shift on
$\ell^2(\mathbb{N}, \mathbb{K})$. Every $\mu \in \mathbb{K}$ with $\|\mu\| < 1$ lies in the
spectrum of $S$ in the algebra of bounded operators on $\ell^2(\mathbb{N}, \mathbb{K})$.

Indeed, write $I$ for the identity operator. If $\mu I - S$ were invertible it would be
surjective, so $(\mu I - S)x = v$ for some $x$, where $v = (1, \bar\mu, \bar\mu^2, \dots)$ is the
geometric vector of the conjugate $\bar\mu$. Since the adjoint of $S$ is the backward shift $B$
and $Bv = \bar\mu v$, pairing $(\mu I - S)x = v$ with $v$ gives $\|v\|^2 = 0$, contradicting
$v \neq 0$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpShiftOperatorSpectrum.mem_spectrum_shiftCLM_of_norm_lt`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpShiftOperatorSpectrum.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/LpShiftOperatorSpectrum.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#mem-spectrum-shift-clm-of-norm-lt).

## The open unit ball lies in the spectrum of the backward shift

Let $\mathbb{K}$ be
$\mathbb{R}$ or $\mathbb{C}$ and let $B$ be the backward shift on $\ell^2(\mathbb{N}, \mathbb{K})$.
Every $\mu \in \mathbb{K}$ with $\|\mu\| < 1$ lies in the spectrum of $B$ in the algebra of
bounded operators on $\ell^2(\mathbb{N}, \mathbb{K})$.

Indeed, writing $I$ for the identity operator, the geometric vector $(1, \mu, \mu^2, \dots)$ lies
in the kernel of $\mu I - B$, so $\mu I - B$ is not injective, hence not invertible.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpShiftOperatorSpectrum.mem_spectrum_backwardCLM_of_norm_lt`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpShiftOperatorSpectrum.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/LpShiftOperatorSpectrum.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#mem-spectrum-backward-clm-of-norm-lt).

## Spectrum of the unilateral shift

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$.
The spectrum over $\mathbb{K}$ of the unilateral shift on $\ell^2(\mathbb{N}, \mathbb{K})$
is the closed unit ball $\{\mu \in \mathbb{K} : |\mu| \le 1\}$ of $\mathbb{K}$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpShiftOperatorSpectrum.spectrum_shiftCLM`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpShiftOperatorSpectrum.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/LpShiftOperatorSpectrum.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#spectrum-shift-clm).

## Spectrum of the backward shift

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$. The
spectrum of the backward shift on $\ell^2(\mathbb{N}, \mathbb{K})$, in the algebra of bounded
operators, is the closed unit ball $\{\mu \in \mathbb{K} : \|\mu\| \le 1\}$: the closed unit
disc when $\mathbb{K} = \mathbb{C}$ and the interval $[-1, 1]$ when $\mathbb{K} = \mathbb{R}$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpShiftOperatorSpectrum.spectrum_backwardCLM`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpShiftOperatorSpectrum.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/LpShiftOperatorSpectrum.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#spectrum-backward-clm).

## Iterated forward shift inserts leading zeroes

Iterating the forward-shift function `n` times inserts `n` zeroes
in front of the sequence.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftFredholmIndex.shiftFun_iterate_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#shift-fun-iterate-apply).

## Iterated backward shift drops leading coordinates

Iterating the backward-shift function `n` times drops the first
`n` coordinates.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftFredholmIndex.backwardFun_iterate_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#backward-fun-iterate-apply).

## Powers of the unilateral shift as iterates of the shift map

The coercion of `S ^ n` is the `n`-fold iterate of `shiftFun`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftFredholmIndex.shiftCLM_pow_coe`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#shift-clm-pow-coe).

## Powers of the backward shift as iterates of the backward map

The coercion of `B ^ n` is the `n`-fold iterate of `backwardFun`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftFredholmIndex.backwardCLM_pow_coe`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#backward-clm-pow-coe).

## Pointwise action of a power of the unilateral shift

Pointwise action of `S ^ n`: it inserts `n` zeroes in front.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftFredholmIndex.shiftCLM_pow_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#shift-clm-pow-apply).

## Pointwise action of a power of the backward shift

Pointwise action of `B ^ n`: it drops the first `n` coordinates.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftFredholmIndex.backwardCLM_pow_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#backward-clm-pow-apply).

## Backward shift power is a left inverse of the shift power

`B ^ n` is a left inverse of `S ^ n`: shifting up then down
recovers the original sequence.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftFredholmIndex.backwardCLM_pow_comp_shiftCLM_pow`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#backward-clm-pow-comp-shift-clm-pow).

## Injectivity of powers of the unilateral shift

The unilateral shift power is injective.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftFredholmIndex.injective_shiftCLM_pow`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#injective-shift-clm-pow).

## Surjectivity of powers of the backward shift

The backward shift power is surjective.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftFredholmIndex.surjective_backwardCLM_pow`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#surjective-backward-clm-pow).

## Kernel of a power of the backward shift

A vector is in the kernel of `B ^ n` iff its coordinates from `n`
onwards all vanish.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftFredholmIndex.mem_ker_backwardCLM_pow`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#mem-ker-backward-clm-pow).

## Range of a power of the unilateral shift

A vector is in the range of `S ^ n` iff its first `n` coordinates
vanish.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftFredholmIndex.mem_range_shiftCLM_pow`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#mem-range-shift-clm-pow).

## First-coordinates map on square-summable sequences

The map taking a sequence to its first `n` coordinates.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftFredholmIndex.firstCoords`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#first-coords).

## Extension of a finite tuple by zeroes

The extension of a tuple of `n` coordinates by zeroes.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftFredholmIndex.extZeroFun`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#ext-zero-fun).

## Zero-extended finite tuples are square-summable

A finitely supported sequence is in `ℓ²`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftFredholmIndex.memℓp_extZeroFun`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#mem-p-ext-zero-fun).

## Linear extension-by-zero map into $\ell^2$

The linear extension-by-zero map `(Fin n → 𝕜) →ₗ[𝕜] ℓ²(ℕ, 𝕜)`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftFredholmIndex.extZero`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#ext-zero).

## Pointwise action of the extension-by-zero map

Pointwise action of the extension-by-zero map.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftFredholmIndex.extZero_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean, line 264](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean#L264). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#ext-zero-apply).

## First coordinates of a zero extension recover the tuple

Taking first coordinates after extension by zeroes is the identity.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftFredholmIndex.firstCoords_extZero`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean, line 269](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean#L269). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#first-coords-ext-zero).

## Kernel vectors of a backward shift power are zero-extended tuples

A vector in the kernel of `B ^ n` is determined by its first `n`
coordinates: extending those coordinates by zeroes recovers it.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftFredholmIndex.extZero_firstCoords_of_mem_ker`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#ext-zero-first-coords-of-mem-ker).

## Kernel of the backward shift power as a space of finite tuples

The kernel of `B ^ n` is linearly equivalent to `Fin n → 𝕜`: a
vector in the kernel is exactly its first `n` coordinates.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftFredholmIndex.kerBackwardCLM_powEquiv`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean, line 295](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean#L295). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#ker-backward-clm-pow-equiv).

## Finite-dimensionality of the kernel of a backward shift power

The kernel of `B ^ n` is finite-dimensional.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftFredholmIndex.finiteDimensional_ker_backwardCLM_pow`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean, line 310](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean#L310). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#finite-dimensional-ker-backward-clm-pow).

## Dimension of the kernel of a backward shift power

The kernel of `B ^ n` has dimension `n`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftFredholmIndex.finrank_ker_backwardCLM_pow`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean, line 315](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean#L315). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#finrank-ker-backward-clm-pow).

## Kernel of the first-coordinates map is the range of the shift power

The kernel of the first-`n`-coordinates map is the range of
`S ^ n`: both consist of the sequences whose first `n` coordinates
vanish.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftFredholmIndex.ker_firstCoords_eq_range_shiftCLM_pow`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean, line 323](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean#L323). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#ker-first-coords-eq-range-shift-clm-pow).

## Dimension of the cokernel of a unilateral shift power

The cokernel of `S ^ n` has dimension `n`: the quotient of `ℓ²`
by the range of `S ^ n` is equivalent to `Fin n → 𝕜` via the first
`n` coordinates.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftFredholmIndex.finrank_quotient_range_shiftCLM_pow`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean, line 352](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean#L352). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#finrank-quotient-range-shift-clm-pow).

## Backward shift power inverts the shift power modulo finite rank

The quasi-inverse relation `B ^ n ∘L S ^ n = 1` holds exactly,
hence also modulo finite-rank operators.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftFredholmIndex.approx_backward_comp_shift`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean, line 367](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean#L367). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#approx-backward-comp-shift).

## Shift power inverts the backward shift power modulo finite rank

The defect `S ^ n ∘L B ^ n - 1` has finite rank: its range lies in
the finite-dimensional kernel of `B ^ n`, since applying `B ^ n`
after it gives `0`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftFredholmIndex.approx_shift_comp_backward`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean, line 383](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean#L383). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#approx-shift-comp-backward).

## Powers of the unilateral shift are Fredholm

Every power of the unilateral shift is a Fredholm operator: `B ^ n`
is a quasi-inverse.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftFredholmIndex.isFredholm_shiftCLM_pow`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean, line 409](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean#L409). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#is-fredholm-shift-clm-pow).

## Powers of the backward shift are Fredholm

Every power of the backward shift is a Fredholm operator: `S ^ n`
is a quasi-inverse.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftFredholmIndex.isFredholm_backwardCLM_pow`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean, line 415](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean#L415). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#is-fredholm-backward-clm-pow).

## Fredholm index of a unilateral shift power is $-n$

The Fredholm index of `S ^ n` is `-n`: the shift power is
injective, and its cokernel has dimension `n`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftFredholmIndex.index_shiftCLM_pow`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean, line 421](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean#L421). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#index-shift-clm-pow).

## Fredholm index of a backward shift power is $n$

The Fredholm index of `B ^ n` is `n`: the backward shift power is
surjective, and its kernel has dimension `n`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftFredholmIndex.index_backwardCLM_pow`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean, line 429](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean#L429). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#index-backward-clm-pow).

## Fredholm index of the unilateral shift is $-1$

The Fredholm index of the unilateral shift is `-1`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftFredholmIndex.index_shiftCLM`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean, line 436](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean#L436). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#index-shift-clm).

## Fredholm index of the backward shift is $1$

The Fredholm index of the backward shift is `1`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftFredholmIndex.index_backwardCLM`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean, line 440](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean#L440). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#index-backward-clm).

## Shift composed with backward shift is Fredholm

`S ∘L B` is Fredholm: it is the composite of two Fredholm operators.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftFredholmIndex.isFredholm_shift_comp_backward`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean, line 444](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean#L444). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#is-fredholm-shift-comp-backward).

## Shift composed with backward shift has Fredholm index zero

`S ∘L B` has Fredholm index `0`, as index additivity under
composition demands: `(-1) + 1 = 0`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftFredholmIndex.index_shift_comp_backward`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean, line 450](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftFredholmIndex.lean#L450). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#index-shift-comp-backward).

## Essential spectrum of a bounded operator

The **essential spectrum** of a bounded operator `T`: the set of
scalars `μ` for which `T - μ • 1` is not a Fredholm operator.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftEssentialSpectrum.essentialSpectrum`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/ShiftEssentialSpectrum.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftEssentialSpectrum.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#essential-spectrum).

## Pointwise action of one minus a scaled backward shift

Pointwise action of `1 - μ • B`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftEssentialSpectrum.one_sub_smul_backward_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftEssentialSpectrum.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftEssentialSpectrum.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#one-sub-smul-backward-apply).

## Factorization of the shifted unilateral shift

The key factorization: `S - μ = S (1 - μ B) + μ (S B - 1)`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftEssentialSpectrum.shift_sub_smul_one_eq`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftEssentialSpectrum.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftEssentialSpectrum.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#shift-sub-smul-one-eq).

## Shifted unilateral shift has trivial kernel

`S - μ • 1` has trivial kernel for every `μ`: the coordinate
equations force every coordinate to vanish.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftEssentialSpectrum.injective_shift_sub`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftEssentialSpectrum.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftEssentialSpectrum.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#injective-shift-sub).

## One minus a small multiple of the backward shift is invertible

`1 - μ • B` is a unit when `‖μ‖ < 1`, by the Neumann-series
criterion `isUnit_one_sub_of_norm_lt_one`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftEssentialSpectrum.isUnit_one_sub_smul_backward`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftEssentialSpectrum.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftEssentialSpectrum.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#is-unit-one-sub-smul-backward).

## Invertible operators are Fredholm

A unit operator is Fredholm, via `IsHomeomorph` and
`IsInvertible.isFredholm`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftEssentialSpectrum.isFredholm_of_isUnit`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftEssentialSpectrum.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftEssentialSpectrum.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#is-fredholm-of-is-unit).

## One minus a small multiple of the backward shift is Fredholm

`1 - μ • B` is Fredholm when `‖μ‖ < 1`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftEssentialSpectrum.isFredholm_one_sub_smul_backward`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftEssentialSpectrum.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftEssentialSpectrum.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#is-fredholm-one-sub-smul-backward).

## Shifted unilateral shift is Fredholm inside the unit disk

For `‖μ‖ < 1`, `S - μ • 1` is Fredholm: it is the Fredholm
operator `S (1 - μ B)` plus the finite-rank operator `μ (S B - 1)`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftEssentialSpectrum.isFredholm_shift_sub_smul_one_of_norm_lt_one`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftEssentialSpectrum.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftEssentialSpectrum.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#is-fredholm-shift-sub-smul-one-of-norm-l).

## Shifted unilateral shift has index $-1$ inside the unit disk

The index of `S - μ • 1` is `-1` for `‖μ‖ < 1`: the canonical
homotopy theorem makes the index constant along `S - (t μ) • 1`,
`t ∈ [0, 1]`, and the canonical shift has index `-1` at `t = 0`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftEssentialSpectrum.index_shift_sub_smul_one_of_norm_lt_one`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftEssentialSpectrum.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftEssentialSpectrum.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#index-shift-sub-smul-one-of-norm-lt-one).

## Shifted unilateral shift is invertible outside the unit disk

For `‖μ‖ > 1`, `S - μ • 1` is a unit: it equals
`(algebraMap (-μ)) * (1 - μ⁻¹ • S)`, a product of units.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftEssentialSpectrum.isUnit_shift_sub_smul_one_of_one_lt_norm`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftEssentialSpectrum.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftEssentialSpectrum.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#is-unit-shift-sub-smul-one-of-one-lt-nor).

## Shifted unilateral shift is Fredholm outside the unit disk

For `‖μ‖ > 1`, `S - μ • 1` is Fredholm, as it is a unit.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftEssentialSpectrum.isFredholm_shift_sub_smul_one_of_one_lt_norm`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftEssentialSpectrum.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftEssentialSpectrum.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#is-fredholm-shift-sub-smul-one-of-one-lt).

## Shifted unilateral shift has index zero outside the unit disk

For `‖μ‖ > 1`, `S - μ • 1` has index `0`: a unit is bijective.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftEssentialSpectrum.index_shift_sub_smul_one_of_one_lt_norm`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftEssentialSpectrum.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftEssentialSpectrum.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#index-shift-sub-smul-one-of-one-lt-norm).

## Truncated geometric sequence

The truncated geometric sequence `(1, μ̄, μ̄², …, μ̄ᴺ, 0, …)`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftEssentialSpectrum.approxFun`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/ShiftEssentialSpectrum.lean, line 281](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftEssentialSpectrum.lean#L281). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#approx-fun).

## Truncated geometric sequence is square-summable

The truncated geometric sequence is in `ℓ²`: it has finite support.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftEssentialSpectrum.memℓp_approxFun`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftEssentialSpectrum.lean, line 284](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftEssentialSpectrum.lean#L284). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#mem-p-approx-fun).

## Truncated geometric vector in $\ell^2$

The truncated geometric sequence as an `ℓ²` vector.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftEssentialSpectrum.approxVec`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/ShiftEssentialSpectrum.lean, line 293](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftEssentialSpectrum.lean#L293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#approx-vec).

## Squared norm of the truncated geometric vector

The squared norm of the truncated geometric vector is `N + 1`,
when `‖μ‖ = 1`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftEssentialSpectrum.norm_sq_approxVec`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftEssentialSpectrum.lean, line 300](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftEssentialSpectrum.lean#L300). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#norm-sq-approx-vec).

## Shifted unilateral shift on the truncated geometric vector

The coordinates of `(S - μ • 1)` applied to the truncated
geometric vector: `-μ` at `0`, `(star μ)^N` at `N + 1`, and `0`
elsewhere, when `‖μ‖ = 1`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftEssentialSpectrum.sub_smul_one_approxVec_apply_zero`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftEssentialSpectrum.lean, line 324](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftEssentialSpectrum.lean#L324). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#sub-smul-one-approx-vec-apply-zero).

## Squared norm of the shifted shift on the truncated geometric vector

The squared norm of `(S - μ • 1)` applied to the truncated
geometric vector is `2`, when `‖μ‖ = 1`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftEssentialSpectrum.norm_sq_sub_smul_one_approxVec`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftEssentialSpectrum.lean, line 364](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftEssentialSpectrum.lean#L364). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#norm-sq-sub-smul-one-approx-vec).

## Shifted unilateral shift is not Fredholm on the unit circle

For `‖μ‖ = 1`, `S - μ • 1` is not Fredholm: it has trivial kernel
and closed range would make it bounded below, contradicting the
approximate eigenvectors.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftEssentialSpectrum.not_isFredholm_shift_sub_smul_one_of_norm_eq_one`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftEssentialSpectrum.lean, line 388](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftEssentialSpectrum.lean#L388). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#not-is-fredholm-shift-sub-smul-one-of-no).

## Essential spectrum of the unilateral shift is the unit circle

The essential spectrum of the unilateral shift is the unit circle:
`S - μ • 1` is Fredholm exactly off the circle.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftEssentialSpectrum.essentialSpectrum_shiftCLM`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftEssentialSpectrum.lean, line 425](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftEssentialSpectrum.lean#L425). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#essential-spectrum-shift-clm).

## Membership in the essential spectrum of the unilateral shift

Membership form: `μ` is in the essential spectrum of the shift
iff `‖μ‖ = 1`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftEssentialSpectrum.mem_essentialSpectrum_shiftCLM`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftEssentialSpectrum.lean, line 440](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftEssentialSpectrum.lean#L440). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#mem-essential-spectrum-shift-clm).

## Quadratic form of the forward shift as a series

The quadratic form of the forward shift as a series over consecutive
coordinates: `⟪S x, x⟫ = ∑' n, conj (x n) * x (n + 1)`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftNumericalRange.quadForm_fwdShift_eq_tsum`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftNumericalRange.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftNumericalRange.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#quad-form-fwd-shift-eq-tsum).

## Quadratic form of the backward shift as a series

The quadratic form of the backward shift as a series over consecutive
coordinates: `⟪B x, x⟫ = ∑' n, conj (x (n + 1)) * x n`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftNumericalRange.quadForm_bwdShift_eq_tsum`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftNumericalRange.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftNumericalRange.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#quad-form-bwd-shift-eq-tsum).

## Strict AM-GM bound on consecutive coordinates of a unit vector

For a unit vector `x`, the sum of the products of consecutive
coordinate norms is strictly less than `1`: termwise AM–GM gives a
bound of `(1 + (1 - ‖x 0‖²)) / 2 ≤ 1`, and the AM–GM inequality is
strict at the coordinate supplied by `exists_norm_ne_norm_succ`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftNumericalRange.sum_norm_mul_succ_lt_one`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftNumericalRange.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftNumericalRange.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#sum-norm-mul-succ-lt-one).

## Square-summability of the scaled geometric sequence

The geometric sequence attached to `u`, with coordinates
`√(1 - ‖u‖²) * u ^ n`, is in `ℓ²`. When `‖u‖ ≥ 1` the square root is `0`
and the sequence is identically `0`; the interesting case is `‖u‖ < 1`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftNumericalRange.memℓp_geom`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftNumericalRange.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftNumericalRange.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#mem-p-geom).

## Geometric unit vector attached to a point of the disc

The geometric vector attached to `u`: the `ℓ²` sequence with
coordinates `√(1 - ‖u‖²) * u ^ n`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftNumericalRange.geom`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/ShiftNumericalRange.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftNumericalRange.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#geom).

## Pointwise action of the geometric vector

Pointwise action of the geometric vector.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftNumericalRange.geom_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftNumericalRange.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftNumericalRange.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#geom-apply).

## Geometric vector of a point in the open disc is a unit vector

The geometric vector attached to `u` with `‖u‖ < 1` is a unit vector.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftNumericalRange.norm_geom`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftNumericalRange.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftNumericalRange.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#norm-geom).

## Forward shift quadratic form at a geometric vector

The quadratic form of the forward shift at the geometric vector
attached to `u` is `u` itself.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftNumericalRange.quadForm_fwd_geom`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftNumericalRange.lean, line 270](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftNumericalRange.lean#L270). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#quad-form-fwd-geom).

## Backward shift quadratic form at a geometric vector

The quadratic form of the backward shift at the geometric vector
attached to `u` is `conj u`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftNumericalRange.quadForm_bwd_geom`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftNumericalRange.lean, line 313](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftNumericalRange.lean#L313). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#quad-form-bwd-geom).

## Open unit disc lies in the forward shift's numerical range

Every `u` with `‖u‖ < 1` lies in the numerical range of the forward
shift, witnessed by the geometric vector attached to `u`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftNumericalRange.mem_numericalRange_fwdShift_of_norm_lt_one`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftNumericalRange.lean, line 357](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftNumericalRange.lean#L357). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#mem-numerical-range-fwd-shift-of-norm-lt).

## Open unit disc lies in the backward shift's numerical range

Every `w` with `‖w‖ < 1` lies in the numerical range of the backward
shift, witnessed by the geometric vector attached to `conj w`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftNumericalRange.mem_numericalRange_bwdShift_of_norm_lt_one`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftNumericalRange.lean, line 363](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftNumericalRange.lean#L363). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#mem-numerical-range-bwd-shift-of-norm-lt).

## Forward shift's numerical range lies in the open unit disc

Every point of the numerical range of the forward shift has norm
strictly less than `1`, by the AM–GM strict bound.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftNumericalRange.norm_lt_one_of_mem_numericalRange_fwdShift`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftNumericalRange.lean, line 373](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftNumericalRange.lean#L373). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#norm-lt-one-of-mem-numerical-range-fwd-s).

## Backward shift's numerical range lies in the open unit disc

Every point of the numerical range of the backward shift has norm
strictly less than `1`, by the AM–GM strict bound.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftNumericalRange.norm_lt_one_of_mem_numericalRange_bwdShift`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftNumericalRange.lean, line 389](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftNumericalRange.lean#L389). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#norm-lt-one-of-mem-numerical-range-bwd-s).

## Numerical range of the unilateral shift is the open unit disc

The numerical range of the unilateral shift on `ℓ²(ℕ, ℂ)` is the
open unit disc.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftNumericalRange.numericalRange_fwdShiftCLM`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftNumericalRange.lean, line 407](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftNumericalRange.lean#L407). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#numerical-range-fwd-shift-clm).

## Numerical range of the backward shift is the open unit disc

The numerical range of the backward shift on `ℓ²(ℕ, ℂ)` is the
open unit disc.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ShiftNumericalRange.numericalRange_bwdShiftCLM`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ShiftNumericalRange.lean, line 421](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ShiftNumericalRange.lean#L421). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#numerical-range-bwd-shift-clm).

## Unilateral shift operator

A bounded linear operator $T$ on a complex inner product
space $H$ is a unilateral shift if there is a Hilbert basis $(b_n)_{n \in \mathbb{N}}$ of $H$
such that $T b_n = b_{n+1}$ for every $n \in \mathbb{N}$.

Formalized by `MathlibExt.Analysis.OperatorTheory.UnilateralShiftCharacterizationWanted.IsShift`, a definition declared in [WantedExt/Analysis/OperatorTheory/UnilateralShiftCharacterizationWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/OperatorTheory/UnilateralShiftCharacterizationWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#is-shift).

## Isometric characterization of the unilateral shift

Let $H$ be a separable complex
Hilbert space, and call a bounded linear operator $T : H \to H$ a shift if there is an
orthonormal basis $(e_n)_{n \in \mathbb{N}}$ of $H$ with $T e_n = e_{n+1}$ for every
$n \in \mathbb{N}$. Then a bounded linear operator $T : H \to H$ is a shift if and only if the
following three conditions hold: $T$ is an isometry, that is,
$\langle T x, T y \rangle = \langle x, y \rangle$ for all $x, y \in H$; the ranges of the powers
of $T$ satisfy $\bigcap_{n \ge 1} \mathrm{Ran}(T^n) = \{0\}$; and the orthogonal complement
$(\mathrm{Ran}\, T)^\perp$ of the range of $T$ has dimension $1$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Operator theory; Special classes of linear operators), problem `ma_proofbench_l2_33`.

Stated but not proved: `MathlibExt.Analysis.OperatorTheory.UnilateralShiftCharacterizationWanted.isShift_iff_isometry_iInf_range_pow_eq_bot_finrank_orthogonal_eq_one` is written with `theorem_wanted` in [WantedExt/Analysis/OperatorTheory/UnilateralShiftCharacterizationWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/OperatorTheory/UnilateralShiftCharacterizationWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html#is-shift-iff-isometry-i-inf-range-pow-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Unilateral shift](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/unilateral-shift)
