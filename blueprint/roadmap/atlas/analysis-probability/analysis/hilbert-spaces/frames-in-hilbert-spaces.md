---
declaration: section
origin: cited
lean: MathlibExt.Analysis.InnerProductSpace.FiniteFrame.IsFrame, MathlibExt.Analysis.InnerProductSpace.FiniteFrame.IsFrame.pos_left, MathlibExt.Analysis.InnerProductSpace.FiniteFrame.IsFrame.pos_right, MathlibExt.Analysis.InnerProductSpace.FiniteFrame.IsFrame.lower, MathlibExt.Analysis.InnerProductSpace.FiniteFrame.IsFrame.upper, MathlibExt.Analysis.InnerProductSpace.FiniteFrame.frameOperator, MathlibExt.Analysis.InnerProductSpace.FiniteFrame.frameOperator_apply, MathlibExt.Analysis.InnerProductSpace.FiniteFrame.inner_frameOperator_apply
statement: formalized
proof: formalized
---

# Frames in Hilbert spaces

24 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/frames-in-hilbert-spaces/index.html).

## Finite frame

Let $E$ be an inner product space over $\mathbb{K} = \mathbb{R}$ or
$\mathbb{C}$. A finite family $(f_i)_{i \in \iota}$ in $E$ is a frame with frame bounds
$A, B \in \mathbb{R}$ if $A > 0$, $B > 0$ and, for every $x \in E$,
$A \|x\|^2 \le \sum_{i \in \iota} |\langle f_i, x \rangle|^2 \le B \|x\|^2$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.FiniteFrame.IsFrame`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/FiniteFrame.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FiniteFrame.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/frames-in-hilbert-spaces/index.html#is-frame).

## The lower frame bound is positive

Let $E$ be an inner product space over
$\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$. If a finite family $(f_i)_{i \in \iota}$ in $E$ is a
frame with frame bounds $A$ and $B$, then $A > 0$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.FiniteFrame.IsFrame.pos_left`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/FiniteFrame.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FiniteFrame.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/frames-in-hilbert-spaces/index.html#pos-left).

## The upper frame bound is positive

If a finite family $(f_i)_{i \in \iota}$ in an inner
product space $E$ over $\mathbb{K}$ ($\mathbb{R}$ or $\mathbb{C}$) is a frame with frame bounds $A$
and $B$, then $0 < B$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.FiniteFrame.IsFrame.pos_right`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/FiniteFrame.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FiniteFrame.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/frames-in-hilbert-spaces/index.html#pos-right).

## Lower frame inequality

Let $E$ be an inner product space over $\mathbb{K} = \mathbb{R}$
or $\mathbb{C}$ and let $(f_i)_{i \in \iota}$ be a finite frame in $E$ with frame bounds $A$ and
$B$. Then $A \|x\|^2 \le \sum_{i \in \iota} |\langle f_i, x \rangle|^2$ for every $x \in E$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.FiniteFrame.IsFrame.lower`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/FiniteFrame.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FiniteFrame.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/frames-in-hilbert-spaces/index.html#lower).

## Upper frame inequality

If a finite family $(f_i)_{i \in \iota}$ in an inner product space
$E$ over $\mathbb{K}$ ($\mathbb{R}$ or $\mathbb{C}$) is a frame with frame bounds $A$ and $B$, then
$\sum_{i} |\langle f_i, x \rangle|^2 \le B \|x\|^2$ for every $x \in E$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.FiniteFrame.IsFrame.upper`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/FiniteFrame.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FiniteFrame.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/frames-in-hilbert-spaces/index.html#upper).

## Frame operator

For a finite family $(f_i)_{i \in \iota}$ in an inner product space $E$
over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, the frame operator is the bounded linear operator
$S \colon E \to E$ given by $S x = \sum_{i \in \iota} \langle f_i, x \rangle f_i$, the sum of the
rank-one operators $x \mapsto \langle f_i, x \rangle f_i$. The inner product is conjugate-linear
in its first argument.

Formalized by `MathlibExt.Analysis.InnerProductSpace.FiniteFrame.frameOperator`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/FiniteFrame.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FiniteFrame.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/frames-in-hilbert-spaces/index.html#frame-operator).

## Frame operator formula

For a finite family $(f_i)_{i \in \iota}$ in an inner product
space $E$ over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, the frame operator $S$ of the family
satisfies $S x = \sum_{i \in \iota} \langle f_i, x \rangle f_i$ for every $x \in E$, where the
inner product is conjugate-linear in its first argument.

Formalized by `MathlibExt.Analysis.InnerProductSpace.FiniteFrame.frameOperator_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/FiniteFrame.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FiniteFrame.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/frames-in-hilbert-spaces/index.html#frame-operator-apply).

## Inner product against the frame operator

Let $E$ be an inner product space over
$\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, with inner product conjugate-linear in the first
argument, and let $S$ be the frame operator of a finite family $(f_i)_{i \in \iota}$ in $E$. Then
$\langle S x, y \rangle = \sum_{i \in \iota} \overline{\langle f_i, x \rangle} \,
\langle f_i, y \rangle$ for all $x, y \in E$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.FiniteFrame.inner_frameOperator_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/FiniteFrame.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FiniteFrame.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/frames-in-hilbert-spaces/index.html#inner-frame-operator-apply).

## Quadratic form of the frame operator

Let $S$ be the frame operator of a finite family
$(f_i)_{i \in \iota}$ in an inner product space $E$ over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$.
For every $x \in E$,
$\langle S x, x \rangle = \sum_{i \in \iota} |\langle f_i, x \rangle|^2$; the right side is a
real number, viewed as an element of $\mathbb{K}$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.FiniteFrame.inner_frameOperator_apply_self`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/FiniteFrame.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FiniteFrame.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/frames-in-hilbert-spaces/index.html#inner-frame-operator-apply-self).

## Real part of the frame quadratic form

Let $(f_i)_{i \in \iota}$ be a finite family in an
inner product space $E$ over $\mathbb{K}$ ($\mathbb{R}$ or $\mathbb{C}$), with frame operator $S$.
For every $x \in E$,
$\operatorname{Re} \langle S x, x \rangle = \sum_{i} |\langle f_i, x \rangle|^2$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.FiniteFrame.re_inner_frameOperator_apply_self`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/FiniteFrame.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FiniteFrame.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/frames-in-hilbert-spaces/index.html#re-inner-frame-operator-apply-self).

## Cauchy–Schwarz bound for the frame operator

Let $(f_i)_{i \in \iota}$ be a finite family in
an inner product space $E$ over $\mathbb{K}$ ($\mathbb{R}$ or $\mathbb{C}$), with frame operator
$S$. For all $x, y \in E$,

$$
|\langle S x, y \rangle|^2 \le \Big(\sum_{i} |\langle f_i, x \rangle|^2\Big)
\Big(\sum_{i} |\langle f_i, y \rangle|^2\Big).
$$

Formalized by `MathlibExt.Analysis.InnerProductSpace.FiniteFrame.sq_norm_inner_frameOperator_apply_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/FiniteFrame.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FiniteFrame.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/frames-in-hilbert-spaces/index.html#sq-norm-inner-frame-operator-apply-le).

## The frame operator is self-adjoint

Let $E$ be a Hilbert space over
$\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$. For every finite family $(f_i)_{i \in \iota}$ in $E$,
not necessarily a frame, the frame operator of $(f_i)_{i \in \iota}$ is self-adjoint.

Formalized by `MathlibExt.Analysis.InnerProductSpace.FiniteFrame.isSelfAdjoint_frameOperator`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/FiniteFrame.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FiniteFrame.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/frames-in-hilbert-spaces/index.html#is-self-adjoint-frame-operator).

## The frame operator is bounded below

Let $E$ be an inner product space over
$\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$ and let $(f_i)_{i \in \iota}$ be a finite frame in $E$
with frame bounds $A$ and $B$ and frame operator $S$. Then $A \|x\| \le \|S x\|$ for every
$x \in E$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.FiniteFrame.le_norm_frameOperator_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/FiniteFrame.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FiniteFrame.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/frames-in-hilbert-spaces/index.html#le-norm-frame-operator-apply).

## The frame operator of a frame is invertible

Let $E$ be a Hilbert space over
$\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$ and let $(f_i)_{i \in \iota}$ be a finite frame in $E$
with frame bounds $A$ and $B$. Then its frame operator $S$ is a unit in the algebra of bounded
linear operators on $E$, that is, $S$ has a bounded linear two-sided inverse.

The operator $S$ is bounded below and self-adjoint, so it is injective with closed range whose
orthogonal complement is trivial.

Formalized by `MathlibExt.Analysis.InnerProductSpace.FiniteFrame.isUnit_frameOperator`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/FiniteFrame.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FiniteFrame.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/frames-in-hilbert-spaces/index.html#is-unit-frame-operator).

## The frame operator has norm at most the upper frame bound

Let $E$ be an inner product
space over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$ and let $(f_i)_{i \in \iota}$ be a finite
frame in $E$ with frame bounds $A$ and $B$ and frame operator $S$. Then the operator norm of $S$
satisfies $\|S\| \le B$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.FiniteFrame.norm_frameOperator_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/FiniteFrame.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FiniteFrame.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/frames-in-hilbert-spaces/index.html#norm-frame-operator-le).

## Inverse frame operator

Let $(f_i)_{i \in \iota}$, with $\iota$ finite, be a frame with
bounds $A$ and $B$ in a Hilbert space $E$ over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$. Its frame
operator $S$ is invertible in the algebra of bounded linear operators on $E$, and the inverse
frame operator $S^{-1}$ is its inverse there.

Formalized by `MathlibExt.Analysis.InnerProductSpace.FiniteFrame.frameOperatorInv`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/FiniteFrame.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FiniteFrame.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/frames-in-hilbert-spaces/index.html#frame-operator-inv).

## The inverse frame operator is a right inverse

Let $(f_i)_{i \in \iota}$, with $\iota$
finite, be a frame with bounds $A$ and $B$ in a Hilbert space $E$ over $\mathbb{K} = \mathbb{R}$ or
$\mathbb{C}$, with frame operator $S$ and inverse frame operator $S^{-1}$. Then
$S \circ S^{-1}$ is the identity operator on $E$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.FiniteFrame.frameOperator_comp_frameOperatorInv`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/FiniteFrame.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FiniteFrame.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/frames-in-hilbert-spaces/index.html#frame-operator-comp-frame-operator-inv).

## The inverse frame operator is a left inverse

Let $(f_i)_{i \in \iota}$, with $\iota$
finite, be a frame with bounds $A$ and $B$ in a Hilbert space $E$ over $\mathbb{K} = \mathbb{R}$ or
$\mathbb{C}$, with frame operator $S$ and inverse frame operator $S^{-1}$. Then
$S^{-1} \circ S$ is the identity operator on $E$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.FiniteFrame.frameOperatorInv_comp_frameOperator`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/FiniteFrame.lean, line 270](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FiniteFrame.lean#L270). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/frames-in-hilbert-spaces/index.html#frame-operator-inv-comp-frame-operator).

## The inverse frame operator is self-adjoint

Let $E$ be a Hilbert space over
$\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$ and let $(f_i)_{i \in \iota}$ be a finite frame in $E$
with frame bounds $A$ and $B$. Then the inverse $S^{-1}$ of its frame operator $S$ is
self-adjoint.

Formalized by `MathlibExt.Analysis.InnerProductSpace.FiniteFrame.isSelfAdjoint_frameOperatorInv`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/FiniteFrame.lean, line 281](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FiniteFrame.lean#L281). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/frames-in-hilbert-spaces/index.html#is-self-adjoint-frame-operator-inv).

## Frame reconstruction formula

Let $(f_i)_{i \in \iota}$, with $\iota$ finite, be a frame
with bounds $A$ and $B$ in a Hilbert space $E$ over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, and
let $S^{-1}$ be the inverse of its frame operator. Then every $x \in E$ satisfies
$x = \sum_{i \in \iota} \langle f_i, S^{-1} x \rangle f_i$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.FiniteFrame.frame_reconstruction`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/FiniteFrame.lean, line 306](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FiniteFrame.lean#L306). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/frames-in-hilbert-spaces/index.html#frame-reconstruction).

## Canonical dual frame

Let $(f_i)_{i \in \iota}$, with $\iota$ finite, be a frame with
bounds $A$ and $B$ in a Hilbert space $E$ over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, and let
$S^{-1}$ be the inverse of its frame operator. The canonical dual frame is the family
$(S^{-1} f_i)_{i \in \iota}$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.FiniteFrame.dualFrame`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/FiniteFrame.lean, line 317](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FiniteFrame.lean#L317). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/frames-in-hilbert-spaces/index.html#dual-frame).

## Frame operator of the canonical dual frame

Let $(f_i)_{i \in \iota}$, with $\iota$
finite, be a frame with bounds $A$ and $B$ in a Hilbert space $E$ over $\mathbb{K} = \mathbb{R}$ or
$\mathbb{C}$, and let $S^{-1}$ be the inverse of its frame operator. Then the frame operator of
the canonical dual frame $(S^{-1} f_i)_{i \in \iota}$ is $S^{-1}$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.FiniteFrame.frameOperator_dualFrame`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/FiniteFrame.lean, line 322](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FiniteFrame.lean#L322). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/frames-in-hilbert-spaces/index.html#frame-operator-dual-frame).

## The canonical dual frame is a frame

Let $E$ be a Hilbert space over
$\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$ and let $(f_i)_{i \in \iota}$ be a finite frame in $E$
with frame bounds $A$ and $B$ and frame operator $S$. Then the canonical dual frame
$(S^{-1} f_i)_{i \in \iota}$ is a frame with lower frame bound $1/B$ and upper frame bound $1/A$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.FiniteFrame.isFrame_dualFrame`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/FiniteFrame.lean, line 343](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FiniteFrame.lean#L343). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/frames-in-hilbert-spaces/index.html#is-frame-dual-frame).

## Tight frames have scalar frame operator

Let $(f_i)_{i \in \iota}$, with $\iota$
finite, be a frame in a Hilbert space $E$ over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$ whose lower
and upper frame bounds are both equal to $A$. Then its frame operator is $S = A \cdot I$, where $I$
is the identity operator on $E$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.FiniteFrame.frameOperator_eq_smul_one_of_isTightFrame`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/FiniteFrame.lean, line 437](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FiniteFrame.lean#L437). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/frames-in-hilbert-spaces/index.html#frame-operator-eq-smul-one-of-is-tight-f).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Frames in Hilbert spaces](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/frames-in-hilbert-spaces/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/hilbert-spaces/frames-in-hilbert-spaces)
