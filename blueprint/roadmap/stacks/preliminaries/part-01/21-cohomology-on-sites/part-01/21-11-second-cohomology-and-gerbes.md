---
declaration: section
origin: cited
lean: CategoryTheory.Gerbe.nonempty_fiber_of_cohomology_vanishing, CategoryTheory.Gerbe.exists_band_nonempty_fiber_of_cohomology_vanishing, CategoryTheory.Gerbe.exists_covering_fiber_nonempty_of_cofinal_h1_isZero
statement: formalized
proof: formalized
---

# 21.11 Second cohomology and gerbes

Section 21.11 of the Stacks Project, [Tag 0CJZ](https://stacks.math.columbia.edu/tag/0CJZ). 1 tag here is carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CK0, a lemma

[Tag 0CK0](https://stacks.math.columbia.edu/tag/0CK0) in the Stacks Project.

**`CategoryTheory.Gerbe.nonempty_fiber_of_cohomology_vanishing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Gerbe/ExistenceOfAnObject.lean, line 1173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Gerbe/ExistenceOfAnObject.lean#L1173).

> **Stacks 0CK0.** Let `p : S ⥤ C` be a gerbe over the site `(C, J)` — fibred in groupoids, a
> stack, locally nonempty, locally connected — and let `G` be the sheaf of abelian groups
> constructed in Stacks 0CJY: an abelian sheaf given with comparisons `θ y : G|_V ≅ Aut(y)`, one
> for every object `y` of every fibre, multiplicative and compatible with conjugation and with base
> change. Let `U` be an object of `C` such that
>
> 1. there is a cofinal system `Cov` of coverings of `U` — a set of covering families refining every
>    covering sieve of `U` — with `H¹(U_i, G) = 0` for every member `U_i` of every family in it and
>    `H¹(U_i ×_U U_j, G) = 0` for every pair of members, and
> 2. `H²(U, G) = 0`.
>
> Then there is an object of `S` lying over `U`.
>
> That the automorphism sheaves of the gerbe are abelian needs no separate hypothesis: each `θ y` is
> a multiplicative isomorphism onto `Aut(y)` from a sheaf of abelian groups, so `Aut(y)` is abelian.
> For the form in which `G` and its comparisons are produced rather than assumed, see
> `CategoryTheory.Gerbe.exists_band_nonempty_fiber_of_cohomology_vanishing`.

```lean
public theorem nonempty_fiber_of_cohomology_vanishing
    {C : Type u₁} {S : Type u₂}
    [Category.{v₁} C] [Category.{v₂} S]
    (J : GrothendieckTopology C) (p : S ⥤ C)
    (hp : p.IsFiberedInGroupoids) (hst : p.IsStack J)
    (hne : p.LocallyNonempty J) (hlc : p.LocallyConnected J)
    [∀ X : C, HasSheafify (J.over X) AddCommGrpCat.{max u₁ v₁ v₂}]
    [∀ X : C, HasExt.{x} (Sheaf (J.over X) AddCommGrpCat.{max u₁ v₁ v₂})]
    (G : Sheaf J AddCommGrpCat.{max u₁ v₁ v₂})
    (hBand :
      haveI : p.IsFibered := hp.isFibered
      haveI : ∀ V : C, IsGroupoid (p.Fiber V) := hp.fiber_isGroupoid
      ∃ (θ : ∀ (V : C) (y : p.Fiber V),
          (Over.forget V).op ⋙ G.obj ⋙ AddCommGrpCat.toCommGrp.{max u₁ v₁ v₂} ⋙
              forget CommGrpCat.{max u₁ v₁ v₂} ≅
            p.morPresheaf y y ⋙ uliftFunctor.{max u₁ v₁, v₂}),
        (∀ (V : C) (y : p.Fiber V) (g : Over V) (a b : G.obj.obj (op g.left)),
          ((θ V y).hom.app (op g) (Multiplicative.ofAdd (a + b))).down =
            ((θ V y).hom.app (op g) (Multiplicative.ofAdd a)).down ≫
              ((θ V y).hom.app (op g) (Multiplicative.ofAdd b)).down) ∧
        (∀ (V : C) (y z : p.Fiber V) (φ : y ⟶ z) (g : Over V)
            (a : G.obj.obj (op g.left)),
          ((θ V z).hom.app (op g) (Multiplicative.ofAdd a)).down =
            Functor.pullbackFiberHom (CategoryTheory.inv φ) g.hom ≫
              ((θ V y).hom.app (op g) (Multiplicative.ofAdd a)).down ≫
                Functor.pullbackFiberHom φ g.hom) ∧
        (∀ (V : C) (y : p.Fiber V) (g : Over V)
            (a : G.obj.obj (op g.left)),
          ((θ V y).hom.app (op g) (Multiplicative.ofAdd a)).down =
            (Functor.pullbackFiberIdIso (p.pullbackFiber y g.hom)).inv ≫
              ((θ g.left (p.pullbackFiber y g.hom)).hom.app
                (op (Over.mk (𝟙 g.left))) (Multiplicative.ofAdd a)).down ≫
                  (Functor.pullbackFiberIdIso (p.pullbackFiber y g.hom)).hom))
    (U : C) (Cov : Set (PreZeroHypercover.{max u₁ v₁ v₂} U))
    (hCover : ∀ E ∈ Cov, E.sieve₀ ∈ J U)
    (hCofinal : ∀ R ∈ J U, ∃ E : PreZeroHypercover.{max u₁ v₁ v₂} U,
      E ∈ Cov ∧ E.sieve₀ ≤ R)
    (hPullback : ∀ (E : PreZeroHypercover.{max u₁ v₁ v₂} U), E ∈ Cov →
      ∀ i j : E.I₀, HasPullback (E.f i) (E.f j))
    (hH1 : ∀ (E : PreZeroHypercover.{max u₁ v₁ v₂} U), E ∈ Cov →
      ∀ i : E.I₀, Subsingleton (Sheaf.H (G.over (E.X i)) 1))
    (hH1pair : ∀ (E : PreZeroHypercover.{max u₁ v₁ v₂} U) (hE : E ∈ Cov)
      (i j : E.I₀),
      let : HasPullback (E.f i) (E.f j) := hPullback E hE i j
      Subsingleton (Sheaf.H (G.over (pullback (E.f i) (E.f j))) 1))
    (hH2 : Subsingleton (Sheaf.H (G.over U) 2)) :
    Nonempty (p.Fiber U)
```

**`CategoryTheory.Gerbe.exists_band_nonempty_fiber_of_cohomology_vanishing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Gerbe/ExistenceOfAnObject.lean, line 1272](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Gerbe/ExistenceOfAnObject.lean#L1272).

> **Stacks 0CK0, with nothing assumed.** Let `p : S ⥤ C` be a gerbe over the site `(C, J)` whose
> automorphism sheaves are abelian. Then there are a sheaf `G` of abelian groups on `C` and
> comparisons `θ y : G|_V ≅ Aut(y)` — that is, the sheaf constructed in Stacks 0CJY, together with
> the data that identifies it: multiplicativity, compatibility with conjugation, and compatibility
> over varying base object — such that for every object `U` of `C` with
>
> 1. a cofinal system `Cov` of coverings of `U` whose members `U_i` have `H¹(U_i, G) = 0` and whose
>    pairs of members have `H¹(U_i ×_U U_j, G) = 0`, and
> 2. `H²(U, G) = 0`
>
> there is an object of `S` lying over `U`.
>
> This is `CategoryTheory.Gerbe.nonempty_fiber_of_cohomology_vanishing` with its hypothesis on `G`
> discharged: `G` is here the band of
> `CategoryTheory.Gerbe.exists_sheaf_iso_morPresheaf_self_uliftFunctor_base`, carried from
> `CommGrpCat` to `AddCommGrpCat` — the universe in which `Sheaf.H` takes its coefficients — along
> `commGroupAddCommGroupEquivalence`, whose unit and counit are `Iso.refl`, so the comparisons
> transport unchanged. No hypothesis of this statement is the conclusion of another tag.

```lean
public theorem exists_band_nonempty_fiber_of_cohomology_vanishing
    {C : Type u₁} {S : Type u₂}
    [Category.{v₁} C] [Category.{v₂} S]
    (J : GrothendieckTopology C) (p : S ⥤ C)
    (hp : p.IsFiberedInGroupoids) (hst : p.IsStack J)
    (hne : p.LocallyNonempty J) (hlc : p.LocallyConnected J)
    (habel : ∀ (V : C) (y : p.Fiber V) (α β : y ⟶ y), α ≫ β = β ≫ α)
    [∀ X : C, HasSheafify (J.over X) AddCommGrpCat.{max u₁ v₁ v₂}]
    [∀ X : C, HasExt.{x} (Sheaf (J.over X) AddCommGrpCat.{max u₁ v₁ v₂})] :
    haveI : p.IsFibered := hp.isFibered
    haveI : ∀ V : C, IsGroupoid (p.Fiber V) := hp.fiber_isGroupoid
    ∃ (G : Sheaf J AddCommGrpCat.{max u₁ v₁ v₂})
      (θ : ∀ (V : C) (y : p.Fiber V),
        (Over.forget V).op ⋙ G.obj ⋙ AddCommGrpCat.toCommGrp.{max u₁ v₁ v₂} ⋙
            forget CommGrpCat.{max u₁ v₁ v₂} ≅
          p.morPresheaf y y ⋙ uliftFunctor.{max u₁ v₁, v₂}),
      (∀ (V : C) (y : p.Fiber V) (g : Over V) (a b : G.obj.obj (op g.left)),
          ((θ V y).hom.app (op g) (Multiplicative.ofAdd (a + b))).down =
            ((θ V y).hom.app (op g) (Multiplicative.ofAdd a)).down ≫
              ((θ V y).hom.app (op g) (Multiplicative.ofAdd b)).down) ∧
        (∀ (V : C) (y z : p.Fiber V) (φ : y ⟶ z) (g : Over V)
            (a : G.obj.obj (op g.left)),
          ((θ V z).hom.app (op g) (Multiplicative.ofAdd a)).down =
            Functor.pullbackFiberHom (CategoryTheory.inv φ) g.hom ≫
              ((θ V y).hom.app (op g) (Multiplicative.ofAdd a)).down ≫
                Functor.pullbackFiberHom φ g.hom) ∧
        (∀ (V : C) (y : p.Fiber V) (g : Over V)
            (a : G.obj.obj (op g.left)),
          ((θ V y).hom.app (op g) (Multiplicative.ofAdd a)).down =
            (Functor.pullbackFiberIdIso (p.pullbackFiber y g.hom)).inv ≫
              ((θ g.left (p.pullbackFiber y g.hom)).hom.app
                (op (Over.mk (𝟙 g.left))) (Multiplicative.ofAdd a)).down ≫
                  (Functor.pullbackFiberIdIso (p.pullbackFiber y g.hom)).hom) ∧
        ∀ (U : C) (Cov : Set (PreZeroHypercover.{max u₁ v₁ v₂} U)),
          (∀ E ∈ Cov, E.sieve₀ ∈ J U) →
          (∀ R ∈ J U, ∃ E : PreZeroHypercover.{max u₁ v₁ v₂} U, E ∈ Cov ∧ E.sieve₀ ≤ R) →
          ∀ hPullback : ∀ (E : PreZeroHypercover.{max u₁ v₁ v₂} U), E ∈ Cov →
              ∀ i j : E.I₀, HasPullback (E.f i) (E.f j),
            (∀ (E : PreZeroHypercover.{max u₁ v₁ v₂} U), E ∈ Cov →
              ∀ i : E.I₀, Subsingleton (Sheaf.H (G.over (E.X i)) 1)) →
            (∀ (E : PreZeroHypercover.{max u₁ v₁ v₂} U) (hE : E ∈ Cov) (i j : E.I₀),
              let : HasPullback (E.f i) (E.f j) := hPullback E hE i j
              Subsingleton (Sheaf.H (G.over (pullback (E.f i) (E.f j))) 1)) →
            Subsingleton (Sheaf.H (G.over U) 2) → Nonempty (p.Fiber U)
```

**`CategoryTheory.Gerbe.exists_covering_fiber_nonempty_of_cofinal_h1_isZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Gerbe/SecondCohomology.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Gerbe/SecondCohomology.lean#L113). The attribute's comment: “the refinement step of the proof: a covering of U drawn from the cofinal system of hypothesis (1), carrying an object of 𝒮 over each of its members”.

> **Stacks 0CK0, the refinement step.** Let `p : 𝒮 ⥤ 𝒞` be locally nonempty for `J` — clause
> (2) of the definition of a gerbe, Stacks 06NZ — let `𝒢` be an abelian sheaf on `(𝒞, J)`, and let
> `U` be an object of `𝒞` satisfying hypothesis (1) of Stacks 0CK0: there is a cofinal system of
> coverings of `U`, that is a family of covering families refining every covering sieve of `U`,
> each member `U_i` of which has `H¹(U_i, 𝒢) = 0` and each double overlap `U_i ×_U U_j` of which
> has `H¹(U_i ×_U U_j, 𝒢) = 0`.
>
> Then there is a covering family `{U_i → U}` with all of that vanishing which in addition carries
> an object of `𝒮` over every member.
>
> This is the source's "Choose a covering `{U_i → U}` and objects `x_i` of `𝒮` over `U_i`. By
> assumption (1) we may choose the covering such that `H¹(U_i, 𝒢) = 0` and
> `H¹(U_i ×_U U_j, 𝒢) = 0`." Local nonemptiness supplies a covering sieve of `U` along every arrow
> of which the fibre of `p` is nonempty; cofinality refines it to a member of the system, whose
> every arrow `U_i → U` lies in that sieve.

```lean
theorem exists_covering_fiber_nonempty_of_cofinal_h1_isZero
    (p : 𝒮 ⥤ 𝒞) (J : GrothendieckTopology 𝒞)
    [HasSheafify J AddCommGrpCat.{v₁}] [HasExt.{x} (Sheaf J AddCommGrpCat.{v₁})]
    (hne : p.LocallyNonempty J) (𝒢 : Sheaf J AddCommGrpCat.{v₁}) (U : 𝒞)
    (hcof : ∀ R ∈ J U, ∃ (I : Type w) (V : I → 𝒞) (f : ∀ i, V i ⟶ U),
      Sieve.ofArrows V f ∈ J U ∧ Sieve.ofArrows V f ≤ R ∧
      (∀ i, IsZero (Sheaf.H' 𝒢 1 (V i))) ∧
      ∃ (Vij : I → I → 𝒞) (pr₁ : ∀ i j, Vij i j ⟶ V i) (pr₂ : ∀ i j, Vij i j ⟶ V j),
        (∀ i j, IsPullback (pr₁ i j) (pr₂ i j) (f i) (f j)) ∧
        ∀ i j, IsZero (Sheaf.H' 𝒢 1 (Vij i j))) :
    ∃ (I : Type w) (V : I → 𝒞) (f : ∀ i, V i ⟶ U),
      Sieve.ofArrows V f ∈ J U ∧
      (∀ i, Nonempty (p.Fiber (V i))) ∧
      (∀ i, IsZero (Sheaf.H' 𝒢 1 (V i))) ∧
      ∃ (Vij : I → I → 𝒞) (pr₁ : ∀ i j, Vij i j ⟶ V i) (pr₂ : ∀ i j, Vij i j ⟶ V j),
        (∀ i j, IsPullback (pr₁ i j) (pr₂ i j) (f i) (f j)) ∧
        ∀ i j, IsZero (Sheaf.H' 𝒢 1 (Vij i j))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.11, Tag 0CJZ](https://stacks.math.columbia.edu/tag/0CJZ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
