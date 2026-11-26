---
declaration: module
origin: cited
lean: GlobalGaugeGroup.unitsMapHom, GlobalGaugeGroup.matrixCLM, GlobalGaugeGroup.matrixCLM_injective, GlobalGaugeGroup.matrixCLM_surjective, GlobalGaugeGroup.continuous_matrixCLM, GlobalGaugeGroup.matrixCLM_exp_smul, GlobalGaugeGroup.clmRep, GlobalGaugeGroup.derivMat
statement: formalized
proof: formalized
---

# Matter fields from matrix representations of a global gauge group

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.MatterField.OfMatrixRep`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/OfMatrixRep.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/OfMatrixRep.lean): 44 declarations, 29 with a docstring.

> Continuous representations of a global gauge group by complex matrices, and the matter fields
> they define.

## i. Overview

> A model-building table says how a field transforms by writing down a matrix. The field has an
> internal index `ι`, and a gauge transformation acts on it by an invertible `ι × ι` complex
> matrix. Such a matrix representation of the global gauge group `G` is a continuous
> homomorphism `G.group →ₜ* (Matrix ι ι ℂ)ˣ`. Its derivative `GlobalGaugeGroup.derivMat ρ c` is
> the matrix by which an element `c` of the Lie algebra acts. It is the matrix version of
> `GlobalGaugeGroup.derivRep`, and is characterised by the exponential law
> `ρ (exp (t c)) = exp (t derivMat ρ c)`.
>
> The representations named in a table are assembled from a few pieces. These are the trivial
> representation, the Kronecker product `MatrixRep.kron` and the twist `MatrixRep.charge` by a
> power of a character of the gauge group. The derivative of each is computed from the
> exponential law.
>
> A matrix representation `ρ` on `ι` gives a matter field on any target space
> `V ≃ S ⊗ (ι → ℂ)`, where `S` carries a representation of the Lorentz group. The gauge group
> acts by `ρ` on the internal index and the Lorentz group on `S`. This is
> `MatterField.ofMatrixRep`. Its action of the Lie algebra is the derivative of `ρ`, and its jet
> action is then fixed by the derivative.

## ii. Key results

> - `GlobalGaugeGroup.derivMat` : the derivative of a matrix representation, a matrix for each
>   element of the Lie algebra.
> - `GlobalGaugeGroup.apply_eq_exp_derivMat`, `GlobalGaugeGroup.derivMat_eq_of` : the exponential
>   law, and the uniqueness of the derivative.
> - `GlobalGaugeGroup.MatrixRep.trivial`, `GlobalGaugeGroup.MatrixRep.kron`,
>   `GlobalGaugeGroup.MatrixRep.charge` : the trivial representation, the Kronecker product and
>   the charge twist.
> - `GlobalGaugeGroup.MatrixRep.derivMat_trivial`, `GlobalGaugeGroup.MatrixRep.derivMat_kron`,
>   `GlobalGaugeGroup.MatrixRep.derivMat_charge` : their derivatives.
> - `GlobalGaugeGroup.MatrixRep.valEnd` : the endomorphism of `V ≃ S ⊗ (ι → ℂ)` defined by a
>   matrix on the internal index.
> - `GlobalGaugeGroup.MatrixRep.repLorentz` : the Lorentz action on `V ≃ S ⊗ (ι → ℂ)`, which
>   commutes with every `valEnd`.
> - `GlobalGaugeGroup.MatterField.ofMatrixRep` : the matter field of a matrix
>   representation.
> - `GlobalGaugeGroup.MatterField.ofMatrixRep_repAlgebra` : its action of the Lie algebra
>   is the derivative of the matrix representation.

## iv. References

> * None.

## A. The derivative of a matrix representation

> A continuous representation of `G` by invertible matrices is differentiated by viewing the
> matrices as continuous linear maps of Euclidean space, where `GlobalGaugeGroup.derivRep`
> applies.

**`GlobalGaugeGroup.unitsMapHom`**, a def, [line 95](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/OfMatrixRep.lean#L95).

> The continuous homomorphism of unit groups induced by a continuous monoid homomorphism.

```lean
noncomputable def unitsMapHom {M N : Type} [Monoid M] [Monoid N] [TopologicalSpace M]
    [TopologicalSpace N] (f : M →* N) (hf : Continuous f) : Mˣ →ₜ* Nˣ
```

**`GlobalGaugeGroup.matrixCLM`**, a def, [line 101](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/OfMatrixRep.lean#L101).

> The algebra map from complex matrices to the continuous linear endomorphisms of Euclidean
> space, a matrix acting on vectors.

```lean
noncomputable def matrixCLM :
    Matrix ι ι ℂ →ₐ[ℂ] (EuclideanSpace ℂ ι →L[ℂ] EuclideanSpace ℂ ι)
```

**`GlobalGaugeGroup.matrixCLM_injective`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/OfMatrixRep.lean#L105).

```lean
lemma matrixCLM_injective : Function.Injective (matrixCLM (ι := ι))
```

**`GlobalGaugeGroup.matrixCLM_surjective`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/OfMatrixRep.lean#L108).

```lean
lemma matrixCLM_surjective : Function.Surjective (matrixCLM (ι := ι))
```

**`GlobalGaugeGroup.continuous_matrixCLM`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/OfMatrixRep.lean#L111).

```lean
lemma continuous_matrixCLM : Continuous (matrixCLM (ι := ι))
```

**`GlobalGaugeGroup.matrixCLM_exp_smul`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/OfMatrixRep.lean#L116).

> The map `matrixCLM` commutes with the exponential of a real multiple of a matrix.

```lean
lemma matrixCLM_exp_smul (t : ℝ) (A : Matrix ι ι ℂ) :
    matrixCLM (exp (t • A)) = exp (t • matrixCLM A)
```

**`GlobalGaugeGroup.clmRep`**, a def, [line 126](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/OfMatrixRep.lean#L126).

> A matrix representation of the global gauge group `G`, as a representation on Euclidean
> space.

```lean
noncomputable def clmRep (ρ : G.group →ₜ* (Matrix ι ι ℂ)ˣ) :
    G.group →ₜ* (EuclideanSpace ℂ ι →L[ℂ] EuclideanSpace ℂ ι)ˣ
```

**`GlobalGaugeGroup.derivMat`**, a def, [line 135](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/OfMatrixRep.lean#L135).

> The derivative of a continuous matrix representation `ρ` of the global gauge group. It is the
> matrix by which an element `c` of the Lie algebra acts, with
> `ρ (exp (t c)) = exp (t derivMat ρ c)`.

```lean
noncomputable def derivMat (c : G.lieSubalgebra) : Matrix ι ι ℂ
```

**`GlobalGaugeGroup.matrixCLM_derivMat`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/OfMatrixRep.lean#L138).

```lean
lemma matrixCLM_derivMat (c : G.lieSubalgebra) :
    matrixCLM (derivMat ρ c) = derivRep (clmRep ρ) c
```

**`GlobalGaugeGroup.apply_eq_exp_derivMat`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/OfMatrixRep.lean#L144).

> The matrix representation maps the one-parameter subgroup of a generator `c` to the
> exponential of its derivative, `ρ (exp (t c)) = exp (t derivMat ρ c)`.

```lean
lemma apply_eq_exp_derivMat {c : G.lieSubalgebra} {t : ℝ} {g : G.group}
    (hg : ((g : GL κ ℂ) : Matrix κ κ ℂ) = exp (t • (c : Matrix κ κ ℂ))) :
    ((ρ g : (Matrix ι ι ℂ)ˣ) : Matrix ι ι ℂ) = exp (t • derivMat ρ c)
```

**`GlobalGaugeGroup.derivMat_eq_of`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/OfMatrixRep.lean#L153).

> The derivative of a matrix representation at `c` is the unique matrix `Z` with
> `ρ (exp (t c)) = exp (t Z)` for all `t`.

```lean
lemma derivMat_eq_of {c : G.lieSubalgebra} {Z : Matrix ι ι ℂ}
    (hZ : ∀ (t : ℝ) (g : G.group),
      ((g : GL κ ℂ) : Matrix κ κ ℂ) = exp (t • (c : Matrix κ κ ℂ)) →
        ((ρ g : (Matrix ι ι ℂ)ˣ) : Matrix ι ι ℂ) = exp (t • Z)) :
    derivMat ρ c = Z
```

## B. The standard constructions

> A character of the gauge group, such as the hypercharge phase, twists a representation by an
> integer power. The derivative of a character `χ` at `c` is a number `z` with
> `χ (exp (t c)) = exp (t z)`.

**`GlobalGaugeGroup.MatrixRep.trivial`**, a def, [line 183](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/OfMatrixRep.lean#L183).

> The trivial representation on one internal index. Every gauge transformation acts as the
> identity.

```lean
noncomputable def trivial : G.group →ₜ* (Matrix (Fin 1) (Fin 1) ℂ)ˣ
```

**`GlobalGaugeGroup.MatrixRep.derivMat_trivial`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/OfMatrixRep.lean#L187).

> The derivative of the trivial representation is zero.

```lean
lemma derivMat_trivial (c : G.lieSubalgebra) : derivMat (trivial (G := G)) c = 0
```

**`GlobalGaugeGroup.MatrixRep.kroneckerMonoidHom`**, a def, [line 193](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/OfMatrixRep.lean#L193).

> The Kronecker product of matrices, as a monoid homomorphism on pairs.

```lean
def kroneckerMonoidHom :
    Matrix ι₁ ι₁ ℂ × Matrix ι₂ ι₂ ℂ →* Matrix (ι₁ × ι₂) (ι₁ × ι₂) ℂ
```

**`GlobalGaugeGroup.MatrixRep.continuous_kroneckerMonoidHom`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/OfMatrixRep.lean#L199).

```lean
lemma continuous_kroneckerMonoidHom :
    Continuous (kroneckerMonoidHom (ι₁ := ι₁) (ι₂ := ι₂))
```

**`GlobalGaugeGroup.MatrixRep.kron`**, a def, [line 207](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/OfMatrixRep.lean#L207).

> The Kronecker product of two matrix representations, acting on the product of their
> internal indices.

```lean
noncomputable def kron (ρ₁ : G.group →ₜ* (Matrix ι₁ ι₁ ℂ)ˣ) (ρ₂ : G.group →ₜ* (Matrix ι₂ ι₂ ℂ)ˣ) :
    G.group →ₜ* (Matrix (ι₁ × ι₂) (ι₁ × ι₂) ℂ)ˣ
```

**`GlobalGaugeGroup.MatrixRep.kron_val`**, a lemma, [line 221](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/OfMatrixRep.lean#L221).

> A gauge transformation acts on the Kronecker product by the Kronecker product of its two
> actions.

```lean
lemma kron_val (ρ₁ : G.group →ₜ* (Matrix ι₁ ι₁ ℂ)ˣ) (ρ₂ : G.group →ₜ* (Matrix ι₂ ι₂ ℂ)ˣ)
    (g : G.group) :
    ((kron ρ₁ ρ₂ g : (Matrix (ι₁ × ι₂) (ι₁ × ι₂) ℂ)ˣ) : Matrix (ι₁ × ι₂) (ι₁ × ι₂) ℂ) =
      (ρ₁ g : Matrix ι₁ ι₁ ℂ) ⊗ₖ (ρ₂ g : Matrix ι₂ ι₂ ℂ)
```

**`GlobalGaugeGroup.MatrixRep.derivMat_kron`**, a lemma, [line 228](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/OfMatrixRep.lean#L228).

> The derivative of the Kronecker product of two representations is the Kronecker sum of
> their derivatives.

```lean
lemma derivMat_kron (ρ₁ : G.group →ₜ* (Matrix ι₁ ι₁ ℂ)ˣ) (ρ₂ : G.group →ₜ* (Matrix ι₂ ι₂ ℂ)ˣ)
    (c : G.lieSubalgebra) :
    derivMat (kron ρ₁ ρ₂) c =
      derivMat ρ₁ c ⊗ₖ (1 : Matrix ι₂ ι₂ ℂ) + (1 : Matrix ι₁ ι₁ ℂ) ⊗ₖ derivMat ρ₂ c
```

**`GlobalGaugeGroup.MatrixRep.scalarUnits`**, a def, [line 237](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/OfMatrixRep.lean#L237).

> The scalar matrices, as a homomorphism of unit groups from the nonzero complex numbers.

```lean
noncomputable def scalarUnits (ι : Type) [Fintype ι] [DecidableEq ι] :
    ℂˣ →* (Matrix ι ι ℂ)ˣ
```

**`GlobalGaugeGroup.MatrixRep.continuous_scalarUnits`**, a lemma, [line 241](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/OfMatrixRep.lean#L241).

```lean
lemma continuous_scalarUnits (ι : Type) [Fintype ι] [DecidableEq ι] :
    Continuous (scalarUnits ι)
```

**`GlobalGaugeGroup.MatrixRep.mul_scalarUnits_comm`**, a lemma, [line 246](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/OfMatrixRep.lean#L246).

> Scalar matrices commute with every invertible matrix.

```lean
lemma mul_scalarUnits_comm (U : (Matrix ι ι ℂ)ˣ) (z : ℂˣ) :
    U * scalarUnits ι z = scalarUnits ι z * U
```

**`GlobalGaugeGroup.MatrixRep.charge`**, a def, [line 253](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/OfMatrixRep.lean#L253).

> The twist of a matrix representation `ρ` by the `n`-th power of a character `χ`. A gauge
> transformation `g` acts by `χ(g)ⁿ ρ(g)`. This is how a field of charge `n` under a `U(1)`
> factor is built from its neutral part.

```lean
noncomputable def charge (n : ℤ) (χ : G.group →ₜ* ℂˣ) (ρ : G.group →ₜ* (Matrix ι ι ℂ)ˣ) :
    G.group →ₜ* (Matrix ι ι ℂ)ˣ
```

**`GlobalGaugeGroup.MatrixRep.charge_val`**, a lemma, [line 268](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/OfMatrixRep.lean#L268).

> A gauge transformation acts on the charge twist by the scalar `χ(g)ⁿ` times its action
> on `ρ`.

```lean
lemma charge_val (n : ℤ) (χ : G.group →ₜ* ℂˣ) (ρ : G.group →ₜ* (Matrix ι ι ℂ)ˣ) (g : G.group) :
    ((charge n χ ρ g : (Matrix ι ι ℂ)ˣ) : Matrix ι ι ℂ) =
      ((χ g ^ n : ℂˣ) : ℂ) • (ρ g : Matrix ι ι ℂ)
```

**`GlobalGaugeGroup.MatrixRep.derivMat_charge`**, a lemma, [line 275](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/OfMatrixRep.lean#L275).

> The derivative of the charge twist. If `z` is the derivative of the character `χ` at `c`,
> that is `χ (exp (t c)) = exp (t z)`, the derivative of the twist is `dρ + (n z) 1`.

```lean
lemma derivMat_charge (n : ℤ) (χ : G.group →ₜ* ℂˣ) (ρ : G.group →ₜ* (Matrix ι ι ℂ)ˣ)
    {c : G.lieSubalgebra} {z : ℂ}
    (hχ : ∀ (t : ℝ) (g : G.group),
      ((g : GL κ ℂ) : Matrix κ κ ℂ) = exp (t • (c : Matrix κ κ ℂ)) →
        ((χ g : ℂˣ) : ℂ) = Complex.exp (t * z)) :
    derivMat (charge n χ ρ) c = derivMat ρ c + ((n : ℂ) * z) • (1 : Matrix ι ι ℂ)
```

## C. Endomorphisms from matrices

> The target space of a field is `V ≃ S ⊗ (ι → ℂ)`, where the gauge group acts on the internal
> index `ι` and the Lorentz group on `S`. A matrix on `ι` then acts on `V` with `S` untouched.
> On a normed target space it acts by a continuous linear map, and a matrix representation
> becomes a continuous representation on `V`.

**`GlobalGaugeGroup.MatrixRep.valEndAlgHom`**, a def, [line 305](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/OfMatrixRep.lean#L305).

> The endomorphism of the target space `V ≃ S ⊗ (ι → ℂ)` defined by a complex matrix on
> the internal index, as an algebra map.

```lean
noncomputable def valEndAlgHom : Matrix ι ι ℂ →ₐ[ℂ] Module.End ℂ V
```

**`GlobalGaugeGroup.MatrixRep.valEnd`**, a def, [line 312](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/OfMatrixRep.lean#L312).

> The endomorphism of the target space `V ≃ S ⊗ (ι → ℂ)` defined by a complex matrix on
> the internal index, with the Lorentz factor untouched.

```lean
noncomputable def valEnd (B : Matrix ι ι ℂ) : V →ₗ[ℂ] V
```

**`GlobalGaugeGroup.MatrixRep.valEnd_apply`**, a lemma, [line 314](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/OfMatrixRep.lean#L314).

```lean
lemma valEnd_apply (B : Matrix ι ι ℂ) (d : V) :
    valEnd e B d = e.symm (LinearMap.lTensor S (Matrix.toLin' B) (e d))
```

**`GlobalGaugeGroup.MatrixRep.valEnd_apply_symm_tmul`**, a lemma, [line 318](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/OfMatrixRep.lean#L318).

> A matrix on the internal index acts on a pure tensor through its action on the vector.

```lean
lemma valEnd_apply_symm_tmul (B : Matrix ι ι ℂ) (s : S) (v : ι → ℂ) :
    valEnd e B (e.symm (s ⊗ₜ[ℂ] v)) = e.symm (s ⊗ₜ[ℂ] (B.mulVec v))
```

**`GlobalGaugeGroup.MatrixRep.valEnd_add`**, a lemma, [line 322](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/OfMatrixRep.lean#L322).

```lean
lemma valEnd_add (A B : Matrix ι ι ℂ) : valEnd e (A + B) = valEnd e A + valEnd e B
```

**`GlobalGaugeGroup.MatrixRep.valEnd_smul`**, a lemma, [line 325](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/OfMatrixRep.lean#L325).

```lean
lemma valEnd_smul (z : ℂ) (A : Matrix ι ι ℂ) : valEnd e (z • A) = z • valEnd e A
```

**`GlobalGaugeGroup.MatrixRep.valEnd_zero`**, a lemma, [line 328](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/OfMatrixRep.lean#L328).

```lean
lemma valEnd_zero : valEnd e (0 : Matrix ι ι ℂ) = 0
```

**`GlobalGaugeGroup.MatrixRep.valEnd_neg`**, a lemma, [line 330](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/OfMatrixRep.lean#L330).

```lean
lemma valEnd_neg (A : Matrix ι ι ℂ) : valEnd e (-A) = -valEnd e A
```

**`GlobalGaugeGroup.MatrixRep.valEnd_multiset_sum`**, a lemma, [line 333](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/OfMatrixRep.lean#L333).

```lean
lemma valEnd_multiset_sum (m : Multiset (Matrix ι ι ℂ)) :
    valEnd e m.sum = (m.map (valEnd e)).sum
```

**`GlobalGaugeGroup.MatrixRep.valEnd_mul`**, a lemma, [line 337](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/OfMatrixRep.lean#L337).

```lean
lemma valEnd_mul (A B : Matrix ι ι ℂ) : valEnd e (A * B) = valEnd e A ∘ₗ valEnd e B
```

**`GlobalGaugeGroup.MatrixRep.valEnd_one`**, a lemma, [line 340](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/OfMatrixRep.lean#L340).

```lean
lemma valEnd_one : valEnd e (1 : Matrix ι ι ℂ) = LinearMap.id
```

**`GlobalGaugeGroup.MatrixRep.repLorentz`**, a def, [line 344](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/OfMatrixRep.lean#L344).

> The Lorentz action on the target space `V ≃ S ⊗ (ι → ℂ)`, the given action on the Lorentz
> factor `S` transported through the identification.

```lean
noncomputable def repLorentz (ρ : Representation ℂ SL(2,ℂ) S) : Representation ℂ SL(2,ℂ) V
```

**`GlobalGaugeGroup.MatrixRep.repLorentz_apply_symm_tmul`**, a lemma, [line 350](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/OfMatrixRep.lean#L350).

> The Lorentz action on a pure tensor acts on the Lorentz factor.

```lean
lemma repLorentz_apply_symm_tmul (ρ : Representation ℂ SL(2,ℂ) S) (Λ : SL(2,ℂ)) (s : S)
    (v : ι → ℂ) : repLorentz e ρ Λ (e.symm (s ⊗ₜ[ℂ] v)) = e.symm (ρ Λ s ⊗ₜ[ℂ] v)
```

**`GlobalGaugeGroup.MatrixRep.valEnd_comm_repLorentz`**, a lemma, [line 357](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/OfMatrixRep.lean#L357).

> A matrix on the internal index commutes with the Lorentz action, since the two act on
> different tensor factors. This is how the gauge action of a field commutes with its Lorentz
> action.

```lean
lemma valEnd_comm_repLorentz (ρ : Representation ℂ SL(2,ℂ) S) (B : Matrix ι ι ℂ) (Λ : SL(2,ℂ))
    (v : V) : valEnd e B (repLorentz e ρ Λ v) = repLorentz e ρ Λ (valEnd e B v)
```

**`GlobalGaugeGroup.MatrixRep.valEndCLM`**, a def, [line 376](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/OfMatrixRep.lean#L376).

> A matrix on the internal index, as a continuous linear endomorphism of a normed target
> space `V ≃ S ⊗ (ι → ℂ)`.

```lean
noncomputable def valEndCLM : Matrix ι ι ℂ →ₐ[ℂ] (V →L[ℂ] V)
```

**`GlobalGaugeGroup.MatrixRep.continuous_valEndCLM`**, a lemma, [line 379](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/OfMatrixRep.lean#L379).

```lean
lemma continuous_valEndCLM : Continuous (valEndCLM e)
```

**`GlobalGaugeGroup.MatrixRep.valEndRep`**, a def, [line 384](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/OfMatrixRep.lean#L384).

> The continuous representation of the global gauge group on `V` by the matrices of a matrix
> representation on the internal index.

```lean
noncomputable def valEndRep (ρ : G.group →ₜ* (Matrix ι ι ℂ)ˣ) : G.group →ₜ* (V →L[ℂ] V)ˣ
```

## D. The matter field of a matrix representation

> A matrix representation `ρ` gives a matter field on any normed target space
> `V ≃ S ⊗ (ι → ℂ)`, with the gauge group acting by `ρ` on the internal index and the Lorentz
> group on `S`. Its action of the Lie algebra is the derivative of `ρ`.

**`GlobalGaugeGroup.MatterField.ofMatrixRep`**, a def, [line 412](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/OfMatrixRep.lean#L412).

> The matter field of a matrix representation `ρ`, on a target space `V ≃ S ⊗ (ι → ℂ)`.
> The global gauge group acts by `ρ` on the internal index and the Lorentz group through
> `repL` on `S`. The field has mass weight `w` and statistics `σ`.

```lean
noncomputable def ofMatrixRep (ρ : G.group →ₜ* (Matrix ι ι ℂ)ˣ)
    (repL : Representation ℂ SL(2,ℂ) S) (w : ℕ) (σ : FieldStatistic) : G.MatterField
```

**`GlobalGaugeGroup.MatterField.lieAlgebraRep_ofMatrixRep`**, a lemma, [line 426](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/OfMatrixRep.lean#L426).

> The Lie algebra representation of the matter field of a matrix representation is the
> derivative of the matrix representation, acting on the internal index.

```lean
lemma lieAlgebraRep_ofMatrixRep (c : G.lieSubalgebra) :
    lieAlgebraRep (ofMatrixRep e ρ repL w σ) c = valEndCLM e (derivMat ρ c)
```

**`GlobalGaugeGroup.MatterField.ofMatrixRep_repAlgebra`**, a lemma, [line 437](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/OfMatrixRep.lean#L437).

> The action of the Lie algebra on the matter field of a matrix representation is the
> derivative of the representation, acting on the internal index.

```lean
lemma ofMatrixRep_repAlgebra (c : G.lieSubalgebra) :
    (ofMatrixRep e ρ repL w σ).repAlgebra c = valEnd e (derivMat ρ c)
```

## Depends on

- [The jet action of a matter field](matterfield-gaugejetaction.md)

## Proof depends on

- [Exponentials of block-diagonal, Kronecker and scalar matrices](../../../mathematics/part-02/formathlib/analysis-normed-algebra-matrixexponential.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/OfMatrixRep.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/OfMatrixRep.lean)
