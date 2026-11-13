---
declaration: section
origin: cited
lean: MathlibExt.Analysis.InnerProductSpace.WeightedShiftOperator.weightedShiftFun, MathlibExt.Analysis.InnerProductSpace.WeightedShiftOperator.weightedBackwardFun, MathlibExt.Analysis.InnerProductSpace.WeightedShiftOperator.weightedShiftFun_zero, MathlibExt.Analysis.InnerProductSpace.WeightedShiftOperator.weightedShiftFun_succ, MathlibExt.Analysis.InnerProductSpace.WeightedShiftOperator.weightedBackwardFun_apply, MathlibExt.Analysis.InnerProductSpace.WeightedShiftOperator.weightedShiftCLM, MathlibExt.Analysis.InnerProductSpace.WeightedShiftOperator.weightedBackwardCLM, MathlibExt.Analysis.InnerProductSpace.WeightedShiftOperator.weightedShiftLinMap
statement: formalized
proof: formalized
---

# Weighted shifts

42 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/weighted-shifts/index.html).

## Weighted forward shift of a sequence

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$. For a weight sequence $w : \mathbb{N} \to \mathbb{K}$ and a sequence
$x : \mathbb{N} \to \mathbb{K}$, the weighted forward shift of $x$ is the sequence $y$ with
$y_0 = 0$ and $y_{n+1} = w_n x_n$ for every $n \in \mathbb{N}$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WeightedShiftOperator.weightedShiftFun`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/weighted-shifts/index.html#weighted-shift-fun).

## Weighted backward shift of a sequence

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$.
For weights $w : \mathbb{N} \to \mathbb{K}$ and a sequence $x : \mathbb{N} \to \mathbb{K}$, the
weighted backward shift of $x$ is the sequence whose term at index $i$ is
$\overline{w_i}\, x_{i+1}$.

The weights are conjugated so that the resulting operator on $\ell^2$ is the adjoint of the
weighted forward shift.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WeightedShiftOperator.weightedBackwardFun`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/weighted-shifts/index.html#weighted-backward-fun).

## Weighted forward shift at index zero

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$.
For all weights $w : \mathbb{N} \to \mathbb{K}$ and every sequence $x : \mathbb{N} \to \mathbb{K}$,
the term at index $0$ of the weighted forward shift of $x$ is $0$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WeightedShiftOperator.weightedShiftFun_zero`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/weighted-shifts/index.html#weighted-shift-fun-zero).

## Weighted forward shift at a successor index

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$. For weights $w : \mathbb{N} \to \mathbb{K}$, a sequence
$x : \mathbb{N} \to \mathbb{K}$ and $n \in \mathbb{N}$, the term at index $n + 1$ of the weighted
forward shift of $x$ is $w_n x_n$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WeightedShiftOperator.weightedShiftFun_succ`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/weighted-shifts/index.html#weighted-shift-fun-succ).

## Coordinates of the weighted backward-shift function

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$. For weights $w : \mathbb{N} \to \mathbb{K}$, a sequence
$x : \mathbb{N} \to \mathbb{K}$ and $i \in \mathbb{N}$, the weighted backward-shift function of
$w$ applied to $x$ takes the value $\overline{w_i}\, x_{i+1}$ at $i$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WeightedShiftOperator.weightedBackwardFun_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/weighted-shifts/index.html#weighted-backward-fun-apply).

## Weighted forward shift operator

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$ and let
$w : \mathbb{N} \to \mathbb{K}$ be weights with $\sup_n |w_n| < \infty$. The weighted forward
shift with weights $w$ is the bounded operator on $\ell^2(\mathbb{N}, \mathbb{K})$ obtained by
first applying the diagonal operator $x \mapsto (w_n x_n)_{n}$ and then the unilateral forward
shift $(x_0, x_1, \dots) \mapsto (0, x_0, x_1, \dots)$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WeightedShiftOperator.weightedShiftCLM`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/weighted-shifts/index.html#weighted-shift-clm).

## Weighted backward shift

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$ and let
$w : \mathbb{N} \to \mathbb{K}$ be weights with bounded moduli. The weighted backward shift $B_w$
is the bounded operator on $\ell^2(\mathbb{N}, \mathbb{K})$ obtained by applying the backward shift
$(x_0, x_1, \dots) \mapsto (x_1, x_2, \dots)$ and then multiplying coordinate $i$ by
$\overline{w_i}$; thus $(B_w x)_i = \overline{w_i}\, x_{i+1}$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WeightedShiftOperator.weightedBackwardCLM`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/weighted-shifts/index.html#weighted-backward-clm).

## Weighted forward shift as a linear map

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$, and let $w : \mathbb{N} \to \mathbb{K}$ be a weight sequence whose norms
$\|w_n\|$ are bounded above. The weighted forward shift linear map is the $\mathbb{K}$-linear
map $\ell^2(\mathbb{N}, \mathbb{K}) \to \ell^2(\mathbb{N}, \mathbb{K})$ underlying the bounded
weighted forward shift operator (multiplication by $w$ followed by the forward shift), which
sends $x$ to the sequence $y$ with $y_0 = 0$ and $y_{n+1} = w_n x_n$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WeightedShiftOperator.weightedShiftLinMap`, an abbreviation declared in [MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/weighted-shifts/index.html#weighted-shift-lin-map).

## Weighted backward shift as a linear map

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$
and let $w : \mathbb{N} \to \mathbb{K}$ be weights with $\sup_n |w_n| < \infty$. The weighted
backward shift linear map with weights $w$ is the bounded weighted backward shift operator on
$\ell^2(\mathbb{N}, \mathbb{K})$ with weights $w$, regarded as a $\mathbb{K}$-linear map from
$\ell^2(\mathbb{N}, \mathbb{K})$ to itself (forgetting continuity).

Formalized by `MathlibExt.Analysis.InnerProductSpace.WeightedShiftOperator.weightedBackwardLinMap`, an abbreviation declared in [MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/weighted-shifts/index.html#weighted-backward-lin-map).

## Coordinates of the weighted forward shift

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$, let $w : \mathbb{N} \to \mathbb{K}$ be weights with $\sup_n |w_n| < \infty$, and let
$S_w$ be the weighted forward shift operator on $\ell^2(\mathbb{N}, \mathbb{K})$ with weights $w$.
For every $x \in \ell^2(\mathbb{N}, \mathbb{K})$ and every $i \in \mathbb{N}$, the coordinate
$(S_w x)_i$ is the term at index $i$ of the weighted forward shift of the sequence $x$; that is,
$(S_w x)_0 = 0$ and $(S_w x)_{n+1} = w_n x_n$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WeightedShiftOperator.weightedShiftCLM_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/weighted-shifts/index.html#weighted-shift-clm-apply).

## Coordinates of the weighted backward shift

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$, let $w : \mathbb{N} \to \mathbb{K}$ be weights with bounded moduli, and let $B_w$ be
the weighted backward shift on $\ell^2(\mathbb{N}, \mathbb{K})$. For every
$x \in \ell^2(\mathbb{N}, \mathbb{K})$ and every $i \in \mathbb{N}$, the $i$-th coordinate of
$B_w x$ is the weighted backward-shift function of $w$ applied to $x$ at $i$, that is,
$(B_w x)_i = \overline{w_i}\, x_{i+1}$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WeightedShiftOperator.weightedBackwardCLM_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/weighted-shifts/index.html#weighted-backward-clm-apply).

## The weighted forward shift agrees with the shift of sequences

Let $\mathbb{K}$ be
$\mathbb{R}$ or $\mathbb{C}$ and let $w : \mathbb{N} \to \mathbb{K}$ be weights with
$\sup_n |w_n| < \infty$. For every $x \in \ell^2(\mathbb{N}, \mathbb{K})$, the image of $x$ under
the weighted forward shift operator with weights $w$ is as a sequence the weighted forward
shift of $x$: its term at index $0$ is $0$ and its term at index $n + 1$ is $w_n x_n$ for
every $n$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WeightedShiftOperator.weightedShiftCLM_apply_coe`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/weighted-shifts/index.html#weighted-shift-clm-apply-coe).

## Coordinates of the weighted forward shift linear map

Let $\mathbb{K}$ be
$\mathbb{R}$ or $\mathbb{C}$, and let $w : \mathbb{N} \to \mathbb{K}$ be a weight sequence
whose norms $\|w_n\|$ are bounded above. For every $x \in \ell^2(\mathbb{N}, \mathbb{K})$, the
image of $x$ under the weighted forward shift linear map, viewed as a sequence, is the weighted
forward shift of $x$: its coordinate $0$ is $0$ and its coordinate $n + 1$ is $w_n x_n$ for
every $n$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WeightedShiftOperator.weightedShiftLinMap_apply_coe`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/weighted-shifts/index.html#weighted-shift-lin-map-apply-coe).

## The weighted backward shift linear map agrees with the shift of sequences

Let
$\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$ and let $w : \mathbb{N} \to \mathbb{K}$ be weights with
$\sup_n |w_n| < \infty$. For every $x \in \ell^2(\mathbb{N}, \mathbb{K})$, the image of $x$ under
the weighted backward shift with weights $w$, regarded as a linear map on
$\ell^2(\mathbb{N}, \mathbb{K})$, is as a sequence the weighted backward shift of $x$: its term
at index $i$ is $\overline{w_i}\, x_{i+1}$ for every $i$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WeightedShiftOperator.weightedBackwardLinMap_apply_coe`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/weighted-shifts/index.html#weighted-backward-lin-map-apply-coe).

## Weighted forward shifts preserve square-summability

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$ and let $(w_n)_{n \in \mathbb{N}}$ be a bounded sequence in $\mathbb{K}$. For every
$x \in \ell^2(\mathbb{N}, \mathbb{K})$, the sequence $y$ with $y_0 = 0$ and
$y_{n+1} = w_n x_n$ is square-summable.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WeightedShiftOperator.memℓp_weightedShiftFun`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/weighted-shifts/index.html#mem-p-weighted-shift-fun).

## Weighted backward shifts preserve square-summability

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$ and let $(w_n)_{n \in \mathbb{N}}$ be a bounded sequence in $\mathbb{K}$. For every
$x \in \ell^2(\mathbb{N}, \mathbb{K})$, the sequence $(\overline{w_i}\, x_{i+1})_{i \in \mathbb{N}}$
is square-summable.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WeightedShiftOperator.memℓp_weightedBackwardFun`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/weighted-shifts/index.html#mem-p-weighted-backward-fun).

## The weighted forward shift on basis vectors

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$, let $w : \mathbb{N} \to \mathbb{K}$ be weights with $\sup_n |w_n| < \infty$, and let
$(e_n)_{n \in \mathbb{N}}$ be the standard basis vectors of $\ell^2(\mathbb{N}, \mathbb{K})$. For
every $n$, the weighted forward shift operator with weights $w$ sends $e_n$ to $w_n e_{n+1}$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WeightedShiftOperator.weightedShiftCLM_single`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/weighted-shifts/index.html#weighted-shift-clm-single).

## Weighted backward shift on basis vectors

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$, let $w : \mathbb{N} \to \mathbb{K}$ be weights with bounded moduli, and write $e_n$
for the $n$-th standard basis vector of $\ell^2(\mathbb{N}, \mathbb{K})$. For every $n$, the
weighted backward shift $B_w$ satisfies $B_w e_{n+1} = \overline{w_n}\, e_n$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WeightedShiftOperator.weightedBackwardCLM_single_succ`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/weighted-shifts/index.html#weighted-backward-clm-single-succ).

## Uniform weight bounds bound the weighted shift

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$, let $w : \mathbb{N} \to \mathbb{K}$ be weights with bounded moduli, and let $S_w$ be
the weighted forward shift on $\ell^2(\mathbb{N}, \mathbb{K})$. If $C$ is a real number with
$|w_n| \le C$ for every $n$, then the operator norm of $S_w$ is at most $C$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WeightedShiftOperator.norm_weightedShiftCLM_le_of_forall_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/weighted-shifts/index.html#norm-weighted-shift-clm-le-of-forall-le).

## Operator norm of a weighted shift

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$ and
let $w : \mathbb{N} \to \mathbb{K}$ be weights with bounded moduli. The weighted forward shift
$S_w$ on $\ell^2(\mathbb{N}, \mathbb{K})$ has operator norm $\|S_w\| = \sup_n |w_n|$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WeightedShiftOperator.norm_weightedShiftCLM`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/weighted-shifts/index.html#norm-weighted-shift-clm).

## Adjoint of the weighted shift

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$ and let
$(w_n)_{n \in \mathbb{N}}$ be a bounded sequence in $\mathbb{K}$. The adjoint of the weighted
forward shift $S_w$ on $\ell^2(\mathbb{N}, \mathbb{K})$, given by $(S_w x)_0 = 0$ and
$(S_w x)_{n+1} = w_n x_n$, is the weighted backward shift $B_w$, given by
$(B_w x)_i = \overline{w_i}\, x_{i+1}$; that is, $S_w^* = B_w$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WeightedShiftOperator.adjoint_weightedShiftCLM`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/weighted-shifts/index.html#adjoint-weighted-shift-clm).

## Norm of the weighted backward shift

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$ and
let $(w_n)_{n \in \mathbb{N}}$ be a bounded sequence in $\mathbb{K}$. The weighted backward shift
$B_w$ on $\ell^2(\mathbb{N}, \mathbb{K})$, given by $(B_w x)_i = \overline{w_i}\, x_{i+1}$, has
operator norm $\|B_w\| = \sup_n |w_n|$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WeightedShiftOperator.norm_weightedBackwardCLM`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/weighted-shifts/index.html#norm-weighted-backward-clm).

## Norm bound for weighted shift images

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$ and
let $w : \mathbb{N} \to \mathbb{K}$ be weights with bounded moduli. For every
$x \in \ell^2(\mathbb{N}, \mathbb{K})$, the weighted forward shift $S_w$, viewed as a linear map,
satisfies $\|S_w x\| \le \left(\sup_n |w_n|\right) \|x\|$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WeightedShiftOperator.norm_weightedShiftLinMap_apply_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/weighted-shifts/index.html#norm-weighted-shift-lin-map-apply-le).

## Norm bound for the weighted backward shift

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$ and let $(w_n)_{n \in \mathbb{N}}$ be a bounded sequence in $\mathbb{K}$, and let
$B_w$ be the weighted backward shift on $\ell^2(\mathbb{N}, \mathbb{K})$, given by
$(B_w x)_i = \overline{w_i}\, x_{i+1}$. Then $\|B_w x\| \le (\sup_n |w_n|)\, \|x\|$ for every
$x \in \ell^2(\mathbb{N}, \mathbb{K})$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WeightedShiftOperator.norm_weightedBackwardLinMap_apply_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean, line 257](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean#L257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/weighted-shifts/index.html#norm-weighted-backward-lin-map-apply-le).

## The weighted backward shift after the forward shift is diagonal

Let $\mathbb{K}$ be
$\mathbb{R}$ or $\mathbb{C}$, let $(w_n)_{n \in \mathbb{N}}$ be a bounded sequence in $\mathbb{K}$,
and on $\ell^2(\mathbb{N}, \mathbb{K})$ let $S_w$ be the weighted forward shift,
$(S_w x)_0 = 0$ and $(S_w x)_{n+1} = w_n x_n$, and $B_w$ the weighted backward shift,
$(B_w x)_i = \overline{w_i}\, x_{i+1}$. Then $(B_w S_w x)_i = |w_i|^2 x_i$ for every
$x \in \ell^2(\mathbb{N}, \mathbb{K})$ and every $i \in \mathbb{N}$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WeightedShiftOperator.backward_comp_shift_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/weighted-shifts/index.html#backward-comp-shift-apply).

## Forward-after-backward weighted shift is diagonal

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$, let $w : \mathbb{N} \to \mathbb{K}$ be weights with bounded moduli, and let $S_w$ and
$B_w$ be the weighted forward and backward shifts on $\ell^2(\mathbb{N}, \mathbb{K})$. For every
$x \in \ell^2(\mathbb{N}, \mathbb{K})$, the composite $S_w B_w$ satisfies $(S_w B_w x)_0 = 0$ and
$(S_w B_w x)_i = |w_{i-1}|^2 x_i$ for every $i \ge 1$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WeightedShiftOperator.shift_comp_backward_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/weighted-shifts/index.html#shift-comp-backward-apply).

## The weighted backward shift is a left inverse for unimodular weights

Let $\mathbb{K}$ be
$\mathbb{R}$ or $\mathbb{C}$ and let $(w_n)_{n \in \mathbb{N}}$ be a sequence in $\mathbb{K}$ with
$|w_n| = 1$ for every $n$. On $\ell^2(\mathbb{N}, \mathbb{K})$ let $S_w$ be the weighted forward
shift, $(S_w x)_0 = 0$ and $(S_w x)_{n+1} = w_n x_n$, and $B_w$ the weighted backward shift,
$(B_w x)_i = \overline{w_i}\, x_{i+1}$. Then $B_w S_w$ is the identity operator.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WeightedShiftOperator.backward_comp_shift_eq_one`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean, line 284](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean#L284). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/weighted-shifts/index.html#backward-comp-shift-eq-one).

## Weighted shifts with nonzero weights are injective

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$ and let $(w_n)_{n \in \mathbb{N}}$ be a bounded sequence in $\mathbb{K}$ with
$w_n \neq 0$ for every $n$. Then the weighted forward shift $S_w$ on
$\ell^2(\mathbb{N}, \mathbb{K})$, given by $(S_w x)_0 = 0$ and $(S_w x)_{n+1} = w_n x_n$, is
injective.

The coordinates of $x$ are recovered from $S_w x$ one by one: $x_n = (S_w x)_{n+1} / w_n$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WeightedShiftOperator.injective_weightedShiftCLM`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/weighted-shifts/index.html#injective-weighted-shift-clm).

## A vanishing weight makes the weighted shift non-injective

Let $\mathbb{K}$ be
$\mathbb{R}$ or $\mathbb{C}$ and let $w : \mathbb{N} \to \mathbb{K}$ be weights with bounded
moduli. If $w_n = 0$ for some $n$, then the weighted forward shift $S_w$ on
$\ell^2(\mathbb{N}, \mathbb{K})$ is not injective.

Indeed, $S_w$ sends the $n$-th standard basis vector to $0$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WeightedShiftOperator.not_injective_weightedShiftCLM`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean, line 307](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean#L307). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/weighted-shifts/index.html#not-injective-weighted-shift-clm).

## Weighted shifts with unimodular weights preserve norms

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$ and let $(w_n)_{n \in \mathbb{N}}$ be a sequence in $\mathbb{K}$ with $|w_n| = 1$ for
every $n$. Then the weighted forward shift $S_w$ on $\ell^2(\mathbb{N}, \mathbb{K})$, given by
$(S_w x)_0 = 0$ and $(S_w x)_{n+1} = w_n x_n$, satisfies $\|S_w x\| = \|x\|$ for every
$x \in \ell^2(\mathbb{N}, \mathbb{K})$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WeightedShiftOperator.norm_weightedShiftCLM_apply_of_forall_norm_eq_one`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean, line 319](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean#L319). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/weighted-shifts/index.html#norm-weighted-shift-clm-apply-of-forall).

## Isometric weighted shifts

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$ and let
$(w_n)_{n \in \mathbb{N}}$ be a bounded sequence in $\mathbb{K}$. The weighted forward shift
$S_w$ on $\ell^2(\mathbb{N}, \mathbb{K})$, given by $(S_w x)_0 = 0$ and
$(S_w x)_{n+1} = w_n x_n$, is an isometry if and only if $|w_n| = 1$ for every $n$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WeightedShiftOperator.isometry_weightedShiftCLM_iff`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean, line 338](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean#L338). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/weighted-shifts/index.html#isometry-weighted-shift-clm-iff).

## The weighted forward shift with unit weights is the unilateral shift

Let $\mathbb{K}$ be
$\mathbb{R}$ or $\mathbb{C}$. The weighted forward shift operator on
$\ell^2(\mathbb{N}, \mathbb{K})$ whose weights are all equal to $1$ is the unilateral forward
shift on $\ell^2(\mathbb{N}, \mathbb{K})$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WeightedShiftOperator.weightedShiftCLM_one`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean, line 352](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean#L352). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/weighted-shifts/index.html#weighted-shift-clm-one).

## Unit weights give the plain backward shift

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$. With every weight equal to $1$, the weighted backward shift on
$\ell^2(\mathbb{N}, \mathbb{K})$ is the canonical backward shift.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WeightedShiftOperator.weightedBackwardCLM_one`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean, line 359](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WeightedShiftOperator.lean#L359). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/weighted-shifts/index.html#weighted-backward-clm-one).

## Truncated weights

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$. For a sequence
$w : \mathbb{N} \to \mathbb{K}$ and $N \in \mathbb{N}$, the truncation of $w$ after $N$ coordinates
is the sequence $w^{(N)}$ with $w^{(N)}_n = w_n$ for $n < N$ and $w^{(N)}_n = 0$ for $n \ge N$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WeightedShiftCompact.truncWeights`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/WeightedShiftCompact.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WeightedShiftCompact.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/weighted-shifts/index.html#trunc-weights).

## Truncated weights agree with the weights below the cutoff

Let $\mathbb{K}$ be
$\mathbb{R}$ or $\mathbb{C}$, let $w : \mathbb{N} \to \mathbb{K}$, and let $N, n \in \mathbb{N}$
with $n < N$. Then the truncation $w^{(N)}$ of $w$ after $N$ coordinates (equal to $w_k$ for
$k < N$ and to $0$ for $k \ge N$) satisfies $w^{(N)}_n = w_n$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WeightedShiftCompact.truncWeights_apply_lt`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WeightedShiftCompact.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WeightedShiftCompact.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/weighted-shifts/index.html#trunc-weights-apply-lt).

## Truncated weights vanish from the cutoff on

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$, let $w : \mathbb{N} \to \mathbb{K}$, and let $N, n \in \mathbb{N}$ with $n \ge N$.
Then the truncation $w^{(N)}$ of $w$ after $N$ coordinates (equal to $w_k$ for $k < N$ and to $0$
for $k \ge N$) satisfies $w^{(N)}_n = 0$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WeightedShiftCompact.truncWeights_apply_ge`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WeightedShiftCompact.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WeightedShiftCompact.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/weighted-shifts/index.html#trunc-weights-apply-ge).

## Truncated weights are bounded

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$, let
$w : \mathbb{N} \to \mathbb{K}$ be bounded, that is, $|w_n| \le C$ for all $n$ for some constant
$C$, and let $N \in \mathbb{N}$. Then the truncation $w^{(N)}$ of $w$ after $N$ coordinates, given
by $w^{(N)}_n = w_n$ for $n < N$ and $w^{(N)}_n = 0$ for $n \ge N$, is bounded as well.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WeightedShiftCompact.bddAbove_truncWeights`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WeightedShiftCompact.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WeightedShiftCompact.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/weighted-shifts/index.html#bdd-above-trunc-weights).

## Differences of bounded sequences are bounded

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$, and let $w, v : \mathbb{N} \to \mathbb{K}$ be bounded sequences, that is, there are
constants $C$ and $D$ with $|w_n| \le C$ and $|v_n| \le D$ for all $n$. Then $w - v$ is bounded:
there is a constant $E$ with $|w_n - v_n| \le E$ for all $n$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WeightedShiftCompact.bddAbove_sub`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WeightedShiftCompact.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WeightedShiftCompact.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/weighted-shifts/index.html#bdd-above-sub).

## Weighted shift of a difference of weights

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$, and let $w, v : \mathbb{N} \to \mathbb{K}$ be sequences such that $w$, $v$ and $w - v$
are bounded. Writing $S_u$ for the weighted forward shift on $\ell^2(\mathbb{N}, \mathbb{K})$ with
bounded weights $u$, sending $x$ to $(0, u_0 x_0, u_1 x_1, \dots)$, we have
$S_{w - v} = S_w - S_v$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WeightedShiftCompact.weightedShiftCLM_sub`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WeightedShiftCompact.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WeightedShiftCompact.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/weighted-shifts/index.html#weighted-shift-clm-sub).

## Weighted shifts with truncated weights converge in operator norm

Let $\mathbb{K}$ be
$\mathbb{R}$ or $\mathbb{C}$ and let $w : \mathbb{N} \to \mathbb{K}$ be a bounded sequence with
$w_n \to 0$. For $N \in \mathbb{N}$ let $w^{(N)}$ be the truncation of $w$ after $N$ coordinates,
with $w^{(N)}_n = w_n$ for $n < N$ and $w^{(N)}_n = 0$ for $n \ge N$, and for bounded weights $u$
let $S_u$ be the weighted forward shift on $\ell^2(\mathbb{N}, \mathbb{K})$, sending $x$ to
$(0, u_0 x_0, u_1 x_1, \dots)$. Then $S_{w^{(N)}} \to S_w$ in operator norm as $N \to \infty$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WeightedShiftCompact.tendsto_weightedShiftCLM_trunc`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WeightedShiftCompact.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WeightedShiftCompact.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/weighted-shifts/index.html#tendsto-weighted-shift-clm-trunc).

## Compactness criterion for weighted shifts

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$
and let $w : \mathbb{N} \to \mathbb{K}$ be a bounded sequence of weights, that is, $|w_n| \le C$
for all $n$ for some constant $C$. The weighted forward shift $S_w$ on
$\ell^2(\mathbb{N}, \mathbb{K})$, which sends $x$ to $(0, w_0 x_0, w_1 x_1, \dots)$, is a compact
operator if and only if $w_n \to 0$ as $n \to \infty$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WeightedShiftCompact.isCompactOperator_weightedShiftCLM_iff`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WeightedShiftCompact.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WeightedShiftCompact.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/weighted-shifts/index.html#is-compact-operator-weighted-shift-clm-i).

## Weighted shifts with eventually vanishing weights are compact

Let $\mathbb{K}$ be
$\mathbb{R}$ or $\mathbb{C}$, let $w : \mathbb{N} \to \mathbb{K}$ be a bounded sequence of weights,
and suppose there is $N \in \mathbb{N}$ with $w_n = 0$ for all $n \ge N$. Then the weighted forward
shift $S_w$ on $\ell^2(\mathbb{N}, \mathbb{K})$, which sends $x$ to $(0, w_0 x_0, w_1 x_1, \dots)$,
is a compact operator.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WeightedShiftCompact.isCompactOperator_weightedShift_of_forall_eq_zero`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WeightedShiftCompact.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/WeightedShiftCompact.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/weighted-shifts/index.html#is-compact-operator-weighted-shift-of-fo).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Weighted shifts](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/weighted-shifts/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/weighted-shifts)
