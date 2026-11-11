---
declaration: section
origin: cited
lean: homComplexHomologyAddEquiv, Stacks.HomComplex.Currying.curryIso, Stacks.HomComplex.Currying.curryIso_hom_apply, Stacks.HomComplex.Currying.curryIso_naturality_left, Stacks.HomComplex.Currying.curryIso_naturality_middle, Stacks.HomComplex.Currying.curryIso_naturality_right, StacksDraft.TensorHomEquiv.tensorHomEquiv, StacksDraft.TensorHomEquiv.tensorHomEquiv_apply
statement: formalized
proof: formalized
---

# 15.73 Hom complexes

Section 15.73 of the Stacks Project, [Tag 0A8H](https://stacks.math.columbia.edu/tag/0A8H). 11 tags here are carried by 28 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0A5X, an equation

[Tag 0A5X](https://stacks.math.columbia.edu/tag/0A5X) in the Stacks Project.

**`homComplexHomologyAddEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/RHom.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/HomComplex/RHom.lean#L109).

> **Stacks 0A5X**.
> The canonical identification `Hⁿ(Hom^•(L, M)) ≃+ Hom_{K(C)}(L, M⟦n⟧)` of the degree-`n`
> cohomology of the Hom complex with morphisms in the homotopy category.

```lean
noncomputable def homComplexHomologyAddEquiv
    {C : Type u} [Category.{v} C] [Preadditive C] (L M : CochainComplex C ℤ) (n : ℤ) :
    (L.HomComplex M).homology n ≃+
      ((HomotopyCategory.quotient C (ComplexShape.up ℤ)).obj L ⟶
        (HomotopyCategory.quotient C (ComplexShape.up ℤ)).obj (M⟦n⟧))
```

## Tag 0A5Y, a lemma

[Tag 0A5Y](https://stacks.math.columbia.edu/tag/0A5Y) in the Stacks Project.

**`Stacks.HomComplex.Currying.curryIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/Currying.lean, line 327](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/HomComplex/Currying.lean#L327).

> **Stacks 0A5Y**.
> The canonical tensor–Hom currying isomorphism of complexes of `R`-modules
> `Hom^•(K, Hom^•(L, M)) ≅ Hom^•(Tot(K ⊗_R L), M)`, given in each degree by transposing a
> degreewise linear map.

```lean
noncomputable def curryIso (K L M : CochainComplex (ModuleCat.{u} R) ℤ) :
    HomComplexR R K (HomComplexR R L M) ≅ HomComplexR R (K ⊗ L) M
```

**`Stacks.HomComplex.Currying.curryIso_hom_apply`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/Currying.lean, line 342](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/HomComplex/Currying.lean#L342).

> **Stacks 0A5Y**.
> The currying isomorphism sends a cochain `α` to the cochain whose value on the summand
> `K^r ⊗ L^s` of `Tot^t(K ⊗ L)` is `x ⊗ y ↦ α^r(x)(y)`. This determines it in every degree and on
> every summand.

```lean
lemma curryIso_hom_apply (K L M : CochainComplex (ModuleCat.{u} R) ℤ) (n r s t p : ℤ)
    (hrs : r + s = t) (htp : t + n = p)
    (α : Cochain K (HomComplexR R L M) n) (x : K.X r) (y : L.X s) :
    ((((curryIso K L M).hom.f n).hom α).v t p htp).hom
        ((ιTensorObj K L r s t hrs).hom (x ⊗ₜ[R] y)) =
      (((α.v r (r + n) (by omega)).hom x).v s p (by omega)).hom y
```

**`Stacks.HomComplex.Currying.curryIso_naturality_left`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/Currying.lean, line 413](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/HomComplex/Currying.lean#L413).

> **Stacks 0A5Y**.
> Currying is contravariantly natural in the first complex: precomposing with `f : K' ⟶ K` inside
> the iterated Hom complex corresponds to precomposing with `f ▷ L` on the total complex.

```lean
lemma curryIso_naturality_left {K K' L M : CochainComplex (ModuleCat.{u} R) ℤ} (f : K' ⟶ K) :
    Stacks.HomComplex.TensorHomMap.precomp R K' K (HomComplexR R L M) f ≫ (curryIso K' L M).hom =
      (curryIso K L M).hom ≫ Stacks.HomComplex.TensorHomMap.precomp R (K' ⊗ L) (K ⊗ L) M (f ▷ L)
```

**`Stacks.HomComplex.Currying.curryIso_naturality_middle`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/Currying.lean, line 435](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/HomComplex/Currying.lean#L435).

> **Stacks 0A5Y**.
> Currying is contravariantly natural in the middle complex: precomposing the inner Hom complex
> with `f : L' ⟶ L` corresponds to precomposing with `K ◁ f` on the total complex.

```lean
lemma curryIso_naturality_middle {K L L' M : CochainComplex (ModuleCat.{u} R) ℤ} (f : L' ⟶ L) :
    Stacks.HomComplex.TensorHomMap.postcomp R K (HomComplexR R L M) (HomComplexR R L' M)
        (Stacks.HomComplex.TensorHomMap.precomp R L' L M f) ≫ (curryIso K L' M).hom =
      (curryIso K L M).hom ≫ Stacks.HomComplex.TensorHomMap.precomp R (K ⊗ L') (K ⊗ L) M (K ◁ f)
```

**`Stacks.HomComplex.Currying.curryIso_naturality_right`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/Currying.lean, line 460](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/HomComplex/Currying.lean#L460).

> **Stacks 0A5Y**.
> Currying is covariantly natural in the target complex.

```lean
lemma curryIso_naturality_right {K L M M' : CochainComplex (ModuleCat.{u} R) ℤ} (f : M ⟶ M') :
    Stacks.HomComplex.TensorHomMap.postcomp R K (HomComplexR R L M) (HomComplexR R L M')
        (Stacks.HomComplex.TensorHomMap.postcomp R L M M' f) ≫ (curryIso K L M').hom =
      (curryIso K L M).hom ≫ Stacks.HomComplex.TensorHomMap.postcomp R (K ⊗ L) M M' f
```

## Tag 0A5Z, an equation

[Tag 0A5Z](https://stacks.math.columbia.edu/tag/0A5Z) in the Stacks Project.

**`StacksDraft.TensorHomEquiv.tensorHomEquiv`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/TensorHomEquiv.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/TensorHomEquiv.lean#L57).

> **Stacks 0A5Z.** Linear maps into a module of linear maps are canonically equivalent to
> linear maps out of the corresponding tensor product: `Hom_R(K, Hom_R(L, M))` is identified with
> `Hom_R(K ⊗_R L, M)` by sending `f` to the map determined by `x ⊗ y ↦ f(x)(y)`.

```lean
alias tensorHomEquiv
```

**`StacksDraft.TensorHomEquiv.tensorHomEquiv`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/TensorHomEquiv.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/TensorHomEquiv.lean#L57).

> **Stacks 0A5Z.** Linear maps into a module of linear maps are canonically equivalent to
> linear maps out of the corresponding tensor product: `Hom_R(K, Hom_R(L, M))` is identified with
> `Hom_R(K ⊗_R L, M)` by sending `f` to the map determined by `x ⊗ y ↦ f(x)(y)`.

```lean
alias tensorHomEquiv
```

**`StacksDraft.TensorHomEquiv.tensorHomEquiv_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/TensorHomEquiv.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/TensorHomEquiv.lean#L62).

> **Stacks 0A5Z.** The tensor–Hom equivalence sends `f : K →ₗ[R] L →ₗ[R] M` to the linear map
> taking the pure tensor `x ⊗ y` to `f x y`.

```lean
theorem tensorHomEquiv_apply {R : Type*} [CommRing R] (K L M : Type*)
    [AddCommGroup K] [AddCommGroup L] [AddCommGroup M]
    [Module R K] [Module R L] [Module R M]
    (f : K →ₗ[R] L →ₗ[R] M) (x : K) (y : L) :
    tensorHomEquiv (RingHom.id R) K L M f (x ⊗ₜ[R] y) = f x y
```

**`StacksDraft.TensorHomEquiv.tensorHomEquiv_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/TensorHomEquiv.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/TensorHomEquiv.lean#L62).

> **Stacks 0A5Z.** The tensor–Hom equivalence sends `f : K →ₗ[R] L →ₗ[R] M` to the linear map
> taking the pure tensor `x ⊗ y` to `f x y`.

```lean
theorem tensorHomEquiv_apply {R : Type*} [CommRing R] (K L M : Type*)
    [AddCommGroup K] [AddCommGroup L] [AddCommGroup M]
    [Module R K] [Module R L] [Module R M]
    (f : K →ₗ[R] L →ₗ[R] M) (x : K) (y : L) :
    tensorHomEquiv (RingHom.id R) K L M f (x ⊗ₜ[R] y) = f x y
```

**`StacksDraft.TensorHomEquiv.tensorHomEquiv_symm_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/TensorHomEquiv.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/TensorHomEquiv.lean#L72).

> **Stacks 0A5Z.** The inverse of the tensor–Hom equivalence sends `g : K ⊗[R] L →ₗ[R] M` to
> the map `x ↦ y ↦ g (x ⊗ y)`.

```lean
theorem tensorHomEquiv_symm_apply {R : Type*} [CommRing R] (K L M : Type*)
    [AddCommGroup K] [AddCommGroup L] [AddCommGroup M]
    [Module R K] [Module R L] [Module R M]
    (g : K ⊗[R] L →ₗ[R] M) (x : K) (y : L) :
    ((tensorHomEquiv (RingHom.id R) K L M).symm g) x y = g (x ⊗ₜ[R] y)
```

**`StacksDraft.TensorHomEquiv.tensorHomEquiv_symm_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/TensorHomEquiv.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/TensorHomEquiv.lean#L72).

> **Stacks 0A5Z.** The inverse of the tensor–Hom equivalence sends `g : K ⊗[R] L →ₗ[R] M` to
> the map `x ↦ y ↦ g (x ⊗ y)`.

```lean
theorem tensorHomEquiv_symm_apply {R : Type*} [CommRing R] (K L M : Type*)
    [AddCommGroup K] [AddCommGroup L] [AddCommGroup M]
    [Module R K] [Module R L] [Module R M]
    (g : K ⊗[R] L →ₗ[R] M) (x : K) (y : L) :
    ((tensorHomEquiv (RingHom.id R) K L M).symm g) x y = g (x ⊗ₜ[R] y)
```

## Tag 0GWQ, a remark

[Tag 0GWQ](https://stacks.math.columbia.edu/tag/0GWQ) in the Stacks Project.

**`Stacks.HomComplex.MonoidalClosed.cochainComplex_symmetricMonoidalClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/Currying.lean, line 688](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/HomComplex/Currying.lean#L688).

> **Stacks 0GWQ**.
> Cochain complexes of modules over a commutative ring form a symmetric monoidal closed category.
> The concrete Hom complexes, with pre- and postcomposition on morphisms, form a bifunctor
> naturally isomorphic to the internal Hom bifunctor. Under this isomorphism, the closed-structure
> adjunction, after applying the symmetry `K ⊗ L ≅ L ⊗ K`, is the canonical currying isomorphism of
> Hom complexes. Moreover, a degree-zero cochain is the cochain of a unique morphism of complexes
> if and only if its differential vanishes.

```lean
theorem cochainComplex_symmetricMonoidalClosed (R : Type u) [CommRing R] :
    ∃ (s : SymmetricCategory (CochainComplex (ModuleCat.{u} R) ℤ)),
      letI := s
      ∃ (closed : MonoidalClosed (CochainComplex (ModuleCat.{u} R) ℤ)),
        letI := closed
        ∃ (H : (CochainComplex (ModuleCat.{u} R) ℤ)ᵒᵖ ⥤
            CochainComplex (ModuleCat.{u} R) ℤ ⥤ CochainComplex (ModuleCat.{u} R) ℤ)
          (hObj : ∀ (L M : CochainComplex (ModuleCat.{u} R) ℤ),
            (H.obj (Opposite.op L)).obj M = HomComplexR R L M),
          (∀ (L M N : CochainComplex (ModuleCat.{u} R) ℤ) (f : M ⟶ N),
            (H.obj (Opposite.op L)).map f =
              eqToHom (hObj L M) ≫ Stacks.HomComplex.TensorHomMap.postcomp R L M N f ≫ eqToHom (hObj
                L N).symm) ∧
          (∀ (K L M : CochainComplex (ModuleCat.{u} R) ℤ) (f : K ⟶ L),
            (H.map f.op).app M =
              eqToHom (hObj L M) ≫ Stacks.HomComplex.TensorHomMap.precomp R K L M f ≫ eqToHom (hObj
                K M).symm) ∧
          ∃ e : MonoidalClosed.internalHom ≅ H,
            (∀ (L M : CochainComplex (ModuleCat.{u} R) ℤ) (f : Cochain L M 0),
                (∃! φ : L ⟶ M, Cochain.ofHom φ = f) ↔ δ 0 1 f = 0) ∧
            ∀ (K L M : CochainComplex (ModuleCat.{u} R) ℤ)
                (φ : K ⟶ HomComplexR R L M),
              Cochain.ofHom
                  ((s.toBraidedCategory.braiding K L).hom ≫
                    MonoidalClosed.uncurry
                      (φ ≫ eqToHom (hObj L M).symm ≫ (e.app (Opposite.op L)).inv.app M)) =
                (Stacks.HomComplex.Currying.curryIso K L M).hom.f 0 (Cochain.ofHom φ)
```

## Tag 0A8I, a lemma

[Tag 0A8I](https://stacks.math.columbia.edu/tag/0A8I) in the Stacks Project.

**`composition_morphism_exists`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/Composition.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/HomComplex/Composition.lean#L144). References: SGA 4 XVII (1.1.10), “(iii), special case”.

> There is a morphism of complexes of `R`-modules
> `c : tensorObj (HomComplexR R L M) (HomComplexR R K L) ⟶ HomComplexR R K M` such that for
> `β : Cochain L M p` and `γ : Cochain K L q` with `p + q = n`, the `(p, q)`-component of `c` sends
> `β ⊗ₜ γ` to the composite cochain `γ.comp β`.

```lean
theorem composition_morphism_exists :
    ∃ c : HomologicalComplex.tensorObj (HomComplexR R L M) (HomComplexR R K L) ⟶ HomComplexR R K M,
      ∀ (p q n : ℤ) (h : p + q = n) (β : Cochain L M p) (γ : Cochain K L q),
        (HomologicalComplex.ιTensorObj (HomComplexR R L M) (HomComplexR R K L) p q n h ≫ c.f n).hom
            (β ⊗ₜ[R] γ)
          = γ.comp β (by rw [add_comm]; exact h)
```

## Tag 0BYM, a lemma

[Tag 0BYM](https://stacks.math.columbia.edu/tag/0BYM) in the Stacks Project.

**`Stacks.HomComplex.TensorHomComparison.theta`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/TensorHom.lean, line 431](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/HomComplex/TensorHom.lean#L431).

> **Stacks 0BYM**.
> The canonical morphism of complexes `Θ : Tot(K ⊗_R Hom^•(M, L)) ⟶ Hom^•(M, Tot(K ⊗_R L))`,
> given in degree `n` by `thetaDeg`.

```lean
noncomputable def theta (K L M : CochainComplex (ModuleCat R) ℤ) :
    (K ⊗ HomComplexR R M L) ⟶ HomComplexR R M (K ⊗ L)
```

**`Stacks.HomComplex.TensorHomComparison.theta_natural_K`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/TensorHom.lean, line 465](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/HomComplex/TensorHom.lean#L465).

> **Stacks 0BYM** (naturality in `K`).
> For `fK : K ⟶ K'`, `Θ ≫ Hom^•(id_M, fK ▷ L) = (fK ▷ Hom^•(M, L)) ≫ Θ`.

```lean
theorem theta_natural_K (K K' L M : CochainComplex (ModuleCat R) ℤ) (fK : K ⟶ K') :
    theta K L M ≫ HomCxMap M M (K ⊗ L) (K' ⊗ L) (𝟙 M) (fK ▷ L)
      = (fK ▷ HomComplexR R M L) ≫ theta K' L M
```

**`Stacks.HomComplex.TensorHomComparison.theta_natural_L`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/TensorHom.lean, line 496](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/HomComplex/TensorHom.lean#L496).

> **Stacks 0BYM** (naturality in `L`).
> For `gL : L ⟶ L'`, `Θ ≫ Hom^•(id_M, K ◁ gL) = (K ◁ Hom^•(id_M, gL)) ≫ Θ`.

```lean
theorem theta_natural_L (K L L' M : CochainComplex (ModuleCat R) ℤ) (gL : L ⟶ L') :
    theta K L M ≫ HomCxMap M M (K ⊗ L) (K ⊗ L') (𝟙 M) (K ◁ gL)
      = (K ◁ HomCxMap M M L L' (𝟙 M) gL) ≫ theta K L' M
```

**`Stacks.HomComplex.TensorHomComparison.theta_natural_M`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/TensorHom.lean, line 528](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/HomComplex/TensorHom.lean#L528).

> **Stacks 0BYM** (naturality in `M`).
> For `hM : M' ⟶ M`, `Θ ≫ Hom^•(hM, id_{K ⊗ L}) = (K ◁ Hom^•(hM, id_L)) ≫ Θ`.

```lean
theorem theta_natural_M (K L M M' : CochainComplex (ModuleCat R) ℤ) (hM : M' ⟶ M) :
    theta K L M ≫ HomCxMap M M' (K ⊗ L) (K ⊗ L) hM (𝟙 (K ⊗ L))
      = (K ◁ HomCxMap M M' L L hM (𝟙 L)) ≫ theta K L M'
```

## Tag 0A62, a lemma

[Tag 0A62](https://stacks.math.columbia.edu/tag/0A62) in the Stacks Project.

**`Stacks.HomComplex.TensorHomMap.Phi`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/Basic.lean, line 301](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/HomComplex/Basic.lean#L301).

> **Stacks 0A62**.
> The morphism of complexes of `R`-modules `Φ_{K,L} : K ⟶ Hom^•(L, Tot(K ⊗_R L))` whose degree-`n`
> component sends `β ∈ K^n` to the cochain `y ↦ β ⊗ y`.

```lean
noncomputable def Phi (K L : CochainComplex (ModuleCat R) ℤ) :
    K ⟶ CochainComplex.HomComplexR R L (K ⊗ L)
```

**`Stacks.HomComplex.TensorHomMap.Phi_natural_mixed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/Basic.lean, line 316](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/HomComplex/Basic.lean#L316).

> **Stacks 0A62**.
> For `f : K ⟶ K'` and `g : L ⟶ L'`, postcomposing `Φ_{K,L}` with `Tot(f ⊗ g) = f ⊗ₘ g` equals
> `f ≫ Φ_{K',L'}` followed by precomposition with `g`; both send `β` and `y` to `f(β) ⊗ g(y)`.

```lean
theorem Phi_natural_mixed (K K' L L' : CochainComplex (ModuleCat R) ℤ) (f : K ⟶ K') (g : L ⟶ L') :
    Phi R K L ≫ postcomp R L (K ⊗ L) (K' ⊗ L') (f ⊗ₘ g) =
      f ≫ Phi R K' L' ≫ precomp R L L' (K' ⊗ L') g
```

## Tag 0A60, a lemma

[Tag 0A60](https://stacks.math.columbia.edu/tag/0A60) in the Stacks Project.

**`ChainEvaluation.chainEvaluation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/Evaluation.lean, line 454](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/HomComplex/Evaluation.lean#L454).

> **Stacks 0A60**.
> The canonical morphism of complexes `Tot(Hom^•(J, I) ⊗ K) ⟶ Hom^•(Hom^•(K, J), I)`. On
> homogeneous elements it sends `f ⊗ k` to the map `g ↦ f (g k)`, with the Koszul signs of the
> total and Hom complexes.

```lean
noncomputable def chainEvaluation
    (K J I : CochainComplex (ModuleCat R) ℤ) :
    (HomComplexR R J I ⊗ K) ⟶ HomComplexR R (HomComplexR R K J) I
```

**`ChainEvaluation.chainEvaluation_natural_K`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/Evaluation.lean, line 481](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/HomComplex/Evaluation.lean#L481).

> **Stacks 0A60**.
> Evaluation is natural in the complex `K` being evaluated at: tensoring with `f : K ⟶ K'` and
> then evaluating is evaluating and then precomposing the outer Hom complex with `f^* :
> Hom^•(K', J) ⟶ Hom^•(K, J)`.

```lean
theorem chainEvaluation_natural_K
    (K K' J I : CochainComplex (ModuleCat.{u} R) ℤ) (f : K ⟶ K') :
    (HomComplexR R J I ◁ f) ≫ chainEvaluation K' J I =
      chainEvaluation K J I ≫ Stacks.HomComplex.TensorHomMap.precomp R (HomComplexR R K' J)
        (HomComplexR R K J) I (Stacks.HomComplex.TensorHomMap.precomp R K K' J f)
```

**`ChainEvaluation.chainEvaluation_natural_J`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/Evaluation.lean, line 548](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/HomComplex/Evaluation.lean#L548).

> **Stacks 0A60**.
> Evaluation is natural in the middle complex `J`: precomposing the inner Hom complex with
> `f : J ⟶ J'` on the source corresponds to postcomposing `Hom^•(K, J) ⟶ Hom^•(K, J')` on the
> target.

```lean
theorem chainEvaluation_natural_J
    (K J J' I : CochainComplex (ModuleCat.{u} R) ℤ) (f : J ⟶ J') :
    (Stacks.HomComplex.TensorHomMap.precomp R J J' I f ▷ K) ≫ chainEvaluation K J I =
      chainEvaluation K J' I ≫ Stacks.HomComplex.TensorHomMap.precomp R (HomComplexR R K J)
        (HomComplexR R K J') I (Stacks.HomComplex.TensorHomMap.postcomp R K J J' f)
```

**`ChainEvaluation.chainEvaluation_natural_I`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/Evaluation.lean, line 624](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/HomComplex/Evaluation.lean#L624).

> **Stacks 0A60**.
> Evaluation is natural in the target complex `I`: postcomposing with `f : I ⟶ I'` commutes with
> evaluation.

```lean
theorem chainEvaluation_natural_I
    (K J I I' : CochainComplex (ModuleCat.{u} R) ℤ) (f : I ⟶ I') :
    (Stacks.HomComplex.TensorHomMap.postcomp R J I I' f ▷ K) ≫ chainEvaluation K J I' =
      chainEvaluation K J I ≫ Stacks.HomComplex.TensorHomMap.postcomp R (HomComplexR R K J) I I' f
```

**`ChainEvaluation.chainEvaluation_tmul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/Evaluation.lean, line 799](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/HomComplex/Evaluation.lean#L799).

> **Stacks 0A60**.
> The homogeneous formula for `chainEvaluation`: the image of `φ ⊗ k` sends a cochain `ψ`
> to `φ (ψ k)`, up to the Koszul sign `(-1)^(s + (-a) s)` of evaluation.

```lean
theorem chainEvaluation_tmul
    (K J I : CochainComplex (ModuleCat.{u} R) ℤ)
    (t s n q p a : ℤ) (hn : t + s = n) (hq : q + n = p)
    (ha : s + q = a) (hp : a + t = p)
    (φ : Cochain J I t) (k : K.X s) (ψ : Cochain K J q) :
    ((((chainEvaluation K J I).f n).hom
      ((ιTensorObj (HomComplexR R J I) K t s n hn).hom (φ ⊗ₜ[R] k))).v
        q p hq).hom ψ =
      (s + (-a) * s).negOnePow •
        (φ.v a p hp).hom ((ψ.v s a ha).hom k)
```

## Tag 0FNE, an equation

[Tag 0FNE](https://stacks.math.columbia.edu/tag/0FNE) in the Stacks Project.

**`CochainComplex.HomComplex.iteratedHomComplex_differential_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/Differentials.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/HomComplex/Differentials.lean#L87).

> **Stacks 0FNE.** The differential of a degree-`n` cochain in `Hom^•(Hom^•(K, L), M)`,
> evaluated on `f ∈ Hom^{-s-1}(K, L)`, is the sum of the target, middle and source differential
> terms, with respective signs `1`, `-(-1)^n` and `(-1)^(p+1)`.

```lean
theorem iteratedHomComplex_differential_apply
    {R : Type u} [CommRing R]
    (K L M : CochainComplex (ModuleCat.{v} R) ℤ)
    (n p s : ℤ) (hps : p + s = n)
    (β : Cochain (HomComplexR R K L) M n)
    (f : Cochain K L (-s - 1)) :
    ((δ n (n + 1) β).v (-s - 1) p (by omega)).hom f =
      (M.d (p - 1) p).hom ((β.v (-s - 1) (p - 1) (by omega)).hom f) -
        n.negOnePow •
          ((β.v (-s) p (by omega)).hom
            (f.comp (Cochain.diff L) (by omega))) +
        (p + 1).negOnePow •
          ((β.v (-s) p (by omega)).hom
            ((Cochain.diff K).comp f (by omega)))
```

## Tag 0FNF, an equation

[Tag 0FNF](https://stacks.math.columbia.edu/tag/0FNF) in the Stacks Project.

**`CochainComplex.HomComplex.tensorHomComplex_differential_component`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/Differentials.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/HomComplex/Differentials.lean#L221).

> **Stacks 0FNF.** On the `(p, q, r)`-component of `Tot(Hom^•(L, M) ⊗ K)`, the total
> differential is the Hom-complex differential plus `(-1)^(p+q)` times the differential of `K`;
> the Hom-complex differential itself is postcomposition by `d_M` minus `(-1)^(p+q)` times
> precomposition by `d_L`. Thus the total differential is the three-term expression
> `d_M - (-1)^(p+q) d_L + (-1)^(p+q) d_K`.

```lean
theorem tensorHomComplex_differential_component
    (L M K : CochainComplex (ModuleCat R) ℤ) (p q r : ℤ) :
    let H := HomComplexR R L M
    let T := HomologicalComplex.tensorObj H K
    ((homComponent R L M p q ▷ K.X r) ≫
          HomologicalComplex.ιTensorObj H K (p + q) r (p + q + r) rfl ≫
          T.d (p + q + r) (p + q + r + 1) =
        (postcomposeDifferential R L M p q ▷ K.X r) ≫
            (homComponent R L M (p + 1) q ▷ K.X r) ≫
            HomologicalComplex.ιTensorObj H K (p + 1 + q) r
              (p + q + r + 1) (by omega) +
          -(p + q).negOnePow •
            ((precomposeDifferential R L M p q ▷ K.X r) ≫
              (homComponent R L M p (q + 1) ▷ K.X r) ≫
              HomologicalComplex.ιTensorObj H K (p + (q + 1)) r
                (p + q + r + 1) (by omega)) +
          (p + q).negOnePow •
            ((homComponent R L M p q ⊗ₘ K.d r (r + 1)) ≫
              HomologicalComplex.ιTensorObj H K (p + q) (r + 1)
                (p + q + r + 1) (by omega)))
```

## Tag 0A61, a remark

[Tag 0A61](https://stacks.math.columbia.edu/tag/0A61) in the Stacks Project.

**`ChainEvaluation.homComplex_braiding_sign_eq_evaluation_sign`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/Evaluation.lean, line 1053](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/HomComplex/Evaluation.lean#L1053).

> **Stacks 0A61**.
> For any Koszul symmetric structure on cochain complexes — one whose braiding restricts on the
> summand `A^p ⊗ B^q` to `(-1)^{pq}` times the symmetry of `ModuleCat R` — the braiding on the
> summand `K^r ⊗ Hom^{a-r}(K, J)` carries the sign `(-1)^{r + (-a) r}` that occurs in the direct
> construction of evaluation into an iterated Hom complex (`chainEvaluation_tmul`). So the
> monoidal construction of the map of Stacks 0A60 and the direct one use the same sign.

```lean
theorem homComplex_braiding_sign_eq_evaluation_sign
    (s : SymmetricCategory (CochainComplex (ModuleCat.{u} R) ℤ))
    (hKoszul : ∀ (A B : CochainComplex (ModuleCat.{u} R) ℤ) (p q n : ℤ) (h : p + q = n),
      ιTensorObj A B p q n h ≫ (s.toBraidedCategory.braiding A B).hom.f n =
        ((p * q).negOnePow : ℤˣ) •
          ((β_ (A.X p) (B.X q)).hom ≫
            ιTensorObj B A q p n (by simpa [add_comm] using h)))
    (K J : CochainComplex (ModuleCat.{u} R) ℤ) (a r : ℤ) :
    ιTensorObj K (HomComplexR R K J) r (a - r) a (by omega) ≫
        (s.toBraidedCategory.braiding K (HomComplexR R K J)).hom.f a =
      ((r + (-a) * r).negOnePow : ℤˣ) •
        ((β_ (K.X r) ((HomComplexR R K J).X (a - r))).hom ≫
          ιTensorObj (HomComplexR R K J) K (a - r) r a (by omega))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.73, Tag 0A8H](https://stacks.math.columbia.edu/tag/0A8H)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
