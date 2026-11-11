---
declaration: section
origin: cited
lean: Stacks.DeRham.exists_funnyMap, Stacks.DeRham.funnyMap, Stacks.DeRham.funnyMap_comp, Stacks.DeRham.funnyMap_zero, Stacks.DeRham.funnyMap_wedge, Stacks.DeRham.funnyMap_naturality, Stacks.DeRham.presentationFunnyMap, Stacks.DeRham.presentationFunnyMap_zero
statement: formalized
proof: formalized
---

# 50.18 Comparing sheaves of differential forms

Section 50.18 of the Stacks Project, [Tag 0FL7](https://stacks.math.columbia.edu/tag/0FL7). 6 tags here are carried by 14 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FL8, a lemma

[Tag 0FL8](https://stacks.math.columbia.edu/tag/0FL8) in the Stacks Project.

**`Stacks.DeRham.exists_funnyMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/FunnyMap.lean, line 962](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/FunnyMap.lean#L962). The attribute's comment: “top-wedge construction”.

> The top-wedge construction descends to `⋀ᵖ(L / d(M⁻¹))`, independently of both the
> retraction and the basis: there is a family of maps whose value on the image of every
> `η : ⋀ᵖ L` is `funnyMapLift p n r π d b η`.

```lean
theorem exists_funnyMap (n : ℕ)
    (i : K →ₗ[R] L) (π : L →ₗ[R] Mzero)
    (d : Mneg →ₗ[R] L) (dM : Mneg →ₗ[R] Mzero)
    (_hi : Function.Injective i) (_hexact : Function.Exact i π)
    (_hπ : Function.Surjective π) (_hsquare : π.comp d = dM)
    (_hzero : Nonempty (Module.Basis (Fin n) R Mzero))
    (_hneg : Nonempty (Module.Basis (Fin n) R Mneg)) :
    ∃ c : ∀ p : ℕ, (⋀[R]^p (L ⧸ LinearMap.range d)) →ₗ[R]
        (⋀[R]^p K) ⊗[R] twoTermDeterminant R n Mneg Mzero,
      ∀ (p : ℕ) (r : L →ₗ[R] K), r.comp i = LinearMap.id →
        ∀ (b : Module.Basis (Fin n) R Mneg) (η : ⋀[R]^p L),
          c p (exteriorPower.map p (LinearMap.range d).mkQ η) =
            funnyMapLift p n r π d b η
```

**`Stacks.DeRham.funnyMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/FunnyMap.lean, line 996](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/FunnyMap.lean#L996). The attribute's comment: “canonical maps”.

> The canonical maps `cᵖ : ⋀ᵖ(L / d(M⁻¹)) → ⋀ᵖK ⊗ det(M⁻¹ → M⁰)` attached to the exact
> two-term diagram, characterized by `funnyMap_apply_lift`.

```lean
noncomputable def funnyMap (n : ℕ)
    (i : K →ₗ[R] L) (π : L →ₗ[R] Mzero)
    (d : Mneg →ₗ[R] L) (dM : Mneg →ₗ[R] Mzero)
    (hi : Function.Injective i) (hexact : Function.Exact i π)
    (hπ : Function.Surjective π) (hsquare : π.comp d = dM)
    (hzero : Nonempty (Module.Basis (Fin n) R Mzero))
    (hneg : Nonempty (Module.Basis (Fin n) R Mneg)) :
    ∀ p : ℕ, (⋀[R]^p (L ⧸ LinearMap.range d)) →ₗ[R]
      (⋀[R]^p K) ⊗[R] twoTermDeterminant R n Mneg Mzero
```

**`Stacks.DeRham.funnyMap_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/FunnyMap.lean, line 1026](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/FunnyMap.lean#L1026). The attribute's comment: “restriction to K”.

> Restricting the degree-`p` canonical map to `K` is tensoring with the determinant
> element.

```lean
theorem funnyMap_comp (n p : ℕ)
    (i : K →ₗ[R] L) (π : L →ₗ[R] Mzero)
    (d : Mneg →ₗ[R] L) (dM : Mneg →ₗ[R] Mzero)
    (hi : Function.Injective i) (hexact : Function.Exact i π)
    (hπ : Function.Surjective π) (hsquare : π.comp d = dM)
    (hzero : Nonempty (Module.Basis (Fin n) R Mzero))
    (hneg : Nonempty (Module.Basis (Fin n) R Mneg)) (ω : ⋀[R]^p K) :
    funnyMap n i π d dM hi hexact hπ hsquare hzero hneg p
        (exteriorPower.map p ((LinearMap.range d).mkQ.comp i) ω) =
      ω ⊗ₜ[R] twoTermDeterminantElement R dM hneg
```

**`Stacks.DeRham.funnyMap_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/FunnyMap.lean, line 1082](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/FunnyMap.lean#L1082). The attribute's comment: “degree zero”.

> In degree zero, the canonical map takes `1` to the determinant element.

```lean
theorem funnyMap_zero (n : ℕ)
    (i : K →ₗ[R] L) (π : L →ₗ[R] Mzero)
    (d : Mneg →ₗ[R] L) (dM : Mneg →ₗ[R] Mzero)
    (hi : Function.Injective i) (hexact : Function.Exact i π)
    (hπ : Function.Surjective π) (hsquare : π.comp d = dM)
    (hzero : Nonempty (Module.Basis (Fin n) R Mzero))
    (hneg : Nonempty (Module.Basis (Fin n) R Mneg)) :
    funnyMap n i π d dM hi hexact hπ hsquare hzero hneg 0
        (exteriorPower.ιMulti R 0 (fun j ↦ Fin.elim0 j)) =
      (exteriorPower.ιMulti R 0 (fun j ↦ Fin.elim0 j)) ⊗ₜ[R]
        twoTermDeterminantElement R dM hneg
```

**`Stacks.DeRham.funnyMap_wedge`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/FunnyMap.lean, line 1104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/FunnyMap.lean#L1104). The attribute's comment: “wedge compatibility”.

> The canonical maps commute with wedging on the left by an exterior power of `K`.

```lean
theorem funnyMap_wedge (n q p : ℕ)
    (i : K →ₗ[R] L) (π : L →ₗ[R] Mzero)
    (d : Mneg →ₗ[R] L) (dM : Mneg →ₗ[R] Mzero)
    (hi : Function.Injective i) (hexact : Function.Exact i π)
    (hπ : Function.Surjective π) (hsquare : π.comp d = dM)
    (hzero : Nonempty (Module.Basis (Fin n) R Mzero))
    (hneg : Nonempty (Module.Basis (Fin n) R Mneg))
    (ω : ⋀[R]^q K) (η : ⋀[R]^p (L ⧸ LinearMap.range d)) :
    funnyMap n i π d dM hi hexact hπ hsquare hzero hneg (q + p)
        (exteriorPower.wedgeMul (R := R) q p
          (exteriorPower.map q ((LinearMap.range d).mkQ.comp i) ω) η) =
      (exteriorPower.wedgeMul (R := R) q p ω).rTensor
        (twoTermDeterminant R n Mneg Mzero)
        (funnyMap n i π d dM hi hexact hπ hsquare hzero hneg p η)
```

## Tag 0H9F, a lemma

[Tag 0H9F](https://stacks.math.columbia.edu/tag/0H9F) in the Stacks Project.

**`Stacks.DeRham.funnyMap_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/Complex/FunnyMapNaturality.lean, line 41](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/Complex/FunnyMapNaturality.lean#L41).

> The canonical maps `Stacks.DeRham.funnyMap` are natural for compatible morphisms of two-term
> diagrams, provided the two terms of the complex are carried isomorphically to their scalar
> extensions.

```lean
theorem funnyMap_naturality
    {K₁ L₁ N₁ Z₁ K₂ L₂ N₂ Z₂ : Type*}
    [AddCommGroup K₁] [Module R₁ K₁]
    [AddCommGroup L₁] [Module R₁ L₁]
    [AddCommGroup N₁] [Module R₁ N₁]
    [AddCommGroup Z₁] [Module R₁ Z₁]
    [AddCommGroup K₂] [Module R₂ K₂]
    [AddCommGroup L₂] [Module R₂ L₂]
    [AddCommGroup N₂] [Module R₂ N₂]
    [AddCommGroup Z₂] [Module R₂ Z₂]
    (n p : ℕ)
    (i₁ : K₁ →ₗ[R₁] L₁) (π₁ : L₁ →ₗ[R₁] Z₁)
    (d₁ : N₁ →ₗ[R₁] L₁) (dM₁ : N₁ →ₗ[R₁] Z₁)
    (i₂ : K₂ →ₗ[R₂] L₂) (π₂ : L₂ →ₗ[R₂] Z₂)
    (d₂ : N₂ →ₗ[R₂] L₂) (dM₂ : N₂ →ₗ[R₂] Z₂)
    (hi₁ : Function.Injective i₁) (hexact₁ : Function.Exact i₁ π₁)
    (hπ₁ : Function.Surjective π₁) (hsquare₁ : π₁.comp d₁ = dM₁)
    (hi₂ : Function.Injective i₂) (hexact₂ : Function.Exact i₂ π₂)
    (hπ₂ : Function.Surjective π₂) (hsquare₂ : π₂.comp d₂ = dM₂)
    (hZ₁ : Nonempty (Module.Basis (Fin n) R₁ Z₁))
    (hN₁ : Nonempty (Module.Basis (Fin n) R₁ N₁))
    (hZ₂ : Nonempty (Module.Basis (Fin n) R₂ Z₂))
    (hN₂ : Nonempty (Module.Basis (Fin n) R₂ N₂))
    (k : K₁ →ₛₗ[algebraMap R₁ R₂] K₂)
    (l : L₁ →ₛₗ[algebraMap R₁ R₂] L₂)
    (neg : N₁ →ₛₗ[algebraMap R₁ R₂] N₂)
    (zero : Z₁ →ₛₗ[algebraMap R₁ R₂] Z₂)
    (hki : ∀ x, l (i₁ x) = i₂ (k x))
    (hlπ : ∀ x, zero (π₁ x) = π₂ (l x))
    (hnd : ∀ x, l (d₁ x) = d₂ (neg x))
    (negBaseChange : TensorProduct R₁ R₂ N₁ ≃ₗ[R₂] N₂)
    (zeroBaseChange : TensorProduct R₁ R₂ Z₁ ≃ₗ[R₂] Z₂)
    (hnegBaseChange : ∀ x r, negBaseChange (r ⊗ₜ[R₁] x) = r • neg x)
    (hzeroBaseChange : ∀ x r, zeroBaseChange (r ⊗ₜ[R₁] x) = r • zero x)
    (onH : (⋀[R₁]^p (L₁ ⧸ LinearMap.range d₁)) →ₛₗ[algebraMap R₁ R₂]
      (⋀[R₂]^p (L₂ ⧸ LinearMap.range d₂)))
    (onK : (⋀[R₁]^p K₁) →ₛₗ[algebraMap R₁ R₂] (⋀[R₂]^p K₂))
    (onNegTop : (⋀[R₁]^n N₁) →ₛₗ[algebraMap R₁ R₂] (⋀[R₂]^n N₂))
    (onZeroTop : (⋀[R₁]^n Z₁) →ₛₗ[algebraMap R₁ R₂] (⋀[R₂]^n Z₂))
    (onNegDual : Module.Dual R₁ (⋀[R₁]^n N₁) →ₛₗ[algebraMap R₁ R₂]
      Module.Dual R₂ (⋀[R₂]^n N₂))
    (onDet : twoTermDeterminant R₁ n N₁ Z₁ →ₛₗ[algebraMap R₁ R₂]
      twoTermDeterminant R₂ n N₂ Z₂)
    (honH : ∀ x : Fin p → L₁,
      onH (exteriorPower.ιMulti R₁ p (fun j ↦ (LinearMap.range d₁).mkQ (x j))) =
        exteriorPower.ιMulti R₂ p (fun j ↦ (LinearMap.range d₂).mkQ (l (x j))))
    (honK : ∀ x : Fin p → K₁,
      onK (exteriorPower.ιMulti R₁ p x) =
        exteriorPower.ιMulti R₂ p (fun j ↦ k (x j)))
    (honNegTop : ∀ x : Fin n → N₁,
      onNegTop (exteriorPower.ιMulti R₁ n x) =
        exteriorPower.ιMulti R₂ n (fun j ↦ neg (x j)))
    (honZeroTop : ∀ x : Fin n → Z₁,
      onZeroTop (exteriorPower.ιMulti R₁ n x) =
        exteriorPower.ιMulti R₂ n (fun j ↦ zero (x j)))
    (honNegDual : ∀ (φ : Module.Dual R₁ (⋀[R₁]^n N₁)) (x : ⋀[R₁]^n N₁),
      onNegDual φ (onNegTop x) = algebraMap R₁ R₂ (φ x))
    (honDet : ∀ (z : ⋀[R₁]^n Z₁) (φ : Module.Dual R₁ (⋀[R₁]^n N₁)),
      onDet (z ⊗ₜ[R₁] φ) = onZeroTop z ⊗ₜ[R₂] onNegDual φ) :
    (TensorProduct.map onK onDet).comp
        (funnyMap n i₁ π₁ d₁ dM₁ hi₁ hexact₁ hπ₁ hsquare₁ hZ₁ hN₁ p) =
      (funnyMap n i₂ π₂ d₂ dM₂ hi₂ hexact₂ hπ₂ hsquare₂ hZ₂ hN₂ p).comp onH
```

## Tag 0FL9, a remark

[Tag 0FL9](https://stacks.math.columbia.edu/tag/0FL9) in the Stacks Project.

**`Stacks.DeRham.presentationFunnyMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/Complex/LocalDescription.lean, line 336](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/Complex/LocalDescription.lean#L336). The attribute's comment: “canonical maps”.

> The canonical maps on absolute differential forms associated to a square presentation of `B`
> over `A` which is a relative global complete intersection:
> `Ω^p_{B⁄ℤ} → Ω^p_{A⁄ℤ} ⊗ det(NL_{B/A})`.

```lean
noncomputable def presentationFunnyMap (p : ℕ) :
    (⋀[B]^p Ω[B⁄ℤ]) →ₗ[B]
      (⋀[B]^p (B ⊗[A] Ω[A⁄ℤ])) ⊗[B]
        twoTermDeterminant B n P.toExtension.Cotangent P.toExtension.CotangentSpace
```

**`Stacks.DeRham.presentationFunnyMap_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/Complex/LocalDescription.lean, line 345](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/Complex/LocalDescription.lean#L345). The attribute's comment: “degree zero”.

> In degree zero the canonical map takes the unit to the determinant element of the relative
> naive cotangent complex.

```lean
theorem presentationFunnyMap_zero :
    presentationFunnyMap P 0 (exteriorPower.ιMulti B 0 (fun j ↦ Fin.elim0 j)) =
      (exteriorPower.ιMulti B 0 (fun j ↦ Fin.elim0 j)) ⊗ₜ[B]
        cotangentDeterminantElement P
```

**`Stacks.DeRham.presentationFunnyMap_wedge`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/Complex/LocalDescription.lean, line 354](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/Complex/LocalDescription.lean#L354). The attribute's comment: “wedge compatibility”.

> The canonical maps commute with wedging by a base-changed absolute differential form
> on `A`.

```lean
theorem presentationFunnyMap_wedge (q p : ℕ) (ω : ⋀[B]^q (B ⊗[A] Ω[A⁄ℤ]))
    (η : ⋀[B]^p Ω[B⁄ℤ]) :
    presentationFunnyMap P (q + p)
        (exteriorPower.wedgeMul (R := B) q p
          (exteriorPower.map q (KaehlerDifferential.mapBaseChange ℤ A B) ω) η) =
      (exteriorPower.wedgeMul (R := B) q p ω).rTensor
        (twoTermDeterminant B n P.toExtension.Cotangent P.toExtension.CotangentSpace)
        (presentationFunnyMap P p η)
```

**`Stacks.DeRham.presentationFunnyMap_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/Complex/LocalDescription.lean, line 367](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/Complex/LocalDescription.lean#L367). The attribute's comment: “composition with pullback”.

> Composing the canonical map on forms with pullback from `A` is multiplication by the
> determinant element of the relative naive cotangent complex.

```lean
theorem presentationFunnyMap_comp (p : ℕ) (ω : ⋀[B]^p (B ⊗[A] Ω[A⁄ℤ])) :
    presentationFunnyMap P p
        (exteriorPower.map p (KaehlerDifferential.mapBaseChange ℤ A B) ω) =
      ω ⊗ₜ[B] cotangentDeterminantElement P
```

**`Algebra.isRelativeGlobalCompleteIntersection_of_quasiFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/QuasiFinite.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/QuasiFinite.lean#L60). The attribute's comment: “the source's `B` is a relative global complete intersection over `A`, at the level of the algebra; the presentation-level form, which is what the rest of the remark uses, is `Algebra.Presentation.isRelativeGlobalCompleteIntersection_of_quasiFinite`”.

> A quasi-finite `A`-algebra `B` admitting a presentation
> `B = A[x_1, …, x_n]/(f_1, …, f_n)` by as many relations as variables is a relative global
> complete intersection over `A` (Definition 00SP).

```lean
theorem isRelativeGlobalCompleteIntersection_of_quasiFinite {n : ℕ}
    (P : Algebra.Presentation A B (Fin n) (Fin n)) :
    Algebra.IsRelativeGlobalCompleteIntersection A B
```

Declarations registered for the tag:

- [`Algebra.Presentation.exists_basis_cotangent_relation`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/RelativeConormal.lean#L981), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/DeRham/Complex/LocalDescription.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/Complex/LocalDescription.lean#L62) (StacksFrontier): “conormal basis”.
- [`Stacks.DeRham.cotangentDiagram`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/Complex/LocalDescription.lean#L192), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/DeRham/Complex/LocalDescriptionQuasiFinite.lean, line 31](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/Complex/LocalDescriptionQuasiFinite.lean#L31) (StacksFrontier): “the displayed diagram itself, instantiated at a square presentation which is a relative global complete intersection: the short exact sequence 0 -> B (x)\_A Omega\_\{A/Z} -> B (x)\_P Omega\_\{P/Z} -> Omega\_\{P/A} (x)\_P B -> 0 of B-modules whose outer terms are free of rank n, the two-term complex out of the conormal module into it, the commuting square identifying that complex with the cotangent complex of the presentation, and the identification of the cokernel with Omega\_\{B/Z} under which the base-change map from Omega\_\{A/Z} becomes the quotient map. The type of such diagrams is the structure Stacks.DeRham.CotangentDiagram; this is the witness, so the diagram is exhibited and not just described”.
- [`Algebra.Presentation.isRelativeGlobalCompleteIntersection_of_quasiFinite`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/QuasiFinite.lean#L103), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/RingTheory/CompleteIntersection/QuasiFinite.lean, line 39](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/QuasiFinite.lean#L39) (StacksFrontier): “the relative global complete intersection: the source's `A → B` quasi-finite is `Algebra.QuasiFinite A B`, which for an algebra with a finite presentation is its Definition 00PL, and `B = A[x_1, …, x_n]/(f_1, …, f_n)` is a presentation with `Nat.card σ = Nat.card ι`”.

## Tag 0H9G, a lemma

[Tag 0H9G](https://stacks.math.columbia.edu/tag/0H9G) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.GarelMaps.subsingleton_isCompatible_detNLPullbackIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/Comparison/Uniqueness.lean, line 881](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/Comparison/Uniqueness.lean#L881). The attribute's comment: “at most one collection c'^p satisfying 0H9C and 0H9D compatible with c through the square, using the 07HX maps and the 0FKB identification b^*det(NL\_\{Y/X}) = det(NL\_\{Y'/X'})”.

> **Stacks Project, Lemma 0H9G.** Consider a commutative square `b ≫ f = f' ≫ a` of schemes
> which induces an isomorphism of `Y'` with an open subscheme of `X' ×_X Y`, with `f` locally
> quasi-finite and syntomic (so that `f'` is too), and maps
> `c^p : Ω^p_{Y/ℤ} ⟶ f^*Ω^p_{X/ℤ} ⊗ det(NL_{Y/X})` satisfying (0H9C) and (0H9D). Then there is at
> most one collection of maps `c'^p : Ω^p_{Y'/ℤ} ⟶ f'^*Ω^p_{X'/ℤ} ⊗ det(NL_{Y'/X'})` satisfying
> (0H9C) and (0H9D) for which the squares of the lemma commute, the right-hand vertical arrows
> using the maps `b^*Ω^p_{Y/ℤ} ⟶ Ω^p_{Y'/ℤ}` and `a^*Ω^p_{X/ℤ} ⟶ Ω^p_{X'/ℤ}` of Section 07HX and the
> identification `b^*det(NL_{Y/X}) = det(NL_{Y'/X'})` of Section 0FKB.

```lean
theorem GarelMaps.subsingleton_isCompatible_detNLPullbackIso (w : b ≫ f = f' ≫ a)
    [IsOpenImmersion (pullback.lift b f' w)] (hf : Syntomic f) [LocallyQuasiFinite f]
    (c : f.GarelMaps (f.detNL hf)) :
    haveI := locallyQuasiFinite_of_isOpenImmersion_lift w
    c.IsNormalized (f.deltaNL hf) → c.IsMultiplicative →
      {c' : f'.GarelMaps (f'.detNL (syntomic_of_isOpenImmersion_lift w hf)) |
        c'.IsNormalized (f'.deltaNL (syntomic_of_isOpenImmersion_lift w hf)) ∧
          c'.IsMultiplicative ∧
          GarelMaps.IsCompatible w
            (detNLPullbackIso w hf (syntomic_of_isOpenImmersion_lift w hf)).hom c c'}.Subsingleton
```

## Tag 0H9H, a lemma

[Tag 0H9H](https://stacks.math.columbia.edu/tag/0H9H) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.exists_garelMaps_isCompatible_resLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/Comparison/LocalCompatibility.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/Comparison/LocalCompatibility.lean#L73). The attribute's comment: “for every y' there are opens V' ∋ y', V, U', U of the square and maps c^p\_\{V/U}, c^p\_\{V'/U'} satisfying 0H9C and 0H9D compatible in the sense of 0H9G”.

> **Stacks Project, Lemma 0H9H.** Let `b ≫ f = f' ≫ a` be a commutative square of schemes
> which induces an isomorphism of `Y'` with an open subscheme of `X' ×_X Y`, with `f` locally
> quasi-finite and syntomic. Then for every `y' ∈ Y'` there are opens `V' ⊆ Y'`, `V ⊆ Y`,
> `U' ⊆ X'`, `U ⊆ X` with `y' ∈ V'`, `f'(V') ⊆ U'`, `b(V') ⊆ V`, `a(U') ⊆ U` and `f(V) ⊆ U`, and
> maps `c^p_{V/U}` and `c^p_{V'/U'}` satisfying (0H9C) and (0H9D) which are compatible with the
> restricted square in the sense of Lemma 0H9G, through the identification
> `b^*det(NL_{V/U}) = det(NL_{V'/U'})` of Lemma 0FKB.

```lean
theorem exists_garelMaps_isCompatible_resLE (w : b ≫ f = f' ≫ a)
    [IsOpenImmersion (pullback.lift b f' w)] (hf : Syntomic f) [LocallyQuasiFinite f] (y' : Y') :
    ∃ (V' : Y'.Opens) (V : Y.Opens) (U' : X'.Opens) (U : X.Opens) (e' : V' ≤ f' ⁻¹ᵁ U')
      (hV : V' ≤ b ⁻¹ᵁ V) (hU : U' ≤ a ⁻¹ᵁ U) (e : V ≤ f ⁻¹ᵁ U), y' ∈ V' ∧
      haveI := isOpenImmersion_lift_resLE_resLE w e e' hU hV
      haveI := locallyQuasiFinite_of_isOpenImmersion_lift (resLE_comp_resLE_eq w e e' hU hV)
      ∃ (c : (f.resLE U V e).GarelMaps
          ((f.resLE U V e).detNL (IsZariskiLocalAtSource.resLE (P := @Syntomic) e hf)))
        (c' : (f'.resLE U' V' e').GarelMaps ((f'.resLE U' V' e').detNL
          (syntomic_of_isOpenImmersion_lift (resLE_comp_resLE_eq w e e' hU hV)
            (IsZariskiLocalAtSource.resLE (P := @Syntomic) e hf)))),
        c.IsNormalized
            ((f.resLE U V e).deltaNL (IsZariskiLocalAtSource.resLE (P := @Syntomic) e hf)) ∧
          c.IsMultiplicative ∧
          c'.IsNormalized ((f'.resLE U' V' e').deltaNL
            (syntomic_of_isOpenImmersion_lift (resLE_comp_resLE_eq w e e' hU hV)
              (IsZariskiLocalAtSource.resLE (P := @Syntomic) e hf))) ∧
          c'.IsMultiplicative ∧
          GarelMaps.IsCompatible (resLE_comp_resLE_eq w e e' hU hV)
            (detNLPullbackIso (resLE_comp_resLE_eq w e e' hU hV)
              (IsZariskiLocalAtSource.resLE (P := @Syntomic) e hf)
              (syntomic_of_isOpenImmersion_lift (resLE_comp_resLE_eq w e e' hU hV)
                (IsZariskiLocalAtSource.resLE (P := @Syntomic) e hf))).hom c c'
```

## Tag 0FLA, a lemma

[Tag 0FLA](https://stacks.math.columbia.edu/tag/0FLA) in the Stacks Project.

**`AlgebraicGeometry.GarelRule.existsUnique_isNormalized_isMultiplicative_isCompatible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/Comparison/ExistenceBaseChange.lean, line 335](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/Comparison/ExistenceBaseChange.lean#L335). The attribute's comment: “the unique rule c^p\_\{Y/X} satisfying 0H9C, 0H9D and 0H9E, and its composition with f^*Ω^p\_\{X/Z} → Ω^p\_\{Y/Z} is multiplication by δ(NL\_\{Y/X})”.

> There exists a unique rule that to every locally quasi-finite syntomic morphism of schemes
> `f : Y ⟶ X` assigns `𝒪_Y`-module maps
> `c^p_{Y/X} : Ω^p_{Y/ℤ} ⟶ f^*Ω^p_{X/ℤ} ⊗_{𝒪_Y} det(NL_{Y/X})` for `p ≥ 0` satisfying (0H9C),
> (0H9D) and (0H9E). In particular, the composition of `c^p_{Y/X}` with
> `f^*Ω^p_{X/ℤ} ⟶ Ω^p_{Y/ℤ}` is multiplication by `δ(NL_{Y/X})`.

```lean
theorem existsUnique_isNormalized_isMultiplicative_isCompatible :
    (∃! c : GarelRule.{u}, c.IsNormalized ∧ c.IsMultiplicative ∧ c.IsCompatible) ∧
      ∀ c : GarelRule.{u}, c.IsNormalized → c.IsMultiplicative → c.IsCompatible →
        ∀ ⦃X Y : Scheme.{u}⦄ (f : Y ⟶ X) (hf : Syntomic f) (hq : LocallyQuasiFinite f) (p : ℕ),
          f.absoluteFormsMap p ≫ c f hf hq p =
            (ρ_ (f.pullbackForms p)).inv ≫ (f.pullbackForms p ◁
              Scheme.Modules.globalSectionHom (f.detNL hf) (haveI := hq; f.deltaNL hf))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 50.18, Tag 0FL7](https://stacks.math.columbia.edu/tag/0FL7)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
