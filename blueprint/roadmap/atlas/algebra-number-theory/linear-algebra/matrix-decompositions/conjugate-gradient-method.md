---
declaration: section
origin: cited
lean: MathlibExt.LinearAlgebra.Matrix.ConjugateGradient.energyNorm, MathlibExt.LinearAlgebra.Matrix.ConjugateGradient.krylov, MathlibExt.LinearAlgebra.Matrix.ConjugateGradient.State, MathlibExt.LinearAlgebra.Matrix.ConjugateGradient.step, MathlibExt.LinearAlgebra.Matrix.ConjugateGradient.init, MathlibExt.LinearAlgebra.Matrix.ConjugateGradient.iterate, MathlibExt.LinearAlgebra.Matrix.ConjugateGradient.iterate_x_sub_mem_krylov, MathlibExt.LinearAlgebra.Matrix.ConjugateGradient.energyNorm_iterate_le
statement: formalized
proof: formalized
---

# Conjugate gradient method

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/conjugate-gradient-method/index.html).

## Energy norm induced by a matrix

The energy norm `‖v‖_A = √(vᵀ A v)`; a norm when `A` is positive definite.

Formalized by `MathlibExt.LinearAlgebra.Matrix.ConjugateGradient.energyNorm`, a definition declared in [MathlibExt/LinearAlgebra/Matrix/ConjugateGradient.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/ConjugateGradient.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/conjugate-gradient-method/index.html#energy-norm).

## Krylov subspace

The Krylov space `𝒦_k(A, r) = span {r, A r, …, A^{k-1} r}`.

Formalized by `MathlibExt.LinearAlgebra.Matrix.ConjugateGradient.krylov`, a definition declared in [MathlibExt/LinearAlgebra/Matrix/ConjugateGradient.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/ConjugateGradient.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/conjugate-gradient-method/index.html#krylov).

## State of the conjugate gradient method

The state of the conjugate gradient method: iterate `x`, residual `r = b - A x` and search
direction `d`.

Formalized by `MathlibExt.LinearAlgebra.Matrix.ConjugateGradient.State`, a structure declared in [MathlibExt/LinearAlgebra/Matrix/ConjugateGradient.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/ConjugateGradient.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/conjugate-gradient-method/index.html#state).

## One Hestenes–Stiefel conjugate gradient step

One Hestenes–Stiefel conjugate gradient step.

Formalized by `MathlibExt.LinearAlgebra.Matrix.ConjugateGradient.step`, a definition declared in [MathlibExt/LinearAlgebra/Matrix/ConjugateGradient.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/ConjugateGradient.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/conjugate-gradient-method/index.html#step).

## Initial conjugate gradient state

The initial state `x₀`, `r₀ = d₀ = b - A x₀`.

Formalized by `MathlibExt.LinearAlgebra.Matrix.ConjugateGradient.init`, a definition declared in [MathlibExt/LinearAlgebra/Matrix/ConjugateGradient.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/ConjugateGradient.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/conjugate-gradient-method/index.html#init).

## Conjugate gradient state after $k$ steps

The `k`-th conjugate gradient state from `x₀` for the system `A x = b`.

Formalized by `MathlibExt.LinearAlgebra.Matrix.ConjugateGradient.iterate`, a definition declared in [MathlibExt/LinearAlgebra/Matrix/ConjugateGradient.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/ConjugateGradient.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/conjugate-gradient-method/index.html#iterate).

## CG stays in the Krylov space

`x_k - x₀ ∈ 𝒦_k(A, r₀)`.

Formalized by `MathlibExt.LinearAlgebra.Matrix.ConjugateGradient.iterate_x_sub_mem_krylov`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/ConjugateGradient.lean, line 278](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/ConjugateGradient.lean#L278). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/conjugate-gradient-method/index.html#iterate-x-sub-mem-krylov).

## CG minimizes the energy norm of the error over the Krylov space

For the solution `x⋆`
of `A x⋆ = b`, `‖x_k - x⋆‖_A ≤ ‖x₀ + z - x⋆‖_A` for every `z ∈ 𝒦_k(A, r₀)`.

Formalized by `MathlibExt.LinearAlgebra.Matrix.ConjugateGradient.energyNorm_iterate_le`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/ConjugateGradient.lean, line 285](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/ConjugateGradient.lean#L285). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/conjugate-gradient-method/index.html#energy-norm-iterate-le).

## The Chebyshev bound for Krylov energy minimizers

If the eigenvalues of `A` lie in
`[a, c]` with `0 < a`, and `x` minimizes `‖· - x⋆‖_A` over `x₀ + 𝒦_k(A, A (x⋆ - x₀))`, then
`‖x - x⋆‖_A ≤ 2 ((√κ - 1) / (√κ + 1))^k ‖x₀ - x⋆‖_A` with `κ = c / a`.

Formalized by `MathlibExt.LinearAlgebra.Matrix.ConjugateGradient.energyNorm_le_of_isMin_krylov`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/ConjugateGradient.lean, line 509](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/ConjugateGradient.lean#L509). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/conjugate-gradient-method/index.html#energy-norm-le-of-is-min-krylov).

## The conjugate gradient error bound

If the eigenvalues of `A` lie in `[a, c]` with
`0 < a` and `A x⋆ = b`, the CG iterates satisfy
`‖x_k - x⋆‖_A ≤ 2 ((√κ - 1) / (√κ + 1))^k ‖x₀ - x⋆‖_A` with `κ = c / a`.

Formalized by `MathlibExt.LinearAlgebra.Matrix.ConjugateGradient.energyNorm_iterate_sub_le`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/ConjugateGradient.lean, line 563](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/ConjugateGradient.lean#L563). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/conjugate-gradient-method/index.html#energy-norm-iterate-sub-le).

## Spectral condition number of a positive definite matrix

The spectral condition number `λ_max / λ_min` of a positive definite matrix. For `n = 0` it
is `0 / 0 = 0` (no eigenvalues), a junk value; the bound below is stated for `0 < n`.

Formalized by `MathlibExt.LinearAlgebra.Matrix.ConjugateGradient.condNum`, a definition declared in [MathlibExt/LinearAlgebra/Matrix/ConjugateGradient.lean, line 575](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/ConjugateGradient.lean#L575). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/conjugate-gradient-method/index.html#cond-num).

## The conjugate gradient error bound in terms of the condition number

**The conjugate gradient error bound in terms of the condition number** `κ` of `A`:
`‖x_k - x⋆‖_A ≤ 2 ((√κ - 1) / (√κ + 1))^k ‖x₀ - x⋆‖_A`.

Formalized by `MathlibExt.LinearAlgebra.Matrix.ConjugateGradient.energyNorm_iterate_sub_le_condNum`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/ConjugateGradient.lean, line 581](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/ConjugateGradient.lean#L581). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/conjugate-gradient-method/index.html#energy-norm-iterate-sub-le-cond-num).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Conjugate gradient method](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/conjugate-gradient-method/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/LinearAlgebra/matrix-decompositions/conjugate-gradient-method)
