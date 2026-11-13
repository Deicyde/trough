---
declaration: section
origin: cited
lean: CochainComplex.InjectiveResolution, CategoryTheory.InjectiveResolution.toCochainComplexResolution, CochainComplex.InjectiveResolution.toNatResolution, CochainComplex.isGE_iff_exists_quasiIso_isStrictlyGE, CochainComplex.exists_injectiveResolution_isStrictlyGE, CochainComplex.isKInjective_of_injective, CochainComplex.IsKInjective.nonempty_homotopy_zero, CochainComplex.IsKInjective.rightOrthogonal
statement: formalized
proof: formalized
---

# 13.18 Injective resolutions

Section 13.18 of the Stacks Project, [Tag 013G](https://stacks.math.columbia.edu/tag/013G). 9 tags here are carried by 12 declarations of the repository (all in StacksFrontier) and 5 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 013I, a definition

[Tag 013I](https://stacks.math.columbia.edu/tag/013I) in the Stacks Project.

**`CochainComplex.InjectiveResolution`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/Resolution/Defs/InjectiveResolution.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/Resolution/Defs/InjectiveResolution.lean#L50). References: SGA 2 VIII (1.3); SGA 4½ Etat 0 (3.1.8), “injective case”.

> An injective resolution of a cochain complex `K` in a category `C`: a bounded below cochain
> complex `cocomplex` of injective objects of `C`, together with a quasi-isomorphism
> `ι : K ⟶ cocomplex`.

```lean
public structure InjectiveResolution (K : CochainComplex C ℤ)
```

**`CategoryTheory.InjectiveResolution.toCochainComplexResolution`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/Resolution/NatIntBridge.lean, line 289](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/Resolution/NatIntBridge.lean#L289). The attribute's comment: “the identification of the `ℕ`-graded half of the tag with the `ℤ`-graded one”.

> An injective resolution of an object `X`, indexed by `ℕ`, read as an injective resolution of
> the cochain complex `X[0]`, indexed by `ℤ`: the resolving complex is extended by zero in the
> negative degrees, which is Mathlib's `CategoryTheory.InjectiveResolution.cochainComplex`.

```lean
def toCochainComplexResolution (R : InjectiveResolution X) :
    CochainComplex.InjectiveResolution ((CochainComplex.singleFunctor C 0).obj X)
```

**`CochainComplex.InjectiveResolution.toNatResolution`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/Resolution/NatIntBridge.lean, line 325](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/Resolution/NatIntBridge.lean#L325). The attribute's comment: “the identification of the `ℤ`-graded half of the tag with the `ℕ`-graded one, for a resolving complex vanishing in the negative degrees”.

> An injective resolution of the cochain complex `X[0]`, indexed by `ℤ` and vanishing in the
> negative degrees, read as an injective resolution of the object `X`, indexed by `ℕ`: the resolving
> complex is restricted along `ComplexShape.embeddingUpNat`.
>
> The hypothesis that the resolving complex vanish in the negative degrees cannot be dropped; see
> the module docstring.

```lean
def toNatResolution
    (R : CochainComplex.InjectiveResolution ((CochainComplex.singleFunctor C 0).obj X))
    [R.cocomplex.IsStrictlyGE 0] : CategoryTheory.InjectiveResolution X
```

## Tag 013J, a lemma

[Tag 013J](https://stacks.math.columbia.edu/tag/013J) in the Stacks Project.

**`CochainComplex.isGE_iff_exists_quasiIso_isStrictlyGE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/Resolution/InjectiveResolution.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/Resolution/InjectiveResolution.lean#L93).

> Let `C` be a category with zero morphisms, a zero object and homology for every short complex,
> and let `K` be a cochain complex of `C`. The cohomology of `K` vanishes in all degrees `< n` if and
> only if there is a quasi-isomorphism `f : K ⟶ L` with `L` zero in all degrees `< n`.

```lean
public theorem isGE_iff_exists_quasiIso_isStrictlyGE {C : Type*} [Category C]
    [HasZeroMorphisms C] [HasZeroObject C] [CategoryWithHomology C]
    (K : CochainComplex C ℤ) (n : ℤ) :
    K.IsGE n ↔ ∃ (L : CochainComplex C ℤ) (f : K ⟶ L) (_ : QuasiIso f), L.IsStrictlyGE n
```

## Tag 013K, a lemma

[Tag 013K](https://stacks.math.columbia.edu/tag/013K) in the Stacks Project.

**`CochainComplex.exists_injectiveResolution_isStrictlyGE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/Resolution/InjectiveResolution.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/Resolution/InjectiveResolution.lean#L110). References: SGA 4½ Etat 0 (3.2.3), “(4) existence”; SGA 4½ Etat 0 (4.2.3.1), “Corollary 1”.

> Let `A` be an abelian category with enough injectives, let `a : ℤ` and let `K` be a cochain
> complex of `A` with `H ^ n (K) = 0` for `n < a`. Then `K` has an injective resolution `R` whose
> resolving complex satisfies `R.cocomplex.X n = 0` for `n < a`; and if moreover `K.X n = 0` for
> `n < a`, then `R` can be chosen with all the components `R.ι.f n : K.X n ⟶ R.cocomplex.X n`
> monomorphisms.

```lean
public theorem exists_injectiveResolution_isStrictlyGE [EnoughInjectives A] (a : ℤ)
    (K : CochainComplex A ℤ) [K.IsGE a] :
    ∃ (R : K.InjectiveResolution) (_ : K.IsStrictlyGE a → ∀ n, Mono (R.ι.f n)),
      R.cocomplex.IsStrictlyGE a
```

## Tag 013R, a lemma

[Tag 013R](https://stacks.math.columbia.edu/tag/013R) in the Stacks Project.

Declarations registered for the tag:

- [`CochainComplex.isKInjective_of_injective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CochainComplex.isKInjective_of_injective#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Homology/Resolution/InjectiveResolution.lean, line 464](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/Resolution/InjectiveResolution.lean#L464) (StacksFrontier): “the lemma's induction, with a supplied bound `d` for the boundedness below: a complex which is strictly bounded below by `d` and whose terms are injective objects is K-injective”.
- [`CochainComplex.IsKInjective.nonempty_homotopy_zero`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CochainComplex.IsKInjective.nonempty_homotopy_zero#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Homology/Resolution/InjectiveResolution.lean, line 468](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/Resolution/InjectiveResolution.lean#L468) (StacksFrontier): “the conclusion at one morphism, the source's sentence: a morphism from an acyclic complex to a K-injective complex is homotopic to zero”.
- [`CochainComplex.IsKInjective.rightOrthogonal`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CochainComplex.IsKInjective.rightOrthogonal#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Homology/Resolution/InjectiveResolution.lean, line 472](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/Resolution/InjectiveResolution.lean#L472) (StacksFrontier): “the conclusion in `K(A)`: a K-injective complex is right orthogonal to the acyclic complexes, i.e. every morphism `K ⟶ I` of `K(A)` with `K` acyclic is zero”.

## Tag 05TF, a remark

[Tag 05TF](https://stacks.math.columbia.edu/tag/05TF) in the Stacks Project.

**`CochainComplex.bijective_precomp_quotient_map`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/Resolution/InjectiveResolution.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/Resolution/InjectiveResolution.lean#L131).

> If `I` is a K-injective cochain complex and `α : K ⟶ L` is a quasi-isomorphism, then
> precomposition with the image of `α` in the homotopy category `K(A)` is a bijection
> `Hom_{K(A)}(L, I) → Hom_{K(A)}(K, I)`.

```lean
lemma bijective_precomp_quotient_map [I.IsKInjective] (α : K ⟶ L) [QuasiIso α] :
    Function.Bijective (fun β : (HomotopyCategory.quotient A (ComplexShape.up ℤ)).obj L ⟶
        (HomotopyCategory.quotient A (ComplexShape.up ℤ)).obj I =>
      (HomotopyCategory.quotient A (ComplexShape.up ℤ)).map α ≫ β)
```

## Tag 013P, a lemma

[Tag 013P](https://stacks.math.columbia.edu/tag/013P) in the Stacks Project.

**`CochainComplex.IsKInjective.exists_factorization_of_quasiIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/Resolution/InjectiveResolution.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/Resolution/InjectiveResolution.lean#L159). The attribute's comment: “for a K-injective target, which by 013R covers the source's hypothesis that the target be bounded below with injective terms; the extra hypotheses of part (2) are attached to its own conjunct”. References: SGA 2 VIII (1.4), “existence of Cu”.

> Let `A` be an abelian category, let `α : K ⟶ L` be a quasi-isomorphism of cochain complexes of
> `A`, let `I` be a K-injective cochain complex of `A` and let `γ : K ⟶ I`. Then (1) there is a
> morphism of complexes `β : L ⟶ I` such that `α ≫ β` is homotopic to `γ`, and (2) if every term of
> `I` is an injective object and `α` is a monomorphism in every degree, then there is a `β` with
> `α ≫ β = γ`.

```lean
public theorem IsKInjective.exists_factorization_of_quasiIso [I.IsKInjective] (α : K ⟶ L)
    [QuasiIso α] (γ : K ⟶ I) :
    (∃ β : L ⟶ I, Nonempty (Homotopy (α ≫ β) γ)) ∧
      (∀ [∀ n, Injective (I.X n)] [∀ n, Mono (α.f n)], ∃ β : L ⟶ I, α ≫ β = γ)
```

**`CochainComplex.exists_desc_of_quasiIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/Resolution/NatIntBridge.lean, line 438](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/Resolution/NatIntBridge.lean#L438). The attribute's comment: “part (2), for `ℕ`-indexed complexes, with the source required only to be quasi-isomorphic to a complex concentrated in degree zero and the target only to have injective terms”. References: EGA 0 (12.1.4), “partial”.

> **Stacks 013P, part (2), for `ℕ`-indexed complexes: descent with minimal hypotheses.** Let `C`
> be an abelian category, let `ε : Z[0] ⟶ K` be a quasi-isomorphism of cochain complexes of `C`
> indexed by `ℕ`, let `L` be a cochain complex of injective objects and let `γ : Z[0] ⟶ L`. Then
> `γ = ε ≫ β` for a (unique up to homotopy, see
> `CochainComplex.nonempty_homotopy_of_precomp_quasiIso`) morphism `β : K ⟶ L`.
>
> Neither `K` nor `L` is required to be an injective resolution: the terms of `K` are arbitrary and
> `L` resolves nothing. Mathlib's `CategoryTheory.InjectiveResolution.desc` is the special case
> where both are the resolving complexes of injective resolutions.

```lean
theorem exists_desc_of_quasiIso [∀ n, Injective (L.X n)] (ε : (single₀ C).obj Z ⟶ K) [QuasiIso ε]
    (γ : (single₀ C).obj Z ⟶ L) : ∃ β : K ⟶ L, ε ≫ β = γ
```

## Tag 013S, a lemma

[Tag 013S](https://stacks.math.columbia.edu/tag/013S) in the Stacks Project.

**`CochainComplex.IsKInjective.nonempty_homotopy_of_precomp_quasiIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/Resolution/InjectiveResolution.lean, line 174](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/Resolution/InjectiveResolution.lean#L174). The attribute's comment: “for a K-injective target, which by Tag 013R covers the source's bounded below complex of injective objects; the source's intermediary `γ : K ⟶ I` is eliminated by transitivity of homotopy”. References: SGA 2 VIII (1.4), “uniqueness of Cu”.

> Let `A` be an abelian category, let `α : K ⟶ L` be a quasi-isomorphism of cochain complexes of
> `A` and let `I` be a K-injective cochain complex of `A`. Then two morphisms `β₁, β₂ : L ⟶ I` with
> `α ≫ β₁` homotopic to `α ≫ β₂` are homotopic.

```lean
public theorem IsKInjective.nonempty_homotopy_of_precomp_quasiIso [I.IsKInjective] (α : K ⟶ L)
    [QuasiIso α] {β₁ β₂ : L ⟶ I} (h : Homotopy (α ≫ β₁) (α ≫ β₂)) :
    Nonempty (Homotopy β₁ β₂)
```

**`CochainComplex.nonempty_homotopy_of_precomp_quasiIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/Resolution/NatIntBridge.lean, line 468](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/Resolution/NatIntBridge.lean#L468). The attribute's comment: “for `ℕ`-indexed complexes, with the source required only to be quasi-isomorphic to a complex concentrated in degree zero and the target only to have injective terms”. References: EGA 0 (12.1.4), “partial”; SGA 2 VIII (1.4), “special case”.

> **Stacks 013S, for `ℕ`-indexed complexes: uniqueness of the descent with minimal
> hypotheses.** Two morphisms `β₁, β₂ : K ⟶ L` from a cochain complex quasi-isomorphic to `Z[0]`
> into a cochain complex of injective objects which agree, up to homotopy, after precomposition with
> a quasi-isomorphism `ε : Z[0] ⟶ K`, are homotopic.
>
> As in `CochainComplex.exists_desc_of_quasiIso`, neither complex need be an injective resolution.
> Mathlib's `CategoryTheory.InjectiveResolution.descHomotopy` is the special case where both are;
> `CategoryTheory.InjectiveResolution.descHomotopy'` weakens the target alone.

```lean
theorem nonempty_homotopy_of_precomp_quasiIso [∀ n, Injective (L.X n)]
    (ε : (single₀ C).obj Z ⟶ K) [QuasiIso ε] {β₁ β₂ : K ⟶ L}
    (h : Homotopy (ε ≫ β₁) (ε ≫ β₂)) : Nonempty (Homotopy β₁ β₂)
```

## Tag 05TG, a lemma

[Tag 05TG](https://stacks.math.columbia.edu/tag/05TG) in the Stacks Project.

Declarations registered for the tag:

- [`CochainComplex.IsKInjective.Qh_map_bijective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CochainComplex.IsKInjective.Qh_map_bijective#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Homology/Resolution/InjectiveResolution.lean, line 184](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/Resolution/InjectiveResolution.lean#L184) (StacksFrontier): “the bijection `Mor_{K(A)}(K, I) → Mor_{D(A)}(K, I)` for a K-injective `I`”.
- [`CochainComplex.isKInjective_of_injective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CochainComplex.isKInjective_of_injective#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Homology/Resolution/InjectiveResolution.lean, line 186](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/Resolution/InjectiveResolution.lean#L186) (StacksFrontier): “a complex strictly bounded below with injective terms is K-injective”.

## Tag 013T, a lemma

[Tag 013T](https://stacks.math.columbia.edu/tag/013T) in the Stacks Project.

**`CategoryTheory.ShortComplex.ShortExact.exists_shortExact_injectiveResolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/Resolution/InjectiveResolution.lean, line 434](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/Resolution/InjectiveResolution.lean#L434). The attribute's comment: “parts (1)–(3); the given resolution of the first term is a hypothesis and the degree bound of parts (2) and (3) is an implication in the conclusion, so the source's plain assertion follows by resolving the first term with 013K”.

> Let `A` be an abelian category with enough injectives, let `S : 0 ⟶ X₁ ⟶ X₂ ⟶ X₃ ⟶ 0` be a
> short exact sequence of cochain complexes of `A` with `X₂` (hence `X₁` and `X₃`) vanishing in the
> degrees `< a`, and let `R₁` be any injective resolution of `X₁`. Then there are injective
> resolutions `R₂` of `X₂` and `R₃` of `X₃` and a short exact sequence `0 ⟶ I₁ ⟶ I₂ ⟶ I₃ ⟶ 0` of the
> resolving complexes making both squares commute; and if `I₁` also vanishes in the degrees `< a`,
> then `I₂` and `I₃` may be chosen to do so as well.

```lean
public theorem exists_shortExact_injectiveResolution [EnoughInjectives A] (a : ℤ)
    {S : ShortComplex (CochainComplex A ℤ)} (hS : S.ShortExact) [S.X₂.IsStrictlyGE a]
    (R₁ : S.X₁.InjectiveResolution) :
    ∃ (R₂ : S.X₂.InjectiveResolution) (R₃ : S.X₃.InjectiveResolution)
      (f : R₁.cocomplex ⟶ R₂.cocomplex) (g : R₂.cocomplex ⟶ R₃.cocomplex)
      (w : f ≫ g = 0) (_ : (ShortComplex.mk f g w).ShortExact)
      (_ : R₁.cocomplex.IsStrictlyGE a →
        R₂.cocomplex.IsStrictlyGE a ∧ R₃.cocomplex.IsStrictlyGE a),
      R₁.ι ≫ f = S.f ≫ R₂.ι ∧ R₂.ι ≫ g = S.g ≫ R₃.ι
```

**`CategoryTheory.ShortComplex.ShortExact.exists_injectiveResolution_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/Resolution/NatHorseshoe.lean, line 171](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/Resolution/NatHorseshoe.lean#L171). The attribute's comment: “the `ℕ`-graded form for a short exact sequence of objects, with the degreewise splitting of the resulting sequence of resolving complexes”.

> **The injective horseshoe for `ℕ`-indexed resolutions of objects.** Let `A` be an abelian
> category with enough injectives and let `0 ⟶ X₁ ⟶ X₂ ⟶ X₃ ⟶ 0` be a short exact sequence of
> objects of `A`. Then there are injective resolutions `J₁`, `J₂`, `J₃` of the three terms and a
> short exact sequence `0 ⟶ J₁ ⟶ J₂ ⟶ J₃ ⟶ 0` of the resolving complexes over it: the two squares
> built from the augmentations commute in degree zero, and the sequence is split in every degree.
>
> This is the `ℕ`-indexed form of Stacks 013T for a sequence of objects. It is deduced from the
> `ℤ`-indexed `StacksDraft.CartanEilenbergResolutions.horseshoeProperty`, with the two outer
> resolutions prescribed to be the extensions by zero of arbitrary `ℕ`-indexed ones, by restricting
> the resulting sequence of complexes back along `ComplexShape.embeddingUpNat`.
>
> The degreewise splitting is what makes the sequence stay short exact under an arbitrary additive
> functor applied degreewise; it is not read off the twisted-biproduct construction of the
> horseshoe but recovered afterwards from
> `CategoryTheory.ShortComplex.ShortExact.splittingOfInjective`, the first term of the sequence in
> degree `n` being the injective object `J₁.cocomplex.X n`.

```lean
theorem exists_injectiveResolution_shortExact [EnoughInjectives A]
    {S : ShortComplex A} (hS : S.ShortExact) :
    ∃ (J₁ : InjectiveResolution S.X₁) (J₂ : InjectiveResolution S.X₂)
      (J₃ : InjectiveResolution S.X₃) (f : J₁.cocomplex ⟶ J₂.cocomplex)
      (g : J₂.cocomplex ⟶ J₃.cocomplex) (w : f ≫ g = 0),
      (ShortComplex.mk f g w).ShortExact ∧
      J₁.ι.f 0 ≫ f.f 0 = S.f ≫ J₂.ι.f 0 ∧ J₂.ι.f 0 ≫ g.f 0 = S.g ≫ J₃.ι.f 0 ∧
      ∀ n, ∃ _ : (ShortComplex.mk (f.f n) (g.f n)
        (congrFun (congrArg HomologicalComplex.Hom.f w) n)).Splitting, True
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 13.18, Tag 013G](https://stacks.math.columbia.edu/tag/013G)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
