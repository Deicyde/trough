---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.Hom.cotangentComplex, AlgebraicGeometry.Scheme.Hom.cotangentComplexDerived, AlgebraicGeometry.Scheme.Hom.affineCotangentComparison_spec, Stacks.AffineCotangentSheaf.affineCotangentComparison_restriction, AlgebraicGeometry.SchemeOverRing.constantComparison, AlgebraicGeometry.SchemeOverRing.isIso_constantComparison_iff, AlgebraicGeometry.SchemeOverRing.isIso_constantComparison
statement: formalized
proof: formalized
---

# 92.24 The cotangent complex of a morphism of schemes

Section 92.24 of the Stacks Project, [Tag 08T1](https://stacks.math.columbia.edu/tag/08T1). 3 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08T2, a definition

[Tag 08T2](https://stacks.math.columbia.edu/tag/08T2) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.cotangentComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SchemeCotangentComplex.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SchemeCotangentComplex.lean#L116).

> **Stacks 08T2.** The cotangent complex `L_{X/Y}` of a morphism of schemes `f : X ⟶ Y`: the
> cotangent complex of `f` read as a morphism of the Zariski ringed topoi of `X` and `Y`, a
> complex of sheaves of `𝒪_X`-modules.

```lean
noncomputable def cotangentComplex :
    CochainComplex
      (Sheaf.targetModules (Opens.grothendieckTopology ↥X) X.zariskiRingedTopos.O) ℤ
```

**`AlgebraicGeometry.Scheme.Hom.cotangentComplexDerived`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SchemeCotangentComplex.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SchemeCotangentComplex.lean#L124). The attribute's comment: “the derived object”.

> **Stacks 08T2.** The cotangent complex `L_{X/Y}` of a morphism of schemes, regarded as an
> object of the derived category of sheaves of `𝒪_X`-modules.

```lean
noncomputable abbrev cotangentComplexDerived
    [HasDerivedCategory.{u} (Sheaf.targetModules (Opens.grothendieckTopology ↥X)
      X.zariskiRingedTopos.O)] :
    DerivedCategory
      (Sheaf.targetModules (Opens.grothendieckTopology ↥X) X.zariskiRingedTopos.O)
```

## Tag 08T3, a lemma

[Tag 08T3](https://stacks.math.columbia.edu/tag/08T3) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.affineCotangentComparison_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/AffineCotangentComparisonIsIso.lean, line 251](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SheavesOfRings/AffineCotangentComparisonIsIso.lean#L251). The attribute's comment: “the whole lemma, in one covering statement: (1) the canonical map, pinned as the adjunct under the tilde-Gamma adjunction of the canonical map L\_\{B/A} -> Gamma(L\_\{X/Y}|\_U) built from A -> (f^\{-1}O\_Y)(U) and Remark 08SX; (2) it is an isomorphism in D(O\_U); (3) it is compatible with restriction to smaller affine opens U' of X and opens V' of Y. Hypotheses: exactly the source's, U and V affine with f(U) inside V”.

> **Stacks Project, Tag 08T3.**
>
> Let `f : X ⟶ Y` be a morphism of schemes and let `U = Spec B ⊂ X` and `V = Spec A ⊂ Y` be
> affine opens with `f(U) ⊂ V`, so that `B = 𝒪_X(U)` and `A = 𝒪_Y(V)`. The map of complexes
> `AlgebraicGeometry.Scheme.Hom.affineCotangentComparison f hU e : ~(L_{B/A}) ⟶ L_{X/Y}|_U`
> satisfies the three assertions of the lemma:
>
> 1. it is **the canonical map**: in every degree it is the adjunct, under the universal property
>    of `~` (Tag 01I7), of the canonical map `L_{B/A} ⟶ Γ(L_{X/Y}|_U)`,
>    `AlgebraicGeometry.Scheme.Hom.gammaCotangentComparison`, which is the map
>    `L_{B/A} ⟶ L_{𝒪_X(U)/(f⁻¹𝒪_Y)(U)}` induced by `A ⟶ (f⁻¹𝒪_Y)(U)` followed by the canonical map
>    `L_{𝒪_X(U)/(f⁻¹𝒪_Y)(U)} ⟶ L_{X/Y}(U)` of Remark 08SX;
> 2. it is **an isomorphism in `D(𝒪_U)`**;
> 3. it is **compatible with restricting to smaller affine opens** `U' ⊂ U` of `X` and `V' ⊂ V` of
>    `Y` with `f(U') ⊂ V'`: the square formed by the canonical maps for `(U, V)` and `(U', V')`
>    and the two restriction maps commutes.

```lean
theorem affineCotangentComparison_spec [HasDerivedCategory.{w} (Spec Γ(X, U)).Modules] :
    (∀ j : ℤ, (tilde.adjunction (R := Γ(X, U))).homEquiv _ _
        ((affineCotangentComparison f hU e).f j) = (gammaCotangentComparison f hU e).f j) ∧
    IsIso (DerivedCategory.Q.map (affineCotangentComparison f hU e)) ∧
    ∀ {U' : X.Opens} (hU' : IsAffineOpen U') {V' : Y.Opens} (e' : U' ≤ f ⁻¹ᵁ V')
      (hUle : U' ≤ U) (hVle : V' ≤ V),
      affineCotangentComparison f hU e ≫
          Stacks.AffineCotangentSheaf.restrictedCotangentRestriction f hU hU' hUle =
        Stacks.AffineCotangentSheaf.tildeCotangentRestriction f e e' hUle hVle ≫
          ((Scheme.Modules.pushforward
            (Stacks.AffineCotangentSheaf.specRestriction hUle)).mapHomologicalComplex
              (ComplexShape.up ℤ)).map (affineCotangentComparison f hU' e')
```

**`Stacks.AffineCotangentSheaf.affineCotangentComparison_restriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/AffineCotangentRestrictionSheaf.lean, line 396](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SheavesOfRings/AffineCotangentRestrictionSheaf.lean#L396). The attribute's comment: “ASSERTION 3 ONLY, and AS SHEAVES: the canonical map of this tag, ~(L\_\{O\_X(U)/O\_Y(V)}) -> L\_\{X/Y}|\_U, is compatible with restriction along affine opens U' <= U and opens V' <= V, as an EQUALITY of maps of complexes of sheaves of O\_\{Spec O\_X(U)}-modules -- not a Nonempty and not the sectionwise statement. The two vertical maps of the square are tildeCotangentRestriction and restrictedCotangentRestriction; the latter is the genuine sheaf restriction map, which restrictionUnit\_app\_app proves acts on sections as presheaf.map (homOfLE \_).op. CARRIED: IsAffineOpen U and IsAffineOpen U', which are the source's own hypotheses -- the comparison map is only defined for an affine open -- and nothing else; IsAffineOpen V and IsAffineOpen V' are NOT carried, so this is more general than the source in the base variables. ASSERTIONS 1 AND 2 ARE NOT CLAIMED HERE”.

> **Stacks 08T3, assertion 3, as sheaves.** For a morphism of schemes `f : X ⟶ Y`, affine opens
> `U' ≤ U` of `X` and opens `V' ≤ V` of `Y` with `f(U) ⊂ V` and `f(U') ⊂ V'`, the canonical map
> `~(L_{𝒪_X(U)/𝒪_Y(V)}) ⟶ L_{X/Y}|_U` of Tag 08T3 is compatible with restriction: writing
> `ρ : Spec 𝒪_X(U') ⟶ Spec 𝒪_X(U)` for the morphism induced by restriction, the square formed by
> the two comparison maps and the two restriction maps commutes as an equality of maps of complexes
> of `𝒪_{Spec 𝒪_X(U)}`-modules.

```lean
theorem affineCotangentComparison_restriction (e : U ≤ f ⁻¹ᵁ V) (e' : U' ≤ f ⁻¹ᵁ V')
    (hUle : U' ≤ U) (hVle : V' ≤ V) :
    affineCotangentComparison f hU e ≫ restrictedCotangentRestriction f hU hU' hUle =
      tildeCotangentRestriction f e e' hUle hVle ≫
        ((Scheme.Modules.pushforward (specRestriction hUle)).mapHomologicalComplex
          (ComplexShape.up ℤ)).map (affineCotangentComparison f hU' e')
```

## Tag 08V6, a lemma

[Tag 08V6](https://stacks.math.columbia.edu/tag/08V6) in the Stacks Project.

**`AlgebraicGeometry.SchemeOverRing.constantComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SchemeOverRing.lean, line 226](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SchemeOverRing.lean#L226). The attribute's comment: “the canonical comparison L\_\{O\_X/const Lambda} ⟶ L\_\{X/Spec Lambda} of the tag, constructed unconditionally as the change-of-base arrow of Tag 08SZ for the tower const Lambda ⟶ p^-1 O\_\{Spec Lambda} ⟶ O\_X, with the constant sheaf being Mathlib's constantSheaf and the target the cotangent complex of p of Tag 08UU (cotangentComplexRelative\_eq). That it is an ISOMORPHISM is NOT claimed by this declaration; see isIso\_constantComparison\_iff and the module documentation”.

> The canonical comparison `L_{𝒪_X/Λ̲} ⟶ L_{X/Spec Λ}`: the change-of-base-ring map of the tower
> `Λ̲ ⟶ p⁻¹𝒪_{Spec Λ} ⟶ 𝒪_X`.

```lean
def constantComparison : cotangentComplexConstant Λ p ⟶ cotangentComplexRelative Λ p
```

**`AlgebraicGeometry.SchemeOverRing.isIso_constantComparison_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SchemeOverRing.lean, line 245](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SchemeOverRing.lean#L245). The attribute's comment: “the REDUCTION of the tag, not the tag: an IFF between the comparison being an isomorphism in D(O\_X) and the vanishing of the first vertex of the fundamental triangle, the pullback of the source's L\_q. The vanishing -- the source's Tag 08T0 plus Tag 08R2 step -- is NOT proved here and is not assumed either; it is the right-hand side. ONE carried hypothesis, exactly the one Tag 08SZ carries: the short exact sequence `S`/`hS` realizing the two canonical arrows (`hf`, `hg`) on the three vertices (`e1`, `e2`, `e3`), the sheaf-level analogue of Tag 08SD, absent from this library. See the module documentation”.

> Granted the short exact sequence Tag 08SZ carries for the tower `Λ̲ ⟶ p⁻¹𝒪_{Spec Λ} ⟶ 𝒪_X`, the
> canonical comparison `L_{𝒪_X/Λ̲} ⟶ L_{X/Spec Λ}` is an isomorphism in `D(𝒪_X)` exactly when the
> first vertex `L_{p⁻¹𝒪_{Spec Λ}/Λ̲} ⊗_{p⁻¹𝒪_{Spec Λ}} 𝒪_X` of the fundamental triangle vanishes
> there.
>
> The hypothesis carried is the one Tag 08SZ carries, in the same shape: a short complex `S` of
> complexes of sheaves of `𝒪_X`-modules that is short exact (`hS`), whose three terms are the three
> vertices (`e₁`, `e₂`, `e₃`) and whose two maps are the two canonical arrows (`hf`, `hg`).

```lean
theorem isIso_constantComparison_iff
    [HasDerivedCategory.{t} (CategoryTheory.Sheaf.targetModules.{u, u, u}
      (Opens.grothendieckTopology ↥X) (structureSheafOfSite X))]
    (S : ShortComplex (CochainComplex
      (CategoryTheory.Sheaf.targetModules.{u, u, u} (Opens.grothendieckTopology ↥X)
        (structureSheafOfSite X)) ℤ))
    (hS : S.ShortExact) (e₁ : S.X₁ ≅ pullbackCotangentComplex Λ p)
    (e₂ : S.X₂ ≅ cotangentComplexConstant Λ p)
    (e₃ : S.X₃ ≅ cotangentComplexRelative Λ p)
    (hf : S.f = e₁.hom ≫ CategoryTheory.Sheaf.towerCotangentBaseChange.{u, u, u}
      (Opens.grothendieckTopology ↥X) (constantToPullback Λ p)
      (pullbackStructureMap Λ p) ≫ e₂.inv)
    (hg : S.g = e₂.hom ≫ constantComparison Λ p ≫ e₃.inv) :
    IsIso ((DerivedCategory.Q (C := CategoryTheory.Sheaf.targetModules.{u, u, u}
          (Opens.grothendieckTopology ↥X) (structureSheafOfSite X))).map
        (constantComparison Λ p)) ↔
      IsZero ((DerivedCategory.Q (C := CategoryTheory.Sheaf.targetModules.{u, u, u}
        (Opens.grothendieckTopology ↥X) (structureSheafOfSite X))).obj
          (pullbackCotangentComplex Λ p))
```

**`AlgebraicGeometry.SchemeOverRing.isIso_constantComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SchemeOverRingComparison.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SchemeOverRingComparison.lean#L227). The attribute's comment: “L\_\{X/Spec Lambda} = L\_\{O\_X/const Lambda} in D(O\_X) for a scheme X over a ring Lambda, const Lambda the constant sheaf with value Lambda on X: the canonical comparison L\_\{O\_X/const Lambda} ⟶ L\_\{X/Spec Lambda} (constantComparison) is an isomorphism in D(O\_X)”.

> **Stacks Project, Tag 08V6.** Let `Λ` be a ring and let `X` be a scheme over `Λ`. Then
> `L_{X/Spec Λ} = L_{𝒪_X/Λ̲}` in `D(𝒪_X)`, where `Λ̲` is the constant sheaf with value `Λ` on `X`:
> the canonical comparison `L_{𝒪_X/Λ̲} ⟶ L_{X/Spec Λ}`, the change-of-base map of the tower
> `Λ̲ ⟶ p⁻¹𝒪_{Spec Λ} ⟶ 𝒪_X`, is an isomorphism in the derived category.

```lean
theorem isIso_constantComparison
    [HasDerivedCategory.{t} (CategoryTheory.Sheaf.targetModules.{u, u, u}
      (Opens.grothendieckTopology ↥X) (structureSheafOfSite X))] :
    IsIso ((DerivedCategory.Q (C := CategoryTheory.Sheaf.targetModules.{u, u, u}
      (Opens.grothendieckTopology ↥X) (structureSheafOfSite X))).map (constantComparison Λ p))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 92.24, Tag 08T1](https://stacks.math.columbia.edu/tag/08T1)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
