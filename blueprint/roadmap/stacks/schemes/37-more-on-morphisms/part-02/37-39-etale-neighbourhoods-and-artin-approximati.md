---
declaration: section
origin: cited
lean: StacksDraft.ArtinApproximation.exists_elementaryEtaleNeighborhood_approximation, StacksDraft.ArtinApproximation.exists_common_elementaryEtaleNeighborhood_of_adicCompletion_ringEquiv, AlgebraicGeometry.exists_elementaryEtaleNeighborhood_absoluteApproximation_full_section, StacksDraft.ArtinApproximation.exists_elementaryEtaleNeighborhood_absoluteApproximation, StacksDraft.ArtinApproximation.exists_common_elementaryEtaleNeighborhood_absoluteApproximation, StacksDraft.ArtinApproximation.exists_elementaryEtaleNeighborhood_baseApproximation, StacksDraft.ArtinApproximation.exists_elementaryEtaleNeighborhood_relativeApproximation, StacksDraft.ArtinApproximation.exists_relativeMapApproximation
statement: formalized
proof: formalized
---

# 37.39 Étale neighbourhoods and Artin approximation

Section 37.39 of the Stacks Project, [Tag 0CAT](https://stacks.math.columbia.edu/tag/0CAT). 9 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CAU, a lemma

[Tag 0CAU](https://stacks.math.columbia.edu/tag/0CAU) in the Stacks Project.

**`StacksDraft.ArtinApproximation.exists_elementaryEtaleNeighborhood_approximation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/ArtinApproximationScheme.lean, line 509](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/ArtinApproximationScheme.lean#L509). The attribute's comment: “the full scheme-level statement, with the congruence in the completed local ring of the neighbourhood. The hypotheses are exactly the source's own: `S` locally Noetherian, `f` and `g` locally of finite type, `x` and `y` over the same point, `𝒪_{S, s}` a G-ring, and the local `𝒪_{S, s}`-algebra map `φ : 𝒪_{Y, y} → 𝒪^∧_{X, x}`. The affine case enters through the unconditional Stacks 0CAR `StacksDraft.ArtinApproximation.artinApproximationGRing`. The source's own proof of 37.39.1 is the reduction to the affine case, and that reduction is what is PROVED here on top of the affine case `StacksDraft.ArtinApproximation.exists_etaleApproximation`: the affine charts, the chart descriptions of the three local rings, the elementariness of the neighbourhood from the ring-level residue field equality, and the transport of the congruence. The source states the conclusion for a diagram; here it is the single congruence that the diagram expresses.”.

> **Stacks Project, Tag 0CAU (More on Morphisms, Lemma 37.39.1).** Let `S` be a locally
> Noetherian scheme, let `f : X ⟶ S` and `g : Y ⟶ S` be locally of finite type, and let `x ∈ X`
> and `y ∈ Y` lie over the same point `s = f x = g y` of `S`. Assume `𝒪_{S, s}` is a G-ring, and
> let `φ : 𝒪_{Y, y} → 𝒪^∧_{X, x}` be a local homomorphism of `𝒪_{S, s}`-algebras. Then for every
> `N ≥ 1` there are an elementary étale neighbourhood `(U, u)` of `(X, x)` and a morphism
> `F : U ⟶ Y` over `S` with `F u = y` such that the square formed by `φ`, the map
> `𝒪^∧_{X, x} → 𝒪^∧_{U, u}`, the map `F^♯_u : 𝒪_{Y, y} → 𝒪_{U, u}` and `𝒪_{U, u} → 𝒪^∧_{U, u}`
> commutes modulo `𝔪_u^N`.
>
> The proof reduces to the affine case
> `StacksDraft.ArtinApproximation.exists_etaleApproximation`, which rests on Stacks 0CAR
> `StacksDraft.ArtinApproximation.artinApproximationGRing`: it chooses affine charts, transports
> `φ` to the charts, and reads `Spec A'` as an elementary étale neighbourhood of `(X, x)` with a
> morphism to `Y` over `S`.

```lean
theorem exists_elementaryEtaleNeighborhood_approximation
    {S X Y : Scheme.{u}} (f : X ⟶ S) (g : Y ⟶ S)
    [IsLocallyNoetherian S] [LocallyOfFiniteType f] [LocallyOfFiniteType g]
    (x : X) (y : Y) (hxy : f x = g y)
    (hG : IsGRing (S.presheaf.stalk (f x)))
    (N : ℕ) (hN : 1 ≤ N)
    (φ : Y.presheaf.stalk y →+*
      AdicCompletion (maximalIdeal (X.presheaf.stalk x)) (X.presheaf.stalk x))
    (hφ : IsLocalHom φ)
    (hbase : φ.comp ((S.presheaf.stalkCongr (.of_eq hxy)).hom ≫ g.stalkMap y).hom =
      (algebraMap (X.presheaf.stalk x)
        (AdicCompletion (maximalIdeal (X.presheaf.stalk x)) (X.presheaf.stalk x))).comp
        (f.stalkMap x).hom) :
    ∃ U : EtaleNeighborhood X x, U.IsElementary ∧
      ∃ (F : U.scheme ⟶ Y) (hF : F U.point = y), F ≫ g = U.toBase ≫ f ∧
        ∀ a : Y.presheaf.stalk y,
          adicCompletionMap
              (((X.presheaf.stalkCongr (.of_eq U.map_point.symm)).hom ≫
                U.toBase.stalkMap U.point).hom)
              (maximalIdeal (X.presheaf.stalk x))
              (maximalIdeal (U.scheme.presheaf.stalk U.point))
              (map_maximalIdeal_le_etaleNeighborhood U) (φ a) -
            algebraMap (U.scheme.presheaf.stalk U.point)
              (AdicCompletion (maximalIdeal (U.scheme.presheaf.stalk U.point))
                (U.scheme.presheaf.stalk U.point))
              (((Y.presheaf.stalkCongr (.of_eq hF.symm)).hom ≫ F.stalkMap U.point).hom a) ∈
            Ideal.map
              (algebraMap (U.scheme.presheaf.stalk U.point)
                (AdicCompletion (maximalIdeal (U.scheme.presheaf.stalk U.point))
                  (U.scheme.presheaf.stalk U.point)))
              (maximalIdeal (U.scheme.presheaf.stalk U.point) ^ N)
```

## Tag 0CAV, a lemma

[Tag 0CAV](https://stacks.math.columbia.edu/tag/0CAV) in the Stacks Project.

**`StacksDraft.ArtinApproximation.exists_common_elementaryEtaleNeighborhood_of_adicCompletion_ringEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/IsomorphismApproximation.lean, line 391](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/IsomorphismApproximation.lean#L391). The attribute's comment: “with NO carried hypotheses, exactly as Tag 0CAU it rests on: the only hypotheses are the source's own. Everything in the source's own proof of 37.39.2 is proved here. The congruence is stated on the whole completed local ring of the neighbourhood rather than only on the image of the local ring, which is what the source's diagram of complete local rings asserts”.

> **Stacks Project, Tag 0CAV (More on Morphisms, Lemma 37.39.2).** Let `S` be a locally
> Noetherian scheme, let `f : X ⟶ S` and `g : Y ⟶ S` be locally of finite type, and let `x ∈ X`
> and `y ∈ Y` lie over a common point `s` of `S` whose local ring is a G-ring. Suppose given an
> isomorphism `Φ : 𝒪^∧_{Y, y} ≅ 𝒪^∧_{X, x}` which is compatible with the two maps from
> `𝒪_{S, s}`. Then for every `N ≥ 1` there is a single pointed scheme `(U, u)` sitting in a
> diagram `(X, x) ← (U, u) → (Y, y)` over `S` in which *both* legs are elementary étale
> neighbourhoods, and over which the triangle of completed local rings commutes modulo
> `𝔪_u ^ N`: for every `z ∈ 𝒪^∧_{Y, y}`, the two images of `z` in `𝒪^∧_{U, u}` — one obtained by
> transporting `z` through `Φ` and then along the first leg, the other by going directly along the
> second leg — differ by an element of `𝔪_u ^ N · 𝒪^∧_{U, u}`.
>
> Tag 0CAU already produces the neighbourhood `(U₀, u₀)` of `(X, x)` and a morphism `F : U₀ ⟶ Y`
> over `S` whose congruence holds on the image of `𝒪_{Y, y}`. The content added here is that `F`
> is étale at `u₀`, which is extracted from the congruence itself: it forces the induced map
> `𝒪^∧_{Y, y} → 𝒪^∧_{U₀, u₀}` to be bijective, and a bijection of completions upgrades to
> étaleness of local rings by Tag 039M. Shrinking `U₀` to an open on which `F` is étale gives the
> required `(U, u)`.
>
> The difference of the two completion maps is written with an explicit `HSub` instance because
> the two completions are only definitionally, not reducibly, the same ring: the second is indexed
> by the scheme of `EtaleNeighborhood.along`, whose `scheme` field is the first one by `rfl`. The
> term is the ordinary `_ - _`.

```lean
theorem exists_common_elementaryEtaleNeighborhood_of_adicCompletion_ringEquiv
    {S X Y : Scheme.{u}} (f : X ⟶ S) (g : Y ⟶ S)
    [IsLocallyNoetherian S] [LocallyOfFiniteType f] [LocallyOfFiniteType g]
    (x : X) (y : Y) (hxy : f x = g y)
    (hG : IsGRing (S.presheaf.stalk (f x)))
    (N : ℕ) (hN : 1 ≤ N)
    (Φ : AdicCompletion (maximalIdeal (Y.presheaf.stalk y)) (Y.presheaf.stalk y) ≃+*
      AdicCompletion (maximalIdeal (X.presheaf.stalk x)) (X.presheaf.stalk x))
    (hΦ : Φ.toRingHom.comp ((algebraMap (Y.presheaf.stalk y)
        (AdicCompletion (maximalIdeal (Y.presheaf.stalk y)) (Y.presheaf.stalk y))).comp
          ((S.presheaf.stalkCongr (.of_eq hxy)).hom ≫ g.stalkMap y).hom) =
      (algebraMap (X.presheaf.stalk x)
        (AdicCompletion (maximalIdeal (X.presheaf.stalk x)) (X.presheaf.stalk x))).comp
          (f.stalkMap x).hom) :
    ∃ (U : EtaleNeighborhood X x) (q : U.scheme ⟶ Y) (hqEt : Etale q) (hq : q U.point = y),
      U.IsElementary ∧ (U.along q hqEt hq).IsElementary ∧ q ≫ g = U.toBase ≫ f ∧
        ∀ z : AdicCompletion (maximalIdeal (Y.presheaf.stalk y)) (Y.presheaf.stalk y),
          @HSub.hSub _ _ _ instHSub (U.completionMap (Φ z))
              ((U.along q hqEt hq).completionMap z) ∈
            Ideal.map (algebraMap (U.scheme.presheaf.stalk U.point)
              (AdicCompletion (maximalIdeal (U.scheme.presheaf.stalk U.point))
                (U.scheme.presheaf.stalk U.point)))
              (maximalIdeal (U.scheme.presheaf.stalk U.point) ^ N)
```

## Tag 0GDX, a lemma

[Tag 0GDX](https://stacks.math.columbia.edu/tag/0GDX) in the Stacks Project.

**`AlgebraicGeometry.exists_elementaryEtaleNeighborhood_absoluteApproximation_full_section`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/AbsoluteApproximationFull.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/AbsoluteApproximationFull.lean#L92). The attribute's comment: “clauses (1), (2), (3) and (4) of the conclusion, together with the commutativity of the source's diagram: (1) the elementary étale neighbourhood `(V, v)` of `(S, s)`; (2) the morphism `F : W ⟶ X` with `F(w) = x`, étale and trivial on residue fields at `w`, i.e. an elementary étale neighbourhood `(W, w) → (X, x)`; (3) `τ(v) = t`; and (4) the elementary étale neighbourhood `(W, w) → (Y ×_{T, τ} V, y_τ)`. HOW `y_τ` IS SPECIFIED -- the one part of the source's sentence that is NOT proved: the source takes for `y_τ` the point corresponding to `y_σ` under the identification `(Y_σ)_s = (Y ×_T V)_v`. Here `y_τ` is specified by lying over `y` and over `v`, together with the equality of the two morphisms `Spec κ(s) ⟶ T` -- one through `Spec 𝒪^∧_{S, s}` and `σ`, one through `V` and `τ` -- which IS that identification of the two fibres as one and the same scheme. That `y_τ` and `y_σ` are the same point OF that common fibre is not established. NO hypothesis beyond the source's is carried: Theorem 07QZ in particular is not, being proved as `StacksDraft.ArtinApproximation.localApproximationProperty`, so Tags 0CAU, 0CAV, 07GC, 07PS, 01ZC, 01ZM, 07RP and 057G that this rests on are unconditional. Two of the source's hypotheses are WEAKENED, so what is proved is stronger there: `T` of finite type over `Spec ℤ` is only required to be LOCALLY of finite type, and `φ` is only required to be a map of `𝒪_{S, s}`-algebras rather than of `𝒪^∧_{S, s}`-algebras”.

> **Stacks Tag 0GDX, clauses (1)–(4), with the two morphisms `Spec κ(s) ⟶ T` identified.**
> Let `fX : X ⟶ S` be locally of finite type with `S`
> locally Noetherian, let `gY : Y ⟶ T` be locally of finite type with `T` of finite type over `ℤ`,
> let `x ∈ X` lie over `s ∈ S` with `𝒪_{S, s}` a G-ring, and let
> `σ : 𝒪_{T, t} → 𝒪^∧_{S, s}` be a local homomorphism. Let `yσ` be a point of
> `Y ×_T Spec 𝒪^∧_{S, s}` lying over `y ∈ Y` and over the closed point, and let
> `φ : 𝒪^∧_{X, x} ≅ 𝒪^∧_{Y ×_T Spec 𝒪^∧_{S, s}, yσ}` be an isomorphism of `𝒪_{S, s}`-algebras.
> Then there are an elementary étale neighbourhood `V` of `(S, s)`, a morphism `τ : V ⟶ T` carrying
> the marked point to `t`, a point `yτ` of `Y ×_{T, τ} V` over `y` and over the marked point of
> `V`, and an elementary étale neighbourhood `W` of `(Y ×_{T, τ} V, yτ)` together with a morphism
> `F : W ⟶ X` carrying the marked point to `x` which is étale, trivial on residue fields, and
> compatible with the structure morphisms to `S`; moreover the canonical section
> `Spec κ(s) ⟶ Spec 𝒪^∧_{S, s}` followed by `Spec 𝒪^∧_{S, s} ⟶ T` agrees with the canonical
> section `Spec κ(s) ⟶ V` followed by `τ`.

```lean
public theorem exists_elementaryEtaleNeighborhood_absoluteApproximation_full_section
    {S T X Y : Scheme.{u}} [IsLocallyNoetherian S]
    (fX : X ⟶ S) (gY : Y ⟶ T) [LocallyOfFiniteType fX] [LocallyOfFiniteType gY]
    (hT : LocallyOfFiniteType (specULiftZIsTerminal.{u}.from T))
    (x : X) (s : S) (hfx : fX x = s) (t : T) (y : Y)
    (hG : IsGRing (S.presheaf.stalk s))
    (σ : T.presheaf.stalk t →+* AdicCompletion (maximalIdeal (S.presheaf.stalk s))
      (S.presheaf.stalk s))
    (hσ : IsLocalHom σ)
    (yσ : ↥(pullback gY (Spec.map (CommRingCat.ofHom σ) ≫ T.fromSpecStalk t)))
    (hyσ₁ : pullback.fst gY (Spec.map (CommRingCat.ofHom σ) ≫ T.fromSpecStalk t) yσ = y)
    (hyσ₂ : pullback.snd gY (Spec.map (CommRingCat.ofHom σ) ≫ T.fromSpecStalk t) yσ =
      closedPoint _)
    (φ : AdicCompletion (maximalIdeal (X.presheaf.stalk x)) (X.presheaf.stalk x) ≃+*
      AdicCompletion (maximalIdeal ((pullback gY (Spec.map (CommRingCat.ofHom σ) ≫
          T.fromSpecStalk t)).presheaf.stalk yσ))
        ((pullback gY (Spec.map (CommRingCat.ofHom σ) ≫ T.fromSpecStalk t)).presheaf.stalk yσ))
    (hbase : (pullback.snd gY (Spec.map (CommRingCat.ofHom σ) ≫ T.fromSpecStalk t) ≫
      Spec.map (CommRingCat.ofHom (algebraMap (S.presheaf.stalk s)
        (AdicCompletion (maximalIdeal (S.presheaf.stalk s)) (S.presheaf.stalk s)))) ≫
      S.fromSpecStalk s) yσ = s)
    (hφ : φ.toRingHom.comp ((algebraMap (X.presheaf.stalk x)
        (AdicCompletion (maximalIdeal (X.presheaf.stalk x)) (X.presheaf.stalk x))).comp
          (fX.stalkHomAt hfx)) =
      (algebraMap ((pullback gY (Spec.map (CommRingCat.ofHom σ) ≫
            T.fromSpecStalk t)).presheaf.stalk yσ)
          (AdicCompletion (maximalIdeal ((pullback gY (Spec.map (CommRingCat.ofHom σ) ≫
              T.fromSpecStalk t)).presheaf.stalk yσ))
            ((pullback gY (Spec.map (CommRingCat.ofHom σ) ≫
              T.fromSpecStalk t)).presheaf.stalk yσ))).comp
        ((pullback.snd gY (Spec.map (CommRingCat.ofHom σ) ≫ T.fromSpecStalk t) ≫
          Spec.map (CommRingCat.ofHom (algebraMap (S.presheaf.stalk s)
            (AdicCompletion (maximalIdeal (S.presheaf.stalk s)) (S.presheaf.stalk s)))) ≫
          S.fromSpecStalk s).stalkHomAt hbase)) :
    ∃ V : EtaleNeighborhood S s, ∃ hVel : V.IsElementary,
      ∃ (τ : V.scheme ⟶ T) (_ : τ V.point = t),
        specResidueFieldSection (Spec.map (CommRingCat.ofHom (algebraMap (S.presheaf.stalk s)
              (AdicCompletion (maximalIdeal (S.presheaf.stalk s)) (S.presheaf.stalk s)))) ≫
            S.fromSpecStalk s) (specCompletedStalkToBase_closedPoint s)
            (isIso_residueFieldMap_specCompletedStalkToBase s) ≫
            (Spec.map (CommRingCat.ofHom σ) ≫ T.fromSpecStalk t) =
          specResidueFieldSection V.toBase V.map_point
            ((EtaleNeighborhood.isElementary_iff V).mp hVel) ≫ τ ∧
        ∃ yτ : ↥(pullback gY τ),
          pullback.fst gY τ yτ = y ∧ pullback.snd gY τ yτ = V.point ∧
          ∃ W : EtaleNeighborhood (pullback gY τ) yτ, W.IsElementary ∧
            ∃ (F : W.scheme ⟶ X) (_ : F W.point = x),
              Etale F ∧ IsIso (F.residueFieldMap W.point) ∧
                F ≫ fX = W.toBase ≫ pullback.snd gY τ ≫ V.toBase
```

**`StacksDraft.ArtinApproximation.exists_elementaryEtaleNeighborhood_absoluteApproximation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/FiniteTypeBaseApproximation.lean, line 280](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/FiniteTypeBaseApproximation.lean#L280). The attribute's comment: “clauses (1) and (3) of the conclusion: the elementary étale neighbourhood `(V, v)` of `(S, s)` and the morphism `τ : V ⟶ T` with `τ(v) = t`. What is proved is STRONGER than those two clauses: it carries in addition the congruence that Tag 0CAW records as its clause (3), namely that the square relating `σ` to `τ^♯_v` commutes modulo `𝔪_v ^ N`, which is why this registration is kept; and the source's `T` of finite type over `Spec ℤ` is weakened to LOCALLY of finite type. None of `X`, `Y`, `φ`, `y_σ` enters this statement, so it says nothing about clauses (2) and (4) — the elementary étale neighbourhood `(W, w)` of `(X, x)` which is simultaneously one of `(Y ×_{T, τ} V, y_τ)`. THOSE ARE PROVED ELSEWHERE, twice over and independently, and both of those statements carry a registration for the whole conclusion: all four clauses are `AlgebraicGeometry.exists_elementaryEtaleNeighborhood_absoluteApproximation_full_section` in `StacksFrontier.AlgebraicGeometry.Morphisms.EtaleNeighbourhood.AbsoluteApproximationFull`, and also `StacksDraft.ArtinApproximation.exists_common_elementaryEtaleNeighborhood_absoluteApproximation` in `StacksFrontier.AlgebraicGeometry.Morphisms.EtaleNeighbourhood.RelativeMapApproximation`. NO hypothesis beyond the source's is carried: the library's Tag 0CAU behind this deduction is unconditional, Theorem 07QZ being proved as `StacksDraft.ArtinApproximation.localApproximationProperty`”.

> **Stacks Project, Tag 0GDX, clauses (1) and (3).** Let `S` be a locally Noetherian scheme,
> let `T` be locally of finite type over `Spec ℤ`, let `t ∈ T` and `s ∈ S`, assume `𝒪_{S, s}` is a
> G-ring, and let `σ : 𝒪_{T, t} → 𝒪^∧_{S, s}` be a local homomorphism. Then for every `N ≥ 1`
> there are an elementary étale neighbourhood `(V, v)` of `(S, s)` and a morphism `τ : V ⟶ T` with
> `τ v = t`; moreover the square relating `σ` to `τ^♯_v` commutes modulo `𝔪_v ^ N`, which is the
> extra conclusion that Tag 0CAW records as its clause (3).

```lean
theorem exists_elementaryEtaleNeighborhood_absoluteApproximation
    {S T : Scheme.{u}} [IsLocallyNoetherian S]
    (hT : LocallyOfFiniteType (specULiftZIsTerminal.{u}.from T))
    (t : T) (s : S) (hG : IsGRing (S.presheaf.stalk s))
    (N : ℕ) (hN : 1 ≤ N)
    (σ : T.presheaf.stalk t →+*
      AdicCompletion (maximalIdeal (S.presheaf.stalk s)) (S.presheaf.stalk s))
    (hσ : IsLocalHom σ) :
    ∃ V : EtaleNeighborhood S s, V.IsElementary ∧
      ∃ (τ : V.scheme ⟶ T) (hτ : τ V.point = t),
        ∀ a : T.presheaf.stalk t,
          V.completionMap (σ a) -
              algebraMap (V.scheme.presheaf.stalk V.point)
                (AdicCompletion (maximalIdeal (V.scheme.presheaf.stalk V.point))
                  (V.scheme.presheaf.stalk V.point)) (τ.stalkHomAt hτ a) ∈
            Ideal.map
              (algebraMap (V.scheme.presheaf.stalk V.point)
                (AdicCompletion (maximalIdeal (V.scheme.presheaf.stalk V.point))
                  (V.scheme.presheaf.stalk V.point)))
              (maximalIdeal (V.scheme.presheaf.stalk V.point) ^ N)
```

**`StacksDraft.ArtinApproximation.exists_common_elementaryEtaleNeighborhood_absoluteApproximation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/RelativeMapApproximation.lean, line 4440](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/RelativeMapApproximation.lean#L4440). The attribute's comment: “What is proved is STRONGER than the source in two respects, both inherited from the first stage of Tag 0CAW which replaces the étale slice of Tag 057G here: the pair `(V, τ)` satisfies in addition the congruence that Tag 0CAW records as its clause (3), namely that the square relating `σ` to `τ^♯_v` commutes modulo `𝔪_v ^ N` for the given `N ≥ 1`; and the source's `T` of finite type over `Spec ℤ` is weakened to LOCALLY of finite type”.

> **Stacks Project, Tag 0GDX.** Let `S` be a locally Noetherian scheme, let `s ∈ S` have a
> G-ring local ring, let `T` be locally of finite type over `Spec ℤ`, let `p : X ⟶ S` and
> `q : Y ⟶ T` be locally of finite type, let `x ∈ X` lie over `s` and `y ∈ Y` over `t ∈ T`, and
> let `σ : 𝒪_{T, t} → 𝒪^∧_{S, s}` be a local homomorphism. Write
> `Y_σ = Y ×_{T, σ} Spec 𝒪^∧_{S, s}` and let `y_σ ∈ Y_σ` lie over `y` and over the closed point.
> An isomorphism `φ : 𝒪^∧_{X, x} ≅ 𝒪^∧_{Y_σ, y_σ}` of `𝒪_{S, s}`-algebras is then induced, after
> elementary étale changes, by a morphism of schemes: there are an elementary étale neighbourhood
> `(V, v)` of `(S, s)`, a morphism `τ : V ⟶ T` with `τ v = t`, and an elementary étale
> neighbourhood `(W, w)` of `(X, x)` which is simultaneously an elementary étale neighbourhood of
> `(Y ×_{T, τ} V, y_τ)`, where `y_τ` corresponds to `y_σ` under the identification of the closed
> fibres `(Y_σ)_s = (Y ×_T V)_v`.
>
> The identification of the closed fibres is given explicitly: an isomorphism `e` of the residue
> fields of the two bases compatible with their maps to `S` and to `T`, and an isomorphism of the
> scheme-theoretic fibres compatible with the two maps to `Y` and with `e`, carrying the point
> above `y_σ` to the point above `y_τ`.

```lean
theorem exists_common_elementaryEtaleNeighborhood_absoluteApproximation
    {X S Y T : Scheme.{u}} [IsLocallyNoetherian S] (p : X ⟶ S) (q : Y ⟶ T)
    [LocallyOfFiniteType p] [LocallyOfFiniteType q]
    (hT : LocallyOfFiniteType (specULiftZIsTerminal.{u}.from T))
    {x : X} {s : S} {y : Y} {t : T} (hx : p x = s) (hy : q y = t)
    (hG : IsGRing (S.presheaf.stalk s)) (N : ℕ) (hN : 1 ≤ N)
    (σ : T.presheaf.stalk t →+*
      AdicCompletion (maximalIdeal (S.presheaf.stalk s)) (S.presheaf.stalk s))
    (hσ : IsLocalHom σ)
    (yσ : (pullback q (relativeBaseChangeMorphism s σ) : Scheme.{u}))
    (hyσY : pullback.fst q (relativeBaseChangeMorphism s σ) yσ = y)
    (hyσZ : pullback.snd q (relativeBaseChangeMorphism s σ) yσ =
      specCompletedStalkPoint S s)
    (φ : AdicCompletion (maximalIdeal (X.presheaf.stalk x)) (X.presheaf.stalk x) ≃+*
      AdicCompletion
        (maximalIdeal
          ((pullback q (relativeBaseChangeMorphism s σ)).presheaf.stalk yσ))
        ((pullback q (relativeBaseChangeMorphism s σ)).presheaf.stalk yσ))
    (hφ : φ.toRingHom.comp ((algebraMap (X.presheaf.stalk x)
          (AdicCompletion (maximalIdeal (X.presheaf.stalk x)) (X.presheaf.stalk x))).comp
        (p.stalkHomAt hx)) =
      (algebraMap ((pullback q (relativeBaseChangeMorphism s σ)).presheaf.stalk yσ)
          (AdicCompletion
            (maximalIdeal
              ((pullback q (relativeBaseChangeMorphism s σ)).presheaf.stalk yσ))
            ((pullback q (relativeBaseChangeMorphism s σ)).presheaf.stalk yσ))).comp
        (((pullback.snd q (relativeBaseChangeMorphism s σ)).stalkHomAt hyσZ).comp
          ((specCompletedStalkTo S s).stalkHomAt
            (specCompletedStalkTo_specCompletedStalkPoint S s)))) :
    ∃ (V : EtaleNeighborhood S s) (τ : V.scheme ⟶ T) (hτ : τ V.point = t)
      (yτ : (pullback q τ : Scheme.{u}))
      (_ : pullback.fst q τ yτ = y) (hyτV : pullback.snd q τ yτ = V.point)
      (W : EtaleNeighborhood X x) (g : W.scheme ⟶ pullback q τ)
      (hgPoint : g W.point = yτ) (_ : Etale g),
      V.IsElementary ∧ W.IsElementary ∧
        IsIso (((pullback q τ).residueFieldCongr hgPoint).inv ≫
          g.residueFieldMap W.point) ∧
        g ≫ pullback.snd q τ ≫ V.toBase = W.toBase ≫ p ∧
        (∀ b : T.presheaf.stalk t,
          V.completionMap (σ b) -
              algebraMap (V.scheme.presheaf.stalk V.point)
                (AdicCompletion (maximalIdeal (V.scheme.presheaf.stalk V.point))
                  (V.scheme.presheaf.stalk V.point)) (τ.stalkHomAt hτ b) ∈
            Ideal.map
              (algebraMap (V.scheme.presheaf.stalk V.point)
                (AdicCompletion (maximalIdeal (V.scheme.presheaf.stalk V.point))
                  (V.scheme.presheaf.stalk V.point)))
              (maximalIdeal (V.scheme.presheaf.stalk V.point) ^ N)) ∧
        ∃ (eBase : (specCompletedStalk S s).residueField (specCompletedStalkPoint S s) ≅
            V.scheme.residueField V.point)
          (eFiber : (pullback.snd q (relativeBaseChangeMorphism s σ)).fiber
              (specCompletedStalkPoint S s) ≅
            (pullback.snd q τ).fiber V.point),
          (Spec.map eBase.inv ≫ V.scheme.fromSpecResidueField V.point ≫ V.toBase =
            (specCompletedStalk S s).fromSpecResidueField (specCompletedStalkPoint S s) ≫
              specCompletedStalkTo S s) ∧
          (Spec.map eBase.inv ≫ V.scheme.fromSpecResidueField V.point ≫ τ =
            (specCompletedStalk S s).fromSpecResidueField (specCompletedStalkPoint S s) ≫
              relativeBaseChangeMorphism s σ) ∧
          (eFiber.hom ≫ (pullback.snd q τ).fiberι V.point ≫ pullback.fst q τ =
            (pullback.snd q (relativeBaseChangeMorphism s σ)).fiberι
                (specCompletedStalkPoint S s) ≫
              pullback.fst q (relativeBaseChangeMorphism s σ)) ∧
          (eFiber.hom ≫ (pullback.snd q τ).fiberToSpecResidueField V.point =
            (pullback.snd q (relativeBaseChangeMorphism s σ)).fiberToSpecResidueField
                (specCompletedStalkPoint S s) ≫ Spec.map eBase.inv) ∧
          (eFiber.hom (((pullback.snd q (relativeBaseChangeMorphism s σ)).fiberHomeo
              (specCompletedStalkPoint S s)).symm ⟨yσ, hyσZ⟩) =
            ((pullback.snd q τ).fiberHomeo V.point).symm ⟨yτ, hyτV⟩)
```

## Tag 0CAW, a lemma

[Tag 0CAW](https://stacks.math.columbia.edu/tag/0CAW) in the Stacks Project.

**`StacksDraft.ArtinApproximation.exists_elementaryEtaleNeighborhood_baseApproximation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/BaseChangeApproximation.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/BaseChangeApproximation.lean#L131). The attribute's comment: “the FIRST STAGE of the conclusion: clause (1) for `v` and `τ` (`v ↦ s` and `τ(v) = t`), clause (2) (`(V, v) → (S, s)` is an elementary étale neighbourhood) and clause (3) (the square relating `σ` to `τ^♯_v` commutes modulo `𝔪_v ^ N`), with `τ` a morphism over `S`. This is the source's own last step, Tag 0CAU applied to `(S, s) ← (S, s)`, `(T, t) → (S, s)` and `σ`. Clauses (4) and (5) are NOT established by this declaration; see `StacksDraft.ArtinApproximation.exists_elementaryEtaleNeighborhood_relativeApproximation`. There is NO hypothesis beyond the source's: the Tag 0CAU used here is unconditional, Theorem 07QZ being proved as `StacksDraft.ArtinApproximation.localApproximationProperty`”.

> **Stacks Project, Tag 0CAW, first stage: clauses (1) for `(v, τ)`, (2) and (3).** Let `S` be
> a locally Noetherian scheme, let `h : T ⟶ S` be locally of finite type, let `t ∈ T` lie over
> `s ∈ S`, assume `𝒪_{S, s}` is a G-ring, and let `σ : 𝒪_{T, t} → 𝒪^∧_{S, s}` be a local
> homomorphism of `𝒪_{S, s}`-algebras. Then for every `N ≥ 1` there are an elementary étale
> neighbourhood `(V, v)` of `(S, s)` and a morphism `τ : V ⟶ T` over `S` with `τ v = t` such that
> the square
> ```
> 𝒪^∧_{S, s} ⟶ 𝒪^∧_{V, v}
>     ↑σ             ↑
> 𝒪_{T, t}  —τ^♯—→ 𝒪_{V, v}
> ```
> commutes modulo `𝔪_v ^ N`.
>
> This is Tag 0CAU for the pointed diagram `(S, s) ← (S, s)`, `(T, t) → (S, s)` and the map `σ`:
> the source's own proof of 0CAW ends by applying 0CAU "one more time to `Spec C` and `Spec R` over
> `Spec R` and the map `C → R^∧`", and that application is this statement.

```lean
theorem exists_elementaryEtaleNeighborhood_baseApproximation
    {S T : Scheme.{u}} (h : T ⟶ S)
    [IsLocallyNoetherian S] [LocallyOfFiniteType h]
    (t : T) (s : S) (hts : h t = s)
    (hG : IsGRing (S.presheaf.stalk s))
    (N : ℕ) (hN : 1 ≤ N)
    (σ : T.presheaf.stalk t →+*
      AdicCompletion (maximalIdeal (S.presheaf.stalk s)) (S.presheaf.stalk s))
    (hσ : IsLocalHom σ)
    (hσbase : σ.comp (h.stalkHomAt hts) =
      algebraMap (S.presheaf.stalk s)
        (AdicCompletion (maximalIdeal (S.presheaf.stalk s)) (S.presheaf.stalk s))) :
    ∃ V : EtaleNeighborhood S s, V.IsElementary ∧
      ∃ (τ : V.scheme ⟶ T) (hτ : τ V.point = t), τ ≫ h = V.toBase ∧
        ∀ a : T.presheaf.stalk t,
          V.completionMap (σ a) -
              algebraMap (V.scheme.presheaf.stalk V.point)
                (AdicCompletion (maximalIdeal (V.scheme.presheaf.stalk V.point))
                  (V.scheme.presheaf.stalk V.point)) (τ.stalkHomAt hτ a) ∈
            Ideal.map
              (algebraMap (V.scheme.presheaf.stalk V.point)
                (AdicCompletion (maximalIdeal (V.scheme.presheaf.stalk V.point))
                  (V.scheme.presheaf.stalk V.point)))
              (maximalIdeal (V.scheme.presheaf.stalk V.point) ^ N)
```

**`StacksDraft.ArtinApproximation.exists_elementaryEtaleNeighborhood_relativeApproximation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/BaseChangeApproximation.lean, line 201](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/BaseChangeApproximation.lean#L201). The attribute's comment: “the SECOND STAGE of the conclusion, for a first stage supplied as hypotheses: the remaining part of clause (1) — `w ↦ (y, v)`, which is `W.map_point`, and the morphism `f : W ⟶ X ×_S V` with `f(w) = (x, v)`, delivered as the two projection identities of `f` together with `F w = x` and the hypothesis placing `y_τ` over `v` — clause (4) (`(W, w) → (Y ×_{T, τ} V, (y, v))` is an elementary étale neighbourhood), and clause (5) in the form of the congruence modulo `𝔪_w ^ N` in `𝒪^∧_{W, w}` that the source's square expresses once the identification `𝒪_{Y_σ, y_σ}/𝔪^N = 𝒪_{Y ×_{T, τ} V, (y, v)}/𝔪^N` is removed from both sides. HYPOTHESES BEYOND THE SOURCE'S, all stated explicitly — Theorem 07QZ is NOT among them, the Tag 0CAU used here being unconditional: (a) the first stage itself, i.e. the elementary étale neighbourhood `(V, v)` of `(S, s)` with the morphism `τ : V ⟶ T`, which `StacksDraft.ArtinApproximation.exists_elementaryEtaleNeighborhood_baseApproximation` produces from the source's hypotheses; (b) the point `y_τ` of `Y ×_{T, τ} V` over `v`; (c) the local `𝒪_{S, s}`-algebra map `φ : 𝒪_{X, x} → 𝒪^∧_{Y ×_{T, τ} V, y_τ}` in place of the source's `φ : 𝒪_{X, x} → 𝒪^∧_{Y_σ, y_σ}`, the bridge between the two being the canonical isomorphism of `Y_σ` with `Y ×_{T, τ} V` over `𝒪_{V, v}/𝔪_v ^ N = 𝒪_{S, s}/𝔪_s ^ N` which clauses (2) and (3) make available. That identification IS constructed, as `StacksDraft.ArtinApproximation.exists_truncationEquiv_stalk_relativeBaseChange`, but only as an isomorphism of the local rings TRUNCATED at `𝔪 ^ N`, which is the shape clause (5) uses it in; it does not produce a map into the COMPLETED local ring `𝒪^∧_{Y ×_{T, τ} V, (y, v)}` out of the source's `φ`, and no isomorphism of the completions exists, so hypothesis (c) is not discharged by it”.

> **Stacks Project, Tag 0CAW, second stage: the rest of clause (1), clause (4), and clause (5)
> in the form of a congruence in `𝒪^∧_{W, w}`.** Given the first stage — an elementary étale
> neighbourhood `(V, v)` of `(S, s)` and a morphism `τ : V ⟶ T` — a point `y_τ` of
> `Y ×_{T, τ} V` lying over `v`, and a local `𝒪_{S, s}`-algebra map
> `φ : 𝒪_{X, x} → 𝒪^∧_{Y ×_{T, τ} V, y_τ}`, there are for every `N ≥ 1` an elementary étale
> neighbourhood `(W, w)` of `(Y ×_{T, τ} V, y_τ)` and a morphism `F : W ⟶ X` over `S` with
> `F w = x`, hence a morphism `W ⟶ X ×_S V` carrying `w` to `(x, v)`, such that `φ` followed by
> the map `𝒪^∧_{Y ×_{T, τ} V, y_τ} → 𝒪^∧_{W, w}` agrees modulo `𝔪_w ^ N` with the map
> `𝒪_{X, x} → 𝒪_{W, w}` induced by `F`.
>
> This is Tag 0CAU for the pointed diagram `(Y ×_{T, τ} V, y_τ) → (S, s)`, `(X, x) → (S, s)`, the
> first leg being read over `S` through `V ⟶ S`.

```lean
theorem exists_elementaryEtaleNeighborhood_relativeApproximation
    {S T X Y : Scheme.{u}} (f : X ⟶ S) (g : Y ⟶ T)
    [IsLocallyNoetherian S] [LocallyOfFiniteType f] [LocallyOfFiniteType g]
    (x : X) (hG : IsGRing (S.presheaf.stalk (f x)))
    (V : EtaleNeighborhood S (f x)) (τ : V.scheme ⟶ T)
    (yτ : ↥(pullback g τ)) (hyτ : pullback.snd g τ yτ = V.point)
    (N : ℕ) (hN : 1 ≤ N)
    (φ : X.presheaf.stalk x →+*
      AdicCompletion (maximalIdeal ((pullback g τ).presheaf.stalk yτ))
        ((pullback g τ).presheaf.stalk yτ))
    (hφ : IsLocalHom φ)
    (hφbase : φ.comp (f.stalkMap x).hom =
      (algebraMap ((pullback g τ).presheaf.stalk yτ)
          (AdicCompletion (maximalIdeal ((pullback g τ).presheaf.stalk yτ))
            ((pullback g τ).presheaf.stalk yτ))).comp
        (((pullback.snd g τ).stalkHomAt hyτ).comp V.stalkHom)) :
    ∃ W : EtaleNeighborhood (pullback g τ) yτ, W.IsElementary ∧
      ∃ (F : W.scheme ⟶ X) (hF : F W.point = x),
        F ≫ f = W.toBase ≫ pullback.snd g τ ≫ V.toBase ∧
        (∃ fW : W.scheme ⟶ pullback f V.toBase,
          fW ≫ pullback.fst f V.toBase = F ∧
            fW ≫ pullback.snd f V.toBase = W.toBase ≫ pullback.snd g τ) ∧
        ∀ a : X.presheaf.stalk x,
          W.completionMap (φ a) -
              algebraMap (W.scheme.presheaf.stalk W.point)
                (AdicCompletion (maximalIdeal (W.scheme.presheaf.stalk W.point))
                  (W.scheme.presheaf.stalk W.point)) (F.stalkHomAt hF a) ∈
            Ideal.map
              (algebraMap (W.scheme.presheaf.stalk W.point)
                (AdicCompletion (maximalIdeal (W.scheme.presheaf.stalk W.point))
                  (W.scheme.presheaf.stalk W.point)))
              (maximalIdeal (W.scheme.presheaf.stalk W.point) ^ N)
```

**`StacksDraft.ArtinApproximation.exists_relativeMapApproximation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/CompletedBaseChangeMapApproximation.lean, line 344](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/CompletedBaseChangeMapApproximation.lean#L344). The attribute's comment: “the source's own hypotheses, with nothing beyond them: `h : T ⟶ S` locally of finite type, a G-ring `𝒪_{S, s}`, a local `𝒪_{S, s}`-algebra map `σ : 𝒪_{T, t} → 𝒪^∧_{S, s}`, the base change `Y_σ = Y ×_{T, σ} Spec 𝒪^∧_{S, s}`, a point `y_σ` of `Y_σ` over `y` (the source's `the` point: lying over `y` forces it over the closed point, by `StacksDraft.ArtinApproximation.snd_eq_closedPoint_of_fst_eq`, so no second hypothesis places it there) and a local `𝒪_{S, s}`-algebra map `φ : 𝒪_{X, x} → 𝒪^∧_{Y_σ, y_σ}`. Theorem 07QZ is discharged, not an input: the `LocalApproximationProperty` hypothesis of Tag 0CAU behind both stages is supplied by `StacksDraft.ArtinApproximation.localApproximationProperty`, which rests on the unconditional Tag 07QZ `Stacks.Smoothing.exists_localEtaleSolution_of_isGRing` and hence on the unconditional Popescu Theorem 07GC `Stacks.Smoothing.indSmooth_of_isRegularRingMap`. The conclusion is the source's whole diagram: clause (1) — `v ↦ s`, `τ(v) = t`, `f(w) = (x, v)` as the two projection identities of `f` with `F w = x`, and `w ↦ (y, v)` as `W.map_point` with the point of `Y ×_{T, τ} V` lying over `y` and `v`; clause (2); clause (3); clause (4); and clause (5), the commuting square, whose `=` between `𝒪_{Y_σ, y_σ}/𝔪^N` and `𝒪_{Y ×_{T, τ} V, (y, v)}/𝔪^N` is exhibited as the ring isomorphism `θ` together with the two compatibilities that characterise it as the source's canonical identification over `𝒪_{V, v}/𝔪_v ^ N = 𝒪_{S, s}/𝔪_s ^ N`: it matches the two maps from `𝒪_{Y, y}` and the two maps from `𝒪_{S, s}`. Only the truncations are identified; the completions need not be isomorphic, as the cusp-versus-node example in the module docstring of `StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/FiniteTypeBaseApproximation.lean` shows. The route is the source's own: Tag 0CAU over `Spec 𝒪^∧_{S, s}` replaces `φ` by a morphism to `X` out of an elementary étale neighbourhood of `(Y_σ, y_σ)`, that pointed span descends to a smooth stage of Popescu's presentation of `𝒪^∧_{S, s}`, and Tag 0CAU applied one more time to `Spec 𝒪_{T, t}` and `Spec 𝒪_{S, s}` over `Spec 𝒪_{S, s}` replaces the stage by `(V, v)`; `θ` is the order-`N` comparison of the two base changes of the stage object, along `Spec 𝒪^∧_{S, s} ⟶ D` and along `V ⟶ D`, read through the two étale legs. The identification of the closed fibres `(Y_σ)_s ≅ (Y ×_T V)_v` of Tag 0GDX is recorded as well”.

> **Stacks Project, Tag 0CAW (More on Morphisms, Lemma 37.39.6).** Let `S` be a locally
> Noetherian scheme, let `p : X ⟶ S`, `q : Y ⟶ T` and `h : T ⟶ S` be locally of finite type, let
> `x ∈ X` lie over `s ∈ S` and `y ∈ Y` over `t ∈ T` with `h t = s`, and assume `𝒪_{S, s}` is a
> G-ring. Let `σ : 𝒪_{T, t} → 𝒪^∧_{S, s}` be a local `𝒪_{S, s}`-algebra map, write
> `Y_σ = Y ×_{T, σ} Spec 𝒪^∧_{S, s}`, let `y_σ` be a point of `Y_σ` over `y` — the only one, since
> such a point lies over the closed point by
> `StacksDraft.ArtinApproximation.snd_eq_closedPoint_of_fst_eq` — and let
> `φ : 𝒪_{X, x} → 𝒪^∧_{Y_σ, y_σ}` be a local `𝒪_{S, s}`-algebra map.
>
> Then for every `N ≥ 1` there is a commutative diagram
> ```
> X ← X ×_S V ←—f— W —→ Y ×_{T, τ} V → Y
> ↓               ↓                     ↓
> S ←——————————— V ———τ——————————————→ T
> ```
> of schemes over `S` with points `w ∈ W` and `v ∈ V` such that
> 1. `v ↦ s`, `τ v = t`, `f w = (x, v)` and `w ↦ (y, v)`;
> 2. `(V, v) → (S, s)` is an elementary étale neighbourhood;
> 3. the square relating `σ` to `τ^♯_v` commutes modulo `𝔪_v ^ N`;
> 4. `(W, w) → (Y ×_{T, τ} V, (y, v))` is an elementary étale neighbourhood;
> 5. the square
> ```
> 𝒪_{X, x} —φ→ 𝒪^∧_{Y_σ, y_σ} → 𝒪_{Y_σ, y_σ}/𝔪^N —θ→ 𝒪_{Y ×_{T, τ} V, (y, v)}/𝔪^N
>    ‖                                                           ↓
> 𝒪_{X, x} → 𝒪_{X ×_S V, (x, v)} —f^♯_w→ 𝒪_{W, w} ———————→ 𝒪_{W, w}/𝔪^N
> ```
> commutes, where `θ` is the canonical isomorphism of `Y_σ` with `Y ×_{T, τ} V` over
> `𝒪_{V, v}/𝔪_v ^ N = 𝒪_{S, s}/𝔪_s ^ N` that clauses (2) and (3) provide.
>
> The isomorphism `θ` is exhibited, together with the compatibilities which characterise it: it
> matches the two maps from `𝒪_{Y, y}` and the two maps from `𝒪_{S, s}`. Only the `𝔪 ^ N`
> truncations are identified; the completions `𝒪^∧_{Y_σ, y_σ}` and `𝒪^∧_{Y ×_{T, τ} V, (y, v)}`
> need not be isomorphic, as the cusp-versus-node example in the module docstring of
> `StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/FiniteTypeBaseApproximation.lean`
> shows. The correspondence of `(y, v)` with `y_σ` on the closed fibres is recorded in addition, as
> in Tag 0GDX.

```lean
theorem exists_relativeMapApproximation
    {X S Y T : Scheme.{u}} [IsLocallyNoetherian S] (p : X ⟶ S) (q : Y ⟶ T) (h : T ⟶ S)
    [LocallyOfFiniteType p] [LocallyOfFiniteType q] [LocallyOfFiniteType h]
    {x : X} {s : S} {y : Y} {t : T} (hx : p x = s) (hy : q y = t) (hts : h t = s)
    (hG : IsGRing (S.presheaf.stalk s)) (N : ℕ) (hN : 1 ≤ N)
    (σ : T.presheaf.stalk t →+*
      AdicCompletion (maximalIdeal (S.presheaf.stalk s)) (S.presheaf.stalk s))
    (hσ : IsLocalHom σ)
    (hσbase : σ.comp (h.stalkHomAt hts) =
      algebraMap (S.presheaf.stalk s)
        (AdicCompletion (maximalIdeal (S.presheaf.stalk s)) (S.presheaf.stalk s)))
    (yσ : (pullback q (relativeBaseChangeMorphism s σ) : Scheme.{u}))
    (hyσY : pullback.fst q (relativeBaseChangeMorphism s σ) yσ = y)
    (φ : X.presheaf.stalk x →+*
      AdicCompletion
        (maximalIdeal
          ((pullback q (relativeBaseChangeMorphism s σ)).presheaf.stalk yσ))
        ((pullback q (relativeBaseChangeMorphism s σ)).presheaf.stalk yσ))
    (hφ : IsLocalHom φ)
    (hφbase : φ.comp (p.stalkHomAt hx) =
      (algebraMap ((pullback q (relativeBaseChangeMorphism s σ)).presheaf.stalk yσ)
          (AdicCompletion
            (maximalIdeal
              ((pullback q (relativeBaseChangeMorphism s σ)).presheaf.stalk yσ))
            ((pullback q (relativeBaseChangeMorphism s σ)).presheaf.stalk yσ))).comp
        (((pullback.snd q (relativeBaseChangeMorphism s σ)).stalkHomAt
            (snd_eq_closedPoint_of_fst_eq h q hy hts σ hσbase
              (relativeBaseChangeMorphism s σ) rfl yσ hyσY)).comp
          ((specCompletedStalkTo S s).stalkHomAt
            (specCompletedStalkTo_specCompletedStalkPoint S s)))) :
    ∃ (V : EtaleNeighborhood S s) (τ : V.scheme ⟶ T) (hτ : τ V.point = t)
      (yτ : (pullback q τ : Scheme.{u}))
      (hyτY : pullback.fst q τ yτ = y) (hyτV : pullback.snd q τ yτ = V.point)
      (W : EtaleNeighborhood (pullback q τ) yτ) (F : W.scheme ⟶ X) (hF : F W.point = x)
      (f : W.scheme ⟶ pullback p V.toBase),
      V.IsElementary ∧ W.IsElementary ∧ τ ≫ h = V.toBase ∧
        f ≫ pullback.fst p V.toBase = F ∧
        f ≫ pullback.snd p V.toBase = W.toBase ≫ pullback.snd q τ ∧
        F ≫ p = W.toBase ≫ pullback.snd q τ ≫ V.toBase ∧
        (∀ b : T.presheaf.stalk t,
          V.completionMap (σ b) -
              algebraMap (V.scheme.presheaf.stalk V.point)
                (AdicCompletion (maximalIdeal (V.scheme.presheaf.stalk V.point))
                  (V.scheme.presheaf.stalk V.point)) (τ.stalkHomAt hτ b) ∈
            Ideal.map
              (algebraMap (V.scheme.presheaf.stalk V.point)
                (AdicCompletion (maximalIdeal (V.scheme.presheaf.stalk V.point))
                  (V.scheme.presheaf.stalk V.point)))
              (maximalIdeal (V.scheme.presheaf.stalk V.point) ^ N)) ∧
        (∃ θ : ((pullback q (relativeBaseChangeMorphism s σ)).presheaf.stalk yσ ⧸
              maximalIdeal
                ((pullback q (relativeBaseChangeMorphism s σ)).presheaf.stalk yσ) ^ N) ≃+*
            ((pullback q τ).presheaf.stalk yτ ⧸
              maximalIdeal ((pullback q τ).presheaf.stalk yτ) ^ N),
          (∀ b : Y.presheaf.stalk y,
            θ (Ideal.Quotient.mk (maximalIdeal
                ((pullback q (relativeBaseChangeMorphism s σ)).presheaf.stalk yσ) ^ N)
                ((pullback.fst q (relativeBaseChangeMorphism s σ)).stalkHomAt hyσY b)) =
              Ideal.Quotient.mk (maximalIdeal ((pullback q τ).presheaf.stalk yτ) ^ N)
                ((pullback.fst q τ).stalkHomAt hyτY b)) ∧
          (∀ c : S.presheaf.stalk s,
            θ (Ideal.Quotient.mk (maximalIdeal
                ((pullback q (relativeBaseChangeMorphism s σ)).presheaf.stalk yσ) ^ N)
                ((pullback.snd q (relativeBaseChangeMorphism s σ)).stalkHomAt
                  (snd_eq_closedPoint_of_fst_eq h q hy hts σ hσbase
                    (relativeBaseChangeMorphism s σ) rfl yσ hyσY)
                  ((specCompletedStalkTo S s).stalkHomAt
                    (specCompletedStalkTo_specCompletedStalkPoint S s) c))) =
              Ideal.Quotient.mk (maximalIdeal ((pullback q τ).presheaf.stalk yτ) ^ N)
                ((pullback.snd q τ).stalkHomAt hyτV (V.stalkHom c))) ∧
          ∀ (α : X.presheaf.stalk x) (z : (pullback q τ).presheaf.stalk yτ),
            θ (AdicCompletion.evalₐ (maximalIdeal
                ((pullback q (relativeBaseChangeMorphism s σ)).presheaf.stalk yσ)) N
                (φ α)) =
              Ideal.Quotient.mk (maximalIdeal ((pullback q τ).presheaf.stalk yτ) ^ N) z →
            Ideal.Quotient.mk (maximalIdeal (W.scheme.presheaf.stalk W.point) ^ N)
                (W.stalkHom z) =
              Ideal.Quotient.mk (maximalIdeal (W.scheme.presheaf.stalk W.point) ^ N)
                (F.stalkHomAt hF α)) ∧
        ∃ (eBase : (specCompletedStalk S s).residueField (specCompletedStalkPoint S s) ≅
            V.scheme.residueField V.point)
          (eFiber : (pullback.snd q (relativeBaseChangeMorphism s σ)).fiber
              (specCompletedStalkPoint S s) ≅
            (pullback.snd q τ).fiber V.point),
          (Spec.map eBase.inv ≫ V.scheme.fromSpecResidueField V.point ≫ V.toBase =
            (specCompletedStalk S s).fromSpecResidueField (specCompletedStalkPoint S s) ≫
              specCompletedStalkTo S s) ∧
          (Spec.map eBase.inv ≫ V.scheme.fromSpecResidueField V.point ≫ τ =
            (specCompletedStalk S s).fromSpecResidueField (specCompletedStalkPoint S s) ≫
              relativeBaseChangeMorphism s σ) ∧
          (eFiber.hom ≫ (pullback.snd q τ).fiberι V.point ≫ pullback.fst q τ =
            (pullback.snd q (relativeBaseChangeMorphism s σ)).fiberι
                (specCompletedStalkPoint S s) ≫
              pullback.fst q (relativeBaseChangeMorphism s σ)) ∧
          (eFiber.hom ≫ (pullback.snd q τ).fiberToSpecResidueField V.point =
            (pullback.snd q (relativeBaseChangeMorphism s σ)).fiberToSpecResidueField
                (specCompletedStalkPoint S s) ≫ Spec.map eBase.inv) ∧
          (eFiber.hom (((pullback.snd q (relativeBaseChangeMorphism s σ)).fiberHomeo
              (specCompletedStalkPoint S s)).symm
              ⟨yσ, snd_eq_closedPoint_of_fst_eq h q hy hts σ hσbase
                (relativeBaseChangeMorphism s σ) rfl yσ hyσY⟩) =
            ((pullback.snd q τ).fiberHomeo V.point).symm ⟨yτ, hyτV⟩)
```

## Tag 0CAX, a lemma

[Tag 0CAX](https://stacks.math.columbia.edu/tag/0CAX) in the Stacks Project.

**`AlgebraicGeometry.exists_finiteType_pointed_extension_agree_mod_maximalIdeal_pow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/ArtinApproximation.lean, line 814](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/ArtinApproximation.lean#L814).

> A local map from the stalk of a finite-type Noetherian scheme to the completed local ring
> of its base can be made rigid modulo any positive power of the base maximal ideal after a
> pointed finite-type extension.
>
> This is the source's statement, in which the comparison maps `σ'` are required to be local. It is
> `AlgebraicGeometry.exists_finiteType_pointed_extension_agree_mod_maximalIdeal_pow_of_factors`,
> which proves the agreement clause for every `σ'` factoring through the extension.

```lean
theorem exists_finiteType_pointed_extension_agree_mod_maximalIdeal_pow
    {S T : Scheme.{u}} (f : T ⟶ S)
    [IsNoetherian S] [IsNoetherian T]
    [LocallyOfFiniteType f] [QuasiCompact f]
    (s : S) (t : T) (ht : f t = s)
    (sigma : T.presheaf.stalk t →+*
      AdicCompletion (maximalIdeal (S.presheaf.stalk s)) (S.presheaf.stalk s))
    (hsigma : IsLocalHom sigma)
    (hsigma_base :
      sigma.comp ((f.stalkMap t).hom.comp
        (eqToHom (congrArg (fun z ↦ S.presheaf.stalk z) ht).symm).hom) =
        algebraMap (S.presheaf.stalk s)
          (AdicCompletion (maximalIdeal (S.presheaf.stalk s)) (S.presheaf.stalk s)))
    (N : ℕ) (hN : 1 ≤ N) :
    ∃ (T' : Scheme.{u}) (g : T' ⟶ T) (t' : T') (hgt : g t' = t)
      (_ : LocallyOfFiniteType g) (_ : QuasiCompact g),
      ∃ tau : T'.presheaf.stalk t' →+*
          AdicCompletion (maximalIdeal (S.presheaf.stalk s)) (S.presheaf.stalk s),
        IsLocalHom tau ∧
        sigma = tau.comp ((g.stalkMap t').hom.comp
          (eqToHom (congrArg (fun z ↦ T.presheaf.stalk z) hgt).symm).hom) ∧
        tau.comp ((g.stalkMap t').hom.comp
          ((eqToHom (congrArg (fun z ↦ T.presheaf.stalk z) hgt).symm).hom.comp
            ((f.stalkMap t).hom.comp
              (eqToHom (congrArg (fun z ↦ S.presheaf.stalk z) ht).symm).hom))) =
          algebraMap (S.presheaf.stalk s)
            (AdicCompletion (maximalIdeal (S.presheaf.stalk s)) (S.presheaf.stalk s)) ∧
        (∀ (sigma' : T.presheaf.stalk t →+*
            AdicCompletion (maximalIdeal (S.presheaf.stalk s)) (S.presheaf.stalk s)),
          IsLocalHom sigma' →
          sigma'.comp ((f.stalkMap t).hom.comp
              (eqToHom (congrArg (fun z ↦ S.presheaf.stalk z) ht).symm).hom) =
              algebraMap (S.presheaf.stalk s)
                (AdicCompletion (maximalIdeal (S.presheaf.stalk s))
                  (S.presheaf.stalk s)) →
          (∃ tau' : T'.presheaf.stalk t' →+*
              AdicCompletion (maximalIdeal (S.presheaf.stalk s)) (S.presheaf.stalk s),
            sigma' = tau'.comp ((g.stalkMap t').hom.comp
              (eqToHom (congrArg (fun z ↦ T.presheaf.stalk z) hgt).symm).hom)) →
          ∀ a : T.presheaf.stalk t,
            sigma a - sigma' a ∈
              Ideal.map
                (algebraMap (S.presheaf.stalk s)
                  (AdicCompletion (maximalIdeal (S.presheaf.stalk s))
                    (S.presheaf.stalk s)))
                (maximalIdeal (S.presheaf.stalk s) ^ N))
```

## Tag 0CAY, a lemma

[Tag 0CAY](https://stacks.math.columbia.edu/tag/0CAY) in the Stacks Project.

**`Stacks.ConormalApproximation.exists_finiteType_pointed_extension_conormalAlgebra_iso_of_isLocalHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/ConormalApproximationSubFamily.lean, line 698](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/ConormalApproximationSubFamily.lean#L698).

> **Stacks 0CAY.** Let `Y → T → S` be finite type morphisms of Noetherian schemes, let `t ∈ T`
> lie over `s ∈ S` and let `σ : 𝒪_{T,t} → 𝒪^∧_{S,s}` be a local `𝒪_{S,s}`-algebra map. Then there
> is a finite type morphism of pointed schemes `(T', t') → (T, t)` through which `σ` factors by a
> local homomorphism, such that for *every* local `𝒪_{S,s}`-algebra map
> `σ' : 𝒪_{T,t} → 𝒪^∧_{S,s}` factoring through `𝒪_{T',t'}` the two closed immersions
> `Y_σ ← Y_t → Y_{σ'}` of the fibre into the two base changes exist and have isomorphic conormal
> algebras.
>
> The hypotheses are the source's and nothing more: `σ` is assumed local because the source assumes
> it ("let `σ : 𝒪_{T,t} → 𝒪_{S,s}^∧` be a local `𝒪_{S,s}`-algebra map"), and it is in any case
> forced — a factorisation of `σ` through a local homomorphism out of the stalk of an extension
> makes `σ` local.
>
> This is
> `Stacks.ConormalApproximation.exists_finiteType_pointed_extension_conormalAlgebra_iso_of_bound`
> with its comparison hypothesis discharged by
> `Stacks.ConormalApproximation.hasConormalBoundAlongExtension_of_isLocalHom`. The two facts that
> discharge it are the locality of the identity-induced comparison
> (`Stacks.ArtinRees.sameDenominator_iff_exists_isInducedByIdentity` together with
> `Stacks.ConormalApproximation.sameDenominator_of_presentations` and
> `Stacks.ConormalApproximation.sameDenominator_of_localization`), which lets the chart-local
> comparison be propagated from a chart to the basic opens inside it, and the compactness of the
> fibre, which makes finitely many charts enough — so the per-presentation Artin-Rees bound of the
> affine core suffices, which is exactly the source's "cover `Y` by finitely many affines and glue
> by uniqueness".

```lean
theorem exists_finiteType_pointed_extension_conormalAlgebra_iso_of_isLocalHom
    {S T Y : Scheme.{u}} (f : T ⟶ S) (p : Y ⟶ T)
    [IsNoetherian S] [IsNoetherian T] [IsNoetherian Y]
    [LocallyOfFiniteType f] [QuasiCompact f]
    [LocallyOfFiniteType p] [QuasiCompact p]
    (s : S) (t : T) (ht : f t = s)
    (sigma : T.presheaf.stalk t →+* completedStalk S s) (hsigma : IsLocalHom sigma)
    (hsigma_base : sigma.comp (pointedStalkMap f ht) =
      algebraMap (S.presheaf.stalk s) (completedStalk S s)) :
    ∃ (T' : Scheme.{u}) (g : T' ⟶ T) (t' : T') (hgt : g t' = t)
      (_ : LocallyOfFiniteType g) (_ : QuasiCompact g),
      ∃ tau : T'.presheaf.stalk t' →+* completedStalk S s,
        IsLocalHom tau ∧
        sigma = tau.comp (pointedStalkMap g hgt) ∧
        ∀ sigma' : T.presheaf.stalk t →+* completedStalk S s,
          IsLocalHom sigma' →
          sigma'.comp (pointedStalkMap f ht) =
            algebraMap (S.presheaf.stalk s) (completedStalk S s) →
          (∃ tau' : T'.presheaf.stalk t' →+* completedStalk S s,
            sigma' = tau'.comp (pointedStalkMap g hgt)) →
          HasIsoConormalFibreImmersions p t
            (Spec.map (CommRingCat.ofHom sigma) ≫ T.fromSpecStalk t)
            (Spec.map (CommRingCat.ofHom sigma') ≫ T.fromSpecStalk t)
```

## Tag 0CAZ, an equation

[Tag 0CAZ](https://stacks.math.columbia.edu/tag/0CAZ) in the Stacks Project.

**`Stacks.SyzygyCoefficients.exact_resolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FiniteType/SyzygyCoefficients.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/FiniteType/SyzygyCoefficients.lean#L131).

> Let `P` present `B` as `C[x_1, …, x_n]/(f_1, …, f_m)`, let `σ : C → D` make `D` a
> `C`-algebra and let `a_{kj} ∈ D[x_1, …, x_n]`, `k = 1, …, K`, generate the module of relations
> among the `σ(f_j)`. Then `D[x]^{⊕K} → D[x]^{⊕m} → D[x] → B ⊗_{C, σ} D → 0` is exact.

```lean
theorem exact_resolution
    {C : Type u} {B : Type v} {D : Type w}
    [CommRing C] [CommRing B] [CommRing D] [Algebra C B] [Algebra C D]
    {n m K : ℕ} (P : Algebra.Presentation C B (Fin n) (Fin m))
    (a : Fin K → Fin m → MvPolynomial (Fin n) D)
    (ha : ∀ k, ∑ j, a k j * MvPolynomial.map (algebraMap C D) (P.relation j) = 0)
    (hgen : ∀ v : Fin m → MvPolynomial (Fin n) D,
      (∑ j, v j * MvPolynomial.map (algebraMap C D) (P.relation j) = 0) →
      ∃ w : Fin K → MvPolynomial (Fin n) D, ∀ j, v j = ∑ k, w k * a k j) :
    LinearMap.ker (relationMap D P) = LinearMap.range (syzygyMap a) ∧
      LinearMap.range (relationMap D P) =
        RingHom.ker (aeval (R := D) (S₁ := D ⊗[C] B) (P.baseChange D).val) ∧
      Function.Surjective (aeval (R := D) (S₁ := D ⊗[C] B) (P.baseChange D).val)
```

## Tag 0CB0, an equation

[Tag 0CB0](https://stacks.math.columbia.edu/tag/0CB0) in the Stacks Project.

**`Stacks.SyzygyCoefficients.exists_finiteType_resolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FiniteType/SyzygyCoefficients.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/FiniteType/SyzygyCoefficients.lean#L190).

> Let `P` present `B` as `C[x_1, …, x_n]/(f_1, …, f_m)`, let `D` be a `C`-algebra, and let
> `a_{kj} ∈ D[x_1, …, x_n]`, `k = 1, …, K`, be syzygies `∑_j a_{kj} f_j = 0` generating all
> syzygies among the images of the `f_j`. Then there are a `C`-algebra `C'` of finite type, a
> `C`-algebra map `τ : C' → D` and polynomials `t_{kj} ∈ C'[x_1, …, x_n]` with `∑_j t_{kj} f_j = 0`,
> such that `τ` carries the `t_{kj}` to the `a_{kj}` and the four-term complex over
> `C'[x_1, …, x_n]` built from the `t_{kj}` and the `f_j` is exact at `C'[x_1, …, x_n]` and at
> `B ⊗_C C'`.

```lean
theorem exists_finiteType_resolution
    {C : Type u} {B : Type v} {D : Type w}
    [CommRing C] [CommRing B] [CommRing D] [Algebra C B] [Algebra C D]
    {n m K : ℕ} (P : Algebra.Presentation C B (Fin n) (Fin m))
    (a : Fin K → Fin m → MvPolynomial (Fin n) D)
    (ha : ∀ k, ∑ j, a k j * MvPolynomial.map (algebraMap C D) (P.relation j) = 0)
    (_hgen : ∀ v : Fin m → MvPolynomial (Fin n) D,
      (∑ j, v j * MvPolynomial.map (algebraMap C D) (P.relation j) = 0) →
      ∃ w : Fin K → MvPolynomial (Fin n) D, ∀ j, v j = ∑ k, w k * a k j) :
    ∃ (C' : Type u) (_ : CommRing C') (_ : Algebra C C') (_ : Algebra.FiniteType C C')
      (τ : C' →ₐ[C] D) (t : Fin K → Fin m → MvPolynomial (Fin n) C'),
      (∀ k, ∑ j, t k j * MvPolynomial.map (algebraMap C C') (P.relation j) = 0) ∧
      (∀ k j, MvPolynomial.map (τ : C' →+* D) (t k j) = a k j) ∧
      (∀ j, MvPolynomial.map (τ : C' →+* D)
        (MvPolynomial.map (algebraMap C C') (P.relation j)) =
        MvPolynomial.map (algebraMap C D) (P.relation j)) ∧
      Ideal.span (Set.range fun j : Fin m =>
          MvPolynomial.map (algebraMap C C') (P.relation j)) =
        RingHom.ker (aeval (R := C') (S₁ := C' ⊗[C] B) (P.baseChange C').val) ∧
      Function.Surjective (aeval (R := C') (S₁ := C' ⊗[C] B) (P.baseChange C').val)
```

## Tag 0CB1, a lemma

[Tag 0CB1](https://stacks.math.columbia.edu/tag/0CB1) in the Stacks Project.

**`StacksDraft.ArtinApproximation.exists_etale_relativeIsomorphismApproximation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/RelativeMapApproximation.lean, line 4580](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/RelativeMapApproximation.lean#L4580). The attribute's comment: “the source's own hypotheses, with nothing beyond them: `h : T ⟶ S` locally of finite type, `σ : 𝒪_{T, t} → 𝒪^∧_{S, s}` a local `𝒪_{S, s}`-algebra map for `h`, the base change `Y_σ = Y ×_{T, σ} Spec 𝒪^∧_{S, s}`, a point `y_σ` of `Y_σ` over `y` and the closed point, and the isomorphism `φ : 𝒪^∧_{X, x} ≅ 𝒪^∧_{Y_σ, y_σ}` of `𝒪_{S, s}`-algebras which is what 0CB1 adds to Tag 0CAW. Theorem 07QZ is NOT carried: the `LocalApproximationProperty` hypothesis of Tag 0CAU behind Tag 0CAV and behind the first stage of Tag 0CAW is discharged with `StacksDraft.ArtinApproximation.localApproximationProperty`, which rests on the unconditional Tag 07QZ `Stacks.Smoothing.exists_localEtaleSolution_of_isGRing` and hence on the unconditional Popescu Theorem 07GC `Stacks.Smoothing.indSmooth_of_isRegularRingMap`. The conclusion is the source's whole diagram: clauses (1), (2), (3), (4) and (5) of Tag 0CAW together with the étaleness of `f : W ⟶ X ×_S V`, which is the content of 0CB1. Clause (5) is the ring isomorphism `θ : 𝒪_{Y_σ, y_σ}/𝔪^N ≅ 𝒪_{Y ×_{T, τ} V, (y, v)}/𝔪^N` which the conclusion exhibits, compatible with the two maps from `𝒪_{Y, y}` and with the two maps from `𝒪_{S, s}` — the compatibilities which characterise the source's canonical identification over `𝒪_{V, v}/𝔪_v ^ N = 𝒪_{S, s}/𝔪_s ^ N` — together with the source's commuting square: `φ` read on `𝒪_{X, x}` through `θ` and then through `W ⟶ Y ×_{T, τ} V` is `F^♯_w` modulo `𝔪_w ^ N`. Only the `𝔪 ^ N`-truncations are identified; the completions `𝒪^∧_{Y_σ, y_σ}` and `𝒪^∧_{Y ×_{T, τ} V, y_τ}` need not be isomorphic, as the cusp-versus-node example in the module docstring of `StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/FiniteTypeBaseApproximation.lean` shows. The identification of the closed fibres `(Y_σ)_s ≅ (Y ×_T V)_v` of Tag 0GDX is recorded as well. The route to étaleness is Tag 0CAV over `Spec 𝒪^∧_{S, s}` followed by the descent of Tag 0GDX, which delivers `W ⟶ X` étale directly, in place of the source's comparison of associated graded rings through Tag 0CAY; clause (5) comes from the congruence modulo `𝔪 ^ N` that Tag 0CAV supplies upstairs, transported to `W` by the order-`N` comparison of the two base changes of the stage object along `Spec 𝒪^∧_{S, s} ⟶ D` and along `V ⟶ D`”.

> **Stacks Project, Tag 0CB1 (More on Morphisms, Lemma 37.39.7).** With the notation and
> assumptions of Tag 0CAW — a locally Noetherian `S`, morphisms `p : X ⟶ S`, `q : Y ⟶ T` and
> `h : T ⟶ S` locally of finite type, points `x ↦ s` and `y ↦ t ↦ s`, a G-ring `𝒪_{S, s}`, a
> local `𝒪_{S, s}`-algebra map `σ : 𝒪_{T, t} → 𝒪^∧_{S, s}`, the base change
> `Y_σ = Y ×_{T, σ} Spec 𝒪^∧_{S, s}` and a point `y_σ` of it over `y` and over the closed point —
> assume moreover that `φ` induces an isomorphism `𝒪^∧_{X, x} ≅ 𝒪^∧_{Y_σ, y_σ}` of
> `𝒪_{S, s}`-algebras on completions. Then for every `N ≥ 1` the diagram of Tag 0CAW can be
> chosen with `f` étale: there are an elementary étale neighbourhood `(V, v)` of `(S, s)`, a
> morphism `τ : V ⟶ T` over `S` with `τ v = t` whose square with `σ` commutes modulo `𝔪_v ^ N`, a
> point `y_τ` of `Y ×_{T, τ} V` over `y` and `v` which corresponds to `y_σ` on the closed fibres,
> an elementary étale neighbourhood `(W, w)` of `(Y ×_{T, τ} V, y_τ)`, a morphism `F : W ⟶ X`
> over `S` carrying `w` to `x`, and an **étale** `f : W ⟶ X ×_S V` with `f ≫ pr₁ = F` and
> `f ≫ pr₂ = W ⟶ Y ×_{T, τ} V ⟶ V`, so that `f w = (x, v)`.
>
> Clause (5) of Tag 0CAW is the ring isomorphism
> `θ : 𝒪_{Y_σ, y_σ}/𝔪_{y_σ} ^ N ≅ 𝒪_{Y ×_{T, τ} V, (y, v)}/𝔪_{(y, v)} ^ N`
> which the conclusion exhibits, compatible with the two maps from `𝒪_{Y, y}` and with the two
> maps from `𝒪_{S, s}` — the compatibilities which make `θ` the source's canonical identification
> of the two base changes over `𝒪_{V, v}/𝔪_v ^ N = 𝒪_{S, s}/𝔪_s ^ N` — together with the
> commutativity of the source's square: `φ` read on `𝒪_{X, x}` through `θ` and then through the
> elementary étale neighbourhood `W ⟶ Y ×_{T, τ} V` is `F^♯_w` modulo `𝔪_w ^ N`. No isomorphism
> of the completions `𝒪^∧_{Y_σ, y_σ}` and `𝒪^∧_{Y ×_{T, τ} V, y_τ}` is asserted: only the
> `𝔪 ^ N`-truncations are identified, and for a pair `(V, τ)` satisfying clauses (2) and (3)
> alone the completions can be a cusp and a node.
>
> The correspondence of `y_τ` with `y_σ` is recorded in addition, as in Tag 0GDX: an isomorphism
> `eBase` of the residue fields of the two bases compatible with their maps to `S` and to `T`, and
> an isomorphism `eFiber` of the scheme-theoretic closed fibres compatible with the two maps to
> `Y` and with `eBase`, carrying the point above `y_σ` to the point above `y_τ`.

```lean
theorem exists_etale_relativeIsomorphismApproximation
    {X S Y T : Scheme.{u}} [IsLocallyNoetherian S] (p : X ⟶ S) (q : Y ⟶ T) (h : T ⟶ S)
    [LocallyOfFiniteType p] [LocallyOfFiniteType q] [LocallyOfFiniteType h]
    {x : X} {s : S} {y : Y} {t : T} (hx : p x = s) (hy : q y = t) (hts : h t = s)
    (hG : IsGRing (S.presheaf.stalk s)) (N : ℕ) (hN : 1 ≤ N)
    (σ : T.presheaf.stalk t →+*
      AdicCompletion (maximalIdeal (S.presheaf.stalk s)) (S.presheaf.stalk s))
    (hσ : IsLocalHom σ)
    (hσbase : σ.comp (h.stalkHomAt hts) =
      algebraMap (S.presheaf.stalk s)
        (AdicCompletion (maximalIdeal (S.presheaf.stalk s)) (S.presheaf.stalk s)))
    (yσ : (pullback q (relativeBaseChangeMorphism s σ) : Scheme.{u}))
    (hyσY : pullback.fst q (relativeBaseChangeMorphism s σ) yσ = y)
    (hyσZ : pullback.snd q (relativeBaseChangeMorphism s σ) yσ =
      specCompletedStalkPoint S s)
    (φ : AdicCompletion (maximalIdeal (X.presheaf.stalk x)) (X.presheaf.stalk x) ≃+*
      AdicCompletion
        (maximalIdeal
          ((pullback q (relativeBaseChangeMorphism s σ)).presheaf.stalk yσ))
        ((pullback q (relativeBaseChangeMorphism s σ)).presheaf.stalk yσ))
    (hφ : φ.toRingHom.comp ((algebraMap (X.presheaf.stalk x)
          (AdicCompletion (maximalIdeal (X.presheaf.stalk x)) (X.presheaf.stalk x))).comp
        (p.stalkHomAt hx)) =
      (algebraMap ((pullback q (relativeBaseChangeMorphism s σ)).presheaf.stalk yσ)
          (AdicCompletion
            (maximalIdeal
              ((pullback q (relativeBaseChangeMorphism s σ)).presheaf.stalk yσ))
            ((pullback q (relativeBaseChangeMorphism s σ)).presheaf.stalk yσ))).comp
        (((pullback.snd q (relativeBaseChangeMorphism s σ)).stalkHomAt hyσZ).comp
          ((specCompletedStalkTo S s).stalkHomAt
            (specCompletedStalkTo_specCompletedStalkPoint S s)))) :
    ∃ (V : EtaleNeighborhood S s) (τ : V.scheme ⟶ T) (hτ : τ V.point = t)
      (yτ : (pullback q τ : Scheme.{u}))
      (hyτY : pullback.fst q τ yτ = y) (hyτV : pullback.snd q τ yτ = V.point)
      (W : EtaleNeighborhood (pullback q τ) yτ) (F : W.scheme ⟶ X) (hF : F W.point = x)
      (f : W.scheme ⟶ pullback p V.toBase),
      V.IsElementary ∧ W.IsElementary ∧ τ ≫ h = V.toBase ∧ Etale f ∧
        f ≫ pullback.fst p V.toBase = F ∧
        f ≫ pullback.snd p V.toBase = W.toBase ≫ pullback.snd q τ ∧
        F ≫ p = W.toBase ≫ pullback.snd q τ ≫ V.toBase ∧
        (∀ b : T.presheaf.stalk t,
          V.completionMap (σ b) -
              algebraMap (V.scheme.presheaf.stalk V.point)
                (AdicCompletion (maximalIdeal (V.scheme.presheaf.stalk V.point))
                  (V.scheme.presheaf.stalk V.point)) (τ.stalkHomAt hτ b) ∈
            Ideal.map
              (algebraMap (V.scheme.presheaf.stalk V.point)
                (AdicCompletion (maximalIdeal (V.scheme.presheaf.stalk V.point))
                  (V.scheme.presheaf.stalk V.point)))
              (maximalIdeal (V.scheme.presheaf.stalk V.point) ^ N)) ∧
        (∃ θ : ((pullback q (relativeBaseChangeMorphism s σ)).presheaf.stalk yσ) ⧸
              (maximalIdeal
                ((pullback q (relativeBaseChangeMorphism s σ)).presheaf.stalk yσ) ^ N) ≃+*
            ((pullback q τ).presheaf.stalk yτ) ⧸
              (maximalIdeal ((pullback q τ).presheaf.stalk yτ) ^ N),
          (∀ b : Y.presheaf.stalk y,
            θ (Ideal.Quotient.mk (maximalIdeal
                ((pullback q (relativeBaseChangeMorphism s σ)).presheaf.stalk yσ) ^ N)
                ((pullback.fst q (relativeBaseChangeMorphism s σ)).stalkHomAt hyσY b)) =
              Ideal.Quotient.mk (maximalIdeal ((pullback q τ).presheaf.stalk yτ) ^ N)
                ((pullback.fst q τ).stalkHomAt hyτY b)) ∧
          (∀ c : S.presheaf.stalk s,
            θ (Ideal.Quotient.mk (maximalIdeal
                ((pullback q (relativeBaseChangeMorphism s σ)).presheaf.stalk yσ) ^ N)
                ((pullback.snd q (relativeBaseChangeMorphism s σ)).stalkHomAt hyσZ
                  ((specCompletedStalkTo S s).stalkHomAt
                    (specCompletedStalkTo_specCompletedStalkPoint S s) c))) =
              Ideal.Quotient.mk (maximalIdeal ((pullback q τ).presheaf.stalk yτ) ^ N)
                ((pullback.snd q τ).stalkHomAt hyτV (V.stalkHom c))) ∧
          ∀ (α : X.presheaf.stalk x) (z : (pullback q τ).presheaf.stalk yτ),
            θ (AdicCompletion.evalₐ (maximalIdeal
                ((pullback q (relativeBaseChangeMorphism s σ)).presheaf.stalk yσ)) N
                (φ (algebraMap (X.presheaf.stalk x)
                  (AdicCompletion (maximalIdeal (X.presheaf.stalk x))
                    (X.presheaf.stalk x)) α))) =
              Ideal.Quotient.mk (maximalIdeal ((pullback q τ).presheaf.stalk yτ) ^ N) z →
            Ideal.Quotient.mk (maximalIdeal (W.scheme.presheaf.stalk W.point) ^ N)
                (W.stalkHom z) =
              Ideal.Quotient.mk (maximalIdeal (W.scheme.presheaf.stalk W.point) ^ N)
                (F.stalkHomAt hF α)) ∧
        ∃ (eBase : (specCompletedStalk S s).residueField (specCompletedStalkPoint S s) ≅
            V.scheme.residueField V.point)
          (eFiber : (pullback.snd q (relativeBaseChangeMorphism s σ)).fiber
              (specCompletedStalkPoint S s) ≅
            (pullback.snd q τ).fiber V.point),
          (Spec.map eBase.inv ≫ V.scheme.fromSpecResidueField V.point ≫ V.toBase =
            (specCompletedStalk S s).fromSpecResidueField (specCompletedStalkPoint S s) ≫
              specCompletedStalkTo S s) ∧
          (Spec.map eBase.inv ≫ V.scheme.fromSpecResidueField V.point ≫ τ =
            (specCompletedStalk S s).fromSpecResidueField (specCompletedStalkPoint S s) ≫
              relativeBaseChangeMorphism s σ) ∧
          (eFiber.hom ≫ (pullback.snd q τ).fiberι V.point ≫ pullback.fst q τ =
            (pullback.snd q (relativeBaseChangeMorphism s σ)).fiberι
                (specCompletedStalkPoint S s) ≫
              pullback.fst q (relativeBaseChangeMorphism s σ)) ∧
          (eFiber.hom ≫ (pullback.snd q τ).fiberToSpecResidueField V.point =
            (pullback.snd q (relativeBaseChangeMorphism s σ)).fiberToSpecResidueField
                (specCompletedStalkPoint S s) ≫ Spec.map eBase.inv) ∧
          (eFiber.hom (((pullback.snd q (relativeBaseChangeMorphism s σ)).fiberHomeo
              (specCompletedStalkPoint S s)).symm ⟨yσ, hyσZ⟩) =
            ((pullback.snd q τ).fiberHomeo V.point).symm ⟨yτ, hyτV⟩)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.39, Tag 0CAT](https://stacks.math.columbia.edu/tag/0CAT)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
