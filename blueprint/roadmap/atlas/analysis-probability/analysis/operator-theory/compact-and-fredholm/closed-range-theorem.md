---
declaration: section
origin: cited
lean: ContinuousLinearMap.setRange_eq_coe_linearMap_range, ContinuousLinearMap.range_comp_subtypeL_orthogonalComplement_ker, ContinuousLinearMap.injective_comp_subtypeL_orthogonalComplement_ker, ContinuousLinearMap.isClosed_range_adjoint_of_isClosed_range, ContinuousLinearMap.isClosed_range_adjoint_iff, MathlibExt.Analysis.OperatorTheory.AdjointCompFredholmClosedRangeWanted.isClosed_range_of_isFredholm_adjoint_comp, MathlibExt.Analysis.OperatorTheory.HilbertAdjointClosedRangeWanted.isClosed_range_adjoint_of_isClosed_range
statement: formalized
---

# Closed range theorem

7 results, 5 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/closed-range-theorem/index.html).

## The range of a bounded operator as a set

Let $E'$ and $F'$ be Hilbert spaces over
$\mathbb{K}$, where $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$, and let $S : E' \to F'$ be a
bounded linear operator. The set of values of $S$ equals the underlying set of the range of $S$
regarded as a linear subspace of $F'$.

This lets closedness of the range pass between the anti-Lipschitz criterion, stated for the
set of values, and the adjoint orthogonality identities, stated for the linear subspace.

Formalized by `ContinuousLinearMap.setRange_eq_coe_linearMap_range`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ClosedRangeAdjoint.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ClosedRangeAdjoint.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/closed-range-theorem/index.html#set-range-eq-coe-linear-map-range).

## Restriction to the orthogonal complement of the kernel keeps the range

Let $E$ be a
Hilbert space and $F$ an inner product space over $\mathbb{K}$, where $\mathbb{K}$ is
$\mathbb{R}$ or $\mathbb{C}$, and let $T : E \to F$ be a bounded linear operator. Then the
restriction of $T$ to the orthogonal complement $(\ker T)^\perp$ of its kernel has the same
range as $T$: every value $T x$ is attained at the orthogonal projection of $x$ onto
$(\ker T)^\perp$, since the difference lies in $\ker T$.

Formalized by `ContinuousLinearMap.range_comp_subtypeL_orthogonalComplement_ker`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ClosedRangeAdjoint.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ClosedRangeAdjoint.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/closed-range-theorem/index.html#range-comp-subtype-l-orthogonal-compleme).

## Restriction to the orthogonal complement of the kernel is injective

Let $E$ and $F$
be inner product spaces over $\mathbb{K}$, where $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$,
and let $T : E \to F$ be a bounded linear operator. Then the restriction of $T$ to the
orthogonal complement $(\ker T)^\perp$ of its kernel is injective: a vector lying in both
$\ker T$ and $(\ker T)^\perp$ is zero.

Formalized by `ContinuousLinearMap.injective_comp_subtypeL_orthogonalComplement_ker`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ClosedRangeAdjoint.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ClosedRangeAdjoint.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/closed-range-theorem/index.html#injective-comp-subtype-l-orthogonal-comp).

## Closed range passes to the adjoint

Let $E$ and $F$ be Hilbert spaces over $\mathbb{K}$,
where $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$, and let $T : E \to F$ be a bounded linear
operator with adjoint $T^\dagger$. If the range of $T$ is closed in $F$, then the range of
$T^\dagger$ is closed in $E$.

Proof sketch: if the range of $T$ is closed, then $T$ is bounded below on $(\ker T)^\perp$
(the anti-Lipschitz criterion for its injective restriction), say $\|x\| \le C \|T x\|$ there.
Every $y \in (\ker T^\dagger)^\perp$ lies in the range of $T$, because
$(\operatorname{ran} T)^\perp = \ker T^\dagger$ and the range is closed. Writing $y = T x$ with
$x \in (\ker T)^\perp$ gives
$\|y\|^2 = \operatorname{Re} \langle x, T^\dagger y \rangle \le \|x\| \|T^\dagger y\| \le
C \|y\| \|T^\dagger y\|$; cancelling $\|y\|$ shows that $T^\dagger$ is bounded below on
$(\ker T^\dagger)^\perp$, so its range, which is the range of its restriction to
$(\ker T^\dagger)^\perp$, is closed.

Formalized by `ContinuousLinearMap.isClosed_range_adjoint_of_isClosed_range`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ClosedRangeAdjoint.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ClosedRangeAdjoint.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/closed-range-theorem/index.html#is-closed-range-adjoint-of-is-closed-ran).

## Closed range theorem for adjoints

Let $E$ and $F$ be Hilbert spaces over $\mathbb{K}$,
where $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$, and let $T : E \to F$ be a bounded linear
operator with adjoint $T^\dagger$. Then the range of $T$ is closed in $F$ if and only if the
range of $T^\dagger$ is closed in $E$.

The reverse direction is the forward direction applied to $T^\dagger$, using
$T^{\dagger\dagger} = T$.

Formalized by `ContinuousLinearMap.isClosed_range_adjoint_iff`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ClosedRangeAdjoint.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/ClosedRangeAdjoint.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/closed-range-theorem/index.html#is-closed-range-adjoint-iff).

## Closed range from a Fredholm $T^*T$

**Closed range from a Fredholm $T^*T$.** Let $X$ and $Y$ be complex Hilbert spaces and let
$T : X \to Y$ be a bounded linear operator with Hilbert space adjoint $T^* : Y \to X$. If
$T^*T : X \to X$ is a Fredholm operator, then the range of $T$ is closed in $Y$.

Here a Fredholm operator is a bounded linear operator that is open onto its range, whose range is
closed and of finite codimension, and whose kernel is finite-dimensional and has a closed
complement. The source asks only for a finite-dimensional kernel and a range of finite
codimension; between Hilbert spaces the two agree, since a finite-codimensional range of a bounded
operator is closed.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Operator theory; General theory of linear operators), problem `ma_proofbench_l2_23`, with the change above.

Stated but not proved: `MathlibExt.Analysis.OperatorTheory.AdjointCompFredholmClosedRangeWanted.isClosed_range_of_isFredholm_adjoint_comp` is written with `theorem_wanted` in [WantedExt/Analysis/OperatorTheory/AdjointCompFredholmClosedRangeWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/OperatorTheory/AdjointCompFredholmClosedRangeWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/closed-range-theorem/index.html#is-closed-range-of-is-fredholm-adjoint-c).

## Closed range passes to the Hilbert space adjoint

Let $X$ and $Y$ be complex Hilbert spaces
and let $A : X \to Y$ be a bounded linear operator with Hilbert space adjoint $A^* : Y \to X$. If
the range of $A$ is closed in $Y$, then the range of $A^*$ is closed in $X$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Operator theory; General theory of linear operators), problem `ma_proofbench_l2_85`.

Stated but not proved: `MathlibExt.Analysis.OperatorTheory.HilbertAdjointClosedRangeWanted.isClosed_range_adjoint_of_isClosed_range` is written with `theorem_wanted` in [WantedExt/Analysis/OperatorTheory/HilbertAdjointClosedRangeWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/OperatorTheory/HilbertAdjointClosedRangeWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/closed-range-theorem/index.html#is-closed-range-adjoint-of-is-closed-ran-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Closed range theorem](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/closed-range-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/operator-theory/compact-and-fredholm/closed-range-theorem)
