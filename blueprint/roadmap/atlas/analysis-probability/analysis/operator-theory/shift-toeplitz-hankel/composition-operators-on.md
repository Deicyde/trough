---
declaration: section
origin: cited
lean: MathlibExt.Analysis.InnerProductSpace.CompositionOperator.HasBoundedFibers, MathlibExt.Analysis.InnerProductSpace.CompositionOperator.fiberCard, MathlibExt.Analysis.InnerProductSpace.CompositionOperator.fiberCard_eq_ncard, MathlibExt.Analysis.InnerProductSpace.CompositionOperator.fiberSup, MathlibExt.Analysis.InnerProductSpace.CompositionOperator.fiberSup_eq_iSup, MathlibExt.Analysis.InnerProductSpace.CompositionOperator.compFun, MathlibExt.Analysis.InnerProductSpace.CompositionOperator.memℓp_compFun, MathlibExt.Analysis.InnerProductSpace.CompositionOperator.tsum_compFun_norm_sq_le
statement: formalized
proof: formalized
---

# Composition operators on ℓ²

32 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/composition-operators-on/index.html).

## Uniformly bounded fibers of a map on the naturals

The fibers of `ψ` are finite and uniformly bounded by `M`: every value
is taken at most `M` times. This is the boundedness hypothesis for the
composition operator.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompositionOperator.HasBoundedFibers`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/composition-operators-on/index.html#has-bounded-fibers).

## Fiber cardinality of a map

The number of preimages of `m` under `ψ`, defined for a finite fiber.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompositionOperator.fiberCard`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/composition-operators-on/index.html#fiber-card).

## Fiber count agrees with set cardinality

On its finite domain, the fiber count agrees with the standard natural cardinality.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompositionOperator.fiberCard_eq_ncard`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/composition-operators-on/index.html#fiber-card-eq-ncard).

## Supremum of the fiber counts of a map

The real supremum of the fiber counts of `ψ`, defined for uniformly bounded finite
fibers. The bound in `hψ` ensures that the real-valued family is bounded above.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompositionOperator.fiberSup`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/composition-operators-on/index.html#fiber-sup).

## Fiber supremum as a supremum of cardinalities

On its bounded finite domain, the fiber supremum agrees with the supremum of natural
cardinalities. Its value is independent of the chosen bound and evidence.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompositionOperator.fiberSup_eq_iSup`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/composition-operators-on/index.html#fiber-sup-eq-i-sup).

## Precomposition of a sequence with a map

The composition function: precompose a sequence with `ψ`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompositionOperator.compFun`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/composition-operators-on/index.html#comp-fun).

## Precomposition preserves square-summability

The composed sequence of an `ℓ²` sequence is in `ℓ²`, under the bounded
fibers hypothesis.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompositionOperator.memℓp_compFun`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/composition-operators-on/index.html#mem-p-comp-fun).

## Squared-norm sum bound for a precomposed sequence

The squared-norm sum of the composed sequence is at most `fiberSup ψ hψ`
times the squared-norm sum of the original sequence.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompositionOperator.tsum_compFun_norm_sq_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/composition-operators-on/index.html#tsum-comp-fun-norm-sq-le).

## Composition operator as a linear map

The composition operator as a linear map.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompositionOperator.compLinMap`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/composition-operators-on/index.html#comp-lin-map).

## Pointwise action of the composition linear map

Pointwise action of the composition linear map.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompositionOperator.compLinMap_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/composition-operators-on/index.html#comp-lin-map-apply).

## Squared-norm bound for the composition linear map

The squared norm of `C_ψ x` is at most `fiberSup ψ hψ * ‖x‖²`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompositionOperator.norm_sq_compLinMap_apply_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/composition-operators-on/index.html#norm-sq-comp-lin-map-apply-le).

## Fiber supremum is nonnegative

`fiberSup ψ hψ` is nonnegative.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompositionOperator.fiberSup_nonneg`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/composition-operators-on/index.html#fiber-sup-nonneg).

## Norm bound for the composition linear map

The composition operator is bounded by `√(fiberSup ψ hψ)`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompositionOperator.norm_compLinMap_apply_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/composition-operators-on/index.html#norm-comp-lin-map-apply-le).

## Bounded composition operator on $\ell^2$

The composition operator as a bounded operator on `ℓ²(ℕ, 𝕜)`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompositionOperator.compCLM`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/composition-operators-on/index.html#comp-clm).

## Pointwise action of the bounded composition operator

Pointwise action of the composition operator.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompositionOperator.compCLM_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/composition-operators-on/index.html#comp-clm-apply).

## Vectorwise norm bound for the composition operator

The composition operator is bounded by `√(fiberSup ψ hψ)` on every vector.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompositionOperator.norm_compCLM_apply_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/composition-operators-on/index.html#norm-comp-clm-apply-le).

## Operator-norm bound for the composition operator

The operator norm of `C_ψ` is at most `√(fiberSup ψ hψ)`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompositionOperator.norm_compCLM_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/composition-operators-on/index.html#norm-comp-clm-le).

## Norm of the composition operator on a basis vector

The norm of `C_ψ` applied to a standard basis vector is the square root
of the corresponding fiber count.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompositionOperator.norm_compCLM_single`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/composition-operators-on/index.html#norm-comp-clm-single).

## Operator norm of a composition operator

The operator norm of the composition operator:
`‖C_ψ‖ = √(fiberSup ψ hψ)`, the square root of the largest fiber count.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompositionOperator.norm_compCLM`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/composition-operators-on/index.html#norm-comp-clm).

## Adjoint of a composition operator is the fiber-sum operator

The adjoint of the composition operator is the fiber-sum operator:
`((C_ψ)† y) m` is the sum of `y` over the fiber of `m`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompositionOperator.adjoint_compCLM_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean, line 326](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean#L326). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/composition-operators-on/index.html#adjoint-comp-clm-apply).

## Bounded fibers are preserved under composition

Fiber bounds compose: the fibers of `ψ ∘ φ` are bounded by the product
of the bounds.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompositionOperator.hasBoundedFibers_comp`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean, line 365](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean#L365). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/composition-operators-on/index.html#has-bounded-fibers-comp).

## Composition of composition operators

Composition of composition operators is composition of symbols in the
reversed order: `C_φ ∘L C_ψ = C_{ψ ∘ φ}`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompositionOperator.compCLM_comp`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean, line 418](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean#L418). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/composition-operators-on/index.html#comp-clm-comp).

## Composition operator of a pointwise identity symbol

If `ψ` is pointwise the identity, `C_ψ` is the identity operator.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompositionOperator.compCLM_eq_of_forall`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean, line 426](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean#L426). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/composition-operators-on/index.html#comp-clm-eq-of-forall).

## Composition operator of the identity is the identity

`C_id` is the identity operator.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompositionOperator.compCLM_id`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean, line 432](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean#L432). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/composition-operators-on/index.html#comp-clm-id).

## Injective maps have fibers of size at most one

An injective symbol has fibers of size at most one.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompositionOperator.hasBoundedFibers_of_injective`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean, line 436](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean#L436). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/composition-operators-on/index.html#has-bounded-fibers-of-injective).

## Permutations have fibers of size one

A permutation symbol has fibers of size one.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompositionOperator.hasBoundedFibers_equiv`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean, line 452](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean#L452). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/composition-operators-on/index.html#has-bounded-fibers-equiv).

## Adjoint of a composition operator with a permutation symbol

The adjoint of the composition operator for a permutation symbol is the
composition operator of the inverse permutation.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompositionOperator.adjoint_compCLM_of_equiv`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean, line 457](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean#L457). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/composition-operators-on/index.html#adjoint-comp-clm-of-equiv).

## Permutation composition operators are unitary

A permutation symbol gives a unitary composition operator.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompositionOperator.compCLM_mem_unitary`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean, line 475](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean#L475). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/composition-operators-on/index.html#comp-clm-mem-unitary).

## Composition operator is injective iff its symbol is surjective

`C_ψ` is injective iff `ψ` is surjective: a missing value gives a
basis vector in the kernel, and a surjective symbol lets every coordinate
be read off from the image.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompositionOperator.injective_compCLM_iff`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean, line 494](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean#L494). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/composition-operators-on/index.html#injective-comp-clm-iff).

## Composition operator is surjective iff its symbol is injective

`C_ψ` is surjective iff `ψ` is injective: if `ψ a = ψ b` with
`a ≠ b`, the `a`-th and `b`-th coordinates of every vector in the range
agree, so `e_a` is not in the range; if `ψ` is injective, the preimage of
`y` is obtained by applying the adjoint and reading off the fiber sums.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompositionOperator.surjective_compCLM_iff`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean, line 528](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean#L528). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/composition-operators-on/index.html#surjective-comp-clm-iff).

## Halving map has fibers of size at most two

Halving pairs: the map `n ↦ n / 2` has fibers of size at most two.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompositionOperator.hasBoundedFibers_div_two`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean, line 560](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean#L560). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/composition-operators-on/index.html#has-bounded-fibers-div-two).

## Composition operators on $\ell^2$ are never compact

A composition operator on `ℓ²(ℕ, 𝕜)` is never compact: the images of
the basis vectors indexed by the (necessarily infinite) range of `ψ` are
pairwise orthogonal and bounded below in norm, so they have no Cauchy
subsequence.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompositionOperator.not_isCompactOperator_compCLM`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean, line 582](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CompositionOperator.lean#L582). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/composition-operators-on/index.html#not-is-compact-operator-comp-clm).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Composition operators on ℓ²](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/composition-operators-on/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/composition-operators-on)
