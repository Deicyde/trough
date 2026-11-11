---
declaration: section
origin: cited
lean: Stacks.WeilCohomology.existsUnique_isTotalChernClass_of_source, Stacks.WeilCohomology.eq_of_isTotalChernClass, Stacks.WeilCohomology.ChernSetup.chernClass, Stacks.WeilCohomology.ChernSetup.sum_chernClass_eq_zero, Stacks.WeilCohomology.ChernSetup.exists_injective_hasInvertibleFiltration, Stacks.WeilCohomology.ChernSetup.chernClass_tensorObj, Stacks.WeilCohomology.IsTotalChernClassOnLocallyFree.apply_classOf_tensorObj_invertible, Stacks.WeilCohomology.chernClass_tensorObjRingedSpace
statement: formalized
proof: formalized
---

# 45.12 Chern classes

Section 45.12 of the Stacks Project, [Tag 0FI4](https://stacks.math.columbia.edu/tag/0FI4). 5 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FI5, a proposition

[Tag 0FI5](https://stacks.math.columbia.edu/tag/0FI5) in the Stacks Project.

**`Stacks.WeilCohomology.existsUnique_isTotalChernClass_of_source`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/ChernClasses/KZeroRule.lean, line 598](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/ChernClasses/KZeroRule.lean#L598). The attribute's comment: “the proposition: existence and uniqueness of the rule c^A on all of K\_0(Vect(X)), with its three properties, K\_0(Vect(X)) being the Grothendieck group AlgebraicGeometry.VectorBundleKZero of Tag 0FDK and prod\_\{i >= 0} A^i(X) the family of components together with the clause mem\_grade. NO constant rank and NO restriction to generators: properties (1) and (2) are stated for every element of K\_0(Vect(X)) and the construction is for a module of arbitrary rank. The standing situation is the structure Stacks.WeilCohomology.ChernSetup -- the data the source fixes, with clause (1), clause (2), clause (3)(a), condition (1), condition (2), condition (4) and the source's grading A(X) = sum of the A^i(X) as isInternal\_grade -- together with the three remaining conditions of the section, each in the source's own form: condition (3) at f^*L itself; clause (3)(b) as the closure property IsBundleCompare at f^*E itself; and clause (3)(c) as the closure property IsBundleEmbedding with condition (5) read at c\_1^A(O\_P(P')) for the divisor module characterized divisor-theoretically by IsSubbundleDivisorModule. NO hypothesis is read more strongly than the source states it: the invariance of the total Chern class under an isomorphism of modules, which K\_0(Vect(X)) forces on any rule out of it and which a comparison of P(E) with P(E') would get only by asking clause (3)(b) at every E' isomorphic to f^*E, is instead PROVED, as chernSeries\_eq\_of\_iso, from multiplicativity in the short exact sequence 0 to E to E' to 0; the pseudofunctoriality coherence isomorphism h^*(g^*E) = (h . g)^*E, which the source has for free, comes from the same theorem through pull\_chernSeries\_coeff\_of\_iso. The structure Stacks.WeilCohomology.ChernSituation is built inside the proof and is not an argument. PROVED here and in this directory, not assumed: the projective bundle with its flat projection, its invertible twist and its tautological sequence of kernel rank r, from clause (3)(a) (BundleObject.toBundleDatum); the rank-one case of that kernel rank (isFiniteLocallyFreeOfRank\_kernel\_of\_epi\_isInvertible\_pred); condition (3) under an isomorphism of invertible modules (pull\_c\_1); condition (4) read with the grading (mem\_grade\_of\_bundleFormula); the identification of twists along the induced morphism P(f^*E) to P(E) (exists\_bundleCompare) and along the induced closed immersion P(F) to P(E) (exists\_divisorDatum); the source's identification O\_P(P') = O\_P(1) tensor (p^*L)^\{-1}, from the description of P(F) in P(E) as the zero scheme of a regular section (BundleObject.twistClass\_eq\_picardClassOf\_add); clause (1), clause (2) and condition (2) with the local constancy of the rank, in the form 'A(X) is separated by, patched from and graded by its restrictions to the loci where E has constant rank' (eq\_of\_pull\_constantRank, exists\_pull\_eq\_constantRank, mem\_grade\_of\_pull\_constantRank, subsingleton\_of\_isEmpty); the construction of the Chern classes, equation 45.12.1.1, their centrality and homogeneity, their compatibility with pullback, the Whitney formula for an invertible submodule, multiplicativity in an arbitrary short exact sequence by induction on the rank, the arbitrary-rank total Chern class, the extension to K\_0(Vect(X)) with the formal inverse, the three properties, and the uniqueness; the source's 'it suffices to check this after pulling back by P(E^dual) -- thus we may assume we have an invertible submodule L of E such that both E/L and F/L are finite locally free' (exists\_splitInvertibleSub); the rank of the middle term of the sequence of clause (3)(c), from AlgebraicGeometry.SheafOfModules.rank\_add\_of\_shortExact; and the first Chern class of the divisor class of that clause, from condition (3) with the additivity of c\_1^A on Pic (c\_1\_divisorClass)”.

> **Stacks Project, Tag 0FI5.** In the standing situation of Section 45.12 there is a unique
> rule which assigns to every object `X` of `𝒞` a total Chern class
>
> `c^A : K₀(Vect(X)) ⟶ ∏_{i ≥ 0} A^i(X)`
>
> such that (1) `c^A(α + β) = c^A(α) c^A(β)` and `c^A(0) = 1`, (2) `f^* ∘ c^A = c^A ∘ f^*` for a
> morphism `f : X' ⟶ X` of `𝒞`, and (3) `c^A([ℒ]) = 1 + c₁^A(ℒ)` for `ℒ ∈ Pic(X)`.
>
> **What the situation is.** `Stacks.WeilCohomology.ChernSetup` is the source's own standing
> situation: the graded rings `A(X)` with the pullback ring maps and the additive
> `c₁^A : Pic(X) ⟶ A¹(X)` — the data the source fixes — together with clause (1), clause (2),
> clause (3)(a), condition (1), condition (2) and condition (4), and the grading
> `A(X) = ⨁_{i ≥ 0} A^i(X)` as `isInternal_grade`. Every field of it is a datum or a condition the
> source states; in particular `Stacks.WeilCohomology.ChernSetup.bundleDatum` — the projective
> bundle with its flat projection, its invertible twist and its tautological sequence — is a
> *definition*, built from clause (3)(a) by
> `Stacks.WeilCohomology.BundleObject.toBundleDatum`, and not a field.
>
> The three remaining conditions of the section are the hypotheses here:
>
> * condition (3), `f^*c₁^A(ℒ) = c₁^A(f^*ℒ)`, at `f^*ℒ` itself;
> * clause (3)(b), that the induced `𝐏(f^*ℰ) ⟶ 𝐏(ℰ)` is a morphism of `𝒞`
>   (`Stacks.WeilCohomology.IsBundleCompare`), at `f^*ℰ` itself and with nothing about twists;
> * clause (3)(c), that the induced closed immersion `𝐏(𝓕) ⟶ 𝐏(ℰ)` is a morphism of `𝒞`
>   (`Stacks.WeilCohomology.IsBundleEmbedding`), together with condition (5) read at
>   `c₁^A(𝒪_P(𝐏(𝓕)))` for the divisor module characterized by
>   `Stacks.WeilCohomology.IsSubbundleDivisorModule`.
>
> **No hypothesis is read more strongly than the source states it.** In particular `hcompare` is
> clause (3)(b) at `f^*ℰ` itself. The invariance of the total Chern class under an isomorphism of
> modules, which `K₀(Vect(X))` forces on any rule out of it and which a comparison of the
> projective bundles `𝐏(ℰ)` and `𝐏(ℰ')` would get only from a stronger reading of that clause, is
> instead the theorem `Stacks.WeilCohomology.ChernSituation.chernSeries_eq_of_iso`, proved from
> multiplicativity in the short exact sequence `0 ⟶ ℰ ⟶ ℰ' ⟶ 0 ⟶ 0`. The pseudofunctoriality
> coherence isomorphism `h^*(g^*ℰ) ≅ (h ≫ g)^*ℰ`, which the source has for free by writing `f^*`
> as a strict functor, is handled by the same theorem through
> `Stacks.WeilCohomology.ChernSituation.pull_chernSeries_coeff_of_iso`.
>
> The `Stacks.WeilCohomology.ChernSituation` the development is written over is assembled from
> these inside the proof, so it is not an argument of this statement. Everything the source
> derives rather than assumes is a theorem: condition (3) under an isomorphism of invertible
> modules (`Stacks.WeilCohomology.ChernSituation.pull_c₁`), condition (4) read with the grading
> (`Stacks.WeilCohomology.SourceChernSetup.mem_grade_of_bundleFormula`), the identifications of
> twists along the two induced morphisms
> (`Stacks.WeilCohomology.ChernSituation.exists_bundleCompare` and
> `Stacks.WeilCohomology.ChernSituation.exists_divisorDatum`), and
> `𝒪_P(𝐏(𝓕)) ≅ 𝒪_P(1) ⊗ (p^*ℒ)^{⊗ -1}`
> (`Stacks.WeilCohomology.BundleObject.twistClass_eq_picardClassOf_add`).

```lean
theorem existsUnique_isTotalChernClass_of_source (𝔄 : SourceChernSetup.{u, v, v₁, w} C S)
    (hpull : PullbackFirstChernCondition 𝔄) (hcompare : BundleCompareClause 𝔄)
    (hdivisor : DivisorDatumClause 𝔄) :
    ∃! c : ∀ X : C, VectorBundleKZero (S.obj X) → ℕ → 𝔄.A X,
    IsTotalChernClassOnLocallyFree 𝔄.toChernSetup c
```

**`Stacks.WeilCohomology.eq_of_isTotalChernClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/ChernClasses/TotalChernClass.lean, line 226](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/ChernClasses/TotalChernClass.lean#L226). The attribute's comment: “uniqueness, for the class of a module of constant rank; the existence half of the rule on all of K₀ needs condition (5), which `ChernSetup` does not carry, and property (2) is stated on generators — see the module documentation”.

> **The uniqueness half of Stacks Tag 0FI5.** Properties (1), (2) and (3) determine the total
> Chern class of the class of a finite locally free module of constant rank: any two rules with
> those properties agree there.
>
> The splitting principle of Tag 0FI7 supplies `p : P ⟶ X` with `p^*` injective on `A` and a
> filtration of `p^*ℰ` with invertible successive quotients. That filtration writes `[p^*ℰ]` as a
> sum of classes of invertible modules in `K₀(Vect(P))`, where properties (1) and (3) determine the
> total Chern class; property (2) identifies the result with `p^*c^A([ℰ])`, and `p^*` is
> injective.

```lean
theorem eq_of_isTotalChernClass {𝔄 : ChernSetup.{u, v, v₁, w} C S}
    {c c' : ∀ X : C, VectorBundleKZero (S.obj X) → ℕ → 𝔄.A X}
    (hc : IsTotalChernClass 𝔄 c) (hc' : IsTotalChernClass 𝔄 c') (X : C)
    (E : (S.obj X).Modules) (r : ℕ)
    (hE : AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E r) (n : ℕ) :
    c X (VectorBundleKZero.classOf (S.obj X) E) n =
      c' X (VectorBundleKZero.classOf (S.obj X) E) n
```

**`Stacks.WeilCohomology.ChernSetup.chernClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/ChernClasses/TotalChernClass.lean, line 274](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/ChernClasses/TotalChernClass.lean#L274). The attribute's comment: “the Chern classes of one finite locally free module of constant positive rank; not yet the rule on K₀”.

> **The Chern classes `c_j^A(ℰ)` of a finite locally free module of constant rank `r + 1`.**
> The zeroth is `1`, those in degrees `1, …, r + 1` are the entries of `chernTuple` with the signs
> of equation 45.12.1.1, and the rest vanish.
>
> This is the construction half of Tag 0FI5 for a single module: a real body, the inverse of the
> bijection of condition (4) applied to an explicit element. It is not yet a rule on `K₀(Vect(X))`;
> see the module documentation.

```lean
def chernClass (j : ℕ) : 𝔄.A X
```

**`Stacks.WeilCohomology.ChernSetup.sum_chernClass_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/ChernClasses/TotalChernClass.lean, line 300](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/ChernClasses/TotalChernClass.lean#L300). The attribute's comment: “equation 45.12.1.1, the relation defining the Chern classes”.

> **Equation 45.12.1.1**, the relation that defines the Chern classes:
> `∑_{i=0}^{r+1} (-1)^i c₁^A(𝒪_P(1))^i ∪ p^*c^A_{r+1-i}(ℰ) = 0` in `A(𝐏(ℰ))`.
>
> The term at `i = r + 1` is `(-1)^{r+1} c₁^A(𝒪_P(1))^{r+1}`, because `c_0^A(ℰ) = 1`; the terms
> below it reproduce the projective bundle formula applied to the tuple, the two signs cancelling,
> and that is `-(-1)^{r+1} c₁^A(𝒪_P(1))^{r+1}` by construction.

```lean
theorem sum_chernClass_eq_zero :
    ∑ i : Fin (r + 2), ((-1 : ℤ) ^ (i : ℕ)) •
        (𝔄.c₁ (𝔄.bundleDatum X E r hE).bundle (𝔄.bundleDatum X E r hE).twistClass ^ (i : ℕ) *
          𝔄.pull (𝔄.bundleDatum X E r hE).proj (𝔄.chernClass X E r hE (r + 1 - (i : ℕ)))) = 0
```

## Tag 0FI7, a lemma

[Tag 0FI7](https://stacks.math.columbia.edu/tag/0FI7) in the Stacks Project.

**`Stacks.WeilCohomology.ChernSetup.exists_injective_hasInvertibleFiltration`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/ChernClasses/SplittingPrinciple.lean, line 276](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/ChernClasses/SplittingPrinciple.lean#L276). The attribute's comment: “the ranks are constant, as in the source; see the module documentation for the clauses of the standing situation that `ChernSetup` transcribes”.

> **The splitting principle, Stacks Tag 0FI7.** In the standing situation of Section 45.12, let
> `X` be an object of `𝒞` and let `ℰ_i` be a finite collection of locally free `𝒪_X`-modules of
> ranks `r_i`. There is a morphism `p : P ⟶ X` of `𝒞` such that `p^* : A(X) ⟶ A(P)` is injective
> and each `p^*ℰ_i` has a filtration of length `r_i` whose successive quotients are invertible
> `𝒪_P`-modules. The projection is moreover flat.
>
> The induction is on `∑ rᵢ`. If every rank is at most one the identity of `X` already works, each
> `ℰ_i` being zero or invertible. Otherwise some `rᵢ` exceeds one; the projective bundle of `ℰ_i`
> gives `p : P ⟶ X` with its tautological sequence `0 ⟶ 𝓕 ⟶ p^*ℰ_i ⟶ 𝒪_P(1) ⟶ 0`, and `p^*` is
> injective by the projective bundle formula. The inductive hypothesis applied to `𝓕` together
> with the `p^*ℰ_{i'}` for `i' ≠ i` produces `q : Q ⟶ P`, and `q ≫ p` is the required morphism:
> flatness of `S q` keeps the tautological sequence exact after pullback, so the filtration of
> `q^*𝓕` extends by one step to one of `q^*p^*ℰ_i`.

```lean
theorem exists_injective_hasInvertibleFiltration (𝔄 : ChernSetup.{u, v, v₁, w} C S) (X : C)
    (I : Type*) [Finite I] (E : I → (S.obj X).Modules) (r : I → ℕ)
    (hE : ∀ i, AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} (E i) (r i)) :
    ∃ (P : C) (p : P ⟶ X), Flat (S.map p) ∧ Function.Injective (𝔄.pull p) ∧
      ∀ i, HasInvertibleFiltration (S.obj P)
        ((Scheme.Modules.pullback (S.map p)).obj (E i)) (r i)
```

## Tag 0FI8, a lemma

[Tag 0FI8](https://stacks.math.columbia.edu/tag/0FI8) in the Stacks Project.

**`Stacks.WeilCohomology.ChernSetup.chernClass_tensorObj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/ChernClasses/Twist.lean, line 267](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/ChernClasses/Twist.lean#L267). The attribute's comment: “the comparison `𝐏(ℰ) ≅ 𝐏(ℰ ⊗ ℒ)` of projective bundles and its effect on the tautological class are hypotheses, the situation carrying no functoriality of `𝐏`; the rank is constant and that of `ℰ ⊗ ℒ` is assumed; see the module documentation”.

> Let `ℰ` be a finite locally free `𝒪_X`-module of constant rank `r + 1` and let `ℒ` be an
> invertible `𝒪_X`-module, with `ℰ ⊗ ℒ` again of rank `r + 1`. Then for `i ≤ r + 1`
> `c^A_i(ℰ ⊗ ℒ) = ∑_{j=0}^{i} binom(r + 1 - i + j, j) c^A_{i-j}(ℰ) ∪ c₁^A(ℒ)^j`,
> given an isomorphism `g : 𝐏(ℰ) ≅ 𝐏(ℰ ⊗ ℒ)` over `X` under which `c₁^A(𝒪_{𝐏(ℰ ⊗ ℒ)}(1))` pulls
> back to `c₁^A(𝒪_{𝐏(ℰ)}(1)) + p^*c₁^A(ℒ)`.

```lean
theorem chernClass_tensorObj (𝔄 : ChernSetup.{u, v, v₁, w} C S) (X : C)
    (E L : (S.obj X).Modules) (r : ℕ)
    (hE : AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E (r + 1))
    (hL : AlgebraicGeometry.SheafOfModules.IsInvertible (S.obj X).presheaf
      (S.obj X).ringCatSheaf.2 L)
    (hEL : AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u}
      (Scheme.Modules.tensorObjRingedSpace (S.obj X) E L) (r + 1))
    (g : (𝔄.bundleDatum X E r hE).bundle ≅
      (𝔄.bundleDatum X (Scheme.Modules.tensorObjRingedSpace (S.obj X) E L) r hEL).bundle)
    (hg : g.hom ≫ (𝔄.bundleDatum X
        (Scheme.Modules.tensorObjRingedSpace (S.obj X) E L) r hEL).proj =
      (𝔄.bundleDatum X E r hE).proj)
    (htwist : 𝔄.pull g.hom
        (𝔄.c₁ (𝔄.bundleDatum X (Scheme.Modules.tensorObjRingedSpace (S.obj X) E L) r hEL).bundle
          (𝔄.bundleDatum X
            (Scheme.Modules.tensorObjRingedSpace (S.obj X) E L) r hEL).twistClass) =
      𝔄.c₁ (𝔄.bundleDatum X E r hE).bundle (𝔄.bundleDatum X E r hE).twistClass +
        𝔄.pull (𝔄.bundleDatum X E r hE).proj (𝔄.c₁ X (picardClassOf (S.obj X) L hL)))
    (i : ℕ) (hi : i ≤ r + 1) :
    𝔄.chernClass X (Scheme.Modules.tensorObjRingedSpace (S.obj X) E L) r hEL i =
      ∑ j ∈ Finset.range (i + 1), (r + 1 - i + j).choose j •
        (𝔄.chernClass X E r hE (i - j) * 𝔄.c₁ X (picardClassOf (S.obj X) L hL) ^ j)
```

**`Stacks.WeilCohomology.IsTotalChernClassOnLocallyFree.apply_classOf_tensorObj_invertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/ChernClasses/TwistFormula.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/ChernClasses/TwistFormula.lean#L180). The attribute's comment: “for every rule c^A with the three properties of Tag 0FI5 (by that proposition there is exactly one), at the Chern classes c^A\_i(E) = the i-th component of c^A([E]); E of constant rank r, L invertible, i <= r. Unconditional: no comparison of projective bundles is assumed; the proof is the splitting principle 0FI7 instead of Constructions 02NC”.

> **Stacks Project, Tag 0FI8: the Chern classes of a twist.** In the standing situation of
> Section 45.12, let `c^A` be a rule with the three properties of Tag 0FI5, let `ℰ` be a finite
> locally free `𝒪_X`-module of constant rank `r` and `ℒ` an invertible `𝒪_X`-module. Then for
> `i ≤ r`
>
> `c^A_i(ℰ ⊗ ℒ) = ∑_{j=0}^{i} binom(r - i + j, j) c^A_{i-j}(ℰ) ∪ c₁^A(ℒ)^j`,
>
> where `c^A_i(ℱ)` is the `i`-th component of `c^A([ℱ])`. By the splitting principle, Tag 0FI7,
> after an injective pullback `ℰ` has Chern roots `x_1, …, x_r` and `ℰ ⊗ ℒ` the roots `x_k + t`
> with `t` the pullback of `c₁^A(ℒ)`; the formula is then
> `Stacks.WeilCohomology.esymm_map_add_const`.

```lean
theorem apply_classOf_tensorObj_invertible (hc : IsTotalChernClassOnLocallyFree 𝔄 c) (X : C)
    (E L : (S.obj X).Modules) (r : ℕ)
    (hE : AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E r)
    (hL : AlgebraicGeometry.SheafOfModules.IsInvertible (S.obj X).presheaf
      (S.obj X).ringCatSheaf.2 L) (i : ℕ) (hi : i ≤ r) :
    c X (VectorBundleKZero.classOf (S.obj X)
        (Scheme.Modules.tensorObjRingedSpace (S.obj X) E L)) i =
      ∑ j ∈ Finset.range (i + 1), (r - i + j).choose j •
        (c X (VectorBundleKZero.classOf (S.obj X) E) (i - j) *
          𝔄.c₁ X (picardClassOf (S.obj X) L hL) ^ j)
```

**`Stacks.WeilCohomology.chernClass_tensorObjRingedSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/ChernClasses/TwistUnconditional.lean, line 422](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/ChernClasses/TwistUnconditional.lean#L422). The attribute's comment: “for E of constant rank r + 1 and every i, the binomial coefficient binom(r - i + j, j) written (r + 1 + j - i).choose j in N, which agrees with it wherever the term c\_\{i-j}(E) is nonzero. The situation is SourceChernSetup with the source's condition (3), clause (3)(b) and clause (3)(c) (QuotientBundleEmbeddingClause, the closure property for an arbitrary surjection), each as the source states it. PROVED, not assumed: the comparison of P(E) with P(E tensor L) inside the category and g^*c\_1(O(1)) = c\_1(O(1)) + p^*c\_1(L) (exists\_bundleTensor\_comparison, from Tag 02NC exists\_bundleTensorIso, Tag 01CD and Tag 01CX), and the rank of E tensor L. The rule c^A on K\_0 and an arbitrary finite locally free E are ChernSituation.totalChernClass\_classOf\_tensorObjRingedSpace and ChernSituation.pull\_totalChernClass\_classOf\_tensorObjRingedSpace”.

> **Stacks Project, Tag 0FI8.** In the standing situation of Section 45.12, let `ℰ` be a finite
> locally free `𝒪_X`-module of constant rank `r + 1` and `ℒ` an invertible `𝒪_X`-module. Then for
> every `i`
> `c^A_i(ℰ ⊗ ℒ) = ∑_{j=0}^{i} binom(r + 1 - i + j, j) c^A_{i-j}(ℰ) ∪ c₁^A(ℒ)^j`,
> the binomial coefficient written `(r + 1 + j - i).choose j` (see the module documentation).
>
> The situation is `Stacks.WeilCohomology.SourceChernSetup` with the source's condition (3),
> clause (3)(b) and clause (3)(c), each in the source's own form. The comparison of `𝐏(ℰ)` with
> `𝐏(ℰ ⊗ ℒ)` and its effect on `c₁^A(𝒪(1))` are proved
> (`Stacks.WeilCohomology.exists_bundleTensor_comparison`, from Tag 02NC), and so is the rank of
> `ℰ ⊗ ℒ`.

```lean
theorem chernClass_tensorObjRingedSpace (𝔄 : SourceChernSetup.{u, v, v₁, w} C S)
    (hpull : PullbackFirstChernCondition 𝔄) (hcompare : BundleCompareClause 𝔄)
    (hquot : QuotientBundleEmbeddingClause 𝔄) (X : C) (E L : (S.obj X).Modules) (r : ℕ)
    (hE : AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E (r + 1))
    (hL : AlgebraicGeometry.SheafOfModules.IsInvertible (S.obj X).presheaf
      (S.obj X).ringCatSheaf.2 L) (i : ℕ) :
    𝔄.chernClass X (Scheme.Modules.tensorObjRingedSpace (S.obj X) E L) r
        (isFiniteLocallyFreeOfRank_tensorObjRingedSpace_of_isInvertible E L (r + 1) hE hL) i =
      ∑ j ∈ Finset.range (i + 1), (r + 1 + j - i).choose j •
        (𝔄.chernClass X E r hE (i - j) * 𝔄.c₁ X (picardClassOf (S.obj X) L hL) ^ j)
```

**`Stacks.WeilCohomology.ChernSituation.totalChernClass_classOf_tensorObjRingedSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/ChernClasses/TwistUnconditional.lean, line 543](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/ChernClasses/TwistUnconditional.lean#L543). The attribute's comment: “for the rule c^A of Tag 0FI5 (ChernSituation.totalChernClass on K\_0(Vect(X))), E of constant rank r, r = 0 included, and every i; binom(r - i + j, j) written (r + j - i).choose j in N, which agrees with it wherever c\_\{i-j}(E) is nonzero. The situation is ChernSituation, the source's clauses and conditions each in the source's form, with the source's clause (3)(c) for an arbitrary surjection (QuotientBundleEmbeddingClause). The comparison of P(E) with P(E tensor L) and the rank of E tensor L are proved; see chernClass\_tensorObjRingedSpace”.

> **Stacks Project, Tag 0FI8, for the rule `c^A` of Tag 0FI5.** In the standing situation, for
> `ℰ` finite locally free of constant rank `r` (`r = 0` included) and `ℒ` invertible,
> `c^A_i([ℰ ⊗ ℒ]) = ∑_{j=0}^{i} binom(r - i + j, j) c^A_{i-j}([ℰ]) ∪ c₁^A(ℒ)^j` for every `i`.

```lean
theorem totalChernClass_classOf_tensorObjRingedSpace
    (hquot : QuotientBundleEmbeddingClause 𝔖.toSourceChernSetup) (X : C)
    (E L : (S.obj X).Modules) (r : ℕ)
    (hE : AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E r)
    (hL : AlgebraicGeometry.SheafOfModules.IsInvertible (S.obj X).presheaf
      (S.obj X).ringCatSheaf.2 L) (i : ℕ) :
    𝔖.totalChernClass X
        (VectorBundleKZero.classOf (S.obj X) (Scheme.Modules.tensorObjRingedSpace (S.obj X) E L))
        i =
      ∑ j ∈ Finset.range (i + 1), (r + j - i).choose j •
        (𝔖.totalChernClass X (VectorBundleKZero.classOf (S.obj X) E) (i - j) *
          𝔖.c₁ X (picardClassOf (S.obj X) L hL) ^ j)
```

**`Stacks.WeilCohomology.ChernSituation.pull_totalChernClass_classOf_tensorObjRingedSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/ChernClasses/TwistUnconditional.lean, line 578](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/ChernClasses/TwistUnconditional.lean#L578). The attribute's comment: “for the rule c^A of Tag 0FI5 and an ARBITRARY finite locally free E: the formula holds after pullback along every morphism f : Z to X of the category along which E has constant rank r, which by condition (2) (ChernSituation.eq\_of\_pull\_one) determines c^A\_i(E tensor L); binom(r - i + j, j) written (r + j - i).choose j in N, which agrees with it wherever c\_\{i-j}(f^*E) is nonzero. The situation is ChernSituation with the source's clause (3)(c) for an arbitrary surjection (QuotientBundleEmbeddingClause). Proved, not assumed: the comparison of P(E) with P(E tensor L), the rank of E tensor L, and f^*(E tensor L) = f^*E tensor f^*L (Tag 01CD)”.

> **Stacks Project, Tag 0FI8, for the rule `c^A` of Tag 0FI5 and an arbitrary finite locally
> free module.** In the standing situation, let `ℰ` be finite locally free, of possibly
> non-constant rank, and `ℒ` invertible. On every object `f : Z ⟶ X` over `X` on which `ℰ` has
> constant rank `r`,
> `f^*c^A_i([ℰ ⊗ ℒ]) = ∑_{j=0}^{i} binom(r - i + j, j) f^*c^A_{i-j}([ℰ]) ∪ f^*c₁^A(ℒ)^j`.
>
> The source's `r` is the rank of `ℰ`, and its proof begins "by the construction of `c^A_i` we may
> assume `ℰ` has constant rank `r`": the formula is read on the loci of constant rank, and by
> condition (2) these determine `A(X)` (`Stacks.WeilCohomology.ChernSituation.eq_of_pull_one`).

```lean
theorem pull_totalChernClass_classOf_tensorObjRingedSpace
    (hquot : QuotientBundleEmbeddingClause 𝔖.toSourceChernSetup) (X : C)
    (E L : (S.obj X).Modules)
    (hE : AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u}
      (R := (S.obj X).ringCatSheaf) E)
    (hL : AlgebraicGeometry.SheafOfModules.IsInvertible (S.obj X).presheaf
      (S.obj X).ringCatSheaf.2 L) (Z : C) (f : Z ⟶ X) (r : ℕ)
    (hr : AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u}
      ((Scheme.Modules.pullback (S.map f)).obj E) r) (i : ℕ) :
    𝔖.pull f (𝔖.totalChernClass X
        (VectorBundleKZero.classOf (S.obj X) (Scheme.Modules.tensorObjRingedSpace (S.obj X) E L))
        i) =
      ∑ j ∈ Finset.range (i + 1), (r + j - i).choose j •
        (𝔖.pull f (𝔖.totalChernClass X (VectorBundleKZero.classOf (S.obj X) E) (i - j)) *
          𝔖.pull f (𝔖.c₁ X (picardClassOf (S.obj X) L hL)) ^ j)
```

## Tag 0FI9, a proposition

[Tag 0FI9](https://stacks.math.columbia.edu/tag/0FI9) in the Stacks Project.

**`Stacks.WeilCohomology.eq_of_isChernCharacter`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/ChernClasses/ChernCharacter.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/ChernClasses/ChernCharacter.lean#L167). The attribute's comment: “uniqueness, for the class of a module of constant rank; the existence half needs the locally constant rank r^A, which is indexed by condition (2) of the situation, and the Chern classes of Tag 0FI5 on all of K₀, and property (2) is stated on generators — see the module documentation”.

> **The uniqueness half of Stacks Tag 0FI9.** Properties (1), (2) and (3) determine the Chern
> character of the class of a finite locally free module of constant rank: any two rules with those
> properties agree there.
>
> The splitting principle of Tag 0FI7 supplies `p : P ⟶ X` with `p^*` injective on `A` and a
> filtration of `p^*ℰ` with invertible successive quotients. That filtration writes `[p^*ℰ]` as a
> sum of classes of invertible modules in `K₀(Vect(P))`, where additivity and the value on an
> invertible module determine the Chern character; property (2) identifies the result with
> `p^*ch^A([ℰ])`, and `p^*` is injective.

```lean
theorem eq_of_isChernCharacter {𝔄 : ChernSetup.{u, v, v₁, w} C S}
    [∀ X : C, Algebra ℚ (𝔄.A X)]
    {ch ch' : ∀ X : C, VectorBundleKZero (S.obj X) → ℕ → 𝔄.A X}
    (hch : IsChernCharacter 𝔄 ch) (hch' : IsChernCharacter 𝔄 ch') (X : C)
    (E : (S.obj X).Modules) (r : ℕ)
    (hE : AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E r) (n : ℕ) :
    ch X (VectorBundleKZero.classOf (S.obj X) E) n =
      ch' X (VectorBundleKZero.classOf (S.obj X) E) n
```

**`Stacks.WeilCohomology.existsUnique_isChernCharacter_of_source`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/ChernClasses/ChernCharacterExistence.lean, line 788](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/ChernClasses/ChernCharacterExistence.lean#L788). The attribute's comment: “the unique rule `ch^A : K₀(Vect(X)) ⟶ ∏_{i ≥ 0} A^i(X)` with properties (1), (2) and (3), both halves, on all of `K₀(Vect(X))` and with no restriction on the rank, in the standing situation of Section 45.12 read with `𝐐`-coefficients. The standing situation is the structure Stacks.WeilCohomology.ChernSetup -- the data the source fixes, with clause (1), clause (2), clause (3)(a), condition (1), condition (2), condition (4) and the source's grading A(X) = sum of the A^i(X) -- together with the section's three remaining conditions (PullbackFirstChernCondition, BundleCompareClause, DivisorDatumClause), each in the source's own form, and the `𝐐`-coefficients as an algebra structure with the rationals lying in `A^0(X)`. The structures Stacks.WeilCohomology.ChernSituation and RationalChernSituation are built inside the proof and are not arguments. PROVED and not assumed: the total Chern classes of Tag 0FI5, which the source's own proof cites as Proposition 45.12.1 (Stacks.WeilCohomology.ChernSituation.isTotalChernClass\_totalChernClass); the rank class `r^A`, which is Stacks.WeilCohomology.SourceChernSetup.rankClass, constructed from condition (2) as the source constructs it, with its membership in `A^0(X)` and its compatibility with pullback along an arbitrary morphism; and the projective bundle with its flat projection, invertible twist and tautological sequence, from clause (3)(a). Property (2) is stated on the generators, which `IsChernCharacterOnLocallyFree.map_pull_kzero` upgrades to the source's form, read against the CONSTRUCTED pullback homomorphism AlgebraicGeometry.VectorBundleKZero.pullbackRingHom of `K₀(Vect(-))`. NO hypothesis is read more strongly than the source states it: BundleCompareClause is clause (3)(b) at f^*E itself, and the invariance of the total Chern class under an isomorphism of modules, together with the pseudofunctoriality coherence isomorphism h^*(g^*E) = (h . g)^*E, are PROVED (chernSeries\_eq\_of\_iso, pull\_chernSeries\_coeff\_of\_iso) rather than obtained by asking that clause at every module isomorphic to f^*E”.

> In the standing situation of Section 45.12, read with `𝐐`-coefficients, there is exactly one
> rule assigning to every object `X` of `𝒞` a Chern character
>
> `ch^A : K₀(Vect(X)) ⟶ ∏_{i ≥ 0} A^i(X)`
>
> which is a ring map, is compatible with pullback, and sends an invertible module `ℒ` to
> `exp(c₁^A(ℒ))`.
>
> The situation is a `Stacks.WeilCohomology.SourceChernSetup` together with the section's three
> remaining conditions as the hypotheses `hpull`, `hcompare` and `hdivisor`
> (`Stacks.WeilCohomology.PullbackFirstChernCondition`, `Stacks.WeilCohomology.BundleCompareClause`,
> `Stacks.WeilCohomology.DivisorDatumClause`), and the `𝐐`-coefficients are the `ℚ`-algebra
> structure together with `hq`, which says that the rationals lie in `A^0(X)`.

```lean
theorem existsUnique_isChernCharacter_of_source (𝔄 : SourceChernSetup.{u, v, v₁, w} C S)
    [∀ X : C, Algebra ℚ (𝔄.A X)]
    (hq : ∀ (X : C) (q : ℚ), algebraMap ℚ (𝔄.A X) q ∈ 𝔄.grade X 0)
    (hpull : PullbackFirstChernCondition 𝔄) (hcompare : BundleCompareClause 𝔄)
    (hdivisor : DivisorDatumClause 𝔄) :
    ∃! ch : ∀ X : C, VectorBundleKZero (S.obj X) → ℕ → 𝔄.A X,
    IsChernCharacterOnLocallyFree 𝔄.toChernSetup ch
```

**`Stacks.WeilCohomology.eq_of_isChernCharacterOnLocallyFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/ChernClasses/ChernCharacterUniqueness.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/ChernClasses/ChernCharacterUniqueness.lean#L168). The attribute's comment: “uniqueness, on all of `K₀(Vect(X))` and with no restriction on the rank: two rules with properties (1), (2) and (3) are equal. Property (2) is stated on the generators, which `IsChernCharacterOnLocallyFree.map_pull_kzero` upgrades to the source's form, read against the CONSTRUCTED pullback homomorphism AlgebraicGeometry.VectorBundleKZero.pullbackRingHom of `K₀(Vect(-))`”.

> **The uniqueness half of Stacks Tag 0FI9.** Properties (1), (2) and (3) determine the Chern
> character on all of `K₀(Vect(X))`: any two rules with those properties are equal.

```lean
theorem eq_of_isChernCharacterOnLocallyFree {𝔄 : SourceChernSetup.{u, v, v₁, w} C S}
    [∀ X : C, Algebra ℚ (𝔄.A X)]
    {ch ch' : ∀ X : C, VectorBundleKZero (S.obj X) → ℕ → 𝔄.A X}
    (hch : IsChernCharacterOnLocallyFree 𝔄.toChernSetup ch)
    (hch' : IsChernCharacterOnLocallyFree 𝔄.toChernSetup ch') (X : C)
    (α : VectorBundleKZero (S.obj X)) (n : ℕ) :
    ch X α n = ch' X α n
```

## Tag 0FIA, a lemma

[Tag 0FIA](https://stacks.math.columbia.edu/tag/0FIA) in the Stacks Project.

**`Stacks.WeilCohomology.chernClass_secondAdams_kZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/ChernClasses/AdamsEigenvaluesKZero.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/ChernClasses/AdamsEigenvaluesKZero.lean#L191). The attribute's comment: “the identity `c^A_i(psi^2(alpha)) = 2^i c^A_i(alpha)` for EVERY element alpha of K\_0(Vect(X)) and a module of ARBITRARY rank -- the source's own statement, with no restriction to generators and no constant rank: the reduction to the generators is eq\_of\_convolutive\_of\_eq\_classOf and the reduction to constant rank is the source's decomposition of X by the rank, ChernSetup.eq\_of\_pull\_constantRank. The rule c^A is the predicate IsTotalChernClassOnLocallyFree of Tag 0FI5, which exactly one rule satisfies (existsUnique\_isTotalChernClass\_of\_source), so fixing it by that predicate is the source's 'let c^A be as in Proposition 45.12.1'. psi^2 is named by the two properties Tag 0FEJ gives it, its value on an invertible module and its commutation with the pullback of K\_0(Vect(-)), and the identity is proved for every ring endomorphism with those two properties; this repository CONSTRUCTS such a map, VectorBundleKZero.secondAdamsRingHom, and the two properties are verified for it in chernClass\_secondAdams\_secondAdamsRingHom. The pullback of K\_0(Vect(-)) is NOT named by a property: it is the constructed ring homomorphism VectorBundleKZero.pullbackRingHom, with its defining property pullback\_classOf, and property (2) is read against it by IsTotalChernClassOnLocallyFree.map\_pull\_kZero. psi^2([L]) = [L tensor L] is read in Pic, where addition is the tensor product by Tag 01CX (picardClassOf\_tensorObjRingedSpace)”.

> **Stacks Project, Tag 0FIA for the total Chern class.** The second Adams operator scales the
> degree-`n` part of the total Chern class by `2^n`: `c^A_n(ψ²(α)) = 2^n c^A_n(α)` for every
> `α ∈ K₀(Vect(X))`.
>
> The rule `c^A` is the one of Tag 0FI5, named by
> `Stacks.WeilCohomology.IsTotalChernClassOnLocallyFree`, and
> `ψ²` is named by the two properties Tag 0FEJ gives it. The pullback of `K₀(Vect(-))` is the
> constructed `AlgebraicGeometry.VectorBundleKZero.pullbackRingHom`; see the module documentation.

```lean
theorem chernClass_secondAdams_kZero
    {c : ∀ X : C, VectorBundleKZero (S.obj X) → ℕ → 𝔄.A X}
    (hc : IsTotalChernClassOnLocallyFree 𝔄.toChernSetup c)
    (hψpull : ∀ {X Y : C} (f : X ⟶ Y) (α : VectorBundleKZero (S.obj Y)),
      VectorBundleKZero.pullbackRingHom (S.map f) (ψ Y α) =
        ψ X (VectorBundleKZero.pullbackRingHom (S.map f) α))
    (hψinv : ∀ (X : C) (L : (S.obj X).Modules)
      (hL : AlgebraicGeometry.SheafOfModules.IsInvertible (S.obj X).presheaf
        (S.obj X).ringCatSheaf.2 L),
      ∃ (M : (S.obj X).Modules) (hM : AlgebraicGeometry.SheafOfModules.IsInvertible
        (S.obj X).presheaf (S.obj X).ringCatSheaf.2 M),
        ψ X (VectorBundleKZero.classOf (S.obj X) L) =
            VectorBundleKZero.classOf (S.obj X) M ∧
          picardClassOf (S.obj X) M hM = 2 • picardClassOf (S.obj X) L hL)
    (X : C) (α : VectorBundleKZero (S.obj X)) (n : ℕ) :
    c X (ψ X α) n = (2 ^ n : ℕ) • c X α n
```

**`Stacks.WeilCohomology.chernCharacter_secondAdams_kZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/ChernClasses/AdamsEigenvaluesKZero.lean, line 258](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/ChernClasses/AdamsEigenvaluesKZero.lean#L258). The attribute's comment: “the identity `ch^A_i(psi^2(alpha)) = 2^i ch^A_i(alpha)` for EVERY element alpha of K\_0(Vect(X)) and a module of ARBITRARY rank -- the source's own statement, with no restriction to generators and no constant rank: the reduction to the generators is VectorBundleKZero.addHom\_ext and the reduction to constant rank is the source's decomposition of X by the rank, ChernSetup.eq\_of\_pull\_constantRank. The rule ch^A is the predicate IsChernCharacterOnLocallyFree of Tag 0FI9, which exactly one rule satisfies (existsUnique\_isChernCharacter\_of\_source), so fixing it by that predicate is the source's 'let ch^A be as in Proposition 45.12.4'. psi^2 is named by the two properties Tag 0FEJ gives it, its value on an invertible module and its commutation with the pullback of K\_0(Vect(-)), and the identity is proved for every ring endomorphism with those two properties; this repository CONSTRUCTS such a map, VectorBundleKZero.secondAdamsRingHom, and the two properties are verified for it in chernCharacter\_secondAdams\_secondAdamsRingHom. The pullback of K\_0(Vect(-)) is NOT named by a property: it is the constructed ring homomorphism VectorBundleKZero.pullbackRingHom, with its defining property pullback\_classOf, and property (2) is read against it by IsChernCharacterOnLocallyFree.map\_pull\_kzero. psi^2([L]) = [L tensor L] is read in Pic, where addition is the tensor product by Tag 01CX (picardClassOf\_tensorObjRingedSpace)”.

> **Stacks Project, Tag 0FIA for the Chern character.** The second Adams operator scales the
> degree-`n` part of the Chern character by `2^n`: `ch^A_n(ψ²(α)) = 2^n ch^A_n(α)` for every
> `α ∈ K₀(Vect(X))`.
>
> The rule `ch^A` is the one of Tag 0FI9, named by
> `Stacks.WeilCohomology.IsChernCharacterOnLocallyFree`, and
> `ψ²` is named by the two properties Tag 0FEJ gives it. The pullback of `K₀(Vect(-))` is the
> constructed `AlgebraicGeometry.VectorBundleKZero.pullbackRingHom`; see the module documentation.

```lean
theorem chernCharacter_secondAdams_kZero [∀ X : C, Algebra ℚ (𝔄.A X)]
    {ch : ∀ X : C, VectorBundleKZero (S.obj X) → ℕ → 𝔄.A X}
    (hch : IsChernCharacterOnLocallyFree 𝔄.toChernSetup ch)
    (hψpull : ∀ {X Y : C} (f : X ⟶ Y) (α : VectorBundleKZero (S.obj Y)),
      VectorBundleKZero.pullbackRingHom (S.map f) (ψ Y α) =
        ψ X (VectorBundleKZero.pullbackRingHom (S.map f) α))
    (hψinv : ∀ (X : C) (L : (S.obj X).Modules)
      (hL : AlgebraicGeometry.SheafOfModules.IsInvertible (S.obj X).presheaf
        (S.obj X).ringCatSheaf.2 L),
      ∃ (M : (S.obj X).Modules) (hM : AlgebraicGeometry.SheafOfModules.IsInvertible
        (S.obj X).presheaf (S.obj X).ringCatSheaf.2 M),
        ψ X (VectorBundleKZero.classOf (S.obj X) L) =
            VectorBundleKZero.classOf (S.obj X) M ∧
          picardClassOf (S.obj X) M hM = 2 • picardClassOf (S.obj X) L hL)
    (X : C) (α : VectorBundleKZero (S.obj X)) (n : ℕ) :
    ch X (ψ X α) n = (2 ^ n : ℕ) • ch X α n
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 45.12, Tag 0FI4](https://stacks.math.columbia.edu/tag/0FI4)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
