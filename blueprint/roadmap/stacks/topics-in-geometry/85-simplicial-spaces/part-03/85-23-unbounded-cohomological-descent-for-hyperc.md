---
declaration: section
origin: cited
lean: Stacks.Cohomology.CohomologicalDescent.IsStableUnderRestriction, Stacks.Cohomology.CohomologicalDescent.IsLocalOnCoverings, Stacks.Cohomology.CohomologicalDescent.LocalCohomologicalBound, AlgebraicGeometry.Space.isStableUnderRestriction_spacesEtaleQuasicoherentSlices, AlgebraicGeometry.Space.spacesEtaleQuasicoherent_localSerre, AlgebraicGeometry.Scheme.LocallyFiniteTypeEtale.localSerre_of_finite, AlgebraicGeometry.Scheme.LocallyFiniteTypeEtale.localSerre_of_isSepClosed, AlgebraicGeometry.Scheme.Hom.etaleCohomologyBound
statement: formalized
proof: formalized
---

# 85.23 Unbounded cohomological descent for hypercoverings

Section 85.23 of the Stacks Project, [Tag 0DC1](https://stacks.math.columbia.edu/tag/0DC1). 6 tags here are carried by 20 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DC2, an item

[Tag 0DC2](https://stacks.math.columbia.edu/tag/0DC2) in the Stacks Project.

**`Stacks.Cohomology.CohomologicalDescent.IsStableUnderRestriction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/LocalSerreFamily.lean, line 100](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/LocalSerreFamily.lean#L100). The attribute's comment: “condition (1): restriction along U ⟶ V sends A\_V into A\_U”.

> The first condition on a family of subcategories `A_U` of the categories of modules on the
> localizations of a ringed site: for every morphism `f : U ⟶ V` of the site, the restriction functor
> from modules on `C/V` to modules on `C/U` sends `A_V` into `A_U`.

```lean
def IsStableUnderRestriction (A : SliceProperties X) : Prop
```

## Tag 0DC3, an item

[Tag 0DC3](https://stacks.math.columbia.edu/tag/0DC3) in the Stacks Project.

**`Stacks.Cohomology.CohomologicalDescent.IsLocalOnCoverings`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/LocalSerreFamily.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/LocalSerreFamily.lean#L109). The attribute's comment: “condition (2): membership in A\_U is local on coverings of U”.

> The second condition on a family of subcategories `A_U` of the categories of modules on the
> localizations of a ringed site: for every covering `{U_i ⟶ U}` of the site, a module on `C/U` lies
> in `A_U` if and only if its restriction to `C/U_i` lies in `A_{U_i}` for every `i`.

```lean
def IsLocalOnCoverings (A : SliceProperties X) : Prop
```

## Tag 0DC4, an item

[Tag 0DC4](https://stacks.math.columbia.edu/tag/0DC4) in the Stacks Project.

**`Stacks.Cohomology.CohomologicalDescent.LocalCohomologicalBound`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/LocalSerreFamily.lean, line 121](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/LocalSerreFamily.lean#L121). The attribute's comment: “condition (3): a locally covering set, with coverings acyclic for A\_V above d\_V”.

> The third condition on a family of subcategories `A_U` of the categories of modules on the
> localizations of a ringed site: there is a set `B` of objects of the site such that every object
> has a covering by members of `B`, and every `V` in `B` carries an integer `d_V` and a cofinal
> system of coverings of `V` on whose members the cohomology of every module of `A_V` vanishes in
> degrees above `d_V`. The set, the bounds and the covering systems are stored as chosen data.

```lean
structure LocalCohomologicalBound (A : SliceProperties X)
```

## Tag 0DC5, an example

[Tag 0DC5](https://stacks.math.columbia.edu/tag/0DC5) in the Stacks Project.

**`AlgebraicGeometry.Space.isStableUnderRestriction_spacesEtaleQuasicoherentSlices`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SpacesEtaleQuasicoherentLocalSerre.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SpacesEtaleQuasicoherentLocalSerre.lean#L108). The attribute's comment: “property (1), i.e. condition 0DC2 for the family A\_U of quasi-coherent modules on the slices of the spaces-etale site of an algebraic space: restriction along a morphism U -> V of the site sends A\_V into A\_U. NOT covered by this declaration: property (2) (condition 0DC3, locality on coverings), property (3) (condition 0DC4, the set B = Ob(C) with d\_V = 0 and the cofinal affine coverings), and the standing assumption that each A\_U is a weak Serre subcategory; no LocalSerreFamily is assembled. See the module documentation for why each of those is unreachable in this development -- in particular the positive-degree vanishing of the cohomology of a quasi-coherent module on an affine object of the etale site, the clause of Stacks 03DW that the source's reference to Stacks 01XB and Stacks 071Y supplies, is proved nowhere here and also blocks Stacks 0720 and Stacks 08EX”.

> **Stability under restriction.**  Let `X` be an algebraic space over a scheme `S` and let
> `C = X_{spaces, étale}` be the étale site on the algebraic spaces étale over `X`, with its
> structure sheaf.  Then the family which assigns to an object `U` of `C` the quasi-coherent modules
> on `C/U` is stable under restriction: for a morphism `f : U ⟶ V` of `C`, the restriction functor
> from modules on `C/V` to modules on `C/U` sends quasi-coherent modules to quasi-coherent modules.
>
> This is condition (1) of Tag 0DC1, i.e. the condition
> `Stacks.Cohomology.CohomologicalDescent.IsStableUnderRestriction` of Tag 0DC2, for this family.

```lean
theorem isStableUnderRestriction_spacesEtaleQuasicoherentSlices :
    Stacks.Cohomology.CohomologicalDescent.IsStableUnderRestriction
      (spacesEtaleRingedSite B S hS X) (spacesEtaleQuasicoherentSlices B S hS X)
```

**`AlgebraicGeometry.Space.spacesEtaleQuasicoherent_localSerre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SpacesEtaleQuasicoherentLocalSerreFamily.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SpacesEtaleQuasicoherentLocalSerreFamily.lean#L119).

> **Stacks 0DC5.**  Let `S` be a scheme, `X` an algebraic space over `S`,
> `C = X_{spaces, étale}` with its structure sheaf, and `A_U` the quasi-coherent `𝒪_U`-modules on
> the slice `C/U`.  Then each `A_U` is a weak Serre subcategory, and the three conditions of
> Stacks 0DC1 hold: restriction along a morphism `U ⟶ V` of `C` sends `A_V` into `A_U`
> (Stacks 0DC2); membership in `A_U` is local on coverings of `U` (Stacks 0DC3); and condition
> (3) (Stacks 0DC4) holds with `B = Ob(C)`, `d_V = 0` and `Cov_V` the coverings `{V_i ⟶ V}` with
> every `V_i` affine, that is, for such a covering, every `p > 0` and every `F` in `A_V`,
> `H^p(V_i, F) = 0`.

```lean
theorem spacesEtaleQuasicoherent_localSerre :
    (∀ U, (spacesEtaleQuasicoherentSlices B S hS X U).IsWeakSerreClass) ∧
      IsStableUnderRestriction (spacesEtaleRingedSite B S hS X)
        (spacesEtaleQuasicoherentSlices B S hS X) ∧
      IsLocalOnCoverings (spacesEtaleRingedSite B S hS X)
        (spacesEtaleQuasicoherentSlices B S hS X) ∧
      ∃ b : LocalCohomologicalBound (spacesEtaleRingedSite B S hS X)
          (spacesEtaleQuasicoherentSlices B S hS X),
        b.B = Set.univ ∧ (∀ V hV, b.degreeBound V hV = 0) ∧
          ∀ V hV (𝒰 : PreZeroHypercover.{u + 1} V), (b.coverings V hV).cov 𝒰 ↔
            𝒰.sieve₀ ∈ (spacesEtaleRingedSite B S hS X).J V ∧
              ∀ i, IsAffineSpace B S hS (𝒰.X i).obj.left.1
```

## Tag 0DC6, an example

[Tag 0DC6](https://stacks.math.columbia.edu/tag/0DC6) in the Stacks Project.

**`AlgebraicGeometry.Scheme.LocallyFiniteTypeEtale.localSerre_of_finite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/LocallyFiniteTypeFieldLocalSerreFamily.lean, line 262](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Etale/LocallyFiniteTypeFieldLocalSerreFamily.lean#L262). The attribute's comment: “type (1): S the spectrum of a finite field”.

> **Stacks 0DC6, type (1): `S` the spectrum of a finite field.** Let `S ≅ Spec k` with `k` a
> finite field, let `Λ` be a finite ring whose order is invertible on `S`, let `C` be the category
> of schemes locally of finite type over `S` with the étale topology, ringed by the constant sheaf
> `Λ` (`ringedSite S Λ`), and let `A_U` be the category of all sheaves of `Λ`-modules on `C/U`.
> Then the conditions (1), (2), (3) of Stacks 0DC1 hold: each `A_U` is a weak Serre subcategory,
> restriction along `U ⟶ V` sends `A_V` into `A_U` (Stacks 0DC2), membership in `A_U` is local on
> coverings (Stacks 0DC3), and (Stacks 0DC4) with `B` the set of quasi-compact objects, for
> `V ∈ B` the integer `d_V = 1 + 2 dim(S) + sup_{v ∈ V} (trdeg_{κ(s)} κ(v) + 2 dim 𝒪_{V, v})`, and
> `Cov_V` the étale coverings `{V_i ⟶ V}` with every `V_i` quasi-compact, `H^p(V_i, F) = 0` for
> every `{V_i ⟶ V}` in `Cov_V`, every `p > d_V` and every `F` in `A_V`.

```lean
theorem localSerre_of_finite (k : Type u) [Field k] [Finite k] (e : S ≅ Spec (.of k)) :
    ∀ (Λ : Type u) [CommRing Λ] [Finite Λ], IsUnit (Nat.card Λ : Γ(S, ⊤)) →
      (∀ U, (allModules S Λ U).IsWeakSerreClass) ∧
        IsStableUnderRestriction (ringedSite S Λ) (allModules S Λ) ∧
        IsLocalOnCoverings (ringedSite S Λ) (allModules S Λ) ∧
        ∃ b : LocalCohomologicalBound (ringedSite S Λ) (allModules S Λ),
          b.B = {V | IsQuasiCompact ((liftedEquiv S).inverse.obj V)} ∧
          (∀ V hV, ∃ d : ℕ, b.degreeBound V hV = d ∧
            ((liftedEquiv S).inverse.obj V).obj.hom.etaleCohomologyBound = d) ∧
          ∀ V hV (𝒰 : PreZeroHypercover.{u + 1} V),
            (b.coverings V hV).cov 𝒰 ↔ IsQuasiCompactEtaleCovering 𝒰
```

**`AlgebraicGeometry.Scheme.LocallyFiniteTypeEtale.localSerre_of_isSepClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/LocallyFiniteTypeFieldLocalSerreFamily.lean, line 287](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Etale/LocallyFiniteTypeFieldLocalSerreFamily.lean#L287). The attribute's comment: “type (2): S the spectrum of a separably closed field”.

> **Stacks 0DC6, type (2): `S` the spectrum of a separably closed field.** Let `S ≅ Spec k`
> with `k` a separably closed field, let `Λ` be a finite ring whose order is invertible on `S`, let
> `C` be the category of schemes locally of finite type over `S` with the étale topology, ringed by
> the constant sheaf `Λ` (`ringedSite S Λ`), and let `A_U` be the category of all sheaves of
> `Λ`-modules on `C/U`. Then the conditions (1), (2), (3) of Stacks 0DC1 hold: each `A_U` is a weak
> Serre subcategory, restriction along `U ⟶ V` sends `A_V` into `A_U` (Stacks 0DC2), membership in
> `A_U` is local on coverings (Stacks 0DC3), and (Stacks 0DC4) with `B` the set of quasi-compact
> objects, for `V ∈ B` the integer
> `d_V = 1 + 2 dim(S) + sup_{v ∈ V} (trdeg_{κ(s)} κ(v) + 2 dim 𝒪_{V, v})`, and `Cov_V` the étale
> coverings `{V_i ⟶ V}` with every `V_i` quasi-compact, `H^p(V_i, F) = 0` for every
> `{V_i ⟶ V}` in `Cov_V`, every `p > d_V` and every `F` in `A_V`.

```lean
theorem localSerre_of_isSepClosed (k : Type u) [Field k] [IsSepClosed k]
    (e : S ≅ Spec (.of k)) :
    ∀ (Λ : Type u) [CommRing Λ] [Finite Λ], IsUnit (Nat.card Λ : Γ(S, ⊤)) →
      (∀ U, (allModules S Λ U).IsWeakSerreClass) ∧
        IsStableUnderRestriction (ringedSite S Λ) (allModules S Λ) ∧
        IsLocalOnCoverings (ringedSite S Λ) (allModules S Λ) ∧
        ∃ b : LocalCohomologicalBound (ringedSite S Λ) (allModules S Λ),
          b.B = {V | IsQuasiCompact ((liftedEquiv S).inverse.obj V)} ∧
          (∀ V hV, ∃ d : ℕ, b.degreeBound V hV = d ∧
            ((liftedEquiv S).inverse.obj V).obj.hom.etaleCohomologyBound = d) ∧
          ∀ V hV (𝒰 : PreZeroHypercover.{u + 1} V),
            (b.coverings V hV).cov 𝒰 ↔ IsQuasiCompactEtaleCovering 𝒰
```

**`AlgebraicGeometry.Scheme.Hom.etaleCohomologyBound`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/LocallyFiniteTypeSite.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Etale/LocallyFiniteTypeSite.lean#L77). The attribute's comment: “the bound d\_V”.

> The degree `1 + 2 dim S + sup_v (trdeg_{κ(s)} κ(v) + 2 dim 𝒪_{X, v})` attached to a
> morphism `f : X ⟶ S`, where `s` is the image of `v` under `f`.

```lean
public def Hom.etaleCohomologyBound {X S : Scheme.{u}} (f : X ⟶ S) : WithBot ℕ∞
```

**`AlgebraicGeometry.Scheme.LocallyFiniteTypeEtale`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/LocallyFiniteTypeSite.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Etale/LocallyFiniteTypeSite.lean#L91). The attribute's comment: “the site C of schemes locally of finite type over S”.

> The schemes locally of finite type over `S`, as a full subcategory of the schemes
> over `S`.

```lean
public abbrev LocallyFiniteTypeEtale (S : Scheme.{u}) : Type _
```

**`AlgebraicGeometry.Scheme.LocallyFiniteTypeEtale.topology`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/LocallyFiniteTypeSite.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Etale/LocallyFiniteTypeSite.lean#L103). The attribute's comment: “the étale topology on C”.

> The étale topology on the schemes locally of finite type over `S`: the coarsest topology
> containing every sieve whose underlying family of schemes generates an étale covering.

```lean
public abbrev topology (S : Scheme.{u}) : GrothendieckTopology (LocallyFiniteTypeEtale S)
```

**`AlgebraicGeometry.Scheme.LocallyFiniteTypeEtale.IsQuasiCompact`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/LocallyFiniteTypeSite.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Etale/LocallyFiniteTypeSite.lean#L111). The attribute's comment: “the set B of quasi-compact objects”.

> An object of the locally-finite-type étale site is quasi-compact when the scheme
> underlying it is.

```lean
public def IsQuasiCompact (V : LocallyFiniteTypeEtale S) : Prop
```

**`AlgebraicGeometry.Scheme.LocallyFiniteTypeEtale.IsQuasiCompactCovering`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/LocallyFiniteTypeSite.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Etale/LocallyFiniteTypeSite.lean#L116). The attribute's comment: “the coverings Cov\_V”.

> A family `{U i ⟶ V}` in the locally-finite-type étale site is a distinguished covering of
> `V` when every `U i` is quasi-compact and the family generates a covering sieve.

```lean
public def IsQuasiCompactCovering {V : LocallyFiniteTypeEtale S} {I : Type w}
    (U : I → LocallyFiniteTypeEtale S) (f : ∀ i, U i ⟶ V) : Prop
```

**`AlgebraicGeometry.Scheme.LocallyFiniteTypeEtale.exists_isQuasiCompactCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/LocallyFiniteTypeSite.lean, line 174](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Etale/LocallyFiniteTypeSite.lean#L174). The attribute's comment: “every object of C is covered by members of B”.

> Every scheme locally of finite type over `S` has an étale covering whose members are
> quasi-compact.

```lean
public theorem exists_isQuasiCompactCovering (V : LocallyFiniteTypeEtale S) :
    ∃ (I : Type u) (U : I → LocallyFiniteTypeEtale S) (f : ∀ i, U i ⟶ V),
      IsQuasiCompactCovering U f
```

**`AlgebraicGeometry.Scheme.LocallyFiniteTypeEtale.exists_isQuasiCompactCovering_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/LocallyFiniteTypeSite.lean, line 182](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Etale/LocallyFiniteTypeSite.lean#L182). The attribute's comment: “Cov\_V is a cofinal system of coverings”.

> Every étale covering sieve of a scheme locally of finite type over `S` is refined by an
> étale covering whose members are quasi-compact.

```lean
public theorem exists_isQuasiCompactCovering_le (V : LocallyFiniteTypeEtale S) (R : Sieve V)
    (hR : R ∈ topology S V) :
    ∃ (I : Type (u + 1)) (U : I → LocallyFiniteTypeEtale S) (f : ∀ i, U i ⟶ V),
      IsQuasiCompactCovering U f ∧ Sieve.generate (Presieve.ofArrows U f) ≤ R
```

**`AlgebraicGeometry.Scheme.IsUnboundedDescentEtaleBase`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/LocallyFiniteTypeSiteBound.lean, line 175](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Etale/LocallyFiniteTypeSiteBound.lean#L175). The attribute's comment: “the four types of base scheme S”.

> **The types of base scheme of Stacks 0DC6.**  `S` is the spectrum of a finite field, the
> spectrum of a separably closed field, the spectrum of a strictly henselian Noetherian local ring,
> or the spectrum of a henselian Noetherian local ring with finite residue field.

```lean
def IsUnboundedDescentEtaleBase (S : Scheme.{u}) : Prop
```

**`AlgebraicGeometry.Scheme.IsUnboundedDescentEtaleBase.exists_natCast_eq_etaleCohomologyBound`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/LocallyFiniteTypeSiteBound.lean, line 211](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Etale/LocallyFiniteTypeSiteBound.lean#L211). The attribute's comment: “d\_V is an integer for V in B”.

> **The bound `d_V` of Stacks 0DC6 is an integer.**  For `S` of one of the four types of
> Stacks 0DC6 and `V` a quasi-compact scheme locally of finite type over `S`, the bound
> `d_V = 1 + 2 dim(S) + sup_{v ∈ V} (trdeg_{κ(s)} κ(v) + 2 dim 𝒪_{V, v})` is a natural number.

```lean
theorem exists_natCast_eq_etaleCohomologyBound {S : Scheme.{u}}
    (hS : IsUnboundedDescentEtaleBase S) (V : LocallyFiniteTypeEtale S)
    (hV : LocallyFiniteTypeEtale.IsQuasiCompact V) :
    ∃ d : ℕ, V.obj.hom.etaleCohomologyBound = d
```

**`AlgebraicGeometry.Scheme.LocallyFiniteTypeEtale.localSerre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/LocallyFiniteTypeSiteGabberUnconditional.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Etale/LocallyFiniteTypeSiteGabberUnconditional.lean#L103). The attribute's comment: “all four types”.

> **Stacks 0DC6.** Let `S` be the spectrum of a finite field, of a separably closed field, of a
> strictly henselian Noetherian local ring, or of a henselian Noetherian local ring with finite
> residue field, and let `Λ` be a finite ring whose order is invertible on `S`. On the ringed site
> `(C, Λ)` of schemes locally of finite type over `S`, the family `A_U` of all sheaves of
> `Λ`-modules satisfies conditions (1), (2), (3) of Stacks 0DC1, with `B` the quasi-compact
> objects, `d_V = 1 + 2 dim(S) + sup_{v ∈ V} (trdeg_{κ(s)} κ(v) + 2 dim 𝒪_{V, v})` and `Cov_V`
> the étale coverings of `V` by quasi-compact objects.

```lean
theorem localSerre (Λ : Type u) [CommRing Λ] [Finite Λ]
    (hS : IsUnboundedDescentEtaleBase S) (hn : IsUnit (Nat.card Λ : Γ(S, ⊤))) :
    (∀ U, (allModules S Λ U).IsWeakSerreClass) ∧
      IsStableUnderRestriction (ringedSite S Λ) (allModules S Λ) ∧
      IsLocalOnCoverings (ringedSite S Λ) (allModules S Λ) ∧
      ∃ b : LocalCohomologicalBound (ringedSite S Λ) (allModules S Λ),
        b.B = {V | IsQuasiCompact ((liftedEquiv S).inverse.obj V)} ∧
        (∀ V hV, ∃ d : ℕ, b.degreeBound V hV = d ∧
          ((liftedEquiv S).inverse.obj V).obj.hom.etaleCohomologyBound = d) ∧
        ∀ V hV (𝒰 : PreZeroHypercover.{u + 1} V),
          (b.coverings V hV).cov 𝒰 ↔ IsQuasiCompactEtaleCovering 𝒰
```

## Tag 0DC7, a lemma

[Tag 0DC7](https://stacks.math.columbia.edu/tag/0DC7) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.exists_derivedPullbackEquivalence_localSerreFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/HypercoveringUnboundedEquivalence.lean, line 167](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/HypercoveringUnboundedEquivalence.lean#L167).

> **Stacks 0DC7.** Let `(C, O_C)` be a ringed site with equalizers and fibre products, and let
> `A_U ⊂ Mod(O_U)` be weak Serre subcategories satisfying conditions 0DC2, 0DC3 and 0DC4 (the
> fields of `T : LocalSerreFamily`), with `A ⊂ Mod(O_C)` the modules whose restriction to every
> `C/U` lies in `A_U`. Let `K` be a hypercovering of `C`, let
> `a : ((C/K)_total, O) ⟶ (C, O_C)` be the ringed augmentation of Remark 0D9W, with `O = a⁻¹O_C`,
> and let `A_total ⊂ Mod(O)` be the cartesian `O`-modules `F` whose restriction `F_n` lies in
> `A_{K_n} = ∏_i A_{U_{n,i}}` for every `n`. Then `A_total` is a weak Serre subcategory of
> `Mod(O)`, and `La^*` defines an equivalence
>
> `D_A(O_C) ⟶ D_{A_total}(O)`
>
> with quasi-inverse `Ra_*`: there is an equivalence of the full subcategories of the unbounded
> derived categories on the objects with cohomology in `A`, respectively `A_total`, whose functor
> is the restriction of the derived pullback `La^*` and whose inverse is the restriction of the
> derived direct image `Ra_*`.

```lean
theorem exists_derivedPullbackEquivalence_localSerreFamily :
    (totalLocalSerre J H OC T).IsWeakSerreClass ∧
      ∃ e : (DerivedCategoryB.derivedCategoryB (baseLocalSerre J OC T)).FullSubcategory ≌
          (DerivedCategoryB.derivedCategoryB (totalLocalSerre J H OC T)).FullSubcategory,
        e.functor ⋙ (DerivedCategoryB.derivedCategoryB (totalLocalSerre J H OC T)).ι =
            (DerivedCategoryB.derivedCategoryB (baseLocalSerre J OC T)).ι ⋙
              (RingedToposHom.leftDerivedPullbackOfIsIsoFSharp
                (hypercoveringRingedAugmentation J H OC).totalRingedHom).functor ∧
          e.inverse ⋙ (DerivedCategoryB.derivedCategoryB (baseLocalSerre J OC T)).ι =
            (DerivedCategoryB.derivedCategoryB (totalLocalSerre J H OC T)).ι ⋙
              derivedPushforward (X := (hypercoveringSituation J H).totalRingedTopos
                (hypercoveringRingedAugmentation J H OC).O)
                (Y := (hypercoveringRingedAugmentation J H OC).augmentationRingedTopos)
                (hypercoveringRingedAugmentation J H OC).totalRingedHom
```

**`Stacks.Cohomology.CohomologicalDescent.isWeakSerreClass_cartesianDegreewiseModules`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/HypercoveringUnboundedLocalSerre.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/HypercoveringUnboundedLocalSerre.lean#L123). The attribute's comment: “the class A\_total of cartesian O-modules whose restriction to each simplicial component lies in the prescribed class there is a weak Serre subcategory of Mod(O). Two hypotheses are carried: hflat, left exactness of the pullback of modules along the transition morphism of each face map, which is the hypothesis in the shape this library's Tag 0D7J (2) takes it and is weaker than the source's flatness of the face transitions; and hA, that each A\_n is a weak Serre subcategory. The family A\_n is arbitrary, where the source takes the family A\_\{K\_n} = prod\_i A\_\{U\_\{n,i}} attached to a LocalSerreFamily, i.e. to Tags 0DC2, 0DC3 and 0DC4; assembling that particular family needs the module form of Tag 0D89 and is not available. NOT covered: the equivalence D\_A(O\_C) = D\_\{A\_total}(O), the two assertions that La^* and Ra\_* preserve the classes, and the identification of the two functors of the equivalence -- the unbounded engine of Tag 0D7V is stated for a RingedToposSiteHom and the augmentation of a hypercovering admits no such presentation. NOT covered either: that a^* induces an equivalence A = A\_total, whose descent half needs the covering argument on the slices C/U\_\{n,i}”.

> `A_total` is a weak Serre subcategory of `Mod(O)`. Let `O` be a sheaf of commutative rings on
> the total site of a simplicial-site situation such that the pullback of modules along the
> transition morphism of each face map is left exact, and let `A_n` be a weak Serre subcategory of
> the category of modules on the degree-`n` component, for every `n`. Then the cartesian
> `O`-modules whose restriction to each component lies in the class there form a weak Serre
> subcategory of `Mod(O)`.

```lean
theorem isWeakSerreClass_cartesianDegreewiseModules
    (hflat : ∀ (k : ℕ) (i : Fin (k + 2)),
      PreservesFiniteLimits
        ((S.transitionRingedToposHom O (SimplexCategory.δ i)).toModulesHom.pullbackModules))
    (hA : ∀ n : SimplexCategory, (A n).IsWeakSerreClass) :
    (cartesianDegreewiseModules S O A).IsWeakSerreClass
```

**`Stacks.Cohomology.CohomologicalDescent.isWeakSerreClass_cartesianDegreewiseModules_hypercovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/HypercoveringUnboundedLocalSerre.lean, line 175](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/HypercoveringUnboundedLocalSerre.lean#L175). The attribute's comment: “the class A\_total is a weak Serre subcategory of Mod(O), at the total ringed site of a hypercovering with O = a^\{-1}O\_C, i.e. for the site and structure sheaf of Tag 0D9W. Same two hypotheses as the general form: hflat, left exactness of the pullback of modules along the transition morphism of each face map, and hA, that each A\_n is a weak Serre subcategory; and the same restriction, that the family A\_n is arbitrary rather than the source's prod\_i A\_\{U\_\{n,i}}. None of the derived assertions of the tag are covered here”.

> `A_total` is a weak Serre subcategory, at the total ringed site of a hypercovering. Let `C` be
> a site with equalizers and fibre products, let `O_C` be a sheaf of commutative rings on it and let
> `K` be a hypercovering of `C`; let `a : (Sh((C/K)_total), O) ⟶ (Sh(C), O_C)` be the ringed
> augmentation of Stacks 0D9W, so that `O = a⁻¹O_C`. For a family `A_n` of weak Serre
> subcategories of the categories of modules on the localizations `C/K_n`, the cartesian
> `O`-modules whose restriction `F_n` lies in `A_n` for every `n` form a weak Serre subcategory of
> `Mod(O)`.

```lean
theorem isWeakSerreClass_cartesianDegreewiseModules_hypercovering {C : Type u} [SmallCategory C]
    [CategoryTheory.Limits.HasEqualizers C] [CategoryTheory.Limits.HasPullbacks C]
    (J : Pretopology C)
    (H : Stacks.CategoryTheory.Hypercovering.HypercoveringOfTerminal.{u, u} J)
    (OC : Sheaf J.toGrothendieck CommRingCat.{u})
    (A : ∀ n : SimplexCategory, ObjectProperty (SheafOfModules.{u}
      (componentRingSheaf (hypercoveringSituation J H)
        ((hypercoveringSituation J H).totalRingSheaf
          (hypercoveringRingedAugmentation J H OC).O) n)))
    (hflat : ∀ (k : ℕ) (i : Fin (k + 2)), PreservesFiniteLimits
      (((hypercoveringSituation J H).transitionRingedToposHom
        (hypercoveringRingedAugmentation J H OC).O
        (SimplexCategory.δ i)).toModulesHom.pullbackModules))
    (hA : ∀ n : SimplexCategory, (A n).IsWeakSerreClass) :
    (cartesianDegreewiseModules (hypercoveringSituation J H)
      (hypercoveringRingedAugmentation J H OC).O A).IsWeakSerreClass
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 85.23, Tag 0DC1](https://stacks.math.columbia.edu/tag/0DC1)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
