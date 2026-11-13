---
declaration: section
origin: cited
lean: Stacks.Injectives.SheafificationTowerFactorization.exists_extension_towerIota_succ, Stacks.Injectives.SheafificationTowerFactorization.exists_ordinal_towerFactorsThrough, CategoryTheory.Sheaf.freeYonedaHomEquiv, Stacks.Injectives.BaerCriterion.injective_of_extends_freeAbSheaf, CategoryTheory.Sheaf.hasFunctorialInjectiveEmbeddings_addCommGrpCat, CategoryTheory.Sheaf.enoughInjectives_addCommGrpCat
statement: formalized
proof: formalized
---

# 19.7 Abelian Sheaves on a site

Section 19.7 of the Stacks Project, [Tag 01DL](https://stacks.math.columbia.edu/tag/01DL). 5 tags here are carried by 5 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01DM, a lemma

[Tag 01DM](https://stacks.math.columbia.edu/tag/01DM) in the Stacks Project.

**`Stacks.Injectives.SheafificationTowerFactorization.exists_extension_towerIota_succ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Sheaf/SheafificationTowerFactorization.lean, line 428](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Injectives/Sheaf/SheafificationTowerFactorization.lean#L428).

> Let `F` be an abelian sheaf and `α ≤ β` a non-maximal stage of the tower, so that
> `α + 1 ≤ β` as well. Let `ι : G₁ ⟶ G₂` be an injective (i.e. monomorphic) map of abelian sheaves
> and let `f : G₁ ⟶ J_α(F)` be a morphism. Then there is a morphism `g : G₂ ⟶ J_{α+1}(F)` making
> the square with the transition map `ι_{α,α+1} : J_α(F) ⟶ J_{α+1}(F)` commute, i.e.
> `ι ≫ g = f ≫ ι_{α,α+1}`.

```lean
theorem exists_extension_towerIota_succ (β : Ordinal.{u}) (α : Set.Iic β) (hα : ¬ IsMax α)
    (F : AbSheaf J) {G₁ G₂ : AbSheaf J} (ι : G₁ ⟶ G₂) [Mono ι]
    (f : G₁ ⟶ towerObj J β α F) :
    ∃ g : G₂ ⟶ towerObj J β (Order.succ α) F,
      ι ≫ g = f ≫ towerIota J β (Order.le_succ α) F
```

## Tag 01DN, a lemma

[Tag 01DN](https://stacks.math.columbia.edu/tag/01DN) in the Stacks Project.

**`Stacks.Injectives.SheafificationTowerFactorization.exists_ordinal_towerFactorsThrough`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Sheaf/SheafificationTowerFactorization.lean, line 835](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Injectives/Sheaf/SheafificationTowerFactorization.lean#L835).

> Let `{G i}_{i : I}` be a set of abelian sheaves on `C`. There is an ordinal `β`, depending
> only on `J` and the family `{G i}`, such that for every abelian sheaf `F`, every index `i`, and
> every morphism `φ : G i → J_β(F)`, there is an ordinal `α < β` such that `φ` factors through
> `J_α(F)`.

```lean
theorem exists_ordinal_towerFactorsThrough {I : Type u} (G : I → AbSheaf J) :
    ∃ β : Ordinal.{u},
      ∀ (F : AbSheaf J) (i : I) (φ : G i ⟶ towerTop J β F),
        ∃ (α : Set.Iic β) (h : (α : Ordinal) < β),
          TowerFactorsThrough J β
            (le_of_lt (show α < (⟨β, le_refl β⟩ : Set.Iic β) from h)) F (G i) φ
```

## Tag 05NY, an equation

[Tag 05NY](https://stacks.math.columbia.edu/tag/05NY) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Sheaf.freeYonedaHomEquiv`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Sheaf.freeYonedaHomEquiv#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Adjunction.lean, line 33](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Sites/Adjunction.lean#L33) (StacksCore): “Mor\_\{Ab(C)}(Z\_X^#, G) = G(X)”.

## Tag 01DO, a lemma

[Tag 01DO](https://stacks.math.columbia.edu/tag/01DO) in the Stacks Project.

**`Stacks.Injectives.BaerCriterion.injective_of_extends_freeAbSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Sheaf/BaerCriterion.lean, line 557](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Injectives/Sheaf/BaerCriterion.lean#L557).

> Let `𝒥` be a sheaf of abelian groups such that for every object `X` of `C`, every abelian
> subsheaf `S ⊆ Z_X^#`, and every morphism `φ : S → 𝒥`, there exists a morphism `ψ : Z_X^# → 𝒥`
> extending `φ`. Then `𝒥` is an injective sheaf of abelian groups.

```lean
theorem injective_of_extends_freeAbSheaf
    (𝒥 : Sheaf J Ab.{u})
    (H : ∀ (X : C) (S : AbelianSubsheaf J (freeAbSheaf J X)) (φ : S.sheaf ⟶ 𝒥),
      ∃ ψ : freeAbSheaf J X ⟶ 𝒥, Extends J S φ ψ) :
    IsInjectiveSheaf J 𝒥
```

## Tag 01DP, a theorem

[Tag 01DP](https://stacks.math.columbia.edu/tag/01DP) in the Stacks Project.

**`CategoryTheory.Sheaf.hasFunctorialInjectiveEmbeddings_addCommGrpCat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/FunctorialInjectiveEmbeddings.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/FunctorialInjectiveEmbeddings.lean#L111). The attribute's comment: “functorial injective embeddings”. References: SGA 4½ Arcata (1.6.3), “enough injectives”; SGA 4 V (0.1.1), “sheaves on a site”.

> **Stacks Project, Tag 01DP.** The category of sheaves of abelian groups on a site has
> functorial injective embeddings in the sense of [Stacks, Tag 0139].

```lean
theorem hasFunctorialInjectiveEmbeddings_addCommGrpCat [HasSheafify J AddCommGrpCat.{w}]
    [EssentiallySmall.{w} C] :
    HasFunctorialInjectiveEmbeddings (Sheaf J AddCommGrpCat.{w})
```

**`CategoryTheory.Sheaf.enoughInjectives_addCommGrpCat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/FunctorialInjectiveEmbeddings.lean, line 126](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/FunctorialInjectiveEmbeddings.lean#L126). The attribute's comment: “enough injectives”. References: SGA 4½ Arcata (1.6.3), “enough injectives”; SGA 4 V (0.1.1), “sheaves on a site”; SGA 3 I (3.1.2), “special case”; SGA 4 I (7.13), “special case”; SGA 4 V (0.2.1), “special case”; SGA 4 V (2.5.2), “special case”.

> **Stacks Project, Tag 01DP.** The category of sheaves of abelian groups on a site has
> enough injectives. This is deduced from the functorial statement
> `hasFunctorialInjectiveEmbeddings_addCommGrpCat`, as in the source.

```lean
theorem enoughInjectives_addCommGrpCat [HasSheafify J AddCommGrpCat.{w}]
    [EssentiallySmall.{w} C] :
    EnoughInjectives (Sheaf J AddCommGrpCat.{w})
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 19.7, Tag 01DL](https://stacks.math.columbia.edu/tag/01DL)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
