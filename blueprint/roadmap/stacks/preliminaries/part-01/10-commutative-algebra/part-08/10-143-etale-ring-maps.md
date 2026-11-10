---
declaration: section
origin: cited
lean: Algebra.Etale.iff_isStandardSmoothOfRelativeDimension_zero, Algebra.etaleLocus_eq_of_isPushout, Algebra.Etale.exists_etale_stage_of_isColimit, Algebra.Etale.iff_exists_algEquiv_prod, Algebra.IsEtaleAt.map_eq_maximalIdeal_and_finite_isSeparable_residueField, RingHom.Etale.quasiFinite, Algebra.IsEtaleAt.of_flat_of_map_eq_maximalIdeal, RingHom.Etale.of_comp
statement: formalized
proof: formalized
---

# 10.143 Étale ring maps

Section 10.143 of the Stacks Project, [Tag 00U0](https://stacks.math.columbia.edu/tag/00U0). 11 tags here are carried by 19 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00U9, a lemma

[Tag 00U9](https://stacks.math.columbia.edu/tag/00U9) in the Stacks Project.

Declarations registered for the tag:

- [`Algebra.Etale.iff_isStandardSmoothOfRelativeDimension_zero`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.Etale.iff_isStandardSmoothOfRelativeDimension_zero#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Etale/Basic/FirstProperties.lean, line 205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/Basic/FirstProperties.lean#L205) (StacksFrontier): “An étale algebra is standard smooth of relative dimension `0`, that is, it admits a presentation with as many equations as variables whose Jacobian determinant is invertible. Mathlib proves the equivalence, of which the tag is the forward implication.”. References: SGA 1 II (1.3), “clause (i), special case”.

## Tag 00U2, a lemma

[Tag 00U2](https://stacks.math.columbia.edu/tag/00U2) in the Stacks Project.

**`Algebra.etaleLocus_eq_of_isPushout`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/Basic/FirstProperties.lean, line 406](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/Basic/FirstProperties.lean#L406). The attribute's comment: “(5). Stated for `Algebra.etaleLocus`, hence without the tag's hypothesis that `R → S` be of finite presentation, which neither the conclusion nor the proof uses; with that hypothesis the two loci are the tag's. The base change is the abstract `Algebra.IsPushout`. See the module docstring, which also records where in Mathlib the other ten items live.”.

> Let `R → S` be a ring map, let `R → R'` be flat and let `S'` be the base change of `S` along
> `R → R'`. Then the set of primes of `S'` where `R' → S'` is étale is the inverse image, under
> `Spec S' → Spec S`, of the set of primes of `S` where `R → S` is étale.

```lean
theorem Algebra.etaleLocus_eq_of_isPushout
    (R S : Type*) [CommRing R] [CommRing S] [Algebra R S]
    (R' S' : Type*) [CommRing R'] [CommRing S'] [Algebra R R'] [Algebra S S'] [Algebra R' S']
    [Algebra R S'] [IsScalarTower R R' S'] [IsScalarTower R S S']
    [Algebra.IsPushout R S R' S'] [Module.Flat R R'] :
    Algebra.etaleLocus R' S' =
      PrimeSpectrum.comap (algebraMap S S') ⁻¹' Algebra.etaleLocus R S
```

**`Algebra.Etale.exists_etale_stage_of_isColimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/FilteredColimitStage.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/FilteredColimitStage.lean#L105). The attribute's comment: “(9) The filtered colimit `A = colim A_i` is an arbitrary filtered diagram `F : J ⥤ CommRingCat` together with a colimiting cocone `c` with vertex `A`, plus the instance saying the colimit is computed on underlying sets; the stages `A_i` are `F.obj i` and the comparison maps are the legs `c.ι.app i`, which are also the `A_i`-algebra structure of `A` in the conclusion. The isomorphism `B ≅ A ⊗_{A_i} B_i` is one of `A`-algebras, with the tensor product as the model of the base change. The existing registration of item (5) is `Algebra.etaleLocus_eq_of_isPushout`; item (8), which this is deduced from, is Mathlib's `Algebra.Etale.exists_subalgebra_fg`. See the module docstring.”.

> **Item (9) of Stacks 00U2.** Let `A = colim_{i ∈ J} A_i` be a filtered colimit of rings,
> computed on underlying sets, and let `B` be an étale `A`-algebra. Then there are an index `i` and
> an étale `A_i`-algebra `B_i` with `B ≅ A ⊗_{A_i} B_i` as `A`-algebras, the `A_i`-algebra structure
> of `A` being the comparison map `A_i → A`.

```lean
theorem Algebra.Etale.exists_etale_stage_of_isColimit {J : Type w} [Category.{t} J] [IsFiltered J]
    (F : J ⥤ CommRingCat.{u}) {c : Cocone F} (hc : IsColimit c)
    [PreservesColimit F (forget CommRingCat)]
    (B : Type*) [CommRing B] [Algebra (c.pt : Type u) B] [Algebra.Etale (c.pt : Type u) B] :
    ∃ (i : J) (Bᵢ : Type u) (_ : CommRing Bᵢ) (_ : Algebra (F.obj i : Type u) Bᵢ),
      Algebra.Etale (F.obj i : Type u) Bᵢ ∧
        (letI : Algebra (F.obj i : Type u) (c.pt : Type u) := (c.ι.app i).hom.toAlgebra;
          Nonempty (B ≃ₐ[(c.pt : Type u)] (c.pt : Type u) ⊗[(F.obj i : Type u)] Bᵢ))
```

## Tag 00U3, a lemma

[Tag 00U3](https://stacks.math.columbia.edu/tag/00U3) in the Stacks Project.

Declarations registered for the tag:

- [`Algebra.Etale.iff_exists_algEquiv_prod`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.Etale.iff_exists_algEquiv_prod#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 253](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch10.lean#L253) (StacksFrontier). References: EGA III (7.8.6); EGA IV (17.6.2), “a ⇔ c', special case”; EGA IV (17.15.11), “a ⇔ c, affine case”; EGA IV (18.2.3); EGA IV (18.3.3); SGA 1 I (10.1), “special case”; SGA 1 IX (1.2), “special case”; SGA 1 IX (1.8), “more general”; SGA 1 IX (1.9); SGA 1 XIII (2.0), “more general”; SGA 3 VIIB (1.6), “special case”; SGA 3 VIIB (1.6.E), “special case”; SGA 3 VIIB (2.5), “special case”; SGA 3 XVII (5.2.1), “partial”; SGA 4½ Arcata (2.1.2); SGA 4½ Arcata (2.4.2); SGA 4½ Sommes trig (4.5), “partial”; SGA 4½ Sommes trig (6.1), “partial”.

## Tag 00U4, a lemma

[Tag 00U4](https://stacks.math.columbia.edu/tag/00U4) in the Stacks Project.

**`Algebra.IsEtaleAt.map_eq_maximalIdeal_and_finite_isSeparable_residueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/ResidueFieldExtension.lean, line 637](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/ResidueFieldExtension.lean#L637). The attribute's comment: “The source's hypothesis that `R → S` be étale at `q` is taken in the weaker form of its two consequences: `Algebra.IsEtaleAt R q`, and `S_q` essentially of finite type over `R` (rather than finite presentation of `S` over `R`). Item (1) is recorded as `p S_q = m_{S_q}`; the source's other half `q S_q = m_{S_q}` holds for any prime and is `Localization.AtPrime.map_eq_maximalIdeal`. See the module docstring, which also records that the unramified version of this statement is the separate tag 00UW.”. References: SGA 1 I (3.1), “(i)”.

> **Stacks 00U4.** Let `R → S` be a ring map and let `q` be a prime of `S` lying over a prime
> `p` of `R`. If `R → S` is étale at `q` then (1) the ideal `p S_q` is the maximal ideal of the
> local ring `S_q`, hence equals `q S_q`, and (2) the residue field extension `κ(q)/κ(p)` is finite
> separable.

```lean
public theorem Algebra.IsEtaleAt.map_eq_maximalIdeal_and_finite_isSeparable_residueField
    {R S : Type*} [CommRing R] [CommRing S] [Algebra R S]
    (p : Ideal R) [p.IsPrime] (q : Ideal S) [q.IsPrime] [q.LiesOver p]
    [Algebra (Localization.AtPrime p) (Localization.AtPrime q)]
    [Localization.AtPrime.IsLiesOverAlgebra p q]
    [Algebra.EssFiniteType R (Localization.AtPrime q)] [Algebra.IsEtaleAt R q] :
    p.map (algebraMap R (Localization.AtPrime q)) = maximalIdeal (Localization.AtPrime q) ∧
      Module.Finite p.ResidueField q.ResidueField ∧
      Algebra.IsSeparable p.ResidueField q.ResidueField
```

## Tag 00U5, a lemma

[Tag 00U5](https://stacks.math.columbia.edu/tag/00U5) in the Stacks Project.

**`RingHom.Etale.quasiFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/Basic/FirstProperties.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/Basic/FirstProperties.lean#L195).

> An étale ring map is quasi-finite: every fibre `κ(P) ⊗ S` is a finite `κ(P)`-algebra.

```lean
theorem RingHom.Etale.quasiFinite
    {R S : Type*} [CommRing R] [CommRing S]
    (f : R →+* S) (hf : f.Etale) :
    f.QuasiFinite
```

## Tag 00U6, a lemma

[Tag 00U6](https://stacks.math.columbia.edu/tag/00U6) in the Stacks Project.

**`Algebra.IsEtaleAt.of_flat_of_map_eq_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/Basic/FirstProperties.lean, line 347](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/Basic/FirstProperties.lean#L347). The attribute's comment: “"Étale at `q`" is `Algebra.IsEtaleAt R q`, which under hypothesis (1) is the source's Definition 00U1 (`Algebra.exists_etale_of_isEtaleAt` in one direction, `Algebra.basicOpen_subset_etaleLocus_iff_etale` in the other). Hypothesis (3) is recorded as `p S_q = m_{S_q}`; the source's `p S_q = q S_q` follows by `Localization.AtPrime.map_eq_maximalIdeal`. The finiteness half of (4) is stated because the source states it, and is implied by the rest; see the module docstring.”. References: EGA IV (18.2.3), “a') ⇒ a)”; SGA 1 IX (1.2), “converse direction”.

> Let `R → S` be a ring map and let `q` be a prime of `S` lying over a prime `p` of `R`. If (1)
> `R → S` is of finite presentation, (2) `R_p → S_q` is flat, (3) `p S_q` is the maximal ideal of the
> local ring `S_q`, and (4) the field extension `κ(q)/κ(p)` is finite separable, then `R → S` is
> étale at `q`.

```lean
theorem Algebra.IsEtaleAt.of_flat_of_map_eq_maximalIdeal
    {R S : Type*} [CommRing R] [CommRing S] [Algebra R S] [Algebra.FinitePresentation R S]
    (p : Ideal R) [p.IsPrime] (q : Ideal S) [q.IsPrime] [q.LiesOver p]
    [Algebra (Localization.AtPrime p) (Localization.AtPrime q)]
    [Localization.AtPrime.IsLiesOverAlgebra p q]
    [Module.Flat (Localization.AtPrime p) (Localization.AtPrime q)]
    [Module.Finite p.ResidueField q.ResidueField]
    [Algebra.IsSeparable p.ResidueField q.ResidueField]
    (h : p.map (algebraMap R (Localization.AtPrime q)) =
      IsLocalRing.maximalIdeal (Localization.AtPrime q)) :
    Algebra.IsEtaleAt R q
```

## Tag 00U7, a lemma

[Tag 00U7](https://stacks.math.columbia.edu/tag/00U7) in the Stacks Project.

**`RingHom.Etale.of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/Basic/FirstProperties.lean, line 267](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/Basic/FirstProperties.lean#L267). The attribute's comment: “Stated for ring maps and their composite rather than for a tower of algebras: the source quantifies over `R`-algebra maps `S → T`, for which `RingHom.Etale` is the predicate, and the sibling `RingHom.FormallyEtale.of_comp` is stated that way. The hypothesis that `R → S` be étale is weakened to the two properties the mathematics uses, formal unramifiedness and finite type; see the module docstring for a witness that the generalization is strict.”.

> Let `f : R →+* S` and `g : S →+* T` be ring maps, so that `g` is a map of `R`-algebras for the
> `R`-algebra structure `g ∘ f` on `T`. If `f` is formally unramified and of finite type and `g ∘ f`
> is étale, then `g` is étale. In particular a map between two étale `R`-algebras is étale.

```lean
theorem RingHom.Etale.of_comp {R S T : Type*} [CommRing R] [CommRing S] [CommRing T]
    {f : R →+* S} {g : S →+* T} (hf : f.FormallyUnramified) (hf' : f.FiniteType)
    (h : (g.comp f).Etale) : g.Etale
```

## Tag 00U8, a lemma

[Tag 00U8](https://stacks.math.columbia.edu/tag/00U8) in the Stacks Project.

**`Algebra.exists_isIdempotentElem_isLocalizationAway_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/Basic/FirstProperties.lean, line 219](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/Basic/FirstProperties.lean#L219).

> A surjective, flat, finitely presented ring map `R → S` exhibits `S` as the localization of
> `R` at an idempotent `e`: the kernel of `algebraMap R S` is the ideal `(1 - e)`, and `S` is the
> localization of `R` away from `e`.

```lean
theorem Algebra.exists_isIdempotentElem_isLocalizationAway_of_surjective
    (R S : Type*) [CommRing R] [CommRing S] [Algebra R S]
    (hsurj : Function.Surjective (algebraMap R S))
    [Module.Flat R S] [Algebra.FinitePresentation R S] :
    ∃ e : R, IsIdempotentElem e ∧
      RingHom.ker (algebraMap R S) = Ideal.span {1 - e} ∧
      IsLocalization.Away e S
```

## Tag 04D1, a lemma

[Tag 04D1](https://stacks.math.columbia.edu/tag/04D1) in the Stacks Project.

**`etale_lift_along_surjection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/Lifting.lean, line 287](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/Lifting.lean#L287). References: EGA IV (18.1.1), “special case”.

> Étale ring maps lift along surjections of rings: if `A' → A` is a surjection of commutative
> rings with kernel `I` and `B` is an étale `A`-algebra, then `B` is the reduction of an étale
> `A'`-algebra, in the sense that there are an étale `A'`-algebra `C` and a surjection of
> `A'`-algebras `ψ : C → B` with `RingHom.ker ψ = I C`.

```lean
theorem etale_lift_along_surjection (A' : Type u) (A : Type v) (B : Type w)
    [CommRing A'] [CommRing A] [CommRing B] [Algebra A' A] [Algebra A B] [Algebra A' B]
    [IsScalarTower A' A B] (hA : Function.Surjective (algebraMap A' A)) [Algebra.Etale A B] :
    ∃ (C : Type u) (_ : CommRing C) (_ : Algebra A' C), Algebra.Etale A' C ∧
      ∃ ψ : C →ₐ[A'] B, Function.Surjective ψ ∧
        RingHom.ker (ψ : C →+* B) = (RingHom.ker (algebraMap A' A)).map (algebraMap A' C)
```

## Tag 05YT, a lemma

[Tag 05YT](https://stacks.math.columbia.edu/tag/05YT) in the Stacks Project.

**`Stacks.Thickenings.etale_of_isKerBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Etale.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Etale.lean#L120). The attribute's comment: “The scheme-level form: on a commutative square of schemes with closed immersions `i : X ⟶ X'` and `j : Y ⟶ Y'`, square-zero kernel ideal sheaf for `j` and the kernel ideal of `i` the base change along `f'` of that of `j`, étaleness of `f` gives étaleness of `f'`. The affine-local content on each pair of affine opens is the lemma itself, which is already proved for ring maps as `Algebra.Etale.of_ker_sq_eq_bot_of_isBaseChange`; what is proved here is the reduction of the scheme statement to it.”.

> Let
>
> ```
> X --f--→ Y
> |        |
> i        j
> ↓        ↓
> X' -f'-→ Y'
> ```
>
> be a commutative square of schemes with `i` and `j` closed immersions. If the kernel ideal
> sheaf of `j` has square zero, the kernel ideal sheaf of `i` is the base change along `f'` of the
> kernel ideal sheaf of `j`, and `f` is étale, then `f'` is étale. The two hypotheses on `j`
> together say that `j` is a first-order thickening, `Stacks.Thickenings.IsFirstOrderThickening`;
> nothing is assumed about the order of `i`, nor that either closed immersion is surjective on
> points.

```lean
theorem etale_of_isKerBaseChange {i : X ⟶ X'} {f : X ⟶ Y} {f' : X' ⟶ Y'} {j : Y ⟶ Y'}
    [IsClosedImmersion i] [IsClosedImmersion j] (hcomm : i ≫ f' = f ≫ j) (hj : j.ker ^ 2 = ⊥)
    (hbc : IsKerBaseChange i f' j) [Etale f] : Etale f'
```

**`Algebra.Etale.of_ker_sq_eq_bot_of_isBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/Basic/FirstProperties.lean, line 599](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/Basic/FirstProperties.lean#L599). The attribute's comment: “The source's `J = I ⊗_A B` is spelled as bijectivity of the canonical map `B' ⊗[A'] I → J`, i.e. as `IsBaseChange B' f` for the map `f : I → J` induced by `A' → B'`; tensoring over `A'` rather than `A` avoids the `A`-module structure on `I`, which is unavailable to typeclass inference, and asks for the same thing (see the module docstring). The source's hypothesis `J ^ 2 = ⊥` is dropped: it follows from `hI` and the surjectivity half of `hbc`.”.

> Let `A' → A` and `B' → B` be surjective ring maps forming a commutative square with `A' → B'`
> and `A → B`, and write `I = ker (A' → A)`, `J = ker (B' → B)`. If `I` has square zero, `A → B` is
> étale, and `J` is the base change of `I` along `A' → B'` (`J = I ⊗_A B`), then `A' → B'` is étale.

```lean
theorem Algebra.Etale.of_ker_sq_eq_bot_of_isBaseChange
    {A' A B' B : Type*} [CommRing A'] [CommRing A] [CommRing B'] [CommRing B]
    [Algebra A' A] [Algebra A' B'] [Algebra A' B] [Algebra A B] [Algebra B' B]
    [IsScalarTower A' A B] [IsScalarTower A' B' B] [Algebra.Etale A B]
    (hA : Function.Surjective (algebraMap A' A)) (hB : Function.Surjective (algebraMap B' B))
    (hI : RingHom.ker (algebraMap A' A) ^ 2 = ⊥)
    (f : RingHom.ker (algebraMap A' A) →ₗ[A'] RingHom.ker (algebraMap B' B))
    (hf : ∀ x, (f x : B') = algebraMap A' B' (x : A')) (hbc : IsBaseChange B' f) :
    Algebra.Etale A' B'
```

## Tag 00UA, an example

[Tag 00UA](https://stacks.math.columbia.edu/tag/00UA) in the Stacks Project.

**`MvPolynomial.surjective_aeval_universalFactorizationMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/UniversalFactorizationResultant.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/UniversalFactorizationResultant.lean#L145). The attribute's comment: “The symbolic presentation `S = R[b, c]/(a_k(b, c) - a_k)`: the map from `R[b, c]` is surjective.”.

> The `R[a]`-algebra map `R[a][b, c] → S` sending `bᵢ ↦ bᵢ` and `cⱼ ↦ cⱼ` is surjective.

```lean
theorem surjective_aeval_universalFactorizationMap :
    letI := (universalFactorizationMap R n m k hn).toAlgebra
    Function.Surjective (aeval (R := MvPolynomial (Fin n) R) (S₁ := 𝓢)
      (Sum.elim (fun i ↦ X i ⊗ₜ[R] 1) fun j ↦ 1 ⊗ₜ[R] X j))
```

**`MvPolynomial.ker_aeval_universalFactorizationMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/UniversalFactorizationResultant.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/UniversalFactorizationResultant.lean#L156). The attribute's comment: “The symbolic presentation `S = R[b, c]/(a_k(b, c) - a_k)`: the kernel. The polynomial `a_k(b, c)` is the image of `a_k` under `R[a] → S ≃ R[b, c]`.”.

> The kernel of `R[a][b, c] → S` is generated by the relations `aⱼ(b, c) - aⱼ`, where
> `aⱼ(b, c)` is the image of `aⱼ` written as a polynomial in the `b`'s and `c`'s.

```lean
theorem ker_aeval_universalFactorizationMap :
    letI := (universalFactorizationMap R n m k hn).toAlgebra
    RingHom.ker (aeval (R := MvPolynomial (Fin n) R) (S₁ := 𝓢)
      (Sum.elim (fun i ↦ X i ⊗ₜ[R] 1) fun j ↦ 1 ⊗ₜ[R] X j)) =
    Ideal.span (Set.range fun j : Fin n ↦
      (tensorEquivSum R (Fin m) (Fin k) R (universalFactorizationMap R n m k hn (X j))).map C -
        C (X j))
```

**`MvPolynomial.pderiv_universalFactorizationMap_eq_sylvester`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/UniversalFactorizationResultant.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/UniversalFactorizationResultant.lean#L175). The attribute's comment: “The matrix of partial derivatives is the Sylvester matrix of `g` and `h`. Mathlib's `Polynomial.sylvester` is the transpose of the source's matrix, and the variables are ordered by increasing degree; see the module docstring.”.

> The matrix of partial derivatives of the relations `aⱼ(b, c) - aⱼ` with respect to the
> variables `bᵢ`, `cⱼ` is the transpose of the Sylvester matrix of the generic monic polynomials
> `g` and `h` over `R[a][b, c]`. Its rows are indexed by the variables and its columns by the
> relations.

```lean
theorem pderiv_universalFactorizationMap_eq_sylvester :
    (Matrix.of fun (i : Fin m ⊕ Fin k) (j : Fin n) ↦ pderiv i
      ((tensorEquivSum R (Fin m) (Fin k) R (universalFactorizationMap R n m k hn (X j))).map C -
        C (X j))) =
    ((Polynomial.sylvester
      ((Polynomial.freeMonic R m).map ((mapAlgHom (Algebra.ofId R (MvPolynomial (Fin n) R))).comp
        (rename Sum.inl)).toRingHom)
      ((Polynomial.freeMonic R k).map ((mapAlgHom (Algebra.ofId R (MvPolynomial (Fin n) R))).comp
        (rename Sum.inr)).toRingHom) m k).submatrix (finCongr hn) finSumFinEquiv)ᵀ
```

**`MvPolynomial.aeval_pderiv_universalFactorizationMap_eq_transpose_toMatrix_sylvesterMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/UniversalFactorizationResultant.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/UniversalFactorizationResultant.lean#L229). The attribute's comment: “The Sylvester matrix is the transpose of the matrix of the linear map `S[x]_{<m} ⊕ S[x]_{<n} → S[x]_{<n+m}`, `a ⊕ b ↦ ag + bh`, stated for the matrix of partial derivatives with entries in `S`. Mathlib's `Polynomial.sylvesterMap` lists the two summands in the other order; see the module docstring.”.

> In `S`, the matrix of partial derivatives of the relations `aⱼ(b, c) - aⱼ` is the transpose
> of the matrix of the `S`-linear map `S[x]_{<m} × S[x]_{<k} → S[x]_{<m+k}`,
> `(p, q) ↦ g q + h p`, in the monomial bases.

```lean
theorem aeval_pderiv_universalFactorizationMap_eq_transpose_toMatrix_sylvesterMap :
    letI := (universalFactorizationMap R n m k hn).toAlgebra
    (Matrix.of fun (i : Fin m ⊕ Fin k) (j : Fin n) ↦
      aeval (R := MvPolynomial (Fin n) R) (S₁ := 𝓢)
        (Sum.elim (fun i ↦ X i ⊗ₜ[R] 1) fun j ↦ 1 ⊗ₜ[R] X j) (pderiv i
          ((tensorEquivSum R (Fin m) (Fin k) R
            (universalFactorizationMap R n m k hn (X j))).map C - C (X j)))) =
    ((LinearMap.toMatrix
      (((Polynomial.degreeLT.basis 𝓢 m).prod (Polynomial.degreeLT.basis 𝓢 k)).reindex
        finSumFinEquiv)
      (Polynomial.degreeLT.basis 𝓢 (m + k))
      (Polynomial.sylvesterMap 𝐠 𝐡 (Polynomial.natDegree_map_freeMonic_le m _)
        (Polynomial.natDegree_map_freeMonic_le k _))).submatrix (finCongr hn) finSumFinEquiv)ᵀ
```

**`MvPolynomial.aeval_det_pderiv_universalFactorizationMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/UniversalFactorizationResultant.lean, line 256](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/UniversalFactorizationResultant.lean#L256). The attribute's comment: “The determinant `Δ` of the matrix of partial derivatives is the resultant `Res_x(g, h)`.”.

> The determinant `Δ` of the matrix of partial derivatives of the relations `aⱼ(b, c) - aⱼ`,
> with the variables `b₀, …, bₘ₋₁, c₀, …, cₖ₋₁` in this order, is in `S` the resultant
> `Res(g, h)`.

```lean
theorem aeval_det_pderiv_universalFactorizationMap :
    letI := (universalFactorizationMap R n m k hn).toAlgebra
    aeval (R := MvPolynomial (Fin n) R) (S₁ := 𝓢)
      (Sum.elim (fun i ↦ X i ⊗ₜ[R] 1) fun j ↦ 1 ⊗ₜ[R] X j)
      (Matrix.of fun i j : Fin n ↦ pderiv (finSumFinEquiv.symm (finCongr hn i))
        ((tensorEquivSum R (Fin m) (Fin k) R
          (universalFactorizationMap R n m k hn (X j))).map C - C (X j))).det =
    Polynomial.resultant 𝐠 𝐡
```

**`MvPolynomial.etale_localizationAway_resultant_universalFactorizationMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/UniversalFactorizationResultant.lean, line 283](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/UniversalFactorizationResultant.lean#L283). The attribute's comment: “The conclusion: `R → S[1/Δ] = S[1/Res_x(g, h)]` is étale.”.

> `R[a] → S[1/Δ]` is étale, where `Δ = Res(g, h)`.

```lean
theorem etale_localizationAway_resultant_universalFactorizationMap :
    letI := (universalFactorizationMap R n m k hn).toAlgebra
    Algebra.Etale (MvPolynomial (Fin n) R) (Localization.Away (Polynomial.resultant 𝐠 𝐡))
```

**`MvPolynomial.tfae_universalFactorizationMap_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/UniversalFactorizationResultant.lean, line 330](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/UniversalFactorizationResultant.lean#L330). The attribute's comment: “For a prime `q ⊂ S`: (1) `R → S` is étale at `q`, (2) `Δ = Res_x(g, h) ∉ q`, (3) the images of `g, h` in `κ(q)[x]` are relatively prime, are equivalent. Étale at `q` is the source's definition, `∃ f ∉ q, Algebra.Etale R (Localization.Away f)`.”.

> For a prime `q` of `S` the following are equivalent: `R[a] → S` is étale at `q`, that is,
> `R[a] → S_f` is étale for some `f ∉ q`; `Δ = Res(g, h) ∉ q`; the images of `g` and `h` in
> `κ(q)[x]` are coprime.

```lean
theorem tfae_universalFactorizationMap_etale (q : Ideal 𝓢) [q.IsPrime] :
    letI := (universalFactorizationMap R n m k hn).toAlgebra
    List.TFAE [∃ f ∉ q, Algebra.Etale (MvPolynomial (Fin n) R) (Localization.Away f),
      Polynomial.resultant 𝐠 𝐡 ∉ q,
      IsCoprime (𝐠.map (algebraMap 𝓢 q.ResidueField)) (𝐡.map (algebraMap 𝓢 q.ResidueField))]
```

**`MvPolynomial.exists_mulVec_sylvester_map_eq_zero_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/UniversalFactorizationResultant.lean, line 353](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/UniversalFactorizationResultant.lean#L353). The attribute's comment: “The reason given for (2) ⇔ (3): the image of the Sylvester matrix in `Mat(n + m, κ(q))` has a kernel if and only if `ḡ, h̄` have a factor in common. Mathlib's `Polynomial.sylvester` is the transpose of the source's matrix; a square matrix over a field and its transpose have a nonzero kernel simultaneously.”.

> For a prime `q` of `S`, the Sylvester matrix of the images of `g` and `h` in `κ(q)[x]` has a
> nonzero kernel if and only if these images have a common factor which is not a unit.

```lean
theorem exists_mulVec_sylvester_map_eq_zero_iff (q : Ideal 𝓢) [q.IsPrime] :
    (∃ v ≠ 0, Polynomial.sylvester (𝐠.map (algebraMap 𝓢 q.ResidueField))
      (𝐡.map (algebraMap 𝓢 q.ResidueField)) m k *ᵥ v = 0) ↔
    ∃ d, d ∣ 𝐠.map (algebraMap 𝓢 q.ResidueField) ∧ d ∣ 𝐡.map (algebraMap 𝓢 q.ResidueField) ∧
      ¬IsUnit d
```

**`MvPolynomial.isEtaleAt_universalFactorizationMap_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/UniversalFactorizationResultant.lean, line 377](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/UniversalFactorizationResultant.lean#L377). The attribute's comment: “(1) ⇔ (2), with étale at `q` read as Mathlib's `Algebra.IsEtaleAt`, which agrees with the source's definition since `S` is of finite presentation over `R`.”.

> `R[a] → S` is étale at a prime `q` of `S` in the sense of `Algebra.IsEtaleAt` if and only if
> `Δ = Res(g, h) ∉ q`.

```lean
theorem isEtaleAt_universalFactorizationMap_iff (q : Ideal 𝓢) [q.IsPrime] :
    letI := (universalFactorizationMap R n m k hn).toAlgebra
    Algebra.IsEtaleAt (MvPolynomial (Fin n) R) q ↔ Polynomial.resultant 𝐠 𝐡 ∉ q
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.143, Tag 00U0](https://stacks.math.columbia.edu/tag/00U0)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
