---
declaration: section
origin: cited
lean: CategoryTheory.PreZeroHypercover.HomOver, CategoryTheory.PreZeroHypercover.homOverIdEquivHom, CategoryTheory.PreZeroHypercover.Hom, CategoryTheory.PreZeroHypercover.CombinatoriallyEquivalent, CategoryTheory.PreZeroHypercover.TautologicallyEquivalent, CategoryTheory.PreZeroHypercover.tautologicallyEquivalent_of_combinatoriallyEquivalent, CategoryTheory.PreZeroHypercover.nonempty_hom_and_nonempty_hom_of_tautologicallyEquivalent, CategoryTheory.PreZeroHypercover.combinatoriallyEquivalent_refl
statement: formalized
proof: formalized
---

# 7.8 Families of morphisms with fixed target

Section 7.8 of the Stacks Project, [Tag 00VS](https://stacks.math.columbia.edu/tag/00VS). 8 tags here are carried by 23 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00VT, a definition

[Tag 00VT](https://stacks.math.columbia.edu/tag/00VT) in the Stacks Project.

**`CategoryTheory.PreZeroHypercover.HomOver`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercover/ZeroOver.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercover/ZeroOver.lean#L61). The attribute's comment: “(1) A morphism of families of morphisms with fixed target.”.

> **Stacks 00VT (1)**: a *morphism of families of morphisms with fixed target* from
> `𝒰 = {U i ⟶ S}` to `𝒱 = {V j ⟶ T}` over a morphism `g : S ⟶ T` of the targets. It consists
> of a map of index sets `s₀`, and for each index `i` a morphism `h₀ i : U i ⟶ V (s₀ i)`,
> subject to commutativity of the square
>
> ```
> U i          ⟶  V (s₀ i)
>  |                 |
>  v                 v
>  S           ⟶     T
> ```
>
> Mathlib's `PreZeroHypercover.Hom` is the special case in which the two families have the
> same target and `g` is the identity; see `homOverIdEquivHom`.

```lean
structure HomOver {S T : C} (E : PreZeroHypercover.{w} S) (F : PreZeroHypercover.{w'} T)
    (g : S ⟶ T)
```

**`CategoryTheory.PreZeroHypercover.homOverIdEquivHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercover/ZeroOver.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercover/ZeroOver.lean#L108). The attribute's comment: “(2) The special case `U = V` with `U ⟶ V` the identity: a refinement.”.

> **Stacks 00VT (2)**: a *refinement* is a morphism of families with fixed target whose
> morphism of targets is the identity. Such morphisms are exactly Mathlib's
> `PreZeroHypercover.Hom`, the morphisms of the category of families of morphisms with the
> given fixed target.

```lean
def homOverIdEquivHom (E : PreZeroHypercover.{w} S) (F : PreZeroHypercover.{w'} S) :
    E.HomOver F (𝟙 S) ≃ E.Hom F
```

Declarations registered for the tag:

- [`CategoryTheory.PreZeroHypercover.Hom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.PreZeroHypercover.Hom#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Hypercover/ZeroOver.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercover/ZeroOver.lean#L114) (StacksFrontier): “(2) Refinements of a family of morphisms with fixed target are the morphisms of Mathlib's category of such families; `homOverIdEquivHom` identifies them with the morphisms of 00VT (1) whose morphism of targets is the identity.”.

## Tag 00VU, a definition

[Tag 00VU](https://stacks.math.columbia.edu/tag/00VU) in the Stacks Project.

**`CategoryTheory.PreZeroHypercover.CombinatoriallyEquivalent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Pretopology/CombinatorialEquivalence.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Pretopology/CombinatorialEquivalence.lean#L53). The attribute's comment: “(1)”.

> **Stacks 00VU (1).** Two families of morphisms with the same fixed target `U` are
> *combinatorially equivalent* if there are maps `α : I → J` and `β : J → I` with
> `φ_i = ψ_{α i}` and `ψ_j = φ_{β j}`.
>
> An equality of morphisms `φ_i = ψ_{α i}` presupposes an equality of their sources
> `U_i = V_{α i}`, which is the `h` below; `eqToHom` transports along it.

```lean
def CombinatoriallyEquivalent
    (E : PreZeroHypercover.{w} U) (F : PreZeroHypercover.{w'} U) : Prop
```

**`CategoryTheory.PreZeroHypercover.TautologicallyEquivalent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Pretopology/CombinatorialEquivalence.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Pretopology/CombinatorialEquivalence.lean#L65). The attribute's comment: “(2)”.

> **Stacks 00VU (2).** Two families of morphisms with the same fixed target `U` are
> *tautologically equivalent* if there are maps `α : I → J` and `β : J → I` together with, for
> every index, a commutative triangle over `U` whose horizontal arrow is an *isomorphism*:
> `U_i ≅ V_{α i}` over `U`, and `V_j ≅ U_{β j}` over `U`.

```lean
def TautologicallyEquivalent
    (E : PreZeroHypercover.{w} U) (F : PreZeroHypercover.{w'} U) : Prop
```

## Tag 00VV, a lemma

[Tag 00VV](https://stacks.math.columbia.edu/tag/00VV) in the Stacks Project.

**`CategoryTheory.PreZeroHypercover.tautologicallyEquivalent_of_combinatoriallyEquivalent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Pretopology/EquivalenceComparison.lean, line 46](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Pretopology/EquivalenceComparison.lean#L46). The attribute's comment: “(1)”.

> **Stacks 00VV (1).** Combinatorially equivalent families are tautologically equivalent: an
> equality of sources gives an isomorphism between them, via `eqToIso`.

```lean
theorem tautologicallyEquivalent_of_combinatoriallyEquivalent
    (E : PreZeroHypercover.{w} U) (F : PreZeroHypercover.{w'} U) :
    CombinatoriallyEquivalent E F → TautologicallyEquivalent E F
```

**`CategoryTheory.PreZeroHypercover.nonempty_hom_and_nonempty_hom_of_tautologicallyEquivalent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Pretopology/EquivalenceComparison.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Pretopology/EquivalenceComparison.lean#L57). The attribute's comment: “(2)”.

> **Stacks 00VV (2).** Tautologically equivalent families refine each other: the horizontal
> isomorphism of each triangle is in particular a morphism over the common target, so the
> triangles assemble into a `PreZeroHypercover.Hom` in each direction.

```lean
theorem nonempty_hom_and_nonempty_hom_of_tautologicallyEquivalent
    (E : PreZeroHypercover.{w} U) (F : PreZeroHypercover.{w'} U) :
    TautologicallyEquivalent E F → Nonempty (E.Hom F) ∧ Nonempty (F.Hom E)
```

**`CategoryTheory.PreZeroHypercover.combinatoriallyEquivalent_refl`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Pretopology/EquivalenceComparison.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Pretopology/EquivalenceComparison.lean#L97). The attribute's comment: “(3)”.

> **Stacks 00VV (3).** Combinatorial equivalence is reflexive.

```lean
theorem combinatoriallyEquivalent_refl (E : PreZeroHypercover.{w} U) :
    CombinatoriallyEquivalent E E
```

**`CategoryTheory.PreZeroHypercover.combinatoriallyEquivalent_trans`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Pretopology/EquivalenceComparison.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Pretopology/EquivalenceComparison.lean#L104). The attribute's comment: “(3)”.

> **Stacks 00VV (3).** Combinatorial equivalence is transitive: compose the index maps and
> the source equalities, and `eqToHom_trans` composes the transports.

```lean
theorem combinatoriallyEquivalent_trans (E : PreZeroHypercover.{w} U)
    (F : PreZeroHypercover.{w'} U) (G : PreZeroHypercover.{w''} U) :
    CombinatoriallyEquivalent E F → CombinatoriallyEquivalent F G →
      CombinatoriallyEquivalent E G
```

**`CategoryTheory.PreZeroHypercover.combinatoriallyEquivalent_equivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Pretopology/EquivalenceComparison.lean, line 117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Pretopology/EquivalenceComparison.lean#L117). The attribute's comment: “(3)”.

> **Stacks 00VV (3)** as stated there: combinatorial equivalence *is* an equivalence relation
> on the families of morphisms with fixed target `U`.

```lean
theorem combinatoriallyEquivalent_equivalence :
    _root_.Equivalence (fun E F : PreZeroHypercover.{w} U => CombinatoriallyEquivalent E F)
```

**`CategoryTheory.PreZeroHypercover.tautologicallyEquivalent_refl`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Pretopology/EquivalenceComparison.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Pretopology/EquivalenceComparison.lean#L127). The attribute's comment: “(4)”.

> **Stacks 00VV (4).** Tautological equivalence is reflexive.

```lean
theorem tautologicallyEquivalent_refl (E : PreZeroHypercover.{w} U) :
    TautologicallyEquivalent E E
```

**`CategoryTheory.PreZeroHypercover.tautologicallyEquivalent_trans`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Pretopology/EquivalenceComparison.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Pretopology/EquivalenceComparison.lean#L134). The attribute's comment: “(4)”.

> **Stacks 00VV (4).** Tautological equivalence is transitive: compose the index maps, and
> compose the triangles' horizontal isomorphisms with `Iso.trans`.

```lean
theorem tautologicallyEquivalent_trans (E : PreZeroHypercover.{w} U)
    (F : PreZeroHypercover.{w'} U) (G : PreZeroHypercover.{w''} U) :
    TautologicallyEquivalent E F → TautologicallyEquivalent F G →
      TautologicallyEquivalent E G
```

**`CategoryTheory.PreZeroHypercover.tautologicallyEquivalent_equivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Pretopology/EquivalenceComparison.lean, line 150](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Pretopology/EquivalenceComparison.lean#L150). The attribute's comment: “(4)”.

> **Stacks 00VV (4)** as stated there: tautological equivalence *is* an equivalence relation
> on the families of morphisms with fixed target `U`.

```lean
theorem tautologicallyEquivalent_equivalence :
    _root_.Equivalence (fun E F : PreZeroHypercover.{w} U => TautologicallyEquivalent E F)
```

**`CategoryTheory.PreZeroHypercover.nonempty_hom_refl`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Pretopology/EquivalenceComparison.lean, line 160](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Pretopology/EquivalenceComparison.lean#L160). The attribute's comment: “(5)”.

> **Stacks 00VV (5).** Every family refines itself, by the identity refinement.

```lean
theorem nonempty_hom_refl (E : PreZeroHypercover.{w} U) :
    Nonempty (E.Hom E) ∧ Nonempty (E.Hom E)
```

**`CategoryTheory.PreZeroHypercover.nonempty_hom_trans`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Pretopology/EquivalenceComparison.lean, line 166](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Pretopology/EquivalenceComparison.lean#L166). The attribute's comment: “(5)”.

> **Stacks 00VV (5).** Mutual refinement is transitive, by composing refinements.

```lean
theorem nonempty_hom_trans (E : PreZeroHypercover.{w} U) (F : PreZeroHypercover.{w'} U)
    (G : PreZeroHypercover.{w''} U) :
    (Nonempty (E.Hom F) ∧ Nonempty (F.Hom E)) → (Nonempty (F.Hom G) ∧ Nonempty (G.Hom F)) →
      (Nonempty (E.Hom G) ∧ Nonempty (G.Hom E))
```

**`CategoryTheory.PreZeroHypercover.nonempty_hom_equivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Pretopology/EquivalenceComparison.lean, line 175](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Pretopology/EquivalenceComparison.lean#L175). The attribute's comment: “(5)”.

> **Stacks 00VV (5)** as stated there: mutual refinement *is* an equivalence relation on the
> families of morphisms with fixed target `U`. Symmetry is the swap.

```lean
theorem nonempty_hom_equivalence :
    _root_.Equivalence
      (fun E F : PreZeroHypercover.{w} U => Nonempty (E.Hom F) ∧ Nonempty (F.Hom E))
```

## Tag 00VW, a lemma

[Tag 00VW](https://stacks.math.columbia.edu/tag/00VW) in the Stacks Project.

**`CategoryTheory.PreZeroHypercover.isSheafFor_presieve₀_iff_of_tautologicallyEquivalent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Pretopology/TautologicalRelaxed.lean, line 37](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Pretopology/TautologicalRelaxed.lean#L37).

> **Stacks 00VW.** Tautologically equivalent families of morphisms with a fixed target
> generate the same sieve, hence impose the same sheaf condition on every presheaf.

```lean
theorem isSheafFor_presieve₀_iff_of_tautologicallyEquivalent
    (E : PreZeroHypercover.{w} U) (F : PreZeroHypercover.{w'} U)
    (h : TautologicallyEquivalent E F) (P : Cᵒᵖ ⥤ Type t) :
    Presieve.IsSheafFor P E.presieve₀ ↔ Presieve.IsSheafFor P F.presieve₀
```

## Tag 0G1K, a lemma

[Tag 0G1K](https://stacks.math.columbia.edu/tag/0G1K) in the Stacks Project.

**`CategoryTheory.PreZeroHypercover.injective_of_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Pretopology/GeneratedTopology.lean, line 33](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Pretopology/GeneratedTopology.lean#L33).

> **Stacks 0G1K.** Let `𝒰 = {U_i ⟶ U}` and `𝒱 = {V_j ⟶ U}` be families of morphisms with
> fixed target `U`, and let `φ` exhibit `𝒱` as a refinement of `𝒰`. If `F(U) ⟶ ∏_j F(V_j)` is
> injective, then so is `F(U) ⟶ ∏_i F(U_i)`: each `U_i` is reached from some `V_j` through `φ`,
> so agreeing on all the `V_j` already forces agreement on all the `U_i`.

```lean
theorem injective_of_hom (𝒰 : PreZeroHypercover.{w} U) (𝒱 : PreZeroHypercover.{w'} U)
    (φ : 𝒱.Hom 𝒰) (F : Cᵒᵖ ⥤ Type t)
    (hinj : Function.Injective
      fun (x : F.obj (Opposite.op U)) (j : 𝒱.I₀) => F.map (𝒱.f j).op x) :
    Function.Injective
      fun (x : F.obj (Opposite.op U)) (i : 𝒰.I₀) => F.map (𝒰.f i).op x
```

## Tag 0G1L, a lemma

[Tag 0G1L](https://stacks.math.columbia.edu/tag/0G1L) in the Stacks Project.

**`isSheafFor_ofArrows_of_refinement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Descent/SheafForTransArrows.lean, line 86](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Descent/SheafForTransArrows.lean#L86).

> Let `{πU i : Uᵢ i ⟶ U}` and `{πV j : V j ⟶ U}` be families of morphisms such that each `πV j`
> factors as `f j ≫ πU (α j)`, and let `UV i j` be a pullback of `πU i` and `πV j`. If `ℱ` is a
> sheaf for `{πV j}` and, for each `i`, the restriction maps `ℱ(Uᵢ i) ⟶ ℱ(UV i j)` are jointly
> injective, then `ℱ` is a sheaf for `{πU i}`.

```lean
theorem isSheafFor_ofArrows_of_refinement
    {C : Type*} [Category C] {U : C}
    {I J : Type*} (Uᵢ : I → C) (V : J → C) (UV : I → J → C)
    (πU : ∀ i, Uᵢ i ⟶ U) (πV : ∀ j, V j ⟶ U)
    (α : J → I) (f : ∀ j, V j ⟶ Uᵢ (α j))
    (hf : ∀ j, f j ≫ πU (α j) = πV j)
    (uvToV : ∀ i j, UV i j ⟶ V j) (uvToU : ∀ i j, UV i j ⟶ Uᵢ i)
    (huv : ∀ i j, uvToV i j ≫ πV j = uvToU i j ≫ πU i)
    (hpbUU : ∀ i i', HasPullback (πU i) (πU i'))
    (hpbUV : ∀ i j, IsLimit (PullbackCone.mk (uvToV i j) (uvToU i j) (huv i j)))
    (hpbVV : ∀ j j', HasPullback (πV j) (πV j'))
    (ℱ : Cᵒᵖ ⥤ Type*)
    (hV : Presieve.IsSheafFor ℱ (Presieve.ofArrows V πV))
    (hinj : ∀ i, Function.Injective fun s : ℱ.obj (op (Uᵢ i)) =>
      fun j : J => ℱ.map (uvToU i j).op s) :
    Presieve.IsSheafFor ℱ (Presieve.ofArrows Uᵢ πU)
```

## Tag 00VX, a lemma

[Tag 00VX](https://stacks.math.columbia.edu/tag/00VX) in the Stacks Project.

**`Covering.isSheaf_of_tautologicallyEquivalent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Pretopology/SiteSheavesUpToRefinement.lean, line 80](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Pretopology/SiteSheavesUpToRefinement.lean#L80). The attribute's comment: “(1)”.

> **Stacks 00VX (1)**, the inclusion: if every covering of the site `IsCov₁` is tautologically
> equivalent to some covering of the site `IsCov₂`, then `Sh(C, IsCov₂) ⊆ Sh(C, IsCov₁)`.

```lean
theorem isSheaf_of_tautologicallyEquivalent {IsCov₁ : Covering.{u, v, w₁} C → Prop}
    {IsCov₂ : Covering.{u, v, w₂} C → Prop} (_h₁ : IsSite IsCov₁) (_h₂ : IsSite IsCov₂)
    (h : ∀ 𝒰 : Covering.{u, v, w₁} C, IsCov₁ 𝒰 → ∃ 𝒱 : PreZeroHypercover.{w₂} 𝒰.1,
      IsCov₂ ⟨𝒰.1, 𝒱⟩ ∧ PreZeroHypercover.TautologicallyEquivalent 𝒰.2 𝒱)
    (P : Cᵒᵖ ⥤ Type t) (hP : IsSheaf IsCov₂ P) : IsSheaf IsCov₁ P
```

**`Covering.isSheaf_iff_of_tautologicallyEquivalent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Pretopology/SiteSheavesUpToRefinement.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Pretopology/SiteSheavesUpToRefinement.lean#L93). The attribute's comment: “(1)”.

> **Stacks 00VX (1)**, the equality: if moreover every covering of `IsCov₂` is tautologically
> equivalent to some covering of `IsCov₁`, then the two sites have the same sheaves.

```lean
theorem isSheaf_iff_of_tautologicallyEquivalent {IsCov₁ : Covering.{u, v, w₁} C → Prop}
    {IsCov₂ : Covering.{u, v, w₂} C → Prop} (h₁ : IsSite IsCov₁) (h₂ : IsSite IsCov₂)
    (h₁₂ : ∀ 𝒰 : Covering.{u, v, w₁} C, IsCov₁ 𝒰 → ∃ 𝒱 : PreZeroHypercover.{w₂} 𝒰.1,
      IsCov₂ ⟨𝒰.1, 𝒱⟩ ∧ PreZeroHypercover.TautologicallyEquivalent 𝒰.2 𝒱)
    (h₂₁ : ∀ 𝒰 : Covering.{u, v, w₂} C, IsCov₂ 𝒰 → ∃ 𝒱 : PreZeroHypercover.{w₁} 𝒰.1,
      IsCov₁ ⟨𝒰.1, 𝒱⟩ ∧ PreZeroHypercover.TautologicallyEquivalent 𝒰.2 𝒱)
    (P : Cᵒᵖ ⥤ Type t) : IsSheaf IsCov₁ P ↔ IsSheaf IsCov₂ P
```

**`Covering.isSheaf_of_factorsThru`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Pretopology/SiteSheavesUpToRefinement.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Pretopology/SiteSheavesUpToRefinement.lean#L110). The attribute's comment: “(2)”.

> **Stacks 00VX (2)**, the inclusion: if every covering of the site `IsCov₁` is refined by some
> covering of the site `IsCov₂`, then `Sh(C, IsCov₂) ⊆ Sh(C, IsCov₁)`.
>
> As in the source, a sheaf for `IsCov₂` is a sheaf for the refining covering `{Vⱼ ⟶ U}` and,
> by the base change axiom of `IsCov₂`, separated for each `{Vⱼ ×_U Uᵢ ⟶ Uᵢ}`; this is the input
> of Stacks 0G1L, here `Presieve.isSheafFor_of_factorsThru`.

```lean
theorem isSheaf_of_factorsThru {IsCov₁ : Covering.{u, v, w₁} C → Prop}
    {IsCov₂ : Covering.{u, v, w₂} C → Prop} (_h₁ : IsSite IsCov₁) (h₂ : IsSite IsCov₂)
    (h : ∀ 𝒰 : Covering.{u, v, w₁} C, IsCov₁ 𝒰 → ∃ 𝒱 : PreZeroHypercover.{w₂} 𝒰.1,
      IsCov₂ ⟨𝒰.1, 𝒱⟩ ∧ 𝒱.presieve₀.FactorsThru 𝒰.2.presieve₀)
    (P : Cᵒᵖ ⥤ Type t) (hP : IsSheaf IsCov₂ P) : IsSheaf IsCov₁ P
```

**`Covering.isSheaf_iff_of_factorsThru`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Pretopology/SiteSheavesUpToRefinement.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Pretopology/SiteSheavesUpToRefinement.lean#L127). The attribute's comment: “(2)”.

> **Stacks 00VX (2)**, the equality: if moreover every covering of `IsCov₂` is refined by some
> covering of `IsCov₁`, then the two sites have the same sheaves.

```lean
theorem isSheaf_iff_of_factorsThru {IsCov₁ : Covering.{u, v, w₁} C → Prop}
    {IsCov₂ : Covering.{u, v, w₂} C → Prop} (h₁ : IsSite IsCov₁) (h₂ : IsSite IsCov₂)
    (h₁₂ : ∀ 𝒰 : Covering.{u, v, w₁} C, IsCov₁ 𝒰 → ∃ 𝒱 : PreZeroHypercover.{w₂} 𝒰.1,
      IsCov₂ ⟨𝒰.1, 𝒱⟩ ∧ 𝒱.presieve₀.FactorsThru 𝒰.2.presieve₀)
    (h₂₁ : ∀ 𝒰 : Covering.{u, v, w₂} C, IsCov₂ 𝒰 → ∃ 𝒱 : PreZeroHypercover.{w₁} 𝒰.1,
      IsCov₁ ⟨𝒰.1, 𝒱⟩ ∧ 𝒱.presieve₀.FactorsThru 𝒰.2.presieve₀)
    (P : Cᵒᵖ ⥤ Type t) : IsSheaf IsCov₁ P ↔ IsSheaf IsCov₂ P
```

## Tag 00VY, a lemma

[Tag 00VY](https://stacks.math.columbia.edu/tag/00VY) in the Stacks Project.

**`CategoryTheory.PreZeroHypercover.sh_eq_of_forall_combinatoriallyEquivalent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Pretopology/SameTopology.lean, line 201](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Pretopology/SameTopology.lean#L201).

> **Stacks 00VY**: if `Cov₁ ⊆ Cov` and `Cov₂ ⊆ Cov` and every covering in `Cov` is
> combinatorially equivalent to a covering in `Cov₁` and to a covering in `Cov₂`, then
> `Sh(𝒞, Cov₁) = Sh(𝒞, Cov₂)`. The source assumes that `Cov` satisfies the axioms of 00VH and that
> `Cov₁`, `Cov₂` are sites; the conclusion holds for arbitrary covering data, so this statement
> takes no site axiom and no fibre products and contains the source's as a special case. Here
> `Sh Cov` is the category of sheaves for the topology generated by `Cov`;
> `forall_isSheafFor_iff_of_forall_combinatoriallyEquivalent` gives the same conclusion for the
> sheaf condition taken family by family.

```lean
theorem sh_eq_of_forall_combinatoriallyEquivalent (Cov Cov₁ Cov₂ : CovData.{w, v, u} C)
    (hCov₁_sub : CovData.Subset Cov₁ Cov) (hCov₂_sub : CovData.Subset Cov₂ Cov)
    (h₁ : ∀ ⦃U : C⦄ ⦃E : PreZeroHypercover.{w} U⦄, E ∈ Cov U →
      ∃ F : PreZeroHypercover.{w} U, F ∈ Cov₁ U ∧ CombinatoriallyEquivalent E F)
    (h₂ : ∀ ⦃U : C⦄ ⦃E : PreZeroHypercover.{w} U⦄, E ∈ Cov U →
      ∃ F : PreZeroHypercover.{w} U, F ∈ Cov₂ U ∧ CombinatoriallyEquivalent E F) :
    Sh Cov₁ = Sh Cov₂
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 7.8, Tag 00VS](https://stacks.math.columbia.edu/tag/00VS)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
