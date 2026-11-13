---
declaration: section
origin: cited
lean: CategoryTheory.Functor.iterate, CategoryTheory.Functor.iterate_add, CategoryTheory.Godement.face, CategoryTheory.Godement.degeneracy, CategoryTheory.Godement.exists_augmented_standardResolution, CategoryTheory.Godement.exists_augmented_standardResolution_whisker, CategoryTheory.SimplicialObject.Augmented.exists_section_of_comp_hom_app_zero_eq_id, CategoryTheory.Godement.exists_homotopy_hcomp_hcomp
statement: formalized
proof: formalized
---

# 14.33 Preparation for standard resolutions

Section 14.33 of the Stacks Project, [Tag 0G5L](https://stacks.math.columbia.edu/tag/0G5L). 6 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0G5M, an example

[Tag 0G5M](https://stacks.math.columbia.edu/tag/0G5M) in the Stacks Project.

**`CategoryTheory.Functor.iterate`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/StandardResolution/Godement.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/StandardResolution/Godement.lean#L97).

> **Stacks 0G5M**.
> The `n`-fold composite `Y ∘ … ∘ Y` of an endofunctor `Y : C ⥤ C` with itself, with
> `Y.iterate 0 = 𝟭 C` and `Y.iterate (n + 1) = Y.iterate n ⋙ Y`, so that the copy of `Y` added at
> each step is the outermost one. On objects it is the `n`-fold iterate of `Y.obj`, whence the name.
> Godement's `X_n`, a composite of `n + 1` copies of `Y`, is `Y.iterate (n + 1)`, and his `X_{-1}` is
> `Y.iterate 0`.

```lean
public def iterate (Y : C ⥤ C) : ℕ → C ⥤ C
```

**`CategoryTheory.Functor.iterate_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/StandardResolution/Godement.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/StandardResolution/Godement.lean#L120).

> **Stacks 0G5M**.
> The powers of an endofunctor are additive: `Y^{m+n} = Y^m ∘ Y^n` in `⋙`-order, i.e.
> `Y.iterate (m + n) = Y.iterate m ⋙ Y.iterate n`. This is the observation `X_{n+m+1} = X_n ∘ X_m`,
> where `X_n = Y.iterate (n + 1)`.

```lean
public theorem iterate_add (Y : C ⥤ C) (m n : ℕ) :
    Y.iterate (m + n) = Y.iterate m ⋙ Y.iterate n
```

**`CategoryTheory.Godement.face`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/StandardResolution/Godement.lean, line 138](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/StandardResolution/Godement.lean#L138).

> **Stacks 0G5M**.
> The face `d^n_j : X_n ⟶ X_{n-1}` attached to a transformation `d : Y ⟶ 𝟭 C`, for `n ≥ 0` and
> `0 ≤ j ≤ n`: it whiskers `d` into the `j`-th of the `n + 1` copies of `Y` in
> `X_n = Y.iterate (n + 1)`, counted from the left, i.e. from the outside, so that
> `d^n_j = 1_{X_{j-1}} ⋆ d ⋆ 1_{X_{n-j-1}}`. It is defined by the recursion `d^n_0 = d ⋆ 1_{X_{n-1}}`
> and `d^{n+1}_{j+1} = 1_Y ⋆ d^n_j`; in particular `face d 0 0 = d : X_0 = Y ⟶ 𝟭 C` is the
> augmentation. No compatibility between `d` and a comultiplication is assumed.

```lean
public def face (d : Y ⟶ 𝟭 C) :
    (n : ℕ) → Fin (n + 1) → (Y.iterate (n + 1) ⟶ Y.iterate n)
```

**`CategoryTheory.Godement.degeneracy`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/StandardResolution/Godement.lean, line 152](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/StandardResolution/Godement.lean#L152).

> **Stacks 0G5M**.
> The degeneracy `s^n_j : X_n ⟶ X_{n+1}` attached to a transformation `s : Y ⟶ Y ⋙ Y`, for `n ≥ 0`
> and `0 ≤ j ≤ n`: it whiskers `s` into the `j`-th of the `n + 1` copies of `Y` in
> `X_n = Y.iterate (n + 1)`, counted from the left, i.e. from the outside, so that
> `s^n_j = 1_{X_{j-1}} ⋆ s ⋆ 1_{X_{n-j-1}}`. It is defined by the recursion `s^n_0 = s ⋆ 1_{X_{n-1}}`
> and `s^{n+1}_{j+1} = 1_Y ⋆ s^n_j`. No compatibility between `s` and a counit is assumed.

```lean
public def degeneracy (s : Y ⟶ Y ⋙ Y) :
    (n : ℕ) → Fin (n + 1) → (Y.iterate (n + 1) ⟶ Y.iterate (n + 2))
```

## Tag 0G5N, a lemma

[Tag 0G5N](https://stacks.math.columbia.edu/tag/0G5N) in the Stacks Project.

**`CategoryTheory.Godement.exists_augmented_standardResolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/StandardResolution/Godement.lean, line 612](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/StandardResolution/Godement.lean#L612).

> **Stacks 0G5N**.
> Let `Y : C ⥤ C` be an endofunctor with transformations `d : Y ⟶ 𝟭 C` and `s : Y ⟶ Y ⋙ Y` satisfying
> the counit identities `1_Y = (d ⋆ 1_Y) ∘ s = (1_Y ⋆ d) ∘ s` and coassociativity
> `(s ⋆ 1_Y) ∘ s = (1_Y ⋆ s) ∘ s`, i.e. let `(Y, d, s)` be a comonad on `C`. Then the powers
> `X_n = Y.iterate (n + 1)`, with the faces `Godement.face d` and the degeneracies
> `Godement.degeneracy s`, are a simplicial object of the category `C ⥤ C` of endofunctors of `C`,
> augmented over `X_{-1} = Y.iterate 0 = 𝟭 C` by `face d 0 0 = d : X_0 = Y ⟶ 𝟭 C`.

```lean
public theorem exists_augmented_standardResolution {C : Type u} [Category.{v} C] {Y : C ⥤ C}
    (d : Y ⟶ 𝟭 C) (s : Y ⟶ Y ⋙ Y)
    (left_counit : s ≫ Functor.whiskerLeft Y d = 𝟙 Y)
    (right_counit : s ≫ Functor.whiskerRight d Y = 𝟙 Y)
    (coassoc : s ≫ Functor.whiskerLeft Y s = s ≫ Functor.whiskerRight s Y) :
    ∃ (X : SimplicialObject.Augmented (C ⥤ C))
      (h : ∀ n : ℕ, X.left.obj (op ⦋n⦌) = Y.iterate (n + 1)) (hX : X.right = 𝟭 C),
      (∀ (n : ℕ) (j : Fin (n + 2)),
        X.left.δ j = eqToHom (h (n + 1)) ≫ face d (n + 1) j ≫ eqToHom (h n).symm) ∧
      (∀ (n : ℕ) (j : Fin (n + 1)),
        X.left.σ j = eqToHom (h n) ≫ degeneracy s n j ≫ eqToHom (h (n + 1)).symm) ∧
      X.hom.app (op ⦋0⦌) = eqToHom (h 0) ≫ face d 0 0 ≫ eqToHom hX.symm
```

## Tag 0G5P, an example

[Tag 0G5P](https://stacks.math.columbia.edu/tag/0G5P) in the Stacks Project.

**`CategoryTheory.Godement.exists_augmented_standardResolution_whisker`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/StandardResolution/Godement.lean, line 698](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/StandardResolution/Godement.lean#L698).

> **Stacks 0G5P**.
> Let `Y : C ⥤ C` be an endofunctor with transformations `d : Y ⟶ 𝟭 C` and `s : Y ⟶ Y ⋙ Y` satisfying
> the counit identities `1_Y = (d ⋆ 1_Y) ∘ s = (1_Y ⋆ d) ∘ s` and coassociativity
> `(s ⋆ 1_Y) ∘ s = (1_Y ⋆ s) ∘ s`, i.e. let `(Y, d, s)` be a comonad on `C`, and let `F : A ⥤ C` and
> `G : C ⥤ B` be functors. Then the conjugated powers `G ∘ X_n ∘ F = F ⋙ Y.iterate (n+1) ⋙ G`, with
> the faces `1_G ⋆ d^n_j ⋆ 1_F` and degeneracies `1_G ⋆ s^n_j ⋆ 1_F` obtained from `Godement.face d`
> and `Godement.degeneracy s` by whiskering with `F` and `G`, are a simplicial object of the category
> `A ⥤ B` of functors from `A` to `B`, augmented over `G ∘ F = F ⋙ G` by `1_G ⋆ d ⋆ 1_F`.

```lean
public theorem exists_augmented_standardResolution_whisker
    {A : Type u₁} [Category.{v₁} A] {B : Type u₂} [Category.{v₂} B]
    {C : Type u} [Category.{v} C] {Y : C ⥤ C}
    (d : Y ⟶ 𝟭 C) (s : Y ⟶ Y ⋙ Y) (F : A ⥤ C) (G : C ⥤ B)
    (left_counit : s ≫ Functor.whiskerLeft Y d = 𝟙 Y)
    (right_counit : s ≫ Functor.whiskerRight d Y = 𝟙 Y)
    (coassoc : s ≫ Functor.whiskerLeft Y s = s ≫ Functor.whiskerRight s Y) :
    ∃ (X : SimplicialObject.Augmented (A ⥤ B))
      (h : ∀ n : ℕ, X.left.obj (op ⦋n⦌) = F ⋙ Y.iterate (n + 1) ⋙ G)
      (hX : X.right = F ⋙ G),
      (∀ (n : ℕ) (j : Fin (n + 2)),
        X.left.δ j = eqToHom (h (n + 1)) ≫
          Functor.whiskerRight (Functor.whiskerLeft F (face d (n + 1) j)) G ≫
            eqToHom (h n).symm) ∧
      (∀ (n : ℕ) (j : Fin (n + 1)),
        X.left.σ j = eqToHom (h n) ≫
          Functor.whiskerRight (Functor.whiskerLeft F (degeneracy s n j)) G ≫
            eqToHom (h (n + 1)).symm) ∧
      X.hom.app (op ⦋0⦌) = eqToHom (h 0) ≫
        Functor.whiskerRight (Functor.whiskerLeft F (face d 0 0)) G ≫ eqToHom hX.symm
```

## Tag 0G5Q, a lemma

[Tag 0G5Q](https://stacks.math.columbia.edu/tag/0G5Q) in the Stacks Project.

**`CategoryTheory.SimplicialObject.Augmented.exists_section_of_comp_hom_app_zero_eq_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/StandardResolution/Godement.lean, line 768](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/StandardResolution/Godement.lean#L768).

> **Stacks 0G5Q**.
> Let `X` be an augmented simplicial object of `D`, with augmentation
> `ε = X.hom : X.left ⟶ const X.right`, and let `h₀ : X.right ⟶ X_0` satisfy `ε_0 ∘ h₀ = 1`. Then
> there is a morphism of simplicial objects `h : const X.right ⟶ X.left` restricting to `h₀` in
> degree `0` and satisfying `ε ∘ h = 1`; necessarily `h_n = u_n ∘ h₀` with `u_n : X_0 ⟶ X_n` induced
> by the unique morphism `⦋n⦌ ⟶ ⦋0⦌`.

```lean
public theorem exists_section_of_comp_hom_app_zero_eq_id {D : Type u} [Category.{v} D]
    (X : SimplicialObject.Augmented D) (h₀ : X.right ⟶ X.left.obj (op ⦋0⦌))
    (hh₀ : h₀ ≫ X.hom.app (op ⦋0⦌) = 𝟙 X.right) :
    ∃ h : (SimplicialObject.const D).obj X.right ⟶ X.left,
      h.app (op ⦋0⦌) = h₀ ∧ h ≫ X.hom = 𝟙 ((SimplicialObject.const D).obj X.right)
```

## Tag 0G5R, a lemma

[Tag 0G5R](https://stacks.math.columbia.edu/tag/0G5R) in the Stacks Project.

**`CategoryTheory.Godement.exists_homotopy_hcomp_hcomp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/StandardResolution/Whiskering.lean, line 657](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/StandardResolution/Whiskering.lean#L657).

> **Stacks 0G5R**.
> Let `Y : C ⥤ C` be an endofunctor with transformations `d : Y ⟶ 𝟭 C` and `s : Y ⟶ Y ⋙ Y`, let `F`,
> `F' : A ⥤ C` and `G`, `G' : C ⥤ B` be functors, and let `Z`, `Z'` be the augmented simplicial
> objects `G ∘ X ∘ F` and `G' ∘ X ∘ F'` of `A ⥤ B` obtained by conjugating the powers
> `X_n = Y.iterate (n + 1)`. Let `(a_n) : G ∘ X ⟶ G' ∘ X` and `(b_n) : X ∘ F ⟶ X ∘ F'` be morphisms
> of simplicial objects, i.e. families commuting with the faces `Godement.face d` and degeneracies
> `Godement.degeneracy s`, compatible via the augmentations with `a : G ⟶ G'` and `b : F ⟶ F'`. Then
> the two horizontal composites `a ⋆ (b_n)` and `(a_n) ⋆ b` are morphisms `Z ⟶ Z'` of augmented
> simplicial objects with component `a ⋆ b` over the augmentations, and they are homotopic: there is
> a simplicial homotopy from `(a_n) ⋆ b` to `a ⋆ (b_n)`, given by `h_{n, i} = a_{i-1} ⋆ b_{n-i}`.

```lean
public theorem exists_homotopy_hcomp_hcomp
    {A : Type u₁} [Category.{v₁} A] {B : Type u₂} [Category.{v₂} B]
    {C : Type u} [Category.{v} C] {Y : C ⥤ C}
    (d : Y ⟶ 𝟭 C) (s : Y ⟶ Y ⋙ Y) (F F' : A ⥤ C) (G G' : C ⥤ B)
    (a : G ⟶ G') (b : F ⟶ F')
    (an : (n : ℕ) → (Y.iterate (n + 1) ⋙ G ⟶ Y.iterate (n + 1) ⋙ G'))
    (bn : (n : ℕ) → (F ⋙ Y.iterate (n + 1) ⟶ F' ⋙ Y.iterate (n + 1)))
    (han_face : ∀ (n : ℕ) (j : Fin (n + 2)),
      an (n + 1) ≫ Functor.whiskerRight (face d (n + 1) j) G' =
        Functor.whiskerRight (face d (n + 1) j) G ≫ an n)
    (han_degeneracy : ∀ (n : ℕ) (j : Fin (n + 1)),
      an n ≫ Functor.whiskerRight (degeneracy s n j) G' =
        Functor.whiskerRight (degeneracy s n j) G ≫ an (n + 1))
    (han_aug : an 0 ≫ Functor.whiskerRight (face d 0 0) G' =
      Functor.whiskerRight (face d 0 0) G ≫ a)
    (hbn_face : ∀ (n : ℕ) (j : Fin (n + 2)),
      bn (n + 1) ≫ Functor.whiskerLeft F' (face d (n + 1) j) =
        Functor.whiskerLeft F (face d (n + 1) j) ≫ bn n)
    (hbn_degeneracy : ∀ (n : ℕ) (j : Fin (n + 1)),
      bn n ≫ Functor.whiskerLeft F' (degeneracy s n j) =
        Functor.whiskerLeft F (degeneracy s n j) ≫ bn (n + 1))
    (hbn_aug : bn 0 ≫ Functor.whiskerLeft F' (face d 0 0) =
      Functor.whiskerLeft F (face d 0 0) ≫ b)
    (Z Z' : SimplicialObject.Augmented (A ⥤ B))
    (hZ : ∀ n : ℕ, Z.left.obj (op ⦋n⦌) = F ⋙ Y.iterate (n + 1) ⋙ G)
    (hZr : Z.right = F ⋙ G)
    (hZδ : ∀ (n : ℕ) (j : Fin (n + 2)), Z.left.δ j = eqToHom (hZ (n + 1)) ≫
      Functor.whiskerRight (Functor.whiskerLeft F (face d (n + 1) j)) G ≫ eqToHom (hZ n).symm)
    (hZσ : ∀ (n : ℕ) (j : Fin (n + 1)), Z.left.σ j = eqToHom (hZ n) ≫
      Functor.whiskerRight (Functor.whiskerLeft F (degeneracy s n j)) G ≫
        eqToHom (hZ (n + 1)).symm)
    (hZhom : Z.hom.app (op ⦋0⦌) = eqToHom (hZ 0) ≫
      Functor.whiskerRight (Functor.whiskerLeft F (face d 0 0)) G ≫ eqToHom hZr.symm)
    (hZ' : ∀ n : ℕ, Z'.left.obj (op ⦋n⦌) = F' ⋙ Y.iterate (n + 1) ⋙ G')
    (hZr' : Z'.right = F' ⋙ G')
    (hZδ' : ∀ (n : ℕ) (j : Fin (n + 2)), Z'.left.δ j = eqToHom (hZ' (n + 1)) ≫
      Functor.whiskerRight (Functor.whiskerLeft F' (face d (n + 1) j)) G' ≫ eqToHom (hZ' n).symm)
    (hZσ' : ∀ (n : ℕ) (j : Fin (n + 1)), Z'.left.σ j = eqToHom (hZ' n) ≫
      Functor.whiskerRight (Functor.whiskerLeft F' (degeneracy s n j)) G' ≫
        eqToHom (hZ' (n + 1)).symm)
    (hZhom' : Z'.hom.app (op ⦋0⦌) = eqToHom (hZ' 0) ≫
      Functor.whiskerRight (Functor.whiskerLeft F' (face d 0 0)) G' ≫ eqToHom hZr'.symm) :
    ∃ α β : Z ⟶ Z',
      (∀ n : ℕ, α.left.app (op ⦋n⦌) = eqToHom (hZ n) ≫
        NatTrans.hcomp (F := F ⋙ Y.iterate (n + 1)) (bn n) a ≫ eqToHom (hZ' n).symm) ∧
      (∀ n : ℕ, β.left.app (op ⦋n⦌) = eqToHom (hZ n) ≫
        NatTrans.hcomp b (an n) ≫ eqToHom (hZ' n).symm) ∧
      α.right = eqToHom hZr ≫ NatTrans.hcomp b a ≫ eqToHom hZr'.symm ∧
      β.right = eqToHom hZr ≫ NatTrans.hcomp b a ≫ eqToHom hZr'.symm ∧
      Nonempty (SimplicialObject.Homotopy β.left α.left)
```

## Tag 0G5S, a lemma

[Tag 0G5S](https://stacks.math.columbia.edu/tag/0G5S) in the Stacks Project.

**`CategoryTheory.Godement.exists_homotopy_whiskerLeft_whiskerRight`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/StandardResolution/Whiskering.lean, line 959](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/StandardResolution/Whiskering.lean#L959).

> **Stacks 0G5S**.
> Let `Y : C ⥤ C` be an endofunctor with transformations `d : Y ⟶ 𝟭 C` and `s : Y ⟶ Y ⋙ Y`, and let
> `X` be an augmented simplicial object of the category `C ⥤ C` of endofunctors of `C` whose terms
> are the powers `X_n = Y.iterate (n + 1)`, whose faces and degeneracies are `Godement.face d` and
> `Godement.degeneracy s`, and whose augmentation has target `𝟭 C`. Let `f : 𝟭 C ⟶ 𝟭 C` be an
> endomorphism of the identity functor. Then the two whiskerings `f ⋆ 1_{X_n}` and `1_{X_n} ⋆ f` of
> `f` onto the terms of `X` are morphisms of simplicial objects, compatible with `f` through the
> augmentation `ε : X ⟶ 𝟭 C`, i.e. they are endomorphisms of `X` in the category of augmented
> simplicial objects with component `f` over `𝟭 C`. Moreover they are homotopic: there is a
> simplicial homotopy from `1_X ⋆ f` to `f ⋆ 1_X`, given by `h_{n, i} = 1_i ⋆ f ⋆ 1_{n + 1 - i}`.

```lean
public theorem exists_homotopy_whiskerLeft_whiskerRight {C : Type u} [Category.{v} C]
    {Y : C ⥤ C} (d : Y ⟶ 𝟭 C) (s : Y ⟶ Y ⋙ Y) (f : 𝟭 C ⟶ 𝟭 C)
    (X : SimplicialObject.Augmented (C ⥤ C))
    (h : ∀ n : ℕ, X.left.obj (op ⦋n⦌) = Y.iterate (n + 1)) (hX : X.right = 𝟭 C)
    (hδ : ∀ (n : ℕ) (j : Fin (n + 2)),
      X.left.δ j = eqToHom (h (n + 1)) ≫ face d (n + 1) j ≫ eqToHom (h n).symm)
    (hσ : ∀ (n : ℕ) (j : Fin (n + 1)),
      X.left.σ j = eqToHom (h n) ≫ degeneracy s n j ≫ eqToHom (h (n + 1)).symm) :
    ∃ α β : X ⟶ X,
      (∀ n : ℕ, α.left.app (op ⦋n⦌) =
        eqToHom (h n) ≫ Functor.whiskerLeft (Y.iterate (n + 1)) f ≫ eqToHom (h n).symm) ∧
      (∀ n : ℕ, β.left.app (op ⦋n⦌) =
        eqToHom (h n) ≫ Functor.whiskerRight f (Y.iterate (n + 1)) ≫ eqToHom (h n).symm) ∧
      α.right = eqToHom hX ≫ f ≫ eqToHom hX.symm ∧
      β.right = eqToHom hX ≫ f ≫ eqToHom hX.symm ∧
      Nonempty (SimplicialObject.Homotopy β.left α.left)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 14.33, Tag 0G5L](https://stacks.math.columbia.edu/tag/0G5L)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
