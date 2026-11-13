---
declaration: section
origin: cited
lean: CategoryTheory.CocontinuousSimplicialSite.RingedMorphism, CategoryTheory.CocontinuousSimplicialSite.RingedMorphism.ringHomEquiv, CategoryTheory.SimplicialSite.RingedMorphism, CategoryTheory.SimplicialSite.RingedMorphism.ringHomEquiv, CategoryTheory.SimplicialSiteMorphism.ringHomEquiv, CategoryTheory.SimplicialSiteSituation.RingedMorphism, CategoryTheory.SimplicialSiteSituation.componentPullbackUnderlyingIso, CategoryTheory.SimplicialSiteSituation.componentPullbackUnderlyingIso_unit
statement: formalized
proof: formalized
---

# 85.7 Morphisms of ringed simplicial sites

Section 85.7 of the Stacks Project, [Tag 0DGY](https://stacks.math.columbia.edu/tag/0DGY). 3 tags here are carried by 56 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DGZ, a remark

[Tag 0DGZ](https://stacks.math.columbia.edu/tag/0DGZ) in the Stacks Project.

**`CategoryTheory.CocontinuousSimplicialSite.RingedMorphism`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedMorphism.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedMorphism.lean#L95). The attribute's comment: “ringed simplicial site morphism, case (B) of Situation 09WE”.

> **Stacks 0DGZ**, case (B). A morphism between ringed simplicial sites: a morphism `h`
> between the underlying simplicial sites, together with a homomorphism of sheaves of rings
> `h♯ : h_total⁻¹ 𝒪' ⟶ 𝒪` on the total site.

```lean
structure RingedMorphism (C C' : CocontinuousSimplicialSite.{u})
    (O : Sheaf (⟨Sum.inr C⟩ : SimplicialSiteSituation.{u}).totalTopology RingCat.{u})
    (O' : Sheaf (⟨Sum.inr C'⟩ : SimplicialSiteSituation.{u}).totalTopology RingCat.{u})
```

**`CategoryTheory.CocontinuousSimplicialSite.RingedMorphism.ringHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedMorphism.lean, line 122](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedMorphism.lean#L122). The attribute's comment: “the two equivalent forms of the ring map, case (B)”. References: SGA 4 XVII (0.2.1), “ringed simplicial sites”.

> **Stacks 0DGZ**, case (B). A homomorphism of sheaves of rings `h_total⁻¹ 𝒪' ⟶ 𝒪` is the
> same thing as a homomorphism `𝒪' ⟶ h_{total, *} 𝒪`: the two are exchanged by the adjunction
> between the inverse image and the direct image of sheaves of rings along the morphism of total
> topoi.

```lean
def ringHomEquiv (h : CocontinuousSimplicialSite.Morphism C C')
    (O : Sheaf (⟨Sum.inr C⟩ : SimplicialSiteSituation.{u}).totalTopology RingCat.{u})
    (O' : Sheaf (⟨Sum.inr C'⟩ : SimplicialSiteSituation.{u}).totalTopology RingCat.{u}) :
    (h.totalInverseImageRing O' ⟶ O) ≃ (O' ⟶ h.totalPushforwardRing O)
```

**`CategoryTheory.SimplicialSite.RingedMorphism`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedMorphismContinuous.lean, line 155](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedMorphismContinuous.lean#L155). The attribute's comment: “ringed simplicial site morphism, case (A) of Situation 09WE”.

> **Stacks 0DGZ**, case (A). A morphism between ringed simplicial sites: a morphism `h`
> between the underlying simplicial sites, together with a homomorphism of sheaves of rings
> `h♯ : h_total⁻¹ 𝒪' ⟶ 𝒪` on the total site.

```lean
structure RingedMorphism (C C' : SimplicialSite.{u})
    (O : Sheaf C.totalTopology RingCat.{u})
    (O' : Sheaf C'.totalTopology RingCat.{u})
```

**`CategoryTheory.SimplicialSite.RingedMorphism.ringHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedMorphismContinuous.lean, line 181](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedMorphismContinuous.lean#L181). The attribute's comment: “the two equivalent forms of the ring map, case (A)”. References: SGA 4 XVII (0.2.1), “ringed simplicial sites”.

> **Stacks 0DGZ**, case (A). A homomorphism of sheaves of rings `h_total⁻¹ 𝒪' ⟶ 𝒪` is the
> same thing as a homomorphism `𝒪' ⟶ h_{total, *} 𝒪`: the two are exchanged by the adjunction
> between the inverse image and the direct image of sheaves of rings along the total functor.

```lean
def ringHomEquiv (h : SimplicialSite.Morphism C C')
    (O : Sheaf C.totalTopology RingCat.{u})
    (O' : Sheaf C'.totalTopology RingCat.{u}) :
    (h.totalInverseImageRing O' ⟶ O) ≃ (O' ⟶ h.totalPushforwardRing O)
```

**`CategoryTheory.SimplicialSiteMorphism.ringHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedMorphismSituation.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedMorphismSituation.lean#L141). The attribute's comment: “the two equivalent forms of the ring map, case (A)”. References: SGA 4 XVII (0.2.1), “ringed simplicial sites”.

> **Stacks 0DGZ**, both cases of Situation 09WE. A homomorphism of sheaves of rings
> `h_total⁻¹ 𝒪' ⟶ 𝒪` is the same thing as a homomorphism `𝒪' ⟶ h_{total, *} 𝒪`: the two are
> exchanged by the adjunction between the inverse image and the direct image of sheaves of rings
> along the morphism of total topoi.

```lean
def ringHomEquiv (h : SimplicialSiteMorphism S S')
    (O : Sheaf S.totalTopology RingCat.{u}) (O' : Sheaf S'.totalTopology RingCat.{u}) :
    (h.totalInverseImageRing O' ⟶ O) ≃ (O' ⟶ h.totalPushforwardRing O)
```

**`CategoryTheory.SimplicialSiteMorphism.ringHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedMorphismSituation.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedMorphismSituation.lean#L141). The attribute's comment: “the two equivalent forms of the ring map, case (B)”. References: SGA 4 XVII (0.2.1), “ringed simplicial sites”.

> **Stacks 0DGZ**, both cases of Situation 09WE. A homomorphism of sheaves of rings
> `h_total⁻¹ 𝒪' ⟶ 𝒪` is the same thing as a homomorphism `𝒪' ⟶ h_{total, *} 𝒪`: the two are
> exchanged by the adjunction between the inverse image and the direct image of sheaves of rings
> along the morphism of total topoi.

```lean
def ringHomEquiv (h : SimplicialSiteMorphism S S')
    (O : Sheaf S.totalTopology RingCat.{u}) (O' : Sheaf S'.totalTopology RingCat.{u}) :
    (h.totalInverseImageRing O' ⟶ O) ≃ (O' ⟶ h.totalPushforwardRing O)
```

**`CategoryTheory.SimplicialSiteSituation.RingedMorphism`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedMorphismSituation.lean, line 171](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedMorphismSituation.lean#L171). The attribute's comment: “ringed simplicial site morphism, case (A) of Situation 09WE”.

> **Stacks 0DGZ**, both cases of Situation 09WE. A morphism between ringed simplicial sites: a
> morphism `h` between the underlying simplicial sites, together with a homomorphism of sheaves of
> rings `h♯ : h_total⁻¹ 𝒪' ⟶ 𝒪` on the total site.

```lean
structure SimplicialSiteSituation.RingedMorphism (S S' : SimplicialSiteSituation.{u})
    (O : Sheaf S.totalTopology RingCat.{u})
    (O' : Sheaf S'.totalTopology RingCat.{u})
```

**`CategoryTheory.SimplicialSiteSituation.RingedMorphism`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedMorphismSituation.lean, line 171](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedMorphismSituation.lean#L171). The attribute's comment: “ringed simplicial site morphism, case (B) of Situation 09WE”.

> **Stacks 0DGZ**, both cases of Situation 09WE. A morphism between ringed simplicial sites: a
> morphism `h` between the underlying simplicial sites, together with a homomorphism of sheaves of
> rings `h♯ : h_total⁻¹ 𝒪' ⟶ 𝒪` on the total site.

```lean
structure SimplicialSiteSituation.RingedMorphism (S S' : SimplicialSiteSituation.{u})
    (O : Sheaf S.totalTopology RingCat.{u})
    (O' : Sheaf S'.totalTopology RingCat.{u})
```

## Tag 0DH0, a lemma

[Tag 0DH0](https://stacks.math.columbia.edu/tag/0DH0) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.componentPullbackUnderlyingIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean, line 737](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean#L737). The attribute's comment: “restriction of modules to components”.

> **Stacks 0DH0.** Restriction of sheaves of modules to the simplicial component of degree
> `n` has the inverse image of sheaves of sets as its underlying sheaf, naturally in the module:
> the component structure sheaf is itself the restriction of the total structure sheaf, so the
> pullback of modules extends scalars along an isomorphism.

```lean
def componentPullbackUnderlyingIso :
    (componentRingedToposHom S O n).toModulesHom.pullbackModules ⋙
        Sheaf.moduleSheafFunctor
          ((Stacks.SheafOfModules.Tensor.ringSheaf (J := (componentRingedTopos S O n).J))
          (componentRingedTopos S O n).O) ≅
      Sheaf.moduleSheafFunctor
        ((Stacks.SheafOfModules.Tensor.ringSheaf (J := (totalRingedTopos S O).J))
          (totalRingedTopos S O).O) ⋙
        (componentRingedToposHom S O n).toToposHom.inverseImage
```

**`CategoryTheory.SimplicialSiteSituation.componentPullbackUnderlyingIso_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean, line 756](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean#L756). The attribute's comment: “the canonical restriction of modules”.

> **Stacks 0DH0.** The comparison of the previous declaration is the canonical one, not an
> arbitrary isomorphism: precomposing it with the unit of extension of scalars along the
> component structure map — which is what
> `AlgebraicGeometry.RingedToposHom.pullbackUnitUnderlyingIso` is, by
> `AlgebraicGeometry.RingedToposHom.pullbackUnitUnderlyingIso_hom_app` — returns the comparison
> of Stacks 03D2 between the underlying sheaf of the inverse image of modules and the inverse
> image of the underlying sheaf.

```lean
theorem componentPullbackUnderlyingIso_unit :
    RingedToposHom.pullbackUnitUnderlyingIso (componentRingedToposHom S O n) ≪≫
        componentPullbackUnderlyingIso S O n =
      inverseImageModuleSheafIso (componentRingedToposHom S O n).toToposHom
        ((Stacks.SheafOfModules.Tensor.ringSheaf (J := (totalRingedTopos S O).J))
          (totalRingedTopos S O).O)
```

**`CategoryTheory.CocontinuousSimplicialSite.Morphism.componentInverseImageCommRingIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean, line 810](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean#L810). The attribute's comment: “the canonical ring comparison”.

> **Stacks 0DH0.** The comparison of the two inverse images of sheaves of commutative rings
> around the square of simplicial degree `n`. This is the identification
> `gₙ⁻¹h_{total}⁻¹𝒪' = hₙ⁻¹(g'ₙ)⁻¹𝒪'` through which the source defines the degreewise structure
> map.

```lean
def componentInverseImageCommRingIso (h : Morphism C C') (n : SimplexCategory) :
    inverseImageCommRingFunctor.{u, u, u, u, u, u} (viaTotalMorphism h n) ≅
      inverseImageCommRingFunctor.{u, u, u, u, u, u} (viaComponentMorphism h n)
```

**`CategoryTheory.CocontinuousSimplicialSite.Morphism.componentInverseImageCommRingIso_forget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean, line 823](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean#L823). The attribute's comment: “the canonical underlying comparison”.

> **Stacks 0DH0.** The comparison of inverse images of sheaves of commutative rings has the
> comparison of inverse images of sheaves of sets as its underlying map, which determines it
> uniquely by
> `Stacks.Sheaves.ToposPushforward.inverseImageCommRingIsoOfToposIso_existsUnique`.

```lean
theorem componentInverseImageCommRingIso_forget (h : Morphism C C') (n : SimplexCategory)
    (O' : Sheaf C'.situation.totalTopology CommRingCat.{u}) :
    (sheafCompose (C.situation.componentTopology n) (forget CommRingCat.{u})).map
        ((componentInverseImageCommRingIso h n).hom.app O') =
      (componentInverseImageIso h n).hom.app
        ((sheafCompose C'.situation.totalTopology (forget CommRingCat.{u})).obj O')
```

**`CategoryTheory.CocontinuousSimplicialSite.Morphism.totalRingedToposHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean, line 950](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean#L950). The attribute's comment: “the total morphism of ringed topoi”.

> **Stacks 0DH0.** The morphism of total ringed topoi induced by a morphism between ringed
> simplicial sites.

```lean
def totalRingedToposHom
    (h : Morphism C C') (φ : h.totalInverseImageRing
      ((Stacks.SheafOfModules.Tensor.ringSheaf (J := C'.situation.totalTopology) O')) ⟶
        (Stacks.SheafOfModules.Tensor.ringSheaf (J := C.situation.totalTopology) O)) :
    RingedToposHom (C.situation.totalRingedTopos O) (C'.situation.totalRingedTopos O')
```

**`CategoryTheory.CocontinuousSimplicialSite.Morphism.componentRingedToposHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean, line 1003](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean#L1003). The attribute's comment: “the component morphisms of ringed topoi”.

> **Stacks 0DH0.** The morphism of component ringed topoi in simplicial degree `n` induced by a
> morphism between ringed simplicial sites.

```lean
def componentRingedToposHom
    (h : Morphism C C') (φ : h.totalInverseImageRing
      ((Stacks.SheafOfModules.Tensor.ringSheaf (J := C'.situation.totalTopology) O')) ⟶
        (Stacks.SheafOfModules.Tensor.ringSheaf (J := C.situation.totalTopology) O))
    (n : SimplexCategory) :
    RingedToposHom (C.situation.componentRingedTopos O n)
      (C'.situation.componentRingedTopos O' n)
```

**`CategoryTheory.CocontinuousSimplicialSite.Morphism.componentRingedToposHom_toToposHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean, line 1021](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean#L1021). The attribute's comment: “the underlying degreewise geometric morphisms”.

> **Stacks 0DH0.** The underlying geometric morphism of the degreewise morphism of ringed
> topoi is the component morphism of topoi of Stacks 0D95.

```lean
theorem componentRingedToposHom_toToposHom
    (h : Morphism C C') (φ : h.totalInverseImageRing
      ((Stacks.SheafOfModules.Tensor.ringSheaf (J := C'.situation.totalTopology) O')) ⟶
        (Stacks.SheafOfModules.Tensor.ringSheaf (J := C.situation.totalTopology) O))
    (n : SimplexCategory) :
    ((h.componentRingedToposHom φ) n).toToposHom =
      (SimplicialSiteMorphism.ofCocontinuous h).componentMorphism n
```

**`CategoryTheory.CocontinuousSimplicialSite.Morphism.componentRingedToposHom_commutes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean, line 1043](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean#L1043). The attribute's comment: “the commutative squares of ringed topoi”.

> **Stacks 0DH0.** The square of ringed topoi formed by the total morphism, the degreewise
> morphism and the two canonical morphisms from the components of simplicial degree `n` commutes:
> the comparison of inverse images identifies the two composite structure maps.

```lean
theorem componentRingedToposHom_commutes
    (h : Morphism C C') (φ : h.totalInverseImageRing
      ((Stacks.SheafOfModules.Tensor.ringSheaf (J := C'.situation.totalTopology) O')) ⟶
        (Stacks.SheafOfModules.Tensor.ringSheaf (J := C.situation.totalTopology) O))
    (n : SimplexCategory) :
    (h.componentInverseImageCommRingIso n).hom.app O' ≫
        ((C'.situation.componentRingedToposHom O' n).comp
          ((h.componentRingedToposHom φ) n)).fSharpInverseImage =
      ((h.totalRingedToposHom φ).comp
        (C.situation.componentRingedToposHom O n)).fSharpInverseImage
```

**`CategoryTheory.CocontinuousSimplicialSite.Morphism.componentPushforwardModulesForgetIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean, line 1085](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean#L1085). The attribute's comment: “the underlying restriction of the direct image of modules”.

> **Stacks 0DH0, the assertion on sheaves of modules, on underlying sheaves of sets.**
> Inverse image to the simplicial component of degree `n` of a direct image of sheaves of modules
> along the total morphism is the degreewise direct image of the inverse image to that component.
>
> The comparison is the one of Stacks 0D96 and nothing else: the pullback of modules along a
> component inclusion is inverse image on underlying sheaves of sets, by
> `CategoryTheory.SimplicialSiteSituation.componentPullbackUnderlyingIso`, and the direct image of
> modules is direct image there on the nose.

```lean
def componentPushforwardModulesForgetIso
    (h : Morphism C C') (φ : h.totalInverseImageRing
      ((Stacks.SheafOfModules.Tensor.ringSheaf (J := C'.situation.totalTopology) O')) ⟶
        (Stacks.SheafOfModules.Tensor.ringSheaf (J := C.situation.totalTopology) O))
    (n : SimplexCategory) :
    (h.totalRingedToposHom φ).pushforwardModules ⋙
        (C'.situation.componentRingedToposHom O' n).toModulesHom.pullbackModules ⋙
          Sheaf.moduleSheafFunctor
            ((Stacks.SheafOfModules.Tensor.ringSheaf
              (J := (C'.situation.componentRingedTopos O' n).J)
              (C'.situation.componentRingedTopos O' n).O)) ≅
      (C.situation.componentRingedToposHom O n).toModulesHom.pullbackModules ⋙
        ((h.componentRingedToposHom φ) n).pushforwardModules ⋙
          Sheaf.moduleSheafFunctor
            ((Stacks.SheafOfModules.Tensor.ringSheaf
              (J := (C'.situation.componentRingedTopos O' n).J)
              (C'.situation.componentRingedTopos O' n).O))
```

**`CategoryTheory.CocontinuousSimplicialSite.Morphism.componentRingedToposHom_twoIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean, line 1166](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean#L1166). The attribute's comment: “the degreewise square as a 2-isomorphism of ringed topoi”.

> **Stacks 0DH0.** The degreewise square commutes as a square of *ringed* topoi, in the sense
> of Stacks 04IC: the two composites `h_{total} ∘ g_n` and `g'_n ∘ h_n` are 2-isomorphic.
>
> The comparison of the direct images is the one of Stacks 0D96, and the compatibility with the
> three structure maps is `componentRingedToposHom_commutes` read on underlying sheaves of sets,
> through `AlgebraicGeometry.RingedToposHom.TwoIso.ofInverseImageIso`, which transposes a
> compatibility of the inverse-image forms into one of the direct-image forms. The underlying
> comparison of inverse images is pinned by
> `CategoryTheory.CocontinuousSimplicialSite.Morphism.componentInverseImageCommRingIso_forget`,
> so this 2-isomorphism is not an arbitrary one.

```lean
noncomputable def componentRingedToposHom_twoIso
    (h : Morphism C C') (φ : h.totalInverseImageRing
      ((Stacks.SheafOfModules.Tensor.ringSheaf (J := C'.situation.totalTopology) O')) ⟶
        (Stacks.SheafOfModules.Tensor.ringSheaf (J := C.situation.totalTopology) O))
    (n : SimplexCategory) :
    RingedToposHom.TwoIso.{u, u, u, u, u, u}
      (viaTotalRingedToposHom h φ n) (viaComponentRingedToposHom h φ n)
```

**`CategoryTheory.CocontinuousSimplicialSite.Morphism.componentPushforwardModulesSquareIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean, line 1199](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean#L1199). The attribute's comment: “the commutative squares, on direct images of sheaves of modules”.

> **Stacks 0DH0, the degreewise square on direct images of sheaves of modules.** Direct image
> to the total ringed topos of the target, taken through the component of degree `n` of the
> source, agrees with direct image taken through the component of degree `n` of the target:
>
> `h_{total,*} ∘ g_{n,*} ≅ g'_{n,*} ∘ h_{n,*}` on `Mod(𝒪_n)`.
>
> This is the commuting square of ringed topoi of
> `componentRingedToposHom_twoIso` read on sheaves of modules, and it is a genuine module-level
> statement: the comparison is additive and linear, not merely a comparison of underlying sheaves
> of sets.

```lean
noncomputable def componentPushforwardModulesSquareIso
    (h : Morphism C C') (φ : h.totalInverseImageRing
      ((Stacks.SheafOfModules.Tensor.ringSheaf (J := C'.situation.totalTopology) O')) ⟶
        (Stacks.SheafOfModules.Tensor.ringSheaf (J := C.situation.totalTopology) O))
    (n : SimplexCategory) :
    (C.situation.componentRingedToposHom O n).pushforwardModules ⋙
        (h.totalRingedToposHom φ).pushforwardModules ≅
      ((h.componentRingedToposHom φ) n).pushforwardModules ⋙
        (C'.situation.componentRingedToposHom O' n).pushforwardModules
```

**`CategoryTheory.CocontinuousSimplicialSite.Morphism.componentPullbackModulesSquareIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean, line 1222](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean#L1222). The attribute's comment: “the commutative squares, on pullbacks of sheaves of modules”.

> **Stacks 0DH0, the degreewise square on pullbacks of sheaves of modules.** The same square,
> read on pullbacks:
>
> `g_n^* ∘ h_{total}^* ≅ h_n^* ∘ (g'_n)^*` on `Mod(𝒪')`.
>
> Both sides are left adjoint to the two sides of `componentPushforwardModulesSquareIso`, so this
> is uniqueness of left adjoints applied to that isomorphism.

```lean
noncomputable def componentPullbackModulesSquareIso
    (h : Morphism C C') (φ : h.totalInverseImageRing
      ((Stacks.SheafOfModules.Tensor.ringSheaf (J := C'.situation.totalTopology) O')) ⟶
        (Stacks.SheafOfModules.Tensor.ringSheaf (J := C.situation.totalTopology) O))
    (n : SimplexCategory) :
    (h.totalRingedToposHom φ).toModulesHom.pullbackModules ⋙
        (C.situation.componentRingedToposHom O n).toModulesHom.pullbackModules ≅
      (C'.situation.componentRingedToposHom O' n).toModulesHom.pullbackModules ⋙
        ((h.componentRingedToposHom φ) n).toModulesHom.pullbackModules
```

**`CategoryTheory.CocontinuousSimplicialSite.Morphism.componentPushforwardModulesComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean, line 1247](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean#L1247). The attribute's comment: “the comparison of the last assertion, on sheaves of modules”.

> **Stacks 0DH0, the comparison of the last assertion.** The canonical morphism of functors
> `Mod(𝒪) ⟶ Mod(𝒪'_n)`
>
> `(g'_n)^* ∘ h_{total,*} ⟶ h_{n,*} ∘ g_n^*`
>
> attached to the degreewise square: the mate of `componentPushforwardModulesSquareIso` under the
> two adjunctions `g_n^* ⊣ g_{n,*}` and `(g'_n)^* ⊣ (g'_n)_*` of Stacks 03D7. The source's last
> assertion is that this comparison is invertible, which is the Beck–Chevalley content of the
> degreewise square; see the implementation notes of this file.

```lean
noncomputable def componentPushforwardModulesComparison
    (h : Morphism C C') (φ : h.totalInverseImageRing
      ((Stacks.SheafOfModules.Tensor.ringSheaf (J := C'.situation.totalTopology) O')) ⟶
        (Stacks.SheafOfModules.Tensor.ringSheaf (J := C.situation.totalTopology) O))
    (n : SimplexCategory) :
    (h.totalRingedToposHom φ).pushforwardModules ⋙
        (C'.situation.componentRingedToposHom O' n).toModulesHom.pullbackModules ⟶
      (C.situation.componentRingedToposHom O n).toModulesHom.pullbackModules ⋙
        ((h.componentRingedToposHom φ) n).pushforwardModules
```

**`CategoryTheory.CocontinuousSimplicialSite.Morphism.componentPushforwardModulesComparison_mate`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean, line 1267](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean#L1267). The attribute's comment: “the comparison of the last assertion is the mate of the square”.

> **Stacks 0DH0.** The comparison of the last assertion is pinned by the degreewise square:
> its mate under the two adjunctions of Stacks 03D7 is the square of direct images of sheaves of
> modules. In particular it is not an arbitrary natural transformation.

```lean
theorem componentPushforwardModulesComparison_mate
    (h : Morphism C C') (φ : h.totalInverseImageRing
      ((Stacks.SheafOfModules.Tensor.ringSheaf (J := C'.situation.totalTopology) O')) ⟶
        (Stacks.SheafOfModules.Tensor.ringSheaf (J := C.situation.totalTopology) O))
    (n : SimplexCategory) :
    mateEquiv
        (RingedToposHom.pullbackAdjPushforwardModules
          (C.situation.componentRingedToposHom O n))
        (RingedToposHom.pullbackAdjPushforwardModules
          (C'.situation.componentRingedToposHom O' n))
        (componentPushforwardModulesComparison h φ n) =
      TwoSquare.mk _ _ _ _ (componentPushforwardModulesSquareIso h φ n).hom
```

**`CategoryTheory.CocontinuousSimplicialSite.Morphism.componentPushforwardModulesIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean, line 1429](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean#L1429). The attribute's comment: “the last assertion, on sheaves of modules”.

> **Stacks 0DH0, the last assertion, on sheaves of modules.** Inverse image to the simplicial
> component of degree `n` of a direct image of sheaves of modules along the total morphism is the
> degreewise direct image of the inverse image to that component:
>
> `(g'_n)^* ∘ h_{total,*} ≅ h_{n,*} ∘ g_n^*` as functors `Mod(𝒪) ⟶ Mod(𝒪'_n)`,
>
> the isomorphism being the canonical comparison `componentPushforwardModulesComparison`
> attached to the degreewise square. That comparison is invertible by
> `isIso_componentPushforwardModulesComparison`, which is the Beck–Chevalley statement for the
> square; so this is unconditional, as is the assertion on underlying sheaves of sets,
> `componentPushforwardModulesForgetIso`.

```lean
noncomputable def componentPushforwardModulesIso
    (h : Morphism C C') (φ : h.totalInverseImageRing
      ((Stacks.SheafOfModules.Tensor.ringSheaf (J := C'.situation.totalTopology) O')) ⟶
        (Stacks.SheafOfModules.Tensor.ringSheaf (J := C.situation.totalTopology) O))
    (n : SimplexCategory) :
    (h.totalRingedToposHom φ).pushforwardModules ⋙
        (C'.situation.componentRingedToposHom O' n).toModulesHom.pullbackModules ≅
      (C.situation.componentRingedToposHom O n).toModulesHom.pullbackModules ⋙
        ((h.componentRingedToposHom φ) n).pushforwardModules
```

**`CategoryTheory.CocontinuousSimplicialSite.RingedMorphism.totalRingedToposHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean, line 1480](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean#L1480). The attribute's comment: “the total morphism of ringed topoi”.

> **Stacks 0DH0.** The morphism of total ringed topoi induced by a morphism between ringed
> simplicial sites.

```lean
def totalRingedToposHom
    (h : RingedMorphism C C'
      ((Stacks.SheafOfModules.Tensor.ringSheaf (J := C.situation.totalTopology)) O)
      ((Stacks.SheafOfModules.Tensor.ringSheaf (J := C'.situation.totalTopology)) O')) :
    RingedToposHom (C.situation.totalRingedTopos O) (C'.situation.totalRingedTopos O')
```

**`CategoryTheory.CocontinuousSimplicialSite.RingedMorphism.componentRingedToposHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean, line 1533](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean#L1533). The attribute's comment: “the component morphisms of ringed topoi”.

> **Stacks 0DH0.** The morphism of component ringed topoi in simplicial degree `n` induced by a
> morphism between ringed simplicial sites.

```lean
def componentRingedToposHom
    (h : RingedMorphism C C'
      ((Stacks.SheafOfModules.Tensor.ringSheaf (J := C.situation.totalTopology)) O)
      ((Stacks.SheafOfModules.Tensor.ringSheaf (J := C'.situation.totalTopology)) O'))
    (n : SimplexCategory) :
    RingedToposHom (C.situation.componentRingedTopos O n)
      (C'.situation.componentRingedTopos O' n)
```

**`CategoryTheory.CocontinuousSimplicialSite.RingedMorphism.componentRingedToposHom_toToposHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean, line 1551](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean#L1551). The attribute's comment: “the underlying degreewise geometric morphisms”.

> **Stacks 0DH0.** The underlying geometric morphism of the degreewise morphism of ringed
> topoi is the component morphism of topoi of Stacks 0D95.

```lean
theorem componentRingedToposHom_toToposHom
    (h : RingedMorphism C C'
      ((Stacks.SheafOfModules.Tensor.ringSheaf (J := C.situation.totalTopology)) O)
      ((Stacks.SheafOfModules.Tensor.ringSheaf (J := C'.situation.totalTopology)) O'))
    (n : SimplexCategory) :
    (h.componentRingedToposHom n).toToposHom =
      (SimplicialSiteMorphism.ofCocontinuous h.hom).componentMorphism n
```

**`CategoryTheory.CocontinuousSimplicialSite.RingedMorphism.componentRingedToposHom_commutes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean, line 1573](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean#L1573). The attribute's comment: “the commutative squares of ringed topoi”.

> **Stacks 0DH0.** The square of ringed topoi formed by the total morphism, the degreewise
> morphism and the two canonical morphisms from the components of simplicial degree `n` commutes:
> the comparison of inverse images identifies the two composite structure maps.

```lean
theorem componentRingedToposHom_commutes
    (h : RingedMorphism C C'
      ((Stacks.SheafOfModules.Tensor.ringSheaf (J := C.situation.totalTopology)) O)
      ((Stacks.SheafOfModules.Tensor.ringSheaf (J := C'.situation.totalTopology)) O'))
    (n : SimplexCategory) :
    (h.hom.componentInverseImageCommRingIso n).hom.app O' ≫
        ((C'.situation.componentRingedToposHom O' n).comp
          (h.componentRingedToposHom n)).fSharpInverseImage =
      (h.totalRingedToposHom.comp
        (C.situation.componentRingedToposHom O n)).fSharpInverseImage
```

**`CategoryTheory.CocontinuousSimplicialSite.RingedMorphism.componentPushforwardModulesForgetIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean, line 1594](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean#L1594). The attribute's comment: “the underlying restriction of the direct image of modules”.

> **Stacks 0DH0, the assertion on sheaves of modules, on underlying sheaves of sets.**
> Inverse image to the simplicial component of degree `n` of a direct image of sheaves of modules
> along the total morphism is the degreewise direct image of the inverse image to that component.
>
> The comparison is the one of Stacks 0D96 and nothing else: the pullback of modules along a
> component inclusion is inverse image on underlying sheaves of sets, by
> `CategoryTheory.SimplicialSiteSituation.componentPullbackUnderlyingIso`, and the direct image of
> modules is direct image there on the nose.

```lean
def componentPushforwardModulesForgetIso
    (h : RingedMorphism C C'
      ((Stacks.SheafOfModules.Tensor.ringSheaf (J := C.situation.totalTopology)) O)
      ((Stacks.SheafOfModules.Tensor.ringSheaf (J := C'.situation.totalTopology)) O'))
    (n : SimplexCategory) :
    h.totalRingedToposHom.pushforwardModules ⋙
        (C'.situation.componentRingedToposHom O' n).toModulesHom.pullbackModules ⋙
          Sheaf.moduleSheafFunctor
            ((Stacks.SheafOfModules.Tensor.ringSheaf
              (J := (C'.situation.componentRingedTopos O' n).J))
              (C'.situation.componentRingedTopos O' n).O) ≅
      (C.situation.componentRingedToposHom O n).toModulesHom.pullbackModules ⋙
        (h.componentRingedToposHom n).pushforwardModules ⋙
          Sheaf.moduleSheafFunctor
            ((Stacks.SheafOfModules.Tensor.ringSheaf
              (J := (C'.situation.componentRingedTopos O' n).J))
              (C'.situation.componentRingedTopos O' n).O)
```

**`CategoryTheory.CocontinuousSimplicialSite.RingedMorphism.componentRingedToposHom_twoIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean, line 1675](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean#L1675). The attribute's comment: “the degreewise square as a 2-isomorphism of ringed topoi”.

> **Stacks 0DH0.** The degreewise square commutes as a square of *ringed* topoi, in the sense
> of Stacks 04IC: the two composites `h_{total} ∘ g_n` and `g'_n ∘ h_n` are 2-isomorphic.
>
> The comparison of the direct images is the one of Stacks 0D96, and the compatibility with the
> three structure maps is `componentRingedToposHom_commutes` read on underlying sheaves of sets,
> through `AlgebraicGeometry.RingedToposHom.TwoIso.ofInverseImageIso`, which transposes a
> compatibility of the inverse-image forms into one of the direct-image forms. The underlying
> comparison of inverse images is pinned by
> `CategoryTheory.CocontinuousSimplicialSite.Morphism.componentInverseImageCommRingIso_forget`,
> so this 2-isomorphism is not an arbitrary one.

```lean
noncomputable def componentRingedToposHom_twoIso
    (h : RingedMorphism C C'
      ((Stacks.SheafOfModules.Tensor.ringSheaf (J := C.situation.totalTopology)) O)
      ((Stacks.SheafOfModules.Tensor.ringSheaf (J := C'.situation.totalTopology)) O'))
    (n : SimplexCategory) :
    RingedToposHom.TwoIso.{u, u, u, u, u, u}
      (viaTotalRingedToposHom h n) (viaComponentRingedToposHom h n)
```

**`CategoryTheory.CocontinuousSimplicialSite.RingedMorphism.componentPushforwardModulesSquareIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean, line 1708](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean#L1708). The attribute's comment: “the commutative squares, on direct images of sheaves of modules”.

> **Stacks 0DH0, the degreewise square on direct images of sheaves of modules.** Direct image
> to the total ringed topos of the target, taken through the component of degree `n` of the
> source, agrees with direct image taken through the component of degree `n` of the target:
>
> `h_{total,*} ∘ g_{n,*} ≅ g'_{n,*} ∘ h_{n,*}` on `Mod(𝒪_n)`.
>
> This is the commuting square of ringed topoi of
> `componentRingedToposHom_twoIso` read on sheaves of modules, and it is a genuine module-level
> statement: the comparison is additive and linear, not merely a comparison of underlying sheaves
> of sets.

```lean
noncomputable def componentPushforwardModulesSquareIso
    (h : RingedMorphism C C'
      ((Stacks.SheafOfModules.Tensor.ringSheaf (J := C.situation.totalTopology)) O)
      ((Stacks.SheafOfModules.Tensor.ringSheaf (J := C'.situation.totalTopology)) O'))
    (n : SimplexCategory) :
    (C.situation.componentRingedToposHom O n).pushforwardModules ⋙
        h.totalRingedToposHom.pushforwardModules ≅
      (h.componentRingedToposHom n).pushforwardModules ⋙
        (C'.situation.componentRingedToposHom O' n).pushforwardModules
```

**`CategoryTheory.CocontinuousSimplicialSite.RingedMorphism.componentPullbackModulesSquareIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean, line 1731](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean#L1731). The attribute's comment: “the commutative squares, on pullbacks of sheaves of modules”.

> **Stacks 0DH0, the degreewise square on pullbacks of sheaves of modules.** The same square,
> read on pullbacks:
>
> `g_n^* ∘ h_{total}^* ≅ h_n^* ∘ (g'_n)^*` on `Mod(𝒪')`.
>
> Both sides are left adjoint to the two sides of `componentPushforwardModulesSquareIso`, so this
> is uniqueness of left adjoints applied to that isomorphism.

```lean
noncomputable def componentPullbackModulesSquareIso
    (h : RingedMorphism C C' (Stacks.SheafOfModules.Tensor.ringSheaf O)
      (Stacks.SheafOfModules.Tensor.ringSheaf O')) (n : SimplexCategory) :
    h.totalRingedToposHom.toModulesHom.pullbackModules ⋙
        (C.situation.componentRingedToposHom O n).toModulesHom.pullbackModules ≅
      (C'.situation.componentRingedToposHom O' n).toModulesHom.pullbackModules ⋙
        (h.componentRingedToposHom n).toModulesHom.pullbackModules
```

**`CategoryTheory.CocontinuousSimplicialSite.RingedMorphism.componentPushforwardModulesComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean, line 1754](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean#L1754). The attribute's comment: “the comparison of the last assertion, on sheaves of modules”.

> **Stacks 0DH0, the comparison of the last assertion.** The canonical morphism of functors
> `Mod(𝒪) ⟶ Mod(𝒪'_n)`
>
> `(g'_n)^* ∘ h_{total,*} ⟶ h_{n,*} ∘ g_n^*`
>
> attached to the degreewise square: the mate of `componentPushforwardModulesSquareIso` under the
> two adjunctions `g_n^* ⊣ g_{n,*}` and `(g'_n)^* ⊣ (g'_n)_*` of Stacks 03D7. The source's last
> assertion is that this comparison is invertible, which is
> `isIso_componentPushforwardModulesComparison`.

```lean
noncomputable def componentPushforwardModulesComparison
    (h : RingedMorphism C C'
      ((Stacks.SheafOfModules.Tensor.ringSheaf (J := C.situation.totalTopology)) O)
      ((Stacks.SheafOfModules.Tensor.ringSheaf (J := C'.situation.totalTopology)) O'))
    (n : SimplexCategory) :
    h.totalRingedToposHom.pushforwardModules ⋙
        (C'.situation.componentRingedToposHom O' n).toModulesHom.pullbackModules ⟶
      (C.situation.componentRingedToposHom O n).toModulesHom.pullbackModules ⋙
        (h.componentRingedToposHom n).pushforwardModules
```

**`CategoryTheory.CocontinuousSimplicialSite.RingedMorphism.componentPushforwardModulesComparison_mate`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean, line 1774](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean#L1774). The attribute's comment: “the comparison of the last assertion is the mate of the square”.

> **Stacks 0DH0.** The comparison of the last assertion is pinned by the degreewise square:
> its mate under the two adjunctions of Stacks 03D7 is the square of direct images of sheaves of
> modules. In particular it is not an arbitrary natural transformation.

```lean
theorem componentPushforwardModulesComparison_mate
    (h : RingedMorphism C C'
      ((Stacks.SheafOfModules.Tensor.ringSheaf (J := C.situation.totalTopology)) O)
      ((Stacks.SheafOfModules.Tensor.ringSheaf (J := C'.situation.totalTopology)) O'))
    (n : SimplexCategory) :
    mateEquiv
        (RingedToposHom.pullbackAdjPushforwardModules
          (C.situation.componentRingedToposHom O n))
        (RingedToposHom.pullbackAdjPushforwardModules
          (C'.situation.componentRingedToposHom O' n))
        (componentPushforwardModulesComparison h n) =
      TwoSquare.mk _ _ _ _ (componentPushforwardModulesSquareIso h n).hom
```

**`CategoryTheory.CocontinuousSimplicialSite.RingedMorphism.isIso_componentPushforwardModulesComparison`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean, line 1809](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean#L1809). The attribute's comment: “the comparison of the last assertion is invertible”.

> **Stacks 0DH0, the last assertion: the comparison is invertible.** The canonical comparison
> `(g'_n)^* ∘ h_{total,*} ⟶ h_{n,*} ∘ g_n^*` of sheaves of modules is an isomorphism. On
> underlying sheaves of sets it is the mate of the degreewise square of topoi, which is invertible
> by the Beck–Chevalley property of the square of component inclusions,
> `CategoryTheory.CocontinuousSimplicialSite.Morphism.isIso_totalComponentPushforwardMate`; and
> the two pullbacks `g_n^*`, `(g'_n)^*` are inverse images on underlying sheaves of sets, so the
> module-level mate lies over that one
> (`AlgebraicGeometry.RingedToposHom.isIso_mateEquiv_symm_pushforwardModules_of_isIso`).

```lean
instance isIso_componentPushforwardModulesComparison
    (h : RingedMorphism C C'
      ((Stacks.SheafOfModules.Tensor.ringSheaf (J := C.situation.totalTopology)) O)
      ((Stacks.SheafOfModules.Tensor.ringSheaf (J := C'.situation.totalTopology)) O'))
    (n : SimplexCategory) :
    IsIso (componentPushforwardModulesComparison h n)
```

**`CategoryTheory.CocontinuousSimplicialSite.RingedMorphism.componentPushforwardModulesIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean, line 1834](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean#L1834). The attribute's comment: “the last assertion, on sheaves of modules”.

> **Stacks 0DH0, the last assertion, on sheaves of modules.** Inverse image to the simplicial
> component of degree `n` of a direct image of sheaves of modules along the total morphism is the
> degreewise direct image of the inverse image to that component:
>
> `(g'_n)^* ∘ h_{total,*} ≅ h_{n,*} ∘ g_n^*` as functors `Mod(𝒪) ⟶ Mod(𝒪'_n)`,
>
> the isomorphism being the canonical comparison `componentPushforwardModulesComparison`
> attached to the degreewise square, which is invertible by
> `isIso_componentPushforwardModulesComparison`.

```lean
noncomputable def componentPushforwardModulesIso
    (h : RingedMorphism C C'
      ((Stacks.SheafOfModules.Tensor.ringSheaf (J := C.situation.totalTopology)) O)
      ((Stacks.SheafOfModules.Tensor.ringSheaf (J := C'.situation.totalTopology)) O'))
    (n : SimplexCategory) :
    h.totalRingedToposHom.pushforwardModules ⋙
        (C'.situation.componentRingedToposHom O' n).toModulesHom.pullbackModules ≅
      (C.situation.componentRingedToposHom O n).toModulesHom.pullbackModules ⋙
        (h.componentRingedToposHom n).pushforwardModules
```

**`CategoryTheory.SimplicialSite.Morphism.componentInverseImageCommRingIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphismContinuous.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphismContinuous.lean#L134). The attribute's comment: “the canonical ring comparison, case (A)”.

> **Stacks 0DH0**, case (A). The comparison of the two inverse images of sheaves of
> commutative rings around the square of simplicial degree `n`: the identification
> `gₙ⁻¹h_{total}⁻¹𝒪' = hₙ⁻¹(g'ₙ)⁻¹𝒪'` through which the source defines the degreewise structure
> map.

```lean
def componentInverseImageCommRingIso (h : SimplicialSite.Morphism C C') (n : SimplexCategory) :
    inverseImageCommRingFunctor.{u, u, u, u, u, u} (viaTotalMorphism h n) ≅
      inverseImageCommRingFunctor.{u, u, u, u, u, u} (viaComponentMorphism h n)
```

**`CategoryTheory.SimplicialSite.Morphism.componentInverseImageCommRingIso_forget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphismContinuous.lean, line 145](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphismContinuous.lean#L145). The attribute's comment: “the canonical underlying comparison, case (A)”.

> **Stacks 0DH0**, case (A). The comparison of inverse images of sheaves of commutative rings
> has the comparison of inverse images of sheaves of sets as its underlying map.

```lean
theorem componentInverseImageCommRingIso_forget (h : SimplicialSite.Morphism C C')
    (n : SimplexCategory) (O' : Sheaf C'.situation.totalTopology CommRingCat.{u}) :
    (sheafCompose (C.situation.componentTopology n) (forget CommRingCat.{u})).map
        ((componentInverseImageCommRingIso h n).hom.app O') =
      (componentInverseImageIso h n).hom.app
        ((sheafCompose C'.situation.totalTopology (forget CommRingCat.{u})).obj O')
```

**`CategoryTheory.SimplicialSite.RingedMorphism.totalRingedToposHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphismContinuous.lean, line 189](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphismContinuous.lean#L189). The attribute's comment: “the total morphism of ringed topoi, case (A)”.

> **Stacks 0DH0**, case (A). The morphism of total ringed topoi induced by a morphism between
> ringed simplicial sites.

```lean
def totalRingedToposHom
    (h : RingedMorphism C C' (C.totalRingSheaf O) (C'.totalRingSheaf O')) :
    RingedToposHom (C.situation.totalRingedTopos O) (C'.situation.totalRingedTopos O')
```

**`CategoryTheory.SimplicialSite.RingedMorphism.componentRingedToposHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphismContinuous.lean, line 227](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphismContinuous.lean#L227). The attribute's comment: “the component morphisms of ringed topoi, case (A)”.

> **Stacks 0DH0**, case (A). The morphism of component ringed topoi in simplicial degree `n`
> induced by a morphism between ringed simplicial sites.

```lean
def componentRingedToposHom
    (h : RingedMorphism C C' (C.totalRingSheaf O) (C'.totalRingSheaf O')) (n : SimplexCategory) :
    RingedToposHom (C.situation.componentRingedTopos O n)
      (C'.situation.componentRingedTopos O' n)
```

**`CategoryTheory.SimplicialSite.RingedMorphism.componentRingedToposHom_toToposHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphismContinuous.lean, line 242](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphismContinuous.lean#L242). The attribute's comment: “the underlying degreewise geometric morphisms, case (A)”.

> **Stacks 0DH0**, case (A). The underlying geometric morphism of the degreewise morphism of
> ringed topoi is the component morphism of topoi of Stacks 0D95.

```lean
theorem componentRingedToposHom_toToposHom
    (h : RingedMorphism C C' (C.totalRingSheaf O) (C'.totalRingSheaf O')) (n : SimplexCategory) :
    (h.componentRingedToposHom n).toToposHom =
      (SimplicialSiteMorphism.ofMorphismOfSites h.hom).componentMorphism n
```

**`CategoryTheory.SimplicialSite.RingedMorphism.componentRingedToposHom_commutes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphismContinuous.lean, line 258](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphismContinuous.lean#L258). The attribute's comment: “the commutative squares of ringed topoi, case (A)”.

> **Stacks 0DH0**, case (A). The square of ringed topoi formed by the total morphism, the
> degreewise morphism and the two canonical morphisms from the components of simplicial degree `n`
> commutes: the comparison of inverse images identifies the two composite structure maps.

```lean
theorem componentRingedToposHom_commutes
    (h : RingedMorphism C C' (C.totalRingSheaf O) (C'.totalRingSheaf O')) (n : SimplexCategory) :
    (h.hom.componentInverseImageCommRingIso n).hom.app O' ≫
        ((C'.situation.componentRingedToposHom O' n).comp
          (h.componentRingedToposHom n)).fSharpInverseImage =
      (h.totalRingedToposHom.comp
        (C.situation.componentRingedToposHom O n)).fSharpInverseImage
```

**`CategoryTheory.SimplicialSite.RingedMorphism.componentRingedToposHom_twoIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphismContinuous.lean, line 319](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphismContinuous.lean#L319). The attribute's comment: “the degreewise square as a 2-isomorphism of ringed topoi, case (A)”.

> **Stacks 0DH0**, case (A). The degreewise square commutes as a square of *ringed* topoi, in
> the sense of Stacks 04IC: the two composites `h_{total} ∘ g_n` and `g'_n ∘ h_n` are
> 2-isomorphic, the comparison of direct images being the one of Stacks 0D96.

```lean
noncomputable def componentRingedToposHom_twoIso
    (h : RingedMorphism C C' (C.totalRingSheaf O) (C'.totalRingSheaf O')) (n : SimplexCategory) :
    RingedToposHom.TwoIso.{u, u, u, u, u, u}
      (viaTotalRingedToposHom h n) (viaComponentRingedToposHom h n)
```

**`CategoryTheory.SimplicialSite.RingedMorphism.componentPushforwardModulesSquareIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphismContinuous.lean, line 341](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphismContinuous.lean#L341). The attribute's comment: “the commutative squares, on direct images of sheaves of modules, case (A)”.

> **Stacks 0DH0**, case (A), the degreewise square on direct images of sheaves of modules:
> `h_{total,*} ∘ g_{n,*} ≅ g'_{n,*} ∘ h_{n,*}` on `Mod(𝒪_n)`.

```lean
noncomputable def componentPushforwardModulesSquareIso
    (h : RingedMorphism C C' (C.totalRingSheaf O) (C'.totalRingSheaf O')) (n : SimplexCategory) :
    (C.situation.componentRingedToposHom O n).pushforwardModules ⋙
        h.totalRingedToposHom.pushforwardModules ≅
      (h.componentRingedToposHom n).pushforwardModules ⋙
        (C'.situation.componentRingedToposHom O' n).pushforwardModules
```

**`CategoryTheory.SimplicialSite.RingedMorphism.componentPullbackModulesSquareIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphismContinuous.lean, line 356](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphismContinuous.lean#L356). The attribute's comment: “the commutative squares, on pullbacks of sheaves of modules, case (A)”.

> **Stacks 0DH0**, case (A), the degreewise square on pullbacks of sheaves of modules:
> `g_n^* ∘ h_{total}^* ≅ h_n^* ∘ (g'_n)^*` on `Mod(𝒪')`.

```lean
noncomputable def componentPullbackModulesSquareIso
    (h : RingedMorphism C C' (C.totalRingSheaf O) (C'.totalRingSheaf O')) (n : SimplexCategory) :
    h.totalRingedToposHom.toModulesHom.pullbackModules ⋙
        (C.situation.componentRingedToposHom O n).toModulesHom.pullbackModules ≅
      (C'.situation.componentRingedToposHom O' n).toModulesHom.pullbackModules ⋙
        (h.componentRingedToposHom n).toModulesHom.pullbackModules
```

**`CategoryTheory.SimplicialSite.RingedMorphism.componentPushforwardModulesComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphismContinuous.lean, line 376](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphismContinuous.lean#L376). The attribute's comment: “the comparison of the last assertion, on sheaves of modules, case (A)”.

> **Stacks 0DH0**, case (A), the comparison of the last assertion: the canonical morphism of
> functors `Mod(𝒪) ⟶ Mod(𝒪'_n)`
>
> `(g'_n)^* ∘ h_{total,*} ⟶ h_{n,*} ∘ g_n^*`,
>
> the mate of `componentPushforwardModulesSquareIso` under the two adjunctions `g_n^* ⊣ g_{n,*}`
> and `(g'_n)^* ⊣ (g'_n)_*` of Stacks 03D7.

```lean
noncomputable def componentPushforwardModulesComparison
    (h : RingedMorphism C C' (C.totalRingSheaf O) (C'.totalRingSheaf O')) (n : SimplexCategory) :
    h.totalRingedToposHom.pushforwardModules ⋙
        (C'.situation.componentRingedToposHom O' n).toModulesHom.pullbackModules ⟶
      (C.situation.componentRingedToposHom O n).toModulesHom.pullbackModules ⋙
        (h.componentRingedToposHom n).pushforwardModules
```

**`CategoryTheory.SimplicialSite.RingedMorphism.componentPushforwardModulesComparison_mate`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphismContinuous.lean, line 393](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphismContinuous.lean#L393). The attribute's comment: “the comparison of the last assertion is the mate of the square, case (A)”.

> **Stacks 0DH0**, case (A). The comparison of the last assertion is pinned by the degreewise
> square: its mate under the two adjunctions of Stacks 03D7 is the square of direct images of
> sheaves of modules.

```lean
theorem componentPushforwardModulesComparison_mate
    (h : RingedMorphism C C' (C.totalRingSheaf O) (C'.totalRingSheaf O')) (n : SimplexCategory) :
    mateEquiv
        (RingedToposHom.pullbackAdjPushforwardModules
          (C.situation.componentRingedToposHom O n))
        (RingedToposHom.pullbackAdjPushforwardModules
          (C'.situation.componentRingedToposHom O' n))
        (componentPushforwardModulesComparison h n) =
      TwoSquare.mk _ _ _ _ (componentPushforwardModulesSquareIso h n).hom
```

**`CategoryTheory.SimplicialSite.RingedMorphism.isIso_componentPushforwardModulesComparison`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphismContinuous.lean, line 417](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphismContinuous.lean#L417). The attribute's comment: “the comparison of the last assertion is invertible, case (A)”.

> **Stacks 0DH0**, case (A), the last assertion: the comparison is invertible. On underlying
> sheaves of sets it is the mate of the degreewise square of topoi, which is invertible by
> `CategoryTheory.SimplicialSite.Morphism.isIso_totalComponentPushforwardMate`.

```lean
instance isIso_componentPushforwardModulesComparison
    (h : RingedMorphism C C' (C.totalRingSheaf O) (C'.totalRingSheaf O')) (n : SimplexCategory) :
    IsIso (componentPushforwardModulesComparison h n)
```

**`CategoryTheory.SimplicialSite.RingedMorphism.componentPushforwardModulesIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphismContinuous.lean, line 435](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphismContinuous.lean#L435). The attribute's comment: “the last assertion, on sheaves of modules, case (A)”.

> **Stacks 0DH0**, case (A), the last assertion, on sheaves of modules:
>
> `(g'_n)^* ∘ h_{total,*} ≅ h_{n,*} ∘ g_n^*` as functors `Mod(𝒪) ⟶ Mod(𝒪'_n)`,
>
> the isomorphism being the canonical comparison `componentPushforwardModulesComparison`.

```lean
noncomputable def componentPushforwardModulesIso
    (h : RingedMorphism C C' (C.totalRingSheaf O) (C'.totalRingSheaf O')) (n : SimplexCategory) :
    h.totalRingedToposHom.pushforwardModules ⋙
        (C'.situation.componentRingedToposHom O' n).toModulesHom.pullbackModules ≅
      (C.situation.componentRingedToposHom O n).toModulesHom.pullbackModules ⋙
        (h.componentRingedToposHom n).pushforwardModules
```

## Tag 0DH1, a lemma

[Tag 0DH1](https://stacks.math.columbia.edu/tag/0DH1) in the Stacks Project.

**`CategoryTheory.SimplicialSite.RingedMorphism.derivedComponentPushforwardModulesIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphismContinuousDerivedPushforward.lean, line 459](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphismContinuousDerivedPushforward.lean#L459). The attribute's comment: “case (A)”.

> **Stacks 0DH1**, case (A). With notation and hypotheses as in Stacks 0DH0, for simplicial
> sites whose transitions are morphisms of sites and a morphism of ringed simplicial sites built
> from morphisms of sites: for `K` in the unbounded derived category of sheaves of `𝒪`-modules on
> the total site,
>
> `(g'_n)^* Rh_{total,*} K = Rh_{n,*} g_n^* K`.
>
> The source's equality is read as a natural isomorphism of functors on the derived category.
> Both sides are right derived functors of one and the same functor on the unbounded homotopy
> category of `𝒪`-modules, by
> `isRightDerivedFunctor_derivedTotalPushforwardRestrictModulesUnit` and
> `isRightDerivedFunctor_derivedRestrictTotalPushforwardModulesUnit` of this namespace, the two
> being identified by the canonical comparison of Stacks 0DH0, `componentPushforwardModulesIso`.
> The isomorphism is the induced comparison of the two right derived functors, pinned down by
> `derivedComponentPushforwardModulesIso_fac`.

```lean
def derivedComponentPushforwardModulesIso
    (h : SimplicialSite.RingedMorphism C C' (C.totalRingSheaf O) (C'.totalRingSheaf O'))
    (n : SimplexCategory) :
    derivedTotalPushforwardModules h ⋙
        C'.situation.derivedComponentPullbackModules O' n ≅
      C.situation.derivedComponentPullbackModules O n ⋙
        derivedComponentPushforwardModules h n
```

**`CategoryTheory.SimplicialSiteSituation.componentPullbackModules_preservesFiniteLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphismDerivedPushforward.lean, line 243](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphismDerivedPushforward.lean#L243). The attribute's comment: “exactness of the pullback of modules to a component”. References: SGA 4 IV (13.7), “special case”.

> **Pullback of sheaves of modules to the simplicial component of degree `n` is left exact.**
> The component structure sheaf is the restriction of the total one, so the component structure
> map is invertible and the pullback of modules has the inverse image of sheaves of sets as its
> underlying sheaf, by
> `CategoryTheory.SimplicialSiteSituation.componentPullbackUnderlyingIso`; the inverse image is
> left exact because `g_n` is a morphism of topoi, and the underlying-sheaf functor on sheaves of
> modules preserves finite limits and reflects isomorphisms, hence reflects finite limits.
>
> This is the source's observation that `g_n^* = g_n^{-1}` is exact, which is what makes `Lg_n^*`
> computable on any representative complex.

```lean
theorem componentPullbackModules_preservesFiniteLimits :
    PreservesFiniteLimits (componentRingedToposHom S O n).toModulesHom.pullbackModules
```

**`CategoryTheory.SimplicialSiteSituation.componentPullbackModules_preservesFiniteColimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphismDerivedPushforward.lean, line 265](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphismDerivedPushforward.lean#L265). The attribute's comment: “exactness of the pullback of modules to a component”.

> **Pullback of sheaves of modules to the simplicial component of degree `n` is right exact**,
> being a left adjoint. This is the finite case of Stacks 03DC part (2).

```lean
theorem componentPullbackModules_preservesFiniteColimits :
    PreservesFiniteColimits (componentRingedToposHom S O n).toModulesHom.pullbackModules
```

**`CategoryTheory.CocontinuousSimplicialSite.RingedMorphism.derivedComponentPushforwardModulesIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphismDerivedPushforward.lean, line 544](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphismDerivedPushforward.lean#L544). The attribute's comment: “case (B)”.

> **Stacks 0DH1**, case (B). With notation and hypotheses as in Stacks 0DH0: for `K` in the
> unbounded derived category of sheaves of `𝒪`-modules on the total site,
>
> `(g'_n)^* Rh_{total,*} K = Rh_{n,*} g_n^* K`.
>
> The source's equality is read as a natural isomorphism of functors on the derived category.
> Both sides are right derived functors of one and the same functor on the unbounded homotopy
> category of `𝒪`-modules, by
> `isRightDerivedFunctor_derivedTotalPushforwardRestrictModulesUnit` and
> `isRightDerivedFunctor_derivedRestrictTotalPushforwardModulesUnit` of this namespace, the two
> being identified by the canonical comparison of Stacks 0DH0, `componentPushforwardModulesIso`.
> The isomorphism is the induced comparison of the two right derived functors, pinned down by
> `derivedComponentPushforwardModulesIso_fac`.

```lean
def derivedComponentPushforwardModulesIso :
    derivedTotalPushforwardModules h ⋙
        C'.situation.derivedComponentPullbackModules O' n ≅
      C.situation.derivedComponentPullbackModules O n ⋙
        derivedComponentPushforwardModules h n
```

**`CategoryTheory.CocontinuousSimplicialSite.Morphism.derivedComponentPushforwardModulesIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphismDerivedPushforward.lean, line 750](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphismDerivedPushforward.lean#L750). The attribute's comment: “case (B)”.

> **Stacks 0DH1**, case (B). With notation and hypotheses as in Stacks 0DH0: for `K` in the
> unbounded derived category of sheaves of `𝒪`-modules on the total site,
>
> `(g'_n)^* Rh_{total,*} K = Rh_{n,*} g_n^* K`.
>
> The source's equality is read as a natural isomorphism of functors on the derived category.
> Both sides are right derived functors of one and the same functor on the unbounded homotopy
> category of `𝒪`-modules, by
> `isRightDerivedFunctor_derivedTotalPushforwardRestrictModulesUnit` and
> `isRightDerivedFunctor_derivedRestrictTotalPushforwardModulesUnit` of this namespace, the two
> being identified by the underived comparison `e`.
>
> The hypothesis `e` is the last assertion of Stacks 0DH0 at the level of sheaves of modules, and
> `hK` is Stacks 09WH for sheaves of modules; see the implementation notes of this file for why
> both are deferred.

```lean
def derivedComponentPushforwardModulesIso
    (e : (h.totalRingedToposHom φ).pushforwardModules ⋙
        (C'.situation.componentRingedToposHom O' n).toModulesHom.pullbackModules ≅
      (C.situation.componentRingedToposHom O n).toModulesHom.pullbackModules ⋙
        ((h.componentRingedToposHom φ) n).pushforwardModules)
    (hK : ∀ I : CochainComplex (SheafOfModules.{u}
        ((Stacks.SheafOfModules.Tensor.ringSheaf (J := (C.situation.totalRingedTopos O).J)
            (C.situation.totalRingedTopos O).O))) ℤ,
      I.IsKInjective →
        CochainComplex.IsKInjective
          (((C.situation.componentRingedToposHom O n).toModulesHom.pullbackModules
              |>.mapHomologicalComplex (ComplexShape.up ℤ)).obj I)) :
    derivedTotalPushforwardModules h φ ⋙
        C'.situation.derivedComponentPullbackModules O' n ≅
      C.situation.derivedComponentPullbackModules O n ⋙
        derivedComponentPushforwardModules h φ n
```

**`CategoryTheory.CocontinuousSimplicialSite.Morphism.derivedComponentPushforwardModulesIso_fac`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphismDerivedPushforward.lean, line 781](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphismDerivedPushforward.lean#L781). The attribute's comment: “case (B), the canonical comparison”.

> **Stacks 0DH1**, the isomorphism is the canonical one. Composing the canonical comparison
> into the first right derived functor with the isomorphism gives the underived comparison
> followed by the canonical comparison into the second. Since a morphism out of a right derived
> functor is determined by that identity, this pins the isomorphism down completely.

```lean
theorem derivedComponentPushforwardModulesIso_fac
    (e : (h.totalRingedToposHom φ).pushforwardModules ⋙
        (C'.situation.componentRingedToposHom O' n).toModulesHom.pullbackModules ≅
      (C.situation.componentRingedToposHom O n).toModulesHom.pullbackModules ⋙
        ((h.componentRingedToposHom φ) n).pushforwardModules)
    (hK : ∀ I : CochainComplex (SheafOfModules.{u}
        ((Stacks.SheafOfModules.Tensor.ringSheaf (J := (C.situation.totalRingedTopos O).J)
            (C.situation.totalRingedTopos O).O))) ℤ,
      I.IsKInjective →
        CochainComplex.IsKInjective
          (((C.situation.componentRingedToposHom O n).toModulesHom.pullbackModules
              |>.mapHomologicalComplex (ComplexShape.up ℤ)).obj I)) :
    derivedTotalPushforwardRestrictModulesUnit h φ n ≫
        Functor.whiskerLeft DerivedCategory.Qh
          (derivedComponentPushforwardModulesIso h φ n e hK).hom =
      (Functor.isoWhiskerRight (homotopyComponentPushforwardModulesIso h φ n e)
            DerivedCategory.Qh).hom ≫
        derivedRestrictTotalPushforwardModulesUnit h φ n
```

**`CategoryTheory.CocontinuousSimplicialSite.Morphism.derivedComponentPushforwardModulesIsoOfSquare`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphismDerivedPushforward.lean, line 832](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphismDerivedPushforward.lean#L832). The attribute's comment: “case (B), over the canonical comparison of the degreewise square”.

> **Stacks 0DH1**, case (B), over the canonical comparison of the degreewise square. With
> notation and hypotheses as in Stacks 0DH0: for `K` in the unbounded derived category of sheaves
> of `𝒪`-modules on the total site,
>
> `(g'_n)^* Rh_{total,*} K = Rh_{n,*} g_n^* K`.
>
> This is `derivedComponentPushforwardModulesIso` with the underived comparison taken to be the
> canonical one of
> `CategoryTheory.CocontinuousSimplicialSite.Morphism.componentPushforwardModulesIso`,
> rather than an arbitrary isomorphism. The only hypothesis is `hK`, Stacks 09WH for sheaves of
> modules; see the implementation notes of this file.

```lean
def derivedComponentPushforwardModulesIsoOfSquare
    (hK : ∀ I : CochainComplex (SheafOfModules.{u}
        ((Stacks.SheafOfModules.Tensor.ringSheaf (J := (C.situation.totalRingedTopos O).J)
            (C.situation.totalRingedTopos O).O))) ℤ,
      I.IsKInjective →
        CochainComplex.IsKInjective
          (((C.situation.componentRingedToposHom O n).toModulesHom.pullbackModules
              |>.mapHomologicalComplex (ComplexShape.up ℤ)).obj I)) :
    derivedTotalPushforwardModules h φ ⋙
        C'.situation.derivedComponentPullbackModules O' n ≅
      C.situation.derivedComponentPullbackModules O n ⋙
        derivedComponentPushforwardModules h φ n
```

**`CategoryTheory.CocontinuousSimplicialSite.Morphism.derivedComponentPushforwardModulesIsoOfSquare_fac`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphismDerivedPushforward.lean, line 854](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphismDerivedPushforward.lean#L854). The attribute's comment: “case (B), the canonical comparison of the degreewise square pins the isomorphism”.

> **Stacks 0DH1**, case (B) over the canonical comparison: the isomorphism is pinned by the
> canonical comparison of the degreewise square. Composing the canonical comparison into the
> first right derived functor with it gives the canonical underived comparison, applied
> degreewise to complexes, followed by the canonical comparison into the second right derived
> functor. Since a morphism out of a right derived functor is determined by that identity, this
> determines the isomorphism completely from the square of ringed topoi.

```lean
theorem derivedComponentPushforwardModulesIsoOfSquare_fac
    (hK : ∀ I : CochainComplex (SheafOfModules.{u}
        ((Stacks.SheafOfModules.Tensor.ringSheaf (J := (C.situation.totalRingedTopos O).J)
            (C.situation.totalRingedTopos O).O))) ℤ,
      I.IsKInjective →
        CochainComplex.IsKInjective
          (((C.situation.componentRingedToposHom O n).toModulesHom.pullbackModules
              |>.mapHomologicalComplex (ComplexShape.up ℤ)).obj I)) :
    derivedTotalPushforwardRestrictModulesUnit h φ n ≫
        Functor.whiskerLeft DerivedCategory.Qh
          (derivedComponentPushforwardModulesIsoOfSquare h φ n hK).hom =
      (Functor.isoWhiskerRight
            (homotopyComponentPushforwardModulesIso h φ n
              (componentPushforwardModulesIso h φ n)) DerivedCategory.Qh).hom ≫
        derivedRestrictTotalPushforwardModulesUnit h φ n
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 85.7, Tag 0DGY](https://stacks.math.columbia.edu/tag/0DGY)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
