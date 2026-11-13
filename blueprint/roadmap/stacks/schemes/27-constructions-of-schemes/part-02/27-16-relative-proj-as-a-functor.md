---
declaration: section
origin: cited
lean: Stacks.AlgebraicGeometry.RelativeProjQcohSheaf.Fd.toBase, Stacks.AlgebraicGeometry.RelativeProjQcohSheaf.Fd.overFunctor, Stacks.AlgebraicGeometry.RelativeProjQcohSheaf.Quadruple, Stacks.AlgebraicGeometry.RelativeProjQcohSheaf.Quadruple.StrictlyEquivalent, Stacks.AlgebraicGeometry.RelativeProjQcohSheaf.Quadruple.strictlyEquivalent_equivalence, Stacks.AlgebraicGeometry.RelativeProjQcohSheaf.Fd, Stacks.AlgebraicGeometry.RelativeProjQcohSheaf.Quadruple.strictlyEquivalent_pullback_id, Stacks.AlgebraicGeometry.RelativeProjQcohSheaf.Quadruple.strictlyEquivalent_pullback_comp
statement: formalized
proof: formalized
---

# 27.16 Relative Proj as a functor

Section 27.16 of the Stacks Project, [Tag 01NS](https://stacks.math.columbia.edu/tag/01NS). 13 tags here are carried by 27 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01NS, the section

[Tag 01NS](https://stacks.math.columbia.edu/tag/01NS) in the Stacks Project.

**`Stacks.AlgebraicGeometry.RelativeProjQcohSheaf.Fd.toBase`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjQcohSheaf/OverBase.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RelativeProjQcohSheaf/OverBase.lean#L97). The attribute's comment: “the projection of F\_d to the functor of points of the base, as a natural transformation F\_d ⟹ h\_S: a class in F\_d(T) records a morphism T ⟶ S and the identification is natural in the test scheme. This is the structure that makes `representable by a scheme over S` (Tag 01NV) and the fibre product h\_\{S'} ×\_\{h\_S} F\_d (Tag 01NT) statable; neither of those is proved here”.

> **Stacks Project, Section 01NS: the projection `F_d ⟹ h_S`.** A point of `F_d(T)` is the
> strict equivalence class of a quadruple `(d, f : T → S, L, ψ)`, and this is the natural
> transformation sending it to the morphism `f` it records.
>
> Naturality is the computation `Fd.pullback_fst` of the morphism to the base of a pulled-back
> class: it is the composite of the morphism of test schemes with the old one, which is exactly the
> action of `h_S` on a morphism.

```lean
def Fd.toBase : Fd.functor A d ⟶ yoneda.obj S ⋙ uliftFunctor.{u + 1, u}
```

**`Stacks.AlgebraicGeometry.RelativeProjQcohSheaf.Fd.overFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjQcohSheaf/OverBase.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RelativeProjQcohSheaf/OverBase.lean#L142). The attribute's comment: “the functor F\_d on the category of schemes OVER S, for an arbitrary base scheme: on an object f : T ⟶ S the set of strict equivalence classes of quadruples (d, f, L, psi) with that structure morphism, on a morphism of Sch/S the pullback of a quadruple. The two functor laws are Fd.pullback\_id and Fd.pullback\_comp. Representability of F\_d is Tag 01NV and is not proved here”.

> **Stacks Project, Section 01NS: the functor `F_d : (Sch/S)^{opp} ⟶ Sets`.** On an object
> `f : T ⟶ S` of the category of schemes over `S` its value is the fibre of `F_d(T)` over `f`,
> that is, the set of strict equivalence classes of quadruples `(d, f, L, ψ)` with that structure
> morphism; on a morphism of `Sch/S` it is the pullback of a quadruple, which lands in the fibre
> over the new structure morphism because the morphism to the base of a pulled-back class is the
> composite.
>
> This is the form of `F_d` the source's phrase "a functor on schemes over `S`" refers to; the
> form fibred over `Hom(-, S)` on all of `Sch` is
> `...RelativeProjQcohSheaf.Fd.functor` together with the projection `Fd.toBase`.

```lean
def Fd.overFunctor : (Over S)ᵒᵖ ⥤ Type (u + 1)
```

**`Stacks.AlgebraicGeometry.RelativeProjQcohSheaf.Quadruple`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjQcohSheaf/Quadruple.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RelativeProjQcohSheaf/Quadruple.lean#L127). The attribute's comment: “quadruples over a test scheme”.

> **Stacks Project, Section 01NS.** A quadruple `(d, f : T → S, L, ψ)` over the test scheme
> `T`: an invertible `𝒪_T`-module `L`, a homomorphism `ψ` of graded `𝒪_T`-algebras from the
> pullback of the `d`-th Veronese regrading of `𝒜` to the Laurent algebra of `L`, and the
> requirement that the degree-one component `f^*𝒜_d ⟶ L` of `ψ` be surjective.
>
> The integer `d` and the morphism `f` are parameters; the pair `(L, ψ)` is the data.

```lean
structure Quadruple (f : T ⟶ S)
    (A : SheafOfModules.GradedAlgebra.{u, u} (structureRingSheaf S.toRingedSpace)) (d : ℤ)
```

**`Stacks.AlgebraicGeometry.RelativeProjQcohSheaf.Quadruple.StrictlyEquivalent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjQcohSheaf/Quadruple.lean, line 189](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RelativeProjQcohSheaf/Quadruple.lean#L189). The attribute's comment: “strict equivalence of quadruples”.

> **Stacks Project, Section 01NS.** Two quadruples over the same morphism `f` are *strictly
> equivalent* when there is an isomorphism `β : L ≅ L'` of their invertible modules with
> `β ∘ ψ = ψ'`.
>
> The composite `β ∘ ψ` is spelled through the isomorphism `γ` of Laurent algebras induced by `β`:
> the condition is that `γ` be an isomorphism of sheaves of graded algebras whose degree-one
> component is `β` and which carries `ψ` to `ψ'` in every degree.

```lean
def StrictlyEquivalent (P Q : Quadruple f A d) : Prop
```

**`Stacks.AlgebraicGeometry.RelativeProjQcohSheaf.Quadruple.strictlyEquivalent_equivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjQcohSheaf/Quadruple.lean, line 214](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RelativeProjQcohSheaf/Quadruple.lean#L214). The attribute's comment: “strict equivalence of quadruples”.

> **Strict equivalence of quadruples is an equivalence relation.**

```lean
theorem strictlyEquivalent_equivalence :
    Equivalence (StrictlyEquivalent (f := f) (A := A) (d := d))
```

**`Stacks.AlgebraicGeometry.RelativeProjQcohSheaf.Fd`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjQcohSheaf/Quadruple.lean, line 267](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RelativeProjQcohSheaf/Quadruple.lean#L267). The attribute's comment: “the set of strict equivalence classes of quadruples over a test scheme”.

> **Stacks Project, Section 01NS.** The set `F_d(T)` of strict equivalence classes of
> quadruples `(d, f : T → S, L, ψ)` over the test scheme `T`.
>
> Strict equivalence relates only quadruples over the same morphism `f : T ⟶ S`, so the set of
> classes is fibred over the morphisms `T ⟶ S`, which is the morphism recorded by a quadruple.

```lean
def Fd (A : SheafOfModules.GradedAlgebra.{u, u} (structureRingSheaf S.toRingedSpace)) (d : ℤ)
    (T : Scheme.{u}) : Type (u + 1)
```

**`Stacks.AlgebraicGeometry.RelativeProjQcohSheaf.Quadruple.strictlyEquivalent_pullback_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjQcohSheaf/UnionFunctor.lean, line 334](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RelativeProjQcohSheaf/UnionFunctor.lean#L334). The attribute's comment: “the pullback of a quadruple along the identity morphism of the test scheme is strictly equivalent to the quadruple”.

> The pullback of a quadruple along an identity is strictly equivalent to the quadruple.

```lean
theorem strictlyEquivalent_pullback_id (P : Quadruple f A d) :
    StrictlyEquivalent (P.pullback (𝟙 T)) P
```

**`Stacks.AlgebraicGeometry.RelativeProjQcohSheaf.Quadruple.strictlyEquivalent_pullback_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjQcohSheaf/UnionFunctor.lean, line 343](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RelativeProjQcohSheaf/UnionFunctor.lean#L343). The attribute's comment: “the pullback of a quadruple along a composite of morphisms of test schemes is strictly equivalent to the twice-pulled-back quadruple”.

> The pullback of a quadruple along a composite of morphisms of test schemes is strictly
> equivalent to the twice-pulled-back quadruple.

```lean
theorem strictlyEquivalent_pullback_comp (P : Quadruple f A d) (g : T' ⟶ T) (g' : T'' ⟶ T') :
    StrictlyEquivalent ((P.pullback g).pullback g') (P.pullback (g' ≫ g))
```

**`Stacks.AlgebraicGeometry.RelativeProjQcohSheaf.Fd.functor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjQcohSheaf/UnionFunctor.lean, line 375](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RelativeProjQcohSheaf/UnionFunctor.lean#L375). The attribute's comment: “the functor F\_d : Sch^opp -> Sets at a fixed degree d, with both functor laws proved (Fd.pullback\_id and Fd.pullback\_comp): on objects the set F\_d(T) of strict equivalence classes of quadruples of degree d, on morphisms the pullback of a quadruple. Representability of F\_d by a scheme is Tag 01NV and is not proved here”.

> The functor `F_d : Sch^{opp} ⟶ Sets` at a fixed degree `d`. It sends a test scheme `T` to the
> set `F_d(T)` of strict equivalence classes of quadruples `(d, f : T → S, L, ψ)` of degree `d`, and
> a morphism `g : T' ⟶ T` of test schemes to the map sending the class of a quadruple to the class
> of its pullback along `g`.

```lean
def Fd.functor (A : SheafOfModules.GradedAlgebra.{u, u} (structureRingSheaf S.toRingedSpace))
    (d : ℤ) : Scheme.{u}ᵒᵖ ⥤ Type (u + 1)
```

**`Stacks.AlgebraicGeometry.RelativeProjQcohSheaf.Quadruple.StrictlyEquivalent.pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjQcohSheaf/UnionPullback.lean, line 528](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RelativeProjQcohSheaf/UnionPullback.lean#L528). The attribute's comment: “the pullback of a quadruple along a morphism of test schemes respects strict equivalence”.

> **Stacks Project, Section 01NS: the pullback of a quadruple respects strict equivalence.**
> Strict equivalence is witnessed by an isomorphism of the Laurent algebras carrying `ψ` to `ψ'`;
> `laurentPullbackIso` carries that witness to one for the pullbacks, and
> `Twisting.pullbackApp_comp_laurentTransport_of_app` is the compatibility with `ψ`.

```lean
theorem StrictlyEquivalent.pullback {P Q : Quadruple f A d} (h : StrictlyEquivalent P Q)
    (g : T' ⟶ T) : StrictlyEquivalent (P.pullback g) (Q.pullback g)
```

**`Stacks.AlgebraicGeometry.RelativeProjQcohSheaf.Quadruple.Equivalent.pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjQcohSheaf/UnionPullback.lean, line 559](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RelativeProjQcohSheaf/UnionPullback.lean#L559). The attribute's comment: “the pullback of a quadruple along a morphism of test schemes respects equivalence of quadruples of possibly different degrees”.

> **Stacks Project, Section 01NS: the pullback of a quadruple respects equivalence of quadruples
> of possibly different degrees.** Equivalence is the comparison at the common multiple `d d'` of the
> two degrees, and the pullback leaves both degrees unchanged.

```lean
theorem Equivalent.pullback {P : Quadruple f A d} {Q : Quadruple f A d'} (h : Equivalent P Q)
    (g : T' ⟶ T) : Equivalent (P.pullback g) (Q.pullback g)
```

**`Stacks.AlgebraicGeometry.RelativeProjQcohSheaf.Fd.pullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjQcohSheaf/UnionPullback.lean, line 575](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RelativeProjQcohSheaf/UnionPullback.lean#L575). The attribute's comment: “the map F\_d(T) → F\_d(T') of a morphism of test schemes at a fixed degree d, the pullback of a quadruple descended to the strict equivalence classes”.

> **Stacks Project, Section 01NS: the map `F_d(T) → F_d(T')` of a morphism `g : T' ⟶ T` of test
> schemes**, at a fixed degree `d`. A point of `F_d(T)` over `f : T ⟶ S` is a quadruple of degree
> `d` over `f` taken modulo strict equivalence; its image is the pullback of that quadruple, again
> of degree `d`, over `g ≫ f`. This is well defined because the pullback respects strict
> equivalence (`Quadruple.StrictlyEquivalent.pullback`), and no identification across degrees is
> involved.

```lean
def Fd.pullback {A : SheafOfModules.GradedAlgebra.{u, u} (structureRingSheaf S.toRingedSpace)}
    {d : ℤ} (g : T' ⟶ T) (ξ : Fd A d T) : Fd A d T'
```

## Tag 01NT, a lemma

[Tag 01NT](https://stacks.math.columbia.edu/tag/01NT) in the Stacks Project.

**`Stacks.AlgebraicGeometry.RelativeProjQcohSheaf.Fd.baseChangePullbackIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjQcohSheaf/BaseChangeFunctor.lean, line 936](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RelativeProjQcohSheaf/BaseChangeFunctor.lean#L936). The attribute's comment: “the canonical isomorphism F'\_d = h\_\{S'} x\_\{h\_S} F\_d of functors on Sch^opp read off at the categorical fibre product, with its compatibility with both projections (baseChangePullbackIso\_hom\_fst and \_hom\_snd), so that it is the canonical isomorphism and not merely some isomorphism. Stated for every integer d”.

> **Stacks Project, Tag 01NT: the canonical isomorphism `F'_d ≅ h_{S'} ×_{h_S} F_d`**, with the
> right-hand side the categorical fibre product of the cospan `h_{S'} ⟶ h_S ⟵ F_d` in the functor
> category. It is canonical: `Fd.baseChangePullbackIso_hom_fst` and `..._hom_snd` identify its
> composites with the two projections as the projection of `F'_d` to the functor of points of `S'`
> and the canonical map `F'_d ⟹ F_d`.

```lean
def Fd.baseChangePullbackIso :
    Fd.functor (baseAlgebra g A) d ≅
      Limits.pullback (yonedaBaseMap g) (Fd.toBase A d)
```

## Tag 01NU, a lemma

[Tag 01NU](https://stacks.math.columbia.edu/tag/01NU) in the Stacks Project.

**`Stacks.AlgebraicGeometry.RelativeProjQcohSheaf.Fd.representableByDegreeOpen`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjQcohSheaf/AffineFdRepresentable.lean, line 361](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RelativeProjQcohSheaf/AffineFdRepresentable.lean#L361). The attribute's comment: “THE TAG, for an AFFINE base: for S affine, A with quasi-coherent homogeneous pieces (Situation 01NN) and d >= 1, the functor F\_d of strict equivalence classes of quadruples of Section 01NS is REPRESENTABLE by the open U\_d of Equation 27.12.0.1 inside Proj Gamma(S, A) a CategoryTheory.Functor.RepresentableBy for Fd.functor, i.e. the bijections Quadruple.fdEquiv together with their naturality in the test scheme (Quadruple.classifyingHomOfClass\_pullback, which rests on the unconditional veroneseSections\_pullback).”.

> **Stacks Project, Tag 01NU: the functor `F_d` of Section 01NS is represented by the open
> `U_d ⊆ Proj Γ(S, 𝒜)` of Equation 27.12.0.1.** Let `S` be affine, `𝒜` a graded `𝒪_S`-algebra with
> quasi-coherent homogeneous pieces (Situation 01NN) and `d ≥ 1`. The bijections
> `...RelativeProjQcohSheaf.Quadruple.fdEquiv` of
> `StacksFrontier/AlgebraicGeometry/RelativeProjQcohSheaf/AffineQuadrupleBijection.lean`, one for each
> test scheme, form a natural isomorphism `Mor(−, U_d) ≅ F_d`: the naturality clause is
> `Quadruple.classifyingHomOfClass_pullback`, transported across the bijection.
>
> The hypotheses are exactly `IsAffine S`, the quasi-coherence of the homogeneous pieces, and
> `0 < d`; the naturality statements the proof rests on are unconditional.

```lean
public def Fd.representableByDegreeOpen [IsAffine S] (hk : 0 < k)
    (hqc : ∀ n : ℤ, ((situationAlgebra B).piece n).IsQuasicoherent) :
    (Fd.functor (situationAlgebra B) (k : ℤ)).RepresentableBy
      (degreeOpen (B.grading (⊤ : S.Opens)) k).toScheme
```

## Tag 01NV, a lemma

[Tag 01NV](https://stacks.math.columbia.edu/tag/01NV) in the Stacks Project.

**`Stacks.AlgebraicGeometry.RelativeProjQcohSheaf.Fd.exists_representableBy_functor_of_pos`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjQcohSheaf/AffineOpenCharts.lean, line 515](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RelativeProjQcohSheaf/AffineOpenCharts.lean#L515). The attribute's comment: “THE TAG, UNCONDITIONALLY: for S a scheme, A a quasi-coherent graded O\_S-algebra (Situation 01NN) and d = k with 0 < k, the functor F\_d of Section 01NS is representable by a scheme over S. The conclusion is about Fd.functor, the genuine functor whose restriction maps are the pullback of a quadruple, and it records that the representing morphism composed with p : Y -> S is the class's own morphism to S.”.

> **Stacks Project, Tag 01NV.** Let `S` be a scheme, `𝒜` a quasi-coherent graded
> `𝒪_S`-algebra (Situation 01NN) and `d ≥ 1`. The functor `F_d` of Section 01NS is representable
> by a scheme over `S`: there are a scheme `Y`, a morphism `p : Y ⟶ S` and a representation of
> `F_d` by `Y` under which the morphism `T ⟶ Y` representing a class `ξ ∈ F_d(T)`, composed with
> `p`, is the morphism `T ⟶ S` recorded by `ξ`.

```lean
theorem Fd.exists_representableBy_functor_of_pos :
    ∃ (Y : Scheme.{u}) (p : Y ⟶ S)
      (e : (Fd.functor (situationAlgebra A) (k : ℤ)).RepresentableBy Y),
      ∀ (T : Scheme.{u}) (ξ : Fd (situationAlgebra A) (k : ℤ) T),
        e.homEquiv.symm ξ ≫ p = ξ.1
```

## Tag 01NW, a lemma

[Tag 01NW](https://stacks.math.columbia.edu/tag/01NW) in the Stacks Project.

**`Stacks.AlgebraicGeometry.RelativeProjQcohSheaf.Quadruple.tfae_compatibleAt_lcm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjQcohSheaf/EquivalenceDescent.lean, line 954](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RelativeProjQcohSheaf/EquivalenceDescent.lean#L954). The attribute's comment: “for two quadruples over the same morphism with positive degrees d and d', and the least common multiple m of d and d' written as m = a d = a' d', these three conditions are equivalent: compatibility at the cofactors (a, a') of the least common multiple; equivalence of the two quadruples, i.e. compatibility at (d', d); and compatibility at the cofactors of some positive common multiple of the two degrees”.

> **[Stacks, Tag 01NW].** In Situation 01NN, let `T` be a scheme and let `(d, f, L, ψ)` and
> `(d', f, L', ψ')` be two quadruples over `T` with `d` and `d'` positive, and write the least
> common multiple `m` of `d` and `d'` as `m = a₀ d = a₀' d'`. Then the following three conditions
> are equivalent:
>
> 1. the two quadruples are compatible at `(a₀, a₀')`, that is, there is an isomorphism
>    `β : L^{⊗ a₀} ⟶ (L')^{⊗ a₀'}` for which `β ∘ ψ|_{f^*𝒜^{(m)}}` and `ψ'|_{f^*𝒜^{(m)}}` agree as
>    graded ring maps;
> 2. the two quadruples are equivalent, that is, compatible at `(d', d)`;
> 3. the two quadruples are compatible at `(a, a')` for some positive common multiple
>    `m = a d = a' d'` of their degrees.
>
> The source's remaining clause `f = f'` is not a separate condition here: both quadruples are
> taken over the same morphism `f : T ⟶ S`, which is a parameter of the type `Quadruple f 𝒜 d`,
> so the two morphisms are equal by construction in all three conditions.
>
> The five implications of the cycle are the five declarations above and in
> `StacksFrontier.AlgebraicGeometry.RelativeProjQcohSheaf.Equivalence`:
> `equivalent_of_lcm_compatible`, `exists_compatible_of_equivalent`,
> `lcm_compatible_of_exists_compatible`, `lcm_compatible_of_equivalent` and
> `equivalent_of_exists_compatible`.

```lean
theorem tfae_compatibleAt_lcm (hd : 0 < d) (hd' : 0 < d') {a₀ a₀' : ℤ}
    (ha₀ : (Int.lcm d d' : ℤ) = a₀ * d) (ha₀' : (Int.lcm d d' : ℤ) = a₀' * d') :
    List.TFAE
      [CompatibleAt P Q a₀ a₀',
        Equivalent P Q,
        ∃ m a a' : ℤ, 0 < m ∧ m = a * d ∧ m = a' * d' ∧ CompatibleAt P Q a a']
```

## Tag 01NX, an equation

[Tag 01NX](https://stacks.math.columbia.edu/tag/01NX) in the Stacks Project.

**`Stacks.AlgebraicGeometry.RelativeProjQcohSheaf.F.limFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjQcohSheaf/UnionRepresentable.lean, line 150](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RelativeProjQcohSheaf/UnionRepresentable.lean#L150). The attribute's comment: “the functor F of the display for EVERY test scheme, which closes the second qualification recorded on F.functor: the source defines F(T) as the union over d >= 1 of the F\_d(T) only for a quasi- compact T and as the inverse limit of those over the quasi-compact opens of T in general, and that inverse limit, previously NOT CONSTRUCTED, is this functor. Both functor laws come from AlgebraicGeometry.Scheme.QcExtension.pullback\_id and pullback\_comp; F.limEquiv is the identification with the union on a quasi-compact test scheme, and AlgebraicGeometry.Scheme.QcExtension.equivQcOpen the identification of the index used here (all morphisms out of quasi-compact schemes, which makes the functoriality in T a reindexing) with the quasi-compact opens of T that the source indexes by. The FIRST qualification recorded on F.functor is DISCHARGED and is NOT inherited: the value of this functor on a quasi-compact test scheme is the source's F(T) itself, not a quotient of it. UnionRel IS an equivalence relation, being cofinal equality ...UnionEquivalenceRelation.unionRel\_iff\_cofinallyEqual and ...UnionEquivalenceRelation.unionRel\_equivalence so two quadruples of positive degree have the same point of F(T) EXACTLY when they are equivalent (...UnionEquivalenceRelation.F.mk\_eq\_mk\_iff\_equivalent, and ...UnionEquivalenceRelation.F.mk\_eq\_mk\_iff\_strictlyEquivalent when the two degrees agree). The brick that had been missing was NOT the implication (3) => (1) of Tag 01NW, which was already proved as ...EquivalenceDescent.Quadruple.lcm\_compatible\_of\_exists\_compatible, but the converse of ...PowerTransitionColimit.Quadruple.strictlyEquivalent\_scale\_of\_compatibleAt, namely ...UnionEquivalenceRelation.Quadruple.compatibleAt\_of\_strictlyEquivalent\_scale; neither Tag 01NB nor Tag 01NU is used for it.”.

> **Stacks Project, display 01NX, on all of `Sch`.** The functor sending a test scheme `T` to
> the union `F(T) = ⋃_{d ≥ 1} F_d(T)` when `T` is quasi-compact, and to the inverse limit of those
> unions over the quasi-compact opens of `T` in general.
>
> It is the quasi-compact extension `AlgebraicGeometry.Scheme.QcExtension.functor` of
> `F.functor`, the union taken at every test scheme; `F.limEquiv` says the two agree on a
> quasi-compact test scheme, and `AlgebraicGeometry.Scheme.QcExtension.equivQcOpen` that the
> extension is the limit over the quasi-compact opens the source writes.

```lean
def F.limFunctor (A : SheafOfModules.GradedAlgebra.{u, u} (structureRingSheaf S.toRingedSpace)) :
    Scheme.{u}ᵒᵖ ⥤ Type (u + 1)
```

## Tag 01NY, a lemma

[Tag 01NY](https://stacks.math.columbia.edu/tag/01NY) in the Stacks Project.

**`Stacks.AlgebraicGeometry.RelativeProjQcohSheaf.F.isRepresentable_limFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjQcohSheaf/RelativeProjRepresents.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RelativeProjQcohSheaf/RelativeProjRepresents.lean#L104). The attribute's comment: “the tag's sentence in one statement, with no datum beyond the scheme and the graded algebra: the functor F of the display 01NX is representable by a scheme, the representing scheme being the constructed relative homogeneous spectrum Proj\_S(A)”.

> **[Stacks, Tag 01NY].** In Situation 01NN — a scheme `S` and a quasi-coherent graded
> `𝒪_S`-algebra `𝒜` — the functor `F` of the display 01NX is representable by a scheme.
>
> This is the tag's sentence itself, with no datum quantified over beyond `S` and `𝒜`: the
> representing scheme is `Proj_S(𝒜)` of [Stacks, Tag 01NQ], and the representation is
> `F.representableByRelativeProjOfCharts` at that scheme. The functor is `F.limFunctor`, the
> display on *every* test scheme — the union over `d ≥ 1` of the `F_d` on a quasi-compact one and
> the inverse limit of those over the quasi-compact opens in general — so the statement is about
> the source's `F` and not about one `F_d`.
>
> The sibling `F.representableByRelativeProjOfCharts` is the sharper form, naming the representing
> scheme and allowing it to be an arbitrary relative homogeneous spectrum of `𝒜`; this is the bare
> existential the tag states. Nothing is assumed beyond Situation 01NN, which `𝒜` carries.

```lean
theorem F.isRepresentable_limFunctor :
    (F.limFunctor (situationAlgebra A)).IsRepresentable
```

## Tag 01NZ, a lemma

[Tag 01NZ](https://stacks.math.columbia.edu/tag/01NZ) in the Stacks Project.

**`Stacks.AlgebraicGeometry.RelativeProjQcohSheaf.representableBy_and_existsUnique_isoOver`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjQcohSheaf/RelativeProjRepresents.lean, line 177](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RelativeProjQcohSheaf/RelativeProjRepresents.lean#L177). The attribute's comment: “for a scheme S and a quasi-coherent graded O\_S-algebra A (Situation 01NN) and any scheme over S carrying projective-spectrum charts on the affine opens of S, the constructed relative homogeneous spectrum Proj\_S(A) represents the functor F.limFunctor of the display 01NX, and there is exactly one isomorphism from Proj\_S(A) to that scheme compatible with the charts, which is an isomorphism over S”.

> **[Stacks, Tag 01NZ].** In Situation 01NN, let `P` be any scheme over `S` carrying
> projective-spectrum charts on the affine opens of `S` — for instance the scheme representing the
> functor `F`, which is such a datum by the source's *"over each affine open of `S` we can identify
> `X` with the homogeneous spectrum of the sections of `𝒜` over that open"*. Then
>
> 1. the relative homogeneous spectrum `π : Proj_S(𝒜) → S` of [Stacks, Tag 01NQ] represents `F`,
>    and
> 2. there is exactly one isomorphism `Proj_S(𝒜) ≅ P` compatible with the charts, and it is an
>    isomorphism over `S`.
>
> Together these say that `Proj_S(𝒜)` and the scheme representing `F` are canonically isomorphic
> as schemes over `S`, which is the source's statement: the first assertion identifies `Proj_S(𝒜)`
> as a representing object and the second produces the canonical comparison with any other
> chart-carrying scheme over `S`, uniquely.
>
> The first assertion is a representation, hence data rather than a proposition, so the two are
> packaged by `PProd` rather than `And`. The chart datum `P` is the only binder beyond Situation
> 01NN, and it is data the statement needs in order to speak of the second scheme at all; it is not
> a hypothesis of the source, since `relativeProj A` is itself a `RelativeProjData A` and so is
> every projective bundle of `...SheafSymmetricAlgebra`.
>
> The two assertions are `relativeProjRepresentableByFunctorUnconditional` of this file and
> `...RelativeProjQcohSheaf.existsUnique_isoOver` of
> `StacksFrontier.AlgebraicGeometry.RelativeProjQcohSheaf.GluedRepresents`.

```lean
def representableBy_and_existsUnique_isoOver (P : RelativeProjData A) :
    PProd ((F.limFunctor (situationAlgebra A)).RepresentableBy (relativeProj A).scheme)
      (∃! e : (relativeProj A).scheme ≅ P.scheme,
        (∀ U : S.affineOpens, (relativeProj A).chart U.1 U.2 ≫ e.hom = P.chart U.1 U.2) ∧
          e.hom ≫ P.toBase = (relativeProj A).toBase)
```

## Tag 01O0, a definition

[Tag 01O0](https://stacks.math.columbia.edu/tag/01O0) in the Stacks Project.

**`Stacks.AlgebraicGeometry.RelativeProj.relativeHomogeneousSpectrum`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProj/Spectrum.lean, line 87](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RelativeProj/Spectrum.lean#L87). The attribute's comment: “the scheme Proj\_S(A) itself. The tag NAMES the scheme constructed in Lemma 01NQ, which in this repository is the field `scheme` of `Stacks.AlgebraicGeometry.RelativeProj.relativeProj`, a construction (a colimit over the small affine Zariski site of S) and not a choice; the structure morphism pi the tag's last sentence names is `relativeHomogeneousSpectrumToBase`, which carries this tag too. NOT re-asserted here: the tag's reference to the functor F of the display 01NX and to Lemma 01NZ, namely that this scheme REPRESENTS F. The functor F is not constructed in this repository; that representability is carried, with the source's inputs to it, in `...RelativeProjQcohSheaf.RepresentingProjData` and proved there as `...RepresentingProjData.relativeProjRepresentableBy`”. References: EGA II (3.1.3); EGA II (8.3.1).

> The relative homogeneous spectrum `Proj_S(A)`, or relative Proj, of a quasi-coherent sheaf
> of graded `𝒪_S`-algebras `A` over a scheme `S`: the scheme glued from the projective spectra of
> the graded rings of sections of `A` over the affine opens of `S`.

```lean
public def relativeHomogeneousSpectrum : Scheme.{u}
```

**`Stacks.AlgebraicGeometry.RelativeProj.relativeHomogeneousSpectrumToBase`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProj/Spectrum.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RelativeProj/Spectrum.lean#L93). The attribute's comment: “ONLY the structure morphism pi : Proj\_S(A) → S of the tag's last sentence; the scheme itself is `relativeHomogeneousSpectrum`, whose clause string describes the covering set and what the tag's reference to 01NX/01NZ is and where it lives”.

> The structure morphism `π : Proj_S(A) → S` of the relative homogeneous spectrum.

```lean
public def relativeHomogeneousSpectrumToBase :
    relativeHomogeneousSpectrum A ⟶ S
```

## Tag 01O1, a lemma

[Tag 01O1](https://stacks.math.columbia.edu/tag/01O1) in the Stacks Project.

**`Stacks.AlgebraicGeometry.RelativeProjTwistChartBridge.tag01O1`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjTwistChartBridge/ThetaIsomorphism.lean, line 150](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RelativeProjTwistChartBridge/ThetaIsomorphism.lean#L150). The attribute's comment: “for a quadruple (f : T -> S, d, L, psi) with associated morphism r : T -> Proj\_S(A), the morphism the representation of F by Proj\_S(A) attaches to the class of the quadruple: r lies over S, and there is an isomorphism theta of Z-graded O\_T-algebras from r^*((+)\_n O(nd)) to (+)\_n L^(x)n, preserving the unit, with psi = theta o psi\_univ in every degree, and every homomorphism of graded algebras with psi = Theta o psi\_univ is theta”.

> **Stacks Project, Tag 01O1.** In Situation 01NN — `S` a scheme and `𝒜` a quasi-coherent
> graded `𝒪_S`-algebra — let `(f : T → S, d, ℒ, ψ)` be a quadruple of Section 01NS, so `d ≥ 1`, and
> let `r = r_{d, ℒ, ψ} : T → Proj_S(𝒜)` be the associated morphism
> (`...RelativeProjTwistChartBridge.thetaMorphism`: the morphism into `U_d` that the class of the
> quadruple defines, followed by `U_d ⊆ Proj_S(𝒜)`). Write `𝒪(n)` for the twists of `Proj_S(𝒜)`
> with their homogeneous-section map `ψ_univ` (`...GluedTwistAlgebra.twistDataOfGradedAlgebra`).
> Then
>
> 1. `r` is the morphism the representability of `F` attaches to the quadruple: the image of its
>    class in `F(T)` under the representation
>    `...RelativeProjQcohSheaf.relativeProjRepresentableByFunctorUnconditional` of the functor `F`
>    of the display 01NX by `Proj_S(𝒜)`, which is the representation of [Stacks, Tag 01NZ];
> 2. `r` is a morphism over `S`;
> 3. there is an isomorphism of sheaves of `ℤ`-graded `𝒪_T`-algebras
>    `θ : r^*(⨁_{n ∈ ℤ} 𝒪(nd)) ≅ ⨁_{n ∈ ℤ} ℒ^{⊗ n}`, which preserves the unit;
> 4. the triangle commutes: `ψ = θ ∘ ψ_univ` in every degree, the maps out of
>    `𝒜^{(d)}` being read through the adjunction `f^* ⊣ f_*`, so that `ψ_univ` becomes
>    `...RelativeProjTwists.TwistData.psiLegVeronese`; and
> 5. the triangle determines `θ`: any homomorphism of graded algebras
>    `r^*(⨁_n 𝒪(nd)) ⟶ ⨁_n ℒ^{⊗ n}` making it commute is `θ`.

```lean
theorem tag01O1 (hd : 0 < d) (P : Quadruple f (situationAlgebra A) (d : ℤ)) :
    thetaMorphism hd P =
        (relativeProjRepresentableByFunctorUnconditional A).homEquiv.symm
          (RelativeProjInvertibleMorphism.F.toLim A (F.mk f (by exact_mod_cast hd) P)) ∧
    thetaMorphism hd P ≫ (relativeProj A).toBase = f ∧
      ∃ θ : pullbackTwistVeronese (GluedTwistAlgebra.twistDataOfGradedAlgebra A) (d : ℤ)
          (thetaMorphism hd P) ≅ laurent P.L,
        SheafOfModules.GradedAlgebra.oneHom
              (pullbackTwistVeronese (GluedTwistAlgebra.twistDataOfGradedAlgebra A) (d : ℤ)
                (thetaMorphism hd P)) ≫ θ.hom.app 0 =
            SheafOfModules.GradedAlgebra.oneHom (laurent P.L) ∧
          (∀ n : ℤ, (GluedTwistAlgebra.twistDataOfGradedAlgebra A).psiLegVeronese
              (thetaMorphism hd P) (thetaMorphism_comp_toBase hd P) (d : ℤ) n ≫ θ.hom.app n =
                P.twisting.app n) ∧
          ∀ Θ : pullbackTwistVeronese (GluedTwistAlgebra.twistDataOfGradedAlgebra A) (d : ℤ)
              (thetaMorphism hd P) ⟶ laurent P.L,
            (∀ n : ℤ, (GluedTwistAlgebra.twistDataOfGradedAlgebra A).psiLegVeronese
              (thetaMorphism hd P) (thetaMorphism_comp_toBase hd P) (d : ℤ) n ≫ Θ.app n =
                P.twisting.app n) → Θ = θ.hom
```

## Tag 01O2, a lemma

[Tag 01O2](https://stacks.math.columbia.edu/tag/01O2) in the Stacks Project.

**`Stacks.RelativeProj.Data.isSeparated_toBase`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/TerminalRelativeProj.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Blowup/TerminalRelativeProj.lean#L125). The attribute's comment: “the gluing-datum form”. References: EGA II (2.4.2); EGA II (3.1.3), “separated over Y”; EGA II (8.14.1), “more general”.

> **Stacks Project, Tag 01O2.** The structure morphism of a relative `Proj` is separated.
>
> Separatedness is local on the target, so it suffices to check it over the affine opens of the
> base; over an affine open `U` the preimage is the chart `Proj (𝒜 U)`, a separated scheme, and a
> morphism out of a separated scheme is separated.

```lean
instance isSeparated_toBase (d : Data 𝒜) : IsSeparated d.toBase
```

**`Stacks.RelativeProj.Situation.isSeparated_relativeProjToBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BlowUpSeparatedInput/Basic.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/BlowUpSeparatedInput/Basic.lean#L98). References: EGA II (3.1.3), “separated over Y”; EGA II (8.14.1).

> **Stacks Project, Tag 01O2.** The structure morphism of the relative `Proj` of a
> quasi-coherent, commutative, nonnegatively graded algebra on a scheme is separated.
>
> Separatedness is local at the target, and over an affine open `W` of the base the restriction of
> `relativeProjToBase` is the chart structure morphism `Proj Γ(W, 𝒜) ⟶ W`, because both are
> pullbacks of `relativeProjToBase` along `W.ι`.

```lean
public theorem _root_.Stacks.RelativeProj.Situation.isSeparated_relativeProjToBase
    (s : Stacks.RelativeProj.Situation.{u}) :
    IsSeparated (Stacks.RelativeProj.Situation.relativeProjToBase s)
```

## Tag 01O3, a lemma

[Tag 01O3](https://stacks.math.columbia.edu/tag/01O3) in the Stacks Project.

**`Stacks.AlgebraicGeometry.RelativeProjBaseChangeTwist.relativeProj_baseChange_twist`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjBaseChangeTwist/Theta.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RelativeProjBaseChangeTwist/Theta.lean#L74). The attribute's comment: “the canonical isomorphism r : Proj\_S'(g^*A) -> S' x\_S Proj\_S(A) over S', and the isomorphism theta : r^* pr\_2^* ((+)\_d O(d)) -> (+)\_d O\_\{Proj\_S'(g^*A)}(d) of Z-graded algebras, preserving the unit”.

> **Stacks Project, Tag 01O3.** Let `S` be a scheme, `A` a quasi-coherent sheaf of graded
> `𝒪_S`-algebras and `g : S' → S` a morphism of schemes. The canonical isomorphism
> `r : Proj_{S'}(g^*A) ≅ S' ×_S Proj_S(A)` (`baseChangeIso`) lies over `S'` and has second
> component the base change `Proj_{S'}(g^*A) → Proj_S(A)`, and `θ` (`baseChangeTheta`) is an
> isomorphism of `ℤ`-graded algebras
> `r^* pr₂^* (⨁_d 𝒪_{Proj_S(A)}(d)) ≅ ⨁_d 𝒪_{Proj_{S'}(g^*A)}(d)`, which preserves the unit.

```lean
theorem relativeProj_baseChange_twist :
    (baseChangeIso A g).hom ≫
          pullback.fst g (Stacks.AlgebraicGeometry.RelativeProj.relativeProj A).toBase =
        (Stacks.AlgebraicGeometry.RelativeProj.relativeProj (A.pullback g)).toBase ∧
      (baseChangeIso A g).hom ≫
          pullback.snd g (Stacks.AlgebraicGeometry.RelativeProj.relativeProj A).toBase =
        baseChangeHom A g ∧
      ∀ U, ((baseChangeTheta A g).hom.app 0).val.app U
          ((pbAlgS (baseChangeIso A g).hom
            (Stacks.RingedSpace.pullbackGradedAlgebra
              (pullback.snd g
                (Stacks.AlgebraicGeometry.RelativeProj.relativeProj A).toBase).toLRSHom.toShHom
              (twistAlgebra A))).one.eval U) =
        (twistAlgebra (A.pullback g)).one.eval U
```

**`Stacks.RelativeProj.Situation.twistSheafPullbackIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/ModuleGlueing/RelativeProjTwistBaseChangeGlued.lean, line 455](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/ModuleGlueing/RelativeProjTwistBaseChangeGlued.lean#L455). The attribute's comment: “the graded isomorphism θ on the twisting sheaves, in each degree separately, as clause (3) of Tag 01N2 is carried with the same reading”. References: EGA II (2.8.10), “partial”; EGA II (2.8.11), “more general”; EGA II (4.1.3), “more general”.

> **The twist assertion of [Stacks, Tag 01O3].** For a morphism `g : S' ⟶ S`, relative `Proj`
> situations `s` over `S` and `s'` over `S'`, and an identification `Φ` of the graded algebra of
> `s'` with the pullback along `g` of that of `s`, degreewise invertible, the base-change morphism
> `r : Proj_{S'}(g^*𝒜) ⟶ Proj_S(𝒜)` carries the `n`-th twisting sheaf to the `n`-th twisting sheaf:
>
> `θ n : r^* 𝒪_{Proj_S(𝒜)}(n) ≅ 𝒪_{Proj_{S'}(g^*𝒜)}(n)`,
>
> for every `n : ℤ` and with no hypothesis beyond the two situations and the datum `Φ`.
>
> The scheme half of the tag — the isomorphism `r` itself, and the cartesian square — is
> `Stacks.RelativeProj.Situation.relativeProjBaseChangeIso` and
> `isPullback_relativeProjBaseChange`.
>
> Multiplicativity of `θ` is not proved: this is the degreewise isomorphism, exactly as clause (3)
> of Tag 01N2 is carried by `Stacks.ProjBaseChange.isIso_twistMap_includeRight` with the same
> restriction.

```lean
public def twistSheafPullbackIso :
    (Scheme.Modules.pullback (relativeProjBaseChange g Φ hΦ)).obj (twistSheaf s n)
      ≅ twistSheaf s' n
```

## Tag 01O4, a lemma

[Tag 01O4](https://stacks.math.columbia.edu/tag/01O4) in the Stacks Project.

**`Stacks.AlgebraicGeometry.TwistMapsInvertible.f1Bundle_and_twists`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TwistMapsInvertible/RepresentsAndTwists.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/TwistMapsInvertible/RepresentsAndTwists.lean#L95). The attribute's comment: “for a scheme S and a quasi-coherent sheaf of graded O\_S-modules A generated as an A\_0-algebra by A\_1, three things hold of X = Proj\_S(A): X represents the functor F\_1 sending f : T -> S to the strict isomorphism classes of pairs (L, psi) with L an invertible O\_T-module and psi : f^*A -> ⨁\_\{n >= 0} L^\{⊗ n} a graded algebra homomorphism whose degree-one component f^*A\_1 -> L is surjective, by bijections normalised at the identity of X and natural in the test scheme; every homogeneous piece O\_X(n) of the canonical twist datum on X is an invertible O\_X-module; and the multiplication maps O\_X(n) (x) O\_X(m) -> O\_X(n+m) are isomorphisms in all integer degrees”.

> **[Stacks, Tag 01O4].** Let `S` be a scheme and `𝒜` a quasi-coherent sheaf of graded
> `𝒪_S`-modules generated as an `𝒜_0`-algebra by `𝒜_1`. Then, for `X = Proj_S(𝒜)`:
>
> 1. `X` represents the functor `F_1` of pairs `(L, ψ)` with `L` invertible and `f^*𝒜_1 ⟶ L`
>    surjective, up to strict equivalence — the bijections between the morphisms `T ⟶ X` over `S`
>    and the strict isomorphism classes of such pairs, normalised at the identity of `X` and
>    natural in the test scheme;
> 2. every homogeneous piece `𝒪_X(n)` of the canonical twist datum on `X` is an invertible
>    `𝒪_X`-module; and
> 3. the multiplication maps `𝒪_X(n) ⊗ 𝒪_X(m) ⟶ 𝒪_X(n + m)` are isomorphisms in all integer
>    degrees.
>
> The first assertion is a family of bijections, hence data rather than a proposition, so it is
> joined to the other two by `PProd` rather than `And`.
>
> The hypothesis `hgen` is the source's own degree-one generation. The binder `TA` is the choice of
> tensor algebras, which is data the library needs in order to state the first assertion at all,
> and the comparison of its pullbacks is the canonical `tensorAlgebraPullbackIsos`. The twists are
> the canonical twist datum `twistDataOfGradedAlgebra`, constructed from `𝒜` alone.
>
> The three assertions are `...ProjRepresentsF1.f1Bundle`,
> `twistDataOfGradedAlgebra_isInvertible` and `isIso_mulSheaf_twistDataOfGradedAlgebra`.

```lean
def f1Bundle_and_twists {S : Scheme.{u}} (A : SheafGradedAlgebra.{u} S) (TA : TensorAlgebras.{u})
    (hgen : IsGeneratedInDegreeOne A) :
    PProd (F1Bundle A TA (tensorAlgebraPullbackIsos TA))
      ((∀ n : ℤ, AlgebraicGeometry.SheafOfModules.IsInvertible (relativeProj A).scheme.presheaf
            (relativeProj A).scheme.ringCatSheaf.2
            ((twistDataOfGradedAlgebra A).algebra.piece n)) ∧
        ∀ n m : ℤ, IsIso (_root_.SheafOfModules.GradedAlgebra.mulSheaf
          (twistDataOfGradedAlgebra A).algebra n m))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 27.16, Tag 01NS](https://stacks.math.columbia.edu/tag/01NS)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
