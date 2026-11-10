---
declaration: section
origin: cited
lean: Stacks.Cohomology.MonoidalComplexesOfModules.symmetricMonoidalComplexes, Stacks.SheafOfModules.Strict.dualComplexOfLocallyStrictlyPerfect, Stacks.SheafOfModules.Strict.dualComplex, Stacks.SheafOfModules.Strict.exactPairingDualComplex, Stacks.SheafOfModules.Strict.exactPairingDualComplexOfLocallyStrictlyPerfect, Stacks.SheafOfModules.termwiseExactPairingDualSheaf, Stacks.SheafOfModules.Strict.isLocallyStrictlyPerfect_and_isoDualComplex_of_exactPairing, Stacks.SheafOfModules.isIso_tensorDualToSheafHom_of_localSummand
statement: formalized
proof: formalized
---

# 21.48 Duals

Section 21.48 of the Stacks Project, [Tag 0FPP](https://stacks.math.columbia.edu/tag/0FPP). 8 tags here are carried by 32 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FPQ, a lemma

[Tag 0FPQ](https://stacks.math.columbia.edu/tag/0FPQ) in the Stacks Project.

**`Stacks.Cohomology.MonoidalComplexesOfModules.symmetricMonoidalComplexes`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Monoidal/ComplexesOfModules.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Monoidal/ComplexesOfModules.lean#L133). References: SGA 4 XVII (4.1.6), “⊗ on complexes”.

> Complexes of modules on any ringed site form a symmetric monoidal category; its tensor
> bifunctor is totalized sheaf tensor.

```lean
public def symmetricMonoidalComplexes : SymmetricMonoidalComplexes R
```

## Tag 0FPR, an example

[Tag 0FPR](https://stacks.math.columbia.edu/tag/0FPR) in the Stacks Project.

**`Stacks.SheafOfModules.Strict.dualComplexOfLocallyStrictlyPerfect`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Duals/DualComplexOfALocallyStrictlyPerfectComplex.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Duals/DualComplexOfALocallyStrictlyPerfectComplex.lean#L157). The attribute's comment: “the construction of the complex `𝒢^• = SheafHom^•(ℱ^•, 𝒪)` under the tag's OWN hypothesis — that every object of the site has a covering on whose members `ℱ^•` is strictly perfect — rather than under the termwise condition that `Stacks.SheafOfModules.Strict.dualComplex` assumes. The terms and the signed-transpose differential are `dualComplex_X` and `dualComplex_d`, through which this is the same complex. NOT the left-dual assertion of the tag, which for this same complex is `Stacks.SheafOfModules.Strict.exactPairingDualComplexOfLocallyStrictlyPerfect`: `Stacks.SheafOfModules.Strict.exactPairingDualComplex` proves it only for a complex vanishing outside one global finite set of degrees, and the hypothesis here bounds `ℱ^•` only locally, so `η = ∑ ηₙ` is a locally finite sum of morphisms and has to be produced from its components”.

> **The dual complex `𝒢^• = SheafHom^•(ℱ^•, 𝒪)` of [Stacks, Tag 0FPR], under the hypothesis
> of the tag.** Its degree-`j` term is the dual sheaf `SheafHom(ℱ^{-j}, 𝒪)` and its differential
> is the signed transpose `d_𝒢^j = -(-1)^j (d_ℱ^{-j-1})^∨`, exactly as in
> `Stacks.SheafOfModules.Strict.dualComplex`; what is new is that the hypothesis is the tag's own
> local one, not the termwise condition extracted from it.

```lean
def dualComplexOfLocallyStrictlyPerfect (hK : IsLocallyStrictlyPerfect R K) :
    CochainComplex (Mod R) ℤ
```

**`Stacks.SheafOfModules.Strict.dualComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Duals/DualComplexOfModules.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Duals/DualComplexOfModules.lean#L138). The attribute's comment: “the construction of the complex `𝒢^• = SheafHom^•(ℱ^•, 𝒪)`: its degree-`j` term is the dual sheaf `SheafHom(ℱ^{-j}, 𝒪)` of Tag 0FNY — the single surviving factor of the degree-`j` term of the Hom complex of Tag 0A8X into `𝒪` placed in degree zero — and its differential is the signed transpose `d_𝒢^j = -(-1)^j (d_ℱ^{-j-1})^∨` of Tag 0FNK. The remaining assertion of the tag, that `𝒢^•` with `η = ∑ ηₙ` and `ε = ∑ εₙ` is a left dual of `ℱ^•`, is `Stacks.SheafOfModules.Strict.exactPairingDualComplex`, and under the tag's OWN hypothesis `Stacks.SheafOfModules.Strict.exactPairingDualComplexOfLocallyStrictlyPerfect`. Only the termwise half of the tag's hypothesis is assumed here; the same complex under the tag's OWN hypothesis is `Stacks.SheafOfModules.Strict.dualComplexOfLocallyStrictlyPerfect`”. References: SGA 4 XVII (1.1.6), “special case”.

> **The dual complex `𝒢^• = SheafHom^•(ℱ^•, 𝒪)` of [Stacks, Tag 0FPR].** Its degree-`j` term
> is the dual sheaf `SheafHom(ℱ^{-j}, 𝒪)` of [Stacks, Tag 0FNY], and its differential is the
> signed transpose `d_𝒢^j = -(-1)^j (d_ℱ^{-j-1})^∨`, the sign convention of [Stacks, Tag 0FNK].

```lean
def dualComplex : CochainComplex (Mod R) ℤ
```

**`Stacks.SheafOfModules.Strict.exactPairingDualComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Duals/DualComplexOfModules.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Duals/DualComplexOfModules.lean#L187). The attribute's comment: “the left-dual assertion: `𝒢^•` with `η = ∑ ηₙ` and `ε = ∑ εₙ`, the coevaluations and evaluations of Tag 0FNY at the terms, satisfies the two triangle identities of Tag 0FFP in the monoidal category of complexes of Tag 0FPQ. The complex `𝒢^•` is `Stacks.SheafOfModules.Strict.dualComplex`, whose terms and signed-transpose differential are `dualComplex_X` and `dualComplex_d`. NOT under the tag's own hypothesis: that every object has a covering on which `ℱ^•` is strictly perfect gives the termwise local finiteness assumed here, but boundedness only locally, whereas `s` is one global finite set of degrees. The same conclusion under the tag's own hypothesis, with `η = ∑ ηₙ` made sense of as a locally finite sum, is `Stacks.SheafOfModules.Strict.exactPairingDualComplexOfLocallyStrictlyPerfect`; the converse local boundedness is `Stacks.SheafOfModules.Strict.isLocallyBounded_of_exactPairing`”.

> **[Stacks, Tag 0FPR] for a complex of bounded support.** Let `ℱ^•` be a complex of
> `𝒪`-modules each of whose terms is, locally on the site, a direct summand of a finite free
> `𝒪`-module, and suppose `ℱ^•` vanishes outside a finite set `s` of degrees. Then the complex
> `𝒢^• = SheafHom^•(ℱ^•, 𝒪)`, together with `η = ∑ ηₙ` and `ε = ∑ εₙ` assembled from the
> coevaluations and evaluations of [Stacks, Tag 0FNY], is a left dual of `ℱ^•` in the monoidal
> category of complexes of `𝒪`-modules of [Stacks, Tag 0FPQ]: both triangle identities hold.

```lean
def exactPairingDualComplex (s : Finset ℤ) (hb : ∀ m, m ∉ s → IsZero (F.X m)) :
    @ExactPairing _ _ (monoidalCategoryCochainComplex R) F (dualComplex R F hF)
```

**`Stacks.SheafOfModules.Strict.exactPairingDualComplexOfLocallyStrictlyPerfect`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Duals/LeftDualOfALocallyStrictlyPerfectComplex.lean, line 251](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Duals/LeftDualOfALocallyStrictlyPerfectComplex.lean#L251). The attribute's comment: “the WHOLE assertion of the tag under the tag's OWN hypothesis: for a complex `ℱ^•` of 𝒪-modules such that every object of the site has a covering on whose members `ℱ^•` is strictly perfect (Tag 08FL), the complex `𝒢^• = SheafHom^•(ℱ^•, 𝒪)` together with η = ∑ ηₙ and ε = ∑ εₙ — the coevaluations and evaluations of Tag 0FNY at the terms — is a left dual of `ℱ^•` in the monoidal category of complexes of Tag 0FPQ, i.e. both triangle identities of Tag 0FFP hold. No boundedness is assumed: `Stacks.SheafOfModules.Strict.exactPairingDualComplex` proves the same conclusion only for a complex vanishing outside one global finite set of degrees, and the hypothesis here bounds `ℱ^•` only locally, so that η = ∑ ηₙ is a locally finite sum. It is produced from its components, the degree-zero part of `ℱ^• ⊗ 𝒢^•` being a coproduct of locally finitely many nonzero summands and therefore also their product (`Stacks.SheafOfModules.CoproductSheafification.isIso_coprodToProd`). The complex `𝒢^•` is `Stacks.SheafOfModules.Strict.dualComplexOfLocallyStrictlyPerfect`, with terms and signed-transpose differential `dualComplexOfLocallyStrictlyPerfect_X` and `dualComplex_d`. The converse, that a complex with a left dual is locally strictly perfect and has this very complex with these very pairings as its left dual, is Tag 0FPS, `Stacks.SheafOfModules.Strict.exists_dualComplexIso_of_exactPairing`”.

> **[Stacks, Tag 0FPR].** Let `(C, 𝒪)` be a ringed site and let `ℱ^•` be a complex of
> `𝒪`-modules such that for every object `U` of `C` there exists a covering `{U_i → U}` with
> `ℱ^•|_{U_i}` strictly perfect. Then the complex `𝒢^• = SheafHom^•(ℱ^•, 𝒪)`, together with
> `η = ∑ ηₙ` and `ε = ∑ εₙ` assembled from the coevaluations and evaluations of
> [Stacks, Tag 0FNY] at the terms, is a **left dual** of `ℱ^•` in the monoidal category of
> complexes of `𝒪`-modules of [Stacks, Tag 0FPQ]: both triangle identities hold.
>
> The hypothesis is the tag's own and nothing else is assumed: in particular `ℱ^•` is bounded only
> locally, so `η` is only a locally finite sum. It exists because the degree-zero part of
> `ℱ^• ⊗ 𝒢^•` is a coproduct whose summands locally all but finitely many vanish, hence is also
> the product, and a morphism into it is given by — and determined by — its components.

```lean
def exactPairingDualComplexOfLocallyStrictlyPerfect (hK : IsLocallyStrictlyPerfect R K) :
    @ExactPairing _ _ (monoidalCategoryCochainComplex R) K
      (dualComplexOfLocallyStrictlyPerfect R K hK)
```

**`Stacks.SheafOfModules.termwiseExactPairingDualSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Duals/TermwiseDualsOfAComplexOfModules.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Duals/TermwiseDualsOfAComplexOfModules.lean#L155). The attribute's comment: “the degreewise pairings only: for each n the dual sheaf `SheafHom(ℱⁿ, 𝒪)` is a left dual of the term `ℱⁿ`, with the coevaluation ηₙ and evaluation εₙ of Tag 0FNY, in the monoidal category of 𝒪-modules `Strict.monoidalCategory`. NOT the assertion of the tag, which is about the complex `𝒢^• = SheafHom^•(ℱ^•, 𝒪)`: neither the sums η = ∑ ηₙ and ε = ∑ εₙ, nor the triangle identities for them, nor the left-dual property of `𝒢^•` in the monoidal category of complexes of Tag 0FPQ, is proved here. Those three are proved over a site by `Stacks.SheafOfModules.Strict.dualComplex` and `Stacks.SheafOfModules.Strict.exactPairingDualComplex`, for a complex of globally bounded support. The construction of `𝒢^•` is available under the tag's own hypothesis, that every object has a covering on which `ℱ^•` is strictly perfect, as `Stacks.SheafOfModules.Strict.dualComplexOfLocallyStrictlyPerfect`, and the left-dual assertion under that hypothesis is `Stacks.SheafOfModules.Strict.exactPairingDualComplexOfLocallyStrictlyPerfect`. See the module's Implementation notes”.

> **[Stacks, Tag 0FPR], the degreewise pairings.** For each degree `n`, the dual sheaf
> `SheafHom(ℱ^n, 𝒪)` is a left dual of the term `ℱ^n` in the monoidal category of `𝒪`-modules:
> the coevaluation `ηₙ : 𝒪 ⟶ ℱ^n ⊗ SheafHom(ℱ^n, 𝒪)` and the evaluation
> `εₙ : SheafHom(ℱ^n, 𝒪) ⊗ ℱ^n ⟶ 𝒪` of [Stacks, Tag 0FNY] satisfy the two triangle identities.
>
> These are exactly the `ηₙ` and `εₙ` that [Stacks, Tag 0FPR] sums to form `η` and `ε`.

```lean
public def termwiseExactPairingDualSheaf
    (hF : IsTermwiseLocallyDirectSummandOfFiniteFree 𝒪 h𝒪 F) (n : ℤ) :
    ExactPairing (F.X n) (dualSheaf 𝒪 h𝒪 (F.X n))
```

## Tag 0FPS, a lemma

[Tag 0FPS](https://stacks.math.columbia.edu/tag/0FPS) in the Stacks Project.

**`Stacks.SheafOfModules.Strict.isLocallyStrictlyPerfect_and_isoDualComplex_of_exactPairing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Duals/ComplexWithALeftDual.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Duals/ComplexWithALeftDual.lean#L157). The attribute's comment: “the WHOLE tag, under the tag's OWN hypothesis that `ℱ^•` has a left dual `𝒢^•` in the monoidal category of complexes of 𝒪-modules of Tag 0FPQ, whose tensor product is the one of Tag 01CA. Both conclusions: every object of the site has a covering on whose members `ℱ^•` is strictly perfect in the sense of Tag 08FL — the witness `Stacks.SheafOfModules.Strict.IsLocallyStrictlyPerfect`, unfolding to the covering sieve and `IsStrictlyPerfect` of the restricted complex — and `𝒢^•` is the left dual of Example 0FPR with its pairings: it is isomorphic to `Stacks.SheafOfModules.Strict.dualComplexOfLocallyStrictlyPerfect`, the complex `SheafHom^•(ℱ^•, 𝒪)`, by an isomorphism matching the coevaluation and the evaluation of the given pairing with those of `Stacks.SheafOfModules.Strict.exactPairingDualComplexOfLocallyStrictlyPerfect`, the η = ∑ ηₙ and ε = ∑ εₙ of that example — which is uniqueness of left duals (Tag 0FFR)”.

> **[Stacks, Tag 0FPS]**. Let `(C, 𝒪)` be a ringed site and `ℱ^•` a complex of `𝒪`-modules with a
> left dual `𝒢^•` in the monoidal category of complexes of `𝒪`-modules. Then every object of the site
> has a covering on whose members `ℱ^•` is strictly perfect, and the left dual is the complex of
> [Stacks, Tag 0FPR] together with its pairings.

```lean
theorem isLocallyStrictlyPerfect_and_isoDualComplex_of_exactPairing
    (p : @ExactPairing _ _ (monoidalCategoryCochainComplex R) K L) :
    letI := monoidalCategoryCochainComplex R
    letI := p
    letI := exactPairingDualComplexOfLocallyStrictlyPerfect
      (isLocallyStrictlyPerfect_of_exactPairing R K L p)
    IsLocallyStrictlyPerfect R K ∧
      ∃ e : L ≅ dualComplexOfLocallyStrictlyPerfect R K
          (isLocallyStrictlyPerfect_of_exactPairing R K L p),
        η_ K L ≫ K ◁ e.hom =
            η_ K (dualComplexOfLocallyStrictlyPerfect R K
              (isLocallyStrictlyPerfect_of_exactPairing R K L p)) ∧
          e.hom ▷ K ≫ ε_ K (dualComplexOfLocallyStrictlyPerfect R K
              (isLocallyStrictlyPerfect_of_exactPairing R K L p)) = ε_ K L
```

## Tag 08JJ, a lemma

[Tag 08JJ](https://stacks.math.columbia.edu/tag/08JJ) in the Stacks Project.

**`Stacks.SheafOfModules.isIso_tensorDualToSheafHom_of_localSummand`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorDualSheafHom.lean, line 543](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorDualSheafHom.lean#L543). The attribute's comment: “step (5) of the proof only: the canonical map `F ⊗_𝒪 SheafHom(E, 𝒪) ⟶ SheafHom(E, F)` is an isomorphism for `E` locally a summand of a finite free module and `F` arbitrary. None of the tag's four assertions is proved here; in particular the derived statement `M ⊗^L_𝒪 K^∨ ≅ RSheafHom(K, M)` for perfect `K` is not, and still needs a complex-level comparison with its Koszul signs, the tensor-side analogue of Tag 08JH, locality of the derived tensor product on a slice, and a K-flat representative on a ringed site.”. References: EGA 0 (5.4.2), “more general”; SGA 5 IIIB (5.0), “more general”.

> **Step (5) of the proof of Stacks 08JJ.** Let `(C, 𝒪)` be a ringed site, let `E` be a sheaf of
> `𝒪`-modules which is locally a direct summand of a finite free sheaf of modules, and let `F` be an
> arbitrary sheaf of `𝒪`-modules. Then the canonical map
>
> `F ⊗_𝒪 SheafHom(E, 𝒪) ⟶ SheafHom(E, F)`
>
> is an isomorphism.
>
> The map is `Stacks.SheafOfModules.tensorDualToSheafHom`, pinned down on local sections by
> `Stacks.SheafOfModules.tensorDualToSheafHom_toTensorSheafSection`. At `E = F` this is the first
> assertion of Tag 0FNY, `Stacks.SheafOfModules.isIso_tensorDualToEndomorphism_of_localSummand`.
>
> The hypothesis is the one of Tag 0FNY, that `E` is a summand of a finite free module *locally*;
> Stacks 08JJ's step (5) asks for a global summand, which is a special case.

```lean
theorem isIso_tensorDualToSheafHom_of_localSummand
    (hE : IsLocallyDirectSummandOfFiniteFree 𝒪 h𝒪 E) :
    IsIso (tensorDualToSheafHom 𝒪 h𝒪 E F)
```

**`AlgebraicGeometry.RingedSite.isIso_derivedSheafHomEvaluation_of_coversTop`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/EvaluationLocality.lean, line 289](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/EvaluationLocality.lean#L289). The attribute's comment: “the locality step for the evaluation morphism of Tag 0A97 only: invertibility of `ev : RSheafHom(L, M) ⊗^L_O K ⟶ RSheafHom(RSheafHom(K, L), M)`, and hence of the bidual map `K ⟶ (K^∨)^∨` of `AlgebraicGeometry.RingedSite.derivedBidual`, may be checked after restriction to the slices over a family of objects covering the final object, where it becomes quasi-isomorphy of the evaluation morphism of internal Hom complexes of Tag 0A92. NONE of the four assertions of Tag 08JJ is proved here and in particular the bidual map is NOT shown to be invertible for a perfect K: quasi-isomorphy over each member of the covering family is a HYPOTHESIS below. The base case that discharges it — that `evaluationMap` is a quasi-isomorphism when its source complex is strictly perfect (Tag 08FL) — is `AlgebraicGeometry.RingedSite.quasiIso_evaluationMap_of_isStrictlyPerfect`, and the second assertion of Tag 08JJ follows from the two together, in `AlgebraicGeometry.RingedSite.isIso_derivedBidual_of_isPerfect`. The reduction performed here is the same one `Stacks.SheafOfModules.isIso_of_coversTop_mapDerivedCategory` performs for an arbitrary morphism of `D(Mod(O))`, but carried out at the chain level, because the derived evaluation morphism has no restriction compatibility of its own; the chain-level square it uses is `AlgebraicGeometry.RingedSite.evaluationMap_restrict_square`”.

> **Invertibility of the evaluation morphism of derived internal Homs is local on the site.**
> Let `V : ι → C` be a family of objects covering the final object of the site, let `A` be a K-flat
> complex representing `K`, and let `B` and `C` be K-injective complexes representing `L` and `M`.
> If the evaluation morphism of internal Hom complexes of Stacks 0A92 formed over each `V i`, at
> the restrictions of `A`, `B` and `C`, is a quasi-isomorphism, then the evaluation morphism of
> derived internal Homs of Stacks 0A97 at `K`, `L`, `M` is an isomorphism.

```lean
theorem isIso_derivedSheafHomEvaluation_of_coversTop
    (K L M : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    {A B C : CochainComplex (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) ℤ}
    (hA : Stacks.SheafOfModules.IsKFlat X.O A) [B.IsKInjective] [C.IsKInjective]
    (eA : DerivedCategory.Q.obj A ≅ K) (eB : DerivedCategory.Q.obj B ≅ L)
    (eC : DerivedCategory.Q.obj C ≅ M)
    {ι : Type*} {V : ι → X.C} (hV : X.J.CoversTop V)
    (h : ∀ i, QuasiIso (evaluationMap (X.over (V i)) (restrictComplex X A (V i))
      (restrictComplex X B (V i)) (restrictComplex X C (V i)))) :
    IsIso (derivedSheafHomEvaluation X T Hd K L M)
```

**`AlgebraicGeometry.RingedSite.isIso_derivedBidual_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/EvaluationPerfect.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/EvaluationPerfect.lean#L155). The attribute's comment: “the canonical map `K ⟶ (K^∨)^∨` is an isomorphism for a perfect object `K` of `D(O)`, where `K^∨` is the derived dual `RSheafHom_O(K, O)`; this is one of the four assertions of the tag, and the hypothesis is perfection of `K` alone”.

> **The bidual map of a perfect object is an isomorphism.** For a perfect object
> `K` of `D(O)` the canonical map
>
> `K ⟶ (K^∨)^∨`
>
> of `AlgebraicGeometry.RingedSite.derivedBidual` is an isomorphism, where `K^∨` is the derived
> dual `RSheafHom(K, O)`.

```lean
theorem isIso_derivedBidual_of_isPerfect
    (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (hK : X.IsPerfect K) :
    IsIso (derivedBidual X T K)
```

**`AlgebraicGeometry.RingedSite.isPerfect_derivedDual`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/Duals.lean, line 267](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/Duals.lean#L267). The attribute's comment: “the dual of a perfect object is perfect”. References: SGA 6 I (7.3), “perfect ⇒ dual perfect”; SGA 6 III (4.9), “Case S = X = Y”.

> **Stacks 08JJ, first assertion.** Let `(C, O)` be a ringed site and let `K` be a perfect
> object of `D(O)`. Then the dual `K^∨ = RSheafHom(K, O)` is perfect as well.
>
> Perfectness is local, so it is enough to model `K^∨` above a covering of each object of the
> site. Over a member `V` on which `K` is modelled by a strictly perfect complex `E`, the
> restriction of `K^∨` is `RSheafHom(K|_V, O|_V)` by Stacks 08JB, which is the class of the
> internal Hom complex `SheafHom(E, O|_V)` by Stacks 08JH; and that complex is strictly perfect
> because the dual of a direct summand of a finite free module is again one.

```lean
theorem isPerfect_derivedDual
    (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (hK : X.IsPerfect K) : X.IsPerfect (derivedDual X K)
```

**`AlgebraicGeometry.RingedSite.derivedDualTensorSheafHomIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/DualTensorSheafHom.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/DualTensorSheafHom.lean#L196). The attribute's comment: “the isomorphism M ⊗^L_O K^∨ ≅ RSheafHom_O(K, M) for perfect K; not the invertibility of the canonical map of Stacks 08JD, which is a different morphism of the same type”.

> **Stacks 08JJ: tensoring with the dual of a perfect object is derived internal Hom.** Let
> `(C, O)` be a ringed site, let `K` be a perfect object of `D(O)` with dual
> `K^∨ = RSheafHom(K, O)`, and let `M` be an arbitrary object of `D(O)`. Then
>
> `M ⊗^L_O K^∨ ≅ RSheafHom_O(K, M)`.
>
> It is the diagonal morphism of Stacks 0BYS at tensor factor `M`, internal-Hom source `K` and
> target the structure sheaf in degree zero — invertible by Stacks 0ATN because `K` is perfect,
> its source being `M ⊗^L_O RSheafHom(K, O) = M ⊗^L_O K^∨` — followed by the internal Hom out of
> `K` of the right unit constraint `M ⊗^L_O O ≅ M` of Stacks 0FPT.

```lean
def derivedDualTensorSheafHomIso
    (K M : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (hK : X.IsPerfect K) :
    ((Stacks.SheafOfModules.derivedTensorProductFunctor X).obj M).obj (derivedDual X K) ≅
      ((derivedSheafHomBifunctor X).obj (op K)).obj M
```

**`AlgebraicGeometry.RingedSite.derivedDualTensorSheafHomIso_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/DualTensorSheafHom.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/DualTensorSheafHom.lean#L212). The attribute's comment: “that isomorphism is functorial in M”.

> **Stacks 08JJ: the isomorphism is functorial in `M`.** This is the functoriality the source
> asserts: the diagonal of Stacks 0BYS is natural in its tensor factor and the right unit
> constraint of Stacks 0FPT is natural, so the composite of the two is.

```lean
theorem derivedDualTensorSheafHomIso_naturality
    (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (hK : X.IsPerfect K)
    {M M' : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))}
    (f : M ⟶ M') :
    ((Stacks.SheafOfModules.derivedTensorProductFunctor X).map f).app (derivedDual X K) ≫
        (derivedDualTensorSheafHomIso X K M' hK).hom =
      (derivedDualTensorSheafHomIso X K M hK).hom ≫
        ((derivedSheafHomBifunctor X).obj (op K)).map f
```

**`AlgebraicGeometry.RingedSite.derivedDualTensorGlobalSectionsEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/DualTensorSheafHom.lean, line 276](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/DualTensorSheafHom.lean#L276). The attribute's comment: “the identification H⁰(C, M ⊗^L_O K^∨) = Hom_{D(O)}(K, M) for perfect K, as an isomorphism of abelian groups; not the bijectivity of the induced map of Stacks 08JD”.

> **Stacks 08JJ: `H⁰(C, M ⊗^L_O K^∨) = Hom_{D(O)}(K, M)` for perfect `K`.** The degree-zero
> global hypercohomology of `M ⊗^L_O K^∨` is the group of morphisms `K ⟶ M` in `D(O)`.
>
> It is the degree-zero global hypercohomology of `derivedDualTensorSheafHomIso`, which is an
> isomorphism of abelian groups because derived global sections and the degree-zero cohomology
> functor both preserve isomorphisms, followed by the identification
> `H⁰(C, RSheafHom(K, M)) = Hom_{D(O)}(K, M)` of Stacks 08JA.

```lean
def derivedDualTensorGlobalSectionsEquiv
    (K M : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (hK : X.IsPerfect K) :
    ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} 0).obj
        ((derivedModuleGlobalSections X).obj
          (((Stacks.SheafOfModules.derivedTensorProductFunctor X).obj M).obj
            (derivedDual X K))) : Type u) ≃+ (K ⟶ M)
```

**`AlgebraicGeometry.RingedSite.isIso_derivedTensorDualToSheafHom_of_isPerfect_canonical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/DualTensorSheafHomCanonical.lean, line 482](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/DualTensorSheafHomCanonical.lean#L482). The attribute's comment: “the canonical map M ⊗^L_O L^∨ ⟶ RSheafHom_O(L, M) of Stacks 08JD is an isomorphism for a perfect L”.

> **Stacks 08JJ, third assertion, for the canonical map of Stacks 08JD.** Let `(C, O)` be a
> ringed site, let `L` be a **perfect** object of `D(O)` with dual `L^∨ = RSheafHom(L, O)` and let
> `M` be an arbitrary object of `D(O)`. Then the canonical map
>
> `M ⊗^L_O L^∨ ⟶ RSheafHom(L, M)`
>
> of Stacks 08JD, `AlgebraicGeometry.RingedSite.derivedTensorDualToSheafHom`, is an isomorphism.
>
> The isomorphism itself was already in the library as
> `AlgebraicGeometry.RingedSite.derivedDualTensorSheafHomIso`, the diagonal of Stacks 0BYS at
> target object the structure sheaf; what is proved here is that the *canonical* map of
> Stacks 08JD is that diagonal, so that the invertibility supplied by Stacks 0ATN applies to it.
> The comparison is
> `AlgebraicGeometry.RingedSite.derivedTensorDualToSheafHom_comp_derivedSheafHomComparison`, whose
> chain-level content is `AlgebraicGeometry.RingedSite.tensorHomInterchange_comp_homMap`: the
> interchange morphism of Stacks 0BYR is the diagonal of Stacks 0A93 tensored with the identity
> followed by the composition morphism of Stacks 0A91, so no Koszul sign separates the two
> morphisms.

```lean
theorem isIso_derivedTensorDualToSheafHom_of_isPerfect_canonical
    (L M : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (hL : X.IsPerfect L) :
    IsIso (derivedTensorDualToSheafHom X
      (Stacks.SheafOfModules.canonicalDerivedTensorProduct X) L M)
```

**`Stacks.SheafOfModules.isIso_of_coversTop_mapDerivedCategory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Slice/DerivedIsomorphismLocality.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Slice/DerivedIsomorphismLocality.lean#L112). The attribute's comment: “the locality step of the proof only: invertibility of a morphism of `D(Mod(O))` may be checked after restriction to the slices over a family of objects covering the final object. Stacks 08JJ uses this reduction twice, for the bidual map `K ⟶ (K^∨)^∨` and for the canonical map `M ⊗^L_O K^∨ ⟶ RSheafHom_O(K, M)`; neither of those maps is shown to be an isomorphism here, and none of the tag's four assertions is proved here.”.

> **Invertibility in the derived category of sheaves of modules is local on the site.** Let
> `V : ι → C` be a family of objects covering the final object of the site. A morphism of
> `D(Mod(R))` whose image under restriction to the slice site over each `V i` is an isomorphism
> is itself an isomorphism.

```lean
theorem isIso_of_coversTop_mapDerivedCategory {ι : Type*} {V : ι → C} (hV : J.CoversTop V)
    {K L : DerivedCategory (SheafOfModules.{w} R)} (f : K ⟶ L)
    (hf : ∀ i, IsIso ((SheafOfModules.overFunctor.{w} R (V i)).mapDerivedCategory.map f)) :
    IsIso f
```

## Tag 0FPT, a lemma

[Tag 0FPT](https://stacks.math.columbia.edu/tag/0FPT) in the Stacks Project.

**`Stacks.DerivedTensor.RingedSite.DerivedTensorProduct.braidingIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/DerivedSymmetryAndUnit.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/DerivedSymmetryAndUnit.lean#L116). The attribute's comment: “the commutativity constraint at a pair of objects, as an isomorphism; not the monoidal structure and not its coherence axioms”.

> **[Stacks, Tag 0FPT], the commutativity constraint.** The derived tensor product of two
> objects of `D(𝒪)` is symmetric: `A ⊗^L_𝒪 B ≅ B ⊗^L_𝒪 A`.
>
> Both objects are replaced by their chosen K-flat models, on which the derived tensor product is
> the ordinary total tensor complex; there the isomorphism is the Koszul symmetry
> `Stacks.SheafOfModules.Tensor.tensorComplexFlipIso`.

```lean
def braidingIso (A B : DerivedModules X.O) :
    (T.tensor.obj A).obj B ≅ (T.tensor.obj B).obj A
```

**`Stacks.DerivedTensor.RingedSite.DerivedTensorProduct.rightUnitIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/DerivedSymmetryAndUnit.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/DerivedSymmetryAndUnit.lean#L139). The attribute's comment: “the unit constraint on the right at an object, as an isomorphism; not the monoidal structure and not its coherence axioms”.

> **[Stacks, Tag 0FPT], the unit constraint on the right.** The structure sheaf in degree zero
> is a unit for the derived tensor product: `A ⊗^L_𝒪 𝒪 ≅ A`.
>
> The right factor is already K-flat by `Stacks.SheafOfModules.isKFlat_single_unit`, so only the
> left factor is replaced by its chosen K-flat model; on representatives the statement is the
> ordinary unit law `Stacks.SheafOfModules.tensorComplexUnitIso`.

```lean
def rightUnitIso (A : DerivedModules X.O) :
    (T.tensor.obj A).obj (unitObject X) ≅ A
```

**`Stacks.DerivedTensor.RingedSite.DerivedTensorProduct.leftUnitIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/DerivedSymmetryAndUnit.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/DerivedSymmetryAndUnit.lean#L154). The attribute's comment: “the unit constraint on the left at an object, as an isomorphism; not the monoidal structure and not its coherence axioms”.

> **[Stacks, Tag 0FPT], the unit constraint on the left.** The structure sheaf in degree zero
> is a unit for the derived tensor product on the other side too: `𝒪 ⊗^L_𝒪 A ≅ A`.
>
> It is the right unit constraint read through the commutativity constraint.

```lean
def leftUnitIso (A : DerivedModules X.O) :
    (T.tensor.obj (unitObject X)).obj A ≅ A
```

**`Stacks.SheafOfModules.DerivedMonoidal.symmetricMonoidalDerivedTensor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Monoidal/DerivedTensorConstraints.lean, line 198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Monoidal/DerivedTensorConstraints.lean#L198).

> **The derived category of modules on a ringed site is a symmetric monoidal category with
> tensor product the derived tensor product and the usual associativity and commutativity
> constraints**, the latter being those of the total tensor product of complexes with the Koszul
> sign convention.

```lean
public def symmetricMonoidalDerivedTensor : SymmetricMonoidalDerivedTensor R
```

## Tag 0FPU, an example

[Tag 0FPU](https://stacks.math.columbia.edu/tag/0FPU) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.isIso_derivedTensorDualToSheafHom_self`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/DerivedDualLeftDual.lean, line 268](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/DerivedDualLeftDual.lean#L268). The attribute's comment: “tensor_hom_iso”. References: SGA 5 IIIB (5.0).

> **Stacks 0FPU: the canonical map `K ⊗^𝐋_O K^∨ ⟶ R𝓗om_O(K, K)` is an isomorphism.**  For a
> perfect object `K` of `D(O)` the canonical map of Stacks 08JD at `M = K` is invertible.
>
> This is the assertion Stacks 0FPU cites, from [Stacks, Tag 08JJ], in order to define the
> coevaluation; the source states it only at `M = K`, which is the case registered here.  The
> general statement, for an arbitrary target and an arbitrary derived tensor product datum, is
> `AlgebraicGeometry.RingedSite.isIso_derivedTensorDualToSheafHom_of_isPerfect` of
> `StacksFrontier.Topology.Sheaves.Cohomology.InternalHom.DerivedCompositionPerfect`, which is where
> the mathematics is; nothing is re-proved here.

```lean
theorem isIso_derivedTensorDualToSheafHom_self
    (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (hK : X.IsPerfect K) :
    IsIso (derivedTensorDualToSheafHom X
      (Stacks.SheafOfModules.canonicalDerivedTensorProduct X) K K)
```

**`AlgebraicGeometry.RingedSite.coevaluation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/DerivedDualLeftDual.lean, line 290](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/DerivedDualLeftDual.lean#L290). The attribute's comment: “coevaluation”.

> **Stacks 0FPU: the coevaluation of a perfect object.**  For a perfect object `K` of `D(O)`
> with dual `K^∨ = R𝓗om_O(K, O)` the coevaluation is the morphism
>
> `η : O ⟶ K ⊗^𝐋_O K^∨`
>
> corresponding to `id_K` under the comparison `K ⊗^𝐋_O K^∨ ≅ R𝓗om_O(K, K)` of Stacks 08JD: the
> section corresponding to `id_K` (`AlgebraicGeometry.RingedSite.derivedIdentitySection`, the class
> of the identity under the two identifications of Stacks 08JA), followed by the inverse of that
> comparison.
>
> This is `AlgebraicGeometry.RingedSite.derivedDualCoevaluation`, which takes the invertibility of
> the comparison as a hypothesis, with that hypothesis discharged for a perfect `K` by
> `isIso_derivedTensorDualToSheafHom_self`.

```lean
def coevaluation
    (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (hK : X.IsPerfect K) :
    derivedStructureSheaf X ⟶
      ((Stacks.SheafOfModules.derivedTensorProductFunctor X).obj K).obj (derivedDual X K)
```

**`AlgebraicGeometry.RingedSite.evaluation_coevaluation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/DerivedDualLeftDual.lean, line 440](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/DerivedDualLeftDual.lean#L440). The attribute's comment: “left_dual”.

> **Stacks 0FPU, the triangle identity on the perfect object.**  For a perfect `K`, with the
> coevaluation `η` and the evaluation `ε`,
>
> `(η ▷ K) ≫ α ≫ (K ◁ ε) = λ ≫ ρ⁻¹`.
>
> The chain is `(η ▷ K) ≫ α ≫ (K ◁ ε) ≫ ρ = ((η ≫ Φ) ▷ K) ≫ app = (ι ▷ K) ≫ app = λ`, whose
> first step is (E1), whose middle step is `monoidalCoevaluation_comp` and whose last step is the
> unit law (UL), `AlgebraicGeometry.RingedSite.derivedSheafHomCounit_unit_law_monoidal`, at the
> section corresponding to `id_K`.

```lean
theorem evaluation_coevaluation
    (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (hK : X.IsPerfect K) :
    monoidalCoevaluation X K hK ▷ K ≫ (α_ K (derivedDual X K) K).hom ≫
        K ◁ monoidalEvaluation X K = (λ_ K).hom ≫ (ρ_ K).inv
```

**`AlgebraicGeometry.RingedSite.derivedDualExactPairing`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/DerivedDualLeftDual.lean, line 468](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/DerivedDualLeftDual.lean#L468). The attribute's comment: “left_dual”.

> **Stacks 0FPU: the derived dual of a perfect object is a left dual.**  For a perfect object
> `K` of `D(O)` the pair `(η, ε)` is an exact pairing — `K^∨ = R𝓗om_O(K, O)` is a left dual of `K`
> in the sense of [Stacks, Tag 0FFP] — in the monoidal structure of [Stacks, Tag 0FPT] on `D(O)`.
>
> Only the first triangle identity is checked: the second follows from it by
> `CategoryTheory.ExactPairing.ofEvaluationCoevaluation`, because the evaluation detects
> endomorphisms of `K^∨` (`eq_id_of_whiskerRight_comp_derivedDualEvaluation`), which is what the
> closed structure of `D(O)` supplies.

```lean
def derivedDualExactPairing
    (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (hK : X.IsPerfect K) : ExactPairing K (derivedDual X K)
```

**`AlgebraicGeometry.RingedSite.coevaluation_evaluation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/DerivedDualLeftDual.lean, line 482](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/DerivedDualLeftDual.lean#L482). The attribute's comment: “left_dual”.

> **Stacks 0FPU, the triangle identity on the derived dual.**  For a perfect `K`,
>
> `(K^∨ ◁ η) ≫ α⁻¹ ≫ (ε ▷ K^∨) = ρ ≫ λ⁻¹`.
>
> This is the second clause of `derivedDualExactPairing`, which
> `CategoryTheory.ExactPairing.ofEvaluationCoevaluation` derives from the first.

```lean
theorem coevaluation_evaluation
    (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (hK : X.IsPerfect K) :
    derivedDual X K ◁ monoidalCoevaluation X K hK ≫
        (α_ (derivedDual X K) K (derivedDual X K)).inv ≫
        monoidalEvaluation X K ▷ derivedDual X K =
      (ρ_ (derivedDual X K)).hom ≫ (λ_ (derivedDual X K)).inv
```

**`AlgebraicGeometry.RingedSite.exists_exactPairing_derivedDual`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/DerivedDualLeftDual.lean, line 543](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/DerivedDualLeftDual.lean#L543). The attribute's comment: “left_dual”.

> **Stacks 0FPU: the derived dual of a perfect object is a left dual, on an arbitrary ringed
> site.**  Let `(C, O)` be a ringed site and `K` a perfect object of `D(O)`, with dual
> `K^∨ = R𝓗om_O(K, O)`, coevaluation `η` (the section corresponding to `id_K` under
> `K ⊗^𝐋_O K^∨ ≅ R𝓗om_O(K, K)`) and evaluation `ε`.  Then `(K^∨, η, ε)` is a left dual of `K`
> in the monoidal category `D(O)` of [Stacks, Tag 0FPT], in the sense of [Stacks, Tag 0FFP]: there
> is an exact pairing between `K` and `K^∨` whose coevaluation is `η` and whose evaluation is `ε`,
> that is, both triangle identities hold for `η` and `ε`.
>
> The only hypothesis is the perfectness of `K`.  The additivity of `⊗_O` in each variable, the
> existence of the total tensor complexes, and sheafification of abelian sheaves on the site and
> on its slices hold for every ringed site, and are discharged here; the pairing is
> `AlgebraicGeometry.RingedSite.derivedDualExactPairing`.

```lean
theorem exists_exactPairing_derivedDual
    (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)))
    (hK : Y.IsPerfect K) :
    ∃ P : ExactPairing K (derivedDual Y K),
      P.coevaluation' = monoidalCoevaluation Y K hK ∧
        P.evaluation' = monoidalEvaluation Y K
```

**`AlgebraicGeometry.RingedSite.derivedDualEvaluation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/DualityPairing.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/DualityPairing.lean#L210). The attribute's comment: “evaluation”.

> **Stacks 0FPU: the evaluation map.** For an object `K` of `D(O)` with dual
> `K^∨ = RSheafHom(K, O)` the evaluation is the morphism
>
> `ε : K^∨ ⊗^L_O K ⟶ O`
>
> matched with the identity of `K^∨` by the tensor–internal-Hom bijection of Stacks 08J8, under
> which morphisms `K^∨ ⊗^L_O K ⟶ O` are morphisms `K^∨ ⟶ RSheafHom(K, O) = K^∨`. No perfectness
> hypothesis is needed: evaluation exists for every object of `D(O)`.

```lean
def derivedDualEvaluation
    (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) :
    ((Stacks.SheafOfModules.derivedTensorProductFunctor X).obj (derivedDual X K)).obj K ⟶
      derivedStructureSheaf X
```

## Tag 0FPV, a lemma

[Tag 0FPV](https://stacks.math.columbia.edu/tag/0FPV) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.isPerfect_and_isIso_derivedDualToLeftDual`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/LeftDualIsPerfect.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/LeftDualIsPerfect.lean#L151). The attribute's comment: “both assertions: `M` is perfect, and the left dual `N` is the object `RSheafHom(M, O)` of Example 0FPU, by the morphism `derivedDualToLeftDual` which the pairing matches with the evaluation of Example 0FPU and which carries the evaluation of the pairing to that of Example 0FPU. The monoidal structure on `D(O)` is the one of Tag 0FPT, `Stacks.SheafOfModules.DerivedMonoidal.derivedMonoidal`, a left dual is Mathlib's `CategoryTheory.ExactPairing` (Definition 0FFP), and perfect is `AlgebraicGeometry.RingedSite.IsPerfect` (Definition 08G5)”.

> **Stacks 0FPV.** Let `(C, O)` be a ringed site and let `M` be an object of `D(O)` with a left
> dual `N` in the symmetric monoidal category `D(O)` of Stacks 0FPT. Then `M` is perfect, and the
> left dual is the object `M^∨ = RSheafHom(M, O)` of Example 0FPU: the morphism `M^∨ ⟶ N` which the
> pairing matches with the evaluation of Example 0FPU is an isomorphism, and it carries the
> evaluation `ε` of the pairing to the evaluation `ε'` of Example 0FPU.
>
> The first assertion is `isPerfect_of_exactPairing`, the second `isIso_derivedDualToLeftDual`
> together with `whiskerRight_derivedDualToLeftDual`.

```lean
theorem isPerfect_and_isIso_derivedDualToLeftDual
    (M N : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (pair : letI := derivedMonoidal X.O; ExactPairing M N) :
    X.IsPerfect M ∧
      (letI := derivedMonoidal X.O; letI := pair;
        IsIso (derivedDualToLeftDual M N) ∧
          derivedDualToLeftDual M N ▷ M ≫ ε_ M N = derivedDualEvaluationMonoidal M)
```

**`AlgebraicGeometry.RingedSite.isIso_derivedDualToLeftDual`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/LeftDualIsTheDerivedDual.lean, line 897](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/LeftDualIsTheDerivedDual.lean#L897). The attribute's comment: “the left dual is the object constructed in Example 0FPU, namely the derived dual `RSheafHom(M, O)` of Tag 08JD, and the identification is the morphism matched with the evaluation of Example 0FPU by the pairing; see `AlgebraicGeometry.RingedSite.whiskerRight_derivedDualToLeftDual` for the compatibility of the two evaluations. The monoidal structure on `D(O)` is the one of Tag 0FPT, `Stacks.SheafOfModules.DerivedMonoidal.derivedMonoidal`, and a left dual is Mathlib's `CategoryTheory.ExactPairing`, which is Definition 0FFP”.

> **Stacks 0FPV, second assertion: a left dual of `M` is the dual object of Example 0FPU.**
> The morphism `M^∨ = RSheafHom(M, O) ⟶ N` which the exact pairing matches with the evaluation of
> Example 0FPU is an isomorphism; its inverse is the morphism which the tensor–internal-Hom
> bijection of Stacks 08J8 matches with the evaluation of the pairing.

```lean
theorem isIso_derivedDualToLeftDual : IsIso (derivedDualToLeftDual M N)
```

## Tag 0A0A, a lemma

[Tag 0A0A](https://stacks.math.columbia.edu/tag/0A0A) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.isDerivedLimit_tensorDerivedDual_of_isHomotopyColimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedHomOfAHomotopyColimit.lean, line 272](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedHomOfAHomotopyColimit.lean#L272). The attribute's comment: “the stated identity `RSheafHom(K, E) = R lim (E ⊗^L_O Kₙ^∨)` for `K = hocolim Kₙ`, with two inputs of the source's proof assumed rather than proved: `hcomp`, that the canonical map `RSheafHom(⊕ Kₙ, E) ⟶ ∏ RSheafHom(Kₙ, E)` is an isomorphism, which is the last step of the proof; and `hdual`, clause 3 of Stacks 08JJ, that the canonical map of Stacks 08JD `E ⊗^L_O Kₙ^∨ ⟶ RSheafHom(Kₙ, E)` is an isomorphism, which no declaration of this library asserts. The perfectness of the `Kₙ` is used in the source only to invoke that clause, so it is not assumed here, and the existence of the direct sum `⊕ Kₙ` and of the two products is not assumed either, being supplied by the instances of Stacks 07D9; everything else of the tag is proved, in particular the whole comparison of triangles.”.

> **Stacks 0A0A.**  Let `(Kₙ)` be a system of objects of `D(O)` and let `K = hocolim Kₙ`.  For
> every object `E` of `D(O)`,
>
> `RSheafHom(K, E) = R lim (E ⊗^L_O Kₙ^∨)`,
>
> granted the two inputs the source's proof uses and the library does not have: that the canonical
> map `RSheafHom(⊕ Kₙ, E) ⟶ ∏ RSheafHom(Kₙ, E)` is an isomorphism, and that the canonical map
> `E ⊗^L_O Kₙ^∨ ⟶ RSheafHom(Kₙ, E)` of Stacks 08JD is an isomorphism for every `n`, which is
> clause 3 of Stacks 08JJ and is where the perfectness of the `Kₙ` is used in the source.
>
> Given the second hypothesis the tensor-dual system is isomorphic to the system
> `n ↦ RSheafHom(Kₙ, E)`, so the assertion is
> `AlgebraicGeometry.RingedSite.isDerivedLimit_derivedSheafHom_of_isHomotopyColimit` transported
> along that isomorphism.

```lean
theorem isDerivedLimit_tensorDerivedDual_of_isHomotopyColimit
    (F : ℕ ⥤ DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (E : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (hcomp : IsIso (Pi.lift (fun n : ℕ ↦
        ((derivedSheafHomBifunctor X).flip.obj E).map (Sigma.ι F.obj n).op) :
      ((derivedSheafHomBifunctor X).flip.obj E).obj (op (∐ F.obj)) ⟶
        ∏ᶜ fun n : ℕ ↦ (derivedSheafHomSystem X F E).obj (op n)))
    (hdual : ∀ n : ℕ, IsIso (derivedTensorDualToSheafHom X T (F.obj n) E))
    {K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))}
    (hK : IsHomotopyColimit F K) :
    IsDerivedLimit (tensorDerivedDualSystem X T F E)
      (((derivedSheafHomBifunctor X).flip.obj E).obj (op K))
```

**`AlgebraicGeometry.RingedSite.derivedHom_isDerivedLimit_tensorDual`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/DerivedDualSystemLimit.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/DerivedDualSystemLimit.lean#L152). The attribute's comment: “the identity `R𝑆heafHom(K, E) = R lim (E ⊗^L_O Kₙ^∨)` for a system of perfect objects `Kₙ` with derived colimit `K`, at the hypotheses of the source: the perfectness of each `Kₙ` and `K = hocolim Kₙ`. The direct-sum comparison and the identification of Stacks 08JJ that the source's proof uses are both proved in the library, so this needs nothing beyond those two hypotheses: the ringed site carries no hypothesis, the sheafification and additivity instances the statement's constructions need being synthesized rather than assumed, and the existence of `⊕ Kₙ` and of the products coming from the instances of Stacks 07D9”.

> **Stacks 0A0A: derived internal Hom out of a homotopy colimit of perfect objects.** Let
> `(𝒞, 𝒪)` be a ringed site, let `(Kₙ)` be a system of perfect objects of `D(𝒪)`, let
> `K = hocolim Kₙ` and let `E` be an object of `D(𝒪)`. Then
>
> `R𝑆heafHom_𝒪(K, E) = R lim (E ⊗^𝐋_𝒪 Kₙ^∨)`.
>
> Perfectness of the terms turns the system of tensor products with the duals into the system
> `n ↦ R𝑆heafHom_𝒪(Kₙ, E)`, by Stacks 08JJ and its contravariant naturality; the latter system
> has `R𝑆heafHom_𝒪(K, E)` as its derived limit for every system with derived colimit `K`.

```lean
theorem derivedHom_isDerivedLimit_tensorDual
    (F : ℕ ⥤ DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (K E : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (hF : ∀ n : ℕ, X.IsPerfect (F.obj n))
    (hK : IsHomotopyColimit F K) :
    IsDerivedLimit
        (tensorDerivedDualSystem X (Stacks.SheafOfModules.canonicalDerivedTensorProduct X) F E)
      (((derivedSheafHomBifunctor X).obj (op K)).obj E)
```

**`AlgebraicGeometry.RingedSite.isDerivedLimit_tensorDerivedDual_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/DualTensorDerivedLimit.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/DualTensorDerivedLimit.lean#L122). The attribute's comment: “the stated identity `RSheafHom(K, E) = R lim (E ⊗^L_O Kₙ^∨)` for `K = hocolim Kₙ` with the `Kₙ` perfect, for the canonical derived tensor product, with both inputs of the source's proof proved rather than assumed”.

> **Stacks 0A0A for a system of perfect objects.** Let `(Kₙ)` be a system of perfect objects
> of `D(𝒪)` whose direct sum exists and let `K = hocolim Kₙ`. For every object `E` of `D(𝒪)`,
>
> `R𝑆heafHom_𝒪(K, E) = R lim (E ⊗^𝐋_𝒪 Kₙ^∨)`,
>
> the derived tensor product being the canonical one of [Stacks, Tag 06YU].
>
> Both inputs of the source's proof are discharged: the direct-sum comparison
> `R𝑆heafHom_𝒪(⊕ Kₙ, E) ⟶ ∏ R𝑆heafHom_𝒪(Kₙ, E)` by
> `AlgebraicGeometry.RingedSite.isIso_derivedSheafHomSigmaComparison`, and clause 3 of
> [Stacks, Tag 08JJ] by `AlgebraicGeometry.RingedSite.tensorDerivedDualSystemIsoOfPerfect`, which
> is where perfectness is used — exactly as in the source.

```lean
theorem isDerivedLimit_tensorDerivedDual_of_isPerfect
    (F : ℕ ⥤ DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    [HasCoproduct F.obj]
    (E : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    [HasProduct fun n : ℕ ↦ (derivedSheafHomSystem X F E).obj (op n)]
    [HasProduct fun n : ℕ ↦ (tensorDerivedDualSystem X
      (Stacks.SheafOfModules.canonicalDerivedTensorProduct.{u} X) F E).obj (op n)]
    (hF : ∀ n : ℕ, X.IsPerfect (F.obj n))
    {K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))}
    (hK : IsHomotopyColimit F K) :
    IsDerivedLimit (tensorDerivedDualSystem X
        (Stacks.SheafOfModules.canonicalDerivedTensorProduct.{u} X) F E)
      (((derivedSheafHomBifunctor X).flip.obj E).obj (op K))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.48, Tag 0FPP](https://stacks.math.columbia.edu/tag/0FPP)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
