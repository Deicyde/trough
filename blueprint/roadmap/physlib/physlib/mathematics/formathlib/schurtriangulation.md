---
declaration: module
origin: cited
lean: Fin.subNat', Equiv.sumEquivSigmalCond, Equiv.finAddEquivSigmaCond, Equiv.finAddEquivSigmaCond_true, Equiv.finAddEquivSigmaCond_false, Matrix.UpperTriangular, LinearMap.SchurTriangulationAux, LinearMap.SchurTriangulationAux.of
statement: formalized
proof: formalized
---

# Schur triangulation

The module `Physlib.Mathematics.ForMathlib.SchurTriangulation`, [Physlib/Mathematics/ForMathlib/SchurTriangulation.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/SchurTriangulation.lean): 15 declarations (2 instances with no name), 13 with a docstring.

> Schur triangulation is more commonly known as Schur decomposition or Schur triangularization, but
> "triangulation" makes the API more readable. It states that a square matrix over an algebraically
> closed field, e.g., `ℂ`, is unitarily similar to an upper triangular matrix.

## Main definitions

> - `Matrix.schur_triangulation` : a matrix `A : Matrix n n 𝕜` with `𝕜` being algebraically closed can
> be decomposed as `A = U * T * star U` where `U` is unitary and `T` is upper triangular.
> - `Matrix.schurTriangulationUnitary` : the unitary matrix `U` as previously stated.
> - `Matrix.schurTriangulation` : the upper triangular matrix `T` as previously stated.
> - Some auxiliary definitions are not meant to be used directly, but
> `LinearMap.SchurTriangulationAux.of` contains the main algorithm for the triangulation procedure.

**`Fin.subNat'`**, a def, [line 33](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/SchurTriangulation.lean#L33).

> `subNat' i h` subtracts `m` from `i`. This is an alternative form of `Fin.subNat`.

```lean
def Fin.subNat' (i : Fin (m + n)) (h : ¬ i < m) : Fin n
```

**`Equiv.sumEquivSigmalCond`**, a def, [line 39](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/SchurTriangulation.lean#L39).

> An alternative form of `Equiv.sumEquivSigmaBool` where `Bool.casesOn` is replaced by `cond`.

```lean
def sumEquivSigmalCond : Fin m ⊕ Fin n ≃ Σ b, cond b (Fin m) (Fin n)
```

**`Equiv.finAddEquivSigmaCond`**, a def, [line 47](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/SchurTriangulation.lean#L47).

> The composition of `finSumFinEquiv` and `Equiv.sumEquivSigmalCond` used by
> `LinearMap.SchurTriangulationAux.of`.

```lean
def finAddEquivSigmaCond : Fin (m + n) ≃ Σ b, cond b (Fin m) (Fin n)
```

**`Equiv.finAddEquivSigmaCond_true`**, a lemma, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/SchurTriangulation.lean#L52).

```lean
lemma finAddEquivSigmaCond_true (h : i < m) : finAddEquivSigmaCond i = ⟨true, i, h⟩
```

**`Equiv.finAddEquivSigmaCond_false`**, a lemma, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/SchurTriangulation.lean#L55).

```lean
lemma finAddEquivSigmaCond_false (h : ¬ i < m) : finAddEquivSigmaCond i = ⟨false, i.subNat' h⟩
```

**An instance with no name**, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/SchurTriangulation.lean#L66).

> The type family parameterized by `Bool` is finite if each type variant is finite.

```lean
instance [M : Fintype m] [N : Fintype n] (b : Bool) : Fintype (cond b m n)
```

**An instance with no name**, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/SchurTriangulation.lean#L70).

> The type family parameterized by `Bool` has decidable equality if each type variant is
> decidable.

```lean
instance [DecidableEq m] [DecidableEq n] : DecidableEq (Σ b, cond b m n)
```

**`Matrix.UpperTriangular`**, an abbrev, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/SchurTriangulation.lean#L80).

> The subtype of upper triangular matrices.

```lean
abbrev UpperTriangular (n R) [LT n] [CommRing R]
```

**`LinearMap.SchurTriangulationAux`**, a structure, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/SchurTriangulation.lean#L93).

> **Don't use this definition directly.** Instead, use `Matrix.schurTriangulationBasis`,
> `Matrix.schurTriangulationUnitary`, and `Matrix.schurTriangulation`. See also
> `LinearMap.SchurTriangulationAux.of` and `Matrix.schurTriangulationAux`.

```lean
structure SchurTriangulationAux (f : Module.End 𝕜 E) where
  /-- The dimension of the inner product space `E`. -/
  dim : ℕ
  hdim : Module.finrank 𝕜 E = dim
  /-- An orthonormal basis of `E` that induces an upper triangular form for `f`. -/
  basis : OrthonormalBasis (Fin dim) 𝕜 E
  upperTriangular : (toMatrix basis.toBasis basis.toBasis f).IsUpperTriangular
```

## Schur's recursive triangulation procedure

> Given a linear endomorphism `f` on a non-trivial finite-dimensional vector space `E` over an
> algebraically closed field `𝕜`, one can always pick an eigenvalue `μ` of `f` whose corresponding
> eigenspace `V` is non-trivial. Given that `E` is also an inner product space, let `bV` and `bW` be
> orthonormal bases for `V` and `Vᗮ` respectively. Then, the collection of vectors in `bV` and `bW`
> forms an orthonormal basis `bE` for `E`, as the direct sum of `V` and `Vᗮ` is an internal
> decomposition of `E`. The matrix representation of `f` with respect to `bE` satisfies
>
> $$
> \sideset{_\mathrm{bE}}{_\mathrm{bE}}{[f]} =
> \begin{bmatrix}
>   \sideset{_\mathrm{bV}}{_\mathrm{bV}}{[f]} &
>   \sideset{_\mathrm{bW}}{_\mathrm{bV}}{[f]} \\
>   \sideset{_\mathrm{bV}}{_\mathrm{bW}}{[f]} &
>   \sideset{_\mathrm{bW}}{_\mathrm{bW}}{[f]}
> \end{bmatrix} =
> \begin{bmatrix} \mu I & □ \\ 0 & \sideset{_\mathrm{bW}}{_\mathrm{bW}}{[f]} \end{bmatrix},
> $$
>
> which is upper triangular as long as $\sideset{_\mathrm{bW}}{_\mathrm{bW}}{[f]}$ is. Finally, one
> observes that the recursion from $\sideset{_\mathrm{bE}}{_\mathrm{bE}}{[f]}$ to
> $\sideset{_\mathrm{bW}}{_\mathrm{bW}}{[f]}$ is well-founded, as the dimension of `bW` is smaller
> than that of `bE` because `bV` is non-trivial.
>
> However, in order to leverage `DirectSum.IsInternal.collectedOrthonormalBasis`, the type
> `Σ b, cond b (Fin m) (Fin n)` has to be used instead of the more natural `Fin m ⊕ Fin n` while their
> equivalence is propositionally established by `Equiv.sumEquivSigmalCond`.

**`LinearMap.SchurTriangulationAux.of`**, a def, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/SchurTriangulation.lean#L138).

> **Don't use this definition directly.** This is the key algorithm behind
> `Matrix.schur_triangulation`.

```lean
protected noncomputable def SchurTriangulationAux.of
    [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [FiniteDimensional 𝕜 E] (f : Module.End 𝕜 E) :
    SchurTriangulationAux f
```

**`Matrix.schurTriangulationAux`**, a def, [line 239](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/SchurTriangulation.lean#L239).

> This is `LinearMap.SchurTriangulationAux` adapted for matrices in the
> Euclidean space.

```lean
noncomputable def schurTriangulationAux :
    OrthonormalBasis n 𝕜 (EuclideanSpace 𝕜 n) × UpperTriangular n 𝕜
```

**`Matrix.schurTriangulationBasis`**, a def, [line 256](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/SchurTriangulation.lean#L256).

> The change of basis that induces the upper triangular form `A.schurTriangulation` of a matrix
> `A` over an algebraically closed field.

```lean
noncomputable def schurTriangulationBasis : OrthonormalBasis n 𝕜 (EuclideanSpace 𝕜 n)
```

**`Matrix.schurTriangulationUnitary`**, a def, [line 261](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/SchurTriangulation.lean#L261).

> The unitary matrix that induces the upper triangular form `A.schurTriangulation` to which a
> matrix `A` over an algebraically closed field is unitarily similar.

```lean
noncomputable def schurTriangulationUnitary : unitaryGroup n 𝕜
```

**`Matrix.schurTriangulation`**, a def, [line 267](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/SchurTriangulation.lean#L267).

> The upper triangular form induced by `A.schurTriangulationUnitary` to which a matrix `A` over an
> algebraically closed field is unitarily similar.

```lean
noncomputable def schurTriangulation : UpperTriangular n 𝕜
```

**`Matrix.schur_triangulation`**, a lemma, [line 273](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/SchurTriangulation.lean#L273).

> **Schur triangulation**, **Schur decomposition** for matrices over an algebraically closed
> field. In particular, a complex matrix can be converted to upper-triangular form by a change of
> basis. In other words, any complex matrix is unitarily similar to an upper triangular matrix.

```lean
lemma schur_triangulation :
    A = A.schurTriangulationUnitary * A.schurTriangulation * star A.schurTriangulationUnitary
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Mathematics/ForMathlib/SchurTriangulation.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/SchurTriangulation.lean)
