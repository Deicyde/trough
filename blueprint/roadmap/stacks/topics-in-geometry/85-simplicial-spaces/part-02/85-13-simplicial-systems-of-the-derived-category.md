---
declaration: section
origin: cited
lean: CategoryTheory.SimplicialDerivedSystem, CategoryTheory.SimplicialDerivedSystem.Cartesian, CategoryTheory.SimplicialDerivedSystem.Hom, CategoryTheory.SimplicialDerivedSystem.cartesianInclusion, CategoryTheory.SimplicialSiteSituation.associatedDerivedSystemData, CategoryTheory.SimplicialSiteSituation.associatedDerivedSystem_cartesian, CategoryTheory.SimplicialSiteSituation.pairDerivedSystem, CategoryTheory.SimplicialSiteSituation.pairDerivedSystem_obj
statement: formalized
proof: formalized
---

# 85.13 Simplicial systems of the derived category

Section 85.13 of the Stacks Project, [Tag 0D9F](https://stacks.math.columbia.edu/tag/0D9F). 7 tags here are carried by 17 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0D9G, a definition

[Tag 0D9G](https://stacks.math.columbia.edu/tag/0D9G) in the Stacks Project.

**`CategoryTheory.SimplicialDerivedSystem`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/DerivedSystem.lean, line 478](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/DerivedSystem.lean#L478). The attribute's comment: “the simplicial system”.

> A simplicial system of the derived category for `S`: an object `K_n` of the derived category
> of abelian sheaves on each component site, and for every simplex map `φ : [m] ⟶ [n]` a map
> `K_φ : f_φ⁻¹K_m ⟶ K_n` from the derived inverse image, such that `K_{φ ∘ ψ}` is
> `K_φ ∘ f_φ⁻¹K_ψ` under the canonical identification `f_{φ ∘ ψ}⁻¹ ≅ f_φ⁻¹ ∘ f_ψ⁻¹`. As in the
> source, no condition is imposed at identities.

```lean
structure SimplicialDerivedSystem
```

**`CategoryTheory.SimplicialDerivedSystem.Cartesian`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/DerivedSystem.lean, line 494](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/DerivedSystem.lean#L494). The attribute's comment: “cartesian systems”.

> A system is cartesian if all its transition maps are isomorphisms.

```lean
abbrev Cartesian (K : SimplicialDerivedSystem S) : Prop
```

**`CategoryTheory.SimplicialDerivedSystem.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/DerivedSystem.lean, line 499](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/DerivedSystem.lean#L499). The attribute's comment: “morphisms of simplicial systems”.

> A morphism is a degreewise morphism commuting with every transition map.

```lean
structure Hom (K L : SimplicialDerivedSystem S)
```

**`CategoryTheory.SimplicialDerivedSystem.cartesianInclusion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/DerivedSystem.lean, line 550](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/DerivedSystem.lean#L550).

> Simplicial systems of the derived category: the category whose objects are the systems
> `(K_n, K_φ)` of `SimplicialDerivedSystem S` and whose morphisms are the degreewise maps commuting
> with the transitions (`SimplicialDerivedSystem.Hom`), together with its full subcategory of
> cartesian systems, those whose transitions `K_φ` are all isomorphisms.

```lean
def cartesianInclusion : (cartesian S).FullSubcategory ⥤ SimplicialDerivedSystem S
```

## Tag 0D9H, a lemma

[Tag 0D9H](https://stacks.math.columbia.edu/tag/0D9H) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.associatedDerivedSystemData`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/AssociatedDerivedSystem.lean, line 461](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/AssociatedDerivedSystem.lean#L461). The attribute's comment: “associated simplicial system”.

> The canonical simplicial system of the derived category attached to an object `K` of the
> derived category of abelian sheaves on the total site, together with the equations stating that
> its object in degree `n` is the derived restriction of `K` and its transition along a simplex map
> is the canonical derived transition at `K`.

```lean
def associatedDerivedSystemData (K : DerivedCategory (Sheaf S.totalTopology Ab.{u})) :
    { T : SimplicialDerivedSystem S //
      (∀ n, T.obj n = (derivedComponent S n).obj K) ∧
      (∀ ⦃m n : SimplexCategory⦄ (φ : m ⟶ n),
        HEq (T.map φ) ((derivedTransition S φ).app K)) }
```

**`CategoryTheory.SimplicialSiteSituation.associatedDerivedSystem_cartesian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/AssociatedDerivedSystem.lean, line 479](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/AssociatedDerivedSystem.lean#L479). The attribute's comment: “cartesian objects give cartesian systems”.

> The simplicial system of derived restrictions of a cartesian object is cartesian.

```lean
theorem associatedDerivedSystem_cartesian
    (K : DerivedCategory (Sheaf S.totalTopology Ab.{u})) (hK : S.IsCartesianDerived K) :
    (associatedDerivedSystem S K).Cartesian
```

## Tag 0GME, a lemma

[Tag 0GME](https://stacks.math.columbia.edu/tag/0GME) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.pairDerivedSystem`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/DerivedCocycleSystem.lean, line 979](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/DerivedCocycleSystem.lean#L979). The attribute's comment: “the simplicial system”.

> **Stacks 0GME.** The cartesian simplicial system of the derived category attached to a pair
> `(K₀, α)`: in degree `n` the derived inverse image of `K₀` along the last vertex of `⦋n⦌`.

```lean
def pairDerivedSystem (P : DerivedCocyclePair S) : SimplicialDerivedSystem S
```

**`CategoryTheory.SimplicialSiteSituation.pairDerivedSystem_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/DerivedCocycleSystem.lean, line 989](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/DerivedCocycleSystem.lean#L989). The attribute's comment: “the objects of the system”.

> **Stacks 0GME.** The object of the system in degree `n` is `f_{τⁿₙ}⁻¹K₀`, the derived
> inverse image of `K₀` along the last vertex of `⦋n⦌`.

```lean
theorem pairDerivedSystem_obj (P : DerivedCocyclePair S) (n : SimplexCategory) :
    (S.pairDerivedSystem P).obj n =
      (derivedInverseImage S
        (SimplexCategory.const (SimplexCategory.mk 0) n (Fin.last n.len))).obj P.obj
```

**`CategoryTheory.SimplicialSiteSituation.pairDerivedSystem_cartesian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/DerivedCocycleSystem.lean, line 996](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/DerivedCocycleSystem.lean#L996). The attribute's comment: “the system is cartesian”.

> **Stacks 0GME.** The system attached to a pair is cartesian.

```lean
theorem pairDerivedSystem_cartesian (P : DerivedCocyclePair S) :
    (S.pairDerivedSystem P).Cartesian
```

## Tag 0D9I, a lemma

[Tag 0D9I](https://stacks.math.columbia.edu/tag/0D9I) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.derivedTensorIntegerResolutionPostnikovSystem`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/IntegerResolutionDerivedTensor.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/IntegerResolutionDerivedTensor.lean#L142).

> **Stacks 0D9I(1) for `- ⊗^L_ℤ K`.** For each length `N`, the images under `- ⊗^L_ℤ K` of
> the brutal-truncation triangles `Yₙ₊₁ ⟶ Xₙ₊₁ ⟶ Yₙ ⟶ Yₙ₊₁[1]` of the integral resolution are a
> Postnikov system (Derived Categories, Definition 0D7Z) for `X_N ⟶ ⋯ ⟶ X₁ ⟶ X₀`, where
> `Xₙ = g_{n!}ℤ ⊗^L_ℤ K` by `derivedTensorIntegerResolutionTermIso`.

```lean
def derivedTensorIntegerResolutionPostnikovSystem (N : ℕ) :
    Triangulated.PostnikovSystem
      (fun i : Fin (N + 1) =>
        (integerDerivedTensorRight S K).obj (integerResolutionTerm S (i : ℕ)))
      (fun i : Fin N =>
        (integerDerivedTensorRight S K).map
          (termDiff (integerResolutionComplex S) (i : ℕ)))
```

**`CategoryTheory.SimplicialSiteSituation.isHomotopyColimit_derivedTensorIntegerResolutionSystem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/IntegerResolutionDerivedTensor.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/IntegerResolutionDerivedTensor.lean#L186).

> **Stacks 0D9I(2) for `- ⊗^L_ℤ K`.** The object `K` is the derived colimit of the system
> `Yₙ[n] = (g_{n!}ℤ → … → g_{0!}ℤ) ⊗^L_ℤ K`.

```lean
theorem isHomotopyColimit_derivedTensorIntegerResolutionSystem :
    IsHomotopyColimit (integerResolutionSystem S ⋙ integerDerivedTensorRight S K) K
```

**`CategoryTheory.SimplicialSiteSituation.map_integerResolutionPostnikovSystem`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/IntegerResolutionPostnikov.lean, line 942](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/IntegerResolutionPostnikov.lean#L942).

> **Stacks 0D9I(1).** For an exact functor `T` of `D(𝒞_total)` — such as `- ⊗^L_ℤ K` for an
> object `K` of `D(𝒞_total)` — the images under `T` of the brutal-truncation triangles of the
> integral resolution are a Postnikov system for `T(X_N) ⟶ ⋯ ⟶ T(X₁) ⟶ T(X₀)`.

```lean
def map_integerResolutionPostnikovSystem
    (T : DerivedCategory (Sheaf S.totalTopology Ab.{u}) ⥤
      DerivedCategory (Sheaf S.totalTopology Ab.{u})) [T.CommShift ℤ] [T.IsTriangulated]
    (N : ℕ) :
    Triangulated.PostnikovSystem
      (fun i : Fin (N + 1) => T.obj (integerResolutionTerm S (i : ℕ)))
      (fun i : Fin N => T.map (termDiff (integerResolutionComplex S) (i : ℕ)))
```

**`CategoryTheory.SimplicialSiteSituation.isHomotopyColimit_map_integerResolutionSystem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/IntegerResolutionPostnikov.lean, line 969](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/IntegerResolutionPostnikov.lean#L969).

> **Stacks 0D9I(2).** For an exact functor `T` of `D(𝒞_total)` commuting with countable
> direct sums — such as `- ⊗^L_ℤ K` for an object `K` of `D(𝒞_total)` — the object `T(ℤ)` is the
> derived colimit of the system `T(Yₙ[n])`.

```lean
theorem isHomotopyColimit_map_integerResolutionSystem
    (T : DerivedCategory (Sheaf S.totalTopology Ab.{u}) ⥤
      DerivedCategory (Sheaf S.totalTopology Ab.{u})) [T.CommShift ℤ] [T.IsTriangulated]
    [PreservesColimit (Discrete.functor (integerResolutionSystem S).obj) T] :
    IsHomotopyColimit (integerResolutionSystem S ⋙ T)
      (T.obj (DerivedCategory.Q.obj (integerResolutionComplex S)))
```

## Tag 0D9J, a lemma

[Tag 0D9J](https://stacks.math.columbia.edu/tag/0D9J) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.eq_zero_of_derivedComponent_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/CartesianDerivedMapVanishing.lean, line 537](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/CartesianDerivedMapVanishing.lean#L537).

> **Stacks 0D9J.** In the simplicial-site situation of Stacks 09WE, let `K` and `K'` be objects
> of `D(𝒞_total)` with `K` cartesian, and suppose that every morphism `Kᵢ[i] ⟶ K'ᵢ` vanishes for
> `i > 0` and that every morphism `Kᵢ[i + 1] ⟶ K'ᵢ` vanishes for `i ≥ 0`. Then a map `K ⟶ K'`
> inducing the zero map `K₀ ⟶ K'₀` is zero.
>
> The proof is the source's. Stacks 0D9I presents `K` as the derived colimit of the system
> `Yₙ[n]`, whose successive quotients are the shifted terms `Xₙ[n]`; Stacks 0D9E identifies `Xₙ`
> with `g_{n!}Kₙ`, which turns the two vanishing hypotheses into the vanishing of the groups
> `Hom(Xᵢ[t], K')` the induction consumes.

```lean
theorem eq_zero_of_derivedComponent_zero
    (hK : IsCartesianDerived S K)
    (hHom : ∀ i : ℕ, 0 < i →
      ∀ g : ((derivedComponent S ⦋i⦌).obj K)⟦(i : ℤ)⟧ ⟶ (derivedComponent S ⦋i⦌).obj K', g = 0)
    (hHomSucc : ∀ i : ℕ, ∀ g : ((derivedComponent S ⦋i⦌).obj K)⟦((i + 1 : ℕ) : ℤ)⟧ ⟶
      (derivedComponent S ⦋i⦌).obj K', g = 0)
    (f : K ⟶ K') (hf : (derivedComponent S ⦋0⦌).map f = 0) :
    f = 0
```

## Tag 0D9K, a lemma

[Tag 0D9K](https://stacks.math.columbia.edu/tag/0D9K) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.exists_hom_of_isCartesianDerived`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/CartesianDerivedLiftMorphism.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/CartesianDerivedLiftMorphism.lean#L150). The attribute's comment: “a morphism of simplicial systems comes from the total site, at the source's hypotheses (1) and (2): the degree-zero lift is `CategoryTheory.SimplicialSiteSituation.exists_hom_derivedComponent_zero_eq`, which makes the source's two omitted computations -- the vanishing of `X_1 ⟶ X_0 ⟶ K'` against the transition of the realization, and the reading of the structural map `X_0 ⟶ K` as the counit -- and the passage from degree zero to all degrees is `CategoryTheory.SimplicialSiteSituation.exists_hom_iff_exists_hom_zero`”.

> **Stacks 0D9K.** In the simplicial-site situation of Stacks 09WE, let `K` and `K'` be objects
> of the derived category of abelian sheaves on the total site. If `K` is cartesian in the sense of
> Stacks 07TF (3) and `Hom(K_i[i - 1], K'_i) = 0` for `i > 1`, then every morphism of the
> associated simplicial systems of Stacks 0D9H is induced by a morphism `K ⟶ K'`: there is a
> `γ : K ⟶ K'` whose derived restriction to every simplicial degree is the given component.

```lean
theorem exists_hom_of_isCartesianDerived
    (K K' : DerivedCategory (Sheaf S.totalTopology Ab.{u}))
    (hK : S.IsCartesianDerived K)
    (hHom : S.ShiftedComponentHomVanishing K K')
    (f : SimplicialDerivedSystem.Hom (S.associatedDerivedSystem K)
      (S.associatedDerivedSystem K')) :
    ∃ γ : K ⟶ K', ∀ n : SimplexCategory, (derivedComponent S n).map γ = f.app n
```

## Tag 0D9L, a lemma

[Tag 0D9L](https://stacks.math.columbia.edu/tag/0D9L) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.exists_isCartesianDerived_of_simplicialDerivedSystem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/CartesianDerivedOfSystem.lean, line 344](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/CartesianDerivedOfSystem.lean#L344).

> A cartesian simplicial system of the derived categories of the components, whose objects have
> no positively shifted self-maps, is the system associated with a cartesian object of the derived
> category of the total site.

```lean
theorem exists_isCartesianDerived_of_simplicialDerivedSystem (T : SimplicialDerivedSystem S)
    (hT : SimplicialDerivedSystem.Cartesian T)
    (hHom : ∀ (k : SimplexCategory) (t : ℕ), 0 < t →
      ∀ f : (shiftFunctor (DerivedCategory (Sheaf (S.componentTopology k) Ab.{u}))
        (t : ℤ)).obj (T.obj k) ⟶ T.obj k, f = 0) :
    ∃ K : DerivedCategory (Sheaf S.totalTopology Ab.{u}),
      S.IsCartesianDerived K ∧
        ∃ γ : ∀ n, T.obj n ≅ (S.associatedDerivedSystem K).obj n,
          ∀ ⦃m n : SimplexCategory⦄ (φ : m ⟶ n),
            T.map φ ≫ (γ n).hom =
              (derivedInverseImage S φ).map ((γ m).hom) ≫
                (S.associatedDerivedSystem K).map φ
```

**`CategoryTheory.SimplicialSiteSituation.nonempty_sequentialPostnikovSystem_realizationComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/CartesianDerivedPostnikov.lean, line 341](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/CartesianDerivedPostnikov.lean#L341). The attribute's comment: “the Postnikov system of the realization complex”.

> **Stacks 0D9L, the Postnikov system of the realization.**  The complex whose term in degree
> `n` is the extension by lower shriek of the object of the system in degree `n`, and whose
> differential is the alternating sum of the transitions along the face maps, carries a sequential
> Postnikov system: its differentials compose to zero, and all positively shifted morphisms between
> its terms vanish.
>
> This is the construction step of Stacks 0D9L.  The totalization of this Postnikov system, the
> identification of its restriction to each simplicial degree with the object of the system in that
> degree, and the cartesianness of the result are in
> `StacksFrontier.CategoryTheory.Sites.Simplicial.CartesianDerivedOfSystem`.

```lean
theorem nonempty_sequentialPostnikovSystem_realizationComplex (T : SimplicialDerivedSystem S)
    (hT : SimplicialDerivedSystem.Cartesian T)
    (hHom : ∀ (k : SimplexCategory) (t : ℕ), 0 < t →
      ∀ f : (shiftFunctor (DerivedCategory (Sheaf (S.componentTopology k) Ab.{u}))
        (t : ℤ)).obj (T.obj k) ⟶ T.obj k, f = 0) :
    Nonempty (Triangulated.SequentialPostnikovSystem
      (fun n : ℕ => realizationTerm S T ⦋n⦌)
      (fun n : ℕ => (realizationComplex T hT).d (n + 1) n))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 85.13, Tag 0D9F](https://stacks.math.columbia.edu/tag/0D9F)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
