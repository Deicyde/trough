---
declaration: module
origin: cited
lean: Fermion.Dirac.gammaMatrix_anticomm, Fermion.Dirac.gamma_anticomm, Fermion.Dirac.gammaMatrix, Fermion.Dirac.gammaMatrix_toMatrix, Fermion.Dirac.gammaMatrix_basis_toMatrix, Fermion.Dirac.gammaMatrix_basis_anticomm, Fermion.Dirac.gammaMatrix_mul_self, Fermion.Dirac.gamma
statement: formalized
proof: formalized
---

# Gamma endomorphisms of Dirac fermions

The module `Physlib.Relativity.Fermions.Dirac.GammaMatrices`, [Physlib/Relativity/Fermions/Dirac/GammaMatrices.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/GammaMatrices.lean): 29 declarations, 29 with a docstring, 2 listed as significant.

> The basis `chiralBasis` orders the coordinates as
> `(left 0, left 1, dualRight 0, dualRight 1)`. The Weyl bases are the standard
> coordinate bases: the first component has an undotted upper spinor index and the
> second a dotted lower spinor index.
>
> `gammaMatrix` is Clifford multiplication by a real Lorentz vector, valued in
> complex linear endomorphisms of `Dirac`. Physlib's `Lorentz.Vector` has upper
> Lorentz indices and uses the Pauli basis `(1, -σ¹, -σ², -σ³)` for its Hermitian
> matrix representation. Thus `gammaMatrix v` has upper-right block
> `v⁰ 1 - vⁱ σⁱ` and lower-left block `v⁰ 1 + vⁱ σⁱ` in the chiral basis.
>
> The upper-index components `gamma μ` are derived by raising the index of
> `gammaMatrix (Lorentz.Vector.basis μ)`. In particular,
> `gammaMatrix v = v⁰ gamma 0 - vⁱ gamma i`, with signature `(+,-,-,-)`.
> These coordinates differ from the Dirac representation in
> `Physlib.Relativity.CliffordAlgebra`.
>
> The Clifford relations hold at the endomorphism level. The chirality operator
> `gamma5` has matrix `diag(-1, -1, 1, 1)`, and defines the complementary projectors
> `leftChiralProjector` and `rightChiralProjector`.

## A. Clifford multiplication by Lorentz vectors

**`Fermion.Dirac.gammaMatrix`**, a def, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/GammaMatrices.lean#L49).

> Clifford multiplication by a Lorentz vector on `Dirac`, defined using its chiral basis.
> This map is real linear because `Lorentz.Vector` is a real vector space. Each value is
> a complex linear endomorphism; multiplication is composition, with the right factor first.

```lean
def gammaMatrix : Lorentz.Vector →ₗ[ℝ] Module.End ℂ Dirac
```

**`Fermion.Dirac.gammaMatrix_toMatrix`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/GammaMatrices.lean#L74).

> The chiral matrix of Clifford multiplication has blocks `[0, v_μ σ^μ; v^μ σ^μ, 0]`.

```lean
lemma gammaMatrix_toMatrix (v : Lorentz.Vector) :
    LinearMap.toMatrix chiralBasis chiralBasis (gammaMatrix v) =
      (fromBlocks 0 (∑ μ, (minkowskiMatrix μ μ * v μ) • PauliMatrix.pauliMatrix μ)
        (∑ μ, v μ • PauliMatrix.pauliMatrix μ) 0).submatrix
        finSumFinEquiv.symm finSumFinEquiv.symm
```

**`Fermion.Dirac.gammaMatrix_basis_toMatrix`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/GammaMatrices.lean#L82).

> The chiral matrices of Clifford multiplication on the Lorentz basis vectors.

```lean
lemma gammaMatrix_basis_toMatrix (μ : Fin 1 ⊕ Fin 3) :
    LinearMap.toMatrix chiralBasis chiralBasis (gammaMatrix (Lorentz.Vector.basis μ)) =
      match μ with
      | Sum.inl 0 => !![0, 0, 1, 0; 0, 0, 0, 1; 1, 0, 0, 0; 0, 1, 0, 0]
      | Sum.inr 0 => !![0, 0, 0, -1; 0, 0, -1, 0; 0, 1, 0, 0; 1, 0, 0, 0]
      | Sum.inr 1 => !![0, 0, 0, I; 0, 0, -I, 0; 0, -I, 0, 0; I, 0, 0, 0]
      | Sum.inr 2 => !![0, 0, -1, 0; 0, 0, 0, 1; 1, 0, 0, 0; 0, -1, 0, 0]
```

**`Fermion.Dirac.gammaMatrix_basis_anticomm`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/GammaMatrices.lean#L100).

> The Clifford anticommutator on pairs of Lorentz basis vectors.

```lean
lemma gammaMatrix_basis_anticomm (μ ν : Fin 1 ⊕ Fin 3) :
    gammaMatrix (Lorentz.Vector.basis μ) * gammaMatrix (Lorentz.Vector.basis ν) +
      gammaMatrix (Lorentz.Vector.basis ν) * gammaMatrix (Lorentz.Vector.basis μ) =
      (2 * ⟪Lorentz.Vector.basis μ, Lorentz.Vector.basis ν⟫ₘ) •
        (1 : Module.End ℂ Dirac)
```

**`Fermion.Dirac.gammaMatrix_anticomm`**, a theorem, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/GammaMatrices.lean#L114). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Clifford multiplication satisfies the anticommutator relation for the Minkowski product.

```lean
theorem gammaMatrix_anticomm (v w : Lorentz.Vector) :
    gammaMatrix v * gammaMatrix w + gammaMatrix w * gammaMatrix v =
      (2 * ⟪v, w⟫ₘ) • (1 : Module.End ℂ Dirac)
```

**`Fermion.Dirac.gammaMatrix_mul_self`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/GammaMatrices.lean#L133).

> Clifford multiplication squares to the Minkowski norm squared times the identity.

```lean
lemma gammaMatrix_mul_self (v : Lorentz.Vector) :
    gammaMatrix v * gammaMatrix v = ⟪v, v⟫ₘ • (1 : Module.End ℂ Dirac)
```

## B. Upper-index gamma components

**`Fermion.Dirac.gamma`**, a def, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/GammaMatrices.lean#L142).

> The upper-index gamma components `γ^μ`, obtained by raising the index of
> Clifford multiplication on the Lorentz basis. Their chiral blocks are `[0, σ^μ; bar σ^μ, 0]`.

```lean
def gamma (μ : Fin 1 ⊕ Fin 3) : Module.End ℂ Dirac
```

**`Fermion.Dirac.gammaMatrix_basis`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/GammaMatrices.lean#L146).

> Clifford multiplication on a Lorentz basis vector is the corresponding lower-index gamma.

```lean
lemma gammaMatrix_basis (μ : Fin 1 ⊕ Fin 3) :
    gammaMatrix (Lorentz.Vector.basis μ) = minkowskiMatrix μ μ • gamma μ
```

**`Fermion.Dirac.gammaMatrix_eq_sum`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/GammaMatrices.lean#L151).

> Clifford multiplication contracts the lower-index vector coordinates with `γ^μ`.

```lean
lemma gammaMatrix_eq_sum (v : Lorentz.Vector) :
    gammaMatrix v = ∑ μ, (minkowskiMatrix μ μ * v μ) • gamma μ
```

**`Fermion.Dirac.gamma_toMatrix`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/GammaMatrices.lean#L162).

> The matrix of a gamma endomorphism in the chiral basis.

```lean
lemma gamma_toMatrix (μ : Fin 1 ⊕ Fin 3) :
    LinearMap.toMatrix chiralBasis chiralBasis (gamma μ) =
      match μ with
      | Sum.inl 0 => !![0, 0, 1, 0; 0, 0, 0, 1; 1, 0, 0, 0; 0, 1, 0, 0]
      | Sum.inr 0 => !![0, 0, 0, 1; 0, 0, 1, 0; 0, -1, 0, 0; -1, 0, 0, 0]
      | Sum.inr 1 => !![0, 0, 0, -I; 0, 0, I, 0; 0, I, 0, 0; -I, 0, 0, 0]
      | Sum.inr 2 => !![0, 0, 1, 0; 0, 0, 0, -1; -1, 0, 0, 0; 0, 1, 0, 0]
```

**`Fermion.Dirac.gamma_anticomm`**, a theorem, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/GammaMatrices.lean#L174). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The Clifford anticommutator for gamma endomorphisms, with signature `(+,-,-,-)`.

```lean
theorem gamma_anticomm (μ ν : Fin 1 ⊕ Fin 3) :
    gamma μ * gamma ν + gamma ν * gamma μ =
      (2 * (minkowskiMatrix μ ν : ℂ)) • (1 : Module.End ℂ Dirac)
```

**`Fermion.Dirac.gamma_mul_self`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/GammaMatrices.lean#L184).

> A gamma endomorphism squares to the corresponding diagonal metric sign.

```lean
lemma gamma_mul_self (μ : Fin 1 ⊕ Fin 3) :
    gamma μ * gamma μ = (minkowskiMatrix μ μ : ℂ) • (1 : Module.End ℂ Dirac)
```

**`Fermion.Dirac.gamma_inl_zero_mul_self`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/GammaMatrices.lean#L191).

> The time gamma endomorphism squares to the identity.

```lean
lemma gamma_inl_zero_mul_self : gamma (Sum.inl 0) * gamma (Sum.inl 0) = 1
```

**`Fermion.Dirac.gamma_inr_mul_self`**, a lemma, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/GammaMatrices.lean#L196).

> Each spatial gamma endomorphism squares to minus the identity.

```lean
lemma gamma_inr_mul_self (i : Fin 3) : gamma (Sum.inr i) * gamma (Sum.inr i) = -1
```

**`Fermion.Dirac.gamma_mul_gamma_of_ne`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/GammaMatrices.lean#L200).

> Gamma endomorphisms with distinct Lorentz indices anticommute.

```lean
lemma gamma_mul_gamma_of_ne {μ ν : Fin 1 ⊕ Fin 3} (h : μ ≠ ν) :
    gamma μ * gamma ν = -(gamma ν * gamma μ)
```

## C. Chirality

**`Fermion.Dirac.gamma5`**, a def, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/GammaMatrices.lean#L209).

> The chirality endomorphism `γ⁵ = i γ⁰ γ¹ γ² γ³`.

```lean
def gamma5 : Module.End ℂ Dirac
```

**`Fermion.Dirac.gamma5_toMatrix`**, a lemma, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/GammaMatrices.lean#L215).

> In the chiral basis, `γ⁵` is negative on the left-handed coordinates and positive
> on the dual-right-handed coordinates.

```lean
lemma gamma5_toMatrix :
    LinearMap.toMatrix chiralBasis chiralBasis gamma5 = diagonal ![-1, -1, 1, 1]
```

**`Fermion.Dirac.gamma5_mul_self`**, a lemma, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/GammaMatrices.lean#L224).

> The chirality endomorphism squares to the identity.

```lean
lemma gamma5_mul_self : gamma5 * gamma5 = 1
```

**`Fermion.Dirac.gamma5_mul_gamma`**, a lemma, [line 233](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/GammaMatrices.lean#L233).

> The chirality endomorphism anticommutes with every gamma endomorphism.

```lean
lemma gamma5_mul_gamma (μ : Fin 1 ⊕ Fin 3) : gamma5 * gamma μ = -(gamma μ * gamma5)
```

**`Fermion.Dirac.gamma5_mul_gammaMatrix`**, a lemma, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/GammaMatrices.lean#L242).

> Chirality anticommutes with Clifford multiplication by every Lorentz vector.

```lean
lemma gamma5_mul_gammaMatrix (v : Lorentz.Vector) :
    gamma5 * gammaMatrix v = -(gammaMatrix v * gamma5)
```

## D. Chiral projectors

**`Fermion.Dirac.leftChiralProjector`**, a def, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/GammaMatrices.lean#L251).

> The projector `(1 - γ⁵) / 2` onto the left-handed Weyl component.

```lean
def leftChiralProjector : Module.End ℂ Dirac
```

**`Fermion.Dirac.rightChiralProjector`**, a def, [line 254](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/GammaMatrices.lean#L254).

> The projector `(1 + γ⁵) / 2` onto the dual-right-handed Weyl component.

```lean
def rightChiralProjector : Module.End ℂ Dirac
```

**`Fermion.Dirac.leftChiralProjector_toMatrix`**, a lemma, [line 258](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/GammaMatrices.lean#L258).

> The left chiral projector retains the first two chiral coordinates.

```lean
lemma leftChiralProjector_toMatrix :
    LinearMap.toMatrix chiralBasis chiralBasis leftChiralProjector = diagonal ![1, 1, 0, 0]
```

**`Fermion.Dirac.rightChiralProjector_toMatrix`**, a lemma, [line 267](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/GammaMatrices.lean#L267).

> The right chiral projector retains the last two chiral coordinates.

```lean
lemma rightChiralProjector_toMatrix :
    LinearMap.toMatrix chiralBasis chiralBasis rightChiralProjector = diagonal ![0, 0, 1, 1]
```

**`Fermion.Dirac.leftChiralProjector_mul_self`**, a lemma, [line 276](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/GammaMatrices.lean#L276).

> The left chiral projector is idempotent.

```lean
lemma leftChiralProjector_mul_self : leftChiralProjector * leftChiralProjector =
    leftChiralProjector
```

**`Fermion.Dirac.rightChiralProjector_mul_self`**, a lemma, [line 284](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/GammaMatrices.lean#L284).

> The right chiral projector is idempotent.

```lean
lemma rightChiralProjector_mul_self : rightChiralProjector * rightChiralProjector =
    rightChiralProjector
```

**`Fermion.Dirac.leftChiralProjector_mul_rightChiralProjector`**, a lemma, [line 292](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/GammaMatrices.lean#L292).

> The chiral projectors are orthogonal.

```lean
lemma leftChiralProjector_mul_rightChiralProjector :
    leftChiralProjector * rightChiralProjector = 0
```

**`Fermion.Dirac.rightChiralProjector_mul_leftChiralProjector`**, a lemma, [line 300](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/GammaMatrices.lean#L300).

> The chiral projectors are orthogonal in the reverse order as well.

```lean
lemma rightChiralProjector_mul_leftChiralProjector :
    rightChiralProjector * leftChiralProjector = 0
```

**`Fermion.Dirac.leftChiralProjector_add_rightChiralProjector`**, a lemma, [line 308](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/GammaMatrices.lean#L308).

> The two chiral projectors resolve the identity on `Dirac`.

```lean
lemma leftChiralProjector_add_rightChiralProjector :
    leftChiralProjector + rightChiralProjector = 1
```

## Depends on

- [Dirac fermions](basic.md)
- [Minkowski product on Lorentz vectors](../../tensors/part-03/realtensor-vector-minkowskiproduct.md)

## Sources

- [Physlib/Relativity/Fermions/Dirac/GammaMatrices.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/GammaMatrices.lean)
