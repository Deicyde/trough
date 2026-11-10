---
declaration: section
origin: cited
lean: CategoryTheory.Functor.FiberedMor, CategoryTheory.Functor.fibYonedaEvaluation, CategoryTheory.Functor.fibYonedaEvaluation_isEquivalence, CategoryTheory.Functor.twoYonedaEvaluation, CategoryTheory.Functor.twoYonedaEvaluation_isEquivalence, CategoryTheory.Functor.TwoYoneda.liftBasedEvaluationIso, CategoryTheory.Functor.TwoYoneda.hom₂OfFiberHom, CategoryTheory.Functor.twoYonedaPresheaf
statement: formalized
proof: formalized
---

# 4.41 The 2-Yoneda lemma

Section 4.41 of the Stacks Project, [Tag 0GWH](https://stacks.math.columbia.edu/tag/0GWH). 3 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GWI, a lemma

[Tag 0GWI](https://stacks.math.columbia.edu/tag/0GWI) in the Stacks Project.

**`CategoryTheory.Functor.FiberedMor`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoYoneda/Fibered.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoYoneda/Fibered.lean#L67).

> A morphism of fibred categories `(𝒞/U, Over.forget U) ⟶ (𝒮, p)`, i.e. an object of
> the category `Mor_{Fib/𝒞}(𝒞/U, 𝒮)` of Stacks Definition 02XP(2) with source the slice
> fibration. It is a functor over `𝒞` — a `BasedFunctor` between the based categories
> attached to `Over.forget U` and to `p`, so the underlying functor `Over U ⥤ 𝒮` commutes
> strictly with the projections to `𝒞` — which in addition preserves strongly Cartesian
> morphisms.
>
> Since the slice projection `Over.forget U` is a fibration in which every morphism
> `g : a ⟶ b` of `Over U` is strongly Cartesian over its underlying `𝒞`-arrow
> `g.left = (Over.forget U).map g`, the preservation condition specialises to the
> unconditional requirement that `toFunctor.map g` be strongly Cartesian over `g.left`.

```lean
structure FiberedMor (p : 𝒮 ⥤ 𝒞) (U : 𝒞) extends
    BasedCategory.ofFunctor (Over.forget U) ⥤ᵇ BasedCategory.ofFunctor p
```

**`CategoryTheory.Functor.fibYonedaEvaluation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoYoneda/Fibered.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoYoneda/Fibered.lean#L139).

> The evaluation, or "2-Yoneda", functor
> `ev_U : Mor_{Fib/𝒞}(𝒞/U, 𝒮) ⥤ 𝒮_U`, `G ↦ G 1_U`.
>
> On objects it sends a morphism of fibred categories `G` to its value at the terminal
> object `1_U = (U, 𝟙 U)` of `𝒞/U`, which lies in the fibre over `U` because
> `G ⋙ p = Over.forget U`. On a 2-morphism `t` it returns the component of `t` at `1_U`,
> which lies over `𝟙 U` and is therefore a morphism of the fibre.

```lean
def fibYonedaEvaluation (p : 𝒮 ⥤ 𝒞) (U : 𝒞) : FiberedMor p U ⥤ p.Fiber U
```

**`CategoryTheory.Functor.fibYonedaEvaluation_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoYoneda/Fibered.lean, line 409](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoYoneda/Fibered.lean#L409).

> **The 2-Yoneda lemma for fibred categories (Stacks 0GWI).** For a fibred category
> `p : 𝒮 ⥤ 𝒞` and an object `U : 𝒞`, the evaluation functor
> `ev_U : Mor_{Fib/𝒞}(𝒞/U, 𝒮) ⥤ 𝒮_U`, `G ↦ G 1_U`, is an equivalence of categories.

```lean
theorem fibYonedaEvaluation_isEquivalence (p : 𝒮 ⥤ 𝒞) [p.IsFibered] (U : 𝒞) :
    (fibYonedaEvaluation p U).IsEquivalence
```

## Tag 004B, a lemma

[Tag 004B](https://stacks.math.columbia.edu/tag/004B) in the Stacks Project.

**`CategoryTheory.Functor.twoYonedaEvaluation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoYoneda/Basic.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoYoneda/Basic.lean#L124).

> The evaluation functor `ev : Mor_{Cat/C}(C/U, S) ⥤ S_U` of the 2-Yoneda lemma.
>
> On objects it sends a functor over `C`, `G : C/U ⥤ S` (packaged as a based functor),
> to `G(id_U) = G(Over.mk (𝟙 U))`, which lies in the fibre over `U` since
> `p ∘ G = π_U` and `π_U (Over.mk (𝟙 U)) = U`.
>
> On a 2-morphism `η : G ⟶ G'` (a based natural transformation) it returns the
> component `η_{(U, 𝟙 U)}`, which lies over `𝟙 U` and is therefore a morphism of `S_U`.

```lean
noncomputable def Functor.twoYonedaEvaluation (p : S ⥤ C) (U : C) :
    (BasedCategory.ofFunctor (Over.forget U) ⥤ᵇ BasedCategory.ofFunctor p) ⥤ p.Fiber U
```

**`CategoryTheory.Functor.twoYonedaEvaluation_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoYoneda/Basic.lean, line 368](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoYoneda/Basic.lean#L368).

> **The 2-Yoneda lemma (Stacks 004B).**
> Let `p : S ⥤ C` be fibred in groupoids and let `U` be an object of `C`. Then the
> evaluation functor `ev : Mor_{Cat/C}(C/U, S) ⥤ S_U`, `G ↦ G(id_U)`, is an equivalence
> of categories.
>
> It is faithful, full and essentially surjective by
> `Functor.twoYonedaEvaluation_faithful`, `Functor.twoYonedaEvaluation_full` and
> `Functor.twoYonedaEvaluation_essSurj`, and a functor with these three properties is an
> equivalence.

```lean
theorem Functor.twoYonedaEvaluation_isEquivalence (p : S ⥤ C) (hp : p.IsFiberedInGroupoids)
    (U : C) : (Functor.twoYonedaEvaluation p U).IsEquivalence
```

**`CategoryTheory.Functor.TwoYoneda.liftBasedEvaluationIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoYoneda/RepresentedPoint.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoYoneda/RepresentedPoint.lean#L65). The attribute's comment: “essential surjectivity of evaluation, as data”.

> **Stacks 004B**, essential surjectivity as data. The functor over `C` on the slice `C/U`
> assembled from the chosen cartesian lifts of an object `x` of the fibre of `p` over `U` evaluates
> at the terminal object to an object canonically isomorphic to `x`: the chosen lift at `𝟙 U` is an
> arrow of the fibre, and the fibre of a category fibred in groupoids is a groupoid.

```lean
noncomputable def liftBasedEvaluationIso (p : S ⥤ C) (hp : p.IsFiberedInGroupoids) (U : C)
    (x : p.Fiber U) :
    (Functor.twoYonedaEvaluation p U).obj (liftBased p hp U x) ≅ x
```

**`CategoryTheory.Functor.TwoYoneda.hom₂OfFiberHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoYoneda/RepresentedPoint.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoYoneda/RepresentedPoint.lean#L80). The attribute's comment: “fullness of evaluation, as data”.

> **Stacks 004B**, fullness as data. The 2-morphism of functors over `C` on the slice `C/U`
> representing a morphism of the fibre objects they evaluate to.

```lean
noncomputable def hom₂OfFiberHom
    (φ : (Functor.twoYonedaEvaluation p U).obj G ⟶ (Functor.twoYonedaEvaluation p U).obj G') :
    G ⟶ G'
```

## Tag 076J, a remark

[Tag 076J](https://stacks.math.columbia.edu/tag/076J) in the Stacks Project.

**`CategoryTheory.Functor.twoYonedaPresheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoYoneda/SplitModel.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoYoneda/SplitModel.lean#L154).

> The contravariant functor `F : 𝒞 ⥤ Groupoids` with `F(U) = Mor_{Cat/𝒞}(𝒞/U, 𝒮)` and
> `F(f) : F(V) ⥤ F(U)` given by precomposition with the functor `𝒞/U ⥤ 𝒞/V` induced by
> `f : U ⟶ V`.

```lean
noncomputable def Functor.twoYonedaPresheaf (p : 𝒮 ⥤ 𝒞) (hp : p.IsFiberedInGroupoids) :
    𝒞ᵒᵖ ⥤ Grpd.{max u₁ v₁ v₂, max u₁ v₁ u₂ v₂}
```

**`CategoryTheory.Functor.twoYonedaComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoYoneda/SplitModel.lean, line 237](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoYoneda/SplitModel.lean#L237).

> The functor `G : 𝒮' ⥤ 𝒮` sending the pair `(U, x)` to `x(id_U)`.

```lean
noncomputable def twoYonedaComparison (hp : p.IsFiberedInGroupoids) :
    ∫ᶜ (p.twoYonedaPresheaf hp ⋙ Grpd.forgetToCat).toPseudofunctor' ⥤
      (BasedCategory.ofFunctor p).obj
```

**`CategoryTheory.Functor.twoYonedaComparison_comp`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoYoneda/SplitModel.lean, line 287](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoYoneda/SplitModel.lean#L287).

> The functor `G` is a functor over `𝒞`: its composite with `p` is the projection of the
> category `𝒮'` attached to `F`.

```lean
lemma twoYonedaComparison_comp (hp : p.IsFiberedInGroupoids) :
    p.twoYonedaComparison hp ⋙ p = (presheafOfGroupoids (p.twoYonedaPresheaf hp)).p
```

**`CategoryTheory.Functor.twoYonedaComparison_isEquivalenceOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoYoneda/SplitModel.lean, line 337](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoYoneda/SplitModel.lean#L337).

> The functor `G` is an equivalence in the 2-category of categories fibred in groupoids over
> `𝒞`: it admits a quasi-inverse which is again a functor over `𝒞`, and the unit and counit have
> all their components lying over identity morphisms of `𝒞`.

```lean
theorem twoYonedaComparison_isEquivalenceOver (hp : p.IsFiberedInGroupoids) :
    ∃ (H : 𝒮 ⥤ (presheafOfGroupoids (p.twoYonedaPresheaf hp)).obj)
      (_ : H ⋙ (presheafOfGroupoids (p.twoYonedaPresheaf hp)).p = p)
      (η : p.twoYonedaComparison hp ⋙ H ≅ 𝟭 _)
      (ε : H ⋙ p.twoYonedaComparison hp ≅ 𝟭 _),
      (∀ a, (presheafOfGroupoids (p.twoYonedaPresheaf hp)).p.IsHomLift
          (𝟙 ((presheafOfGroupoids (p.twoYonedaPresheaf hp)).p.obj a)) (η.hom.app a)) ∧
      (∀ z, p.IsHomLift (𝟙 (p.obj z)) (ε.hom.app z))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 4.41, Tag 0GWH](https://stacks.math.columbia.edu/tag/0GWH)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
