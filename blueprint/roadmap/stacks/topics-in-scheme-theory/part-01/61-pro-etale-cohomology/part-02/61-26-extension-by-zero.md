---
declaration: section
origin: cited
lean: AlgebraicGeometry.ProEtale.Abelian.exists_extensionByZero, AlgebraicGeometry.ProEtale.Abelian.sheafifiedExtensionByZero, AlgebraicGeometry.ProEtale.Abelian.sheafifiedExtensionByZeroAdjunction, AlgebraicGeometry.ProEtale.Modules.exists_extensionByZero, AlgebraicGeometry.ProEtale.Modules.sheafifiedExtensionByZero, AlgebraicGeometry.ProEtale.Modules.sheafifiedExtensionByZeroAdjunction, AlgebraicGeometry.ProEtale.Sets.extensionByZero, AlgebraicGeometry.ProEtale.Sets.extensionByZeroAdjunction
statement: formalized
proof: formalized
---

# 61.26 Extension by zero

Section 61.26 of the Stacks Project, [Tag 09AD](https://stacks.math.columbia.edu/tag/09AD). 6 tags here are carried by 30 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 09AE, a definition

[Tag 09AE](https://stacks.math.columbia.edu/tag/09AE) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.Abelian.exists_extensionByZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/Abelian.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/Abelian.lean#L75). The attribute's comment: “extension\_by\_zero\_abelian”. References: SGA 4 IV (11.3.1), “pro-étale site, Ab”.

> Restriction of abelian pro-étale sheaves has a left adjoint.

```lean
theorem exists_extensionByZero {U X : Scheme.{u}} (j : U ⟶ X) [WeaklyEtale j] :
    Nonempty (Σ F : Sheaf (Scheme.ProEt.topology U) AddCommGrpCat.{max (u + 1) v} ⥤
      Sheaf (Scheme.ProEt.topology X) AddCommGrpCat.{max (u + 1) v},
        F ⊣ proetaleRestriction j)
```

**`AlgebraicGeometry.ProEtale.Abelian.sheafifiedExtensionByZero`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/Abelian.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/Abelian.lean#L109). The attribute's comment: “(2), the functor j\_! : Ab(U\_proetale) -> Ab(X\_proetale) called extension by zero, as explicit data: the sheafification of the left Kan extension along the opposite of postcomposition by j”.

> Extension by zero of abelian sheaves on the small pro-étale site, as an explicit functor:
> the composite of the inclusion of sheaves into presheaves, left Kan extension along the
> opposite of postcomposition by `j`, and sheafification.

```lean
def sheafifiedExtensionByZero {U X : Scheme.{u}} (j : U ⟶ X) [WeaklyEtale j] :
    Sheaf (Scheme.ProEt.topology U) AddCommGrpCat.{max (u + 1) v} ⥤
      Sheaf (Scheme.ProEt.topology X) AddCommGrpCat.{max (u + 1) v}
```

**`AlgebraicGeometry.ProEtale.Abelian.sheafifiedExtensionByZeroAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/Abelian.lean, line 121](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/Abelian.lean#L121). The attribute's comment: “(2), the adjunction j\_! ⊣ j^\{-1} on abelian sheaves, witnessing that restriction along a weakly étale morphism has extension by zero as a left adjoint”.

> The explicit extension-by-zero functor is left adjoint to restriction.

```lean
def sheafifiedExtensionByZeroAdjunction {U X : Scheme.{u}} (j : U ⟶ X) [WeaklyEtale j] :
    sheafifiedExtensionByZero.{u, v} j ⊣ proetaleRestriction.{u, v} j
```

**`AlgebraicGeometry.ProEtale.Modules.exists_extensionByZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/Modules.lean, line 154](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/Modules.lean#L154). The attribute's comment: “extension\_by\_zero\_modules”. References: SGA 4 IV (11.3.1), “pro-étale, Λ-modules”.

> Restriction of pro-étale module sheaves has a left adjoint.

```lean
theorem exists_extensionByZero {U X : Scheme.{u}} (j : U ⟶ X) [WeaklyEtale j]
    (Λ : Type v) [Ring Λ] :
    Nonempty (Σ F : Sheaf (Scheme.ProEt.topology U) (ModuleCat.{max (u + 1) w} Λ) ⥤
      Sheaf (Scheme.ProEt.topology X) (ModuleCat.{max (u + 1) w} Λ),
        F ⊣ proetaleRestriction j Λ)
```

**`AlgebraicGeometry.ProEtale.Modules.sheafifiedExtensionByZero`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/Modules.lean, line 195](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/Modules.lean#L195). The attribute's comment: “(3), the functor j\_! : Mod(U\_proetale, Λ) -> Mod(X\_proetale, Λ) called extension by zero, as explicit data: the sheafification of the left Kan extension along the opposite of postcomposition by j”.

> Extension by zero of pro-étale sheaves of `Λ`-modules, as an explicit functor: the
> composite of the inclusion of sheaves into presheaves, left Kan extension along the opposite
> of postcomposition by `j`, and sheafification.

```lean
def sheafifiedExtensionByZero {U X : Scheme.{u}} (j : U ⟶ X) [WeaklyEtale j]
    (Λ : Type v) [Ring Λ] :
    Sheaf (Scheme.ProEt.topology U) (ModuleCat.{max (u + 1) w} Λ) ⥤
      Sheaf (Scheme.ProEt.topology X) (ModuleCat.{max (u + 1) w} Λ)
```

**`AlgebraicGeometry.ProEtale.Modules.sheafifiedExtensionByZeroAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/Modules.lean, line 208](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/Modules.lean#L208). The attribute's comment: “(3), the adjunction j\_! ⊣ j^\{-1} on sheaves of Λ-modules, witnessing that restriction along a weakly étale morphism has extension by zero as a left adjoint”.

> The explicit extension-by-zero functor is left adjoint to restriction.

```lean
def sheafifiedExtensionByZeroAdjunction {U X : Scheme.{u}} (j : U ⟶ X) [WeaklyEtale j]
    (Λ : Type v) [Ring Λ] :
    sheafifiedExtensionByZero.{u, v, w} j Λ ⊣ proetaleRestriction.{u, v, w} j Λ
```

**`AlgebraicGeometry.ProEtale.Sets.extensionByZero`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/Sets.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/Sets.lean#L56). The attribute's comment: “extension\_by\_zero\_sets”.

> Extension by zero of sheaves of sets along a weakly étale morphism.

```lean
def extensionByZero {U X : Scheme.{u}} (j : U ⟶ X) [WeaklyEtale j] :
    Sheaf (Scheme.ProEt.topology U) (Type (max (u + 1) v)) ⥤
      Sheaf (Scheme.ProEt.topology X) (Type (max (u + 1) v))
```

**`AlgebraicGeometry.ProEtale.Sets.extensionByZeroAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/Sets.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/Sets.lean#L66). The attribute's comment: “extension\_by\_zero\_sets”.

> Extension by zero is left adjoint to restriction.

```lean
def extensionByZeroAdjunction {U X : Scheme.{u}} (j : U ⟶ X) [WeaklyEtale j] :
    extensionByZero.{u, v} j ⊣ proetaleRestriction.{u, v} j
```

## Tag 09AF, a lemma

[Tag 09AF](https://stacks.math.columbia.edu/tag/09AF) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.epsilonInverseImageExtensionByZeroIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/EtaleComparison.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/EtaleComparison.lean#L133). The attribute's comment: “the natural isomorphism eps^\{-1} j\_! = j\_! eps^\{-1}”.

> **Stacks Tag 09AF.** For an étale morphism `j : U ⟶ X`, pulling back along the comparison
> morphism `ε` of the small pro-étale and small étale sites commutes with extension by zero:
> `ε^{-1} j_! ≅ j_! ε^{-1}` on abelian sheaves.  Both sides are left adjoint to
> `ε_* j^{-1} = j^{-1} ε_*`.

```lean
def epsilonInverseImageExtensionByZeroIso :
    Stacks.EtaleCohomology.extensionByZero.{u, v} j ⋙ epsilonInverseImage.{u, v} X ≅
      epsilonInverseImage.{u, v} U ⋙ Abelian.extensionByZero.{u, v} j
```

**`AlgebraicGeometry.ProEtale.epsilonInverseImageExtensionByZeroObjIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/EtaleComparison.lean, line 145](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/EtaleComparison.lean#L145). The attribute's comment: “at an abelian sheaf G on U\_etale: eps^\{-1} j\_! G = j\_! eps^\{-1} G”.

> **Stacks Tag 09AF**, evaluated at an abelian sheaf `G` on `U_étale`:
> `ε^{-1} j_! G = j_! ε^{-1} G` as abelian sheaves on `X_proétale`.  This is the form in which the
> source states the lemma.

```lean
def epsilonInverseImageExtensionByZeroObjIso
    (G : Sheaf U.smallEtaleTopology AddCommGrpCat.{max (u + 1) v}) :
    (epsilonInverseImage.{u, v} X).obj
        ((Stacks.EtaleCohomology.extensionByZero.{u, v} j).obj G) ≅
      (Abelian.extensionByZero.{u, v} j).obj ((epsilonInverseImage.{u, v} U).obj G)
```

## Tag 09AG, a lemma

[Tag 09AG](https://stacks.math.columbia.edu/tag/09AG) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.isZero_extensionByZero_sections_of_specializes_to_closed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/ClosedFibreVanishing.lean, line 620](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/ClosedFibreVanishing.lean#L620).

> Extension by zero vanishes on an affine pro-étale object whose points
> specialize to a closed fibre disjoint from the weakly étale source.

```lean
theorem isZero_extensionByZero_sections_of_specializes_to_closed
    {U X Z : Scheme.{u}} (j : U ⟶ X) [WeaklyEtale j]
    (i : Z ⟶ X) [IsClosedImmersion i]
    (hdisjoint : IsEmpty (pullback j i : Scheme.{u}))
    (V : X.ProEt) [IsAffine V.left]
    (hV : ∀ x : V.left, ∃ z : (pullback V.hom i : Scheme.{u}),
      Specializes x ((pullback.fst V.hom i).base z))
    (F : Sheaf (Scheme.ProEt.topology U) AddCommGrpCat.{max (u + 1) v}) :
    IsZero (((Abelian.extensionByZero j).obj F).obj.obj (op V))
```

## Tag 09BN, a lemma

[Tag 09BN](https://stacks.math.columbia.edu/tag/09BN) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.extensionByZero_unit_isIso_sets`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/OpenImmersion.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/OpenImmersion.lean#L133). The attribute's comment: “sets: extension-by-zero unit”.

> The extension-by-zero unit for sheaves of sets along an open immersion
> is a natural isomorphism.

```lean
theorem extensionByZero_unit_isIso_sets {U X : Scheme.{u}}
    (j : U ⟶ X) [IsOpenImmersion j] :
    IsIso (Sets.extensionByZeroAdjunction.{u, v} j).unit
```

**`AlgebraicGeometry.ProEtale.extensionByZero_fullyFaithful_sets`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/OpenImmersion.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/OpenImmersion.lean#L141). The attribute's comment: “sets: extension by zero fully faithful”.

> Extension by zero of pro-étale sheaves of sets is fully faithful.

```lean
theorem extensionByZero_fullyFaithful_sets {U X : Scheme.{u}}
    (j : U ⟶ X) [IsOpenImmersion j] :
    Nonempty (Sets.extensionByZero.{u, v} j).FullyFaithful
```

**`AlgebraicGeometry.ProEtale.directImage_counit_isIso_sets`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/OpenImmersion.lean, line 316](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/OpenImmersion.lean#L316). The attribute's comment: “sets: direct-image counit”. References: SGA 4 I (5.7), “u\_* half, sheaves of”.

> The direct-image counit for sheaves of sets along an open immersion
> is a natural isomorphism.

```lean
theorem directImage_counit_isIso_sets
    (B : BigProetaleSite.{u}) {T S : B.Scheme} (j : T ⟶ S)
    [IsOpenImmersion (B.inclusion.map j)] :
    IsIso (smallProetaleMorphism B T S j).adj.counit
```

**`AlgebraicGeometry.ProEtale.directImage_fullyFaithful_sets`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/OpenImmersion.lean, line 362](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/OpenImmersion.lean#L362). The attribute's comment: “sets: direct image fully faithful”.

> Direct image of pro-étale sheaves of sets is fully faithful.

```lean
theorem directImage_fullyFaithful_sets
    (B : BigProetaleSite.{u}) {T S : B.Scheme} (j : T ⟶ S)
    [IsOpenImmersion (B.inclusion.map j)] :
    Nonempty (smallProetaleMorphism B T S j).pushforward.FullyFaithful
```

**`AlgebraicGeometry.ProEtale.extensionByZero_unit_isIso_abelian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/OpenImmersion.lean, line 373](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/OpenImmersion.lean#L373). The attribute's comment: “abelian: extension-by-zero unit”.

> The extension-by-zero unit for abelian pro-étale sheaves along an open
> immersion is a natural isomorphism.

```lean
theorem extensionByZero_unit_isIso_abelian {U X : Scheme.{u}}
    (j : U ⟶ X) [IsOpenImmersion j] :
    IsIso (Abelian.extensionByZero_adjunction.{u, v} j).unit
```

**`AlgebraicGeometry.ProEtale.extensionByZero_fullyFaithful_abelian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/OpenImmersion.lean, line 382](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/OpenImmersion.lean#L382). The attribute's comment: “abelian: extension by zero fully faithful”.

> Extension by zero of abelian pro-étale sheaves is fully faithful.

```lean
theorem extensionByZero_fullyFaithful_abelian {U X : Scheme.{u}}
    (j : U ⟶ X) [IsOpenImmersion j] :
    Nonempty (Abelian.extensionByZero.{u, v} j).FullyFaithful
```

**`AlgebraicGeometry.ProEtale.exists_directImage_abelian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/OpenImmersion.lean, line 391](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/OpenImmersion.lean#L391). The attribute's comment: “abelian: direct-image functor”.

> Restriction of abelian pro-étale sheaves has a right adjoint.

```lean
theorem exists_directImage_abelian {U X : Scheme.{u}}
    (j : U ⟶ X) [IsOpenImmersion j] :
    Nonempty (Σ R : Sheaf (Scheme.ProEt.topology U) AddCommGrpCat.{max (u + 1) v} ⥤
      Sheaf (Scheme.ProEt.topology X) AddCommGrpCat.{max (u + 1) v},
      Abelian.proetaleRestriction j ⊣ R)
```

**`AlgebraicGeometry.ProEtale.directImage_counit_isIso_abelian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/OpenImmersion.lean, line 401](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/OpenImmersion.lean#L401). The attribute's comment: “abelian: direct-image counit”. References: SGA 4 I (5.7), “u\_* half, pro-étale”.

> The counit of restriction and any of its right adjoints is invertible.

```lean
theorem directImage_counit_isIso_abelian {U X : Scheme.{u}}
    (j : U ⟶ X) [IsOpenImmersion j]
    (R : Sheaf (Scheme.ProEt.topology U) AddCommGrpCat.{max (u + 1) v} ⥤
      Sheaf (Scheme.ProEt.topology X) AddCommGrpCat.{max (u + 1) v})
    (adj : Abelian.proetaleRestriction j ⊣ R) :
    IsIso adj.counit
```

**`AlgebraicGeometry.ProEtale.directImage_fullyFaithful_abelian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/OpenImmersion.lean, line 413](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/OpenImmersion.lean#L413). The attribute's comment: “abelian: direct image fully faithful”.

> Direct image of abelian pro-étale sheaves is fully faithful.

```lean
theorem directImage_fullyFaithful_abelian {U X : Scheme.{u}}
    (j : U ⟶ X) [IsOpenImmersion j]
    (R : Sheaf (Scheme.ProEt.topology U) AddCommGrpCat.{max (u + 1) v} ⥤
      Sheaf (Scheme.ProEt.topology X) AddCommGrpCat.{max (u + 1) v})
    (adj : Abelian.proetaleRestriction j ⊣ R) :
    Nonempty R.FullyFaithful
```

**`AlgebraicGeometry.ProEtale.extensionByZero_unit_isIso_modules`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/OpenImmersion.lean, line 425](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/OpenImmersion.lean#L425). The attribute's comment: “modules: extension-by-zero unit”.

> The extension-by-zero unit for module pro-étale sheaves along an open
> immersion is a natural isomorphism.

```lean
theorem extensionByZero_unit_isIso_modules {U X : Scheme.{u}}
    (j : U ⟶ X) [IsOpenImmersion j] (Λ : Type v) [Ring Λ] :
    IsIso (Modules.extensionByZero_adjunction.{u, v, w} j Λ).unit
```

**`AlgebraicGeometry.ProEtale.extensionByZero_fullyFaithful_modules`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/OpenImmersion.lean, line 434](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/OpenImmersion.lean#L434). The attribute's comment: “modules: extension by zero fully faithful”.

> Extension by zero of module pro-étale sheaves is fully faithful.

```lean
theorem extensionByZero_fullyFaithful_modules {U X : Scheme.{u}}
    (j : U ⟶ X) [IsOpenImmersion j] (Λ : Type v) [Ring Λ] :
    Nonempty (Modules.extensionByZero.{u, v, w} j Λ).FullyFaithful
```

**`AlgebraicGeometry.ProEtale.exists_directImage_modules`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/OpenImmersion.lean, line 443](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/OpenImmersion.lean#L443). The attribute's comment: “modules: direct-image functor”.

> Restriction of module pro-étale sheaves has a right adjoint.

```lean
theorem exists_directImage_modules {U X : Scheme.{u}}
    (j : U ⟶ X) [IsOpenImmersion j] (Λ : Type v) [Ring Λ] :
    Nonempty (Σ R : Sheaf (Scheme.ProEt.topology U) (ModuleCat.{max (u + 1) w} Λ) ⥤
      Sheaf (Scheme.ProEt.topology X) (ModuleCat.{max (u + 1) w} Λ),
      Modules.proetaleRestriction j Λ ⊣ R)
```

**`AlgebraicGeometry.ProEtale.directImage_counit_isIso_modules`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/OpenImmersion.lean, line 453](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/OpenImmersion.lean#L453). The attribute's comment: “modules: direct-image counit”. References: SGA 4 I (5.7), “u\_* half, Λ-modules”.

> The counit of restriction and any of its right adjoints is invertible.

```lean
theorem directImage_counit_isIso_modules {U X : Scheme.{u}}
    (j : U ⟶ X) [IsOpenImmersion j] (Λ : Type v) [Ring Λ]
    (R : Sheaf (Scheme.ProEt.topology U) (ModuleCat.{max (u + 1) w} Λ) ⥤
      Sheaf (Scheme.ProEt.topology X) (ModuleCat.{max (u + 1) w} Λ))
    (adj : Modules.proetaleRestriction j Λ ⊣ R) :
    IsIso adj.counit
```

**`AlgebraicGeometry.ProEtale.directImage_fullyFaithful_modules`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/OpenImmersion.lean, line 465](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/OpenImmersion.lean#L465). The attribute's comment: “modules: direct image fully faithful”.

> Direct image of module pro-étale sheaves is fully faithful.

```lean
theorem directImage_fullyFaithful_modules {U X : Scheme.{u}}
    (j : U ⟶ X) [IsOpenImmersion j] (Λ : Type v) [Ring Λ]
    (R : Sheaf (Scheme.ProEt.topology U) (ModuleCat.{max (u + 1) w} Λ) ⥤
      Sheaf (Scheme.ProEt.topology X) (ModuleCat.{max (u + 1) w} Λ))
    (adj : Modules.proetaleRestriction j Λ ⊣ R) :
    Nonempty R.FullyFaithful
```

## Tag 09AH, a lemma

[Tag 09AH](https://stacks.math.columbia.edu/tag/09AH) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.hasEnoughObjects_openPart_or_closedFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/OpenClosedSequence.lean, line 762](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/OpenClosedSequence.lean#L762). The attribute's comment: “the geometric reduction of the source's proof: quasi-compactness of j splits every affine weakly contractible object of X\_proetale into a part lying over U and the ind-Zariski localization along its closed fibre”.

> **Stacks 09AH, the geometric reduction.** For a closed immersion `i` and its complementary
> quasi-compact open immersion `j`, every object of `X_proétale` is covered by objects which are
> either pulled back from `U_proétale`, or affine, weakly contractible and with all their points
> specializing into the closed fibre.
>
> Quasi-compactness of `j` is what makes the closed fibre of an affine object cut out by finitely
> many equations, and hence what produces the ind-Zariski localization of Stacks 096V along it.

```lean
theorem hasEnoughObjects_openPart_or_closedFibre {Z U X : Scheme.{u}} (i : Z ⟶ X)
    [IsClosedImmersion i] (j : U ⟶ X) [IsOpenImmersion j] [QuasiCompact j]
    (hij : Set.range j.base = (Set.range i.base)ᶜ) :
    (Scheme.ProEt.topology X).HasEnoughObjects (fun V : X.ProEt ↦
      (∃ W : U.ProEt, Nonempty (V ≅ (proetalePostcompose j).obj W)) ∨
      (IsAffine V.left ∧ (Scheme.ProEt.topology X).IsWeaklyContractible V ∧
        ∀ x : V.left, ∃ z : (pullback V.hom i : Scheme.{u}),
          Specializes x ((pullback.fst V.hom i).base z)))
```

**`AlgebraicGeometry.ProEtale.openClosedShortComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/OpenClosedSequence.lean, line 885](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/OpenClosedSequence.lean#L885). The attribute's comment: “the two canonical maps j\_! j^\{-1} F -> F -> i\_* i^\{-1} F and the fact that they compose to zero, i.e. the short complex of the tag; its short exactness is NOT proved here, see shortExact\_openClosedShortComplex\_of\_isIso\_unit\_app”.

> **Stacks 09AH.** The canonical short complex `j_! j^{-1} F ⟶ F ⟶ i_* i^{-1} F` on the small
> pro-étale site of `X`, for a closed subscheme `i : Z ⟶ X` and the inclusion `j : U ⟶ X` of its
> complement. Its two maps are the counit of `j_! ⊣ j^{-1}` and the unit of `i^{-1} ⊣ i_*`.
>
> The tag states in addition that this short complex is short exact when `j` is quasi-compact. That
> is not proved here: `shortExact_openClosedShortComplex_of_isIso_unit_app` below reduces it to the
> single input described in the header of this file.

```lean
def openClosedShortComplex
    (F : Sheaf (Scheme.ProEt.topology X) AddCommGrpCat.{max (u + 1) v}) :
    ShortComplex (Sheaf (Scheme.ProEt.topology X) AddCommGrpCat.{max (u + 1) v})
```

**`AlgebraicGeometry.ProEtale.shortExact_map_proetaleRestriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/OpenClosedSequence.lean, line 916](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/OpenClosedSequence.lean#L916). The attribute's comment: “exactness over the open part only: the restriction to U of the canonical short complex is short exact, unconditionally. Short exactness of the sequence on X\_proetale itself is NOT proved in this file: shortExact\_openClosedShortComplex\_of\_isIso\_unit\_app proves it at the source's hypotheses but assumes Tag 09AC for the site of AlgebraicGeometry.Scheme.ProEt, namely that the unit F -> i\_* i^\{-1} F is invertible on sections over every affine weakly contractible object all of whose points specialize into its closed fibre”.

> **Stacks 09AH, over the open part.** Restricted to `U`, the short complex of the tag is
> short exact, and indeed split: its third term vanishes over `U` and its first map becomes
> invertible there.

```lean
theorem shortExact_map_proetaleRestriction [IsOpenImmersion j]
    (F : Sheaf (Scheme.ProEt.topology X) AddCommGrpCat.{max (u + 1) v}) :
    ((openClosedShortComplex.{u, v} i j hij F).map
      (Abelian.proetaleRestriction.{u, v} j)).ShortExact
```

**`AlgebraicGeometry.ProEtale.shortExact_openClosedShortComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/OpenClosedSequenceShortExact.lean, line 76](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/OpenClosedSequenceShortExact.lean#L76).

> **Stacks 09AH.** Let `i : Z ⟶ X` be a closed immersion and let `j : U ⟶ X` be an open
> immersion onto the complement of its image, and assume `j` quasi-compact. For every abelian sheaf
> `F` on the small pro-étale site of `X` the canonical sequence
> `0 → j_! j^{-1} F → F → i_* i^{-1} F → 0`,
> whose maps are the counit of `j_! ⊣ j^{-1}` and the unit of `i^{-1} ⊣ i_*`, is short exact.

```lean
theorem shortExact_openClosedShortComplex {Z U X : Scheme.{u}} (i : Z ⟶ X) (j : U ⟶ X)
    [IsClosedImmersion i] [IsOpenImmersion j] [QuasiCompact j]
    (hij : Set.range j.base = (Set.range i.base)ᶜ)
    (F : Sheaf (Scheme.ProEt.topology X) AddCommGrpCat.{max (u + 1) v}) :
    (openClosedShortComplex.{u, v} i j hij F).ShortExact
```

## Tag 09BP, a lemma

[Tag 09BP](https://stacks.math.columbia.edu/tag/09BP) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.preservesLimits_extensionByZero_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/PreservesLimits.lean, line 389](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/PreservesLimits.lean#L389).

> **Stacks 09BP.** For a quasi-compact open immersion `j : U ⟶ X` of schemes, extension by
> zero `j_! : Ab(U_proétale) ⥤ Ab(X_proétale)` of abelian sheaves on the small pro-étale sites
> commutes with limits.
>
> Nothing is assumed: `j_! j^{-1}` commutes with limits by
> `preservesLimits_proetaleRestriction_comp_extensionByZero_of_quasiCompact`, whose proof computes
> the sections of `j_! j^{-1}` on the covering family that quasi-compactness of `j` produces; and
> `j_!` is isomorphic to `j_! j^{-1} j_*` because the counit of `j^{-1} ⊣ j_*` is invertible for
> an open immersion.

```lean
theorem preservesLimits_extensionByZero_unconditional [IsOpenImmersion j] [QuasiCompact j] :
    PreservesLimits (Abelian.extensionByZero.{u, v} j)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 61.26, Tag 09AD](https://stacks.math.columbia.edu/tag/09AD)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
