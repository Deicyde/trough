---
declaration: module
origin: cited
lean: Matrix.crossProductMatrix, Matrix.crossProductMatrix_mulVec, Matrix.crossProductMatrix_transpose, Matrix.crossProductVee, Matrix.crossProductVee_crossProductMatrix, Matrix.crossProductMatrix_crossProductVee
statement: formalized
proof: formalized
---

# The hat map on three-dimensional vectors

The module `Physlib.Mathematics.Modules.CrossProductMatrix`, [Physlib/Mathematics/Modules/CrossProductMatrix.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Modules/CrossProductMatrix.lean): 6 declarations, 6 with a docstring.

> The hat map sends a vector `ω : Fin 3 → ℝ` to the skew-symmetric matrix `[ω]ₓ` characterised by
> `[ω]ₓ *ᵥ v = ω ⨯₃ v`. It realises the correspondence between `ℝ³` and the skew-symmetric `3 × 3`
> matrices (the Lie algebra `𝖘𝖔(3)`), and underlies the angular velocity of a rigid body.
> The vee map only selects matrix entries and is defined for arbitrary coefficient types,
> including operator-valued matrices.

**`Matrix.crossProductMatrix`**, a def, [line 28](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Modules/CrossProductMatrix.lean#L28).

> The hat map `[ω]ₓ`: the skew-symmetric `3 × 3` matrix acting as the cross product with `ω`,
> i.e. `[ω]ₓ *ᵥ v = ω ⨯₃ v`.

```lean
def crossProductMatrix (ω : Fin 3 → ℝ) : Matrix (Fin 3) (Fin 3) ℝ
```

**`Matrix.crossProductMatrix_mulVec`**, a lemma, [line 33](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Modules/CrossProductMatrix.lean#L33).

> The hat matrix acts on a vector as the cross product.

```lean
lemma crossProductMatrix_mulVec (ω v : Fin 3 → ℝ) :
    crossProductMatrix ω *ᵥ v = ω ⨯₃ v
```

**`Matrix.crossProductMatrix_transpose`**, a lemma, [line 41](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Modules/CrossProductMatrix.lean#L41).

> The hat map produces skew-symmetric matrices.

```lean
lemma crossProductMatrix_transpose (ω : Fin 3 → ℝ) :
    (crossProductMatrix ω)ᵀ = - crossProductMatrix ω
```

**`Matrix.crossProductVee`**, a def, [line 48](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Modules/CrossProductMatrix.lean#L48).

> The vee map: reads the vector off a `3 × 3` matrix with arbitrary coefficients.
> For real coefficients, it is a left inverse of the hat map.

```lean
def crossProductVee {α : Type*} (A : Matrix (Fin 3) (Fin 3) α) : Fin 3 → α
```

**`Matrix.crossProductVee_crossProductMatrix`**, a lemma, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Modules/CrossProductMatrix.lean#L53).

> The vee map is a left inverse of the hat map.

```lean
lemma crossProductVee_crossProductMatrix (ω : Fin 3 → ℝ) :
    crossProductVee (crossProductMatrix ω) = ω
```

**`Matrix.crossProductMatrix_crossProductVee`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Modules/CrossProductMatrix.lean#L61).

> On skew-symmetric matrices the hat map is also a right inverse of the vee map: if `Aᵀ = -A`
> then `[Aᵛ]ₓ = A`. Together with `crossProductVee_crossProductMatrix` this identifies `ℝ³` with the
> skew-symmetric `3 × 3` matrices `𝖘𝖔(3)`.

```lean
lemma crossProductMatrix_crossProductVee {A : Matrix (Fin 3) (Fin 3) ℝ} (hA : Aᵀ = -A) :
    crossProductMatrix (crossProductVee A) = A
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Mathematics/Modules/CrossProductMatrix.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Modules/CrossProductMatrix.lean)
