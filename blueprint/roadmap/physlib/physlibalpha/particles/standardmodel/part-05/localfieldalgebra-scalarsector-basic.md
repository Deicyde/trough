---
declaration: module
origin: cited
lean: StandardModel.ScalarSector.covH, StandardModel.ScalarSector.covBarH, StandardModel.ScalarSector.rep_mul, StandardModel.ScalarSector.repLorentz_mul, StandardModel.ScalarSector.H_equivariant, StandardModel.ScalarSector.barH_equivariant, StandardModel.ScalarSector.H_comm_H, StandardModel.ScalarSector.H_comm_barH
statement: formalized
proof: formalized
---

# The scalar sector of the covariant field algebra

The module `PhyslibAlpha.Particles.StandardModel.LocalFieldAlgebra.ScalarSector.Basic`, [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean): 67 declarations, 67 with a docstring.

> The Higgs towers, the algebra they generate, and its mass-weight submodules up to weight eight.

## i. Overview

> The scalar sector of the Standard Model's covariant field algebra `fieldData.LocalCovFieldAlgebra`
> is the part built from the covariant towers `∇_l H` and `∇_l H̄` of the Higgs field and its
> conjugate. The towers `covH` and `covBarH` are those of `fieldData.LocalCovFieldAlgebra`, and every
> law they satisfy (the gauge law, the Lorentz law, bosonic commutation and the mass weight) is a law
> of `fieldData.LocalCovFieldAlgebra`, restated here for the towers. From them the file builds the
> submodules `higgsSubmodule n` and `barHiggsSubmodule n` of terms linear in `∇_d H` and `∇_d H̄`, the
> algebra `higgsAlgebra` they generate, and its mass-weight submodules `massWeightSubmodule n`. Each
> of these carries a gauge weight decomposition. The mass-weight submodules are described by the
> results of `PhyslibAlpha.Mathematics.HomogeneousGenerators`, and removing the leftmost Higgs tower
> of each product gives them explicitly at weights `2`, `4`, `6` and `8`. These are the pieces from
> which the Higgs terms of the Standard Model Lagrangian are assembled downstream.

## ii. Key results

> - `covH`, `covBarH` : the Higgs and conjugate Higgs towers in the covariant field algebra.
> - `H_equivariant`, `H_comm_H`, `H_massWeight`, `repLorentz_H` and their conjugates : the
>   laws of the towers.
> - `higgsSubmoduleGaugeWeight`, `barHiggsSubmoduleGaugeWeight` : the gauge weight
>   decompositions of the Higgs submodules.
> - `rep_dotGaugeHiggs_invariant`, `repLorentz_dotGaugeHiggs` : the gauge invariance and the
>   Lorentz law of the inner product `H† H` with derivatives on the two factors.
> - `massWeightSubmodule_eq_iSup_mul`, `massWeightSubmodule_eq` : removing the leftmost Higgs
>   tower, and the binary weight recursion.
> - `massWeightSubmodule_two_eq` up to `massWeightSubmodule_eight_eq` : the mass weights up to eight.
> - `massWeightSubmoduleGaugeWeight` : the gauge weight decomposition of the mass-weight
>   submodules.

## iv. References

> * None.

## A. The Higgs towers and their laws

> The two towers the sector is written in are the covariant derivatives of the Higgs field and
> of its conjugate, as elements of the covariant field algebra of the Standard Model. Every law
> they satisfy is a law of that algebra, restated here for the towers.

**`StandardModel.ScalarSector.covH`**, a def, [line 93](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L93).

> The covariant derivatives `∇_l H` of the Higgs field inside the covariant field algebra
> of the Standard Model.

```lean
noncomputable def covH (n : ℕ) (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ HiggsVec →ₗ[ℂ] fieldData.LocalCovFieldAlgebra
```

**`StandardModel.ScalarSector.covBarH`**, a def, [line 99](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L99).

> The covariant derivatives `∇_l H̄` of the conjugate Higgs field inside the covariant field
> algebra of the Standard Model.

```lean
noncomputable def covBarH (n : ℕ) (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ (ConjModule HiggsVec) →ₗ[ℂ] fieldData.LocalCovFieldAlgebra
```

**`StandardModel.ScalarSector.rep_mul`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L104).

> Gauge transformations act on `fieldData.LocalCovFieldAlgebra` by algebra maps.

```lean
lemma rep_mul (g : GaugeGroupI) (b₁ b₂ : fieldData.LocalCovFieldAlgebra) :
    repGaugeGroupI g (b₁ * b₂) = repGaugeGroupI g b₁ * repGaugeGroupI g b₂
```

**`StandardModel.ScalarSector.repLorentz_mul`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L109).

> Lorentz transformations act on `fieldData.LocalCovFieldAlgebra` by algebra maps.

```lean
lemma repLorentz_mul (Λ : SL(2,ℂ)) (b₁ b₂ : fieldData.LocalCovFieldAlgebra) :
    repLorentzGroup Λ (b₁ * b₂) = repLorentzGroup Λ b₁ * repLorentzGroup Λ b₂
```

### A.1. The gauge laws

**`StandardModel.ScalarSector.H_equivariant`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L121).

> The Higgs symbol carries the dual of the gauge representation on `HiggsVec`. The
> `SU(2)` index transforms contragrediently, and the hypercharge character by `u⁻³`.

```lean
lemma H_equivariant (g : GaugeGroupI) (φ : Module.Dual ℂ HiggsVec) (n : ℕ)
    (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    repGaugeGroupI g (covH n l φ) = covH n l (HiggsVec.repGaugeGroupI.dual g φ)
```

**`StandardModel.ScalarSector.barH_equivariant`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L128).

> The conjugate Higgs symbol carries the conjugate-dual of the gauge representation,
> the physicists' `H^† ↦ H^† g^†`.

```lean
lemma barH_equivariant (g : GaugeGroupI) (φ : Module.Dual ℂ (ConjModule HiggsVec)) (n : ℕ)
    (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    repGaugeGroupI g (covBarH n l φ) = covBarH n l (HiggsVec.repGaugeGroupI.conj.dual g φ)
```

### A.2. The commutation laws and the mass weights

**`StandardModel.ScalarSector.H_comm_H`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L140).

> The Higgs is bosonic, so two Higgs symbols commute.

```lean
lemma H_comm_H (φ ψ : Module.Dual ℂ HiggsVec) (n1 n2 : ℕ)
    (l1 : Fin n1 → (Fin 1 ⊕ Fin 3)) (l2 : Fin n2 → (Fin 1 ⊕ Fin 3)) :
    Commute (covH n1 l1 φ) (covH n2 l2 ψ)
```

**`StandardModel.ScalarSector.H_comm_barH`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L146).

> A Higgs symbol commutes with a conjugate Higgs symbol.

```lean
lemma H_comm_barH (φ : Module.Dual ℂ HiggsVec) (ψ : Module.Dual ℂ (ConjModule HiggsVec))
    (n1 n2 : ℕ) (l1 : Fin n1 → (Fin 1 ⊕ Fin 3)) (l2 : Fin n2 → (Fin 1 ⊕ Fin 3)) :
    Commute (covH n1 l1 φ) (covBarH n2 l2 ψ)
```

**`StandardModel.ScalarSector.barH_comm_barH`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L152).

> Two conjugate Higgs symbols commute.

```lean
lemma barH_comm_barH (φ ψ : Module.Dual ℂ (ConjModule HiggsVec)) (n1 n2 : ℕ)
    (l1 : Fin n1 → (Fin 1 ⊕ Fin 3)) (l2 : Fin n2 → (Fin 1 ⊕ Fin 3)) :
    Commute (covBarH n1 l1 φ) (covBarH n2 l2 ψ)
```

**`StandardModel.ScalarSector.H_massWeight`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L158).

> The mass weight of the Higgs tower is `2 * (1 + n)`.

```lean
lemma H_massWeight (φ : Module.Dual ℂ HiggsVec) (n : ℕ) (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    massWeightPoly (covH n l φ) = Polynomial.monomial (2 * (1 + n)) (covH n l φ)
```

**`StandardModel.ScalarSector.barH_massWeight`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L163).

> The mass weight of the conjugate Higgs tower is `2 * (1 + n)`.

```lean
lemma barH_massWeight (φ : Module.Dual ℂ (ConjModule HiggsVec)) (n : ℕ)
    (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    massWeightPoly (covBarH n l φ)
      = Polynomial.monomial (2 * (1 + n)) (covBarH n l φ)
```

### A.3. The Lorentz laws

**`StandardModel.ScalarSector.repLorentz_H`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L178).

> The Higgs tower transforms under the Lorentz group as the covariant derivatives of a
> Lorentz scalar. Each derivative slot mixes by the Lorentz matrix, and the value index is
> inert.

```lean
lemma repLorentz_H : IsLorentzCovDerivTransforms repLorentzGroup
    (Representation.trivial ℂ SL(2,ℂ) HiggsVec) (fun {n} => covH n)
```

**`StandardModel.ScalarSector.repLorentz_barH`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L184).

> The conjugate Higgs tower transforms as the covariant derivatives of a Lorentz scalar,
> through the conjugate of the trivial representation.

```lean
lemma repLorentz_barH : IsLorentzCovDerivTransforms repLorentzGroup
    (Representation.trivial ℂ SL(2,ℂ) HiggsVec).conj (fun {n} => covBarH n)
```

**`StandardModel.ScalarSector.repLorentz_H_apply`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L190).

> The pointwise form of `repLorentz_H`. The Lorentz action rotates the derivative indices
> of a Higgs symbol, and the value index is inert.

```lean
lemma repLorentz_H_apply (g : SL(2,ℂ)) (φ : Module.Dual ℂ HiggsVec) (n : ℕ)
    (l : Fin n → Fin 1 ⊕ Fin 3) :
    repLorentzGroup g (covH n l φ) = ∑ (a : Fin n → Fin 1 ⊕ Fin 3),
      (∏ (i : Fin n), (((SL2C.toLorentzGroup g).1 (a i) (l i) : ℝ) : ℂ)) • covH n a φ
```

**`StandardModel.ScalarSector.repLorentz_barH_apply`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L197).

> The pointwise form of `repLorentz_barH`.

```lean
lemma repLorentz_barH_apply (g : SL(2,ℂ)) (φ : Module.Dual ℂ (ConjModule HiggsVec))
    (n : ℕ) (l : Fin n → Fin 1 ⊕ Fin 3) :
    repLorentzGroup g (covBarH n l φ) = ∑ (a : Fin n → Fin 1 ⊕ Fin 3),
      (∏ (i : Fin n), (((SL2C.toLorentzGroup g).1 (a i) (l i) : ℝ) : ℂ)) • covBarH n a φ
```

## B. The Higgs algebra

> The subalgebra of `fieldData.LocalCovFieldAlgebra` generated by every `∇_d H` and `∇_d H̄`. Its
> elements commute with one another, so any two of its submodules commute as submodules; and a
> property closed under sums and products which holds on the symbols and on the scalars holds on all
> of it.

**`StandardModel.ScalarSector.higgsAlgebra`**, a def, [line 216](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L216).

> The subalgebra of `fieldData.LocalCovFieldAlgebra` generated by the Higgs, its conjugate and all
> their derivatives.

```lean
noncomputable def higgsAlgebra :
    Subalgebra ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.ScalarSector.covH_mem_higgsAlgebra`**, a lemma, [line 222](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L222).

> A Higgs symbol lies in the Higgs algebra.

```lean
lemma covH_mem_higgsAlgebra {n : ℕ} (d : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ HiggsVec) : covH n d φ ∈ higgsAlgebra
```

**`StandardModel.ScalarSector.covBarH_mem_higgsAlgebra`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L227).

> A conjugate Higgs symbol lies in the Higgs algebra.

```lean
lemma covBarH_mem_higgsAlgebra {n : ℕ} (d : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule HiggsVec)) : covBarH n d φ ∈ higgsAlgebra
```

**`StandardModel.ScalarSector.higgsAlgebra_induction`**, a lemma, [line 234](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L234).

> Induction on the Higgs algebra. A property of elements of `fieldData.LocalCovFieldAlgebra` which
> holds on every Higgs and conjugate Higgs symbol and on every scalar, and is closed under sums and
> products of elements of the algebra, holds on the whole algebra.

```lean
lemma higgsAlgebra_induction {P : fieldData.LocalCovFieldAlgebra → Prop}
    (hH : ∀ (n : ℕ) (d : Fin n → (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ HiggsVec),
      P (covH n d φ))
    (hbarH : ∀ (n : ℕ) (d : Fin n → (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (ConjModule HiggsVec)),
      P (covBarH n d φ))
    (halg : ∀ r : ℂ, P (algebraMap ℂ fieldData.LocalCovFieldAlgebra r))
    (hadd : ∀ x y, x ∈ higgsAlgebra → y ∈ higgsAlgebra → P x → P y → P (x + y))
    (hmul : ∀ x y, x ∈ higgsAlgebra → y ∈ higgsAlgebra → P x → P y → P (x * y))
    {x : fieldData.LocalCovFieldAlgebra} (hx : x ∈ higgsAlgebra) : P x
```

**`StandardModel.ScalarSector.commute_of_mem_higgsAlgebra`**, a lemma, [line 254](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L254).

> Any two elements of the Higgs algebra commute.

```lean
lemma commute_of_mem_higgsAlgebra {x y : fieldData.LocalCovFieldAlgebra} (hx : x ∈ higgsAlgebra)
    (hy : y ∈ higgsAlgebra) : Commute x y
```

**`StandardModel.ScalarSector.mul_comm_of_le_higgsAlgebra`**, a lemma, [line 273](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L273).

> Two submodules of the Higgs algebra commute.

```lean
lemma mul_comm_of_le_higgsAlgebra {M N : Submodule ℂ fieldData.LocalCovFieldAlgebra}
    (hM : M ≤ Subalgebra.toSubmodule higgsAlgebra)
    (hN : N ≤ Subalgebra.toSubmodule higgsAlgebra) : M * N = N * M
```

## C. The components and the Higgs submodules

> The components `∇_d H^i` and `∇_d H̄^i` are the symbols evaluated on the dual of the standard
> basis of `HiggsVec`. The Higgs submodule with `n` derivatives is the span of the symbols
> `∇_d H` over all multi-indices `d` of length `n`, equally the span of the components.

**`StandardModel.ScalarSector.higgs`**, a def, [line 294](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L294).

> The component `∇_d H^i` in the algebra.

```lean
noncomputable def higgs
    {n : ℕ} (d : Fin n → (Fin 1 ⊕ Fin 3)) (i : Fin 2) : fieldData.LocalCovFieldAlgebra
```

**`StandardModel.ScalarSector.barHiggs`**, a def, [line 299](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L299).

> The component `∇_d H̄^i` in the algebra.

```lean
noncomputable def barHiggs
    {n : ℕ} (d : Fin n → (Fin 1 ⊕ Fin 3)) (i : Fin 2) : fieldData.LocalCovFieldAlgebra
```

### C.1. The gauge action on the components

**`StandardModel.ScalarSector.rep_higgsComponent`**, a lemma, [line 311](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L311).

> The gauge group mixes the components of `∇_d H` by the matrix `u⁻³ g⁻¹` of the
> hypercharge and `SU(2)` parts of `g⁻¹`.

```lean
lemma rep_higgsComponent (g : GaugeGroupI) {n : ℕ} (d : Fin n → (Fin 1 ⊕ Fin 3)) (i : Fin 2) :
    repGaugeGroupI g (higgs d i) =
      ∑ j, (((g⁻¹).toU1 : ℂ) ^ 3 * (g⁻¹).toSU2.1 i j) • higgs d j
```

**`StandardModel.ScalarSector.rep_barHiggsComponent`**, a lemma, [line 327](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L327).

> The gauge group mixes the components of `∇_d H̄` by the conjugate matrix.

```lean
lemma rep_barHiggsComponent (g : GaugeGroupI) {n : ℕ} (d : Fin n → (Fin 1 ⊕ Fin 3))
    (i : Fin 2) :
    repGaugeGroupI g (barHiggs d i) =
      ∑ j, (starRingEnd ℂ (((g⁻¹).toU1 : ℂ) ^ 3 * (g⁻¹).toSU2.1 i j)) • barHiggs d j
```

### C.2. The Higgs and conjugate Higgs submodules

**`StandardModel.ScalarSector.higgsSubmodule`**, a def, [line 353](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L353).

> The submodule of `fieldData.LocalCovFieldAlgebra` generated by the Higgs symbols carrying `n`
> derivatives, the join, over the Lorentz indices `d`, of the ranges of the symbol maps `H n d`. Its
> elements are the terms linear in `∇_d H` — of mass dimension `1 + n`.

```lean
noncomputable def higgsSubmodule (n : ℕ) :
    Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.ScalarSector.barHiggsSubmodule`**, a def, [line 360](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L360).

> The submodule of `fieldData.LocalCovFieldAlgebra` generated by the conjugate Higgs symbols
> carrying `n` derivatives, the join, over the Lorentz indices `d`, of the ranges of the symbol maps
> `barH n d`.

```lean
noncomputable def barHiggsSubmodule (n : ℕ) :
    Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.ScalarSector.higgsSubmodule_eq_iSup_span`**, a lemma, [line 365](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L365).

> The Higgs submodule is spanned by the components `∇_d H^j`.

```lean
lemma higgsSubmodule_eq_iSup_span (n : ℕ) :
    higgsSubmodule n = ⨆ (d : Fin n → (Fin 1 ⊕ Fin 3)) (j : Fin 2), ℂ ∙ higgs d j
```

**`StandardModel.ScalarSector.barHiggsSubmodule_eq_iSup_span`**, a lemma, [line 374](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L374).

> The conjugate Higgs submodule is spanned by the components `∇_d H̄^j`.

```lean
lemma barHiggsSubmodule_eq_iSup_span (n : ℕ) :
    barHiggsSubmodule n
      = ⨆ (d : Fin n → (Fin 1 ⊕ Fin 3)) (j : Fin 2), ℂ ∙ barHiggs d j
```

**`StandardModel.ScalarSector.higgsSubmodule_le_higgsAlgebra`**, a lemma, [line 384](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L384).

> The Higgs submodule lies in the Higgs algebra.

```lean
lemma higgsSubmodule_le_higgsAlgebra (n : ℕ) :
    higgsSubmodule n ≤ Subalgebra.toSubmodule higgsAlgebra
```

**`StandardModel.ScalarSector.barHiggsSubmodule_le_higgsAlgebra`**, a lemma, [line 392](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L392).

> The conjugate Higgs submodule lies in the Higgs algebra.

```lean
lemma barHiggsSubmodule_le_higgsAlgebra (n : ℕ) :
    barHiggsSubmodule n ≤ Subalgebra.toSubmodule higgsAlgebra
```

**`StandardModel.ScalarSector.barHiggsSubmodule_comm_higgsSubmodule`**, a lemma, [line 401](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L401).

> The conjugate Higgs and Higgs submodules commute.

```lean
lemma barHiggsSubmodule_comm_higgsSubmodule (n1 n2 : ℕ) :
    (barHiggsSubmodule n1) * (higgsSubmodule n2)
    =  (higgsSubmodule n2)  * (barHiggsSubmodule n1)
```

**`StandardModel.ScalarSector.higgsSubmodule_comm_higgsSubmodule`**, a lemma, [line 408](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L408).

> Two Higgs submodules commute.

```lean
lemma higgsSubmodule_comm_higgsSubmodule (n1 n2 : ℕ) :
    (higgsSubmodule n1) * (higgsSubmodule n2)
    =  (higgsSubmodule n2)  * (higgsSubmodule n1)
```

**`StandardModel.ScalarSector.barHiggsSubmodule_comm_barHiggsSubmodule`**, a lemma, [line 415](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L415).

> Two conjugate Higgs submodules commute.

```lean
lemma barHiggsSubmodule_comm_barHiggsSubmodule (n1 n2 : ℕ) :
    (barHiggsSubmodule n1) * (barHiggsSubmodule n2)
    =  (barHiggsSubmodule n2)  * (barHiggsSubmodule n1)
```

**`StandardModel.ScalarSector.barHiggs_higgs_left_comm`**, a lemma, [line 423](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L423).

> A conjugate Higgs submodule commutes past a Higgs submodule standing in front of a third
> factor.

```lean
lemma barHiggs_higgs_left_comm (n1 n2 : ℕ) (C : Submodule ℂ fieldData.LocalCovFieldAlgebra) :
    barHiggsSubmodule n1 * (higgsSubmodule n2 * C)
      = higgsSubmodule n2 * (barHiggsSubmodule n1 * C)
```

## D. The gauge weight decomposition of the Higgs submodules

> The four torus generators `gaugeTorusGen i` act on each component by a character: `∇_d H^j`
> has isospin weight `-isoWeight j` and hypercharge weight `-3`, and `∇_d H̄^j` the opposite.
> The general construction `doubletGaugeWeight` turns a family of such two-component
> eigenvectors into a gauge weight decomposition of its span, and the two Higgs submodules
> are instances of it.

**`StandardModel.ScalarSector.rep_gaugeTorusGen_higgs`**, a lemma, [line 442](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L442).

> The torus generators act on `∇_d H^j` by the character of weight
> `(0, 0, -isoWeight j, -3)`.

```lean
lemma rep_gaugeTorusGen_higgs (i : Fin 4) {n : ℕ} (d : Fin n → (Fin 1 ⊕ Fin 3)) (j : Fin 2) :
    repGaugeGroupI (gaugeTorusGen i) (higgs d j)
      = ((expI : ℂ) ^ GaugeWeight.coord (0, 0, -isoWeight j, -3) i) • higgs d j
```

**`StandardModel.ScalarSector.rep_gaugeTorusGen_barHiggs`**, a lemma, [line 456](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L456).

> The torus generators act on `∇_d H̄^j` by the character of weight
> `(0, 0, isoWeight j, 3)`.

```lean
lemma rep_gaugeTorusGen_barHiggs (i : Fin 4) {n : ℕ} (d : Fin n → (Fin 1 ⊕ Fin 3))
    (j : Fin 2) :
    repGaugeGroupI (gaugeTorusGen i) (barHiggs d j)
      = ((expI : ℂ) ^ GaugeWeight.coord (0, 0, isoWeight j, 3) i) • barHiggs d j
```

**`StandardModel.ScalarSector.iSup_span_le_eigenspace`**, a lemma, [line 467](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L467).

> The span of a family of eigenvectors of a torus generator lies in its eigenspace.

```lean
lemma iSup_span_le_eigenspace {ι : Type} (i : Fin 4) (y : ι → fieldData.LocalCovFieldAlgebra)
    (w : GaugeWeight)
    (hy : ∀ d, repGaugeGroupI (gaugeTorusGen i) (y d) = ((expI : ℂ) ^ w.coord i) • y d) :
    (⨆ d, ℂ ∙ y d)
      ≤ Module.End.eigenspace (repGaugeGroupI (gaugeTorusGen i)) ((expI : ℂ) ^ w.coord i)
```

**`StandardModel.ScalarSector.doubletGaugeWeight`**, a def, [line 480](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L480).

> The gauge weight decomposition of the span of a two-component family `x d j` of torus
> eigenvectors, the components `x d 0` of weight `w₀` and `x d 1` of weight `w₁ ≠ w₀`. The
> weight-`w₀` piece is the span of the `x d 0` and the weight-`w₁` piece that of the
> `x d 1`.

```lean
noncomputable def doubletGaugeWeight {ι : Type} (x : ι → Fin 2 → fieldData.LocalCovFieldAlgebra)
    (w₀ w₁ : GaugeWeight) (hw : w₀ ≠ w₁)
    (hx₀ : ∀ (i : Fin 4) (d : ι),
      repGaugeGroupI (gaugeTorusGen i) (x d 0) = ((expI : ℂ) ^ w₀.coord i) • x d 0)
    (hx₁ : ∀ (i : Fin 4) (d : ι),
      repGaugeGroupI (gaugeTorusGen i) (x d 1) = ((expI : ℂ) ^ w₁.coord i) • x d 1) :
    GaugeWeightDecomposition repGaugeGroupI (⨆ (d : ι) (j : Fin 2), ℂ ∙ x d j)
```

**`StandardModel.ScalarSector.higgsSubmoduleGaugeWeight`**, an instance, [line 517](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L517).

> The gauge weight decomposition of the Higgs submodule. `∇_d H⁰` spans the piece of
> weight `(0, 0, -1, -3)` and `∇_d H¹` that of weight `(0, 0, 1, -3)`.

```lean
noncomputable instance higgsSubmoduleGaugeWeight (n : ℕ) :
    GaugeWeightDecomposition repGaugeGroupI (higgsSubmodule n)
```

**`StandardModel.ScalarSector.barHiggsSubmoduleGaugeWeight`**, an instance, [line 525](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L525).

> The gauge weight decomposition of the conjugate Higgs submodule. `∇_d H̄⁰` spans the
> piece of weight `(0, 0, 1, 3)` and `∇_d H̄¹` that of weight `(0, 0, -1, 3)`.

```lean
noncomputable instance barHiggsSubmoduleGaugeWeight (n : ℕ) :
    GaugeWeightDecomposition repGaugeGroupI (barHiggsSubmodule n)
```

## E. The Higgs inner product

> The pairing `∇_{d1} H⁰ ∇_{d2} H̄⁰ + ∇_{d1} H¹ ∇_{d2} H̄¹` is invariant under the gauge group,
> since `H̄` transforms by the conjugate of the unitary matrix acting on `H`, and its two
> derivative multi-indices rotate independently under the Lorentz group.

**`StandardModel.ScalarSector.dotGaugeHiggs`**, a def, [line 543](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L543).

> The gauge-invariant pairing `∇_{d1} H^j ∇_{d2} H̄^j`, summed over the isospin index.

```lean
noncomputable def dotGaugeHiggs
    {n1 n2 : ℕ} (d1 : Fin n1 → (Fin 1 ⊕ Fin 3)) (d2 : Fin n2 → (Fin 1 ⊕ Fin 3)) :
    fieldData.LocalCovFieldAlgebra
```

**`StandardModel.ScalarSector.rep_dotGaugeHiggs_invariant`**, a lemma, [line 549](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L549).

> The pairing is gauge invariant, since the matrix acting on `H` is unitary, and `H̄` transforms
> by its conjugate.

```lean
lemma rep_dotGaugeHiggs_invariant {n1 n2 : ℕ} (g : GaugeGroupI) (d1 : Fin n1 → (Fin 1 ⊕ Fin 3))
    (d2 : Fin n2 → (Fin 1 ⊕ Fin 3)) :
    repGaugeGroupI g (dotGaugeHiggs d1 d2) = dotGaugeHiggs d1 d2
```

**`StandardModel.ScalarSector.repLorentz_higgs`**, a lemma, [line 589](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L589).

> The Lorentz action rotates the derivative indices of a Higgs component.

```lean
lemma repLorentz_higgs {n : ℕ} (g : SL(2,ℂ)) (d : Fin n → Fin 1 ⊕ Fin 3) (k : Fin 2) :
    repLorentzGroup g (higgs d k) = ∑ a : Fin n → Fin 1 ⊕ Fin 3,
      (∏ j, (((SL2C.toLorentzGroup g).1 (a j) (d j) : ℝ) : ℂ)) • higgs a k
```

**`StandardModel.ScalarSector.repLorentz_barHiggs`**, a lemma, [line 596](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L596).

> The Lorentz action rotates the derivative indices of a conjugate Higgs component.

```lean
lemma repLorentz_barHiggs {n : ℕ} (g : SL(2,ℂ)) (d : Fin n → Fin 1 ⊕ Fin 3) (k : Fin 2) :
    repLorentzGroup g (barHiggs d k) = ∑ a : Fin n → Fin 1 ⊕ Fin 3,
      (∏ j, (((SL2C.toLorentzGroup g).1 (a j) (d j) : ℝ) : ℂ)) • barHiggs a k
```

**`StandardModel.ScalarSector.repLorentz_dotGaugeHiggs`**, a lemma, [line 604](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L604).

> The Lorentz action on the Higgs inner product. The two factors' derivative indices
> rotate independently, and the inner product itself is a Lorentz scalar.

```lean
lemma repLorentz_dotGaugeHiggs {m n : ℕ} (g : SL(2,ℂ))
    (d₁ : Fin m → Fin 1 ⊕ Fin 3) (d₂ : Fin n → Fin 1 ⊕ Fin 3) :
    repLorentzGroup g (dotGaugeHiggs d₁ d₂) =
      ∑ a₁ : Fin m → Fin 1 ⊕ Fin 3, ∑ a₂ : Fin n → Fin 1 ⊕ Fin 3,
        ((∏ j, (((SL2C.toLorentzGroup g).1 (a₁ j) (d₁ j) : ℝ) : ℂ)) *
          (∏ j, (((SL2C.toLorentzGroup g).1 (a₂ j) (d₂ j) : ℝ) : ℂ))) •
          dotGaugeHiggs a₁ a₂
```

## F. The mass weight submodules

> A Higgs tower `∇ⁿH` or `∇ⁿH̄` has mass weight `2 * (1 + n)`, twice its mass dimension
> `1 + n`; a term of mass dimension four, as in the Lagrangian, has weight eight.

**`StandardModel.ScalarSector.massWeightSubmodule`**, a def, [line 626](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L626).

> All terms built from the Higgs symbols and their derivatives which have mass weight
> exactly `n`, the intersection of the algebra generated by every `∇_d H` and `∇_d H̄` with
> the part on which `massWeightPoly` is the monomial `X ^ n`.

```lean
noncomputable def massWeightSubmodule (n : ℕ) :
    Submodule ℂ fieldData.LocalCovFieldAlgebra
```

### F.1. Membership and the grading

**`StandardModel.ScalarSector.mem_massWeightSubmodule_iff`**, a lemma, [line 642](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L642).

> An element has mass weight `n` when it lies in the Higgs algebra and `massWeightPoly`
> scales it by `X ^ n`.

```lean
lemma mem_massWeightSubmodule_iff {n : ℕ} {x : fieldData.LocalCovFieldAlgebra} :
    x ∈ massWeightSubmodule n
      ↔ x ∈ higgsAlgebra ∧ massWeightPoly x = Polynomial.monomial n x
```

**`StandardModel.ScalarSector.massWeightPoly_of_mem_massWeightSubmodule`**, a lemma, [line 648](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L648).

> The mass weight of an element of the weight-`n` submodule.

```lean
lemma massWeightPoly_of_mem_massWeightSubmodule {n : ℕ} {x : fieldData.LocalCovFieldAlgebra}
    (hx : x ∈ massWeightSubmodule n) : massWeightPoly x = Polynomial.monomial n x
```

**`StandardModel.ScalarSector.mem_higgsAlgebra_of_mem_massWeightSubmodule`**, a lemma, [line 653](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L653).

> The weight-`n` submodule lies in the Higgs algebra.

```lean
lemma mem_higgsAlgebra_of_mem_massWeightSubmodule {n : ℕ} {x : fieldData.LocalCovFieldAlgebra}
    (hx : x ∈ massWeightSubmodule n) : x ∈ higgsAlgebra
```

**`StandardModel.ScalarSector.one_le_massWeightSubmodule_zero`**, a lemma, [line 658](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L658).

> The scalars have mass weight zero.

```lean
lemma one_le_massWeightSubmodule_zero : (1 : Submodule ℂ fieldData.LocalCovFieldAlgebra) ≤
    massWeightSubmodule 0
```

**`StandardModel.ScalarSector.massWeightSubmodule_mul_le`**, a lemma, [line 663](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L663).

> Mass weights add under multiplication.

```lean
lemma massWeightSubmodule_mul_le (m n : ℕ) :
    massWeightSubmodule m * massWeightSubmodule n ≤ massWeightSubmodule (m + n)
```

**`StandardModel.ScalarSector.massWeightSubmodule_higgsSubmodule_le`**, a lemma, [line 668](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L668).

> The Higgs symbols with `n` derivatives have mass weight `2 * (1 + n)`.

```lean
lemma massWeightSubmodule_higgsSubmodule_le (n : ℕ) :
    higgsSubmodule n ≤ massWeightSubmodule (2 * (1 + n))
```

**`StandardModel.ScalarSector.massWeightSubmodule_barHiggsSubmodule_le`**, a lemma, [line 676](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L676).

> The conjugate Higgs symbols with `n` derivatives have mass weight `2 * (1 + n)`.

```lean
lemma massWeightSubmodule_barHiggsSubmodule_le (n : ℕ) :
    barHiggsSubmodule n ≤ massWeightSubmodule (2 * (1 + n))
```

### F.2. The weight decompositions

> The Higgs algebra is generated by the towers `∇ⁿH ⊔ ∇ⁿH̄`, on which `massWeightPoly` is the
> monomial `X ^ (2 * (1 + n))`. The results of `PhyslibAlpha.Mathematics.HomogeneousGenerators`
> then describe every mass weight submodule, as a join of products of towers in the order
> written.

**`StandardModel.ScalarSector.higgsAlgebra_eq_adjoin`**, a lemma, [line 697](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L697).

> The Higgs algebra is generated by the Higgs and conjugate Higgs towers of every
> derivative order.

```lean
lemma higgsAlgebra_eq_adjoin :
    higgsAlgebra = Algebra.adjoin ℂ
      (⋃ n, ((higgsSubmodule n ⊔ barHiggsSubmodule n : Submodule ℂ fieldData.LocalCovFieldAlgebra) :
        Set fieldData.LocalCovFieldAlgebra))
```

**`StandardModel.ScalarSector.massWeightPoly_of_mem_higgsSubmodule_sup`**, a lemma, [line 713](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L713).

> `massWeightPoly` is the monomial `X ^ (2 * (1 + n))` on the Higgs and conjugate Higgs
> towers with `n` derivatives.

```lean
lemma massWeightPoly_of_mem_higgsSubmodule_sup (n : ℕ) :
    ∀ x ∈ higgsSubmodule n ⊔ barHiggsSubmodule n,
      massWeightPoly x = Polynomial.monomial (2 * (1 + n)) x
```

**`StandardModel.ScalarSector.massWeightSubmodule_zero_eq`**, a lemma, [line 721](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L721).

> Weight zero is the scalars, as every Higgs tower has positive weight.

```lean
lemma massWeightSubmodule_zero_eq : massWeightSubmodule 0 = 1
```

**`StandardModel.ScalarSector.massWeightSubmodule_eq`**, a lemma, [line 727](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L727).

> The weight recursion. A term of positive mass weight `i` is a sum of symbols of weight
> `i` and of products of two terms of lower positive weight adding up to `i`.

```lean
lemma massWeightSubmodule_eq (i : ℕ) (hi : 0 < i) :
    massWeightSubmodule i
      = (⨆ k ∈ Finset.univ.filter (fun k : Fin i => 2 * (1 + (k : ℕ)) = i),
          higgsSubmodule (k : ℕ) ⊔ barHiggsSubmodule (k : ℕ))
        ⊔ (⨆ p ∈ Finset.univ.filter (fun p : Fin i × Fin i => (p.1 : ℕ) + (p.2 : ℕ) = i),
            massWeightSubmodule (p.1 : ℕ) * massWeightSubmodule (p.2 : ℕ))
```

**`StandardModel.ScalarSector.massWeightSubmodule_eq_iSup_mul`**, a lemma, [line 740](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L740).

> Removing the leftmost Higgs tower. A term of positive weight `w` is a sum of products
> of a tower `∇ⁿH` or `∇ⁿH̄`, of weight `2 * (1 + n) ≤ w`, with a term of the remaining
> weight.

```lean
lemma massWeightSubmodule_eq_iSup_mul (w : ℕ) (hw : 0 < w) :
    massWeightSubmodule w
      = ⨆ n ∈ (Finset.range (w + 1)).filter (fun n => 2 * (1 + n) ≤ w),
          (higgsSubmodule n ⊔ barHiggsSubmodule n) * massWeightSubmodule (w - 2 * (1 + n))
```

### F.3. The odd mass weights vanish

**`StandardModel.ScalarSector.massWeightSubmodule_odd_eq_bot`**, a lemma, [line 756](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L756).

> The odd mass weight submodules are trivial, since every Higgs tower has even weight, and
> weights add under products.

```lean
lemma massWeightSubmodule_odd_eq_bot (n : ℕ) (hn : Odd n) :
    massWeightSubmodule n = ⊥
```

### F.4. The gauge weight decomposition

**`StandardModel.ScalarSector.massWeightSubmoduleGaugeWeight`**, a def, [line 774](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L774).

> The gauge weight decomposition of the mass weight submodules. By recursion on the
> weight through `massWeightSubmodule_eq`. A term of weight `i` is either a symbol of that
> weight — decomposed by `higgsSubmoduleGaugeWeight` and `barHiggsSubmoduleGaugeWeight` — or
> a product of two terms of lower positive weight, decomposed by `mul` from the
> decompositions supplied by the recursion.

```lean
noncomputable def massWeightSubmoduleGaugeWeight :
    (i : ℕ) → 0 < i → GaugeWeightDecomposition repGaugeGroupI (massWeightSubmodule i)
```

**`StandardModel.ScalarSector.massWeightSubmoduleGaugeWeightOfNeZero`**, an instance, [line 796](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L796).

> The `NeZero` form of `massWeightSubmoduleGaugeWeight`.

```lean
noncomputable instance massWeightSubmoduleGaugeWeightOfNeZero (i : ℕ) [NeZero i] :
    GaugeWeightDecomposition repGaugeGroupI (massWeightSubmodule i)
```

### F.5. Mass weights up to eight

> Each case removes the leftmost tower. The towers with `0`, `1`, `2` and `3` derivatives
> have weights `2`, `4`, `6` and `8`, and the remaining weight is read off from a smaller weight.
> Expanding the joins gives the products of `H` and `H̄`; the Higgs algebra is commutative,
> so orders differing only by the position of commuting factors are merged, and the products
> are written in a fixed order.

**`StandardModel.ScalarSector.massWeightSubmodule_two_eq`**, a lemma, [line 813](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L813).

> Weight two is the underived Higgs and conjugate Higgs.

```lean
lemma massWeightSubmodule_two_eq :
    massWeightSubmodule 2 = higgsSubmodule 0 ⊔ barHiggsSubmodule 0
```

**`StandardModel.ScalarSector.massWeightSubmodule_four_eq`**, a lemma, [line 822](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L822).

> Weight four is spanned by the once-derived symbols and the products of two underived ones. The
> leftmost tower is underived, leaving weight two, or once-derived, leaving weight zero.

```lean
lemma massWeightSubmodule_four_eq :
    massWeightSubmodule 4 = higgsSubmodule 1 ⊔ barHiggsSubmodule 1 ⊔
    higgsSubmodule 0 * higgsSubmodule 0 ⊔ higgsSubmodule 0 *
    barHiggsSubmodule 0 ⊔ barHiggsSubmodule 0 * barHiggsSubmodule 0
```

**`StandardModel.ScalarSector.massWeightSubmodule_six_eq`**, a lemma, [line 841](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L841).

> Weight six is spanned by the twice-derived symbols, a once-derived symbol against an underived
> one, and the products of three underived ones. The leftmost tower leaves weight four, two or
> zero.

```lean
lemma massWeightSubmodule_six_eq : massWeightSubmodule 6 =
    -- The derivative terms
    higgsSubmodule 2 ⊔ barHiggsSubmodule 2 ⊔
    higgsSubmodule 1 * higgsSubmodule 0 ⊔
    higgsSubmodule 1 * barHiggsSubmodule 0 ⊔
    barHiggsSubmodule 1 * higgsSubmodule 0 ⊔
    barHiggsSubmodule 1 * barHiggsSubmodule 0 ⊔
    -- The potential terms
    higgsSubmodule 0 * higgsSubmodule 0 * higgsSubmodule 0  ⊔
    higgsSubmodule 0 * higgsSubmodule 0 * barHiggsSubmodule 0 ⊔
    higgsSubmodule 0 * barHiggsSubmodule 0 * barHiggsSubmodule 0 ⊔
    barHiggsSubmodule 0 * barHiggsSubmodule 0 * barHiggsSubmodule 0
```

**`StandardModel.ScalarSector.massWeightSubmodule_eight_eq`**, a lemma, [line 879](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L879).

> Weight eight is spanned by the derivative terms with up to three derivatives, and the products
> of four underived symbols. The leftmost tower leaves weight six, four, two or zero.

```lean
lemma massWeightSubmodule_eight_eq :
    massWeightSubmodule 8 =
      -- The derivative terms
    higgsSubmodule 3 ⊔ barHiggsSubmodule 3 ⊔
    higgsSubmodule 2 * higgsSubmodule 0 ⊔
    higgsSubmodule 2 * barHiggsSubmodule 0 ⊔
    higgsSubmodule 0 * barHiggsSubmodule 2 ⊔
    barHiggsSubmodule 2 * barHiggsSubmodule 0 ⊔
    higgsSubmodule 1 * higgsSubmodule 1 ⊔
    higgsSubmodule 1 * barHiggsSubmodule 1 ⊔
    barHiggsSubmodule 1 * barHiggsSubmodule 1 ⊔
    higgsSubmodule 1 * higgsSubmodule 0 * higgsSubmodule 0 ⊔
    higgsSubmodule 1 * higgsSubmodule 0 * barHiggsSubmodule 0 ⊔
    higgsSubmodule 1 * barHiggsSubmodule 0 * barHiggsSubmodule 0 ⊔
    higgsSubmodule 0 * higgsSubmodule 0 * barHiggsSubmodule 1 ⊔
    higgsSubmodule 0 * barHiggsSubmodule 1 * barHiggsSubmodule 0 ⊔
    barHiggsSubmodule 1 * barHiggsSubmodule 0 * barHiggsSubmodule 0 ⊔
    -- The potential terms
    higgsSubmodule 0 * higgsSubmodule 0 * higgsSubmodule 0 * higgsSubmodule 0 ⊔
    higgsSubmodule 0 * higgsSubmodule 0 * higgsSubmodule 0 * barHiggsSubmodule 0 ⊔
    higgsSubmodule 0 * higgsSubmodule 0 * barHiggsSubmodule 0 * barHiggsSubmodule 0 ⊔
    higgsSubmodule 0 * barHiggsSubmodule 0 * barHiggsSubmodule 0 * barHiggsSubmodule 0 ⊔
    barHiggsSubmodule 0 * barHiggsSubmodule 0 * barHiggsSubmodule 0 *
      barHiggsSubmodule 0
```

## G. Gauge invariants

**`StandardModel.ScalarSector.gaugeInvariantOfMassDim`**, a def, [line 950](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean#L950).

> The gauge invariants of a given mass weight.

```lean
noncomputable def gaugeInvariantOfMassDim (M : ℕ) : Submodule ℂ fieldData.LocalCovFieldAlgebra
```

## Depends on

- [The covariant field algebra of the Standard Model](localfieldalgebra-localcovfieldalgebra-basic.md)

## Proof depends on

- [Subalgebras generated by homogeneous submodules](../../../mathematics/part-01/homogeneousgenerators.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/Basic.lean)
