---
declaration: section
origin: cited
lean: CategoryTheory.Functor.Stackification.isFiberedInGroupoids_of_isStackification, CategoryTheory.Functor.Stackification.isStackInGroupoids_of_isStackification, CategoryTheory.Functor.Stackification.nonempty_isEquivalenceOver_of_locally_fullyFaithful, CategoryTheory.Functor.Stackification.nonempty_isEquivalenceOver_extend, CategoryTheory.Functor.Stackification.extendGroupoid, CategoryTheory.Functor.Stackification.extendGroupoid_comp_eq, CategoryTheory.Functor.Stackification.unitGroupoid, CategoryTheory.Functor.Stackification.isHomLift_unitGroupoid_app
statement: formalized
proof: formalized
---

# 8.9 Stackification of categories fibred in groupoids

Section 8.9 of the Stacks Project, [Tag 02ZO](https://stacks.math.columbia.edu/tag/02ZO). 3 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02ZP, a lemma

[Tag 02ZP](https://stacks.math.columbia.edu/tag/02ZP) in the Stacks Project.

**`CategoryTheory.Functor.Stackification.isFiberedInGroupoids_of_isStackification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stackification/GroupoidStackification.lean, line 255](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Stackification/GroupoidStackification.lean#L255).

> **Stacks 02ZP.** Let `(𝒞, J)` be a site, let `p : 𝒮 ⥤ 𝒞` be a category fibred in groupoids and
> let `G : 𝒮 ⥤ 𝒮'` exhibit the stack `p' : 𝒮' ⥤ 𝒞` as the stackification of the fibred category
> underlying `𝒮` — that is, let `G` be a 1-morphism of fibred categories over `𝒞` satisfying the two
> clauses of Stacks 02ZN. Then `p'` is fibred in groupoids.
>
> This is the whole content of Stacks 02ZP over Stacks 02ZN: the source runs the same construction
> and observes that it lands in groupoid fibres. The statement is conditional on being given the
> stackification, the construction of Stacks 02ZN not being assembled in the tree yet; once it is,
> it supplies `hsp'`, `hG`, `hmor` and `hobj`.
>
> By Stacks 003V it suffices that every fibre of `𝒮'` be a groupoid, which is
> `CategoryTheory.Functor.Stackification.isGroupoid_fiber`.

```lean
theorem isFiberedInGroupoids_of_isStackification : p'.IsFiberedInGroupoids
```

**`CategoryTheory.Functor.Stackification.isStackInGroupoids_of_isStackification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stackification/GroupoidStackification.lean, line 267](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Stackification/GroupoidStackification.lean#L267).

> **Stacks 02ZP, as the source states it: `𝒮'` is a stack in groupoids.** The `IsStack` half is
> the hypothesis `hsp'` and the `IsFiberedInGroupoids` half is
> `CategoryTheory.Functor.Stackification.isFiberedInGroupoids_of_isStackification`; together with
> `hmor` and `hobj`, which are the two clauses of the source's statement carried unchanged from
> hypothesis to conclusion, this says that the given `G` exhibits `𝒮'` as the stackification of `𝒮`
> *in groupoids*.

```lean
theorem isStackInGroupoids_of_isStackification :
    p'.IsFiberedInGroupoids ∧ p'.IsStack J
```

**`CategoryTheory.Functor.Stackification.nonempty_isEquivalenceOver_of_locally_fullyFaithful`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stackification/Uniqueness.lean, line 161](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Stackification/Uniqueness.lean#L161). The attribute's comment: “the determinacy half of the statement — `𝒮'` is determined up to 2-isomorphism by clauses (1) and (2) — read as: a 1-morphism from a stackification into a stack whose composite with the stackification again satisfies the two clauses is an equivalence over the site. The existence half is the construction of Stacks 02ZN, not assembled in the tree; the uniqueness of the 2-isomorphism is Stacks 04W9, `CategoryTheory.Functor.Stackification.restrict_isEquivalence`; and the groupoid half of 02ZP is `CategoryTheory.Functor.Stackification.isStackInGroupoids_of_isStackification`”.

> **The determinacy clause of Stacks 02ZN and 02ZP, in the form a consumer uses.** Let
> `G : 𝒜 ⥤ ℬ` exhibit the stack `p'` as the stackification of the fibred category `p` — that is, let
> it satisfy the two clauses `hGmor` and `hGobj` — and let `H : ℬ ⥤ 𝒳` be a 1-morphism of fibred
> categories into a stack `q`. If the composite `G ⋙ H` satisfies the same two clauses, then `H` is
> an equivalence of `p'` with `q` over `𝒞`.
>
> So two stackifications of one fibred category have equivalent targets, and the comparison realising
> the equivalence is any 1-morphism between them compatible with the two presentations. The two
> clauses, which for a given stackification are hypotheses carried to the conclusion by
> `CategoryTheory.Functor.Stackification.isStackInGroupoids_of_isStackification`, thereby become a
> *criterion* on `G ⋙ H`.
>
> `H` is fully faithful by `CategoryTheory.Functor.Stackification.full_of_extension` and
> `.faithful_of_extension`, Stacks 04WQ for a 1-morphism out of a stackification, whose hypotheses
> are precisely the clauses on `G` and on the composite. It is locally essentially surjective on
> fibres because `G ⋙ H` is, a local preimage under the composite being one under `H`. Stacks 046N,
> `CategoryTheory.Functor.isEquivalenceOver_iff_locallyEssSurjOnFibers`, then concludes.

```lean
theorem nonempty_isEquivalenceOver_of_locally_fullyFaithful :
    Nonempty (IsEquivalenceOver p' q H)
```

**`CategoryTheory.Functor.Stackification.nonempty_isEquivalenceOver_extend`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stackification/Uniqueness.lean, line 265](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Stackification/Uniqueness.lean#L265). The attribute's comment: “the determinacy half of the statement — `𝒮'` is determined up to 2-isomorphism by clauses (1) and (2) — for the canonical extension: a 1-morphism into a stack satisfying the two clauses exhibits that stack as the stackification, so the extension of Stacks 0435 is an equivalence over the site. The existence half is the construction of Stacks 02ZN, not assembled in the tree; the uniqueness of the 2-isomorphism is Stacks 04W9, `CategoryTheory.Functor.Stackification.restrict_isEquivalence`; and the groupoid half of 02ZP is `CategoryTheory.Functor.Stackification.isStackInGroupoids_of_isStackification`”.

> **A stackification is determined up to 2-isomorphism: the "moreover" of Stacks 02ZN, repeated
> by Stacks 02ZP.** Let `G : 𝒜 ⥤ ℬ` exhibit the stack `p'` as the stackification of the fibred
> category `p`, and let `F : 𝒜 ⥤ 𝒳` be a 1-morphism into a stack `q` satisfying the same two
> clauses — `hFmor`, that the induced maps of morphism presheaves are locally bijective, and
> `hFobj`, that every object of a fibre of `q` is locally in the essential image of `F` on fibres.
> Then the extension of `F` along `G` supplied by the universal property, Stacks 0435, is an
> equivalence of `p'` with `q` over `𝒞`.
>
> So a 1-morphism satisfying the two clauses does not merely land in *a* stack: it exhibits its
> target as *the* stackification. The extension is compatible with the two presentations by
> `CategoryTheory.Functor.Stackification.unit`, which is the 2-isomorphism `G ⋙ H ≅ F`, so the
> equivalence identifies the two presentations and not just the two targets.

```lean
theorem nonempty_isEquivalenceOver_extend :
    Nonempty (IsEquivalenceOver p' q
      (extend hG hF hGmor hq.isMorSheaf hGobj hq.hasEffectiveDescent))
```

## Tag 0436, a lemma

[Tag 0436](https://stacks.math.columbia.edu/tag/0436) in the Stacks Project.

**`CategoryTheory.Functor.Stackification.extendGroupoid`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stackification/UniversalPropertyGroupoid.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Stackification/UniversalPropertyGroupoid.lean#L81).

> Let `(𝒞, J)` be a site, let `p : 𝒮 ⥤ 𝒞` be a category fibred in groupoids, let `G : 𝒮 ⥤ 𝒮'`
> exhibit the stack in groupoids `p'` as the stackification of `𝒮`, and let `F : 𝒮 ⥤ 𝒳` be a
> 1-morphism of categories over `𝒞` into a stack in groupoids. This is the extension `H : 𝒮' ⥤ 𝒳`
> of `F` along `G`.

```lean
noncomputable def extendGroupoid : 𝒮' ⥤ 𝒳
```

**`CategoryTheory.Functor.Stackification.extendGroupoid_comp_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stackification/UniversalPropertyGroupoid.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Stackification/UniversalPropertyGroupoid.lean#L90).

> The extension `H : 𝒮' ⥤ 𝒳` is strictly over `𝒞`: `H ⋙ q = p'`.

```lean
theorem extendGroupoid_comp_eq :
    extendGroupoid hp hp' hsp' hq hsq hG hF hmor hobj ⋙ q = p'
```

**`CategoryTheory.Functor.Stackification.unitGroupoid`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stackification/UniversalPropertyGroupoid.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Stackification/UniversalPropertyGroupoid.lean#L107).

> The 2-isomorphism `G ⋙ H ≅ F` between `F` and the composite of `G` with its extension.

```lean
noncomputable def unitGroupoid :
    G ⋙ extendGroupoid hp hp' hsp' hq hsq hG hF hmor hobj ≅ F
```

**`CategoryTheory.Functor.Stackification.isHomLift_unitGroupoid_app`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stackification/UniversalPropertyGroupoid.lean, line 117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Stackification/UniversalPropertyGroupoid.lean#L117).

> Every component of the 2-isomorphism `G ⋙ H ≅ F` lies over an identity morphism of `𝒞`.

```lean
lemma isHomLift_unitGroupoid_app (A : 𝒮) :
    q.IsHomLift (𝟙 (p.obj A)) ((unitGroupoid hp hp' hsp' hq hsq hG hF hmor hobj).hom.app A)
```

## Tag 04Y2, a lemma

[Tag 04Y2](https://stacks.math.columbia.edu/tag/04Y2) in the Stacks Project.

**`CategoryTheory.TwoFibreProductOver.isStackification_of_isStackification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stackification/TwoFibreProductGroupoid/IsStackification.lean, line 353](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Stackification/TwoFibreProductGroupoid/IsStackification.lean#L353).

> **Stacks 04Y2.** Let `(𝒞, J)` be a site, let `f : 𝒳 ⥤ 𝒴` and `g : 𝒵 ⥤ 𝒴` be 1-morphisms of
> categories fibred in groupoids over `𝒞`, let `i : 𝒳 ⥤ 𝒳'`, `j : 𝒴 ⥤ 𝒴'`, `k : 𝒵 ⥤ 𝒵'` be
> stackifications (Stacks 02ZP: the targets are stacks in groupoids, the induced maps
> `Mor(x, y) ⟶ Mor(i x, i y)` of presheaves on `𝒞/U` are locally bijective, and every object of the
> target is locally in the essential image), and let `f' : 𝒳' ⥤ 𝒴'`, `g' : 𝒵' ⥤ 𝒴'` be 1-morphisms
> over `𝒞` 2-commuting with `f` and `g` along `i`, `j`, `k` via vertical 2-isomorphisms `α`, `β`.
> Then the stackification of the 2-fibre product is the 2-fibre product of the stackifications: the
> 2-fibre product `𝒳' ×_{𝒴'} 𝒵'` is a stack over `(𝒞, J)` — a stack in groupoids, being fibred in
> groupoids by Stacks 0041 — and every canonical 1-morphism `H : 𝒳 ×_𝒴 𝒵 ⥤ 𝒳' ×_{𝒴'} 𝒵'`, that is
> every morphism of the two 2-commutative squares, is a 1-morphism of fibred categories over `𝒞`
> which is a stackification of `𝒳 ×_𝒴 𝒵`, in the same two clauses.

```lean
public theorem isStackification_of_isStackification {J : GrothendieckTopology 𝒞} {p𝒳 : 𝒳 ⥤ 𝒞}
    {p𝒴 : 𝒴 ⥤ 𝒞} {p𝒵 : 𝒵 ⥤ 𝒞} {p𝒳' : 𝒳' ⥤ 𝒞} {p𝒴' : 𝒴' ⥤ 𝒞} {p𝒵' : 𝒵' ⥤ 𝒞}
    (h𝒳 : p𝒳.IsFiberedInGroupoids) (h𝒴 : p𝒴.IsFiberedInGroupoids) (h𝒵 : p𝒵.IsFiberedInGroupoids)
    (h𝒳' : p𝒳'.IsFiberedInGroupoids) (h𝒴' : p𝒴'.IsFiberedInGroupoids)
    (h𝒵' : p𝒵'.IsFiberedInGroupoids) (hs𝒳' : p𝒳'.IsStack J) (hs𝒴' : p𝒴'.IsStack J)
    (hs𝒵' : p𝒵'.IsStack J) {f : 𝒳 ⥤ 𝒴} {g : 𝒵 ⥤ 𝒴} (hf : f ⋙ p𝒴 = p𝒳) (hg : g ⋙ p𝒴 = p𝒵)
    {f' : 𝒳' ⥤ 𝒴'} {g' : 𝒵' ⥤ 𝒴'} (hf' : f' ⋙ p𝒴' = p𝒳') (hg' : g' ⋙ p𝒴' = p𝒵') {i : 𝒳 ⥤ 𝒳'}
    {j : 𝒴 ⥤ 𝒴'} {k : 𝒵 ⥤ 𝒵'} (hi : i ⋙ p𝒳' = p𝒳) (hj : j ⋙ p𝒴' = p𝒴) (hk : k ⋙ p𝒵' = p𝒵)
    (hmor𝒳 :
      haveI : p𝒳.IsFibered := h𝒳.isFibered
      haveI : p𝒳'.IsFibered := h𝒳'.isFibered
      ∀ (U : 𝒞) (x₁ x₂ : p𝒳.Fiber U),
        Presheaf.IsLocallyInjective (J.over U)
            ((h𝒳'.isFibredOneMorphism hi).morPresheafMap x₁ x₂) ∧
          Presheaf.IsLocallySurjective (J.over U)
            ((h𝒳'.isFibredOneMorphism hi).morPresheafMap x₁ x₂))
    (hobj𝒳 :
      ∀ x' : 𝒳',
        ∃ R ∈ J (p𝒳'.obj x'),
          ∀ ⦃V : 𝒞⦄ (u : V ⟶ p𝒳'.obj x'),
            R u → ∃ (x : 𝒳) (φ : i.obj x ⟶ x'), p𝒳'.IsStronglyCartesian u φ)
    (hmor𝒴 :
      haveI : p𝒴.IsFibered := h𝒴.isFibered
      haveI : p𝒴'.IsFibered := h𝒴'.isFibered
      ∀ (U : 𝒞) (y₁ y₂ : p𝒴.Fiber U),
        Presheaf.IsLocallyInjective (J.over U)
            ((h𝒴'.isFibredOneMorphism hj).morPresheafMap y₁ y₂) ∧
          Presheaf.IsLocallySurjective (J.over U)
            ((h𝒴'.isFibredOneMorphism hj).morPresheafMap y₁ y₂))
    (_hobj𝒴 :
      ∀ y' : 𝒴',
        ∃ R ∈ J (p𝒴'.obj y'),
          ∀ ⦃V : 𝒞⦄ (u : V ⟶ p𝒴'.obj y'),
            R u → ∃ (y : 𝒴) (φ : j.obj y ⟶ y'), p𝒴'.IsStronglyCartesian u φ)
    (hmor𝒵 :
      haveI : p𝒵.IsFibered := h𝒵.isFibered
      haveI : p𝒵'.IsFibered := h𝒵'.isFibered
      ∀ (U : 𝒞) (z₁ z₂ : p𝒵.Fiber U),
        Presheaf.IsLocallyInjective (J.over U)
            ((h𝒵'.isFibredOneMorphism hk).morPresheafMap z₁ z₂) ∧
          Presheaf.IsLocallySurjective (J.over U)
            ((h𝒵'.isFibredOneMorphism hk).morPresheafMap z₁ z₂))
    (hobj𝒵 :
      ∀ z' : 𝒵',
        ∃ R ∈ J (p𝒵'.obj z'),
          ∀ ⦃V : 𝒞⦄ (u : V ⟶ p𝒵'.obj z'),
            R u → ∃ (z : 𝒵) (φ : k.obj z ⟶ z'), p𝒵'.IsStronglyCartesian u φ)
    (α : i ⋙ f' ≅ f ⋙ j) (hα : ∀ x : 𝒳, p𝒴'.IsHomLift (𝟙 (p𝒳.obj x)) (α.hom.app x))
    (β : k ⋙ g' ≅ g ⋙ j) (hβ : ∀ z : 𝒵, p𝒴'.IsHomLift (𝟙 (p𝒵.obj z)) (β.hom.app z))
    {H : TwoFibreProductOver p𝒳 p𝒵 p𝒴 f g ⥤ TwoFibreProductOver p𝒳' p𝒵' p𝒴' f' g'}
    (γ : H ⋙ fst p𝒳' p𝒵' p𝒴' f' g' ≅ fst p𝒳 p𝒵 p𝒴 f g ⋙ i)
    (hγ : ∀ P : TwoFibreProductOver p𝒳 p𝒵 p𝒴 f g, p𝒳'.IsHomLift (𝟙 P.base) (γ.hom.app P))
    (δ : H ⋙ snd p𝒳' p𝒵' p𝒴' f' g' ≅ snd p𝒳 p𝒵 p𝒴 f g ⋙ k)
    (hδ : ∀ P : TwoFibreProductOver p𝒳 p𝒵 p𝒴 f g, p𝒵'.IsHomLift (𝟙 P.base) (δ.hom.app P))
    (hψ :
      Functor.whiskerLeft H (psi p𝒳' p𝒵' p𝒴' f' g') ≫ Functor.whiskerRight δ.hom g' =
        Functor.whiskerRight γ.hom f' ≫
          Functor.whiskerLeft (fst p𝒳 p𝒵 p𝒴 f g) α.hom ≫
          Functor.whiskerRight (psi p𝒳 p𝒵 p𝒴 f g) j ≫
          Functor.whiskerLeft (snd p𝒳 p𝒵 p𝒴 f g) β.inv) :
    haveI : (structureFunctor p𝒳 p𝒵 p𝒴 f g).IsFibered :=
      (isFiberedInGroupoids p𝒳 p𝒵 p𝒴 f g h𝒳 h𝒵 h𝒴 hf hg).isFibered
    haveI : (structureFunctor p𝒳' p𝒵' p𝒴' f' g').IsFibered :=
      (isFiberedInGroupoids p𝒳' p𝒵' p𝒴' f' g' h𝒳' h𝒵' h𝒴' hf' hg').isFibered
    (structureFunctor p𝒳' p𝒵' p𝒴' f' g').IsStack J ∧
      ∃ hH :
        Functor.IsFibredOneMorphism (structureFunctor p𝒳 p𝒵 p𝒴 f g)
          (structureFunctor p𝒳' p𝒵' p𝒴' f' g') H,
        (∀ (U : 𝒞) (P Q : (structureFunctor p𝒳 p𝒵 p𝒴 f g).Fiber U),
            Presheaf.IsLocallyInjective (J.over U) (hH.morPresheafMap P Q) ∧
              Presheaf.IsLocallySurjective (J.over U) (hH.morPresheafMap P Q)) ∧
          ∀ P' : TwoFibreProductOver p𝒳' p𝒵' p𝒴' f' g',
            ∃ R ∈ J P'.base,
              ∀ ⦃V : 𝒞⦄ (u : V ⟶ P'.base),
                R u →
                  ∃ (P : TwoFibreProductOver p𝒳 p𝒵 p𝒴 f g) (φ : H.obj P ⟶ P'),
                    (structureFunctor p𝒳' p𝒵' p𝒴' f' g').IsStronglyCartesian u φ
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 8.9, Tag 02ZO](https://stacks.math.columbia.edu/tag/02ZO)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
