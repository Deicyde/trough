---
declaration: section
origin: cited
lean: CategoryTheory.FilteredObject.IsFilteredInjective, CategoryTheory.FilteredObject.isFilteredInjective_iff_nonempty_iso_stdBiprod, CategoryTheory.FilteredObject.isSplitMono_of_isFilteredInjective, CategoryTheory.FilteredObject.factors_of_isFilteredInjective, CategoryTheory.FilteredObject.exists_mono_isStrict_isFilteredInjective, CochainComplex.exists_filteredQuasiIso_isStrictlyGE_injective_gradedPiece, CochainComplex.exists_hom_comp_eq_of_filteredQuasiIso_of_injective_gradedPiece, CochainComplex.exists_termwiseSplit_shortExact_of_filteredQuasiIso_of_injective_gr
statement: formalized
proof: formalized
---

# 13.26 Filtered derived category and injective resolutions

Section 13.26 of the Stacks Project, [Tag 015O](https://stacks.math.columbia.edu/tag/015O). 15 tags here are carried by 18 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 015P, a definition

[Tag 015P](https://stacks.math.columbia.edu/tag/015P) in the Stacks Project.

**`CategoryTheory.FilteredObject.IsFilteredInjective`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/Defs.lean, line 244](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/Defs.lean#L244).

> An object `I` of `Fil^f(C)` is *filtered injective* if each graded piece
> `gr^p(I) = F^p I / F^{p + 1} I` is an injective object of `C`. As a property of a filtered object
> of `C`, it records that `I` lies in `Fil^f(C)`, i.e. that its filtration is finite.

```lean
public structure FilteredObject.IsFilteredInjective {C : Type u} [Category.{v} C]
    [HasZeroMorphisms C] [HasCokernels C] (I : FilteredObject C ℤᵒᵖ) : Prop
```

## Tag 05TP, a lemma

[Tag 05TP](https://stacks.math.columbia.edu/tag/05TP) in the Stacks Project.

**`CategoryTheory.FilteredObject.isFilteredInjective_iff_nonempty_iso_stdBiprod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/InjectiveObject.lean, line 758](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/InjectiveObject.lean#L758).

> Let `𝒜` be an abelian category. An object `I` of `Fil^f(𝒜)` is filtered injective if and
> only if there are integers `a ≤ b`, injective objects `I_n` of `𝒜` and an isomorphism
> `I ≅ ⨁_{a ≤ n ≤ b} I_n` of filtered objects, where the right-hand side carries the filtration
> `F^p = ⨁_{n ≥ p} I_n` (`FilteredObject.stdBiprod`). The finiteness of the filtration of `I` is
> part of both sides, and is not a hypothesis.

```lean
theorem isFilteredInjective_iff_nonempty_iso_stdBiprod (I : FilteredObject 𝒜 ℤᵒᵖ) :
    I.IsFilteredInjective ↔ ∃ a b : ℤ, a ≤ b ∧ ∃ Inj : ℤ → 𝒜, (∀ n, Injective (Inj n)) ∧
      Nonempty (I ≅ stdBiprod a b Inj)
```

## Tag 05TQ, a lemma

[Tag 05TQ](https://stacks.math.columbia.edu/tag/05TQ) in the Stacks Project.

**`CategoryTheory.FilteredObject.isSplitMono_of_isFilteredInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/InjectiveSplitting.lean, line 210](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/InjectiveSplitting.lean#L210).

> **Stacks 05TQ.** Let `𝒜` be an abelian category. A strict monomorphism `u : I ⟶ A` of
> filtered objects of `𝒜` whose source `I` is a filtered injective object of `Fil^f(𝒜)` — its
> filtration is finite and every graded piece `gr^p(I) = F^p I / F^{p + 1} I` is an injective object
> of `𝒜` — is a split monomorphism: it admits a retraction in the category of filtered objects.

```lean
public theorem isSplitMono_of_isFilteredInjective {𝒜 : Type u} [Category.{v} 𝒜] [Abelian 𝒜]
    {I A : FilteredObject 𝒜 ℤᵒᵖ} (u : I ⟶ A) [IsStrictHom u] (hI : I.IsFilteredInjective) :
    IsSplitMono u
```

## Tag 05TR, a lemma

[Tag 05TR](https://stacks.math.columbia.edu/tag/05TR) in the Stacks Project.

**`CategoryTheory.FilteredObject.factors_of_isFilteredInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/InjectiveExtension.lean, line 266](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/InjectiveExtension.lean#L266).

> **Stacks 05TR.** Let `𝒜` be an abelian category, let `u : A ⟶ B` be a strict morphism of
> filtered objects of `𝒜` and let `f : A ⟶ I` be a morphism into a filtered injective object `I` of
> `Fil^f(𝒜)`: its filtration is finite and every graded piece `gr^p(I) = F^p I / F^{p + 1} I` is an
> injective object of `𝒜`. Then `f` extends along `u`: there is a morphism `g : B ⟶ I` of filtered
> objects with `f = u ≫ g`. The source assumes `u` to be a strict monomorphism; monomorphy is not
> used, and is automatic on `Fil^f(𝒜)`.

```lean
public theorem factors_of_isFilteredInjective {𝒜 : Type u} [Category.{v} 𝒜] [Abelian 𝒜]
    {A B I : FilteredObject 𝒜 ℤᵒᵖ} (f : A ⟶ I) (u : A ⟶ B) [IsStrictHom u]
    (hI : I.IsFilteredInjective) :
    ∃ g : B ⟶ I, u ≫ g = f
```

## Tag 05TS, a lemma

[Tag 05TS](https://stacks.math.columbia.edu/tag/05TS) in the Stacks Project.

**`CategoryTheory.FilteredObject.exists_mono_isStrict_isFilteredInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/InjectiveResolutionDegreeZero/FilteredResolution.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/InjectiveResolutionDegreeZero/FilteredResolution.lean#L66).

> **Stacks 05TS.** Let `𝒜` be an abelian category with enough injectives. Every object `A` of
> `Fil^f(𝒜)` admits a strict monomorphism `u : A ⟶ I` into a filtered injective object `I`: the
> underlying morphism of `u` is a monomorphism of `𝒜` and `u` is strict.

```lean
public theorem _root_.CategoryTheory.FilteredObject.exists_mono_isStrict_isFilteredInjective
    [EnoughInjectives 𝒜] (A : FilteredObject 𝒜 ℤᵒᵖ) (hA : A.filtration.IsFinite) :
    ∃ (I : FilteredObject 𝒜 ℤᵒᵖ) (u : A ⟶ I), Mono u.hom ∧ IsStrict u ∧ I.IsFilteredInjective
```

## Tag 05TT, a lemma

[Tag 05TT](https://stacks.math.columbia.edu/tag/05TT) in the Stacks Project.

**`CochainComplex.exists_filteredQuasiIso_isStrictlyGE_injective_gradedPiece`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/InjectiveResolutionDegreeZero/FilteredResolution.lean, line 248](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/InjectiveResolutionDegreeZero/FilteredResolution.lean#L248). References: EGA 0 (13.6.2), “existence of resolution”.

> **Stacks 05TT.** Let `𝒜` be an abelian category with enough injectives and let `K^•` be a
> filtered cochain complex of `𝒜` concentrated in degree `0` with finite filtration, i.e. `K^•` is
> `A[0]` for an object `A` of `Fil^f(𝒜)`. Then there is a filtered quasi-isomorphism
> `α : K^• ⟶ I^•`, that is, one whose graded pieces `gr^p(α)` are all quasi-isomorphisms, where
> `I^•` is a complex of filtered injective objects with `I^n = 0` for `n < 0`: every term
> `(I^n, F^• I^n)` is a filtered injective object of `Fil^f(𝒜)`.

```lean
public theorem exists_filteredQuasiIso_isStrictlyGE_injective_gradedPiece {𝒜 : Type u}
    [Category.{v} 𝒜] [Abelian 𝒜] [EnoughInjectives 𝒜]
    (K : FilteredObject (CochainComplex 𝒜 ℤ) ℤᵒᵖ) [K.X.IsStrictlyGE 0] [K.X.IsStrictlyLE 0]
    (hK : K.filtration.IsFinite) :
    ∃ (I : FilteredObject (CochainComplex 𝒜 ℤ) ℤᵒᵖ) (α : K ⟶ I)
      (_ : CochainComplex.filteredQuasiIso 𝒜 α) (_ : I.X.IsStrictlyGE 0),
      ∀ n : ℤ, (evalFil I n).IsFilteredInjective
```

## Tag 05TU, a lemma

[Tag 05TU](https://stacks.math.columbia.edu/tag/05TU) in the Stacks Project.

**`CochainComplex.exists_hom_comp_eq_of_filteredQuasiIso_of_injective_gradedPiece`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/InjectiveHom.lean, line 1468](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/InjectiveHom.lean#L1468). References: EGA 0 (13.6.3), “special case”.

> **Stacks 05TU.** Let `𝒜` be an abelian category, let `f : A ⟶ B` be a morphism of filtered
> objects, placed in degree `0` by taking the filtered complexes `A` and `B` to be concentrated in
> degree `0`, and let `a : A[0] ⟶ I^•` and `b : B[0] ⟶ J^•` be morphisms into filtered complexes with
> degreewise finite filtrations, where `a` is a filtered quasi-isomorphism and `J^•` vanishes in
> negative degrees and consists of filtered injective objects, i.e. every term `(J^n, F^• J^n)` is a
> filtered injective object of `Fil^f(𝒜)`. Then `f` lifts to a morphism `g : I^• ⟶ J^•` with
> `a ≫ g = f ≫ b` on the nose.
>
> This is the lift that `CochainComplex.FilteredInjectiveResolution.exists_resolutionSystem` needs.
>
> Three of the source's hypotheses are unused here and dropped: that `b` be a filtered
> quasi-isomorphism, and that `I^•` vanish in negative degrees and have filtered injective graded
> pieces. The lift comes from the surjectivity half of [Stacks, Tag 05TY], which asks only that `a`
> be a filtered quasi-isomorphism into a complex of `K(Fil^f(𝒜))` and that the target `J^•` be
> bounded below and filtered injective; the homotopy it produces is degenerate because `A` is
> concentrated in degree `0`, which turns the commutation in `K(Fil^f(𝒜))` into an equality of
> morphisms of filtered complexes.

```lean
public theorem exists_hom_comp_eq_of_filteredQuasiIso_of_injective_gradedPiece
    {𝒜 : Type u} [Category.{v} 𝒜] [Abelian 𝒜]
    {A B I J : FilteredObject (CochainComplex 𝒜 ℤ) ℤᵒᵖ}
    [A.X.IsStrictlyGE 0] [A.X.IsStrictlyLE 0] [J.X.IsStrictlyGE 0]
    (f : A ⟶ B) (a : A ⟶ I) (b : B ⟶ J) (ha : filteredQuasiIso 𝒜 a)
    (hAfin : ∀ n : ℤ, ∃ p q : ℤ, IsIso ((A.filtration.ι.app (op p)).f n) ∧
      IsZero ((A.filtration.obj (op q)).X n))
    (hIfin : ∀ n : ℤ, ∃ p q : ℤ, IsIso ((I.filtration.ι.app (op p)).f n) ∧
      IsZero ((I.filtration.obj (op q)).X n))
    (hJ : ∀ n : ℤ, (evalFil J n).IsFilteredInjective) :
    ∃ g : I ⟶ J, a ≫ g = f ≫ b
```

## Tag 05TV, a lemma

[Tag 05TV](https://stacks.math.columbia.edu/tag/05TV) in the Stacks Project.

**`CochainComplex.exists_termwiseSplit_shortExact_of_filteredQuasiIso_of_injective_gr`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/TermwiseSplit/TwistedSum.lean, line 712](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/TermwiseSplit/TwistedSum.lean#L712).

> **Stacks 05TV.** Let `𝒜` be an abelian category and let `0 → A → B → C → 0` be a short exact
> sequence of `Fil^f(𝒜)`, i.e. morphisms `α : A ⟶ B`, `β : B ⟶ C` of filtered objects with finite
> filtrations whose composite vanishes and whose graded pieces form short exact sequences
> `0 → gr^p A → gr^p B → gr^p C → 0`.
> Let `a : A[0] ⟶ I^•` and `c : C[0] ⟶ J^•` be filtered quasi-isomorphisms, where `I^•` and `J^•`
> are complexes of filtered objects with finite filtrations, vanishing in negative degrees, and
> where each `I^n` is a filtered injective object of `Fil^f(𝒜)`. Then
> there are a complex `M^•` of filtered objects, morphisms `u : I^• ⟶ M^•`, `v : M^• ⟶ J^•` and
> `b : B[0] ⟶ M^•` such that `0 → I^• → M^• → J^• → 0` is short exact, `α ≫ b = a ≫ u` and
> `b ≫ v = β ≫ c`, and the sequence `0 → I^n → M^n → J^n → 0` splits in `Fil(𝒜)` in each degree
> `n`: there are a retraction `r` of `u^n` and a section `s` of `v^n` compatible with the
> filtrations. Filtered objects are placed in degree `0` by taking the filtered complexes `A`, `B`,
> `C` to be concentrated in degree `0`.

```lean
public theorem exists_termwiseSplit_shortExact_of_filteredQuasiIso_of_injective_gr
    {𝒜 : Type u} [Category.{v} 𝒜] [Abelian 𝒜]
    {A B C I J : FilteredObject (CochainComplex 𝒜 ℤ) ℤᵒᵖ}
    [A.X.IsStrictlyGE 0] [A.X.IsStrictlyLE 0] [C.X.IsStrictlyGE 0] [C.X.IsStrictlyLE 0]
    [I.X.IsStrictlyGE 0] [J.X.IsStrictlyGE 0]
    (α : A ⟶ B) (β : B ⟶ C) (a : A ⟶ I) (c : C ⟶ J)
    (hcomp : α.hom ≫ β.hom = 0)
    (hgr : ∀ p : ℤ, (ShortComplex.mk ((gr p).map α)
      ((gr p).map β) (by
        have hz : ∀ q : ℤᵒᵖ, (α ≫ β).natTrans.app q = 0 := fun q =>
          zero_of_comp_mono (C.filtration.ι.app q) (by simp [hcomp])
        rw [← Functor.map_comp]
        apply coequalizer.hom_ext
        simp only [grMap_map, cokernel.π_desc, hz, zero_comp]
        exact comp_zero.symm)).ShortExact)
    (ha : filteredQuasiIso 𝒜 a) (hc : filteredQuasiIso 𝒜 c)
    (hA : ∀ n : ℤ, ∃ p q : ℤ, IsIso ((A.filtration.ι.app (op p)).f n) ∧
      IsZero ((A.filtration.obj (op q)).X n))
    (hB : ∀ n : ℤ, ∃ p q : ℤ, IsIso ((B.filtration.ι.app (op p)).f n) ∧
      IsZero ((B.filtration.obj (op q)).X n))
    (hC : ∀ n : ℤ, ∃ p q : ℤ, IsIso ((C.filtration.ι.app (op p)).f n) ∧
      IsZero ((C.filtration.obj (op q)).X n))
    (hJfin : ∀ n : ℤ, ∃ p q : ℤ, IsIso ((J.filtration.ι.app (op p)).f n) ∧
      IsZero ((J.filtration.obj (op q)).X n))
    (hI : ∀ n : ℤ, (evalFil I n).IsFilteredInjective) :
    ∃ (M : FilteredObject (CochainComplex 𝒜 ℤ) ℤᵒᵖ) (u : I ⟶ M) (v : M ⟶ J) (b : B ⟶ M)
      (huv : u.hom ≫ v.hom = 0), (ShortComplex.mk u.hom v.hom huv).ShortExact ∧
      α ≫ b = a ≫ u ∧ b ≫ v = β ≫ c ∧
      ∀ n : ℤ, ∃ (r : M.X.X n ⟶ I.X.X n) (s : J.X.X n ⟶ M.X.X n),
        u.hom.f n ≫ r = 𝟙 (I.X.X n) ∧ s ≫ v.hom.f n = 𝟙 (J.X.X n) ∧
        (∀ p : ℤ, ∃ rp : (M.filtration.obj (op p)).X n ⟶ (I.filtration.obj (op p)).X n,
          rp ≫ (I.filtration.ι.app (op p)).f n = (M.filtration.ι.app (op p)).f n ≫ r) ∧
        (∀ p : ℤ, ∃ sp : (J.filtration.obj (op p)).X n ⟶ (M.filtration.obj (op p)).X n,
          sp ≫ (M.filtration.ι.app (op p)).f n = (J.filtration.ι.app (op p)).f n ≫ s)
```

## Tag 05TW, a lemma

[Tag 05TW](https://stacks.math.columbia.edu/tag/05TW) in the Stacks Project.

**`CochainComplex.exists_mono_isStrictHom_filteredQuasiIso_isStrictlyGE_injective_gradedPiece`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/InjectiveResolution.lean, line 1485](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/InjectiveResolution.lean#L1485). References: EGA 0 (13.6.2), “existence of resolution”.

> **Stacks 05TW.** Let `𝒜` be an abelian category with enough injectives and let `K^•` be a
> filtered cochain complex of `𝒜` with `K^n = 0` for `n < a` and with each `K^n` of finite
> filtration, i.e. an object of `K^+(Fil^f(𝒜))`. Then there is a filtered quasi-isomorphism
> `α : K^• ⟶ I^•`, that is, one whose graded pieces `gr^p(α)` are all quasi-isomorphisms, which is
> moreover a strict monomorphism — degreewise, each `K^n ⟶ I^n` is a monomorphism with
> `F^p K^n = (K^n) ∩ F^p I^n` — where `I^•` is a complex of filtered injective objects with
> `I^n = 0` for `n < a`: every term `(I^n, F^• I^n)` is a filtered injective object of
> `Fil^f(𝒜)`.

```lean
public theorem exists_mono_isStrictHom_filteredQuasiIso_isStrictlyGE_injective_gradedPiece
    (K : FilteredObject (CochainComplex 𝒜 ℤ) ℤᵒᵖ) (a : ℤ) [K.X.IsStrictlyGE a]
    (hK : ∀ n : ℤ, ∃ p q : ℤ, IsIso ((K.filtration.ι.app (op p)).f n) ∧
      IsZero ((K.filtration.obj (op q)).X n)) :
    ∃ (I : FilteredObject (CochainComplex 𝒜 ℤ) ℤᵒᵖ) (α : K ⟶ I)
      (_ : CochainComplex.filteredQuasiIso 𝒜 α) (_ : Mono α.hom)
      (_ : FilteredObject.IsStrictHom α) (_ : I.X.IsStrictlyGE a),
      ∀ n : ℤ, (evalFil I n).IsFilteredInjective
```

## Tag 05TX, a lemma

[Tag 05TX](https://stacks.math.columbia.edu/tag/05TX) in the Stacks Project.

**`CochainComplex.exists_homotopy_zero_of_filteredAcyclic_of_injective_gradedPiece`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/AcyclicHomotopy.lean, line 599](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/AcyclicHomotopy.lean#L599).

> **Stacks 05TX.** Let `𝒜` be an abelian category and let `K^•`, `I^•` be filtered cochain
> complexes of `𝒜` whose terms have finite filtrations, i.e. objects of `K(Fil^f(𝒜))`. Assume `K^•`
> is filtered acyclic, that is every `gr^p K^• = F^p K^•/F^{p + 1} K^•` is acyclic, and that `I^•`
> is bounded below, `I^n = 0` for `n < n₀`, and consists of filtered injective objects of
> `Fil^f(𝒜)`: every term `(I^n, F^• I^n)` is filtered injective. Then every morphism
> `α : K^• ⟶ I^•` of filtered complexes is homotopic to zero by a filtered homotopy: there is a
> homotopy `h` from `α` to `0` on the underlying complexes each of whose components
> `h^{i,j} : K^i ⟶ I^j` carries `F^p K^i` into `F^p I^j`. Equivalently
> `Hom_{K(Fil^f(𝒜))}(K^•, I^•) = 0`.

```lean
public theorem exists_homotopy_zero_of_filteredAcyclic_of_injective_gradedPiece
    {𝒜 : Type u} [Category.{v} 𝒜] [Abelian 𝒜]
    {K I : FilteredObject (CochainComplex 𝒜 ℤ) ℤᵒᵖ} (α : K ⟶ I) (n₀ : ℤ) [I.X.IsStrictlyGE n₀]
    (hK : filteredAcyclic 𝒜 K)
    (hKfin : ∀ n : ℤ, ∃ p q : ℤ, IsIso ((K.filtration.ι.app (op p)).f n) ∧
      IsZero ((K.filtration.obj (op q)).X n))
    (hI : ∀ n : ℤ, (evalFil I n).IsFilteredInjective) :
    ∃ h : Homotopy α.hom 0, ∀ i j p : ℤ,
      ∃ hp : (K.filtration.obj (op p)).X i ⟶ (I.filtration.obj (op p)).X j,
        hp ≫ (I.filtration.ι.app (op p)).f j
          = (K.filtration.ι.app (op p)).f i ≫ h.hom i j
```

## Tag 05TY, a lemma

[Tag 05TY](https://stacks.math.columbia.edu/tag/05TY) in the Stacks Project.

**`CochainComplex.bijective_precomp_full_and_map_eq_iff_filteredHomotopy_of_injective_gradedPiece`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/InjectiveHom.lean, line 1412](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/InjectiveHom.lean#L1412).

> **Stacks 05TY.** Let `𝒜` be an abelian category, let `Filf` be the class of filtered cochain
> complexes of `𝒜` whose filtration is finite in each degree — so that `Filf.FullSubcategory` is
> `K(Fil^f(𝒜))` — and let `Q` be a localisation of it at the filtered quasi-isomorphisms, that is,
> the filtered derived category `DF(𝒜)` (Definition 05S2). Let `I^•` be a bounded below complex,
> `I^n = 0` for `n < n₀`, consisting of filtered injective objects, that is with every `gr^p(I^n)`
> an injective object of `𝒜`. Then:
>
> 1. for every filtered quasi-isomorphism `α : K^• ⟶ L^•` in `K(Fil^f(𝒜))`, precomposition with `α`
>    is a bijection `Hom_{K(Fil^f(𝒜))}(L^•, I^•) ⟶ Hom_{K(Fil^f(𝒜))}(K^•, I^•)`: every
>    `γ : K^• ⟶ I^•` is filtered homotopic to `α ≫ β` for some `β : L^• ⟶ I^•`, and if `α ≫ β` and
>    `α ≫ β'` are filtered homotopic then so are `β` and `β'`;
> 2. for every `M^•` in `K(Fil^f(𝒜))`, `Hom_{K(Fil^f(𝒜))}(M^•, I^•) = Hom_{DF(𝒜)}(M^•, I^•)`: every
>    `φ : Q.obj M^• ⟶ Q.obj I^•` is `Q.map f` for a morphism of filtered complexes `f : M^• ⟶ I^•`,
>    and `Q.map f = Q.map g` exactly when `f` and `g` are filtered homotopic.
>
> Here a *filtered homotopy* between morphisms of filtered complexes is a homotopy `h` of the
> underlying complexes of `𝒜` each of whose components `h^{i,j}` carries `F^p` into `F^p`.

```lean
public theorem bijective_precomp_full_and_map_eq_iff_filteredHomotopy_of_injective_gradedPiece
    {𝒜 : Type u} [Category.{v} 𝒜] [Abelian 𝒜] {D : Type u'} [Category.{v'} D]
    (Filf : ObjectProperty (FilteredObject (CochainComplex 𝒜 ℤ) ℤᵒᵖ))
    (hFilf : ∀ K, Filf K ↔ ∀ n : ℤ, ∃ p q : ℤ,
      IsIso ((K.filtration.ι.app (op p)).f n) ∧ IsZero ((K.filtration.obj (op q)).X n))
    (Q : Filf.FullSubcategory ⥤ D)
    [Q.IsLocalization ((filteredQuasiIso 𝒜).inverseImage Filf.ι)]
    (I : Filf.FullSubcategory) (n₀ : ℤ) [I.obj.X.IsStrictlyGE n₀]
    (hI : ∀ p n : ℤ, Injective (((gr p).obj I.obj).X n)) :
    (∀ (K L : Filf.FullSubcategory) (α : K ⟶ L),
        (filteredQuasiIso 𝒜).inverseImage Filf.ι α →
        (∀ γ : K ⟶ I, ∃ β : L ⟶ I,
          ∃ h : Homotopy (Filf.ι.map (α ≫ β)).hom (Filf.ι.map γ).hom, ∀ i j p : ℤ,
            ∃ hp : (K.obj.filtration.obj (op p)).X i ⟶ (I.obj.filtration.obj (op p)).X j,
              hp ≫ (I.obj.filtration.ι.app (op p)).f j
                = (K.obj.filtration.ι.app (op p)).f i ≫ h.hom i j) ∧
        ∀ β β' : L ⟶ I,
          (∃ h : Homotopy (Filf.ι.map (α ≫ β)).hom (Filf.ι.map (α ≫ β')).hom, ∀ i j p : ℤ,
            ∃ hp : (K.obj.filtration.obj (op p)).X i ⟶ (I.obj.filtration.obj (op p)).X j,
              hp ≫ (I.obj.filtration.ι.app (op p)).f j
                = (K.obj.filtration.ι.app (op p)).f i ≫ h.hom i j) →
          ∃ h : Homotopy (Filf.ι.map β).hom (Filf.ι.map β').hom, ∀ i j p : ℤ,
            ∃ hp : (L.obj.filtration.obj (op p)).X i ⟶ (I.obj.filtration.obj (op p)).X j,
              hp ≫ (I.obj.filtration.ι.app (op p)).f j
                = (L.obj.filtration.ι.app (op p)).f i ≫ h.hom i j) ∧
      ∀ M : Filf.FullSubcategory,
        (∀ φ : Q.obj M ⟶ Q.obj I, ∃ f : M ⟶ I, Q.map f = φ) ∧
        ∀ f g : M ⟶ I, Q.map f = Q.map g ↔
          ∃ h : Homotopy (Filf.ι.map f).hom (Filf.ι.map g).hom, ∀ i j p : ℤ,
            ∃ hp : (M.obj.filtration.obj (op p)).X i ⟶ (I.obj.filtration.obj (op p)).X j,
              hp ≫ (I.obj.filtration.ι.app (op p)).f j
                = (M.obj.filtration.ι.app (op p)).f i ≫ h.hom i j
```

## Tag 015Q, a lemma

[Tag 015Q](https://stacks.math.columbia.edu/tag/015Q) in the Stacks Project.

**`CochainComplex.FilteredDerivedCategory.isEquivalence_isTriangulated_toPlus_and_squares`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/FilteredDerivedCategory/Triangulated.lean, line 571](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/FilteredDerivedCategory/Triangulated.lean#L571).

> Let `𝒜` be an abelian category with enough injectives, let `I^f ⊂ Fil^f(𝒜)`
> be the filtered injective objects and `I ⊂ 𝒜` the injective objects. The canonical functor
> `K⁺(I^f) ⥤ DF⁺(𝒜)` is exact, fully faithful and essentially surjective, i.e. an equivalence of
> triangulated categories. Furthermore the squares
> ```
> K⁺(I^f) ──→ DF⁺(𝒜)          K⁺(I^f) ──→ DF⁺(𝒜)
>   │gr^p        │gr^p           │forget F    │forget F
>   ↓            ↓               ↓            ↓
> K⁺(I) ────→ D⁺(𝒜)           K⁺(I) ────→ D⁺(𝒜)
> ```
> commute. Here `gr^p, forget F : DF(𝒜) ⥤ D(𝒜)` are the functors induced by
> `gr^p, forget F : K(Fil^f(𝒜)) ⥤ K(𝒜)`, as recorded by the isomorphisms
> `Qh ⋙ gr^p ≅ gr^p ⋙ Q` and `Qh ⋙ forget F ≅ forget F ⋙ Q`.

```lean
theorem isEquivalence_isTriangulated_toPlus_and_squares [EnoughInjectives 𝒜] :
    (toPlus 𝒜).IsEquivalence ∧ (toPlus 𝒜).IsTriangulated ∧
      (∀ p : ℤ, Nonempty (Qh (𝒜 := 𝒜) ⋙ grDF p ≅
          (FiniteFilteredObject.grP p).mapHomotopyCategory _ ⋙ DerivedCategory.Qh) ∧
        Nonempty (toPlus 𝒜 ⋙ liftDFPlus (FiniteFilteredObject.grP p) (grP_inverts p) ≅
          (injectivePlus 𝒜).lift ((filteredInjectivePlus 𝒜).ι ⋙
              (FiniteFilteredObject.grP p).mapHomotopyCategory _)
            (fun X => injectivePlus_grP_obj p X.property) ⋙ injectivePlusQ 𝒜)) ∧
      Nonempty (Qh (𝒜 := 𝒜) ⋙ forgetDF ≅
        FiniteFilteredObject.forget.mapHomotopyCategory _ ⋙ DerivedCategory.Qh) ∧
      Nonempty (toPlus 𝒜 ⋙ liftDFPlus FiniteFilteredObject.forget forget_inverts ≅
        (injectivePlus 𝒜).lift ((filteredInjectivePlus 𝒜).ι ⋙
            FiniteFilteredObject.forget.mapHomotopyCategory _)
          (fun X => injectivePlus_forget_obj X.property) ⋙ injectivePlusQ 𝒜)
```

## Tag 015U, an equation

[Tag 015U](https://stacks.math.columbia.edu/tag/015U) in the Stacks Project.

**`CategoryTheory.FilteredDerived.filteredRightDerivedFunctorGrPIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FilteredDerived/Category/GradedRightDerivedFunctor.lean, line 323](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FilteredDerived/Category/GradedRightDerivedFunctor.lean#L323). The attribute's comment: “the isomorphism `gr^p ∘ RT ≅ RT ∘ gr^p` of functors `DF⁺(A) ⥤ D⁺(B)`, for `T` additive and `A` with enough injectives, with `RT = T_ext ∘ j'`: `j'` is `(toPlus A).inv` and `T_ext` is `T` applied termwise on `K⁺(Iᶠ)`, `F^p T(I) = T(F^p I)` (`imageMapOfMonoIso`)”.

> Taking the `p`-th graded piece commutes with the filtered right derived functor: for an
> additive functor `T : A ⥤ B` out of an abelian category with enough injectives, there is a
> natural isomorphism `RT ⋙ gr^p ≅ gr^p ⋙ RT` of functors `DF⁺(A) ⥤ D⁺(B)`, i.e.
> `gr^p ∘ RT ≅ RT ∘ gr^p`, where the `RT` on the left is the filtered right derived functor and
> the one on the right is the right derived functor `D⁺(A) ⥤ D⁺(B)`.
>
> This is the isomorphism of [Stacks, Tag 015U]. There the filtered right derived functor is
> `RT = T_ext ∘ j'` ([Stacks, Tag 05U2]), with `j'` a quasi-inverse of the equivalence
> `K⁺(Iᶠ) ⥤ DF⁺(A)` of [Stacks, Tag 015Q] and `T_ext` the functor of [Stacks, Tag 05U0],
> `T_ext(I) = ⨁ T(I_q)` with `F^p T_ext(I) = ⨁_{q ≥ p} T(I_q)` for a splitting
> `I ≅ ⨁ I_q`, `F^p I = ⨁_{q ≥ p} I_q`, of a filtered injective object ([Stacks, Tag 015T]).
> Here `filteredRightDerivedFunctor T` is `(toPlus A).inv ⋙ filteredInjectivePlusMapToDerivedPlus T`:
> `j'` is `(toPlus A).inv`, and on `K⁺(Iᶠ)` the functor `T` is applied termwise with the
> filtration `F^p T(I) = T(F^p I) ⊆ T(I)`. On a filtered injective object each `F^p I ⟶ I` is a
> split monomorphism, so `T(F^p I) ⟶ T(I)` is a monomorphism and the image filtration is
> `T(F^p I)` itself (`imageMapOfMonoIso`); under a splitting `I ≅ ⨁ I_q` it is
> `⨁_{q ≥ p} T(I_q)`, which is `T_ext(I)`. The identity
> `gr^p(T_ext(I)) ≅ T(gr^p I)` used by the source is `gradedImageIso`.
>
> See [Stacks Project, Tag 03TE](https://stacks.math.columbia.edu/tag/03TE) and
> [Stacks Project, Tag 015U](https://stacks.math.columbia.edu/tag/015U).

```lean
noncomputable def filteredRightDerivedFunctorGrPIso (T : A ⥤ B) [T.Additive]
    [EnoughInjectives A] (p : ℤ) :
    filteredRightDerivedFunctor T ⋙
        CochainComplex.FilteredDerivedCategory.liftDFPlus (FiniteFilteredObject.grP p)
          (CochainComplex.FilteredDerivedCategory.grP_inverts p) ≅
      CochainComplex.FilteredDerivedCategory.liftDFPlus (FiniteFilteredObject.grP p)
          (CochainComplex.FilteredDerivedCategory.grP_inverts p) ⋙
        T.rightDerivedFunctorPlus
```

## Tag 015V, an equation

[Tag 015V](https://stacks.math.columbia.edu/tag/015V) in the Stacks Project.

**`CategoryTheory.FilteredDerived.filteredRightDerivedFunctorForgetIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FilteredDerived/Category/GradedRightDerivedFunctor.lean, line 383](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FilteredDerived/Category/GradedRightDerivedFunctor.lean#L383). The attribute's comment: “(forget F) ∘ RT ≅ RT ∘ (forget F) as functors DF⁺(A) ⥤ D⁺(B), for T additive”.

> Forgetting the filtration commutes with the filtered right derived functor: for an
> additive functor `T : A ⥤ B` out of an abelian category with enough injectives, there is a
> natural isomorphism `RT ⋙ forget F ≅ forget F ⋙ RT` of functors `DF⁺(A) ⥤ D⁺(B)`, where the
> `RT` on the left is the filtered right derived functor `DF⁺(A) ⥤ DF⁺(B)` and the one on the
> right is the right derived functor `D⁺(A) ⥤ D⁺(B)`.
>
> The source assumes `T` left exact; only additivity is used.

```lean
noncomputable def filteredRightDerivedFunctorForgetIso (T : A ⥤ B) [T.Additive]
    [EnoughInjectives A] :
    filteredRightDerivedFunctor T ⋙
        CochainComplex.FilteredDerivedCategory.liftDFPlus FiniteFilteredObject.forget
          CochainComplex.FilteredDerivedCategory.forget_inverts ≅
      CochainComplex.FilteredDerivedCategory.liftDFPlus FiniteFilteredObject.forget
          CochainComplex.FilteredDerivedCategory.forget_inverts ⋙
        T.rightDerivedFunctorPlus
```

## Tag 015W, a lemma

[Tag 015W](https://stacks.math.columbia.edu/tag/015W) in the Stacks Project.

**`CochainComplex.exists_spectralSequence_rightDerivedFunctorPlus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/FilteredDerivedCategory/InjectiveResolutions.lean, line 265](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/FilteredDerivedCategory/InjectiveResolutions.lean#L265). The attribute's comment: “the spectral sequence, its `E_1` page, boundedness, convergence and finiteness of the induced filtration”. References: EGA 0 (13.6.4), “E\_1, abutment, biregular”.

> **Stacks 015W.** Let `T : 𝒜 ⥤ ℬ` be an additive functor of abelian categories, `𝒜` having
> enough injectives, and let `(K^•, F)` be an object of `Comp⁺(Fil^f(𝒜))`: a filtered complex with
> `K^n = 0` for `n < a` whose filtration is finite in each degree. Let `α : K^• ⟶ I^•` be a filtered
> quasi-isomorphism to a bounded below complex of filtered injective objects — such a filtered
> injective resolution exists ([Stacks, Tag 05TW],
> `exists_mono_isStrictHom_filteredQuasiIso_isStrictlyGE_injective_gradedPiece`) and the statement
> holds for every choice of it. Let `E` be the spectral sequence of the filtered complex
> `T(I^•) = RT(K^•)` of `ℬ`, presented as in [Stacks, Tag 012M] by its pages
> `E_r^{p,q} = Z_r^{p,q}/D_r^{p,q}` and its differentials `d_r` of bidegree `(r, -r + 1)` induced by
> the differential of `T(I^•)`. Then
>
> 1. `E_1^{p,q} ≅ R^{p+q}T(gr^p K^•)`;
> 2. `E` is bounded: for each `n` only finitely many `E_0^{p, n - p}` are nonzero;
> 3. `E` converges to `H^*(T(I^•)) = R^*T(K^•)`: `d_r^{p,q} = 0` for `r ≫ 0`, and the stable
>    cycles and boundaries exist and are those of (012S) and (012T) with equality;
> 4. the induced filtration on each `R^nT(K^•) = H^n(T(I^•))` is finite;
> 5. `H^n(T(I^•)) ≅ R^nT(K^•)`.

```lean
theorem exists_spectralSequence_rightDerivedFunctorPlus
    [HasDerivedCategory.{w} A] [EnoughInjectives A] (T : A ⥤ B) [T.Additive]
    {K I : FilteredObject (CochainComplex A ℤ) ℤᵒᵖ} (a b : ℤ) [K.X.IsStrictlyGE a]
    [I.X.IsStrictlyGE b] (hK : K.filtration.IsDegreewiseFinite) (α : K ⟶ I)
    (hα : filteredQuasiIso A α) (hI : ∀ n : ℤ, (evalFil I n).IsFilteredInjective)
    (F : ∀ (_p n : ℤ), Subobject ((mapFilteredInjective T I hI).X.X n))
    (hF : ∀ p n : ℤ, F p n =
      Subobject.mk (((mapFilteredInjective T I hI).filtration.ι.app (op p)).f n))
    (Z : ∀ (_r _p n : ℤ), Subobject ((mapFilteredInjective T I hI).X.X n))
    (hZ : ∀ r p n : ℤ, Z r p n = F p n ⊓
      (Subobject.pullback ((mapFilteredInjective T I hI).X.d n (n + 1))).obj (F (p + r) (n + 1)))
    (D : ∀ (_r _p n : ℤ), Subobject ((mapFilteredInjective T I hI).X.X n))
    (hD : ∀ r p n : ℤ, D r p n = Z (r - 1) (p + 1) n ⊔
      (Subobject.«exists» ((mapFilteredInjective T I hI).X.d (n - 1) n)).obj
        (Z (r - 1) (p - r + 1) (n - 1)))
    (FH : ∀ (n _p : ℤ), Subobject ((mapFilteredInjective T I hI).X.homology n))
    (hFH : ∀ n p : ℤ, FH n p = imageSubobject
      (HomologicalComplex.homologyMap ((mapFilteredInjective T I hI).filtration.ι.app (op p)) n)) :
    ∃ (e : ∀ (r p q n : ℤ) (hr : 0 ≤ r) (_ : n = p + q),
        ((spectralSequenceOf (mapFilteredInjective T I hI) F hF).page r hr).X (p, q) ≅
        cokernel (Subobject.ofLE _ _ (inf_le_right : D r p n ⊓ Z r p n ≤ Z r p n))),
      (∀ (r p q n : ℤ) (hr : 0 ≤ r) (hn : n = p + q),
        ∃ δ : (Z r p n : B) ⟶ (Z r (p + r) (n + 1) : B),
          δ ≫ (Z r (p + r) (n + 1)).arrow =
            (Z r p n).arrow ≫ (mapFilteredInjective T I hI).X.d n (n + 1) ∧
          cokernel.π (Subobject.ofLE _ _ (inf_le_right : D r p n ⊓ Z r p n ≤ Z r p n)) ≫
              (e r p q n hr hn).inv ≫
                ((spectralSequenceOf (mapFilteredInjective T I hI) F hF).page r hr).d
                  (p, q) (p + r, q - r + 1) =
            δ ≫ cokernel.π (Subobject.ofLE _ _ (inf_le_right :
                D r (p + r) (n + 1) ⊓ Z r (p + r) (n + 1) ≤ Z r (p + r) (n + 1))) ≫
              (e r (p + r) (q - r + 1) (n + 1) hr (by omega)).inv) ∧
      (∀ p q : ℤ, Nonempty
        (((spectralSequenceOf (mapFilteredInjective T I hI) F hF).page 1).X (p, q) ≅
        (DerivedCategory.Plus.homologyFunctor B (p + q)).obj
          (T.rightDerivedFunctorPlus.obj (DerivedCategory.Plus.Qh.obj
            ((HomotopyCategory.Plus.quotient A).obj
              ⟨(FilteredObject.gr p).obj K, ⟨a, isStrictlyGE_gr K a p⟩⟩))))) ∧
      (∀ n : ℤ, {p : ℤ | ¬ IsZero
        (((spectralSequenceOf (mapFilteredInjective T I hI) F hF).page 0).X (p, n - p))}.Finite) ∧
      (∀ p q : ℤ, ∃ b : ℤ, ∀ (r : ℤ) (hr : 0 ≤ r), b ≤ r →
        ((spectralSequenceOf (mapFilteredInjective T I hI) F hF).page r hr).d
          (p, q) (p + r, q - r + 1) = 0) ∧
      (∀ p n : ℤ,
        IsGLB (Set.range fun r : ℕ => F p n ⊓
            (Subobject.pullback ((mapFilteredInjective T I hI).X.d n (n + 1))).obj
              (F (p + r) (n + 1)) ⊔ F (p + 1) n)
          (kernelSubobject ((mapFilteredInjective T I hI).X.d n (n + 1)) ⊓ F p n ⊔
            F (p + 1) n) ∧
        IsLUB (Set.range fun r : ℕ => F p n ⊓
            (Subobject.«exists» ((mapFilteredInjective T I hI).X.d (n - 1) n)).obj
              (F (p - r) (n - 1)) ⊔ F (p + 1) n)
          (imageSubobject ((mapFilteredInjective T I hI).X.d (n - 1) n) ⊓ F p n ⊔
            F (p + 1) n)) ∧
      (∀ n : ℤ, ∃ p₀ p₁ : ℤ, p₀ ≤ p₁ ∧ FH n p₀ = ⊤ ∧ FH n p₁ = ⊥) ∧
      (∀ n : ℤ, Nonempty ((mapFilteredInjective T I hI).X.homology n ≅
        (DerivedCategory.Plus.homologyFunctor B n).obj
          (T.rightDerivedFunctorPlus.obj (DerivedCategory.Plus.Qh.obj
            ((HomotopyCategory.Plus.quotient A).obj ⟨K.X, ⟨a, inferInstance⟩⟩)))))
```

**`CochainComplex.exists_spectralSequenceMap_rightDerivedFunctorPlus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/FilteredDerivedCategory/InjectiveResolutions.lean, line 517](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/FilteredDerivedCategory/InjectiveResolutions.lean#L517). The attribute's comment: “functoriality in `K^•`: the induced morphism of spectral sequences, independent of choices on `E_r` for `r ≥ 1`”. References: EGA 0 (13.6.3), “existence of v”; EGA 0 (13.6.4), “E\_r indep. of choices”.

> **Stacks 015W, functoriality.** Let `f : K^• ⟶ L^•` be a morphism of
> `Comp⁺(Fil^f(𝒜))` and let `α : K^• ⟶ I^•`, `β : L^• ⟶ J^•` be filtered injective resolutions.
> There is a morphism `γ : I^• ⟶ J^•` with `α ≫ γ` filtered homotopic to `f ≫ β`
> ([Stacks, Tag 05TY]); it induces a morphism of spectral sequences
> `E_r(T(I^•)) ⟶ E_r(T(J^•))` ([Stacks, Tag 012O]), and on the pages `E_r`, `r ≥ 1`, this
> morphism does not depend on the choice of `γ`.

```lean
theorem exists_spectralSequenceMap_rightDerivedFunctorPlus
    {K L I J : FilteredObject (CochainComplex A ℤ) ℤᵒᵖ}
    (hK : K.filtration.IsDegreewiseFinite)
    (a b : ℤ) [I.X.IsStrictlyGE a] [J.X.IsStrictlyGE b]
    (hI : ∀ n : ℤ, (evalFil I n).IsFilteredInjective)
    (hJ : ∀ n : ℤ, (evalFil J n).IsFilteredInjective)
    (α : K ⟶ I) (hα : filteredQuasiIso A α) (β : L ⟶ J) (f : K ⟶ L) :
    (∃ γ : I ⟶ J, FilteredHomotopic (α ≫ γ) (f ≫ β)) ∧
      ∀ γ γ' : I ⟶ J, FilteredHomotopic (α ≫ γ) (f ≫ β) →
        FilteredHomotopic (α ≫ γ') (f ≫ β) → ∀ (r : ℤ) (hr : 1 ≤ r),
          (filteredSpectralSequenceMap (mapFilteredInjectiveMap T γ hI hJ)).hom r (by omega) =
            (filteredSpectralSequenceMap (mapFilteredInjectiveMap T γ' hI hJ)).hom r
              (by omega)
```

**`CochainComplex.filteredHomotopic_comp_and_spectralSequenceMap_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/FilteredDerivedCategory/InjectiveResolutions.lean, line 542](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/FilteredDerivedCategory/InjectiveResolutions.lean#L542). The attribute's comment: “the construction is compatible with composition”.

> **Stacks 015W, compatibility with composition.** If `γ` lifts `f : K^• ⟶ L^•` and `δ` lifts
> `g : L^• ⟶ M^•` along filtered injective resolutions, then `γ ≫ δ` lifts `f ≫ g`, and the
> morphism of spectral sequences induced by `γ ≫ δ` is the composite of those induced by `γ` and
> `δ`.

```lean
theorem filteredHomotopic_comp_and_spectralSequenceMap_comp
    {K L M I J P : FilteredObject (CochainComplex A ℤ) ℤᵒᵖ}
    (hI : ∀ n : ℤ, (evalFil I n).IsFilteredInjective)
    (hJ : ∀ n : ℤ, (evalFil J n).IsFilteredInjective)
    (hP : ∀ n : ℤ, (evalFil P n).IsFilteredInjective)
    (α : K ⟶ I) (β : L ⟶ J) (ε : M ⟶ P) (f : K ⟶ L) (g : L ⟶ M) (γ : I ⟶ J) (δ : J ⟶ P)
    (hγ : FilteredHomotopic (α ≫ γ) (f ≫ β)) (hδ : FilteredHomotopic (β ≫ δ) (g ≫ ε)) :
    FilteredHomotopic (α ≫ γ ≫ δ) ((f ≫ g) ≫ ε) ∧
      filteredSpectralSequenceMap (mapFilteredInjectiveMap T (γ ≫ δ) hI hP) =
        filteredSpectralSequenceMap (mapFilteredInjectiveMap T γ hI hJ) ≫
          filteredSpectralSequenceMap (mapFilteredInjectiveMap T δ hJ hP)
```

**`CochainComplex.isIso_spectralSequenceMap_rightDerivedFunctorPlus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/FilteredDerivedCategory/InjectiveResolutions.lean, line 568](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/FilteredDerivedCategory/InjectiveResolutions.lean#L568). The attribute's comment: “the terms `(E_r, d_r)` for `r ≥ 1` do not depend on any choices”. References: EGA 0 (13.6.4), “partial”.

> **Stacks 015W, independence of choices.** For two filtered injective resolutions
> `α : K^• ⟶ I^•` and `α' : K^• ⟶ I'^•` of the same object, any `γ : I^• ⟶ I'^•` with
> `α ≫ γ` filtered homotopic to `α'` induces isomorphisms `E_r(T(I^•)) ≅ E_r(T(I'^•))` on all pages
> `r ≥ 1`; when `I'^• = I^•` and `α' = α` the induced morphism is the identity on these pages. So
> the terms `(E_r, d_r)`, `r ≥ 1`, do not depend on the choice of resolution.

```lean
theorem isIso_spectralSequenceMap_rightDerivedFunctorPlus
    {K I I' : FilteredObject (CochainComplex A ℤ) ℤᵒᵖ} (hK : K.filtration.IsDegreewiseFinite)
    (a a' : ℤ) [I.X.IsStrictlyGE a] [I'.X.IsStrictlyGE a']
    (hI : ∀ n : ℤ, (evalFil I n).IsFilteredInjective)
    (hI' : ∀ n : ℤ, (evalFil I' n).IsFilteredInjective)
    (α : K ⟶ I) (hα : filteredQuasiIso A α) (α' : K ⟶ I') (hα' : filteredQuasiIso A α')
    (γ : I ⟶ I') (hγ : FilteredHomotopic (α ≫ γ) α') :
    (∀ (r : ℤ) (hr : 1 ≤ r),
      IsIso ((filteredSpectralSequenceMap (mapFilteredInjectiveMap T γ hI hI')).hom r
        (by omega))) ∧
    ∀ γ₀ : I ⟶ I, FilteredHomotopic (α ≫ γ₀) α → ∀ (r : ℤ) (hr : 1 ≤ r),
      (filteredSpectralSequenceMap (mapFilteredInjectiveMap T γ₀ hI hI)).hom r (by omega) =
        𝟙 _
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 13.26, Tag 015O](https://stacks.math.columbia.edu/tag/015O)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
