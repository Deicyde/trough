---
declaration: section
origin: cited
lean: Stacks.SheafOfModules.isBilinearPairing_iff_moduleObj_isBilinear, Stacks.SheafOfModules.isBilinearPairing_iff_forall_exists_linearMap, Stacks.SheafOfModules.isBilinearPairing_iff_stalk, Stacks.SheafOfModules.isBilinearPairing_iff_forall_coyoneda, Stacks.SheafOfModules.IsBilinearPairing, Stacks.SheafOfModules.isBilinearPairing_iff_squares
statement: formalized
proof: formalized
---

# 17.15 Bilinear maps

Section 17.15 of the Stacks Project, [Tag 0GIG](https://stacks.math.columbia.edu/tag/0GIG). 1 tag here is carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0GIG, the section

[Tag 0GIG](https://stacks.math.columbia.edu/tag/0GIG) in the Stacks Project.

**`Stacks.SheafOfModules.isBilinearPairing_iff_moduleObj_isBilinear`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/BilinearModuleObj.lean, line 202](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/BilinearModuleObj.lean#L202). The attribute's comment: “the fifth characterisation of the section: `O_X` is a ring object in the category of sheaves of sets, `F`, `G`, `H` are module objects over it, and a bilinear map `F x G -> H` of sheaves of modules is the same thing as a bilinear map of module objects over a ring object, the notion `CategoryTheory.ModuleObj.IsBilinear` defined for module objects over a ring object in any category with finite products (a cartesian monoidal category). The ring and module objects are `Stacks.sheafCommRingObj` and `Stacks.sheafModuleObj`. Over an arbitrary site rather than only the opens of a ringed space”.

> **Bilinear maps of sheaves of modules are bilinear maps of module objects.** Let `O` be a sheaf
> of commutative rings. Its underlying sheaf of sets is a ring object in the category of sheaves of
> sets, and the underlying sheaves of sets of `O`-modules `A`, `B`, `N` are module objects over it.
> A map `q : A × B → N` of sheaves of sets is a bilinear map of sheaves of `O`-modules if and only if
> it is a bilinear map of these module objects.

```lean
theorem isBilinearPairing_iff_moduleObj_isBilinear
    {A B N : _root_.SheafOfModules.{w} (Tensor.ringSheaf O)}
    (q : moduleSheaf (Tensor.ringSheaf O) A ⨯ moduleSheaf (Tensor.ringSheaf O) B ⟶
      moduleSheaf (Tensor.ringSheaf O) N) :
    IsBilinearPairing (Tensor.ringSheaf O) q ↔
      letI := hasSheafCompose_forget₂_commRingCat.{w} J
      letI := sheafCommRingObj J O
      letI := sheafModuleObj J O A
      letI := sheafModuleObj J O B
      letI := sheafModuleObj J O N
      ModuleObj.IsBilinear (underlyingRingSheaf J O) (F := underlyingModuleSheaf J A)
        (G := underlyingModuleSheaf J B) (H := underlyingModuleSheaf J N) q
```

**`Stacks.SheafOfModules.isBilinearPairing_iff_forall_exists_linearMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/BilinearSections.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/BilinearSections.lean#L53). The attribute's comment: “the definition of the section: a bilinear map `F x G -> H` of sheaves of `O_X`-modules is a map of sheaves of sets such that for every open `U` the induced map `F(U) x G(U) -> H(U)` is an `O_X(U)`-bilinear map of modules; here `IsBilinearPairing`, the condition the rest of the section is phrased in, is shown to be exactly that, with `O_X(U)`-bilinear meaning given by an `O_X(U)`-linear map `F(U) -> Hom(G(U), H(U))`. Over an arbitrary site rather than only the opens of a ringed space”.

> **Bilinearity is bilinearity on sections.** A map `q : A × B → N` of the underlying sheaves of
> sets of three sheaves of modules over a sheaf of commutative rings `O` is a bilinear map of sheaves
> of `O`-modules if and only if, for every object `U`, the induced map `A(U) × B(U) → N(U)` is an
> `O(U)`-bilinear map of modules.

```lean
theorem isBilinearPairing_iff_forall_exists_linearMap
    (q : moduleSheaf (Tensor.ringSheaf O) A ⨯ moduleSheaf (Tensor.ringSheaf O) B ⟶
      moduleSheaf (Tensor.ringSheaf O) N) :
    IsBilinearPairing (Tensor.ringSheaf O) q ↔
      ∀ U : Cᵒᵖ, ∃ φ : A.val.obj U →ₗ[(Tensor.ringSheaf O).obj.obj U]
          B.val.obj U →ₗ[(Tensor.ringSheaf O).obj.obj U] N.val.obj U,
        ∀ (a : A.val.obj U) (b : B.val.obj U), φ a b = pairingApp (Tensor.ringSheaf O) q U a b
```

**`Stacks.SheafOfModules.isBilinearPairing_iff_stalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/BilinearStalk.lean, line 281](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/BilinearStalk.lean#L281). The attribute's comment: “the third characterisation of the section: a map of the underlying sheaves of sets which induces a bilinear map of modules on the stalk at every point of `X` is bilinear, and conversely. The stalk is taken in the shape the site gives it, the fibre functor at the point of `Opens X` determined by `x`, which `Opens.pointFiberStalkFunctorIso` identifies with the ordinary stalk; its module structure over the stalk of `O_X` is the one `CategoryTheory.Sheaf.moduleObjModule` transports. Over a not necessarily commutative sheaf of rings. The forward direction is proved for every finite-product-preserving functor to types, as `IsBilinearPairing.isBilinearPairingObj`, and the converse over any site with a conservative family of points, as `isBilinearPairing_iff_forall_sheafFiber`; the points of a topological space are such a family, so this statement carries no hypothesis of its own beyond the standing binders of the section”.

> **The stalk characterisation of bilinearity.** A pairing of the underlying sheaves of sets
> of three sheaves of modules on a topological space is bilinear if and only if the map it induces
> on the stalks at a point is bilinear over the stalk of the sheaf of rings, at every point.
>
> This is the third assertion of the section [Stacks, Tag 0GIG]. The forward direction is
> `IsBilinearPairing.isBilinearPairingObj` and needs nothing of the space; the converse is
> `isBilinearPairing_of_forall_sheafFiber` at the conservative family of points that a
> topological space provides.

```lean
theorem isBilinearPairing_iff_stalk :
    IsBilinearPairing R q ↔ ∀ x : X, IsBilinearPairingObj R q (stalkTypeFunctor x)
```

**`Stacks.SheafOfModules.isBilinearPairing_iff_forall_coyoneda`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/BilinearYoneda.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/BilinearYoneda.lean#L108). The attribute's comment: “the fourth characterisation of the section: a pairing is bilinear if and only if for every sheaf of sets `S` the induced rule `Mor(S, F) x Mor(S, G) -> Mor(S, H)` is bilinear over the ring `Mor(S, O_X)`. The ring and module structures on those morphism sets are the ones `CategoryTheory.Sheaf.ringObjRing` and `CategoryTheory.Sheaf.moduleObjModule` transport along `Mor(S, -)`, which preserves finite products. Over an arbitrary site rather than only the opens of a ringed space, and over a not necessarily commutative sheaf of rings. The forward direction is `IsBilinearPairing.isBilinearPairingObj`; the converse needs only the single `S` which is the source of each of the four squares, with the three arguments taken to be the projections out of it”.

> **The Yoneda characterisation of bilinearity.** A pairing of the underlying sheaves of sets
> is bilinear if and only if the rule it induces on morphisms from an arbitrary sheaf of sets `S`
> is bilinear over the ring of morphisms from `S` to the sheaf of rings.

```lean
theorem isBilinearPairing_iff_forall_coyoneda :
    IsBilinearPairing R q ↔
      ∀ S : Sheaf J (Type w), IsBilinearPairingObj R q (coyoneda.obj (op S))
```

**`Stacks.SheafOfModules.IsBilinearPairing`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorBilinear.lean, line 272](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorBilinear.lean#L272). The attribute's comment: “the definition of the section: a bilinear map `F × G → H` of sheaves of modules is a map of the underlying sheaves of sets whose induced map `F(U) × G(U) → H(U)` on sections is `O_X(U)`-bilinear for every `U`. Over an arbitrary site rather than only the opens of a ringed space, and over a not necessarily commutative sheaf of rings”.

> A morphism from the product of the underlying sheaves of sets of two sheaves of modules to
> that of a third is **bilinear** when, on local sections, it is additive and compatible with
> scalar multiplication in each of its two arguments. This is the condition defining
> `Bilin_O(A × B, N)` in Stacks 18.26.

```lean
structure IsBilinearPairing (q : moduleSheaf R A ⨯ moduleSheaf R B ⟶ moduleSheaf R N) :
    Prop
```

**`Stacks.SheafOfModules.isBilinearPairing_iff_squares`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorBilinear.lean, line 390](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorBilinear.lean#L390). The attribute's comment: “the second characterisation of the section: a pairing is bilinear if and only if certain diagrams of maps of sheaves of sets commute, imitating the usual axioms for bilinear maps of modules. The diagram displayed in the section, for `f(x + y, z) = f(x, z) + f(y, z)`, is `addLeftSquare`. Over an arbitrary site rather than only the opens of a ringed space”.

> Bilinearity of a pairing is equivalent to the four commuting squares.

```lean
lemma isBilinearPairing_iff_squares :
    IsBilinearPairing R q ↔ addLeftSquare R q ∧ addRightSquare R q ∧
      smulLeftSquare R q ∧ smulRightSquare R q
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 17.15, Tag 0GIG](https://stacks.math.columbia.edu/tag/0GIG)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
