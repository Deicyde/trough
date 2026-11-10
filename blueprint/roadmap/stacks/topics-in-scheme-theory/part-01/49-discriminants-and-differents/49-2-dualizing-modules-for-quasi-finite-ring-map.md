---
declaration: section
origin: cited
lean: Stacks.Discriminant.dualizingModule, Stacks.Discriminant.exists_finite_subalgebra_dominating, Stacks.Discriminant.dualizingModuleEquiv, Stacks.Discriminant.dualizingModuleEquiv_tmul, Stacks.Discriminant.dualizingModuleEquiv_refl, Stacks.Discriminant.dualizingModuleEquiv_trans, Stacks.Discriminant.dualizingModule_equiv_of_isLocalization_away, Stacks.Discriminant.dualizingModule_equiv_of_isLocalization_away_tmul
statement: formalized
proof: formalized
---

# 49.2 Dualizing modules for quasi-finite ring maps

Section 49.2 of the Stacks Project, [Tag 0BUK](https://stacks.math.columbia.edu/tag/0BUK). 14 tags here are carried by 33 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BSZ, an equation

[Tag 0BSZ](https://stacks.math.columbia.edu/tag/0BSZ) in the Stacks Project.

**`Stacks.Discriminant.dualizingModule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Discriminant/TraceElement.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Discriminant/TraceElement.lean#L169).

> The relative dualizing module `Hom_A(B', A) ⊗_{B'} B` of a finite-open factorization
> `A → B' → B`.

```lean
def dualizingModule {A : Type u} {B : Type v}
    [CommRing A] [CommRing B] [Algebra A B]
    (F : FiniteOpenFactorization.{u, v, w} A B) : Type (max u v w)
```

## Tag 0BT0, a lemma

[Tag 0BT0](https://stacks.math.columbia.edu/tag/0BT0) in the Stacks Project.

**`Stacks.Discriminant.exists_finite_subalgebra_dominating`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/DualizingModulesQuasi/CommonFactorization.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/DualizingModulesQuasi/CommonFactorization.lean#L136).

> Two finite algebra factorizations, the first of which induces an open immersion on spectra,
> are dominated by a finite subalgebra inducing an open immersion.

```lean
lemma exists_finite_subalgebra_dominating
    {A : Type u} {B B₁ : Type v} {B₂ : Type w}
    [CommRing A] [CommRing B] [CommRing B₁] [CommRing B₂]
    [Algebra A B]
    [Algebra A B₁] [Module.Finite A B₁] [Algebra A B₂] [Module.Finite A B₂]
    (f₁ : B₁ →ₐ[A] B) (f₂ : B₂ →ₐ[A] B)
    [IsOpenImmersion (Spec.map (CommRingCat.ofHom f₁.toRingHom))] :
    ∃ C : Subalgebra A B,
      Module.Finite A C ∧
        IsOpenImmersion (Spec.map (CommRingCat.ofHom C.val.toRingHom)) ∧
          (∃ g₁ : B₁ →ₐ[A] C, C.val.comp g₁ = f₁) ∧
            ∃ g₂ : B₂ →ₐ[A] C, C.val.comp g₂ = f₂
```

## Tag 0BT1, a lemma

[Tag 0BT1](https://stacks.math.columbia.edu/tag/0BT1) in the Stacks Project.

**`Stacks.Discriminant.dualizingModuleEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Discriminant/DualizingModuleComparison.lean, line 237](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Discriminant/DualizingModuleComparison.lean#L237). The attribute's comment: “canonical comparison”.

> **Stacks Project, Tag 0BT1.** The dualizing modules obtained from any two
> finite-open factorizations are canonically equivalent as modules over the target.

```lean
noncomputable def dualizingModuleEquiv
    {A : Type u} {B : Type v} [CommRing A] [CommRing B] [Algebra A B]
    [IsNoetherianRing A]
    (F : FiniteOpenFactorization.{u, v, w} A B)
    (G : FiniteOpenFactorization.{u, v, x} A B) :
    dualizingModule F ≃ₗ[B] dualizingModule G
```

**`Stacks.Discriminant.dualizingModuleEquiv_tmul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Discriminant/DualizingModuleComparison.lean, line 311](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Discriminant/DualizingModuleComparison.lean#L311). The attribute's comment: “characterization on a common refinement”.

> The canonical comparison carries a tensor arising from a functional on a common finite-open
> refinement inside the target to the tensor induced by the same functional in the other
> factorization.  Injectivity of the map to the target expresses the subalgebra condition in
> Tag 0BT0 used by the source proof.

```lean
theorem dualizingModuleEquiv_tmul
    {A : Type u} {B : Type v} [CommRing A] [CommRing B] [Algebra A B]
    [IsNoetherianRing A]
    (F : FiniteOpenFactorization.{u, v, w} A B)
    (G : FiniteOpenFactorization.{u, v, x} A B)
    (H : FiniteOpenFactorization.{u, v, y} A B)
    (hH : Function.Injective (algebraMap H.middle B))
    (rF : F.middle →ₐ[A] H.middle)
    (rG : G.middle →ₐ[A] H.middle)
    (hF : ∀ c : F.middle,
      algebraMap H.middle B (rF c) = algebraMap F.middle B c)
    (hG : ∀ c : G.middle,
      algebraMap H.middle B (rG c) = algebraMap G.middle B c)
    (φ : Module.Dual A H.middle) (b : B) :
    dualizingModuleEquiv F G
        (dualizingModule.tmul F (φ.comp rF.toLinearMap) b) =
      dualizingModule.tmul G (φ.comp rG.toLinearMap) b
```

**`Stacks.Discriminant.dualizingModuleEquiv_refl`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Discriminant/DualizingModuleComparison.lean, line 332](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Discriminant/DualizingModuleComparison.lean#L332). The attribute's comment: “identity comparison”.

> The canonical comparison of a factorization with itself is the identity.

```lean
theorem dualizingModuleEquiv_refl
    {A : Type u} {B : Type v} [CommRing A] [CommRing B] [Algebra A B]
    [IsNoetherianRing A]
    (F : FiniteOpenFactorization.{u, v, w} A B) :
    dualizingModuleEquiv F F = LinearEquiv.refl B (dualizingModule F)
```

**`Stacks.Discriminant.dualizingModuleEquiv_trans`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Discriminant/DualizingModuleComparison.lean, line 385](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Discriminant/DualizingModuleComparison.lean#L385). The attribute's comment: “composition of comparisons”.

> Canonical comparisons compose independently of an intermediate factorization.

```lean
theorem dualizingModuleEquiv_trans
    {A : Type u} {B : Type v} [CommRing A] [CommRing B] [Algebra A B]
    [IsNoetherianRing A]
    (F : FiniteOpenFactorization.{u, v, w} A B)
    (G : FiniteOpenFactorization.{u, v, x} A B)
    (H : FiniteOpenFactorization.{u, v, y} A B) :
    (dualizingModuleEquiv F G).trans (dualizingModuleEquiv G H) =
      dualizingModuleEquiv F H
```

## Tag 0BT2, a lemma

[Tag 0BT2](https://stacks.math.columbia.edu/tag/0BT2) in the Stacks Project.

**`Stacks.Discriminant.dualizingModule_equiv_of_isLocalization_away`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Discriminant/BaseLocalization.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Discriminant/BaseLocalization.lean#L78). The attribute's comment: “part (1)”.

> **Stacks Project, Tag 0BT2, part (1).** If `A → B` factors through the localization of
> `A` away from `f`, then computing the relative dualizing module over that localization does not
> change it.

```lean
public noncomputable def dualizingModule_equiv_of_isLocalization_away
    {A : Type u} {B : Type v} {Af : Type w}
    [CommRing A] [CommRing B] [CommRing Af]
    [Algebra A B] [Algebra A Af] [Algebra Af B] [IsScalarTower A Af B]
    [IsNoetherianRing A] [IsNoetherianRing B] [Algebra.QuasiFinite A B]
    (f : A) [IsLocalization.Away f Af]
    (F : FiniteOpenFactorization.{u, v, x} A B)
    (G : FiniteOpenFactorization.{w, v, y} Af B) :
    dualizingModule F ≃ₗ[B] dualizingModule G
```

**`Stacks.Discriminant.dualizingModule_equiv_of_isLocalization_away_tmul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Discriminant/BaseLocalization.lean, line 373](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Discriminant/BaseLocalization.lean#L373). The attribute's comment: “part (1), characterization”.

> The base-localization identification carries a functional to its scalar extension along a
> compatible finite-open factorization.  The displayed equation characterizes this operation on
> generators and avoids treating the equivalence as an arbitrary module isomorphism.

```lean
public theorem dualizingModule_equiv_of_isLocalization_away_tmul
    {A : Type u} {B : Type v} {Af : Type w}
    [CommRing A] [CommRing B] [CommRing Af]
    [Algebra A B] [Algebra A Af] [Algebra Af B] [IsScalarTower A Af B]
    [IsNoetherianRing A] [IsNoetherianRing B] [Algebra.QuasiFinite A B]
    (f : A) [IsLocalization.Away f Af]
    (F : FiniteOpenFactorization.{u, v, x} A B)
    (G : FiniteOpenFactorization.{w, v, y} Af B)
    [Algebra A G.middle] [IsScalarTower A Af G.middle]
    (r : F.middle →ₐ[A] G.middle)
    (hrloc : letI := r.toRingHom.toAlgebra
      IsLocalization.Away (algebraMap A F.middle f) G.middle)
    (hr : ∀ c : F.middle,
      G.algebraTarget.algebraMap (r c) = F.algebraTarget.algebraMap c)
    (φ : Module.Dual A F.middle) (ψ : Module.Dual Af G.middle)
    (hψ : ∀ c : F.middle, ψ (r c) = algebraMap A Af (φ c)) (b : B) :
    dualizingModule_equiv_of_isLocalization_away f F G
        (dualizingModule.tmul F φ b) = dualizingModule.tmul G ψ b
```

**`Stacks.Discriminant.dualizingModule_equiv_of_isLocalization_away_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Discriminant/BaseLocalization.lean, line 664](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Discriminant/BaseLocalization.lean#L664). The attribute's comment: “part (1), naturality”.

> Changing either finite-open factorization does not change the base-localization map.

```lean
public theorem dualizingModule_equiv_of_isLocalization_away_natural
    {A : Type u} {B : Type v} {Af : Type w}
    [CommRing A] [CommRing B] [CommRing Af]
    [Algebra A B] [Algebra A Af] [Algebra Af B] [IsScalarTower A Af B]
    [IsNoetherianRing A] [IsNoetherianRing B] [IsNoetherianRing Af]
    [Algebra.QuasiFinite A B]
    (f : A) [IsLocalization.Away f Af]
    (F : FiniteOpenFactorization.{u, v, x} A B)
    (F' : FiniteOpenFactorization.{u, v, z} A B)
    (G : FiniteOpenFactorization.{w, v, y} Af B)
    (G' : FiniteOpenFactorization.{w, v, t} Af B) (m : dualizingModule F) :
    dualizingModuleEquiv G G'
        (dualizingModule_equiv_of_isLocalization_away f F G m) =
      dualizingModule_equiv_of_isLocalization_away f F' G'
        (dualizingModuleEquiv F F' m)
```

**`Stacks.Discriminant.localizedModule_dualizingModule_equiv_of_baseLocalization`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Discriminant/SimultaneousLocalization.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Discriminant/SimultaneousLocalization.lean#L53). The attribute's comment: “part (3)”.

> **Stacks Project, Tag 0BT2, part (3).** After localizing the base away from `f` and the
> target away from its image, the relative dualizing module is the corresponding localization of
> the original relative dualizing module.

```lean
public noncomputable def localizedModule_dualizingModule_equiv_of_baseLocalization
    {A : Type u} {B : Type v} {Af : Type w} {Bf : Type x} {M : Type y}
    [CommRing A] [CommRing B] [CommRing Af] [CommRing Bf]
    [Algebra A B] [Algebra A Af] [Algebra B Bf] [Algebra A Bf] [Algebra Af Bf]
    [IsScalarTower A B Bf] [IsScalarTower A Af Bf]
    [IsNoetherianRing A] [IsNoetherianRing B] [Algebra.QuasiFinite A B]
    (f : A) [IsLocalization.Away f Af]
    [IsLocalization.Away (algebraMap A B f) Bf]
    (F : FiniteOpenFactorization.{u, v, z} A B)
    (G : FiniteOpenFactorization.{w, x, q} Af Bf)
    [AddCommGroup M] [Module B M] [Module Bf M] [IsScalarTower B Bf M]
    (localizationMap : dualizingModule F →ₗ[B] M)
    (hM : IsLocalizedModule (Submonoid.powers (algebraMap A B f)) localizationMap) :
    M ≃ₗ[Bf] dualizingModule G
```

**`Stacks.Discriminant.localizedModule_dualizingModule_equiv_of_baseLocalization_eq_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Discriminant/SimultaneousLocalization.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Discriminant/SimultaneousLocalization.lean#L80). The attribute's comment: “part (3), compatibility with parts (1) and (2)”.

> Simultaneous localization is the composite of localization in the target and replacement
> of the base by its localization.  This fixes the canonical identification, rather than merely
> asserting the existence of a linear equivalence.

```lean
public theorem localizedModule_dualizingModule_equiv_of_baseLocalization_eq_comp
    {A : Type u} {B : Type v} {Af : Type w} {Bf : Type x} {M : Type y}
    [CommRing A] [CommRing B] [CommRing Af] [CommRing Bf]
    [Algebra A B] [Algebra A Af] [Algebra B Bf] [Algebra A Bf] [Algebra Af Bf]
    [IsScalarTower A B Bf] [IsScalarTower A Af Bf]
    [IsNoetherianRing A] [IsNoetherianRing B] [IsNoetherianRing Bf]
    [Algebra.QuasiFinite A B] [Algebra.QuasiFinite A Bf]
    (f : A) [IsLocalization.Away f Af]
    [IsLocalization.Away (algebraMap A B f) Bf]
    (F : FiniteOpenFactorization.{u, v, z} A B)
    (H : FiniteOpenFactorization.{u, x, t} A Bf)
    (G : FiniteOpenFactorization.{w, x, q} Af Bf)
    [AddCommGroup M] [Module B M] [Module Bf M] [IsScalarTower B Bf M]
    (localizationMap : dualizingModule F →ₗ[B] M)
    (hM : IsLocalizedModule (Submonoid.powers (algebraMap A B f)) localizationMap) :
    localizedModule_dualizingModule_equiv_of_baseLocalization
        f F G localizationMap hM =
      (localizedModule_dualizingModule_equiv
        (algebraMap A B f) F H localizationMap hM).trans
        (dualizingModule_equiv_of_isLocalization_away f H G)
```

**`Stacks.Discriminant.localizedModule_dualizingModule_equiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Discriminant/TargetLocalization.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Discriminant/TargetLocalization.lean#L58). The attribute's comment: “part (2)”.

> **Stacks Project, Tag 0BT2, part (2).** Localizing the relative dualizing module away from
> an element of the target gives the relative dualizing module of the localized target.

```lean
public noncomputable def localizedModule_dualizingModule_equiv
    {A : Type u} {B : Type v} {Bg : Type w} {M : Type x}
    [CommRing A] [CommRing B] [CommRing Bg]
    [Algebra A B] [Algebra B Bg] [Algebra A Bg] [IsScalarTower A B Bg]
    [IsNoetherianRing A] [IsNoetherianRing B] [Algebra.QuasiFinite A B]
    (g : B) [IsLocalization.Away g Bg]
    (F : FiniteOpenFactorization.{u, v, y} A B)
    (G : FiniteOpenFactorization.{u, w, z} A Bg)
    [AddCommGroup M] [Module B M] [Module Bg M] [IsScalarTower B Bg M]
    (localizationMap : dualizingModule F →ₗ[B] M)
    (hM : IsLocalizedModule (Submonoid.powers g) localizationMap) :
    M ≃ₗ[Bg] dualizingModule G
```

**`Stacks.Discriminant.localizedModule_dualizingModule_equiv_tmul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Discriminant/TargetLocalization.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Discriminant/TargetLocalization.lean#L108). The attribute's comment: “part (2), characterization”.

> On compatible finite-open factorizations, the target-localization map sends a pure tensor
> to the tensor obtained by localizing its coefficient in the target.

```lean
public theorem localizedModule_dualizingModule_equiv_tmul
    {A : Type u} {B : Type v} {Bg : Type w} {M : Type x}
    [CommRing A] [CommRing B] [CommRing Bg]
    [Algebra A B] [Algebra B Bg] [Algebra A Bg] [IsScalarTower A B Bg]
    [IsNoetherianRing A] [IsNoetherianRing B] [Algebra.QuasiFinite A B]
    (g : B) [IsLocalization.Away g Bg]
    (F : FiniteOpenFactorization.{u, v, y} A B)
    (G : FiniteOpenFactorization.{u, w, z} A Bg)
    [AddCommGroup M] [Module B M] [Module Bg M] [IsScalarTower B Bg M]
    (localizationMap : dualizingModule F →ₗ[B] M)
    (hM : IsLocalizedModule (Submonoid.powers g) localizationMap)
    (r : G.middle ≃ₐ[A] F.middle)
    (hr : ∀ c : G.middle,
      algebraMap B Bg (F.algebraTarget.algebraMap (r c)) =
        G.algebraTarget.algebraMap c)
    (φ : Module.Dual A F.middle) (b : B) :
    localizedModule_dualizingModule_equiv g F G localizationMap hM
        (localizationMap (dualizingModule.tmul F φ b)) =
      dualizingModule.tmul G (φ.comp r.toLinearMap) (algebraMap B Bg b)
```

**`Stacks.Discriminant.localizedModule_dualizingModule_equiv_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Discriminant/TargetLocalization.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Discriminant/TargetLocalization.lean#L162). The attribute's comment: “part (2), naturality”.

> The target-localization identification is natural in the finite-open factorization of the
> localized algebra.

```lean
public theorem localizedModule_dualizingModule_equiv_natural
    {A : Type u} {B : Type v} {Bg : Type w} {M : Type x}
    [CommRing A] [CommRing B] [CommRing Bg]
    [Algebra A B] [Algebra B Bg] [Algebra A Bg] [IsScalarTower A B Bg]
    [IsNoetherianRing A] [IsNoetherianRing B] [Algebra.QuasiFinite A B]
    (g : B) [IsLocalization.Away g Bg]
    (F : FiniteOpenFactorization.{u, v, y} A B)
    (G : FiniteOpenFactorization.{u, w, z} A Bg)
    (G' : FiniteOpenFactorization.{u, w, t} A Bg)
    [AddCommGroup M] [Module B M] [Module Bg M] [IsScalarTower B Bg M]
    (localizationMap : dualizingModule F →ₗ[B] M)
    (hM : IsLocalizedModule (Submonoid.powers g) localizationMap) (m : M) :
    dualizingModuleEquiv G G'
        (localizedModule_dualizingModule_equiv g F G localizationMap hM m) =
      localizedModule_dualizingModule_equiv g F G' localizationMap hM m
```

**`Stacks.Discriminant.localizedModule_dualizingModule_equiv_natural_in_source`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Discriminant/TargetLocalization.lean, line 233](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Discriminant/TargetLocalization.lean#L233). The attribute's comment: “part (2), naturality in both factorizations”.

> Localization commutes with the canonical comparison of two factorizations of the original
> algebra, as well as with the comparison of factorizations after localization.  A map between
> abstract localized modules is specified by its action on their localization maps.

```lean
public theorem localizedModule_dualizingModule_equiv_natural_in_source
    {A : Type u} {B : Type v} {Bg : Type w} {M : Type x} {M' : Type y}
    [CommRing A] [CommRing B] [CommRing Bg]
    [Algebra A B] [Algebra B Bg] [Algebra A Bg] [IsScalarTower A B Bg]
    [IsNoetherianRing A] [IsNoetherianRing B] [Algebra.QuasiFinite A B]
    (g : B) [IsLocalization.Away g Bg]
    (F : FiniteOpenFactorization.{u, v, z} A B)
    (F' : FiniteOpenFactorization.{u, v, t} A B)
    (G : FiniteOpenFactorization.{u, w, q} A Bg)
    (G' : FiniteOpenFactorization.{u, w, s} A Bg)
    [AddCommGroup M] [Module B M] [Module Bg M] [IsScalarTower B Bg M]
    [AddCommGroup M'] [Module B M'] [Module Bg M'] [IsScalarTower B Bg M']
    (localizationMap : dualizingModule F →ₗ[B] M)
    (hM : IsLocalizedModule (Submonoid.powers g) localizationMap)
    (localizationMap' : dualizingModule F' →ₗ[B] M')
    (hM' : IsLocalizedModule (Submonoid.powers g) localizationMap')
    (comparison : M →ₗ[Bg] M')
    (hcomparison : ∀ m : dualizingModule F,
      comparison (localizationMap m) =
        localizationMap' (dualizingModuleEquiv F F' m))
    (m : M) :
    dualizingModuleEquiv G G'
        (localizedModule_dualizingModule_equiv g F G localizationMap hM m) =
      localizedModule_dualizingModule_equiv g F' G' localizationMap' hM'
        (comparison m)
```

## Tag 0BVB, an equation

[Tag 0BVB](https://stacks.math.columbia.edu/tag/0BVB) in the Stacks Project.

**`Stacks.Discriminant.dualizingModule.baseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/DualizingModulesQuasi/BaseChange.lean, line 492](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/DualizingModulesQuasi/BaseChange.lean#L492). The attribute's comment: “the base change map”.

> **Stacks Project, Tag 0BVB.** The canonical base change map on relative dualizing
> modules, computed using a chosen finite-open factorization.  On the dual factor it extends
> `φ : B' →ₗ[A] A` to the `A₁`-linear map sending `a₁ ⊗ b'` to
> `a₁ * algebraMap A A₁ (φ b')`; tensoring this map with `B → A₁ ⊗[A] B` gives the displayed
> map.

```lean
noncomputable def baseChange (F : FiniteOpenFactorization.{u, v, w} A B)
    (A₁ : Type x) [CommRing A₁] [Algebra A A₁] :
    letI : Algebra B (A₁ ⊗[A] B) := Algebra.TensorProduct.rightAlgebra
    letI : Module B
        (dualizingModule (FiniteOpenFactorization.baseChange F A₁)) :=
      Module.compHom _ (algebraMap B (A₁ ⊗[A] B))
    dualizingModule F →ₗ[B]
      dualizingModule (FiniteOpenFactorization.baseChange F A₁)
```

**`Stacks.Discriminant.dualizingModule.baseChange_tmul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/DualizingModulesQuasi/BaseChange.lean, line 627](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/DualizingModulesQuasi/BaseChange.lean#L627). The attribute's comment: “pure tensor formula”.

> On a pure tensor, the relative-dualizing base change map extends the dual functional
> and sends the coefficient to its scalar extension.

```lean
theorem baseChange_tmul (F : FiniteOpenFactorization.{u, v, w} A B)
    (A₁ : Type x) [CommRing A₁] [Algebra A A₁]
    (f : Module.Dual A F.middle) (b : B) :
    letI : Algebra B (A₁ ⊗[A] B) := Algebra.TensorProduct.rightAlgebra
    letI : Module B
        (dualizingModule (FiniteOpenFactorization.baseChange F A₁)) :=
      Module.compHom _ (algebraMap B (A₁ ⊗[A] B))
    baseChange F A₁ (dualizingModule.tmul F f b) =
      dualizingModule.tmul (FiniteOpenFactorization.baseChange F A₁)
        (f.baseChange A₁) (1 ⊗ₜ[A] b)
```

## Tag 0BVC, a lemma

[Tag 0BVC](https://stacks.math.columbia.edu/tag/0BVC) in the Stacks Project.

**`Stacks.Discriminant.dualizingModule.baseChange_congr`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Discriminant/DualizingBaseChange/Independence.lean, line 240](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Discriminant/DualizingBaseChange/Independence.lean#L240). The attribute's comment: “independence of factorization”.

> The base change map respects the canonical identification between dualizing
> modules computed using two finite-open factorizations.

```lean
theorem baseChange_congr
    {A : Type u} {B : Type v} [CommRing A] [CommRing B] [Algebra A B]
    [IsNoetherianRing A]
    (F : FiniteOpenFactorization.{u, v, w} A B)
    (G : FiniteOpenFactorization.{u, v, x} A B)
    (A₁ : Type y) [CommRing A₁] [Algebra A A₁] [IsNoetherianRing A₁]
    (ω : dualizingModule F) :
    dualizingModuleEquiv
        (FiniteOpenFactorization.baseChange F A₁)
        (FiniteOpenFactorization.baseChange G A₁)
        (dualizingModule.baseChange F A₁ ω) =
      dualizingModule.baseChange G A₁
        (dualizingModuleEquiv F G ω)
```

**`Stacks.Discriminant.dualizingModule.baseChange_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Discriminant/DualizingBaseChange/Tower.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Discriminant/DualizingBaseChange/Tower.lean#L195). The attribute's comment: “composition of base changes”.

> Successive base change maps agree with direct base change after the
> canonical identification of the iterated tensor product with the direct one.

```lean
theorem baseChange_comp
    {A : Type u} {B : Type v} [CommRing A] [CommRing B] [Algebra A B]
    (F : FiniteOpenFactorization.{u, v, w} A B)
    (A₁ : Type x) [CommRing A₁] [Algebra A A₁]
    (A₂ : Type y) [CommRing A₂] [Algebra A A₂] [Algebra A₁ A₂]
    [IsScalarTower A A₁ A₂]
    (ω : dualizingModule F) :
    (baseChangeTowerEquiv F A₁ A₂).1
        (dualizingModule.baseChange
          (FiniteOpenFactorization.baseChange F A₁) A₂
          (dualizingModule.baseChange F A₁ ω)) =
      dualizingModule.baseChange F A₂ ω
```

## Tag 0BT3, a lemma

[Tag 0BT3](https://stacks.math.columbia.edu/tag/0BT3) in the Stacks Project.

**`Stacks.Discriminant.dualizingModule_isBaseChange_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/DualizingModulesQuasi/FlatBaseChange.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/DualizingModulesQuasi/FlatBaseChange.lean#L48).

> **Stacks Project, Tag 0BT3.** Flat base change identifies the scalar extension of
> the relative dualizing module with the relative dualizing module after base change.

```lean
theorem dualizingModule_isBaseChange_of_flat
    {A : Type u} {B : Type v} [CommRing A] [CommRing B] [Algebra A B]
    [IsNoetherianRing A]
    (F : FiniteOpenFactorization.{u, v, w} A B)
    (A₁ : Type x) [CommRing A₁] [Algebra A A₁] [Module.Flat A A₁] :
    letI : Algebra B (A₁ ⊗[A] B) := Algebra.TensorProduct.rightAlgebra
    letI : Module B
        (dualizingModule (FiniteOpenFactorization.baseChange F A₁)) :=
      Module.compHom _ (algebraMap B (A₁ ⊗[A] B))
    letI : IsScalarTower B (A₁ ⊗[A] B)
        (dualizingModule (FiniteOpenFactorization.baseChange F A₁)) :=
      IsScalarTower.of_algebraMap_smul (fun _ _ => rfl)
    IsBaseChange (A₁ ⊗[A] B) (dualizingModule.baseChange F A₁)
```

## Tag 0BT4, a lemma

[Tag 0BT4](https://stacks.math.columbia.edu/tag/0BT4) in the Stacks Project.

**`Stacks.Discriminant.dualizingModule.comp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Discriminant/DualizingComposition/Basic.lean, line 378](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Discriminant/DualizingComposition/Basic.lean#L378).

> **Stacks Project, Tag 0BT4.** The canonical composition map for relative
> dualizing modules of two composable quasi-finite algebra maps.

```lean
noncomputable def comp
    {A : Type u} {B : Type v} {C : Type w}
    [CommRing A] [CommRing B] [CommRing C]
    [Algebra A B] [Algebra B C] [Algebra A C] [IsScalarTower A B C]
    [IsNoetherianRing A] [IsNoetherianRing B] [IsNoetherianRing C]
    (F : FiniteOpenFactorization.{u, v, x} A B)
    (G : FiniteOpenFactorization.{v, w, y} B C)
    (H : FiniteOpenFactorization.{u, w, z} A C) :
    letI : Module B (dualizingModule G) :=
      Module.compHom _ (algebraMap B C)
    letI : SMulCommClass B C (dualizingModule G) :=
      ⟨fun b c m => by
        change (algebraMap B C b) • c • m = c • (algebraMap B C b) • m
        rw [smul_comm]⟩
    letI : Module C
        (dualizingModule G ⊗[B] dualizingModule F) :=
      TensorProduct.leftModule
    letI : Module C
        (dualizingModule F ⊗[B] dualizingModule G) :=
      (TensorProduct.comm B (dualizingModule F)
        (dualizingModule G)).toAddEquiv.module C
    (dualizingModule F ⊗[B] dualizingModule G) →ₗ[C]
      dualizingModule H
```

**`Stacks.Discriminant.dualizingModule.comp_of_compatible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Discriminant/DualizingComposition/Basic.lean, line 471](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Discriminant/DualizingComposition/Basic.lean#L471). The attribute's comment: “composition of Hom maps for compatible factorizations”.

> For compatible finite-open factorizations, a functional on the middle
> algebra that descends to the finite intermediate algebra composes with the
> first functional. This applies to nonfinite quasi-finite maps as well.

```lean
theorem comp_of_compatible
    {A : Type u} {B : Type v} {C : Type w}
    [CommRing A] [CommRing B] [CommRing C]
    [Algebra A B] [Algebra B C] [Algebra A C] [IsScalarTower A B C]
    [IsNoetherianRing A] [IsNoetherianRing B] [IsNoetherianRing C]
    (F : FiniteOpenFactorization.{u, v, x} A B)
    (G : FiniteOpenFactorization.{v, w, y} B C)
    (H : FiniteOpenFactorization.{u, w, z} A C)
    [Algebra F.middle H.middle] [IsScalarTower A F.middle H.middle]
    (j : H.middle →+* G.middle)
    (hjF : ∀ s : F.middle,
      j (algebraMap F.middle H.middle s) =
        algebraMap B G.middle (algebraMap F.middle B s))
    (hjC : ∀ t : H.middle,
      algebraMap G.middle C (j t) = algebraMap H.middle C t)
    (hjspan : Submodule.span B (Set.range j) = ⊤)
    (f : Module.Dual A F.middle) (g : Module.Dual B G.middle)
    (g' : Module.Dual F.middle H.middle)
    (hg : ∀ t : H.middle, g (j t) = algebraMap F.middle B (g' t))
    (d : F.middle) (c : C) :
    letI : Module B (dualizingModule G) :=
      Module.compHom _ (algebraMap B C)
    letI : SMulCommClass B C (dualizingModule G) :=
      ⟨fun b c m => by
        change (algebraMap B C b) • c • m = c • (algebraMap B C b) • m
        rw [smul_comm]⟩
    letI : Module C
        (dualizingModule G ⊗[B] dualizingModule F) :=
      TensorProduct.leftModule
    letI : Module C
        (dualizingModule F ⊗[B] dualizingModule G) :=
      (TensorProduct.comm B (dualizingModule F)
        (dualizingModule G)).toAddEquiv.module C
    ∃ h : Module.Dual A H.middle,
      (comp F G H ((dualizingModule.tmul F f
          (algebraMap F.middle B d)) ⊗ₜ[B]
        (dualizingModule.tmul G g c)) =
          dualizingModule.tmul H h c) ∧
      (∀ t : H.middle,
        h t = f (d * g' t))
```

**`Stacks.Discriminant.dualizingModule.comp_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Discriminant/DualizingComposition/Basic.lean, line 554](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Discriminant/DualizingComposition/Basic.lean#L554). The attribute's comment: “independence of factorization”.

> The composition map commutes with the canonical comparison isomorphisms
> when any of the three finite-open factorizations is changed.

```lean
theorem comp_naturality
    {A : Type u} {B : Type v} {C : Type w}
    [CommRing A] [CommRing B] [CommRing C]
    [Algebra A B] [Algebra B C] [Algebra A C] [IsScalarTower A B C]
    [IsNoetherianRing A] [IsNoetherianRing B] [IsNoetherianRing C]
    (F : FiniteOpenFactorization.{u, v, x} A B)
    (G : FiniteOpenFactorization.{v, w, y} B C)
    (H : FiniteOpenFactorization.{u, w, z} A C)
    (F' : FiniteOpenFactorization.{u, v, x'} A B)
    (G' : FiniteOpenFactorization.{v, w, y'} B C)
    (H' : FiniteOpenFactorization.{u, w, z'} A C)
    (ω : dualizingModule F)
    (η : dualizingModule G) :
    letI : Module B (dualizingModule G) :=
      Module.compHom _ (algebraMap B C)
    letI : SMulCommClass B C (dualizingModule G) :=
      ⟨fun b c m => by
        change (algebraMap B C b) • c • m = c • (algebraMap B C b) • m
        rw [smul_comm]⟩
    letI : Module C
        (dualizingModule G ⊗[B] dualizingModule F) :=
      TensorProduct.leftModule
    letI : Module C
        (dualizingModule F ⊗[B] dualizingModule G) :=
      (TensorProduct.comm B (dualizingModule F)
        (dualizingModule G)).toAddEquiv.module C
    letI : Module B (dualizingModule G') :=
      Module.compHom _ (algebraMap B C)
    letI : SMulCommClass B C (dualizingModule G') :=
      ⟨fun b c m => by
        change (algebraMap B C b) • c • m = c • (algebraMap B C b) • m
        rw [smul_comm]⟩
    letI : Module C
        (dualizingModule G' ⊗[B] dualizingModule F') :=
      TensorProduct.leftModule
    letI : Module C
        (dualizingModule F' ⊗[B] dualizingModule G') :=
      (TensorProduct.comm B (dualizingModule F')
        (dualizingModule G')).toAddEquiv.module C
    comp F' G' H'
        ((dualizingModuleEquiv F F' ω) ⊗ₜ[B]
          (dualizingModuleEquiv G G' η)) =
      dualizingModuleEquiv H H' (comp F G H (ω ⊗ₜ[B] η))
```

## Tag 0BT5, a lemma

[Tag 0BT5](https://stacks.math.columbia.edu/tag/0BT5) in the Stacks Project.

**`Stacks.Discriminant.dualizingModuleProdEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Discriminant/DualizingModuleProduct.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Discriminant/DualizingModuleProduct.lean#L89).

> **Stacks Project, Tag 0BT5.** The dualizing module of a product of quasi-finite
> Noetherian algebras is canonically the product of their dualizing modules.

```lean
noncomputable def dualizingModuleProdEquiv
    {A : Type u} {B : Type v} {C : Type w}
    [CommRing A] [CommRing B] [CommRing C]
    [Algebra A B] [Algebra A C]
    [IsNoetherianRing A] [IsNoetherianRing B] [IsNoetherianRing C]
    [Algebra.QuasiFinite A B] [Algebra.QuasiFinite A C]
    (F : FiniteOpenFactorization.{u, max v w, x} A (B × C))
    (FB : FiniteOpenFactorization.{u, v, y} A B)
    (FC : FiniteOpenFactorization.{u, w, z} A C) :
    letI : Module (B × C) (dualizingModule FB) :=
      Module.compHom _ (RingHom.fst B C)
    letI : Module (B × C) (dualizingModule FC) :=
      Module.compHom _ (RingHom.snd B C)
    dualizingModule F ≃ₗ[B × C] (dualizingModule FB × dualizingModule FC)
```

**`Stacks.Discriminant.dualizingModuleProdEquiv_tmul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Discriminant/DualizingModuleProduct.lean, line 473](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Discriminant/DualizingModuleProduct.lean#L473). The attribute's comment: “pure-tensor formula for a product factorization”.

> For a product factorization, the product equivalence sends a pure tensor to the pair
> obtained by restricting its functional to the two factors and projecting its coefficient.
> The compatibility condition identifies the map from the middle algebra to the product target
> with the componentwise maps.

```lean
theorem dualizingModuleProdEquiv_tmul
    {A : Type u} {B : Type v} {C : Type w}
    [CommRing A] [CommRing B] [CommRing C]
    [Algebra A B] [Algebra A C]
    [IsNoetherianRing A] [IsNoetherianRing B] [IsNoetherianRing C]
    [Algebra.QuasiFinite A B] [Algebra.QuasiFinite A C]
    (F : FiniteOpenFactorization.{u, max v w, x} A (B × C))
    (FB : FiniteOpenFactorization.{u, v, y} A B)
    (FC : FiniteOpenFactorization.{u, w, z} A C)
    (e : (FB.middle × FC.middle) ≃ₐ[A] F.middle)
    (hcompat : ∀ p : FB.middle × FC.middle,
      (algebraMap F.middle (B × C)) (e p) =
        ((algebraMap FB.middle B) p.1, (algebraMap FC.middle C) p.2))
    (f : Module.Dual A F.middle) (b : B) (c : C) :
    (dualizingModuleProdEquiv F FB FC) (dualizingModule.tmul F f (b, c)) =
      (dualizingModule.tmul FB
        (f.comp (e.toLinearMap.comp (LinearMap.inl A FB.middle FC.middle))) b,
       dualizingModule.tmul FC
        (f.comp (e.toLinearMap.comp (LinearMap.inr A FB.middle FC.middle))) c)
```

**`Stacks.Discriminant.dualizingModuleProdEquiv_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Discriminant/DualizingModuleProduct.lean, line 605](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Discriminant/DualizingModuleProduct.lean#L605). The attribute's comment: “independence of factorization”.

> Changing the finite-open factorizations of the product and its two factors commutes
> with the canonical product equivalence.

```lean
theorem dualizingModuleProdEquiv_naturality
    {A : Type u} {B : Type v} {C : Type w}
    [CommRing A] [CommRing B] [CommRing C]
    [Algebra A B] [Algebra A C]
    [IsNoetherianRing A] [IsNoetherianRing B] [IsNoetherianRing C]
    [Algebra.QuasiFinite A B] [Algebra.QuasiFinite A C]
    (F : FiniteOpenFactorization.{u, max v w, x} A (B × C))
    (G : FiniteOpenFactorization.{u, max v w, x'} A (B × C))
    (FB : FiniteOpenFactorization.{u, v, y} A B)
    (GB : FiniteOpenFactorization.{u, v, y'} A B)
    (FC : FiniteOpenFactorization.{u, w, z} A C)
    (GC : FiniteOpenFactorization.{u, w, z'} A C)
    (ω : dualizingModule F) :
    (dualizingModuleProdEquiv G GB GC) (dualizingModuleEquiv F G ω) =
      (dualizingModuleEquiv FB GB
        ((dualizingModuleProdEquiv F FB FC ω).1),
       dualizingModuleEquiv FC GC
        ((dualizingModuleProdEquiv F FB FC ω).2))
```

## Tag 0BVD, a lemma

[Tag 0BVD](https://stacks.math.columbia.edu/tag/0BVD) in the Stacks Project.

**`Stacks.Discriminant.mem_associatedPrimes_dualizingModule_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/DualizingModulesQuasi/AssociatedPrimes.lean, line 500](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/DualizingModulesQuasi/AssociatedPrimes.lean#L500).

> **Stacks Project, Tag 0BVD.** A prime of an algebra with a finite-open factorization
> is associated to its relative dualizing module if and only if it lies over an associated
> prime of the base.

```lean
public theorem mem_associatedPrimes_dualizingModule_iff
    {A : Type u} {B : Type v} [CommRing A] [CommRing B] [Algebra A B]
    [IsNoetherianRing A] [IsNoetherianRing B]
    (F : FiniteOpenFactorization.{u, v, w} A B) (q : PrimeSpectrum B) :
    q.asIdeal ∈ associatedPrimes B (dualizingModule F) ↔
      q.asIdeal.comap (algebraMap A B) ∈ associatedPrimes A A
```

## Tag 0BVE, a lemma

[Tag 0BVE](https://stacks.math.columbia.edu/tag/0BVE) in the Stacks Project.

**`Stacks.Discriminant.dualizingModule_flat`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Discriminant/FlatOverBase.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Discriminant/FlatOverBase.lean#L133).

> **Stacks Project, Tag 0BVE.** The relative dualizing module of a flat quasi-finite
> homomorphism of Noetherian rings is flat over the base ring.

```lean
public lemma dualizingModule_flat
    {A : Type u} {B : Type v} [CommRing A] [CommRing B] [Algebra A B]
    [IsNoetherianRing A] [IsNoetherianRing B] [Algebra.FiniteType A B]
    [Algebra.QuasiFinite A B] [Module.Flat A B]
    (F : FiniteOpenFactorization.{u, v, w} A B) :
    letI : Module A (dualizingModule F) :=
      Module.compHom (dualizingModule F) (algebraMap A B)
    Module.Flat A (dualizingModule F)
```

## Tag 0BVF, a lemma

[Tag 0BVF](https://stacks.math.columbia.edu/tag/0BVF) in the Stacks Project.

**`Stacks.Discriminant.dualizingModule.baseChangeLinearMap_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/DualizingModulesQuasi/FlatAlgebraBaseChange/Bijective.lean, line 547](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/DualizingModulesQuasi/FlatAlgebraBaseChange/Bijective.lean#L547).

> **Stacks Project, Tag 0BVF.** For a flat quasi-finite algebra over a Noetherian
> base, arbitrary base change induces an isomorphism of relative dualizing modules.

```lean
theorem baseChangeLinearMap_bijective
    (F : FiniteOpenFactorization.{u, v, w} A B)
    [IsNoetherianRing A] [Module.Flat A B]
    (A₁ : Type x) [CommRing A₁] [Algebra A A₁] :
    Function.Bijective (baseChangeLinearMap F A₁)
```

## Tag 0BVG, a remark

[Tag 0BVG](https://stacks.math.columbia.edu/tag/0BVG) in the Stacks Project.

**`Stacks.Discriminant.exists_relativeDualizingModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizingModuleExistence0BVG.lean, line 574](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizingModuleExistence0BVG.lean#L574). The attribute's comment: “existence”.

> **The relative dualizing module of a locally quasi-finite morphism of locally Noetherian
> schemes exists.** There is a coherent quasi-coherent `𝒪_Y`-module whose sections over every
> affine chart of `f` are the algebraic relative dualizing module of that chart, compatibly with
> restriction inside a chart and with the chart comparison over the adapted opens.
>
> This is `exists_relativeDualizingModule_of_hubRestrict` with its hypothesis discharged by
> `hubRestrict`.

```lean
public theorem exists_relativeDualizingModule :
    ∃ (M : Y.Modules)
      (c : ∀ (i : AdaptedOpen f) (W : Y.Opens), W ≤ i.source.1 →
        Γ(M, W) ≃ₗ[Γ(Y, W)] Γ(adaptedChartSheaf f i, W)),
      M.IsQuasicoherent ∧ _root_.SheafOfModules.IsCoherent M ∧
        (∀ (i : AdaptedOpen f) (W W' : Y.Opens) (hW : W ≤ i.source.1) (h : W' ≤ W)
          (s : Γ(M, W)),
          c i W' (h.trans hW) (M.presheaf.map (homOfLE h).op s) =
            (adaptedChartSheaf f i).presheaf.map (homOfLE h).op (c i W hW s)) ∧
        (∀ (k i j : AdaptedOpen f) (hki : k.Good i.source i.base)
          (hkj : k.Good j.source j.base) (s : Γ(M, k.source.1)),
          c j k.source.1 hkj.le s =
            adaptedSheafComparison f k i j hki hkj (c i k.source.1 hki.le s))
```

**`Stacks.Discriminant.nonempty_relativeDualizingModuleData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizingModuleExistence0BVG.lean, line 605](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizingModuleExistence0BVG.lean#L605). The attribute's comment: “existence, with the chart identifications”.

> **The relative dualizing module of Tag 0BVG, as chart data.** For a morphism locally of
> finite type and locally quasi-finite between locally Noetherian schemes, the module of
> `Stacks.Discriminant.exists_relativeDualizingModule` carries the data of a
> `Stacks.Discriminant.RelativeDualizingModuleData`: identifications of its sections over every
> affine chart with the algebraic relative dualizing module of that chart, independent of the
> finite-open factorization and compatible with shrinking the base chart or the source chart to a
> principal open.
>
> The identification over a chart `(U, V)` is the gluing comparison at the adapted open `(V, U)`
> followed by the hub of that adapted open at itself.  The hubs of one adapted open at two charts
> good for it agree on glued sections, so the two compatibilities are the explicit forms
> `hubRestrict_of_source_eq_of_basicOpen` and `hubRestrict_of_base_eq_of_basicOpen` of the
> restriction compatibility of the hubs.

```lean
public theorem nonempty_relativeDualizingModuleData : Nonempty (RelativeDualizingModuleData f)
```

**`Stacks.Discriminant.existsUnique_relativeDualizingComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizingModuleUniqueness0BVG.lean, line 328](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizingModuleUniqueness0BVG.lean#L328). The attribute's comment: “uniqueness”.

> **Stacks Project, Tag 0BVG, uniqueness.** The relative dualizing module of a locally
> quasi-finite morphism of locally Noetherian schemes is unique: any two coherent `𝒪_Y`-modules
> carrying the chart data of Tag 0BVG are related by one and only one isomorphism of their sections
> over every open of the source which is compatible with the restriction maps and which carries the
> identification of the sections over every affine chart `Spec(B) = V ⊆ Y`, `Spec(A) = U ⊆ X` with
> `f(V) ⊆ U` with `ω_{B/A}` to the other.
>
> As in the source, uniqueness is uniqueness up to the canonical isomorphism: the two modules are
> two sheaves and cannot be literally equal, and what is asserted is that the identifications
> `H⁰(V, ω_{Y/X}) = ω_{B/A}` determine the comparison between them completely.

```lean
public theorem existsUnique_relativeDualizingComparison
    (D D' : RelativeDualizingModuleData f) [LocallyOfFiniteType f] :
    ∃! E : ∀ W : Y.Opens, Γ(D.sheaf, W) ≃ₗ[Γ(Y, W)] Γ(D'.sheaf, W),
      (∀ (W W' : Y.Opens) (h : W' ≤ W) (s : Γ(D.sheaf, W)),
          E W' (restrictₗ D.sheaf h s) = restrictₗ D'.sheaf h (E W s)) ∧
        ∀ (U : X.affineOpens) (V : Y.affineOpens) (hVU : V.1 ≤ f ⁻¹ᵁ U.1),
          letI : Algebra Γ(X, U.1) Γ(Y, V.1) := (f.appLE U V hVU).hom.toAlgebra
          ∀ (F : FiniteOpenFactorization.{u, u, u} Γ(X, U.1) Γ(Y, V.1))
            (s : Γ(D.sheaf, V.1)),
            D'.localEquiv U V hVU F (E V.1 s) = D.localEquiv U V hVU F s
```

## Tag 0C0I, a lemma

[Tag 0C0I](https://stacks.math.columbia.edu/tag/0C0I) in the Stacks Project.

**`Dualizing.nonempty_dualizingModule_linearEquiv_homologyZero_relativeDualizingComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UpperShriek/QuasiFiniteDualizingModule.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/UpperShriek/QuasiFiniteDualizingModule.lean#L227). The attribute's comment: “ω_{B/A} = H⁰(ω•_{B/A}), the source's isomorphism being nonunique”.

> **Stacks Project, Tag 0C0I.**  Let `A → B` be a quasi-finite homomorphism of Noetherian rings
> and let `ω•_{B/A}` be its algebraic relative dualizing complex.  Then the relative dualizing
> module `ω_{B/A} = Hom_A(B', A) ⊗_{B'} B` of a finite-open factorization `A → B' → B` is
> isomorphic to `H⁰(ω•_{B/A})` as a `B`-module.
>
> The source's isomorphism is *nonunique*, so the conclusion is the existence of a `B`-linear
> equivalence rather than the invertibility of a named map.

```lean
public theorem nonempty_dualizingModule_linearEquiv_homologyZero_relativeDualizingComplex
    {A B : Type u} [CommRing A] [CommRing B] [Algebra A B]
    [IsNoetherianRing A] [IsNoetherianRing B] [Algebra.QuasiFinite A B]
    (F : FiniteOpenFactorization.{u, u, u} A B)
    (p : PolynomialPresentation (algebraMap A B)) :
    Nonempty (dualizingModule F ≃ₗ[B]
      ↥((DerivedCategory.homologyFunctor (ModuleCat.{u} B) 0).obj
        p.relativeDualizingComplex))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 49.2, Tag 0BUK](https://stacks.math.columbia.edu/tag/0BUK)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
