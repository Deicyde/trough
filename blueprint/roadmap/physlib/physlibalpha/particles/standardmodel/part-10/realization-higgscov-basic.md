---
declaration: module
origin: cited
lean: StandardModel.HiggsAlgebraCovRealization, StandardModel.HiggsAlgebraCovRealization.covH, StandardModel.HiggsAlgebraCovRealization.covBarH, StandardModel.HiggsAlgebraCovRealization.map_rep_eq, StandardModel.HiggsAlgebraCovRealization.H_equivariant, StandardModel.HiggsAlgebraCovRealization.barH_equivariant, StandardModel.HiggsAlgebraCovRealization.H_comm_H, StandardModel.HiggsAlgebraCovRealization.H_comm_barH
statement: formalized
proof: formalized
---

# The algebra valued Higgs boson

The module `PhyslibAlpha.Particles.StandardModel.Realization.HiggsCov.Basic`, [PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean): 70 declarations, 70 with a docstring.

## i. Overview

> An algebra `B` carries a Higgs sector when the covariant towers `∇_l H` and `∇_l H̄`, and
> every polynomial expression in them, sit inside it compatibly with the global gauge action,
> the Lorentz action and the mass-weight grading. `CovHiggsJetAlgebra` is the universal object
> with those towers, so the statement is a single one: an algebra map
> `CovHiggsJetAlgebra →ₐ[ℂ] B`, equivariant for the global gauge group and the Lorentz group
> and compatible with `massWeightPoly`. That is the structure `HiggsAlgebraCovRealization`,
> together with the two demands that the group actions be multiplicative on the whole of `B`.
>
> The towers `covH` and `covBarH` are the towers of the covariant jet algebra of the Higgs
> field pushed along the map, and every law they satisfy is that algebra's law pushed along
> it. From them the file builds the submodules `higgsSubmodule n` and `barHiggsSubmodule n`
> of terms linear in `∇_d H` and `∇_d H̄`, the algebra `higgsAlgebra` they generate, and its
> mass-weight submodules `massWeightSubmodule n`. Each of these carries a gauge weight
> decomposition. The mass-weight submodules are described by the results of
> `PhyslibAlpha.Mathematics.HomogeneousGenerators`, and removing the leftmost Higgs tower of each
> product gives them explicitly at weights `2`, `4`, `6` and `8`. These are the pieces from
> which the Higgs terms of the Standard Model Lagrangian are assembled downstream.

## ii. Key results

> - `HiggsAlgebraCovRealization` : the structure.
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

**`StandardModel.HiggsAlgebraCovRealization`**, a structure, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L99).

> The algebra `B`, with a gauge action, a Lorentz action and a mass-weight grading,
> carries a Higgs sector when it receives an algebra map from the covariant jet algebra of
> the Higgs field which is equivariant for both actions and compatible with the grading.
> The covariant towers `∇_l H` and `∇_l H̄` then sit inside `B` as the images of that
> algebra's own, and every law they satisfy there is its law pushed along the map.
>
> It is the Higgs-sector counterpart of `CovAlgebraRealization`, and stands to
> `CovHiggsJetAlgebra` as that does to `CovJetAlgebra`.
>
> The last two fields are not consequences of the first three: an equivariant map forces
> the two actions to be multiplicative only on its image, whereas the sector needs them
> multiplicative on the whole of `B`.

```lean
structure HiggsAlgebraCovRealization (B : Type) [Ring B] [Algebra ℂ B]
    (rep : Representation ℂ GaugeGroupI B)
    (repLorentz : Representation ℂ SL(2,ℂ) B)
    (massWeightPoly : B →ₐ[ℂ] Polynomial B) where
  /-- The algebra map out of the covariant jet algebra of the Higgs field: it is what
    places the Higgs towers, and every polynomial expression in them, inside `B`. -/
  toAlgHom : CovHiggsJetAlgebra →ₐ[ℂ] B
  /-- The map is equivariant for the global gauge group. -/
  map_rep : ∀ (g : GaugeGroupI) (x : CovHiggsJetAlgebra),
    toAlgHom (CovHiggsJetAlgebra.repGaugeGroupI g x) = rep g (toAlgHom x)
  /-- The map is equivariant for the Lorentz group. -/
  map_repLorentz : ∀ (Λ : SL(2,ℂ)) (x : CovHiggsJetAlgebra),
    toAlgHom (CovHiggsJetAlgebra.repLorentzGroup Λ x) = repLorentz Λ (toAlgHom x)
  /-- The map carries the mass-weight grading of the covariant jet algebra of the Higgs
    field to that of `B`. -/
  map_massWeight : ∀ x : CovHiggsJetAlgebra, massWeightPoly (toAlgHom x)
    = Polynomial.mapAlgHom toAlgHom (CovHiggsJetAlgebra.massWeightPoly x)
  /-- Gauge transformations act on `B` by algebra maps. -/
  rep_mul : ∀ (g : GaugeGroupI) (b₁ b₂ : B), rep g (b₁ * b₂) = rep g b₁ * rep g b₂
  /-- Lorentz transformations act on `B` by algebra maps. -/
  repLorentz_mul : ∀ (Λ : SL(2,ℂ)) (b₁ b₂ : B),
    repLorentz Λ (b₁ * b₂) = repLorentz Λ b₁ * repLorentz Λ b₂
```

## A. The Higgs towers and their laws

> The two towers the sector is written in are not data of the structure. They are the towers
> of the covariant jet algebra of the Higgs field, carried into `B` along the defining
> algebra map, and every law they satisfy is that algebra's law pushed along it.

**`StandardModel.HiggsAlgebraCovRealization.covH`**, a def, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L146).

> The covariant derivatives `∇_l H` of the Higgs field inside `B`.

```lean
noncomputable def covH (n : ℕ) (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ HiggsVec →ₗ[ℂ] B
```

**`StandardModel.HiggsAlgebraCovRealization.covBarH`**, a def, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L151).

> The covariant derivatives `∇_l H̄` of the conjugate Higgs field inside `B`.

```lean
noncomputable def covBarH (n : ℕ) (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ (ConjModule HiggsVec) →ₗ[ℂ] B
```

### A.1. The gauge laws

**`StandardModel.HiggsAlgebraCovRealization.map_rep_eq`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L163).

> A gauge law of the covariant jet algebra of the Higgs field transports along the
> defining map.

```lean
lemma map_rep_eq {g : GaugeGroupI} {x y : CovHiggsJetAlgebra}
    (hxy : CovHiggsJetAlgebra.repGaugeGroupI g x = y) :
    rep g (h.toAlgHom x) = h.toAlgHom y
```

**`StandardModel.HiggsAlgebraCovRealization.H_equivariant`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L170).

> The Higgs symbol carries the dual of the gauge representation on `HiggsVec`: the
> `SU(2)` index transforms contragrediently, and the hypercharge character by `u⁻³`.

```lean
lemma H_equivariant (g : GaugeGroupI) (φ : Module.Dual ℂ HiggsVec) (n : ℕ)
    (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    rep g (h.covH n l φ) = h.covH n l (HiggsVec.repGaugeGroupI.dual g φ)
```

**`StandardModel.HiggsAlgebraCovRealization.barH_equivariant`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L177).

> The conjugate Higgs symbol carries the conjugate-dual of the gauge representation:
> the physicists' `H^† ↦ H^† g^†`.

```lean
lemma barH_equivariant (g : GaugeGroupI) (φ : Module.Dual ℂ (ConjModule HiggsVec)) (n : ℕ)
    (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    rep g (h.covBarH n l φ) = h.covBarH n l (HiggsVec.repGaugeGroupI.conj.dual g φ)
```

### A.2. The commutation laws and the mass weights

**`StandardModel.HiggsAlgebraCovRealization.H_comm_H`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L189).

> The Higgs is bosonic: two Higgs symbols commute.

```lean
lemma H_comm_H (φ ψ : Module.Dual ℂ HiggsVec) (n1 n2 : ℕ)
    (l1 : Fin n1 → (Fin 1 ⊕ Fin 3)) (l2 : Fin n2 → (Fin 1 ⊕ Fin 3)) :
    Commute (h.covH n1 l1 φ) (h.covH n2 l2 ψ)
```

**`StandardModel.HiggsAlgebraCovRealization.H_comm_barH`**, a lemma, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L195).

> A Higgs symbol commutes with a conjugate Higgs symbol.

```lean
lemma H_comm_barH (φ : Module.Dual ℂ HiggsVec) (ψ : Module.Dual ℂ (ConjModule HiggsVec))
    (n1 n2 : ℕ) (l1 : Fin n1 → (Fin 1 ⊕ Fin 3)) (l2 : Fin n2 → (Fin 1 ⊕ Fin 3)) :
    Commute (h.covH n1 l1 φ) (h.covBarH n2 l2 ψ)
```

**`StandardModel.HiggsAlgebraCovRealization.barH_comm_barH`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L201).

> Two conjugate Higgs symbols commute.

```lean
lemma barH_comm_barH (φ ψ : Module.Dual ℂ (ConjModule HiggsVec)) (n1 n2 : ℕ)
    (l1 : Fin n1 → (Fin 1 ⊕ Fin 3)) (l2 : Fin n2 → (Fin 1 ⊕ Fin 3)) :
    Commute (h.covBarH n1 l1 φ) (h.covBarH n2 l2 ψ)
```

**`StandardModel.HiggsAlgebraCovRealization.map_massWeight_monomial`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L207).

> A mass-weight eigenvalue equation transports along the defining map.

```lean
lemma map_massWeight_monomial {n : ℕ} {x : CovHiggsJetAlgebra}
    (hx : CovHiggsJetAlgebra.massWeightPoly x = Polynomial.monomial n x) :
    massWeightPoly (h.toAlgHom x) = Polynomial.monomial n (h.toAlgHom x)
```

**`StandardModel.HiggsAlgebraCovRealization.H_massWeight`**, a lemma, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L215).

> The mass weight of the Higgs tower is `2 * (1 + n)`.

```lean
lemma H_massWeight (φ : Module.Dual ℂ HiggsVec) (n : ℕ) (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    massWeightPoly (h.covH n l φ) = Polynomial.monomial (2 * (1 + n)) (h.covH n l φ)
```

**`StandardModel.HiggsAlgebraCovRealization.barH_massWeight`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L220).

> The mass weight of the conjugate Higgs tower is `2 * (1 + n)`.

```lean
lemma barH_massWeight (φ : Module.Dual ℂ (ConjModule HiggsVec)) (n : ℕ)
    (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    massWeightPoly (h.covBarH n l φ)
      = Polynomial.monomial (2 * (1 + n)) (h.covBarH n l φ)
```

### A.3. The Lorentz laws

**`StandardModel.HiggsAlgebraCovRealization.map_lorentz`**, a lemma, [line 234](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L234).

> A Lorentz law of the covariant jet algebra of the Higgs field transports along the
> defining map.

```lean
lemma map_lorentz {V : Type} [AddCommGroup V] [Module ℂ V]
    {repV : Representation ℂ SL(2,ℂ) V}
    {G : {n : ℕ} → (Fin n → (Fin 1 ⊕ Fin 3)) → Module.Dual ℂ V →ₗ[ℂ] CovHiggsJetAlgebra}
    (hG : IsLorentzCovDerivTransforms CovHiggsJetAlgebra.repLorentzGroup repV G) :
    IsLorentzCovDerivTransforms repLorentz repV
      (fun {_n} l => h.toAlgHom.toLinearMap ∘ₗ G l)
```

**`StandardModel.HiggsAlgebraCovRealization.repLorentz_H`**, a lemma, [line 250](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L250).

> The Higgs tower transforms under the Lorentz group as the covariant derivatives of a
> Lorentz scalar: each derivative slot mixes by the Lorentz matrix, and the value index is
> inert.

```lean
lemma repLorentz_H : IsLorentzCovDerivTransforms repLorentz
    (Representation.trivial ℂ SL(2,ℂ) HiggsVec) (fun {n} => h.covH n)
```

**`StandardModel.HiggsAlgebraCovRealization.repLorentz_barH`**, a lemma, [line 256](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L256).

> The conjugate Higgs tower transforms as the covariant derivatives of a Lorentz scalar,
> through the conjugate of the trivial representation.

```lean
lemma repLorentz_barH : IsLorentzCovDerivTransforms repLorentz
    (Representation.trivial ℂ SL(2,ℂ) HiggsVec).conj (fun {n} => h.covBarH n)
```

**`StandardModel.HiggsAlgebraCovRealization.repLorentz_H_apply`**, a lemma, [line 263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L263).

> The pointwise form of `repLorentz_H`: the Lorentz action rotates the derivative indices
> of a Higgs symbol, and the value index is inert.

```lean
lemma repLorentz_H_apply (g : SL(2,ℂ)) (φ : Module.Dual ℂ HiggsVec) (n : ℕ)
    (l : Fin n → Fin 1 ⊕ Fin 3) :
    repLorentz g (h.covH n l φ) = ∑ (a : Fin n → Fin 1 ⊕ Fin 3),
      (∏ (i : Fin n), (((SL2C.toLorentzGroup g).1 (a i) (l i) : ℝ) : ℂ)) • h.covH n a φ
```

**`StandardModel.HiggsAlgebraCovRealization.repLorentz_barH_apply`**, a lemma, [line 271](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L271).

> The pointwise form of `repLorentz_barH`.

```lean
lemma repLorentz_barH_apply (g : SL(2,ℂ)) (φ : Module.Dual ℂ (ConjModule HiggsVec))
    (n : ℕ) (l : Fin n → Fin 1 ⊕ Fin 3) :
    repLorentz g (h.covBarH n l φ) = ∑ (a : Fin n → Fin 1 ⊕ Fin 3),
      (∏ (i : Fin n), (((SL2C.toLorentzGroup g).1 (a i) (l i) : ℝ) : ℂ)) • h.covBarH n a φ
```

## B. The Higgs algebra

> The subalgebra of `B` generated by every `∇_d H` and `∇_d H̄`. Its elements commute with
> one another, so any two of its submodules commute as submodules; and a property closed under
> sums and products which holds on the symbols and on the scalars holds on all of it.

**`StandardModel.HiggsAlgebraCovRealization.higgsAlgebra`**, a def, [line 289](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L289).

> The subalgebra of `B` generated by the Higgs, its conjugate and all their
> derivatives.

```lean
def higgsAlgebra (h : HiggsAlgebraCovRealization B rep repLorentz massWeightPoly) :
    Subalgebra ℂ B
```

**`StandardModel.HiggsAlgebraCovRealization.covH_mem_higgsAlgebra`**, a lemma, [line 294](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L294).

> A Higgs symbol lies in the Higgs algebra.

```lean
lemma covH_mem_higgsAlgebra {n : ℕ} (d : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ HiggsVec) : h.covH n d φ ∈ h.higgsAlgebra
```

**`StandardModel.HiggsAlgebraCovRealization.covBarH_mem_higgsAlgebra`**, a lemma, [line 299](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L299).

> A conjugate Higgs symbol lies in the Higgs algebra.

```lean
lemma covBarH_mem_higgsAlgebra {n : ℕ} (d : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule HiggsVec)) : h.covBarH n d φ ∈ h.higgsAlgebra
```

**`StandardModel.HiggsAlgebraCovRealization.higgsAlgebra_induction`**, a lemma, [line 306](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L306).

> Induction on the Higgs algebra: a property of elements of `B` which holds on every
> Higgs and conjugate Higgs symbol and on every scalar, and is closed under sums and
> products of elements of the algebra, holds on the whole algebra.

```lean
lemma higgsAlgebra_induction {P : B → Prop}
    (hH : ∀ (n : ℕ) (d : Fin n → (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ HiggsVec),
      P (h.covH n d φ))
    (hbarH : ∀ (n : ℕ) (d : Fin n → (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (ConjModule HiggsVec)),
      P (h.covBarH n d φ))
    (halg : ∀ r : ℂ, P (algebraMap ℂ B r))
    (hadd : ∀ x y, x ∈ h.higgsAlgebra → y ∈ h.higgsAlgebra → P x → P y → P (x + y))
    (hmul : ∀ x y, x ∈ h.higgsAlgebra → y ∈ h.higgsAlgebra → P x → P y → P (x * y))
    {x : B} (hx : x ∈ h.higgsAlgebra) : P x
```

**`StandardModel.HiggsAlgebraCovRealization.commute_of_mem_higgsAlgebra`**, a lemma, [line 326](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L326).

> Any two elements of the Higgs algebra commute.

```lean
lemma commute_of_mem_higgsAlgebra {x y : B} (hx : x ∈ h.higgsAlgebra)
    (hy : y ∈ h.higgsAlgebra) : Commute x y
```

**`StandardModel.HiggsAlgebraCovRealization.mul_comm_of_le_higgsAlgebra`**, a lemma, [line 345](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L345).

> Two submodules of the Higgs algebra commute.

```lean
lemma mul_comm_of_le_higgsAlgebra {M N : Submodule ℂ B}
    (hM : M ≤ Subalgebra.toSubmodule h.higgsAlgebra)
    (hN : N ≤ Subalgebra.toSubmodule h.higgsAlgebra) : M * N = N * M
```

## C. The components and the Higgs submodules

> The components `∇_d H^i` and `∇_d H̄^i` are the symbols evaluated on the dual of the standard
> basis of `HiggsVec`. The Higgs submodule with `n` derivatives is the span of the symbols
> `∇_d H` over all multi-indices `d` of length `n`, equally the span of the components.

**`StandardModel.HiggsAlgebraCovRealization.higgs`**, a def, [line 366](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L366).

> The component `∇_d H^i` in the algebra.

```lean
noncomputable def higgs (h : HiggsAlgebraCovRealization B rep repLorentz massWeightPoly)
    {n : ℕ} (d : Fin n → (Fin 1 ⊕ Fin 3)) (i : Fin 2) : B
```

**`StandardModel.HiggsAlgebraCovRealization.barHiggs`**, a def, [line 371](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L371).

> The component `∇_d H̄^i` in the algebra.

```lean
noncomputable def barHiggs (h : HiggsAlgebraCovRealization B rep repLorentz massWeightPoly)
    {n : ℕ} (d : Fin n → (Fin 1 ⊕ Fin 3)) (i : Fin 2) : B
```

### C.1. The gauge action on the components

**`StandardModel.HiggsAlgebraCovRealization.rep_higgsComponent`**, a lemma, [line 383](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L383).

> The gauge group mixes the components of `∇_d H` by the matrix `u⁻³ g⁻¹` of the
> hypercharge and `SU(2)` parts of `g⁻¹`.

```lean
lemma rep_higgsComponent (g : GaugeGroupI) {n : ℕ} (d : Fin n → (Fin 1 ⊕ Fin 3)) (i : Fin 2) :
    rep g (h.higgs d i) =
      ∑ j, (((g⁻¹).toU1 : ℂ) ^ 3 * (g⁻¹).toSU2.1 i j) • h.higgs d j
```

**`StandardModel.HiggsAlgebraCovRealization.rep_barHiggsComponent`**, a lemma, [line 399](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L399).

> The gauge group mixes the components of `∇_d H̄` by the conjugate matrix.

```lean
lemma rep_barHiggsComponent (g : GaugeGroupI) {n : ℕ} (d : Fin n → (Fin 1 ⊕ Fin 3))
    (i : Fin 2) :
    rep g (h.barHiggs d i) =
      ∑ j, (starRingEnd ℂ (((g⁻¹).toU1 : ℂ) ^ 3 * (g⁻¹).toSU2.1 i j)) • h.barHiggs d j
```

### C.2. The Higgs and conjugate Higgs submodules

**`StandardModel.HiggsAlgebraCovRealization.higgsSubmodule`**, a def, [line 425](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L425).

> The submodule of `B` generated by the Higgs symbols carrying `n` derivatives: the join,
> over the Lorentz indices `d`, of the ranges of the symbol maps `H n d`. Its elements are
> the terms linear in `∇_d H` — of mass dimension `1 + n`.

```lean
noncomputable def higgsSubmodule
    (h : HiggsAlgebraCovRealization B rep repLorentz massWeightPoly) (n : ℕ) :
    Submodule ℂ B
```

**`StandardModel.HiggsAlgebraCovRealization.barHiggsSubmodule`**, a def, [line 431](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L431).

> The submodule of `B` generated by the conjugate Higgs symbols carrying `n` derivatives:
> the join, over the Lorentz indices `d`, of the ranges of the symbol maps `barH n d`.

```lean
noncomputable def barHiggsSubmodule
    (h : HiggsAlgebraCovRealization B rep repLorentz massWeightPoly) (n : ℕ) :
    Submodule ℂ B
```

**`StandardModel.HiggsAlgebraCovRealization.higgsSubmodule_eq_iSup_span`**, a lemma, [line 436](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L436).

> The Higgs submodule is spanned by the components `∇_d H^j`.

```lean
lemma higgsSubmodule_eq_iSup_span (n : ℕ) :
    h.higgsSubmodule n = ⨆ (d : Fin n → (Fin 1 ⊕ Fin 3)) (j : Fin 2), ℂ ∙ h.higgs d j
```

**`StandardModel.HiggsAlgebraCovRealization.barHiggsSubmodule_eq_iSup_span`**, a lemma, [line 445](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L445).

> The conjugate Higgs submodule is spanned by the components `∇_d H̄^j`.

```lean
lemma barHiggsSubmodule_eq_iSup_span (n : ℕ) :
    h.barHiggsSubmodule n
      = ⨆ (d : Fin n → (Fin 1 ⊕ Fin 3)) (j : Fin 2), ℂ ∙ h.barHiggs d j
```

**`StandardModel.HiggsAlgebraCovRealization.higgsSubmodule_le_higgsAlgebra`**, a lemma, [line 455](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L455).

> The Higgs submodule lies in the Higgs algebra.

```lean
lemma higgsSubmodule_le_higgsAlgebra (n : ℕ) :
    h.higgsSubmodule n ≤ Subalgebra.toSubmodule h.higgsAlgebra
```

**`StandardModel.HiggsAlgebraCovRealization.barHiggsSubmodule_le_higgsAlgebra`**, a lemma, [line 463](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L463).

> The conjugate Higgs submodule lies in the Higgs algebra.

```lean
lemma barHiggsSubmodule_le_higgsAlgebra (n : ℕ) :
    h.barHiggsSubmodule n ≤ Subalgebra.toSubmodule h.higgsAlgebra
```

**`StandardModel.HiggsAlgebraCovRealization.barHiggsSubmodule_comm_higgsSubmodule`**, a lemma, [line 472](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L472).

> The conjugate Higgs and Higgs submodules commute.

```lean
lemma barHiggsSubmodule_comm_higgsSubmodule (n1 n2 : ℕ) :
    (h.barHiggsSubmodule n1) * (h.higgsSubmodule n2)
    =  (h.higgsSubmodule n2)  * (h.barHiggsSubmodule n1)
```

**`StandardModel.HiggsAlgebraCovRealization.higgsSubmodule_comm_higgsSubmodule`**, a lemma, [line 479](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L479).

> Two Higgs submodules commute.

```lean
lemma higgsSubmodule_comm_higgsSubmodule (n1 n2 : ℕ) :
    (h.higgsSubmodule n1) * (h.higgsSubmodule n2)
    =  (h.higgsSubmodule n2)  * (h.higgsSubmodule n1)
```

**`StandardModel.HiggsAlgebraCovRealization.barHiggsSubmodule_comm_barHiggsSubmodule`**, a lemma, [line 486](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L486).

> Two conjugate Higgs submodules commute.

```lean
lemma barHiggsSubmodule_comm_barHiggsSubmodule (n1 n2 : ℕ) :
    (h.barHiggsSubmodule n1) * (h.barHiggsSubmodule n2)
    =  (h.barHiggsSubmodule n2)  * (h.barHiggsSubmodule n1)
```

**`StandardModel.HiggsAlgebraCovRealization.barHiggs_higgs_left_comm`**, a lemma, [line 494](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L494).

> A conjugate Higgs submodule commutes past a Higgs submodule standing in front of a third
> factor.

```lean
lemma barHiggs_higgs_left_comm (n1 n2 : ℕ) (C : Submodule ℂ B) :
    h.barHiggsSubmodule n1 * (h.higgsSubmodule n2 * C)
      = h.higgsSubmodule n2 * (h.barHiggsSubmodule n1 * C)
```

## D. The gauge weight decomposition of the Higgs submodules

> The four torus generators `gaugeTorusGen i` act on each component by a character: `∇_d H^j`
> has isospin weight `-isoWeight j` and hypercharge weight `-3`, and `∇_d H̄^j` the opposite.
> The general construction `doubletGaugeWeight` turns a family of such two-component
> eigenvectors into a gauge weight decomposition of its span, and the two Higgs submodules
> are instances of it.

**`StandardModel.HiggsAlgebraCovRealization.rep_gaugeTorusGen_higgs`**, a lemma, [line 513](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L513).

> The torus generators act on `∇_d H^j` by the character of weight
> `(0, 0, -isoWeight j, -3)`.

```lean
lemma rep_gaugeTorusGen_higgs (i : Fin 4) {n : ℕ} (d : Fin n → (Fin 1 ⊕ Fin 3)) (j : Fin 2) :
    rep (gaugeTorusGen i) (h.higgs d j)
      = ((expI : ℂ) ^ GaugeWeight.coord (0, 0, -isoWeight j, -3) i) • h.higgs d j
```

**`StandardModel.HiggsAlgebraCovRealization.rep_gaugeTorusGen_barHiggs`**, a lemma, [line 527](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L527).

> The torus generators act on `∇_d H̄^j` by the character of weight
> `(0, 0, isoWeight j, 3)`.

```lean
lemma rep_gaugeTorusGen_barHiggs (i : Fin 4) {n : ℕ} (d : Fin n → (Fin 1 ⊕ Fin 3))
    (j : Fin 2) :
    rep (gaugeTorusGen i) (h.barHiggs d j)
      = ((expI : ℂ) ^ GaugeWeight.coord (0, 0, isoWeight j, 3) i) • h.barHiggs d j
```

**`StandardModel.HiggsAlgebraCovRealization.iSup_span_le_eigenspace`**, a lemma, [line 538](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L538).

> The span of a family of eigenvectors of a torus generator lies in its eigenspace.

```lean
lemma iSup_span_le_eigenspace {ι : Type} (i : Fin 4) (y : ι → B) (w : GaugeWeight)
    (hy : ∀ d, rep (gaugeTorusGen i) (y d) = ((expI : ℂ) ^ w.coord i) • y d) :
    (⨆ d, ℂ ∙ y d) ≤ Module.End.eigenspace (rep (gaugeTorusGen i)) ((expI : ℂ) ^ w.coord i)
```

**`StandardModel.HiggsAlgebraCovRealization.doubletGaugeWeight`**, a def, [line 549](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L549).

> The gauge weight decomposition of the span of a two-component family `x d j` of torus
> eigenvectors, the components `x d 0` of weight `w₀` and `x d 1` of weight `w₁ ≠ w₀`: the
> weight-`w₀` piece is the span of the `x d 0` and the weight-`w₁` piece that of the
> `x d 1`.

```lean
noncomputable def doubletGaugeWeight {ι : Type} (hmul : IsMulRep rep) (x : ι → Fin 2 → B)
    (w₀ w₁ : GaugeWeight) (hw : w₀ ≠ w₁)
    (hx₀ : ∀ (i : Fin 4) (d : ι),
      rep (gaugeTorusGen i) (x d 0) = ((expI : ℂ) ^ w₀.coord i) • x d 0)
    (hx₁ : ∀ (i : Fin 4) (d : ι),
      rep (gaugeTorusGen i) (x d 1) = ((expI : ℂ) ^ w₁.coord i) • x d 1) :
    GaugeWeightDecomposition rep (⨆ (d : ι) (j : Fin 2), ℂ ∙ x d j)
```

**`StandardModel.HiggsAlgebraCovRealization.higgsSubmoduleGaugeWeight`**, an instance, [line 586](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L586).

> The gauge weight decomposition of the Higgs submodule: `∇_d H⁰` spans the piece of
> weight `(0, 0, -1, -3)` and `∇_d H¹` that of weight `(0, 0, 1, -3)`.

```lean
noncomputable instance higgsSubmoduleGaugeWeight (n : ℕ) :
    GaugeWeightDecomposition rep (h.higgsSubmodule n)
```

**`StandardModel.HiggsAlgebraCovRealization.barHiggsSubmoduleGaugeWeight`**, an instance, [line 594](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L594).

> The gauge weight decomposition of the conjugate Higgs submodule: `∇_d H̄⁰` spans the
> piece of weight `(0, 0, 1, 3)` and `∇_d H̄¹` that of weight `(0, 0, -1, 3)`.

```lean
noncomputable instance barHiggsSubmoduleGaugeWeight (n : ℕ) :
    GaugeWeightDecomposition rep (h.barHiggsSubmodule n)
```

## E. The Higgs inner product

> The pairing `∇_{d1} H⁰ ∇_{d2} H̄⁰ + ∇_{d1} H¹ ∇_{d2} H̄¹` is invariant under the gauge group,
> since `H̄` transforms by the conjugate of the unitary matrix acting on `H`, and its two
> derivative multi-indices rotate independently under the Lorentz group.

**`StandardModel.HiggsAlgebraCovRealization.dotGaugeHiggs`**, a def, [line 612](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L612).

> The gauge-invariant pairing `∇_{d1} H^j ∇_{d2} H̄^j`, summed over the isospin index.

```lean
noncomputable def dotGaugeHiggs (h : HiggsAlgebraCovRealization B rep repLorentz massWeightPoly)
    {n1 n2 : ℕ} (d1 : Fin n1 → (Fin 1 ⊕ Fin 3)) (d2 : Fin n2 → (Fin 1 ⊕ Fin 3)) :
    B
```

**`StandardModel.HiggsAlgebraCovRealization.rep_dotGaugeHiggs_invariant`**, a lemma, [line 618](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L618).

> The pairing is gauge invariant: the matrix acting on `H` is unitary, and `H̄` transforms
> by its conjugate.

```lean
lemma rep_dotGaugeHiggs_invariant {n1 n2 : ℕ} (g : GaugeGroupI) (d1 : Fin n1 → (Fin 1 ⊕ Fin 3))
    (d2 : Fin n2 → (Fin 1 ⊕ Fin 3)) :
    rep g (h.dotGaugeHiggs d1 d2) = h.dotGaugeHiggs d1 d2
```

**`StandardModel.HiggsAlgebraCovRealization.repLorentz_higgs`**, a lemma, [line 657](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L657).

> The Lorentz action rotates the derivative indices of a Higgs component.

```lean
lemma repLorentz_higgs {n : ℕ} (g : SL(2,ℂ)) (d : Fin n → Fin 1 ⊕ Fin 3) (k : Fin 2) :
    repLorentz g (h.higgs d k) = ∑ a : Fin n → Fin 1 ⊕ Fin 3,
      (∏ j, (((SL2C.toLorentzGroup g).1 (a j) (d j) : ℝ) : ℂ)) • h.higgs a k
```

**`StandardModel.HiggsAlgebraCovRealization.repLorentz_barHiggs`**, a lemma, [line 664](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L664).

> The Lorentz action rotates the derivative indices of a conjugate Higgs component.

```lean
lemma repLorentz_barHiggs {n : ℕ} (g : SL(2,ℂ)) (d : Fin n → Fin 1 ⊕ Fin 3) (k : Fin 2) :
    repLorentz g (h.barHiggs d k) = ∑ a : Fin n → Fin 1 ⊕ Fin 3,
      (∏ j, (((SL2C.toLorentzGroup g).1 (a j) (d j) : ℝ) : ℂ)) • h.barHiggs a k
```

**`StandardModel.HiggsAlgebraCovRealization.repLorentz_dotGaugeHiggs`**, a lemma, [line 672](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L672).

> The Lorentz action on the Higgs inner product: the two factors' derivative indices
> rotate independently, and the inner product itself is a Lorentz scalar.

```lean
lemma repLorentz_dotGaugeHiggs {m n : ℕ} (g : SL(2,ℂ))
    (d₁ : Fin m → Fin 1 ⊕ Fin 3) (d₂ : Fin n → Fin 1 ⊕ Fin 3) :
    repLorentz g (h.dotGaugeHiggs d₁ d₂) =
      ∑ a₁ : Fin m → Fin 1 ⊕ Fin 3, ∑ a₂ : Fin n → Fin 1 ⊕ Fin 3,
        ((∏ j, (((SL2C.toLorentzGroup g).1 (a₁ j) (d₁ j) : ℝ) : ℂ)) *
          (∏ j, (((SL2C.toLorentzGroup g).1 (a₂ j) (d₂ j) : ℝ) : ℂ))) •
          h.dotGaugeHiggs a₁ a₂
```

## F. The mass weight submodules

> A Higgs tower `∇ⁿH` or `∇ⁿH̄` has mass weight `2 * (1 + n)`, twice its mass dimension
> `1 + n`; a term of mass dimension four, as in the Lagrangian, has weight eight.

**`StandardModel.HiggsAlgebraCovRealization.massWeightSubmodule`**, a def, [line 694](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L694).

> All terms built from the Higgs symbols and their derivatives which have mass weight
> exactly `n`: the intersection of the algebra generated by every `∇_d H` and `∇_d H̄` with
> the part on which `massWeightPoly` is the monomial `X ^ n`.

```lean
noncomputable def massWeightSubmodule
    (h : HiggsAlgebraCovRealization B rep repLorentz massWeightPoly) (n : ℕ) :
    Submodule ℂ B
```

### F.1. Membership and the grading

**`StandardModel.HiggsAlgebraCovRealization.mem_massWeightSubmodule_iff`**, a lemma, [line 709](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L709).

> An element has mass weight `n` when it lies in the Higgs algebra and `massWeightPoly`
> scales it by `X ^ n`.

```lean
lemma mem_massWeightSubmodule_iff {n : ℕ} {x : B} :
    x ∈ h.massWeightSubmodule n
      ↔ x ∈ h.higgsAlgebra ∧ massWeightPoly x = Polynomial.monomial n x
```

**`StandardModel.HiggsAlgebraCovRealization.massWeightPoly_of_mem_massWeightSubmodule`**, a lemma, [line 715](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L715).

> The mass weight of an element of the weight-`n` submodule.

```lean
lemma massWeightPoly_of_mem_massWeightSubmodule {n : ℕ} {x : B}
    (hx : x ∈ h.massWeightSubmodule n) : massWeightPoly x = Polynomial.monomial n x
```

**`StandardModel.HiggsAlgebraCovRealization.mem_higgsAlgebra_of_mem_massWeightSubmodule`**, a lemma, [line 720](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L720).

> The weight-`n` submodule lies in the Higgs algebra.

```lean
lemma mem_higgsAlgebra_of_mem_massWeightSubmodule {n : ℕ} {x : B}
    (hx : x ∈ h.massWeightSubmodule n) : x ∈ h.higgsAlgebra
```

**`StandardModel.HiggsAlgebraCovRealization.massWeightSubmodule_mul_comm`**, a lemma, [line 725](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L725).

> Two mass weight submodules commute.

```lean
lemma massWeightSubmodule_mul_comm (n m : ℕ) :
    h.massWeightSubmodule n * h.massWeightSubmodule m
    = h.massWeightSubmodule m * h.massWeightSubmodule n
```

**`StandardModel.HiggsAlgebraCovRealization.one_le_massWeightSubmodule_zero`**, a lemma, [line 731](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L731).

> The scalars have mass weight zero.

```lean
lemma one_le_massWeightSubmodule_zero : (1 : Submodule ℂ B) ≤ h.massWeightSubmodule 0
```

**`StandardModel.HiggsAlgebraCovRealization.massWeightSubmodule_mul_le`**, a lemma, [line 735](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L735).

> Mass weights add under multiplication.

```lean
lemma massWeightSubmodule_mul_le (m n : ℕ) :
    h.massWeightSubmodule m * h.massWeightSubmodule n ≤ h.massWeightSubmodule (m + n)
```

**`StandardModel.HiggsAlgebraCovRealization.massWeightSubmodule_higgsSubmodule_le`**, a lemma, [line 740](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L740).

> The Higgs symbols with `n` derivatives have mass weight `2 * (1 + n)`.

```lean
lemma massWeightSubmodule_higgsSubmodule_le (n : ℕ) :
    h.higgsSubmodule n ≤ h.massWeightSubmodule (2 * (1 + n))
```

**`StandardModel.HiggsAlgebraCovRealization.massWeightSubmodule_barHiggsSubmodule_le`**, a lemma, [line 748](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L748).

> The conjugate Higgs symbols with `n` derivatives have mass weight `2 * (1 + n)`.

```lean
lemma massWeightSubmodule_barHiggsSubmodule_le (n : ℕ) :
    h.barHiggsSubmodule n ≤ h.massWeightSubmodule (2 * (1 + n))
```

### F.2. The weight decompositions

> The Higgs algebra is generated by the towers `∇ⁿH ⊔ ∇ⁿH̄`, on which `massWeightPoly` is the
> monomial `X ^ (2 * (1 + n))`. The results of `PhyslibAlpha.Mathematics.HomogeneousGenerators`
> then describe every mass weight submodule, as a join of products of towers in the order
> written.

**`StandardModel.HiggsAlgebraCovRealization.higgsAlgebra_eq_adjoin`**, a lemma, [line 769](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L769).

> The Higgs algebra is generated by the Higgs and conjugate Higgs towers of every
> derivative order.

```lean
lemma higgsAlgebra_eq_adjoin :
    h.higgsAlgebra = Algebra.adjoin ℂ
      (⋃ n, ((h.higgsSubmodule n ⊔ h.barHiggsSubmodule n : Submodule ℂ B) : Set B))
```

**`StandardModel.HiggsAlgebraCovRealization.massWeightPoly_of_mem_higgsSubmodule_sup`**, a lemma, [line 784](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L784).

> `massWeightPoly` is the monomial `X ^ (2 * (1 + n))` on the Higgs and conjugate Higgs
> towers with `n` derivatives.

```lean
lemma massWeightPoly_of_mem_higgsSubmodule_sup (n : ℕ) :
    ∀ x ∈ h.higgsSubmodule n ⊔ h.barHiggsSubmodule n,
      massWeightPoly x = Polynomial.monomial (2 * (1 + n)) x
```

**`StandardModel.HiggsAlgebraCovRealization.massWeightSubmodule_zero_eq`**, a lemma, [line 792](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L792).

> Weight zero is the scalars: every Higgs tower has positive weight.

```lean
lemma massWeightSubmodule_zero_eq : h.massWeightSubmodule 0 = 1
```

**`StandardModel.HiggsAlgebraCovRealization.massWeightSubmodule_eq`**, a lemma, [line 798](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L798).

> The weight recursion: a term of positive mass weight `i` is a sum of symbols of weight
> `i` and of products of two terms of lower positive weight adding up to `i`.

```lean
lemma massWeightSubmodule_eq (i : ℕ) (hi : 0 < i) :
    h.massWeightSubmodule i
      = (⨆ k ∈ Finset.univ.filter (fun k : Fin i => 2 * (1 + (k : ℕ)) = i),
          h.higgsSubmodule (k : ℕ) ⊔ h.barHiggsSubmodule (k : ℕ))
        ⊔ (⨆ p ∈ Finset.univ.filter (fun p : Fin i × Fin i => (p.1 : ℕ) + (p.2 : ℕ) = i),
            h.massWeightSubmodule (p.1 : ℕ) * h.massWeightSubmodule (p.2 : ℕ))
```

**`StandardModel.HiggsAlgebraCovRealization.massWeightSubmodule_eq_iSup_mul`**, a lemma, [line 811](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L811).

> Removing the leftmost Higgs tower: a term of positive weight `w` is a sum of products
> of a tower `∇ⁿH` or `∇ⁿH̄`, of weight `2 * (1 + n) ≤ w`, with a term of the remaining
> weight.

```lean
lemma massWeightSubmodule_eq_iSup_mul (w : ℕ) (hw : 0 < w) :
    h.massWeightSubmodule w
      = ⨆ n ∈ (Finset.range (w + 1)).filter (fun n => 2 * (1 + n) ≤ w),
          (h.higgsSubmodule n ⊔ h.barHiggsSubmodule n) * h.massWeightSubmodule (w - 2 * (1 + n))
```

### F.3. The odd mass weights vanish

**`StandardModel.HiggsAlgebraCovRealization.massWeightSubmodule_odd_eq_bot`**, a lemma, [line 827](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L827).

> The odd mass weight submodules are trivial: every Higgs tower has even weight, and
> weights add under products.

```lean
lemma massWeightSubmodule_odd_eq_bot (n : ℕ) (hn : Odd n) :
    h.massWeightSubmodule n = ⊥
```

### F.4. The gauge weight decomposition

**`StandardModel.HiggsAlgebraCovRealization.massWeightSubmoduleGaugeWeight`**, a def, [line 845](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L845).

> The gauge weight decomposition of the mass weight submodules. By recursion on the
> weight through `massWeightSubmodule_eq`: a term of weight `i` is either a symbol of that
> weight — decomposed by `higgsSubmoduleGaugeWeight` and `barHiggsSubmoduleGaugeWeight` — or
> a product of two terms of lower positive weight, decomposed by `mul` from the
> decompositions supplied by the recursion.

```lean
noncomputable def massWeightSubmoduleGaugeWeight :
    (i : ℕ) → 0 < i → GaugeWeightDecomposition rep (h.massWeightSubmodule i)
```

**`StandardModel.HiggsAlgebraCovRealization.massWeightSubmoduleGaugeWeightOfNeZero`**, an instance, [line 866](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L866).

> The `NeZero` form of `massWeightSubmoduleGaugeWeight`.

```lean
noncomputable instance massWeightSubmoduleGaugeWeightOfNeZero (i : ℕ) [NeZero i] :
    GaugeWeightDecomposition rep (h.massWeightSubmodule i)
```

### F.5. Mass weights up to eight

> Each case removes the leftmost tower. The towers with `0`, `1`, `2` and `3` derivatives
> have weights `2`, `4`, `6` and `8`, and the remaining weight is read off from a smaller weight.
> Expanding the joins gives the products of `H` and `H̄`; the Higgs algebra is commutative,
> so orders differing only by the position of commuting factors are merged, and the products
> are written in a fixed order.

**`StandardModel.HiggsAlgebraCovRealization.massWeightSubmodule_two_eq`**, a lemma, [line 883](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L883).

> Weight two: the underived Higgs and conjugate Higgs.

```lean
lemma massWeightSubmodule_two_eq :
    h.massWeightSubmodule 2 = h.higgsSubmodule 0 ⊔ h.barHiggsSubmodule 0
```

**`StandardModel.HiggsAlgebraCovRealization.massWeightSubmodule_four_eq`**, a lemma, [line 892](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L892).

> Weight four: the once-derived symbols and the products of two underived ones. The
> leftmost tower is underived, leaving weight two, or once-derived, leaving weight zero.

```lean
lemma massWeightSubmodule_four_eq :
    h.massWeightSubmodule 4 = h.higgsSubmodule 1 ⊔ h.barHiggsSubmodule 1 ⊔
    h.higgsSubmodule 0 * h.higgsSubmodule 0 ⊔ h.higgsSubmodule 0 *
    h.barHiggsSubmodule 0 ⊔ h.barHiggsSubmodule 0 * h.barHiggsSubmodule 0
```

**`StandardModel.HiggsAlgebraCovRealization.massWeightSubmodule_six_eq`**, a lemma, [line 907](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L907).

> Weight six: the twice-derived symbols, a once-derived symbol against an underived one,
> and the products of three underived ones. The leftmost tower leaves weight four, two or
> zero.

```lean
lemma massWeightSubmodule_six_eq : h.massWeightSubmodule 6 =
    -- The derivative terms
    h.higgsSubmodule 2 ⊔ h.barHiggsSubmodule 2 ⊔
    h.higgsSubmodule 1 * h.higgsSubmodule 0 ⊔
    h.higgsSubmodule 1 * h.barHiggsSubmodule 0 ⊔
    h.barHiggsSubmodule 1 * h.higgsSubmodule 0 ⊔
    h.barHiggsSubmodule 1 * h.barHiggsSubmodule 0 ⊔
    -- The potential terms
    h.higgsSubmodule 0 * h.higgsSubmodule 0 * h.higgsSubmodule 0  ⊔
    h.higgsSubmodule 0 * h.higgsSubmodule 0 * h.barHiggsSubmodule 0 ⊔
    h.higgsSubmodule 0 * h.barHiggsSubmodule 0 * h.barHiggsSubmodule 0 ⊔
    h.barHiggsSubmodule 0 * h.barHiggsSubmodule 0 * h.barHiggsSubmodule 0
```

**`StandardModel.HiggsAlgebraCovRealization.massWeightSubmodule_eight_eq`**, a lemma, [line 940](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L940).

> Weight eight: the derivative terms with up to three derivatives, and the products of
> four underived symbols. The leftmost tower leaves weight six, four, two or zero.

```lean
lemma massWeightSubmodule_eight_eq :
    h.massWeightSubmodule 8 =
      -- The derivative terms
    h.higgsSubmodule 3 ⊔ h.barHiggsSubmodule 3 ⊔
    h.higgsSubmodule 2 * h.higgsSubmodule 0 ⊔
    h.higgsSubmodule 2 * h.barHiggsSubmodule 0 ⊔
    h.higgsSubmodule 0 * h.barHiggsSubmodule 2 ⊔
    h.barHiggsSubmodule 2 * h.barHiggsSubmodule 0 ⊔
    h.higgsSubmodule 1 * h.higgsSubmodule 1 ⊔
    h.higgsSubmodule 1 * h.barHiggsSubmodule 1 ⊔
    h.barHiggsSubmodule 1 * h.barHiggsSubmodule 1 ⊔
    h.higgsSubmodule 1 * h.higgsSubmodule 0 * h.higgsSubmodule 0 ⊔
    h.higgsSubmodule 1 * h.higgsSubmodule 0 * h.barHiggsSubmodule 0 ⊔
    h.higgsSubmodule 1 * h.barHiggsSubmodule 0 * h.barHiggsSubmodule 0 ⊔
    h.higgsSubmodule 0 * h.higgsSubmodule 0 * h.barHiggsSubmodule 1 ⊔
    h.higgsSubmodule 0 * h.barHiggsSubmodule 1 * h.barHiggsSubmodule 0 ⊔
    h.barHiggsSubmodule 1 * h.barHiggsSubmodule 0 * h.barHiggsSubmodule 0 ⊔
    -- The potential terms
    h.higgsSubmodule 0 * h.higgsSubmodule 0 * h.higgsSubmodule 0 * h.higgsSubmodule 0 ⊔
    h.higgsSubmodule 0 * h.higgsSubmodule 0 * h.higgsSubmodule 0 * h.barHiggsSubmodule 0 ⊔
    h.higgsSubmodule 0 * h.higgsSubmodule 0 * h.barHiggsSubmodule 0 * h.barHiggsSubmodule 0 ⊔
    h.higgsSubmodule 0 * h.barHiggsSubmodule 0 * h.barHiggsSubmodule 0 * h.barHiggsSubmodule 0 ⊔
    h.barHiggsSubmodule 0 * h.barHiggsSubmodule 0 * h.barHiggsSubmodule 0 *
      h.barHiggsSubmodule 0
```

## G. Gauge invariants

**`StandardModel.HiggsAlgebraCovRealization.gaugeInvariantOfMassDim`**, a def, [line 1010](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean#L1010).

> The gauge invariants of a given mass weight.

```lean
noncomputable def gaugeInvariantOfMassDim (M : ℕ) : Submodule ℂ B
```

## Depends on

- [The covariant jet algebra of the Higgs field](../part-08/jetalgebra-covjetalgebra-higgs.md)

## Proof depends on

- [Subalgebras generated by homogeneous submodules](../../../mathematics/part-01/homogeneousgenerators.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/Basic.lean)
