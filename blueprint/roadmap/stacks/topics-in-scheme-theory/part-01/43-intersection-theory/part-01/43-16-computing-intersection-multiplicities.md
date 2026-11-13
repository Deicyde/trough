---
declaration: section
origin: cited
lean: AlgebraicGeometry.TorFormula.localIntersectionMultiplicity_stalk_eq_length_stalk_sup_of_isCohenMacaulay, AlgebraicGeometry.TorFormula.cohenMacaulayIntersectionFormula, Ideal.generalizedHilbertSamuelMultiplicity_eq_alternatingSum_tor_length, Stacks.Intersection.localIntersectionMultiplicity_eq_factorial_mul_leadingCoeff, Stacks.Intersection.localIntersectionMultiplicity_eq_length_quotient_smul_of_isDomain, Ideal.localIntersectionMultiplicity_eq_length_quotient_smul_of_isCohenMacaulayLocalRing
statement: formalized
proof: formalized
---

# 43.16 Computing intersection multiplicities

Section 43.16 of the Stacks Project, [Tag 0B01](https://stacks.math.columbia.edu/tag/0B01). 5 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0B02, a lemma

[Tag 0B02](https://stacks.math.columbia.edu/tag/0B02) in the Stacks Project.

**`AlgebraicGeometry.TorFormula.localIntersectionMultiplicity_stalk_eq_length_stalk_sup_of_isCohenMacaulay`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/ComputingIntersectionMultiplicities/CohenMacaulayCycle.lean, line 408](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/ComputingIntersectionMultiplicities/CohenMacaulayCycle.lean#L408). The attribute's comment: “the first clause, at one component: `e(X, V · W, Z) = length_{𝒪_{X, ξ}}(𝒪_{V ∩ W, ξ})` for an irreducible component `Z` of `V ∩ W` with generic point `ξ`, assuming only that `𝒪_{V, ξ}` and `𝒪_{W, ξ}` are Cohen-Macaulay. The nonsingular variety is a locally Noetherian regular scheme `Y`, the closed subvarieties are sheaves of ideals `V` and `W`, and every hypothesis is read at `ξ` alone: `ξ` lies on `V` and on `W`, that `ξ` is a generic point of a component of `V ∩ W` is the radical condition `√(V_ξ ⊔ W_ξ) = 𝔪_ξ`, and proper intersection at `Z` is the dimension inequality `dim 𝒪_{X, ξ} ≤ dim 𝒪_{V, ξ} + dim 𝒪_{W, ξ}` of Tag 0B1I (for a variety, `dim Z ≤ dim V + dim W - dim X`). `e(X, V · W, Z)` is `Ideal.localIntersectionMultiplicity`, the alternating sum of lengths of `Tor` modules by which Section 43.14 defines the coefficient of `Z` in `V · W`, and `𝒪_{V ∩ W, ξ}` is the stalk at `ξ` of the scheme-theoretic intersection, cut out by `V ⊔ W`. The final `In particular` clause is `AlgebraicGeometry.TorFormula.cohenMacaulayIntersectionFormula`.”.

> **Stacks Project, Tag 0B02, the multiplicity formula at one component.** Let `Y` be a
> locally Noetherian regular scheme and `V`, `W` sheaves of ideals, and let `ξ` be a point lying
> on both of them which is a generic point of `V ∩ W` and at which `V` and `W` intersect
> properly. If `𝒪_{V, ξ}`
> and `𝒪_{W, ξ}` are Cohen-Macaulay, then
>
> `e(X, V · W, Z) = length_{𝒪_{X, ξ}}(𝒪_{V ∩ W, ξ})`,
>
> where `Z` is the component of `V ∩ W` with generic point `ξ` and `V ∩ W` is the
> scheme-theoretic intersection, cut out by `V ⊔ W`. Every hypothesis is imposed at `ξ` alone.

```lean
theorem localIntersectionMultiplicity_stalk_eq_length_stalk_sup_of_isCohenMacaulay
    [IsLocallyNoetherian Y] (hY : IsRegular Y) (V W : Y.IdealSheafData) (z : Y)
    (hzV : z ∈ V.support) (hzW : z ∈ W.support)
    (hCMV : haveI := isLocalRing_quotient_stalk V z hzV
      IsCohenMacaulayLocalRing (Y.presheaf.stalk z ⧸ IdealSheafData.stalk V z))
    (hCMW : haveI := isLocalRing_quotient_stalk W z hzW
      IsCohenMacaulayLocalRing (Y.presheaf.stalk z ⧸ IdealSheafData.stalk W z))
    (hproper : ringKrullDim (Y.presheaf.stalk z) ≤
      ringKrullDim (Y.presheaf.stalk z ⧸ IdealSheafData.stalk V z) +
        ringKrullDim (Y.presheaf.stalk z ⧸ IdealSheafData.stalk W z))
    (hcomponent : (IdealSheafData.stalk V z ⊔ IdealSheafData.stalk W z).radical =
      IsLocalRing.maximalIdeal (Y.presheaf.stalk z)) :
    (IdealSheafData.stalk V z).localIntersectionMultiplicity
        (Y.presheaf.stalk z ⧸ IdealSheafData.stalk W z) =
      ((Module.length (Y.presheaf.stalk z)
        (Y.presheaf.stalk z ⧸ IdealSheafData.stalk (V ⊔ W) z)).toNat : ℚ)
```

**`AlgebraicGeometry.TorFormula.cohenMacaulayIntersectionFormula`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/ComputingIntersectionMultiplicities/CohenMacaulayCycle.lean, line 471](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/ComputingIntersectionMultiplicities/CohenMacaulayCycle.lean#L471). The attribute's comment: “the whole lemma: both the multiplicity formula `e(X, V · W, Z) = length_{𝒪_{X, ξ}}(𝒪_{V ∩ W, ξ})` at the generic point of each component of `V ∩ W` and the source's final `In particular` clause, `V · W = [V ∩ W]_{dim V + dim W - dim X}`, as an identity of algebraic cycles. The nonsingular variety is a regular scheme `Y` of dimension at most `d`, the two closed subvarieties are sheaves of ideals `V` and `W`, and `V · W` is the Section 43.14 product of Tag 0AZR, `AlgebraicGeometry.TorFormula.intersectionProductCycle`, which takes the delta-dimension bounds `hFk` on the supports of the `Tor` sheaves exactly as the definition of that tag does. The source's hypotheses are local at the generic point `ξ` of a component of `V ∩ W`, and that is where they are read: at a point `z` of delta-dimension `k` lying on both subvarieties — which under `hVW` is exactly such a generic point — `𝒪_{V, z}` and `𝒪_{W, z}` are Cohen-Macaulay, proper intersection is the dimension inequality of Tag 0B1I, and that `z` is a generic point of `V ∩ W` is the radical condition. `e(X, V · W, Z)` is `Ideal.localIntersectionMultiplicity`, the alternating sum of lengths of `Tor` modules by which Section 43.14 computes the multiplicity, and `𝒪_{V ∩ W, ξ}` is the stalk at `z` of the scheme-theoretic intersection, cut out by `V ⊔ W`. `WithBot ℕ∞` has no subtraction, so the source's dimension index `dim V + dim W - dim X` is generalised to an arbitrary `k`, the index at which the two cycles are formed and whose relation to `V ∩ W` is the delta-dimension bound `hVW`. Here the hypotheses are imposed at every such generic point at once, as the `In particular` clause needs; the first clause at a single component, with hypotheses at its generic point alone, is `TorFormula.localIntersectionMultiplicity_stalk_eq_length_stalk_sup_of_isCohenMacaulay`.”.

> **Stacks Project, Tag 0B02.** Let `X` be a nonsingular variety and `V`, `W ⊆ X` closed
> subvarieties which intersect properly, let `Z` be an irreducible component of `V ∩ W` with
> generic point `ξ`, and assume `𝒪_{V, ξ}` and `𝒪_{W, ξ}` are Cohen-Macaulay. Then
>
> `e(X, V · W, Z) = length_{𝒪_{X, ξ}}(𝒪_{V ∩ W, ξ})`,
>
> where `V ∩ W` is the scheme-theoretic intersection; and in particular, if both `V` and `W` are
> Cohen-Macaulay, then `V · W = [V ∩ W]_{dim V + dim W - dim X}`.
>
> The nonsingular variety is a regular scheme `Y` of dimension at most `d`, the two closed
> subvarieties are sheaves of ideals `V` and `W`, and `ξ` is a point `z` of delta-dimension `k`
> lying on both of them, which under `hVW` is exactly the generic point of a component of
> `V ∩ W`. The multiplicity `e(X, V · W, Z)` is `Ideal.localIntersectionMultiplicity`, the
> alternating sum of lengths of `Tor` modules by which Section 43.14 computes it, and
> `𝒪_{V ∩ W, ξ}` is the stalk of the scheme-theoretic intersection, cut out by `V ⊔ W`. The
> product `V · W` is the cycle `AlgebraicGeometry.TorFormula.intersectionProductCycle` of
> Tag 0AZR.

```lean
theorem cohenMacaulayIntersectionFormula
    (C : Stacks.Chow.ChowSituation.{u}) (f : Y ⟶ C.S) [LocallyOfFiniteType f]
    [IsLocallyNoetherian Y] (hY : IsRegular Y) (V W : Y.IdealSheafData) (k : ℤ)
    (d : ℕ) (hd : topologicalKrullDim Y ≤ (d : WithBot ℕ∞))
    (hVW : Stacks.Chow.schemeDeltaDimension C ((V ⊔ W).subschemeι ≫ f) ≤ (k : EInt))
    (hFk : ∀ i : ℕ,
      haveI := isCoherent_torSheaf_of_isRegular Y hY (subschemeStructureSheaf V)
        (subschemeStructureSheaf W) (isCoherent_subschemeStructureSheaf V)
        (isCoherent_subschemeStructureSheaf W) i
      Stacks.Chow.schemeDeltaDimension C
        ((Stacks.Chow.reducedSupport
          (torSheaf Y (subschemeStructureSheaf V) (subschemeStructureSheaf W) i)).subschemeι ≫ f)
        ≤ WithBotTop.coe k)
    (hpt : ∀ z : Y, Stacks.Chow.relativeDimension C.dimensionFunction f z = k →
      ∀ (hzV : z ∈ V.support) (hzW : z ∈ W.support),
        haveI := isLocalRing_quotient_stalk V z hzV
        haveI := isLocalRing_quotient_stalk W z hzW
        IsCohenMacaulayLocalRing (Y.presheaf.stalk z ⧸ IdealSheafData.stalk V z) ∧
        IsCohenMacaulayLocalRing (Y.presheaf.stalk z ⧸ IdealSheafData.stalk W z) ∧
        ringKrullDim (Y.presheaf.stalk z) ≤
          ringKrullDim (Y.presheaf.stalk z ⧸ IdealSheafData.stalk V z) +
            ringKrullDim (Y.presheaf.stalk z ⧸ IdealSheafData.stalk W z) ∧
        (IdealSheafData.stalk V z ⊔ IdealSheafData.stalk W z).radical =
          IsLocalRing.maximalIdeal (Y.presheaf.stalk z)) :
    (∀ z : Y, Stacks.Chow.relativeDimension C.dimensionFunction f z = k →
        z ∈ V.support → z ∈ W.support →
          (IdealSheafData.stalk V z).localIntersectionMultiplicity
              (Y.presheaf.stalk z ⧸ IdealSheafData.stalk W z) =
            ((Module.length (Y.presheaf.stalk z)
              (Y.presheaf.stalk z ⧸ IdealSheafData.stalk (V ⊔ W) z)).toNat : ℚ)) ∧
      (Stacks.Chow.cycleAssociatedToClosedSubscheme C f (V ⊔ W).subschemeι k).1 =
        intersectionProductCycle C f hY (subschemeStructureSheaf V) (subschemeStructureSheaf W)
          (isCoherent_subschemeStructureSheaf V) (isCoherent_subschemeStructureSheaf W) k hFk
```

## Tag 0B03, a lemma

[Tag 0B03](https://stacks.math.columbia.edu/tag/0B03) in the Stacks Project.

**`Ideal.generalizedHilbertSamuelMultiplicity_eq_alternatingSum_tor_length`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/ComputingIntersectionMultiplicities/TorEulerCharacteristic.lean, line 290](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/ComputingIntersectionMultiplicities/TorEulerCharacteristic.lean#L290).

> The generalized multiplicity of an ideal generated by a regular sequence equals the
> alternating sum of the lengths of the Tor groups of `A / I` and `M`.

```lean
theorem generalizedHilbertSamuelMultiplicity_eq_alternatingSum_tor_length
    {A : Type u} [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (I : Ideal A) (r : ℕ) (f : Fin r → A) (M : Type u)
    [AddCommGroup M] [Module A M] [Module.Finite A M]
    (hf : RingTheory.Sequence.IsRegular A (List.ofFn f))
    (hI : I = Ideal.span (Set.range f))
    (hM : Module.supportDim A (M ⧸ I • (⊤ : Submodule A M)) = 0) :
    I.generalizedHilbertSamuelMultiplicity M r =
      ∑ i : Fin (r + 1), (-1 : ℚ) ^ (i : ℕ) *
        ((Module.length A
          (((Tor (ModuleCat.{u} A) (i : ℕ)).obj (ModuleCat.of A (A ⧸ I))).obj
            (ModuleCat.of A M))).toNat : ℚ)
```

## Tag 0B04, a lemma

[Tag 0B04](https://stacks.math.columbia.edu/tag/0B04) in the Stacks Project.

**`Stacks.Intersection.localIntersectionMultiplicity_eq_factorial_mul_leadingCoeff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/ComputingIntersectionMultiplicities/HilbertPolynomialMultiplicity.lean, line 486](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/ComputingIntersectionMultiplicities/HilbertPolynomialMultiplicity.lean#L486). The attribute's comment: “the multiplicity formula and the positivity of the leading coefficient, in local form at the generic point”.

> **Stacks 0B04, in local form at the generic point.** Let `A` be a regular local ring, let `I`
> be an ideal generated by a regular sequence `f₁, …, f_c`, and let `J` be an ideal with
> `dim (A ⧸ (I ⊔ J)) = 0` and `dim A ≤ dim (A ⧸ I) + dim (A ⧸ J)`. Then the function
> `t ↦ length_A ((A ⧸ J) ⧸ I ^ t (A ⧸ J))` is computed for `t ≫ 0` by a rational polynomial of
> degree `c` with positive leading coefficient, and the Tor-formula intersection multiplicity of
> the pair is `c !` times that leading coefficient.
>
> Geometrically, for `A` the local ring of a nonsingular variety `X` at the generic point `ξ` of an
> irreducible component `Z` of `V ∩ W`, with `I` and `J` the local ideals of two closed
> subvarieties intersecting properly and `I` cut out by a regular sequence of length `c`, this says
> that `e(X, V · W, Z)` is `c !` times the leading coefficient of the Hilbert polynomial
> `t ↦ length_{𝒪_{X, ξ}} 𝒪_{W, ξ} / (f₁, …, f_c) ^ t`, and that this coefficient is positive.

```lean
theorem localIntersectionMultiplicity_eq_factorial_mul_leadingCoeff {A : Type u} [CommRing A]
    [IsRegularLocalRing A] {c : ℕ} (f : Fin c → A) (I J : Ideal A)
    (hf : RingTheory.Sequence.IsRegular A (List.ofFn f))
    (hI : I = Ideal.span (Set.range f))
    (h0 : ringKrullDim (A ⧸ (I ⊔ J)) = 0)
    (hproper : ringKrullDim A ≤ ringKrullDim (A ⧸ I) + ringKrullDim (A ⧸ J)) :
    ∃ P : ℚ[X], I.ComputesGeneralizedHilbertPoly (A ⧸ J) P ∧
      P.degree = (c : WithBot ℕ) ∧ 0 < P.leadingCoeff ∧
      I.localIntersectionMultiplicity (A ⧸ J) = (c.factorial : ℚ) * P.leadingCoeff
```

## Tag 0B05, a lemma

[Tag 0B05](https://stacks.math.columbia.edu/tag/0B05) in the Stacks Project.

**`Stacks.Intersection.localIntersectionMultiplicity_eq_length_quotient_smul_of_isDomain`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/ComputingIntersectionMultiplicities/HilbertPolynomialMultiplicity.lean, line 589](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/ComputingIntersectionMultiplicities/HilbertPolynomialMultiplicity.lean#L589). The attribute's comment: “the multiplicity formula for an effective Cartier divisor, in local form at the generic point: for `I` generated by a single nonzerodivisor `f₁` of the regular local ring `A` and `A ⧸ J` a domain, the Tor-formula multiplicity of the pair is `length_A ((A ⧸ J) ⧸ f₁ (A ⧸ J))`. The hypotheses are those of Tag 0B04, transported to `A = 𝒪_{X, ξ}` exactly as there, with the extra hypothesis that `A ⧸ J` is a domain, which the source carries in the standing assumption that `W` is a closed subvariety and which the local form of Tag 0B04 does not need; without it the conclusion fails, for instance for `A = k[x, y]` at the origin with `I = (y)` and `J = (x², xy)`.”.

> **Stacks 0B05.** In the situation of Tag 0B04, assume `c = 1`, so that `I = (f₁)` with `f₁` a
> nonzerodivisor of `A`, and assume `A ⧸ J` is a domain. Then the Tor-formula intersection
> multiplicity of the pair is the single length `length_A ((A ⧸ J) ⧸ f₁ (A ⧸ J))`.
>
> Geometrically, for `A = 𝒪_{X, ξ}` at the generic point `ξ` of an irreducible component `Z` of
> `V ∩ W` and `I`, `J` the local ideals of two closed subvarieties intersecting properly, `c = 1`
> says that `V` is an effective Cartier divisor and `A ⧸ J = 𝒪_{W, ξ}` is a domain because `W` is
> a variety; the conclusion is
> `e(X, V · W, Z) = length_{𝒪_{X, ξ}}(𝒪_{W, ξ} / f₁ 𝒪_{W, ξ})`. The hypothesis
> `dim (A ⧸ (I ⊔ J)) = 0` forces `f₁ ∉ J`, so `f₁` is a nonzerodivisor on the one-dimensional
> domain `A ⧸ J` and `length_A ((A ⧸ J) ⧸ f₁ⁿ (A ⧸ J)) = n · length_A ((A ⧸ J) ⧸ f₁ (A ⧸ J))`.

```lean
theorem localIntersectionMultiplicity_eq_length_quotient_smul_of_isDomain {A : Type u}
    [CommRing A] [IsRegularLocalRing A] (f : Fin 1 → A) (I J : Ideal A) [IsDomain (A ⧸ J)]
    (hf : RingTheory.Sequence.IsRegular A (List.ofFn f))
    (hI : I = Ideal.span (Set.range f))
    (h0 : ringKrullDim (A ⧸ (I ⊔ J)) = 0)
    (hproper : ringKrullDim A ≤ ringKrullDim (A ⧸ I) + ringKrullDim (A ⧸ J)) :
    I.localIntersectionMultiplicity (A ⧸ J) =
      ((Module.length A ((A ⧸ J) ⧸ I • (⊤ : Submodule A (A ⧸ J)))).toNat : ℚ)
```

## Tag 0B06, a lemma

[Tag 0B06](https://stacks.math.columbia.edu/tag/0B06) in the Stacks Project.

**`Ideal.localIntersectionMultiplicity_eq_length_quotient_smul_of_isCohenMacaulayLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/ComputingIntersectionMultiplicities/CohenMacaulayMultiplicity.lean, line 760](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/ComputingIntersectionMultiplicities/CohenMacaulayMultiplicity.lean#L760). The attribute's comment: “the multiplicity formula when the local ring of the second subvariety is Cohen-Macaulay, in local form at the generic point: for `I` generated by a regular sequence of length `c` in the regular local ring `A` and `A ⧸ J` Cohen-Macaulay, the Tor-formula multiplicity of the pair is `length_A ((A ⧸ J) ⧸ I (A ⧸ J))`. The source's hypotheses are those of Tag 0B04, transported to `A = 𝒪_{X, ξ}` exactly as there, with proper intersection the dimension inequality of Tag 0B1I and `ξ` being the generic point of a component of `V ∩ W` the vanishing of `dim (A ⧸ (I ⊔ J))`.”.

> **Stacks 0B06.** In the situation of Tag 0B04 — `A` a regular local ring, `I` generated by a
> regular sequence `f₁, …, f_c`, `J` an ideal with `dim (A ⧸ (I ⊔ J)) = 0` and
> `dim A ≤ dim (A ⧸ I) + dim (A ⧸ J)` — assume moreover that `A ⧸ J` is Cohen-Macaulay. Then the
> Tor-formula intersection multiplicity of the pair is the single length
> `length_A ((A ⧸ J) ⧸ (f₁, …, f_c)(A ⧸ J))`, with no Hilbert polynomial left over.
>
> Geometrically, for `A = 𝒪_{X, ξ}` at the generic point `ξ` of an irreducible component `Z` of
> `V ∩ W` and `I`, `J` the local ideals of two closed subvarieties intersecting properly with `V`
> cut out at `ξ` by the regular sequence, this says
> `e(X, V · W, Z) = length_{𝒪_{X, ξ}}(𝒪_{W, ξ} / f₁𝒪_{W, ξ} + … + f_c𝒪_{W, ξ})` as soon as
> `𝒪_{W, ξ}` is Cohen-Macaulay.

```lean
public theorem localIntersectionMultiplicity_eq_length_quotient_smul_of_isCohenMacaulayLocalRing
    {A : Type u} [CommRing A] [IsRegularLocalRing A] {c : ℕ} (f : Fin c → A) (I J : Ideal A)
    [IsLocalRing (A ⧸ J)] (hJ : IsCohenMacaulayLocalRing (A ⧸ J))
    (hf : RingTheory.Sequence.IsRegular A (List.ofFn f))
    (hI : I = Ideal.span (Set.range f))
    (h0 : ringKrullDim (A ⧸ (I ⊔ J)) = 0)
    (hproper : ringKrullDim A ≤ ringKrullDim (A ⧸ I) + ringKrullDim (A ⧸ J)) :
    I.localIntersectionMultiplicity (A ⧸ J) =
      ((Module.length A ((A ⧸ J) ⧸ I • (⊤ : Submodule A (A ⧸ J)))).toNat : ℚ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 43.16, Tag 0B01](https://stacks.math.columbia.edu/tag/0B01)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
