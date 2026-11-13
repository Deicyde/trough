---
declaration: section
origin: cited
lean: Stacks.Discriminant.finiteFactorRestriction, Stacks.Discriminant.IsTraceElement, Stacks.Discriminant.isTraceElement_congr, Stacks.Discriminant.isTraceElement_unique, Stacks.Discriminant.isTraceElement_finiteFlatTraceElement, Stacks.Discriminant.isTraceElement_baseChange, Stacks.Discriminant.isTraceElement_of_isLocalization_away, Stacks.Discriminant.isTraceElement_fst
statement: formalized
proof: formalized
---

# 49.4 Traces for flat quasi-finite ring maps

Section 49.4 of the Stacks Project, [Tag 0BSY](https://stacks.math.columbia.edu/tag/0BSY). 8 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0BT6, a definition

[Tag 0BT6](https://stacks.math.columbia.edu/tag/0BT6) in the Stacks Project.

**`Stacks.Discriminant.finiteFactorRestriction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Discriminant/TraceCondition.lean, line 158](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Discriminant/TraceCondition.lean#L158). The attribute's comment: “the restriction of a dualizing element to a finite direct factor”.

> The canonical restriction of a relative dualizing element to a finite direct factor
> after base change, together with the pure-tensor formula that characterizes it. The formula
> is the first component of the product map of Tag 0BT5, written through the finite-projective
> trace of the factor over the intermediate algebra.

```lean
def finiteFactorRestriction
    {A : Type u} {B : Type v}
    [CommRing A] [CommRing B] [Algebra A B]
    (F : FiniteOpenFactorization.{u, v, w} A B)
    (A₁ : Type x) [CommRing A₁] [Algebra A A₁]
    (C : Type y) (D : Type z) [CommRing C] [CommRing D]
    [Algebra A₁ C] [Algebra A₁ D]
    (e : (A₁ ⊗[A] B) ≃ₐ[A₁] (C × D))
    [Algebra (FiniteOpenFactorization.baseChange F A₁).middle C]
    (hcompat : ∀ a : (FiniteOpenFactorization.baseChange F A₁).middle,
      algebraMap _ C a =
        (e (algebraMap _ (A₁ ⊗[A] B) a)).1)
    (hfinite : Module.Finite A₁ C)
    (hprojective : Module.Projective A₁ C)
    (hmfinite : Module.Finite
      (FiniteOpenFactorization.baseChange F A₁).middle C)
    (hmprojective : Module.Projective
      (FiniteOpenFactorization.baseChange F A₁).middle C) :
    let F₁ := FiniteOpenFactorization.baseChange F A₁
    letI : Module A₁ (dualizingModule F₁) :=
      Module.compHom _ (algebraMap A₁ (A₁ ⊗[A] B))
    { h : dualizingModule F₁ →ₗ[A₁] Module.Dual A₁ C //
      letI : Module.Finite F₁.middle C := hmfinite
      letI : Module.Projective F₁.middle C := hmprojective
      ∀ (f : Module.Dual A₁ F₁.middle) (b : A₁ ⊗[A] B) (c : C),
        h (dualizingModule.tmul F₁ f b) c =
          f ((finiteProjectiveTrace F₁.middle C)
            (Algebra.lmul F₁.middle C ((e b).1 * c))) }
```

**`Stacks.Discriminant.IsTraceElement`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Discriminant/TraceCondition.lean, line 196](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Discriminant/TraceCondition.lean#L196). The attribute's comment: “trace\_element\_property”.

> **Stacks Project, Tag 0BT6.** A trace element is an element of the relative dualizing
> module whose image in every finite direct factor, after an arbitrary Noetherian base change,
> is the finite-projective trace of that factor.

```lean
def IsTraceElement
    {A : Type u} {B : Type v}
    [CommRing A] [CommRing B] [Algebra A B]
    [IsNoetherianRing A] [IsNoetherianRing B]
    [Module.Flat A B] [Algebra.QuasiFinite A B]
    (F : FiniteOpenFactorization.{u, v, w} A B)
    (τ : dualizingModule F) : Prop
```

**`Stacks.Discriminant.isTraceElement_congr`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/TraceElement/Independence.lean, line 221](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/TraceElement/Independence.lean#L221). The attribute's comment: “trace\_element\_property; independence of factorization”.

> **Stacks Project, Tag 0BT6.** The trace-element condition does not depend on the
> finite-open factorization chosen to represent the relative dualizing module. The three test
> universes are independent of each other and of the universes of the two factorizations.

```lean
theorem isTraceElement_congr
    {A : Type u} {B : Type v} [CommRing A] [CommRing B] [Algebra A B]
    [IsNoetherianRing A] [IsNoetherianRing B] [Module.Flat A B] [Algebra.QuasiFinite A B]
    (F : FiniteOpenFactorization.{u, v, w} A B)
    (G : FiniteOpenFactorization.{u, v, x} A B)
    (τ : dualizingModule F) :
    IsTraceElement.{u, v, w, s, t, r} F τ ↔
      IsTraceElement.{u, v, x, s, t, r} G (dualizingModuleEquiv F G τ)
```

## Tag 0BT7, a lemma

[Tag 0BT7](https://stacks.math.columbia.edu/tag/0BT7) in the Stacks Project.

**`Stacks.Discriminant.isTraceElement_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Discriminant/TraceElementUnique.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Discriminant/TraceElementUnique.lean#L52).

> **Stacks Project, Tag 0BT7.** A flat quasi-finite algebra of Noetherian rings has at most
> one trace element.

```lean
theorem isTraceElement_unique
    {A : Type u} {B : Type v}
    [CommRing A] [CommRing B] [Algebra A B]
    [IsNoetherianRing A] [IsNoetherianRing B]
    [Module.Flat A B] [Algebra.QuasiFinite A B]
    (F : FiniteOpenFactorization.{u, v, w} A B)
    {τ₁ τ₂ : dualizingModule F}
    (h₁ : IsTraceElement.{u, v, w, u, max u v, max u v} F τ₁)
    (h₂ : IsTraceElement.{u, v, w, u, max u v, max u v} F τ₂) :
    τ₁ = τ₂
```

## Tag 0BT8, a lemma

[Tag 0BT8](https://stacks.math.columbia.edu/tag/0BT8) in the Stacks Project.

**`Stacks.Discriminant.isTraceElement_finiteFlatTraceElement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/TraceElement/FiniteFlat.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/TraceElement/FiniteFlat.lean#L104).

> **Stacks Project, Tag 0BT8.** For a finite flat map of Noetherian rings, the ordinary
> trace of the finite projective algebra is a trace element of the relative dualizing module.

```lean
theorem isTraceElement_finiteFlatTraceElement (A : Type u) (B : Type v)
    [CommRing A] [CommRing B] [Algebra A B] [IsNoetherianRing A] [IsNoetherianRing B]
    [Module.Finite A B] [Module.Flat A B] :
    IsTraceElement.{u, v, v, x, y, z} (selfFactorization A B) (finiteFlatTraceElement A B)
```

## Tag 0BT9, a lemma

[Tag 0BT9](https://stacks.math.columbia.edu/tag/0BT9) in the Stacks Project.

**`Stacks.Discriminant.isTraceElement_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/TraceElement/BaseChange.lean, line 45](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/TraceElement/BaseChange.lean#L45). The attribute's comment: “trace\_base\_change”.

> **Stacks Project, Tag 0BT9.** The image of a trace element under the base-change map of
> the relative dualizing module is a trace element over the new base.

```lean
theorem isTraceElement_baseChange
    {A : Type u} {B : Type v} [CommRing A] [CommRing B] [Algebra A B]
    [IsNoetherianRing A] [IsNoetherianRing B] [Module.Flat A B] [Algebra.QuasiFinite A B]
    [Algebra.FiniteType A B]
    (F : FiniteOpenFactorization.{u, v, w} A B)
    (A₁ : Type x) [CommRing A₁] [Algebra A A₁] [IsNoetherianRing A₁]
    (τ : dualizingModule F) (hτ : IsTraceElement.{u, v, w, s, t, r} F τ) :
    letI : IsNoetherianRing (A₁ ⊗[A] B) := Algebra.FiniteType.isNoetherianRing A₁ _
    IsTraceElement.{x, max x v, max x w, s, t, r}
      (FiniteOpenFactorization.baseChange F A₁) (dualizingModule.baseChange F A₁ τ)
```

**`Stacks.Discriminant.isTraceElement_of_isLocalization_away`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/TraceElement/BaseLocalization.lean, line 175](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/TraceElement/BaseLocalization.lean#L175). The attribute's comment: “trace\_base\_localization”.

> **Stacks Project, Tag 0BT9.** A trace element of the relative dualizing module over a
> localization of the base remains a trace element over the original base, under the
> identification of Tag 0BT2, part (1).
>
> The trace-element condition over `R` tests a decomposition `S ⊗_R B ≃ C × D` with `C` finite
> over `S`. Since `f` becomes invertible in `B`, it is invertible in `C`, so the same decomposition
> is visible over the localization `S_f`, where the condition over `A` applies. The two
> restriction functionals to `C` differ by the localization map `S → S_f`, and a functional on a
> finite module is determined by its image there.

```lean
theorem isTraceElement_of_isLocalization_away
    {R : Type u} {A : Type v} {B : Type w}
    [CommRing R] [CommRing A] [CommRing B]
    [Algebra R A] [Algebra A B] [Algebra R B] [IsScalarTower R A B]
    [IsNoetherianRing R] [IsNoetherianRing A] [IsNoetherianRing B]
    [Module.Flat A B] [Algebra.QuasiFinite A B]
    (f : R) [IsLocalization.Away f A]
    (FR : FiniteOpenFactorization.{u, w, x} R B)
    (FA : FiniteOpenFactorization.{v, w, y} A B)
    (τ : dualizingModule FA) (hτ : IsTraceElement.{v, w, y, s, t, z} FA τ) :
    letI : Module.Flat R A := IsLocalization.flat A (Submonoid.powers f)
    letI : Algebra.QuasiFinite R A :=
      Algebra.QuasiFinite.of_isLocalization (Submonoid.powers f)
    letI : Module.Flat R B := Module.Flat.trans R A B
    letI : Algebra.QuasiFinite R B := Algebra.QuasiFinite.trans R A B
    IsTraceElement.{u, w, x, s, t, z} FR
      ((dualizingModule_equiv_of_isLocalization_away f FR FA).symm τ)
```

**`Stacks.Discriminant.isTraceElement_fst`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/TraceElement/ProductFactors.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/TraceElement/ProductFactors.lean#L95). The attribute's comment: “trace\_product\_factors”.

> **Stacks Project, Tag 0BT9.** A trace element of the relative dualizing module of a
> product restricts to a trace element on the first factor.

```lean
theorem isTraceElement_fst [Module.Flat A B]
    (F : FiniteOpenFactorization.{u, max v w, x} A (B × C))
    (FB : FiniteOpenFactorization.{u, v, y} A B)
    (FC : FiniteOpenFactorization.{u, w, z} A C)
    {τ : dualizingModule F}
    (hτ : IsTraceElement.{u, max v w, x, s, t, max r (max s w)} F τ) :
    IsTraceElement.{u, v, y, s, t, r} FB ((dualizingModuleProdEquiv F FB FC τ).1)
```

**`Stacks.Discriminant.isTraceElement_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/TraceElement/ProductFactors.lean, line 222](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/TraceElement/ProductFactors.lean#L222). The attribute's comment: “trace\_product\_factors”.

> **Stacks Project, Tag 0BT9.** A trace element of the relative dualizing module of a
> product restricts to a trace element on the second factor.

```lean
theorem isTraceElement_snd [Module.Flat A C]
    (F : FiniteOpenFactorization.{u, max v w, x} A (B × C))
    (FB : FiniteOpenFactorization.{u, v, y} A B)
    (FC : FiniteOpenFactorization.{u, w, z} A C)
    {τ : dualizingModule F}
    (hτ : IsTraceElement.{u, max v w, x, s, t, max r (max s v)} F τ) :
    IsTraceElement.{u, w, z, s, t, r} FC ((dualizingModuleProdEquiv F FB FC τ).2)
```

**`Stacks.Discriminant.isTraceElement_localization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/TraceElement/TargetLocalization.lean, line 260](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/TraceElement/TargetLocalization.lean#L260). The attribute's comment: “trace\_algebra\_localization”.

> **Stacks Project, Tag 0BT9.** A trace element of the relative dualizing module of a flat
> quasi-finite map of Noetherian rings remains a trace element after an away localization of the
> target, under the identification of Tag 0BT2, part (2).

```lean
theorem isTraceElement_localization
    {A : Type u} {B : Type v} {Bg : Type w} {M : Type x}
    [CommRing A] [CommRing B] [CommRing Bg]
    [Algebra A B] [Algebra B Bg] [Algebra A Bg] [IsScalarTower A B Bg]
    [IsNoetherianRing A] [IsNoetherianRing B]
    [Module.Flat A B] [Algebra.QuasiFinite A B]
    (g : B) [IsLocalization.Away g Bg]
    (F : FiniteOpenFactorization.{u, v, y} A B)
    (G : FiniteOpenFactorization.{u, w, z} A Bg)
    [AddCommGroup M] [Module B M] [Module Bg M] [IsScalarTower B Bg M]
    (localizationMap : dualizingModule F →ₗ[B] M)
    (hM : IsLocalizedModule (Submonoid.powers g) localizationMap)
    {τ : dualizingModule F} (hτ : IsTraceElement.{u, v, y, s, t, max s v} F τ) :
    letI : IsNoetherianRing Bg :=
      IsLocalization.isNoetherianRing (Submonoid.powers g) Bg inferInstance
    letI : Module.Flat B Bg := IsLocalization.flat Bg (Submonoid.powers g)
    letI : Module.Flat A Bg := Module.Flat.trans A B Bg
    letI : Algebra.QuasiFinite A Bg :=
      Algebra.QuasiFinite.of_isLocalization (Submonoid.powers g)
    IsTraceElement.{u, w, z, s, t, r} G
      (localizedModule_dualizingModule_equiv g F G localizationMap hM
        (localizationMap τ))
```

## Tag 0BTA, a lemma

[Tag 0BTA](https://stacks.math.columbia.edu/tag/0BTA) in the Stacks Project.

**`Stacks.Discriminant.isTraceElement_of_localization_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/TraceElement/LocalizationCover.lean, line 769](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/TraceElement/LocalizationCover.lean#L769).

> **Stacks Project, Tag 0BTA.** A section of the relative dualizing module of a flat
> quasi-finite map of Noetherian rings which is a trace element on every member of a finite
> principal open cover of the target is a trace element.

```lean
theorem isTraceElement_of_localization_cover
    {A : Type u} {B : Type v} [CommRing A] [CommRing B] [Algebra A B]
    [IsNoetherianRing A] [IsNoetherianRing B] [Module.Flat A B] [Algebra.QuasiFinite A B]
    (F : FiniteOpenFactorization.{u, v, w} A B)
    {n : ℕ} (g : Fin n → B) (hcover : Ideal.span (Set.range g) = ⊤)
    (τ : dualizingModule F)
    (G : ∀ i : Fin n, FiniteOpenFactorization.{u, v, z} A (Localization.Away (g i)))
    (hlocal : ∀ i : Fin n,
      letI : IsNoetherianRing (Localization.Away (g i)) :=
        IsLocalization.isNoetherianRing (Submonoid.powers (g i))
          (Localization.Away (g i)) inferInstance
      letI : Module.Flat B (Localization.Away (g i)) :=
        IsLocalization.flat (Localization.Away (g i)) (Submonoid.powers (g i))
      letI : Module.Flat A (Localization.Away (g i)) :=
        Module.Flat.trans A B (Localization.Away (g i))
      letI : Algebra.QuasiFinite A (Localization.Away (g i)) :=
        Algebra.QuasiFinite.of_isLocalization (Submonoid.powers (g i))
      IsTraceElement.{u, v, z, s, t, r} (G i)
        (localizedModule_dualizingModule_equiv (g i) F (G i)
          (LocalizedModule.mkLinearMap (Submonoid.powers (g i)) (dualizingModule F))
          (inferInstance : IsLocalizedModule (Submonoid.powers (g i))
            (LocalizedModule.mkLinearMap (Submonoid.powers (g i)) (dualizingModule F)))
          (LocalizedModule.mkLinearMap (Submonoid.powers (g i)) (dualizingModule F) τ))) :
    IsTraceElement.{u, v, w, s, t, r} F τ
```

## Tag 0BTB, a lemma

[Tag 0BTB](https://stacks.math.columbia.edu/tag/0BTB) in the Stacks Project.

**`Stacks.Discriminant.exists_isTraceElement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/TraceElement/Existence.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/TraceElement/Existence.lean#L142).

> **Stacks Project, Tag 0BTB.** A flat quasi-finite map of Noetherian rings has a trace
> element in its relative dualizing module.

```lean
theorem exists_isTraceElement (F : FiniteOpenFactorization.{u, v, w} A B) :
    ∃ τ : dualizingModule F, IsTraceElement.{u, v, w, x, y, z} F τ
```

## Tag 0BVJ, a remark

[Tag 0BVJ](https://stacks.math.columbia.edu/tag/0BVJ) in the Stacks Project.

**`Stacks.Discriminant.relativeTraceSection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeTraceSection.lean, line 358](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RelativeTraceSection.lean#L358).

> **Stacks Project, Tag 0BVJ.** The relative trace section `τ_{Y/X}` of a flat locally
> quasi-finite morphism of locally Noetherian schemes: the global section of the relative
> dualizing module obtained by gluing the trace elements of the affine charts along the cover of
> the source by the source charts of the chart pairs.

```lean
def relativeTraceSection (D : RelativeDualizingModuleData f) : Γ(D.sheaf, ⊤)
```

**`Stacks.Discriminant.localEquiv_relativeTraceSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeTraceSection.lean, line 384](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RelativeTraceSection.lean#L384).

> **Stacks Project, Tag 0BVJ.** On every pair of affine opens `Spec B = V ⊆ Y`,
> `Spec A = U ⊆ X` with `f(V) ⊆ U`, the relative trace section restricts to the trace element
> `τ_{B/A}` of the relative dualizing module `ω_{B/A}`, under the canonical identification of
> the sections over `V` with `ω_{B/A}`.

```lean
theorem localEquiv_relativeTraceSection (D : RelativeDualizingModuleData f)
    (U : X.affineOpens) (V : Y.affineOpens) (hVU : V.1 ≤ f ⁻¹ᵁ U.1) :
    letI : Algebra Γ(X, U.1) Γ(Y, V.1) := (f.appLE U V hVU).hom.toAlgebra
    letI : IsNoetherianRing Γ(X, U.1) := IsLocallyNoetherian.component_noetherian U
    letI : IsNoetherianRing Γ(Y, V.1) := IsLocallyNoetherian.component_noetherian V
    letI : Module.Flat Γ(X, U.1) Γ(Y, V.1) :=
      RingHom.flat_algebraMap_iff.mp (f.flat_appLE U.2 V.2 hVU)
    letI : Algebra.QuasiFinite Γ(X, U.1) Γ(Y, V.1) :=
      RingHom.quasiFinite_algebraMap.mp (LocallyQuasiFinite.quasiFinite_appLE U.2 V.2 hVU)
    ∀ F : FiniteOpenFactorization.{u, u, u} Γ(X, U.1) Γ(Y, V.1),
      D.localEquiv U V hVU F
          (restrictₗ D.sheaf (le_top : V.1 ≤ ⊤) (relativeTraceSection D)) =
        dualizingModule.traceCandidate F
```

## Tag 0C13, a lemma

[Tag 0C13](https://stacks.math.columbia.edu/tag/0C13) in the Stacks Project.

**`Stacks.Discriminant.trace_ne_zero_iff_isTraceElement_ne_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Discriminant/TraceNonvanishing.lean, line 259](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Discriminant/TraceNonvanishing.lean#L259). The attribute's comment: “conditions (1) and (2)”.

> **Stacks Project, Tag 0C13, (1) ⟺ (2).** For a finite algebra `A` over a field `k`, the
> algebra trace `Tr_{A/k}` is nonzero exactly when a trace element of the relative dualizing module
> is nonzero.
>
> The trace element is given by the predicate `Stacks.Discriminant.IsTraceElement` rather than
> chosen; by uniqueness (Tag 0BT7) this is a statement about a single determined element.

```lean
theorem trace_ne_zero_iff_isTraceElement_ne_zero (k : Type u) (A : Type v) [Field k] [CommRing A]
    [Algebra k A] [Module.Finite k A] (F : FiniteOpenFactorization.{u, v, w} k A)
    (τ : dualizingModule F) :
    letI : IsNoetherianRing A := IsNoetherianRing.of_finite k A
    IsTraceElement.{u, v, w, u, max u v, max u v} F τ → (Algebra.trace k A ≠ 0 ↔ τ ≠ 0)
```

**`Stacks.Discriminant.trace_ne_zero_iff_isSeparable_and_length_ne_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Discriminant/TraceNonvanishing.lean, line 298](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Discriminant/TraceNonvanishing.lean#L298). The attribute's comment: “conditions (1) and (3)”.

> **Stacks Project, Tag 0C13, (1) ⟺ (3).** For a finite local algebra `A` over a field `k`, the
> algebra trace `Tr_{A/k}` is nonzero exactly when the residue field of `A` is separable over `k`
> and the length of `A` is prime to the characteristic of `k`.
>
> "Prime to the characteristic" is the nonvanishing in `k` of the natural number `length_A(A)`, a
> condition that also covers characteristic zero.

```lean
theorem trace_ne_zero_iff_isSeparable_and_length_ne_zero (k : Type u) (A : Type v) [Field k]
    [CommRing A] [Algebra k A] [IsLocalRing A] [Module.Finite k A] :
    Algebra.trace k A ≠ 0 ↔
      Algebra.IsSeparable k (ResidueField A) ∧ ((Module.length A A).toNat : k) ≠ 0
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 49.4, Tag 0BSY](https://stacks.math.columbia.edu/tag/0BSY)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
