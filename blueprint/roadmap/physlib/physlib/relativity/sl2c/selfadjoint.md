---
declaration: module
origin: cited
lean: Lorentz.ℍ₂, Lorentz.SL2C.toSelfAdjointMap', Lorentz.SL2C.toSelfAdjointMap_det_one', Lorentz.SL2C.toSelfAdjointEquiv, Lorentz.SL2C.toSelfAdjointMap_mul, Lorentz.SL2C.toSelfAdjointMap_similar_det
statement: formalized
proof: formalized
---

# Extra lemmas regarding `Lorentz.SL2C.toSelfAdjointMap`

The module `Physlib.Relativity.SL2C.SelfAdjoint`, [Physlib/Relativity/SL2C/SelfAdjoint.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/SelfAdjoint.lean): 6 declarations, 3 with a docstring.

> This file redefines `Lorentz.SL2C.toSelfAdjointMap` by dropping the special linear condition for its
> first argument `M`. Then, `Lorentz.SL2C.toSelfAdjointMap_det_one` is proved for `M` being upper
> triangular.

## Main definitions

> - `Lorentz.SL2C.toSelfAdjointMap'`: definitionally equal to `Lorentz.SL2C.toSelfAdjointMap` but `M`
> is not required to be special linear.
> - `Lorentz.SL2C.toSelfAdjointMap_det_one'`: proves `Lorentz.SL2C.toSelfAdjointMap_det_one` with the
> additional requirement that `M` be upper triangular. The general case is reduced to this special
> case via `Matrix.schur_triangulation` in `Lorentz.SL2C.toSelfAdjointMap_det_one`.

**`Lorentz.ℍ₂`**, an abbrev, [line 42](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/SelfAdjoint.lean#L42).

> A convenient abbreviation for the type of self-adjoint complex 2-by-2 matrices.

```lean
noncomputable abbrev ℍ₂
```

**`Lorentz.SL2C.toSelfAdjointMap'`**, a def, [line 48](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/SelfAdjoint.lean#L48).

> Definitionally equal to `Lorentz.SL2C.toSelfAdjointMap` but dropping the requirement that `M` be
> special linear.

```lean
noncomputable def toSelfAdjointMap' (M : ℂ²ˣ²) : ℍ₂ →ₗ[ℝ] ℍ₂
```

## Showing `Lorentz.SL2C.toSelfAdjointMap` has determinant 1

> Since `Lorentz.ℍ₂` as a real vector space has the 4 Pauli matrices as basis, we know that its vector
> representation consists of 4 real components. This makes the matrix representation of
> `toSelfAdjointMap M` a 4-by-4 real matrix `F`. To make the computation of `F.det` manageable, the
> following basis is used instead of the Pauli matrices to induce as many zeros as possible in `F`:
>
> $$
> E_0 = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix},
> E_1 = \begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix},
> E_2 = \sigma_1 = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix},
> E_3 = -\sigma_2 = \begin{bmatrix} 0 & i \\ -i & 0 \end{bmatrix},
> $$
>
> Suppose that $M = \begin{bmatrix} x & □ \\ 0 & y \end{bmatrix}$ is upper triangular, the basis
> $\{E_k\}_{k=0}^3$ induces the matrix representation
>
> $$
> F = \begin{bmatrix}
>   \lvert x\rvert^2 & □ & □ & □ \\
>   0 & \lvert y\rvert^2 & 0 & 0 \\
>   0 & □ & \operatorname{Re}(x\bar{y}) & -\operatorname{Im}(x\bar{y}) \\
>   0 & □ & \operatorname{Im}(x\bar{y}) & \operatorname{Re}(x\bar{y}) \\
> \end{bmatrix}.
> $$
>
> If $xy = 1$, the Schur complement formula `Matrix.det_fromBlocks₂₂` yields
>
> $$\begin{align}
> \det F &=
> \begin{vmatrix}
>   \operatorname{Re}(x\bar{y}) & -\operatorname{Im}(x\bar{y}) \\
>   \operatorname{Im}(x\bar{y}) & \operatorname{Re}(x\bar{y})
> \end{vmatrix} \det\left(\begin{bmatrix} \lvert x\rvert^2 & □ \\ 0 & \lvert y\rvert^2 \end{bmatrix} -
>   \begin{bmatrix} □ & □ \\ 0 & 0 \end{bmatrix}
>   \begin{bmatrix} □ & □ \\ □ & □ \end{bmatrix}
>   \begin{bmatrix} 0 & □ \\ 0 & □ \end{bmatrix}
> \right) \\ &=
> \lvert x\bar{y}\rvert^2 \lvert x\rvert^2 \lvert y\rvert^2 = \lvert xy\rvert^4 = 1.
> \end{align}$$
>
> This concludes `Lorentz.SL2C.toSelfAdjointMap_det_one'`. To get
> `Lorentz.SL2C.toSelfAdjointMap_det_one`, triangulate the special linear matrix using
> `Matrix.schur_triangulation`, and observe that `Matrix.schurTriangulation` preserves the determinant
> which is 1.

**`Lorentz.SL2C.toSelfAdjointMap_det_one'`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/SelfAdjoint.lean#L98).

```lean
lemma toSelfAdjointMap_det_one' {M : ℂ²ˣ²} (hM : M.IsUpperTriangular) (detM : M.det = 1) :
    LinearMap.det (toSelfAdjointMap' M) = 1
```

**`Lorentz.SL2C.toSelfAdjointEquiv`**, a def, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/SelfAdjoint.lean#L180).

> This promotes `Lorentz.SL2C.toSelfAdjointMap M` and its definitional equivalence,
> `Lorentz.SL2C.toSelfAdjointMap' M`, to a linear equivalence by recognizing the linear inverse to be
> `Lorentz.SL2C.toSelfAdjointMap M⁻¹`, i.e., `Lorentz.SL2C.toSelfAdjointMap' M⁻¹`.

```lean
noncomputable def toSelfAdjointEquiv (M : ℂ²ˣ²) [Invertible M] : ℍ₂ ≃ₗ[ℝ] ℍ₂
```

**`Lorentz.SL2C.toSelfAdjointMap_mul`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/SelfAdjoint.lean#L192).

```lean
lemma toSelfAdjointMap_mul (M N : ℂ²ˣ²) :
    toSelfAdjointMap' (M * N) = toSelfAdjointMap' M ∘ₗ toSelfAdjointMap' N
```

**`Lorentz.SL2C.toSelfAdjointMap_similar_det`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/SelfAdjoint.lean#L197).

```lean
lemma toSelfAdjointMap_similar_det (M N : ℂ²ˣ²) [Invertible M] :
    LinearMap.det (toSelfAdjointMap' (M * N * M⁻¹)) = LinearMap.det (toSelfAdjointMap' N)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Relativity/SL2C/SelfAdjoint.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/SelfAdjoint.lean)
