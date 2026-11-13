---
declaration: section
origin: cited
lean: MathlibExt.Analysis.InnerProductSpace.HilbertBasisDiagonal.diagonalOperator, MathlibExt.Analysis.InnerProductSpace.HilbertBasisDiagonal.repr_diagonalOperator_apply, MathlibExt.Analysis.InnerProductSpace.HilbertBasisDiagonal.diagonalOperator_eq_tsum, MathlibExt.Analysis.InnerProductSpace.HilbertBasisDiagonal.diagonalOperator_apply_basis, MathlibExt.Analysis.InnerProductSpace.HilbertBasisDiagonal.diagonalOperator_sq, MathlibExt.Analysis.InnerProductSpace.LpDiagonalOperator.lp_smul_apply, MathlibExt.Analysis.InnerProductSpace.LpDiagonalOperator.memℓp_diagonal, MathlibExt.Analysis.InnerProductSpace.LpDiagonalOperator.diagonalCLM
statement: formalized
proof: formalized
---

# Diagonal operators

27 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/diagonal-operators/index.html).

## Bounded diagonal operator on a Hilbert basis

The bounded diagonal continuous linear map with coefficients `a` in the
Hilbert basis `b`. Its uniform coefficient bound is part of the constructor.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertBasisDiagonal.diagonalOperator`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/HilbertBasisDiagonal.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/HilbertBasisDiagonal.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/diagonal-operators/index.html#diagonal-operator).

## Coordinates of a diagonal operator

Let $(b_i)_{i \in \iota}$ be a Hilbert basis of an inner
product space $H$ over $\mathbb{K}$ ($\mathbb{R}$ or $\mathbb{C}$), with inner product
$\langle \cdot, \cdot \rangle$ conjugate-linear in the first argument, let
$a : \iota \to \mathbb{K}$ satisfy $|a_i| \le C$ for all $i$, and let $D$ be the diagonal operator
with coefficients $a$. For every $x \in H$ and $i \in \iota$, the $i$-th coordinate of $D x$ in
$\ell^2(\iota)$ with respect to the basis $(b_i)$ is $a_i \langle b_i, x \rangle$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertBasisDiagonal.repr_diagonalOperator_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertBasisDiagonal.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/HilbertBasisDiagonal.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/diagonal-operators/index.html#repr-diagonal-operator-apply).

## Series formula for a diagonal operator

Let $(b_i)_{i \in \iota}$ be a Hilbert basis of an
inner product space $H$ over $\mathbb{K}$ ($\mathbb{R}$ or $\mathbb{C}$), with inner product
$\langle \cdot, \cdot \rangle$ conjugate-linear in the first argument, and let
$a : \iota \to \mathbb{K}$ satisfy $|a_i| \le C$ for all $i$. The diagonal operator $D$ with
coefficients $a$ satisfies, for every $x \in H$,

$$
D x = \sum_{i \in \iota} a_i \langle b_i, x \rangle \, b_i,
$$

where the sum is the unconditional sum over $\iota$ (taken to be $0$ if the family is not
summable).

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertBasisDiagonal.diagonalOperator_eq_tsum`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertBasisDiagonal.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/HilbertBasisDiagonal.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/diagonal-operators/index.html#diagonal-operator-eq-tsum).

## Action of a diagonal operator on the basis

Let $(b_i)_{i \in \iota}$ be a Hilbert
basis of an inner product space $H$ over $\mathbb{K}$ ($\mathbb{R}$ or $\mathbb{C}$), let
$a : \iota \to \mathbb{K}$ satisfy $|a_i| \le C$ for all $i$, and let $D$ be the diagonal
operator with coefficients $a$. Then $D b_j = a_j b_j$ for every $j \in \iota$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertBasisDiagonal.diagonalOperator_apply_basis`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertBasisDiagonal.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/HilbertBasisDiagonal.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/diagonal-operators/index.html#diagonal-operator-apply-basis).

## Square of a diagonal operator

Let $(b_i)_{i \in \iota}$ be a Hilbert basis of an
inner product space $H$ over $\mathbb{K}$ ($\mathbb{R}$ or $\mathbb{C}$), and let
$a : \iota \to \mathbb{K}$ satisfy $|a_i| \le C$ for all $i$. Let $D_a$ be the diagonal
operator with coefficients $a$, and let $D_{a^2}$ be the diagonal operator with coefficients
$a_i^2$, which satisfy $|a_i^2| \le C^2$. Then $D_a(D_a x) = D_{a^2} x$ for every
$x \in H$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertBasisDiagonal.diagonalOperator_sq`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertBasisDiagonal.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/HilbertBasisDiagonal.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/diagonal-operators/index.html#diagonal-operator-sq).

## Scalar multiplication on $\ell^2$ is pointwise

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$. For every $c \in \mathbb{K}$, every $x \in \ell^2(\iota, \mathbb{K})$ and every
$i \in \iota$, the $i$-th coordinate of $c x$ is $(c x)_i = c \, x_i$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpDiagonalOperator.lp_smul_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpDiagonalOperator.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/LpDiagonalOperator.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/diagonal-operators/index.html#lp-smul-apply).

## Bounded multipliers preserve $\ell^2$

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$. If
$a : \iota \to \mathbb{K}$ is bounded, that is, $|a_i| \le C$ for some real $C$ and all $i$, then
for every $x \in \ell^2(\iota, \mathbb{K})$ the sequence $(a_i x_i)_{i \in \iota}$ lies in
$\ell^2(\iota, \mathbb{K})$, that is, the family $(|a_i x_i|^2)_{i \in \iota}$ is summable.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpDiagonalOperator.memℓp_diagonal`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpDiagonalOperator.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/LpDiagonalOperator.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/diagonal-operators/index.html#mem-p-diagonal).

## Diagonal operator on ℓ²

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$, let $\iota$ be
a type and let $a : \iota \to \mathbb{K}$ be a bounded sequence, that is, $\|a_i\| \le C$ for some
real $C$ and all $i \in \iota$. The diagonal operator $D_a$ with coefficients $a$ is the bounded
linear operator on $\ell^2(\iota, \mathbb{K})$ that sends $x$ to the sequence
$(a_i x_i)_{i \in \iota}$.

It is defined as the Hilbert-basis diagonal operator for the standard Hilbert basis of
$\ell^2(\iota, \mathbb{K})$, using the bound $\max(C, 0)$ for a chosen bound $C$, so that empty
index types also admit a nonnegative bound.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpDiagonalOperator.diagonalCLM`, an abbreviation declared in [MathlibExt/Analysis/InnerProductSpace/LpDiagonalOperator.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/LpDiagonalOperator.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/diagonal-operators/index.html#diagonal-clm).

## Coordinates of a diagonal operator on ℓ²

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$, let $\iota$ be a type, let $a : \iota \to \mathbb{K}$ be a bounded sequence and let
$D_a$ be the diagonal operator on $\ell^2(\iota, \mathbb{K})$ with coefficients $a$. For every
$x \in \ell^2(\iota, \mathbb{K})$ and every $i \in \iota$, the $i$-th coordinate of $D_a x$ is
$a_i x_i$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpDiagonalOperator.diagonalCLM_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpDiagonalOperator.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/LpDiagonalOperator.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/diagonal-operators/index.html#diagonal-clm-apply).

## Diagonal operator on ℓ² as a linear map

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$, let $\iota$ be a type and let $a : \iota \to \mathbb{K}$ be a bounded sequence. This
is the diagonal operator on $\ell^2(\iota, \mathbb{K})$ with coefficients $a$, regarded as a
$\mathbb{K}$-linear map $\ell^2(\iota, \mathbb{K}) \to \ell^2(\iota, \mathbb{K})$ by forgetting
its continuity.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpDiagonalOperator.diagonalLinMap`, an abbreviation declared in [MathlibExt/Analysis/InnerProductSpace/LpDiagonalOperator.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/LpDiagonalOperator.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/diagonal-operators/index.html#diagonal-lin-map).

## Coordinates of the diagonal linear map on ℓ²

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$, let $\iota$ be a type and let $a : \iota \to \mathbb{K}$ be a bounded sequence. For
every $x \in \ell^2(\iota, \mathbb{K})$ and every $i \in \iota$, the diagonal operator with
coefficients $a$, regarded as a linear map, sends $x$ to a sequence whose $i$-th coordinate is
$a_i x_i$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpDiagonalOperator.diagonalLinMap_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpDiagonalOperator.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/LpDiagonalOperator.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/diagonal-operators/index.html#diagonal-lin-map-apply).

## Pointwise bound for diagonal operators

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$,
let $a : \iota \to \mathbb{K}$ be bounded, and let $D_a$ be the diagonal operator
$x \mapsto (a_i x_i)_{i \in \iota}$ on $\ell^2(\iota, \mathbb{K})$, viewed as a linear map. If
$C \ge 0$ and $|a_i| \le C$ for every $i \in \iota$, then $\|D_a x\| \le C \|x\|$ for every
$x \in \ell^2(\iota, \mathbb{K})$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpDiagonalOperator.norm_diagonalLinMap_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpDiagonalOperator.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/LpDiagonalOperator.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/diagonal-operators/index.html#norm-diagonal-lin-map-le).

## Diagonal operators on standard basis vectors

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$, let $\iota$ be a type, let $a : \iota \to \mathbb{K}$ be a bounded sequence and let
$D_a$ be the diagonal operator on $\ell^2(\iota, \mathbb{K})$ with coefficients $a$. For
$i \in \iota$ let $e_i \in \ell^2(\iota, \mathbb{K})$ be the sequence equal to $1$ at $i$ and $0$
elsewhere. Then for every $i \in \iota$ and every $c \in \mathbb{K}$ we have
$D_a(c\,e_i) = a_i \, (c\,e_i)$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpDiagonalOperator.diagonalCLM_single`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpDiagonalOperator.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/LpDiagonalOperator.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/diagonal-operators/index.html#diagonal-clm-single).

## The diagonal operator with all coefficients one is the identity

Let $\mathbb{K}$ be
$\mathbb{R}$ or $\mathbb{C}$ and let $\iota$ be a type. The diagonal operator on
$\ell^2(\iota, \mathbb{K})$ whose coefficients all equal $1$ is the identity operator.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpDiagonalOperator.diagonalCLM_one`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpDiagonalOperator.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/LpDiagonalOperator.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/diagonal-operators/index.html#diagonal-clm-one).

## Composition of diagonal operators

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$, let
$\iota$ be a type, and for a bounded sequence $c : \iota \to \mathbb{K}$ let $D_c$ be the diagonal
operator on $\ell^2(\iota, \mathbb{K})$ with coefficients $c$. For bounded sequences
$a, b : \iota \to \mathbb{K}$, we have $D_b \circ D_a = D_{ba}$, where $ba$ is the pointwise
product $i \mapsto b_i a_i$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpDiagonalOperator.diagonalCLM_comp`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpDiagonalOperator.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/LpDiagonalOperator.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/diagonal-operators/index.html#diagonal-clm-comp).

## Difference of diagonal operators

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$, let
$\iota$ be a type, and for a bounded sequence $c : \iota \to \mathbb{K}$ let $D_c$ be the diagonal
operator on $\ell^2(\iota, \mathbb{K})$ with coefficients $c$. For bounded sequences
$a, b : \iota \to \mathbb{K}$, we have $D_a - D_b = D_{a - b}$, where $a - b$ is the sequence
$i \mapsto a_i - b_i$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpDiagonalOperator.diagonalCLM_sub`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpDiagonalOperator.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/LpDiagonalOperator.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/diagonal-operators/index.html#diagonal-clm-sub).

## Operator norm bound for diagonal operators

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$, let $a : \iota \to \mathbb{K}$ be bounded, and let $D_a$ be the diagonal operator
$x \mapsto (a_i x_i)_{i \in \iota}$ on $\ell^2(\iota, \mathbb{K})$. If $C \ge 0$ and $|a_i| \le C$
for every $i \in \iota$, then the operator norm satisfies $\|D_a\| \le C$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpDiagonalOperator.norm_diagonalCLM_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpDiagonalOperator.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/LpDiagonalOperator.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/diagonal-operators/index.html#norm-diagonal-clm-le).

## Operator norm of a diagonal operator

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$, let
$a : \iota \to \mathbb{K}$ be bounded, and let $D_a$ be the diagonal operator
$x \mapsto (a_i x_i)_{i \in \iota}$ on $\ell^2(\iota, \mathbb{K})$. Then the operator norm of $D_a$
is $\|D_a\| = \sup_{i \in \iota} |a_i|$, where the supremum is taken to be $0$ when $\iota$ is
empty.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpDiagonalOperator.norm_diagonalCLM`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpDiagonalOperator.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/LpDiagonalOperator.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/diagonal-operators/index.html#norm-diagonal-clm).

## Adjoint of a diagonal operator

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$, let
$\iota$ be a type and let $a : \iota \to \mathbb{K}$ be a bounded sequence. The adjoint of the
diagonal operator $D_a$ on $\ell^2(\iota, \mathbb{K})$ with coefficients $a$ is the diagonal
operator with the conjugate coefficients $i \mapsto \overline{a_i}$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpDiagonalOperator.adjoint_diagonalCLM`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpDiagonalOperator.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/LpDiagonalOperator.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/diagonal-operators/index.html#adjoint-diagonal-clm).

## Self-adjoint diagonal operators on $\ell^2$

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$, let $a : \iota \to \mathbb{K}$ be bounded, and let $D_a$ be the diagonal operator
$x \mapsto (a_i x_i)_{i \in \iota}$ on $\ell^2(\iota, \mathbb{K})$. Then $D_a$ is self-adjoint if
and only if $\overline{a_i} = a_i$, that is, $a_i$ is real, for every $i \in \iota$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpDiagonalOperator.isSelfAdjoint_diagonalCLM_iff`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpDiagonalOperator.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/LpDiagonalOperator.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/diagonal-operators/index.html#is-self-adjoint-diagonal-clm-iff).

## Rank-one term of the finite-support decomposition on $\ell^2$

A rank-one term of the finite-support decomposition, evaluated pointwise.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpDiagonalOperator.singleCLM_comp_evalCLM_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpDiagonalOperator.lean, line 276](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/LpDiagonalOperator.lean#L276). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/diagonal-operators/index.html#single-clm-comp-eval-clm-apply).

## Compact diagonal operators on ℓ²

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$, let
$\iota$ be a type and let $a : \iota \to \mathbb{K}$ be a bounded sequence. The diagonal operator
on $\ell^2(\iota, \mathbb{K})$ with coefficients $a$ is compact if and only if $a$ tends to $0$
along the cofinite filter on $\iota$, that is, for every $\varepsilon > 0$ only finitely many
$i \in \iota$ satisfy $\|a_i\| \ge \varepsilon$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpDiagonalOperator.isCompactOperator_diagonalCLM_iff`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpDiagonalOperator.lean, line 476](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/LpDiagonalOperator.lean#L476). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/diagonal-operators/index.html#is-compact-operator-diagonal-clm-iff).

## Shifting a diagonal operator by a scalar

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$, let $a : \iota \to \mathbb{K}$ be a bounded family of coefficients, let $D_a$ be the
diagonal operator on $\ell^2(\iota, \mathbb{K})$ given by $(D_a x)_i = a_i x_i$, and let $I$ be
the identity operator. For every $\mu \in \mathbb{K}$, $\mu I - D_a = D_{\mu - a}$, the diagonal
operator with coefficients $\mu - a_i$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpDiagonalOperatorSpectrum.smul_one_sub_diagonalCLM_eq`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpDiagonalOperatorSpectrum.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/LpDiagonalOperatorSpectrum.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/diagonal-operators/index.html#smul-one-sub-diagonal-clm-eq).

## Invertibility of a shifted diagonal operator

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$, let $a : \iota \to \mathbb{K}$ be a bounded family of coefficients, let $D_a$ be the
diagonal operator on $\ell^2(\iota, \mathbb{K})$ given by $(D_a x)_i = a_i x_i$, and let $I$ be
the identity operator. If $\mu \in \mathbb{K}$ does not lie in the closure of
$\{a_i : i \in \iota\}$, then $\mu I - D_a$ is invertible in the algebra of bounded operators on
$\ell^2(\iota, \mathbb{K})$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpDiagonalOperatorSpectrum.isUnit_smul_one_sub_diagonalCLM_of_not_mem_closure_range`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpDiagonalOperatorSpectrum.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/LpDiagonalOperatorSpectrum.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/diagonal-operators/index.html#is-unit-smul-one-sub-diagonal-clm-of-not).

## Points off the closure of the coefficients are not in the spectrum

Let $\mathbb{K}$ be
$\mathbb{R}$ or $\mathbb{C}$, let $a : \iota \to \mathbb{K}$ be a bounded family of coefficients,
and let $D_a$ be the diagonal operator on $\ell^2(\iota, \mathbb{K})$ given by
$(D_a x)_i = a_i x_i$. If $\mu \in \mathbb{K}$ does not lie in the closure of
$\{a_i : i \in \iota\}$, then $\mu$ is not in the spectrum of $D_a$ over $\mathbb{K}$, that is,
$\mu I - D_a$ is invertible as a bounded operator, where $I$ is the identity operator.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpDiagonalOperatorSpectrum.not_mem_spectrum_of_not_mem_closure_range`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpDiagonalOperatorSpectrum.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/LpDiagonalOperatorSpectrum.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/diagonal-operators/index.html#not-mem-spectrum-of-not-mem-closure-rang).

## Every coefficient of a diagonal operator lies in its spectrum

Let $\mathbb{K}$ be
$\mathbb{R}$ or $\mathbb{C}$, let $a : \iota \to \mathbb{K}$ be a bounded family of coefficients,
and let $D_a$ be the diagonal operator on $\ell^2(\iota, \mathbb{K})$ given by
$(D_a x)_i = a_i x_i$. Then every $a_j$ with $j \in \iota$ lies in the spectrum of $D_a$ over
$\mathbb{K}$, the set of $\mu \in \mathbb{K}$ for which $\mu I - D_a$ is not invertible as a
bounded operator, where $I$ is the identity operator.

For each $j \in \iota$, the $j$-th coordinate vector lies in the kernel of $a_j I - D_a$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpDiagonalOperatorSpectrum.range_subset_spectrum`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpDiagonalOperatorSpectrum.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/LpDiagonalOperatorSpectrum.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/diagonal-operators/index.html#range-subset-spectrum).

## Spectrum of a diagonal operator

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$, let
$a : \iota \to \mathbb{K}$ be a bounded family of coefficients, and let $D_a$ be the diagonal
operator on $\ell^2(\iota, \mathbb{K})$ given by $(D_a x)_i = a_i x_i$. The spectrum of $D_a$ over
$\mathbb{K}$, the set of $\mu \in \mathbb{K}$ for which $\mu I - D_a$ is not invertible as a
bounded operator ($I$ the identity operator), is the closure of $\{a_i : i \in \iota\}$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.LpDiagonalOperatorSpectrum.spectrum_diagonalCLM`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/LpDiagonalOperatorSpectrum.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/LpDiagonalOperatorSpectrum.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/diagonal-operators/index.html#spectrum-diagonal-clm).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Diagonal operators](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/diagonal-operators/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/operator-theory/integral-and-multiplication/diagonal-operators)
