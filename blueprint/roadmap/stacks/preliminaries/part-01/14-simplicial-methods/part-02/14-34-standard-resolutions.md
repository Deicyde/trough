---
declaration: section
origin: cited
lean: CategoryTheory.Adjunction, CategoryTheory.Adjunction.right_triangle, CategoryTheory.Adjunction.left_triangle, CategoryTheory.Comonad.exists_augmented_standardResolution, CategoryTheory.Adjunction.exists_homotopyInverse_whiskered_standardResolution, AlgebraicTopology.homotopyEquivalences_forget_iff_quasiIso_of_surjective, AlgebraicTopology.homotopyEquivalences_forget_iff_quasiIso_forget₂_of_surjective, ModuleCat.free_standardResolution_face_degeneracy_apply
statement: formalized
proof: formalized
---

# 14.34 Standard resolutions

Section 14.34 of the Stacks Project, [Tag 08N8](https://stacks.math.columbia.edu/tag/08N8). 9 tags here are carried by 7 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08N9, a situation

[Tag 08N9](https://stacks.math.columbia.edu/tag/08N9) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Adjunction`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Adjunction#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch14.lean, line 30](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch14.lean#L30) (StacksFrontier): “the situation: V : A ⥤ S with a left adjoint U : S ⥤ A, as the adjunction U ⊣ V”. References: SGA 3 I (5.3.1.1); SGA 4 II (6.5); SGA 4 IV (1.5); SGA 4 IV (3.1), “more general”.

## Tag 08NB, an equation

[Tag 08NB](https://stacks.math.columbia.edu/tag/08NB) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Adjunction.right_triangle`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Adjunction.right_triangle#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch14.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch14.lean#L122) (StacksFrontier): “V → VUV → V is the identity (for `adj : U ⊣ V`, Mathlib's `F = U`, `G = V`; up to unitors)”.
- [`CategoryTheory.Adjunction.left_triangle`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Adjunction.left_triangle#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch14.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch14.lean#L125) (StacksFrontier): “U → UVU → U is the identity (same conventions)”.

## Tag 08NC, a lemma

[Tag 08NC](https://stacks.math.columbia.edu/tag/08NC) in the Stacks Project.

**`CategoryTheory.Comonad.exists_augmented_standardResolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/StandardResolution/Basic.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/StandardResolution/Basic.lean#L179).

> **Stacks 08NC**.
> Let `G` be a comonad on a category `A`, with counit `G.ε : G ⟶ 𝟭 A` and comultiplication
> `G.δ : G ⟶ G ⋙ G`. The iterates `Z (n + 1)` of `G`, with `Z 0 = 𝟭 A`, carry faces
> `d n j : Z (n + 1) ⟶ Z n` and degeneracies `s n j : Z (n + 1) ⟶ Z (n + 2)` for `0 ≤ j ≤ n`,
> obtained by whiskering `G.ε`, resp. `G.δ`, into the `j`-th factor `G` counted from the left in the
> composite `Z (n + 1) = G ∘ ⋯ ∘ G`, and these are the faces and degeneracies of a simplicial object
> of the category `A ⥤ A` of endofunctors of `A`, augmented over the constant simplicial object `𝟭 A`
> by `ε₀ = d 0 0 = G.ε`.

```lean
public theorem exists_augmented_standardResolution {A : Type u} [Category.{v} A]
    (G : Comonad A) :
    ∃ (Z : ℕ → (A ⥤ A)) (hZ : ∀ n : ℕ, Z (n + 1) = Z n ⋙ (G : A ⥤ A))
      (d : ∀ n : ℕ, Fin (n + 1) → (Z (n + 1) ⟶ Z n))
      (s : ∀ n : ℕ, Fin (n + 1) → (Z (n + 1) ⟶ Z (n + 2))),
      Z 0 = 𝟭 A ∧
      (∀ n : ℕ, d n 0 = eqToHom (hZ n) ≫ Functor.whiskerLeft (Z n) G.ε) ∧
      (∀ (n : ℕ) (j : Fin (n + 1)),
        d (n + 1) j.succ =
          eqToHom (hZ (n + 1)) ≫ Functor.whiskerRight (d n j) (G : A ⥤ A) ≫
            eqToHom (hZ n).symm) ∧
      (∀ n : ℕ,
        s n 0 = eqToHom (hZ n) ≫ Functor.whiskerLeft (Z n) G.δ ≫
          Functor.whiskerRight (eqToHom (hZ n).symm) (G : A ⥤ A) ≫ eqToHom (hZ (n + 1)).symm) ∧
      (∀ (n : ℕ) (j : Fin (n + 1)),
        s (n + 1) j.succ =
          eqToHom (hZ (n + 1)) ≫ Functor.whiskerRight (s n j) (G : A ⥤ A) ≫
            eqToHom (hZ (n + 2)).symm) ∧
      ∃ (X : SimplicialObject.Augmented (A ⥤ A))
        (h : ∀ n : ℕ, X.left.obj (op ⦋n⦌) = Z (n + 1)) (hX : X.right = Z 0),
        (∀ (n : ℕ) (j : Fin (n + 2)),
          X.left.δ j = eqToHom (h (n + 1)) ≫ d (n + 1) j ≫ eqToHom (h n).symm) ∧
        (∀ (n : ℕ) (j : Fin (n + 1)),
          X.left.σ j = eqToHom (h n) ≫ s n j ≫ eqToHom (h (n + 1)).symm) ∧
        X.hom.app (op ⦋0⦌) = eqToHom (h 0) ≫ d 0 0 ≫ eqToHom hX.symm
```

## Tag 08ND, a lemma

[Tag 08ND](https://stacks.math.columbia.edu/tag/08ND) in the Stacks Project.

**`CategoryTheory.Adjunction.exists_homotopyInverse_whiskered_standardResolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/StandardResolution/Basic.lean, line 494](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/StandardResolution/Basic.lean#L494).

> **Stacks 08ND**.
> Let `V : A ⥤ S` have a left adjoint `U : S ⥤ A`, and let `X` be the standard resolution: the
> augmented simplicial object of `A ⥤ A` with terms the iterates `Z (n + 1)` of the comonad
> `U ∘ V`, faces and degeneracies `d`, `s` whiskering its counit, resp. its comultiplication,
> into the `j`-th factor, point `Z 0 = 𝟭 A` and augmentation `ε₀ = d 0 0`. Then the whiskered
> augmentations `1_V ⋆ ε : V ∘ X ⟶ V` and `ε ⋆ 1_U : X ∘ U ⟶ U` are homotopy equivalences: each
> admits a morphism `r` in the other direction such that both composites with it are homotopic to
> the identities, homotopic meaning related by the equivalence relation generated by the existence
> of a simplicial homotopy.

```lean
public theorem exists_homotopyInverse_whiskered_standardResolution
    {A : Type u₁} [Category.{v₁} A] {S : Type u₂} [Category.{v₂} S]
    {U : S ⥤ A} {V : A ⥤ S} (adj : U ⊣ V)
    (Z : ℕ → (A ⥤ A)) (hZ : ∀ n : ℕ, Z (n + 1) = Z n ⋙ (adj.toComonad : A ⥤ A))
    (d : ∀ n : ℕ, Fin (n + 1) → (Z (n + 1) ⟶ Z n))
    (s : ∀ n : ℕ, Fin (n + 1) → (Z (n + 1) ⟶ Z (n + 2)))
    (hZ₀ : Z 0 = 𝟭 A)
    (hd₀ : ∀ n : ℕ, d n 0 = eqToHom (hZ n) ≫ Functor.whiskerLeft (Z n) adj.toComonad.ε)
    (hd : ∀ (n : ℕ) (j : Fin (n + 1)), d (n + 1) j.succ =
      eqToHom (hZ (n + 1)) ≫ Functor.whiskerRight (d n j) (adj.toComonad : A ⥤ A) ≫
        eqToHom (hZ n).symm)
    (hs₀ : ∀ n : ℕ, s n 0 = eqToHom (hZ n) ≫ Functor.whiskerLeft (Z n) adj.toComonad.δ ≫
      Functor.whiskerRight (eqToHom (hZ n).symm) (adj.toComonad : A ⥤ A) ≫
        eqToHom (hZ (n + 1)).symm)
    (hs : ∀ (n : ℕ) (j : Fin (n + 1)), s (n + 1) j.succ =
      eqToHom (hZ (n + 1)) ≫ Functor.whiskerRight (s n j) (adj.toComonad : A ⥤ A) ≫
        eqToHom (hZ (n + 2)).symm)
    (X : SimplicialObject.Augmented (A ⥤ A))
    (h : ∀ n : ℕ, X.left.obj (Opposite.op ⦋n⦌) = Z (n + 1)) (hX : X.right = Z 0)
    (hδ : ∀ (n : ℕ) (j : Fin (n + 2)),
      X.left.δ j = eqToHom (h (n + 1)) ≫ d (n + 1) j ≫ eqToHom (h n).symm)
    (hσ : ∀ (n : ℕ) (j : Fin (n + 1)),
      X.left.σ j = eqToHom (h n) ≫ s n j ≫ eqToHom (h (n + 1)).symm)
    (hε : X.hom.app (Opposite.op ⦋0⦌) = eqToHom (h 0) ≫ d 0 0 ≫ eqToHom hX.symm)
    (a : X.left ⋙ (Functor.whiskeringRight A A S).obj V ⟶
      (Functor.const SimplexCategoryᵒᵖ).obj (X.right ⋙ V))
    (ha : ∀ n : SimplexCategoryᵒᵖ, a.app n = Functor.whiskerRight (X.hom.app n) V)
    (b : X.left ⋙ (Functor.whiskeringLeft S A A).obj U ⟶
      (Functor.const SimplexCategoryᵒᵖ).obj (U ⋙ X.right))
    (hb : ∀ n : SimplexCategoryᵒᵖ, b.app n = Functor.whiskerLeft U (X.hom.app n)) :
    (∃ r : (Functor.const SimplexCategoryᵒᵖ).obj (X.right ⋙ V) ⟶
        X.left ⋙ (Functor.whiskeringRight A A S).obj V,
      Relation.EqvGen (fun f g => Nonempty (SimplicialObject.Homotopy f g)) (a ≫ r) (𝟙 _) ∧
      Relation.EqvGen (fun f g => Nonempty (SimplicialObject.Homotopy f g)) (r ≫ a) (𝟙 _)) ∧
    (∃ r : (Functor.const SimplexCategoryᵒᵖ).obj (U ⋙ X.right) ⟶
        X.left ⋙ (Functor.whiskeringLeft S A A).obj U,
      Relation.EqvGen (fun f g => Nonempty (SimplicialObject.Homotopy f g)) (b ≫ r) (𝟙 _) ∧
      Relation.EqvGen (fun f g => Nonempty (SimplicialObject.Homotopy f g)) (r ≫ b) (𝟙 _))
```

## Tag 0G5T, an example

[Tag 0G5T](https://stacks.math.columbia.edu/tag/0G5T) in the Stacks Project.

**`AlgebraicTopology.homotopyEquivalences_forget_iff_quasiIso_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/StandardResolution/Basic.lean, line 1094](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/StandardResolution/Basic.lean#L1094).

> **Stacks 0G5T**.
> Let `R` be a ring and let `f : X ⟶ Y` be a morphism of simplicial `R`-modules which is surjective
> in each degree. Then the underlying morphism of simplicial sets `X ⋙ forget ⟶ Y ⋙ forget` is a
> homotopy equivalence — it admits a morphism of simplicial sets back whose two composites with it
> are homotopic to the identities — if and only if the induced morphism `s(X) ⟶ s(Y)` of associated
> chain complexes of `R`-modules is a quasi-isomorphism. Applied to the augmentation `X(M) ⟶ M` of
> the standard resolution of an `R`-module `M` by free modules, whose underlying augmentation of
> simplicial sets is a homotopy equivalence, this says that `M` is the only nonzero homology group of
> the complex associated to `X(M)`.

```lean
public theorem homotopyEquivalences_forget_iff_quasiIso_of_surjective {R : Type u} [Ring R]
    {X Y : SimplicialObject (ModuleCat.{v} R)} (f : X ⟶ Y)
    (hf : ∀ n : SimplexCategoryᵒᵖ, Function.Surjective (f.app n).hom) :
    SimplicialObject.homotopyEquivalences (Type v)
        (Functor.whiskerRight f (forget (ModuleCat.{v} R))) ↔
      QuasiIso ((alternatingFaceMapComplex (ModuleCat.{v} R)).map f)
```

## Tag 08NA, an example

[Tag 08NA](https://stacks.math.columbia.edu/tag/08NA) in the Stacks Project.

**`AlgebraicTopology.homotopyEquivalences_forget_iff_quasiIso_forget₂_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/StandardResolution/Basic.lean, line 1115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/StandardResolution/Basic.lean#L1115).

> **Stacks 08NA**.
> Let `A` be a ring and let `f : X ⟶ Y` be a morphism of simplicial `A`-algebras which is surjective
> in each degree. Then the underlying morphism of simplicial sets is a homotopy equivalence if and
> only if the induced morphism `s(X) ⟶ s(Y)` of the chain complexes associated to the underlying
> simplicial `A`-modules is a quasi-isomorphism. Applied to the augmentation `X(B) ⟶ B` of the
> standard resolution of a commutative `A`-algebra `B` by the polynomial algebras `A[A[⋯[B]⋯]]`,
> whose underlying augmentation of simplicial sets is a homotopy equivalence, this says that `B` is
> the only nonzero homology group of the complex of `A`-modules associated to `X(B)`.

```lean
public theorem homotopyEquivalences_forget_iff_quasiIso_forget₂_of_surjective {A : Type u}
    [CommRing A] {X Y : SimplicialObject (AlgCat.{v} A)} (f : X ⟶ Y)
    (hf : ∀ n : SimplexCategoryᵒᵖ, Function.Surjective (f.app n).hom) :
    SimplicialObject.homotopyEquivalences (Type v)
        (Functor.whiskerRight f (forget (AlgCat.{v} A))) ↔
      QuasiIso ((alternatingFaceMapComplex (ModuleCat.{v} A)).map
        (Functor.whiskerRight f (forget₂ (AlgCat.{v} A) (ModuleCat.{v} A))))
```

## Tag 0G5U, an example

[Tag 0G5U](https://stacks.math.columbia.edu/tag/0G5U) in the Stacks Project.

**`ModuleCat.free_standardResolution_face_degeneracy_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/StandardResolution/Basic.lean, line 1179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/StandardResolution/Basic.lean#L1179).

> **Stacks 0G5U**.
> Let `R` be a ring, `M` an `R`-module and `R[N]` the free `R`-module on the underlying set of an
> `R`-module `N`, with `[n] = ModuleCat.comonadMk n` and `∑ᵢ f nᵢ rᵢ = ModuleCat.comonadSum ξ f` for
> `ξ = ∑ᵢ rᵢ[nᵢ]`. For the simplicial `R`-module `X(M)` with `X₁(M) = R[R[M]]` and
> `X₂(M) = R[R[R[M]]]`, and a typical element `ξ = ∑ᵢ rᵢ[∑ⱼ r_ij[m_ij]]` of `X₁(M)`, the two faces
> `d₀, d₁ : R[R[M]] → R[M]` — the counit of the free-forgetful adjunction contracting the outer,
> resp. the inner, bracket — are given by `d₀(ξ) = ∑_{i,j} rᵢr_ij[m_ij]` and
> `d₁(ξ) = ∑ᵢ rᵢ[∑ⱼ r_ij m_ij]`, and the two degeneracies `s₀, s₁ : R[R[M]] → R[R[R[M]]]` — its
> comultiplication doubling the outer, resp. the inner, bracket — by `s₀(ξ) = ∑ᵢ rᵢ[[∑ⱼ r_ij[m_ij]]]`
> and `s₁(ξ) = ∑ᵢ rᵢ[∑ⱼ r_ij[[m_ij]]]`.

```lean
public theorem free_standardResolution_face_degeneracy_apply {R : Type u} [Ring R]
    (M : ModuleCat.{u} R)
    (ξ : ((adj R).toComonad.obj ((adj R).toComonad.obj M) : Type u)) :
    (adj R).toComonad.ε.app ((adj R).toComonad.obj M) ξ = comonadSum ξ (fun x r => r • x) ∧
      (adj R).toComonad.map ((adj R).toComonad.ε.app M) ξ =
        comonadSum ξ (fun x r => r • comonadMk (comonadSum x (fun m c => c • m))) ∧
      (adj R).toComonad.δ.app ((adj R).toComonad.obj M) ξ =
        comonadSum ξ (fun x r => r • comonadMk (comonadMk x)) ∧
      (adj R).toComonad.map ((adj R).toComonad.δ.app M) ξ =
        comonadSum ξ (fun x r =>
          r • comonadMk (comonadSum x (fun m c => c • comonadMk (comonadMk m))))
```

## Tag 09CB, an example

[Tag 09CB](https://stacks.math.columbia.edu/tag/09CB) in the Stacks Project.

**`AlgCat.face_eq_lift_and_degeneracy_eq_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/StandardResolution/Basic.lean, line 607](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/StandardResolution/Basic.lean#L607).

> **Stacks 09CB**.
> Let `A` be a ring and let `X` be an `A`-algebra. In the tower `Xₙ = A[A[⋯[X]⋯]]` (`n + 1` brackets)
> of the standard resolution of `X` for the free/forget adjunction, each stage being the free algebra
> on the previous one, the faces `dⁿⱼ` and degeneracies `sⁿⱼ` are described on the variables by:
> `dⁿ₀` substitutes for the variable `[z]` the element `z`, so it is `FreeAlgebra.lift A id` and
> `d⁰₀ : A[X] ⟶ X` is the augmentation; `sⁿ₀` sends `[z]` to `[[z]]`; and `dⁿ⁺¹ⱼ₊₁`, `sⁿ⁺¹ⱼ₊₁` send
> `[z]` to `[dⁿⱼ(z)]`, resp. `[sⁿⱼ(z)]`. In degree `1`, for
> `x = ∑ a_k [b_{k,1}] ⋯ [b_{k,n_k}] ∈ A[X]`, this is `d₀([x]) = x`,
> `d₁([x]) = [∑ a_k b_{k,1} ⋯ b_{k,n_k}]`, `s₀([x]) = [[x]]` and
> `s₁([x]) = [∑ a_k [[b_{k,1}]] ⋯ [[b_{k,n_k}]]]`.

```lean
public theorem face_eq_lift_and_degeneracy_eq_lift {A : Type u} [CommRing A] (X : AlgCat.{u} A)
    (n : ℕ) :
    ((Godement.face (adj (R := A)).toComonad.ε n 0).app X).hom = FreeAlgebra.lift A id ∧
      (∀ j : Fin (n + 1), ((Godement.face (adj (R := A)).toComonad.ε (n + 1) j.succ).app X).hom =
        FreeAlgebra.lift A (FreeAlgebra.ι A ∘
          ((Godement.face (adj (R := A)).toComonad.ε n j).app X).hom)) ∧
      ((Godement.degeneracy (adj (R := A)).toComonad.δ n 0).app X).hom =
        FreeAlgebra.lift A (fun z => FreeAlgebra.ι A (FreeAlgebra.ι A z)) ∧
      (∀ j : Fin (n + 1),
        ((Godement.degeneracy (adj (R := A)).toComonad.δ (n + 1) j.succ).app X).hom =
          FreeAlgebra.lift A (FreeAlgebra.ι A ∘
            ((Godement.degeneracy (adj (R := A)).toComonad.δ n j).app X).hom))
```

## Tag 08NE, an example

[Tag 08NE](https://stacks.math.columbia.edu/tag/08NE) in the Stacks Project.

**`AlgCat.exists_homotopyInverse_whiskered_standardResolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/StandardResolution/Basic.lean, line 967](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/StandardResolution/Basic.lean#L967).

> **Stacks 08NE**.
> Let `A` be a ring, let `U : Sets → Alg_A` be the free algebra functor and `V` the forgetful
> functor, and let `X` be the standard resolution of the comonad `Y = U ∘ V`: the augmented
> simplicial object of `Fun(Alg_A, Alg_A)` with terms the iterates `Xₙ = Y^{n+1}`, so that
> `Xₙ(B) = A[A[⋯[B]⋯]]` with `n + 1` brackets, faces `Godement.face`, degeneracies
> `Godement.degeneracy`, point `𝟭` and augmentation `d⁰₀`. Then the whiskered augmentations
> `1_V ⋆ ε : V ∘ X ⟶ V` and `ε ⋆ 1_U : X ∘ U ⟶ U` are homotopy equivalences with their homotopy
> inverses displayed: in degree `n` the first is the map of sets `b ↦ [⋯[b]⋯]` (`n + 1` brackets)
> and the second is the `A`-algebra map `∑ a [e₁]⋯[e_p] ↦ ∑ a [⋯[e₁]⋯]⋯[⋯[e_p]⋯]` sending a
> variable `[e]` to `[⋯[e]⋯]` (`n + 2` brackets), and both composites of each with the augmentation
> are homotopic to the identity, homotopic meaning related by the equivalence relation generated by
> the existence of a simplicial homotopy. Evaluating the first clause at an `A`-algebra `B` gives
> the homotopy equivalence of the underlying simplicial sets of `X(B) ⟶ B`, and the second at a set
> `E` the homotopy equivalence of simplicial `A`-algebras `X(A[E]) ⟶ A[E]`.

```lean
public theorem exists_homotopyInverse_whiskered_standardResolution {A : Type u} [CommRing A]
    (X : SimplicialObject.Augmented (AlgCat.{u} A ⥤ AlgCat.{u} A))
    (h : ∀ n : ℕ, X.left.obj (op ⦋n⦌) =
      (AlgCat.adj A).toComonad.toFunctor.iterate (n + 1))
    (hX : X.right = 𝟭 (AlgCat.{u} A))
    (hδ : ∀ (n : ℕ) (j : Fin (n + 2)), X.left.δ j =
      eqToHom (h (n + 1)) ≫ Godement.face (AlgCat.adj A).toComonad.ε (n + 1) j ≫
        eqToHom (h n).symm)
    (hσ : ∀ (n : ℕ) (j : Fin (n + 1)), X.left.σ j =
      eqToHom (h n) ≫ Godement.degeneracy (AlgCat.adj A).toComonad.δ n j ≫
        eqToHom (h (n + 1)).symm)
    (hε : X.hom.app (op ⦋0⦌) =
      eqToHom (h 0) ≫ Godement.face (AlgCat.adj A).toComonad.ε 0 0 ≫ eqToHom hX.symm)
    (a : X.left ⋙ (Functor.whiskeringRight (AlgCat.{u} A) (AlgCat.{u} A) (Type u)).obj
        (forget (AlgCat.{u} A)) ⟶
      (Functor.const SimplexCategoryᵒᵖ).obj (X.right ⋙ forget (AlgCat.{u} A)))
    (ha : ∀ n : SimplexCategoryᵒᵖ,
      a.app n = Functor.whiskerRight (X.hom.app n) (forget (AlgCat.{u} A)))
    (b : X.left ⋙ (Functor.whiskeringLeft (Type u) (AlgCat.{u} A) (AlgCat.{u} A)).obj
        (AlgCat.free A) ⟶
      (Functor.const SimplexCategoryᵒᵖ).obj (AlgCat.free A ⋙ X.right))
    (hb : ∀ n : SimplexCategoryᵒᵖ,
      b.app n = Functor.whiskerLeft (AlgCat.free A) (X.hom.app n))
    (ρ : ∀ n : ℕ, forget (AlgCat.{u} A) ⟶
      (AlgCat.adj A).toComonad.toFunctor.iterate (n + 1) ⋙ forget (AlgCat.{u} A))
    (hρ₀ : ∀ (B : AlgCat.{u} A) (x : B), (ρ 0).app B x = comonadι B x)
    (hρ : ∀ (n : ℕ) (B : AlgCat.{u} A) (x : B),
      (ρ (n + 1)).app B x = comonadι _ ((ρ n).app B x))
    (τ : ∀ n : ℕ, AlgCat.free A ⟶
      AlgCat.free A ⋙ (AlgCat.adj A).toComonad.toFunctor.iterate (n + 1))
    (hτ₀ : ∀ (E : Type u) (e : E), ((τ 0).app E).hom (freeι E e) = comonadι _ (freeι E e))
    (hτ : ∀ (n : ℕ) (E : Type u) (e : E), ((τ (n + 1)).app E).hom (freeι E e) =
      comonadι _ (((τ n).app E).hom (freeι E e))) :
    (∃ r : (Functor.const SimplexCategoryᵒᵖ).obj (X.right ⋙ forget (AlgCat.{u} A)) ⟶
        X.left ⋙ (Functor.whiskeringRight (AlgCat.{u} A) (AlgCat.{u} A) (Type u)).obj
          (forget (AlgCat.{u} A)),
      (∀ n : ℕ, r.app (op ⦋n⦌) =
        eqToHom (congrArg (fun F => F ⋙ forget (AlgCat.{u} A)) hX) ≫ ρ n ≫
          eqToHom (congrArg (fun F => F ⋙ forget (AlgCat.{u} A)) (h n)).symm) ∧
      Relation.EqvGen (fun f g => Nonempty (SimplicialObject.Homotopy f g)) (a ≫ r) (𝟙 _) ∧
      Relation.EqvGen (fun f g => Nonempty (SimplicialObject.Homotopy f g)) (r ≫ a) (𝟙 _)) ∧
    (∃ r : (Functor.const SimplexCategoryᵒᵖ).obj (AlgCat.free A ⋙ X.right) ⟶
        X.left ⋙ (Functor.whiskeringLeft (Type u) (AlgCat.{u} A) (AlgCat.{u} A)).obj
          (AlgCat.free A),
      (∀ n : ℕ, r.app (op ⦋n⦌) =
        eqToHom (congrArg (fun F => AlgCat.free A ⋙ F) hX) ≫ τ n ≫
          eqToHom (congrArg (fun F => AlgCat.free A ⋙ F) (h n)).symm) ∧
      Relation.EqvGen (fun f g => Nonempty (SimplicialObject.Homotopy f g)) (b ≫ r) (𝟙 _) ∧
      Relation.EqvGen (fun f g => Nonempty (SimplicialObject.Homotopy f g)) (r ≫ b) (𝟙 _))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 14.34, Tag 08N8](https://stacks.math.columbia.edu/tag/08N8)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
