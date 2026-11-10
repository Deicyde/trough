---
declaration: section
origin: cited
lean: CategoryTheory.DerivedCategory.Ext, CategoryTheory.Abelian.zExt, DerivedCategory.surjective_extZero_comp_iff_surjective_comp, ExtByResolutions.ext_via_injective_resolution_bijective, ExtByResolutions.ext_via_projective_resolution_bijective, DerivedCategory.bijective_homologyFunctor_shiftMap_of_isLE_of_isGE, CategoryTheory.Abelian.YonedaExtension, CategoryTheory.Abelian.YonedaExtension.Equivalent
statement: formalized
proof: formalized
---

# 13.27 Ext groups

Section 13.27 of the Stacks Project, [Tag 06XP](https://stacks.math.columbia.edu/tag/06XP). 10 tags here are carried by 19 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06XQ, a definition

[Tag 06XQ](https://stacks.math.columbia.edu/tag/06XQ) in the Stacks Project.

**`CategoryTheory.DerivedCategory.Ext`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Ext/Basic/ExtAndYonedaExtensions.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Ext/Basic/ExtAndYonedaExtensions.lean#L51). References: SGA 4½ Etat 0 (3.2.1).

> The `i`-th extension group `Ext^i_𝒜(X, Y) = Hom_{D(𝒜)}(X, Y⟦i⟧)` of an object `X` of the
> derived category `D(𝒜)` of an abelian category `𝒜` by an object `Y`, for `i : ℤ`. It is
> canonically identified with `Hom_{D(𝒜)}(X⟦-i⟧, Y)` via the adjunction between the shifts
> `⟦-i⟧ ⊣ ⟦i⟧`.

```lean
public noncomputable abbrev DerivedCategory.Ext (X Y : DerivedCategory C) (i : ℤ) : Type _
```

**`CategoryTheory.Abelian.zExt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Ext/Basic/ExtAndYonedaExtensions.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Ext/Basic/ExtAndYonedaExtensions.lean#L59). References: SGA 4½ Etat 0 (3.2.1), “degree-0 objects”.

> The `i`-th extension group `Ext^i_𝒜(A, B) = Ext^i_𝒜(A[0], B[0])` of an object `A` of an
> abelian category `𝒜` by an object `B`, for `i : ℤ`, where `A[0]` is the image of `A` under
> `𝒜 ⥤ D(𝒜)`, the complex concentrated in degree `0`. For `i = (n : ℕ)` this is Mathlib's
> `CategoryTheory.Abelian.Ext A B n`, up to the equivalence `Abelian.Ext.homEquiv`.

```lean
public noncomputable abbrev Abelian.zExt (A B : C) (i : ℤ) : Type _
```

**`DerivedCategory.surjective_extZero_comp_iff_surjective_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Ext/ZeroDegree.lean, line 40](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Ext/ZeroDegree.lean#L40). The attribute's comment: “degree zero”.

> Precomposition with `ξ` is surjective on degree-zero `Ext` groups into `Y` exactly when it
> is surjective on morphisms into `Y`. In degree `0` an `Ext` class *is* a morphism, by
> `CategoryTheory.ShiftedHom.homEquiv`, and the identification commutes with precomposition.

```lean
public theorem surjective_extZero_comp_iff_surjective_comp
    {E X : DerivedCategory C} (ξ : E ⟶ X) (Y : DerivedCategory C) :
    Function.Surjective (fun α : DerivedCategory.Ext X Y 0 => ξ ≫ α) ↔
      Function.Surjective (fun f : X ⟶ Y => ξ ≫ f)
```

## Tag 06XR, a lemma

[Tag 06XR](https://stacks.math.columbia.edu/tag/06XR) in the Stacks Project.

**`ExtByResolutions.ext_via_injective_resolution_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Ext/Basic/SplittingAndResolutions.lean, line 681](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Ext/Basic/SplittingAndResolutions.lean#L681). The attribute's comment: “(1)”.

> Statement 1 (Stacks 06XR, part 1): computing Ext via an injective resolution.
> Given an injective resolution `f : Y ⟶ I` (Definition 2), the canonical map
> `canMapOfInjectiveResolution` (induced by `f`) is a bijection
>   `Hom_{K(A)}(X, I[i]) → Hom_{D(A)}(Q(X), Q(Y)[i])`.
> This is the canonical identification
>   `Ext^i_A(X, Y) = Hom_{D(A)}(Q(X), Q(Y)[i]) ≅ Hom_{K(A)}(X, I[i])`.

```lean
theorem ext_via_injective_resolution_bijective
    (X Y I : CochainComplex C ℤ) (i : ℤ)
    {f : Y ⟶ I} (hf : IsInjectiveResolution f) :
    haveI := hf.quasiIso
    Function.Bijective (canMapOfInjectiveResolution X Y I i f)
```

**`ExtByResolutions.ext_via_projective_resolution_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Ext/Basic/SplittingAndResolutions.lean, line 724](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Ext/Basic/SplittingAndResolutions.lean#L724). The attribute's comment: “(2)”.

> Statement 2 (Stacks 06XR, part 2): computing Ext via a projective resolution.
> Given a projective resolution `g : P ⟶ X` (Definition 3), the canonical map
> `canMapOfProjectiveResolution` (induced by `g`) is a bijection
>   `Hom_{K(A)}(P[-i], Y) → Hom_{D(A)}(Q(X), Q(Y)[i])`.
> This is the canonical identification
>   `Ext^i_A(X, Y) = Hom_{D(A)}(Q(X), Q(Y)[i]) ≅ Hom_{K(A)}(P[-i], Y)`.

```lean
theorem ext_via_projective_resolution_bijective
    (X Y P : CochainComplex C ℤ) (i : ℤ)
    {g : P ⟶ X} (hg : IsProjectiveResolution g) :
    haveI := hg.quasiIso
    Function.Bijective (canMapOfProjectiveResolution X Y P i g)
```

## Tag 06XS, a lemma

[Tag 06XS](https://stacks.math.columbia.edu/tag/06XS) in the Stacks Project.

**`DerivedCategory.bijective_homologyFunctor_shiftMap_of_isLE_of_isGE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Ext/Basic/ExtOneAndVanishing.lean, line 571](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Ext/Basic/ExtOneAndVanishing.lean#L571).

> Let `𝒜` be an abelian category and let `X`, `Y` be objects of `D(𝒜)` such that
> `H^i(X) = 0` for `i > a` and `H^j(Y) = 0` for `j < b`. If `n + a = a'` and `a' ≤ b`, then taking
> homology in degree `a`,
> `Ext^n_𝒜(X, Y) = Hom_{D(𝒜)}(X, Y⟦n⟧) → Hom_𝒜(H^a(X), H^{a'}(Y))`,
> is bijective. For `a' < b` the target is the zero group, so this says that
> `Ext^n_𝒜(X, Y) = 0` for `n < b - a`; for `a' = b` it is the identification
> `Ext^{b - a}_𝒜(X, Y) = Hom_𝒜(H^a(X), H^b(Y))`.

```lean
public theorem bijective_homologyFunctor_shiftMap_of_isLE_of_isGE
    (X Y : DerivedCategory C) (a b n a' : ℤ) [X.IsLE a] [Y.IsGE b]
    (ha' : n + a = a') (hab : a' ≤ b) :
    Function.Bijective (fun f : DerivedCategory.Ext X Y n ↦
      ((homologyFunctor C 0).shiftMap f a a' ha' :
        (homologyFunctor C a).obj X ⟶ (homologyFunctor C a').obj Y))
```

## Tag 06XT, a definition

[Tag 06XT](https://stacks.math.columbia.edu/tag/06XT) in the Stacks Project.

**`CategoryTheory.Abelian.YonedaExtension`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Ext/Basic/ExtAndYonedaExtensions.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Ext/Basic/ExtAndYonedaExtensions.lean#L82).

> A *degree `n + 1` Yoneda extension of `B` by `A`* in an abelian category `𝒜` is an exact
> sequence `0 → A → Z_n → Z_{n - 1} → ⋯ → Z_0 → B → 0` in `𝒜`. It is given by the sequence
> `Z : Fin (n + 1) ⥤ 𝒜` of its middle terms, `Z.obj' k = Z_{n - k}`, together with the outer
> maps `f : A ⟶ Z.left = Z_n` and `g : Z.right = Z_0 ⟶ B`, and by the exactness of the sequence
> at each of `A`, `Z_n, …, Z_0` and `B`. For `n = 0` this is a short exact sequence
> `0 → A → Z_0 → B → 0`.

```lean
public structure YonedaExtension (B A : 𝒜) (n : ℕ)
```

**`CategoryTheory.Abelian.YonedaExtension.Equivalent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Ext/Basic/ExtAndYonedaExtensions.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Ext/Basic/ExtAndYonedaExtensions.lean#L109).

> Two degree `n + 1` Yoneda extensions `E`, `E'` of `B` by `A` in an abelian category are
> *equivalent* if there exists a degree `n + 1` Yoneda extension `E''` of `B` by `A` and maps
> `φ : E''.Z ⟶ E.Z` and `ψ : E''.Z ⟶ E'.Z` of the middle terms which are compatible with the
> maps from `A` and the maps to `B`, i.e. such that the two diagrams obtained by putting `E''`
> between `E` and `E'` commute, with the identity on `A` and on `B`.

```lean
public def YonedaExtension.Equivalent (E E' : YonedaExtension B A n) : Prop
```

## Tag 06XU, a lemma

[Tag 06XU](https://stacks.math.columbia.edu/tag/06XU) in the Stacks Project.

**`CategoryTheory.Abelian.eq_of_isExtClassMap`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Ext/Basic/YonedaClassMap.lean, line 422](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Ext/Basic/YonedaClassMap.lean#L422). The attribute's comment: “uniqueness of the class map”.

> There is at most one class map: the degree `1` values are prescribed, and cutting an
> extension at its left end computes the value in degree `n + 2` from a value in degree `n + 1`.

```lean
lemma eq_of_isExtClassMap
    (δ₁ δ₂ : ∀ (B A : 𝒜) (n : ℕ), YonedaExtension B A n → Ext.{w} B A (n + 1))
    (h₁ : IsExtClassMap δ₁) (h₂ : IsExtClassMap δ₂) : δ₁ = δ₂
```

**`CategoryTheory.Abelian.extClassMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Ext/Basic/YonedaClassMap.lean, line 442](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Ext/Basic/YonedaClassMap.lean#L442). The attribute's comment: “the class map δ itself; `isExtClassMap_extClassMap` is its two defining properties and `eq_of_isExtClassMap` their uniqueness”. References: EGA 0 (12.3.2), “canonical map δ”.

> **The class of a Yoneda extension.** It is defined by recursion on the degree: in degree `1`
> it is the class `CategoryTheory.ShortComplex.ShortExact.extClass` of the short exact sequence
> the extension is, and in degree `n + 2` it is the class of the extension cut at its left end
> (`cut`) composed with the class of the cutting short exact sequence
> (`shortExact_cut`). It is the unique such map: `isExtClassMap_extClassMap` is the pair of
> properties and `eq_of_isExtClassMap` their uniqueness.

```lean
noncomputable def extClassMap {B : 𝒜} :
    ∀ (n : ℕ) {A : 𝒜}, YonedaExtension B A n → Ext.{w} B A (n + 1)
```

**`CategoryTheory.Abelian.extClassMap_eq_of_equivalent`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Ext/Basic/YonedaClassMap.lean, line 489](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Ext/Basic/YonedaClassMap.lean#L489). The attribute's comment: “equivalent Yoneda extensions have the same class”. References: EGA 0 (12.3.2), “E~E' ⇒ δE=δE'”; SGA 7 VII (3.2), “c(X, special case”.

> Equivalent Yoneda extensions have the same class.

```lean
lemma extClassMap_eq_of_equivalent {B A : 𝒜} {n : ℕ} {E E' : YonedaExtension B A n}
    (h : E.Equivalent E') : extClassMap n E = extClassMap n E'
```

**`CategoryTheory.Abelian.isExtClassMap_extClassMap`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Ext/Basic/YonedaClassMap.lean, line 523](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Ext/Basic/YonedaClassMap.lean#L523). The attribute's comment: “the two defining properties of the class map”.

> The class map has the two properties which pin it down.

```lean
lemma isExtClassMap_extClassMap :
    IsExtClassMap (fun (_ _ : 𝒜) (n : ℕ) (E : YonedaExtension _ _ n) => extClassMap.{w} n E)
```

**`CategoryTheory.Abelian.surjective_extClassMap`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Ext/Basic/YonedaClassMap.lean, line 608](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Ext/Basic/YonedaClassMap.lean#L608). The attribute's comment: “every element of `Ext^{n + 1}` is the class of a degree `n + 1` Yoneda extension”. References: EGA 0 (12.3.2), “surjectivity of δ”; SGA 7 VII (3.2.5), “partial”.

> **The class map is surjective**: every element of `Ext^{n + 1}_𝒜(B, A)` is the class of a
> degree `n + 1` Yoneda extension of `B` by `A`. The induction is on the degree: an element `ξ`
> of `Ext^{n + 1}_𝒜(B, A)` is killed by a monomorphism `A ⟶ Z`
> (`exists_shortExact_comp_mk₀_eq_zero`), hence, by the covariant long exact
> sequence of the short exact sequence `S : 0 → A → Z → C → 0`, of the form
> `ξ = η ∘ δ(S)` with `η ∈ Ext^n_𝒜(B, C)`. For `n ≥ 1` the inductive hypothesis writes
> `η = δ(E')` for a degree `n` extension `E'` of `B` by `C`, and `E'` spliced with `S` is an
> extension of class `ξ` (`extClassMap_splice`). For `n = 0`, `η` is a map
> `u : B ⟶ C` and the pullback of `S` along `u` is a short exact sequence
> `0 → A → Z ×_C B → B → 0` of class `ξ`, by naturality of
> `CategoryTheory.ShortComplex.ShortExact.extClass`.

```lean
lemma surjective_extClassMap (B A : 𝒜) (n : ℕ) :
    Function.Surjective (fun E : YonedaExtension B A n => extClassMap.{w} n E)
```

**`CategoryTheory.Abelian.equivalent_of_extClassMap_eq`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Ext/Basic/YonedaClassMap.lean, line 880](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Ext/Basic/YonedaClassMap.lean#L880). The attribute's comment: “Yoneda extensions of the same degree with the same class are equivalent”. References: EGA 0 (12.3.2), “δE=δE' ⇒ E~E'”.

> Two Yoneda extensions of the same degree with the same class are equivalent.

```lean
lemma equivalent_of_extClassMap_eq {B A : 𝒜} {n : ℕ} (E E' : YonedaExtension B A n)
    (h : extClassMap.{w} n E = extClassMap.{w} n E') : E.Equivalent E'
```

## Tag 06XV, a lemma

[Tag 06XV](https://stacks.math.columbia.edu/tag/06XV) in the Stacks Project.

**`CategoryTheory.Abelian.Ext.extClass_surjective_and_eq_iff_iso_and_baerSum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Ext/Basic/ExtOneAndVanishing.lean, line 247](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Ext/Basic/ExtOneAndVanishing.lean#L247). References: EGA 0 (12.3.2); SGA 7 VII (3.2.5), “partial”.

> **`Ext^1` is the Ext-group of extensions.** Let `𝒜` be an abelian category and let `A`, `B`
> be objects of `𝒜`. The class `δ(E) ∈ Ext^1_𝒜(B, A)` of an extension
> `E : 0 → A → E → B → 0` of `B` by `A`, i.e. Mathlib's
> `CategoryTheory.ShortComplex.ShortExact.extClass`, has the following three properties:
>
> * every element of `Ext^1_𝒜(B, A)` is the class of an extension of `B` by `A`;
> * two extensions of `B` by `A` have the same class if and only if they are isomorphic, i.e.
>   there is an isomorphism of their middle terms compatible with the maps from `A` and to `B`;
> * the class of a Baer sum is the sum of the classes: if `0 → A → T → B ⊕ B → 0` is an
>   extension receiving a morphism from the direct sum extension
>   `0 → A ⊕ A → E₁ ⊕ E₂ → B ⊕ B → 0` over the sum map `Σ : A ⊕ A → A`, and if
>   `0 → A → E → B → 0` maps to it over the diagonal `Δ : B → B ⊕ B`, then
>   `δ(E) = δ(E₁) + δ(E₂)`.
>
> Hence `δ` induces an isomorphism from the Ext-group `Ext_𝒜(B, A)` of isomorphism classes of
> extensions of `B` by `A` under Baer sum onto the group `Ext^1_𝒜(B, A)`.

```lean
public theorem Ext.extClass_surjective_and_eq_iff_iso_and_baerSum (B A : 𝒜) :
    (∀ x : Ext.{w} B A 1, ∃ (E : 𝒜) (i : A ⟶ E) (p : E ⟶ B) (w : i ≫ p = 0)
        (h : (ShortComplex.mk i p w).ShortExact), h.extClass = x) ∧
    (∀ (E E' : 𝒜) (i : A ⟶ E) (p : E ⟶ B) (w : i ≫ p = 0) (i' : A ⟶ E') (p' : E' ⟶ B)
        (w' : i' ≫ p' = 0) (h : (ShortComplex.mk i p w).ShortExact)
        (h' : (ShortComplex.mk i' p' w').ShortExact),
        h.extClass = h'.extClass ↔ ∃ φ : E ≅ E', i ≫ φ.hom = i' ∧ φ.hom ≫ p' = p) ∧
    (∀ (E₁ E₂ E T : 𝒜) (i₁ : A ⟶ E₁) (p₁ : E₁ ⟶ B) (w₁ : i₁ ≫ p₁ = 0)
        (i₂ : A ⟶ E₂) (p₂ : E₂ ⟶ B) (w₂ : i₂ ≫ p₂ = 0)
        (i : A ⟶ E) (p : E ⟶ B) (w : i ≫ p = 0)
        (j : A ⟶ T) (q : T ⟶ B ⊞ B) (wT : j ≫ q = 0)
        (h₁ : (ShortComplex.mk i₁ p₁ w₁).ShortExact)
        (h₂ : (ShortComplex.mk i₂ p₂ w₂).ShortExact)
        (h : (ShortComplex.mk i p w).ShortExact)
        (_hT : (ShortComplex.mk j q wT).ShortExact)
        (u : E₁ ⊞ E₂ ⟶ T) (v : E ⟶ T),
        biprod.map i₁ i₂ ≫ u = biprod.desc (𝟙 A) (𝟙 A) ≫ j →
        u ≫ q = biprod.map p₁ p₂ →
        i ≫ v = j → v ≫ q = p ≫ biprod.lift (𝟙 B) (𝟙 B) →
          h.extClass = h₁.extClass + h₂.extClass)
```

## Tag 0GSM, a lemma

[Tag 0GSM](https://stacks.math.columbia.edu/tag/0GSM) in the Stacks Project.

**`CategoryTheory.ShortComplex.ShortExact.extClass_comp_extClass_eq_zero_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Ext/Basic/ExtOneAndVanishing.lean, line 432](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Ext/Basic/ExtOneAndVanishing.lean#L432).

> **Vanishing of a Yoneda product of two extension classes.** Let `0 → A → Z → B → 0` and
> `0 → B → Z' → C → 0` be short exact sequences in an abelian category `𝒜`, with classes
> `[Z] ∈ Ext^1_𝒜(B, A)` and `[Z'] ∈ Ext^1_𝒜(C, B)`. Then the Yoneda product
> `[Z] ∘ [Z'] ∈ Ext^2_𝒜(C, A)` is zero if and only if there is a commutative diagram with exact
> rows and columns
>
> ```
>                  0             0
>                  ↓             ↓
>   0 →   A   →    Z     →       B      →  0
>       ‖ 1 ‖      ↓             ↓
>   0 →   A   →    W     →       Z'     →  0
>                  ↓             ↓
>                  C   → ‖ 1 ‖ → C
>                  ↓             ↓
>                  0             0
> ```
>
> in `𝒜`, i.e. if and only if `0 → A → Z → B → 0` is the restriction along `B → Z'` of an
> extension `0 → A → W → Z' → 0` of `Z'` by `A`.

```lean
public theorem extClass_comp_extClass_eq_zero_iff {A Z B Z' C : 𝒜}
    {f : A ⟶ Z} {g : Z ⟶ B} {hfg : f ≫ g = 0}
    (hS : (ShortComplex.mk f g hfg).ShortExact)
    {f' : B ⟶ Z'} {g' : Z' ⟶ C} {hf'g' : f' ≫ g' = 0}
    (hS' : (ShortComplex.mk f' g' hf'g').ShortExact) :
    hS'.extClass.comp hS.extClass rfl = 0 ↔
      ∃ (W : 𝒜) (a : A ⟶ W) (q : W ⟶ Z') (i : Z ⟶ W) (p : W ⟶ C)
        (haq : a ≫ q = 0) (hip : i ≫ p = 0),
        (ShortComplex.mk a q haq).ShortExact ∧ (ShortComplex.mk i p hip).ShortExact ∧
          f ≫ i = a ∧ i ≫ q = g ≫ f' ∧ q ≫ g' = p
```

## Tag 0EWW, a lemma

[Tag 0EWW](https://stacks.math.columbia.edu/tag/0EWW) in the Stacks Project.

**`CategoryTheory.hasProjectiveDimensionLT_of_forall_ext_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Ext/Basic/ExtOneAndVanishing.lean, line 324](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Ext/Basic/ExtOneAndVanishing.lean#L324).

> **Vanishing of `Ext^p_𝒜(X, -)` forces projective dimension `< p`.**
> If `𝒜` is an abelian category and `Ext^p_𝒜(X, Y) = 0` for every object `Y` of `𝒜`, then `X` has
> projective dimension `< p`, i.e. `Ext^i_𝒜(X, Y) = 0` for every `i ≥ p` and every `Y`. This
> generalizes `CategoryTheory.hasProjectiveDimensionLT_of_enoughInjectives` by dropping the
> assumption `[EnoughInjectives 𝒜]`. [Stacks, Tag 0EWW] states the reading for all pairs of
> objects at once, which follows by applying this to every object of `𝒜`.

```lean
public theorem hasProjectiveDimensionLT_of_forall_ext_eq_zero (X : 𝒜) (p : ℕ)
    (h : ∀ (Y : 𝒜) (e : Abelian.Ext.{w} X Y p), e = 0) : HasProjectiveDimensionLT X p
```

## Tag 0GM4, a lemma

[Tag 0GM4](https://stacks.math.columbia.edu/tag/0GM4) in the Stacks Project.

**`DerivedCategory.nonempty_iso_biproduct_singleFunctor_obj_homology_of_forall_ext_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Ext/Basic/SplittingAndResolutions.lean, line 365](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Ext/Basic/SplittingAndResolutions.lean#L365).

> **A bounded complex with no higher Ext between its cohomologies is the sum of them.**
> Let `𝒜` be an abelian category and let `K` be an object of `D(𝒜)` whose cohomology vanishes
> outside `[a, b]`. If `Ext^p_𝒜(H^i(K), H^j(K)) = 0` for all `p ≥ 2` and all `i > j`, then `K` is
> isomorphic to the direct sum `⨁_{a ≤ i ≤ b} H^i(K)[-i]` of its cohomologies. The isomorphism
> depends on choices of splittings, so only its existence is asserted. For `a = b` this is
> `DerivedCategory.exists_iso_singleFunctor_obj_of_isGE_of_isLE`.

```lean
public theorem nonempty_iso_biproduct_singleFunctor_obj_homology_of_forall_ext_eq_zero
    (K : DerivedCategory C) (a b : ℤ) [K.IsGE a] [K.IsLE b]
    (h : ∀ (i j : ℤ) (p : ℕ), j < i → 2 ≤ p →
      ∀ e : Abelian.Ext.{w'} ((homologyFunctor C i).obj K) ((homologyFunctor C j).obj K) p,
        e = 0) :
    Nonempty (K ≅ ⨁ fun i : Finset.Icc a b =>
      (singleFunctor C i.1).obj ((homologyFunctor C i.1).obj K))
```

## Tag 0EWX, a lemma

[Tag 0EWX](https://stacks.math.columbia.edu/tag/0EWX) in the Stacks Project.

**`DerivedCategory.nonempty_iso_biproduct_singleFunctor_obj_homology_of_forall_ext_two_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Ext/Basic/SplittingAndResolutions.lean, line 413](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Ext/Basic/SplittingAndResolutions.lean#L413).

> **A bounded complex over a category with no `Ext²` is the sum of its cohomologies.**
> Let `𝒜` be an abelian category with `Ext²_𝒜(B, A) = 0` for every pair of objects `A`, `B`, and
> let `K` be an object of `D(𝒜)` whose cohomology vanishes outside `[a, b]`. Then `K` is
> isomorphic to the direct sum `⨁_{a ≤ i ≤ b} H^i(K)[-i]` of its cohomologies. The isomorphism
> depends on choices of splittings, so only its existence is asserted. This is the special case
> of `DerivedCategory.nonempty_iso_biproduct_singleFunctor_obj_homology_of_forall_ext_eq_zero`
> ([Stacks, Tag 0GM4]) in which the vanishing of `Ext^p`, `p ≥ 2`, comes from the category rather
> than from `K`, via [Stacks, Tag 0EWW].

```lean
public theorem nonempty_iso_biproduct_singleFunctor_obj_homology_of_forall_ext_two_eq_zero
    (K : DerivedCategory C) (a b : ℤ) [K.IsGE a] [K.IsLE b]
    (h : ∀ (A B : C) (e : Abelian.Ext.{w'} B A 2), e = 0) :
    Nonempty (K ≅ ⨁ fun i : Finset.Icc a b =>
      (singleFunctor C i.1).obj ((homologyFunctor C i.1).obj K))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 13.27, Tag 06XP](https://stacks.math.columbia.edu/tag/06XP)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
