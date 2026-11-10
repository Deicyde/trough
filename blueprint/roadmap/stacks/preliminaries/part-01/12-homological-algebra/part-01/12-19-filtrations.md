---
declaration: section
origin: cited
lean: CategoryTheory.FilteredObject.gr, CategoryTheory.FilteredObject.grGraded, CategoryTheory.Filtration.antitone, CategoryTheory.Filtration.ofAntitone, CategoryTheory.Filtration.pullback, CategoryTheory.Filtration.pushforward, CategoryTheory.Filtration.HasInter, CategoryTheory.Filtration.HasUnion
statement: formalized
proof: formalized
---

# 12.19 Filtrations

Section 12.19 of the Stacks Project, [Tag 0120](https://stacks.math.columbia.edu/tag/0120). 16 tags here are carried by 74 declarations of the repository (73 in StacksCore and 1 in StacksFrontier) and 5 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0120, the section

[Tag 0120](https://stacks.math.columbia.edu/tag/0120) in the Stacks Project.

**`CategoryTheory.FilteredObject.gr`**, an abbrev in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/GradedPieces.lean, line 297](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/GradedPieces.lean#L297). The attribute's comment: “the graded pieces `gr^p(A) = F^pA/F^{p+1}A` of the text before 05SP, as functors”. References: EGA 0 (11.1.1), “partial”; EGA 0 (13.6.4).

> Stacks' graded piece `gr^p(A) = F^pA/F^{p+1}A` of a decreasing `ℤ`-filtration (`I := ℤᵒᵖ`), as
> a functor `Fil(𝒜) ⥤ 𝒜`; `(gr p).obj A = cokernel (A.filtration.step (succHom p))` by `rfl`.

```lean
noncomputable abbrev gr (p : ℤ) : FilteredObject C ℤᵒᵖ ⥤ C
```

**`CategoryTheory.FilteredObject.grGraded`**, an abbrev in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/GradedPieces.lean, line 302](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/GradedPieces.lean#L302). The attribute's comment: “the functor `gr : Fil(𝒜) ⥤ Gr(𝒜)` of the paragraph before 05SP”.

> Stacks' `gr : Fil(𝒜) ⥤ Gr(𝒜)`, the graded object with `p`-th piece `gr^p(A)`;
> `grGraded ⋙ GradedObject.eval p ≅ gr p` is `Iso.refl _`.

```lean
noncomputable abbrev grGraded : FilteredObject C ℤᵒᵖ ⥤ GradedObject ℤ C
```

## Tag 0121, a definition

[Tag 0121](https://stacks.math.columbia.edu/tag/0121) in the Stacks Project.

**`CategoryTheory.Filtration.antitone`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Basic.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Basic.lean#L146). The attribute's comment: “(1) the decreasing condition, for `I := ℤᵒᵖ`”.

> Stacks 0121(1): a filtration indexed by `ℤᵒᵖ` is decreasing, `F^mA ⊆ F^nA` for `n ≤ m`.

```lean
lemma antitone (F : Filtration X ℤᵒᵖ) : Antitone fun n : ℤ => F.subobject (op n)
```

**`CategoryTheory.Filtration.ofAntitone`**, a def in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Basic.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Basic.lean#L153). The attribute's comment: “(1) a decreasing family of subobjects, as a filtration indexed by `ℤᵒᵖ`”.

> Stacks 0121(1), conversely: a decreasing family `F : ℤ → Subobject X` of subobjects is a
> filtration indexed by `ℤᵒᵖ`, whose `n`-th step is (the underlying object of) `F n`.

```lean
noncomputable def ofAntitone (F : ℤ → Subobject X) (hF : Antitone F) : Filtration X ℤᵒᵖ
```

**`CategoryTheory.Filtration.pullback`**, a def in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Basic.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Basic.lean#L197). The attribute's comment: “(5) the induced filtration, along any morphism `f`; the tag is `f` a monomorphism”.

> The pullback filtration `f⁻¹F` along `f : Y ⟶ X`, with steps `Y ×_X F^iX`. For a
> monomorphism `f` this is the induced filtration `F^iY = Y ∩ F^iX` of Stacks 0121(5).

```lean
noncomputable def pullback (F : Filtration X I) {Y : C} (f : Y ⟶ X) : Filtration Y I
```

**`CategoryTheory.Filtration.pushforward`**, a def in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Basic.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Basic.lean#L238). The attribute's comment: “(6) the quotient filtration, along any morphism `π`; the tag is `π` an epimorphism”.

> The image filtration `π(F)` along `π : X ⟶ Y`, with steps the images of `F^iX ⟶ X ⟶ Y`.
> For an epimorphism `π` this is the quotient filtration `F^iY = π(F^iX)` of Stacks 0121(6).

```lean
noncomputable def pushforward (F : Filtration X I) {Y : C} (g : X ⟶ Y) : Filtration Y I
```

**`CategoryTheory.Filtration.HasInter`**, a def in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Basic.lean, line 277](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Basic.lean#L277). The attribute's comment: “(8) existence of `⋂ F^iA`, as a greatest lower bound in `Subobject A`”.

> Stacks 0121(8): `⋂ F^iA` exists, i.e. the steps have a greatest lower bound in
> `Subobject X`.

```lean
def HasInter (F : Filtration X I) : Prop
```

**`CategoryTheory.Filtration.HasUnion`**, a def in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Basic.lean, line 281](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Basic.lean#L281). The attribute's comment: “(8) existence of `⋃ F^iA`, as a least upper bound in `Subobject A`”.

> Stacks 0121(8): `⋃ F^iA` exists, i.e. the steps have a least upper bound in `Subobject X`.

```lean
def HasUnion (F : Filtration X I) : Prop
```

**`CategoryTheory.Filtration.IsSeparated`**, a def in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Basic.lean, line 285](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Basic.lean#L285). The attribute's comment: “(9) separated”.

> Stacks 0121(9): a filtration is separated if `⋂ F^iA = 0`.

```lean
def IsSeparated [HasInitial C] [InitialMonoClass C] (F : Filtration X I) : Prop
```

**`CategoryTheory.Filtration.IsExhaustive`**, a def in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Basic.lean, line 290](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Basic.lean#L290). The attribute's comment: “(9) exhaustive”. References: EGA 0 (11.1.3).

> Stacks 0121(9): a filtration is exhaustive if `⋃ F^iA = A`.

```lean
def IsExhaustive (F : Filtration X I) : Prop
```

**`CategoryTheory.FilteredObject.factors`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Basic.lean, line 447](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Basic.lean#L447). The attribute's comment: “(3) a morphism of filtered objects satisfies `φ(F^iA) ⊆ F^iB`”.

> Stacks 0121(3), one direction: a morphism of filtered objects satisfies `φ(F^iA) ⊆ F^iB`.

```lean
lemma factors (f : A ⟶ B) (i : I) :
    (B.subobject i).Factors (A.filtration.ι.app i ≫ f.hom)
```

**`CategoryTheory.FilteredObject.homMk'`**, a def in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Basic.lean, line 454](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Basic.lean#L454). The attribute's comment: “(3) `φ` with `φ(F^iA) ⊆ F^iB` for all `i` is a morphism of filtered objects”.

> Stacks 0121(3), the other direction: a morphism `φ : A ⟶ B` with `φ(F^iA) ⊆ F^iB` for all
> `i` is a morphism of filtered objects.

```lean
noncomputable def homMk' (φ : A.X ⟶ B.X)
    (h : ∀ i, (B.subobject i).Factors (A.filtration.ι.app i ≫ φ)) : A ⟶ B
```

**`CategoryTheory.Filtration.IsFinite`**, a class in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Finite.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Finite.lean#L61). The attribute's comment: “(7) for an arbitrary index category and any category `C`”.

> **Stacks 0121** (7).
> A filtration is finite if some step is all of `X` and some step is an initial object.

```lean
class IsFinite (F : Filtration X I) : Prop extends HasTopStep F, HasBotStep F
```

**`CochainComplex.Filtered.exists_inducedFiltrationStep_le`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Leray/FunctorialFilteredAbutment.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/Leray/FunctorialFilteredAbutment.lean#L86). The attribute's comment: “(3) for the filtrations induced on cohomology by a morphism of filtered complexes”.

> A morphism of filtered complexes carries each step of the induced filtration of cohomology into
> the corresponding step: `H^n(φ)(F^pH^n(K^•)) ⊆ F^pH^n(L^•)`.

```lean
lemma exists_inducedFiltrationStep_le {K L : Filtered C} (φ : K ⟶ L) (n p : ℤ) :
    (Subobject.«exists» (HomologicalComplex.homologyMap φ.hom n)).obj
        (K.inducedFiltrationStep n p) ≤ L.inducedFiltrationStep n p
```

Declarations registered for the tag:

- [`CategoryTheory.Filtration`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Filtration#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Filtration/Basic.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Basic.lean#L74) (StacksCore): “(1) for an arbitrary index category `I`; the tag is `I := ℤᵒᵖ`”.
- [`CategoryTheory.FilteredObject`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.FilteredObject#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Filtration/Basic.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Basic.lean#L76) (StacksCore): “(2) filtered objects of an arbitrary category”. References: SGA 4 Vbis (2.5.1), “more general”.
- [`CategoryTheory.FilteredObject.Hom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.FilteredObject.Hom#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Filtration/Basic.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Basic.lean#L77) (StacksCore): “(3) morphisms of filtered objects, as `φ` together with the maps `F^iA ⟶ F^iB`”. References: SGA 4 Vbis (2.5.1), “more general”.
- [`CategoryTheory.FilteredObject.instCategory`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.FilteredObject.instCategory#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Filtration/Basic.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Basic.lean#L79) (StacksCore): “(4) the category `Fil(𝒜)`”.
- [`CategoryTheory.FilteredObject.forget`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.FilteredObject.forget#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Filtration/Basic.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Basic.lean#L80) (StacksCore): “the forgetful functor `Fil(𝒜) ⥤ 𝒜`”.

## Tag 0122, a lemma

[Tag 0122](https://stacks.math.columbia.edu/tag/0122) in the Stacks Project.

**`CategoryTheory.FilteredObject.hasKernels`**, an instance in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Limits.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Limits.lean#L132). The attribute's comment: “(3) kernels, with the induced filtration”.

> Stacks 0122 (3): `Fil(𝒜)` has kernels.

```lean
noncomputable instance hasKernels : HasKernels (FilteredObject C I)
```

**`CategoryTheory.FilteredObject.hasCokernels`**, an instance in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Limits.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Limits.lean#L208). The attribute's comment: “(3) cokernels, with the quotient filtration”.

> Stacks 0122 (3): `Fil(𝒜)` has cokernels.

```lean
noncomputable instance hasCokernels : HasCokernels (FilteredObject C I)
```

**`CategoryTheory.FilteredObject.imageIso`**, a def in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Limits.lean, line 291](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Limits.lean#L291). The attribute's comment: “(3) images `Ker(Coker f)`: `Im(f.hom)` with the induced filtration”.

> Stacks 0122 (3): the image of `f` in `Fil(𝒜)` is `Im(f.hom)` with the induced filtration.

```lean
noncomputable def imageIso (f : A ⟶ B) : Abelian.image f ≅ imageObj f
```

**`CategoryTheory.FilteredObject.coimageIso`**, a def in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Limits.lean, line 321](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Limits.lean#L321). The attribute's comment: “(3) coimages `Coker(Ker f)`: `Coim(f.hom)` with the quotient filtration”.

> Stacks 0122 (3): the coimage of `f` in `Fil(𝒜)` is `Coim(f.hom)` with the quotient
> filtration.

```lean
noncomputable def coimageIso (f : A ⟶ B) : Abelian.coimage f ≅ coimageObj f
```

**`CategoryTheory.FilteredObject.preadditive`**, an instance in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Preadditive.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Preadditive.lean#L107). The attribute's comment: “(1) `Fil(𝒜)` is preadditive, for any preadditive `𝒜` and any index category”. References: SGA 4 Vbis (2.5.1), “partial”.

> Stacks 0122 (1): `Fil(𝒜)` is preadditive. Morphisms are added on the underlying morphism
> and on every step of the filtration.

```lean
noncomputable instance preadditive : Preadditive (FilteredObject C I)
```

**`CategoryTheory.FilteredObject.hasZeroObject`**, an instance in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Preadditive.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Preadditive.lean#L162). The attribute's comment: “(2) the zero object, for any `𝒜` with a zero object and any index category”.

> Stacks 0122 (2): `Fil(𝒜)` has a zero object.

```lean
noncomputable instance hasZeroObject : HasZeroObject (FilteredObject C I)
```

**`CategoryTheory.FilteredObject.hasBinaryBiproducts`**, an instance in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Preadditive.lean, line 233](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Preadditive.lean#L233). The attribute's comment: “(1) direct sums `A ⊕ B` with `F^i(A ⊕ B) = F^iA ⊕ F^iB`, for any index category”.

> Stacks 0122 (1): `Fil(𝒜)` has direct sums, `F^i(A ⊕ B) = F^iA ⊕ F^iB`.

```lean
noncomputable instance hasBinaryBiproducts : HasBinaryBiproducts (FilteredObject C I)
```

**`CategoryTheory.FilteredObject.hasFiniteBiproducts`**, an instance in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Preadditive.lean, line 367](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Preadditive.lean#L367). The attribute's comment: “(1) `Fil(𝒜)` is additive: preadditive with finite biproducts”.

> Stacks 0122 (1): `Fil(𝒜)` is an additive category (preadditive with finite biproducts).

```lean
noncomputable instance hasFiniteBiproducts [HasZeroObject C] :
    HasFiniteBiproducts (FilteredObject C I)
```

## Tag 0123, a definition

[Tag 0123](https://stacks.math.columbia.edu/tag/0123) in the Stacks Project.

**`CategoryTheory.FilteredObject.IsStrict`**, a class in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Strict.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Strict.lean#L196). The attribute's comment: “for filtered objects of any category with images and pullbacks”.

> Stacks 0123: a morphism `f : A ⟶ B` of filtered objects is *strict* if
> `f(F^iA) = f(A) ∩ F^iB` for all `i`.

```lean
class IsStrict (f : A ⟶ B) : Prop
```

**`CategoryTheory.FilteredObject.isStrict_iff_pullback_eq_sup`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Strict.lean, line 540](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Strict.lean#L540). The attribute's comment: “the equivalent condition `f⁻¹(F^iB) = F^iA + Ker(f)` of the following remark”.

> The remark after Stacks 0123: `f` is strict if and only if `f⁻¹(F^iB) = F^iA + Ker(f)`
> for all `i`.

```lean
theorem isStrict_iff_pullback_eq_sup (f : A ⟶ B) :
    IsStrict f ↔ ∀ i, (Subobject.pullback f.hom).obj (B.subobject i) =
      A.subobject i ⊔ kernelSubobject f.hom
```

## Tag 05SI, a lemma

[Tag 05SI](https://stacks.math.columbia.edu/tag/05SI) in the Stacks Project.

**`CategoryTheory.FilteredObject.isStrict_iff_isIso_coimageImageComparison`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Strict.lean, line 602](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Strict.lean#L602). The attribute's comment: “for an arbitrary index category `I`”.

> Stacks 05SI: a morphism `f : A ⟶ B` of filtered objects of an abelian category is strict if
> and only if the canonical morphism `Coim(f) ⟶ Im(f)` of Stacks 0107, computed in `Fil(𝒜)`, is an
> isomorphism. The comparison is always an isomorphism in `𝒜`; the content is that the quotient
> filtration on `Coim(f)` and the induced filtration on `Im(f)` agree.

```lean
theorem isStrict_iff_isIso_coimageImageComparison (f : A ⟶ B) :
    IsStrict f ↔ IsIso (Abelian.coimageImageComparison f)
```

## Tag 05SK, a lemma

[Tag 05SK](https://stacks.math.columbia.edu/tag/05SK) in the Stacks Project.

**`CategoryTheory.FilteredObject.IsStrict.biprod_lift`**, an instance in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Strict.lean, line 385](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Strict.lean#L385). The attribute's comment: “`(f, g)` is strict, for any additive `𝒜` with images and pullbacks and any `I`”.

> Stacks 05SK, strictness: if `f : A ⟶ B` is a strict monomorphism of filtered objects and
> `g : A ⟶ D` is any morphism of filtered objects, then `(f, g) : A ⟶ B ⊕ D` is strict. For a
> monomorphism, strictness is the cartesian condition (0124), which is stable under pairing
> (`isStrictHom_biprod_lift`); this needs only preadditivity, binary biproducts, images and pullbacks
> in `𝒜`.

```lean
instance IsStrict.biprod_lift (f : A ⟶ B) (g : A ⟶ D) [Mono f.hom] [IsStrict f] :
    IsStrict (biprod.lift f g)
```

**`CategoryTheory.FilteredObject.isStrict_and_mono_biprod_lift`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Strict.lean, line 396](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Strict.lean#L396). The attribute's comment: “for any additive `𝒜` with images and pullbacks, and any index category `I`”.

> Stacks 05SK: if `f : A ⟶ B` is a strict monomorphism of filtered objects and `g : A ⟶ D` is
> any morphism of filtered objects, then `(f, g) : A ⟶ B ⊕ D` is a strict monomorphism.

```lean
theorem isStrict_and_mono_biprod_lift (f : A ⟶ B) (g : A ⟶ D) [Mono f.hom] [IsStrict f] :
    IsStrict (biprod.lift f g) ∧ Mono (biprod.lift f g)
```

## Tag 05SL, a lemma

[Tag 05SL](https://stacks.math.columbia.edu/tag/05SL) in the Stacks Project.

**`CategoryTheory.FilteredObject.IsStrict.biprod_desc`**, an instance in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Strict.lean, line 485](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Strict.lean#L485). The attribute's comment: “`f ⊕ g` is strict, for any balanced additive `𝒜` with images and pullbacks”.

> Stacks 05SL, strictness: if `f : B ⟶ A` is a strict epimorphism of filtered objects and
> `g : D ⟶ A` is any morphism of filtered objects, then `f ⊕ g : B ⊕ D ⟶ A` is strict. This needs
> only a balanced additive `𝒜` with images and pullbacks.

```lean
instance IsStrict.biprod_desc {D : FilteredObject C I} (f : B ⟶ A) (g : D ⟶ A) [Epi f.hom]
    [IsStrict f] : IsStrict (biprod.desc f g)
```

**`CategoryTheory.FilteredObject.isStrict_and_epi_biprod_desc`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Strict.lean, line 492](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Strict.lean#L492). The attribute's comment: “for any balanced additive `𝒜` with images and pullbacks, and any `I`”.

> Stacks 05SL: if `f : B ⟶ A` is a strict epimorphism of filtered objects and `g : D ⟶ A` is any
> morphism of filtered objects, then `f ⊕ g : B ⊕ D ⟶ A` is a strict epimorphism.

```lean
theorem isStrict_and_epi_biprod_desc {D : FilteredObject C I} (f : B ⟶ A) (g : D ⟶ A) [Epi f.hom]
    [IsStrict f] : IsStrict (biprod.desc f g) ∧ Epi (biprod.desc f g)
```

## Tag 0124, a lemma

[Tag 0124](https://stacks.math.columbia.edu/tag/0124) in the Stacks Project.

**`CategoryTheory.FilteredObject.isStrict_iff_subobject_eq_pullback_of_mono`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Strict.lean, line 271](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Strict.lean#L271). The attribute's comment: “the injective case: `u` is strict iff the filtration on `A` is the induced one”.

> Stacks 0124, the injective case: a monomorphism `u : A ⟶ B` of filtered objects is strict
> if and only if the filtration on `A` is the induced filtration `F^iA = A ∩ F^iB`. This holds in
> any category with images and pullbacks.

```lean
theorem isStrict_iff_subobject_eq_pullback_of_mono (f : A ⟶ B) [Mono f.hom] :
    IsStrict f ↔ ∀ i, A.subobject i = (B.filtration.pullback f.hom).subobject i
```

**`CategoryTheory.FilteredObject.isStrict_iff_subobject_eq_pushforward_of_epi`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Strict.lean, line 410](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Strict.lean#L410). The attribute's comment: “the surjective case: `u` is strict iff the filtration on `B` is the quotient one”.

> Stacks 0124, the surjective case: an epimorphism `u : A ⟶ B` of filtered objects is strict
> if and only if the filtration on `B` is the quotient filtration `F^iB = u(F^iA)`. This holds in
> any balanced category with images and pullbacks.

```lean
theorem isStrict_iff_subobject_eq_pushforward_of_epi (f : A ⟶ B) [Epi f.hom] :
    IsStrict f ↔ ∀ i, B.subobject i = (A.filtration.pushforward f.hom).subobject i
```

## Tag 05SJ, a lemma

[Tag 05SJ](https://stacks.math.columbia.edu/tag/05SJ) in the Stacks Project.

**`CategoryTheory.FilteredObject.isStrict_comp_iff_of_mono`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Strict.lean, line 287](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Strict.lean#L287). The attribute's comment: “(2) as an equivalence: for a strict monomorphism `g`, `f ≫ g` is strict iff `f` is”.

> Stacks 05SJ (2), as an equivalence: if `g : B ⟶ D` is a strict monomorphism, then `f ≫ g` is
> strict if and only if `f` is. Indeed `g` preserves intersections, so
> `g(f(F^iA)) = g(f(A)) ∩ F^iD` unwinds to `g(f(F^iA)) = g(f(A) ∩ F^iB)`, and `g` is injective on
> subobjects. This holds in any category with images and pullbacks.

```lean
theorem isStrict_comp_iff_of_mono {D : FilteredObject C I} (f : A ⟶ B) (g : B ⟶ D) [IsStrict g]
    [Mono g.hom] : IsStrict (f ≫ g) ↔ IsStrict f
```

**`CategoryTheory.FilteredObject.IsStrict.comp_of_mono`**, an instance in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Strict.lean, line 300](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Strict.lean#L300). The attribute's comment: “(2): `g ∘ f` is strict for strict `f`, `g` with `g` a monomorphism”.

> Stacks 05SJ (2): the composite of two strict morphisms is strict when the second one is a
> monomorphism.

```lean
instance IsStrict.comp_of_mono {D : FilteredObject C I} (f : A ⟶ B) (g : B ⟶ D) [IsStrict f]
    [IsStrict g] [Mono g.hom] : IsStrict (f ≫ g)
```

**`CategoryTheory.FilteredObject.isStrict_comp_iff_of_epi`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Strict.lean, line 452](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Strict.lean#L452). The attribute's comment: “(3) as an equivalence: for a strict epimorphism `f`, `f ≫ g` is strict iff `g` is”.

> Stacks 05SJ (3), as an equivalence: if `f : A ⟶ B` is a strict epimorphism, then `f ≫ g` is
> strict if and only if `g` is. Indeed `f(F^iA) = F^iB` and `g(f(A)) = g(B)`. This holds in any
> balanced category with images and pullbacks.

```lean
theorem isStrict_comp_iff_of_epi {D : FilteredObject C I} (f : A ⟶ B) (g : B ⟶ D) [IsStrict f]
    [Epi f.hom] : IsStrict (f ≫ g) ↔ IsStrict g
```

**`CategoryTheory.FilteredObject.IsStrict.comp_of_epi`**, an instance in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Strict.lean, line 462](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Strict.lean#L462). The attribute's comment: “(3): `g ∘ f` is strict for strict `f`, `g` with `f` an epimorphism”.

> Stacks 05SJ (3): the composite of two strict morphisms is strict when the first one is an
> epimorphism.

```lean
instance IsStrict.comp_of_epi {D : FilteredObject C I} (f : A ⟶ B) (g : B ⟶ D) [IsStrict f]
    [IsStrict g] [Epi f.hom] : IsStrict (f ≫ g)
```

## Tag 0129, a lemma

[Tag 0129](https://stacks.math.columbia.edu/tag/0129) in the Stacks Project.

**`CategoryTheory.FilteredObject.isStrictHom_pullbackHom`**, an instance in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Basic.lean, line 379](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Basic.lean#L379). The attribute's comment: “`X → A` is strict, for any `k`, `n`”.

> The induced filtration is cartesian over `A`. For `X ⊆ Y ⊆ A` and `m = k ≫ n` this makes
> `X → A` strict (Stacks 0129), through `IsStrictHom.isStrict`; no hypothesis on `k`, `n`.

```lean
instance isStrictHom_pullbackHom (A : FilteredObject C I) {Y : C} (m : Y ⟶ A.X) :
    IsStrictHom (pullbackHom A m)
```

**`CategoryTheory.FilteredObject.isStrictHom_pullbackObjHom`**, an instance in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Basic.lean, line 740](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Basic.lean#L740). The attribute's comment: “`X → Y` is strict”.

> The filtration induced along `k ≫ n` is induced along `k` from the one induced along `n`,
> `X ∩ F^iA = X ∩ (Y ∩ F^iA)`: `pullbackObjHom A k n` is cartesian, as its composite with the
> cartesian `pullbackHom A n` is the cartesian `pullbackHom A (k ≫ n)`. No hypothesis on `k`, `n`.
> Hence `X → Y` is strict (Stacks 0129), through `IsStrictHom.isStrict`.
> (An instance: `pullbackObjHom` is a `def`, so type class search cannot derive this.)

```lean
instance isStrictHom_pullbackObjHom : IsStrictHom (pullbackObjHom A k n)
```

**`CategoryTheory.FilteredObject.isStrict_pullbackHom`**, an instance in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Strict.lean, line 502](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Strict.lean#L502). The attribute's comment: “`X → A`, `Y → A`: a subobject with the induced filtration is strict”.

> A subobject with the induced filtration is a strict monomorphism.

```lean
instance isStrict_pullbackHom [HasPullbacks C] [HasImages C] (A : FilteredObject C I) {Y : C}
    (m : Y ⟶ A.X) [Mono m] : IsStrict (pullbackHom A m)
```

**`CategoryTheory.FilteredObject.isStrict_pushforwardHom`**, an instance in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Strict.lean, line 510](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Strict.lean#L510). The attribute's comment: “`Y → Y/X`: a quotient with the quotient filtration is strict”.

> The image filtration makes `e` a strict morphism, for any `e`: `e(F^iA) ⊆ e(A)`. For an
> epimorphism `e` this says that a quotient with the quotient filtration is a strict epimorphism.

```lean
instance isStrict_pushforwardHom [HasPullbacks C] [HasImages C] (A : FilteredObject C I)
    {Z : C} (e : A.X ⟶ Z) : IsStrict (pushforwardHom A e)
```

**`CategoryTheory.FilteredObject.isStrictHom_subquotientHom`**, an instance in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Subquotient.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Subquotient.lean#L170). The attribute's comment: “`Y/X`'s quotient filtration is the one induced from `A/X`, so `Y/X → A/X` is strict; any `k`, `n`, any `I`”.

> Stacks 0129: the two filtrations on `Y/X` agree, i.e. `Y/X ⟶ A/X` is cartesian: the quotient
> filtration on `Y/X` (from the induced filtration on `Y`) is the filtration induced along
> `Y/X ⟶ A/X` from the quotient filtration on `A/X`. On the steps this is the identity
> `π(Y ∩ F^iA) = q⁻¹(π'(F^iA))`, `π : Y → Y/X`, `π' : A → A/X`, `q : Y/X → A/X`, the modular law
> read in `Subobject (Y/X)`. No hypothesis on `k` or `n`: for a monomorphism `n` (Stacks' `Y ⊆ A`)
> this is the statement of 0129; in general "induced" means pulled back along `Y/X → A/X`, and
> `Mono n` enters only for `Y/X = Ker(A/X → A/Y)`.

```lean
instance isStrictHom_subquotientHom : IsStrictHom (subquotientHom A k n)
```

**`CategoryTheory.FilteredObject.subquotientIsoPullbackObj`**, a def in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Subquotient.lean, line 188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Subquotient.lean#L188). The attribute's comment: “`Y/X` with the quotient filtration is the pullback along `Y/X → A/X` of `A/X`”.

> Stacks 0129, literally: `Y/X` with the quotient filtration is `q⁻¹(A/X)`, the pullback along
> `q : Y/X ⟶ A/X` of the quotient filtration on `A/X` (for a monomorphism `n`: the subobject
> `Y/X ⊆ A/X` with its induced filtration), as filtered objects over `A/X`
> (`subquotientIsoPullbackObj_hom_pullbackHom`).

```lean
noncomputable def subquotientIsoPullbackObj :
    subquotientObj A k n ≅
      pullbackObj (pushforwardObj A (cokernel.π (k ≫ n)))
        (cokernel.map k (k ≫ n) (𝟙 X) n (by simp))
```

**`CategoryTheory.FilteredObject.subquotientIsoKernelObj`**, a def in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Subquotient.lean, line 215](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Subquotient.lean#L215). The attribute's comment: “`Y/X` with the quotient filtration is `Ker(A/X → A/Y)` with the induced filtration”.

> Stacks 0129, literally: `Y/X` with the quotient filtration is `Ker(A/X → A/Y)` with the
> induced filtration, as filtered objects over `A/X` (`subquotientIsoKernelObj_hom_kernelι`); the
> underlying isomorphism is the third isomorphism theorem `Abelian.cokernelIsoKernelCokernelMap`.

```lean
noncomputable def subquotientIsoKernelObj [Mono n] :
    subquotientObj A k n ≅ kernelObj (quotientHom A k n)
```

**`CategoryTheory.FilteredObject.isStrict_pullbackHom_comp_pushforwardHom`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Subquotient.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Subquotient.lean#L238). The attribute's comment: “`Y → A/X` is strict; the case that is not formal from 05SJ”.

> Stacks 0129: `Y → A/X` is strict. This is the one claim with content: `Y → A/X` is the strict
> morphism `Y → A` (a strict monomorphism when `n` is) followed by the strict epimorphism
> `A → A/X`, and by Stacks 05SJ (1) such a composite need not be strict. Here it is, because it is
> also the strict epimorphism `Y → Y/X` followed by the strict (cartesian) morphism `Y/X → A/X`, to
> which Stacks 05SJ (3) applies (for a monomorphism `n` the latter is a strict monomorphism and
> 05SJ (2) applies as well). No hypothesis on `k`, `n`.

```lean
theorem isStrict_pullbackHom_comp_pushforwardHom :
    IsStrict (pullbackHom A n ≫ pushforwardHom A (cokernel.π (k ≫ n)))
```

## Tag 05SM, a lemma

[Tag 05SM](https://stacks.math.columbia.edu/tag/05SM) in the Stacks Project.

**`CategoryTheory.FilteredObject.isPushout_quot_map`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/GradedExact.lean, line 433](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/GradedExact.lean#L433). The attribute's comment: “the pushout is level-wise on the quotients by the steps, for any `I`”.

> Stacks 05SM, the pushout: `B ⊔_A D` exists in `Fil(𝒜)` (`hasFiniteColimits`) and its
> quotients by the steps are computed level-wise,
> `(B ⊔_A D)/F^i(B ⊔_A D) = B/F^iB ⊔_{A/F^iA} D/F^iD`, for any index category `I` and any additive
> `𝒜` with cokernels and strong epi images. (The steps themselves are not computed level-wise:
> `F^i(B ⊔_A D)` is the image of `F^iB ⊕ F^iD`.)

```lean
theorem isPushout_quot_map (i : I) :
    IsPushout ((quot i).map f) ((quot i).map g) ((quot i).map (pushout.inl f g))
      ((quot i).map (pushout.inr f g))
```

**`CategoryTheory.FilteredObject.hasFiniteColimits`**, an instance in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Limits.lean, line 355](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Limits.lean#L355). The attribute's comment: “the pushout exists, for any `I`, `𝒜` additive with cokernels and strong epi images”.

> `Fil(𝒜)` has all finite colimits; in particular the pushouts of Stacks 05SM exist.

```lean
noncomputable instance hasFiniteColimits [HasCokernels C] [HasImages C] [HasStrongEpiImages C] :
    HasFiniteColimits (FilteredObject C I)
```

**`CategoryTheory.FilteredObject.isStrict_pushout_inr`**, an instance in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Pushouts.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Pushouts.lean#L87). The attribute's comment: “if `f` is strict, so is its cobase change `f' : D ⟶ B ⊔_A D`, for any `I`”.

> Stacks 05SM: if `f : A ⟶ B` is strict, so is its cobase change `f' : D ⟶ B ⊔_A D` along
> any `g : A ⟶ D`. On the quotient by the step `i`, `Ker(D/F^iD ⟶ (B ⊔_A D)/F^i) = g_i(Ker f_i)`
> since the quotients of the pushout are computed level-wise and the kernel of a cobase change is
> the image of the kernel; by strictness `Ker f_i` is the image of `Ker f` in `A/F^iA`, so this is
> the image in `D/F^iD` of `g(Ker f) = Ker f'`, which is the strictness of `f'`.

```lean
instance isStrict_pushout_inr [IsStrict f] : IsStrict (pushout.inr f g)
```

**`CategoryTheory.FilteredObject.isStrict_pushout_inl`**, an instance in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Pushouts.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Pushouts.lean#L97). The attribute's comment: “if `g` is strict, so is its cobase change `g' : B ⟶ B ⊔_A D`, for any `I`”.

> Stacks 05SM, symmetrically: if `g : A ⟶ D` is strict, so is its cobase change
> `g' : B ⟶ B ⊔_A D` along any `f : A ⟶ B`.

```lean
instance isStrict_pushout_inl [IsStrict g] : IsStrict (pushout.inl f g)
```

## Tag 05SN, a lemma

[Tag 05SN](https://stacks.math.columbia.edu/tag/05SN) in the Stacks Project.

**`CategoryTheory.FilteredObject.hasFiniteLimits`**, an instance in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Limits.lean, line 346](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Limits.lean#L346). The attribute's comment: “the fibre product exists, for any `I` and any additive `𝒜` with kernels”.

> `Fil(𝒜)` has all finite limits when `𝒜` is preadditive with a zero object, binary
> biproducts and kernels; in particular the fibre products of Stacks 05SN exist.

```lean
noncomputable instance hasFiniteLimits [HasKernels C] : HasFiniteLimits (FilteredObject C I)
```

**`CategoryTheory.FilteredObject.isPullback_natTrans_app`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Limits.lean, line 439](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Limits.lean#L439). The attribute's comment: “the fibre product is level-wise, `F^i(B ×_A D) = F^iB ×_{F^iA} F^iD`, for any `I`”.

> Stacks 05SN, the fibre product: `B ×_A D` exists in `Fil(𝒜)` (`hasFiniteLimits`) and its
> filtration is computed level-wise, `F^i(B ×_A D) = F^iB ×_{F^iA} F^iD`, for any index category
> `I` and any additive `𝒜` with kernels.

```lean
theorem isPullback_natTrans_app (i : I) :
    IsPullback ((pullback.fst f g).natTrans.app i) ((pullback.snd f g).natTrans.app i)
      (f.natTrans.app i) (g.natTrans.app i)
```

**`CategoryTheory.FilteredObject.isStrict_pullback_snd`**, an instance in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Pullbacks.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Pullbacks.lean#L66). The attribute's comment: “if `f` is strict, so is its base change `f' : B ×_A D ⟶ D`, for any `I`”.

> Stacks 05SN: if `f : B ⟶ A` is strict, so is its base change `f' : B ×_A D ⟶ D` along any
> `g : D ⟶ A`.

```lean
instance isStrict_pullback_snd [IsStrict f] : IsStrict (pullback.snd f g)
```

**`CategoryTheory.FilteredObject.isStrict_pullback_fst`**, an instance in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Pullbacks.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Pullbacks.lean#L78). The attribute's comment: “if `g` is strict, so is its base change `g' : B ×_A D ⟶ B`, for any `I`”.

> Stacks 05SN, symmetrically: if `g : D ⟶ A` is strict, so is its base change
> `g' : B ×_A D ⟶ B` along any `f : B ⟶ A`.

```lean
instance isStrict_pullback_fst [IsStrict g] : IsStrict (pullback.fst f g)
```

## Tag 05SP, a lemma

[Tag 05SP](https://stacks.math.columbia.edu/tag/05SP) in the Stacks Project.

**`CategoryTheory.FilteredObject.shortExact_subQuotShortComplex_map_grMap`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/GradedExact.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/GradedExact.lean#L148). The attribute's comment: “(1), general: any short exact `0 → Y → A → Z → 0` of `𝒜`, `Y` induced, `Z` quotient”. References: EGA IV (19.6.1), “more general”.

> Stacks 05SP (1), general form: for a short exact sequence `0 → Y → A → Z → 0` of `𝒜` with `A`
> filtered, `Y` carrying the induced filtration and `Z` the quotient filtration, the sequence
> `0 → gr(Y) → gr(A) → gr(Z) → 0` of graded pieces along any index arrow is short exact.

```lean
theorem shortExact_subQuotShortComplex_map_grMap (hS : (ShortComplex.mk m e w).ShortExact)
    {i j : I} (f : i ⟶ j) :
    ((subQuotShortComplex A m e w).map (grMap f)).ShortExact
```

**`CategoryTheory.FilteredObject.shortExact_subQuotShortComplex_cokernel_map_grMap`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/GradedExact.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/GradedExact.lean#L167). The attribute's comment: “(1) literally: `X ⊆ A` induced, `A/X` quotient, along any index arrow”. References: EGA IV (19.6.1), “more general”.

> Stacks 05SP (1), literally: for `X ⊆ A` with the induced filtration and `A/X` with the
> quotient filtration, `0 → gr(X) → gr(A) → gr(A/X) → 0` is short exact, along any index arrow.

```lean
theorem shortExact_subQuotShortComplex_cokernel_map_grMap (A : FilteredObject C I) {Y : C}
    (m : Y ⟶ A.X) [Mono m] {i j : I} (f : i ⟶ j) :
    ((subQuotShortComplex A m (cokernel.π m) (cokernel.condition m)).map (grMap f)).ShortExact
```

**`CategoryTheory.FilteredObject.shortExact_map_grMap`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/GradedExact.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/GradedExact.lean#L194). The attribute's comment: “(1) in `Fil(𝒜)`: a short exact sequence of `𝒜` with strict morphisms, any arrow”. References: EGA IV (19.6.1), “rows of (19.6.1.1)”.

> Stacks 05SP (1), intrinsically in `Fil(𝒜)`: if `0 → X → A → Q → 0` is a short exact sequence
> of `𝒜` whose two morphisms are strict morphisms of filtered objects (equivalently, `X` has the
> induced and `Q` the quotient filtration, Stacks 0124), then `0 → gr(X) → gr(A) → gr(Q) → 0` is
> short exact, along any index arrow.

```lean
theorem shortExact_map_grMap (hS : (S.map forget).ShortExact) [IsStrict S.f] [IsStrict S.g]
    {i j : I} (f : i ⟶ j) : (S.map (grMap f)).ShortExact
```

**`CategoryTheory.FilteredObject.shortExact_map_grMap_kernel_ι_coimage_π`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/GradedExact.lean, line 257](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/GradedExact.lean#L257). The attribute's comment: “(2) `0 → gr(Ker f) → gr(A) → gr(Coim f) → 0`, any `f`, along any index arrow”.

> Stacks 05SP (2), first sequence: `0 → gr(Ker f) → gr(A) → gr(Coim f) → 0` is short exact, for
> any morphism `f` of filtered objects, on Mathlib's kernel and coimage computed in `Fil(𝒜)`.

```lean
theorem shortExact_map_grMap_kernel_ι_coimage_π {i j : I} (φ : i ⟶ j) :
    ((ShortComplex.mk (kernel.ι f) (Abelian.coimage.π f) (cokernel.condition _)).map
      (grMap φ)).ShortExact
```

**`CategoryTheory.FilteredObject.shortExact_map_grMap_image_ι_cokernel_π`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/GradedExact.lean, line 265](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/GradedExact.lean#L265). The attribute's comment: “(2) `0 → gr(Im f) → gr(B) → gr(Coker f) → 0`, any `f`, along any index arrow”.

> Stacks 05SP (2), second sequence: `0 → gr(Im f) → gr(B) → gr(Coker f) → 0` is short exact, for
> any morphism `f` of filtered objects, on Mathlib's image and cokernel computed in `Fil(𝒜)`.

```lean
theorem shortExact_map_grMap_image_ι_cokernel_π {i j : I} (φ : i ⟶ j) :
    ((ShortComplex.mk (Abelian.image.ι f) (cokernel.π f) (kernel.condition _)).map
      (grMap φ)).ShortExact
```

## Tag 0127, a lemma

[Tag 0127](https://stacks.math.columbia.edu/tag/0127) in the Stacks Project.

**`CategoryTheory.FilteredObject.isStrict_iff_forall_exact_gr_kernel_ι`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/GradedStrict.lean, line 333](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/GradedStrict.lean#L333). The attribute's comment: “(1) ⇔ (4); needs only a top step of `A`”.

> Stacks 0127, (1) ⇔ (4): `f` is strict iff `gr(Ker f) → gr(A) → gr(B)` is exact, when `A` has a
> top step.

```lean
theorem isStrict_iff_forall_exact_gr_kernel_ι [HasTopStep A.filtration] :
    IsStrict f ↔ ∀ p, ((ShortComplex.mk (kernel.ι f) f (kernel.condition f)).map (gr p)).Exact
```

**`CategoryTheory.FilteredObject.isStrict_iff_forall_exact_gr_cokernel_π`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/GradedStrict.lean, line 342](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/GradedStrict.lean#L342). The attribute's comment: “(1) ⇔ (5); needs only a zero step of `B`”.

> Stacks 0127, (1) ⇔ (5): `f` is strict iff `gr(A) → gr(B) → gr(Coker f)` is exact, when `B` has
> a zero step.

```lean
theorem isStrict_iff_forall_exact_gr_cokernel_π [HasBotStep B.filtration] :
    IsStrict f ↔
      ∀ p, ((ShortComplex.mk f (cokernel.π f) (cokernel.condition f)).map (gr p)).Exact
```

**`CategoryTheory.FilteredObject.isStrict_iff_forall_isIso_gr_of_hasTopStep`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/GradedStrict.lean, line 352](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/GradedStrict.lean#L352). The attribute's comment: “(1) ⇔ (3), under a top step of `A`”.

> Stacks 0127, (1) ⇔ (3): `f` is strict iff `gr^p(Coim f) → gr^p(Im f)` is an isomorphism for all
> `p`, when `A` has a top step.

```lean
theorem isStrict_iff_forall_isIso_gr_of_hasTopStep [HasTopStep A.filtration] :
    IsStrict f ↔ ∀ p, IsIso ((gr p).map (Abelian.coimageImageComparison f))
```

**`CategoryTheory.FilteredObject.isStrict_iff_forall_isIso_gr_of_hasBotStep`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/GradedStrict.lean, line 361](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/GradedStrict.lean#L361). The attribute's comment: “(1) ⇔ (3), under a zero step of `B`”.

> Stacks 0127, (1) ⇔ (3): `f` is strict iff `gr^p(Coim f) → gr^p(Im f)` is an isomorphism for all
> `p`, when `B` has a zero step.

```lean
theorem isStrict_iff_forall_isIso_gr_of_hasBotStep [HasBotStep B.filtration] :
    IsStrict f ↔ ∀ p, IsIso ((gr p).map (Abelian.coimageImageComparison f))
```

**`CategoryTheory.FilteredObject.isStrict_iff_forall_exact_gr_kernel_ι_cokernel_π_of_hasTopStep`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/GradedStrict.lean, line 370](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/GradedStrict.lean#L370). The attribute's comment: “(1) ⇔ (6), under a top step of `A`”.

> Stacks 0127, (1) ⇔ (6): `f` is strict iff `0 → gr(Ker f) → gr(A) → gr(B) → gr(Coker f) → 0` is
> exact, when `A` has a top step.

```lean
theorem isStrict_iff_forall_exact_gr_kernel_ι_cokernel_π_of_hasTopStep [HasTopStep A.filtration] :
    IsStrict f ↔ ∀ p, (ComposableArrows.mk₃ ((gr p).map (kernel.ι f)) ((gr p).map f)
        ((gr p).map (cokernel.π f))).Exact ∧ Mono ((gr p).map (kernel.ι f)) ∧
        Epi ((gr p).map (cokernel.π f))
```

**`CategoryTheory.FilteredObject.isStrict_iff_forall_exact_gr_kernel_ι_cokernel_π_of_hasBotStep`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/GradedStrict.lean, line 380](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/GradedStrict.lean#L380). The attribute's comment: “(1) ⇔ (6), under a zero step of `B`”.

> Stacks 0127, (1) ⇔ (6): `f` is strict iff `0 → gr(Ker f) → gr(A) → gr(B) → gr(Coker f) → 0` is
> exact, when `B` has a zero step.

```lean
theorem isStrict_iff_forall_exact_gr_kernel_ι_cokernel_π_of_hasBotStep [HasBotStep B.filtration] :
    IsStrict f ↔ ∀ p, (ComposableArrows.mk₃ ((gr p).map (kernel.ι f)) ((gr p).map f)
        ((gr p).map (cokernel.π f))).Exact ∧ Mono ((gr p).map (kernel.ι f)) ∧
        Epi ((gr p).map (cokernel.π f))
```

**`CategoryTheory.FilteredObject.isStrict_tfae`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/GradedStrict.lean, line 393](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/GradedStrict.lean#L393). The attribute's comment: “for `A` with a top step and `B` with a zero step; in particular finite filtrations”.

> Stacks 0127: for `f : A ⟶ B` with `A` having a top step and `B` a zero step (in particular
> for finite filtrations), the following are equivalent: (1) `f` is strict; (2) `Coim f → Im f` is an
> isomorphism in `Fil(𝒜)`; (3) `gr(Coim f) → gr(Im f)` is an isomorphism; (4) `gr(Ker f) → gr(A) →
> gr(B)` is exact; (5) `gr(A) → gr(B) → gr(Coker f)` is exact; (6) `0 → gr(Ker f) → gr(A) → gr(B) →
> gr(Coker f) → 0` is exact.

```lean
theorem isStrict_tfae [HasTopStep A.filtration] [HasBotStep B.filtration] :
    [IsStrict f,
      IsIso (Abelian.coimageImageComparison f),
      ∀ p, IsIso ((gr p).map (Abelian.coimageImageComparison f)),
      ∀ p, ((ShortComplex.mk (kernel.ι f) f (kernel.condition f)).map (gr p)).Exact,
      ∀ p, ((ShortComplex.mk f (cokernel.π f) (cokernel.condition f)).map (gr p)).Exact,
      ∀ p, (ComposableArrows.mk₃ ((gr p).map (kernel.ι f)) ((gr p).map f)
        ((gr p).map (cokernel.π f))).Exact ∧ Mono ((gr p).map (kernel.ι f)) ∧
        Epi ((gr p).map (cokernel.π f))].TFAE
```

## Tag 0128, a lemma

[Tag 0128](https://stacks.math.columbia.edu/tag/0128) in the Stacks Project.

**`CategoryTheory.FilteredObject.preservesLeftHomologyOf_grMap`**, an instance in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Homology.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Homology.lean#L225). The attribute's comment: “`gr_φ` preserves the left homology of a complex of strict morphisms; any `φ`, `I`”.

> Stacks 0128, abstract form: for a complex `S` of strict morphisms, `gr_φ` preserves the left
> homology of `S`, along any index arrow `φ`: it preserves the kernel of the strict `β`
> (`preservesLimit_parallelPair_grMap_of_isStrict`) and the cokernel of `A ⟶ Ker β`, strict because
> `α` is (`preservesColimit_parallelPair_grMap_of_isStrict`), i.e. the left homology data
> `homologyObjLeftHomologyData S`.

```lean
instance preservesLeftHomologyOf_grMap [IsStrict S.f] [IsStrict S.g] :
    (grMap φ).PreservesLeftHomologyOf S
```

**`CategoryTheory.FilteredObject.grMapHomologyIso`**, a def in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Homology.lean, line 270](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Homology.lean#L270). The attribute's comment: “`gr(Ker β / Im α) = Ker(gr β) / Im(gr α)`, along any index arrow, any `I`”.

> Stacks 0128: `gr_φ(Ker β / Im α) ≅ Ker(gr_φ β) / Im(gr_φ α)`, along any index arrow, for any
> index category; the right-hand side is Mathlib's homology of the short complex `gr_φ(S)`.

```lean
noncomputable def grMapHomologyIso [IsStrict S.f] [IsStrict S.g] :
    (grMap φ).obj (homologyObj S) ≅ (S.map (grMap φ)).homology
```

**`CategoryTheory.FilteredObject.grHomologyIso`**, a def in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Homology.lean, line 307](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Homology.lean#L307). The attribute's comment: “in Stacks' indexing, `gr^p(Ker β / Im α) = Ker(gr^p β) / Im(gr^p α)`”.

> Stacks 0128 in Stacks' indexing: `gr^p(Ker β / Im α) ≅ Ker(gr^p β) / Im(gr^p α)` for every
> `p`, for a complex of filtered objects over `ℤᵒᵖ` with `α`, `β` strict.

```lean
noncomputable def grHomologyIso (p : ℤ) :
    (gr p).obj (homologyObj S) ≅ (S.map (gr p)).homology
```

**`CategoryTheory.FilteredObject.grGradedHomologyIso`**, a def in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/Homology.lean, line 315](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Homology.lean#L315). The attribute's comment: “in `Gr(𝒜)`: `gr(Ker β / Im α) = Ker(gr β) / Im(gr α)` as graded objects”.

> Stacks 0128 in `Gr(𝒜)`: `gr(Ker β / Im α) ≅ Ker(gr β) / Im(gr α)` as graded objects, the
> right-hand side being the homology of `gr(S)` in `Gr(𝒜)` (computed degreewise, as the exact
> functor `GradedObject.eval p` preserves homology).

```lean
noncomputable def grGradedHomologyIso :
    grGraded.obj (homologyObj S) ≅ (S.map grGraded).homology
```

## Tag 05QH, a lemma

[Tag 05QH](https://stacks.math.columbia.edu/tag/05QH) in the Stacks Project.

**`CategoryTheory.FilteredObject.exact_map_eval_of_exact_map_gr`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/GradedReflectsExact.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/GradedReflectsExact.lean#L82). The attribute's comment: “(2); needs only a zero step of `B`”.

> Stacks 05QH (2): if `gr(A) → gr(B) → gr(C)` is exact then `F^pA → F^pB → F^pC` is exact for
> every `p`; needs only a zero step of `B`.

```lean
theorem exact_map_eval_of_exact_map_gr (hS : ∀ p, (S.map (gr p)).Exact)
    [HasBotStep S.X₂.filtration] (p : ℤ) : (S.map (eval (op p))).Exact
```

**`CategoryTheory.FilteredObject.exact_map_quot_of_exact_map_gr`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/GradedReflectsExact.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/GradedReflectsExact.lean#L90). The attribute's comment: “(3); needs only a top step of `B`”.

> Stacks 05QH (3): if `gr(A) → gr(B) → gr(C)` is exact then `A/F^pA → B/F^pB → C/F^pC` is
> exact for every `p`; needs only a top step of `B`.

```lean
theorem exact_map_quot_of_exact_map_gr (hS : ∀ p, (S.map (gr p)).Exact)
    [HasTopStep S.X₂.filtration] (p : ℤ) : (S.map (quot (op p))).Exact
```

**`CategoryTheory.FilteredObject.exact_map_forget_of_exact_map_gr`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/GradedReflectsExact.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/GradedReflectsExact.lean#L98). The attribute's comment: “(5); needs only a finite filtration on `B`”.

> Stacks 05QH (5): if `gr(A) → gr(B) → gr(C)` is exact then `A → B → C` is exact in `𝒜`; needs
> only a finite filtration on `B`.

```lean
theorem exact_map_forget_of_exact_map_gr (hS : ∀ p, (S.map (gr p)).Exact)
    [HasTopStep S.X₂.filtration] [HasBotStep S.X₂.filtration] : (S.map forget).Exact
```

**`CategoryTheory.FilteredObject.isStrict_f_of_exact_map_gr`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/GradedReflectsExact.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/GradedReflectsExact.lean#L116). The attribute's comment: “(4) for `A → B`; needs only a zero step of `B`”.

> Stacks 05QH (4) for `A → B`: if `gr(A) → gr(B) → gr(C)` is exact then `A → B` is strict; needs
> only a zero step of `B`.

```lean
theorem isStrict_f_of_exact_map_gr (hS : ∀ p, (S.map (gr p)).Exact)
    [HasBotStep S.X₂.filtration] : IsStrict S.f
```

**`CategoryTheory.FilteredObject.isStrict_g_of_exact_map_gr`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/GradedReflectsExact.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/GradedReflectsExact.lean#L133). The attribute's comment: “(4) for `B → C`; needs only a top step of `B`”.

> Stacks 05QH (4) for `B → C`: if `gr(A) → gr(B) → gr(C)` is exact then `B → C` is strict; needs
> only a top step of `B`.

```lean
theorem isStrict_g_of_exact_map_gr (hS : ∀ p, (S.map (gr p)).Exact)
    [HasTopStep S.X₂.filtration] : IsStrict S.g
```

**`CategoryTheory.FilteredObject.exact_of_exact_map_grGraded`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/GradedReflectsExact.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/GradedReflectsExact.lean#L143). The attribute's comment: “needs only a finite filtration on `B`; `A` and `C` are arbitrary”.

> Stacks 05QH: let `A → B → C` be a complex of filtered objects of an abelian category with
> `gr(A) → gr(B) → gr(C)` exact and `B` finitely filtered (Stacks assumes `A`, `B`, `C` finite).
> Then (1) `gr^p(A) → gr^p(B) → gr^p(C)` is exact for every `p`, (2) `F^pA → F^pB → F^pC` is
> exact for every `p`, (3) `A/F^pA → B/F^pB → C/F^pC` is exact for every `p`, (4) `A → B` and
> `B → C` are strict, and (5) `A → B → C` is exact in `𝒜`.

```lean
theorem exact_of_exact_map_grGraded [IsFinite S.X₂.filtration] (hS : (S.map grGraded).Exact) :
    (∀ p, (S.map (gr p)).Exact) ∧ (∀ p, (S.map (eval (op p))).Exact) ∧
      (∀ p, (S.map (quot (op p))).Exact) ∧ (IsStrict S.f ∧ IsStrict S.g) ∧
      (S.map forget).Exact
```

**`CategoryTheory.FilteredObject.exact_map_grGraded_iff`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Filtration/GradedStrict.lean, line 433](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/GradedStrict.lean#L433). The attribute's comment: “(1): exactness of `gr(A) → gr(B) → gr(C)` is exactness of every `gr^p`”.

> Exactness in `Gr(𝒜)` of `gr` applied to a short complex is exactness of every `gr^p`.

```lean
lemma exact_map_grGraded_iff (S : ShortComplex (FilteredObject C ℤᵒᵖ)) :
    (S.map grGraded).Exact ↔ ∀ p, (S.map (gr p)).Exact
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 12.19, Tag 0120](https://stacks.math.columbia.edu/tag/0120)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
