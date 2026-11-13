---
declaration: module
origin: cited
lean: LocalGaugeCovFieldAlgebra.Realization, LocalGaugeCovFieldAlgebra.Realization.id, LocalGaugeCovFieldAlgebra.Realization.id_toAlgHom, LocalGaugeCovFieldAlgebra.Realization.map_repValue, LocalGaugeCovFieldAlgebra.Realization.map_repLorentz, LocalGaugeCovFieldAlgebra.Realization.repGauge_mul, LocalGaugeCovFieldAlgebra.Realization.repLorentz_mul, LocalGaugeCovFieldAlgebra.Realization.F
statement: formalized
proof: formalized
---

# Realizations of the covariant field algebra (LocalGaugeCov/Realization)

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GaugeBoson.LocalGaugeCov.Realization`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeCov/Realization.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeCov/Realization.lean): 24 declarations, 14 with a docstring.

## i. Overview

> A real algebra `B` carries the covariant gauge-boson tower when the covariant field algebra
> maps into it by a real algebra map equivariant for the ordinary gauge group `G₀` (acting on
> the source by `repValue`) and for the Lorentz group, both acting on `B` by algebra
> endomorphisms: `LocalGaugeCovFieldAlgebra.Realization`. The gauge compatibility is with `G₀`
> alone because the jet action on the covariant field algebra factors through evaluation.
>
> The covariant field algebra is not free on its generators, so a realization is its algebra
> map and not an assignment of the generators; generation gives uniqueness only
> (`Realization.ext_F`). A realization of the local gauge field algebra restricts to one of
> the covariant field algebra (`LocalGaugeFieldAlgebra.Realization.restrict`), with `G₀`
> acting on the target through the constant jets. The converse extension is not claimed.

## ii. Key results

> - `LocalGaugeCovFieldAlgebra.Realization` : an algebra carrying the covariant tower.
> - `LocalGaugeCovFieldAlgebra.Realization.F` : the covariant tower of a realization, with the
>   laws `gauge_F` and `lorentz_F` and the extensionality `ext_F`.
> - `LocalGaugeFieldAlgebra.Realization.restrict` : restriction to the covariant field
>   algebra, with `restrict_F_eq_iteratedCovDerivAdjoint` identifying its tower.

## iv. References

> * None.

## A. Realizations

**`LocalGaugeCovFieldAlgebra.Realization`**, an abbrev, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeCov/Realization.lean#L72).

> A real algebra `B` carrying the covariant gauge-boson tower of the package `jets`: a
> real algebra map out of the covariant field algebra, equivariant for the ordinary gauge
> group and the Lorentz group, both acting on the whole of `B` by algebra endomorphisms. It
> is built from the fields `toAlgHom`, `map_fst`, `map_snd`, `fst_mul`, `snd_mul` of
> `Representation.EquivariantAlgHom`, which the lemmas `map_repValue`, `map_repLorentz`,
> `repGauge_mul` and `repLorentz_mul` name.

```lean
abbrev Realization (jets : LocalGaugeData G₀ 𝔤 GJ 𝔤J) (B : Type) [Ring B] [Algebra ℝ B]
    (repGauge : Representation ℝ G₀ B) (repLorentz : Representation ℝ SL(2,ℂ) B)
```

**`LocalGaugeCovFieldAlgebra.Realization.id`**, a def, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeCov/Realization.lean#L83).

> The covariant field algebra realized in itself, by the identity.

```lean
noncomputable def id : Realization jets (LocalGaugeCovFieldAlgebra 𝔤) (repValue jets)
    (repLorentzGroup 𝔤)
```

**`LocalGaugeCovFieldAlgebra.Realization.id_toAlgHom`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeCov/Realization.lean#L88).

```lean
lemma id_toAlgHom : (id jets).toAlgHom = AlgHom.id ℝ (LocalGaugeCovFieldAlgebra 𝔤)
```

**`LocalGaugeCovFieldAlgebra.Realization.map_repValue`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeCov/Realization.lean#L93).

> The map is equivariant for the ordinary gauge group.

```lean
lemma map_repValue (g : G₀) (x : LocalGaugeCovFieldAlgebra 𝔤) :
    k.toAlgHom (repValue jets g x) = repGauge g (k.toAlgHom x)
```

**`LocalGaugeCovFieldAlgebra.Realization.map_repLorentz`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeCov/Realization.lean#L98).

> The map is equivariant for the Lorentz group.

```lean
lemma map_repLorentz (Λ : SL(2,ℂ)) (x : LocalGaugeCovFieldAlgebra 𝔤) :
    k.toAlgHom (repLorentzGroup 𝔤 Λ x) = repLorentz Λ (k.toAlgHom x)
```

**`LocalGaugeCovFieldAlgebra.Realization.repGauge_mul`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeCov/Realization.lean#L104).

> The ordinary gauge group acts on the whole of `B` by algebra endomorphisms.

```lean
lemma repGauge_mul (g : G₀) (b₁ b₂ : B) :
    repGauge g (b₁ * b₂) = repGauge g b₁ * repGauge g b₂
```

**`LocalGaugeCovFieldAlgebra.Realization.repLorentz_mul`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeCov/Realization.lean#L110).

> The Lorentz group acts on the whole of `B` by algebra endomorphisms.

```lean
lemma repLorentz_mul (Λ : SL(2,ℂ)) (b₁ b₂ : B) :
    repLorentz Λ (b₁ * b₂) = repLorentz Λ b₁ * repLorentz Λ b₂
```

## B. The covariant tower of a realization

**`LocalGaugeCovFieldAlgebra.Realization.F`**, a def, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeCov/Realization.lean#L122).

> The covariant tower `∇_l F_μν^φ` of a realization: the images of the generators of the
> covariant field algebra.

```lean
noncomputable def F (l : List (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3) :
    Module.Dual ℝ 𝔤 →ₗ[ℝ] B
```

**`LocalGaugeCovFieldAlgebra.Realization.F_apply`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeCov/Realization.lean#L126).

```lean
lemma F_apply (l : List (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ 𝔤) :
    k.F l μ ν φ = k.toAlgHom (covF 𝔤 l μ ν φ)
```

**`LocalGaugeCovFieldAlgebra.Realization.id_F`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeCov/Realization.lean#L130).

```lean
lemma id_F : (id jets).F = covF 𝔤
```

**`LocalGaugeCovFieldAlgebra.Realization.F_nil`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeCov/Realization.lean#L132).

```lean
lemma F_nil (μ ν : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ 𝔤) :
    k.F [] μ ν φ = k.toAlgHom ⟨fieldStrength 𝔤 μ ν φ, fieldStrength_mem μ ν φ⟩
```

**`LocalGaugeCovFieldAlgebra.Realization.commute_F`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeCov/Realization.lean#L135).

```lean
lemma commute_F (l l' : List (Fin 1 ⊕ Fin 3)) (μ ν μ' ν' : Fin 1 ⊕ Fin 3)
    (φ ψ : Module.Dual ℝ 𝔤) : Commute (k.F l μ ν φ) (k.F l' μ' ν' ψ)
```

**`LocalGaugeCovFieldAlgebra.Realization.ext_F`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeCov/Realization.lean#L141).

> Two realizations with the same covariant tower are equal. This is uniqueness only: a
> tower in `B` need not come from a realization.

```lean
lemma ext_F {k₁ k₂ : Realization jets B repGauge repLorentz}
    (hF : ∀ (l : List (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ 𝔤),
      k₁.F l μ ν φ = k₂.F l μ ν φ) : k₁ = k₂
```

**`LocalGaugeCovFieldAlgebra.Realization.gauge_F`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeCov/Realization.lean#L148).

> The gauge law of the covariant tower: the adjoint index rotates through the dual
> adjoint action of the inverse.

```lean
lemma gauge_F (g : G₀) (l : List (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ 𝔤) :
    repGauge g (k.F l μ ν φ) = k.F l μ ν ((jets.adjoint g⁻¹).dualMap φ)
```

**`LocalGaugeCovFieldAlgebra.Realization.lorentz_F`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeCov/Realization.lean#L156).

> The Lorentz law of the covariant tower: every covariant slot and both covector indices
> mix by the columns of the Lorentz matrix.

```lean
lemma lorentz_F (Λ : SL(2,ℂ)) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ 𝔤) :
    repLorentz Λ (k.F (List.ofFn l) μ ν φ)
      = ∑ p : Fin n → (Fin 1 ⊕ Fin 3), (∏ i, ((SL2C.toLorentzGroup Λ).1 (p i) (l i) : ℝ)) •
          ∑ a, ((SL2C.toLorentzGroup Λ).1 a μ : ℝ) • ∑ b, ((SL2C.toLorentzGroup Λ).1 b ν : ℝ) •
            k.F (List.ofFn p) a b φ
```

**`LocalGaugeCovFieldAlgebra.Realization.map_repJet`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeCov/Realization.lean#L171).

> A covariant realization intertwines the jet action with the `G₀` action at the value
> of the jet.

```lean
lemma map_repJet (U : GJ) (x : LocalGaugeCovFieldAlgebra 𝔤) :
    k.toAlgHom (repJet jets U x) = repGauge (jets.eval U) (k.toAlgHom x)
```

## C. Restriction from the local gauge field algebra

**`LocalGaugeFieldAlgebra.Realization.restrict`**, a def, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeCov/Realization.lean#L193).

> The restriction of a realization of the local gauge field algebra to the covariant
> field algebra, along the inclusion; the ordinary gauge group acts on the target as the
> constant jets.

```lean
noncomputable def restrict :
    LocalGaugeCovFieldAlgebra.Realization jets B (repJet.comp jets.ofConstant) repLorentz
```

**`LocalGaugeFieldAlgebra.Realization.restrict_toAlgHom_apply`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeCov/Realization.lean#L200).

```lean
lemma restrict_toAlgHom_apply (x : LocalGaugeCovFieldAlgebra 𝔤) :
    h.restrict.toAlgHom x = h.toAlgHom x
```

**`LocalGaugeFieldAlgebra.Realization.restrict_id_toAlgHom`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeCov/Realization.lean#L203).

```lean
lemma restrict_id_toAlgHom :
    (id jets).restrict.toAlgHom = (LocalGaugeCovFieldAlgebra 𝔤).val
```

**`LocalGaugeFieldAlgebra.Realization.restrict_F`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeCov/Realization.lean#L207).

```lean
lemma restrict_F (l : List (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ 𝔤) :
    h.restrict.F l μ ν φ = h.toAlgHom (covDerivFieldStrength 𝔤 l μ ν φ)
```

**`LocalGaugeFieldAlgebra.Realization.restrict_F_eq_iteratedCovDerivAdjoint`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeCov/Realization.lean#L211).

> The covariant tower of a restriction is the covariant tower of the symbols of `B`.

```lean
lemma restrict_F_eq_iteratedCovDerivAdjoint (l : List (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ 𝔤) :
    h.restrict.F l μ ν φ = GaugeAlgebraRealization.iteratedCovDerivAdjoint h.A l
      (GaugeAlgebraRealization.fieldStrength h.A μ ν) 0 φ
```

**`LocalGaugeFieldAlgebra.Realization.restrict_F_nil`**, a lemma, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeCov/Realization.lean#L217).

```lean
lemma restrict_F_nil (μ ν : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ 𝔤) :
    h.restrict.F [] μ ν φ = GaugeAlgebraRealization.fieldStrength h.A μ ν 0 φ
```

**`LocalGaugeFieldAlgebra.Realization.restrict_map_repJet`**, a lemma, [line 221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeCov/Realization.lean#L221).

```lean
lemma restrict_map_repJet (U : GJ) (x : LocalGaugeCovFieldAlgebra 𝔤) :
    h.restrict.toAlgHom (LocalGaugeCovFieldAlgebra.repJet jets U x)
      = repJet U (h.restrict.toAlgHom x)
```

**`LocalGaugeFieldAlgebra.Realization.repJet_restrict_toAlgHom`**, a lemma, [line 228](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeCov/Realization.lean#L228).

> On the image of the covariant field algebra a jet acts as the constant jet of its
> value; nothing is assumed about the jet action elsewhere in `B`.

```lean
lemma repJet_restrict_toAlgHom (U : GJ) (x : LocalGaugeCovFieldAlgebra 𝔤) :
    repJet U (h.restrict.toAlgHom x)
      = repJet (jets.ofConstant (jets.eval U)) (h.restrict.toAlgHom x)
```

## Depends on

- [Realizations of the local gauge field algebra](gaugeboson-localgauge-realization.md)
- [The covariant field algebra of the gauge bosons](gaugeboson-localgaugecov-basic.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeCov/Realization.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeCov/Realization.lean)
