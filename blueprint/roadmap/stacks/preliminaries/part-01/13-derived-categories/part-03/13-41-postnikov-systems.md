---
declaration: section
origin: cited
lean: CategoryTheory.Triangulated.PostnikovSystem, CategoryTheory.Triangulated.nonempty_postnikovSystem_of_length_le_two, CategoryTheory.Triangulated.PostnikovSystem.hom_shift_obj_eq_zero_and_exists_hom, CategoryTheory.Triangulated.PostnikovSystem.subsingleton_hom_last, CategoryTheory.Triangulated.nonempty_postnikovSystem_of_hom_shift_eq_zero, CategoryTheory.Triangulated.PostnikovSystem.exists_iso
statement: formalized
proof: formalized
---

# 13.41 Postnikov systems

Section 13.41 of the Stacks Project, [Tag 0D7Y](https://stacks.math.columbia.edu/tag/0D7Y). 5 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0D7Z, a definition

[Tag 0D7Z](https://stacks.math.columbia.edu/tag/0D7Z) in the Stacks Project.

**`CategoryTheory.Triangulated.PostnikovSystem`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/PostnikovSystems.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/PostnikovSystems.lean#L84).

> A *Postnikov system* for a complex `Xₙ ⟶ Xₙ₋₁ ⟶ ⋯ ⟶ X₀` in a pretriangulated category,
> the morphisms of the complex being `d i : X i.succ ⟶ X i.castSucc`: objects `Y₀, …, Yₙ` together
> with an isomorphism `Y₀ ⟶ X₀` and distinguished triangles
> `Yᵢ₊₁ ⟶ Xᵢ₊₁ ⟶ Yᵢ ⟶ Yᵢ₊₁⟦1⟧` in which the composition `Xᵢ₊₁ ⟶ Yᵢ ⟶ Xᵢ` is the given morphism
> `Xᵢ₊₁ ⟶ Xᵢ`.

```lean
public structure PostnikovSystem {n : ℕ} (X : Fin (n + 1) → D)
    (d : ∀ i : Fin n, X i.succ ⟶ X i.castSucc)
```

## Tag 0D81, a lemma

[Tag 0D81](https://stacks.math.columbia.edu/tag/0D81) in the Stacks Project.

**`CategoryTheory.Triangulated.nonempty_postnikovSystem_of_length_le_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/PostnikovSystems.lean, line 299](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/PostnikovSystems.lean#L299).

> A complex `Xₙ ⟶ Xₙ₋₁ ⟶ ⋯ ⟶ X₀` of length `n ≤ 2` in a pretriangulated category admits a
> Postnikov system. The bound is sharp: for `n > 2` Postnikov systems do not always exist.

```lean
theorem nonempty_postnikovSystem_of_length_le_two {n : ℕ}
    (hn : n ≤ 2) (X : Fin (n + 1) → D) (d : ∀ i : Fin n, X i.succ ⟶ X i.castSucc)
    (hd : ∀ (i : Fin n) (h : (i : ℕ) + 1 < n), d ⟨(i : ℕ) + 1, h⟩ ≫ d i = 0) :
    Nonempty (PostnikovSystem X d)
```

## Tag 0D82, a lemma

[Tag 0D82](https://stacks.math.columbia.edu/tag/0D82) in the Stacks Project.

**`CategoryTheory.Triangulated.PostnikovSystem.hom_shift_obj_eq_zero_and_exists_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/PostnikovSystems.lean, line 453](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/PostnikovSystems.lean#L453).

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

**`CategoryTheory.Triangulated.PostnikovSystem.subsingleton_hom_last`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/PostnikovSystems.lean, line 870](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/PostnikovSystems.lean#L870).

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
> induce the same morphism `Yₙ ⟶ Y'ₙ` on the totalizations.

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

## Tag 0D83, a lemma

[Tag 0D83](https://stacks.math.columbia.edu/tag/0D83) in the Stacks Project.

**`CategoryTheory.Triangulated.nonempty_postnikovSystem_of_hom_shift_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/PostnikovSystems.lean, line 589](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/PostnikovSystems.lean#L589).

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

**`CategoryTheory.Triangulated.PostnikovSystem.exists_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/PostnikovSystems.lean, line 654](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/PostnikovSystems.lean#L654).

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
