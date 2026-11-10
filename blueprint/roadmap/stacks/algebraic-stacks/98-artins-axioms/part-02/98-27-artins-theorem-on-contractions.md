---
declaration: section
origin: cited
lean: AlgebraicGeometry.Artin.ContractionSituation, AlgebraicGeometry.Artin.ContractionSituation.U', AlgebraicGeometry.Artin.ContractionSituation.LocalRingsAreGRings, AlgebraicGeometry.Artin.Analytification, AlgebraicGeometry.Artin.ContractionSituation.AnalyticSquareCommutes, AlgebraicGeometry.Artin.ContractionSituation.isIso_rigFunctor_map_g_and_range_pointsMap_ι_U', AlgebraicGeometry.Artin.ContractionSituation.analyticSquareCommutes_iff, AlgebraicGeometry.Artin.contractionFunctor
statement: formalized
proof: formalized
---

# 98.27 Artin's theorem on contractions

Section 98.27 of the Stacks Project, [Tag 0GH7](https://stacks.math.columbia.edu/tag/0GH7). 18 tags here are carried by 36 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GH8, a situation

[Tag 0GH8](https://stacks.math.columbia.edu/tag/0GH8) in the Stacks Project.

**`AlgebraicGeometry.Artin.ContractionSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Artin/ContractionSituation.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Artin/ContractionSituation.lean#L130). The attribute's comment: “the standing data S, X', T', W, W_red and g; the reduction of `W`, its inclusion and the witness that the inclusion exhibits it as the reduction are carried as the fields `Wred`, `WredInclusion` and `isReduction_WredInclusion` rather than constructed. That costs no generality: Stacks 0AIN supplies these for every formal algebraic space, and a reduction is unique up to unique isomorphism by its universal property, so the requirement that the reduction be locally of finite type over `S` does not depend on which one is supplied”.

> **Stacks 0GH8.** The standing situation of Artin's theorem on contractions: a locally
> Noetherian base scheme `S` contained in a big fppf site `B`, an algebraic space `X'` locally
> of finite type over `S`, a closed subset `T' ⊆ |X'|`, a locally Noetherian formal algebraic
> space `W` over `S` with reduction `W_red` locally of finite type over `S`, and a formal
> modification `g : X'_{/T'} ⟶ W` from the completion of `X'` along `T'` to `W`.
>
> The open subspace `U' ⊆ X'` with `|U'| = |X'| ∖ T'` is not a field: it is constructed from
> `T'` as `AlgebraicGeometry.Artin.ContractionSituation.U'`.
>
> The reduction of `W` is carried as data rather than constructed; see the module
> documentation.

```lean
structure ContractionSituation (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
```

**`AlgebraicGeometry.Artin.ContractionSituation.U'`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Artin/ContractionSituation.lean, line 184](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Artin/ContractionSituation.lean#L184). The attribute's comment: “the open subspace U' ⊆ X' with |U'| = |X'| ∖ T', which is determined by T' and therefore constructed rather than carried as a field of the situation”.

> The open subspace `U' ⊆ X'` of the situation of Stacks 0GH8, the one with
> `|U'| = |X'| ∖ T'`: the subfunctor of `X'` cut out by the complement of `T'` under the
> correspondence of Stacks 03BZ. Its two defining properties are
> `AlgebraicGeometry.Artin.ContractionSituation.isOpenSubspace_U'` and
> `AlgebraicGeometry.Artin.ContractionSituation.range_pointsMap_ι_U'`.

```lean
def U' : Subfunctor c.X'
```

## Tag 0GH9, a remark

[Tag 0GH9](https://stacks.math.columbia.edu/tag/0GH9) in the Stacks Project.

**`AlgebraicGeometry.Artin.ContractionSituation.LocalRingsAreGRings`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Artin/ContractionGRingHypothesis.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Artin/ContractionGRingHypothesis.lean#L78). The attribute's comment: “the standing hypothesis the remark announces, that the local rings of S are G-rings, as a predicate on Situation 0GH8. The remark's two other sentences — that the source therefore does not prove its theorem for every Situation 0GH8, and the invitation to a reader who can prove the general case or supply a counterexample — assert no mathematics and are not formalized”.

> **Stacks 0GH9.** The hypothesis the remark announces for the situation of Stacks 0GH8:
> every local ring of the base scheme `S` is a G-ring in the sense of Stacks 07GH.

```lean
def LocalRingsAreGRings (_c : ContractionSituation B S hS) : Prop
```

## Tag 0GID, a remark

[Tag 0GID](https://stacks.math.columbia.edu/tag/0GID) in the Stacks Project.

**`AlgebraicGeometry.Artin.Analytification`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Artin/AnalyticReformulation.lean, line 209](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Artin/AnalyticReformulation.lean#L209). The attribute's comment: “the fictitious category of analytic spaces over S and the fictitious analytification functor, together with the four properties the remark requires of them: (a) that open immersions, closed immersions and open complements of closed immersions exist in An_S, (b) that the analytification of a reduction Y_red ⟶ Y is a closed immersion with Y^rig ⟶ Y^an as its open complement, (c) that for an algebraic space Y and a closed Z the analytification of Y_{/Z} ⟶ Y is an open immersion and induces an open immersion can : (Y_{/Z})^rig ⟶ (Y ∖ Z)^an, and (d) that the rigid part of a formal modification is an isomorphism. The remark's closing claim, that the resulting requirement is equivalent to compatibility condition (4), is not stated: the source makes it only under assumptions of faithfulness of the analytification functor that it does not formulate”.

> **Stacks 0GID.** The analytification data the remark posits, over a base `S` contained in
> a big fppf site `B` and with values in a category `An` standing for the fictitious category
> `An_S` of analytic spaces over `S`: an analytification `Y ↦ Y^an`, its rigid part
> `Y ↦ Y^rig` with the inclusion `Y^rig ⟶ Y^an`, the notions of open immersion, closed
> immersion and open complement in `An`, and the comparison morphisms
> `can : (Y_{/Z})^rig ⟶ (Y ∖ Z)^an`, subject to the four requirements the remark imposes.
>
> Nothing here is asserted to exist: this is the remark's fiction carried as a hypothesis, so
> that what the remark deduces from it can be stated and proved. See the module documentation
> for the two places where the encoding departs from the source — the two functors are total on
> the ambient category of fppf sheaves rather than defined only on locally Noetherian formal
> algebraic spaces, and `Y ↦ Y_red` is not an operation, property (b) being quantified over
> reductions instead.

```lean
structure Analytification (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (An : Type v) [Category.{w} An]
```

**`AlgebraicGeometry.Artin.ContractionSituation.AnalyticSquareCommutes`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Artin/AnalyticReformulation.lean, line 335](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Artin/AnalyticReformulation.lean#L335). The attribute's comment: “the requirement that the displayed square of analytic spaces commute: the comparison morphism can : (V_{/Z})^rig ⟶ (V ∖ Z)^an followed by the analytification of u' agrees with x̂^rig followed by the inverse of the isomorphism g^rig and then by can : (X'_{/T'})^rig ⟶ (X' ∖ T')^an. It is stated as a requirement on the posited analytification data, exactly as the source states it, and is not asserted to be equivalent to compatibility condition (4)”.

> **Stacks 0GID.** The requirement of the remark: that the square
>
> ```
>         (V_{/Z})^rig  --can-->  (V ∖ Z)^an
>             |                        |
>   (g^rig)⁻¹ ∘ x̂^rig              (u')^an
>             v                        v
>       (X'_{/T'})^rig  --can-->  (X' ∖ T')^an
> ```
>
> commute, for a triple `(Z, u', x̂)` satisfying conditions (1), (2), (3) and for analytification
> data as the remark posits. The two horizontal morphisms are the comparison morphisms of
> property (c), the right-hand column is the analytification of `u'`, and the left-hand column
> is `x̂^rig` followed by the inverse of the isomorphism `g^rig` of property (d).
>
> This is a requirement on the given data, and only that. Whether it is equivalent to
> compatibility condition (4) is left open: the source asserts that equivalence only under
> assumptions of faithfulness of the analytification functor which it does not state.

```lean
def AnalyticSquareCommutes {V : BigFppfOver B S hS} (t : PreCompatibilityTriple c V) : Prop
```

**`AlgebraicGeometry.Artin.ContractionSituation.isIso_rigFunctor_map_g_and_range_pointsMap_ι_U'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Artin/AnalyticReformulation.lean, line 352](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Artin/AnalyticReformulation.lean#L352). The attribute's comment: “that the requirement is well formed, which is the remark's sentence "this makes sense as g^rig : (X'_{/T'})^rig ⟶ W^rig is an isomorphism and U' = X' ∖ T'": the first conjunct is the invertibility of g^rig, which is what lets the left-hand column of the square be formed as (g^rig)⁻¹ ∘ x̂^rig, and the second is that the point set of U' is the complement of T'”.

> **Stacks 0GID.** The remark's own observation that its requirement is well formed: in
> Situation 0GH8 the morphism `g^rig : (X'_{/T'})^rig ⟶ W^rig` is an isomorphism, by property
> (d) of the analytification data applied to the formal modification `g`, so that the composite
> `(g^rig)⁻¹ ∘ x̂^rig` forming the left-hand column of the square exists; and `|U'| = |X'| ∖ T'`,
> so that the bottom row of the square, which lands in the analytification of the open subspace
> of `X'` complementary to `T'`, may be read as landing in `(X' ∖ T')^an`.

```lean
theorem isIso_rigFunctor_map_g_and_range_pointsMap_ι_U' :
    IsIso (d.rigFunctor.map c.g) ∧
      Set.range (Space.pointsMap B S hS c.U'.toFunctor c.U'.ι) = c.T'ᶜ
```

**`AlgebraicGeometry.Artin.ContractionSituation.analyticSquareCommutes_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Artin/AnalyticReformulation.lean, line 373](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Artin/AnalyticReformulation.lean#L373). The attribute's comment: “that the requirement is well formed, in the inverse-free form that carries the mathematical content of the remark's sentence "this makes sense as g^rig is an isomorphism": the square commutes exactly when there is a UNIQUE filler h over x̂^rig along g^rig making the square formed from h commute. The left-hand column of the source's square is not given data, it is that filler, and it exists and is unique precisely because g^rig is invertible by property (d). This is the substantive reading; the conjunction in AlgebraicGeometry.Artin.ContractionSituation.isIso_rigFunctor_map_g_and_range_pointsMap_ι_U' is the literal reading of the same sentence”.

> The inverse-free form of the remark's requirement: the square commutes exactly when there
> is a unique morphism `h : (V_{/Z})^rig ⟶ (X'_{/T'})^rig` with `h` followed by `g^rig` equal
> to `x̂^rig` and with the square formed from `h` commutative.
>
> This is the precise content of the remark's "this makes sense": the left-hand column of the
> square is not given, it is the unique filler over `x̂^rig` along `g^rig`, and it exists
> because `g^rig` is an isomorphism.

```lean
theorem analyticSquareCommutes_iff {V : BigFppfOver B S hS} (t : PreCompatibilityTriple c V) :
    AnalyticSquareCommutes c d t ↔
      ∃! h : d.rigFunctor.obj (Space.completionSheaf B S hS (yoneda.obj V) t.Z) ⟶
          d.rigFunctor.obj (Space.completionSheaf B S hS c.X' c.T'),
        h ≫ d.rigFunctor.map c.g = d.rigFunctor.map t.x ∧
          d.can (yoneda.obj V) (isAlgebraicSpace_yoneda B S hS V) t.Z t.isClosed_Z ≫
              d.anFunctor.map (Space.sheafifiedULiftMap B S hS t.u') =
            h ≫ d.can c.X' c.isAlgebraicSpace_X' c.T' c.isClosed_T'
```

## Tag 0GHA, a lemma

[Tag 0GHA](https://stacks.math.columbia.edu/tag/0GHA) in the Stacks Project.

**`AlgebraicGeometry.Artin.contractionFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Artin/ContractionFunctor.lean, line 690](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Artin/ContractionFunctor.lean#L690). The attribute's comment: “the functor F, its values on objects and morphisms and the two functor laws, unconditionally; adicness of the third component of a triple is the defining condition of Stacks 0AQ3, that the morphism be representable by algebraic spaces”.

> **Stacks 0GHA.** In the situation of Stacks 0GH8 the rule `F` that sends a locally
> Noetherian scheme `V` over `S` to the set of triples `(Z, u', x̂)` satisfying the
> compatibility condition, and that sends a morphism `φ : V₂ ⟶ V₁` of locally Noetherian
> schemes over `S` to the map `F(φ) : F(V₁) ⟶ F(V₂)` sending `(Z₁, u'₁, x̂₁)` to
> `(Z₂, u'₂, x̂₂)` with `Z₂` the inverse image of `Z₁` under `φ`, with `u'₂` the composition
> of `u'₁` and `φ|_{V₂ ∖ Z₂}`, and with `x̂₂` the composition of `x̂₁` and `φ_{/Z₂}`, is a
> contravariant functor.

```lean
noncomputable def contractionFunctor (c : ContractionSituation B S hS) :
    (LocallyNoetherianOver B S hS)ᵒᵖ ⥤ Type (u + 1)
```

## Tag 0GHB, a lemma

[Tag 0GHB](https://stacks.math.columbia.edu/tag/0GHB) in the Stacks Project.

**`AlgebraicGeometry.Artin.ContractionSituation.Solution.contractionFunctorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Artin/ContractionRepresents.lean, line 574](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Artin/ContractionRepresents.lean#L574). The attribute's comment: “corrected: the solution is assumed to satisfy |U| = |X| ∖ T (the open subspace U of condition (2) is the complement of T), as the source's proof uses (u' : V ∖ Z → U' = U is the restriction of x to V ∖ Z = x⁻¹(X ∖ T)); for the literal notion of solution of Situation 0GH8 the printed statement is false, see AlgebraicGeometry.Artin.ContractionSituation.not_forall_nonempty_iso_of_solution”.

> **Stacks 0GHB, corrected.** In the situation of Stacks 0GH8, a solution
> `(f : X' ⟶ X, T, a)` whose open subspace `U` is the complement of `T`, `|U| = |X| ∖ T`, gives a
> functorial bijection `F(V) = Mor_S(V, X)` on the category of locally Noetherian schemes `V` over
> `S`, where `F` is Artin's functor of Stacks 0GHA: `x : V ⟶ X` corresponds to
> `(x⁻¹T, x|_{V ∖ Z}, a ∘ x_{/Z})`.
>
> The source states this for every solution, but its notion of solution (the prose after
> Situation 0GH8, `AlgebraicGeometry.Artin.ContractionSituation.Solution`) does not ask
> `|U| = |X| ∖ T`, and without that the statement is false:
> `AlgebraicGeometry.Artin.ContractionSituation.not_forall_nonempty_iso_of_solution`. The source's
> proof uses `u' : V ∖ Z ⟶ U' = U` as the restriction of `x` to `V ∖ Z = x⁻¹(|X| ∖ T)`, which is
> the condition added here.

```lean
noncomputable def contractionFunctorIso :
    contractionFunctor c ≅ morOnLocallyNoetherian B S hS X
```

**`AlgebraicGeometry.Artin.ContractionSituation.nonempty_iso_morOnLocallyNoetherian_of_solution_and_not_forall`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Artin/ContractionRepresentsErratum.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Artin/ContractionRepresentsErratum.lean#L84). The attribute's comment: “erratum: as printed the lemma is false for the literal notion of solution of Situation 0GH8 (part 2, over any nonempty S); it holds for the solutions whose open subspace U is the complement X ∖ T, the reading of condition (2) the source's proof uses (part 1)”.

> **Stacks 0GHB, corrected.** In the situation of Stacks 0GH8, over a locally Noetherian scheme
> `S`:
>
> 1. for every solution `(f : X' → X, T, a)` whose open subspace `U` of condition (2) is the open
>    subspace of `X` with `|U| = |X| ∖ T` — the solutions the source's proof works with, since it
>    takes `u' : V ∖ Z → U' = U` to be the restriction of `x` to `V ∖ Z = x⁻¹(|X| ∖ T)` — there is
>    a functorial bijection `F(V) = Mor_S(V, X)` on the category of locally Noetherian schemes `V`
>    over `S`, where `F` is Artin's functor of Stacks 0GHA; and
> 2. for the literal notion of solution of the prose after Situation 0GH8, which lets `U` be any
>    open subspace of `X` onto which `f` maps `U'` isomorphically, the statement as printed fails
>    as soon as `S` is nonempty: the situation `(X' = ∅, T' = ∅, W = ∅, g = id)` has the solution
>    `X = S` (with `U = ∅ ≠ S = X ∖ T`), and `F(S) = ∅ ≠ Mor_S(S, S)`.
>
> The bijection of (1) is `x ↦ (x⁻¹T, x|_{V ∖ Z}, a ∘ x_{/Z})`
> (`AlgebraicGeometry.Artin.ContractionSituation.Solution.contractionFunctorIso`); its inverse comes
> from the existence half of Stacks 0GI3 and its injectivity from the uniqueness of Stacks 0GI1.

```lean
theorem nonempty_iso_morOnLocallyNoetherian_of_solution_and_not_forall
    (hSN : IsLocallyNoetherian S) :
    (∀ (c : ContractionSituation B S hS) (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
        (s : Solution c X), s.U = Space.openSubspaceOfPoints B S hS X s.Tᶜ →
          Nonempty (contractionFunctor c ≅ morOnLocallyNoetherian B S hS X)) ∧
      (Nonempty S → ¬ ∀ (c : ContractionSituation B S hS)
        (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u), Solution c X →
          Nonempty (contractionFunctor c ≅ morOnLocallyNoetherian B S hS X))
```

## Tag 0GHC, a lemma

[Tag 0GHC](https://stacks.math.columbia.edu/tag/0GHC) in the Stacks Project.

**`AlgebraicGeometry.Artin.ContractionSituation.nonempty_solution_of_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Artin/ContractionSolutionExistence.lean, line 305](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Artin/ContractionSolutionExistence.lean#L305). The attribute's comment: “the source's construction of f via h_{X'} → F uses the compatibility witness x' = x̃ ∘ (V' → V), which is incorrect: it restricts to the wrong projection of V_{/Z} ×_W X'_{/T'} (already for g the completion of the blow-up of the plane in the origin, V = X', x̃ = id). The proof takes a corrected route through X: 0GDU over X algebraizes the base change of g along a, the α-supplied witnesses give X'' → X', and 0GDR over X' inverts it”.

> **Stacks 0GHC.** In the situation of Stacks 0GH8, if there exist an algebraic space `X`
> locally of finite type over `S` and a functorial bijection `F(V) = Mor_S(V, X)` on the category of
> locally Noetherian schemes `V` over `S`, then `X` is a solution: there are a proper morphism
> `f : X' ⟶ X`, a closed subset `T ⊆ |X|` and an isomorphism `a : X_{/T} ≅ W` such that `T'` is the
> inverse image of `T`, `f` maps `U'` isomorphically onto an open subspace `U` of `X`, and
> `g = a ∘ f_{/T}`.
>
> The functorial bijection is `α : F ≅ Mor_S(-, X)` with `F` Artin's functor of Stacks 0GHA.
>
> The source's paragraph constructing `f` from a transformation `h_{X'} ⟶ F` is incorrect as
> written: its compatibility witness `x' = x̃ ∘ (V' ⟶ V)` restricts on `V'_{/Z}` to the wrong
> projection of `V_{/Z} ×_W X'_{/T'}` (already for `V = X'`, `x̃ = id` and `g` the completion of the
> blow-up of the affine plane in the origin). The proof takes a corrected route: Stacks 0GDU over `X`
> algebraizes the base change of `g` along `a` to `h : X'' ⟶ X`, the witnesses supplied by `α` give
> `x'' : X'' ⟶ X'`, Stacks 0GDR over `X'` inverts `x''`, and `f = h ∘ x''⁻¹`. The solution produced
> has `U = X ∖ T`, recorded in
> `AlgebraicGeometry.Artin.ContractionSituation.exists_solution_of_iso_range_U`.

```lean
theorem nonempty_solution_of_iso
    (α : contractionFunctor c ≅ morOnLocallyNoetherian B S hS X)
    (hX : IsAlgebraicSpace B S hS X)
    (hft : Space.IsLocallyOfFiniteType B S hS (terminal.from X)) : c.IsSolution X
```

## Tag 0GHD, a remark

[Tag 0GHD](https://stacks.math.columbia.edu/tag/0GHD) in the Stacks Project.

**`AlgebraicGeometry.Artin.ContractionEqualizer.range_pointsMap_toBase_inter_union_subset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Artin/ContractionEqualizer.lean, line 584](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Artin/ContractionEqualizer.lean#L584). The attribute's comment: “assertion (1), in full: that Im(E' → V) ∩ (Z₁ ∪ Z₂) is contained in Z = Z₁ ∩ Z₂, for the fibre product V' = V'₁ ×_V V'₂ and the equalizer E' ⟶ V' that this file constructs from two elements of F(V) and a chosen compatibility witness for each. Proved with no hypothesis on V beyond its being an object of the big fppf site over S, so the tag's own hypothesis that V be a locally Noetherian scheme over S is the special case V := V.obj for a locally Noetherian object V of that site”.

> **Stacks 0GHD**, assertion (1): the image of `E' ⟶ V` meets `Z₁ ∪ Z₂` only inside
> `Z = Z₁ ∩ Z₂`.
>
> A field-valued point of `E'` lying over `Z₁` is carried by `x'₁` into `T'`, and if it did not
> lie over `Z₂` it would be carried by `x'₂` outside `T'`; but the two images agree, `E'` being
> the equalizer. The argument is symmetric in the two indices.

```lean
theorem range_pointsMap_toBase_inter_union_subset :
    Set.range (Space.pointsMap B S hS d.eqz d.toBase) ∩ (d.t₁.Z ∪ d.t₂.Z) ⊆ d.Z
```

**`AlgebraicGeometry.Artin.ContractionEqualizer.mono_pullbackSnd_offCenter`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Artin/ContractionEqualizer.lean, line 749](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Artin/ContractionEqualizer.lean#L749). The attribute's comment: “assertion (2), the monomorphism half in full: that the morphism E' ×_V (V ∖ Z) → V ∖ Z is a monomorphism. The other half of the assertion, that this morphism is the equalizer of the restrictions of u'₁ and u'₂ to V ∖ (Z₁ ∪ Z₂), is `AlgebraicGeometry.Artin.ContractionEqualizer.exists_isLimit_fork_offCenter`. Proved with no hypothesis on V beyond its being an object of the big fppf site over S, so the tag's own hypothesis that V be a locally Noetherian scheme over S is a special case”.

> **Stacks 0GHD**, first half of assertion (2): the morphism
> `E' ×_V (V ∖ Z) ⟶ V ∖ Z` is a monomorphism.

```lean
theorem mono_pullbackSnd_offCenter : Mono (pullback.snd d.toBase d.offCenter.ι)
```

**`AlgebraicGeometry.Artin.ContractionEqualizer.exists_isLimit_fork_offCenter`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Artin/ContractionEqualizer.lean, line 817](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Artin/ContractionEqualizer.lean#L817). The attribute's comment: “assertion (2), the equalizer half in full: that the morphism E' ×_V (V ∖ Z) → V ∖ Z factors through the open subspace V ∖ (Z₁ ∪ Z₂) by a morphism which is a limiting fork for the restrictions of u'₁ and u'₂ to V ∖ (Z₁ ∪ Z₂), that being what it is for the morphism to be equal to their equalizer. The other half of the assertion, that the morphism is a monomorphism, is `AlgebraicGeometry.Artin.ContractionEqualizer.mono_pullbackSnd_offCenter`. Proved with no hypothesis on V beyond its being an object of the big fppf site over S, so the tag's own hypothesis that V be a locally Noetherian scheme over S is a special case”.

> **Stacks 0GHD**, second half of assertion (2): the morphism
> `E' ×_V (V ∖ Z) ⟶ V ∖ Z` *is* the equalizer of the restrictions of `u'₁` and `u'₂` to
> `V ∖ (Z₁ ∪ Z₂)`, in the sense that it factors through `V ∖ (Z₁ ∪ Z₂)` by a morphism which is
> a limiting fork for those two restrictions.

```lean
theorem exists_isLimit_fork_offCenter :
    ∃ e : pullback d.toBase d.offCenter.ι ⟶ d.offBoth.toFunctor,
      e ≫ Subfunctor.homOfLe d.offBoth_le_offCenter =
          pullback.snd d.toBase d.offCenter.ι ∧
        ∃ he : e ≫ d.restrictedMap₁ = e ≫ d.restrictedMap₂,
          Nonempty (IsLimit (Fork.ofι e he))
```

**`AlgebraicGeometry.Artin.ContractionEqualizer.isSeparated_toBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Artin/ContractionEqualizer.lean, line 897](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Artin/ContractionEqualizer.lean#L897). The attribute's comment: “the sentence `Observe that E' → V is separated and locally of finite type', the separatedness half in full: that the morphism E' ⟶ V is separated. The local-finite-type half is `AlgebraicGeometry.Artin.ContractionEqualizer.isLocallyOfFiniteType_toBase`. The remainder of that sentence, that E_W is a locally Noetherian formal algebraic space separated over V, is not claimed here; its separatedness half is `AlgebraicGeometry.Artin.ContractionEqualizer.isSeparatedMorphism_EW`. Proved with no hypothesis on V beyond its being an object of the big fppf site over S, so the tag's own hypothesis that V be a locally Noetherian scheme over S is a special case”.

> **Stacks 0GHD**, first half of the sentence "observe that `E' → V` is separated and
> locally of finite type": the morphism `E' ⟶ V` is separated.
>
> It is the composite of the equalizer inclusion `E' ⟶ V'`, which is a monomorphism, of the
> projection `V' ⟶ V'₁`, which is a base change of the proper morphism `V'₂ ⟶ V`, and of the
> proper morphism `V'₁ ⟶ V`.

```lean
theorem isSeparated_toBase : Space.IsSeparated B S hS d.toBase
```

**`AlgebraicGeometry.Artin.ContractionEqualizer.isLocallyOfFiniteType_toBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Artin/ContractionEqualizer.lean, line 917](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Artin/ContractionEqualizer.lean#L917). The attribute's comment: “the sentence `Observe that E' → V is separated and locally of finite type', the local-finite-type half in full: that the morphism E' ⟶ V is locally of finite type. The separatedness half is `AlgebraicGeometry.Artin.ContractionEqualizer.isSeparated_toBase`. The remainder of that sentence, that E_W is a locally Noetherian formal algebraic space separated over V, is not claimed here; its separatedness half is `AlgebraicGeometry.Artin.ContractionEqualizer.isSeparatedMorphism_EW`. Proved with no hypothesis on V beyond its being an object of the big fppf site over S, so the tag's own hypothesis that V be a locally Noetherian scheme over S is a special case”.

> **Stacks 0GHD**, second half of the sentence "observe that `E' → V` is separated and
> locally of finite type": the morphism `E' ⟶ V` is locally of finite type.
>
> It is the composite of the equalizer inclusion `E' ⟶ V'`, which is a base change of the
> diagonal of `X'` and so locally of finite type by Stacks 02X4, of the projection
> `V' ⟶ V'₁`, which is a base change of the proper morphism `V'₂ ⟶ V`, and of the proper
> morphism `V'₁ ⟶ V`.

```lean
theorem isLocallyOfFiniteType_toBase :
    Space.IsLocallyOfFiniteType B S hS d.toBase
```

**`AlgebraicGeometry.Artin.ContractionEqualizer.mapTriple_eq_iff_factorsOffCenter_and_factorsEW`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Artin/ContractionEqualizer.lean, line 1180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Artin/ContractionEqualizer.lean#L1180). The attribute's comment: “assertion (5), in full: for a morphism φ : A ⟶ V, the two triples restrict to the same element of F(A) if and only if A ∖ φ⁻¹(Z) → V ∖ Z factors through E' ×_V (V ∖ Z) and A_{/φ⁻¹(Z)} → V_{/Z} factors through E_W. Proved for an arbitrary morphism φ of the big fppf site over S, local Noetherianness of A and V being used nowhere, so the tag's own statement, for a morphism of locally Noetherian schemes, is a special case”.

> **Stacks 0GHD**, assertion (5): given a morphism `φ : A ⟶ V`, the two triples
> `(Z₁, u'₁, x̂₁)` and `(Z₂, u'₂, x̂₂)` restrict to the same element of `F(A)` if and only if
> `A ∖ φ⁻¹(Z) ⟶ V ∖ Z` factors through `E' ×_V (V ∖ Z)` and `A_{/φ⁻¹(Z)} ⟶ V_{/Z}` factors
> through `E_W`.
>
> The restriction of a triple along `φ` is
> `AlgebraicGeometry.Artin.ContractionSituation.mapTriple`, which is the value on `φ` of Artin's
> functor `F` (`AlgebraicGeometry.Artin.contractionFunctor`) when `A` and `V` are locally
> Noetherian. The two conditions of (b) are
> `AlgebraicGeometry.Artin.ContractionEqualizer.FactorsOffCenter` and
> `AlgebraicGeometry.Artin.ContractionEqualizer.FactorsEW`; `E_W` is the equalizer of the two
> morphisms `V_{/Z} ⟶ W` in the category of fppf sheaves, which is where formal algebraic spaces
> over `S` live, so factoring through it is factoring through the remark's `E_W`.

```lean
theorem mapTriple_eq_iff_factorsOffCenter_and_factorsEW :
    mapTriple c φ d.t₁ = mapTriple c φ d.t₂ ↔ d.FactorsOffCenter φ ∧ d.FactorsEW φ
```

**`AlgebraicGeometry.Artin.ContractionEqualizer.isPullback_completedToSituation_completedToEW`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Artin/ContractionEqualizerCompletion.lean, line 603](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Artin/ContractionEqualizerCompletion.lean#L603). The attribute's comment: “assertion (3), the factorization and the cartesian square in full: that E'_{/Z} → V_{/Z} factors through E_W and that the square E'_{/Z} → X'_{/T'}, E_W → W over g is cartesian, in the category of fppf sheaves where formal algebraic spaces over S live. The closing sentence of (3), that E'_{/Z} → E_W is then a formal modification as a base change of g, is Stacks 0GDN applied to this square and is not claimed here. Proved for an arbitrary object V of the big fppf site over S, so the tag's own hypothesis that V be a locally Noetherian scheme over S is a special case”.

> **Stacks 0GHD**, assertion (3): the morphism `E'_{/Z} ⟶ V_{/Z}` factors through `E_W`, by
> `AlgebraicGeometry.Artin.ContractionEqualizer.completedToEW`, and the square formed by
> `E'_{/Z} ⟶ X'_{/T'}`, `E'_{/Z} ⟶ E_W`, the formal modification `g : X'_{/T'} ⟶ W` and the
> morphism `E_W ⟶ V_{/Z} ⟶ W` is cartesian.

```lean
theorem isPullback_completedToSituation_completedToEW :
    d.completedToEW ≫ equalizer.ι d.xhat₁ d.xhat₂ = d.completedToBase ∧
      IsPullback d.completedToSituation d.completedToEW c.g
        (equalizer.ι d.xhat₁ d.xhat₂ ≫ d.xhat₁)
```

**`AlgebraicGeometry.Artin.ContractionEqualizer.isSeparatedMorphism_EW`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Artin/ContractionEqualizerCompletion.lean, line 639](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Artin/ContractionEqualizerCompletion.lean#L639). The attribute's comment: “the sentence `E_W is a locally Noetherian formal algebraic space separated over V', the separatedness half in full: that E_W ⟶ V is separated, i.e. that its relative diagonal is a closed immersion. The other half, that E_W is a locally Noetherian formal algebraic space, is not claimed here. Proved for an arbitrary object V of the big fppf site over S, so the tag's own hypothesis that V be a locally Noetherian scheme over S is a special case”.

> **Stacks 0GHD**, the separatedness half of the sentence "`E_W` is a locally Noetherian
> formal algebraic space separated over `V`": the morphism `E_W ⟶ V` is separated, its relative
> diagonal being an isomorphism because `E_W ⟶ V_{/Z}` and `V_{/Z} ⟶ V` are monomorphisms.

```lean
theorem isSeparatedMorphism_EW : FormalSpace.IsSeparatedMorphism B S hS d.EWToBase
```

**`AlgebraicGeometry.Artin.ContractionEqualizer.morIsoDiagonalFibre`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Artin/ContractionEqualizerRepresents.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Artin/ContractionEqualizerRepresents.lean#L60). The attribute's comment: “final conclusion (with the corrected notion of solution, see 0GHB: the open subspace U of the solution is the complement of T): a solution E → V of the triple of (4) represents F ×_{Δ, F × F} V on locally Noetherian schemes over V, by corrected 0GHB for the situation of (4) and the identification of its functor with F ×_{Δ, F × F} V through (5)”.

> **Stacks 0GHD, the final conclusion.** For the data of Stacks 0GHD over a locally Noetherian
> scheme `V`, a solution `E ⟶ V` of the situation of assertion (4) whose open subspace `U` is the
> complement of `T` (the notion of solution for which Stacks 0GHB holds) represents the fibre
> `F ×_{Δ, F × F} V` on the category of locally Noetherian schemes over `V`: there is an
> isomorphism of functors `Mor_V(-, E) ≅ F ×_{Δ, F × F} V`.

```lean
noncomputable def morIsoDiagonalFibre
    {E : (BigFppfOver B V.left.obj V.left.property)ᵒᵖ ⥤ Type u}
    (s : Solution (d.situation hVN) E)
    (hU : Set.range (Space.pointsMap B V.left.obj V.left.property s.U.toFunctor s.U.ι) =
      s.Tᶜ) :
    morOnLocallyNoetherian B V.left.obj V.left.property E ≅ d.diagonalFibre
```

**`AlgebraicGeometry.Artin.ContractionEqualizer.nonempty_iso_diagonalFibre_of_solution_and_not_forall`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Artin/ContractionEqualizerRepresentsErratum.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Artin/ContractionEqualizerRepresentsErratum.lean#L95). The attribute's comment: “erratum: the final conclusion, that a solution E → V of the triple of (4) represents F ×_{Δ, F × F} V on locally Noetherian schemes over V, is false as printed for the literal notion of solution of Situation 0GH8 (part 2, over any nonempty S); it holds for the solutions whose open subspace U is the complement E ∖ T, the reading of condition (2) the source's proof of 0GHB uses (part 1)”.

> **Stacks 0GHD, final conclusion, corrected.** In the situation of Stacks 0GH8, over a locally
> Noetherian scheme `S`, let `V` be a locally Noetherian scheme over `S` and `d` the data of Stacks
> 0GHD over `V` (two elements of `F(V)` with chosen compatibility witnesses):
>
> 1. for every solution `(f : E' → E, T, a)` of the triple of (4) whose open subspace `U` of
>    condition (2) is the open subspace of `E` with `|U| = |E| ∖ T` — the solutions the source's
>    proof of 0GHB works with, since it takes `u' : V ∖ Z → U' = U` to be the restriction of `x` to
>    `V ∖ Z = x⁻¹(|X| ∖ T)` — `E` represents `F ×_{Δ, F × F} V` on the category of locally
>    Noetherian schemes over `V`; and
> 2. for the literal notion of solution of the prose after Situation 0GH8, which lets `U` be any
>    open subspace of `E` onto which `f` maps `U'` isomorphically, the statement as printed fails
>    as soon as `S` is nonempty: for the situation `(S ⨿ S, ∅, (S ⨿ S)_{/∅}, id)` and the triples
>    of the two inclusions `S ⟶ S ⨿ S` over `V = S`, the triple of (4) is `(∅, ∅, ∅ → ∅)`, which
>    has the solution `E = V` (with `U = ∅ ≠ V = E ∖ T`), and `Mor_V(V, V) ∋ id` while
>    `F ×_{Δ, F × F} V` has no element over `V`.
>
> The isomorphism of (1) is `AlgebraicGeometry.Artin.ContractionEqualizer.morIsoDiagonalFibre`:
> corrected Stacks 0GHB for the situation of (4), followed by the identification of its functor with
> `F ×_{Δ, F × F} V` through assertion (5).

```lean
theorem nonempty_iso_diagonalFibre_of_solution_and_not_forall
    (hSN : IsLocallyNoetherian S) :
    (∀ (c : ContractionSituation B S hS) (V : BigFppfOver B S hS)
        (d : ContractionEqualizer c V) (hVN : IsLocallyNoetherian V.left.obj)
        (E : (BigFppfOver B V.left.obj V.left.property)ᵒᵖ ⥤ Type u)
        (s : Solution (d.situation hVN) E),
        s.U = Space.openSubspaceOfPoints B V.left.obj V.left.property E s.Tᶜ →
          Nonempty (morOnLocallyNoetherian B V.left.obj V.left.property E ≅ d.diagonalFibre)) ∧
      (Nonempty S → ¬ ∀ (c : ContractionSituation B S hS) (V : BigFppfOver B S hS)
        (d : ContractionEqualizer c V) (hVN : IsLocallyNoetherian V.left.obj)
        (E : (BigFppfOver B V.left.obj V.left.property)ᵒᵖ ⥤ Type u),
        Solution (d.situation hVN) E →
          Nonempty (morOnLocallyNoetherian B V.left.obj V.left.property E ≅ d.diagonalFibre))
```

**`AlgebraicGeometry.Artin.ContractionEqualizer.isLocallyNoetherian_EW`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Artin/ContractionEqualizerSituation.lean, line 367](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Artin/ContractionEqualizerSituation.lean#L367). The attribute's comment: “the sentence `E_W is a locally Noetherian formal algebraic space separated over V', the locally Noetherian half in full, for V a locally Noetherian scheme over S; the separatedness half is AlgebraicGeometry.Artin.ContractionEqualizer.isSeparatedMorphism_EW”.

> **`E_W` is a locally Noetherian formal algebraic space**, half of the sentence of Stacks 0GHD
> "`E_W` is a locally Noetherian formal algebraic space separated over `V`": `E_W ⟶ V_{/Z}` is
> locally of finite type (a base change of the diagonal of `W`, Stacks 0AIP) and `V_{/Z}` is locally
> Noetherian (Stacks 0AQ1), so this is Stacks 0AQ8.

```lean
theorem isLocallyNoetherian_EW (hVN : IsLocallyNoetherian V.left.obj) :
    FormalSpace.IsLocallyNoetherian B S hS d.EW
```

**`AlgebraicGeometry.Artin.ContractionEqualizer.isFormalModification_completedToEW`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Artin/ContractionEqualizerSituation.lean, line 381](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Artin/ContractionEqualizerSituation.lean#L381). The attribute's comment: “assertion (3), the closing sentence in full: E'_{/Z} → E_W is a formal modification, as the base change of g along E_W → W, for V a locally Noetherian scheme over S”.

> **`E'_{/Z} ⟶ E_W` is a formal modification**, the closing sentence of Stacks 0GHD (3): by
> assertion (3) it is the base change of the formal modification `g : X'_{/T'} ⟶ W` along the
> adic morphism `E_W ⟶ W` from the locally Noetherian `E_W`, so this is Stacks 0GDN.

```lean
theorem isFormalModification_completedToEW (hVN : IsLocallyNoetherian V.left.obj) :
    IsFormalModification B S hS d.completedToEW
```

**`AlgebraicGeometry.Artin.ContractionEqualizer.situation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Artin/ContractionEqualizerSituation.lean, line 414](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Artin/ContractionEqualizerSituation.lean#L414). The attribute's comment: “assertion (4), in full: E', (E' → V)⁻¹Z and E'_{/Z} → E_W form a situation as in Situation 0GH8 with base scheme the locally Noetherian scheme V, the objects over S lying over V being moved to the big fppf site of V by Stacks 04SG. The inputs are proved: E_W is a locally Noetherian formal algebraic space (isLocallyNoetherian_EW, by 0AIP and 0AQ8), E'_{/Z} → E_W is a formal modification (isFormalModification_completedToEW, by assertion (3) and 0GDN along the adic morphism E_W → W), and the reduction of E_W over V is locally of finite type over V (isLocallyOfFiniteTypeULift_of_isReduction)”.

> **Stacks 0GHD, assertion (4).** For `V` a locally Noetherian scheme over `S`, the algebraic
> space `E'` with its morphism to `V`, the closed subset `(E' ⟶ V)⁻¹ Z ⊆ |E'|` and the morphism
> `E'_{/Z} ⟶ E_W` form a situation as in Stacks 0GH8 with base scheme `V`: through the change of
> base of Stacks 04SG they become an algebraic space `E'_V` locally of finite type over `V`
> (`ContractionSituation.X'`), the closed subset `T'` of `|E'_V|` corresponding to
> `(E' ⟶ V)⁻¹ Z` (`ContractionSituation.T'`), the locally Noetherian formal algebraic space `W_V`
> attached to `E_W ⟶ V` (`ContractionSituation.W`) and the formal modification attached to
> `E'_{/Z} ⟶ E_W` (`ContractionSituation.g`); the reduction of `W_V` is locally of finite type over
> `V`. The components are recorded by `situation_space`, `situation_closedSubset`, `situation_W` and
> `smallerBaseSheafFunctor_map_situation_g`.

```lean
def situation (hVN : IsLocallyNoetherian V.left.obj) :
    ContractionSituation B V.left.obj V.left.property
```

## Tag 0GHE, a lemma

[Tag 0GHE](https://stacks.math.columbia.edu/tag/0GHE) in the Stacks Project.

**`AlgebraicGeometry.Artin.ContractionSituation.exists_solution_of_isClosedImmersion_and_not_forall`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Artin/ContractionClosedImmersionErratum.lean, line 399](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Artin/ContractionClosedImmersionErratum.lean#L399). The attribute's comment: “erratum: as printed online the lemma is false without the hypothesis that X' → S is proper (part 2, over any S with a closed subset that is not open, e.g. S = 𝔸¹_k, Z = {0}, X' = 𝔾_m, T' = ∅); with that hypothesis, which the source's proof uses, it holds (part 1)”.

> **Stacks 0GHE, decided.** In the situation of Stacks 0GH8, over a locally Noetherian scheme
> `S`:
>
> 1. if `X' → S` is proper and `Z ⊆ |S|` is a closed subset such that the inverse image of `Z` in
>    `X'` is `T'`, the morphism `u : U' → S ∖ Z` is a closed immersion and the morphism
>    `w : W → S_{/Z}` is a closed immersion, then there exists a solution `(f : X' → X, T, a)`, and
>    moreover `X → S` is a closed immersion (the solution produced also has `|U| = |X| ∖ T`); and
> 2. without the hypothesis that `X' → S` is proper, the statement fails as soon as `S` has a
>    closed subset which is not open (for instance `S = 𝔸¹_k`, with the closed point `0`): for an
>    open `O ⊆ S` which is not closed, the situation `(X' = O, T' = ∅, W = X'_{/T'}, g = id)` with
>    `Z = S ∖ O` satisfies the three conditions, but has no solution with `X → S` a closed
>    immersion, since such a solution would make `X' → S` proper and hence `O` closed in `S`.
>
> Part 1 is `AlgebraicGeometry.Artin.ContractionSituation.exists_solution_of_isClosedImmersion`;
> part 2 is `AlgebraicGeometry.Artin.ContractionSituation.not_exists_solution_openSituation`.

```lean
theorem exists_solution_of_isClosedImmersion_and_not_forall (hSN : IsLocallyNoetherian S) :
    (∀ (c : ContractionSituation B S hS), Space.IsProper B S hS (terminal.from c.X') →
      ∀ (Z : Set (Space.points B S hS (⊤_ ((BigFppfOver B S hS)ᵒᵖ ⥤ Type u)))), IsClosed Z →
      Space.pointsMap B S hS c.X' (terminal.from c.X') ⁻¹' Z = c.T' →
      ∀ (u : c.U'.toFunctor ⟶
        (Space.openSubspaceOfPoints B S hS (⊤_ ((BigFppfOver B S hS)ᵒᵖ ⥤ Type u)) Zᶜ).toFunctor),
        Space.IsClosedImmersion B S hS u →
      ∀ (w : c.W ⟶ Space.completionSheaf B S hS (⊤_ ((BigFppfOver B S hS)ᵒᵖ ⥤ Type u)) Z),
        FormalSpace.IsClosedImmersion B S hS w →
      ∃ (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (s : c.Solution X),
        Set.range (Space.pointsMap B S hS s.U.toFunctor s.U.ι) = s.Tᶜ ∧
        Space.IsClosedImmersion B S hS (terminal.from X)) ∧
    ((∃ Z : Set S, IsClosed Z ∧ ¬ IsOpen Z) →
      ¬ ∀ (c : ContractionSituation B S hS)
        (Z : Set (Space.points B S hS (⊤_ ((BigFppfOver B S hS)ᵒᵖ ⥤ Type u)))), IsClosed Z →
        Space.pointsMap B S hS c.X' (terminal.from c.X') ⁻¹' Z = c.T' →
        ∀ (u : c.U'.toFunctor ⟶
          (Space.openSubspaceOfPoints B S hS (⊤_ ((BigFppfOver B S hS)ᵒᵖ ⥤ Type u)) Zᶜ).toFunctor),
          Space.IsClosedImmersion B S hS u →
        ∀ (w : c.W ⟶ Space.completionSheaf B S hS (⊤_ ((BigFppfOver B S hS)ᵒᵖ ⥤ Type u)) Z),
          FormalSpace.IsClosedImmersion B S hS w →
        ∃ (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (_ : c.Solution X),
          Space.IsClosedImmersion B S hS (terminal.from X))
```

## Tag 0GHF, a lemma

[Tag 0GHF](https://stacks.math.columbia.edu/tag/0GHF) in the Stacks Project.

**`AlgebraicGeometry.Artin.relative_isClosedImmersion_diag_contractionFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Artin/ContractionDiagonal.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Artin/ContractionDiagonal.lean#L86).

> In the situation of Stacks 0GH8, if `X' ⟶ S` and `W ⟶ S` are separated, then the diagonal
> `Δ : F ⟶ F × F` of the functor `F` of Stacks 0GHA is representable by closed immersions: for every
> locally Noetherian scheme `V` over `S` and every morphism `h_V ⟶ F × F`, the fibre product with `Δ`
> is represented by a locally Noetherian scheme over `S` whose morphism to `V` is a closed immersion.

```lean
theorem relative_isClosedImmersion_diag_contractionFunctor (c : ContractionSituation B S hS)
    (hX' : Space.IsSeparated B S hS (terminal.from c.X'))
    (hW : FormalSpace.IsSeparatedMorphism B S hS (terminal.from c.W)) :
    (MorphismProperty.inverseImage (@IsClosedImmersion.{u} : MorphismProperty Scheme.{u})
        (LocallyNoetherianOver.toScheme B S hS)).relative
      (uliftYoneda.{u + 1} (C := LocallyNoetherianOver B S hS)) (diag (contractionFunctor c))
```

## Tag 0GHG, a lemma

[Tag 0GHG](https://stacks.math.columbia.edu/tag/0GHG) in the Stacks Project.

**`AlgebraicGeometry.Artin.ContractionSituation.satisfiesEtaleSheafProperty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Artin/ContractionEtaleSheafProperty.lean, line 396](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Artin/ContractionEtaleSheafProperty.lean#L396). The attribute's comment: “both the existence and the uniqueness of the amalgamation, granting the locality on the base of the compatibility condition of Stacks 0GHA as h0ADV (the form in which Stacks 0ADV enters the source's argument) and of the adicness condition of Stacks 0AQ2 as hadic”.

> **Stacks 0GHG.** In the situation of Stacks 0GH8 the functor `F` of Stacks 0GHA satisfies
> the sheaf property for every étale covering of locally Noetherian schemes over `S`: a
> compatible family of triples on such a covering has a unique amalgamation.
>
> Existence is `AlgebraicGeometry.Artin.ContractionSituation.exists_mapTriple_eq` and uses the
> two carried inputs; uniqueness is
> `AlgebraicGeometry.Artin.ContractionSituation.eq_of_mapTriple_eq` and uses neither.
> **The two carried inputs, and why neither is equivalent to the conclusion.**
>
> `h0ADV` is the locality on the base of the compatibility condition of [Stacks, Tag 0GHA].  It is
> the form in which [Stacks, Tag 0ADV], étale descent for algebraic spaces, enters the source's
> argument: a witness over `V` is glued from the algebraic spaces `V'_i` and the morphisms
> `p_i, j_i, x̂'_i, x'_i` of the witnesses over the `V_i`, out of a descent datum whose comparison
> isomorphisms come from the uniqueness part of the main theorem on dilatations.  This library has
> neither Tag 0ADV for algebraic spaces nor that uniqueness statement.
>
> `hadic` is the locality on the base of the adicness condition of [Stacks, Tag 0AQ2].  It does not
> follow from [Stacks, Tag 0APY] and [Stacks, Tag 0APV], the two facts about adicness the functor
> `F` is built from: both are closure rules, so every derivation from them concludes adicness of a
> composite built from restrictions, never of a factor.
>
> Each is stated for an arbitrary situation of [Stacks, Tag 0GH8], an arbitrary covering family of
> the big fppf site over `S`, and an arbitrary candidate datum over its base; each constrains one
> already-given datum.  Neither mentions the étale site of locally Noetherian schemes, the family of
> triples, or the existence of an amalgamation, so neither contains the conclusion.  The source's
> proof of this lemma is omitted — the hint is only that morphisms may be defined étale locally — so
> neither is a named citation of it.

```lean
theorem satisfiesEtaleSheafProperty (c : ContractionSituation B S hS)
    (h0ADV : CompatibilityIsLocalOnBase B S hS)
    (hadic : AdicIsLocalOnBase B S hS) :
    SatisfiesEtaleSheafProperty c
```

**`AlgebraicGeometry.Artin.ContractionSituation.contractionFunctor_satisfiesEtaleSheafProperty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Artin/ContractionEtaleSheafPropertyUnconditional.lean, line 189](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Artin/ContractionEtaleSheafPropertyUnconditional.lean#L189).

> In a contraction situation the functor `F` of triples satisfies the sheaf property for all
> étale coverings of locally Noetherian schemes over `S`: a compatible family of triples on such a
> covering has a unique amalgamation.

```lean
theorem contractionFunctor_satisfiesEtaleSheafProperty (c : ContractionSituation B S hS) :
    SatisfiesEtaleSheafProperty c
```

## Tag 0GI5, a lemma

[Tag 0GI5](https://stacks.math.columbia.edu/tag/0GI5) in the Stacks Project.

**`AlgebraicGeometry.Artin.ContractionSituation.limitPreserving_contractionFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Artin/ContractionLimitPreservingProof.lean, line 281](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Artin/ContractionLimitPreservingProof.lean#L281).

> For a contraction situation `c`, the functor `contractionFunctor c` is limit preserving: for
> every cofiltered limit `V = lim V_λ` of affine locally Noetherian objects over `S`, the map
> `colim F(V_λ) ⟶ F(V)` is bijective.

```lean
theorem limitPreserving_contractionFunctor (c : ContractionSituation B S hS) :
    LimitPreserving.{u, u + 1, u, u, u + 1, u} (LocallyNoetherianOver.toScheme B S hS)
      (contractionFunctor c)
```

## Tag 0GI6, a lemma

[Tag 0GI6](https://stacks.math.columbia.edu/tag/0GI6) in the Stacks Project.

**`AlgebraicGeometry.Artin.contractionFunctor_satisfiesRS`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Artin/ContractionRimSchlessinger.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Artin/ContractionRimSchlessinger.lean#L158).

> **Stacks 0GI6.** In the situation of Stacks 0GH8, Artin's functor `F` of Stacks 0GHA
> satisfies the Rim–Schlessinger condition (RS): for every pushout `Y' = Y ⨿_X X'` of spectra of
> Artinian local rings of finite type over `S` along a closed immersion `X ⟶ X'`, every pair of
> elements of `F` over `Y` and `X'` with the same restriction to `X` is the pair of restrictions of
> exactly one element of `F(Y')`.

```lean
theorem contractionFunctor_satisfiesRS (c : ContractionSituation B S hS) :
    LocallyNoetherianOver.SatisfiesRS B S hS (contractionFunctor c)
```

## Tag 0GI7, a lemma

[Tag 0GI7](https://stacks.math.columbia.edu/tag/0GI7) in the Stacks Project.

**`AlgebraicGeometry.Artin.ContractionSituation.finiteDimensional_artinianTangentSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Artin/ContractionTangentSpaceDeformation.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Artin/ContractionTangentSpaceDeformation.lean#L72).

> **Stacks 0GI7.** In Situation 0GH8 the tangent spaces of the functor `F` of Stacks 0GHA are
> finite dimensional: for every field `k` of finite type over `S`, every affine open
> `Spec Λ ⊆ S` through which `Spec k ⟶ S` factors with `Λ → k` finite, and every
> `x₀ ∈ F(Spec k)`, the predeformation category `𝓕_{F,k,x₀}` is a deformation category (so a
> predeformation category whose functor of isomorphism classes satisfies (S2)), and its tangent
> space, with the vector-space structure of Stacks 06IH these give it, is a finite dimensional
> `k`-vector space.

```lean
theorem finiteDimensional_artinianTangentSpace
    (Λ k : Type u) [CommRing Λ] [Field k] [Algebra Λ k] [Module.Finite Λ k]
    (iΛ : Spec (.of Λ) ⟶ S) (hiΛ : IsOpenImmersion iΛ) (x₀ : (contractionFunctor c).Elementsᵒᵖ)
    (hx₀ : (LocallyNoetherianOver.elementsToOver B S hS (contractionFunctor c)).obj x₀ =
      Over.mk (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ)) :
    let D := predeformationCategory iΛ
      (LocallyNoetherianOver.elementsToOver B S hS (contractionFunctor c)) x₀ hx₀
    letI : Category D.carrier := D.category
    let hD := isDeformationCategory_predeformationCategory c Λ k iΛ hiΛ x₀ hx₀
    letI : Fact (IsPredeformationCategory (BasedCategory.ofFunctor D.projection).p) :=
      ⟨hD.predeformation⟩
    letI : Fact (SchlessingerConditionS2 (CategoryOfElements.π
        (isomorphismClasses (BasedCategory.ofFunctor D.projection) hD.predeformation.cofibered))) :=
      ⟨tangentConditionS2 hD⟩
    FiniteDimensional k (artinianTangentSpace Λ k
      (isomorphismClasses (BasedCategory.ofFunctor D.projection) hD.predeformation.cofibered))
```

## Tag 0GI8, a lemma

[Tag 0GI8](https://stacks.math.columbia.edu/tag/0GI8) in the Stacks Project.

**`AlgebraicGeometry.Artin.ContractionSituation.hasEffectiveFormalObjects`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Artin/ContractionFormalObjectEffective.lean, line 41](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Artin/ContractionFormalObjectEffective.lean#L41).

> In Situation 0GH8 assume `X' ⟶ S` is separated. Then every formal object for the contraction
> functor `F` is effective.

```lean
theorem hasEffectiveFormalObjects (hX' : Space.IsSeparated B S hS (terminal.from c.X')) :
    LocallyNoetherianOver.HasEffectiveFormalObjects B S hS (contractionFunctor c)
```

## Tag 0GI9, a lemma

[Tag 0GI9](https://stacks.math.columbia.edu/tag/0GI9) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.exists_isOpenImmersion_smooth_of_isVersalAtCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/VersalSmooth.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/VersalSmooth.lean#L163). The attribute's comment: “an open neighbourhood `U` of the closed point `v` with `U_{/Z} ⟶ W` smooth in the sense of Bootstrap, Definition 03XZ”.

> **Stacks 0GI9.** Let `S` be a locally Noetherian scheme, `V` a scheme locally of finite type
> over `S`, `Z ⊆ |V|` closed, `W` a locally Noetherian formal algebraic space over `S` with `W_red`
> locally of finite type over `S`, and `g : V_{/Z} ⟶ W` an adic morphism. If `v ∈ V` is a closed
> point at which `g` is versal (Section 07XZ), then there is an open neighbourhood `U ⊆ V` of `v`
> such that the restriction `U_{/Z} ⟶ W` of `g` is smooth in the sense of Bootstrap, Definition
> 03XZ.

```lean
theorem exists_isOpenImmersion_smooth_of_isVersalAtCompletion
    [AlgebraicGeometry.IsLocallyNoetherian S] (V : BigFppfOver B S hS)
    (hV : AlgebraicGeometry.LocallyOfFiniteType ((Over.post B.inclusion).obj V : Over S).hom)
    (Z : Set (Space.points B S hS (yoneda.obj V))) (hZ : IsClosed Z)
    (W : FppfSheaf B S hS) (hW : IsLocallyNoetherian B S hS W)
    (Wred : FppfSheaf B S hS) (ι : Wred ⟶ W) (_hι : IsReduction B S hS W Wred ι)
    (_hWred : Space.IsLocallyOfFiniteTypeULift.{u + 1} B S hS (terminal.from Wred.obj))
    (g : Space.completionSheaf B S hS (yoneda.obj V) Z ⟶ W) (hg : IsAdicMorphism B S hS g)
    (v : ((Over.post B.inclusion).obj V : Over S).left) (hvc : IsClosed ({v} : Set _))
    (hvZ : v ∈ Space.pointsToScheme B S hS V '' Z)
    (hvers : IsVersalAtCompletion B S hS V Z W g v) :
    ∃ (U : BigFppfOver B S hS) (i : U ⟶ V),
      IsOpenImmersion ((BigFppfOver.toScheme B S hS).map i) ∧
      v ∈ Set.range ((BigFppfOver.toScheme B S hS).map i) ∧
      ∃ hrep, Space.HasPropertyULift.{u + 1} B S hS
        (fun _ _ a ↦ Space.IsSmoothULift.{u + 1} B S hS a.hom)
        (Space.completionSheafMap B S hS (yoneda.map i) Z ≫ g).hom hrep
```

## Tag 0GIA, a lemma

[Tag 0GIA](https://stacks.math.columbia.edu/tag/0GIA) in the Stacks Project.

**`AlgebraicGeometry.Artin.contractionFunctor_hasOpenVersality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Artin/ContractionOpenVersality.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Artin/ContractionOpenVersality.lean#L155).

> In the situation of Stacks 0GH8 the functor `F` of Stacks 0GHA satisfies openness of versality:
> for every scheme `V` locally of finite type over `S`, every `ξ ∈ F(V)` and every finite type point
> `v₀ ∈ V` at which `ξ` is versal, there is an open neighbourhood of `v₀` in `V` at every finite type
> point of which `ξ` is versal.

```lean
theorem contractionFunctor_hasOpenVersality (c : ContractionSituation B S hS) :
    LocallyNoetherianOver.HasOpenVersality B S hS (contractionFunctor c)
```

## Tag 0GIB, a theorem

[Tag 0GIB](https://stacks.math.columbia.edu/tag/0GIB) in the Stacks Project.

**`AlgebraicGeometry.Artin.ContractionSituation.exists_solution_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Artin/ContractionArtinTheoremUnconditional.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Artin/ContractionArtinTheoremUnconditional.lean#L67).

> **Stacks 0GIB (Artin's theorem on contractions).** Let `S` be a locally Noetherian scheme whose
> local rings at finite type points are G-rings, `X'` an algebraic space locally of finite type over
> `S`, `T' ⊆ |X'|` closed, `W` a locally Noetherian formal algebraic space over `S` with `W_red`
> locally of finite type over `S`, and `g : X'_{/T'} ⟶ W` a formal modification (Situation 0GH8,
> the data of `c`). If `X'` and `W` are separated over `S`, then there are a proper morphism
> `f : X' ⟶ X` of algebraic spaces over `S`, a closed subset `T ⊆ |X|` and an isomorphism
> `a : X_{/T} ≅ W` such that (1) `T'` is the inverse image of `T` under `|f|`, (2) `f` maps
> `X' ∖ T'` isomorphically onto `X ∖ T` (the open subspace `U` of the solution has `|U| = |X| ∖ T`),
> and (3) `g = a ∘ f_{/T}`.

```lean
theorem exists_solution_of_isSeparated (c : ContractionSituation B S hS)
    (hG : ∀ s : S, IsFiniteTypePoint s → IsGRing (S.presheaf.stalk s))
    (hX' : Space.IsSeparated B S hS (terminal.from c.X'))
    (hW : FormalSpace.IsSeparatedMorphism B S hS (terminal.from c.W)) :
    ∃ (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (s : Solution c X),
      Set.range (Space.pointsMap B S hS s.U.toFunctor s.U.ι) = s.Tᶜ
```

## Tag 0GIC, a remark

[Tag 0GIC](https://stacks.math.columbia.edu/tag/0GIC) in the Stacks Project.

**`AlgebraicGeometry.Artin.ContractionSituation.separatednessRemark`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Artin/ContractionSeparatednessRemarkUnconditional.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Artin/ContractionSeparatednessRemarkUnconditional.lean#L75). The attribute's comment: “the diagonal of F is representable with no separatedness of X' or W; the theorem holds for every X' admitting the morphisms x' of Lemma 0GI8, with no separatedness of X' or W; the theorem holds with X' separated and W arbitrary. The closing sentences on quasi-separated X' rest on Remark 0GHK (algebraization results of Bhatt and of Hall-Rydh outside the Stacks project), which the source does not state or prove”.

> In the situation of Stacks 0GH8, with the local rings of `S` at its finite type points G-rings
> and **no separatedness assumed on `X'` or on `W`**:
>
> 1. the diagonal `Δ : F ⟶ F × F` of Artin's functor is representable (by schemes, a fortiori by
>    algebraic spaces): the bootstrap of the remark, applying Artin's theorem in the separated case
>    to the triples `E'`, `(E' ⟶ V)⁻¹Z`, `E'_{/Z} ⟶ E_W` of Stacks 0GHD;
> 2. "the proof of Lemma 0GI8 is the only place where separatedness of `X'` is used, and only to
>    obtain `x' : V' ⟶ X'`": for every `X'` for which the morphisms `x'` exist (the algebraization
>    property `HasCompletionAlgebraization`), Artin's theorem holds, with no separatedness of `X'`
>    or `W`;
> 3. in particular Artin's theorem holds when `X'` alone is separated over `S`, `W` being arbitrary.
>
> The solutions are the solutions of Stacks 0GIB whose open part `U` is the complement of `T` (the
> corrected notion of Stacks 0GHB). The remark's closing sentences on quasi-separated `X'` rest on
> Remark 0GHK, outside the Stacks project; see the module documentation.

```lean
theorem separatednessRemark
    (hG : ∀ s : S, IsFiniteTypePoint s → IsGRing (S.presheaf.stalk s)) :
    (uliftYoneda.{u + 1} (C := LocallyNoetherianOver B S hS)).relativelyRepresentable
        (diag (contractionFunctor c)) ∧
      (c.HasCompletionAlgebraization → ∃ (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
        (s : Solution c X), Set.range (Space.pointsMap B S hS s.U.toFunctor s.U.ι) = s.Tᶜ) ∧
      (Space.IsSeparated B S hS (terminal.from c.X') → ∃ (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
        (s : Solution c X), Set.range (Space.pointsMap B S hS s.U.toFunctor s.U.ι) = s.Tᶜ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 98.27, Tag 0GH7](https://stacks.math.columbia.edu/tag/0GH7)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
