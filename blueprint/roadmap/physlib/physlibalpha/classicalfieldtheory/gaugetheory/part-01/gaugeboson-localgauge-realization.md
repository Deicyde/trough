---
declaration: module
origin: cited
lean: LocalGaugeFieldAlgebra.Realization, LocalGaugeFieldAlgebra.Realization.id, LocalGaugeFieldAlgebra.Realization.id_toAlgHom, LocalGaugeFieldAlgebra.Realization.map_repJet, LocalGaugeFieldAlgebra.Realization.map_repLorentz, LocalGaugeFieldAlgebra.Realization.repJet_mul, LocalGaugeFieldAlgebra.Realization.repLorentz_mul, LocalGaugeFieldAlgebra.Realization.A
statement: formalized
proof: formalized
---

# Realizations of the local gauge field algebra

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GaugeBoson.LocalGauge.Realization`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/Realization.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/Realization.lean): 24 declarations, 14 with a docstring.

## i. Overview

> A real algebra `B` carries the gauge bosons when the local gauge field algebra maps into it
> by a real algebra map equivariant for the jet gauge group and the Lorentz group, both acting
> on `B` by algebra endomorphisms: `LocalGaugeFieldAlgebra.Realization`. The derivative
> symbols of `B` are the images of the algebra's own symbols `∂_s A_μ^φ` (`Realization.A`);
> no derivative operator on `B` is involved.
>
> `GaugeAlgebraRealization` is the same notion with complex scalars, out of the
> complexification `ℂ ⊗[ℝ] LocalGaugeFieldAlgebra 𝔤`. For a complex target the two agree by
> the universal property of base change `AlgHom.liftEquiv` (section D); the real algebra is
> never identified with its complexification.

## ii. Key results

> - `LocalGaugeFieldAlgebra.Realization` : an algebra carrying the gauge bosons over `ℝ`.
> - `LocalGaugeFieldAlgebra.Realization.A` : the derivative symbols of a realization, with the
>   laws `gauge_apply_deriv` and `lorentz_apply` and the extensionality `ext_A`.
> - `LocalGaugeFieldAlgebra.Realization.toAlgHom_covDerivFieldStrength` : the map carries the
>   covariant derivatives of the field strength to those of the symbols of `B`.
> - `LocalGaugeFieldAlgebra.Realization.equivGaugeAlgebraRealization` : for a complex target,
>   real realizations are the complex realizations.

## iv. References

> * None.

## A. Realizations

**`LocalGaugeFieldAlgebra.Realization`**, an abbrev, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/Realization.lean#L73).

> A real algebra `B` carrying the gauge bosons of the package `jets`: a real algebra map
> out of the local gauge field algebra, equivariant for the jet gauge group and the Lorentz
> group, both acting on the whole of `B` by algebra endomorphisms. It is built from the
> fields `toAlgHom`, `map_fst`, `map_snd`, `fst_mul`, `snd_mul` of
> `Representation.EquivariantAlgHom`, which the lemmas `map_repJet`, `map_repLorentz`,
> `repJet_mul` and `repLorentz_mul` name.

```lean
abbrev Realization (jets : LocalGaugeData G₀ 𝔤 GJ 𝔤J) (B : Type) [Ring B] [Algebra ℝ B]
    (repJet : Representation ℝ GJ B) (repLorentz : Representation ℝ SL(2,ℂ) B)
```

**`LocalGaugeFieldAlgebra.Realization.id`**, a def, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/Realization.lean#L87).

> The local gauge field algebra realized in itself, by the identity.

```lean
noncomputable def id : Realization jets (LocalGaugeFieldAlgebra 𝔤)
    (LocalGaugeFieldAlgebra.repJet jets) (repLorentzGroup 𝔤)
```

**`LocalGaugeFieldAlgebra.Realization.id_toAlgHom`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/Realization.lean#L93).

```lean
lemma id_toAlgHom : (id jets).toAlgHom = AlgHom.id ℝ (LocalGaugeFieldAlgebra 𝔤)
```

**`LocalGaugeFieldAlgebra.Realization.map_repJet`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/Realization.lean#L99).

> The map is equivariant for the jet gauge group.

```lean
lemma map_repJet (U : GJ) (x : LocalGaugeFieldAlgebra 𝔤) :
    h.toAlgHom (LocalGaugeFieldAlgebra.repJet jets U x) = repJet U (h.toAlgHom x)
```

**`LocalGaugeFieldAlgebra.Realization.map_repLorentz`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/Realization.lean#L105).

> The map is equivariant for the Lorentz group.

```lean
lemma map_repLorentz (Λ : SL(2,ℂ)) (x : LocalGaugeFieldAlgebra 𝔤) :
    h.toAlgHom (LocalGaugeFieldAlgebra.repLorentzGroup 𝔤 Λ x) = repLorentz Λ (h.toAlgHom x)
```

**`LocalGaugeFieldAlgebra.Realization.repJet_mul`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/Realization.lean#L112).

> The jet gauge group acts on the whole of `B` by algebra endomorphisms.

```lean
lemma repJet_mul (U : GJ) (b₁ b₂ : B) : repJet U (b₁ * b₂) = repJet U b₁ * repJet U b₂
```

**`LocalGaugeFieldAlgebra.Realization.repLorentz_mul`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/Realization.lean#L118).

> The Lorentz group acts on the whole of `B` by algebra endomorphisms.

```lean
lemma repLorentz_mul (Λ : SL(2,ℂ)) (b₁ b₂ : B) :
    repLorentz Λ (b₁ * b₂) = repLorentz Λ b₁ * repLorentz Λ b₂
```

## B. The derivative symbols of a realization

**`LocalGaugeFieldAlgebra.Realization.A`**, a def, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/Realization.lean#L130).

> The derivative symbols `∂_s A_μ^φ` of a realization: the images of the algebra's own
> symbols `derivA`.

```lean
noncomputable def A (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) :
    Module.Dual ℝ 𝔤 →ₗ[ℝ] B
```

**`LocalGaugeFieldAlgebra.Realization.A_apply`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/Realization.lean#L135).

```lean
lemma A_apply (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ 𝔤) :
    h.A s μ φ = h.toAlgHom (derivA 𝔤 s μ φ)
```

**`LocalGaugeFieldAlgebra.Realization.id_A`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/Realization.lean#L140).

```lean
lemma id_A : (id jets).A = derivA 𝔤
```

**`LocalGaugeFieldAlgebra.Realization.commute_A`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/Realization.lean#L143).

```lean
lemma commute_A (p q : Multiset (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3)
    (φ ψ : Module.Dual ℝ 𝔤) : Commute (h.A p μ φ) (h.A q ν ψ)
```

**`LocalGaugeFieldAlgebra.Realization.ext_A`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/Realization.lean#L149).

> Two realizations with the same derivative symbols are equal.

```lean
lemma ext_A {h₁ h₂ : Realization jets B repJet repLorentz}
    (hA : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ 𝔤),
      h₁.A s μ φ = h₂.A s μ φ) : h₁ = h₂
```

**`LocalGaugeFieldAlgebra.Realization.gauge_apply_deriv`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/Realization.lean#L158).

> The gauge law: a jet `U` acts on `∂_s A_μ^φ` by the Leibniz convolution of the dual
> adjoint Taylor coefficients of `U⁻¹` against lower symbols, plus the base-point value of
> the `s`-th derivative of the Maurer–Cartan form of `U⁻¹`.

```lean
lemma gauge_apply_deriv (U : GJ) (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ 𝔤) :
    repJet U (h.A s μ φ) =
      (s.antidiagonal.map fun p => h.A p.2 μ (jets.adjointDualCoeff U⁻¹ p.1 φ)).sum
      + algebraMap ℝ B (φ (jets.evalLie (jets.iteratedDeriv s (jets.maurerCartan U⁻¹ μ))))
```

**`LocalGaugeFieldAlgebra.Realization.lorentz_apply`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/Realization.lean#L169).

> The Lorentz law: the symbol carries one covector index, and each derivative slot
> transforms as a covector.

```lean
lemma lorentz_apply (Λ : SL(2,ℂ)) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ 𝔤) :
    repLorentz Λ (h.A (List.ofFn l) μ φ) =
      ∑ p : Fin n → (Fin 1 ⊕ Fin 3), (∏ i, ((SL2C.toLorentzGroup Λ).1 (p i) (l i) : ℝ)) •
        ∑ a, ((SL2C.toLorentzGroup Λ).1 a μ : ℝ) • h.A (List.ofFn p) a φ
```

## C. The field strength of a realization

**`LocalGaugeFieldAlgebra.Realization.toAlgHom_covDerivFieldStrength`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/Realization.lean#L187).

> The map of a realization carries the covariant derivatives of the field strength to
> those of its symbols.

```lean
lemma toAlgHom_covDerivFieldStrength (l : List (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ 𝔤) :
    h.toAlgHom (covDerivFieldStrength 𝔤 l μ ν φ)
      = GaugeAlgebraRealization.iteratedCovDerivAdjoint h.A l
        (GaugeAlgebraRealization.fieldStrength h.A μ ν) 0 φ
```

**`LocalGaugeFieldAlgebra.Realization.toAlgHom_fieldStrength`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/Realization.lean#L202).

```lean
lemma toAlgHom_fieldStrength (μ ν : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ 𝔤) :
    h.toAlgHom (fieldStrength 𝔤 μ ν φ) = GaugeAlgebraRealization.fieldStrength h.A μ ν 0 φ
```

## D. Comparison with the complex realizations

**`LocalGaugeFieldAlgebra.Realization.toGaugeAlgebraRealization`**, a def, [line 221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/Realization.lean#L221).

> The complexification of a real realization in a complex algebra, by `AlgHom.liftEquiv`;
> the symbols are unchanged.

```lean
noncomputable def toGaugeAlgebraRealization
    (h : Realization jets B (repJet.restrictScalars ℝ) (repLorentz.restrictScalars ℝ)) :
    GaugeAlgebraRealization jets B repJet repLorentz
```

**`LocalGaugeFieldAlgebra.Realization.toGaugeAlgebraRealization_A`**, a lemma, [line 238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/Realization.lean#L238).

```lean
lemma toGaugeAlgebraRealization_A
    (h : Realization jets B (repJet.restrictScalars ℝ) (repLorentz.restrictScalars ℝ)) :
    h.toGaugeAlgebraRealization.A = h.A
```

**`LocalGaugeFieldAlgebra.Realization.toGaugeAlgebraRealization_toAlgHom_one_tmul`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/Realization.lean#L243).

```lean
lemma toGaugeAlgebraRealization_toAlgHom_one_tmul
    (h : Realization jets B (repJet.restrictScalars ℝ) (repLorentz.restrictScalars ℝ))
    (x : LocalGaugeFieldAlgebra 𝔤) :
    h.toGaugeAlgebraRealization.toAlgHom ((1 : ℂ) ⊗ₜ[ℝ] x) = h.toAlgHom x
```

**`GaugeAlgebraRealization.toRealization`**, a def, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/Realization.lean#L251).

> The restriction of scalars of a complex realization: the algebra map precomposed with
> `x ↦ 1 ⊗ₜ x`.

```lean
noncomputable def _root_.GaugeAlgebraRealization.toRealization
    (h : GaugeAlgebraRealization jets B repJet repLorentz) :
    Realization jets B (repJet.restrictScalars ℝ) (repLorentz.restrictScalars ℝ)
```

**`GaugeAlgebraRealization.toRealization_toAlgHom_apply`**, a lemma, [line 268](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/Realization.lean#L268).

```lean
lemma _root_.GaugeAlgebraRealization.toRealization_toAlgHom_apply
    (h : GaugeAlgebraRealization jets B repJet repLorentz) (x : LocalGaugeFieldAlgebra 𝔤) :
    h.toRealization.toAlgHom x = h.toAlgHom ((1 : ℂ) ⊗ₜ[ℝ] x)
```

**`GaugeAlgebraRealization.toRealization_A`**, a lemma, [line 274](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/Realization.lean#L274).

```lean
lemma _root_.GaugeAlgebraRealization.toRealization_A
    (h : GaugeAlgebraRealization jets B repJet repLorentz) : h.toRealization.A = h.A
```

**`GaugeAlgebraRealization.toRealization_id_toAlgHom`**, a lemma, [line 282](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/Realization.lean#L282).

```lean
lemma _root_.GaugeAlgebraRealization.toRealization_id_toAlgHom :
    (GaugeAlgebraRealization.id jets).toRealization.toAlgHom
      = (Algebra.TensorProduct.includeRight :
          LocalGaugeFieldAlgebra 𝔤 →ₐ[ℝ] ℂ ⊗[ℝ] LocalGaugeFieldAlgebra 𝔤)
```

**`LocalGaugeFieldAlgebra.Realization.equivGaugeAlgebraRealization`**, a def, [line 289](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/Realization.lean#L289).

> For a complex target, real realizations are the complex realizations.

```lean
noncomputable def equivGaugeAlgebraRealization :
    Realization jets B (repJet.restrictScalars ℝ) (repLorentz.restrictScalars ℝ)
      ≃ GaugeAlgebraRealization jets B repJet repLorentz
```

## Depends on

- [The field strength in the local gauge field algebra](gaugeboson-localgauge-fieldstrength.md)
- [Representations acting by algebra maps](../../../mathematics/part-01/algebrarepresentation.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/Realization.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/Realization.lean)
