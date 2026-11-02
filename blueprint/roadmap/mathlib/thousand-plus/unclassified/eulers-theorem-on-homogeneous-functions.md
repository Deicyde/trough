---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: HasFDerivAt.apply_self_eq_smul_of_eventuallyEq, HasFDerivAt.apply_self_eq_smul_of_homogeneous, HasFDerivAt.apply_self_eq_nsmul_of_homogeneous
mathlib_file: Mathlib/Analysis/Calculus/LineDeriv/Basic.lean
---

# Euler's theorem on homogeneous functions

Mathlib records this with 3 declarations.

`HasFDerivAt.apply_self_eq_smul_of_eventuallyEq`: A local, vector-valued version of Euler's theorem on homogeneous functions.

If `f (t • x) = w t • f x` for `t` in a neighborhood of `1`, then the derivative of `f` at
`x`, applied to `x`, is `w' • f x`, where `w'` is the derivative of `w` at `1`.

```lean
HasFDerivAt.apply_self_eq_smul_of_eventuallyEq.{u_1, u_2, u_3} {𝕜 : Type u_1}
  [NontriviallyNormedField 𝕜] {F : Type u_2} [NormedAddCommGroup F] [NormedSpace 𝕜 F] {E : Type u_3}
  [NormedAddCommGroup E] [NormedSpace 𝕜 E] {f : E → F} {x : E} {L : E →L[𝕜] F} {w : 𝕜 → 𝕜} {w' : 𝕜}
  (hf : HasFDerivAt f L x) (hw : HasDerivAt w w' 1)
  (hhom : (fun t => f (t • x)) =ᶠ[nhds 1] fun t => w t • f x) : L x = w' • f x
```

`HasFDerivAt.apply_self_eq_smul_of_homogeneous`: A vector-valued version of Euler's theorem for a homogeneous function.

If `f (t • y) = w t • f y` for all scalars `t` and points `y`, then the derivative of `f` at
`x`, applied to `x`, is `w' • f x`, where `w'` is the derivative of `w` at `1`.

```lean
HasFDerivAt.apply_self_eq_smul_of_homogeneous.{u_1, u_2, u_3} {𝕜 : Type u_1}
  [NontriviallyNormedField 𝕜] {F : Type u_2} [NormedAddCommGroup F] [NormedSpace 𝕜 F] {E : Type u_3}
  [NormedAddCommGroup E] [NormedSpace 𝕜 E] {f : E → F} {x : E} {L : E →L[𝕜] F} {w : 𝕜 → 𝕜} {w' : 𝕜}
  (hf : HasFDerivAt f L x) (hw : HasDerivAt w w' 1)
  (hhom : ∀ (t : 𝕜) (y : E), f (t • y) = w t • f y) : L x = w' • f x
```

`HasFDerivAt.apply_self_eq_nsmul_of_homogeneous`: A vector-valued version of Euler's theorem for a homogeneous function of natural degree.

If `f (t • y) = t ^ k • f y` for all scalars `t` and points `y`, then the derivative of `f` at
`x`, applied to `x`, is `k • f x`.

```lean
HasFDerivAt.apply_self_eq_nsmul_of_homogeneous.{u_1, u_2, u_3} {𝕜 : Type u_1}
  [NontriviallyNormedField 𝕜] {F : Type u_2} [NormedAddCommGroup F] [NormedSpace 𝕜 F] {E : Type u_3}
  [NormedAddCommGroup E] [NormedSpace 𝕜 E] {f : E → F} {x : E} {L : E →L[𝕜] F} {k : ℕ}
  (hf : HasFDerivAt f L x) (hhom : ∀ (t : 𝕜) (y : E), f (t • y) = t ^ k • f y) : L x = k • f x
```

The converse stated in the English Wikipedia article is not yet formalized.

## Depends on

- [Derivative at a point](../../undergraduate/single-variable-real-analysis/differentiability/derivative-at-a-point.md)
- [Differentiable function between normed vector spaces](../../overview/analysis/differentiability/differentiable-function-between-normed-vector-sp.md)
- [Finite set](../../overview/data-structures/sets/finite-set.md)
- [Normed vector space over a normed field](../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)

## Proof depends on

- [Associative algebra over a commutative ring](../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)

## Sources

- [Mathlib documentation: `HasFDerivAt.apply_self_eq_smul_of_eventuallyEq`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/LineDeriv/Basic.html#HasFDerivAt.apply_self_eq_smul_of_eventuallyEq)
- [Source of `HasFDerivAt.apply_self_eq_smul_of_eventuallyEq` in Mathlib/Analysis/Calculus/LineDeriv/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/LineDeriv/Basic.lean#L280)
- [Mathlib documentation: `HasFDerivAt.apply_self_eq_smul_of_homogeneous`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/LineDeriv/Basic.html#HasFDerivAt.apply_self_eq_smul_of_homogeneous)
- [Source of `HasFDerivAt.apply_self_eq_smul_of_homogeneous` in Mathlib/Analysis/Calculus/LineDeriv/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/LineDeriv/Basic.lean#L294)
- [Mathlib documentation: `HasFDerivAt.apply_self_eq_nsmul_of_homogeneous`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/LineDeriv/Basic.html#HasFDerivAt.apply_self_eq_nsmul_of_homogeneous)
- [Source of `HasFDerivAt.apply_self_eq_nsmul_of_homogeneous` in Mathlib/Analysis/Calculus/LineDeriv/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/LineDeriv/Basic.lean#L304)
- [1000+ theorems list: Q25378679](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L4218)
- [1000+ theorems project: Q25378679](https://1000-plus.github.io/?length=-1#Q25378679)
- [Wikidata: Q25378679](https://www.wikidata.org/wiki/Q25378679)
