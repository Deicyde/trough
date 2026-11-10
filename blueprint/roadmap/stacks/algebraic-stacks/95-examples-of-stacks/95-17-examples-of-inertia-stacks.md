---
declaration: section
origin: cited
lean: AlgebraicGeometry.fixedScheme, AlgebraicGeometry.fixedSchemeHomEquiv, AlgebraicGeometry.fixedSchemeAut, AlgebraicGeometry.totalToTarget_factorsThroughFixedScheme, AlgebraicGeometry.fixedQuotientToInertia, AlgebraicGeometry.AbstractGroupQuotientStack.inertiaComparison, AlgebraicGeometry.AbstractGroupQuotientStack.inertiaComparison_comp_struct, AlgebraicGeometry.inertia_equivalence_stackCoproduct
statement: formalized
proof: formalized
---

# 95.17 Examples of inertia stacks

Section 95.17 of the Stacks Project, [Tag 0373](https://stacks.math.columbia.edu/tag/0373). 2 tags here are carried by 24 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0374, an example

[Tag 0374](https://stacks.math.columbia.edu/tag/0374) in the Stacks Project.

**`AlgebraicGeometry.fixedScheme`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/AbstractGroupQuotientInertia.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/AbstractGroupQuotientInertia.lean#L166). The attribute's comment: “the fixed-point scheme X^g as the displayed fibre product”.

> **Stacks 0374.** The fixed-point scheme `Y^g = {y ∈ Y | g(y) = y}` of the automorphism
> of `Y` attached to a group element `g`, as the fibre product
> `Y^g = Y ×_{(1, 1), Y ×_S Y, (g, 1)} Y` displayed in the source.

```lean
def fixedScheme (Y : Over S) (a : G →* Aut Y) (g : G) : Over S
```

**`AlgebraicGeometry.fixedSchemeHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/AbstractGroupQuotientInertia.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/AbstractGroupQuotientInertia.lean#L221). The attribute's comment: “X^g = \{x ∈ X | g(x) = x} as a functor of points”.

> **Stacks 0374.** The fibre product `Y ×_{(1, 1), Y ×_S Y, (g, 1)} Y` is the locus
> `Y^g = {y ∈ Y | g(y) = y}`: its `T`-points are exactly the `T`-points of `Y` fixed by the
> automorphism attached to `g`.

```lean
def fixedSchemeHomEquiv (Y : Over S) (a : G →* Aut Y) (g : G) (T : Over S) :
    (T ⟶ fixedScheme S G Y a g) ≃ {x : T ⟶ Y // x ≫ (a g).asIso.hom = x}
```

**`AlgebraicGeometry.fixedSchemeAut`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/AbstractGroupQuotientInertia.lean, line 271](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/AbstractGroupQuotientInertia.lean#L271). The attribute's comment: “the induced action of G on X^g”.

> **Stacks 0374.** The action of `G` on the fixed-point scheme `Y^g` induced by the action
> on `Y`. It is here that commutativity of `G` enters: for `h ∈ G` the automorphism of `Y`
> attached to `h` commutes with the one attached to `g`, hence preserves `Y^g`.

```lean
def fixedSchemeAut (Y : Over S) (a : G →* Aut Y) (g : G) :
    G →* Aut (fixedScheme S G Y a g)
```

**`AlgebraicGeometry.totalToTarget_factorsThroughFixedScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/AbstractGroupQuotientInertia.lean, line 599](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/AbstractGroupQuotientInertia.lean#L599). The attribute's comment: “φ ∘ α = φ makes φ factor through the inclusion of X^g in X”.

> **Stacks 0374.** The source's sentence "the condition that `φ ∘ α = φ` means that `φ`
> factors through the inclusion of `Y^g` in `Y`": for an object of `[Y/G]` whose equivariant
> map is fixed by `g`, every value of that map factors uniquely through `Y^g`.

```lean
theorem totalToTarget_factorsThroughFixedScheme (g : G)
    (A : schemeQuotient.{t} B S hS G Y a)
    (hA : ∀ (V : (BigFppfOver B S hS)ᵒᵖ) (p : A.Total V),
      (schemePointsAut B S hS G Y a g).asIso.hom.app V (A.totalToTarget V p) =
        A.totalToTarget V p)
    (V : (BigFppfOver B S hS)ᵒᵖ) (p : A.Total V) :
    ∃! y : (Over.post B.inclusion).obj V.unop ⟶ fixedScheme S G Y a g,
      y ≫ fixedSchemeIncl S G Y a g = A.totalToTarget V p
```

**`AlgebraicGeometry.fixedQuotientToInertia`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/AbstractGroupQuotientInertia.lean, line 616](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/AbstractGroupQuotientInertia.lean#L616). The attribute's comment: “the g-th summand of the morphism to the inertia stack”.

> **Stacks 0374.** The morphism `[Y^g/G] → I_{[Y/G]}` of the source: a torsor `P` with a
> `G`-equivariant map `ψ : P → Y^g` goes to the triple `(P, ι ∘ ψ)` together with the
> automorphism given by multiplication by `g` on `P`.

```lean
def fixedQuotientToInertia (g : G) :
    fixedSchemeQuotient.{t} B S hS G Y a g ⥤
      AbsoluteInertia (schemeQuotientProjection.{t} B S hS G Y a)
```

**`AlgebraicGeometry.AbstractGroupQuotientStack.inertiaComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/AbstractGroupQuotientInertia.lean, line 645](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/AbstractGroupQuotientInertia.lean#L645). The attribute's comment: “the morphism from the disjoint union of the [X^g/G] to the inertia stack”.

> **Stacks 0374.** The morphism `∐_{g ∈ G} [Y^g/G] → I_{[Y/G]}` of the source, assembled
> from its summands. On `T`-points it is the source's recipe: a `G`-torsor `P → T` with a
> `G`-equivariant `ψ : P → Y^g` is sent to `(P, ι ∘ ψ, α)` with `α` multiplication by `g`.

```lean
def inertiaComparison :
    (Σ g : G, fixedSchemeQuotient.{t} B S hS G Y a g) ⥤
      AbsoluteInertia (schemeQuotientProjection.{t} B S hS G Y a)
```

**`AlgebraicGeometry.AbstractGroupQuotientStack.inertiaComparison_comp_struct`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/AbstractGroupQuotientInertia.lean, line 662](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/AbstractGroupQuotientInertia.lean#L662). The attribute's comment: “the comparison is a morphism over the big fppf site”.

> **Stacks 0374.** The comparison morphism is a morphism *over* `(Sch/S)_fppf`: on each
> summand, composing it with the structure functor of the inertia gives back the projection of
> `[Y^g/G]` to the site, since neither the inclusion `Y^g → Y` nor remembering the
> automorphism `α` changes the object of the site attached to a triple.

```lean
lemma inertiaComparison_comp_struct (g : G) :
    Sigma.incl g ⋙ inertiaComparison.{t} B S hS G Y a ⋙
        relativeInertiaStruct (schemeQuotientProjection.{t} B S hS G Y a)
          (schemeQuotientProjection.{t} B S hS G Y a) =
      schemeQuotientProjection.{t} B S hS G (fixedScheme S G Y a g)
        (fixedSchemeAut Y a g)
```

**`AlgebraicGeometry.inertia_equivalence_stackCoproduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/AbstractGroupQuotientInertiaEquivalence.lean, line 313](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/AbstractGroupQuotientInertiaEquivalence.lean#L313). The attribute's comment: “I\_\{[X/G]} = ∐\_\{g ∈ G} [X^g/G]: an equivalence over (Sch/S)\_fppf from the coproduct of stacks to the inertia stack, restricting on each summand to the canonical functor”.

> **Stacks 0374.** Let `S` be a scheme, `G` a commutative group, `Y → S` a scheme over `S` and
> `a : G →* Aut_S(Y)` an action of `G` on `Y`. Then the inertia stack of `[Y/G]` is the coproduct of
> stacks `I_{[Y/G]} = ∐_{g ∈ G} [Y^g/G]`, where `Y^g = Y ×_{(1, 1), Y ×_S Y, (g, 1)} Y` is the
> fixed-point scheme of `g` (`AlgebraicGeometry.fixedScheme`) with the action of `G` induced by
> `a`: there is an equivalence of categories over `(Sch/S)_fppf` (a quasi-inverse over
> `(Sch/S)_fppf` with unit and counit lying over identities) from the coproduct of stacks
> `∐_{g ∈ G} [Y^g/G]` to `I_{[Y/G]}`, whose restriction to the `g`-th summand `[Y^g/G]` is the
> canonical functor of the source, sending a torsor `P` with an equivariant map `P → Y^g` to `P`
> with the composite map to `Y` and the automorphism given by multiplication by `g`.

```lean
theorem inertia_equivalence_stackCoproduct :
    ∃ H : Functor.StackCoproduct
        (fun g : G => schemeQuotientProjection.{max (u + 1) t} B S hS G (fixedScheme S G Y a g)
          (fixedSchemeAut Y a g))
        (BigFppfOver.topology B S hS) (fun _ => projection_isFiberedInGroupoids) ⥤
        AbsoluteInertia (schemeQuotientProjection.{max (u + 1) t} B S hS G Y a),
      Nonempty (Functor.IsEquivalenceOver (Functor.stackCoproductProj _ _ _)
        (schemeInertiaProj.{max (u + 1) t} B S hS G Y a) H) ∧
      ∀ g : G, Nonempty (Functor.stackCoproductι _ _ _ g ⋙ H ≅
        fixedQuotientToInertia.{max (u + 1) t} B S hS G Y a g)
```

**`AlgebraicGeometry.isPullback_fixedPresheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/AbstractGroupQuotientStackInertia.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/AbstractGroupQuotientStackInertia.lean#L181). The attribute's comment: “the fixed locus as a fibre product”.

> **Stacks 0374.** The fixed subpresheaf `X^σ` is the fibre product
> `X ×_{(1,1), X × X, (σ,1)} X` displayed in the source. On presheaves over the big fppf site
> of `S` the binary product is the fibre product over `S`, as `S` is the terminal object.

```lean
theorem isPullback_fixedPresheaf (σ : X ⟶ X) :
    IsPullback (fixedPresheafIncl σ) (fixedPresheafIncl σ)
      (prod.lift (𝟙 X) (𝟙 X)) (prod.lift σ (𝟙 X))
```

**`AlgebraicGeometry.fixedPresheafAction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/AbstractGroupQuotientStackInertia.lean, line 263](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/AbstractGroupQuotientStackInertia.lean#L263). The attribute's comment: “the induced action on the fixed locus”.

> **Stacks 0374.** Because `G` is commutative, its action on `X` restricts to an action
> on the fixed locus `X^g`. This is what makes the quotient `[X^g/G]` of the source's formula
> meaningful.

```lean
def fixedPresheafAction (ρ : G →* Aut X) (g : G) : G →* Aut (fixedPresheaf (ρ g).asIso.hom)
```

**`AlgebraicGeometry.fixedQuotientStack`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/AbstractGroupQuotientStackInertia.lean, line 353](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/AbstractGroupQuotientStackInertia.lean#L353). The attribute's comment: “the quotient of the fixed locus”.

> **Stacks 0374.** The quotient `[X^g/G]` of the fixed locus `X^g` by `G`, formed by the
> construction of Stacks 0371 applied to `X^g` with its induced action.

```lean
abbrev fixedQuotientStack (g : G) : Type _
```

**`AlgebraicGeometry.inertiaSummand`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/AbstractGroupQuotientStackInertia.lean, line 405](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/AbstractGroupQuotientStackInertia.lean#L405). The attribute's comment: “the canonical functor to the inertia stack”.

> **Stacks 0374.** The canonical functor `[X^g/G] ⥤ I_{[X/G]}`: a torsor with an
> equivariant map to `X^g` is sent to the same torsor, mapping to `X`, together with the
> automorphism given by translation by `g`.

```lean
def inertiaSummand (g : G) :
    fixedQuotientStack B S hS G X ρ g ⥤ quotientInertia B S hS G X ρ
```

**`AlgebraicGeometry.inertiaSummandLift_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/AbstractGroupQuotientStackInertia.lean, line 514](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/AbstractGroupQuotientStackInertia.lean#L514). The attribute's comment: “the g-summand of the inertia stack”.

> **Stacks 0374.** `I_{[X/G]} = ∐_{g ∈ G} [X^g/G]`, summand by summand: for each `g ∈ G`
> the canonical functor is an equivalence from the quotient `[X^g/G]` of the fixed locus onto
> the part of the inertia stack of `[[X/G]]` on which the automorphism is translation by `g`.
> Objects correspond because `φ ∘ α = φ` says that `φ` factors through `X^g → X`, and
> morphisms correspond because a morphism of `[[X/G]]` is `G`-equivariant.

```lean
theorem inertiaSummandLift_isEquivalence (g : G) :
    (inertiaSummandLift (ρ := ρ) g).IsEquivalence
```

**`AlgebraicGeometry.inertiaSummandLift_comp_structure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/AbstractGroupQuotientStackInertia.lean, line 520](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/AbstractGroupQuotientStackInertia.lean#L520). The attribute's comment: “the g-summand is an equivalence over the base”.

> The equivalence of Stacks 0374 is an equivalence over `(Sch/S)_fppf`: it carries the
> projection of `[X^g/G]` to the structure functor of the inertia stack.

```lean
theorem inertiaSummandLift_comp_structure (g : G) :
    inertiaSummandLift (ρ := ρ) g ⋙ ObjectProperty.ι (IsTranslationBy (ρ := ρ) g) ⋙
        relativeInertiaStruct
          (AbstractGroupQuotientStack.projection (B := B) (S := S) (hS := hS) (G := G)
            (X := X) (ρ := ρ))
          (AbstractGroupQuotientStack.projection (B := B) (S := S) (hS := hS) (G := G)
            (X := X) (ρ := ρ)) =
      AbstractGroupQuotientStack.projection (B := B) (S := S) (hS := hS) (G := G)
        (X := fixedPresheaf (ρ g).asIso.hom) (ρ := fixedPresheafAction ρ g)
```

**`AlgebraicGeometry.inertiaCoproduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/AbstractGroupQuotientStackInertia.lean, line 535](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/AbstractGroupQuotientStackInertia.lean#L535). The attribute's comment: “the disjoint union of the quotients of the fixed loci”.

> **Stacks 0374.** The disjoint union `∐_{g ∈ G} [X^g/G]` of the quotients of the fixed
> loci, mapping to the inertia stack of `[[X/G]]`; on the `g`-summand this is
> `AlgebraicGeometry.inertiaSummand`.

```lean
def inertiaCoproduct :
    (Σ g : G, fixedQuotientStack B S hS G X ρ g) ⥤ quotientInertia B S hS G X ρ
```

**`AlgebraicGeometry.incl_comp_inertiaCoproduct_comp_structure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/AbstractGroupQuotientStackInertia.lean, line 546](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/AbstractGroupQuotientStackInertia.lean#L546). The attribute's comment: “the coproduct over the base”.

> The coproduct of Stacks 0374 maps to the inertia stack over `(Sch/S)_fppf`: on each
> summand it carries the projection of `[X^g/G]` to the structure functor of the inertia.

```lean
theorem incl_comp_inertiaCoproduct_comp_structure (g : G) :
    Sigma.incl g ⋙ inertiaCoproduct (ρ := ρ) ⋙
        relativeInertiaStruct
          (AbstractGroupQuotientStack.projection (B := B) (S := S) (hS := hS) (G := G)
            (X := X) (ρ := ρ))
          (AbstractGroupQuotientStack.projection (B := B) (S := S) (hS := hS) (G := G)
            (X := X) (ρ := ρ)) =
      AbstractGroupQuotientStack.projection (B := B) (S := S) (hS := hS) (G := G)
        (X := fixedPresheaf (ρ g).asIso.hom) (ρ := fixedPresheafAction ρ g)
```

**`AlgebraicGeometry.existsUnique_auto_eq_totalSmul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/AbstractGroupQuotientStackInertia.lean, line 563](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/AbstractGroupQuotientStackInertia.lean#L563). The attribute's comment: “the automorphism is a translation”.

> **Stacks 0374.** Conversely to `AlgebraicGeometry.inertiaSummand`: the automorphism `α`
> of an object `(P/T, φ, α)` of `I_{[X/G]}` is, at every section of its torsor, translation by
> a *unique* section of the constant sheaf of groups with value `G`. Commutativity of `G` is
> not needed for this step; what it buys is that the section is independent of the chosen
> point, which is why the summands of the formula are indexed by `G`.

```lean
theorem existsUnique_auto_eq_totalSmul (Z : quotientInertia B S hS G X ρ)
    (V : (BigFppfOver B S hS)ᵒᵖ) (p : Z.obj.Total V) :
    ∃! γ : (constantSheafOfGroups (BigFppfOver.topology B S hS) G).presheaf.obj V,
      Z.obj.totalSmul γ p = Z.auto.asIso.hom.map V p
```

## Tag 0375, an example

[Tag 0375](https://stacks.math.columbia.edu/tag/0375) in the Stacks Project.

**`AlgebraicGeometry.Space.verticalEquivAut`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStackInertia.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PicardStackInertia.lean#L194). The attribute's comment: “the points of the inertia stack of the Picard stack over a test scheme are the pairs of an invertible module on the base change and an automorphism of it”.

> **The data `α` of a point `(L, α)` of the inertia stack of `Picardstack_{X/B}` is an
> automorphism of the invertible module `L`.**
>
> A morphism of `Picardstack_{X/B}` from `(U, b, L)` to itself consists of a base map and an
> isomorphism `(X_{base})^*L ⟶ L`; when the base map is the identity the unit comparison
> `(X_{𝟙 U})^* ≅ 𝟭` of Stacks 03LU turns that isomorphism into an automorphism of `L`, and every
> automorphism of `L` arises from exactly one such morphism.

```lean
def verticalEquivAut (hc : ModulePushforwardCoherence B S hS) {s : PicardSituation B S hS}
    (A : PicardObject s) : A.Vertical ≃ (A.lineBundle ≅ A.lineBundle)
```

**`AlgebraicGeometry.Space.autLineBundleMulEquivAutStructure`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStackInertia.lean, line 242](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PicardStackInertia.lean#L242). The attribute's comment: “an automorphism of an invertible module on the base change is an invertible global function on the base change, so the automorphism group is independent of the module”.

> **The automorphism group of the invertible module of an object of `Picardstack_{X/B}` is the
> automorphism group of the structure sheaf of the base change.**

```lean
def autLineBundleMulEquivAutStructure {s : PicardSituation B S hS} (A : PicardObject s) :
    Aut A.lineBundle ≃* Aut (structureModule (s.baseChange A.T))
```

**`AlgebraicGeometry.Space.PicardObject.autMulEquivMultiplicativeGroupPoints`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStackInertia.lean, line 692](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PicardStackInertia.lean#L692). The attribute's comment: “the 𝐆\_m factor of the inertia stack: when 𝒪\_T ⟶ f\_\{T,*}𝒪\_\{X\_T} is an isomorphism for every test scheme T, the automorphism group of the invertible module of an object of the Picard stack over T is 𝐆\_\{m,S}(T)”.

> **The `𝐆_m` factor of the inertia stack, as an explicit isomorphism of groups.** When
> `𝒪_T ⟶ f_{T, *}𝒪_{X_T}` is an isomorphism for every test scheme `T`, the automorphism group of the
> invertible module of an object of `Picardstack_{X/B}` over `T` is `𝐆_{m, S}(T)`: an automorphism
> is multiplication by a unique invertible regular function on `T`
> (`AlgebraicGeometry.Space.PicardObject.bijective_unitsToAut`), and `H^0(T, 𝒪_T^*)` is
> `𝐆_{m, S}(T)` by Stacks 022U.

```lean
def autMulEquivMultiplicativeGroupPoints (h : s.StructureSheafMapIso) (A : PicardObject s) :
    Aut A.lineBundle ≃* multiplicativeGroupPointsAt B S hS A.T.left
```

**`AlgebraicGeometry.Space.PicardObject.verticalEquivMultiplicativeGroupPoints`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStackInertia.lean, line 718](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PicardStackInertia.lean#L718). The attribute's comment: “the points of the inertia stack above an object of the Picard stack over T are 𝐆\_\{m,S}(T), when 𝒪\_T ⟶ f\_\{T,*}𝒪\_\{X\_T} is an isomorphism for every test scheme T”.

> **The points of the inertia stack.** When `𝒪_T ⟶ f_{T, *}𝒪_{X_T}` is an
> isomorphism for every test scheme `T`, the endomorphisms of an object `(T, b, L)` of
> `Picardstack_{X/B}` lying over the identity of `T` — the points `(L, α)` of the inertia stack above
> it — are the points `𝐆_{m, S}(T)` of the multiplicative group: `α` is an automorphism of `L`
> (`AlgebraicGeometry.Space.verticalEquivAut`, for the comparisons of Stacks 03LU of the library,
> `AlgebraicGeometry.Space.modulePushforwardCoherence`), which is multiplication by a unique
> invertible function on `T`
> (`AlgebraicGeometry.Space.PicardObject.autMulEquivMultiplicativeGroupPoints`).

```lean
def verticalEquivMultiplicativeGroupPoints (h : s.StructureSheafMapIso) (A : PicardObject s) :
    A.Vertical ≃ multiplicativeGroupPointsAt B S hS A.T.left
```

**`AlgebraicGeometry.Space.nonempty_autLineBundle_mulEquiv_multiplicativeGroupPoints_of_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStackInertiaCoordinates.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PicardStackInertiaCoordinates.lean#L241). The attribute's comment: “the 𝐆\_m factor of the inertia stack: under the hypothesis that 𝒪\_T ⟶ f\_\{T,*}𝒪\_\{X\_T} is an isomorphism for every test scheme T, the automorphism group of the invertible module of an object of the Picard stack over T is 𝐆\_\{m,S}(T)”.

> **The `𝐆_m` factor of the inertia stack.**  Assume that for every test scheme `T`
> over the base the structure map `𝒪_T ⟶ f_{T, *}𝒪_{X_T}` of the base change is an isomorphism.
> Then for every object `(U, b, L)` of `Picardstack_{X/B}` the automorphism group of `L` is the
> group `𝐆_{m, S}(U)`.

```lean
theorem nonempty_autLineBundle_mulEquiv_multiplicativeGroupPoints_of_iso
    (h : s.StructureSheafMapIso) (A : PicardObject s) :
    Nonempty (Aut A.lineBundle ≃* multiplicativeGroupPointsAt B S hS A.T.left)
```

**`AlgebraicGeometry.Space.nonempty_vertical_equiv_multiplicativeGroupPoints_of_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStackInertiaCoordinates.lean, line 254](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PicardStackInertiaCoordinates.lean#L254). The attribute's comment: “the points of the inertia stack above an object of the Picard stack over T are 𝐆\_\{m,S}(T), under the hypothesis that 𝒪\_T ⟶ f\_\{T,*}𝒪\_\{X\_T} is an isomorphism for every test scheme T”.

> **The points of the inertia stack.**  Assume that for every test scheme `T` over the base the
> structure map `𝒪_T ⟶ f_{T, *}𝒪_{X_T}` of the base change is an isomorphism.  Then the
> endomorphisms of an object `(U, b, L)` of `Picardstack_{X/B}` lying over the identity of `U` — the
> points of the inertia stack above it — are the points `𝐆_{m, S}(U)`.

```lean
theorem nonempty_vertical_equiv_multiplicativeGroupPoints_of_iso
    (hc : ModulePushforwardCoherence B S hS) (h : s.StructureSheafMapIso) (A : PicardObject s) :
    Nonempty (A.Vertical ≃ multiplicativeGroupPointsAt B S hS A.T.left)
```

**`AlgebraicGeometry.Space.nonempty_equivalenceOver_picardInertia_multiplicativeGroupProduct_of_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStackInertiaCoordinates.lean, line 471](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PicardStackInertiaCoordinates.lean#L471). The attribute's comment: “the inertia stack of the Picard stack is 𝐆\_\{m,S} ×\_S Picardstack\_\{X/B}, as categories over (Sch/S)\_fppf, when 𝒪\_T ⟶ f\_\{T,*}𝒪\_\{X\_T} is an isomorphism for every test scheme T”.

> Let `f : X ⟶ B` be a morphism of algebraic spaces over `S` such that for
> every scheme `T` over `B` the structure map `𝒪_T ⟶ f_{T, *}𝒪_{X_T}` of the base change
> `f_T : X_T ⟶ T` is an isomorphism.  Then the inertia stack of the Picard stack
> `Picardstack_{X/B}` of Section 0372 is
>
> `I_{Picardstack_{X/B}} = 𝐆_{m, S} ×_S Picardstack_{X/B}`
>
> as a category over `(Sch/S)_fppf`: the two are equivalent over the big fppf site, by an
> equivalence which is the identity on the `Picardstack_{X/B}`-factor and sends a point `(L, α)` of
> the inertia over `T` to the point of `𝐆_{m, S}(T) = H^0(T, 𝒪_T^*)` that the automorphism `α` of
> `L` is multiplication by.
>
> In Stacks 0375 `f` is a morphism of schemes; here it is a morphism of algebraic spaces, which
> contains that case.  "Equal" is read as an equivalence over the site
> (`CategoryTheory.StacksRepresentableCFG.EquivalenceOver`), and the product is the 2-fibre product
> `CategoryTheory.inertiaPresheafProduct` of the category of elements of `𝐆_{m, S}` with
> `Picardstack_{X/B}` over the site.

```lean
theorem nonempty_equivalenceOver_picardInertia_multiplicativeGroupProduct_of_iso
    (s : PicardSituation B S hS) (h : s.StructureSheafMapIso) :
    letI : Category.{u + 1} (PicardObject s) :=
      (picardCategoryData (modulePushforwardCoherence B S hS) s).category
    Nonempty (StacksRepresentableCFG.EquivalenceOver
      (relativeInertiaStruct
        (picardCategoryData (modulePushforwardCoherence B S hS) s).siteProjection
        (picardCategoryData (modulePushforwardCoherence B S hS) s).siteProjection)
      (inertiaPresheafProductStruct
        (picardCategoryData (modulePushforwardCoherence B S hS) s).siteProjection
        (multiplicativeGroupPresheaf B S hS)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 95.17, Tag 0373](https://stacks.math.columbia.edu/tag/0373)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
