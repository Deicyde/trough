---
declaration: section
origin: cited
lean: Stacks.Chow.ConormalCompatibleVirtualNormalBundles.ofIsRegularImmersion, Stacks.Chow.localizedChernClass_cap_eq_bivariantCompositeCap_of_isRegularImmersion, Stacks.Chow.localizedChernClass_eq_bivariantComposite_of_isRegularImmersion, Stacks.Chow.completedVirtualNormalGysinClassOfImmersion_comp_ofIsRegularImmersion, Stacks.AlgebraicGeometry.isRegularImmersion_comp, Stacks.Chow.completedBivariantCompositeOfInvertible_completedFlatPullbackOfSmooth_of_section, Stacks.AlgebraicGeometry.isRegularImmersion_of_smooth_section, Stacks.Chow.SmoothFactorization.isKoszulRegularImmersion
statement: formalized
proof: formalized
---

# 42.59 Gysin maps for local complete intersection morphisms

Section 42.59 of the Stacks Project, [Tag 0FEZ](https://stacks.math.columbia.edu/tag/0FEZ). 13 tags here are carried by 35 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FF0, a lemma

[Tag 0FF0](https://stacks.math.columbia.edu/tag/0FF0) in the Stacks Project.

**`Stacks.Chow.ConormalCompatibleVirtualNormalBundles.ofIsRegularImmersion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/RegularImmersionGysinComposition.lean, line 300](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/RegularImmersionGysinComposition.lean#L300). The attribute's comment: “second assertion: the three normal bundles of a pair of regular immersions satisfy the hypothesis of Stacks 0FEC, by the short exact conormal sequence of Stacks 063N”.

> **Stacks 0FF0, the geometric input of the second assertion.** The three normal bundles of a
> pair of regular immersions `Z ⟶ Y ⟶ X` of locally Noetherian schemes form a conormal-compatible
> triple in the sense of Stacks 0FEC: the sequence of their duals is the conormal sequence of
> Stacks 062S conjugated by the three reflexivity isomorphisms, it is short exact by Stacks 063N,
> and its two squares against the conormal sequence commute because the three structural
> surjections are the inverses of those isomorphisms.

```lean
def ConormalCompatibleVirtualNormalBundles.ofIsRegularImmersion :
    ConormalCompatibleVirtualNormalBundles i j
```

**`Stacks.Chow.localizedChernClass_cap_eq_bivariantCompositeCap_of_isRegularImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/RegularImmersionGysinComposition.lean, line 357](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/RegularImmersionGysinComposition.lean#L357). The attribute's comment: “second assertion, (j ∘ i)^! = i^! ∘ j^! read on cap products, at the canonical normal bundles of the two regular immersions; the localized Chern class of Stacks 0FBK is a parameter and the composition formula of Stacks 0FEC is an input, exactly as in Stacks 0FEC”.

> **Stacks 0FF0, second assertion, read on cap products.** For regular immersions
> `i : Z ⟶ Y` and `j : Y ⟶ X` of schemes locally of finite type over the base, equipped with their
> canonical normal bundles, the Gysin map of `j ∘ i` on a test scheme `t : T ⟶ X` is: cap with
> `j^!`, then cap with `i^!`, then push forward along the associativity isomorphism
> `(T ×_X Y) ×_Y Z ≅ T ×_X Z` of pullbacks.
>
> This is Stacks 0FEC at the conormal-compatible triple of the two regular immersions, so the
> composition formula for the three parameterized classes of Stacks 0FBK is an input, as it is in
> the two theorems of Stacks 0FEC themselves.

```lean
theorem localizedChernClass_cap_eq_bivariantCompositeCap_of_isRegularImmersion
    (hc : IsBivariantClassComposition C G sZ sY sX i j hsi hsj hpp p q
      (cloc sZ sY i hsi
        (ConormalCompatibleVirtualNormalBundles.ofIsRegularImmersion i j hi hj).bundleZY p)
      (cloc sY sX j hsj
        (ConormalCompatibleVirtualNormalBundles.ofIsRegularImmersion i j hi hj).bundleYX q)
      (cloc sZ sX (i ≫ j) (comp_comp_structureMorphism_eq hsi hsj)
        (ConormalCompatibleVirtualNormalBundles.ofIsRegularImmersion i j hi hj).bundleZX (p + q)))
    {T : Scheme.{u}} (t : T ⟶ X) [LocallyOfFiniteType t] (k : ℤ)
    (α : chowGroup C (t ≫ sX) k) :
    chowGroupDegreeEquiv C (pullback.fst (i ≫ j) t ≫ sZ)
        (by ring : k - (p + q) = (k - q) - p)
        ((cloc sZ sX (i ≫ j) (comp_comp_structureMorphism_eq hsi hsj)
          (ConormalCompatibleVirtualNormalBundles.ofIsRegularImmersion i j hi hj).bundleZX
          (p + q)).cap t k α) =
      bivariantCompositeCap C G sZ sY sX i j hsi hsj hpp p q
        (cloc sZ sY i hsi
          (ConormalCompatibleVirtualNormalBundles.ofIsRegularImmersion i j hi hj).bundleZY p)
        (cloc sY sX j hsj
          (ConormalCompatibleVirtualNormalBundles.ofIsRegularImmersion i j hi hj).bundleYX q)
        t k α
```

**`Stacks.Chow.localizedChernClass_eq_bivariantComposite_of_isRegularImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/RegularImmersionGysinComposition.lean, line 394](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/RegularImmersionGysinComposition.lean#L394). The attribute's comment: “second assertion, (j ∘ i)^! = i^! ∘ j^! as an equality of bivariant classes, at the canonical normal bundles of the two regular immersions; the localized Chern class of Stacks 0FBK is a parameter and the composition formula of Stacks 0FEC is an input, exactly as in Stacks 0FEC”.

> **Stacks 0FF0, second assertion, as an equality of bivariant classes.** For regular
> immersions `i : Z ⟶ Y` and `j : Y ⟶ X` of schemes locally of finite type over the base, equipped
> with their canonical normal bundles, the Gysin class of `j ∘ i` is the composite of Stacks 0B75
> of the Gysin class of `i` with the Gysin class of `j`:
>
>   `(j ∘ i)^! = i^! ∘ j^!`   in `A^{p+q}(Z ⟶ X)`.
>
> Both classes satisfy the composition formula of Stacks 0FEC — the composite by Stacks 0FE0 — and
> that formula determines the class, so they agree.

```lean
theorem localizedChernClass_eq_bivariantComposite_of_isRegularImmersion
    (hgys : G.IsNaturalUnderBaseChangeIso)
    (hgysc : G.IsNaturalUnderPullbackCompPushforward)
    (hc : IsBivariantClassComposition C G sZ sY sX i j hsi hsj hpp p q
      (cloc sZ sY i hsi
        (ConormalCompatibleVirtualNormalBundles.ofIsRegularImmersion i j hi hj).bundleZY p)
      (cloc sY sX j hsj
        (ConormalCompatibleVirtualNormalBundles.ofIsRegularImmersion i j hi hj).bundleYX q)
      (cloc sZ sX (i ≫ j) (comp_comp_structureMorphism_eq hsi hsj)
        (ConormalCompatibleVirtualNormalBundles.ofIsRegularImmersion i j hi hj).bundleZX
        (p + q))) :
    cloc sZ sX (i ≫ j) (comp_comp_structureMorphism_eq hsi hsj)
        (ConormalCompatibleVirtualNormalBundles.ofIsRegularImmersion i j hi hj).bundleZX
        (p + q) =
      bivariantComposite C G sZ sY sX i j hsi hsj p q
        (cloc sZ sY i hsi
          (ConormalCompatibleVirtualNormalBundles.ofIsRegularImmersion i j hi hj).bundleZY p)
        (cloc sY sX j hsj
          (ConormalCompatibleVirtualNormalBundles.ofIsRegularImmersion i j hi hj).bundleYX q)
        hgys hgysc
```

**`Stacks.Chow.completedVirtualNormalGysinClassOfImmersion_comp_ofIsRegularImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/LciGysinMapComposition.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/LciGysinMapComposition.lean#L73). References: SGA 6 VIII (1.5), “special case”.

> **Stacks 0FF0.** Let `s : X ⟶ W` and `j : W ⟶ P` be regular immersions of schemes locally of
> finite type over the base. Then `s ≫ j` is a regular immersion and
>
>   `(j ∘ s)^! = s^! ∘ j^!`   in `A^*(X ⟶ P)^∧`,
>
> where `(−)^!` is the class `c(− , 𝒩)` of Stacks 0FBQ (3) of the normal bundle `𝒩 = 𝒞^∨` of the
> regular immersion.

```lean
theorem completedVirtualNormalGysinClassOfImmersion_comp_ofIsRegularImmersion
    (C : ChowSituation.{u}) {X W P : Scheme.{u}} (sX : X ⟶ C.S) [LocallyOfFiniteType sX]
    (sW : W ⟶ C.S) [LocallyOfFiniteType sW] (sP : P ⟶ C.S) [LocallyOfFiniteType sP]
    (s : X ⟶ W) (j : W ⟶ P) [IsImmersion s] [IsImmersion j] (hs : s ≫ sW = sX)
    (hj : j ≫ sP = sW) (hsr : IsRegularImmersion s) (hjr : IsRegularImmersion j) :
    letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian sX
    letI : IsLocallyNoetherian W := LocallyOfFiniteType.isLocallyNoetherian sW
    letI : IsLocallyNoetherian P := LocallyOfFiniteType.isLocallyNoetherian sP
    ∃ hr : IsRegularImmersion (s ≫ j),
      completedVirtualNormalGysinClassOfImmersion C sX sP (s ≫ j)
          (comp_comp_structureMorphism_eq hs hj)
          (VirtualNormalBundle.ofIsRegularImmersion (s ≫ j) hr) =
        completedBivariantCompositeOfInvertible C sX sW sP s j hs hj
          (completedVirtualNormalGysinClassOfImmersion C sX sW s hs
            (VirtualNormalBundle.ofIsRegularImmersion s hsr))
          (completedVirtualNormalGysinClassOfImmersion C sW sP j hj
            (VirtualNormalBundle.ofIsRegularImmersion j hjr))
```

Declarations registered for the tag:

- [`Stacks.AlgebraicGeometry.isRegularImmersion_comp`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/Composition.lean#L155), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/RegularImmersionGysinComposition.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/RegularImmersionGysinComposition.lean#L142) (StacksFrontier): “first assertion: the composite of two regular immersions of schemes locally of finite type over the base is a regular immersion; local finite type over the base is not used, and the assertion is Stacks 067Q”.

## Tag 0FF1, a lemma

[Tag 0FF1](https://stacks.math.columbia.edu/tag/0FF1) in the Stacks Project.

**`Stacks.Chow.completedBivariantCompositeOfInvertible_completedFlatPullbackOfSmooth_of_section`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/SectionOfSmooth.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/SectionOfSmooth.lean#L118). The attribute's comment: “second assertion: 1 = s^! ∘ p^* in A^*(X)^∧, the composite read as a completed class for 𝟙 X along s ≫ p = 𝟙 X”.

> Let `p : P ⟶ X` be a smooth morphism of schemes locally of finite type over the base and
> `s : X ⟶ P` a section of `p`, a regular immersion by
> `Stacks.AlgebraicGeometry.isRegularImmersion_of_smooth_section`. Then
>
>   `1 = s^! ∘ p^*` in `A^*(X)^∧`,
>
> for `s^! = c(X ⟶ P, 𝒩_{X/P})` the class of Stacks 0FBQ (3) of the normal sheaf of `s` and `p^*`
> the flat pullback of Stacks 0B78; the composite, a class for `s ≫ p`, is read as a class for
> `𝟙 X = s ≫ p`.

```lean
theorem completedBivariantCompositeOfInvertible_completedFlatPullbackOfSmooth_of_section :
    letI : IsImmersion s := Stacks.AlgebraicGeometry.isImmersion_of_comp_eq_id s p hs
    letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian sX
    letI : IsLocallyNoetherian P := LocallyOfFiniteType.isLocallyNoetherian sP
    completedBivariantGroup.copy C hs
        (comp_comp_structureMorphism_eq (comp_structureMorphism_of_comp_eq_id hp hs) hp)
        (Category.id_comp sX)
        (completedBivariantCompositeOfInvertible C sX sP sX s p
          (comp_structureMorphism_of_comp_eq_id hp hs) hp
          (completedVirtualNormalGysinClassOfImmersion C sX sP s
            (comp_structureMorphism_of_comp_eq_id hp hs)
            (VirtualNormalBundle.ofIsRegularImmersion s
              (Stacks.AlgebraicGeometry.isRegularImmersion_of_smooth_section p s hs)))
          (completedFlatPullbackOfSmooth C sP sX p hp)) =
      completedIdentityClass C sX
```

Declarations registered for the tag:

- [`Stacks.AlgebraicGeometry.isRegularImmersion_of_smooth_section`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Relative/SmoothSection.lean#L65), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/SectionOfSmooth.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/SectionOfSmooth.lean#L164) (StacksFrontier): “first assertion: a section s of a smooth morphism p is a regular immersion; it is Stacks 067R”.

## Tag 0FF2, a lemma

[Tag 0FF2](https://stacks.math.columbia.edu/tag/0FF2) in the Stacks Project.

**`Stacks.Chow.SmoothFactorization.isKoszulRegularImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/FactorizationIndependence.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/FactorizationIndependence.lean#L213). The attribute's comment: “regularity of the immersion of a factorization of an lci morphism, which the statement of Stacks 0FF2 leaves implicit; Stacks 069G enters through its repository form, so the Koszul case of Stacks 0693 is carried as `hcompSmooth`”. References: SGA 6 VIII (1.2).

> **Stacks 069G, for a factorization of a local complete intersection morphism.** The immersion
> `i : X ⟶ P` of a factorization `f = g ∘ i` of a local complete intersection morphism `f` is a
> Koszul-regular immersion. This is what makes the Gysin class `i^!` of section 42.54 of the Stacks
> Project available, and it is the reason Stacks 0FF2 need not assume regularity of the immersion.
>
> Stacks 069G is stated for an immersion of an open of the source; it is applied here to the top
> open and transported back along `AlgebraicGeometry.Scheme.topIso`. The Koszul case of Stacks 0693
> is a hypothesis of Stacks 069G in this repository, hence of this statement.

```lean
theorem SmoothFactorization.isKoszulRegularImmersion
    (hcompSmooth : AlgebraicGeometry.KoszulRegularCompSmooth.{u}) (F : SmoothFactorization f)
    (hf : IsLocalCompleteIntersectionMorphism f) : IsKoszulRegularImmersion F.imm
```

**`Stacks.Chow.SmoothFactorization.exists_refines_both`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/FactorizationIndependence.lean, line 292](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/FactorizationIndependence.lean#L292). The attribute's comment: “the first step of the proof: any two immersion--smooth factorizations of `f` are refined by a common one, through `P ×_Y P'`, which reduces the independence of `f^!` to the case of a single refinement `p : P' ⟶ P`”.

> **Stacks 0FF2, first step.** Any two factorizations of `f` as an immersion followed by a
> smooth morphism are refined by a common one, namely the factorization through the fibre product
> of their intermediate schemes over `Y`. The independence of `f^!` therefore reduces to the case
> of a refining pair.

```lean
theorem SmoothFactorization.exists_refines_both :
    ∃ F'' : SmoothFactorization f, F''.Refines F ∧ F''.Refines F'
```

**`Stacks.Chow.SmoothFactorization.isKoszulRegularImmersion_refinementProj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/FactorizationIndependence.lean, line 389](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/FactorizationIndependence.lean#L389). The attribute's comment: “the second step of the proof: the base change `j` of the immersion along the refinement is a Koszul-regular immersion, the Koszul-regular part of Stacks 067P; the regularity of `i` is the prerequisite `hreg`, supplied for an lci morphism by Stacks 069G”.

> **Stacks 0FF2, second step: regularity of `j`.** The base change `j : X ×_P P' ⟶ P'` of the
> immersion `i` of `F` along the refinement `p` is a Koszul-regular immersion, by the Koszul-regular
> part of Stacks 067P: `p` is smooth, hence flat. For a local complete intersection morphism `f` the
> hypothesis on `i` is automatic, by
> `Stacks.Chow.SmoothFactorization.isKoszulRegularImmersion`.

```lean
theorem SmoothFactorization.isKoszulRegularImmersion_refinementProj
    (hreg : IsKoszulRegularImmersion F.imm) :
    IsKoszulRegularImmersion (F.refinementProj p)
```

**`Stacks.Chow.SmoothFactorization.isRegularImmersion_refinementSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/FactorizationIndependence.lean, line 400](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/FactorizationIndependence.lean#L400). The attribute's comment: “the second step of the proof: the section `s = (1, i')` of the smooth retraction `p̄ : X ×_P P' ⟶ X` is a regular immersion, Stacks 067R”.

> **Stacks 0FF2, second step: regularity of `s`.** The section `s = (1, i')` of the smooth
> retraction `p̄` is a regular immersion, by Stacks 067R. Together with the regularity of `j` this
> is what makes both Gysin classes in the Stacks Project's identity `(i')^! = s^! ∘ j^!`
> (Stacks 0FF0) available.

```lean
theorem SmoothFactorization.isRegularImmersion_refinementSection :
    IsRegularImmersion (F.refinementSection p hp)
```

**`Stacks.Chow.SmoothFactorization.exists_refinement_diagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/FactorizationIndependence.lean, line 416](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/FactorizationIndependence.lean#L416). The attribute's comment: “the second step of the proof, packaged for a refining pair: the cartesian square `W = X ×_P P'` with its smooth retraction `p̄`, the base change `j` of the immersion, and the section `s` of `p̄` satisfying `i' = s ≫ j`, with `j` Koszul-regular and `s` regular; the regularity of the coarser immersion is the prerequisite `hreg`”.

> **Stacks 0FF2, second step, packaged.** For a refining pair of factorizations of `f`, with the
> immersion of the coarser one Koszul-regular, the diagram of the second step of the proof of
> Stacks 0FF2 exists: a scheme `W = X ×_P P'`, a smooth retraction `p̄ : W ⟶ X`, the base change
> `j : W ⟶ P'` of `i` along the refinement, and a section `s : X ⟶ W` of `p̄` with `s ≫ j = i'`,
> where `j` is a Koszul-regular immersion and `s` a regular immersion.

```lean
theorem SmoothFactorization.exists_refinement_diagram {F F' : SmoothFactorization f}
    (h : F'.Refines F) (hreg : IsKoszulRegularImmersion F.imm) :
    ∃ (W : Scheme.{u}) (pbar : W ⟶ X) (j : W ⟶ F'.ambient) (s : X ⟶ W),
      Smooth pbar ∧ s ≫ pbar = 𝟙 X ∧ s ≫ j = F'.imm ∧
        ∃ (hj : IsImmersion j) (hs : IsImmersion s),
          (letI := hj; IsKoszulRegularImmersion j) ∧ letI := hs; IsRegularImmersion s
```

**`Stacks.Chow.SmoothFactorization.gysinMap_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/LciGysinMapComposition.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/LciGysinMapComposition.lean#L104).

> **Stacks 0FF2.** Let `f : X ⟶ Y` be a local complete intersection morphism of schemes locally
> of finite type over the base. The Gysin map `f^! = i^! ∘ g^* ∈ A^*(X ⟶ Y)^∧` of a factorization
> `f = g ∘ i`, `i` an immersion and `g` smooth (Stacks 0FF3), does not depend on the
> factorization.

```lean
theorem SmoothFactorization.gysinMap_eq (F F' : SmoothFactorization f)
    (hlci : IsLocalCompleteIntersectionMorphism f) :
    F.gysinMap C sX sY hf hlci = F'.gysinMap C sX sY hf hlci
```

## Tag 0FF3, a definition

[Tag 0FF3](https://stacks.math.columbia.edu/tag/0FF3) in the Stacks Project.

**`Stacks.Chow.GysinMapExists`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection.lean#L73). The attribute's comment: “the existence of the Gysin map”.

> **Stacks 0FF3.** The Gysin map of a local complete intersection morphism `f : X ⟶ Y` of
> schemes locally of finite type over the base *exists* when `f` factors as an immersion
> `i : X ⟶ P` followed by a smooth morphism `g : P ⟶ Y`.

```lean
def GysinMapExists {X Y : Scheme.{u}} (f : X ⟶ Y) : Prop
```

**`Stacks.Chow.SmoothFactorization.gysinMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/GysinMap.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/GysinMap.lean#L83). The attribute's comment: “the Gysin map f^! = i^! ∘ g^* ∈ A^*(X → Y)^∧ of a factorization f = g ∘ i, i an immersion and g smooth, of a local complete intersection morphism”.

> **Stacks 0FF3, the Gysin map of a factorization.** For a local complete intersection morphism
> `f : X ⟶ Y` and a factorization `f = g ∘ i` with `i : X ⟶ P` an immersion and `g : P ⟶ Y` smooth,
> the class
>
>   `f^! = i^! ∘ g^* ∈ A^*(X ⟶ Y)^∧`,
>
> the composite (Stacks 0FE0) of the class `i^! = c(X ⟶ P, 𝒩_{X/P})` of the regular immersion `i`
> (Stacks 0FBK, 0FBQ (3)) with the flat pullback `g^*` of the smooth morphism `g` (Stacks 0B78).

```lean
def SmoothFactorization.gysinMap (F : SmoothFactorization f)
    (hlci : IsLocalCompleteIntersectionMorphism f) :
    completedBivariantGroup C (gysinSystemOfInvertible C) sX sY f hf
```

**`Stacks.Chow.lciGysinMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/GysinMap.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/GysinMap.lean#L104). The attribute's comment: “the Gysin map f^! ∈ A^*(X → Y)^∧ of a local complete intersection morphism for which the Gysin map exists”.

> **Stacks 0FF3, the Gysin map `f^!`** of a local complete intersection morphism `f : X ⟶ Y` of
> schemes locally of finite type over the base for which the Gysin map exists: the class
> `i^! ∘ g^*` of a chosen factorization `f = g ∘ i`. By Stacks 0FF2 it does not depend on the choice
> (`Stacks.Chow.SmoothFactorization.gysinMap_eq_lciGysinMap`).

```lean
def lciGysinMap (hlci : IsLocalCompleteIntersectionMorphism f) (h : GysinMapExists f) :
    completedBivariantGroup C (gysinSystemOfInvertible C) sX sY f hf
```

**`Stacks.Chow.lciGysinClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/LciGysinClass.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/LciGysinClass.lean#L174). The attribute's comment: “the Gysin map f^! = i^! ∘ g^* in A^*(X → Y)^∧ of a local complete intersection morphism f = g ∘ i, g smooth, i an immersion: i^! = c(X → U, N_{X/U}) of Tag 0FBK for the regular closed immersion of X into the open U ⊆ P where i is closed, g^* the flat pullback of Tag 0B78 on each connected component, ∘ the completed composition of Tag 0FE0”.

> The Gysin map `f^! = i^! ∘ g^* ∈ A^*(X ⟶ Y)^∧` of a local complete intersection morphism
> `f : X ⟶ Y` of schemes locally of finite type over `S`, for a factorization `F` of `f` as an
> immersion `i : X ⟶ P` followed by a smooth morphism `g : P ⟶ Y`: the composite in the completed
> groups of the class `i^! = c(X ⟶ U, 𝒩_{X/U})` of the normal sheaf of the regular closed immersion
> `i' : X ⟶ U` into the open `U ⊆ P` in which `i` is closed, and of the flat pullback `(g|_U)^*`
> along the smooth morphism `g|_U`.

```lean
def lciGysinClass :
    completedBivariantGroup C (gysinSystemOfInvertible C) sX sY f hfs
```

## Tag 0FF4, a lemma

[Tag 0FF4](https://stacks.math.columbia.edu/tag/0FF4) in the Stacks Project.

**`Stacks.Chow.lciGysinMap_eq_completedFlatPullbackOfFlatLCI`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/LciGysinFlat.lean, line 381](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/LciGysinFlat.lean#L381). The attribute's comment: “f^! = f^* in the completed bivariant group A^*(X → Y)^∧, the relative dimension of the flat morphism f being only locally constant”.

> **Stacks 0FF4.** Let `f : X ⟶ Y` be a local complete intersection morphism of schemes locally
> of finite type over the base for which the Gysin map exists. If `f` is flat, its Gysin map
> `f^! ∈ A^*(X ⟶ Y)^∧` (Stacks 0FF3) is the flat-pullback class `f^*` of Stacks 0B78, read in the
> completed bivariant group because the relative dimension of `f` is only locally constant.

```lean
theorem lciGysinMap_eq_completedFlatPullbackOfFlatLCI [Flat f]
    (hlci : IsLocalCompleteIntersectionMorphism f) (h : GysinMapExists f) :
    letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian sX
    letI : IsLocallyNoetherian Y := LocallyOfFiniteType.isLocallyNoetherian sY
    lciGysinMap C sX sY hf hlci h = completedFlatPullbackOfFlatLCI C sX sY f hf hlci
```

## Tag 0FF5, a lemma

[Tag 0FF5](https://stacks.math.columbia.edu/tag/0FF5) in the Stacks Project.

**`Stacks.Chow.GysinMapExists.left_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/Factorization.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/Factorization.lean#L78). The attribute's comment: “the Gysin map exists for the first factor of the composite”.

> **Stacks 0FF5, first assertion.** If the Gysin map exists for a composite `f ≫ g`, then it
> exists for `f`.
>
> Given a factorization `f ≫ g = i ≫ q` with `i : X ⟶ P` an immersion and `q : P ⟶ Z` smooth, the
> morphism `X ⟶ P ×_Z Y` induced by `i` and `f` is an immersion, because composing it with the
> projection to `P` returns `i`, and the projection `P ×_Z Y ⟶ Y` is smooth, being a base change of
> `q`. Their composite is `f`.

```lean
theorem GysinMapExists.left_of_comp {X Y Z : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ Z)
    (h : GysinMapExists (f ≫ g)) : GysinMapExists f
```

**`Stacks.Chow.lciGysinMap_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/LciGysinMapComposition.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/LciGysinMapComposition.lean#L135).

> **Stacks 0FF5.** Let `f : X ⟶ Y` and `g : Y ⟶ Z` be local complete intersection morphisms of
> schemes locally of finite type over the base, and assume the Gysin map exists for `g ∘ f` and
> for `g` (Stacks 0FF3). Then the Gysin map exists for `f`, and
>
>   `(g ∘ f)^! = f^! ∘ g^!`   in `A^*(X ⟶ Z)^∧`.
>
> (`g ∘ f` is a local complete intersection morphism by Stacks 069J.)

```lean
theorem lciGysinMap_comp (hlf : IsLocalCompleteIntersectionMorphism f)
    (hlg : IsLocalCompleteIntersectionMorphism g) (hgf : GysinMapExists (f ≫ g))
    (hG : GysinMapExists g) :
    haveI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian sX
    haveI : IsLocallyNoetherian Y := LocallyOfFiniteType.isLocallyNoetherian sY
    haveI : IsLocallyNoetherian Z := LocallyOfFiniteType.isLocallyNoetherian sZ
    ∃ hF : GysinMapExists f,
      lciGysinMap C sX sZ (comp_comp_structureMorphism_eq hf hg)
          (isLocalCompleteIntersectionMorphism_comp f g hlf hlg) hgf =
        completedBivariantCompositeOfInvertible C sX sY sZ f g hf hg
          (lciGysinMap C sX sY hf hlf hF) (lciGysinMap C sY sZ hg hlg hG)
```

## Tag 0FF6, a lemma

[Tag 0FF6](https://stacks.math.columbia.edu/tag/0FF6) in the Stacks Project.

**`Stacks.Chow.bivariantCommute_flatPullbackBivariantClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/FlatPullbackCommuting.lean, line 189](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/FlatPullbackCommuting.lean#L189). The attribute's comment: “the smooth half only: the flat-pullback bivariant class of Stacks 0B78 commutes with an arbitrary bivariant class. The `i^!` half of the factorization `f = i ≫ g` is excluded; it is Stacks 0FBP, which has no carrier here, as has every tag needed to build `f^!`”.

> **The smooth half of Stacks 0FF6.** The flat-pullback bivariant class of Stacks 0B78 for a
> flat morphism `f₁ : Z₁ ⟶ X` of relative dimension `r` commutes, in the sense of Stacks 0FA2, with
> every bivariant class `c₂ ∈ A^{p₂}(Z₂ ⟶ X)`.
>
> This is the `g^*` half of the factorization `f = i ≫ g` by which the source proves Stacks 0FF6,
> and the source's reason is the one used here: it is immediate from the flat-pullback law of
> Stacks 0B76 (2) for `c₂`. The `i^!` half is Stacks 0FBP, which has no carrier in this repository;
> see the implementation notes of
> `StacksFrontier.AlgebraicGeometry.Chow.Bivariant.FlatPullbackCommuting`.

```lean
theorem bivariantCommute_flatPullbackBivariantClass :
    BivariantCommute C G sX f₁ f₂ (-(r : ℤ)) p₂
      (flatPullbackBivariantClass C G (f₁ ≫ sX) sX f₁ rfl r hfr hS1 hRG h71) c₂
```

**`Stacks.Chow.completedCommutesWithEveryClass_completedBivariantRestriction_lciGysinMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/GysinMapCommutes.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/GysinMapCommutes.lean#L98). The attribute's comment: “for every Y' → Y, the restriction res(f^!) ∈ A^*(X' → Y')^∧ of the Gysin map of a local complete intersection morphism commutes with every c ∈ A^q(Y'' → Y'), every Y'' → Y' and q”.

> **Stacks 0FF6.** Let `f : X ⟶ Y` be a local complete intersection morphism of schemes locally
> of finite type over the base such that the Gysin map `f^! ∈ A^*(X ⟶ Y)^∧` exists (Stacks 0FF3).
> For every `g : Y' ⟶ Y` locally of finite type, the restriction `res(f^!) ∈ A^*(X' ⟶ Y')^∧` of
> `f^!` along `g` (Stacks 0F9Z), `X' = X ×_Y Y'`, commutes with every bivariant class
> `c ∈ A^q(Y'' ⟶ Y')`, for every `Y'' ⟶ Y'` locally of finite type and every degree `q`, in the sense
> of Stacks 0FA2, degree by degree: every term of the tuple attached to `res(f^!)` by Stacks 0FE0
> commutes with `c`.

```lean
theorem completedCommutesWithEveryClass_completedBivariantRestriction_lciGysinMap
    (hlci : IsLocalCompleteIntersectionMorphism f) (h : GysinMapExists f) {Y' : Scheme.{u}}
    (g : Y' ⟶ Y) [LocallyOfFiniteType g] :
    haveI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian sX
    haveI : IsLocallyNoetherian Y := LocallyOfFiniteType.isLocallyNoetherian sY
    haveI : IsLocallyNoetherian Y' := LocallyOfFiniteType.isLocallyNoetherian (g ≫ sY)
    haveI : IsLocallyNoetherian (pullback f g) :=
      LocallyOfFiniteType.isLocallyNoetherian (pullback.fst f g ≫ sX)
    completedCommutesWithEveryClass C (pullback.fst f g ≫ sX) (g ≫ sY) (pullback.snd f g)
      (pullbackSnd_comp_structureMorphism_eq C sX sY f hf g)
      (completedBivariantRestrictionViaSequence C sX sY f hf g
        (lciGysinMap C sX sY hf hlci h))
```

## Tag 0FF7, a lemma

[Tag 0FF7](https://stacks.math.columbia.edu/tag/0FF7) in the Stacks Project.

**`Stacks.Chow.lciGysinCap_fundamentalChowClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/LciGysinFundamentalClass.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/LciGysinFundamentalClass.lean#L174). The attribute's comment: “δ-equidimensional case: `f^![Y']_n = [X']_n'` for `f = i ≫ g`, `g` smooth, with `f^!` characterized as `i^! ∘ g^*` (0FF3, 0FE0) and `i^!` by 0FBK; `g^*[Y'] = [P ×_Y Y']` proved here; carried: 0FEA's regular-sequence step as vanishing excess (so hypothesis (4) is replaced by its consequence), 0FBM's hcone and hinj, 02S1, 02S2, 02RG, 0B71; no clopen reduction”.

> **The Gysin map of a local complete intersection on a fundamental class, δ-equidimensional
> case.** Let `f = i ≫ g` with `i : X ⟶ P` an immersion carrying a virtual normal bundle of
> constant rank `r` and `g : P ⟶ Y` smooth of constant relative dimension `d`, and let
> `g' : Y' ⟶ Y` be a test scheme of δ-dimension at most `n`. Assume
>
> * `ci` satisfies the characterizing relation `Stacks.Chow.IsVirtualNormalGysinClass` for the
>   virtual normal bundle of `i`, so that `ci` is the Gysin class `i^! = c(X ⟶ P, 𝒩)`;
> * `cf` is the composite `ci ∘ g^*` in the sense of `Stacks.Chow.IsBivariantClassComposition`,
>   so that `cf` is the Gysin map `f^! = i^! ∘ g^*`; and
> * `dim_δ(X ×_Y Y') ≤ n + d - r`.
>
> Then `f^![Y']_n = [X']_{n - (r + (-d))}`.

```lean
theorem lciGysinCap_fundamentalChowClass
    (hinj : ∀ {T : Scheme.{u}} (t : T ⟶ P) [LocallyOfFiniteType t] (k : ℤ),
      Function.Injective
        (bundleFlatPullback C sX sN i q hq r NP.flat NP.relativeDimension hdesc t k))
    {ci : BivariantClass C G sX sP i hi (r : ℤ)}
    (hci : IsVirtualNormalGysinClass C G sX sP sN i hi q hq r 0 E
      (bundleFlatPullback C sX sN i q hq r NP.flat NP.relativeDimension hdesc) NP ci)
    {cf : BivariantClass C G sX sY (i ≫ g) (comp_comp_structureMorphism_eq hi hg)
      ((r : ℤ) + -(d : ℤ))}
    (hcf : IsBivariantClassComposition C G sX sP sY i g hi hg hpp (r : ℤ) (-(d : ℤ)) ci
      (flatPullbackBivariantClass C G sP sY g hg d hgd hdesc hRG h71) cf)
    {Y' : Scheme.{u}} (g' : Y' ⟶ Y) [LocallyOfFiniteType g'] (n : ℤ)
    (hY' : schemeDeltaDimension C (g' ≫ sY) ≤ (n : EInt))
    (hX' : schemeDeltaDimension C (pullback.fst i (pullback.fst g g') ≫ sX) ≤
      (((n + (d : ℤ)) - (r : ℤ) : ℤ) : EInt))
    (hcone : chowGroupDegreeEquiv C (pullback.fst (q ≫ i) (pullback.fst g g') ≫ sN)
        (by omega : (n + (d : ℤ)) - (0 : ℤ) = ((n + (d : ℤ)) - (r : ℤ)) + (r : ℤ))
        (E.cap (pullback.fst g g') (n + (d : ℤ))
          (fundamentalChowClass C (pullback.fst g g' ≫ sP) (n + (d : ℤ)))) =
      fundamentalChowClass C (pullback.fst (q ≫ i) (pullback.fst g g') ≫ sN)
        (((n + (d : ℤ)) - (r : ℤ)) + (r : ℤ))) :
    cf.cap g' n (fundamentalChowClass C (g' ≫ sY) n) =
      fundamentalChowClass C (pullback.fst (i ≫ g) g' ≫ sX) (n - ((r : ℤ) + -(d : ℤ)))
```

**`Stacks.Chow.completedCapFundamentalClass_completedBivariantRestriction_lciGysinMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/LciGysinFundamentalCycle.lean, line 536](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/LciGysinFundamentalCycle.lean#L536).

> **Stacks 0FF7.** Consider a cartesian square `X' = X ×_Y Y'` of schemes locally of finite type
> over the base, with `f : X ⟶ Y` and its base change `f' : X' ⟶ Y'`. Assume
>
> 1. `f` is a local complete intersection morphism for which the Gysin map `f^!` exists
>    (Stacks 0FF3);
> 2. `X`, `X'`, `Y`, `Y'` satisfy the equivalent conditions of Stacks 0FE3, here as decompositions
>    into open and closed pieces of constant `δ`-dimension;
> 3. `n_{x'} - n_{y'} = n_x - n_y` for every `x' ∈ X'` with images `x ∈ X`, `y' ∈ Y'`, `y ∈ Y`;
> 4. `𝒪_{Y', f'(ξ)}` is Cohen–Macaulay for every generic point `ξ` of `X'`.
>
> Then `f^![Y'] = [X']`, for the fundamental classes of Stacks 0FE4. Here `n_x` is the common value
> of `δ` at the generic points of the irreducible components through `x` (Stacks 0FE3); it is
> constant on connected components, and equals the index of the piece of the decomposition
> containing the point
> (`Stacks.Chow.relativeDimension_eq_componentDeltaDimension_of_mem_genericPoints`), which is why
> it is written `Stacks.Chow.componentDeltaDimension` of the connected component of `x`. The cap
> product `f^![Y']` is that of the restriction `res(f^!)` of Stacks 0F9Z on the completed groups
> of Stacks 0FE0 (`Stacks.Chow.completedCapFundamentalClass`), and both sides are read on the
> connected components of `X'`, where `[X']` is `[X'_w]_{n_w}`
> (`Stacks.Chow.componentFundamentalClassDirectSum`,
> `Stacks.Chow.chowGroupRestrict_fundamentalClass`).
>
> The proof is the source's. For a factorization `f = g ∘ i` with `i : X ⟶ P` an immersion and
> `g : P ⟶ Y` smooth, `f^! = i^! ∘ g^*` is, on a connected component `X_a` of `X`, homogeneous of
> degree `n_{f(X_a)} - n_{X_a}`, the relative dimension of `g` and the rank of the normal sheaf of
> `i` being constant on the connected components
> (`Stacks.Chow.SmoothFactorization.exists_hasCapFundamentalFormula_gysinMap`);
> there `g^*[T] = [P ×_Y T]`, the local rings of `P ×_Y T` are Cohen–Macaulay where needed, and
> Stacks 0FEA applies to `i`
> (`Stacks.Chow.BivariantClass.capFundamentalFormula_bivariantCompositeOfInvertible`). Restricting
> to `Y'` and to the connected components of `X'` is
> `Stacks.Chow.completedCapFundamentalClass_restriction_of_hasCapFundamentalFormula`.

```lean
theorem completedCapFundamentalClass_completedBivariantRestriction_lciGysinMap
    (hlci : IsLocalCompleteIntersectionMorphism f) (h : GysinMapExists f) {Y' : Scheme.{u}}
    (g : Y' ⟶ Y) [LocallyOfFiniteType g]
    (hX : HasDimensionDecomposition (relativeDimension C.dimensionFunction sX))
    (hY : HasDimensionDecomposition (relativeDimension C.dimensionFunction sY))
    (hX' : HasDimensionDecomposition
      (relativeDimension C.dimensionFunction (pullback.fst f g ≫ sX)))
    (hY' : HasDimensionDecomposition (relativeDimension C.dimensionFunction (g ≫ sY)))
    (hn : ∀ x : (pullback f g : Scheme.{u}),
      componentDeltaDimension C (pullback.fst f g ≫ sX) hX' (_root_.ConnectedComponents.mk x) -
          componentDeltaDimension C (g ≫ sY) hY'
            (_root_.ConnectedComponents.mk (pullback.snd f g x)) =
        componentDeltaDimension C sX hX (_root_.ConnectedComponents.mk (pullback.fst f g x)) -
          componentDeltaDimension C sY hY
            (_root_.ConnectedComponents.mk (f (pullback.fst f g x))))
    (hCM : haveI : IsLocallyNoetherian Y' := LocallyOfFiniteType.isLocallyNoetherian (g ≫ sY)
      ∀ ξ : (pullback f g : Scheme.{u}), ξ ∈ genericPoints (pullback f g : Scheme.{u}) →
        IsCohenMacaulayLocalRing (Y'.presheaf.stalk (pullback.snd f g ξ))) :
    haveI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian sX
    haveI : IsLocallyNoetherian Y := LocallyOfFiniteType.isLocallyNoetherian sY
    haveI : IsLocallyNoetherian Y' := LocallyOfFiniteType.isLocallyNoetherian (g ≫ sY)
    haveI : IsLocallyNoetherian (pullback f g) :=
      LocallyOfFiniteType.isLocallyNoetherian (pullback.fst f g ≫ sX)
    completedCapFundamentalClass C (gysinSystemOfInvertible C) (pullback.fst f g ≫ sX) (g ≫ sY)
        (pullback.snd f g) (pullbackSnd_comp_structureMorphism_eq C sX sY f hf g) hY'
        (completedBivariantRestrictionViaSequence C sX sY f hf g (lciGysinMap C sX sY hf hlci h)) =
      componentFundamentalClassDirectSum C (pullback.fst f g ≫ sX) hX'
```

## Tag 0FF8, a remark

[Tag 0FF8](https://stacks.math.columbia.edu/tag/0FF8) in the Stacks Project.

**`Stacks.Chow.bivariantCommute_flatPullbackBivariantClass_chernClassBivariant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/LciGysinChernClasses.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/LciGysinChernClasses.lean#L172). The attribute's comment: “part (a), the flat `g^*` factor only, in the commuting form of 0FA2: `g^*` commutes with the bivariant Chern class of 0B7H. `res(c_j(E)) = c_j(g^*E)` is NOT identified, the `i^!` factor is 0FBP (absent here), and the Chern character is not stated”.

> **Stacks 0FF8 (a), for the flat factor of the factorization.** The flat-pullback bivariant
> class of Stacks 0B78 attached to a smooth morphism `g : P ⟶ Y` of relative dimension `d` commutes,
> in the sense of Stacks 0FA2, with the bivariant `j`-th Chern class `c_j(ℰ) ∈ A^j(Y ⟶ Y)` of
> Stacks 0B7H.
>
> Stacks 0FF8 (a) asserts `f^! ∘ c_j(ℰ) = c_j(f^*ℰ) ∘ f^!` for the Gysin map of a local complete
> intersection morphism `f = i ≫ g`, citing Stacks 0FF6. Stacks 0FF6 is proved in the source by
> treating the two factors of the factorization separately, and its carrier in this repository,
> `Stacks.Chow.bivariantCommute_flatPullbackBivariantClass`, is the `g^*` factor. This is that
> carrier instantiated at the bivariant Chern class, which is the assembly Stacks 0FF8 performs.
> The `i^!` factor is Stacks 0FBP and has no carrier here; see the implementation notes.
>
> Two further caveats on what this is. First, the statement is the commuting form of Stacks 0FA2
> rather than the displayed composition `f^! ∘ c_j(ℰ) = c_j(f^*ℰ) ∘ f^!`; the two are equivalent by
> `Stacks.Chow.bivariantCommute_iff_cap_eq_of_isBivariantClassComposition`, but rewriting
> `res(c_j(ℰ))` as the bivariant Chern class of `g^*ℰ` is a separate identification, which needs
> the pseudofunctoriality of pullback of modules against `Stacks.Chow.HigherChernCapRule` and is
> not carried out here. Second, the Chern character is not stated.

```lean
theorem bivariantCommute_flatPullbackBivariantClass_chernClassBivariant :
    BivariantCommute C G sY g (𝟙 Y) (-(d : ℤ)) (j : ℤ)
      (flatPullbackBivariantClass C G (g ≫ sY) sY g rfl d hgd hdesc hRG h71)
      (chernClassBivariantOverIdComp C sY E r G cap j hproper hflat hgysin hiso)
```

**`Stacks.Chow.lciGysinCap_fundamentalChowClass_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/LciGysinChernClasses.lean, line 219](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/LciGysinChernClasses.lean#L219). The attribute's comment: “part (b): `f^![Y]_n = [X]_{n-(r-d)}` on `X` itself, from 0FF7 at `Y' = Y`. The 0FE3 conditions enter as the two δ-dimension bounds and the Cohen-Macaulay hypothesis as the vanishing excess `hcone`, exactly as in 0FF7's carrier; no clopen reduction”.

> **Stacks 0FF8 (b).** Let `f = i ≫ g` with `i : X ⟶ P` an immersion carrying a virtual normal
> bundle of constant rank `r` and `g : P ⟶ Y` smooth of constant relative dimension `d`, so that
> the Gysin map exists for `f` in the sense of Stacks 0FF3, and let `f^!` be the Gysin map, entering
> as a bivariant class `cf` characterized as `i^! ∘ g^*`. If `dim_δ(Y) ≤ n` and
> `dim_δ(X ×_P (P ×_Y Y)) ≤ n + d - r`, then
>
>   `f^![Y]_n = [X]_{n - (r - d)}`
>
> in the Chow group of `X` itself.
>
> This is `Stacks.Chow.lciGysinCap_fundamentalChowClass`, the δ-equidimensional case of
> Stacks 0FF7, at the test scheme `g' = 𝟙 Y`, followed by the identification of `X ×_Y Y` with `X`:
> the projection `pullback.fst f (𝟙 Y)` is an isomorphism, and pushforward along an isomorphism
> over the base carries a fundamental class to a fundamental class by
> `Stacks.Chow.chowPushforwardOfIso_fundamentalChowClass`.
>
> The hypotheses are those of `Stacks.Chow.lciGysinCap_fundamentalChowClass`, whose implementation
> notes say what each one is and why none of them is the conclusion; see also the implementation
> notes above for how the Cohen-Macaulay hypothesis and the conditions of Stacks 0FE3 enter.

```lean
theorem lciGysinCap_fundamentalChowClass_id
    (hinj : ∀ {T : Scheme.{u}} (t : T ⟶ P) [LocallyOfFiniteType t] (k : ℤ),
      Function.Injective
        (bundleFlatPullback C sX sN i q hq r NP.flat NP.relativeDimension hdesc t k))
    {ci : BivariantClass C G sX sP i hi (r : ℤ)}
    (hci : IsVirtualNormalGysinClass C G sX sP sN i hi q hq r 0 EC
      (bundleFlatPullback C sX sN i q hq r NP.flat NP.relativeDimension hdesc) NP ci)
    {cf : BivariantClass C G sX sY (i ≫ g) (comp_comp_structureMorphism_eq hi hg)
      ((r : ℤ) + -(d : ℤ))}
    (hcf : IsBivariantClassComposition C G sX sP sY i g hi hg hpp (r : ℤ) (-(d : ℤ)) ci
      (flatPullbackBivariantClass C G sP sY g hg d hgd hdesc hRG h71) cf)
    (n : ℤ) (hY : schemeDeltaDimension C (𝟙 Y ≫ sY) ≤ (n : EInt))
    (hX : schemeDeltaDimension C (pullback.fst i (pullback.fst g (𝟙 Y)) ≫ sX) ≤
      (((n + (d : ℤ)) - (r : ℤ) : ℤ) : EInt))
    (hcone : chowGroupDegreeEquiv C (pullback.fst (q ≫ i) (pullback.fst g (𝟙 Y)) ≫ sN)
        (by omega : (n + (d : ℤ)) - (0 : ℤ) = ((n + (d : ℤ)) - (r : ℤ)) + (r : ℤ))
        (EC.cap (pullback.fst g (𝟙 Y)) (n + (d : ℤ))
          (fundamentalChowClass C (pullback.fst g (𝟙 Y) ≫ sP) (n + (d : ℤ)))) =
      fundamentalChowClass C (pullback.fst (q ≫ i) (pullback.fst g (𝟙 Y)) ≫ sN)
        (((n + (d : ℤ)) - (r : ℤ)) + (r : ℤ))) :
    chowPushforwardOfIso C (pullback.fst (i ≫ g) (𝟙 Y) ≫ sX) sX
        (pullback.fst (i ≫ g) (𝟙 Y)) rfl (n - ((r : ℤ) + -(d : ℤ)))
        (cf.cap (𝟙 Y) n
          (chowGroupCongr C (Category.id_comp sY).symm n (fundamentalChowClass C sY n))) =
      fundamentalChowClass C sX (n - ((r : ℤ) + -(d : ℤ)))
```

**`Stacks.Chow.flatPullbackChow_chernCap_fundamentalChowClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/LciGysinChernClasses.lean, line 290](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/LciGysinChernClasses.lean#L290). The attribute's comment: “part (c), the flat `g^*` factor only: `h^*(c_j(t^*E) ∩ [T]_n) = c_j((h ≫ t)^*E) ∩ [T']_{n+m}` for `h` flat of relative dimension `m` — the Gysin map of a smooth `h` — from 02U8 (carried, as `hflat`) and 02RB. The lci `f^!` needs 0FBP, which is proved only with its own hypotheses carried — `Stacks.Chow.virtualNormalGysinClass_bivariantCommute` of Chow/Bivariant/VirtualNormalCommuting.lean assumes the 0FBL/0FBN factorization, the centrality of Stacks 02UA and the commutation of the second factor, and the reduction of 02UC and 02OS to a divisor is not carried out — so it is not usable here; no Chern character”.

> **Stacks 0FF8 (c), for the flat factor of the factorization.** Let `ℰ` be finite locally free
> of rank `r` on `Y`, let `t : T ⟶ Y` be a test scheme with `dim_δ(T) ≤ n`, and let `h : T' ⟶ T` be
> flat of constant relative dimension `m`. Then
>
>   `h^*(c_j(t^*ℰ) ∩ [T]_n) = c_j((h ≫ t)^*ℰ) ∩ [T']_{n+m}`,
>
> the two sides sitting in the degrees `(n - j) + m` and `(n + m) - j`, which are the same integer
> written two ways.
>
> This is Stacks 0FF8 (c) for the `g^*` factor of the factorization `f = i ≫ g`. For a *smooth*
> `h` the Gysin map of Stacks 0FF3 is flat pullback, by the factorization with `i = 𝟙`, so the
> display above is then literally `h^!(c_j(ℰ) ∩ [T]) = c_j(h^*ℰ) ∩ [T']`; the statement is proved
> in the flat generality that its two inputs support, which is the generality in which
> `StacksFrontier.AlgebraicGeometry.Chow.Bivariant.FlatPullbackCommuting` carries Stacks 0FF6. Those
> inputs are: part (b) for the factor, `h^*[T]_n = [T']_{n+m}`, which is Stacks 02RB on Chow
> groups, `Stacks.Chow.flatPullbackChow_fundamentalChowClass`; and part (a) for the factor, the
> commutation of the Chern class operations with flat pullback, Stacks 02U8, which is the
> hypothesis `hflat` carried here, exactly as `Stacks.Chow.chernClassBivariant` carries it. The lci
> case needs Stacks 0FBP; see the implementation notes. The Chern character is not stated.
>
> `Stacks.Chow.chernIdentityCapRule C sY E r cap hrank j` is the rule `α ↦ c_j(u^*ℰ) ∩ α` on the
> Chow groups of each test scheme `u : U ⟶ Y`; it unfolds to
> `cap (u ≫ sY) ((Scheme.Modules.pullback u).obj E) k j`.

```lean
theorem flatPullbackChow_chernCap_fundamentalChowClass
    (hflat : IdentityCapRule.FlatNaturality C sY (j : ℤ)
      (chernIdentityCapRule C sY E r cap hrank j))
    {T T' : Scheme.{u}} (t : T ⟶ Y) [LocallyOfFiniteType t] (h : T' ⟶ T)
    [LocallyOfFiniteType h] [AlgebraicGeometry.Flat h] (m : ℕ)
    (hm : AlgebraicGeometry.RelativeDimension h m) (n : ℤ)
    (hdim : schemeDeltaDimension C (t ≫ sY) ≤ (n : EInt))
    (hfac : FlatPullbackFactorsThroughRationalEquivalence C ((h ≫ t) ≫ sY) (t ≫ sY) h
      (by simp [Category.assoc]) m hm n)
    (hfacj : FlatPullbackFactorsThroughRationalEquivalence C ((h ≫ t) ≫ sY) (t ≫ sY) h
      (by simp [Category.assoc]) m hm (n - (j : ℤ))) :
    chernIdentityCapRule C sY E r cap hrank j (h ≫ t) (n + (m : ℤ))
        (fundamentalChowClass C ((h ≫ t) ≫ sY) (n + (m : ℤ))) ≍
      flatPullbackChow C ((h ≫ t) ≫ sY) (t ≫ sY) h (by simp [Category.assoc]) m hm
        (n - (j : ℤ)) hfacj
        (chernIdentityCapRule C sY E r cap hrank j t n (fundamentalChowClass C (t ≫ sY) n))
```

**`Stacks.Chow.lciGysinClass_comp_chernClassOfModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/LciGysinChernCommuting.lean, line 286](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/LciGysinChernCommuting.lean#L286). The attribute's comment: “first assertion: f^! ∘ c_i(E) = c_i(f^*E) ∘ f^! for the Gysin map f^! of 0FF3 (`lciGysinClass`) and E finite locally free of any rank (c_i of 0ESW), stated in every graded part (f^!)_q of f^! in A^*(X → Y)^∧; the right side is c_i(f^*E) itself, not res(c_i(E))”.

> **Stacks 0FF8, the Chern classes.** Let `f : X ⟶ Y` be a local complete intersection morphism
> of schemes locally of finite type over `S` for which the Gysin map exists, with `f^!` the Gysin
> map of Stacks 0FF3 built from a factorization `F` of `f`, and let `ℰ` be a finite locally free
> `𝒪_Y`-module of arbitrary rank. Then
>
>   `f^! ∘ c_i(ℰ) = c_i(f^*ℰ) ∘ f^!`,
>
> stated, as an identity in the completed group `A^*(X ⟶ Y)^∧` of Stacks 0FE0 is, degree by degree:
> for every `q`, `(f^!)_q ∘ c_i(ℰ) = c_i(f^*ℰ) ∘ (f^!)_q` in `A^{q+i}(X ⟶ Y)`. The Chern classes are
> those of Stacks 0ESW.

```lean
theorem lciGysinClass_comp_chernClassOfModule (E : Y.Modules)
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u} E] (i : ℕ) (q : ℤ) :
    haveI := isFiniteLocallyFree_pullback_of_isFiniteLocallyFree f E
    (lciGysinClassComponent C sX sY f hfs hf F q).comp
        (BivariantChowClass.equivBivariantClass.symm (chernClassOfModule C sY E i)) =
      (((BivariantChowClass.equivBivariantClass.symm
          (chernClassOfModule C sX ((Scheme.Modules.pullback f).obj E) i)).comp
            (lciGysinClassComponent C sX sY f hfs hf F q)).degreeCongr
        (add_comm (i : ℤ) q)).transport (comp_comp_structureMorphism_eq hfs (Category.id_comp sY))
        (Iso.refl X) (by simp)
```

**`Stacks.Chow.lciGysinClass_comp_chernCharacterOfModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/LciGysinChernCommuting.lean, line 310](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/LciGysinChernCommuting.lean#L310). The attribute's comment: “first assertion, for the Chern character: f^! ∘ ch(E) = ch(f^*E) ∘ f^! in A^*(X → Y) ⊗ Q, stated for every graded part (f^!)_q of the Gysin map of 0FF3 and every component ch_p(E) = P_p(E)/p! of the Chern character of 0ESX, E finite locally free of any rank”.

> **Stacks 0FF8, the Chern character.** In the situation of
> `Stacks.Chow.lciGysinClass_comp_chernClassOfModule`,
>
>   `f^! ∘ ch(ℰ) = ch(f^*ℰ) ∘ f^!`,
>
> stated degree by degree: for every `q` and every `p`, `(f^!)_q ∘ ch_p(ℰ) = ch_p(f^*ℰ) ∘ (f^!)_q` in
> `A^{q+p}(X ⟶ Y) ⊗ 𝐐`, with `ch_p(ℰ) = P_p(ℰ)/p!` the Chern character of Stacks 0ESX
> (`Stacks.Chow.chernCharacterOfModule`) and the composites with a rational class the rational
> extensions of those of Stacks 0B75.

```lean
theorem lciGysinClass_comp_chernCharacterOfModule (E : Y.Modules)
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u} E] (p : ℕ) (q : ℤ) :
    haveI := isFiniteLocallyFree_pullback_of_isFiniteLocallyFree f E
    LinearMap.lTensor ℚ ((lciGysinClassComponent C sX sY f hfs hf F q).compRightHom f hfs
        (p : ℤ)).toIntLinearMap (chernCharacterOfModule C sY E p) =
      LinearMap.lTensor ℚ ((lciGysinClassComponent C sX sY f hfs hf F q).compLeftHom f hfs
        (p : ℤ)).toIntLinearMap
        (chernCharacterOfModule C sX ((Scheme.Modules.pullback f).obj E) p)
```

**`Stacks.Chow.lciGysinClass_completedCap_chernClassOfModule_cap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/LciGysinChernFundamentalClass.lean, line 325](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/LciGysinChernFundamentalClass.lean#L325). The attribute's comment: “third assertion: f^!(c_i(E) ∩ [Y]) = c_i(f^*E) ∩ [X] for the Gysin map of Tag 0FF3, E finite locally free of any rank (c_i of Tag 0ESW), read on the connected components of X in every degree; only the Tag 0FE3 condition on Y is assumed”.

> **Stacks 0FF8, `f^!(c_i(ℰ) ∩ [Y]) = c_i(f^*ℰ) ∩ [X]`.** Let `f : X ⟶ Y` be a local complete
> intersection morphism of schemes locally of finite type over `S` with Gysin map `f^!` of
> Stacks 0FF3 (built from a factorization `F`), let `Y` satisfy the equivalent conditions of
> Stacks 0FE3, and let `ℰ` be a finite locally free `𝒪_Y`-module of any rank, with Chern classes
> `c_i` of Stacks 0ESW. Then
>
>   `f^!(c_i(ℰ) ∩ [Y]) = c_i(f^*ℰ) ∩ [X]`,
>
> the classes read on the connected components `X_k` of `X` (which determine a class on `X`,
> `CH_n(X) = ∏_k CH_n(X_k)`), in every degree `n`: `c_i(ℰ) ∩ [Y]` is the family
> `(c_i(ℰ) ∩ [Y_j]_{m+i})_{j,m}` (`Stacks.Chow.componentClassCap`), `f^!` acts on it by
> `Stacks.Chow.completedCap`, and `[X]` is read as the family of fundamental classes `[X_k]`.
>
> The source assumes `X` and `Y` satisfy the conditions of Stacks 0FE3, for example `Y`
> Cohen–Macaulay; only the condition on `Y` is used.

```lean
theorem lciGysinClass_completedCap_chernClassOfModule_cap
    (hY : HasDimensionDecomposition (relativeDimension C.dimensionFunction sY)) (i : ℕ)
    (k : _root_.ConnectedComponents X) (n : ℤ) :
    haveI := LocallyOfFiniteType.isLocallyNoetherian sX
    haveI := LocallyOfFiniteType.isLocallyNoetherian sY
    haveI := isFiniteLocallyFree_pullback_of_isFiniteLocallyFree f E
    completedCap C sX sY f hfs (lciGysinClass C sX sY f hfs hf F)
        (componentClassCap C sY i (chernClassOfModule C sY E i) (componentFundamentalClass C sY))
        k n =
      componentClassCap C sX i (chernClassOfModule C sX ((Scheme.Modules.pullback f).obj E) i)
        (componentFundamentalClass C sX) k n
```

**`Stacks.Chow.lciGysinClass_completedCap_chernCharacterOfModule_cap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/LciGysinChernFundamentalClass.lean, line 362](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/LciGysinChernFundamentalClass.lean#L362). The attribute's comment: “third assertion, for the Chern character: f^!(ch(E) ∩ [Y]) = ch(f^*E) ∩ [X] in CH_*(X) ⊗ Q, for every component ch_p(E) = P_p(E)/p! of Tag 0ESX, read on the connected components of X; only the Tag 0FE3 condition on Y is assumed”.

> **Stacks 0FF8, `f^!(ch(ℰ) ∩ [Y]) = ch(f^*ℰ) ∩ [X]`.** In the situation of
> `Stacks.Chow.lciGysinClass_completedCap_chernClassOfModule_cap`, for every `p`,
>
>   `f^!(ch_p(ℰ) ∩ [Y]) = ch_p(f^*ℰ) ∩ [X]`   in `CH_*(X) ⊗ 𝐐`,
>
> with `ch_p(ℰ) = P_p(ℰ)/p!` the Chern character of Stacks 0ESX
> (`Stacks.Chow.chernCharacterOfModule`), the cap products of rational classes the rational
> extensions of the integral ones, and the classes read on the connected components as in the
> Chern class statement.

```lean
theorem lciGysinClass_completedCap_chernCharacterOfModule_cap
    (hY : HasDimensionDecomposition (relativeDimension C.dimensionFunction sY)) (p : ℕ) :
    haveI := LocallyOfFiniteType.isLocallyNoetherian sX
    haveI := LocallyOfFiniteType.isLocallyNoetherian sY
    haveI := isFiniteLocallyFree_pullback_of_isFiniteLocallyFree f E
    LinearMap.lTensor ℚ
        (completedCapHom C sX sY f hfs (lciGysinClass C sX sY f hfs hf F)).toIntLinearMap
        (LinearMap.lTensor ℚ
          (componentClassCapHom C sY p (componentFundamentalClass C sY)).toIntLinearMap
          (chernCharacterOfModule C sY E p)) =
      LinearMap.lTensor ℚ
        (componentClassCapHom C sX p (componentFundamentalClass C sX)).toIntLinearMap
        (chernCharacterOfModule C sX ((Scheme.Modules.pullback f).obj E) p)
```

**`Stacks.Chow.lciGysinCap_fundamentalChowClass_id_of_isVirtualNormalBundleClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/LciGysinCompositeFundamentalClass.lean, line 237](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/LciGysinCompositeFundamentalClass.lean#L237). The attribute's comment: “part (b): `f^![Y]_n = [X]_{n-(r-d)}` on `X` itself, from 0FF7 at `Y' = Y`. The 0FE3 conditions enter as the two δ-dimension bounds and the Cohen-Macaulay hypothesis as the vanishing excess `hcone`, exactly as in 0FF7's carrier; no clopen reduction”.

> **Stacks 0FF8 (b).** Let `f = i ≫ g` with `i : X ⟶ P` an immersion carrying a virtual normal
> bundle of constant rank `r` and `g : P ⟶ Y` smooth of constant relative dimension `d`, so that
> the Gysin map exists for `f` in the sense of Stacks 0FF3, and let `f^!` be the Gysin map, entering
> as a bivariant class `cf` characterized as `i^! ∘ g^*`. If `dim_δ(Y) ≤ n` and
> `dim_δ(X ×_P (P ×_Y Y)) ≤ n + d - r`, then
>
>   `f^![Y]_n = [X]_{n - (r - d)}`
>
> in the Chow group of `X` itself.
>
> This is `Stacks.Chow.lciGysinCap_fundamentalChowClass_of_isVirtualNormalBundleClass` — a special
> case of Stacks 0FF7 for a
> class `cf` characterized as `i^! ∘ g^*`, with constant ranks and the excess vanishing as the
> hypothesis `hcone`; the full Stacks 0FF7, for the constructed Gysin map `Stacks.Chow.lciGysinMap`,
> is `Stacks.Chow.completedCapFundamentalClass_completedBivariantRestriction_lciGysinMap` — at the
> test scheme `g' = 𝟙 Y`, followed by the identification of `X ×_Y Y` with `X`:
> the projection `pullback.fst f (𝟙 Y)` is an isomorphism, and pushforward along an isomorphism
> over the base carries a fundamental class to a fundamental class by
> `Stacks.Chow.chowPushforwardOfIso_fundamentalChowClass`.
>
> The hypotheses are those of
> `Stacks.Chow.lciGysinCap_fundamentalChowClass_of_isVirtualNormalBundleClass`, whose implementation
> notes say what each one is and why none of them is the conclusion; see also the implementation
> notes above for how the Cohen-Macaulay hypothesis and the conditions of Stacks 0FE3 enter.

```lean
theorem lciGysinCap_fundamentalChowClass_id_of_isVirtualNormalBundleClass
    {ci : BivariantClass C G sX sP i hi (r : ℤ)}
    (hci : IsVirtualNormalBundleClass C sX sP i hi G 𝒩 r ci)
    {cf : BivariantClass C G sX sY (i ≫ g) (comp_comp_structureMorphism_eq hi hg)
      ((r : ℤ) + -(d : ℤ))}
    (hcf : IsBivariantClassComposition C G sX sP sY i g hi hg hpp (r : ℤ) (-(d : ℤ)) ci
      cg cf)
    (n : ℤ) (hY : schemeDeltaDimension C (𝟙 Y ≫ sY) ≤ (n : EInt))
    (hX : schemeDeltaDimension C (pullback.fst i (pullback.fst g (𝟙 Y)) ≫ sX) ≤
      (((n + (d : ℤ)) - (r : ℤ) : ℤ) : EInt))
    (hcone : chowGroupDegreeEquiv C
        (pullback.fst (𝒩.projection ≫ i) (pullback.fst g (𝟙 Y)) ≫ 𝒩.projection ≫ sX)
        (by omega : (n + (d : ℤ)) - (0 : ℤ) = ((n + (d : ℤ)) - (r : ℤ)) + (r : ℤ))
        ((virtualNormalConeClass C sX sP i hi 𝒩).cap (pullback.fst g (𝟙 Y)) (n + (d : ℤ))
          (fundamentalChowClass C (pullback.fst g (𝟙 Y) ≫ sP) (n + (d : ℤ)))) =
      fundamentalChowClass C
        (pullback.fst (𝒩.projection ≫ i) (pullback.fst g (𝟙 Y)) ≫ 𝒩.projection ≫ sX)
        (((n + (d : ℤ)) - (r : ℤ)) + (r : ℤ))) :
    chowPushforwardOfIso C (pullback.fst (i ≫ g) (𝟙 Y) ≫ sX) sX
        (pullback.fst (i ≫ g) (𝟙 Y)) rfl (n - ((r : ℤ) + -(d : ℤ)))
        (cf.cap (𝟙 Y) n
          (chowGroupCongr C (Category.id_comp sY).symm n (fundamentalChowClass C sY n))) =
      fundamentalChowClass C sX (n - ((r : ℤ) + -(d : ℤ)))
```

**`Stacks.Chow.lciGysinClass_completedCapDegreeZero_fundamentalClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/LciGysinFundamentalClassFormula.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/LciGysinFundamentalClassFormula.lean#L124). The attribute's comment: “second assertion: f^![Y] = [X] in CH^0(X) for X and Y satisfying the conditions of Tag 0FE3, with [X], [Y] the fundamental classes of Tag 0FE4 and f^! the Gysin map of Tag 0FF3; the source's example hypothesis that Y is Cohen-Macaulay is not needed”.

> **Stacks 0FF8 (b), `f^![Y] = [X]`.** Let `f : X ⟶ Y` be a local complete intersection morphism
> of schemes locally of finite type over `S` with Gysin map `f^! ∈ A^*(X ⟶ Y)^∧` of Stacks 0FF3
> (built from a factorization `F`), and let `X` and `Y` satisfy the equivalent conditions of
> Stacks 0FE3. Then
>
>   `f^![Y] = [X]`   in `CH^0(X) = ∏_n CH_n(X_n)`,
>
> with `[X] = ∑_n [X_n]_n` and `[Y]` the fundamental classes of Stacks 0FE4 and `f^! ∩ -` the cap
> product of the completed class on `CH^0` (`Stacks.Chow.completedCapDegreeZero`).
>
> The source adds "for example if `Y` is Cohen–Macaulay"; that is only a sufficient condition for
> the hypothesis of Stacks 0FE3 on `Y`, which is all that is assumed here. The hypothesis on `X`
> enters only to write `[X]` as an element of `CH^0(X)`: the identity of the classes on the
> connected components, `Stacks.Chow.lciGysinClass_completedCap_componentFundamentalClass`, needs
> the hypothesis on `Y` alone.

```lean
theorem lciGysinClass_completedCapDegreeZero_fundamentalClass
    (hX : HasDimensionDecomposition (relativeDimension C.dimensionFunction sX))
    (hY : HasDimensionDecomposition (relativeDimension C.dimensionFunction sY)) :
    haveI := LocallyOfFiniteType.isLocallyNoetherian sX
    haveI := LocallyOfFiniteType.isLocallyNoetherian sY
    completedCapDegreeZero C sX hX sY f hfs hY (lciGysinClass C sX sY f hfs hf F)
        (fundamentalClass C sY hY) =
      fundamentalClass C sX hX
```

## Tag 0FV9, a lemma

[Tag 0FV9](https://stacks.math.columbia.edu/tag/0FV9) in the Stacks Project.

**`Stacks.Chow.completedBivariantTransport_completedBivariantRestriction_lciGysinMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/BaseChangeExcessFormula.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/BaseChangeExcessFormula.lean#L193). The attribute's comment: “the whole lemma: for a cartesian square of schemes locally of finite type over S with f, f' local complete intersection morphisms and the Gysin map existing for f, the kernel C of H^{-1}((g')^*NL_{X/Y}) → H^{-1}(NL_{X'/Y'}) is finite locally free, the Gysin map exists for f', and res(f^!) = c_top(C^∨) ∘ (f')^! in A^*(X' → Y')^∧”.

> Let `g' ≫ f = f' ≫ g` be a cartesian square of schemes locally of finite type over the base,
> with `f` and `f'` local complete intersection morphisms and the Gysin map of Stacks 0FF3 existing
> for `f`. Then the sheaf
>
>   `𝒞 = Ker(H^{-1}((g')^*NL_{X/Y}) ⟶ H^{-1}(NL_{X'/Y'}))`,
>
> for the base change map of Stacks 0FV5, is a finite locally free `𝒪_{X'}`-module, the Gysin map
> exists for `f'`, and
>
>   `res(f^!) = c_top(𝒞^∨) ∘ (f')^!`   in `A^*(X' ⟶ Y')^∧`,
>
> for the Gysin maps of Stacks 0FF3, the restriction of Stacks 0F9Z (carried from the chosen fibre
> product `X ×_Y Y'` to `X'` along the canonical isomorphism), the top Chern class of Stacks 0FA4
> and the composition of Stacks 0FE0 (a class for `𝟙 ≫ f'`).

```lean
theorem completedBivariantTransport_completedBivariantRestriction_lciGysinMap
    (hlf : IsLocalCompleteIntersectionMorphism f) (hlf' : IsLocalCompleteIntersectionMorphism f')
    (hG : GysinMapExists f) :
    ∃ hC : AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u}
        (kernel (HomologicalComplex.homologyMap
          (Stacks.NaiveCotangentFlatBaseChange.baseChangeMapOfComparison f f' g'
            (AlgebraicGeometry.BaseChangeStalk.baseRingComparison f f' g' g hsq.w)
            (AlgebraicGeometry.BaseChangeStalk.baseRingComparison_comp f f' g' g hsq.w)) (-1))),
      ∃ hG' : GysinMapExists f',
        haveI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian sX
        haveI : IsLocallyNoetherian Y := LocallyOfFiniteType.isLocallyNoetherian sY
        haveI : IsLocallyNoetherian X' := LocallyOfFiniteType.isLocallyNoetherian sX'
        haveI : IsLocallyNoetherian Y' := LocallyOfFiniteType.isLocallyNoetherian (g ≫ sY)
        haveI : IsLocallyNoetherian (pullback f g) :=
          LocallyOfFiniteType.isLocallyNoetherian (pullback.fst f g ≫ sX)
        haveI : SheafOfModules.IsFiniteLocallyFree.{u, u, u} (dualSheaf (kernel
            (HomologicalComplex.homologyMap
              (Stacks.NaiveCotangentFlatBaseChange.baseChangeMapOfComparison f f' g'
                (AlgebraicGeometry.BaseChangeStalk.baseRingComparison f f' g' g hsq.w)
                (AlgebraicGeometry.BaseChangeStalk.baseRingComparison_comp f f' g' g hsq.w))
              (-1)))) :=
          isFiniteLocallyFree_dualSheaf_of_schemeOpens _ hC
        completedBivariantTransport C (pullback.fst f g ≫ sX) sX' (g ≫ sY) (pullback.snd f g)
            (pullbackSnd_comp_structureMorphism_eq C sX sY f hf g) f' hf' hsq.isoPullback.symm
            hsq.isoPullback_inv_snd
            (completedBivariantRestrictionViaSequence C sX sY f hf g
              (lciGysinMap C sX sY hf hlf hG)) =
          completedBivariantGroup.copy C (Category.id_comp f') _ hf'
            (completedBivariantCompositeOfInvertible C sX' sX' (g ≫ sY) (𝟙 X') f'
              (Category.id_comp sX') hf'
              (topChernClassOfInvertible C sX' (dualSheaf (kernel (HomologicalComplex.homologyMap
                (Stacks.NaiveCotangentFlatBaseChange.baseChangeMapOfComparison f f' g'
                  (AlgebraicGeometry.BaseChangeStalk.baseRingComparison f f' g' g hsq.w)
                  (AlgebraicGeometry.BaseChangeStalk.baseRingComparison_comp f f' g' g hsq.w))
                (-1)))))
              (lciGysinMap C sX' (g ≫ sY) hf' hlf' hG'))
```

## Tag 0FVA, a lemma

[Tag 0FVA](https://stacks.math.columbia.edu/tag/0FVA) in the Stacks Project.

**`Stacks.Chow.completedBivariantRestriction_lciGysinMap_blowUpToBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/BlowupFormula.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/BlowupFormula.lean#L90). The attribute's comment: “the whole lemma: for a regular closed immersion i : Z → X of schemes locally of finite type over S, the blowing up b : X' → X with centre Z, E = X' ×_X Z with π : E → Z, and the Gysin map existing for b, res(b^!) = c_top(F^∨) ∘ π^* in A^*(E → Z)^∧, F the kernel of π^*C_{Z/X} → C_{E/X'}”.

> **The blow up formula.** Let `i : Z ⟶ X` be a regular closed immersion of schemes locally of
> finite type over the base, `b : X' ⟶ X` the blowing up of `X` with centre `Z`, and `E = X' ×_X Z`
> with `j : E ⟶ X'` and `π : E ⟶ Z`. Assume that the Gysin map of Stacks 0FF3 exists for `b` (a local
> complete intersection morphism, Stacks 0BIQ). Then
>
>   `res(b^!) = c_top(𝓕^∨) ∘ π^*`   in `A^*(E ⟶ Z)^∧`,
>
> where `𝓕` is the kernel of the canonical map `π^*𝒞_{Z/X} ⟶ 𝒞_{E/X'}` (finite locally free,
> `Stacks.Chow.isFiniteLocallyFree_blowupExcessConormal`), `res` is the restriction of Stacks 0F9Z
> along `i`, `c_top` the top Chern class of Stacks 0FA4, `π^*` the flat pullback of the smooth
> morphism `π` and the composition that of Stacks 0FE0 (a class for `𝟙 ≫ π`).

```lean
theorem completedBivariantRestriction_lciGysinMap_blowUpToBase (hi : IsRegularImmersion i)
    (sX : X ⟶ C.S) [LocallyOfFiniteType sX]
    (hG : GysinMapExists (Stacks.Blowup.blowUpToBase i.ker)) :
    haveI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian sX
    haveI := Stacks.Blowup.smooth_pullbackSnd_blowUpToBase i hi
    haveI : IsLocallyNoetherian Z := LocallyOfFiniteType.isLocallyNoetherian (i ≫ sX)
    haveI : IsLocallyNoetherian (Stacks.Blowup.blowUp i.ker) :=
      LocallyOfFiniteType.isLocallyNoetherian (Stacks.Blowup.blowUpToBase i.ker ≫ sX)
    haveI : IsLocallyNoetherian (pullback (Stacks.Blowup.blowUpToBase i.ker) i) :=
      LocallyOfFiniteType.isLocallyNoetherian (pullback.fst (Stacks.Blowup.blowUpToBase i.ker) i ≫
        Stacks.Blowup.blowUpToBase i.ker ≫ sX)
    haveI : SheafOfModules.IsFiniteLocallyFree.{u, u, u} (blowupExcessConormal i) :=
      isFiniteLocallyFree_blowupExcessConormal i hi hG
    haveI : SheafOfModules.IsFiniteLocallyFree.{u, u, u} (dualSheaf (blowupExcessConormal i)) :=
      isFiniteLocallyFree_dualSheaf_of_schemeOpens _ inferInstance
    completedBivariantRestrictionViaSequence C (Stacks.Blowup.blowUpToBase i.ker ≫ sX) sX
        (Stacks.Blowup.blowUpToBase i.ker) rfl i
        (lciGysinMap C (Stacks.Blowup.blowUpToBase i.ker ≫ sX) sX rfl
          (Stacks.Blowup.isLocalCompleteIntersectionMorphism_blowUpToBase i hi) hG) =
      completedBivariantGroup.copy C (Category.id_comp (pullback.snd _ i)) _
        (pullbackSnd_comp_structureMorphism_eq C _ sX _ rfl i)
        (completedBivariantCompositeOfInvertible C
          (pullback.fst (Stacks.Blowup.blowUpToBase i.ker) i ≫
            Stacks.Blowup.blowUpToBase i.ker ≫ sX)
          (pullback.fst (Stacks.Blowup.blowUpToBase i.ker) i ≫
            Stacks.Blowup.blowUpToBase i.ker ≫ sX)
          (i ≫ sX) (𝟙 _) (pullback.snd (Stacks.Blowup.blowUpToBase i.ker) i) (Category.id_comp _)
          (pullbackSnd_comp_structureMorphism_eq C _ sX _ rfl i)
          (topChernClassOfInvertible C _ (dualSheaf (blowupExcessConormal i)))
          (completedFlatPullbackOfSmooth C _ (i ≫ sX)
            (pullback.snd (Stacks.Blowup.blowUpToBase i.ker) i)
            (pullbackSnd_comp_structureMorphism_eq C _ sX _ rfl i)))
```

## Tag 0FF9, a lemma

[Tag 0FF9](https://stacks.math.columbia.edu/tag/0FF9) in the Stacks Project.

**`Stacks.Chow.isLocalCompleteIntersectionMorphism_and_lciGysinRational_rationalIntersectionProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalIntersection/RationalIntersectionProduct.lean, line 513](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RationalIntersection/RationalIntersectionProduct.lean#L513). The attribute's comment: “the whole lemma: for f : X → Y over S with X, Y quasi-compact, regular, of finite dimension, with affine diagonal, f is a local complete intersection morphism, and if the Gysin map of f exists then f^!(α · β) = f^!α · f^!β for the products of 0FEX on CH^*(-) ⊗ Q = CH_*(-) ⊗ Q”.

> **Stacks Project, Tag 0FF9.** Let `(S, δ)` be as in Situation 42.7.1 and let `f : X ⟶ Y` be a
> morphism of schemes locally of finite type over `S` such that both `X` and `Y` are quasi-compact,
> regular, have affine diagonal, and finite dimension. Then `f` is a local complete intersection
> morphism, and if moreover the Gysin map exists for `f`, then
>
>   `f^!(α · β) = f^!α · f^!β`
>
> for the intersection products of Section 0FEX, on `CH^*(-) ⊗ 𝐐 = CH_*(-) ⊗ 𝐐`.

```lean
theorem isLocalCompleteIntersectionMorphism_and_lciGysinRational_rationalIntersectionProduct
    [CompactSpace X] [CompactSpace Y] (hXreg : IsRegular X) (hYreg : IsRegular Y)
    (hXdim : topologicalKrullDim X ≠ ⊤) (hYdim : topologicalKrullDim Y ≠ ⊤) :
    IsLocalCompleteIntersectionMorphism f ∧
      ∀ (h : GysinMapExists f) (α β : DirectSum ℤ fun j : ℤ => ℚ ⊗[ℤ] chowGroup C sY j),
        haveI := isNoetherian_of_compactSpace sX
        haveI := isNoetherian_of_compactSpace sY
        haveI := locallyOfFiniteType_of_comp_eq hf
        lciGysinRational C sX sY hf
            (isLocalCompleteIntersectionMorphism_of_comp_eq_of_isRegular hf hXreg hYreg) h
            (rationalIntersectionProduct hYreg (exists_bounds_relativeDimension C sY hYdim) α β) =
          rationalIntersectionProduct hXreg (exists_bounds_relativeDimension C sX hXdim)
            (lciGysinRational C sX sY hf
              (isLocalCompleteIntersectionMorphism_of_comp_eq_of_isRegular hf hXreg hYreg) h α)
            (lciGysinRational C sX sY hf
              (isLocalCompleteIntersectionMorphism_of_comp_eq_of_isRegular hf hXreg hYreg) h
              β)
```

## Tag 0FFA, a lemma

[Tag 0FFA](https://stacks.math.columbia.edu/tag/0FFA) in the Stacks Project.

**`Stacks.Chow.isLocalCompleteIntersectionMorphism_and_projectionFormula_rationalIntersection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalIntersection/RationalIntersectionProduct.lean, line 581](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RationalIntersection/RationalIntersectionProduct.lean#L581). The attribute's comment: “the whole lemma: for f : X → Y over S with X, Y quasi-compact, regular, of finite dimension, with affine diagonal, f is a local complete intersection morphism, and if the Gysin map of f exists and f is proper then f_*(α · f^!β) = f_*α · β for the products of 0FEX on CH^*(-) ⊗ Q = CH_*(-) ⊗ Q”.

> **Stacks Project, Tag 0FFA.** Let `(S, δ)` be as in Situation 42.7.1 and let `f : X ⟶ Y` be a
> morphism of schemes locally of finite type over `S` such that both `X` and `Y` are quasi-compact,
> regular, have affine diagonal, and finite dimension. Then `f` is a local complete intersection
> morphism, and if moreover the Gysin map exists for `f` and `f` is proper, then
>
>   `f_*(α · f^!β) = f_*α · β`
>
> for the intersection products of Section 0FEX, on `CH^*(-) ⊗ 𝐐 = CH_*(-) ⊗ 𝐐`.

```lean
theorem isLocalCompleteIntersectionMorphism_and_projectionFormula_rationalIntersection
    [CompactSpace X] [CompactSpace Y] (hXreg : IsRegular X) (hYreg : IsRegular Y)
    (hXdim : topologicalKrullDim X ≠ ⊤) (hYdim : topologicalKrullDim Y ≠ ⊤) :
    IsLocalCompleteIntersectionMorphism f ∧
      ∀ [IsProper f] (h : GysinMapExists f)
        (α : DirectSum ℤ fun j : ℤ => ℚ ⊗[ℤ] chowGroup C sX j)
        (β : DirectSum ℤ fun j : ℤ => ℚ ⊗[ℤ] chowGroup C sY j),
        haveI := isNoetherian_of_compactSpace sX
        haveI := isNoetherian_of_compactSpace sY
        rationalProperChowPushforward C sX sY hf
            (rationalIntersectionProduct hXreg (exists_bounds_relativeDimension C sX hXdim) α
              (lciGysinRational C sX sY hf
                (isLocalCompleteIntersectionMorphism_of_comp_eq_of_isRegular hf hXreg hYreg) h
                β)) =
          rationalIntersectionProduct hYreg (exists_bounds_relativeDimension C sY hYdim)
            (rationalProperChowPushforward C sX sY hf α) β
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.59, Tag 0FEZ](https://stacks.math.columbia.edu/tag/0FEZ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
