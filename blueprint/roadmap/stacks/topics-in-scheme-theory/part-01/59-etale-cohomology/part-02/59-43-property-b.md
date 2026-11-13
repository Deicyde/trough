---
declaration: section
origin: cited
lean: Stacks.EtaleCohomology.smallEtalePushforward_preservesEpimorphisms_of_hasPropertyB, Stacks.EtaleCohomology.hasPropertyB_of_etaleNeighborhood_decomposition, Stacks.EtaleCohomology.hasPropertyB_of_isFinite, Stacks.EtaleCohomology.hasPropertyB_of_isIntegralHom, Stacks.EtaleCohomology.smallEtalePushforwardAb_properties_of_isIntegralHom, Stacks.EtaleCohomology.etaleAbelianDirectImage_preservesEpimorphisms_of_isIntegralHom, Stacks.EtaleCohomology.preservesFiniteColimits_etaleAbelianDirectImage_of_isIntegralHom, AlgebraicGeometry.Space.smallEtalePushforward_preservesEpimorphisms_of_isIntegralHom
statement: formalized
proof: formalized
---

# 59.43 Property (B)

Section 59.43 of the Stacks Project, [Tag 04DN](https://stacks.math.columbia.edu/tag/04DN). 5 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04DO, a lemma

[Tag 04DO](https://stacks.math.columbia.edu/tag/04DO) in the Stacks Project.

**`Stacks.EtaleCohomology.smallEtalePushforward_preservesEpimorphisms_of_hasPropertyB`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Descent/PropertyB.lean, line 485](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Descent/PropertyB.lean#L485).

> **Stacks Project, Tag 04DO.** Let `f : X ⟶ Y` be a morphism of schemes with property (B).
> Then direct image along the induced morphism of small étale sites transforms surjections of
> sheaves of sets into surjections.

```lean
theorem smallEtalePushforward_preservesEpimorphisms_of_hasPropertyB {X Y : Scheme.{u}}
    (f : X ⟶ Y) (hf : HasPropertyB f) :
    ((smallEtaleBaseChange f).sheafPushforwardContinuous
      (Type v) (smallEtaleTopology Y) (smallEtaleTopology X)).PreservesEpimorphisms
```

## Tag 04DP, a lemma

[Tag 04DP](https://stacks.math.columbia.edu/tag/04DP) in the Stacks Project.

**`Stacks.EtaleCohomology.hasPropertyB_of_etaleNeighborhood_decomposition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Descent/Basic.lean, line 333](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Descent/Basic.lean#L333).

> A morphism `f : X ⟶ Y` has property (B) as soon as, for every étale `g : V ⟶ Y`, every étale
> covering `U` of `X ×ₗᵧ V` and every point `v` of `V`, there is a single étale neighborhood of `v`
> over which `X ×ₗᵧ V` breaks up into pieces subordinate to `U`.

```lean
theorem hasPropertyB_of_etaleNeighborhood_decomposition
    {X Y : Scheme.{u}} (f : X ⟶ Y)
    (h : ∀ {V : Scheme.{u}} (g : V ⟶ Y) [Etale g]
      (U : (pullback f g).Cover.{u} Scheme.etalePrecoverage) (v : V),
      ∃ (N : EtaleNeighborhood V v)
        (q : pullback f (N.toBase ≫ g) ⟶ pullback f g),
        q ≫ pullback.fst f g = pullback.fst f (N.toBase ≫ g) ∧
        q ≫ pullback.snd f g = pullback.snd f (N.toBase ≫ g) ≫ N.toBase ∧
        ∃ (W : U.I₀ → Scheme.{u}) (e : (∐ W) ≅ pullback f (N.toBase ≫ g))
          (a : ∀ i, W i ⟶ U.X i),
          ∀ i, a i ≫ U.f i = Sigma.ι W i ≫ e.hom ≫ q) :
    HasPropertyB f
```

## Tag 04DQ, a lemma

[Tag 04DQ](https://stacks.math.columbia.edu/tag/04DQ) in the Stacks Project.

**`Stacks.EtaleCohomology.hasPropertyB_of_isFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Descent/FiniteCaseTrim.lean, line 454](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Descent/FiniteCaseTrim.lean#L454).

> **Property (B) for a finite morphism of schemes.** Every étale covering of the base change of
> a finite morphism admits, after a further étale covering of the base, a componentwise subordinate
> disjoint-union decomposition.
>
> This is [Stacks, Tag 04DQ]. It is
> `Stacks.EtaleCohomology.hasPropertyB_of_isFinite_of_idempotents` with its one remaining input,
> `Stacks.EtaleCohomology.HasFiniteCaseDecompositionOfIdempotents`, discharged by
> `Stacks.EtaleCohomology.hasFiniteCaseDecompositionOfIdempotents`.

```lean
theorem hasPropertyB_of_isFinite {X Y : Scheme.{u}} (f : X ⟶ Y) [IsFinite f] : HasPropertyB f
```

## Tag 04DR, a lemma

[Tag 04DR](https://stacks.math.columbia.edu/tag/04DR) in the Stacks Project.

**`Stacks.EtaleCohomology.hasPropertyB_of_isIntegralHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Descent/FiniteCaseTrim.lean, line 467](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Descent/FiniteCaseTrim.lean#L467).

> **Property (B) for an integral morphism of schemes.** Every étale covering of the base change
> of an integral morphism admits, after a further étale covering of the base, a componentwise
> subordinate disjoint-union decomposition.
>
> This is [Stacks, Tag 04DR]. The integral case is deduced from the finite case
> `Stacks.EtaleCohomology.hasPropertyB_of_isFinite` by the limit argument
> `Stacks.EtaleCohomology.hasPropertyB_of_isIntegralHom_of_finite`: an integral morphism over an
> affine base is a directed limit of finite ones, a finite affine étale cover of the limit descends
> to a finite stage, and the decomposition supplied there is transported back.

```lean
theorem hasPropertyB_of_isIntegralHom {X Y : Scheme.{u}} (f : X ⟶ Y) [IsIntegralHom f] :
    HasPropertyB f
```

## Tag 04C2, a lemma

[Tag 04C2](https://stacks.math.columbia.edu/tag/04C2) in the Stacks Project.

**`Stacks.EtaleCohomology.smallEtalePushforwardAb_properties_of_isIntegralHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/IntegralPushforwardExact.lean, line 151](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/IntegralPushforwardExact.lean#L151).

> **Stacks Project, Tag 04C2.** Let `f : X ⟶ Y` be an integral morphism of schemes — a finite
> morphism, for instance. Then
>
> 1. `f_{small, *}` transforms surjections into surjections, on sheaves of sets and on abelian
>    sheaves,
> 2. the counit `f^{-1} f_* F ⟶ F` is surjective for every abelian sheaf `F` on `X_étale`,
> 3. `f_{small, *} : Ab(X_étale) ⥤ Ab(Y_étale)` is faithful and reflects injections and
>    surjections, and
> 4. `f_{small, *} : Ab(X_étale) ⥤ Ab(Y_étale)` is exact.
>
> The seven conjuncts are, in order: part (1) on sheaves of sets, part (1) on abelian sheaves,
> part (2), the three assertions of part (3), and part (4).

```lean
public theorem smallEtalePushforwardAb_properties_of_isIntegralHom {X Y : Scheme.{u}}
    (f : X ⟶ Y) [IsIntegralHom f] :
    ((smallEtaleBaseChange f).sheafPushforwardContinuous (Type (u + 1)) (smallEtaleTopology Y)
        (smallEtaleTopology X)).PreservesEpimorphisms ∧
      (smallEtalePushforwardAb f).PreservesEpimorphisms ∧
      (∀ F : Sheaf (smallEtaleTopology X) Ab.{u + 1},
          Epi ((smallEtaleAdjunctionAb f).counit.app F)) ∧
        (smallEtalePushforwardAb f).Faithful ∧
          (smallEtalePushforwardAb f).ReflectsMonomorphisms ∧
            (smallEtalePushforwardAb f).ReflectsEpimorphisms ∧
              exactFunctor (Sheaf (smallEtaleTopology X) Ab.{u + 1})
                (Sheaf (smallEtaleTopology Y) Ab.{u + 1}) (smallEtalePushforwardAb f)
```

**`Stacks.EtaleCohomology.etaleAbelianDirectImage_preservesEpimorphisms_of_isIntegralHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/IntegralDirectImageAcyclic.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/IntegralDirectImageAcyclic.lean#L98). The attribute's comment: “part (1) for abelian sheaves, at the coefficients of proper base change”.

> **Stacks 04C2, part (1), at the coefficients of the proper base change development.** For an
> integral morphism of schemes `f : X ⟶ Y` — a finite morphism, for instance — direct image
> `f_* : Ab(X_étale) ⥤ Ab(Y_étale)` carries surjections of abelian sheaves with values in
> `AddCommGrpCat.{max (u + 1) v}` to surjections.
>
> A morphism of abelian sheaves is epimorphic exactly when it is locally surjective, and local
> surjectivity is a property of the underlying morphism of sheaves of sets. Since the underlying
> sheaf of sets of a direct image is the direct image of the underlying sheaf of sets, the
> statement reduces to its set-valued counterpart, which is stated for an arbitrary coefficient
> universe.

```lean
public theorem etaleAbelianDirectImage_preservesEpimorphisms_of_isIntegralHom
    (f : X ⟶ Y) [IsIntegralHom f] :
    (etaleAbelianDirectImage.{u, v} f).PreservesEpimorphisms
```

**`Stacks.EtaleCohomology.preservesFiniteColimits_etaleAbelianDirectImage_of_isIntegralHom`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/IntegralDirectImageAcyclic.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/IntegralDirectImageAcyclic.lean#L134). The attribute's comment: “part (2) for abelian sheaves, at the coefficients of proper base change”.

> **Stacks 04C2, part (2), at the coefficients of the proper base change development.** For an
> integral morphism `f : X ⟶ Y`, direct image of abelian sheaves on the small étale sites
> preserves finite colimits.
>
> Direct image is a right adjoint, so it preserves finite limits and is therefore additive; it
> preserves epimorphisms because `f` is integral; and an additive functor between abelian
> categories which preserves kernels and epimorphisms preserves homology, hence finite colimits
> as well.

```lean
public instance preservesFiniteColimits_etaleAbelianDirectImage_of_isIntegralHom
    (f : X ⟶ Y) [IsIntegralHom f] :
    PreservesFiniteColimits (etaleAbelianDirectImage.{u, v} f)
```

**`AlgebraicGeometry.Space.smallEtalePushforward_preservesEpimorphisms_of_isIntegralHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralPushforwardExact.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/IntegralPushforwardExact.lean#L70). The attribute's comment: “part (1), for an integral morphism of algebraic spaces”.

> **Stacks 04C2, part (1), for an integral morphism of algebraic spaces.** The small étale
> direct image of sheaves of sets along an integral morphism of algebraic spaces over `S`
> transforms surjections into surjections.
>
> A scheme atlas `a : yoneda.obj T ⟶ Y` of the target is chosen, and the base change of `f` along
> it is taken from the representability witness that Stacks 03ZQ attaches to an integral
> morphism: that produces an object `P` of the site, a morphism `s : P ⟶ T` and a Cartesian
> square exhibiting `yoneda.map s` as the base change. Its underlying morphism of schemes is
> integral, so `AlgebraicGeometry.Space.representedSmallEtalePushforward_preservesEpimorphisms`
> applies, and
> `AlgebraicGeometry.Space.smallEtalePushforward_preservesEpimorphisms_of_etaleCover` carries the
> conclusion back to `f`.

```lean
theorem smallEtalePushforward_preservesEpimorphisms_of_isIntegralHom
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (hf : IsIntegralHom B S hS f.hom) :
    Functor.PreservesEpimorphisms (smallToposMorphism B S hS f).pushforward
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.43, Tag 04DN](https://stacks.math.columbia.edu/tag/04DN)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
