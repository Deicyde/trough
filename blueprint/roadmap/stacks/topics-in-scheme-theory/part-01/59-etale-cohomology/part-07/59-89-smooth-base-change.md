---
declaration: section
origin: cited
lean: Stacks.EtaleCohomology.exists_galoisCover_killing_class, Stacks.EtaleCohomology.SmoothBaseChange.isIso_higherBaseChangeMapAb_app_of_smooth, Stacks.EtaleCohomology.isIso_smallEtaleDerivedBaseChangeAb_app_of_smoothLimit
statement: formalized
proof: formalized
---

# 59.89 Smooth base change

Section 59.89 of the Stacks Project, [Tag 0EYQ](https://stacks.math.columbia.edu/tag/0EYQ). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EYT, a lemma

[Tag 0EYT](https://stacks.math.columbia.edu/tag/0EYT) in the Stacks Project.

**`Stacks.EtaleCohomology.exists_galoisCover_killing_class`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmoothBaseChange/CurveClassKilling.lean, line 366](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmoothBaseChange/CurveClassKilling.lean#L366).

> **Stacks Project, Tag 0EYT.** Let `K/k` be a field extension, `X` a smooth affine curve over
> `k` with a rational point `x`, `F` an abelian sheaf on `Spec(K)_étale` annihilated by an integer
> `n` invertible in `k`, `q > 0` and `ξ ∈ H^q(X_K, F)`. There are finite extensions `K'/K` and
> `k'/k` with `k' ⊆ K'` and a finite étale Galois cover `Z ⟶ X_{k'}`, whose group has order
> dividing a power of `n` and which is split over `x_{k'}`, such that `ξ` dies in
> `H^q(Z_{K'}, F)`.

```lean
theorem exists_galoisCover_killing_class [IsCurve k f] [Smooth f] [IsAffine X]
    (x : Spec (.of k) ⟶ X) (hx : x ≫ f = 𝟙 _)
    (F : Sheaf (Spec (.of K)).smallEtaleTopology AddCommGrpCat.{u + 1}) {n : ℕ}
    (hn : IsUnit (n : k)) (hF : n • 𝟙 F = 0) {q : ℕ} (hq : 0 < q)
    (ξ : Sheaf.H.{u + 1, u + 1}
      ((etaleAbelianInverseImage.{u, u + 1} (pullback.fst (spectrumMap k K) f)).obj F) q) :
    ∃ (k' K' : Type u) (_ : Field k') (_ : Field K') (_ : Algebra k k') (_ : Algebra K K')
      (_ : Algebra k' K') (_ : Algebra k K') (_ : IsScalarTower k k' K')
      (_ : IsScalarTower k K K') (_ : FiniteDimensional k k') (_ : FiniteDimensional K K')
      (Z : Scheme.{u}) (p : Z ⟶ pullback (spectrumMap k k') f),
      IsGaloisCover p ∧ (∃ m : ℕ, Nat.card (Aut (Over.mk p)) ∣ n ^ m) ∧
        IsSplitOver p (basePoint f k' x hx) ∧ coverBaseChangeClass f K k' K' p F q ξ = 0
```

## Tag 0EYU, a theorem

[Tag 0EYU](https://stacks.math.columbia.edu/tag/0EYU) in the Stacks Project.

**`Stacks.EtaleCohomology.SmoothBaseChange.isIso_higherBaseChangeMapAb_app_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmoothBaseChange/Unconditional.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmoothBaseChange/Unconditional.lean#L53).

> **The smooth base change theorem** ([Stacks, Theorem 0EYU]). In a cartesian square
> ```
> X  ←-h-  Y
> |f       |e
> S  ←-g-  T
> ```
> with `f` smooth and `g` quasi-compact and quasi-separated, the base change map
> `f⁻¹ R^q g_* F ⟶ R^q h_* e⁻¹ F` is an isomorphism for every `q` and every abelian sheaf `F` on
> `T_étale` all of whose stalks at geometric points are torsion of orders invertible on `S`: every
> element of every such stalk is killed by a positive integer `n` which is a unit on `S`.

```lean
theorem isIso_higherBaseChangeMapAb_app_of_smooth
    {X Y S T : Scheme.{u}} (f : X ⟶ S) (h : Y ⟶ X) (e : Y ⟶ T) (g : T ⟶ S)
    (sq : IsPullback h e f g) [Smooth f] [QuasiCompact g] [QuasiSeparated g]
    (F : Sheaf (smallEtaleTopology T) Ab.{u + 1})
    (hF : ∀ (t : GeometricPoint T) (a : (smallEtaleStalkAb t.hom).obj F),
      ∃ n : ℕ, 0 < n ∧ IsUnit ((n : ℤ) : Γ(S, ⊤)) ∧ n • a = 0) (q : ℕ) :
    IsIso ((higherBaseChangeMapAb f g h e sq.w q).app F)
```

## Tag 0F09, a lemma

[Tag 0F09](https://stacks.math.columbia.edu/tag/0F09) in the Stacks Project.

**`Stacks.EtaleCohomology.isIso_smallEtaleDerivedBaseChangeAb_app_of_smoothLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmoothBaseChange/SmoothLimitBaseChangeStalks.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmoothBaseChange/SmoothLimitBaseChangeStalks.lean#L114).

> **Smooth base change along a limit of smooth schemes** ([Stacks, Tag 0F09]). Let `S` be a
> scheme and let `S' = lim S_i` be a directed inverse limit of schemes `S_i` smooth over `S` with
> affine transition morphisms: an inverse system `D` over a directed nonempty preorder `I`, with
> structure morphisms `p_i : S_i ⟶ S` compatible with the transitions, a limit cone `c` with point
> `S'`, and `g : S' ⟶ S` the composite of each leg of `c` with `p_i`. Let `f : X ⟶ S` be
> quasi-compact and quasi-separated and let `X' = X ×_S S'` be a fibre product, with projections
> `f' : X' ⟶ S'` and `g' : X' ⟶ X`. Then for every `E ∈ D⁺(X_étale)` whose cohomology sheaves
> `H^q(E)` have stalks which are torsion of orders invertible on `S` (every element of the stalk at
> every geometric point is killed by a positive integer which is a unit on `S`), the base change map
> `g⁻¹ Rf_* E ⟶ Rf'_* (g')⁻¹ E` is an isomorphism.

```lean
theorem isIso_smallEtaleDerivedBaseChangeAb_app_of_smoothLimit
    {I : Type u} [Preorder I] [IsDirected I (· ≤ ·)] [Nonempty I] {S : Scheme.{u}}
    (D : Iᵒᵖ ⥤ Scheme.{u}) (p : D ⟶ (Functor.const Iᵒᵖ).obj S) (hp : ∀ i, Smooth (p.app i))
    (haff : ∀ ⦃i j : Iᵒᵖ⦄ (a : i ⟶ j), IsAffineHom (D.map a)) (c : Cone D) (hc : IsLimit c)
    (g : c.pt ⟶ S) (hg : ∀ i, c.π.app i ≫ p.app i = g) {X X' : Scheme.{u}} (f : X ⟶ S)
    [QuasiCompact f] [QuasiSeparated f] (f' : X' ⟶ c.pt) (g' : X' ⟶ X)
    (sq : IsPullback f' g' g f) (E : DerivedCategory.Plus (Sheaf (smallEtaleTopology X) Ab.{u + 1}))
    (hE : ∀ (q : ℤ) (t : GeometricPoint X)
      (a : ↑((smallEtaleStalkAb t.hom).obj
        ((DerivedCategory.Plus.homologyFunctor
          (Sheaf (smallEtaleTopology X) Ab.{u + 1}) q).obj E))),
      ∃ n : ℕ, 0 < n ∧ IsUnit ((n : ℤ) : Γ(S, ⊤)) ∧ n • a = 0) :
    IsIso ((smallEtaleDerivedBaseChangeAb g f f' g' sq.w).app E)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.89, Tag 0EYQ](https://stacks.math.columbia.edu/tag/0EYQ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
