---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.Hom.HasLogPolesDeRhamComplex, AlgebraicGeometry.Scheme.Hom.shortExact_logShortComplex_stalk, AlgebraicGeometry.Scheme.Hom.logResidueShortComplex_shortExact, Stacks.LogPoles.shortExact_logShortComplex, AlgebraicGeometry.Scheme.Hom.deRhamComplexLogPoles, Stacks.LogPoles.deRhamComplexLogPoles, AlgebraicGeometry.Scheme.Hom.logFormsWedgeMap_spec, AlgebraicGeometry.Scheme.Hom.logPolesDifferentialGradedAlgebra_spec
statement: formalized
proof: formalized
---

# 50.15 Log poles along a divisor

Section 50.15 of the Stacks Project, [Tag 0FMU](https://stacks.math.columbia.edu/tag/0FMU). 7 tags here are carried by 26 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FMV, a definition

[Tag 0FMV](https://stacks.math.columbia.edu/tag/0FMV) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.HasLogPolesDeRhamComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/LogPoles/Defs.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/LogPoles/Defs.lean#L49).

> The *de Rham complex of log poles is defined* for an effective Cartier divisor `Y ⊆ X`,
> recorded by its ideal sheaf `I`, over a base `S` if for every point `y` of `Y` and every local
> equation `t ∈ 𝒪_{X, y}` of `Y` the map `𝒪_{X, y} → Ω_{X/S, y}`, `g ↦ g · dt`, is a split injection
> and `Ω^p_{X/S, y}` is `t`-torsion free for all `p`.

```lean
def HasLogPolesDeRhamComplex (f : X ⟶ S) (I : X.IdealSheafData) : Prop
```

## Tag 0FMW, a lemma

[Tag 0FMW](https://stacks.math.columbia.edu/tag/0FMW) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.shortExact_logShortComplex_stalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/LogPoles/GlobalResidueSequence.lean, line 351](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/LogPoles/GlobalResidueSequence.lean#L351). The attribute's comment: “for an arbitrary morphism of schemes and an effective Cartier divisor whose log poles complex is defined in the sense of 0FMV, the short exactness of the residue sequence of complexes at each point of the divisor and each local equation there”.

> **Stacks Project, Tag 0FMW.** Let `f : X ⟶ S` be a morphism of schemes and let `Y ⊆ X` be an
> effective Cartier divisor, recorded by its ideal sheaf `I`, with the de Rham complex of log poles
> defined for `Y ⊆ X` over `S` in the sense of [Stacks, Tag 0FMV]. Then at every point `y` of `Y`
> and for every local equation `t` of `Y` at `y` the residue sequence of complexes
>
> `0 → Ω^•_{X/S} → Ω^•_{X/S}(log Y) → Ω^•_{Y/S}[-1] → 0`
>
> of `𝒪_{S, f y}`-modules, built from the germ of `t` over `R = 𝒪_{X, y}`, is short exact. The
> three terms are the de Rham complex of `R`, the complex of log poles
> `Stacks.LogPoles.logComplex` of the germ of `t`, and the shift of the de Rham complex of
> `R ⧸ (germ t)`, which `AlgebraicGeometry.Scheme.Hom.quotientSpanGermEquivStalk` identifies with
> `𝒪_{Y, y}`.
>
> The divisor is only locally principal, and the equation `t` is a local one: both conditions the
> affine case of Tag 0FMW asks on the ring are supplied at the local ring by Tag 0FMV, so nothing
> is assumed about `g ↦ g · dt` on an open of `X`. Local equations exist at every point of an
> effective Cartier divisor by `AlgebraicGeometry.exists_germ_span_eq_ker_stalkMap`.
>
> The source states a short exact sequence of complexes of sheaves on `X`; the module docstring
> records what would be needed to read this one as its stalkwise verification. Of the two pieces
> only the first is genuinely absent: `AlgebraicGeometry.Scheme.Hom.logPolesForms` carries no
> differential, so there is no sheaf-level complex. The identification of its stalk with
> `Stacks.LogPoles.logFormsX` is unassembled rather than missing — its sheaf-side and ring-side
> halves are `AlgebraicGeometry.Scheme.Hom.logPolesFormsStalkEquiv`,
> `AlgebraicGeometry.Scheme.Hom.logPolesFormsStalkKerEquiv`,
> `Stacks.LogPoles.homIdealEquivLogFormsR` and `Stacks.LogPoles.logFormsXKerEquiv`, and what is
> owed is their composite.

```lean
theorem shortExact_logShortComplex_stalk (h : f.HasLogPolesDeRhamComplex I) (y : I.subscheme)
    (U : X.Opens) (hy : I.subschemeι y ∈ U) (t : Γ(X, U))
    (ht : RingHom.ker (I.subschemeι.stalkMap y).hom =
      Ideal.span {(X.presheaf.germ U (I.subschemeι y) hy).hom t}) :
    letI : Algebra (ToType (S.presheaf.stalk (f (I.subschemeι y))))
        (ToType (X.presheaf.stalk (I.subschemeι y))) := algebraStalkMap f (I.subschemeι y)
    (Stacks.LogPoles.logShortComplex
        (A := ToType (S.presheaf.stalk (f (I.subschemeι y))))
        (R := ToType (X.presheaf.stalk (I.subschemeι y)))
        (HasLogPolesDeRhamComplex.isSMulRegular_exteriorPower h y U hy t ht)
        (HasLogPolesDeRhamComplex.exists_retraction_D h y U hy t ht)).ShortExact
```

**`AlgebraicGeometry.Scheme.Hom.logResidueShortComplex_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/LogPoles/LogResidueSequence.lean, line 381](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/LogPoles/LogResidueSequence.lean#L381).

> **Stacks Project, Tag 0FMW.** Let `f : X ⟶ S` be a morphism of schemes and `Y ⊆ X` an
> effective Cartier divisor, cut out by `I`, for which the de Rham complex of log poles is defined
> ([Stacks, Tag 0FMV]). Then the sequence of complexes
>
> `0 → Ω^•_{X/S} → Ω^•_{X/S}(log Y) → i_*Ω^•_{Y/S}[-1] → 0`
>
> formed by the inclusion of forms with no pole and the residue is short exact. Here
> `Ω^p_{X/S}(log Y)` is `AlgebraicGeometry.Scheme.Hom.logPolesForms`, its differential is
> `AlgebraicGeometry.Scheme.Hom.logD`, characterised by the Leibniz rule
> `AlgebraicGeometry.Scheme.Hom.logD_eq`, and the residue is `AlgebraicGeometry.Scheme.Hom.logRes`,
> `α + dlog t ∧ β ↦ β|_Y` (`AlgebraicGeometry.Scheme.Hom.logRes_map_eq`).

```lean
theorem logResidueShortComplex_shortExact : (logResidueShortComplex f I hI hlog).ShortExact
```

**`Stacks.LogPoles.shortExact_logShortComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DeRham/LogPolesSequence.lean, line 508](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DeRham/LogPolesSequence.lean#L508). The attribute's comment: “the affine local case: the residue short exact sequence of complexes for a principal effective Cartier divisor”.

> **Stacks Project, Tag 0FMW**, in its affine local form.  Let `A → R` be a ring map and let
> `t ∈ R` cut out the effective Cartier divisor `Y = Spec (R ⧸ (t))` in `X = Spec R`.  Assume the
> de Rham complex of log poles is defined for `Y ⊆ X` over `S = Spec A`, that is: `g ↦ g · dt` is a
> split injection `R → Ω[R⁄A]` and `Ω^p_{R/A}` is `t`-torsion free for every `p`.  Then there is a
> canonical short exact sequence of complexes
> `0 → Ω^•_{X/S} → Ω^•_{X/S}(log Y) → Ω^•_{Y/S}[-1] → 0`,
> given by the inclusion of the forms with no pole and by the residue.

```lean
theorem shortExact_logShortComplex {t : R}
    (ht : ∀ p : ℕ, IsSMulRegular (↥(⋀[R]^p (Ω[R⁄A]))) t)
    (hsplit : ∃ r : Ω[R⁄A] →ₗ[R] R,
      r ∘ₗ LinearMap.toSpanSingleton R Ω[R⁄A] (KaehlerDifferential.D A R t) = LinearMap.id) :
    (logShortComplex ht hsplit).ShortExact
```

## Tag 0FUA, a definition

[Tag 0FUA](https://stacks.math.columbia.edu/tag/0FUA) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.deRhamComplexLogPoles`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/LogPoles/DeRhamComplexLogPoles.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/LogPoles/DeRhamComplexLogPoles.lean#L155). The attribute's comment: “the complex of sheaves of f⁻¹𝒪\_S-modules on X, for an arbitrary morphism of schemes and an arbitrary effective Cartier divisor for which the de Rham complex of log poles is defined (0FMV)”.

> **The de Rham complex of log poles** `Ω^•_{X/S}(log Y)` for a
> morphism of schemes `f : X ⟶ S` and an effective Cartier divisor `Y ⊆ X`, cut out by `I`, for
> which the de Rham complex of log poles is defined ([Stacks, Tag 0FMV]): the complex of sheaves
> of `f⁻¹𝒪_S`-modules on `X` constructed in [Stacks, Tag 0FMW].

```lean
def deRhamComplexLogPoles :
    CochainComplex (_root_.SheafOfModules.{u} (baseRingSheaf f)) ℕ
```

**`Stacks.LogPoles.deRhamComplexLogPoles`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DeRham/LogPolesComplex.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DeRham/LogPolesComplex.lean#L106). The attribute's comment: “the de Rham complex of log poles is the complex constructed in 0FMW; as 0FMW is formalized in its affine local form, this names that complex, for a principal divisor (t)”.

> **Stacks Project, Tag 0FUA.**  **The de Rham complex of log poles**
> `Ω^•_{X/S}(log Y)` for an effective Cartier divisor `Y = Spec (R ⧸ (t))` in `X = Spec R` over
> `S = Spec A`: the complex constructed in Stacks Tag 0FMW, namely `Stacks.LogPoles.logComplex`.
> A form of degree `p + 1` is a pair `(ω, η)` standing for `ω + dlog t ∧ η`, taken modulo the
> relations `t ω + dt ∧ η = 0`, and the differential is `(ω, η) ↦ (dω, -dη)`.

```lean
def deRhamComplexLogPoles {t : R}
    (ht : ∀ p : ℕ, IsSMulRegular (↥(⋀[R]^p (Ω[R⁄A]))) t) :
    CochainComplex (ModuleCat.{u} A) ℕ
```

## Tag 0FUP, a lemma

[Tag 0FUP](https://stacks.math.columbia.edu/tag/0FUP) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.logFormsWedgeMap_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/LogPoles/LogPolesWedgeProperties.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/LogPoles/LogPolesWedgeProperties.lean#L73). The attribute's comment: “clause (1): existence, uniqueness among all O\_X-bilinear extensions (the Leibniz rule is not needed for uniqueness), and the Leibniz rule”.

> **Stacks Project, Tag 0FUP, clause (1).** The wedge products
> `Ω^p_{X/S} × Ω^q_{X/S} → Ω^{p+q}_{X/S}` extend to `𝒪_X`-bilinear maps
> `Ω^p_{X/S}(log Y) × Ω^q_{X/S}(log Y) → Ω^{p+q}_{X/S}(log Y)`, namely
> `AlgebraicGeometry.Scheme.Hom.logFormsWedgeMap`; the extension is unique among all `𝒪_X`-bilinear
> maps extending the wedge product; and it satisfies the Leibniz rule
> `d(ω ∧ η) = d(ω) ∧ η + (-1)^{deg ω} ω ∧ d(η)`.

```lean
theorem logFormsWedgeMap_spec :
    (∀ (p q : ℕ) (W : X.Opens) (ω : Γ(relativeDifferentialForms f (p : ℤ), W))
      (η : Γ(relativeDifferentialForms f (q : ℤ), W)),
      (logFormsWedgeMap hI hlog p q).app (op W) ((logPolesFormsInclusion f I p).val.app (op W) ω)
          ((logPolesFormsInclusion f I q).val.app (op W) η) =
        (logPolesFormsInclusion f I (p + q)).val.app (op W) (formWedge f p q W ω η)) ∧
    (∀ (p q : ℕ) (m : _root_.SheafOfModules.BilinearMap (logPolesForms f I p)
        (logPolesForms f I q) (logPolesForms f I (p + q))),
      (∀ (W : X.Opens) (ω : Γ(relativeDifferentialForms f (p : ℤ), W))
        (η : Γ(relativeDifferentialForms f (q : ℤ), W)),
        m.app (op W) ((logPolesFormsInclusion f I p).val.app (op W) ω)
            ((logPolesFormsInclusion f I q).val.app (op W) η) =
          (logPolesFormsInclusion f I (p + q)).val.app (op W) (formWedge f p q W ω η)) →
      m = logFormsWedgeMap hI hlog p q) ∧
    (∀ (p q : ℕ) (W : X.Opens) (φ : (logPolesForms f I p).val.obj (op W))
      (ψ : (logPolesForms f I q).val.obj (op W)),
      logD hI hlog ((logFormsWedgeMap hI hlog p q).app (op W) φ ψ) =
        logFormsCast (Nat.add_right_comm p 1 q)
            ((logFormsWedgeMap hI hlog (p + 1) q).app (op W) (logD hI hlog φ) ψ) +
          ((-1 : ℤ) ^ p) • (logFormsWedgeMap hI hlog p (q + 1)).app (op W) φ (logD hI hlog ψ))
```

**`AlgebraicGeometry.Scheme.Hom.logPolesDifferentialGradedAlgebra_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/LogPoles/LogPolesWedgeProperties.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/LogPoles/LogPolesWedgeProperties.lean#L104). The attribute's comment: “clause (2): the sheaf of differential graded f⁻¹O\_S-algebras on the complex of 0FUA, with the multiplication of clause (1), and the inclusion as a homomorphism”.

> **Stacks Project, Tag 0FUP, clause (2).** With the multiplication of clause (1), the de Rham
> complex of log poles `Ω^•_{X/S}(log Y)` of Tag 0FUA is a sheaf of differential graded
> `f⁻¹𝒪_S`-algebras `A`, and the inclusion `Ω^•_{X/S} ⟶ Ω^•_{X/S}(log Y)` underlies a
> homomorphism of sheaves of differential graded algebras from the relative de Rham complex of
> Tag 0FU6 to `A`.

```lean
theorem logPolesDifferentialGradedAlgebra_spec :
    ∃ (A : _root_.SheafOfModules.DifferentialGradedAlgebra.{u, u} (baseRingSheaf f))
      (φ : _root_.SheafOfModules.DifferentialGradedAlgebra.Hom
        (AlgebraicGeometry.SheafOfModules.relativeDeRhamDifferentialGradedAlgebra
          (inverseImageStructureMap f)) A),
      A.complex = deRhamComplexLogPolesInt f I hI hlog ∧
      (∀ (p q : ℕ) (U : X.Opensᵒᵖ) (x : (A.complex.X (p : ℤ)).val.obj U)
        (y : (A.complex.X (q : ℤ)).val.obj U) (x' : (logPolesForms f I p).val.obj U)
        (y' : (logPolesForms f I q).val.obj U), HEq x x' → HEq y y' →
          HEq ((A.mul (p : ℤ) (q : ℤ)).app U x y)
            ((logFormsWedgeMap hI hlog p q).app U x' y')) ∧
      (∀ U : X.Opensᵒᵖ, HEq (A.one.eval U)
        ((logPolesFormsInclusion f I 0).val.app U (formOne U.unop))) ∧
      HEq φ.toHomologicalComplex (deRhamComplexLogPolesIntInclusion f I hI hlog)
```

**`AlgebraicGeometry.Scheme.Hom.logExteriorDesc_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/LogPoles/LogPolesWedgeProperties.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/LogPoles/LogPolesWedgeProperties.lean#L133). The attribute's comment: “clause (3): the map from the p-th exterior power of Ω¹(log Y) induced by the wedge product of clause (1) is an isomorphism onto Ω^p(log Y), for every p”.

> **Stacks Project, Tag 0FUP, clause (3).** Via the maps of clause (1),
> `Ω^p_{X/S}(log Y) = ⋀^p(Ω^1_{X/S}(log Y))`. The forms with logarithmic poles form a sheaf of graded
> `𝒪_X`-algebras `AlgebraicGeometry.Scheme.Hom.logGradedAlgebra` under the wedge product of
> clause (1); the unital homomorphism `AlgebraicGeometry.Scheme.Hom.logExteriorDesc` to it from the
> exterior algebra of `Ω^1_{X/S}(log Y)` is the identity of `Ω^1_{X/S}(log Y)` in degree one, so in
> degree `p` it sends `φ₁ ∧ ⋯ ∧ φ_p` to the wedge product of the `φᵢ`, and it is an isomorphism in
> every degree `p`.

```lean
theorem logExteriorDesc_spec :
    (∀ (p q : ℕ) (U : X.Opensᵒᵖ) (x : (logPolesForms f I p).val.obj U)
      (y : (logPolesForms f I q).val.obj U),
      ((logGradedAlgebra f I hI hlog).mul (p : ℤ) (q : ℤ)).app U x y =
        (logFormsWedgeMap hI hlog p q).app U x y) ∧
    Scheme.Modules.exteriorGenerator (logPolesForms f I 1) ≫ (logExteriorDesc f I hI hlog).app 1 =
      logGenerator f I hI hlog ∧
    ∀ p : ℕ, IsIso ((logExteriorDesc f I hI hlog).app (p : ℤ))
```

**`AlgebraicGeometry.Scheme.Hom.logRes_logFormsWedge_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/LogPoles/LogPolesWedgeProperties.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/LogPoles/LogPolesWedgeProperties.lean#L151). The attribute's comment: “clause (4), in every degree of ω: the formula in degree p + 1, and the vanishing of Res(ω ∧ η) for ω of degree 0, where Res(ω) = 0”.

> **Stacks Project, Tag 0FUP, clause (4).** The residue
> `Res : Ω^•_{X/S}(log Y) → Ω^•_{Y/S}[-1]` satisfies `Res(ω ∧ η) = Res(ω) ∧ η|_Y` for a local
> section `ω` of `Ω^p_{X/S}(log Y)` and a local section `η` of `Ω^q_{X/S}`: in degree `p + 1` this
> is the first conjunct; in degree `0` the residue vanishes, and so does `Res(ω ∧ η)`, the second
> conjunct.

```lean
theorem logRes_logFormsWedge_spec :
    (∀ (p q : ℕ) (W : X.Opens) (ω : (logPolesForms f I (p + 1)).val.obj (op W))
      (η : Γ(relativeDifferentialForms f (q : ℤ), W)),
      logRes hI hlog (logFormsCast (Nat.add_right_comm p 1 q)
          (logFormsWedge hI hlog ω ((logPolesFormsInclusion f I q).val.app (op W) η))) =
        formWedge (I.subschemeι ≫ f) p q (I.subschemeι ⁻¹ᵁ W) (logRes hI hlog ω)
          (formRes I.subschemeι (q : ℤ) W η)) ∧
    (∀ (q : ℕ) (W : X.Opens) (ω : (logPolesForms f I 0).val.obj (op W))
      (η : Γ(relativeDifferentialForms f ((q + 1 : ℕ) : ℤ), W)),
      logRes hI hlog (logFormsCast (Nat.zero_add (q + 1))
          (logFormsWedge hI hlog ω ((logPolesFormsInclusion f I (q + 1)).val.app (op W) η))) = 0)
```

**`Stacks.LogPoles.logWedge`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DeRham/LogPolesProduct.lean, line 399](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DeRham/LogPolesProduct.lean#L399). The attribute's comment: “clause (1), existence: the O\_X-bilinear extension of the wedge product to the log poles complex of 0FMW, at the ring level for a principal divisor (t); the Leibniz rule for this product is not proved”.

> **The product on the de Rham complex of log poles**, `Ω^p(log Y) × Ω^q(log Y) → Ω^\{p+q}(log
> Y)`, as an `𝒪\_X`-bilinear map.  On the pair model it is
> `(ω₁, η₁) ∧ (ω₂, η₂) = (ω₁ ∧ ω₂, η₁ ∧ ω₂ + (-1)^{p+1} ω₁ ∧ η₂)`, with the three degenerate cases
> where a degree is zero given by wedging a function into both components.

```lean
def logWedge (A : Type u) [CommRing A] [Algebra A R]
    (ht : ∀ p : ℕ, IsSMulRegular (↥(⋀[R]^p (Ω[R⁄A]))) t) :
    (p q : ℕ) →
      (logFormsR A t p →ₗ[R] logFormsR A t q →ₗ[R] logFormsR A t (p + q))
```

**`Stacks.LogPoles.logWedge_logInclR`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DeRham/LogPolesProduct.lean, line 449](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DeRham/LogPolesProduct.lean#L449). The attribute's comment: “clause (1), existence: the constructed product restricts to the wedge product on the forms with no pole, which is the defining property of the extension”.

> **The product extends the wedge product of the forms with no pole.**  This is the defining
> property of the extension in clause (1) of Stacks Tag 0FUP: a form with no pole is the pair
> `(ω, 0)`, and the formula on pairs leaves the second component zero.

```lean
theorem logWedge_logInclR
    (ht : ∀ p : ℕ, IsSMulRegular (↥(⋀[R]^p (Ω[R⁄A]))) t)
    (p q : ℕ) (ω : ⋀[R]^p (Ω[R⁄A])) (η : ⋀[R]^q (Ω[R⁄A])) :
    logWedge A ht p q (logInclR t p ω) (logInclR t q η) =
      logInclR t (p + q) (exteriorPower.wedgeMul p q ω η)
```

**`Stacks.LogPoles.eq_logWedge_of_logInclR`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DeRham/LogPolesProduct.lean, line 495](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DeRham/LogPolesProduct.lean#L495). The attribute's comment: “clause (1): the product built here is THE O\_X-bilinear extension, discharging the hypothesis of the uniqueness statement; the Leibniz rule is not proved”.

> **The product of clause (1) is the unique `𝒪_X`-bilinear extension.**  Any `𝒪_X`-bilinear
> product on the de Rham complex of log poles that restricts to the wedge product on the forms with
> no pole is `Stacks.LogPoles.logWedge`.  This discharges the hypothesis of the uniqueness
> statement `Stacks.LogPoles.logWedge_unique` with the construction, so uniqueness is not vacuous.

```lean
theorem eq_logWedge_of_logInclR
    (ht : ∀ p : ℕ, IsSMulRegular (↥(⋀[R]^p (Ω[R⁄A]))) t)
    (w : (p q : ℕ) →
      logFormsR A t p →ₗ[R] logFormsR A t q →ₗ[R] logFormsR A t (p + q))
    (hw : ∀ (p q : ℕ) (ω : ⋀[R]^p (Ω[R⁄A])) (η : ⋀[R]^q (Ω[R⁄A])),
      w p q (logInclR t p ω) (logInclR t q η) =
        logInclR t (p + q) (exteriorPower.wedgeMul p q ω η)) :
    w = logWedge A ht
```

**`Stacks.LogPoles.logWedge_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DeRham/LogPolesWedge.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DeRham/LogPolesWedge.lean#L180). The attribute's comment: “clause (1), the uniqueness half, strengthened by dropping the Leibniz hypothesis: an O\_X-bilinear extension of the wedge to the log poles complex of 0FMW is unique. Existence, and clauses (2), (3), (4), are not proved here”.

> If `t` is a nonzerodivisor on the forms, two `𝒪_X`-bilinear products on the de Rham complex
> of log poles that both restrict to the wedge product on the forms with no pole are equal.

```lean
theorem logWedge_unique {t : R}
    (ht : ∀ p : ℕ, IsSMulRegular (↥(⋀[R]^p (Ω[R⁄A]))) t)
    (w₁ w₂ : (p q : ℕ) →
      logFormsR A t p →ₗ[R] logFormsR A t q →ₗ[R] logFormsR A t (p + q))
    (h₁ : ∀ (p q : ℕ) (ω : ⋀[R]^p (Ω[R⁄A])) (η : ⋀[R]^q (Ω[R⁄A])),
      w₁ p q (logInclR t p ω) (logInclR t q η) =
        logInclR t (p + q) (exteriorPower.wedgeMul p q ω η))
    (h₂ : ∀ (p q : ℕ) (ω : ⋀[R]^p (Ω[R⁄A])) (η : ⋀[R]^q (Ω[R⁄A])),
      w₂ p q (logInclR t p ω) (logInclR t q η) =
        logInclR t (p + q) (exteriorPower.wedgeMul p q ω η)) :
    w₁ = w₂
```

## Tag 0FUQ, a lemma

[Tag 0FUQ](https://stacks.math.columbia.edu/tag/0FUQ) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.LogPolesResidueData.ambientChernBoundary_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/LogPoles/BoundaryChernComparison.lean, line 355](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/LogPoles/BoundaryChernComparison.lean#L355). The attribute's comment: “upper left triangle of the diagram: the map of 0FU7 for c\_1^dR(O\_X(-Y)), in the description 0FUG gives of it as the boundary map of the residue sequence of 0FUF, is the boundary map of the log poles sequence of 0FMW composed with the restriction of relative forms; the three short exact sequences in global form and the two morphisms between them that the source builds from a formula on local sections are carried as the explicit named hypothesis LogPolesResidueData, the library having none of them globally”.

> **Stacks Project, Tag 0FUQ, the upper left triangle.**
>
> `ξ' = δ ∘ (restriction of forms)`
>
> in `D(f^{-1}𝒪_S)`: the map of Tag 0FU7 for `c₁^{dR}(𝒪_X(-Y))`, read through Tag 0FUG as the
> boundary map of the residue sequence of Tag 0FUF for `𝒪_X(-Y)`, factors through the boundary map
> of the log poles sequence of Tag 0FMW along the restriction of relative forms
> `Ω^•_{X/S} ⟶ Ω^•_{Y/S}`.
>
> This is the functoriality of boundary maps along the morphism of short exact sequences
> `AlgebraicGeometry.SheafOfModules.LogPolesResidueData.ambientMap`, whose left arrow is the
> identity.

```lean
theorem ambientChernBoundary_eq :
    d.ambientChernBoundary = DerivedCategory.Q.map d.restriction ≫ d.boundary
```

**`AlgebraicGeometry.SheafOfModules.LogPolesResidueData.boundary_comp_shiftedRestriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/LogPoles/BoundaryChernComparison.lean, line 376](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/LogPoles/BoundaryChernComparison.lean#L376). The attribute's comment: “lower right triangle of the diagram: the boundary map of the log poles sequence of 0FMW, followed by the twofold translate of the restriction of relative forms, is the map of 0FU7 for c\_1^dR(O\_X(-Y)|\_Y) in the description 0FUG gives of it as the boundary map of the residue sequence of 0FUF on the divisor; the sequences and the two morphisms between them are carried as the explicit named hypothesis LogPolesResidueData”.

> **Stacks Project, Tag 0FUQ, the lower right triangle.**
>
> `(restriction of forms)[2] ∘ δ = ζ'`
>
> in `D(f^{-1}𝒪_S)`: the boundary map of the log poles sequence of Tag 0FMW, followed by the
> twofold translate of the restriction of relative forms, is the map of Tag 0FU7 for
> `c₁^{dR}(𝒪_X(-Y)|_Y)`, read through Tag 0FUG as the boundary map of the residue sequence of Tag
> 0FUF for `𝒪_X(-Y)|_Y`.
>
> This is the functoriality of boundary maps along the morphism of short exact sequences
> `AlgebraicGeometry.SheafOfModules.LogPolesResidueData.divisorMap`, whose right arrow is the
> identity.

```lean
theorem boundary_comp_shiftedRestriction :
    d.boundary ≫ (DerivedCategory.Q.map d.restriction)⟦(2 : ℤ)⟧' = d.divisorChernBoundary
```

**`AlgebraicGeometry.SheafOfModules.LogPolesResidueData.commSq_chernBoundary`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/LogPoles/BoundaryChernComparison.lean, line 393](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/LogPoles/BoundaryChernComparison.lean#L393). The attribute's comment: “the square of the diagram, deduced from the two triangles exactly as in the source: the restriction of relative forms, in degree zero and in degree two, carries the map of 0FU7 for c\_1^dR(O\_X(-Y)) to the one for its restriction to the divisor, both read through 0FUG as boundary maps of residue sequences of 0FUF; the sequences and the two morphisms between them are carried as the explicit named hypothesis LogPolesResidueData”.

> **Stacks Project, Tag 0FUQ, the square.**
>
> `(restriction of forms)[2] ∘ ξ' = ζ' ∘ (restriction of forms)`
>
> in `D(f^{-1}𝒪_S)`: the square built from the maps of Tag 0FU7 for `c₁^{dR}(𝒪_X(-Y))` and for its
> restriction to the divisor, and from the restriction of relative forms in both degrees, commutes.
> As in the source this is deduced from the commutativity of the two triangles cut out by the
> boundary map `δ` of the log poles sequence of Tag 0FMW along the diagonal.

```lean
theorem commSq_chernBoundary :
    d.ambientChernBoundary ≫ (DerivedCategory.Q.map d.restriction)⟦(2 : ℤ)⟧' =
      DerivedCategory.Q.map d.restriction ≫ d.divisorChernBoundary
```

**`AlgebraicGeometry.SheafOfModules.LogPolesResidueData.deRhamClassDerivedMorphism_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/LogPoles/BoundaryChernComparison.lean, line 426](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/LogPoles/BoundaryChernComparison.lean#L426). The attribute's comment: “upper left triangle with xi' named as the map of 0FU7 attached to the de Rham first Chern class of O\_X(-Y), the identification of 0FUG being made through the uniqueness in 0FU7; carried as explicit named hypotheses are LogPolesResidueData (the three short exact sequences in global form and the two morphisms between them), together with the three inputs the library's own 0FUG carries, namely hlift, hev and realizationComparison”.

> **Stacks Project, Tag 0FUQ, the upper left triangle, with `ξ'` named as in the statement of
> Tag 0FUQ.**
>
> `ξ' = δ ∘ (restriction of forms)`
>
> in `D(f^{-1}𝒪_S)`, where `ξ'` is the morphism of Tag 0FU7 attached to the de Rham
> first Chern class `ξ = c₁^{dR}(ℒ)` of the invertible module `ℒ`, which for Tag 0FUQ is
> `𝒪_X(-Y)`, and `δ` is the boundary map of the shifted log poles sequence of Tag 0FMW.
>
> The identification of the boundary map of the residue sequence of Tag 0FUF with `ξ'` is Tag 0FUG,
> and it is made here through the uniqueness of Tag 0FU7,
> `AlgebraicGeometry.SheafOfModules.eq_deRhamClassDerivedMorphism`, with the same two inputs that
> the library's Tag 0FUG carries: `hlift`, that the boundary map lifts to the derived category of
> right differential graded `Ω^•_{X/S}`-modules, and `hev`, that its value at the unit is
> `c₁^{dR}(ℒ)`. The third input, `realizationComparison`, transports the first Chern class from the
> abelian-sheaf realization of de Rham cohomology, in which it is constructed, to the
> sheaf-of-modules realization in which the classes of Tag 0FU7 live.

```lean
theorem deRhamClassDerivedMorphism_eq (c : DeRhamDerivedModuleCorrespondence B D)
    (realizationComparison : deRhamCohomologyAbelian B D 2 →+ deRhamCohomology B D 2)
    (L : _root_.SheafOfModules.{u} (structureSheaf X.sheaf))
    (hL : Stacks.SheafOfModules.IsInvertible X.sheaf.obj (structureSheaf X.sheaf).property L)
    (hlift : ∃ g : deRhamDerivedRegular B D ⟶ deRhamDerivedRegularShift B D 2,
      c.forget 2 g = d.ambientChernBoundary)
    (hev : c.evalOne 2 d.ambientChernBoundary =
      realizationComparison (deRhamFirstChernClassAbelianOf B D L hL)) :
    deRhamClassDerivedMorphism B D c 2
        (realizationComparison (deRhamFirstChernClassAbelianOf B D L hL)) =
      DerivedCategory.Q.map d.restriction ≫ d.boundary
```

**`AlgebraicGeometry.SheafOfModules.LogPolesResidueData.commSq_deRhamClassDerivedMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/LogPoles/BoundaryChernComparison.lean, line 455](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/LogPoles/BoundaryChernComparison.lean#L455). The attribute's comment: “the square with xi' named as the map of 0FU7 attached to the de Rham first Chern class of O\_X(-Y); zeta' stays in the description 0FUG gives of it as the boundary map of the residue sequence of 0FUF on the divisor, since the map of 0FU7 is built from the de Rham differential graded algebra of the ambient data and the comparison along the closed immersion that would supply one on the divisor is not in the library; carried as explicit named hypotheses are LogPolesResidueData and the three inputs of 0FUG, namely hlift, hev and realizationComparison”.

> **Stacks Project, Tag 0FUQ, the square, with `ξ'` named as in the statement of Tag 0FUQ.**
>
> `(restriction of forms)[2] ∘ ξ' = ζ' ∘ (restriction of forms)`
>
> in `D(f^{-1}𝒪_S)`, where `ξ'` is the morphism of Tag 0FU7 attached to `c₁^{dR}(ℒ)` for the
> invertible module `ℒ`, which for Tag 0FUQ is `𝒪_X(-Y)`, and `ζ'` is the boundary map of the
> shifted residue sequence of Tag 0FUF on the divisor, which is the description Tag 0FUG gives of
> the morphism of Tag 0FU7 attached to `c₁^{dR}(ℒ|_Y)`.

```lean
theorem commSq_deRhamClassDerivedMorphism (c : DeRhamDerivedModuleCorrespondence B D)
    (realizationComparison : deRhamCohomologyAbelian B D 2 →+ deRhamCohomology B D 2)
    (L : _root_.SheafOfModules.{u} (structureSheaf X.sheaf))
    (hL : Stacks.SheafOfModules.IsInvertible X.sheaf.obj (structureSheaf X.sheaf).property L)
    (hlift : ∃ g : deRhamDerivedRegular B D ⟶ deRhamDerivedRegularShift B D 2,
      c.forget 2 g = d.ambientChernBoundary)
    (hev : c.evalOne 2 d.ambientChernBoundary =
      realizationComparison (deRhamFirstChernClassAbelianOf B D L hL)) :
    deRhamClassDerivedMorphism B D c 2
          (realizationComparison (deRhamFirstChernClassAbelianOf B D L hL)) ≫
        (DerivedCategory.Q.map d.restriction)⟦(2 : ℤ)⟧' =
      DerivedCategory.Q.map d.restriction ≫ d.divisorChernBoundary
```

**`Stacks.LineBundle.idealChernMorphism_eq_comp_boundary`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/LogPoles/ChernClassRestrictionSquare.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/LogPoles/ChernClassRestrictionSquare.lean#L94). The attribute's comment: “the upper left triangle: the map of 0FU7 for c\_1^dR(O\_X(-Y)) is the boundary map delta of the shifted sequence of 0FMW composed with the restriction of forms”.

> The upper left triangle `ξ' = δ ∘ res`: the map `idealChernMorphism` is the restriction of
> forms followed by the boundary map of the shifted log poles sequence.

```lean
theorem idealChernMorphism_eq_comp_boundary :
    idealChernMorphism f I =
      DerivedCategory.Q.map (Scheme.Hom.divisorRestrictionInt f I) ≫
        (Scheme.Hom.logPolesShiftedSequence f hI hlog).boundary
```

**`Stacks.LineBundle.logPolesBoundary_comp_restriction_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/LogPoles/ChernClassRestrictionSquare.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/LogPoles/ChernClassRestrictionSquare.lean#L107). The attribute's comment: “the lower right triangle: the boundary map delta followed by the restriction of forms in degree two is the map of 0FU7 on Y for c\_1^dR(O\_X(-Y)|\_Y), read on X through the exact direct image along the closed immersion”.

> The lower right triangle: `res[2] ∘ δ = ζ'`, with `ζ'` read on `X` through the exact direct
> image along `i : Y ⟶ X` and `Ω^•_{Y/S}` identified with its direct image by
> `Stacks.LineBundle.divisorDeRhamIntHom`.

```lean
theorem logPolesBoundary_comp_restriction_eq :
    (Scheme.Hom.logPolesShiftedSequence f hI hlog).boundary ≫
        (DerivedCategory.Q.map
          (Scheme.Hom.divisorRestrictionInt f I ≫ divisorDeRhamIntHom f I))⟦(2 : ℤ)⟧' =
      DerivedCategory.Q.map (divisorDeRhamIntHom f I) ≫
        divisorPushforwardDerivedMap f I (divisorChernMorphism f I)
```

**`Stacks.LineBundle.idealChernMorphism_comp_restriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/LogPoles/ChernClassRestrictionSquare.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/LogPoles/ChernClassRestrictionSquare.lean#L121). The attribute's comment: “the square of the diagram, deduced from the two triangles”.

> The square: `res[2] ∘ ξ' = ζ' ∘ res`.

```lean
theorem idealChernMorphism_comp_restriction :
    idealChernMorphism f I ≫
        (DerivedCategory.Q.map
          (Scheme.Hom.divisorRestrictionInt f I ≫ divisorDeRhamIntHom f I))⟦(2 : ℤ)⟧' =
      DerivedCategory.Q.map (Scheme.Hom.divisorRestrictionInt f I ≫ divisorDeRhamIntHom f I) ≫
        divisorPushforwardDerivedMap f I (divisorChernMorphism f I)
```

## Tag 0FMX, a lemma

[Tag 0FMX](https://stacks.math.columbia.edu/tag/0FMX) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.cup_deRhamFirstChernClass_eq_zero_of_restriction_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/LogPoles/ChernClassVanishing.lean, line 262](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/LogPoles/ChernClassVanishing.lean#L262). The attribute's comment: “sheaf-of-modules form over a ringed space; see the docstring for what is carried”.

> **Stacks Project, Tag 0FMX**, for the relative de Rham complex of a morphism `φ : A ⟶ 𝒪_X` of
> sheaves of commutative rings on a ringed space.
>
> `c₁^{dR}(𝒪_X(Y)) ∪ b = 0`
>
> in `H^{2 + m}_{dR}`: a relative de Rham cohomology class `b ∈ H^m_{dR}` whose restriction to the
> divisor is zero is killed by cup product with the de Rham first Chern class of `𝒪_X(Y)`. The
> divisor enters through the invertible module `L = 𝒪_X(-Y)` and through the Picard class `ℓ` of
> `𝒪_X(Y)`, which is the inverse of that of `L`; the restriction of `b` is the map that the
> restriction of relative forms `Ω^•_{X/S} ⟶ Ω^•_{Y/S}` induces on `H^m`, the de Rham complex of
> the divisor being read on the ambient space as in Section 50.15 of the source.
>
> The proof is the chain of the source: `c₁^{dR}(𝒪_X(Y)) = -c₁^{dR}(L)` by additivity of the first
> Chern class, `c₁^{dR}(L) ∪ b = ξ'(b)` by Remark 0FU7, property (3), `ξ' = δ ∘ (restriction of
> forms)` by the upper left triangle of Tag 0FUQ, and `δ(b|\_Y) = 0` because `b|\_Y = 0`.
>
> Carried as explicit named hypotheses are the sequences of Tag 0FUQ, `d`; the cup product of
> Cohomology, Section 0FKU, `cp`; the identification of Differential Graded Sheaves, Section 0FU3,
> `cc`; property (3) of Remark 0FU7, `act`; the comparison `realizationComparison` of the two
> realizations of de Rham cohomology; and the two clauses `hlift` and `hev` of Tag 0FUG.

```lean
theorem cup_deRhamFirstChernClass_eq_zero_of_restriction_eq_zero (d : LogPolesResidueData B D)
    (cp : HypercohomologyCupProduct B D) (cc : DeRhamDerivedModuleCorrespondence B D)
    (act : DeRhamClassCupAction B D cp cc)
    (realizationComparison : deRhamCohomologyAbelian B D 2 →+ deRhamCohomology B D 2)
    (L : _root_.SheafOfModules.{u} (structureSheaf X.sheaf))
    (hL : Stacks.SheafOfModules.IsInvertible X.sheaf.obj (structureSheaf X.sheaf).property L)
    (hlift : ∃ g : deRhamDerivedRegular B D ⟶ deRhamDerivedRegularShift B D 2,
      cc.forget 2 g = d.ambientChernBoundary)
    (hev : cc.evalOne 2 d.ambientChernBoundary =
      realizationComparison (deRhamFirstChernClassAbelianOf B D L hL))
    (ℓ : Stacks.SheafOfModules.Picard.PicardGroup X.sheaf.obj (structureSheaf X.sheaf).property)
    (hℓ : ℓ + Stacks.SheafOfModules.Picard.classOf X.sheaf.obj
      (structureSheaf X.sheaf).property L hL = 0)
    (m : ℤ) (b : deRhamCohomology B D m)
    (hb : (derivedHypercohomologyMap (DerivedCategory.Q.map d.restriction) m).hom b = 0) :
    deRhamCupProduct B D cp 2 m
      (realizationComparison (deRhamFirstChernClassAbelian B D ℓ)) b = 0
```

**`AlgebraicGeometry.Scheme.Hom.cup_deRhamFirstChernClass_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/LogPoles/ChernClassVanishing.lean, line 346](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/LogPoles/ChernClassVanishing.lean#L346). The attribute's comment: “morphism-of-schemes form; see the docstring for what is carried”.

> **Stacks Project, Tag 0FMX.** Let `p : X ⟶ S` be a morphism of schemes and let `Y ⊆ X` be an
> effective Cartier divisor for which the de Rham complex of log poles is defined over `S`. If the
> restriction to `Y` of a relative de Rham cohomology class `b ∈ H^m_{dR}(X/S)` is zero, then
>
> `c₁^{dR}(𝒪_X(Y)) ∪ b = 0`
>
> in `H^{2 + m}_{dR}(X/S)`. Here `𝒪_X(Y)` enters through its class `ℓ` in `Pic(X)`, the inverse of
> the class of `L = 𝒪_X(-Y)`, and the restriction of `b` is the map induced on `H^m` by the
> restriction of relative forms `Ω^•_{X/S} ⟶ Ω^•_{Y/S}`.
>
> The two hypotheses the source states on the divisor are the first two fields of `h`. Carried as
> explicit named hypotheses are the sequences of Tag 0FUQ, the third field of `h`; the cup product
> of Cohomology, Section 0FKU, `cp`; the identification of Differential Graded Sheaves, Section
> 0FU3, `cc`; property (3) of Remark 0FU7, `act`; the comparison `realizationComparison` of the two
> realizations of de Rham cohomology; and the two clauses `hlift` and `hev` of Tag 0FUG.

```lean
theorem cup_deRhamFirstChernClass_eq_zero {p : X ⟶ S} {I : X.IdealSheafData}
    (h : LogPolesDivisorData p I)
    (cp : SheafOfModules.HypercohomologyCupProduct (deRhamAlgebras p)
      (SheafOfModules.deRhamDifferential (deRhamAlgebras p)))
    (cc : SheafOfModules.DeRhamDerivedModuleCorrespondence (deRhamAlgebras p)
      (SheafOfModules.deRhamDifferential (deRhamAlgebras p)))
    (act : SheafOfModules.DeRhamClassCupAction (deRhamAlgebras p)
      (SheafOfModules.deRhamDifferential (deRhamAlgebras p)) cp cc)
    (realizationComparison :
      SheafOfModules.deRhamCohomologyAbelian (deRhamAlgebras p)
          (SheafOfModules.deRhamDifferential (deRhamAlgebras p)) 2 →+
        SheafOfModules.deRhamCohomology (deRhamAlgebras p)
          (SheafOfModules.deRhamDifferential (deRhamAlgebras p)) 2)
    (L : _root_.SheafOfModules.{u} (structureSheaf X.sheaf))
    (hL : Stacks.SheafOfModules.IsInvertible X.sheaf.obj (structureSheaf X.sheaf).property L)
    (hlift : ∃ g : SheafOfModules.deRhamDerivedRegular (deRhamAlgebras p)
        (SheafOfModules.deRhamDifferential (deRhamAlgebras p)) ⟶
        SheafOfModules.deRhamDerivedRegularShift (deRhamAlgebras p)
          (SheafOfModules.deRhamDifferential (deRhamAlgebras p)) 2,
      cc.forget 2 g = h.residueData.ambientChernBoundary)
    (hev : cc.evalOne 2 h.residueData.ambientChernBoundary =
      realizationComparison (SheafOfModules.deRhamFirstChernClassAbelianOf (deRhamAlgebras p)
        (SheafOfModules.deRhamDifferential (deRhamAlgebras p)) L hL))
    (ℓ : Stacks.SheafOfModules.Picard.PicardGroup X.sheaf.obj (structureSheaf X.sheaf).property)
    (hℓ : ℓ + Stacks.SheafOfModules.Picard.classOf X.sheaf.obj
      (structureSheaf X.sheaf).property L hL = 0)
    (m : ℤ)
    (b : SheafOfModules.deRhamCohomology (deRhamAlgebras p)
      (SheafOfModules.deRhamDifferential (deRhamAlgebras p)) m)
    (hb : (SheafOfModules.derivedHypercohomologyMap
      (DerivedCategory.Q.map h.residueData.restriction) m).hom b = 0) :
    SheafOfModules.deRhamCupProduct (deRhamAlgebras p)
        (SheafOfModules.deRhamDifferential (deRhamAlgebras p)) cp 2 m
        (realizationComparison (SheafOfModules.deRhamFirstChernClassAbelian (deRhamAlgebras p)
          (SheafOfModules.deRhamDifferential (deRhamAlgebras p)) ℓ)) b = 0
```

**`AlgebraicGeometry.Scheme.Hom.deRhamCohomologyCup_firstChernClass_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/LogPoles/CupFirstChernClassVanishing.lean, line 173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/LogPoles/CupFirstChernClassVanishing.lean#L173).

> **Stacks Project, Tag 0FMX.** Let `p : X ⟶ S` be a morphism of schemes and let `Y ⊆ X` be an
> effective Cartier divisor for which the de Rham complex of log poles is defined over `S`. If a
> class `b ∈ H^m_{dR}(X/S)` restricts to zero on `Y`, then
>
> `c₁^{dR}(𝒪_X(Y)) ∪ b = 0`
>
> in `H^{2 + m}_{dR}(X/S)`. The restriction of `b` is its image under the pullback map
> `H^m_{dR}(X/S) ⟶ H^m_{dR}(Y/S)` of the closed immersion `Y ⟶ X`.

```lean
theorem deRhamCohomologyCup_firstChernClass_eq_zero (hlog : p.HasLogPolesDeRhamComplex Y)
    (m : ℤ)
    (b : SheafOfModules.deRhamCohomology (deRhamAlgebras p)
      (SheafOfModules.deRhamDifferential (deRhamAlgebras p)) m)
    (hb : (deRhamCohomologyPullback Y.subschemeι p (Y.subschemeι ≫ p) (𝟙 S)
      (Category.comp_id _).symm m).hom
        ((SheafOfModules.deRhamCohomologyAbelianIsoDeRhamCohomology (deRhamAlgebras p)
          (SheafOfModules.deRhamDifferential (deRhamAlgebras p)) m).inv.hom b) = 0) :
    SheafOfModules.deRhamCohomologyCup (deRhamAlgebras p)
        (SheafOfModules.deRhamDifferential (deRhamAlgebras p)) 2 m
        (SheafOfModules.deRhamCohomologyFirstChernClass (X := X.toRingedSpace) (deRhamAlgebras p)
          (SheafOfModules.deRhamDifferential (deRhamAlgebras p))
          (Stacks.Divisors.invertibleSheaf' Y) inferInstance) b = 0
```

## Tag 0FMY, a lemma

[Tag 0FMY](https://stacks.math.columbia.edu/tag/0FMY) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.hasLogPolesDeRhamComplex_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/LogPoles/SmoothDivisor.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/LogPoles/SmoothDivisor.lean#L132).

> **Stacks Project, Tag 0FMY.** Let `X ⟶ T ⟶ S` be morphisms of schemes and let `Y ⊆ X` be an
> effective Cartier divisor, recorded by its ideal sheaf `I`.  If both `X ⟶ T` and `Y ⟶ T` are
> smooth, then the de Rham complex of log poles is defined for `Y ⊆ X` over `S`.

```lean
theorem hasLogPolesDeRhamComplex_of_smooth {X T S : Scheme.{u}} (h : X ⟶ T) (g : T ⟶ S)
    (I : X.IdealSheafData) (hI : Stacks.Divisors.IsEffectiveCartierDivisor I)
    [Smooth h] [Smooth (I.subschemeι ≫ h)] :
    (h ≫ g).HasLogPolesDeRhamComplex I
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 50.15, Tag 0FMU](https://stacks.math.columbia.edu/tag/0FMU)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
