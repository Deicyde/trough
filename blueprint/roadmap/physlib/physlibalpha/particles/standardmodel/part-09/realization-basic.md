---
declaration: module
origin: cited
lean: StandardModel.AlgebraRealization, StandardModel.AlgebraRealization.A, StandardModel.AlgebraRealization.H, StandardModel.AlgebraRealization.barH, StandardModel.AlgebraRealization.d, StandardModel.AlgebraRealization.bard, StandardModel.AlgebraRealization.u, StandardModel.AlgebraRealization.baru
statement: formalized
proof: formalized
---

# The algebra valued Standard model

The module `PhyslibAlpha.Particles.StandardModel.Realization.Basic`, [PhyslibAlpha/Particles/StandardModel/Realization/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Basic.lean): 40 declarations, 39 with a docstring; 2 private, not shown.

## i. Overview

> An algebra `B` carries a Standard Model when the fields of the Standard Model, and every
> polynomial expression in them, sit inside it compatibly with the gauge action, the Lorentz
> action and the mass-weight grading. The jet algebra `StandardModel.JetAlgebra` is the
> universal object with those fields, so the statement is a single one: an algebra map
> `JetAlgebra →ₐ[ℂ] B`, equivariant for the jet gauge group and the Lorentz group and
> compatible with `massWeightPoly`. That is the structure `AlgebraRealization`, together with
> the two demands that the group actions be multiplicative on the whole of `B` and not
> merely on the image of the map — the covariant derivative of a matter field needs them
> there.
>
> The thirteen families of derivative symbols are then derived: `h.A`, `h.H`, `h.barH` and
> the ten fermion families are the jet algebra's own families pushed along the map. Every
> transformation law, mass weight and commutation rule they satisfy is likewise the jet
> algebra's own fact pushed along the map. Section B does that transport once for each shape
> a law takes, and sections C to E prove the gauge laws, the Lorentz laws and the mass
> weights, one section per shape. They carry the names they carried when they were axioms,
> so they are used exactly as before.
>
> The statistics of the fields — the commutation and anticommutation laws of the thirteen
> families — are proved the same way in [`Commutations.lean`](realization-commutations.md). The
> covariant reduction, which rests on both, is [`CovariantDeriv.lean`](realization-covariantderiv.md):
> the Lorentz mixing of derivative slots, the field algebra, the covariant derivative towers,
> their gauge covariance and the classification of jet-gauge invariants.

## ii. Key results

> - `StandardModel.AlgebraRealization` : an algebra is a Standard Model when it receives an
>   equivariant algebra map from the jet algebra.
> - `AlgebraRealization.A`, `AlgebraRealization.H` and their companions : the thirteen families of
>   derivative symbols of a Standard Model.
> - `AlgebraRealization.gaugeRealization`, `AlgebraRealization.repLorentz_H`,
>   `AlgebraRealization.massWeight_d` and their companions : the transformation laws and mass
>   weights of those families.

## iv. References

> * None.

**`StandardModel.AlgebraRealization`**, a structure, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Basic.lean#L80).

> The algebra `B`, with a jet gauge action, a Lorentz action and a mass-weight grading,
> is a Standard Model when it receives an algebra map from the jet algebra of the Standard
> Model which is equivariant for both actions and compatible with the grading. The fields
> of the Standard Model then sit inside `B` as the images of the jet algebra's own, and
> every law they satisfy there is the jet algebra's own law pushed along the map.
>
> The last two fields are not consequences of the first four: an equivariant map forces the
> two actions to be multiplicative only on its image, whereas the covariant derivative of a
> matter field needs them multiplicative on the whole of `B`.

```lean
structure AlgebraRealization (B : Type) [Ring B] [Algebra ℂ B]
    (repJet : Representation ℂ JetGaugeGroupI B)
    (repLorentz : Representation ℂ SL(2,ℂ) B)
    (massWeightPoly : B →ₐ[ℂ] Polynomial B) where
  /-- The algebra map out of the jet algebra of the Standard Model: it is what places the
    fields of the Standard Model, and every polynomial expression in them, inside `B`. -/
  toAlgHom : JetAlgebra →ₐ[ℂ] B
  /-- The map is equivariant for the jet gauge group: the gauge action on `B` restricts
    along it to the jet algebra's own. -/
  map_repJet : ∀ (U : JetGaugeGroupI) (x : JetAlgebra),
    toAlgHom (JetAlgebra.repJetGaugeGroupI U x) = repJet U (toAlgHom x)
  /-- The map is equivariant for the Lorentz group: the Lorentz action on `B` restricts
    along it to the jet algebra's own. -/
  map_repLorentz : ∀ (Λ : SL(2,ℂ)) (x : JetAlgebra),
    toAlgHom (JetAlgebra.repLorentzGroup Λ x) = repLorentz Λ (toAlgHom x)
  /-- The map carries the mass-weight grading of the jet algebra to that of `B`: the
    mass-weight polynomial of an image is the image of the mass-weight polynomial. -/
  map_massWeight : ∀ x : JetAlgebra, massWeightPoly (toAlgHom x)
    = Polynomial.mapAlgHom toAlgHom (JetAlgebra.massWeightPoly x)
  /-- The jet gauge action preserves products on the whole of `B`, not merely on the image
    of the jet algebra: gauge transformations act by algebra endomorphisms. -/
  repJet_mul : ∀ (U : JetGaugeGroupI) (b₁ b₂ : B),
    repJet U (b₁ * b₂) = repJet U b₁ * repJet U b₂
  /-- Lorentz transformations act on `B` by algebra maps: the action preserves products, so
    each `repLorentz Λ` is an algebra endomorphism of `B`. -/
  repLorentz_mul : ∀ (Λ : SL(2,ℂ)) (b₁ b₂ : B),
    repLorentz Λ (b₁ * b₂) = repLorentz Λ b₁ * repLorentz Λ b₂
```

## A. The fields of a Standard Model

> The thirteen families of derivative symbols the theory is written in — the gauge field,
> the Higgs field and its conjugate, and the five fermion species in three generations with
> their conjugates — are no longer data of the structure. They are the corresponding
> families of the jet algebra, carried into `B` along the defining algebra map. The gauge
> family is real-linear in its value index, so the map is restricted to `ℝ` there.

**`StandardModel.AlgebraRealization.A`**, a def, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Basic.lean#L129).

> The derivative symbols `∂_s A_μ^ψ` of the gauge field inside `B`.

```lean
noncomputable def A (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) :
    Module.Dual ℝ GaugeAlgebra →ₗ[ℝ] B
```

**`StandardModel.AlgebraRealization.H`**, a def, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Basic.lean#L134).

> The derivative symbols `∂_s H_φ` of the Higgs field inside `B`.

```lean
noncomputable def H (s : Multiset (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ HiggsVec →ₗ[ℂ] B
```

**`StandardModel.AlgebraRealization.barH`**, a def, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Basic.lean#L139).

> The derivative symbols `∂_s H̄_φ` of the conjugate Higgs field inside `B`.

```lean
noncomputable def barH (s : Multiset (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ (ConjModule HiggsVec) →ₗ[ℂ] B
```

**`StandardModel.AlgebraRealization.d`**, a def, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Basic.lean#L144).

> The derivative symbols of the `i`-th generation down-type quark singlet inside `B`.

```lean
noncomputable def d (i : Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ DownSinglet →ₗ[ℂ] B
```

**`StandardModel.AlgebraRealization.bard`**, a def, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Basic.lean#L150).

> The derivative symbols of the `i`-th generation conjugate down-type quark singlet
> inside `B`.

```lean
noncomputable def bard (i : Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ (ConjModule DownSinglet) →ₗ[ℂ] B
```

**`StandardModel.AlgebraRealization.u`**, a def, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Basic.lean#L155).

> The derivative symbols of the `i`-th generation up-type quark singlet inside `B`.

```lean
noncomputable def u (i : Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ UpSinglet →ₗ[ℂ] B
```

**`StandardModel.AlgebraRealization.baru`**, a def, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Basic.lean#L161).

> The derivative symbols of the `i`-th generation conjugate up-type quark singlet
> inside `B`.

```lean
noncomputable def baru (i : Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ (ConjModule UpSinglet) →ₗ[ℂ] B
```

**`StandardModel.AlgebraRealization.Q`**, a def, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Basic.lean#L166).

> The derivative symbols of the `i`-th generation quark doublet inside `B`.

```lean
noncomputable def Q (i : Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ QuarkDoublet →ₗ[ℂ] B
```

**`StandardModel.AlgebraRealization.barQ`**, a def, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Basic.lean#L171).

> The derivative symbols of the `i`-th generation conjugate quark doublet inside `B`.

```lean
noncomputable def barQ (i : Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ (ConjModule QuarkDoublet) →ₗ[ℂ] B
```

**`StandardModel.AlgebraRealization.L`**, a def, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Basic.lean#L176).

> The derivative symbols of the `i`-th generation lepton doublet inside `B`.

```lean
noncomputable def L (i : Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ LeptonDoubletV →ₗ[ℂ] B
```

**`StandardModel.AlgebraRealization.barL`**, a def, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Basic.lean#L181).

> The derivative symbols of the `i`-th generation conjugate lepton doublet inside `B`.

```lean
noncomputable def barL (i : Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ (ConjModule LeptonDoubletV) →ₗ[ℂ] B
```

**`StandardModel.AlgebraRealization.e`**, a def, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Basic.lean#L186).

> The derivative symbols of the `i`-th generation charged-lepton singlet inside `B`.

```lean
noncomputable def e (i : Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ LeptonSinglet →ₗ[ℂ] B
```

**`StandardModel.AlgebraRealization.bare`**, a def, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Basic.lean#L192).

> The derivative symbols of the `i`-th generation conjugate charged-lepton singlet
> inside `B`.

```lean
noncomputable def bare (i : Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ (ConjModule LeptonSinglet) →ₗ[ℂ] B
```

## B. Transporting a fact along the defining map

> Every law the old structure demanded as an axiom is now a theorem, proved once for the jet
> algebra and transported along `toAlgHom`. The transport is the same in each of the shapes
> the laws take, so each shape is done once. The three shapes used here are a Leibniz
> convolution for the gauge action, a slot-mixing sum for the Lorentz action and a monomial
> eigenvalue equation for the mass weights; the anticommutation shape is transported in
> [`Commutations.lean`](realization-commutations.md), beside the laws that use it.

## C. The gauge transformation of the fields

> The gauge field is a gauge field — Lorentz covector symbols, the all-orders adjoint
> Leibniz convolution with the Maurer–Cartan shift, and a multiplicative gauge action — and
> each of the twelve matter families transforms in its own jet gauge representation, the
> barred families in the conjugate of it.

**`StandardModel.AlgebraRealization.gaugeRealization`**, a def, [line 250](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Basic.lean#L250).

> The gauge-boson part of a Standard Model: the realization of the gauge-boson jet
> algebra in `B` through the gauge sector of the jet algebra.

```lean
noncomputable def gaugeRealization :
    GaugeAlgebraRealization localGaugeData B repJet repLorentz
```

**`StandardModel.AlgebraRealization.gaugeRealization_A`**, a lemma, [line 264](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Basic.lean#L264).

```lean
lemma gaugeRealization_A : h.gaugeRealization.A = h.A
```

**`StandardModel.AlgebraRealization.repJet_H`**, a lemma, [line 268](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Basic.lean#L268).

> The law `repJet_H` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma repJet_H : LocalGaugeData.TransformsIn repJet HiggsVec.repJetGaugeGroupI h.H
```

**`StandardModel.AlgebraRealization.repJet_barH`**, a lemma, [line 273](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Basic.lean#L273).

> The law `repJet_barH` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma repJet_barH :
    LocalGaugeData.TransformsIn repJet (JetComponentSpace.repConj HiggsVec.repJetGaugeGroupI)
      h.barH
```

**`StandardModel.AlgebraRealization.repJet_d`**, a lemma, [line 280](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Basic.lean#L280).

> The law `repJet_d` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma repJet_d : ∀ i, LocalGaugeData.TransformsIn repJet DownSinglet.repJetGaugeGroupI (h.d i)
```

**`StandardModel.AlgebraRealization.repJet_bard`**, a lemma, [line 285](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Basic.lean#L285).

> The law `repJet_bard` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma repJet_bard : ∀ i,
    LocalGaugeData.TransformsIn repJet (JetComponentSpace.repConj DownSinglet.repJetGaugeGroupI)
      (h.bard i)
```

**`StandardModel.AlgebraRealization.repJet_u`**, a lemma, [line 292](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Basic.lean#L292).

> The law `repJet_u` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma repJet_u : ∀ i, LocalGaugeData.TransformsIn repJet UpSinglet.repJetGaugeGroupI (h.u i)
```

**`StandardModel.AlgebraRealization.repJet_baru`**, a lemma, [line 297](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Basic.lean#L297).

> The law `repJet_baru` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma repJet_baru : ∀ i,
    LocalGaugeData.TransformsIn repJet (JetComponentSpace.repConj UpSinglet.repJetGaugeGroupI)
      (h.baru i)
```

**`StandardModel.AlgebraRealization.repJet_Q`**, a lemma, [line 304](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Basic.lean#L304).

> The law `repJet_Q` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma repJet_Q : ∀ i, LocalGaugeData.TransformsIn repJet QuarkDoublet.repJetGaugeGroupI (h.Q i)
```

**`StandardModel.AlgebraRealization.repJet_barQ`**, a lemma, [line 309](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Basic.lean#L309).

> The law `repJet_barQ` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma repJet_barQ : ∀ i,
    LocalGaugeData.TransformsIn repJet (JetComponentSpace.repConj QuarkDoublet.repJetGaugeGroupI)
      (h.barQ i)
```

**`StandardModel.AlgebraRealization.repJet_L`**, a lemma, [line 316](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Basic.lean#L316).

> The law `repJet_L` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma repJet_L : ∀ i, LocalGaugeData.TransformsIn repJet LeptonDoubletV.repJetGaugeGroupI (h.L i)
```

**`StandardModel.AlgebraRealization.repJet_barL`**, a lemma, [line 321](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Basic.lean#L321).

> The law `repJet_barL` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma repJet_barL : ∀ i,
    LocalGaugeData.TransformsIn repJet (JetComponentSpace.repConj LeptonDoubletV.repJetGaugeGroupI)
      (h.barL i)
```

**`StandardModel.AlgebraRealization.repJet_e`**, a lemma, [line 328](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Basic.lean#L328).

> The law `repJet_e` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma repJet_e : ∀ i, LocalGaugeData.TransformsIn repJet LeptonSinglet.repJetGaugeGroupI (h.e i)
```

**`StandardModel.AlgebraRealization.repJet_bare`**, a lemma, [line 333](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Basic.lean#L333).

> The law `repJet_bare` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma repJet_bare : ∀ i,
    LocalGaugeData.TransformsIn repJet (JetComponentSpace.repConj LeptonSinglet.repJetGaugeGroupI)
      (h.bare i)
```

## D. The Lorentz transformation of the fields

> The derivative slots of every field mix by per-slot Lorentz matrices, and the value index
> by the contragredient of the species' Lorentz representation: the Higgs is a scalar, the
> fermions are Weyl spinors, and the barred fields carry the conjugate representations.

**`StandardModel.AlgebraRealization.repLorentz_H`**, a lemma, [line 350](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Basic.lean#L350).

> The law `repLorentz_H` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma repLorentz_H : IsLorentzDerivTransforms repLorentz
    (Representation.trivial ℂ SL(2,ℂ) HiggsVec) h.H
```

**`StandardModel.AlgebraRealization.repLorentz_barH`**, a lemma, [line 356](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Basic.lean#L356).

> The law `repLorentz_barH` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma repLorentz_barH : IsLorentzDerivTransforms repLorentz
    (Representation.trivial ℂ SL(2,ℂ) HiggsVec).conj h.barH
```

**`StandardModel.AlgebraRealization.repLorentz_d`**, a lemma, [line 362](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Basic.lean#L362).

> The law `repLorentz_d` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma repLorentz_d : ∀ i, IsLorentzDerivTransforms repLorentz
    DownSinglet.repLorentzGroup (h.d i)
```

**`StandardModel.AlgebraRealization.repLorentz_bard`**, a lemma, [line 368](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Basic.lean#L368).

> The law `repLorentz_bard` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma repLorentz_bard : ∀ i, IsLorentzDerivTransforms repLorentz
    DownSinglet.repLorentzGroup.conj (h.bard i)
```

**`StandardModel.AlgebraRealization.repLorentz_u`**, a lemma, [line 374](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Basic.lean#L374).

> The law `repLorentz_u` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma repLorentz_u : ∀ i, IsLorentzDerivTransforms repLorentz
    UpSinglet.repLorentzGroup (h.u i)
```

**`StandardModel.AlgebraRealization.repLorentz_baru`**, a lemma, [line 380](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Basic.lean#L380).

> The law `repLorentz_baru` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma repLorentz_baru : ∀ i, IsLorentzDerivTransforms repLorentz
    UpSinglet.repLorentzGroup.conj (h.baru i)
```

**`StandardModel.AlgebraRealization.repLorentz_Q`**, a lemma, [line 386](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Basic.lean#L386).

> The law `repLorentz_Q` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma repLorentz_Q : ∀ i, IsLorentzDerivTransforms repLorentz
    QuarkDoublet.repLorentzGroup (h.Q i)
```

**`StandardModel.AlgebraRealization.repLorentz_barQ`**, a lemma, [line 392](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Basic.lean#L392).

> The law `repLorentz_barQ` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma repLorentz_barQ : ∀ i, IsLorentzDerivTransforms repLorentz
    QuarkDoublet.repLorentzGroup.conj (h.barQ i)
```

**`StandardModel.AlgebraRealization.repLorentz_L`**, a lemma, [line 398](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Basic.lean#L398).

> The law `repLorentz_L` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma repLorentz_L : ∀ i, IsLorentzDerivTransforms repLorentz
    LeptonDoubletV.repLorentzGroup (h.L i)
```

**`StandardModel.AlgebraRealization.repLorentz_barL`**, a lemma, [line 404](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Basic.lean#L404).

> The law `repLorentz_barL` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma repLorentz_barL : ∀ i, IsLorentzDerivTransforms repLorentz
    LeptonDoubletV.repLorentzGroup.conj (h.barL i)
```

**`StandardModel.AlgebraRealization.repLorentz_e`**, a lemma, [line 410](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Basic.lean#L410).

> The law `repLorentz_e` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma repLorentz_e : ∀ i, IsLorentzDerivTransforms repLorentz
    LeptonSinglet.repLorentzGroup (h.e i)
```

**`StandardModel.AlgebraRealization.repLorentz_bare`**, a lemma, [line 416](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Basic.lean#L416).

> The law `repLorentz_bare` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma repLorentz_bare : ∀ i, IsLorentzDerivTransforms repLorentz
    LeptonSinglet.repLorentzGroup.conj (h.bare i)
```

## Depends on

- [The mass-weight polynomial on the jet algebra of the Standard Model](../part-08/jetalgebra-massweightpoly.md)

## Proof depends on

- [The transformation laws of the field symbols of the jet algebra](../part-08/jetalgebra-transformsin.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Realization/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Basic.lean)
