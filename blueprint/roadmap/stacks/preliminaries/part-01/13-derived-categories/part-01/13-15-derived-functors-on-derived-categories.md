---
declaration: section
origin: cited
lean: StacksDerivedFunctorComparison.definedAtR_big_iff_plus, StacksDerivedFunctorComparison.valueR_big_iso_plus, StacksDerivedFunctorComparison.computesR_big_iff_plus, StacksDerivedFunctorComparison.definedAtL_big_iff_minus, StacksDerivedFunctorComparison.valueL_big_iso_minus, StacksDerivedFunctorComparison.computesL_big_iff_minus, CategoryTheory.Functor.rightAcyclic, CochainComplex.exists_quasiIso_prop
statement: formalized
proof: formalized
---

# 13.15 Derived functors on derived categories

Section 13.15 of the Stacks Project, [Tag 05T3](https://stacks.math.columbia.edu/tag/05T3). 6 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 05T5, a lemma

[Tag 05T5](https://stacks.math.columbia.edu/tag/05T5) in the Stacks Project.

**`StacksDerivedFunctorComparison.definedAtR_big_iff_plus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/BoundedDerivedFunctorComparison.lean, line 626](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/BoundedDerivedFunctorComparison.lean#L626). The attribute's comment: “(1)”. References: SGA 4 XVII (1.2.4), “Definedness clause”.

> **Statement (1), "defined at".** For `X` an object of `K⁺(A)`, the right derived functor of
> `F : K(A) ⥤ D(B)` is defined at `X` (viewed in `K(A)` via `ι`) if and only if the right derived
> functor of `F⁺ : K⁺(A) ⥤ D⁺(B)` is defined at `X`.

```lean
theorem definedAtR_big_iff_plus (X : HomotopyCategory.Plus A) :
    (∃ c, (Fbig F).IsRightDerivedValueAt (qisBig A) ((HomotopyCategory.Plus.ι A).obj X) c) ↔
      ∃ c, (Fplus F).IsRightDerivedValueAt (qisPlus A) X c
```

**`StacksDerivedFunctorComparison.valueR_big_iso_plus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/BoundedDerivedFunctorComparison.lean, line 662](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/BoundedDerivedFunctorComparison.lean#L662). The attribute's comment: “(1), values”. References: SGA 4 XVII (1.2.4), “Value clause”; SGA 4½ Etat 0 (4.2.3.2), “(A)”.

> **Statement (1), values.** When the right derived functors of `F : K(A) ⥤ D(B)` and of
> `F⁺ : K⁺(A) ⥤ D⁺(B)` are defined at `X`, with values `cbig.pt` and `cplus.pt`, the values are
> canonically isomorphic in `D(B)` via the embedding `D⁺(B) ↪ D(B)`: there is an isomorphism
> `RF(X) ≅ ι(RF⁺(X))` compatible with the structure maps `F(X') ⟶ RF(X)` and `F⁺(X') ⟶ RF⁺(X)` of
> every `s : X ⟶ X'` in `Qis⁺(A)`, in particular with the canonical maps at `𝟙 X`.

```lean
theorem valueR_big_iso_plus (X : HomotopyCategory.Plus A)
    {cbig : Cocone (MorphismProperty.Under.forget (qisBig A) ⊤ ((HomotopyCategory.Plus.ι A).obj X) ⋙
      Under.forget _ ⋙ Fbig F)}
    (hbig : (Fbig F).IsRightDerivedValueAt (qisBig A) ((HomotopyCategory.Plus.ι A).obj X) cbig)
    {cplus : Cocone (MorphismProperty.Under.forget (qisPlus A) ⊤ X ⋙ Under.forget X ⋙ Fplus F)}
    (hplus : (Fplus F).IsRightDerivedValueAt (qisPlus A) X cplus) :
    ∃ e : cbig.pt ≅ (Dplus.ι B).obj cplus.pt,
      ∀ s : (qisPlus A).Under ⊤ X,
        cbig.ι.app (MorphismProperty.Under.mk ⊤ ((HomotopyCategory.Plus.ι A).map s.hom) s.prop) ≫
          e.hom = (Dplus.ι B).map (cplus.ι.app s)
```

**`StacksDerivedFunctorComparison.computesR_big_iff_plus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/BoundedDerivedFunctorComparison.lean, line 685](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/BoundedDerivedFunctorComparison.lean#L685). The attribute's comment: “(2)”.

> **Statement (2).** For `X` an object of `K⁺(A)`, `X` computes the right derived functor of
> `F : K(A) ⥤ D(B)` (viewed in `K(A)`) if and only if `X` computes the right derived functor of
> `F⁺ : K⁺(A) ⥤ D⁺(B)`.

```lean
theorem computesR_big_iff_plus (X : HomotopyCategory.Plus A) :
    (Fbig F).ComputesRightDerived (qisBig A) ((HomotopyCategory.Plus.ι A).obj X) ↔
      (Fplus F).ComputesRightDerived (qisPlus A) X
```

**`StacksDerivedFunctorComparison.definedAtL_big_iff_minus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/BoundedDerivedFunctorComparison.lean, line 717](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/BoundedDerivedFunctorComparison.lean#L717). The attribute's comment: “(3)”. References: SGA 4 XVII (1.2.5), “(iv), single functor”.

> **Statement (3), "defined at".** For `X` an object of `K⁻(A)`, the left derived functor of
> `F : K(A) ⥤ D(B)` is defined at `X` (viewed in `K(A)` via `ι`) if and only if the left derived
> functor of `F⁻ : K⁻(A) ⥤ D⁻(B)` is defined at `X`.

```lean
theorem definedAtL_big_iff_minus (X : KMinus A) :
    (∃ c, (Fbig F).IsLeftDerivedValueAt (qisBig A) ((KMinus.ι A).obj X) c) ↔
      ∃ c, (Fminus F).IsLeftDerivedValueAt (qisMinus A) X c
```

**`StacksDerivedFunctorComparison.valueL_big_iso_minus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/BoundedDerivedFunctorComparison.lean, line 750](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/BoundedDerivedFunctorComparison.lean#L750). The attribute's comment: “(3), values”. References: SGA 4 XVII (1.2.5), “(iv)”; SGA 4½ Etat 0 (4.2.3.2), “(A)”.

> **Statement (3), values.** When the left derived functors of `F : K(A) ⥤ D(B)` and of
> `F⁻ : K⁻(A) ⥤ D⁻(B)` are defined at `X`, with values `cbig.pt` and `cminus.pt`, the values are
> canonically isomorphic in `D(B)` via the embedding `D⁻(B) ↪ D(B)`, compatibly with the structure
> maps `LF(X) ⟶ F(X')` and `LF⁻(X) ⟶ F⁻(X')` of every `s : X' ⟶ X` in `Qis⁻(A)`, in particular
> with the canonical maps at `𝟙 X`.

```lean
theorem valueL_big_iso_minus (X : KMinus A)
    {cbig : Cone (MorphismProperty.Over.forget (qisBig A) ⊤ ((KMinus.ι A).obj X) ⋙
      Over.forget _ ⋙ Fbig F)}
    (hbig : (Fbig F).IsLeftDerivedValueAt (qisBig A) ((KMinus.ι A).obj X) cbig)
    {cminus : Cone (MorphismProperty.Over.forget (qisMinus A) ⊤ X ⋙ Over.forget X ⋙ Fminus F)}
    (hminus : (Fminus F).IsLeftDerivedValueAt (qisMinus A) X cminus) :
    ∃ e : cbig.pt ≅ (Dminus.ι B).obj cminus.pt,
      ∀ s : (qisMinus A).Over ⊤ X,
        e.hom ≫ (Dminus.ι B).map (cminus.π.app s) =
          cbig.π.app (MorphismProperty.Over.mk ⊤ ((KMinus.ι A).map s.hom) s.prop)
```

**`StacksDerivedFunctorComparison.computesL_big_iff_minus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/BoundedDerivedFunctorComparison.lean, line 773](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/BoundedDerivedFunctorComparison.lean#L773). The attribute's comment: “(4)”. References: SGA 4 XVII (1.2.5), “(iv), single functor”.

> **Statement (4).** For `X` an object of `K⁻(A)`, `X` computes the left derived functor of
> `F : K(A) ⥤ D(B)` (viewed in `K(A)`) if and only if `X` computes the left derived functor of
> `F⁻ : K⁻(A) ⥤ D⁻(B)`.

```lean
theorem computesL_big_iff_minus (X : KMinus A) :
    (Fbig F).ComputesLeftDerived (qisBig A) ((KMinus.ι A).obj X) ↔
      (Fminus F).ComputesLeftDerived (qisMinus A) X
```

## Tag 0157, a definition

[Tag 0157](https://stacks.math.columbia.edu/tag/0157) in the Stacks Project.

**`CategoryTheory.Functor.rightAcyclic`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/AcyclicObjects.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/AcyclicObjects.lean#L94). The attribute's comment: “part (3); the `RF` of part (1) is `Functor.totalRightDerived`”. References: SGA 4 XVII (1.2.3), “(ii)”; SGA 4 XVII (1.2.3), “(ii)”; SGA 4 V (0.4).

> An object `A` of an abelian category `C` is **right acyclic** for an additive functor
> `F : C ⥤ D` to an abelian category, or **acyclic for `RF`**, if the complex `A[0]` with `A` in
> degree zero computes the right derived functor `RF` of `F : K⁺(C) ⥤ D⁺(D)`, that is, if the
> canonical map `α_{A[0]} : F(A[0]) ⟶ RF(Qh(A[0]))`, the unit of `RF` at `A[0]`, is an
> isomorphism.

```lean
public def rightAcyclic (F : C ⥤ D) [F.Additive]
    [(F.mapHomotopyCategoryPlus ⋙ DerivedCategory.Plus.Qh).HasRightDerivedFunctor
      (HomotopyCategory.Plus.quasiIso C)] : ObjectProperty C
```

## Tag 05T7, a lemma

[Tag 05T7](https://stacks.math.columbia.edu/tag/05T7) in the Stacks Project.

**`CochainComplex.exists_quasiIso_prop`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/DerivedFunctorsOnDerivedCategories.lean, line 769](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/DerivedFunctorsOnDerivedCategories.lean#L769).

> **Stacks 05T7.** Let `A` be an abelian category, let `P` be a class of
> objects of `A` containing a zero object and such that every object of `A` is a
> quotient of an object satisfying `P`, and let `a : ℤ`.
> (1) If `K.X n = 0` for `n > a`, there is a quasi-isomorphism `f : L ⟶ K` with
> all `f.f n` epimorphisms, all `L.X n` satisfying `P`, and `L.X n = 0` for
> `n > a`.
> (2) If `H ^ n (K) = 0` for `n > a`, there is a quasi-isomorphism `f : L ⟶ K`
> with all `L.X n` satisfying `P` and `L.X n = 0` for `n > a`.

```lean
public theorem exists_quasiIso_prop (P : ObjectProperty A)
    [P.ContainsZero] (hP : ∀ X : A, ∃ (Y : A) (_ : P Y) (p : Y ⟶ X), Epi p) (a : ℤ) :
    (∀ (K : CochainComplex A ℤ) [K.IsStrictlyLE a],
        ∃ (L : CochainComplex A ℤ) (f : L ⟶ K) (_ : ∀ n, Epi (f.f n)) (_ : QuasiIso f)
          (_ : ∀ n, P (L.X n)), L.IsStrictlyLE a) ∧
      (∀ (K : CochainComplex A ℤ) [K.IsLE a],
        ∃ (L : CochainComplex A ℤ) (f : L ⟶ K) (_ : QuasiIso f) (_ : ∀ n, P (L.X n)),
          L.IsStrictlyLE a)
```

## Tag 05T6, a lemma

[Tag 05T6](https://stacks.math.columbia.edu/tag/05T6) in the Stacks Project.

**`CochainComplex.exists_quasiIso_prop_isStrictlyGE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/DerivedFunctorsOnDerivedCategories.lean, line 481](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/DerivedFunctorsOnDerivedCategories.lean#L481).

> **Stacks 05T6.** Let `A` be an abelian category, let `P` be a class of objects of `A`
> containing a zero object and such that every object of `A` is a subobject of an object
> satisfying `P`, and let `a : ℤ`. Let `K` be a cochain complex with `H ^ n (K) = 0` for `n < a`.
> Then there is a quasi-isomorphism `f : K ⟶ L` with all `L.X n` satisfying `P` and `L.X n = 0`
> for `n < a`; and if moreover `K.X n = 0` for `n < a`, then `f` can be chosen with all `f.f n`
> monomorphisms. (Part (2) of the source is the statement with the last clause dropped, part (1)
> is the statement for a strictly bounded below `K`.)

```lean
public theorem exists_quasiIso_prop_isStrictlyGE (P : ObjectProperty A) [P.ContainsZero]
    (hP : ∀ X : A, ∃ (Y : A) (_ : P Y) (i : X ⟶ Y), Mono i) (a : ℤ)
    (K : CochainComplex A ℤ) [K.IsGE a] :
    ∃ (L : CochainComplex A ℤ) (f : K ⟶ L) (_ : QuasiIso f) (_ : ∀ n, P (L.X n))
      (_ : K.IsStrictlyGE a → ∀ n, Mono (f.f n)), L.IsStrictlyGE a
```

## Tag 05T8, a lemma

[Tag 05T8](https://stacks.math.columbia.edu/tag/05T8) in the Stacks Project.

**`CategoryTheory.Functor.hasPointwiseRightDerivedFunctor_and_le_rightAcyclic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/AcyclicObjects.lean, line 618](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/AcyclicObjects.lean#L618). The attribute's comment: “The right derived functor `RF` is defined everywhere on `K⁺(C)`, and every object of `I` is acyclic for it.”. References: SGA 4 V (0.4), “M acyclic for u”; SGA 4½ Etat 0 (4.2.3.2), “SES-stable σ, + case”.

> **Stacks 05T8.** Let `F : C ⥤ D` be an additive functor between abelian categories and let
> `I` be a class of objects of `C` such that every object of `C` is a subobject of an object
> satisfying `I`, and such that for every short exact sequence `0 ⟶ P ⟶ Q ⟶ R ⟶ 0` with `P` and
> `Q` satisfying `I` the object `R` satisfies `I` and `0 ⟶ F P ⟶ F Q ⟶ F R ⟶ 0` is short exact.
> Then the pointwise right derived functor exists on `K⁺(C)`, and every object satisfying `I`
> is acyclic for it.

```lean
public theorem hasPointwiseRightDerivedFunctor_and_le_rightAcyclic
    (F : C ⥤ D) [F.Additive] (I : ObjectProperty C)
    (hI₁ : ∀ X : C, ∃ (Y : C) (_ : I Y) (i : X ⟶ Y), Mono i)
    (hI₂ : ∀ S : ShortComplex C, S.ShortExact → I S.X₁ → I S.X₂ →
      I S.X₃ ∧ (S.map F).ShortExact) :
    ∃ h : (F.mapHomotopyCategoryPlus ⋙ DerivedCategory.Plus.Qh).HasPointwiseRightDerivedFunctor
        (HomotopyCategory.Plus.quasiIso C),
      letI := h
      I ≤ F.rightAcyclic
```

**`CategoryTheory.Functor.le_rightAcyclic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/AcyclicObjects.lean, line 640](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/AcyclicObjects.lean#L640). References: SGA 4 V (0.4), “M acyclic for u”; SGA 4½ Etat 0 (4.2.3.2), “σ right f-acyclic”.

> **Stacks 05T8.** Let `F : C ⥤ D` be an additive functor between abelian categories whose
> right derived functor `RF : D⁺(C) ⥤ D⁺(D)` exists, and let `I` be a class of objects of `C` such
> that every object of `C` is a subobject of an object satisfying `I`, and such that for every short
> exact sequence `0 ⟶ P ⟶ Q ⟶ R ⟶ 0` with `P` and `Q` satisfying `I` the object `R` satisfies `I`
> and `0 ⟶ F P ⟶ F Q ⟶ F R ⟶ 0` is short exact. Then every object satisfying `I` is acyclic for
> `RF`.

```lean
public theorem le_rightAcyclic (F : C ⥤ D) [F.Additive]
    [(F.mapHomotopyCategoryPlus ⋙ DerivedCategory.Plus.Qh).HasRightDerivedFunctor
      (HomotopyCategory.Plus.quasiIso C)] (I : ObjectProperty C)
    (hI₁ : ∀ X : C, ∃ (Y : C) (_ : I Y) (i : X ⟶ Y), Mono i)
    (hI₂ : ∀ S : ShortComplex C, S.ShortExact → I S.X₁ → I S.X₂ →
      I S.X₃ ∧ (S.map F).ShortExact) :
    I ≤ F.rightAcyclic
```

**`CategoryTheory.Functor.RightAcyclicCriterion.map_quasiIso_nat`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/Resolution/NatIntBridge.lean, line 542](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/Resolution/NatIntBridge.lean#L542). The attribute's comment: “the quasi-isomorphism half, for `ℕ`-indexed complexes”.

> **Stacks 05T8 for `ℕ`-indexed complexes.** Let `F : C ⥤ D` be an additive functor between
> abelian categories and let `I` be a class of objects of `C` adapted to `F` in the sense of
> [Stacks 05T8]. Then `F` carries a quasi-isomorphism of cochain complexes indexed by `ℕ` whose
> terms satisfy `I` to a quasi-isomorphism.
>
> This is `CategoryTheory.Functor.RightAcyclicCriterion.map_quasiIso` transported along extension by
> zero. The boundedness hypotheses of that statement are automatic here, an `ℕ`-indexed complex
> being concentrated in the degrees `≥ 0`.

```lean
lemma map_quasiIso_nat (F : C ⥤ D) [F.Additive] (I : ObjectProperty C)
    (hI₁ : ∀ X : C, ∃ (Y : C) (_ : I Y) (i : X ⟶ Y), Mono i)
    (hI₂ : ∀ S : ShortComplex C, S.ShortExact → I S.X₁ → I S.X₂ →
      I S.X₃ ∧ (S.map F).ShortExact)
    {K L : CochainComplex C ℕ} (f : K ⟶ L) [QuasiIso f]
    (hIK : ∀ n, I (K.X n)) (hIL : ∀ n, I (L.X n)) :
    QuasiIso ((F.mapHomologicalComplex (ComplexShape.up ℕ)).map f)
```

**`CategoryTheory.InjectiveResolution.isIso_homologyMap_map_of_desc`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/Resolution/NatIntBridge.lean, line 592](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/Resolution/NatIntBridge.lean#L592). The attribute's comment: “the computation of `Rⁿ F` by a resolution by `I`-objects, for `ℕ`-indexed resolutions”.

> **Right derived functors are computed by any resolution by `F`-adapted objects.** Let `I` be a
> class of objects of `C` adapted to an additive functor `F` in the sense of [Stacks 05T8], let `J`
> be an injective resolution of `X` with terms in `I`, and let `ε : X[0] ⟶ K` be a quasi-isomorphism
> onto a cochain complex with terms in `I` — a resolution of `X` by `I`-objects, not required to be
> injective. Then any descent `β : K ⟶ J.cocomplex` of the identity along `ε` induces an
> isomorphism on the cohomology of the images under `F`.
>
> Such a `β` exists by `CategoryTheory.InjectiveResolution.exists_desc_of_quasiIso` and is unique up
> to homotopy by `CategoryTheory.InjectiveResolution.nonempty_descHomotopy_of_quasiIso`, so the
> resulting identification `CategoryTheory.InjectiveResolution.isoRightDerivedObjOfQuasiIso` of
> `(F.rightDerived n).obj X` with `Hⁿ(F(K))` does not depend on the choice.

```lean
lemma isIso_homologyMap_map_of_desc (F : C ⥤ D) [F.Additive] (I : ObjectProperty C)
    (hI₁ : ∀ Y : C, ∃ (Z : C) (_ : I Z) (i : Y ⟶ Z), Mono i)
    (hI₂ : ∀ S : ShortComplex C, S.ShortExact → I S.X₁ → I S.X₂ →
      I S.X₃ ∧ (S.map F).ShortExact)
    (J : InjectiveResolution X) {K : CochainComplex C ℕ}
    (ε : (CochainComplex.single₀ C).obj X ⟶ K) [QuasiIso ε] (β : K ⟶ J.cocomplex)
    (hβ : ε ≫ β = J.ι) (hIK : ∀ n, I (K.X n)) (hIJ : ∀ n, I (J.cocomplex.X n)) (n : ℕ) :
    IsIso (HomologicalComplex.homologyMap
      ((F.mapHomologicalComplex (ComplexShape.up ℕ)).map β) n)
```

**`CategoryTheory.InjectiveResolution.isoRightDerivedObjOfQuasiIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/Resolution/NatIntBridge.lean, line 612](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/Resolution/NatIntBridge.lean#L612). The attribute's comment: “the resulting identification of `Rⁿ F (X)` with `Hⁿ (F (K))`”.

> The identification of `(F.rightDerived n).obj X` with the degree-`n` cohomology of `F` applied
> to a resolution of `X` by `F`-adapted objects, along a descent `β` of the identity. See
> `CategoryTheory.InjectiveResolution.isIso_homologyMap_map_of_desc` for the hypotheses and for why
> the choice of `β` does not matter.

```lean
def isoRightDerivedObjOfQuasiIso (F : C ⥤ D) [F.Additive] (I : ObjectProperty C)
    (hI₁ : ∀ Y : C, ∃ (Z : C) (_ : I Z) (i : Y ⟶ Z), Mono i)
    (hI₂ : ∀ S : ShortComplex C, S.ShortExact → I S.X₁ → I S.X₂ →
      I S.X₃ ∧ (S.map F).ShortExact)
    (J : InjectiveResolution X) {K : CochainComplex C ℕ}
    (ε : (CochainComplex.single₀ C).obj X ⟶ K) [QuasiIso ε] (β : K ⟶ J.cocomplex)
    (hβ : ε ≫ β = J.ι) (hIK : ∀ n, I (K.X n)) (hIJ : ∀ n, I (J.cocomplex.X n)) (n : ℕ) :
    (F.rightDerived n).obj X ≅
      (HomologicalComplex.homologyFunctor D (ComplexShape.up ℕ) n).obj
        ((F.mapHomologicalComplex (ComplexShape.up ℕ)).obj K)
```

## Tag 05T9, a lemma

[Tag 05T9](https://stacks.math.columbia.edu/tag/05T9) in the Stacks Project.

**`CategoryTheory.Functor.le_rightAcyclic_op`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/AcyclicObjects.lean, line 787](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/AcyclicObjects.lean#L787). References: SGA 4 XVII (1.2.6); SGA 4½ Etat 0 (4.2.3.2), “σ left f-acyclic”.

> **Stacks 05T9.** Let `F : C ⥤ D` be an additive functor between abelian categories and let
> `P` be a class of objects of `C` such that every object of `C` is a quotient of an object
> satisfying `P`, and such that for every short exact sequence `0 ⟶ P ⟶ Q ⟶ R ⟶ 0` with `Q` and
> `R` satisfying `P` the object `P` satisfies `P` and `0 ⟶ F P ⟶ F Q ⟶ F R ⟶ 0` is short exact.
> Then every object satisfying `P` is acyclic for the left derived functor `LF` of `F`, i.e. its
> opposite is acyclic for the right derived functor of `F.op`.

```lean
public theorem le_rightAcyclic_op {C : Type u} {D : Type u'} [Category.{v} C] [Category.{v'} D]
    [Abelian C] [Abelian D] [HasDerivedCategory.{w} Cᵒᵖ] [HasDerivedCategory.{w'} Dᵒᵖ]
    (F : C ⥤ D) [F.Additive]
    [(F.op.mapHomotopyCategoryPlus ⋙ DerivedCategory.Plus.Qh).HasRightDerivedFunctor
      (HomotopyCategory.Plus.quasiIso Cᵒᵖ)] (P : ObjectProperty C)
    (hP₁ : ∀ X : C, ∃ (Y : C) (_ : P Y) (p : Y ⟶ X), Epi p)
    (hP₂ : ∀ S : ShortComplex C, S.ShortExact → P S.X₂ → P S.X₃ →
      P S.X₁ ∧ (S.map F).ShortExact) :
    P.op ≤ F.op.rightAcyclic
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 13.15, Tag 05T3](https://stacks.math.columbia.edu/tag/05T3)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
