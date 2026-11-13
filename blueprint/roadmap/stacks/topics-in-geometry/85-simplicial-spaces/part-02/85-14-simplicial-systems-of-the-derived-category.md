---
declaration: section
origin: cited
lean: CategoryTheory.SimplicialSiteSituation.SimplicialDerivedModuleSystem, CategoryTheory.SimplicialSiteSituation.SimplicialDerivedModuleSystem.Cartesian, CategoryTheory.SimplicialSiteSituation.SimplicialDerivedModuleSystem.Hom, CategoryTheory.SimplicialSiteSituation.derivedModuleSystemData, CategoryTheory.SimplicialSiteSituation.derivedModuleSystem_cartesian, CategoryTheory.SimplicialSiteSituation.pairDerivedModuleSystem, CategoryTheory.SimplicialSiteSituation.pairDerivedModuleSystem_obj, CategoryTheory.SimplicialSiteSituation.pairDerivedModuleSystem_cartesian
statement: formalized
proof: formalized
---

# 85.14 Simplicial systems of the derived category: modules

Section 85.14 of the Stacks Project, [Tag 0D9M](https://stacks.math.columbia.edu/tag/0D9M). 7 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0D9N, a definition

[Tag 0D9N](https://stacks.math.columbia.edu/tag/0D9N) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.SimplicialDerivedModuleSystem`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/DerivedModuleSystem.lean, line 87](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/DerivedModuleSystem.lean#L87). The attribute's comment: “the data of a simplicial system and its cocycle condition”.

> **Stacks 0D9N.** A simplicial system of the derived category of modules for a sheaf of
> commutative rings `O` on the total site of a simplicial-site situation: an object `K_n` of the
> derived category of `O_n`-modules in every simplicial degree `n`, a map
> `K_φ : Lf_φ^* K_m ⟶ K_n` for every simplex map `φ : m ⟶ n`, and the cocycle condition
> `K_{ψ ≫ φ} = K_φ ∘ Lf_φ^* K_ψ` under the canonical identification of `Lf_{ψ ≫ φ}^*` with
> `Lf_ψ^* ⋙ Lf_φ^*`.

```lean
structure SimplicialDerivedModuleSystem
```

**`CategoryTheory.SimplicialSiteSituation.SimplicialDerivedModuleSystem.Cartesian`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/DerivedModuleSystem.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/DerivedModuleSystem.lean#L106). The attribute's comment: “cartesian systems”.

> **Stacks 0D9N.** A simplicial system of the derived category of modules is *cartesian* if
> all of its transition maps `K_φ` are isomorphisms.

```lean
abbrev Cartesian (K : SimplicialDerivedModuleSystem S O) : Prop
```

**`CategoryTheory.SimplicialSiteSituation.SimplicialDerivedModuleSystem.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/DerivedModuleSystem.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/DerivedModuleSystem.lean#L112). The attribute's comment: “morphisms of simplicial systems”.

> **Stacks 0D9N.** A morphism of simplicial systems of the derived category of modules: a
> morphism in every simplicial degree commuting with all of the transition maps.

```lean
structure Hom (K L : SimplicialDerivedModuleSystem S O)
```

## Tag 0D9P, a lemma

[Tag 0D9P](https://stacks.math.columbia.edu/tag/0D9P) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.derivedModuleSystemData`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/DerivedModuleSystemOfObject.lean, line 308](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/DerivedModuleSystemOfObject.lean#L308). The attribute's comment: “the system (K\_n, K(φ)) is a simplicial system of the derived category of modules”.

> **Stacks 0D9P.** The restrictions `K_n` of an object `K` of the derived category of
> `O`-modules on the total site, together with the derived transitions `K(φ)`, form a simplicial
> system of the derived category of modules in the sense of Stacks 0D9N. The two equations are
> part of the datum, so no unrelated family of transitions can satisfy the cocycle condition in
> its place.

```lean
noncomputable def derivedModuleSystemData
    (K : DerivedCategory (S.totalRingedTopos O).Modules) :
    { T : SimplicialDerivedModuleSystem S O //
      (∀ n, T.obj n = (S.derivedComponentModuleRestriction O n).obj K) ∧
      (∀ ⦃m n : SimplexCategory⦄ (φ : m ⟶ n),
        HEq (T.map φ) ((S.derivedComponentModuleTransition O φ).app K)) }
```

**`CategoryTheory.SimplicialSiteSituation.derivedModuleSystem_cartesian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/DerivedModuleSystemOfObject.lean, line 329](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/DerivedModuleSystemOfObject.lean#L329). The attribute's comment: “if K is cartesian then so is the system”.

> **Stacks 0D9P.** The simplicial system of a cartesian object of the derived category of
> `O`-modules is cartesian: its transitions are the derived transitions, which are isomorphisms by
> hypothesis.

```lean
theorem derivedModuleSystem_cartesian (K : DerivedCategory (S.totalRingedTopos O).Modules)
    (hK : S.IsCartesianDerivedModule O K) : (S.derivedModuleSystem O K).Cartesian
```

## Tag 0GMF, a lemma

[Tag 0GMF](https://stacks.math.columbia.edu/tag/0GMF) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.pairDerivedModuleSystem`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/DerivedCocycleSystem/CocyclePairSystem.lean, line 698](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/DerivedCocycleSystem/CocyclePairSystem.lean#L698). The attribute's comment: “the simplicial system”.

> **Stacks 0GMF.** The simplicial system of the derived category of modules attached to a pair
> `(K₀, α)`: in degree `n` the derived pullback of `K₀` along the last vertex of `⦋n⦌`, with the
> transition at `φ` given by pulling back to the image of the last vertex and transporting along
> the edge to the last vertex. The cocycle condition of Stacks 0D9N is
> `pairDerivedModuleTransition_comp`.

```lean
def pairDerivedModuleSystem (Pr : S.DerivedModuleCocyclePair O) :
    SimplicialDerivedModuleSystem S O
```

**`CategoryTheory.SimplicialSiteSituation.pairDerivedModuleSystem_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/DerivedCocycleSystem/CocyclePairSystem.lean, line 707](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/DerivedCocycleSystem/CocyclePairSystem.lean#L707). The attribute's comment: “the objects of the system”.

> **Stacks 0GMF.** The object of the system in degree `n` is `Lf_{τⁿₙ}^* K₀`, the derived
> pullback of `K₀` along the last vertex of `⦋n⦌`.

```lean
theorem pairDerivedModuleSystem_obj (Pr : S.DerivedModuleCocyclePair O) (n : SimplexCategory) :
    (S.pairDerivedModuleSystem O Pr).obj n =
      (S.derivedTransitionPullback O
        (SimplexCategory.const (SimplexCategory.mk 0) n (Fin.last n.len))).obj Pr.obj
```

**`CategoryTheory.SimplicialSiteSituation.pairDerivedModuleSystem_cartesian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/DerivedCocycleSystem/CocyclePairSystem.lean, line 716](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/DerivedCocycleSystem/CocyclePairSystem.lean#L716). The attribute's comment: “the system is cartesian”.

> **Stacks 0GMF.** The system attached to a pair is cartesian: every transition map is an
> isomorphism, for every simplex map and not only for the faces.

```lean
theorem pairDerivedModuleSystem_cartesian (Pr : S.DerivedModuleCocyclePair O) :
    (S.pairDerivedModuleSystem O Pr).Cartesian
```

## Tag 0D9Q, a lemma

[Tag 0D9Q](https://stacks.math.columbia.edu/tag/0D9Q) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.moduleResolutionTensorPostnikovSystem`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ModuleResolutionDerivedTensor.lean, line 344](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ModuleResolutionDerivedTensor.lean#L344). The attribute's comment: “part (1), the Postnikov system of - ⊗^L\_O K”.

> **Stacks 0D9Q(1).** For each length `N`, the triangles
> `Yₙ₊₁ ⟶ Xₙ₊₁ ⟶ Yₙ ⟶ Yₙ₊₁[1]` with `Xₙ = (g_{n!}Oₙ) ⊗^L_O K` and
> `Yₙ = (g_{n!}Oₙ → … → g_{0!}O₀)[-n] ⊗^L_O K` form a Postnikov system (Derived Categories,
> Definition 0D7Z) for `X_N ⟶ ⋯ ⟶ X₁ ⟶ X₀`.
>
> The triangles are the images under `- ⊗^L_O K` of the brutal-truncation triangles of the
> resolution of Stacks 0D9B, and `- ⊗^L_O K` is exact by `isTriangulated_derivedTensorRight`;
> the terms are the source's `Xₙ` by `moduleResolutionTensorTermIso`.

```lean
def moduleResolutionTensorPostnikovSystem (N : ℕ) :
    Triangulated.PostnikovSystem
      (fun i : Fin (N + 1) => (derivedTensorRight R T K).obj (moduleResolutionTerm D (i : ℕ)))
      (fun i : Fin N => (derivedTensorRight R T K).map (moduleResolutionTermDiff D (i : ℕ)))
```

**`CategoryTheory.SimplicialSiteSituation.isHomotopyColimit_moduleResolutionTensorSystem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ModuleResolutionDerivedTensor.lean, line 360](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ModuleResolutionDerivedTensor.lean#L360). The attribute's comment: “part (2), the homotopy colimit, K = hocolim Yₙ[n] for Yₙ = (…)[-n] ⊗^L\_O K”.

> **Stacks 0D9Q(2).** `K = hocolim Yₙ[n]` in `D(O)`, where
> `Yₙ = (g_{n!}Oₙ → … → g_{0!}O₀)[-n] ⊗^L_O K`.
>
> The system `Yₙ[n]` is the image under `- ⊗^L_O K` of the tower of brutal truncations of the
> resolution of Stacks 0D9B, whose derived colimit is the structure sheaf
> (`isHomotopyColimit_moduleResolutionSystem`, Stacks 0D9Q(2) for `O`); the functor `- ⊗^L_O K` is
> exact and commutes with countable direct sums, so it carries that derived colimit to the derived
> colimit of the images, and it sends `O` to `K` by `derivedTensorRightUnitIso`.

```lean
theorem isHomotopyColimit_moduleResolutionTensorSystem :
    IsHomotopyColimit (moduleResolutionSystem D ⋙ derivedTensorRight R T K) K
```

**`CategoryTheory.SimplicialSiteSituation.map_moduleResolutionPostnikovSystem`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ModuleResolutionPostnikov.lean, line 293](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ModuleResolutionPostnikov.lean#L293). The attribute's comment: “part (1), the Postnikov system, for an exact functor in place of - ⊗^L\_O K”.

> **Stacks 0D9Q(1).** For an exact functor `T` of `D(O)` — such as `- ⊗^L_O K` for an object
> `K` of `D(O)` — the images under `T` of the brutal-truncation triangles of the module
> resolution are a Postnikov system for `T(X_N) ⟶ ⋯ ⟶ T(X₁) ⟶ T(X₀)`, where `Xₙ = g_{n!}Oₙ`.

```lean
def map_moduleResolutionPostnikovSystem
    (T : DerivedCategory (SheafOfModules.{u} O) ⥤ DerivedCategory (SheafOfModules.{u} O))
    [T.CommShift ℤ] [T.IsTriangulated] (N : ℕ) :
    Triangulated.PostnikovSystem
      (fun i : Fin (N + 1) => T.obj (moduleResolutionTerm D (i : ℕ)))
      (fun i : Fin N => T.map (moduleResolutionTermDiff D (i : ℕ)))
```

**`CategoryTheory.SimplicialSiteSituation.isHomotopyColimit_map_moduleResolutionSystem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ModuleResolutionPostnikov.lean, line 305](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ModuleResolutionPostnikov.lean#L305). The attribute's comment: “part (2), the homotopy colimit, for an exact functor in place of - ⊗^L\_O K”.

> **Stacks 0D9Q(2).** For an exact functor `T` of `D(O)` commuting with countable direct
> sums — such as `- ⊗^L_O K` for an object `K` of `D(O)`, for which `T(O) = K` — the object
> `T(O)` is the derived colimit of the system `T(Yₙ[n])`.

```lean
theorem isHomotopyColimit_map_moduleResolutionSystem
    (T : DerivedCategory (SheafOfModules.{u} O) ⥤ DerivedCategory (SheafOfModules.{u} O))
    [T.CommShift ℤ] [T.IsTriangulated]
    [PreservesColimit (Discrete.functor (moduleResolutionSystem D).obj) T] :
    IsHomotopyColimit (moduleResolutionSystem D ⋙ T)
      (T.obj ((DerivedCategory.singleFunctor (SheafOfModules.{u} O) 0).obj
        (SheafOfModules.unit O)))
```

## Tag 0D9R, a lemma

[Tag 0D9R](https://stacks.math.columbia.edu/tag/0D9R) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.eq_zero_of_derivedComponentModuleRestriction_map_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/CartesianDerivedModuleProjectionSituation.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/CartesianDerivedModuleProjectionSituation.lean#L99).

> **Stacks 0D9R.** In a simplicial-site situation (Stacks 09WE, either case) let `O` be a sheaf
> of rings on the total site and `K, K'` objects of `D(O)`. Assume
>
> 1. `f_φ^{-1}O_n ⟶ O_m` is flat for every simplex map `φ`,
> 2. `K` is cartesian,
> 3. `Hom(K_i[i], K'_i) = 0` for `i > 0`, and
> 4. `Hom(K_i[i + 1], K'_i) = 0` for `i ≥ 0`.
>
> Then a map `K ⟶ K'` inducing the zero map `K_0 ⟶ K'_0` is zero.

```lean
theorem eq_zero_of_derivedComponentModuleRestriction_map_eq_zero
    (K K' : DerivedCategory (S.totalRingedTopos O).Modules)
    (hflat : ∀ ⦃m n : SimplexCategory⦄ (φ : m ⟶ n), (S.transitionRingedToposHom O φ).IsFlat)
    (hK : S.IsCartesianDerivedModule O K)
    (hHom : ∀ i : ℕ, 0 < i →
      ∀ g : (shiftFunctor (DerivedCategory ((S.componentRingedTopos O ⦋i⦌).Modules)) (i : ℤ)).obj
          ((S.derivedComponentModuleRestriction O ⦋i⦌).obj K) ⟶
        (S.derivedComponentModuleRestriction O ⦋i⦌).obj K', g = 0)
    (hHomSucc : ∀ i : ℕ,
      ∀ g : (shiftFunctor (DerivedCategory ((S.componentRingedTopos O ⦋i⦌).Modules))
            ((i : ℤ) + 1)).obj ((S.derivedComponentModuleRestriction O ⦋i⦌).obj K) ⟶
        (S.derivedComponentModuleRestriction O ⦋i⦌).obj K', g = 0)
    (f : K ⟶ K')
    (hf : (S.derivedComponentModuleRestriction O ⦋0⦌).map f = 0) :
    f = 0
```

## Tag 0D9S, a lemma

[Tag 0D9S](https://stacks.math.columbia.edu/tag/0D9S) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.exists_hom_of_cartesian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/CartesianDerivedModuleMorphism.lean, line 269](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/CartesianDerivedModuleMorphism.lean#L269).

> **Stacks 0D9S.** In Situation 09WE, let `O` be a sheaf of rings on the total site and let
> `K`, `K'` be objects of `D(O)`. Assume
>
> 1. the structure-sheaf transitions `f_φ^{-1}O_n ⟶ O_m` are flat,
> 2. `K` is cartesian, and
> 3. `Hom(K_i[i - 1], K'_i) = 0` for `i > 1`.
>
> Then any morphism `{K_n ⟶ K'_n}` between the associated simplicial systems of the derived
> category of modules comes from a morphism `K ⟶ K'` in `D(O)`.
>
> The situation `S` is an arbitrary term of `CategoryTheory.SimplicialSiteSituation`, so both cases
> of Situation 09WE are covered. The proof is the source's: the Postnikov system of Stacks 0D9Q
> produces a morphism agreeing with the given one in degree zero
> (`exists_hom_derivedComponentModuleRestriction_zero_eq`), and cartesianness of `K` makes it agree
> in every degree (`SimplicialDerivedModuleSystem.Hom.app_eq_of_cartesian`).

```lean
theorem exists_hom_of_cartesian
    (K K' : DerivedCategory (S.totalRingedTopos O).Modules)
    (hflat : ∀ (m n : SimplexCategory) (φ : m ⟶ n), (S.transitionRingedToposHom O φ).IsFlat)
    (hK : S.IsCartesianDerivedModule O K)
    (hHom : ∀ i : ℕ, 1 < i →
      ∀ g : (shiftFunctor (DerivedCategory ((S.componentRingedTopos O ⦋i⦌).Modules))
          ((i : ℤ) - 1)).obj ((S.derivedComponentModuleRestriction O ⦋i⦌).obj K) ⟶
          (S.derivedComponentModuleRestriction O ⦋i⦌).obj K', g = 0)
    (f : SimplicialDerivedModuleSystem.Hom (S.derivedModuleSystem O K)
      (S.derivedModuleSystem O K')) :
    ∃ γ : K ⟶ K', ∀ i : SimplexCategory,
      (S.derivedComponentModuleRestriction O i).map γ = f.app i
```

## Tag 0D9T, a lemma

[Tag 0D9T](https://stacks.math.columbia.edu/tag/0D9T) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.exists_isCartesianDerivedModule_of_moduleSystem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/CartesianDerivedModuleOfModuleSystem.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/CartesianDerivedModuleOfModuleSystem.lean#L97).

> **Stacks 0D9T.** In a simplicial-site situation (Stacks 09WE, either case) let `O` be a sheaf
> of rings on the total site and let `(K_n, K_φ)` be a simplicial system of the derived category of
> modules. Assume
>
> 1. `f_φ^{-1}O_n ⟶ O_m` is flat for every simplex map `φ`,
> 2. `(K_n, K_φ)` is cartesian, and
> 3. `Hom(K_i[t], K_i) = 0` for all `i` and all `t > 0`.
>
> Then there exists a cartesian object `K` of `D(O)` whose associated simplicial system is
> isomorphic to `(K_n, K_φ)`.

```lean
theorem exists_isCartesianDerivedModule_of_moduleSystem
    (hflat : ∀ (n m : SimplexCategory) (φ : n ⟶ m), (S.transitionRingedToposHom O φ).IsFlat)
    (T : SimplicialDerivedModuleSystem S O) (hT : T.Cartesian)
    (hHom : ∀ (k : SimplexCategory) (t : ℕ), 0 < t →
      ∀ f : (shiftFunctor (DerivedCategory (S.componentRingedTopos O k).Modules)
        (t : ℤ)).obj (T.obj k) ⟶ T.obj k, f = 0) :
    ∃ K : DerivedCategory (S.totalRingedTopos O).Modules,
      S.IsCartesianDerivedModule O K ∧ Nonempty (T ≅ S.derivedModuleSystem O K)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 85.14, Tag 0D9M](https://stacks.math.columbia.edu/tag/0D9M)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
