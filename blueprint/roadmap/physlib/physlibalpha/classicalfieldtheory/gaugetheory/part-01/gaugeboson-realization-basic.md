---
declaration: module
origin: cited
lean: GaugeAlgebraRealization, GaugeAlgebraRealization.id, GaugeAlgebraRealization.A_apply, GaugeAlgebraRealization.id_A, GaugeAlgebraRealization.ext, GaugeAlgebraRealization.commute_A, GaugeAlgebraRealization.lorentz_apply, GaugeAlgebraRealization.gauge_apply_deriv
statement: formalized
proof: formalized
---

# Realizations of the gauge-boson jet algebra

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GaugeBoson.Realization.Basic`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/Basic.lean): 8 declarations, 6 with a docstring.

## i. Overview

> An algebra `B` carries the gauge bosons of a gauge theory when the gauge-boson jet algebra,
> the universal algebra on the symbols `∂_s A_μ^φ`, maps into it compatibly with the actions
> of the jet gauge group and of the Lorentz group. That is the structure
> `GaugeAlgebraRealization`: an algebra map `ℂ ⊗[ℝ] LocalGaugeFieldAlgebra 𝔤 →ₐ[ℂ] B` equivariant for
> the two groups, together with the demands that both groups act on the whole of `B` by
> algebra endomorphisms. It is the gauge-boson part of the Standard Model's
> `AlgebraRealization`, for any local-gauge-data package `jets`, and every result about a
> gauge field in an algebra of local expressions is stated for a realization `h`.
>
> The gauge-field symbols of a realization are the jet algebra's own symbols pushed along
> the map, `GaugeAlgebraRealization.A`, and their transformation laws are the jet algebra's
> own laws pushed along it. The base case is the jet algebra realized in itself,
> `GaugeAlgebraRealization.id`: its Lorentz law is that of a Lorentz derivative, and its gauge
> law is the substitution action of the jet gauge group constructed in
> `LocalGaugeFieldAlgebra.GaugeAction`.
>
>
> Let `A_μ^a` be a gauge field for the gauge group `G₀`, with `μ` a spacetime (covector)
> index and `a` an adjoint index. Under a gauge transformation `g` the field transforms as
>
>   `A_μ ↦ Ad_g A_μ + maurerCartan(g)_μ`,
>
> where `maurerCartan(g)_μ = i (∂_μ g) g⁻¹` is the Maurer–Cartan form. The symbols `[∂_s A_μ^a]`
> are coordinate functions on the space of field configurations, so the induced (left)
> action is the pullback along `g⁻¹`: one substitutes `g⁻¹` into the field law and
> differentiates `s` times with the Leibniz rule:
>
>   `g • [∂_s A_μ^a] = ∑_{x+y=s} C(x,y) (∂_x (Ad_{g⁻¹})^a_b)| [∂_y A_μ^b]`
>   `                  + (∂_s maurerCartan(g⁻¹)_μ^a)|`,
>
> where `C(x,y)` is the multinomial coefficient of the splitting and `|` denotes
> evaluation at the base point. All the data on the right is carried by the *jet* of the
> gauge transformation, which is why the gauge representation is a representation of the
> jet group `GJ` and not merely of its value group `G₀`.
>
> In the formalization, `h.A s μ φ` is the symbol `∂_s A_μ^a` contracted with a dual adjoint
> vector `φ`; `∂_x (Ad_{g⁻¹})^a_b|` acting on the dual index is `jets.adjointDualCoeff g⁻¹ x φ`;
> the sum `∑_{x+y=s} C(x,y)` is the sum over `s.antidiagonal`, in which a splitting `(x, y)`
> occurs with multiplicity exactly `C(x,y)`; and `(∂_s maurerCartan(g⁻¹)_μ)|` is
> `jets.evalLie (jets.iteratedDeriv s (jets.maurerCartan g⁻¹ μ))`, paired with `φ` and
> embedded in `B` as a scalar. This is the law `GaugeAlgebraRealization.gauge_apply_deriv`;
> the Lorentz law `GaugeAlgebraRealization.lorentz_apply` says that the symbol carries one
> covector index and that each derivative slot transforms as a covector.
>
>
> - `GaugeAlgebraRealization` : an algebra carrying the gauge bosons, as an equivariant
>   algebra map out of the jet algebra.
> - `GaugeAlgebraRealization.id` : the jet algebra realized in itself.
> - `GaugeAlgebraRealization.A` : the gauge-field symbols of a realization, images of the jet
>   algebra's symbols, with the laws `lorentz_apply` and `gauge_apply_deriv`; product preservation
>   is given by `GaugeAlgebraRealization.repJet_mul`.

## ii. Key results

> - `GaugeAlgebraRealization` : an algebra `B` carrying the gauge bosons of the package `jets`: an
>   algebra map out of the complexified gauge-boson jet algebra, equivariant for the jet gauge group
>   and the Lorentz group, with both groups acting on the whole of `B` by algebra endomorphisms
> - `lorentz_apply` : the Lorentz law: the gauge-field symbol carries one covector index, and each
>   derivative slot transforms as a covector
> - `gauge_apply_deriv` : the gauge law: a jet `U` acts on the derivative symbol `∂_s A_μ^φ` by the
>   Leibniz convolution of the dual adjoint Taylor coefficients of `U⁻¹` against lower symbols (the
>   multiset antidiagonal carrying the multinomial coefficients), plus the base-point value of the
>   `s`-th derivative of the Maurer–Cartan form of `U⁻¹`
> - `GaugeAlgebraRealization.repJet_mul` : the gauge action preserves products: gauge
>   transformations act on the algebra of local expressions as algebra homomorphisms

## iv. References

> * None.

## A. Realizations of the gauge-boson jet algebra

**`GaugeAlgebraRealization`**, a structure, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/Basic.lean#L111).

> An algebra `B` carrying the gauge bosons of the package `jets`: an algebra map out of
> the complexified gauge-boson jet algebra, equivariant for the jet gauge group and the
> Lorentz group, with both groups acting on the whole of `B` by algebra endomorphisms.
> The gauge-field symbols of `B` are the images of the jet algebra's symbols,
> `GaugeAlgebraRealization.A`, and they satisfy the jet algebra's laws by transport.

```lean
structure GaugeAlgebraRealization (jets : LocalGaugeData G₀ 𝔤 GJ 𝔤J) (B : Type) [Ring B]
    [Algebra ℂ B] (repJet : Representation ℂ GJ B) (repLorentz : Representation ℂ SL(2,ℂ) B)
    where
  /-- The algebra map out of the gauge-boson jet algebra: it places the gauge-boson
    symbols, and every polynomial expression in them, inside `B`. -/
  toAlgHom : ℂ ⊗[ℝ] LocalGaugeFieldAlgebra 𝔤 →ₐ[ℂ] B
  /-- The gauge-field symbols `∂_s A_μ^φ` of `B`. They are determined by the map, as the
    images of the jet algebra's symbols (`A_eq`), and are recorded as data so that the
    theory can treat them as opaque symbols and a concrete realization can present the
    symbols it already has. -/
  A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ 𝔤 →ₗ[ℝ] B
  /-- The symbols are the images of the jet algebra's symbols. -/
  A_eq : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ 𝔤),
    A s μ φ = toAlgHom (LocalGaugeFieldAlgebra.gaugeField 𝔤 s μ φ)
  /-- The map is equivariant for the jet gauge group. -/
  map_repJet : ∀ (U : GJ) (x : ℂ ⊗[ℝ] LocalGaugeFieldAlgebra 𝔤),
    toAlgHom (LocalGaugeFieldAlgebra.complexRepJet jets U x) = repJet U (toAlgHom x)
  /-- The map is equivariant for the Lorentz group. -/
  map_repLorentz : ∀ (Λ : SL(2,ℂ)) (x : ℂ ⊗[ℝ] LocalGaugeFieldAlgebra 𝔤),
    toAlgHom (LocalGaugeFieldAlgebra.complexRepLorentzGroup 𝔤 Λ x) = repLorentz Λ (toAlgHom x)
  /-- The jet gauge group acts on the whole of `B` by algebra endomorphisms. -/
  repJet_mul : ∀ (U : GJ) (b₁ b₂ : B), repJet U (b₁ * b₂) = repJet U b₁ * repJet U b₂
  /-- The Lorentz group acts on the whole of `B` by algebra endomorphisms. -/
  repLorentz_mul : ∀ (Λ : SL(2,ℂ)) (b₁ b₂ : B),
    repLorentz Λ (b₁ * b₂) = repLorentz Λ b₁ * repLorentz Λ b₂
```

**`GaugeAlgebraRealization.id`**, a def, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/Basic.lean#L146).

> The gauge-boson jet algebra realized in itself, by the identity.

```lean
noncomputable def id : GaugeAlgebraRealization jets (ℂ ⊗[ℝ] LocalGaugeFieldAlgebra 𝔤)
    (complexRepJet jets) (complexRepLorentzGroup 𝔤)
```

**`GaugeAlgebraRealization.A_apply`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/Basic.lean#L159).

```lean
lemma A_apply (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ 𝔤) :
    h.A s μ φ = h.toAlgHom (gaugeField 𝔤 s μ φ)
```

**`GaugeAlgebraRealization.id_A`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/Basic.lean#L165).

```lean
lemma id_A : (GaugeAlgebraRealization.id jets).A = gaugeField 𝔤
```

**`GaugeAlgebraRealization.ext`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/Basic.lean#L169).

> A realization is determined by its algebra map.

```lean
lemma ext {h₁ h₂ : GaugeAlgebraRealization jets B repJet repLorentz}
    (h : h₁.toAlgHom = h₂.toAlgHom) : h₁ = h₂
```

**`GaugeAlgebraRealization.commute_A`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/Basic.lean#L183).

> The gauge-field symbols of a realization commute, being images of a commutative
> algebra.

```lean
lemma commute_A (p q : Multiset (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3)
    (φ ψ : Module.Dual ℝ 𝔤) : Commute (h.A p μ φ) (h.A q ν ψ)
```

**`GaugeAlgebraRealization.lorentz_apply`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/Basic.lean#L191).

> The Lorentz law: the gauge-field symbol carries one covector index, and each derivative
> slot transforms as a covector.

```lean
lemma lorentz_apply (Λ : SL(2,ℂ)) (n : ℕ) (l : Fin n → (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ 𝔤) :
    repLorentz Λ (h.A (List.ofFn l) μ φ) =
      ∑ (p : Fin n → (Fin 1 ⊕ Fin 3)),
        (∏ (i : Fin n), (((SL2C.toLorentzGroup Λ).1 (p i) (l i) : ℝ) : ℂ)) •
      ∑ a, (((Lorentz.SL2C.toLorentzGroup Λ).1 a μ : ℝ) : ℂ) • h.A (List.ofFn p) a φ
```

**`GaugeAlgebraRealization.gauge_apply_deriv`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/Basic.lean#L211).

> The gauge law: a jet `U` acts on the derivative symbol `∂_s A_μ^φ` by the Leibniz
> convolution of the dual adjoint Taylor coefficients of `U⁻¹` against lower symbols (the
> multiset antidiagonal carrying the multinomial coefficients), plus the base-point value of
> the `s`-th derivative of the Maurer–Cartan form of `U⁻¹`.

```lean
lemma gauge_apply_deriv (U : GJ) (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ 𝔤) :
    repJet U (h.A s μ φ) =
      (s.antidiagonal.map fun p => h.A p.2 μ (jets.adjointDualCoeff U⁻¹ p.1 φ)).sum
      + algebraMap ℂ B (φ (jets.evalLie (jets.iteratedDeriv s (jets.maurerCartan U⁻¹ μ))))
```

## Depends on

- [The gauge-field symbols of the jet algebra and their laws](gaugeboson-localgauge-gaugefield.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/Basic.lean)
