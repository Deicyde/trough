---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Normed.Lp.Dual.lpDualPairing, MathlibExt.Analysis.Normed.Lp.Dual.lpDualPairing_apply, MathlibExt.Analysis.Normed.Lp.Dual.norm_lpDualPairing_le, MathlibExt.Analysis.Normed.Lp.Dual.lpDualPairing_surjective, MathlibExt.Analysis.Normed.Lp.Dual.lpDualPairing_norm, MathlibExt.Analysis.Normed.Lp.Dual.lpDualEquiv, MathlibExt.Analysis.Normed.Lp.DualC0.c0Submodule, MathlibExt.Analysis.Normed.Lp.DualC0.c0
statement: formalized
proof: formalized
---

# Duals of ℓ^p and c₀

47 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c/index.html).

## Canonical duality pairing between $\ell^q$ and $\ell^p$

The canonical pairing `ℓ^q × ℓ^p → 𝕜`, as a continuous linear map
`ℓ^q →L[𝕜] (ℓ^p →L[𝕜] 𝕜)`.

Formalized by `MathlibExt.Analysis.Normed.Lp.Dual.lpDualPairing`, a definition declared in [MathlibExt/Analysis/Normed/Lp/Dual.lean, line 271](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/Dual.lean#L271). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c/index.html#lp-dual-pairing).

## Duality pairing as a sum of coordinatewise products

The pairing is given by the sum of coordinatewise products.

Formalized by `MathlibExt.Analysis.Normed.Lp.Dual.lpDualPairing_apply`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/Dual.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/Dual.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c/index.html#lp-dual-pairing-apply).

## Duality pairing has operator norm at most one

The pairing has operator norm at most one.

Formalized by `MathlibExt.Analysis.Normed.Lp.Dual.norm_lpDualPairing_le`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/Dual.lean, line 290](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/Dual.lean#L290). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c/index.html#norm-lp-dual-pairing-le).

## Every functional on $\ell^p$ comes from an $\ell^q$ sequence

The pairing is surjective: every continuous linear functional on `ℓ^p` is given
by pairing with some `ℓ^q` sequence.

Formalized by `MathlibExt.Analysis.Normed.Lp.Dual.lpDualPairing_surjective`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/Dual.lean, line 301](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/Dual.lean#L301). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c/index.html#lp-dual-pairing-surjective).

## Duality pairing is norm-preserving

The pairing is norm-preserving.

Formalized by `MathlibExt.Analysis.Normed.Lp.Dual.lpDualPairing_norm`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/Dual.lean, line 334](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/Dual.lean#L334). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c/index.html#lp-dual-pairing-norm).

## Dual of $\ell^p$ is isometric to $\ell^q$

The dual of `ℓ^p` is isometrically isomorphic to `ℓ^q`.

Formalized by `MathlibExt.Analysis.Normed.Lp.Dual.lpDualEquiv`, a definition declared in [MathlibExt/Analysis/Normed/Lp/Dual.lean, line 359](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/Dual.lean#L359). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c/index.html#lp-dual-equiv).

## The subspace of null sequences in $\ell^\infty$

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$ and let $\iota$ be an index type. The sequences $x \in \ell^\infty(\iota, \mathbb{K})$
whose coordinates $x_i$ tend to $0$ along the cofinite filter on $\iota$ form a
$\mathbb{K}$-linear subspace of $\ell^\infty(\iota, \mathbb{K})$.

Formalized by `MathlibExt.Analysis.Normed.Lp.DualC0.c0Submodule`, a definition declared in [MathlibExt/Analysis/Normed/Lp/DualC0.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/DualC0.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c/index.html#c0-submodule).

## The sequence space $c_0$

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$ and let $\iota$
be a type. The space $c_0(\iota, \mathbb{K})$ consists of the functions $x : \iota \to \mathbb{K}$
that tend to $0$ along the cofinite filter, that is, for every $\varepsilon > 0$ the set
$\{i : |x_i| \ge \varepsilon\}$ is finite, with pointwise operations and the supremum norm
$\|x\|_\infty = \sup_i |x_i|$. It is realized as the space of continuous functions vanishing at
infinity on $\iota$ with the discrete topology; no topology on $\iota$ is assumed.

Formalized by `MathlibExt.Analysis.Normed.Lp.DualC0.c0`, an abbreviation declared in [MathlibExt/Analysis/Normed/Lp/DualC0.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/DualC0.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c/index.html#c0).

## Elements of $c_0$ tend to zero along the cofinite filter

Let $\mathbb{K}$ be
$\mathbb{R}$ or $\mathbb{C}$, let $\iota$ be an index type, and let $c_0(\iota, \mathbb{K})$ be
the space of functions $\iota \to \mathbb{K}$ vanishing at infinity for the discrete
topology on $\iota$. For every $x \in c_0(\iota, \mathbb{K})$, the coordinates $x_i$ tend to
$0$ along the cofinite filter on $\iota$.

Formalized by `MathlibExt.Analysis.Normed.Lp.DualC0.c0_tendsto_zero`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/DualC0.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/DualC0.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c/index.html#c0-tendsto-zero).

## Coordinates are bounded by the norm in $c_0$

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$, and let $c_0(\iota, \mathbb{K})$ be the space of families $x = (x_i)_{i \in \iota}$ in
$\mathbb{K}$ that tend to $0$ along the cofinite filter, with the supremum norm. Then
$|x_i| \le \|x\|$ for every $x \in c_0(\iota, \mathbb{K})$ and every index $i \in \iota$.

Formalized by `MathlibExt.Analysis.Normed.Lp.DualC0.c0_apply_norm_le`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/DualC0.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/DualC0.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c/index.html#c0-apply-norm-le).

## Inclusion of $c_0$ in $\ell^\infty$

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$
and let $\iota$ be an index type. Every $x \in c_0(\iota, \mathbb{K})$ is a bounded sequence,
and this map sends it to the element of $\ell^\infty(\iota, \mathbb{K})$ with the same
coordinates $x_i$.

Formalized by `MathlibExt.Analysis.Normed.Lp.DualC0.c0ToLp`, a definition declared in [MathlibExt/Analysis/Normed/Lp/DualC0.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/DualC0.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c/index.html#c0-to-lp).

## The $c_0$ norm is the supremum norm

Let $\mathbb{K}$ be the real or complex field and
$\iota$ an index type. For every $x \in c_0(\iota, \mathbb{K})$, the norm of $x$ equals the
norm $\sup_{i \in \iota} |x_i|$ of $x$ viewed as an element of $\ell^\infty(\iota, \mathbb{K})$.

Formalized by `MathlibExt.Analysis.Normed.Lp.DualC0.c0_norm`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/DualC0.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/DualC0.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c/index.html#c0-norm).

## Sequences in $\ell^\infty$ tending to zero as elements of $c_0$

Let $\mathbb{K}$ be
$\mathbb{R}$ or $\mathbb{C}$ and let $\iota$ be an index type. A bounded sequence
$x \in \ell^\infty(\iota, \mathbb{K})$ whose coordinates $x_i$ tend to $0$ along the
cofinite filter on $\iota$ defines the element of $c_0(\iota, \mathbb{K})$ with the same
coordinates.

Formalized by `MathlibExt.Analysis.Normed.Lp.DualC0.c0OfLp`, a definition declared in [MathlibExt/Analysis/Normed/Lp/DualC0.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/DualC0.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c/index.html#c0-of-lp).

## $c_0$ is isometrically isomorphic to the null sequences in $\ell^\infty$

Let $\mathbb{K}$
be the real or complex field and $\iota$ an index type. The map that sends
$x \in c_0(\iota, \mathbb{K})$ to the same sequence $(x_i)_{i \in \iota}$, viewed in the subspace
of $\ell^\infty(\iota, \mathbb{K})$ of sequences tending to $0$ along the cofinite filter, is a
linear isometric equivalence onto that subspace.

Formalized by `MathlibExt.Analysis.Normed.Lp.DualC0.c0LpEquiv`, a definition declared in [MathlibExt/Analysis/Normed/Lp/DualC0.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/DualC0.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c/index.html#c0-lp-equiv).

## Sequence supported at one index

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$ and
let $\iota$ be an index type. For an index $i \in \iota$ and a scalar $a \in \mathbb{K}$, this
is the element of $c_0(\iota, \mathbb{K})$ whose $i$-th coordinate is $a$ and whose other
coordinates are $0$.

Formalized by `MathlibExt.Analysis.Normed.Lp.DualC0.c0Single`, a definition declared in [MathlibExt/Analysis/Normed/Lp/DualC0.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/DualC0.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c/index.html#c0-single).

## Coordinates of the sequence supported at one index

Let $\mathbb{K}$ be $\mathbb{R}$
or $\mathbb{C}$ and let $\iota$ be an index type. For indices $i, j \in \iota$ and
$a \in \mathbb{K}$, the $j$-th coordinate of the element of $c_0(\iota, \mathbb{K})$ that is
$a$ at $i$ and $0$ elsewhere equals $a$ if $j = i$ and $0$ otherwise.

Formalized by `MathlibExt.Analysis.Normed.Lp.DualC0.c0Single_apply`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/DualC0.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/DualC0.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c/index.html#c0-single-apply).

## Norm of a sequence supported at one index

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$ and let $\iota$ be an index type. For $i \in \iota$ and $a \in \mathbb{K}$, the
element of $c_0(\iota, \mathbb{K})$ that is $a$ at $i$ and $0$ elsewhere has norm $\|a\|$.

Formalized by `MathlibExt.Analysis.Normed.Lp.DualC0.c0Single_norm`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/DualC0.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/DualC0.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c/index.html#c0-single-norm).

## Finitely supported sequences in $c_0$

Let $\mathbb{K}$ be the real or complex field and
$\iota$ an index type, and let $e_i \in c_0(\iota, \mathbb{K})$ be the sequence equal to $1$ at
$i$ and $0$ elsewhere. For a finite set $s \subseteq \iota$ and $c : \iota \to \mathbb{K}$, the
finitely supported sequence with coefficients $c$ on $s$ is the element
$\sum_{i \in s} c_i e_i$ of $c_0(\iota, \mathbb{K})$.

Formalized by `MathlibExt.Analysis.Normed.Lp.DualC0.c0FinsetSum`, a definition declared in [MathlibExt/Analysis/Normed/Lp/DualC0.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/DualC0.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c/index.html#c0-finset-sum).

## Coordinates of a finitely supported sequence

Let $\mathbb{K}$ be the real or complex
field and $\iota$ an index type, and let $e_i \in c_0(\iota, \mathbb{K})$ be the sequence equal
to $1$ at $i$ and $0$ elsewhere. For every finite set $s \subseteq \iota$, every
$c : \iota \to \mathbb{K}$ and every $j \in \iota$, the $j$-th coordinate of
$\sum_{i \in s} c_i e_i$ is $c_j$ if $j \in s$ and $0$ otherwise.

Formalized by `MathlibExt.Analysis.Normed.Lp.DualC0.c0FinsetSum_apply`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/DualC0.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/DualC0.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c/index.html#c0-finset-sum-apply).

## A functional on a finitely supported sequence

Let $\mathbb{K}$ be the real or complex
field and $\iota$ an index type, and let $e_i \in c_0(\iota, \mathbb{K})$ be the sequence equal
to $1$ at $i$ and $0$ elsewhere. For every continuous linear functional $\varphi$ on
$c_0(\iota, \mathbb{K})$, every finite set $s \subseteq \iota$ and every $c : \iota \to \mathbb{K}$,
we have $\varphi(\sum_{i \in s} c_i e_i) = \sum_{i \in s} c_i \, \varphi(e_i)$.

Formalized by `MathlibExt.Analysis.Normed.Lp.DualC0.c0FinsetSum_apply_dual`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/DualC0.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/DualC0.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c/index.html#c0-finset-sum-apply-dual).

## Finite truncation of a $c_0$ sequence

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$, let
$\iota$ be a type, let $s \subseteq \iota$ be a finite set and let $x \in c_0(\iota, \mathbb{K})$.
The truncation of $x$ to $s$ is the element of $c_0(\iota, \mathbb{K})$ whose $j$-th coordinate is
$x_j$ for $j \in s$ and $0$ for $j \notin s$; it is defined as $\sum_{i \in s} x_i e_i$, where
$e_i$ is the sequence that is $1$ at $i$ and $0$ elsewhere.

Formalized by `MathlibExt.Analysis.Normed.Lp.DualC0.c0Trunc`, a definition declared in [MathlibExt/Analysis/Normed/Lp/DualC0.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/DualC0.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c/index.html#c0-trunc).

## Coordinates of a finite truncation

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$
and let $\iota$ be an index type. For a finite set $s \subseteq \iota$, an element
$x \in c_0(\iota, \mathbb{K})$ and an index $j \in \iota$, the $j$-th coordinate of the
truncation of $x$ to $s$ equals $x_j$ if $j \in s$ and $0$ otherwise.

Formalized by `MathlibExt.Analysis.Normed.Lp.DualC0.c0Trunc_apply`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/DualC0.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/DualC0.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c/index.html#c0-trunc-apply).

## Coordinate norms of an $\ell^1$ family are summable

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$ and let $\iota$ be any index type. For every $a \in \ell^1(\iota, \mathbb{K})$, the
family of norms $(\|a_i\|)_{i \in \iota}$ is summable.

Formalized by `MathlibExt.Analysis.Normed.Lp.DualC0.summable_norm_lp_one`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/DualC0.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/DualC0.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c/index.html#summable-norm-lp-one).

## Summability of the $\ell^1$–$c_0$ pairing

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$
and let $\iota$ be a type. For every $a \in \ell^1(\iota, \mathbb{K})$ and
$x \in c_0(\iota, \mathbb{K})$, the family $(a_i x_i)_{i \in \iota}$ is (unconditionally)
summable.

Formalized by `MathlibExt.Analysis.Normed.Lp.DualC0.summable_c0Pairing`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/DualC0.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/DualC0.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c/index.html#summable-c0-pairing).

## Pairing with an $\ell^1$ sequence as a linear functional on $c_0$

Let $\mathbb{K}$
be $\mathbb{R}$ or $\mathbb{C}$ and let $\iota$ be an index type. For
$a \in \ell^1(\iota, \mathbb{K})$, this is the $\mathbb{K}$-linear map
$c_0(\iota, \mathbb{K}) \to \mathbb{K}$ sending $x$ to $\sum_{i \in \iota} a_i x_i$.

Formalized by `MathlibExt.Analysis.Normed.Lp.DualC0.c0PairingLin`, a definition declared in [MathlibExt/Analysis/Normed/Lp/DualC0.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/DualC0.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c/index.html#c0-pairing-lin).

## Value of the functional of an $\ell^1$ sequence on $c_0$

Let $\mathbb{K}$ be
$\mathbb{R}$ or $\mathbb{C}$ and let $\iota$ be an index type. For $a \in \ell^1(\iota, \mathbb{K})$
and $x \in c_0(\iota, \mathbb{K})$, the linear functional on $c_0(\iota, \mathbb{K})$ given by
pairing with $a$ takes the value $\sum_{i \in \iota} a_i x_i$ at $x$.

Formalized by `MathlibExt.Analysis.Normed.Lp.DualC0.c0PairingLin_apply`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/DualC0.lean, line 270](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/DualC0.lean#L270). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c/index.html#c0-pairing-lin-apply).

## Bound for the $\ell^1$–$c_0$ pairing

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$ and
let $\iota$ be a type. For every $a \in \ell^1(\iota, \mathbb{K})$ and
$x \in c_0(\iota, \mathbb{K})$, $|\sum_{i \in \iota} a_i x_i| \le \|a\|_1 \|x\|_\infty$, where
$\|a\|_1 = \sum_i |a_i|$ and $\|x\|_\infty = \sup_i |x_i|$.

Formalized by `MathlibExt.Analysis.Normed.Lp.DualC0.norm_c0PairingLin_le`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/DualC0.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/DualC0.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c/index.html#norm-c0-pairing-lin-le).

## The $\ell^1$–$c_0$ pairing as a linear map

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$, let $c_0(\iota, \mathbb{K})$ be the space of families in $\mathbb{K}$ indexed by
$\iota$ that tend to $0$ along the cofinite filter, and let $\ell^1(\iota, \mathbb{K})$ be the
space of absolutely summable families. This is the linear map from $\ell^1(\iota, \mathbb{K})$ to
the space of continuous linear functionals on $c_0(\iota, \mathbb{K})$ that sends $a$ to the
functional $x \mapsto \sum_{i \in \iota} a_i x_i$.

Formalized by `MathlibExt.Analysis.Normed.Lp.DualC0.c0DualPairingLin`, a definition declared in [MathlibExt/Analysis/Normed/Lp/DualC0.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/DualC0.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c/index.html#c0-dual-pairing-lin).

## Formula for the $\ell^1$–$c_0$ pairing as a linear map

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$, let $c_0(\iota, \mathbb{K})$ be the space of families in $\mathbb{K}$ indexed by
$\iota$ that tend to $0$ along the cofinite filter, and let $\ell^1(\iota, \mathbb{K})$ be the
space of absolutely summable families. For $a \in \ell^1(\iota, \mathbb{K})$ and
$x \in c_0(\iota, \mathbb{K})$, the linear map from $\ell^1(\iota, \mathbb{K})$ to the continuous
linear functionals on $c_0(\iota, \mathbb{K})$ given by the pairing sends $a$ to a functional
whose value at $x$ is $\sum_{i \in \iota} a_i x_i$. This holds by definition.

Formalized by `MathlibExt.Analysis.Normed.Lp.DualC0.c0DualPairingLin_apply`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/DualC0.lean, line 318](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/DualC0.lean#L318). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c/index.html#c0-dual-pairing-lin-apply).

## Norm bound for the functional of an $\ell^1$ sequence on $c_0$

Let $\mathbb{K}$ be
$\mathbb{R}$ or $\mathbb{C}$ and let $\iota$ be a type. For every $a \in \ell^1(\iota, \mathbb{K})$,
the image of $a$ under the linear pairing map from $\ell^1(\iota, \mathbb{K})$ to the continuous
linear functionals on $c_0(\iota, \mathbb{K})$, which is the functional
$x \mapsto \sum_{i \in \iota} a_i x_i$, has operator norm at most $\|a\|_1 = \sum_i |a_i|$.

Formalized by `MathlibExt.Analysis.Normed.Lp.DualC0.norm_c0DualPairingLin_le`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/DualC0.lean, line 322](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/DualC0.lean#L322). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c/index.html#norm-c0-dual-pairing-lin-le).

## The $\ell^1$–$c_0$ pairing is continuous in the $\ell^1$ variable

Let $\mathbb{K}$ be
$\mathbb{R}$ or $\mathbb{C}$, let $c_0(\iota, \mathbb{K})$ be the space of families in $\mathbb{K}$
indexed by $\iota$ that tend to $0$ along the cofinite filter, with the supremum norm, and let
$\ell^1(\iota, \mathbb{K})$ be the space of absolutely summable families. The linear map from
$\ell^1(\iota, \mathbb{K})$ to the space of continuous linear functionals on
$c_0(\iota, \mathbb{K})$, with the operator norm, that sends $a$ to the functional
$x \mapsto \sum_{i \in \iota} a_i x_i$ is continuous.

Formalized by `MathlibExt.Analysis.Normed.Lp.DualC0.c0DualPairingLin_continuous`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/DualC0.lean, line 330](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/DualC0.lean#L330). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c/index.html#c0-dual-pairing-lin-continuous).

## The $\ell^1$–$c_0$ duality pairing

Let $\mathbb{K}$ be the real or complex field and
$\iota$ an index type. The pairing is the continuous linear map from $\ell^1(\iota, \mathbb{K})$
to the continuous dual of $c_0(\iota, \mathbb{K})$ that sends $a$ to the functional
$x \mapsto \sum_{i \in \iota} a_i x_i$.

Formalized by `MathlibExt.Analysis.Normed.Lp.DualC0.c0DualPairing`, a definition declared in [MathlibExt/Analysis/Normed/Lp/DualC0.lean, line 337](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/DualC0.lean#L337). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c/index.html#c0-dual-pairing).

## Formula for the $\ell^1$–$c_0$ duality pairing

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$, let $c_0(\iota, \mathbb{K})$ be the space of families in $\mathbb{K}$ indexed by
$\iota$ that tend to $0$ along the cofinite filter, and let $\ell^1(\iota, \mathbb{K})$ be the
space of absolutely summable families. For $a \in \ell^1(\iota, \mathbb{K})$ and
$x \in c_0(\iota, \mathbb{K})$, the canonical continuous linear map from $\ell^1(\iota, \mathbb{K})$
to the continuous linear functionals on $c_0(\iota, \mathbb{K})$ sends $a$ to a functional whose
value at $x$ is $\sum_{i \in \iota} a_i x_i$.

Formalized by `MathlibExt.Analysis.Normed.Lp.DualC0.c0DualPairing_apply`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/DualC0.lean, line 341](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/DualC0.lean#L341). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c/index.html#c0-dual-pairing-apply).

## The pairing map $\ell^1 \to c_0^*$ does not increase norms

**The pairing map $\ell^1 \to c_0^*$ does not increase norms.** Let $\mathbb{K}$ be
$\mathbb{R}$ or $\mathbb{C}$, let $\iota$ be a type, and let $c_0(\iota, \mathbb{K})^*$ be the
space of continuous linear functionals on $c_0(\iota, \mathbb{K})$. For every
$a \in \ell^1(\iota, \mathbb{K})$, the image of $a$ under the continuous linear pairing map
$\ell^1(\iota, \mathbb{K}) \to c_0(\iota, \mathbb{K})^*$, which is the functional
$x \mapsto \sum_{i \in \iota} a_i x_i$, has operator norm at most $\|a\|_1 = \sum_i |a_i|$.

Formalized by `MathlibExt.Analysis.Normed.Lp.DualC0.norm_c0DualPairing_le`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/DualC0.lean, line 346](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/DualC0.lean#L346). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c/index.html#norm-c0-dual-pairing-le).

## Coefficients of a functional on $c_0$

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$,
let $c_0(\iota, \mathbb{K})$ be the space of families in $\mathbb{K}$ indexed by $\iota$ that tend
to $0$ along the cofinite filter, and for $i \in \iota$ let $e_i \in c_0(\iota, \mathbb{K})$ be the
family that is $1$ at $i$ and $0$ elsewhere. The coefficients of a continuous linear functional
$\Phi$ on $c_0(\iota, \mathbb{K})$ are the family $i \mapsto \Phi(e_i)$ in $\mathbb{K}$.

Formalized by `MathlibExt.Analysis.Normed.Lp.DualC0.c0Coeff`, a definition declared in [MathlibExt/Analysis/Normed/Lp/DualC0.lean, line 360](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/DualC0.lean#L360). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c/index.html#c0-coeff).

## The normalizing scalar $\overline{w}/|w|$

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$.
For $w \in \mathbb{K}$, the normalizing scalar $u(w) \in \mathbb{K}$ of $w$ is $0$ if $w = 0$ and
$\overline{w}/|w|$ otherwise, so that $u(w)\, w = |w|$.

Formalized by `MathlibExt.Analysis.Normed.Lp.DualC0.c0UnitScalar`, a definition declared in [MathlibExt/Analysis/Normed/Lp/DualC0.lean, line 364](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/DualC0.lean#L364). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c/index.html#c0-unit-scalar).

## The normalizing scalar times $w$ is $|w|$

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$.
For every $w \in \mathbb{K}$, the normalizing scalar $u(w)$ of $w$, which is $0$ if $w = 0$ and
$\overline{w}/|w|$ otherwise, satisfies $u(w)\, w = |w|$, with $|w|$ regarded as an element of
$\mathbb{K}$.

Formalized by `MathlibExt.Analysis.Normed.Lp.DualC0.c0UnitScalar_mul`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/DualC0.lean, line 368](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/DualC0.lean#L368). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c/index.html#c0-unit-scalar-mul).

## The normalizing scalar has absolute value at most one

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$. For every $w \in \mathbb{K}$, the normalizing scalar $u(w)$ of $w$, which is $0$ if
$w = 0$ and $\overline{w}/|w|$ otherwise, satisfies $|u(w)| \le 1$.

Formalized by `MathlibExt.Analysis.Normed.Lp.DualC0.norm_c0UnitScalar_le`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/DualC0.lean, line 378](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/DualC0.lean#L378). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c/index.html#norm-c0-unit-scalar-le).

## Finite sums of the coefficients of a functional on $c_0$

Let $\mathbb{K}$ be $\mathbb{R}$
or $\mathbb{C}$, let $c_0(\iota, \mathbb{K})$ be the space of families in $\mathbb{K}$ indexed by
$\iota$ that tend to $0$ along the cofinite filter, with the supremum norm, and for $i \in \iota$
let $e_i \in c_0(\iota, \mathbb{K})$ be the family that is $1$ at $i$ and $0$ elsewhere. For every
continuous linear functional $\Phi$ on $c_0(\iota, \mathbb{K})$ and every finite set
$s \subseteq \iota$, we have $\sum_{i \in s} |\Phi(e_i)| \le \|\Phi\|$, where $\|\Phi\|$ is the
operator norm.

Formalized by `MathlibExt.Analysis.Normed.Lp.DualC0.c0Coeff_finset_sum_le`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/DualC0.lean, line 387](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/DualC0.lean#L387). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c/index.html#c0-coeff-finset-sum-le).

## The coefficients of a functional on $c_0$ are absolutely summable

Let $\mathbb{K}$ be
$\mathbb{R}$ or $\mathbb{C}$, let $c_0(\iota, \mathbb{K})$ be the space of families in $\mathbb{K}$
indexed by $\iota$ that tend to $0$ along the cofinite filter, and for $i \in \iota$ let
$e_i \in c_0(\iota, \mathbb{K})$ be the family that is $1$ at $i$ and $0$ elsewhere. For every
continuous linear functional $\Phi$ on $c_0(\iota, \mathbb{K})$, the family
$(\Phi(e_i))_{i \in \iota}$ lies in $\ell^1(\iota, \mathbb{K})$, that is,
$\sum_{i \in \iota} |\Phi(e_i)| < \infty$.

Formalized by `MathlibExt.Analysis.Normed.Lp.DualC0.c0Coeff_memℓp`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/DualC0.lean, line 417](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/DualC0.lean#L417). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c/index.html#c0-coeff-mem-p).

## The $\ell^1$ coefficient sequence of a functional on $c_0$

Let $\mathbb{K}$ be
$\mathbb{R}$ or $\mathbb{C}$, let $c_0(\iota, \mathbb{K})$ be the space of families in $\mathbb{K}$
indexed by $\iota$ that tend to $0$ along the cofinite filter, and for $i \in \iota$ let
$e_i \in c_0(\iota, \mathbb{K})$ be the family that is $1$ at $i$ and $0$ elsewhere. For a
continuous linear functional $\Phi$ on $c_0(\iota, \mathbb{K})$, this is the family
$(\Phi(e_i))_{i \in \iota}$, regarded as an element of the space $\ell^1(\iota, \mathbb{K})$ of
absolutely summable families.

Formalized by `MathlibExt.Analysis.Normed.Lp.DualC0.c0CoeffLp`, a definition declared in [MathlibExt/Analysis/Normed/Lp/DualC0.lean, line 425](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/DualC0.lean#L425). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c/index.html#c0-coeff-lp).

## $\ell^1$ norm of the coefficients of a functional on $c_0$

Let $\mathbb{K}$ be $\mathbb{R}$
or $\mathbb{C}$, let $\iota$ be a type and let $\Phi$ be a continuous linear functional on
$c_0(\iota, \mathbb{K})$. For $i \in \iota$ let $e_i$ be the sequence that is $1$ at $i$ and $0$
elsewhere. The coefficient sequence $(\Phi(e_i))_{i \in \iota}$, as an element of
$\ell^1(\iota, \mathbb{K})$, has norm $\sum_{i \in \iota} |\Phi(e_i)|$ at most the operator norm
$\|\Phi\|$.

Formalized by `MathlibExt.Analysis.Normed.Lp.DualC0.norm_c0CoeffLp_le`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/DualC0.lean, line 429](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/DualC0.lean#L429). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c/index.html#norm-c0-coeff-lp-le).

## Every functional on $c_0$ comes from $\ell^1$

Let $\mathbb{K}$ be the real or complex
field and $\iota$ an index type. For every continuous linear functional $\varphi$ on
$c_0(\iota, \mathbb{K})$ there is $a \in \ell^1(\iota, \mathbb{K})$ with
$\varphi(x) = \sum_{i \in \iota} a_i x_i$ for all $x \in c_0(\iota, \mathbb{K})$; that is, the
pairing map from $\ell^1(\iota, \mathbb{K})$ to the continuous dual of $c_0(\iota, \mathbb{K})$
is surjective.

The proof takes $a_i = \varphi(e_i)$, where $e_i$ is the sequence equal to $1$ at $i$ and $0$
elsewhere, and recovers $\varphi(x)$ as the limit of $\varphi$ on the finite truncations of $x$.

Formalized by `MathlibExt.Analysis.Normed.Lp.DualC0.c0DualPairing_surjective`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/DualC0.lean, line 443](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/DualC0.lean#L443). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c/index.html#c0-dual-pairing-surjective).

## The $\ell^1$–$c_0$ pairing is isometric

Let $\mathbb{K}$ be the real or complex field
and $\iota$ an index type. For every $a \in \ell^1(\iota, \mathbb{K})$, the continuous linear
functional $x \mapsto \sum_{i \in \iota} a_i x_i$ on $c_0(\iota, \mathbb{K})$, the space of
sequences $\iota \to \mathbb{K}$ tending to $0$ at infinity with the supremum norm, has operator
norm equal to $\|a\|_1 = \sum_{i \in \iota} |a_i|$.

Formalized by `MathlibExt.Analysis.Normed.Lp.DualC0.c0DualPairing_norm`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/DualC0.lean, line 506](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/DualC0.lean#L506). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c/index.html#c0-dual-pairing-norm).

## The dual of $c_0$ is $\ell^1$

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$, let
$c_0(\iota, \mathbb{K})$ be the space of families in $\mathbb{K}$ indexed by $\iota$ that tend to
$0$ along the cofinite filter, with the supremum norm, and let $\ell^1(\iota, \mathbb{K})$ be the
space of absolutely summable families, with the norm $\|a\|_1 = \sum_{i \in \iota} |a_i|$. This
is the linear isometric isomorphism from $\ell^1(\iota, \mathbb{K})$ onto the space of continuous
linear functionals on $c_0(\iota, \mathbb{K})$, with the operator norm, that sends $a$ to the
functional $x \mapsto \sum_{i \in \iota} a_i x_i$.

Formalized by `MathlibExt.Analysis.Normed.Lp.DualC0.c0DualEquiv`, a definition declared in [MathlibExt/Analysis/Normed/Lp/DualC0.lean, line 524](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/DualC0.lean#L524). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c/index.html#c0-dual-equiv).

## Coordinate evaluation on $c_0$

Let $\mathbb{K}$ be the real or complex field and $\iota$
an index type. For $i \in \iota$, evaluation at $i$ is the continuous linear functional
$x \mapsto x_i$ on $c_0(\iota, \mathbb{K})$.

Formalized by `MathlibExt.Analysis.Normed.Lp.DualC0.c0Eval`, a definition declared in [MathlibExt/Analysis/Normed/Lp/DualC0.lean, line 537](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/DualC0.lean#L537). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c/index.html#c0-eval).

## Pairing with a unit vector is evaluation

Let $\mathbb{K}$ be the real or complex field
and $\iota$ an index type, and for $i \in \iota$ let $e_i \in \ell^1(\iota, \mathbb{K})$ be the
sequence equal to $1$ at $i$ and $0$ elsewhere. Then the functional
$x \mapsto \sum_{j \in \iota} (e_i)_j x_j$ on $c_0(\iota, \mathbb{K})$ given by pairing with
$e_i$ is the evaluation $x \mapsto x_i$ at $i$.

Formalized by `MathlibExt.Analysis.Normed.Lp.DualC0.c0DualPairing_single_eq_eval`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/DualC0.lean, line 547](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Lp/DualC0.lean#L547). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c/index.html#c0-dual-pairing-single-eq-eval).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Duals of ℓ^p and c₀](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/banach-spaces/sequence-spaces/duals-of-p-and-c)
