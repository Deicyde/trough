---
declaration: section
origin: cited
lean: Stacks.Intersection.intersectionMultiplicity, AlgebraicGeometry.TorFormula.intersectionProductCycle, AlgebraicGeometry.TorFormula.derivedCategoryBMinus_derivedTensor, AlgebraicGeometry.TorFormula.isCoherent_torSheaf, AlgebraicGeometry.TorFormula.supp_torSheaf_subset_inter, AlgebraicGeometry.TorFormula.isCoherent_torSheaf_of_isRegular, AlgebraicGeometry.TorFormula.torSheafStalkIso, AlgebraicGeometry.TorFormula.isZero_torSheaf_of_lt
statement: formalized
proof: formalized
---

# 43.14 Intersection multiplicities using Tor formula

Section 43.14 of the Stacks Project, [Tag 0AZR](https://stacks.math.columbia.edu/tag/0AZR). 5 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AZR, the section

[Tag 0AZR](https://stacks.math.columbia.edu/tag/0AZR) in the Stacks Project.

**`Stacks.Intersection.intersectionMultiplicity`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/TorFormula/IntersectionMultiplicity.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/TorFormula/IntersectionMultiplicity.lean#L112). The attribute's comment: “the intersection multiplicity `e(X, V · W, Z)`, the displayed alternating sum of lengths of local `Tor` modules at the generic point of a component of `V ∩ W`, for two quasi-coherent sheaves of ideals at a point of any scheme. The intersection product `V · W` itself, the cycle whose coefficients these are, is NOT carried; see the module docstring.”. References: SGA 4½ Cycle (2.3.9); SGA 4½ Cycle (3.5).

> **Stacks 0AZR.** The intersection multiplicity `e(X, V · W, Z)` of two closed subschemes of a
> scheme at a point: the alternating sum `∑ᵢ (-1)ⁱ length Torᵢ(𝒪_W, 𝒪_V)` of the lengths of the
> `Tor` modules of their local rings over the local ring of the ambient scheme. For `V` and `W`
> closed subvarieties of a nonsingular variety which intersect properly and `x` the generic point
> of an irreducible component `Z` of `V ∩ W`, this is the coefficient of `Z` in `V · W`.

```lean
def intersectionMultiplicity {X : Scheme.{u}} (V W : X.IdealSheafData) (x : X) : ℚ
```

**`AlgebraicGeometry.TorFormula.intersectionProductCycle`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/TorFormula/IntersectionProductCycle.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/TorFormula/IntersectionProductCycle.lean#L97). The attribute's comment: “the intersection product `W · V = ∑ᵢ (-1)ⁱ [Torᵢ^{𝒪_X}(𝒪_W, 𝒪_V)]_{r+s-dim X}` of Section 43.14, as a cycle. It is formed here for two arbitrary coherent modules on a regular scheme and an arbitrary dimension index `k`, of which the source's `W · V` is the case of the structure sheaves of two properly intersecting closed subvarieties with `k = r + s - dim X`. The source's hypothesis that `V` and `W` intersect properly — which it says is what makes the definition legitimate — enters as the hypothesis `hFk` bounding the delta-dimension of the support of each `Tor` sheaf by `k`, the bound that `Stacks.Chow.coherentSheafCycle` needs. That the alternating sum is finite is `finite_support_torSheafCycle`.”.

> **Stacks 0AZR: the intersection product.** For coherent `𝒪_X`-modules `ℱ` and `𝒢` on a
> regular scheme, the alternating sum `∑ᵢ (-1)ⁱ [Torᵢ^{𝒪_X}(ℱ, 𝒢)]_k` of the cycles of the `Tor`
> sheaves. For `ℱ = 𝒪_W` and `𝒢 = 𝒪_V` the structure sheaves of two closed subvarieties of
> dimensions `s` and `r` which intersect properly, and `k = r + s - dim X`, this is the
> intersection product `W · V`.

```lean
def intersectionProductCycle (C : Stacks.Chow.ChowSituation.{u}) {X : Scheme.{u}} (f : X ⟶ C.S)
    [LocallyOfFiniteType f] (hX : IsRegular X) (F G : X.Modules)
    (hF : SheafOfModules.IsCoherent F) (hG : SheafOfModules.IsCoherent G) (k : ℤ)
    (hFk : ∀ i : ℕ,
      haveI := isCoherent_torSheaf_of_isRegular X hX F G hF hG i
      Stacks.Chow.schemeDeltaDimension C
        ((Stacks.Chow.reducedSupport (torSheaf X F G i)).subschemeι ≫ f) ≤ WithBotTop.coe k) :
    AlgebraicCycle X ℤ
```

## Tag 0AZS, a lemma

[Tag 0AZS](https://stacks.math.columbia.edu/tag/0AZS) in the Stacks Project.

**`AlgebraicGeometry.TorFormula.derivedCategoryBMinus_derivedTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/TorFormula/CoherentTorSheaves.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/TorFormula/CoherentTorSheaves.lean#L246). The attribute's comment: “part (2): D⁻_Coh is closed under the derived tensor product”. References: SGA 6 I (2.16.1), “b), special case”.

> **[Stacks, Tag 0AZS] part (2).** Let `X` be a locally Noetherian scheme. If `K` and `L` are
> in `D⁻_Coh(𝒪_X)` then so is `K ⊗ᴸ_{𝒪_X} L`.
>
> Being in `D⁻_Coh(𝒪_X)` is equivalent to being pseudo-coherent ([Stacks, Tag 08E8]), and the
> derived tensor product of two pseudo-coherent objects is pseudo-coherent
> ([Stacks, Tag 09J3]). Reading the equivalence backwards needs the cohomology sheaves of the
> derived tensor product to be quasi-coherent, which is [Stacks, Tag 08DX]; the bound above is
> `a + b` for bounds `a` and `b` of the two factors.

```lean
theorem derivedCategoryBMinus_derivedTensor (X : Scheme.{u}) [IsLocallyNoetherian X]
    (K L : DerivedCategory X.Modules)
    (hK : DerivedCategoryB.derivedCategoryBMinus (fun F : X.Modules => F.IsCoherent) K)
    (hL : DerivedCategoryB.derivedCategoryBMinus (fun F : X.Modules => F.IsCoherent) L) :
    DerivedCategoryB.derivedCategoryBMinus (fun F : X.Modules => F.IsCoherent)
      (((derivedTensor X).obj K).obj L)
```

**`AlgebraicGeometry.TorFormula.isCoherent_torSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/TorFormula/CoherentTorSheaves.lean, line 309](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/TorFormula/CoherentTorSheaves.lean#L309). The attribute's comment: “part (1): the Tor sheaves of two coherent modules are coherent”.

> **[Stacks, Tag 0AZS] part (1).** Let `X` be a locally Noetherian scheme. If `ℱ` and `𝒢` are
> coherent `𝒪_X`-modules then so is `Tor_p^{𝒪_X}(ℱ, 𝒢)` for every `p`.
>
> A coherent module placed in degree `0` lies in `D⁻_Coh(𝒪_X)`, so part (2) applies to the two
> factors and every cohomology sheaf of their derived tensor product is coherent.

```lean
theorem isCoherent_torSheaf (X : Scheme.{u}) [IsLocallyNoetherian X] (F G : X.Modules)
    (hF : F.IsCoherent) (hG : G.IsCoherent) (p : ℕ) : (torSheaf X F G p).IsCoherent
```

## Tag 0AZT, a lemma

[Tag 0AZT](https://stacks.math.columbia.edu/tag/0AZT) in the Stacks Project.

**`AlgebraicGeometry.TorFormula.supp_torSheaf_subset_inter`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/TorFormula/CoherentTorSheaves.lean, line 444](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/TorFormula/CoherentTorSheaves.lean#L444). The attribute's comment: “the Tor sheaves are supported on the intersection of the supports of the two modules”.

> **[Stacks, Tag 0AZT]: the Tor sheaves are supported on `Supp(ℱ) ∩ Supp(𝒢)`.** Away from
> the support of either factor the corresponding stalk vanishes, and then so does the stalk of
> every `Tor_p^{𝒪_X}(ℱ, 𝒢)`.
>
> No hypothesis on `X` or on the two modules is needed: the argument is the stalkwise computation
> of the derived tensor product on K-flat representatives.

```lean
theorem supp_torSheaf_subset_inter (X : Scheme.{u}) (F G : X.Modules) (p : ℕ) :
    SheafOfModules.supp (torSheaf X F G p) ⊆
      SheafOfModules.supp F ∩ SheafOfModules.supp G
```

**`AlgebraicGeometry.TorFormula.isCoherent_torSheaf_of_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/TorFormula/CoherentTorSheaves.lean, line 463](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/TorFormula/CoherentTorSheaves.lean#L463). The attribute's comment: “the Tor sheaves of two coherent modules on a regular scheme are coherent”.

> **[Stacks, Tag 0AZT]: the Tor sheaves of two coherent modules on a regular scheme are
> coherent.** A regular — that is, nonsingular — scheme is locally Noetherian, by the
> characterization of regularity as local Noetherianity together with regularity of all the local
> rings, so [Stacks, Tag 0AZS] part (1) applies.

```lean
theorem isCoherent_torSheaf_of_isRegular (X : Scheme.{u}) (hX : IsRegular X)
    (F G : X.Modules) (hF : F.IsCoherent) (hG : G.IsCoherent) (p : ℕ) :
    (torSheaf X F G p).IsCoherent
```

**`AlgebraicGeometry.TorFormula.torSheafStalkIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/TorFormula/TorSheafStalk.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/TorFormula/TorSheafStalk.lean#L213). The attribute's comment: “the stalk clause: the stalk at `x` of `Tor_p^{𝒪_X}(ℱ, 𝒢)` is the Tor module `Tor_p^{𝒪_{X, x}}(ℱ_x, 𝒢_x)` of the two stalks over the local ring, with no hypothesis on the scheme or the two modules. The local ring is the `RingCat`-valued stalk of the structure sheaf, which is the ring the stalk functor takes its modules over. The coherence and support clauses are `isCoherent_torSheaf_of_isRegular` and `supp_torSheaf_subset_inter`; the vanishing clause for `p > dim X` is NOT carried, see the module docstring.”.

> **Stacks 0AZT: the stalk of a Tor sheaf is the Tor module of the stalks.** For `𝒪_X`-modules
> `ℱ` and `𝒢` on a scheme `X` and a point `x`, the stalk at `x` of `Tor_p^{𝒪_X}(ℱ, 𝒢)` is
> `Tor_p^{𝒪_{X, x}}(ℱ_x, 𝒢_x)`. No hypothesis on `X`, `ℱ` or `𝒢` is needed.

```lean
def torSheafStalkIso (X : Scheme.{u}) (F G : X.Modules) (p : ℕ) (x : X) :
    letI : MonoidalCategory (ModuleCat.{u} (TopCat.Presheaf.stalk (C := RingCat.{u})
        (Stacks.SheafOfModules.Tensor.ringSheaf.{u, u, u} X.sheaf).obj x)) :=
      Stacks.SheafOfModules.KFlatStalkCriterion.monoidalStalkModuleCat X.sheaf x
    letI : MonoidalPreadditive (ModuleCat.{u} (TopCat.Presheaf.stalk (C := RingCat.{u})
        (Stacks.SheafOfModules.Tensor.ringSheaf.{u, u, u} X.sheaf).obj x)) :=
      Stacks.SheafOfModules.KFlatStalkCriterion.monoidalPreadditiveStalkModuleCat X.sheaf x
    (Scheme.Modules.stalkFunctor X x).obj (torSheaf X F G p) ≅
      ((Tor (ModuleCat.{u} (TopCat.Presheaf.stalk (C := RingCat.{u})
            (Stacks.SheafOfModules.Tensor.ringSheaf.{u, u, u} X.sheaf).obj x)) p).obj
          ((Scheme.Modules.stalkFunctor X x).obj F)).obj
        ((Scheme.Modules.stalkFunctor X x).obj G)
```

**`AlgebraicGeometry.TorFormula.isZero_torSheaf_of_lt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/TorFormula/TorSheafVanishing.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/TorFormula/TorSheafVanishing.lean#L107). The attribute's comment: “the vanishing clause: on a scheme all of whose local rings are regular and whose dimension is at most `d`, the Tor sheaf `Tor_p^{𝒪_X}(ℱ, 𝒢)` vanishes for `p > d`. The source states it for a nonsingular variety with the bound `dim X`, which is the case `d = dim X` of this; the bound is a parameter here because the dimension of a general scheme need not be finite. No hypothesis on the two modules is needed, where the source assumes them coherent. The coherence, support and stalk clauses are `isCoherent_torSheaf_of_isRegular`, `supp_torSheaf_subset_inter` and `torSheafStalkIso`.”.

> **Stacks 0AZT: the Tor sheaves of a regular scheme vanish above its dimension.** If every
> local ring of `X` is regular and `dim X ≤ d`, then `Tor_p^{𝒪_X}(ℱ, 𝒢) = 0` for every `p > d` and
> all `𝒪_X`-modules `ℱ`, `𝒢`.

```lean
theorem isZero_torSheaf_of_lt (X : Scheme.{u})
    (hreg : ∀ x : X, IsRegularLocalRing (X.presheaf.stalk x))
    (F G : X.Modules) (d p : ℕ) (hd : topologicalKrullDim X ≤ (d : WithBot ℕ∞))
    (hdp : d < p) :
    IsZero (torSheaf X F G p)
```

## Tag 0B1I, a lemma

[Tag 0B1I](https://stacks.math.columbia.edu/tag/0B1I) in the Stacks Project.

**`AlgebraicGeometry.intersectionMultiplicity_eq_one_and_exists_isOpen_smoothAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/TorFormulaMultiplicities/MultiplicityOneSmoothness.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/TorFormulaMultiplicities/MultiplicityOneSmoothness.lean#L181). The attribute's comment: “both conclusions, at the generic point of the component”.

> **Stacks 0B1I.** Let `X` be a nonsingular variety over a perfect field `k`, let `V` and `W` be
> the closed subschemes of `X` cut out by the quasi-coherent sheaves of ideals `IV` and `IW`, and
> let `ζ` be the generic point of an irreducible component `Z` of the scheme-theoretic intersection
> `V ∩ W`, with image `ξ` in `X`. Assume that `V` and `W` intersect properly along `Z`, in the local
> form `dim 𝒪_{X, ξ} ≤ dim 𝒪_{V, ξ} + dim 𝒪_{W, ξ}`, and that the multiplicity of `Z` in `V ∩ W`
> is one. Then the intersection multiplicity is `e(X, V · W, Z) = 1`, and there is an open
> neighbourhood of `ξ` in `X` over which both `V` and `W` are smooth: `V` and `W` are smooth in a
> general point of `Z`.

```lean
theorem intersectionMultiplicity_eq_one_and_exists_isOpen_smoothAt (k : Type u) [Field k]
    [PerfectField k] {X : Scheme.{u}} (p : X ⟶ Spec (.of k)) [LocallyOfFiniteType p]
    (IV IW : X.IdealSheafData) (ζ : genericPoints (IV ⊔ IW).subscheme)
    (hX : IsRegularLocalRing (X.presheaf.stalk ((IV ⊔ IW).subschemeι ζ.1)))
    (hproper : ringKrullDim (X.presheaf.stalk ((IV ⊔ IW).subschemeι ζ.1)) ≤
      ringKrullDim (X.presheaf.stalk ((IV ⊔ IW).subschemeι ζ.1) ⧸
          IdealSheafData.stalk IV ((IV ⊔ IW).subschemeι ζ.1)) +
        ringKrullDim (X.presheaf.stalk ((IV ⊔ IW).subschemeι ζ.1) ⧸
          IdealSheafData.stalk IW ((IV ⊔ IW).subschemeι ζ.1)))
    (hmult : Stacks.Chow.componentMultiplicity (IV ⊔ IW).subschemeι ζ = 1) :
    Stacks.Intersection.intersectionMultiplicity IV IW ((IV ⊔ IW).subschemeι ζ.1) = 1 ∧
      ∃ U : X.Opens, (IV ⊔ IW).subschemeι ζ.1 ∈ U ∧
        (∀ v : IV.subscheme, IV.subschemeι v ∈ U →
          InfinitesimalLifting.SmoothAt (IV.subschemeι ≫ p) v) ∧
        (∀ w : IW.subscheme, IW.subschemeι w ∈ U →
          InfinitesimalLifting.SmoothAt (IW.subschemeι ≫ p) w)
```

**`IsRegularLocalRing.localIntersectionMultiplicity_eq_one_of_length_quotient_sup_eq_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/TorFormulaMultiplicities/TransversalIntersection.lean, line 615](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/TorFormulaMultiplicities/TransversalIntersection.lean#L615). The attribute's comment: “the Tor-formula multiplicity, in local form at the generic point”.

> **Stacks 0B1I, the multiplicity-one case of the Tor formula.** Let `A` be a regular local ring
> and let `I`, `J` be ideals with `Module.length A (A ⧸ (I ⊔ J)) = 1` and
> `dim A ≤ dim (A ⧸ I) + dim (A ⧸ J)`. Then the intersection multiplicity of the pair computed by
> the Tor formula is `1`. Geometrically, for `A` the local ring of a nonsingular variety `X` at the
> generic point of an irreducible component `Z` of `V ∩ W`, with `I` and `J` the local ideals of two
> closed subvarieties intersecting properly and `Z` of multiplicity one in `V ∩ W`, this says
> `e(X, V · W, Z) = 1`.

```lean
theorem localIntersectionMultiplicity_eq_one_of_length_quotient_sup_eq_one {A : Type u}
    [CommRing A] [IsRegularLocalRing A] (I J : Ideal A)
    (hmult : Module.length A (A ⧸ (I ⊔ J)) = 1)
    (hproper : ringKrullDim A ≤ ringKrullDim (A ⧸ I) + ringKrullDim (A ⧸ J)) :
    I.localIntersectionMultiplicity (A ⧸ J) = 1
```

## Tag 0B2S, an example

[Tag 0B2S](https://stacks.math.columbia.edu/tag/0B2S) in the Stacks Project.

**`Stacks.Intersection.TwoPlanes.length_stalk_quotient_sup_eq_three_and_intersectionMultiplicity_eq_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/TorFormulaMultiplicities/HigherTorsCompletion.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/TorFormulaMultiplicities/HigherTorsCompletion.lean#L84). The attribute's comment: “the example as stated: for X, p, V, W with an isomorphism of the completed local ring at p with ℂ[[x, y, z, w]] carrying the ideals of V and W to (xz, xw, yz, yw) and (x - z, y - w), the length of 𝒪_{X,p} / (I_V + I_W) is 3 and the chapter's intersection multiplicity e(X, V · W, p) is 2; stated for any locally Noetherian X, any point and any closed subschemes, which contains the source's nonsingular fourfold, closed point and subvarieties”.

> **Tag 0B2S, the two numbers of the example.** Let `X` be a locally Noetherian scheme (for
> instance a nonsingular variety of dimension `4` over `ℂ`), let `p ∈ X` and let `V`, `W` be closed
> subschemes of `X`, given by their ideal sheaves. Assume there is a ring isomorphism
> `e : 𝒪_{X, p}^∧ ≅ ℂ[[x, y, z, w]]` carrying the ideal of `V` in `𝒪_{X, p}^∧` to
> `(xz, xw, yz, yw)` and the ideal of `W` to `(x - z, y - w)`. Then
> `length_{𝒪_{X, p}} 𝒪_{X, p} ⧸ (I_V + I_W) = 3`, while the intersection multiplicity given by the
> Tor formula over `𝒪_{X, p}` is `e(X, V · W, p) = 2`.
>
> The proof transfers the computation in `ℂ[[x, y, z, w]]` along `𝒪_{X, p} → 𝒪_{X, p}^∧ ≅
> ℂ[[x, y, z, w]]`, which is flat, local, and carries the maximal ideal onto the maximal ideal, so
> that it preserves lengths and commutes with Tor.

```lean
theorem length_stalk_quotient_sup_eq_three_and_intersectionMultiplicity_eq_two
    {X : Scheme.{0}} [IsLocallyNoetherian X] (V W : X.IdealSheafData) (p : X)
    (e : AdicCompletion (maximalIdeal (X.presheaf.stalk p)) (X.presheaf.stalk p) ≃+*
      MvPowerSeries (Fin 4) ℂ)
    (hV : ((IdealSheafData.stalk V p).map (algebraMap (X.presheaf.stalk p)
      (AdicCompletion (maximalIdeal (X.presheaf.stalk p)) (X.presheaf.stalk p)))).map e =
        unionOfPlanes)
    (hW : ((IdealSheafData.stalk W p).map (algebraMap (X.presheaf.stalk p)
      (AdicCompletion (maximalIdeal (X.presheaf.stalk p)) (X.presheaf.stalk p)))).map e =
        diagonalPlane) :
    Module.length (X.presheaf.stalk p)
        ((X.presheaf.stalk p) ⧸ IdealSheafData.stalk (V ⊔ W) p) = 3 ∧
      Stacks.Intersection.intersectionMultiplicity V W p = 2
```

**`Stacks.Intersection.TwoPlanes.exists_isSmoothVariety_closedPoint_subvarieties_completion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/TorFormulaMultiplicities/HigherTorsExistence.lean, line 189](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/TorFormulaMultiplicities/HigherTorsExistence.lean#L189). The attribute's comment: “the existence clause "To make an actual example ...": there exist a smooth variety X of dimension 4 over ℂ, a closed point p and integral closed subschemes V, W with an isomorphism of the completed local ring at p with ℂ[[x, y, z, w]] carrying I_V to (xz, xw, yz, yw) and I_W to (x - z, y - w), and for them the length is 3 and e(X, V · W, p) = 2; proved with one explicit instance in A^4 (V the image of (s, t) ↦ (s² - 1, t, s(s² - 1), st), W the plane c = d = 0) in place of the source's general morphism P^2 → P^4”.

> **Tag 0B2S, "To make an actual example": the situation of the example exists.** There are a
> smooth (that is, nonsingular) variety `X` of dimension `4` over `ℂ`, a closed point `p ∈ X`, and
> integral closed subschemes (closed subvarieties) `V, W ⊂ X`, with a ring isomorphism
> `e : 𝒪_{X, p}^∧ ≅ ℂ[[x, y, z, w]]` carrying the ideal of `V` to `(xz, xw, yz, yw)` and the ideal of
> `W` to `(x - z, y - w)`; for them `length_{𝒪_{X, p}} 𝒪_{X, p} ⧸ (I_V + I_W) = 3` and
> `e(X, V · W, p) = 2`.
>
> The instance is `X = 𝔸⁴_ℂ`, `p` the origin, `V` the image of `𝔸² → 𝔸⁴`,
> `(s, t) ↦ (s² - 1, t, s (s² - 1), s t)`, which identifies `(1, 0)` and `(-1, 0)` and has two
> transverse smooth branches at `p`, and `W` the plane `c = d = 0` through `p`.

```lean
theorem exists_isSmoothVariety_closedPoint_subvarieties_completion :
    ∃ (X : Scheme.{0}) (f : X ⟶ Spec (CommRingCat.of ℂ)), IsSmoothVariety ℂ f ∧
      topologicalKrullDim X = 4 ∧
      ∃ (p : X) (V W : X.IdealSheafData), IsClosed ({p} : Set X) ∧
        IsIntegral V.subscheme ∧ IsIntegral W.subscheme ∧
        (∃ e : AdicCompletion (maximalIdeal (X.presheaf.stalk p)) (X.presheaf.stalk p) ≃+*
            MvPowerSeries (Fin 4) ℂ,
          ((IdealSheafData.stalk V p).map (algebraMap _ (AdicCompletion _ _))).map e =
              unionOfPlanes ∧
            ((IdealSheafData.stalk W p).map (algebraMap _ (AdicCompletion _ _))).map e =
              diagonalPlane) ∧
        Module.length (X.presheaf.stalk p)
            ((X.presheaf.stalk p) ⧸ IdealSheafData.stalk (V ⊔ W) p) = 3 ∧
          Stacks.Intersection.intersectionMultiplicity V W p = 2
```

**`Stacks.Intersection.TwoPlanes.length_quotient_sup_eq_three_and_localIntersectionMultiplicity_eq_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/TorFormulaMultiplicities/HigherTorsMultiplicity.lean, line 1206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/TorFormulaMultiplicities/HigherTorsMultiplicity.lean#L1206). The attribute's comment: “the power series computation of the example: in ℂ[[x, y, z, w]] the length of the quotient by (xz, xw, yz, yw) + (x - z, y - w) is 3 and the Tor-formula multiplicity of the pair is 2; the statement on a variety and the existence clause are registered separately”.

> **The two numbers of the example, computed in `ℂ[[x, y, z, w]]`.** For the union of the two
> planes `x = y = 0` and `z = w = 0`, with ideal `(xz, xw, yz, yw)`, and the plane `x = z`, `y = w`,
> with ideal `(x - z, y - w)`, the scheme-theoretic intersection has
> `length ℂ[[x, y, z, w]] / (xz, xw, yz, yw, x - z, y - w) = 3`, while the multiplicity given by the
> Tor formula is `2`. The two differ, so the alternating sum over all the Tor modules cannot be
> replaced by its degree-zero term.
>
> This is the computation in the completed local ring. The example itself is stated for a variety:
> `length_stalk_quotient_sup_eq_three_and_intersectionMultiplicity_eq_two` transfers both numbers
> to `𝒪_{X, p}` and to the chapter's multiplicity `e(X, V · W, p)` along an isomorphism
> `𝒪_{X, p}^∧ ≅ ℂ[[x, y, z, w]]`, and the source's closing sentence, that such
> `X, p, V, W` exist with `V` and `W` closed subvarieties, is
> `exists_isSmoothVariety_closedPoint_subvarieties_completion`, proved
> with an explicit integral surface in `𝔸⁴_ℂ` whose two branches at the origin are transverse smooth
> planes.

```lean
theorem length_quotient_sup_eq_three_and_localIntersectionMultiplicity_eq_two :
    Module.length (MvPowerSeries (Fin 4) ℂ)
        (MvPowerSeries (Fin 4) ℂ ⧸ (unionOfPlanes ⊔ diagonalPlane)) = 3 ∧
      diagonalPlane.localIntersectionMultiplicity
        (MvPowerSeries (Fin 4) ℂ ⧸ unionOfPlanes) = 2
```

**`Stacks.Intersection.TwoPlanes.length_quotient_sup_eq_three`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/TorFormulaMultiplicities/HigherTorsNecessary.lean, line 459](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/TorFormulaMultiplicities/HigherTorsNecessary.lean#L459). The attribute's comment: “the length-3 computation of the example: the naive count for the pair of ideals”.

> **The naive count of the intersection of the two planes with the plane `x = z`, `y = w`.**
> The length of `ℂ[[x, y, z, w]] / (xz, xw, yz, yw, x - z, y - w)` is `3`: the sum of the two
> ideals is `(x - z, y - w) + 𝔪 ^ 2`, whose quotient is `ℂ[[x, y]] / (x, y) ^ 2`. This is the
> length of `Tor_0` in the Tor formula for the intersection multiplicity, and it differs from the
> true multiplicity `2`.

```lean
theorem length_quotient_sup_eq_three :
    Module.length (MvPowerSeries (Fin 4) ℂ)
      (MvPowerSeries (Fin 4) ℂ ⧸ (unionOfPlanes ⊔ diagonalPlane)) = 3
```

**`Stacks.Intersection.TwoPlanes.not_isZero_tor_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/TorFormulaMultiplicities/HigherTorsNecessary.lean, line 666](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/TorFormulaMultiplicities/HigherTorsNecessary.lean#L666). The attribute's comment: “higher Tors are necessary: Tor_1 of the two quotients is nonzero, so the alternating sum is not its degree-zero term; the value e = 2 itself is not computed here”.

> **The higher Tor modules are necessary in the Tor formula for intersection multiplicities.**
> For `V` the union of the two planes `x = y = 0` and `z = w = 0` in `X` a nonsingular fourfold and
> `W` the plane `x = z`, `y = w`, the module `Tor_1^A(𝒪_W, 𝒪_V)` at the point of intersection is
> nonzero. Hence the alternating sum of the lengths of the Tor modules, which is the intersection
> multiplicity `e(X, V · W, p) = 2`, is not the degree-zero term
> `length 𝒪_{V ∩ W, p} = 3` on its own.

```lean
theorem not_isZero_tor_one :
    ¬ IsZero (((Tor (ModuleCat (MvPowerSeries (Fin 4) ℂ)) 1).obj
        (ModuleCat.of (MvPowerSeries (Fin 4) ℂ)
          (MvPowerSeries (Fin 4) ℂ ⧸ diagonalPlane))).obj
      (ModuleCat.of (MvPowerSeries (Fin 4) ℂ)
        (MvPowerSeries (Fin 4) ℂ ⧸ unionOfPlanes)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 43.14, Tag 0AZR](https://stacks.math.columbia.edu/tag/0AZR)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
