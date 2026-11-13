---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.fibreProductCotangentCorner, AlgebraicGeometry.Space.fiberProductCotangentCorner, AlgebraicGeometry.Space.fiberProduct_cotangentComplex_of_torIndependent, AlgebraicGeometry.Space.upperRightCorner_homology, AlgebraicGeometry.Space.fiberProduct_upperRightCorner_homology
statement: formalized
proof: formalized
---

# 92.28 Fibre products of algebraic spaces and the cotangent complex

Section 92.28 of the Stacks Project, [Tag 09DJ](https://stacks.math.columbia.edu/tag/09DJ). 3 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 09DK, an equation

[Tag 09DK](https://stacks.math.columbia.edu/tag/09DK) in the Stacks Project.

**`AlgebraicGeometry.Space.fibreProductCotangentCorner`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Spaces/FibreProductCorner.lean, line 156](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/Spaces/FibreProductCorner.lean#L156). The attribute's comment: “the diagram for a commutative square, in particular for the two projections of a fibre product; `E` is the cone of the map out of the direct sum”.

> **Stacks 09DK.** Let `p : W ⟶ X` and `q : W ⟶ Y` be morphisms of algebraic spaces over `S`
> with `p ≫ f = q ≫ g` for morphisms `f : X ⟶ Z` and `g : Y ⟶ Z`, for instance the two projections
> of `W = X ×_Z Y`. In `D(𝒪_W)` the diagram
>
> ```
> Lp^*L_{X/Z} ──────▶ L_{W/Y} ──────▶ E
>      ‖                ▲             ▲
> Lp^*L_{X/Z} ──────▶ L_{W/Z} ──────▶ L_{W/X}
>                       ▲             ▲
>                 Lq^*L_{Y/Z} ═════ Lq^*L_{Y/Z}
> ```
>
> exists: its middle row is the transitivity triangle of Stacks 08V1 for `W ⟶ X ⟶ Z`, its middle
> column the one for `W ⟶ Y ⟶ Z`, and the object `E` of the upper right corner, with its two
> incoming and two outgoing arrows, turns the top row and the right column into distinguished
> triangles and makes the remaining square commute. The value of the definition is that upper
> right corner, together with the distinguishedness of the two middle triangles and the triangle
> `Lp^*L_{X/Z} ⊕ Lq^*L_{Y/Z} ⟶ L_{W/Z} ⟶ E ⟶`, which exhibits `E` as the cone of the map out of
> the direct sum.

```lean
noncomputable def fibreProductCotangentCorner (h : p ≫ f = q ≫ g) :
    { E : Triangulated.UpperRightCorner (transitivityUnit p f) (transitivityCounit p f)
          (fibreProductColumnUnit h) (fibreProductColumnCounit h) //
      (∃ δ : cotangentComplexDerived B S hS p ⟶
          ((derivedPullbackULift p).obj (cotangentComplexDerived B S hS f))⟦(1 : ℤ)⟧,
        Triangle.mk (transitivityUnit p f) (transitivityCounit p f) δ ∈
          distTriang (DerivedCategory (smallEtaleModulesULift B S hS W))) ∧
      (∃ δ : cotangentComplexDerived B S hS q ⟶
          ((derivedPullbackULift q).obj (cotangentComplexDerived B S hS g))⟦(1 : ℤ)⟧,
        Triangle.mk (fibreProductColumnUnit h) (fibreProductColumnCounit h) δ ∈
          distTriang (DerivedCategory (smallEtaleModulesULift B S hS W))) ∧
      ∃ (ε : cotangentComplexDerived B S hS (p ≫ f) ⟶ E.obj)
        (ζ : E.obj ⟶ ((derivedPullbackULift p).obj (cotangentComplexDerived B S hS f) ⊞
          (derivedPullbackULift q).obj (cotangentComplexDerived B S hS g))⟦(1 : ℤ)⟧),
        Triangle.mk (fibreProductBiprodMap h) ε ζ ∈
          distTriang (DerivedCategory (smallEtaleModulesULift B S hS W)) }
```

**`AlgebraicGeometry.Space.fiberProductCotangentCorner`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Spaces/FibreProductCorner.lean, line 192](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/Spaces/FibreProductCorner.lean#L192). The attribute's comment: “the diagram for the fibre product `X ×_Z Y` and its two projections; `E` is the cone of the map out of the direct sum”.

> **Stacks 09DK**, for the fibre product `X ×_Z Y` of algebraic spaces (Stacks 02X2) with its
> projections `p` and `q`: the diagram of
> `AlgebraicGeometry.Space.fibreProductCotangentCorner` in `D(𝒪_{X ×_Z Y})`, built on the
> transitivity triangles of `X ×_Z Y ⟶ X ⟶ Z` and `X ×_Z Y ⟶ Y ⟶ Z`, with `E` a cone of the map
> `Lp^*L_{X/Z} ⊕ Lq^*L_{Y/Z} ⟶ L_{X ×_Z Y/Z}`.

```lean
noncomputable def fiberProductCotangentCorner
```

## Tag 09DL, a lemma

[Tag 09DL](https://stacks.math.columbia.edu/tag/09DL) in the Stacks Project.

**`AlgebraicGeometry.Space.fiberProduct_cotangentComplex_of_torIndependent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Spaces/FibreProductTorIndependent.lean, line 331](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/Spaces/FibreProductTorIndependent.lean#L331).

> **Stacks 09DL.** Let `X ⟶ Z` and `Y ⟶ Z` be morphisms of algebraic spaces over `S`, and let
> `W = X ×_Z Y` with projections `p` and `q`. If `X` and `Y` are Tor independent over `Z`, then the
> object `E` of Stacks 09DK, i.e. any object fitting into the upper right corner of its diagram, is
> zero, and the canonical map `Lp^*L_{X/Z} ⊕ Lq^*L_{Y/Z} ⟶ L_{W/Z}` is an isomorphism, so that
> `L_{X ×_Z Y/Z} ≅ Lp^*L_{X/Z} ⊕ Lq^*L_{Y/Z}`.

```lean
theorem fiberProduct_cotangentComplex_of_torIndependent (f : X ⟶ Z) (g : Y ⟶ Z)
    (hTor : TorIndependent X.2 Y.2 Z.2 f.hom g.hom) :
    (∀ E : Triangulated.UpperRightCorner (transitivityUnit (ObjectProperty.homMk (pullback.fst
        f.hom g.hom) : (AlgebraicSpaces.fiberProduct B S hS f g) ⟶ X) f) (transitivityCounit
            (ObjectProperty.homMk (pullback.fst f.hom g.hom) : (AlgebraicSpaces.fiberProduct B S hS
                f g) ⟶ X) f)
      (fibreProductColumnUnit (AlgebraicSpaces.isPullback_fiberProduct B S hS f g).w)
      (fibreProductColumnCounit (AlgebraicSpaces.isPullback_fiberProduct B S hS f g).w),
      IsZero E.obj) ∧
    IsIso (fibreProductBiprodMap (AlgebraicSpaces.isPullback_fiberProduct B S hS f g).w)
```

## Tag 09DM, a lemma

[Tag 09DM](https://stacks.math.columbia.edu/tag/09DM) in the Stacks Project.

**`AlgebraicGeometry.Space.upperRightCorner_homology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Spaces/FibreProductCornerCohomology.lean, line 303](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/Spaces/FibreProductCornerCohomology.lean#L303). The attribute's comment: “for every cartesian square of algebraic spaces, in particular for the fibre product with its two projections (`fiberProduct_upperRightCorner_homology`), and every object E fitting into the upper right corner of the diagram of 09DK”.

> **Stacks 09DM, for a cartesian square.** Let `p : W ⟶ X`, `q : W ⟶ Y`, `f : X ⟶ Z`,
> `g : Y ⟶ Z` be a cartesian square of algebraic spaces over `S` and let `E` be an object fitting
> into the upper right corner of the diagram of Stacks 09DK. Then `H^0(E) = H^{-1}(E) = 0`, and at
> every geometric point `w̄` of `W`, with `R = 𝒪_{Z, f(p(w̄))}`, `A = 𝒪_{X, p(w̄)}`,
> `B = 𝒪_{Y, q(w̄)}` and `C = 𝒪_{W, w̄}` the étale local rings and the canonical maps between them,
> `H^{-2}(E)_{w̄} ≅ Tor_1^R(A, B) ⊗_{A ⊗_R B} C` as `C`-modules, `χ : A ⊗_R B → C` being the map
> induced by the canonical maps `A → C` and `B → C`. The stalk `H^{-2}(E)_{w̄}` is a module over the
> stalk of the structure sheaf, which is identified with `C` by
> `AlgebraicGeometry.Space.smallEtaleStructureSheafULiftStalkEquiv`.

```lean
theorem upperRightCorner_homology (hpb : IsPullback p q f g)
    (E : Triangulated.UpperRightCorner (transitivityUnit p f) (transitivityCounit p f)
      (fibreProductColumnUnit hpb.w) (fibreProductColumnCounit hpb.w)) :
    IsZero ((DerivedCategory.homologyFunctor (smallEtaleModulesULift B S hS W) 0).obj E.obj) ∧
    IsZero ((DerivedCategory.homologyFunctor (smallEtaleModulesULift B S hS W) (-1)).obj E.obj) ∧
    ∀ w : GeometricPoint B S hS W.1,
    letI : Algebra (etaleLocalRing B S hS Z.1 (geometricPointMap f.hom (geometricPointMap p.hom w)))
        (etaleLocalRing B S hS X.1 (geometricPointMap p.hom w)) :=
      (etaleLocalRingMap X.2 f.hom (geometricPointMap p.hom w)).toAlgebra
    letI : Algebra (etaleLocalRing B S hS Z.1 (geometricPointMap f.hom (geometricPointMap p.hom w)))
        (etaleLocalRing B S hS Y.1 (geometricPointMap q.hom w)) :=
      ((eqToHom (congrArg (etaleLocalRing B S hS Z.1)
          (congrArg (fun k : W ⟶ Z => geometricPointMap k.hom w) hpb.w)) ≫
        CommRingCat.ofHom (etaleLocalRingMap Y.2 g.hom (geometricPointMap q.hom w))).hom).toAlgebra
    ∃ χ : etaleLocalRing B S hS X.1 (geometricPointMap p.hom w) ⊗[etaleLocalRing B S hS Z.1
        (geometricPointMap f.hom (geometricPointMap p.hom w))]
        etaleLocalRing B S hS Y.1 (geometricPointMap q.hom w) →+* etaleLocalRing B S hS W.1 w,
      χ.comp Algebra.TensorProduct.includeLeftRingHom = etaleLocalRingMap W.2 p.hom w ∧
      χ.comp Algebra.TensorProduct.includeRight.toRingHom = etaleLocalRingMap W.2 q.hom w ∧
      Nonempty ((ModuleCat.extendScalars.{u + 1, u + 1, u + 1}
          (smallEtaleStructureSheafULiftStalkEquiv B S hS W w).toRingHom).obj
          ((Stacks.sheafModuleFiberOfCommRing (geometricSitePoint B S hS W w)
            (smallEtaleStructureSheafULift B S hS W)).obj
            ((DerivedCategory.homologyFunctor (smallEtaleModulesULift B S hS W) (-2)).obj E.obj)) ≅
        (ModuleCat.extendScalars.{u + 1, u + 1, u + 1} χ).obj
          (CommAlgCat.torOneTensorProductModule _ _ _))
```

**`AlgebraicGeometry.Space.fiberProduct_upperRightCorner_homology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Spaces/FibreProductCornerCohomology.lean, line 346](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/Spaces/FibreProductCornerCohomology.lean#L346). The attribute's comment: “for the fibre product X ×\_Z Y with its two projections and every object E fitting into the upper right corner of the diagram of 09DK: H^0(E) = H^\{-1}(E) = 0, and H^\{-2}(E)\_w ≅ Tor\_1^R(A, B) ⊗\_\{A ⊗\_R B} C as C-modules for the etale local rings R, A, B, C”.

> **Stacks 09DM.** Let `X ⟶ Z` and `Y ⟶ Z` be morphisms of algebraic spaces over `S`, let
> `W = X ×_Z Y` with projections `p` and `q`, and let `E` be the object of Stacks 09DK, i.e. any
> object fitting into the upper right corner of its diagram. Then `H^0(E) = H^{-1}(E) = 0`, and
> for a geometric point `w̄` of `W`,
> `H^{-2}(E)_{w̄} ≅ Tor_1^R(A, B) ⊗_{A ⊗_R B} C` as `C`-modules, where `R = 𝒪_{Z, f(p(w̄))}`,
> `A = 𝒪_{X, p(w̄)}`, `B = 𝒪_{Y, q(w̄)}` and `C = 𝒪_{W, w̄}` are the étale local rings,
> `Tor_1^R(A, B)` carries its canonical `A ⊗_R B`-module structure, and `χ : A ⊗_R B → C` is the map
> induced by the canonical maps of étale local rings.

```lean
theorem fiberProduct_upperRightCorner_homology (f : X ⟶ Z) (g : Y ⟶ Z) :
    ∀ E : Triangulated.UpperRightCorner (transitivityUnit (ObjectProperty.homMk (pullback.fst f.hom
        g.hom) : (AlgebraicSpaces.fiberProduct B S hS f g) ⟶ X) f) (transitivityCounit
            (ObjectProperty.homMk (pullback.fst f.hom g.hom) : (AlgebraicSpaces.fiberProduct B S hS
                f g) ⟶ X) f)
      (fibreProductColumnUnit (AlgebraicSpaces.isPullback_fiberProduct B S hS f g).w)
      (fibreProductColumnCounit (AlgebraicSpaces.isPullback_fiberProduct B S hS f g).w),
      IsZero ((DerivedCategory.homologyFunctor (smallEtaleModulesULift B S hS
          (AlgebraicSpaces.fiberProduct B S hS f g)) 0).obj E.obj) ∧
      IsZero ((DerivedCategory.homologyFunctor (smallEtaleModulesULift B S hS
          (AlgebraicSpaces.fiberProduct B S hS f g)) (-1)).obj E.obj) ∧
      ∀ w : GeometricPoint B S hS (AlgebraicSpaces.fiberProduct B S hS f g).1,
      letI : Algebra (etaleLocalRing B S hS Z.1 (geometricPointMap f.hom (geometricPointMap
          (ObjectProperty.homMk (pullback.fst f.hom g.hom) : (AlgebraicSpaces.fiberProduct B S hS f
              g) ⟶ X).hom w)))
          (etaleLocalRing B S hS X.1 (geometricPointMap (ObjectProperty.homMk (pullback.fst f.hom
              g.hom) : (AlgebraicSpaces.fiberProduct B S hS f g) ⟶ X).hom w)) :=
        (etaleLocalRingMap X.2 f.hom (geometricPointMap (ObjectProperty.homMk (pullback.fst f.hom
            g.hom) : (AlgebraicSpaces.fiberProduct B S hS f g) ⟶ X).hom w)).toAlgebra
      letI : Algebra (etaleLocalRing B S hS Z.1 (geometricPointMap f.hom (geometricPointMap
          (ObjectProperty.homMk (pullback.fst f.hom g.hom) : (AlgebraicSpaces.fiberProduct B S hS f
              g) ⟶ X).hom w)))
          (etaleLocalRing B S hS Y.1 (geometricPointMap (ObjectProperty.homMk (pullback.snd f.hom
              g.hom) : (AlgebraicSpaces.fiberProduct B S hS f g) ⟶ Y).hom w)) :=
        ((eqToHom (congrArg (etaleLocalRing B S hS Z.1)
            (congrArg (fun k : (AlgebraicSpaces.fiberProduct B S hS f g) ⟶ Z => geometricPointMap
                k.hom w) (AlgebraicSpaces.isPullback_fiberProduct B S hS f g).w)) ≫
          CommRingCat.ofHom (etaleLocalRingMap Y.2 g.hom (geometricPointMap (ObjectProperty.homMk
              (pullback.snd f.hom g.hom) : (AlgebraicSpaces.fiberProduct B S hS f g) ⟶ Y).hom
                  w))).hom).toAlgebra
      ∃ χ : etaleLocalRing B S hS X.1 (geometricPointMap (ObjectProperty.homMk (pullback.fst f.hom
          g.hom) : (AlgebraicSpaces.fiberProduct B S hS f g) ⟶ X).hom w) ⊗[etaleLocalRing B S hS Z.1
          (geometricPointMap f.hom (geometricPointMap (ObjectProperty.homMk (pullback.fst f.hom
              g.hom) : (AlgebraicSpaces.fiberProduct B S hS f g) ⟶ X).hom w))]
          etaleLocalRing B S hS Y.1 (geometricPointMap (ObjectProperty.homMk (pullback.snd f.hom
              g.hom) : (AlgebraicSpaces.fiberProduct B S hS f g) ⟶ Y).hom w) →+* etaleLocalRing B S
                  hS (AlgebraicSpaces.fiberProduct B S hS f g).1 w,
        χ.comp Algebra.TensorProduct.includeLeftRingHom = etaleLocalRingMap
            (AlgebraicSpaces.fiberProduct B S hS f g).2 (ObjectProperty.homMk (pullback.fst f.hom
                g.hom) : (AlgebraicSpaces.fiberProduct B S hS f g) ⟶ X).hom w ∧
        χ.comp Algebra.TensorProduct.includeRight.toRingHom = etaleLocalRingMap
            (AlgebraicSpaces.fiberProduct B S hS f g).2 (ObjectProperty.homMk (pullback.snd f.hom
                g.hom) : (AlgebraicSpaces.fiberProduct B S hS f g) ⟶ Y).hom w ∧
        Nonempty ((ModuleCat.extendScalars.{u + 1, u + 1, u + 1}
            (smallEtaleStructureSheafULiftStalkEquiv B S hS (AlgebraicSpaces.fiberProduct B S hS f
                g) w).toRingHom).obj
            ((Stacks.sheafModuleFiberOfCommRing (geometricSitePoint B S hS
                (AlgebraicSpaces.fiberProduct B S hS f g) w)
              (smallEtaleStructureSheafULift B S hS (AlgebraicSpaces.fiberProduct B S hS f g))).obj
              ((DerivedCategory.homologyFunctor (smallEtaleModulesULift B S hS
                  (AlgebraicSpaces.fiberProduct B S hS f g)) (-2)).obj E.obj)) ≅
          (ModuleCat.extendScalars.{u + 1, u + 1, u + 1} χ).obj
            (CommAlgCat.torOneTensorProductModule _ _ _))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 92.28, Tag 09DJ](https://stacks.math.columbia.edu/tag/09DJ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
