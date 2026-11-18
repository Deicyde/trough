---
declaration: module
origin: cited
lean: StandardModel.CovAlgebraRealization, StandardModel.CovAlgebraRealization.id, StandardModel.CovAlgebraRealization.covF, StandardModel.CovAlgebraRealization.covH, StandardModel.CovAlgebraRealization.covBarH, StandardModel.CovAlgebraRealization.covD, StandardModel.CovAlgebraRealization.covBarD, StandardModel.CovAlgebraRealization.covU
statement: formalized
proof: formalized
---

# The covariant algebra valued Standard Model

The module `PhyslibAlpha.Particles.StandardModel.CovRealization.Basic`, [PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean): 93 declarations, 90 with a docstring.

## i. Overview

> An algebra `B` carries a covariant Standard Model when the covariant fields of the Standard
> Model, and every polynomial expression in them, sit inside it compatibly with the global
> gauge action, the Lorentz action and the mass-weight grading. The covariant jet algebra
> `StandardModel.CovJetAlgebra` is the universal object with those fields, so the statement is
> a single one: an algebra map `CovJetAlgebra →ₐ[ℂ] B`, equivariant for the global gauge group
> and the Lorentz group and compatible with `massWeightPoly`. That is the structure
> `CovAlgebraRealization`, together with the two demands that the group actions be
> multiplicative on the whole of `B` and not merely on the image of the map.
>
> It stands to the covariant theory exactly as `AlgebraRealization` stands to the structure of
> bare derivative symbols it replaced. The thirteen covariant towers are derived rather than
> given — section B — and every law they satisfy is the covariant jet algebra's own law pushed
> along the map. Section C does that transport once for each shape a law takes, and section D
> assembles them: the three sectors — gauge, Higgs and fermion — and the commutation of towers
> of different sectors, which is what the classification of invariants is written in terms of.
>
> Section E closes the circle in the other direction: a Standard Model in the bare symbols
> carries a covariant one, by restricting its defining algebra map to the covariant
> subalgebra.
>
> A `CovAlgebraRealization` inherits every relation the covariant towers satisfy inside the
> jet algebra — the Ricci identity relating the antisymmetric part of a second covariant
> derivative to the field strength, for one. It is therefore strictly stronger than a bare
> list of the sector laws.

## ii. Key results

> - `StandardModel.CovAlgebraRealization` : an algebra is a covariant Standard Model when it
>   receives an equivariant algebra map from the covariant jet algebra.
> - `CovAlgebraRealization.id` : the covariant jet algebra is a covariant Standard Model,
>   along the identity algebra map.
> - `CovAlgebraRealization.F`, `CovAlgebraRealization.H` and their companions : the thirteen
>   covariant towers of a covariant Standard Model.
> - `CovAlgebraRealization.isHiggsSector`, `CovAlgebraRealization.isGaugeSector`,
>   `CovAlgebraRealization.isFermionSector` : the three sectors of those towers.
> - `CovAlgebraRealization.F_comm_H` and its companions : the towers of different sectors
>   commute.
> - `AlgebraRealization.toCovAlgebraRealization` : every Standard Model carries a covariant
>   Standard Model.

## iv. References

> * None.

**`StandardModel.CovAlgebraRealization`**, a structure, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L93).

> The algebra `B`, with a gauge action, a Lorentz action and a mass-weight grading, is a
> covariant Standard Model when it receives an algebra map from the covariant jet algebra of
> the Standard Model which is equivariant for both actions and compatible with the grading.
> The covariant fields of the Standard Model then sit inside `B` as the images of the
> covariant jet algebra's own, and every law they satisfy there is the covariant jet
> algebra's own law pushed along the map. It is the covariant counterpart of
> `AlgebraRealization`: where that asks for an equivariant algebra map out of `JetAlgebra`,
> on which the whole jet gauge group acts, this asks for one out of `CovJetAlgebra`, on
> which only the global gauge group acts. The last two fields are not consequences of the
> first four: an equivariant map forces the two actions to be multiplicative only on its
> image, whereas the sector structures demand them multiplicative on the whole of `B`.

```lean
structure CovAlgebraRealization (B : Type) [Ring B] [Algebra ℂ B]
    (repGauge : Representation ℂ GaugeGroupI B)
    (repLorentz : Representation ℂ SL(2,ℂ) B)
    (massWeightPoly : B →ₐ[ℂ] Polynomial B) where
  /-- The algebra map out of the covariant jet algebra of the Standard Model: it is what places
  the covariant fields of the Standard Model, and every polynomial expression in them,
  inside `B`. -/
  toAlgHom : CovJetAlgebra →ₐ[ℂ] B
  /-- The map is equivariant for the global gauge group: the gauge action on `B` restricts along
  it to the covariant jet algebra's own. -/
  map_repGauge : ∀ (g : GaugeGroupI) (x : CovJetAlgebra),
    toAlgHom (CovJetAlgebra.repGaugeGroupI g x) = repGauge g (toAlgHom x)
  /-- The map is equivariant for the Lorentz group: the Lorentz action on `B` restricts along it
  to the covariant jet algebra's own. -/
  map_repLorentz : ∀ (Λ : SL(2,ℂ)) (x : CovJetAlgebra),
    toAlgHom (CovJetAlgebra.repLorentzGroup Λ x) = repLorentz Λ (toAlgHom x)
  /-- The map carries the mass-weight grading of the covariant jet algebra to that of `B`: the
  mass-weight polynomial of an image is the image of the mass-weight polynomial. -/
  map_massWeight : ∀ x : CovJetAlgebra, massWeightPoly (toAlgHom x)
    = Polynomial.mapAlgHom toAlgHom (CovJetAlgebra.massWeightPoly x)
  /-- The gauge action preserves products on the whole of `B`, not merely on the image of the
  covariant jet algebra: gauge transformations act by algebra endomorphisms. -/
  repGauge_mul : ∀ (g : GaugeGroupI) (b₁ b₂ : B),
    repGauge g (b₁ * b₂) = repGauge g b₁ * repGauge g b₂
  /-- Lorentz transformations act on `B` by algebra maps: the action preserves products, so each
  `repLorentz Λ` is an algebra endomorphism of `B`. -/
  repLorentz_mul : ∀ (Λ : SL(2,ℂ)) (b₁ b₂ : B),
    repLorentz Λ (b₁ * b₂) = repLorentz Λ b₁ * repLorentz Λ b₂
```

## A. The identity realization

> The covariant jet algebra of the Standard Model is a covariant Standard Model along the
> identity algebra map, since `CovAlgebraRealization` asks precisely for an equivariant
> algebra map out of it. The four compatibility laws hold by definition, and the two
> multiplicativity laws are the ones the global gauge action and the Lorentz action were
> shown to satisfy when they were built.

**`StandardModel.CovAlgebraRealization.id`**, a def, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L138).

> The covariant jet algebra of the Standard Model is a covariant Standard Model: it is one
> along the identity algebra map.

```lean
noncomputable def id : CovAlgebraRealization CovJetAlgebra CovJetAlgebra.repGaugeGroupI
    CovJetAlgebra.repLorentzGroup CovJetAlgebra.massWeightPoly
```

## B. The covariant fields of a covariant Standard Model

> The thirteen covariant towers the theory is written in — the field strength, the Higgs
> field and its conjugate, and the five fermion species in three generations with their
> conjugates, each with all of its covariant derivatives — are not data of the structure.
> They are the corresponding towers of the covariant jet algebra, carried into `B` along the
> defining algebra map. The field-strength tower is real-linear in its value index, so the
> map is restricted to `ℝ` there.

**`StandardModel.CovAlgebraRealization.covF`**, a def, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L168).

> The covariant derivatives `∇_l F_{μν}` of the field strength inside `B`.

```lean
noncomputable def covF {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3) :
    Module.Dual ℝ GaugeAlgebra →ₗ[ℝ] B
```

**`StandardModel.CovAlgebraRealization.covH`**, a def, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L173).

> The covariant derivatives `∇_l H` of the Higgs field inside `B`.

```lean
noncomputable def covH {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ HiggsVec →ₗ[ℂ] B
```

**`StandardModel.CovAlgebraRealization.covBarH`**, a def, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L178).

> The covariant derivatives `∇_l H̄` of the conjugate Higgs field inside `B`.

```lean
noncomputable def covBarH {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ (ConjModule HiggsVec) →ₗ[ℂ] B
```

**`StandardModel.CovAlgebraRealization.covD`**, a def, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L183).

> The covariant derivatives of the `i`-th generation down-type quark singlet inside `B`.

```lean
noncomputable def covD (i : Fin 3) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ DownSinglet →ₗ[ℂ] B
```

**`StandardModel.CovAlgebraRealization.covBarD`**, a def, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L189).

> The covariant derivatives of the `i`-th generation conjugate down-type quark singlet
> inside `B`.

```lean
noncomputable def covBarD (i : Fin 3) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ (ConjModule DownSinglet) →ₗ[ℂ] B
```

**`StandardModel.CovAlgebraRealization.covU`**, a def, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L194).

> The covariant derivatives of the `i`-th generation up-type quark singlet inside `B`.

```lean
noncomputable def covU (i : Fin 3) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ UpSinglet →ₗ[ℂ] B
```

**`StandardModel.CovAlgebraRealization.covBarU`**, a def, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L200).

> The covariant derivatives of the `i`-th generation conjugate up-type quark singlet inside
> `B`.

```lean
noncomputable def covBarU (i : Fin 3) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ (ConjModule UpSinglet) →ₗ[ℂ] B
```

**`StandardModel.CovAlgebraRealization.covQ`**, a def, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L205).

> The covariant derivatives of the `i`-th generation quark doublet inside `B`.

```lean
noncomputable def covQ (i : Fin 3) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ QuarkDoublet →ₗ[ℂ] B
```

**`StandardModel.CovAlgebraRealization.covBarQ`**, a def, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L210).

> The covariant derivatives of the `i`-th generation conjugate quark doublet inside `B`.

```lean
noncomputable def covBarQ (i : Fin 3) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ (ConjModule QuarkDoublet) →ₗ[ℂ] B
```

**`StandardModel.CovAlgebraRealization.covL`**, a def, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L215).

> The covariant derivatives of the `i`-th generation lepton doublet inside `B`.

```lean
noncomputable def covL (i : Fin 3) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ LeptonDoubletV →ₗ[ℂ] B
```

**`StandardModel.CovAlgebraRealization.covBarL`**, a def, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L220).

> The covariant derivatives of the `i`-th generation conjugate lepton doublet inside `B`.

```lean
noncomputable def covBarL (i : Fin 3) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ (ConjModule LeptonDoubletV) →ₗ[ℂ] B
```

**`StandardModel.CovAlgebraRealization.covE`**, a def, [line 225](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L225).

> The covariant derivatives of the `i`-th generation charged-lepton singlet inside `B`.

```lean
noncomputable def covE (i : Fin 3) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ LeptonSinglet →ₗ[ℂ] B
```

**`StandardModel.CovAlgebraRealization.covBarE`**, a def, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L231).

> The covariant derivatives of the `i`-th generation conjugate charged-lepton singlet inside
> `B`.

```lean
noncomputable def covBarE (i : Fin 3) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ (ConjModule LeptonSinglet) →ₗ[ℂ] B
```

## C. Transporting a law along the defining map

> Every law of the covariant jet algebra becomes a law of `B` when pushed along the defining
> algebra map. The transport is the same in each of the shapes the laws take, so each shape
> is done once: a gauge law, a commutation law, an anticommutation law, an antisymmetry, a
> mass-weight eigenvalue equation and a Lorentz slot-mixing sum. Commutation needs no lemma
> of its own — it is `Commute.map`.

**`StandardModel.CovAlgebraRealization.map_repGauge_eq`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L249).

> A gauge transformation law transports along the defining map: the map is equivariant for
> the global gauge group.

```lean
lemma map_repGauge_eq {g : GaugeGroupI} {x y : CovJetAlgebra}
    (hxy : CovJetAlgebra.repGaugeGroupI g x = y) :
    repGauge g (k.toAlgHom x) = k.toAlgHom y
```

**`StandardModel.CovAlgebraRealization.map_anticomm`**, a lemma, [line 256](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L256).

> An anticommutation law transports along the defining map: the map preserves products and
> negation.

```lean
lemma map_anticomm {x y : CovJetAlgebra} (hxy : x * y = -(y * x)) :
    k.toAlgHom x * k.toAlgHom y = -(k.toAlgHom y * k.toAlgHom x)
```

**`StandardModel.CovAlgebraRealization.map_neg_eq`**, a lemma, [line 264](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L264).

> An antisymmetry transports along the defining map: the map preserves negation.

```lean
lemma map_neg_eq {x y : CovJetAlgebra} (hxy : x = -y) :
    k.toAlgHom x = -k.toAlgHom y
```

**`StandardModel.CovAlgebraRealization.map_massWeight_monomial`**, a lemma, [line 270](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L270).

> A mass-weight eigenvalue equation transports along the defining map: the map carries the
> grading of the covariant jet algebra to that of `B`.

```lean
lemma map_massWeight_monomial {n : ℕ} {x : CovJetAlgebra}
    (hx : CovJetAlgebra.massWeightPoly x = Polynomial.monomial n x) :
    massWeightPoly (k.toAlgHom x) = Polynomial.monomial n (k.toAlgHom x)
```

**`StandardModel.CovAlgebraRealization.map_lorentz`**, a lemma, [line 279](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L279).

> A Lorentz transformation law of a covariant tower transports along the defining map: the
> slot mixing is a finite sum of scalar multiples, and the map is linear and equivariant.

```lean
lemma map_lorentz {V : Type} [AddCommGroup V] [Module ℂ V]
    {rep : Representation ℂ SL(2,ℂ) V}
    {G : {n : ℕ} → (Fin n → (Fin 1 ⊕ Fin 3)) → Module.Dual ℂ V →ₗ[ℂ] CovJetAlgebra}
    (hG : IsLorentzCovDerivTransforms CovJetAlgebra.repLorentzGroup rep G) :
    IsLorentzCovDerivTransforms repLorentz rep
    (fun {_n} l => k.toAlgHom.toLinearMap ∘ₗ G l)
```

## D. The sectors, the statistics and the field algebra

> The covariant form of the theory splits into three sectors — gauge, Higgs and fermion —
> and the towers of different sectors commute. Those are the results the classification of
> invariants is written in terms of, and this section makes them available by dot notation on
> a covariant Standard Model, each one the covariant jet algebra's own law pushed along the
> defining map. The field algebra the
> covariant towers generate is here too, together with the centrality of the bosonic towers
> inside it.

**`StandardModel.CovAlgebraRealization.isHiggsSector`**, a def, [line 308](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L308).

> The Higgs sector of a covariant Standard Model: the defining map restricted to the
> covariant jet algebra of the Higgs field.

```lean
noncomputable def isHiggsSector :
    HiggsAlgebraCovRealization B repGauge repLorentz massWeightPoly
```

**`StandardModel.CovAlgebraRealization.isHiggsSector_covH`**, a lemma, [line 326](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L326).

> The Higgs towers of the Higgs sector of a covariant Standard Model are its own.

```lean
lemma isHiggsSector_covH (n : ℕ) (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    k.isHiggsSector.covH n l = k.covH l
```

**`StandardModel.CovAlgebraRealization.isHiggsSector_covBarH`**, a lemma, [line 332](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L332).

> The conjugate Higgs towers of the Higgs sector of a covariant Standard Model are its
> own.

```lean
lemma isHiggsSector_covBarH (n : ℕ) (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    k.isHiggsSector.covBarH n l = k.covBarH l
```

**`StandardModel.CovAlgebraRealization.isGaugeSector`**, a lemma, [line 336](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L336).

> The gauge sector of a covariant Standard Model.

```lean
lemma isGaugeSector : IsGaugeSector B repGauge k.repGauge_mul repLorentz k.repLorentz_mul
    (fun {_n} l μ ν => k.covF l μ ν) massWeightPoly
```

**`StandardModel.CovAlgebraRealization.covF_comp_perm_of_map_lie`**, a lemma, [line 363](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L363).

> At a dual vector vanishing on every bracket, such as the hypercharge coordinate, the
> field-strength tower is symmetric in its derivative slots, at every order: the law of the
> covariant jet algebra, where those covariant derivatives are ordinary ones, pushed along the
> defining map. It is not a law of `IsGaugeSector`, and the components along the non-abelian
> factors have no such symmetry.

```lean
lemma covF_comp_perm_of_map_lie {φ : Module.Dual ℝ GaugeAlgebra}
    (hφ : ∀ x y : GaugeAlgebra, φ ⁅x, y⁆ = 0) {n : ℕ} (σ : Equiv.Perm (Fin n))
    (l : Fin n → (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3) :
    k.covF (l ∘ σ) μ ν φ = k.covF l μ ν φ
```

**`StandardModel.CovAlgebraRealization.isFermionSector`**, a lemma, [line 370](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L370).

> The fermion sector of a covariant Standard Model.

```lean
lemma isFermionSector : IsFermionSector B repGauge k.repGauge_mul repLorentz k.repLorentz_mul
    (fun {_n} i l => k.covD i l) (fun {_n} i l => k.covBarD i l)
    (fun {_n} i l => k.covU i l) (fun {_n} i l => k.covBarU i l)
    (fun {_n} i l => k.covQ i l) (fun {_n} i l => k.covBarQ i l)
    (fun {_n} i l => k.covL i l) (fun {_n} i l => k.covBarL i l)
    (fun {_n} i l => k.covE i l) (fun {_n} i l => k.covBarE i l) massWeightPoly
```

**`StandardModel.CovAlgebraRealization.repGauge_one`**, a lemma, [line 545](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L545).

> The gauge action fixes the unit of the algebra: it is multiplicative, and every element of
> the group is invertible.

```lean
lemma repGauge_one (g : GaugeGroupI) : repGauge g (1 : B) = 1
```

**`StandardModel.CovAlgebraRealization.repLorentz_one`**, a lemma, [line 556](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L556).

> The Lorentz action fixes the unit of the algebra.

```lean
lemma repLorentz_one (Λ : SL(2,ℂ)) : repLorentz Λ (1 : B) = 1
```

### D.1. The cross-sector commutation rules

**`StandardModel.CovAlgebraRealization.F_comm_H`**, a lemma, [line 572](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L572).

> The cross-sector commutation rule `F_comm_H` of a covariant Standard Model.

```lean
lemma F_comm_H {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (μ ν : Fin 1 ⊕ Fin 3)
    (ψ : Module.Dual ℝ GaugeAlgebra) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ HiggsVec) :
    Commute (k.covF l μ ν ψ) (k.covH l' φ)
```

**`StandardModel.CovAlgebraRealization.F_comm_barH`**, a lemma, [line 579](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L579).

> The cross-sector commutation rule `F_comm_barH` of a covariant Standard Model.

```lean
lemma F_comm_barH {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (μ ν : Fin 1 ⊕ Fin 3)
    (ψ : Module.Dual ℝ GaugeAlgebra) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ (ConjModule HiggsVec)) :
    Commute (k.covF l μ ν ψ) (k.covBarH l' φ)
```

**`StandardModel.CovAlgebraRealization.F_comm_d`**, a lemma, [line 586](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L586).

> The cross-sector commutation rule `F_comm_d` of a covariant Standard Model.

```lean
lemma F_comm_d {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (μ ν : Fin 1 ⊕ Fin 3)
    (ψ : Module.Dual ℝ GaugeAlgebra) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ DownSinglet) :
    Commute (k.covF l μ ν ψ) (k.covD i l' φ)
```

**`StandardModel.CovAlgebraRealization.F_comm_bard`**, a lemma, [line 593](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L593).

> The cross-sector commutation rule `F_comm_bard` of a covariant Standard Model.

```lean
lemma F_comm_bard {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (μ ν : Fin 1 ⊕ Fin 3)
    (ψ : Module.Dual ℝ GaugeAlgebra) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ (ConjModule DownSinglet)) :
    Commute (k.covF l μ ν ψ) (k.covBarD i l' φ)
```

**`StandardModel.CovAlgebraRealization.F_comm_u`**, a lemma, [line 600](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L600).

> The cross-sector commutation rule `F_comm_u` of a covariant Standard Model.

```lean
lemma F_comm_u {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (μ ν : Fin 1 ⊕ Fin 3)
    (ψ : Module.Dual ℝ GaugeAlgebra) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ UpSinglet) :
    Commute (k.covF l μ ν ψ) (k.covU i l' φ)
```

**`StandardModel.CovAlgebraRealization.F_comm_baru`**, a lemma, [line 607](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L607).

> The cross-sector commutation rule `F_comm_baru` of a covariant Standard Model.

```lean
lemma F_comm_baru {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (μ ν : Fin 1 ⊕ Fin 3)
    (ψ : Module.Dual ℝ GaugeAlgebra) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ (ConjModule UpSinglet)) :
    Commute (k.covF l μ ν ψ) (k.covBarU i l' φ)
```

**`StandardModel.CovAlgebraRealization.F_comm_Q`**, a lemma, [line 614](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L614).

> The cross-sector commutation rule `F_comm_Q` of a covariant Standard Model.

```lean
lemma F_comm_Q {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (μ ν : Fin 1 ⊕ Fin 3)
    (ψ : Module.Dual ℝ GaugeAlgebra) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ QuarkDoublet) :
    Commute (k.covF l μ ν ψ) (k.covQ i l' φ)
```

**`StandardModel.CovAlgebraRealization.F_comm_barQ`**, a lemma, [line 621](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L621).

> The cross-sector commutation rule `F_comm_barQ` of a covariant Standard Model.

```lean
lemma F_comm_barQ {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (μ ν : Fin 1 ⊕ Fin 3)
    (ψ : Module.Dual ℝ GaugeAlgebra) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ (ConjModule QuarkDoublet)) :
    Commute (k.covF l μ ν ψ) (k.covBarQ i l' φ)
```

**`StandardModel.CovAlgebraRealization.F_comm_L`**, a lemma, [line 628](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L628).

> The cross-sector commutation rule `F_comm_L` of a covariant Standard Model.

```lean
lemma F_comm_L {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (μ ν : Fin 1 ⊕ Fin 3)
    (ψ : Module.Dual ℝ GaugeAlgebra) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ LeptonDoubletV) :
    Commute (k.covF l μ ν ψ) (k.covL i l' φ)
```

**`StandardModel.CovAlgebraRealization.F_comm_barL`**, a lemma, [line 635](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L635).

> The cross-sector commutation rule `F_comm_barL` of a covariant Standard Model.

```lean
lemma F_comm_barL {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (μ ν : Fin 1 ⊕ Fin 3)
    (ψ : Module.Dual ℝ GaugeAlgebra) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ (ConjModule LeptonDoubletV)) :
    Commute (k.covF l μ ν ψ) (k.covBarL i l' φ)
```

**`StandardModel.CovAlgebraRealization.F_comm_e`**, a lemma, [line 642](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L642).

> The cross-sector commutation rule `F_comm_e` of a covariant Standard Model.

```lean
lemma F_comm_e {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (μ ν : Fin 1 ⊕ Fin 3)
    (ψ : Module.Dual ℝ GaugeAlgebra) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ LeptonSinglet) :
    Commute (k.covF l μ ν ψ) (k.covE i l' φ)
```

**`StandardModel.CovAlgebraRealization.F_comm_bare`**, a lemma, [line 649](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L649).

> The cross-sector commutation rule `F_comm_bare` of a covariant Standard Model.

```lean
lemma F_comm_bare {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (μ ν : Fin 1 ⊕ Fin 3)
    (ψ : Module.Dual ℝ GaugeAlgebra) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ (ConjModule LeptonSinglet)) :
    Commute (k.covF l μ ν ψ) (k.covBarE i l' φ)
```

**`StandardModel.CovAlgebraRealization.H_comm_d`**, a lemma, [line 656](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L656).

> The cross-sector commutation rule `H_comm_d` of a covariant Standard Model.

```lean
lemma H_comm_d {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ HiggsVec) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ' : Module.Dual ℂ DownSinglet) :
    Commute (k.covH l φ) (k.covD i l' φ')
```

**`StandardModel.CovAlgebraRealization.H_comm_bard`**, a lemma, [line 663](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L663).

> The cross-sector commutation rule `H_comm_bard` of a covariant Standard Model.

```lean
lemma H_comm_bard {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ HiggsVec) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ' : Module.Dual ℂ (ConjModule DownSinglet)) :
    Commute (k.covH l φ) (k.covBarD i l' φ')
```

**`StandardModel.CovAlgebraRealization.H_comm_u`**, a lemma, [line 670](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L670).

> The cross-sector commutation rule `H_comm_u` of a covariant Standard Model.

```lean
lemma H_comm_u {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ HiggsVec) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ' : Module.Dual ℂ UpSinglet) :
    Commute (k.covH l φ) (k.covU i l' φ')
```

**`StandardModel.CovAlgebraRealization.H_comm_baru`**, a lemma, [line 677](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L677).

> The cross-sector commutation rule `H_comm_baru` of a covariant Standard Model.

```lean
lemma H_comm_baru {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ HiggsVec) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ' : Module.Dual ℂ (ConjModule UpSinglet)) :
    Commute (k.covH l φ) (k.covBarU i l' φ')
```

**`StandardModel.CovAlgebraRealization.H_comm_Q`**, a lemma, [line 684](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L684).

> The cross-sector commutation rule `H_comm_Q` of a covariant Standard Model.

```lean
lemma H_comm_Q {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ HiggsVec) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ' : Module.Dual ℂ QuarkDoublet) :
    Commute (k.covH l φ) (k.covQ i l' φ')
```

**`StandardModel.CovAlgebraRealization.H_comm_barQ`**, a lemma, [line 691](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L691).

> The cross-sector commutation rule `H_comm_barQ` of a covariant Standard Model.

```lean
lemma H_comm_barQ {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ HiggsVec) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ' : Module.Dual ℂ (ConjModule QuarkDoublet)) :
    Commute (k.covH l φ) (k.covBarQ i l' φ')
```

**`StandardModel.CovAlgebraRealization.H_comm_L`**, a lemma, [line 698](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L698).

> The cross-sector commutation rule `H_comm_L` of a covariant Standard Model.

```lean
lemma H_comm_L {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ HiggsVec) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ' : Module.Dual ℂ LeptonDoubletV) :
    Commute (k.covH l φ) (k.covL i l' φ')
```

**`StandardModel.CovAlgebraRealization.H_comm_barL`**, a lemma, [line 705](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L705).

> The cross-sector commutation rule `H_comm_barL` of a covariant Standard Model.

```lean
lemma H_comm_barL {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ HiggsVec) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ' : Module.Dual ℂ (ConjModule LeptonDoubletV)) :
    Commute (k.covH l φ) (k.covBarL i l' φ')
```

**`StandardModel.CovAlgebraRealization.H_comm_e`**, a lemma, [line 712](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L712).

> The cross-sector commutation rule `H_comm_e` of a covariant Standard Model.

```lean
lemma H_comm_e {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ HiggsVec) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ' : Module.Dual ℂ LeptonSinglet) :
    Commute (k.covH l φ) (k.covE i l' φ')
```

**`StandardModel.CovAlgebraRealization.H_comm_bare`**, a lemma, [line 719](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L719).

> The cross-sector commutation rule `H_comm_bare` of a covariant Standard Model.

```lean
lemma H_comm_bare {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ HiggsVec) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ' : Module.Dual ℂ (ConjModule LeptonSinglet)) :
    Commute (k.covH l φ) (k.covBarE i l' φ')
```

**`StandardModel.CovAlgebraRealization.barH_comm_d`**, a lemma, [line 726](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L726).

> The cross-sector commutation rule `barH_comm_d` of a covariant Standard Model.

```lean
lemma barH_comm_d {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ (ConjModule HiggsVec)) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ' : Module.Dual ℂ DownSinglet) :
    Commute (k.covBarH l φ) (k.covD i l' φ')
```

**`StandardModel.CovAlgebraRealization.barH_comm_bard`**, a lemma, [line 733](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L733).

> The cross-sector commutation rule `barH_comm_bard` of a covariant Standard Model.

```lean
lemma barH_comm_bard {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ (ConjModule HiggsVec)) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ' : Module.Dual ℂ (ConjModule DownSinglet)) :
    Commute (k.covBarH l φ) (k.covBarD i l' φ')
```

**`StandardModel.CovAlgebraRealization.barH_comm_u`**, a lemma, [line 740](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L740).

> The cross-sector commutation rule `barH_comm_u` of a covariant Standard Model.

```lean
lemma barH_comm_u {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ (ConjModule HiggsVec)) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ' : Module.Dual ℂ UpSinglet) :
    Commute (k.covBarH l φ) (k.covU i l' φ')
```

**`StandardModel.CovAlgebraRealization.barH_comm_baru`**, a lemma, [line 747](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L747).

> The cross-sector commutation rule `barH_comm_baru` of a covariant Standard Model.

```lean
lemma barH_comm_baru {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ (ConjModule HiggsVec)) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ' : Module.Dual ℂ (ConjModule UpSinglet)) :
    Commute (k.covBarH l φ) (k.covBarU i l' φ')
```

**`StandardModel.CovAlgebraRealization.barH_comm_Q`**, a lemma, [line 754](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L754).

> The cross-sector commutation rule `barH_comm_Q` of a covariant Standard Model.

```lean
lemma barH_comm_Q {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ (ConjModule HiggsVec)) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ' : Module.Dual ℂ QuarkDoublet) :
    Commute (k.covBarH l φ) (k.covQ i l' φ')
```

**`StandardModel.CovAlgebraRealization.barH_comm_barQ`**, a lemma, [line 761](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L761).

> The cross-sector commutation rule `barH_comm_barQ` of a covariant Standard Model.

```lean
lemma barH_comm_barQ {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ (ConjModule HiggsVec)) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ' : Module.Dual ℂ (ConjModule QuarkDoublet)) :
    Commute (k.covBarH l φ) (k.covBarQ i l' φ')
```

**`StandardModel.CovAlgebraRealization.barH_comm_L`**, a lemma, [line 768](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L768).

> The cross-sector commutation rule `barH_comm_L` of a covariant Standard Model.

```lean
lemma barH_comm_L {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ (ConjModule HiggsVec)) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ' : Module.Dual ℂ LeptonDoubletV) :
    Commute (k.covBarH l φ) (k.covL i l' φ')
```

**`StandardModel.CovAlgebraRealization.barH_comm_barL`**, a lemma, [line 775](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L775).

> The cross-sector commutation rule `barH_comm_barL` of a covariant Standard Model.

```lean
lemma barH_comm_barL {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ (ConjModule HiggsVec)) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ' : Module.Dual ℂ (ConjModule LeptonDoubletV)) :
    Commute (k.covBarH l φ) (k.covBarL i l' φ')
```

**`StandardModel.CovAlgebraRealization.barH_comm_e`**, a lemma, [line 782](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L782).

> The cross-sector commutation rule `barH_comm_e` of a covariant Standard Model.

```lean
lemma barH_comm_e {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ (ConjModule HiggsVec)) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ' : Module.Dual ℂ LeptonSinglet) :
    Commute (k.covBarH l φ) (k.covE i l' φ')
```

**`StandardModel.CovAlgebraRealization.barH_comm_bare`**, a lemma, [line 789](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L789).

> The cross-sector commutation rule `barH_comm_bare` of a covariant Standard Model.

```lean
lemma barH_comm_bare {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ (ConjModule HiggsVec)) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ' : Module.Dual ℂ (ConjModule LeptonSinglet)) :
    Commute (k.covBarH l φ) (k.covBarE i l' φ')
```

### D.2. The field algebra

**`StandardModel.CovAlgebraRealization.fieldAlgebra`**, a def, [line 804](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L804).

> The algebra generated by all the covariant fields of a covariant Standard Model: the
> covariant-derivative towers of the field strength, of the Higgs and its conjugate, and of
> the three families of each fermion species with their conjugates.

```lean
def fieldAlgebra : Subalgebra ℂ B
```

**`StandardModel.CovAlgebraRealization.F_commute_mem_fieldAlgebra`**, a lemma, [line 816](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L816).

```lean
lemma F_commute_mem_fieldAlgebra {n : ℕ} {l : Fin n → Fin 1 ⊕ Fin 3} {μ ν : Fin 1 ⊕ Fin 3}
    (φ : Module.Dual ℝ GaugeAlgebra) (x : B) (hx : x ∈ k.fieldAlgebra) :
    k.covF l μ ν φ * x = x * k.covF l μ ν φ
```

**`StandardModel.CovAlgebraRealization.H_commute_mem_fieldAlgebra`**, a lemma, [line 840](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L840).

```lean
lemma H_commute_mem_fieldAlgebra {n : ℕ} {l : Fin n → Fin 1 ⊕ Fin 3}
    (φ : Module.Dual ℂ HiggsVec) (x : B) (hx : x ∈ k.fieldAlgebra) :
    k.covH l φ * x = x * k.covH l φ
```

**`StandardModel.CovAlgebraRealization.barH_commute_mem_fieldAlgebra`**, a lemma, [line 864](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L864).

```lean
lemma barH_commute_mem_fieldAlgebra {n : ℕ} {l : Fin n → Fin 1 ⊕ Fin 3}
    (φ : Module.Dual ℂ (ConjModule HiggsVec)) (x : B) (hx : x ∈ k.fieldAlgebra) :
    k.covBarH l φ * x = x * k.covBarH l φ
```

## E. Naturality of the covariant derivative

> A covariant tower is built from the bare families by two operations only: the pairing of an
> adjoint family against a matter one (`GaugeAlgebraRealization.actionFam`), and the bracket of two
> adjoint families (`GaugeAlgebraRealization.bracketFam`). Each expands, in bases of the gauge algebra
> and of the value space, as a finite double sum of scalar multiples of products of
> components, so each commutes with an algebra map. The whole recursion therefore does, and
> that is the content of this section: the covariant towers of a Standard Model are the jet
> algebra's own covariant towers pushed along the defining map.

**`StandardModel.GaugeAlgebraRealization.mapAdj`**, an abbrev, [line 912](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L912).

> Composing an adjoint-indexed family with an algebra map.

```lean
noncomputable abbrev mapAdj (Φ : B →ₐ[ℂ] B')
    (f : Module.Dual ℝ GaugeAlgebra →ₗ[ℝ] B) : Module.Dual ℝ GaugeAlgebra →ₗ[ℝ] B'
```

**`StandardModel.GaugeAlgebraRealization.map_real_smul`**, a lemma, [line 917](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L917).

> An algebra map over `ℂ` is real-linear.

```lean
lemma map_real_smul (Φ : B →ₐ[ℂ] B') (r : ℝ) (b : B) : Φ (r • b) = r • Φ b
```

**`StandardModel.GaugeAlgebraRealization.actionFam_map`**, a lemma, [line 922](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L922).

> The action pairing commutes with an algebra map: it is a finite double sum of scalar
> multiples of products of components.

```lean
lemma actionFam_map (Φ : B →ₐ[ℂ] B') (act : GaugeAlgebra →ₗ[ℝ] V →ₗ[ℂ] V)
    (f : Module.Dual ℝ GaugeAlgebra →ₗ[ℝ] B) (g : Module.Dual ℂ V →ₗ[ℂ] B)
    (φ : Module.Dual ℂ V) :
    Φ (actionFam act f g φ) = actionFam act (mapAdj Φ f) (Φ.toLinearMap ∘ₗ g) φ
```

**`StandardModel.GaugeAlgebraRealization.bracketFam_map`**, a lemma, [line 936](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L936).

> The bracket of two adjoint families commutes with an algebra map.

```lean
lemma bracketFam_map (Φ : B →ₐ[ℂ] B') (f g : Module.Dual ℝ GaugeAlgebra →ₗ[ℝ] B)
    (φ : Module.Dual ℝ GaugeAlgebra) :
    Φ (bracketFam f g φ) = bracketFam (mapAdj Φ f) (mapAdj Φ g) φ
```

**`StandardModel.GaugeAlgebraRealization.actionFam_map'`**, a lemma, [line 953](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L953).

> The action pairing of two families related by an algebra map is the pairing of the images.

```lean
lemma actionFam_map' (Φ : B →ₐ[ℂ] B')
    {f : Module.Dual ℝ GaugeAlgebra →ₗ[ℝ] B} {f' : Module.Dual ℝ GaugeAlgebra →ₗ[ℝ] B'}
    (hf : ∀ ψ, Φ (f ψ) = f' ψ)
    {g : Module.Dual ℂ V →ₗ[ℂ] B} {g' : Module.Dual ℂ V →ₗ[ℂ] B'} (hg : ∀ χ, Φ (g χ) = g' χ)
    (φ : Module.Dual ℂ V) :
    Φ (actionFam act f g φ) = actionFam act f' g' φ
```

**`StandardModel.GaugeAlgebraRealization.bracketFam_map'`**, a lemma, [line 964](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L964).

> The bracket of two adjoint families related by an algebra map is the bracket of the
> images.

```lean
lemma bracketFam_map' (Φ : B →ₐ[ℂ] B')
    {f : Module.Dual ℝ GaugeAlgebra →ₗ[ℝ] B} {f' : Module.Dual ℝ GaugeAlgebra →ₗ[ℝ] B'}
    (hf : ∀ ψ, Φ (f ψ) = f' ψ)
    {g : Module.Dual ℝ GaugeAlgebra →ₗ[ℝ] B} {g' : Module.Dual ℝ GaugeAlgebra →ₗ[ℝ] B'}
    (hg : ∀ ψ, Φ (g ψ) = g' ψ) (φ : Module.Dual ℝ GaugeAlgebra) :
    Φ (bracketFam f g φ) = bracketFam f' g' φ
```

**`StandardModel.GaugeAlgebraRealization.actionFamConv_map'`**, a lemma, [line 974](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L974).

> The derived action family commutes with an algebra map.

```lean
lemma actionFamConv_map' (Φ : B →ₐ[ℂ] B') (hA : ∀ p ρ ψ, Φ (A p ρ ψ) = A' p ρ ψ)
    {F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B}
    {F' : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B'}
    (hF : ∀ s χ, Φ (F s χ) = F' s χ) (ρ : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ V) :
    Φ (actionFamConv A act ρ F s φ) = actionFamConv A' act ρ F' s φ
```

**`StandardModel.GaugeAlgebraRealization.bracketFamConv_map'`**, a lemma, [line 986](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L986).

> The derived bracket family commutes with an algebra map.

```lean
lemma bracketFamConv_map' (Φ : B →ₐ[ℂ] B') (hA : ∀ p ρ ψ, Φ (A p ρ ψ) = A' p ρ ψ)
    {F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℝ GaugeAlgebra →ₗ[ℝ] B}
    {F' : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℝ GaugeAlgebra →ₗ[ℝ] B'}
    (hF : ∀ s χ, Φ (F s χ) = F' s χ) (ρ : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℝ GaugeAlgebra) :
    Φ (bracketFamConv A ρ F s φ) = bracketFamConv A' ρ F' s φ
```

**`StandardModel.GaugeAlgebraRealization.commutatorFam_map'`**, a lemma, [line 999](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L999).

> The derived commutator family commutes with an algebra map.

```lean
lemma commutatorFam_map' (Φ : B →ₐ[ℂ] B') (hA : ∀ p ρ ψ, Φ (A p ρ ψ) = A' p ρ ψ)
    (μ ν : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℝ GaugeAlgebra) :
    Φ (commutatorFam A μ ν s φ) = commutatorFam A' μ ν s φ
```

**`StandardModel.GaugeAlgebraRealization.fieldStrength_map'`**, a lemma, [line 1009](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L1009).

> The field strength commutes with an algebra map.

```lean
lemma fieldStrength_map' (Φ : B →ₐ[ℂ] B') (hA : ∀ p ρ ψ, Φ (A p ρ ψ) = A' p ρ ψ)
    (μ ν : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℝ GaugeAlgebra) :
    Φ (fieldStrength A μ ν s φ) = fieldStrength A' μ ν s φ
```

**`StandardModel.GaugeAlgebraRealization.covDerivAction_map'`**, a lemma, [line 1016](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L1016).

> The covariant derivative of a matter family commutes with an algebra map.

```lean
lemma covDerivAction_map' (Φ : B →ₐ[ℂ] B') (hA : ∀ p ρ ψ, Φ (A p ρ ψ) = A' p ρ ψ)
    {F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B}
    {F' : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B'}
    (hF : ∀ s χ, Φ (F s χ) = F' s χ) (ρ : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ V) :
    Φ (covDerivAction A act F ρ s φ) = covDerivAction A' act F' ρ s φ
```

**`StandardModel.GaugeAlgebraRealization.covDerivAdjoint_map'`**, a lemma, [line 1025](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L1025).

> The covariant derivative of an adjoint family commutes with an algebra map.

```lean
lemma covDerivAdjoint_map' (Φ : B →ₐ[ℂ] B') (hA : ∀ p ρ ψ, Φ (A p ρ ψ) = A' p ρ ψ)
    {F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℝ GaugeAlgebra →ₗ[ℝ] B}
    {F' : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℝ GaugeAlgebra →ₗ[ℝ] B'}
    (hF : ∀ s χ, Φ (F s χ) = F' s χ) (ρ : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℝ GaugeAlgebra) :
    Φ (covDerivAdjoint A F ρ s φ) = covDerivAdjoint A' F' ρ s φ
```

**`StandardModel.GaugeAlgebraRealization.covDerivIter_map'`**, a lemma, [line 1034](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L1034).

> The iterated covariant derivative of a matter family commutes with an algebra map.

```lean
lemma covDerivIter_map' (Φ : B →ₐ[ℂ] B') (hA : ∀ p ρ ψ, Φ (A p ρ ψ) = A' p ρ ψ)
    {F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B}
    {F' : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B'}
    (hF : ∀ s χ, Φ (F s χ) = F' s χ) :
    ∀ (n : ℕ) (l : Fin n → (Fin 1 ⊕ Fin 3)) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ V),
      Φ (covDerivIter A act F n l s φ) = covDerivIter A' act F' n l s φ
```

**`StandardModel.GaugeAlgebraRealization.iteratedCovDerivAdjoint_map'`**, a lemma, [line 1047](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L1047).

> The iterated covariant derivative of an adjoint family commutes with an algebra map.

```lean
lemma iteratedCovDerivAdjoint_map' (Φ : B →ₐ[ℂ] B') (hA : ∀ p ρ ψ, Φ (A p ρ ψ) = A' p ρ ψ)
    {F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℝ GaugeAlgebra →ₗ[ℝ] B}
    {F' : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℝ GaugeAlgebra →ₗ[ℝ] B'}
    (hF : ∀ s χ, Φ (F s χ) = F' s χ) :
    ∀ (l : List (Fin 1 ⊕ Fin 3)) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℝ GaugeAlgebra),
      Φ (iteratedCovDerivAdjoint A l F s φ) = iteratedCovDerivAdjoint A' l F' s φ
```

## F. Every Standard Model is a covariant Standard Model

> A Standard Model in the bare symbols carries one in the covariant towers: its defining
> algebra map out of the jet algebra restricts to the covariant field algebra, and the
> restriction is equivariant for the global gauge group and the Lorentz group and compatible
> with the mass-weight grading, because the unrestricted map is. The thirteen covariant
> towers of the resulting covariant Standard Model are, on the nose, the covariant towers of
> `AlgebraRealization.CovStandardModel`.

**`StandardModel.AlgebraRealization.toCovAlgebraRealization`**, a def, [line 1084](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L1084).

> A Standard Model is a covariant Standard Model, for the global gauge group: the defining
> algebra map out of the jet algebra, restricted to the covariant jet algebra.

```lean
noncomputable def toCovAlgebraRealization :
    CovAlgebraRealization B (repGlobal repJet) repLorentz massWeightPoly
```

### F.1. The covariant towers agree

**`StandardModel.AlgebraRealization.toAlgHom_id_A`**, a lemma, [line 1107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L1107).

> The defining map of a Standard Model carries the jet algebra's gauge-field symbols to its
> own: both are the jet algebra's, one of them pushed forward.

```lean
lemma toAlgHom_id_A (p : Multiset (Fin 1 ⊕ Fin 3)) (ρ : Fin 1 ⊕ Fin 3)
    (ψ : Module.Dual ℝ GaugeAlgebra) :
    h.toAlgHom (AlgebraRealization.id.A p ρ ψ) = h.A p ρ ψ
```

**`StandardModel.AlgebraRealization.toCovAlgebraRealization_covF`**, a lemma, [line 1114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L1114).

> The field-strength tower of the covariant Standard Model carried by a Standard Model is
> its own field-strength tower.

```lean
lemma toCovAlgebraRealization_covF {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (μ ν : Fin 1 ⊕ Fin 3) :
    h.toCovAlgebraRealization.covF l μ ν = h.covF l μ ν
```

**`StandardModel.AlgebraRealization.toCovAlgebraRealization_covH`**, a lemma, [line 1130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L1130).

> The higgs tower of the covariant Standard Model carried by a Standard Model is its own.

```lean
lemma toCovAlgebraRealization_covH {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    h.toCovAlgebraRealization.covH l = h.covDerivH l
```

**`StandardModel.AlgebraRealization.toCovAlgebraRealization_covBarH`**, a lemma, [line 1142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L1142).

> The conjugate higgs tower of the covariant Standard Model carried by a Standard Model is
> its own.

```lean
lemma toCovAlgebraRealization_covBarH {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    h.toCovAlgebraRealization.covBarH l = h.covDerivBarH l
```

**`StandardModel.AlgebraRealization.toCovAlgebraRealization_covD`**, a lemma, [line 1154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L1154).

> The down-type quark tower of the covariant Standard Model carried by a Standard Model is
> its own.

```lean
lemma toCovAlgebraRealization_covD (i : Fin 3) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    h.toCovAlgebraRealization.covD i l = h.covDerivD i l
```

**`StandardModel.AlgebraRealization.toCovAlgebraRealization_covBarD`**, a lemma, [line 1166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L1166).

> The conjugate down-type quark tower of the covariant Standard Model carried by a Standard
> Model is its own.

```lean
lemma toCovAlgebraRealization_covBarD (i : Fin 3) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    h.toCovAlgebraRealization.covBarD i l = h.covDerivBarD i l
```

**`StandardModel.AlgebraRealization.toCovAlgebraRealization_covU`**, a lemma, [line 1178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L1178).

> The up-type quark tower of the covariant Standard Model carried by a Standard Model is its
> own.

```lean
lemma toCovAlgebraRealization_covU (i : Fin 3) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    h.toCovAlgebraRealization.covU i l = h.covDerivU i l
```

**`StandardModel.AlgebraRealization.toCovAlgebraRealization_covBarU`**, a lemma, [line 1190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L1190).

> The conjugate up-type quark tower of the covariant Standard Model carried by a Standard
> Model is its own.

```lean
lemma toCovAlgebraRealization_covBarU (i : Fin 3) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    h.toCovAlgebraRealization.covBarU i l = h.covDerivBarU i l
```

**`StandardModel.AlgebraRealization.toCovAlgebraRealization_covQ`**, a lemma, [line 1202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L1202).

> The quark doublet tower of the covariant Standard Model carried by a Standard Model is its
> own.

```lean
lemma toCovAlgebraRealization_covQ (i : Fin 3) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    h.toCovAlgebraRealization.covQ i l = h.covDerivQ i l
```

**`StandardModel.AlgebraRealization.toCovAlgebraRealization_covBarQ`**, a lemma, [line 1214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L1214).

> The conjugate quark doublet tower of the covariant Standard Model carried by a Standard
> Model is its own.

```lean
lemma toCovAlgebraRealization_covBarQ (i : Fin 3) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    h.toCovAlgebraRealization.covBarQ i l = h.covDerivBarQ i l
```

**`StandardModel.AlgebraRealization.toCovAlgebraRealization_covL`**, a lemma, [line 1226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L1226).

> The lepton doublet tower of the covariant Standard Model carried by a Standard Model is
> its own.

```lean
lemma toCovAlgebraRealization_covL (i : Fin 3) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    h.toCovAlgebraRealization.covL i l = h.covDerivL i l
```

**`StandardModel.AlgebraRealization.toCovAlgebraRealization_covBarL`**, a lemma, [line 1238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L1238).

> The conjugate lepton doublet tower of the covariant Standard Model carried by a Standard
> Model is its own.

```lean
lemma toCovAlgebraRealization_covBarL (i : Fin 3) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    h.toCovAlgebraRealization.covBarL i l = h.covDerivBarL i l
```

**`StandardModel.AlgebraRealization.toCovAlgebraRealization_covE`**, a lemma, [line 1250](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L1250).

> The charged-lepton singlet tower of the covariant Standard Model carried by a Standard
> Model is its own.

```lean
lemma toCovAlgebraRealization_covE (i : Fin 3) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    h.toCovAlgebraRealization.covE i l = h.covDerivE i l
```

**`StandardModel.AlgebraRealization.toCovAlgebraRealization_covBarE`**, a lemma, [line 1262](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean#L1262).

> The conjugate charged-lepton singlet tower of the covariant Standard Model carried by a
> Standard Model is its own.

```lean
lemma toCovAlgebraRealization_covBarE (i : Fin 3) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    h.toCovAlgebraRealization.covBarE i l = h.covDerivBarE i l
```

## Depends on

- [The fermion sector](../part-05/isfermionsector-basic.md)
- [The gauge sector](../part-06/isgaugesector-basic.md)
- [The algebra valued Higgs boson](../part-10/realization-higgscov-basic.md)

## Proof depends on

- [The sectors of the covariant jet algebra](../part-08/jetalgebra-covjetalgebra-sectors.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Basic.lean)
