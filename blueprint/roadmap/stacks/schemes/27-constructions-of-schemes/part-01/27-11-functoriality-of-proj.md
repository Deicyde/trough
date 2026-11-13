---
declaration: section
origin: cited
lean: Stacks.AlgebraicGeometry.ProjMapCard.projMapData_preserves_products, Stacks.AlgebraicGeometry.ProjMapCardUnit.projMapData_preserves_unit, Stacks.AlgebraicGeometry.ProjTwistChain.awayToSection_comp_appLE_mapHom, Stacks.AlgebraicGeometry.ProjTwistChain.eq_mapHom, Stacks.AlgebraicGeometry.ProjMapUniqueTwist.projMapData_twistMap_unique, Stacks.AlgebraicGeometry.ProjShared.mapDomain, Stacks.AlgebraicGeometry.ProjTwistChain.mapHom_preimage_basicOpen, Stacks.AlgebraicGeometry.ProjTwistCompare.projMapData
statement: formalized
proof: formalized
---

# 27.11 Functoriality of Proj

Section 27.11 of the Stacks Project, [Tag 01MX](https://stacks.math.columbia.edu/tag/01MX). 8 tags here are carried by 27 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01MY, a lemma

[Tag 01MY](https://stacks.math.columbia.edu/tag/01MY) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProjMapCard.projMapData_preserves_products`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjMapCard/Multiplication.lean, line 345](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjMapCard/Multiplication.lean#L345). The attribute's comment: “graded-algebra multiplication”.

> **Tag 01MY, graded-algebra multiplication, on the canonical bundle.** The tagged
> statement's spelling of `twistMap_comp_pullbackTwistMultiplication`: the morphism and the twist
> maps are the fields of `Stacks.AlgebraicGeometry.ProjTwistCompare.projMapData`.

```lean
public theorem projMapData_preserves_products (ψ : 𝒜 →+*ᵍ ℬ)
    (n m : ℤ) :
    pullbackTwistMultiplication 𝒜 (projMapData 𝒜 ℬ ψ).hom n m ≫
      (projMapData 𝒜 ℬ ψ).twistMap (n + m) =
    ((Functor.uncurry.obj (Stacks.SheafOfModules.Tensor.sheafTensor.{u, u, u, u, u}
      ⟨(((mapDomain 𝒜 ℬ ψ).toScheme.toRingedSpace)).presheaf,
      (((mapDomain 𝒜 ℬ ψ).toScheme.toRingedSpace)).IsSheaf⟩)).map
      ((((projMapData 𝒜 ℬ ψ).twistMap n), ((projMapData 𝒜 ℬ ψ).twistMap m)) : (_, _) ⟶ (_, _))) ≫
      pullbackTwistMultiplication ℬ (mapDomain 𝒜 ℬ ψ).ι n m
```

**`Stacks.AlgebraicGeometry.ProjMapCardUnit.projMapData_preserves_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjMapCardUnit/Basic.lean, line 332](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjMapCardUnit/Basic.lean#L332). The attribute's comment: “graded-algebra unit”.

> **Tag 01MY, the graded-algebra unit, on the canonical bundle.** The Stacks statement's
> spelling of `twistMap_comp_pullbackTwistUnit`: the morphism and the twist maps are the fields of
> `Stacks.AlgebraicGeometry.ProjTwistCompare.projMapData`.

```lean
theorem projMapData_preserves_unit (ψ : 𝒜 →+*ᵍ ℬ) :
    pullbackTwistUnit 𝒜 (projMapData 𝒜 ℬ ψ).hom ≫ (projMapData 𝒜 ℬ ψ).twistMap 0 =
      pullbackTwistUnit ℬ (mapDomain 𝒜 ℬ ψ).ι
```

**`Stacks.AlgebraicGeometry.ProjTwistChain.awayToSection_comp_appLE_mapHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjMapData/Basic.lean, line 166](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjMapData/Basic.lean#L166). The attribute's comment: “part (2), localization map on standard opens”.

> **Stacks 01MY (2)**: on the standard open `D₊(ψ f)` of the domain of definition, the
> morphism induced by `ψ` is the one induced by the map `𝒜_{(f)} → ℬ_{(ψ f)}` of degree-zero
> homogeneous localizations.
>
> With no hypothesis on `ψ`; compare `AlgebraicGeometry.Proj.awayToSection_comp_appLE`, which
> states this for `AlgebraicGeometry.Proj.map` and so assumes `ℬ₊ ≤ 𝒜₊.map ψ`.

```lean
public theorem awayToSection_comp_appLE_mapHom (ψ : 𝒜 →+*ᵍ ℬ) (f : A) (d : ℕ) (hf : f ∈ 𝒜 d)
    (hd : 0 < d) :
    Proj.awayToSection 𝒜 f ≫
      Scheme.Hom.appLE (mapHom 𝒜 ℬ ψ) (Proj.basicOpen 𝒜 f)
        ((mapDomain 𝒜 ℬ ψ).ι ⁻¹ᵁ Proj.basicOpen ℬ (ψ f))
        (by rw [mapHom_preimage_basicOpen 𝒜 ℬ ψ f d hf hd]) =
    CommRingCat.ofHom (Away.map ψ f) ≫
      Proj.awayToSection ℬ (ψ f) ≫
        Scheme.Hom.appLE (mapDomain 𝒜 ℬ ψ).ι (Proj.basicOpen ℬ (ψ f))
          ((mapDomain 𝒜 ℬ ψ).ι ⁻¹ᵁ Proj.basicOpen ℬ (ψ f)) le_rfl
```

**`Stacks.AlgebraicGeometry.ProjTwistChain.eq_mapHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjMapData/Basic.lean, line 183](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjMapData/Basic.lean#L183). The attribute's comment: “uniqueness of the scheme morphism”.

> **Stacks 01MY (2), uniqueness**: a morphism out of the domain of definition that has the
> inverse images of standard opens of Tag 01MY (2), and that on each of them is induced by the
> corresponding map of degree-zero homogeneous localizations, is `mapHom`.

```lean
public theorem eq_mapHom (ψ : 𝒜 →+*ᵍ ℬ)
    (p : (mapDomain 𝒜 ℬ ψ).toScheme ⟶ AlgebraicGeometry.Proj 𝒜)
    (hopen : ∀ (f : A) (d : ℕ), f ∈ 𝒜 d → 0 < d →
      p ⁻¹ᵁ AlgebraicGeometry.Proj.basicOpen 𝒜 f =
        (mapDomain 𝒜 ℬ ψ).ι ⁻¹ᵁ AlgebraicGeometry.Proj.basicOpen ℬ (ψ f))
    (hlocal : ∀ (f : A) (d : ℕ) (hf : f ∈ 𝒜 d) (hd : 0 < d),
      Proj.awayToSection 𝒜 f ≫
        Scheme.Hom.appLE p (Proj.basicOpen 𝒜 f)
          ((mapDomain 𝒜 ℬ ψ).ι ⁻¹ᵁ Proj.basicOpen ℬ (ψ f))
          (by rw [hopen f d hf hd]) =
      CommRingCat.ofHom (Away.map ψ f) ≫
        Proj.awayToSection ℬ (ψ f) ≫
          Scheme.Hom.appLE (mapDomain 𝒜 ℬ ψ).ι (Proj.basicOpen ℬ (ψ f))
            ((mapDomain 𝒜 ℬ ψ).ι ⁻¹ᵁ Proj.basicOpen ℬ (ψ f)) le_rfl) :
    p = mapHom 𝒜 ℬ ψ
```

**`Stacks.AlgebraicGeometry.ProjMapUniqueTwist.projMapData_twistMap_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjMapUniqueTwist/Basic.lean, line 283](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjMapUniqueTwist/Basic.lean#L283). The attribute's comment: “uniqueness of the graded-algebra map”.

> **Tag 01MY, uniqueness of the graded-algebra map.** A bundle of the canonical morphism with
> maps on all twists which satisfies condition (1) at `⊤`, the multiplication law in all integer
> degrees and the unit law is the canonical bundle.
>
> Together with `Stacks.AlgebraicGeometry.ProjMapData.eq_mapHom`, this is uniqueness of the
> canonical triple of Tag 01MY.

```lean
public theorem projMapData_twistMap_unique (𝒜 : ℕ → σ) (ℬ : ℕ → τ) [GradedRing 𝒜] [GradedRing ℬ]
    (ψ : 𝒜 →+*ᵍ ℬ) (D : ProjMapData 𝒜 ℬ ψ)
    (hh : D.hom = (projMapData 𝒜 ℬ ψ).hom)
    (hdegree : ∀ (n : ℕ) (a : 𝒜 n),
      (D.twistMap (n : ℤ)).val.app (.op ⊤)
        (((Scheme.Modules.pullbackPushforwardAdjunction D.hom).unit.app
          (twistingSheaf 𝒜 (n : ℤ))).val.app (.op ⊤)
            (degreeSection 𝒜 n a)) =
      ((Scheme.Modules.pullbackPushforwardAdjunction (mapDomain 𝒜 ℬ ψ).ι).unit.app
        (twistingSheaf ℬ (n : ℤ))).val.app (.op ⊤)
          (degreeSection ℬ n ⟨ψ a, ψ.map_mem a.2⟩))
    (hmul : ∀ n m : ℤ,
      pullbackTwistMultiplication 𝒜 D.hom n m ≫ D.twistMap (n + m) =
      ((Functor.uncurry.obj (Stacks.SheafOfModules.Tensor.sheafTensor ⟨(((mapDomain 𝒜 ℬ
        ψ).toScheme.toRingedSpace)).presheaf, (((mapDomain 𝒜 ℬ
        ψ).toScheme.toRingedSpace)).IsSheaf⟩)).map
          (((D.twistMap n), (D.twistMap m)) : (_, _) ⟶ (_, _))) ≫
        pullbackTwistMultiplication ℬ (mapDomain 𝒜 ℬ ψ).ι n m)
    (hunit : pullbackTwistUnit 𝒜 D.hom ≫ D.twistMap 0 =
      pullbackTwistUnit ℬ (mapDomain 𝒜 ℬ ψ).ι) :
    D = projMapData 𝒜 ℬ ψ
```

**`Stacks.AlgebraicGeometry.ProjShared.mapDomain`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjShared/MapDomain.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjShared/MapDomain.lean#L89). The attribute's comment: “the open domain”. References: EGA II (2.8.1); EGA II (3.5.6), “partial”.

> The union of the standard opens `D₊(ψ f)` of `Proj ℬ` for `f` homogeneous of positive
> degree: the largest open on which a graded ring homomorphism `ψ` induces a morphism to
> `Proj 𝒜`.

```lean
public def mapDomain (ψ : 𝒜 →+*ᵍ ℬ) : (Proj ℬ).Opens
```

**`Stacks.AlgebraicGeometry.ProjTwistChain.mapHom_preimage_basicOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjTwistChain/MY.lean, line 248](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjTwistChain/MY.lean#L248). The attribute's comment: “part (2), inverse images of standard opens”. References: EGA II (2.8.1).

> **Stacks 01MY (2)**: the inverse image of a standard open of `Proj 𝒜` under the induced
> morphism is the standard open of the image element.

```lean
public theorem mapHom_preimage_basicOpen (ψ : 𝒜 →+*ᵍ ℬ) (f : A) (d : ℕ) (hf : f ∈ 𝒜 d)
    (hd : 0 < d) :
    mapHom 𝒜 ℬ ψ ⁻¹ᵁ AlgebraicGeometry.Proj.basicOpen 𝒜 f =
      (mapDomain 𝒜 ℬ ψ).ι ⁻¹ᵁ AlgebraicGeometry.Proj.basicOpen ℬ (ψ f)
```

**`Stacks.AlgebraicGeometry.ProjTwistCompare.projMapData`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjTwistCompare/Twist.lean, line 358](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjTwistCompare/Twist.lean#L358). The attribute's comment: “the morphism and the maps on all twists”.

> **The canonical bundle of Tag 01MY**: the glued morphism `mapHom` together with the
> comparison maps `θ` on all twists.

```lean
public def projMapData (ψ : 𝒜 →+*ᵍ ℬ) : ProjMapData 𝒜 ℬ ψ
```

**`Stacks.AlgebraicGeometry.ProjTwistGradedAlgebra.thetaGraded`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjTwistGradedAlgebra/Basic.lean, line 198](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjTwistGradedAlgebra/Basic.lean#L198). The attribute's comment: “theta as a single morphism of sheaves of Z-graded algebras: the comparison maps on all integer twists, assembled into one morphism from the pullback along r\_psi of the graded algebra of integer twists of Proj A to the pullback along the inclusion of U(psi) of that of Proj B”.

> The comparison maps on all integer twists, as one homomorphism of sheaves of `ℤ`-graded
> algebras
> `θ : r_ψ^*(⨁_{n ∈ ℤ} 𝒪_{Proj 𝒜}(n)) ⟶ ⨁_{n ∈ ℤ} 𝒪_{Proj ℬ}(n)|_{U(ψ)}`.
> Its degree-`n` component is `Stacks.AlgebraicGeometry.ProjTwistCompare.twistMap`.

```lean
def thetaGraded (ψ : 𝒜 →+*ᵍ ℬ) :
    pullbackTwistAlgebra 𝒜 (mapHom 𝒜 ℬ ψ) ⟶
      pullbackTwistAlgebra ℬ (mapDomain 𝒜 ℬ ψ).ι
```

**`Stacks.AlgebraicGeometry.ProjTwistTheta.twistMap_degreeSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjTwistTheta/DegreeSection.lean, line 225](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjTwistTheta/DegreeSection.lean#L225). The attribute's comment: “part (1), homogeneous global sections”.

> **Tag 01MY, part (1), homogeneous global sections.** The comparison map on the `n`-th twist
> carries the global section of `O(n)` attached to a homogeneous element `a` of degree `n` to the
> global section attached to `psi a`, both read through the unit of the pullback--pushforward
> adjunction.

```lean
public theorem twistMap_degreeSection (ψ : 𝒜 →+*ᵍ ℬ) (n : ℕ) (a : 𝒜 n) :
    ((projMapData 𝒜 ℬ ψ).twistMap (n : ℤ)).val.app (.op ⊤)
      (((Scheme.Modules.pullbackPushforwardAdjunction (projMapData 𝒜 ℬ ψ).hom).unit.app
        (twistingSheaf 𝒜 (n : ℤ))).val.app (.op ⊤)
          (degreeSection 𝒜 n a)) =
    ((Scheme.Modules.pullbackPushforwardAdjunction (mapDomain 𝒜 ℬ ψ).ι).unit.app
      (twistingSheaf ℬ (n : ℤ))).val.app (.op ⊤)
        (degreeSection ℬ n ⟨ψ a, ψ.map_mem a.2⟩)
```

## Tag 01MZ, a lemma

[Tag 01MZ](https://stacks.math.columbia.edu/tag/01MZ) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProjTwistCompTwistMap.mapDomain_mapHom_twistMap_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjTwistCompTwistMap/Statement.lean, line 100](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjTwistCompTwistMap/Statement.lean#L100). The attribute's comment: “the tag's three assertions in one statement, for an arbitrary composable pair of homomorphisms of nonnegatively graded rings: the domain of definition of the composite is the inverse image under `r_ψ` of the domain of definition of `φ`, the morphism of the composite is `r_φ ∘ r_ψ` restricted to that open, and the comparison maps on every twist compose”. References: EGA II (2.8.4).

> **[Stacks, Tag 01MZ].** Let `𝒜`, `ℬ`, `𝒞` be nonnegatively graded rings, write
> `X = Proj 𝒜`, `Y = Proj ℬ`, `Z = Proj 𝒞`, and let `φ : 𝒜 →+*ᵍ ℬ` and `ψ : ℬ →+*ᵍ 𝒞` be
> homomorphisms of graded rings. Then `U(ψ ∘ φ) = r_ψ⁻¹(U(φ))`, the morphism
> `r_{ψ ∘ φ} : U(ψ ∘ φ) ⟶ X` is `r_φ ∘ r_ψ|_{U(ψ ∘ φ)}`, and `θ_ψ ∘ r_ψ^* θ_φ = θ_{ψ ∘ φ}` on
> every twist.
>
> The three conjuncts are, in order:
>
> 1. **The domain of definition of the composite.** `U(ψ ∘ φ)`, an open of `Z`, is the image under
>   the inclusion of `U(ψ)` of the open `r_ψ⁻¹(U(φ))` of `U(ψ)`. This is `mapDomain_comp`.
> 2. **The morphism of the composite.** Read through the canonical isomorphism
>   `mapDomainCompIso : r_ψ⁻¹(U(φ)) ≅ U(ψ ∘ φ)` that the first conjunct supplies,
>   `r_{ψ ∘ φ}` is the restriction `r_ψ|_{r_ψ⁻¹(U(φ))} : r_ψ⁻¹(U(φ)) ⟶ U(φ)` followed by `r_φ`.
>   This is `mapDomainCompIso_hom_mapHom`.
> 3. **The comparison maps on the twists.** For every `n : ℤ`, Tag 01MY's comparison
>   `θ_{ψ ∘ φ}` on the `n`-th twist, pulled back along the canonical isomorphism, is `θ_φ` pulled
>   back along `r_ψ|_{r_ψ⁻¹(U(φ))}` followed by `θ_ψ` pulled back along the inclusion of
>   `r_ψ⁻¹(U(φ))`, the pseudofunctoriality isomorphisms of the inverse image and the three
>   identifications of composites of the first two conjuncts mediating between the two sides.
>   This is `twistMap_comp`.
>
> The source's data are the three graded rings and the two homomorphisms, and those are the only
> binders here: every domain of definition is an arbitrary open, and `θ` is Tag 01MY's comparison
> for an arbitrary homomorphism of nonnegatively graded rings.

```lean
public theorem mapDomain_mapHom_twistMap_comp (φ : 𝒜 →+*ᵍ ℬ) (ψ : ℬ →+*ᵍ 𝒞) :
    mapDomain 𝒜 𝒞 (ψ.comp φ) =
        (mapDomain ℬ 𝒞 ψ).ι ''ᵁ (mapHom ℬ 𝒞 ψ ⁻¹ᵁ mapDomain 𝒜 ℬ φ) ∧
      (mapDomainCompIso 𝒜 ℬ 𝒞 φ ψ).hom ≫ mapHom 𝒜 𝒞 (ψ.comp φ) =
        (mapHom ℬ 𝒞 ψ ∣_ mapDomain 𝒜 ℬ φ) ≫ mapHom 𝒜 ℬ φ ∧
      ∀ n : ℤ,
        (Scheme.Modules.pullbackComp (mapDomainCompIso 𝒜 ℬ 𝒞 φ ψ).hom
              (mapHom 𝒜 𝒞 (ψ.comp φ))).inv.app (twistingSheaf 𝒜 n) ≫
            (Scheme.Modules.pullback (mapDomainCompIso 𝒜 ℬ 𝒞 φ ψ).hom).map
              (twistMap 𝒜 𝒞 (ψ.comp φ) n) ≫
            (Scheme.Modules.pullbackComp (mapDomainCompIso 𝒜 ℬ 𝒞 φ ψ).hom
              (mapDomain 𝒜 𝒞 (ψ.comp φ)).ι).hom.app (twistingSheaf 𝒞 n) =
          (Scheme.Modules.pullbackCongr
              (mapDomainCompIso_hom_mapHom 𝒜 ℬ 𝒞 φ ψ)).hom.app (twistingSheaf 𝒜 n) ≫
            (Scheme.Modules.pullbackComp (mapHom ℬ 𝒞 ψ ∣_ mapDomain 𝒜 ℬ φ)
              (mapHom 𝒜 ℬ φ)).inv.app (twistingSheaf 𝒜 n) ≫
            (Scheme.Modules.pullback (mapHom ℬ 𝒞 ψ ∣_ mapDomain 𝒜 ℬ φ)).map
              (twistMap 𝒜 ℬ φ n) ≫
            (Scheme.Modules.pullbackComp (mapHom ℬ 𝒞 ψ ∣_ mapDomain 𝒜 ℬ φ)
              (mapDomain 𝒜 ℬ φ).ι).hom.app (twistingSheaf ℬ n) ≫
            (Scheme.Modules.pullbackCongr
              (morphismRestrict_ι (mapHom ℬ 𝒞 ψ) (mapDomain 𝒜 ℬ φ))).hom.app
                (twistingSheaf ℬ n) ≫
            (Scheme.Modules.pullbackComp (mapHom ℬ 𝒞 ψ ⁻¹ᵁ mapDomain 𝒜 ℬ φ).ι
              (mapHom ℬ 𝒞 ψ)).inv.app (twistingSheaf ℬ n) ≫
            (Scheme.Modules.pullback (mapHom ℬ 𝒞 ψ ⁻¹ᵁ mapDomain 𝒜 ℬ φ).ι).map
              (twistMap ℬ 𝒞 ψ n) ≫
            (Scheme.Modules.pullbackComp (mapHom ℬ 𝒞 ψ ⁻¹ᵁ mapDomain 𝒜 ℬ φ).ι
              (mapDomain ℬ 𝒞 ψ).ι).hom.app (twistingSheaf 𝒞 n) ≫
            (Scheme.Modules.pullbackCongr
              (mapDomainCompIso_hom_ι 𝒜 ℬ 𝒞 φ ψ)).inv.app (twistingSheaf 𝒞 n)
```

## Tag 01N0, a lemma

[Tag 01N0](https://stacks.math.columbia.edu/tag/01N0) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProjTwistCompare.NotIsoExample.surjective_and_not_isIso_projMapData_twistMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjTwistCompare/NotIsoExample.lean, line 492](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjTwistCompare/NotIsoExample.lean#L492). The attribute's comment: “part (3), second half: the maps θ are not isomorphisms in general, even if A → B is surjective: A = R[x,y]/(x²) with deg x = 1, deg y = 2 over a nonzero ring R, B = A/(x); ψ is surjective in every degree and as a ring map, and θ₁ is not an isomorphism”.

> **Stacks 01N0 (3), the maps `θ` are not isomorphisms in general, even for a surjective
> `ψ`.** The quotient map `ψ : R[x, y]/(x²) ⟶ R[x, y]/(x)`, with `deg x = 1` and `deg y = 2` over a
> nonzero ring `R`, is surjective in every degree (so it satisfies the hypothesis of Tag 01N0) and
> surjective as a ring map, while the comparison map `θ₁` of Tag 01MY's bundle `projMapData` is not
> an isomorphism. The surjectivity of every `θ_n` under the hypothesis of Tag 01N0 is
> `Stacks.AlgebraicGeometry.ProjTwistEpi.epi_projMapData_twistMap_of_eventually_surjective`.

```lean
theorem surjective_and_not_isIso_projMapData_twistMap :
    (∀ d, Function.Surjective (GradedRingHom.gradedAddHom (psi R) d)) ∧
      Function.Surjective (psi R) ∧
      ¬ IsIso ((projMapData (gradA R) (gradB R) (psi R)).twistMap ((1 : ℕ) : ℤ))
```

**`Stacks.AlgebraicGeometry.ProjTwistEpi.epi_projMapData_twistMap_of_eventually_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjTwistEpi/Basic.lean, line 202](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjTwistEpi/Basic.lean#L202). The attribute's comment: “part (3), first half: θ : r\_ψ^* 𝒪(n) ⟶ 𝒪(n) is surjective for every n when A\_d → B\_d is surjective for all d ≫ 0”.

> If `ψ` is surjective on homogeneous components of all sufficiently large degree, then the
> twist maps of the bundle `projMapData 𝒜 ℬ ψ` are epimorphisms of sheaves of modules.

```lean
public theorem epi_projMapData_twistMap_of_eventually_surjective (ψ : 𝒜 →+*ᵍ ℬ)
    (hψ : ∀ᶠ d : ℕ in atTop, Function.Surjective (GradedRingHom.gradedAddHom ψ d))
    (n : ℤ) : Epi ((projMapData 𝒜 ℬ ψ).twistMap n)
```

**`Stacks.AlgebraicGeometry.RelativeProjChain.mapDomain_eq_top_of_eventually_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjChain/EventualSurjective.lean, line 160](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RelativeProjChain/EventualSurjective.lean#L160). The attribute's comment: “part (1): U(ψ) = Proj B when A\_d → B\_d is surjective for all d ≫ 0”.

> **Stacks 01N0 (1) and 01N1 (1)**: a graded ring homomorphism surjective in all sufficiently
> large degrees is defined on the whole of `Proj ℬ`.
>
> A point of `Proj ℬ` omits some homogeneous `g` of positive degree `m`; a large power `g ^ k` is
> homogeneous of degree `k * m`, is still omitted because the point is prime, and is in the image
> of `ψ`.

```lean
public theorem mapDomain_eq_top_of_eventually_surjective (ψ : 𝒜 →+*ᵍ ℬ)
    (hψ : ∀ᶠ d : ℕ in atTop, Function.Surjective (GradedRingHom.gradedAddHom ψ d)) :
    mapDomain 𝒜 ℬ ψ = ⊤
```

**`Stacks.AlgebraicGeometry.RelativeProjChain.isClosedImmersion_projMapData_hom_of_eventually_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjChain/EventualSurjective.lean, line 230](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RelativeProjChain/EventualSurjective.lean#L230). The attribute's comment: “part (2): r\_ψ : Proj B ⟶ Proj A is a closed immersion when A\_d → B\_d is surjective for all d ≫ 0”.

> **Stacks 01N0 (2) and 01N1 (2)** on Tag 01MY's bundle: the underlying morphism of
> `Stacks.AlgebraicGeometry.ProjTwistCompare.projMapData` is a closed immersion. This is the form
> the statements of the chain quantify over, and it is the previous result unchanged, since the
> bundle's morphism is `mapHom` by definition.

```lean
public theorem isClosedImmersion_projMapData_hom_of_eventually_surjective (ψ : 𝒜 →+*ᵍ ℬ)
    (hψ : ∀ᶠ d : ℕ in atTop, Function.Surjective (GradedRingHom.gradedAddHom ψ d)) :
    IsClosedImmersion (ProjTwistCompare.projMapData 𝒜 ℬ ψ).hom
```

## Tag 07ZE, a lemma

[Tag 07ZE](https://stacks.math.columbia.edu/tag/07ZE) in the Stacks Project.

**`Stacks.AlgebraicGeometry.RelativeProjChain.mapDomain_eq_top_of_eventually_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjChain/EventualBijective.lean, line 166](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RelativeProjChain/EventualBijective.lean#L166). The attribute's comment: “part (1), the domain is all of Proj B”.

> **Stacks 07ZE (1)**: a graded homomorphism bijective in all large degrees is defined on all
> of `Proj ℬ`. Only surjectivity is used, so this is Stacks 01N1's first assertion.

```lean
public theorem mapDomain_eq_top_of_eventually_bijective (ψ : 𝒜 →+*ᵍ ℬ)
    (hψ : ∀ᶠ d : ℕ in atTop, Function.Bijective (GradedRingHom.gradedAddHom ψ d)) :
    mapDomain 𝒜 ℬ ψ = ⊤
```

**`Stacks.AlgebraicGeometry.RelativeProjChain.isIso_projMapData_hom_of_eventually_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjChain/EventualBijective.lean, line 197](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RelativeProjChain/EventualBijective.lean#L197). The attribute's comment: “part (2), the projective-spectrum morphism is an isomorphism”.

> **Stacks 07ZE (2)** on Tag 01MY's bundle: the underlying morphism of
> `Stacks.AlgebraicGeometry.ProjTwistCompare.projMapData` is an isomorphism. This is the form the
> statements of the chain quantify over, and it is the previous result unchanged, since the bundle's
> morphism is `mapHom` by definition.

```lean
public theorem isIso_projMapData_hom_of_eventually_bijective (ψ : 𝒜 →+*ᵍ ℬ)
    (hψ : ∀ᶠ d : ℕ in atTop, Function.Bijective (GradedRingHom.gradedAddHom ψ d)) :
    IsIso (ProjTwistCompare.projMapData 𝒜 ℬ ψ).hom
```

**`Stacks.AlgebraicGeometry.RelativeProjChain.isIso_projMapData_twistMap_of_eventually_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjChain/EventualBijective.lean, line 383](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RelativeProjChain/EventualBijective.lean#L383). The attribute's comment: “part (3), the maps on twists are isomorphisms”.

> **Stacks 07ZE (3)**: a graded homomorphism bijective in all large degrees makes Tag 01MY's
> comparison map on the `n`-th twist an isomorphism, for every `n : ℤ`.
>
> The map is an epimorphism by Stacks 01N0, and a monomorphism because its adjoint form is
> injective on sections and the unit of the adjunction is an isomorphism by assertion (2).

```lean
public theorem isIso_projMapData_twistMap_of_eventually_bijective (ψ : 𝒜 →+*ᵍ ℬ)
    (hψ : ∀ᶠ d : ℕ in atTop, Function.Bijective (GradedRingHom.gradedAddHom ψ d))
    (n : ℤ) :
    IsIso ((ProjTwistCompare.projMapData 𝒜 ℬ ψ).twistMap n)
```

## Tag 01N1, a lemma

[Tag 01N1](https://stacks.math.columbia.edu/tag/01N1) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProjTwistMono.isIso_projMapData_twistMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjTwistMono/Assembly.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjTwistMono/Assembly.lean#L125). The attribute's comment: “part (3): isomorphisms on all twists”.

> **Tag 01N1's third assertion.** For a homomorphism of graded rings surjective on homogeneous
> components of all large degree, with the source generated in degree one over its degree-zero
> part, Tag 01MY's comparison map on the `n`-th twist is an isomorphism for every `n`.

```lean
theorem isIso_projMapData_twistMap (ψ : 𝒜 →+*ᵍ ℬ)
    (hψ : ∀ᶠ d : ℕ in atTop, Function.Surjective (GradedRingHom.gradedAddHom ψ d))
    (hgen : Algebra.adjoin (𝒜 0) (𝒜 1 : Set A) = ⊤) (n : ℤ) :
    IsIso ((ProjTwistCompare.projMapData 𝒜 ℬ ψ).twistMap n)
```

**`Stacks.AlgebraicGeometry.RelativeProjChain.mapDomain_eq_top_of_eventually_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjChain/EventualSurjective.lean, line 160](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RelativeProjChain/EventualSurjective.lean#L160). The attribute's comment: “part (1): the domain is all of Proj”.

> **Stacks 01N0 (1) and 01N1 (1)**: a graded ring homomorphism surjective in all sufficiently
> large degrees is defined on the whole of `Proj ℬ`.
>
> A point of `Proj ℬ` omits some homogeneous `g` of positive degree `m`; a large power `g ^ k` is
> homogeneous of degree `k * m`, is still omitted because the point is prime, and is in the image
> of `ψ`.

```lean
public theorem mapDomain_eq_top_of_eventually_surjective (ψ : 𝒜 →+*ᵍ ℬ)
    (hψ : ∀ᶠ d : ℕ in atTop, Function.Surjective (GradedRingHom.gradedAddHom ψ d)) :
    mapDomain 𝒜 ℬ ψ = ⊤
```

**`Stacks.AlgebraicGeometry.RelativeProjChain.isClosedImmersion_projMapData_hom_of_eventually_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjChain/EventualSurjective.lean, line 230](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RelativeProjChain/EventualSurjective.lean#L230). The attribute's comment: “part (2): the closed immersion”.

> **Stacks 01N0 (2) and 01N1 (2)** on Tag 01MY's bundle: the underlying morphism of
> `Stacks.AlgebraicGeometry.ProjTwistCompare.projMapData` is a closed immersion. This is the form
> the statements of the chain quantify over, and it is the previous result unchanged, since the
> bundle's morphism is `mapHom` by definition.

```lean
public theorem isClosedImmersion_projMapData_hom_of_eventually_surjective (ψ : 𝒜 →+*ᵍ ℬ)
    (hψ : ∀ᶠ d : ℕ in atTop, Function.Surjective (GradedRingHom.gradedAddHom ψ d)) :
    IsClosedImmersion (ProjTwistCompare.projMapData 𝒜 ℬ ψ).hom
```

## Tag 01N2, a lemma

[Tag 01N2](https://stacks.math.columbia.edu/tag/01N2) in the Stacks Project.

**`Stacks.ProjBaseChange.mapDomain_isPullback_isIso_twistMap_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/ProjBaseChangeStatement.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Blowup/ProjBaseChangeStatement.lean#L98). The attribute's comment: “the tag's three assertions in one statement, for the base change of a graded `R`-algebra `A` along an `R`-algebra `S`: the domain of definition of the base-change homomorphism is the whole of `Proj (S ⊗[R] A)`, the square it forms with the structure morphisms to `Spec S` and `Spec R` is a fibre product, and the comparison map on every twist is an isomorphism”.

> **[Stacks, Tag 01N2].** Let `A` be a graded `R`-algebra with grading `𝒜`, let `S` be an
> `R`-algebra, write `X = Proj 𝒜` and `Y = Proj (S ⊗[R] 𝒜)`, and let `ψ : a ↦ 1 ⊗ₜ a` be the
> base-change homomorphism of graded rings. Then `U(ψ) = Y`, the square
>
> ```
> Y = Proj (S ⊗[R] 𝒜) ⟶ Proj 𝒜 = X
>          |                 |
>          v                 v
>       Spec S      ⟶     Spec R
> ```
>
> is a fibre product, and every comparison map `θ : r_ψ^* 𝒪_X(n) ⟶ 𝒪_Y(n)` is an isomorphism.
>
> The three conjuncts are, in order:
>
> 1. **The domain of definition is everything.** The base-changed irrelevant ideal is generated by
>   the images of the homogeneous elements of positive degree, so already the standard opens
>   `D₊(1 ⊗ₜ f)` cover `Y`. This is
>   `Stacks.AlgebraicGeometry.ProjShared.mapDomain_baseChange`.
> 2. **The square is a fibre product.** The structure morphism of each projective spectrum is
>   written as its morphism to the spectrum of the degree-zero part of its grading followed by the
>   spectrum of the structure map of that degree-zero part. This is
>   `Stacks.ProjBaseChange.isPullback_map_Spec`.
> 3. **The comparison maps are isomorphisms.** For every `n : ℤ`, the canonical comparison on the
>   `n`-th twist along `r_ψ = AlgebraicGeometry.Proj.map ψ` is an isomorphism. This is
>   `Stacks.ProjBaseChange.isIso_twistMap_includeRight`.
>
> The source's data are the graded `R`-algebra and the `R`-algebra `S`, and those are the only
> binders here; the identification of the target graded ring with the base change holds by
> construction, since the target is the base change.

```lean
theorem mapDomain_isPullback_isIso_twistMap_baseChange :
    mapDomain 𝒜 (grading 𝒜 S) (includeRight 𝒜 S) = ⊤ ∧
      IsPullback (map 𝒜 S)
          (Proj.toSpecZero (grading 𝒜 S) ≫ Spec.map (ofHom (algebraMap S ↥(grading 𝒜 S 0))))
          (Proj.toSpecZero 𝒜 ≫ Spec.map (ofHom (algebraMap R ↥(𝒜 0))))
          (Spec.map (ofHom (algebraMap R S))) ∧
      ∀ n : ℤ, IsIso (Stacks.ProjTwistComparison.twistMap (includeRight 𝒜 S)
        (irrelevant_le_map 𝒜 S) n)
```

## Tag 01N3, a lemma

[Tag 01N3](https://stacks.math.columbia.edu/tag/01N3) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProjShared.mapDomain_eq_top_of_isLocalizationAway`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjShared/MapDomain.lean, line 181](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjShared/MapDomain.lean#L181). The attribute's comment: “the open domain”.

> **A graded homomorphism that presents its target as a localization of its source at a
> degree-zero element is everywhere defined.**
>
> A homogeneous element `b` of `B` of positive degree becomes, after multiplication by a power of
> the image of `g`, the image of some `a ∈ A`; that image is homogeneous of the same degree, so `b`
> lies in the ideal generated by the images of the positive-degree homogeneous elements of `A`.
> Hence the irrelevant ideal of `ℬ` is contained in that ideal and the standard opens `D₊(ψ f)`
> cover `Proj ℬ`.
>
> The algebra structure is an arbitrary one whose structure map is `ψ`, which covers the structure
> map `ψ.toRingHom.toAlgebra` in particular.
>
> This is the first assertion of Tag 01N3, `U(ψ) = Y`.

```lean
public theorem mapDomain_eq_top_of_isLocalizationAway (ψ : 𝒜 →+*ᵍ ℬ) (g : 𝒜 0)
    [Algebra A B] (halg : algebraMap A B = (ψ : A →+* B))
    [IsLocalization.Away (g : A) B] :
    mapDomain 𝒜 ℬ ψ = ⊤
```

**`Stacks.AlgebraicGeometry.TwistBaseChange.isOpenImmersion_mapHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TwistBaseChange/Fibre.lean, line 204](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/TwistBaseChange/Fibre.lean#L204). The attribute's comment: “the open immersion”.

> **The induced morphism of a graded localization away from a degree-zero element is an open
> immersion.**

```lean
public theorem isOpenImmersion_mapHom (ψ : 𝒜 →+*ᵍ ℬ) {g : A} (hg : g ∈ 𝒜 0) [Algebra A B]
    (halg : (algebraMap A B : A →+* B) = ψ.toRingHom) [IsLocalization.Away g B] :
    IsOpenImmersion (mapHom 𝒜 ℬ ψ)
```

**`Stacks.AlgebraicGeometry.TwistBaseChange.opensRange_mapHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TwistBaseChange/Fibre.lean, line 269](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/TwistBaseChange/Fibre.lean#L269). The attribute's comment: “the inverse image of D(g)”.

> For a graded ring homomorphism exhibiting `B` as a localization of `A` away from an element
> `g` of degree `0`, the open immersion `Proj ℬ ⟶ Proj 𝒜` identifies `Proj ℬ` with the inverse
> image of the standard open `D(g) ⊆ Spec (𝒜 0)` under the structure morphism
> `AlgebraicGeometry.Proj.toSpecZero`.

```lean
public theorem opensRange_mapHom (ψ : 𝒜 →+*ᵍ ℬ) {g : A} (hg : g ∈ 𝒜 0) [Algebra A B]
    (halg : (algebraMap A B : A →+* B) = ψ.toRingHom) [IsLocalization.Away g B]
    [IsOpenImmersion (mapHom 𝒜 ℬ ψ)] :
    (mapHom 𝒜 ℬ ψ).opensRange =
      Proj.toSpecZero 𝒜 ⁻¹ᵁ PrimeSpectrum.basicOpen (⟨g, hg⟩ : 𝒜 0)
```

**`Stacks.AlgebraicGeometry.TwistBaseChange.isIso_projMapData_twistMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TwistBaseChange/Iso.lean, line 290](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/TwistBaseChange/Iso.lean#L290). The attribute's comment: “the maps on twists”.

> If `ψ` presents `B` as the localization `A_g` of `A` at a degree-zero element `g`, then the
> comparison map `θ : r_ψ^* 𝒪_X(n) → 𝒪_Y(n)` of
> `Stacks.AlgebraicGeometry.ProjTwistCompare.projMapData` is an isomorphism for every `n : ℤ`.

```lean
public theorem isIso_projMapData_twistMap (ψ : 𝒜 →+*ᵍ ℬ) {g : A} (hg : g ∈ 𝒜 0) [Algebra A B]
    (halg : (algebraMap A B : A →+* B) = ψ.toRingHom) [IsLocalization.Away g B] (n : ℤ) :
    IsIso ((projMapData 𝒜 ℬ ψ).twistMap n)
```

## Tag 0B5J, a lemma

[Tag 0B5J](https://stacks.math.columbia.edu/tag/0B5J) in the Stacks Project.

**`Stacks.Veronese.tag0B5J`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjVeroneseStatement.lean, line 157](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjVeroneseStatement.lean#L157). The attribute's comment: “the canonical isomorphism i : Proj S to Proj S^(d) induced by the inclusion S^(d) in S, described on homogeneous primes and on the standard opens D+(f) = Spec S\_(f); assertion (1), the canonical isomorphism from the sheaf of a graded S-module M, in any universe, to the pullback of the sheaf of M^(d), described on the standard opens; assertion (2), the isomorphisms O\_X(nd) to i^* O\_X'(n) obtained from (1) at M = S(nd); and the compatibility of these isomorphisms with the multiplication maps of associated sheaves (through the comparison map from M^(d) tensor N^(d) to (M tensor N)^(d)), with the multiplication of twists, with the maps O(n) tensor F(m) to F(n+m) and M~ tensor O(n) to M(n)~, with the maps from S and from M to twisted global sections, and with the products of twisted global sections”. References: EGA II (8.14.13), “partial”.

> **[Stacks, Tag 0B5J].** Let `S` be a graded ring and `d ≥ 1`. Set `S' = S⁽ᵈ⁾`,
> `X = Proj S` and `X' = Proj S'`. There is a canonical isomorphism `i : X ⟶ X'` of schemes such
> that (1) for any graded `S`-module `M`, setting `M' = M⁽ᵈ⁾`, there is a canonical isomorphism
> `M̃ ≅ i^*(M'~)`, and (2) there are canonical isomorphisms `𝒪_X(nd) ≅ i^*𝒪_{X'}(n)`; and these
> isomorphisms are compatible with the multiplication maps of Tag 01MK and hence with the maps of
> Tags 01MO, 03GJ, 01MP, 03GK, 01MQ and 01MR.
>
> The isomorphism `i` is `Stacks.Veronese.veroneseProjIso 𝒮 d hd`, glued from the chart
> isomorphisms; the first conjunct says its underlying morphism `veroneseProjHom` is an
> isomorphism of schemes, that on homogeneous primes it is contraction along `S' ⊆ S`, and that on
> each standard open `D₊(f) = Spec S₍f₎` it is `Spec` of the identification `S'₍f ᵈ₎ ≅ S₍f₎`
> followed by the inclusion of `D₊(f ᵈ)` — the source's "`S₍f₎ ≅ S'₍f ᵈ₎`, compatible with the
> restriction maps". These charts cover `Proj S`, so they determine `i` as a morphism of schemes,
> not only on points. The next conjunct is the consequence `i⁻¹ D₊(f ᵈ) = D₊(f)`, which the
> chart descriptions of assertion (1) are written over. The third conjunct is assertion (1) for a
> module in any universe `v`: the
> isomorphism `Stacks.Veronese.veroneseAssociatedSheafIso 𝒮 𝒨 d hd : M̃ ≅ i^*(M'~)`, with the
> chart description that makes it canonical — on `D₊(f)` its inverse is the degree-zero Veronese
> localization comparison `M'₍f ᵈ₎ ≅ M₍f₎`. The fourth conjunct is assertion (2), each isomorphism
> exhibited as the source derives it: (1) at `M = S(nd)` followed by `(S(nd))⁽ᵈ⁾ ≅ S'(n)`. The
> remaining conjuncts are the trailing clause: the commuting square with the multiplication maps
> of Tag 01MK, and the six squares with the maps of Tags 01MO, 03GJ, 01MP, 03GK, 01MQ and 01MR
> which the source derives from it and whose precise statements it omits. See the module
> documentation for each square, for why the source's proof of the first is corrected here
> (the comparison along its lower edge is not injective at `S = k[x, y]`, `d = 2`,
> `M = N = S(1)`: `Stacks.Veronese.not_injective_veroneseTensorMap`), and for the universes.

```lean
theorem tag0B5J (d : ℕ) (hd : 1 ≤ d) :
    letI := veroneseGradingGradedRing 𝒮 d hd
    -- `i` is an isomorphism of schemes, and on homogeneous primes it is contraction along
    -- `S⁽ᵈ⁾ ⊆ S`
    IsIso (veroneseProjHom 𝒮 d hd) ∧
      (∀ (x : ProjectiveSpectrum 𝒮) (g : veroneseSubring 𝒮 d),
        g ∈ ((veroneseProjIso 𝒮 d hd).hom.base x).asHomogeneousIdeal ↔
          (g : S) ∈ x.asHomogeneousIdeal) ∧
      -- on each chart `D₊(f) = Spec S₍f₎`, `i` is `Spec` of `S'₍f ᵈ₎ ≅ S₍f₎` followed by the
      -- inclusion of `D₊(f ᵈ)`: these determine `i` as a morphism of schemes
      (∀ (f : S) (e : ℕ) (he : 0 < e) (hf : f ∈ 𝒮 e),
        Proj.awayι 𝒮 f hf he ≫ (veroneseProjIso 𝒮 d hd).hom =
          Spec.map (veroneseAwayEquiv 𝒮 d f hf hd).toCommRingCatIso.hom ≫
            Proj.awayι (veroneseGrading 𝒮 d) (veronesePower 𝒮 d f hf)
              (veronesePower_mem 𝒮 d f hf) he) ∧
      -- the chart identification `i⁻¹ D₊(f ᵈ) = D₊(f)`
      (∀ (f : S) (e : ℕ), 0 < e → ∀ hf : f ∈ 𝒮 e,
        (veroneseProjIso 𝒮 d hd).hom ⁻¹ᵁ
            Proj.basicOpen (veroneseGrading 𝒮 d) (veronesePower 𝒮 d f hf) =
          Proj.basicOpen 𝒮 f) ∧
      -- assertion (1): `veroneseAssociatedSheafIso 𝒮 𝒨 d hd : M̃ ≅ i^*(M'~)`, for a module in
      -- any universe, with the chart description that makes it the canonical isomorphism
      (∀ (M : Type v) [AddCommGroup M] [Module S M] (𝒨 : ℤ → AddSubgroup M)
          [Decomposition 𝒨] [SetLike.GradedSMul 𝒮 𝒨],
        letI := veroneseModuleGradingDecomposition 𝒮 𝒨 d hd
        ∀ (f : S) (e : ℕ) (he : 0 < e) (hf : f ∈ 𝒮 e)
          (hvf : veronesePower 𝒮 d f hf ∈ veroneseGrading 𝒮 d e)
          (z : GradedModuleDegreeZeroLocalization (veroneseGrading 𝒮 d)
            (veroneseModuleGrading 𝒮 𝒨 d) (veronesePower 𝒮 d f hf)),
          ProjectiveSpectrum.Proj.associatedModuleSheafStandardOpenEquiv 𝒮 𝒨 hf he
              ((veroneseAssociatedSheafIso 𝒮 𝒨 d hd).inv.val.app (op (Proj.basicOpen 𝒮 f))
                (veroneseProjIso_basicOpen 𝒮 d hd f he hf ▸
                  ((SheafOfModules.pullbackPushforwardAdjunction.{max u v}
                        (veroneseProjIso 𝒮 d hd).hom.toRingCatSheafHom).unit.app
                      (ProjectiveSpectrum.Proj.associatedModuleSheaf (veroneseGrading 𝒮 d)
                        (veroneseModuleGrading 𝒮 𝒨 d))).val.app
                    (op (Proj.basicOpen (veroneseGrading 𝒮 d) (veronesePower 𝒮 d f hf)))
                    ((ProjectiveSpectrum.Proj.associatedModuleSheafStandardOpenEquiv
                        (veroneseGrading 𝒮 d) (veroneseModuleGrading 𝒮 𝒨 d)
                        hvf he).symm z))) =
            veroneseModuleAwayEquiv 𝒮 d 𝒨 f hf hd z) ∧
      -- assertion (2), as the source derives it from (1) at `M = S(nd)`
      (∀ n : ℤ, ∃ E : ProjectiveSpectrum.Proj.twistingSheaf 𝒮 (n * d) ≅
          (Scheme.Modules.pullback (veroneseProjIso 𝒮 d hd).hom).obj
            (ProjectiveSpectrum.Proj.twistingSheaf (veroneseGrading 𝒮 d) n),
        E.hom =
          (associatedModuleSheafVeroneseIso 𝒮 (twistGradingAddSubgroup 𝒮 (n * d)) d hd).hom ≫
            (Scheme.Modules.pullback (veroneseProjIso 𝒮 d hd).hom).map
              (veroneseShiftSheafIso 𝒮 d hd n).hom) ∧
      -- the trailing clause: compatibility of (1) with the multiplication maps
      (∀ (M N : Type u) [AddCommGroup M] [Module S M] [AddCommGroup N] [Module S N]
          (𝒨 : ℤ → AddSubgroup M) [Decomposition 𝒨] [SetLike.GradedSMul 𝒮 𝒨]
          (𝒩 : ℤ → AddSubgroup N) [Decomposition 𝒩] [SetLike.GradedSMul 𝒮 𝒩],
        veroneseTensorSquareLeft 𝒮 𝒨 𝒩 d hd = veroneseTensorSquareRight 𝒮 𝒨 𝒩 d hd) ∧
      -- "and hence with (01MO)": `𝒪(nd) ⊗ 𝒪(md) ⟶ 𝒪((n+m)d)` against `𝒪'(n) ⊗ 𝒪'(m) ⟶ 𝒪'(n+m)`
      (∀ n m : ℤ, veroneseTwistMulLeft 𝒮 d hd n m = veroneseTwistMulRight 𝒮 d hd n m) ∧
      -- "and hence with (03GJ)": `𝒪(nd) ⊗ ℱ(md) ⟶ ℱ((n+m)d)` against
      -- `𝒪'(n) ⊗ ℱ'(m) ⟶ ℱ'(n+m)`, for `ℱ = i^*ℱ'`
      (∀ (F' : SheafOfModules.{u}
            ((sheafCompose (Opens.grothendieckTopology
              (ProjectiveSpectrum.top (veroneseGrading 𝒮 d)))
              (forget₂ CommRingCat.{u} RingCat.{u})).obj
              (ProjectiveSpectrum.Proj.structureSheaf (veroneseGrading 𝒮 d)))) (n m : ℤ),
        veroneseTwistSheafMulLeft 𝒮 d hd F' n m = veroneseTwistSheafMulRight 𝒮 d hd F' n m) ∧
      -- "and hence with (03GK)": products of global sections of `𝒪(nd)` and `ℱ(md)`
      (∀ (F' : SheafOfModules.{u}
            ((sheafCompose (Opens.grothendieckTopology
              (ProjectiveSpectrum.top (veroneseGrading 𝒮 d)))
              (forget₂ CommRingCat.{u} RingCat.{u})).obj
              (ProjectiveSpectrum.Proj.structureSheaf (veroneseGrading 𝒮 d)))) (n m : ℤ)
          (s : (ProjectiveSpectrum.Proj.twistingSheaf 𝒮 (n * d)).val.obj (op ⊤))
          (t : (ProjectiveSpectrum.Proj.twistSheafOfModules 𝒮 (pullbackProjModule 𝒮
            (veroneseGrading 𝒮 d) (veroneseProjIso 𝒮 d hd).hom F') (m * d)).val.obj (op ⊤))
          (s' : (ProjectiveSpectrum.Proj.twistingSheaf (veroneseGrading 𝒮 d) n).val.obj (op ⊤))
          (t' : (ProjectiveSpectrum.Proj.twistSheafOfModules (veroneseGrading 𝒮 d) F' m).val.obj
            (op ⊤)),
        ((veroneseTwistingSheafIso 𝒮 d hd n).hom.val.app (op ⊤)).hom s =
            Stacks.Tag01VSPullbackTensor.modulesPullbackUnit (veroneseProjIso 𝒮 d hd).hom
              (ProjectiveSpectrum.Proj.twistingSheaf (veroneseGrading 𝒮 d) n) ⊤ s' →
        ((veroneseTwistedModuleIso 𝒮 d hd F' m).hom.val.app (op ⊤)).hom t =
            Stacks.Tag01VSPullbackTensor.modulesPullbackUnit (veroneseProjIso 𝒮 d hd).hom
              (ProjectiveSpectrum.Proj.twistSheafOfModules (veroneseGrading 𝒮 d) F' m) ⊤ t' →
        ((veroneseTwistedModuleIso 𝒮 d hd F' (n + m)).hom.val.app (op ⊤)).hom
            (((eqToHom (congrArg (ProjectiveSpectrum.Proj.twistSheafOfModules 𝒮
                (pullbackProjModule 𝒮 (veroneseGrading 𝒮 d) (veroneseProjIso 𝒮 d hd).hom F'))
                (add_mul n m (d : ℤ)).symm)).val.app (op ⊤)).hom
              (ProjectiveSpectrum.Proj.multiplyHomogeneousSections' 𝒮
                (pullbackProjModule 𝒮 (veroneseGrading 𝒮 d) (veroneseProjIso 𝒮 d hd).hom F')
                (n * d) (m * d) s t)) =
          Stacks.Tag01VSPullbackTensor.modulesPullbackUnit (veroneseProjIso 𝒮 d hd).hom
            (ProjectiveSpectrum.Proj.twistSheafOfModules (veroneseGrading 𝒮 d) F' (n + m)) ⊤
            (ProjectiveSpectrum.Proj.multiplyHomogeneousSections' (veroneseGrading 𝒮 d) F' n m
              s' t')) ∧
      -- "and hence with (01MP)": `S → ⨁ₙ Γ(X, 𝒪_X(n))` against `S' → ⨁ₙ Γ(X', 𝒪_{X'}(n))`
      (letI := (ProjectiveSpectrum.Proj.globalSectionsRingMap 𝒮).gradedRing
       letI := (ProjectiveSpectrum.Proj.globalSectionsRingMap (veroneseGrading 𝒮 d)).gradedRing
       ∀ (n : ℕ) (a : veroneseSubring 𝒮 d),
        (veroneseTwistingSheafIso 𝒮 d hd n).hom.val.app (op ⊤)
            ((eqToHom (congrArg (ProjectiveSpectrum.Proj.twistingSheaf 𝒮)
              (Nat.cast_mul n d))).val.app (op ⊤)
              (DirectSum.component ℤ ℕ (ProjectiveSpectrum.Proj.twistGlobalSections 𝒮) (n * d)
                ((ProjectiveSpectrum.Proj.globalSectionsRingMap 𝒮).hom (a : S)))) =
          Stacks.Tag01VSPullbackTensor.modulesPullbackUnit (veroneseProjIso 𝒮 d hd).hom
            (ProjectiveSpectrum.Proj.twistingSheaf (veroneseGrading 𝒮 d) n) ⊤
            (DirectSum.component ℤ ℕ
              (ProjectiveSpectrum.Proj.twistGlobalSections (veroneseGrading 𝒮 d)) n
              ((ProjectiveSpectrum.Proj.globalSectionsRingMap (veroneseGrading 𝒮 d)).hom a))) ∧
      -- "and hence with (01MQ)": `M̃ ⊗ 𝒪_X(nd) ⟶ M(nd)~` against `M'~ ⊗ 𝒪_{X'}(n) ⟶ M'(n)~`
      (∀ (M : Type u) [AddCommGroup M] [Module S M] (𝒨 : ℤ → AddSubgroup M)
          [Decomposition 𝒨] [SetLike.GradedSMul 𝒮 𝒨] (n : ℤ),
        veroneseModuleTwistLeft 𝒮 𝒨 d hd n = veroneseModuleTwistRight 𝒮 𝒨 d hd n) ∧
      -- "and hence with (01MR)": `M → ⨁ₙ Γ(X, M(n)~)` against `M' → ⨁ₙ Γ(X', M'(n)~)`
      (∀ (M : Type v) [AddCommGroup M] [Module S M] (𝒨 : ℤ → AddSubgroup M)
          [Decomposition 𝒨] [SetLike.GradedSMul 𝒮 𝒨],
        letI := veroneseModuleGradingDecomposition 𝒮 𝒨 d hd
        ∀ (n : ℤ) (m : veroneseSubmodule 𝒮 𝒨 d),
        (veroneseShiftedSheafIsoAny 𝒮 𝒨 d hd n).hom.val.app (op ⊤)
            (DirectSum.component ℤ ℤ _ (n * d)
              ((Stacks.AlgebraicGeometry.ProjShiftedSections.globalSectionsModuleMap 𝒮 𝒨).hom
                (m : M))) =
          pullbackUnitAny (veroneseProjIso 𝒮 d hd).hom
            (ProjectiveSpectrum.Proj.associatedModuleSheaf (veroneseGrading 𝒮 d)
              (shiftedGrading (veroneseModuleGrading 𝒮 𝒨 d) n)) ⊤
            (DirectSum.component ℤ ℤ _ n
              ((Stacks.AlgebraicGeometry.ProjShiftedSections.globalSectionsModuleMap
                (veroneseGrading 𝒮 d) (veroneseModuleGrading 𝒮 𝒨 d)).hom m)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 27.11, Tag 01MX](https://stacks.math.columbia.edu/tag/01MX)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
