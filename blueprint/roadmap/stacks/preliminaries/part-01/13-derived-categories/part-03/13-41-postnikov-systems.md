---
declaration: section
origin: cited
lean: CategoryTheory.Triangulated.PostnikovSystem, CategoryTheory.Triangulated.PostnikovSystem.Hom, CategoryTheory.Triangulated.postnikovSystem_small_cases, CategoryTheory.Triangulated.PostnikovSystem.hom_shift_obj_eq_zero_and_exists_hom, CategoryTheory.Triangulated.PostnikovSystem.subsingleton_hom_last, CategoryTheory.Triangulated.PostnikovSystem.subsingleton_hom_of_hom_shift_eq_zero, CategoryTheory.Triangulated.PostnikovSystem.exists_not_subsingleton_hom, CategoryTheory.Triangulated.nonempty_postnikovSystem_of_hom_shift_eq_zero
statement: formalized
proof: formalized
---

# 13.41 Postnikov systems

Section 13.41 of the Stacks Project, [Tag 0D7Y](https://stacks.math.columbia.edu/tag/0D7Y). 5 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0D7Z, a definition

[Tag 0D7Z](https://stacks.math.columbia.edu/tag/0D7Z) in the Stacks Project.

**`CategoryTheory.Triangulated.PostnikovSystem`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/PostnikovSystems.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/PostnikovSystems.lean#L95). The attribute's comment: “Postnikov system; the morphisms of Postnikov systems are `PostnikovSystem.Hom`”.

> A *Postnikov system* for a complex `Xₙ ⟶ Xₙ₋₁ ⟶ ⋯ ⟶ X₀` in a pretriangulated category,
> the morphisms of the complex being `d i : X i.succ ⟶ X i.castSucc`: objects `Y₀, …, Yₙ` together
> with an isomorphism `Y₀ ⟶ X₀` and distinguished triangles
> `Yᵢ₊₁ ⟶ Xᵢ₊₁ ⟶ Yᵢ ⟶ Yᵢ₊₁⟦1⟧` in which the composition `Xᵢ₊₁ ⟶ Yᵢ ⟶ Xᵢ` is the given morphism
> `Xᵢ₊₁ ⟶ Xᵢ`. The morphisms of Postnikov systems, the second notion of this Stacks definition, are
> `CategoryTheory.Triangulated.PostnikovSystem.Hom`.

```lean
public structure PostnikovSystem {n : ℕ} (X : Fin (n + 1) → D)
    (d : ∀ i : Fin n, X i.succ ⟶ X i.castSucc)
```

**`CategoryTheory.Triangulated.PostnikovSystem.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/PostnikovSystems.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/PostnikovSystems.lean#L128). The attribute's comment: “morphism of Postnikov systems”.

> A *morphism of Postnikov systems* `S ⟶ S'` lying over a family of morphisms
> `f i : Xᵢ ⟶ X'ᵢ` between two complexes `Xₙ ⟶ ⋯ ⟶ X₀` and `X'ₙ ⟶ ⋯ ⟶ X'₀` of the same length:
> morphisms `hom i : Yᵢ ⟶ Y'ᵢ` making every diagram of the two systems commute, that is compatible
> with the morphisms `Yᵢ ⟶ Xᵢ`, `Xᵢ₊₁ ⟶ Yᵢ` and `Yᵢ ⟶ Yᵢ₊₁⟦1⟧`. Equivalently, `f` and `hom`
> form morphisms of all the distinguished triangles `Yᵢ₊₁ ⟶ Xᵢ₊₁ ⟶ Yᵢ ⟶ Yᵢ₊₁⟦1⟧` of the two
> systems. That `f` is a morphism of complexes is not imposed: it follows, see `Hom.comm_d`.

```lean
public structure Hom (f : ∀ i, X i ⟶ X' i) (S : PostnikovSystem X d)
    (S' : PostnikovSystem X' d')
```

## Tag 0D81, a lemma

[Tag 0D81](https://stacks.math.columbia.edu/tag/0D81) in the Stacks Project.

**`CategoryTheory.Triangulated.postnikovSystem_small_cases`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/PostnikovSystemsSmallCases.lean, line 313](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/PostnikovSystemsSmallCases.lean#L313). The attribute's comment: “existence in (1)–(3), the unique extension of morphisms in (1) and the extension in (2) hold in every pretriangulated category; the non-uniqueness in (2), the non-extension in (3) and the non-existence in (4), for every n > 2, are witnessed in the triangulated homotopy category K(ℤ-Mod).”.

> Let `D` be a pretriangulated category and consider Postnikov systems for complexes
> `Xₙ ⟶ ⋯ ⟶ X₀` of length `n`, with morphisms of Postnikov systems in the sense of
> `PostnikovSystem.IsHomOver`.
>
> 1. For `n = 0` Postnikov systems always exist and any morphism of complexes extends to a unique
>    morphism of Postnikov systems.
> 2. For `n = 1` Postnikov systems always exist and any morphism of complexes extends to a morphism
>    of Postnikov systems; this extension is not unique in general.
> 3. For `n = 2` Postnikov systems always exist, but morphisms of complexes do not extend to
>    morphisms of Postnikov systems in general.
> 4. For `n > 2` Postnikov systems do not always exist.
>
> The failures in (2), (3) and (4) are exhibited in the homotopy category of `ℤ`-modules, which is
> triangulated.

```lean
theorem postnikovSystem_small_cases :
    ((∀ (X : Fin 1 → D) (d : ∀ i : Fin 0, X i.succ ⟶ X i.castSucc),
        Nonempty (PostnikovSystem X d)) ∧
      ∀ {X X' : Fin 1 → D} {d : ∀ i : Fin 0, X i.succ ⟶ X i.castSucc}
        {d' : ∀ i : Fin 0, X' i.succ ⟶ X' i.castSucc} (S : PostnikovSystem X d)
        (S' : PostnikovSystem X' d') (f : ∀ i, X i ⟶ X' i),
        (∀ i : Fin 0, d i ≫ f i.castSucc = f i.succ ≫ d' i) →
        ∃! g : ∀ i, S.obj i ⟶ S'.obj i, S.IsHomOver S' f g) ∧
    ((∀ (X : Fin 2 → D) (d : ∀ i : Fin 1, X i.succ ⟶ X i.castSucc),
        Nonempty (PostnikovSystem X d)) ∧
      (∀ {X X' : Fin 2 → D} {d : ∀ i : Fin 1, X i.succ ⟶ X i.castSucc}
        {d' : ∀ i : Fin 1, X' i.succ ⟶ X' i.castSucc} (S : PostnikovSystem X d)
        (S' : PostnikovSystem X' d') (f : ∀ i, X i ⟶ X' i),
        (∀ i : Fin 1, d i ≫ f i.castSucc = f i.succ ≫ d' i) →
        ∃ g : ∀ i, S.obj i ⟶ S'.obj i, S.IsHomOver S' f g) ∧
      ∃ (X : Fin 2 → HomotopyCategory (ModuleCat.{0} ℤ) (ComplexShape.up ℤ))
        (d : ∀ i : Fin 1, X i.succ ⟶ X i.castSucc) (S : PostnikovSystem X d)
        (f : ∀ i, X i ⟶ X i), (∀ i : Fin 1, d i ≫ f i.castSucc = f i.succ ≫ d i) ∧
        ∃ g g' : ∀ i, S.obj i ⟶ S.obj i, S.IsHomOver S f g ∧ S.IsHomOver S f g' ∧ g ≠ g') ∧
    ((∀ (X : Fin 3 → D) (d : ∀ i : Fin 2, X i.succ ⟶ X i.castSucc), d 1 ≫ d 0 = 0 →
        Nonempty (PostnikovSystem X d)) ∧
      ∃ (X : Fin 3 → HomotopyCategory (ModuleCat.{0} ℤ) (ComplexShape.up ℤ))
        (d : ∀ i : Fin 2, X i.succ ⟶ X i.castSucc), d 1 ≫ d 0 = 0 ∧
        ∃ S S' : PostnikovSystem X d, ¬ ∃ g, S.IsHomOver S' (fun i => 𝟙 (X i)) g) ∧
    (∀ n : ℕ, 2 < n → ∃ (X : Fin (n + 1) → HomotopyCategory (ModuleCat.{0} ℤ) (ComplexShape.up ℤ))
      (d : ∀ i : Fin n, X i.succ ⟶ X i.castSucc),
      (∀ (i : Fin n) (h : (i : ℕ) + 1 < n), d ⟨(i : ℕ) + 1, h⟩ ≫ d i = 0) ∧
        IsEmpty (PostnikovSystem X d)) ∧
    IsTriangulated (HomotopyCategory (ModuleCat.{0} ℤ) (ComplexShape.up ℤ))
```

## Tag 0D82, a lemma

[Tag 0D82](https://stacks.math.columbia.edu/tag/0D82) in the Stacks Project.

**`CategoryTheory.Triangulated.PostnikovSystem.hom_shift_obj_eq_zero_and_exists_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/PostnikovSystems.lean, line 542](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/PostnikovSystems.lean#L542).

> Let `Xₙ ⟶ ⋯ ⟶ X₀` and `X'ₙ ⟶ ⋯ ⟶ X'₀` be complexes in a pretriangulated category, let `S'`
> be a Postnikov system for the second one, and assume that every morphism `Xᵢ⟦i - j - 1⟧ ⟶ X'ⱼ`
> with `i > j + 1` is zero. Then
>
> 1. every morphism `Xᵢ⟦i - j - 1⟧ ⟶ Y'ⱼ` with `i > j + 1` is zero, and
> 2. for every Postnikov system `S` for the first complex, every morphism of complexes
>    `f i : Xᵢ ⟶ X'ᵢ` extends to a (nonunique) morphism of Postnikov systems `S ⟶ S'`, i.e. to a
>    family `g i : Yᵢ ⟶ Y'ᵢ` compatible with the morphisms `Yᵢ ⟶ Xᵢ`, `Xᵢ₊₁ ⟶ Yᵢ` and
>    `Yᵢ ⟶ Yᵢ₊₁⟦1⟧` of the two systems.

```lean
theorem PostnikovSystem.hom_shift_obj_eq_zero_and_exists_hom {n : ℕ}
    (X : Fin (n + 1) → D) (d : ∀ i : Fin n, X i.succ ⟶ X i.castSucc)
    {X' : Fin (n + 1) → D} {d' : ∀ i : Fin n, X' i.succ ⟶ X' i.castSucc}
    (S' : PostnikovSystem X' d')
    (h : ∀ i j : Fin (n + 1), (j : ℕ) + 1 < (i : ℕ) →
      ∀ f : (X i)⟦((i : ℕ) : ℤ) - ((j : ℕ) : ℤ) - 1⟧ ⟶ X' j, f = 0) :
    (∀ i j : Fin (n + 1), (j : ℕ) + 1 < (i : ℕ) →
        ∀ f : (X i)⟦((i : ℕ) : ℤ) - ((j : ℕ) : ℤ) - 1⟧ ⟶ S'.obj j, f = 0) ∧
      ∀ (S : PostnikovSystem X d) (f : ∀ i, X i ⟶ X' i),
        (∀ i : Fin n, d i ≫ f i.castSucc = f i.succ ≫ d' i) →
        ∃ g : ∀ i, S.obj i ⟶ S'.obj i,
          (∀ i, g i ≫ S'.π i = S.π i ≫ f i) ∧
          (∀ i : Fin n, S.p i ≫ g i.castSucc = f i.succ ≫ S'.p i) ∧
          (∀ i : Fin n, S.δ i ≫ (g i.succ)⟦(1 : ℤ)⟧' = g i.castSucc ≫ S'.δ i)
```

## Tag 0FXE, a lemma

[Tag 0FXE](https://stacks.math.columbia.edu/tag/0FXE) in the Stacks Project.

**`CategoryTheory.Triangulated.PostnikovSystem.subsingleton_hom_last`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/PostnikovSystems.lean, line 963](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/PostnikovSystems.lean#L963). The attribute's comment: “(1), (2), (3): uniqueness of the component on the totalizations”.

> Let `Xₙ ⟶ ⋯ ⟶ X₀` and `X'ₙ ⟶ ⋯ ⟶ X'₀` be complexes in a pretriangulated category, let
> `f i : Xᵢ ⟶ X'ᵢ` be a family of morphisms, and let `S`, `S'` be Postnikov systems for the two
> complexes, with objects `Yᵢ`, `Y'ᵢ`. If
>
> 1. every morphism `Xᵢ⟦i⟧ ⟶ Y'ₙ⟦n⟧` with `i ≥ 1` is zero, or
> 2. every morphism `Yₙ⟦n⟧ ⟶ X'ⱼ⟦j⟧` with `j < n` is zero, or
> 3. every morphism `Xᵢ⟦i - j + 1⟧ ⟶ X'ⱼ` and every morphism `Xⱼ ⟶ X'ᵢ⟦i - j⟧` with `i < j` is
>    zero,
>
> then any two morphisms of Postnikov systems `S ⟶ S'` over `f` — families `g i : Yᵢ ⟶ Y'ᵢ`
> compatible with the morphisms `Yᵢ ⟶ Xᵢ`, `Xᵢ₊₁ ⟶ Yᵢ` and `Yᵢ ⟶ Yᵢ₊₁⟦1⟧` of the two systems —
> induce the same morphism `Yₙ ⟶ Y'ₙ` on the totalizations. Under (3) they agree in every
> component (`PostnikovSystem.subsingleton_hom_of_hom_shift_eq_zero`); under (1) or (2) the
> intermediate components need not agree (`PostnikovSystem.exists_not_subsingleton_hom` in
> `StacksFrontier.CategoryTheory.Triangulated.PostnikovSystemsCounterexample`), and the
> uniqueness of the totalization component is the corrected form of these two cases.

```lean
theorem PostnikovSystem.subsingleton_hom_last {n : ℕ}
    {X X' : Fin (n + 1) → D} {d : ∀ i : Fin n, X i.succ ⟶ X i.castSucc}
    {d' : ∀ i : Fin n, X' i.succ ⟶ X' i.castSucc}
    (S : PostnikovSystem X d) (S' : PostnikovSystem X' d') (f : ∀ i, X i ⟶ X' i)
    (h : (∀ i : Fin (n + 1), 0 < (i : ℕ) →
            ∀ u : (X i)⟦((i : ℕ) : ℤ)⟧ ⟶ (S'.obj (Fin.last n))⟦(n : ℤ)⟧, u = 0) ∨
         (∀ j : Fin (n + 1), (j : ℕ) < n →
            ∀ u : (S.obj (Fin.last n))⟦(n : ℤ)⟧ ⟶ (X' j)⟦((j : ℕ) : ℤ)⟧, u = 0) ∨
         ((∀ i j : Fin (n + 1), (i : ℕ) < (j : ℕ) →
            ∀ u : (X i)⟦((i : ℕ) : ℤ) - ((j : ℕ) : ℤ) + 1⟧ ⟶ X' j, u = 0) ∧
          (∀ i j : Fin (n + 1), (i : ℕ) < (j : ℕ) →
            ∀ u : X j ⟶ (X' i)⟦((i : ℕ) : ℤ) - ((j : ℕ) : ℤ)⟧, u = 0))) :
    ((fun g : ∀ i, S.obj i ⟶ S'.obj i => g (Fin.last n)) ''
      {g : ∀ i, S.obj i ⟶ S'.obj i |
        (∀ i, g i ≫ S'.π i = S.π i ≫ f i) ∧
        (∀ i : Fin n, S.p i ≫ g i.castSucc = f i.succ ≫ S'.p i) ∧
        (∀ i : Fin n, S.δ i ≫ (g i.succ)⟦(1 : ℤ)⟧' = g i.castSucc ≫ S'.δ i)}).Subsingleton
```

**`CategoryTheory.Triangulated.PostnikovSystem.subsingleton_hom_of_hom_shift_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/PostnikovSystems.lean, line 994](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/PostnikovSystems.lean#L994). The attribute's comment: “(3): at most one morphism of Postnikov systems, all components”.

> Let `Xₙ ⟶ ⋯ ⟶ X₀` and `X'ₙ ⟶ ⋯ ⟶ X'₀` be complexes in a pretriangulated category, let
> `f i : Xᵢ ⟶ X'ᵢ` be a family of morphisms, and let `S`, `S'` be Postnikov systems for the two
> complexes, with objects `Yᵢ`, `Y'ᵢ`. If every morphism `Xᵢ⟦i - j + 1⟧ ⟶ X'ⱼ` and every morphism
> `Xⱼ ⟶ X'ᵢ⟦i - j⟧` with `i < j` is zero (case (3) of the Stacks lemma), then there is at most one
> morphism of Postnikov systems `S ⟶ S'` over `f`: any two families `g i : Yᵢ ⟶ Y'ᵢ` compatible
> with the morphisms `Yᵢ ⟶ Xᵢ`, `Xᵢ₊₁ ⟶ Yᵢ` and `Yᵢ ⟶ Yᵢ₊₁⟦1⟧` of the two systems agree in every
> component.

```lean
theorem PostnikovSystem.subsingleton_hom_of_hom_shift_eq_zero {n : ℕ}
    {X X' : Fin (n + 1) → D} {d : ∀ i : Fin n, X i.succ ⟶ X i.castSucc}
    {d' : ∀ i : Fin n, X' i.succ ⟶ X' i.castSucc}
    (S : PostnikovSystem X d) (S' : PostnikovSystem X' d') (f : ∀ i, X i ⟶ X' i)
    (h : ∀ i j : Fin (n + 1), (i : ℕ) < (j : ℕ) →
      ∀ u : (X i)⟦((i : ℕ) : ℤ) - ((j : ℕ) : ℤ) + 1⟧ ⟶ X' j, u = 0)
    (h' : ∀ i j : Fin (n + 1), (i : ℕ) < (j : ℕ) →
      ∀ u : X j ⟶ (X' i)⟦((i : ℕ) : ℤ) - ((j : ℕ) : ℤ)⟧, u = 0) :
    {g : ∀ i, S.obj i ⟶ S'.obj i |
      (∀ i, g i ≫ S'.π i = S.π i ≫ f i) ∧
      (∀ i : Fin n, S.p i ≫ g i.castSucc = f i.succ ≫ S'.p i) ∧
      (∀ i : Fin n, S.δ i ≫ (g i.succ)⟦(1 : ℤ)⟧' = g i.castSucc ≫ S'.δ i)}.Subsingleton
```

**`CategoryTheory.Triangulated.PostnikovSystem.exists_not_subsingleton_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/PostnikovSystemsCounterexample.lean, line 124](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/PostnikovSystemsCounterexample.lean#L124). The attribute's comment: “(1), (2): counterexample to uniqueness of the whole morphism of Postnikov systems”.

> Cases (1) and (2) of [Stacks, Tag 0FXE] do not give uniqueness of the whole morphism of
> Postnikov systems. In any pretriangulated category with a nonzero object `B` there are complexes
> `X₃ ⟶ ⋯ ⟶ X₀` and `X'₃ ⟶ ⋯ ⟶ X'₀`, Postnikov systems `S`, `S'` for them and a morphism of
> complexes `f` such that every morphism `Xᵢ⟦i⟧ ⟶ Y'₃⟦3⟧` with `i ≥ 1` is zero (case (1)) and every
> morphism `Y₃⟦3⟧ ⟶ X'ⱼ⟦j⟧` with `j < 3` is zero (case (2)), and yet there are two different
> morphisms of Postnikov systems `S ⟶ S'` over `f`. Under (1) or (2) the component `Yₙ ⟶ Y'ₙ` on
> the totalizations is unique, which is `PostnikovSystem.subsingleton_hom_last`.

```lean
theorem PostnikovSystem.exists_not_subsingleton_hom (B : D) (hB : ¬ IsZero B) :
    ∃ (X X' : Fin 4 → D) (d : ∀ i : Fin 3, X i.succ ⟶ X i.castSucc)
      (d' : ∀ i : Fin 3, X' i.succ ⟶ X' i.castSucc) (S : PostnikovSystem X d)
      (S' : PostnikovSystem X' d') (f : ∀ i, X i ⟶ X' i),
      (∀ i : Fin 3, d i ≫ f i.castSucc = f i.succ ≫ d' i) ∧
      (∀ i : Fin 4, 0 < (i : ℕ) →
        ∀ u : (X i)⟦((i : ℕ) : ℤ)⟧ ⟶ (S'.obj (Fin.last 3))⟦((3 : ℕ) : ℤ)⟧, u = 0) ∧
      (∀ j : Fin 4, (j : ℕ) < 3 →
        ∀ u : (S.obj (Fin.last 3))⟦((3 : ℕ) : ℤ)⟧ ⟶ (X' j)⟦((j : ℕ) : ℤ)⟧, u = 0) ∧
      ¬ {g : ∀ i, S.obj i ⟶ S'.obj i |
          (∀ i, g i ≫ S'.π i = S.π i ≫ f i) ∧
          (∀ i : Fin 3, S.p i ≫ g i.castSucc = f i.succ ≫ S'.p i) ∧
          (∀ i : Fin 3, S.δ i ≫ (g i.succ)⟦(1 : ℤ)⟧' = g i.castSucc ≫ S'.δ i)}.Subsingleton
```

## Tag 0D83, a lemma

[Tag 0D83](https://stacks.math.columbia.edu/tag/0D83) in the Stacks Project.

**`CategoryTheory.Triangulated.nonempty_postnikovSystem_of_hom_shift_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/PostnikovSystems.lean, line 678](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/PostnikovSystems.lean#L678).

> A complex `Xₙ ⟶ ⋯ ⟶ X₀` in a pretriangulated category, with morphisms `d i : Xᵢ₊₁ ⟶ Xᵢ`,
> admits a Postnikov system as soon as every morphism `Xᵢ⟦i - j - 2⟧ ⟶ Xⱼ` with `i > j + 2` is
> zero. Without that vanishing condition Postnikov systems need not exist once `n > 2`; for
> `n ≤ 2` the condition is vacuous and this is
> `CategoryTheory.Triangulated.nonempty_postnikovSystem_of_length_le_two`.

```lean
theorem nonempty_postnikovSystem_of_hom_shift_eq_zero {n : ℕ} (X : Fin (n + 1) → D)
    (d : ∀ i : Fin n, X i.succ ⟶ X i.castSucc)
    (hd : ∀ (i : Fin n) (h : (i : ℕ) + 1 < n), d ⟨(i : ℕ) + 1, h⟩ ≫ d i = 0)
    (h : ∀ i j : Fin (n + 1), (j : ℕ) + 2 < (i : ℕ) →
      ∀ u : (X i)⟦((i : ℕ) : ℤ) - ((j : ℕ) : ℤ) - 2⟧ ⟶ X j, u = 0) :
    Nonempty (PostnikovSystem X d)
```

**`CategoryTheory.Triangulated.PostnikovSystem.exists_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/PostnikovSystems.lean, line 743](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/PostnikovSystems.lean#L743).

> Let `Xₙ ⟶ ⋯ ⟶ X₀` be a diagram in a pretriangulated category, with morphisms
> `d i : Xᵢ₊₁ ⟶ Xᵢ`, such that every morphism `Xᵢ⟦i - j - 1⟧ ⟶ Xⱼ` with `i > j + 1` is zero. Then
> for every diagram `X'ₙ ⟶ ⋯ ⟶ X'₀` and every isomorphism `f i : Xᵢ ≅ X'ᵢ` of diagrams, any
> Postnikov systems `S`, `S'` for the two are isomorphic over `f`: there is a family of isomorphisms
> `g i : Yᵢ ≅ Y'ᵢ` compatible with the morphisms `Yᵢ ⟶ Xᵢ`, `Xᵢ₊₁ ⟶ Yᵢ` and `Yᵢ ⟶ Yᵢ₊₁⟦1⟧` of the
> two systems. In particular, at `X' = X`, `d' = d` and `f = 𝟙`, any two Postnikov systems for
> `Xₙ ⟶ ⋯ ⟶ X₀` are isomorphic.

```lean
theorem PostnikovSystem.exists_iso {n : ℕ} {X X' : Fin (n + 1) → D}
    {d : ∀ i : Fin n, X i.succ ⟶ X i.castSucc} {d' : ∀ i : Fin n, X' i.succ ⟶ X' i.castSucc}
    (h : ∀ i j : Fin (n + 1), (j : ℕ) + 1 < (i : ℕ) →
      ∀ u : (X i)⟦((i : ℕ) : ℤ) - ((j : ℕ) : ℤ) - 1⟧ ⟶ X j, u = 0)
    (S : PostnikovSystem X d) (S' : PostnikovSystem X' d') (f : ∀ i, X i ≅ X' i)
    (hf : ∀ i : Fin n, d i ≫ (f i.castSucc).hom = (f i.succ).hom ≫ d' i) :
    ∃ g : ∀ i, S.obj i ≅ S'.obj i,
      (∀ i, (g i).hom ≫ S'.π i = S.π i ≫ (f i).hom) ∧
      (∀ i : Fin n, S.p i ≫ (g i.castSucc).hom = (f i.succ).hom ≫ S'.p i) ∧
      (∀ i : Fin n, S.δ i ≫ ((g i.succ).hom)⟦(1 : ℤ)⟧' =
        (g i.castSucc).hom ≫ S'.δ i)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 13.41, Tag 0D7Y](https://stacks.math.columbia.edu/tag/0D7Y)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
