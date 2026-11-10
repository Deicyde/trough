---
declaration: section
origin: cited
lean: AlgebraicGeometry.SmallEtale.fShriekModAdjunction, AlgebraicGeometry.SmallEtale.fUpperShriekModForgetIso, AlgebraicGeometry.SmallEtale.fShriekFunctor_isLeftAdjoint, AlgebraicGeometry.SmallEtale.fUpperShriekSkyscraperIso, AlgebraicGeometry.SmallEtale.fUpperShriekSkyscraperObjIso, AlgebraicGeometry.SmallEtale.etaleUpperShriekIsoRestriction, AlgebraicGeometry.SmallEtale.upperShriekCompIso, AlgebraicGeometry.SmallEtale.upperShriekCompIso_assoc
statement: formalized
proof: formalized
---

# 63.6 Upper shriek for locally quasi-finite morphisms

Section 63.6 of the Stacks Project, [Tag 0F58](https://stacks.math.columbia.edu/tag/0F58). 5 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0F59, a lemma

[Tag 0F59](https://stacks.math.columbia.edu/tag/0F59) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.fShriekModAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/ModuleUpperShriekQuasiFinite.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/ModuleUpperShriekQuasiFinite.lean#L71). The attribute's comment: “part (3), f\_! on étale sheaves of Λ-modules has a right adjoint f^!”.

> The direct image with compact support `f_!` of a locally quasi-finite morphism, on étale
> sheaves of `Λ`-modules, is left adjoint to the upper shriek `f^!` with coefficients in `Λ`.

```lean
public def fShriekModAdjunction :
    fShriekMod.{u, v, r} B Λ f ⊣ fUpperShriekMod.{u, v, r} B Λ f
```

**`AlgebraicGeometry.SmallEtale.fUpperShriekModForgetIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/ModuleUpperShriekQuasiFinite.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/ModuleUpperShriekQuasiFinite.lean#L87). The attribute's comment: “part (3), the Λ-linear f^! agrees with f^! on underlying abelian sheaves”.

> The upper shriek with coefficients in `Λ` agrees with the upper shriek of abelian étale
> sheaves on underlying abelian sheaves: the abelian sheaf underlying `f^!G` is `f^!` of the
> abelian sheaf underlying `G`.

```lean
public def fUpperShriekModForgetIso :
    fUpperShriekMod.{u, v, r} B Λ f ⋙ forgetModuleSheaf.{u, v, r} B X Λ ≅
      forgetModuleSheaf.{u, v, r} B Y Λ ⋙ fUpperShriekFunctor.{u, max v r} B f
```

**`AlgebraicGeometry.SmallEtale.fShriekFunctor_isLeftAdjoint`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/UpperShriekQuasiFinite.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/UpperShriekQuasiFinite.lean#L93). The attribute's comment: “part (1), f\_! on abelian étale sheaves has a right adjoint f^!”.

> **Stacks 0F59, part (1).** The direct image with compact support
> `f_! : Ab(X_étale) ⟶ Ab(Y_étale)` of a locally quasi-finite morphism of schemes has a right
> adjoint `f^! : Ab(Y_étale) ⟶ Ab(X_étale)`.

```lean
public instance fShriekFunctor_isLeftAdjoint :
    (fShriekFunctor.{u, v} B f).IsLeftAdjoint
```

**`AlgebraicGeometry.SmallEtale.fUpperShriekSkyscraperIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/UpperShriekSkyscraper.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/UpperShriekSkyscraper.lean#L57). The attribute's comment: “part (2), f^!(ȳ\_* A) ≅ ∏\_\{f(x̄) = ȳ} x̄\_* A, naturally in A”.

> **Stacks 0F59, part (2).** For a locally quasi-finite morphism `f : X ⟶ Y` and a geometric
> point `ȳ` of `Y`, the upper shriek of the skyscraper at `ȳ` is the product of the skyscrapers
> over the geometric points of `X` lying over `ȳ`: `f^!(ȳ_* A) ≅ ∏_{f(x̄) = ȳ} x̄_* A`, naturally
> in the abelian group `A`.

```lean
public def fUpperShriekSkyscraperIso :
    etaleSkyscraperFunctor B Y.obj Y.property s AddCommGrpCat.{max (u + 1) v} ⋙
        fUpperShriekFunctor.{u, v} B f ≅
      Adjunction.piFamily (fun x : GeometricFiberPoint B f s =>
        etaleSkyscraperFunctor B X.obj X.property (x.toGeometricPoint B f s)
          AddCommGrpCat.{max (u + 1) v})
```

**`AlgebraicGeometry.SmallEtale.fUpperShriekSkyscraperObjIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/UpperShriekSkyscraper.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/UpperShriekSkyscraper.lean#L74). The attribute's comment: “part (2), the formula at a given abelian group A”.

> **Stacks 0F59, part (2).** The value of the isomorphism at an abelian group `A`:
> `f^!(ȳ_* A) ≅ ∏_{f(x̄) = ȳ} x̄_* A`.

```lean
public def fUpperShriekSkyscraperObjIso (M : AddCommGrpCat.{max (u + 1) v}) :
    (fUpperShriekFunctor.{u, v} B f).obj
        (etaleSkyscraper B Y.obj Y.property s AddCommGrpCat.{max (u + 1) v} M) ≅
      ∏ᶜ fun x : GeometricFiberPoint B f s =>
        etaleSkyscraper B X.obj X.property (x.toGeometricPoint B f s)
          AddCommGrpCat.{max (u + 1) v} M
```

## Tag 0F5A, a lemma

[Tag 0F5A](https://stacks.math.columbia.edu/tag/0F5A) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.etaleUpperShriekIsoRestriction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/EtaleUpperShriekRestriction.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/EtaleUpperShriekRestriction.lean#L67). The attribute's comment: “j^! = j^\{-1} for an étale morphism”.

> **Stacks 0F5A.** For an étale morphism `j : U ⟶ X` the upper shriek `j^!` on abelian étale
> sheaves is the inverse image `j^{-1}`: both are right adjoint to `j_!`.

```lean
public def etaleUpperShriekIsoRestriction :
    fUpperShriekFunctor.{u, u + 1} B U.obj.hom ≅ abelianRestriction B X hX U
```

## Tag 0F5B, a lemma

[Tag 0F5B](https://stacks.math.columbia.edu/tag/0F5B) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.upperShriekCompIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/UpperShriekComposition.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/UpperShriekComposition.lean#L94). The attribute's comment: “the canonical isomorphism (g ∘ f)^! ≅ f^! ∘ g^!”.

> **Stacks 0F5B, the canonical isomorphism.** For composable locally quasi-finite morphisms
> `f : X ⟶ Y` and `g : Y ⟶ Z` there is a canonical isomorphism `(g ∘ f)^! ≅ f^! ∘ g^!` of upper
> shriek functors on abelian étale sheaves: the conjugate, under the adjunctions
> `(g ∘ f)_! ⊣ (g ∘ f)^!` and `g_! ∘ f_! ⊣ f^! ∘ g^!`, of the canonical isomorphism
> `(g ∘ f)_! ≅ g_! ∘ f_!` of Stacks 0F6T. The source assumes `f` and `g` separated; that
> hypothesis is not needed.

```lean
public def upperShriekCompIso :
    fUpperShriekFunctor.{u, v} B (f ≫ g) ≅
      fUpperShriekFunctor.{u, v} B g ⋙ fUpperShriekFunctor.{u, v} B f
```

**`AlgebraicGeometry.SmallEtale.upperShriekCompIso_assoc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/UpperShriekComposition.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/UpperShriekComposition.lean#L151). The attribute's comment: “the associativity square”.

> **Stacks 0F5B, the associativity square.** For locally quasi-finite morphisms
> `f : X ⟶ Y`, `g : Y ⟶ Z` and `h : Z ⟶ T` the two isomorphisms
> `(h ∘ g ∘ f)^! ≅ f^! ∘ g^! ∘ h^!` built from the composition isomorphisms of upper shriek agree:
> `(h ∘ g ∘ f)^! → f^! ∘ (h ∘ g)^! → f^! ∘ g^! ∘ h^!` equals
> `(h ∘ g ∘ f)^! → (g ∘ f)^! ∘ h^! → f^! ∘ g^! ∘ h^!`. The identification
> `(h ∘ (g ∘ f))^! = ((h ∘ g) ∘ f)^!` along the associativity of composition, and the
> associator of composition of functors, are written out. The source assumes `f` and `g`
> separated; that hypothesis is not needed.

```lean
public theorem upperShriekCompIso_assoc :
    eqToHom (fUpperShriekFunctor_congr.{u, v} B (Category.assoc f g h).symm) ≫
        (upperShriekCompIso.{u, v} B (f ≫ g) h).hom ≫
          whiskerLeft (fUpperShriekFunctor.{u, v} B h) (upperShriekCompIso.{u, v} B f g).hom =
      (upperShriekCompIso.{u, v} B f (g ≫ h)).hom ≫
        whiskerRight (upperShriekCompIso.{u, v} B g h).hom (fUpperShriekFunctor.{u, v} B f) ≫
          (associator (fUpperShriekFunctor.{u, v} B h) (fUpperShriekFunctor.{u, v} B g)
            (fUpperShriekFunctor.{u, v} B f)).hom
```

## Tag 0F5C, a lemma

[Tag 0F5C](https://stacks.math.columbia.edu/tag/0F5C) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.upperShriekCompIso_etaleUpperShriekIsoRestriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/EtaleUpperShriekComposition.lean, line 468](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/EtaleUpperShriekComposition.lean#L468). The attribute's comment: “(j ∘ j')^! = (j')^! ∘ j^! agrees with (j ∘ j')^\{-1} = (j')^\{-1} ∘ j^\{-1}”.

> **Stacks 0F5C.** Let `j : U ⟶ X` and `j' : V ⟶ U` be étale morphisms. The isomorphism
> `(j ∘ j')^! ≅ (j')^! ∘ j^!` of Stacks 0F5B and the isomorphism
> `(j ∘ j')^{-1} ≅ (j')^{-1} ∘ j^{-1}` of the inverse images agree via the isomorphisms
> `j^! ≅ j^{-1}` of Stacks 0F5A: the square
> `(j ∘ j')^! → (j')^! ∘ j^! → (j')^! ∘ j^{-1} → (j')^{-1} ∘ j^{-1}` equals
> `(j ∘ j')^! → (j ∘ j')^{-1} → (j')^{-1} ∘ j^{-1}`. Here `j` is an object `U` of the small étale
> site of `X`, `j'` an object `V` of the small étale site of `U`, and `j ∘ j'` is `V` viewed as an
> object of the small étale site of `X`, `AlgebraicGeometry.smallEtaleCompObject`.

```lean
public theorem upperShriekCompIso_etaleUpperShriekIsoRestriction :
    upperShriekCompIso.{u, u + 1} B V.obj.hom U.obj.hom ≪≫
        isoWhiskerRight (etaleUpperShriekIsoRestriction B X hX U)
          (fUpperShriekFunctor.{u, u + 1} B V.obj.hom) ≪≫
        isoWhiskerLeft (abelianRestriction B X hX U)
          (etaleUpperShriekIsoRestriction B U.obj.left.1 U.obj.left.property V) =
      etaleUpperShriekIsoRestriction B X hX (smallEtaleCompObject B X hX U V) ≪≫
        (abelianRestrictionCompIso B X hX U V).symm
```

## Tag 0F6U, a lemma

[Tag 0F6U](https://stacks.math.columbia.edu/tag/0F6U) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.fUpperShriekBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/UpperShriekBaseChange.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/UpperShriekBaseChange.lean#L178).

> **Stacks 0F6U.** For a cartesian square with horizontal morphisms `p : X' ⟶ X`,
> `g : Y' ⟶ Y`, vertical morphisms `f : X ⟶ Y`, `f' : X' ⟶ Y'` and `f` locally quasi-finite, the
> upper shriek commutes with direct image: `p_* f'^! ≅ f^! g_*` as functors on abelian sheaves of
> `Y'_étale`. Both sides are right adjoint to the two sides of the base-change isomorphism
> `g⁻¹ f_! ≅ f'_! p⁻¹` of Stacks 0F5J, so they agree by uniqueness of right adjoints.

```lean
public def fUpperShriekBaseChangeIso (sq : IsPullback p f' f g) :
    letI := locallyOfFiniteType_of_isPullback B p f' f g sq
    letI := locallyQuasiFinite_of_isPullback B p f' f g sq
    fUpperShriekFunctor.{u, u + 1} B f' ⋙ abPushforward.{u, u + 1} B p ≅
      abPushforward.{u, u + 1} B g ⋙ fUpperShriekFunctor.{u, u + 1} B f
```

**`AlgebraicGeometry.SmallEtale.fUpperShriekBaseChangeObjIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/UpperShriekBaseChange.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/UpperShriekBaseChange.lean#L192). The attribute's comment: “the identification at a single abelian sheaf”.

> **Stacks 0F6U.** For an abelian sheaf `ℱ` on `Y'_étale` the base-change isomorphism of
> Stacks 0F6U reads `p_* (f'^! ℱ) ≅ f^! (g_* ℱ)`, which is the identification the source states
> sheaf by sheaf.

```lean
public def fUpperShriekBaseChangeObjIso (sq : IsPullback p f' f g)
    (ℱ : Sheaf (SmallEtale.topology B Y'.obj Y'.property) AddCommGrpCat.{u + 1}) :
    letI := locallyOfFiniteType_of_isPullback B p f' f g sq
    letI := locallyQuasiFinite_of_isPullback B p f' f g sq
    (abPushforward.{u, u + 1} B p).obj ((fUpperShriekFunctor.{u, u + 1} B f').obj ℱ) ≅
      (fUpperShriekFunctor.{u, u + 1} B f).obj ((abPushforward.{u, u + 1} B g).obj ℱ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 63.6, Tag 0F58](https://stacks.math.columbia.edu/tag/0F58)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
