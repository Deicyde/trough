---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isIso_smallEtaleProjectionFormulaMap, AlgebraicGeometry.Space.TorIndependent, AlgebraicGeometry.Space.torIndependent_iff_forall_etale_diagram, AlgebraicGeometry.Space.torIndependent_of_isEtale_surjective_diagram, AlgebraicGeometry.Space.exists_isEtale_surjective_diagram_of_torIndependent, AlgebraicGeometry.Space.torIndependent_of_torIndependent_scheme_diagram, AlgebraicGeometry.Space.exists_torIndependent_scheme_diagram_of_torIndependent, AlgebraicGeometry.Space.isIso_smallEtaleDerivedBaseChangeMap_of_torIndependent
statement: formalized
proof: formalized
---

# 75.20 Cohomology and base change, IV

Section 75.20 of the Stacks Project, [Tag 08IM](https://stacks.math.columbia.edu/tag/08IM). 7 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08IN, a lemma

[Tag 08IN](https://stacks.math.columbia.edu/tag/08IN) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_smallEtaleProjectionFormulaMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleProjectionFormulaIso.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleProjectionFormulaIso.lean#L126).

> **Stacks 08IN.**  Let `f : X ⟶ Y` be a quasi-compact and quasi-separated morphism of
> algebraic spaces, `E ∈ D_QCoh(𝒪_X)` and `K ∈ D_QCoh(𝒪_Y)`.  Then the projection formula map
> `Rf_*(E) ⊗^L K ⟶ Rf_*(E ⊗^L Lf^*K)` is an isomorphism.

```lean
theorem isIso_smallEtaleProjectionFormulaMap (hfqc : IsQuasiCompact B S hS f.hom)
    (hfqs : IsQuasiSeparated B S hS f.hom)
    (E : DerivedCategory (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X)))
    (hE : QcohDerived B S hS X E)
    (K : DerivedCategory (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS Y)))
    (hK : QcohDerived B S hS Y K) :
    IsIso (smallEtaleProjectionFormulaMap B S hS f E K)
```

## Tag 08IP, a definition

[Tag 08IP](https://stacks.math.columbia.edu/tag/08IP) in the Stacks Project.

**`AlgebraicGeometry.Space.TorIndependent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/TorIndependence.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/TorIndependence.lean#L58).

> **Stacks 08IP.** Two algebraic spaces are Tor independent over a base when the geometric
> étale local rings at every compatible pair of points are Tor independent
> for the homomorphisms induced on germs by their structure morphisms.

```lean
public def TorIndependent {B : BigFppfSite.{u}} {S : Scheme.{u}}
    {hS : B.Contains S} {F G H : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (_hF : IsAlgebraicSpace B S hS F) (_hG : IsAlgebraicSpace B S hS G)
    (_hH : IsAlgebraicSpace B S hS H)
    (f : F ⟶ H) (g : G ⟶ H) : Prop
```

## Tag 08IQ, a lemma

[Tag 08IQ](https://stacks.math.columbia.edu/tag/08IQ) in the Stacks Project.

**`AlgebraicGeometry.Space.torIndependent_iff_forall_etale_diagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/TorIndependenceEtaleLocal.lean, line 382](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/TorIndependenceEtaleLocal.lean#L382). The attribute's comment: “(1) <=> (2)”.

> **Stacks 08IQ, (1) ⟺ (2).**  Let `X` and `Y` be algebraic spaces over an algebraic space
> `B`.  Then `X` and `Y` are Tor independent over `B` if and only if for every commutative
> diagram
> ```
> U ⟶ W ⟵ V
> ↓    ↓    ↓
> X ⟶ B ⟵ Y
> ```
> with étale vertical arrows, `U` and `V` are Tor independent over `W`.
>
> Condition (3), which asks for a single such diagram in which `W ⟶ B` is surjective and the
> two upper terms are étale surjective over the base changes `X ×_B W` and `Y ×_B W`, is
> equivalent to condition (1): it implies it by
> `AlgebraicGeometry.Space.torIndependent_of_isEtale_surjective_diagram` and follows from it by
> `AlgebraicGeometry.Space.exists_isEtale_surjective_diagram_of_torIndependent`.  Condition (4),
> which reads the conclusion for `U`, `V` and `W` schemes in the sense of Stacks 08IA, that is on
> ordinary local rings, implies condition (1) by
> `AlgebraicGeometry.Space.torIndependent_of_torIndependent_scheme_diagram` in
> `StacksFrontier.AlgebraicGeometry.Spaces.TorIndependenceSchemeComparison`, and follows from
> condition (1) by
> `AlgebraicGeometry.Space.exists_torIndependent_scheme_diagram_of_torIndependent` in
> `StacksFrontier.AlgebraicGeometry.Spaces.TorIndependenceSchemeConverse`.  So the four conditions
> of Stacks 08IQ are equivalent.

```lean
public theorem torIndependent_iff_forall_etale_diagram {Bs X Y : AlgebraicSpaces B S hS}
    (fX : X ⟶ Bs) (gY : Y ⟶ Bs) :
    TorIndependent X.2 Y.2 Bs.2 fX.hom gY.hom ↔
      ∀ (U V W : AlgebraicSpaces B S hS) (a : U ⟶ X) (b : V ⟶ Y) (c : W ⟶ Bs)
        (uw : U ⟶ W) (vw : V ⟶ W), IsEtale B S hS a.hom → IsEtale B S hS b.hom →
        IsEtale B S hS c.hom → uw.hom ≫ c.hom = a.hom ≫ fX.hom →
        vw.hom ≫ c.hom = b.hom ≫ gY.hom → TorIndependent U.2 V.2 W.2 uw.hom vw.hom
```

**`AlgebraicGeometry.Space.torIndependent_of_isEtale_surjective_diagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/TorIndependenceEtaleLocal.lean, line 524](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/TorIndependenceEtaleLocal.lean#L524). The attribute's comment: “(3) => (1)”.

> **Stacks 08IQ, (3) ⟹ (1).**  Let `X` and `Y` be algebraic spaces over an algebraic space
> `Bs`.  Suppose given one commutative diagram
> ```
> U ⟶ W ⟵ V
> ↓    ↓    ↓
> X ⟶ Bs ⟵ Y
> ```
> with étale vertical arrows in which `W ⟶ Bs` is surjective and in which `U` and `V` are étale
> and surjective over the fibre products `X ×_{Bs} W` and `Y ×_{Bs} W`.  If `U` and `V` are Tor
> independent over `W`, then `X` and `Y` are Tor independent over `Bs`.
>
> The two fibre products are presented as arbitrary cartesian squares of the underlying
> presheaves, which is how a fibre product of algebraic spaces is formed.

```lean
public theorem torIndependent_of_isEtale_surjective_diagram
    {Bs X Y U V W PX PY : AlgebraicSpaces B S hS}
    (fX : X ⟶ Bs) (gY : Y ⟶ Bs) (c : W ⟶ Bs)
    (a : U ⟶ X) (uw : U ⟶ W) (b : V ⟶ Y) (vw : V ⟶ W)
    (pX : PX ⟶ X) (pW : PX ⟶ W) (qY : PY ⟶ Y) (qW : PY ⟶ W)
    (u' : U ⟶ PX) (v' : V ⟶ PY)
    (sqX : IsPullback pX.hom pW.hom fX.hom c.hom)
    (sqY : IsPullback qY.hom qW.hom gY.hom c.hom)
    (hu'X : u' ≫ pX = a) (hu'W : u' ≫ pW = uw)
    (hv'Y : v' ≫ qY = b) (hv'W : v' ≫ qW = vw)
    (hcEtale : IsEtale B S hS c.hom) (hcSurj : IsSurjective B S hS c.hom)
    (haEtale : IsEtale B S hS a.hom) (hbEtale : IsEtale B S hS b.hom)
    (huEtale : IsEtale B S hS u'.hom) (huSurj : IsSurjective B S hS u'.hom)
    (hvEtale : IsEtale B S hS v'.hom) (hvSurj : IsSurjective B S hS v'.hom)
    (h : TorIndependent U.2 V.2 W.2 uw.hom vw.hom) :
    TorIndependent X.2 Y.2 Bs.2 fX.hom gY.hom
```

**`AlgebraicGeometry.Space.exists_isEtale_surjective_diagram_of_torIndependent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/TorIndependenceEtaleLocal.lean, line 655](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/TorIndependenceEtaleLocal.lean#L655). The attribute's comment: “(1) => (3)”.

> **Stacks 08IQ, (1) ⟹ (3).**  Let `X` and `Y` be algebraic spaces over an algebraic space
> `Bs` which are Tor independent over `Bs`.  Then there is a commutative diagram
> ```
> U ⟶ W ⟵ V
> ↓    ↓    ↓
> X ⟶ Bs ⟵ Y
> ```
> with étale vertical arrows in which `W ⟶ Bs` is surjective, in which `U` and `V` are étale and
> surjective over the fibre products `X ×_{Bs} W` and `Y ×_{Bs} W`, and in which `U` and `V` are
> Tor independent over `W`: this is the existence asserted by condition (3).
>
> The witness is the diagram of identities, `W = Bs`, `U = X` and `V = Y`, whose two fibre
> products are `X` and `Y` themselves by `CategoryTheory.IsPullback.of_id_fst`; the Tor
> independence asked of the diagram is then the hypothesis on the nose.  The converse implication
> is `AlgebraicGeometry.Space.torIndependent_of_isEtale_surjective_diagram`.

```lean
public theorem exists_isEtale_surjective_diagram_of_torIndependent
    {Bs X Y : AlgebraicSpaces B S hS} (fX : X ⟶ Bs) (gY : Y ⟶ Bs)
    (h : TorIndependent X.2 Y.2 Bs.2 fX.hom gY.hom) :
    ∃ (U V W PX PY : AlgebraicSpaces B S hS) (c : W ⟶ Bs) (a : U ⟶ X) (uw : U ⟶ W)
      (b : V ⟶ Y) (vw : V ⟶ W) (pX : PX ⟶ X) (pW : PX ⟶ W) (qY : PY ⟶ Y) (qW : PY ⟶ W)
      (u' : U ⟶ PX) (v' : V ⟶ PY),
      IsPullback pX.hom pW.hom fX.hom c.hom ∧ IsPullback qY.hom qW.hom gY.hom c.hom ∧
        u' ≫ pX = a ∧ u' ≫ pW = uw ∧ v' ≫ qY = b ∧ v' ≫ qW = vw ∧
        IsEtale B S hS c.hom ∧ IsSurjective B S hS c.hom ∧
        IsEtale B S hS a.hom ∧ IsEtale B S hS b.hom ∧
        IsEtale B S hS u'.hom ∧ IsSurjective B S hS u'.hom ∧
        IsEtale B S hS v'.hom ∧ IsSurjective B S hS v'.hom ∧
        TorIndependent U.2 V.2 W.2 uw.hom vw.hom
```

**`AlgebraicGeometry.Space.torIndependent_of_torIndependent_scheme_diagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/TorIndependenceSchemeComparison.lean, line 595](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/TorIndependenceSchemeComparison.lean#L595). The attribute's comment: “(4) => (1)”.

> **Stacks 08IQ, (4) ⟹ (1).**  Let `X` and `Y` be algebraic spaces over an algebraic space
> `Bs`.  Suppose given one commutative diagram
> ```
> U ⟶ W ⟵ V
> ↓    ↓    ↓
> X ⟶ Bs ⟵ Y
> ```
> in which `U`, `V` and `W` are *schemes*, the vertical arrows are étale, `W ⟶ Bs` is surjective
> and `U` and `V` are étale and surjective over the fibre products `X ×_{Bs} W` and `Y ×_{Bs} W`.
> If `U` and `V` are Tor independent over `W` in the sense of Stacks 08IA, that is on their
> ordinary local rings, then `X` and `Y` are Tor independent over `Bs`.
>
> This is condition (4) of Stacks 08IQ: a diagram as in condition (3) whose three upper terms are
> schemes, with Tor independence read in the sense of Derived Categories of Schemes, Definition
> 08IA.  The passage from the ordinary local rings of the three schemes to the étale local rings
> of the algebraic spaces they represent is
> `AlgebraicGeometry.Space.torIndependent_yoneda_of_torIndependent_scheme`; condition (3) then
> gives condition (1) by
> `AlgebraicGeometry.Space.torIndependent_of_isEtale_surjective_diagram`.

```lean
theorem torIndependent_of_torIndependent_scheme_diagram
    {Bs X Y PX PY : AlgebraicSpaces B S hS} (fX : X ⟶ Bs) (gY : Y ⟶ Bs)
    {U₀ V₀ W₀ : BigFppfOver B S hS}
    (c : yoneda.obj W₀ ⟶ Bs.1) (a : yoneda.obj U₀ ⟶ X.1) (uw : U₀ ⟶ W₀)
    (b : yoneda.obj V₀ ⟶ Y.1) (vw : V₀ ⟶ W₀)
    (pX : PX ⟶ X) (pW : PX.1 ⟶ yoneda.obj W₀) (qY : PY ⟶ Y) (qW : PY.1 ⟶ yoneda.obj W₀)
    (u' : yoneda.obj U₀ ⟶ PX.1) (v' : yoneda.obj V₀ ⟶ PY.1)
    (sqX : IsPullback pX.hom pW fX.hom c) (sqY : IsPullback qY.hom qW gY.hom c)
    (hu'X : u' ≫ pX.hom = a) (hu'W : u' ≫ pW = yoneda.map uw)
    (hv'Y : v' ≫ qY.hom = b) (hv'W : v' ≫ qW = yoneda.map vw)
    (hcEtale : IsEtale B S hS c) (hcSurj : IsSurjective B S hS c)
    (haEtale : IsEtale B S hS a) (hbEtale : IsEtale B S hS b)
    (huEtale : IsEtale B S hS u') (huSurj : IsSurjective B S hS u')
    (hvEtale : IsEtale B S hS v') (hvSurj : IsSurjective B S hS v')
    (h : AlgebraicGeometry.TorIndependent ((BigFppfOver.toScheme B S hS).map uw)
      ((BigFppfOver.toScheme B S hS).map vw)) :
    TorIndependent X.2 Y.2 Bs.2 fX.hom gY.hom
```

**`AlgebraicGeometry.Space.exists_torIndependent_scheme_diagram_of_torIndependent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/TorIndependenceSchemeConverse.lean, line 601](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/TorIndependenceSchemeConverse.lean#L601). The attribute's comment: “(1) => (4)”.

> **Stacks 08IQ, (1) ⟹ (4).**  Let `X` and `Y` be algebraic spaces over an algebraic space
> `Bs` which are Tor independent over `Bs`.  Then there is a commutative diagram
> ```
> U ⟶ W ⟵ V
> ↓    ↓    ↓
> X ⟶ Bs ⟵ Y
> ```
> in which `U`, `V` and `W` are *schemes*, the vertical arrows are étale, `W ⟶ Bs` is surjective,
> `U` and `V` are étale and surjective over the fibre products `X ×_{Bs} W` and `Y ×_{Bs} W`, and
> `U` and `V` are Tor independent over `W` in the sense of Stacks 08IA — that is, on their
> *ordinary* local rings.  This is the existence asserted by condition (4).
>
> The diagram is the atlas tower: a scheme chart `W ⟶ Bs` of the base, then scheme charts of the
> two fibre products, which are algebraic spaces.  Condition (2) of Stacks 08IQ gives Tor
> independence of the étale local rings over that diagram, and
> `AlgebraicGeometry.Space.torIndependent_scheme_of_torIndependent_yoneda` turns it into Tor
> independence of the ordinary local rings.  The converse implication is
> `AlgebraicGeometry.Space.torIndependent_of_torIndependent_scheme_diagram`.

```lean
theorem exists_torIndependent_scheme_diagram_of_torIndependent
    {Bs X Y : AlgebraicSpaces B S hS} (fX : X ⟶ Bs) (gY : Y ⟶ Bs)
    (h : TorIndependent X.2 Y.2 Bs.2 fX.hom gY.hom) :
    ∃ (U₀ V₀ W₀ : BigFppfOver B S hS) (PX PY : AlgebraicSpaces B S hS)
      (c : yoneda.obj W₀ ⟶ Bs.1) (a : yoneda.obj U₀ ⟶ X.1) (uw : U₀ ⟶ W₀)
      (b : yoneda.obj V₀ ⟶ Y.1) (vw : V₀ ⟶ W₀)
      (pX : PX ⟶ X) (pW : PX.1 ⟶ yoneda.obj W₀) (qY : PY ⟶ Y) (qW : PY.1 ⟶ yoneda.obj W₀)
      (u' : yoneda.obj U₀ ⟶ PX.1) (v' : yoneda.obj V₀ ⟶ PY.1),
      IsPullback pX.hom pW fX.hom c ∧ IsPullback qY.hom qW gY.hom c ∧
        u' ≫ pX.hom = a ∧ u' ≫ pW = yoneda.map uw ∧ v' ≫ qY.hom = b ∧
        v' ≫ qW = yoneda.map vw ∧
        IsEtale B S hS c ∧ IsSurjective B S hS c ∧
        IsEtale B S hS a ∧ IsEtale B S hS b ∧
        IsEtale B S hS u' ∧ IsSurjective B S hS u' ∧
        IsEtale B S hS v' ∧ IsSurjective B S hS v' ∧
        AlgebraicGeometry.TorIndependent ((BigFppfOver.toScheme B S hS).map uw)
          ((BigFppfOver.toScheme B S hS).map vw)
```

## Tag 08IR, a lemma

[Tag 08IR](https://stacks.math.columbia.edu/tag/08IR) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_smallEtaleDerivedBaseChangeMap_of_torIndependent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleDerivedTorIndependentBaseChange.lean, line 248](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleDerivedTorIndependentBaseChange.lean#L248).

> **Stacks 08IR.**  Let `g : Y' ⟶ Y` be a morphism of algebraic spaces and `f : X ⟶ Y` a
> quasi-compact and quasi-separated one, with base change `f' : X' ⟶ Y'`, `g' : X' ⟶ X`.  If `X`
> and `Y'` are Tor independent over `Y`, then the base change map
> `Lg^*Rf_*E ⟶ Rf'_*L(g')^*E` is an isomorphism for every `E ∈ D_QCoh(𝒪_X)`.

```lean
theorem isIso_smallEtaleDerivedBaseChangeMap_of_torIndependent (sq : IsPullback g' f' f g)
    (hfqc : IsQuasiCompact B S hS f.hom) (hfqs : IsQuasiSeparated B S hS f.hom)
    (hTor : TorIndependent X.2 Y'.2 Y.2 f.hom g.hom)
    (E : DerivedCategory (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X)))
    (hE : QcohDerived B S hS X E) :
    IsIso (smallEtaleDerivedModuleBaseChangeMap B S hS f g f' g' sq.w E)
```

## Tag 0E4S, a lemma

[Tag 0E4S](https://stacks.math.columbia.edu/tag/0E4S) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_globalDerivedHomBaseChangeMap_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/GlobalDerivedHomBaseChangeIso.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/GlobalDerivedHomBaseChangeIso.lean#L93). The attribute's comment: “case (1): M perfect, K in D_QCoh”.

> **Stacks 0E4S, case (1).** Let `g : S' ⟶ S` be a morphism of affine schemes, `R = Γ(S, 𝒪)`,
> `R' = Γ(S', 𝒪)`, and let `X' = X ×_S S'` for `f : X ⟶ S` quasi-compact and quasi-separated with
> `X` and `S'` Tor independent over `S`. For `M ∈ D(𝒪_X)` perfect and `K ∈ D_QCoh(𝒪_X)` the
> canonical map `RHom_X(M, K) ⊗^L_R R' ⟶ RHom_{X'}(L(g')^*M, L(g')^*K)` is an isomorphism.

```lean
theorem isIso_globalDerivedHomBaseChangeMap_of_isPerfect
    (sq : IsPullback g' f' f (representedSpaceMap B S hS g))
    (hfqc : IsQuasiCompact B S hS f.hom) (hfqs : IsQuasiSeparated B S hS f.hom)
    (hTor : TorIndependent X.2 (isAlgebraicSpace_yoneda B S hS U')
      (isAlgebraicSpace_yoneda B S hS U) f.hom (representedSpaceMap B S hS g).hom)
    (M K : DerivedCategory (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X)))
    (hM : RingedSite.IsPerfect (smallEtaleRingedSite B S hS X.1 X.2) M)
    (hK : QcohDerived B S hS X K) :
    IsIso (globalDerivedHomBaseChangeMap B S hS g f f' g' sq.w M K)
```

**`AlgebraicGeometry.Space.isIso_globalDerivedHomBaseChangeMap_of_isPseudoCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/GlobalDerivedHomBaseChangeIso.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/GlobalDerivedHomBaseChangeIso.lean#L118). The attribute's comment: “case (2): M pseudo-coherent, K in D^+_QCoh, R' of finite tor dimension over R”.

> **Stacks 0E4S, case (2).** Let `g : S' ⟶ S` be a morphism of affine schemes, `R = Γ(S, 𝒪)`,
> `R' = Γ(S', 𝒪)`, and let `X' = X ×_S S'` for `f : X ⟶ S` quasi-compact and quasi-separated with
> `X` and `S'` Tor independent over `S`. If `R'` has finite Tor dimension over `R`, then for
> `M ∈ D(𝒪_X)` pseudo-coherent and `K ∈ D^+_QCoh(𝒪_X)` the canonical map
> `RHom_X(M, K) ⊗^L_R R' ⟶ RHom_{X'}(L(g')^*M, L(g')^*K)` is an isomorphism.

```lean
theorem isIso_globalDerivedHomBaseChangeMap_of_isPseudoCoherent
    (sq : IsPullback g' f' f (representedSpaceMap B S hS g))
    (hfqc : IsQuasiCompact B S hS f.hom) (hfqs : IsQuasiSeparated B S hS f.hom)
    (hTor : TorIndependent X.2 (isAlgebraicSpace_yoneda B S hS U')
      (isAlgebraicSpace_yoneda B S hS U) f.hom (representedSpaceMap B S hS g).hom)
    (hR' : AlgebraicGeometry.HasFiniteTorDimensionRingHom
      (representedAffineCommRingCatHom B S hS g).hom)
    (M K : DerivedCategory (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X)))
    (hM : RingedSite.IsPseudoCoherent (smallEtaleRingedSite B S hS X.1 X.2) M)
    (hK : DerivedCategoryB.derivedCategoryBPlus
          (A := SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X))
          (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
            ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS X.1 X.2).O))) K) :
    IsIso (globalDerivedHomBaseChangeMap B S hS g f f' g' sq.w M K)
```

## Tag 0E4T, a remark

[Tag 0E4T](https://stacks.math.columbia.edu/tag/0E4T) in the Stacks Project.

**`AlgebraicGeometry.Space.globalDerivedHomBaseChangeMap_comp_map_counit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/GlobalDerivedHomBaseChange.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/GlobalDerivedHomBaseChange.lean#L236).

> For `M ∈ D(𝒪_X)` and `L ∈ D(𝒪_{X'})`, the canonical map of Stacks 0E4S at `(M, Rg'_*L)`
> followed by `RΓ(X', -)` of `R𝓗om(L(g')^*M, -)` of the counit `L(g')^*Rg'_*L ⟶ L` is the
> multiplication map `K' ⊗^L_R R' ⟶ K'`, the counit of `- ⊗^L_R R' ⊣` restriction of scalars, at
> `K' = RHom_{X'}(L(g')^*M, L)`, after the identification
> `RHom_X(M, Rg'_*L) = RHom_{X'}(L(g')^*M, L)`.

```lean
theorem globalDerivedHomBaseChangeMap_comp_map_counit
    (M : DerivedCategory (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X)))
    (L : DerivedCategory (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X'))) :
    globalDerivedHomBaseChangeMap B S hS g f f' g' w M
          ((derivedPushforward (X := smallEtaleRingedTopos B S hS X')
            (Y := smallEtaleRingedTopos B S hS X) (smallEtaleRingedToposHom B S hS g')).obj L) ≫
        (representedAffineDerivedSections B S hS U').map ((derivedModulePushforward B S hS f').map
          (((smallEtaleDerivedSheafHom B S hS X').obj
            (op ((smallEtaleDerivedModulePullback B S hS g').obj M))).map
            ((smallEtaleDerivedModuleAdjunction B S hS g').counit.app L))) =
      (representedAffineDerivedExtension B S hS g).functor.map
          ((derivedModulePushforward B S hS f ⋙ representedAffineDerivedSections B S hS U).map
              ((derivedModulePushforwardSheafHomIso g' M).inv.app L) ≫
            (affineBaseDerivedSectionsPushforwardIso B S hS g f f' g' w).hom.app _) ≫
        (RingTheory.TorIndependence.totalDerivedExtensionScalarsAdjunction
      (representedAffineCommRingCatHom B S hS g).hom).counit.app _
```

## Tag 0DKD, a lemma

[Tag 0DKD](https://stacks.math.columbia.edu/tag/0DKD) in the Stacks Project.

**`AlgebraicGeometry.Space.hasTorAmplitude_derivedScalarRestriction_smallEtaleDerivedModulePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/TorIndependentDerivedPullback.lean, line 608](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/TorIndependentDerivedPullback.lean#L608). The attribute's comment: “part (1)”.

> **Stacks 0DKD (1).** Let `X' → X`, `Y' → Y` be a cartesian square of algebraic spaces over
> `S` with `X` and `Y'` Tor independent over `Y`. If `E ∈ D(𝒪_X)` has Tor amplitude in `[a, b]`
> as a complex of `f⁻¹𝒪_Y`-modules, then `L(g')^*E` has Tor amplitude in `[a, b]` as a complex
> of `f'⁻¹𝒪_{Y'}`-modules.

```lean
theorem hasTorAmplitude_derivedScalarRestriction_smallEtaleDerivedModulePullback
    (htor : TorIndependent X.2 Y'.2 Y.2 f.hom g.hom)
    (T : Stacks.SheafOfModules.DerivedTensorProduct (inverseImageRingedSite B S hS f))
    (T' : Stacks.SheafOfModules.DerivedTensorProduct (inverseImageRingedSite B S hS f'))
    (E : DerivedCategory (Modules.{u, u} B S hS X.1 X.2)) (a b : ℤ)
    (hE : HasTorAmplitude T ((derivedScalarRestriction B S hS f).obj E) a b) :
    HasTorAmplitude T' ((derivedScalarRestriction B S hS f').obj
      ((smallEtaleDerivedModulePullback B S hS g').obj E)) a b
```

**`AlgebraicGeometry.Space.isIso_smallEtaleDerivedModulePullbackComparison_of_isFlatOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/TorIndependentDerivedPullback.lean, line 764](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/TorIndependentDerivedPullback.lean#L764). The attribute's comment: “part (2)”.

> **Stacks 0DKD (2).** For a cartesian square of algebraic spaces with `X` and `Y'` Tor
> independent over `Y`, and a quasi-coherent `𝒪_X`-module `𝒢` flat over `Y` (Stacks 05VV), the
> canonical comparison `L(g')^*𝒢 ⟶ (g')^*𝒢` is an isomorphism.

```lean
theorem isIso_smallEtaleDerivedModulePullbackComparison_of_isFlatOver
    (htor : TorIndependent X.2 Y'.2 Y.2 f.hom g.hom) (G : Modules.{u, u} B S hS X.1 X.2)
    [G.IsQuasicoherentOnSite] (hG : IsFlatOver B S hS X.2 f.hom G) :
    IsIso ((smallEtaleDerivedModulePullbackComparison B S hS g').app
      ((HomotopyCategory.quotient _ (ComplexShape.up ℤ)).obj
        ((CochainComplex.singleFunctor
          (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X)) 0).obj G)))
```

**`AlgebraicGeometry.Space.isIso_smallEtaleDerivedModulePullbackComparison_of_ringedToposHom_isFlatOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/TorIndependentDerivedPullbackRingedFlat.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/TorIndependentDerivedPullbackRingedFlat.lean#L149). The attribute's comment: “part (2)”.

> For a cartesian square of algebraic spaces with `X` and `Y'` Tor independent over `Y`, and an
> `𝒪_X`-module `𝒢` flat over `Y` — flat as an `f⁻¹𝒪_Y`-module, Stacks 08M5 — the canonical
> comparison `L(g')^*𝒢 ⟶ (g')^*𝒢` is an isomorphism.

```lean
theorem isIso_smallEtaleDerivedModulePullbackComparison_of_ringedToposHom_isFlatOver
    (htor : TorIndependent X.2 Y'.2 Y.2 f.hom g.hom)
    (G : SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X))
    (hG : RingedToposHom.IsFlatOver (X := smallEtaleRingedTopos B S hS X)
      (Y := smallEtaleRingedTopos B S hS Y) (smallEtaleRingedToposHom B S hS f) G) :
    IsIso ((smallEtaleDerivedModulePullbackComparison B S hS g').app
      ((HomotopyCategory.quotient _ (ComplexShape.up ℤ)).obj
        ((CochainComplex.singleFunctor
          (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X)) 0).obj G)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 75.20, Tag 08IM](https://stacks.math.columbia.edu/tag/08IM)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
