---
declaration: section
origin: cited
lean: AlgebraicGeometry.ProEtale.IsConstructibleAdicSheaf, AlgebraicGeometry.ProEtale.IsLisse, AlgebraicGeometry.ProEtale.IsAdicConstructible, AlgebraicGeometry.ProEtale.IsConstructibleAdicModuleSheaf, AlgebraicGeometry.ProEtale.IsLisseAdicModuleSheaf, AlgebraicGeometry.ProEtale.IsAdicConstructibleModuleSheaf, AlgebraicGeometry.ProEtale.IsAdicLisse, AlgebraicGeometry.ProEtale.exists_isLisseAdicModuleSheaf_stratification
statement: formalized
proof: formalized
---

# 61.28 Constructible adic sheaves

Section 61.28 of the Stacks Project, [Tag 09BS](https://stacks.math.columbia.edu/tag/09BS). 7 tags here are carried by 19 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09BT, a definition

[Tag 09BT](https://stacks.math.columbia.edu/tag/09BT) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.IsConstructibleAdicSheaf`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Constructible/Adic.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Constructible/Adic.lean#L84). The attribute's comment: “part (1): constructible Λ-sheaves”.

> A sheaf of `Λ`-modules on the small pro-étale site is a *constructible `Λ`-sheaf* if it is
> the limit of its quotients by the powers of `I` and each of those quotients is, as a sheaf of
> `Λ ⧸ Iⁿ`-modules, constructible.

```lean
abbrev IsConstructibleAdicSheaf (X : Scheme.{u}) (Λ : Type v) [CommRing Λ] [IsNoetherianRing Λ]
    [UnivLE.{u + 1, w}] (I : Ideal Λ)
    [∀ (n : ℕ) (Y : Scheme.{u}),
      HasWeakSheafify (Scheme.ProEt.topology Y) (ModuleCat.{w} (Λ ⧸ I ^ n))]
    [∀ (n : ℕ) (Y : Scheme.{u}) (V : Y.ProEt),
      HasWeakSheafify ((Scheme.ProEt.topology Y).over V) (ModuleCat.{w} (Λ ⧸ I ^ n))]
    [∀ (n : ℕ) {Z Y : Scheme.{u}} (f : Z ⟶ Y),
      ((Scheme.proetaleBaseChange f).sheafPushforwardContinuous
        (ModuleCat.{w} (Λ ⧸ I ^ n)) (Scheme.ProEt.topology Y)
        (Scheme.ProEt.topology Z)).IsRightAdjoint]
    (F : Sheaf (Scheme.ProEt.topology X) (ModuleCat.{w} Λ)) : Prop
```

**`AlgebraicGeometry.ProEtale.IsLisse`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Constructible/Adic.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Constructible/Adic.lean#L106). The attribute's comment: “part (2): lisse”.

> A constructible `Λ`-sheaf is *lisse* if each of its quotients by a power of `I` is a locally
> constant sheaf of `Λ ⧸ Iⁿ`-modules.

```lean
abbrev IsLisse (X : Scheme.{u}) (Λ : Type v) [CommRing Λ] [IsNoetherianRing Λ]
    [UnivLE.{u + 1, w}] (I : Ideal Λ)
    [∀ (n : ℕ) (Y : Scheme.{u}),
      HasWeakSheafify (Scheme.ProEt.topology Y) (ModuleCat.{w} (Λ ⧸ I ^ n))]
    [∀ (n : ℕ) (Y : Scheme.{u}) (V : Y.ProEt),
      HasWeakSheafify ((Scheme.ProEt.topology Y).over V) (ModuleCat.{w} (Λ ⧸ I ^ n))]
    [∀ (n : ℕ) {Z Y : Scheme.{u}} (f : Z ⟶ Y),
      ((Scheme.proetaleBaseChange f).sheafPushforwardContinuous
        (ModuleCat.{w} (Λ ⧸ I ^ n)) (Scheme.ProEt.topology Y)
        (Scheme.ProEt.topology Z)).IsRightAdjoint]
    (F : Sheaf (Scheme.ProEt.topology X) (ModuleCat.{w} Λ)) : Prop
```

**`AlgebraicGeometry.ProEtale.IsAdicConstructible`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Constructible/Adic.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Constructible/Adic.lean#L128). The attribute's comment: “part (4): adic constructible”.

> A sheaf of `Λ`-modules on the small pro-étale site of `X` is *adic constructible* if every
> affine open of `X` decomposes into constructible locally closed subschemes on each of which the
> inverse image of the sheaf is adic lisse.

```lean
abbrev IsAdicConstructible (X : Scheme.{u}) (Λ : Type v) [CommRing Λ] (I : Ideal Λ)
    [∀ Y : Scheme.{u}, HasWeakSheafify (Scheme.ProEt.topology Y) (ModuleCat.{w} Λ)]
    [∀ (Y : Scheme.{u}) (V : Y.ProEt),
      HasWeakSheafify ((Scheme.ProEt.topology Y).over V) (ModuleCat.{w} Λ)]
    [∀ {Z Y : Scheme.{u}} (f : Z ⟶ Y),
      ((Scheme.proetaleBaseChange f).sheafPushforwardContinuous
        (ModuleCat.{w} Λ) (Scheme.ProEt.topology Y)
        (Scheme.ProEt.topology Z)).IsRightAdjoint]
    (F : Sheaf (Scheme.ProEt.topology X) (ModuleCat.{w} Λ)) : Prop
```

**`AlgebraicGeometry.ProEtale.IsConstructibleAdicModuleSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Constructible/AdicModuleSheaf.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Constructible/AdicModuleSheaf.lean#L95). The attribute's comment: “part (1): constructible Λ-sheaves”.

> **Stacks 09BT (1).** A sheaf of `Λ`-modules on the small pro-étale site is a *constructible
> `Λ`-sheaf* if it is the limit of its quotients by the powers of `I` and each of those quotients
> is, as a sheaf of `Λ ⧸ Iⁿ`-modules, constructible.

```lean
def IsConstructibleAdicModuleSheaf [IsNoetherianRing Λ]
    (F : Sheaf (Scheme.ProEt.topology X) (ModuleCat.{max (u + 1) v w} Λ)) : Prop
```

**`AlgebraicGeometry.ProEtale.IsLisseAdicModuleSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Constructible/AdicModuleSheaf.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Constructible/AdicModuleSheaf.lean#L111). The attribute's comment: “part (2): lisse”.

> **Stacks 09BT (2).** A constructible `Λ`-sheaf is *lisse* if each of its quotients by a
> power of `I` is a locally constant sheaf of `Λ ⧸ Iⁿ`-modules.

```lean
def IsLisseAdicModuleSheaf [IsNoetherianRing Λ]
    (F : Sheaf (Scheme.ProEt.topology X) (ModuleCat.{max (u + 1) v w} Λ)) : Prop
```

**`AlgebraicGeometry.ProEtale.IsAdicConstructibleModuleSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Constructible/AdicModuleSheaf.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Constructible/AdicModuleSheaf.lean#L137). The attribute's comment: “part (4): adic constructible”.

> **Stacks 09BT (4).** A sheaf of `Λ`-modules on the small pro-étale site of `X` is *adic
> constructible* if every affine open of `X` decomposes into constructible locally closed
> subschemes on each of which the inverse image of the sheaf is adic lisse.

```lean
def IsAdicConstructibleModuleSheaf
    (F : Sheaf (Scheme.ProEt.topology X) (ModuleCat.{max (u + 1) v w} Λ)) : Prop
```

**`AlgebraicGeometry.ProEtale.IsAdicLisse`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/AdicSheaves.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/AdicSheaves.lean#L77). The attribute's comment: “adic\_lisse\_sheaf”.

> A sheaf which is pro-étale locally the completed constant sheaf of a fixed
> `I`-adically complete module with finite quotient modulo `I`.

```lean
abbrev IsAdicLisse (X : Scheme.{u}) (Λ : Type v) [CommRing Λ] (I : Ideal Λ)
    [HasWeakSheafify (Scheme.ProEt.topology X) (ModuleCat.{w} Λ)]
    (F : Sheaf (Scheme.ProEt.topology X) (ModuleCat.{w} Λ)) : Prop
```

## Tag 09BU, a lemma

[Tag 09BU](https://stacks.math.columbia.edu/tag/09BU) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.exists_isLisseAdicModuleSheaf_stratification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Constructible/LisseStratification.lean, line 541](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Constructible/LisseStratification.lean#L541). References: SGA 4½ Rapport (2.5), “more general”.

> **Stacks 09BU.** Let `X` be a Noetherian scheme, `Λ` a Noetherian ring and `I ⊆ Λ` an ideal.
> A constructible `Λ`-sheaf on `X_proet` is lisse on the strata of a finite partition of `X` into
> constructible locally closed subschemes.

```lean
theorem exists_isLisseAdicModuleSheaf_stratification [IsNoetherianRing Λ] {X : Scheme.{u}}
    [IsNoetherian X]
    (I : Ideal Λ) {F : Sheaf (Scheme.ProEt.topology X) (ModuleCat.{max (u + 1) v w} Λ)}
    (hF : IsConstructibleAdicModuleSheaf.{w} X Λ I F) :
    ∃ s : Scheme.ConstructibleStratification X ⊤, ∀ i, IsLisseAdicModuleSheaf.{w} (s.piece i) Λ I
      ((proetaleModuleInverseImage.{u, v, w} (s.inclusion i) Λ).obj F)
```

## Tag 09BV, a lemma

[Tag 09BV](https://stacks.math.columbia.edu/tag/09BV) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.exists_iso_completedConstantSheaf_of_isConstant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Constructible/ConstantAdicCompletedIso.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Constructible/ConstantAdicCompletedIso.lean#L169). The attribute's comment: “the sheaf is the completed constant sheaf of a finite complete module”.

> Let `X` be a scheme whose pro-étale topos is not empty, let `Λ` be a Noetherian ring and
> `I ⊆ Λ` an ideal, and let `F` be a sheaf of `Λ`-modules on the small pro-étale site of `X` such
> that
>
> 1. `F` is the limit of its adic reductions `F / IⁿF`,
> 2. every `F / IⁿF` is a constant sheaf, and
> 3. `F / IF` is the constant sheaf of a finite module.
>
> Then `F ≅ M̲^∧` for an `I`-adically complete `Λ`-module `M` which is finite over `Λ^∧`.

```lean
theorem exists_iso_completedConstantSheaf_of_isConstant
    (hne : ∃ U : X.ProEt, (⊥ : Sieve U) ∉ Scheme.ProEt.topology X U)
    (F : Sheaf (Scheme.ProEt.topology X) (ModuleCat.{max (u + 1) w} Λ))
    (Q : ℕᵒᵖ ⥤ Sheaf (Scheme.ProEt.topology X) (ModuleCat.{max (u + 1) w} Λ))
    (q : (Functor.const ℕᵒᵖ).obj F ⟶ Q)
    (hq : ∀ n : ℕ, IsQuotientBy X Λ (I ^ n) F (Q.obj (op n)) (q.app (op n)))
    (hlim : IsLimit (Limits.Cone.mk F q))
    (hconst : ∀ n : ℕ, ∃ N : ModuleCat.{max (u + 1) w} Λ,
      Nonempty ((constantSheaf (Scheme.ProEt.topology X)
        (ModuleCat.{max (u + 1) w} Λ)).obj N ≅ Q.obj (op n)))
    (hfin : ∃ N : ModuleCat.{max (u + 1) w} Λ,
      Module.Finite Λ (N : Type (max (u + 1) w)) ∧
      Nonempty ((constantSheaf (Scheme.ProEt.topology X)
        (ModuleCat.{max (u + 1) w} Λ)).obj N ≅ Q.obj (op 1))) :
    ∃ M : ModuleCat.{max (u + 1) w} Λ,
      IsAdicComplete I (M : Type (max (u + 1) w)) ∧
      Module.Finite (AdicCompletion I Λ) (AdicCompletion I (M : Type (max (u + 1) w))) ∧
      Nonempty (F ≅ completedConstantSheaf X Λ I M)
```

**`Stacks.ModuleSheaf.exists_finite_isAdicComplete_constantSheaf_iso_of_isConstant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Constructible/ConstantAdicQuotientTower.lean, line 355](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Constructible/ConstantAdicQuotientTower.lean#L355). The attribute's comment: “the coefficient module, on any site with a terminal object”.

> **Stacks 09BV, the coefficient module, on a site with a terminal object.** Let `Λ` be
> Noetherian, `I ⊆ Λ` an ideal and `F` a sheaf of `Λ`-modules on a site with a terminal object whose
> topos is not empty, whose reductions `F / IⁿF` are constant sheaves and whose first reduction is
> the constant sheaf of a finite module. Then there is an `I`-adically complete `Λ`-module `M`,
> finite over `Λ^∧` and with every reduction `M / IⁿM` finite over `Λ`, whose tower of constant
> reductions is termwise isomorphic to the adic quotient tower of `F`.

```lean
theorem exists_finite_isAdicComplete_constantSheaf_iso_of_isConstant (I : Ideal Λ)
    (hne : ∃ U : C, (⊥ : Sieve U) ∉ J U)
    (F : Sheaf J (ModuleCat.{w} Λ))
    (Q : ℕᵒᵖ ⥤ Sheaf J (ModuleCat.{w} Λ))
    (q : (Functor.const ℕᵒᵖ).obj F ⟶ Q)
    (hq : ∀ n : ℕ, IsQuotientBy J Λ (I ^ n) F (Q.obj (op n)) (q.app (op n)))
    (hconst : ∀ n : ℕ, ∃ N : ModuleCat.{w} Λ,
      Nonempty ((constantSheaf J (ModuleCat.{w} Λ)).obj N ≅
        Q.obj (op n)))
    (hfin : ∃ N : ModuleCat.{w} Λ, Module.Finite Λ (N : Type w) ∧
      Nonempty ((constantSheaf J (ModuleCat.{w} Λ)).obj N ≅
        Q.obj (op 1))) :
    ∃ M : ModuleCat.{w} Λ, IsAdicComplete I (M : Type w) ∧
      Module.Finite Λ ((M : Type w) ⧸ (I • ⊤ : Submodule Λ (M : Type w))) ∧
      Module.Finite (AdicCompletion I Λ) (AdicCompletion I (M : Type w)) ∧
      (∀ n : ℕ, Module.Finite Λ ((M : Type w) ⧸ (I ^ n • ⊤ : Submodule Λ (M : Type w)))) ∧
      ∀ n : ℕ, Nonempty ((adicQuotientModuleSystem Λ I M ⋙
        constantSheaf J (ModuleCat.{w} Λ)).obj (op n) ≅
          Q.obj (op n))
```

**`AlgebraicGeometry.ProEtale.exists_finite_isAdicComplete_constantSheaf_iso_of_isConstant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Constructible/ConstantAdicReductions.lean, line 475](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Constructible/ConstantAdicReductions.lean#L475). The attribute's comment: “the finite complete coefficient module and its termwise constant reductions”.

> **Stacks 09BV, the coefficient module.** Let `Λ` be Noetherian, `I ⊆ Λ` an ideal and `F` a
> sheaf of `Λ`-modules on the small pro-étale site whose reductions `F / IⁿF` are constant sheaves
> and whose first reduction is of finite type. Then there is an `I`-adically complete `Λ`-module
> `M`, finite over `Λ^∧` and with every reduction `M / IⁿM` finite over `Λ`, whose tower of constant
> reductions is termwise isomorphic to the adic quotient tower of `F`.

```lean
theorem exists_finite_isAdicComplete_constantSheaf_iso_of_isConstant (I : Ideal Λ)
    (hne : ∃ U : X.ProEt, (⊥ : Sieve U) ∉ Scheme.ProEt.topology X U)
    (F : Sheaf (Scheme.ProEt.topology X) (ModuleCat.{w} Λ))
    (Q : ℕᵒᵖ ⥤ Sheaf (Scheme.ProEt.topology X) (ModuleCat.{w} Λ))
    (q : (Functor.const ℕᵒᵖ).obj F ⟶ Q)
    (hq : ∀ n : ℕ, IsQuotientBy X Λ (I ^ n) F (Q.obj (op n)) (q.app (op n)))
    (hconst : ∀ n : ℕ, ∃ N : ModuleCat.{w} Λ,
      Nonempty ((constantSheaf (Scheme.ProEt.topology X) (ModuleCat.{w} Λ)).obj N ≅
        Q.obj (op n)))
    (hfin : ∃ N : ModuleCat.{w} Λ, Module.Finite Λ (N : Type w) ∧
      Nonempty ((constantSheaf (Scheme.ProEt.topology X) (ModuleCat.{w} Λ)).obj N ≅
        Q.obj (op 1))) :
    ∃ M : ModuleCat.{w} Λ, IsAdicComplete I (M : Type w) ∧
      Module.Finite Λ ((M : Type w) ⧸ (I • ⊤ : Submodule Λ (M : Type w))) ∧
      Module.Finite (AdicCompletion I Λ) (AdicCompletion I (M : Type w)) ∧
      (∀ n : ℕ, Module.Finite Λ ((M : Type w) ⧸ (I ^ n • ⊤ : Submodule Λ (M : Type w)))) ∧
      ∀ n : ℕ, Nonempty ((adicQuotientModuleSystem Λ I M ⋙
        constantSheaf (Scheme.ProEt.topology X) (ModuleCat.{w} Λ)).obj (op n) ≅
          Q.obj (op n))
```

## Tag 09BW, a lemma

[Tag 09BW](https://stacks.math.columbia.edu/tag/09BW) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.isAdicLisse_of_isLisseAdicModuleSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Constructible/AdicLisse.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Constructible/AdicLisse.lean#L62).

> **Stacks 09BW.** Let `X` be a connected scheme, `Λ` a Noetherian ring and `I ⊆ Λ` an ideal.
> A lisse constructible `Λ`-sheaf on the small pro-étale site of `X` is adic lisse.

```lean
theorem isAdicLisse_of_isLisseAdicModuleSheaf [ConnectedSpace X] [IsNoetherianRing Λ]
    {F : Sheaf (Scheme.ProEt.topology X) (ModuleCat.{max (u + 1) v w} Λ)}
    (hF : IsLisseAdicModuleSheaf.{w} X Λ I F) : IsAdicLisse X Λ I F
```

## Tag 09BX, a lemma

[Tag 09BX](https://stacks.math.columbia.edu/tag/09BX) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.isAdicConstructibleModuleSheaf_of_isConstructibleAdicModuleSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Constructible/AdicConstructible.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Constructible/AdicConstructible.lean#L84).

> **Stacks 09BX.** Let `X` be a Noetherian scheme, `Λ` a Noetherian ring and `I ⊆ Λ` an ideal.
> A constructible `Λ`-sheaf on the small pro-étale site of `X` is adic constructible: it is lisse on
> the strata of a finite partition of `X` (Stacks 09BU).

```lean
theorem isAdicConstructibleModuleSheaf_of_isConstructibleAdicModuleSheaf [IsNoetherianRing Λ]
    {X : Scheme.{u}} [IsNoetherian X]
    {F : Sheaf (Scheme.ProEt.topology X) (ModuleCat.{max (u + 1) v w} Λ)}
    (hF : IsConstructibleAdicModuleSheaf.{w} X Λ I F) :
    IsAdicConstructibleModuleSheaf.{w} X Λ I F
```

## Tag 09BY, a lemma

[Tag 09BY](https://stacks.math.columbia.edu/tag/09BY) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.isZero_of_isDerivedComplete_of_idealProduct_eq_top_of_slicedObjectsSituation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/AdicCompletionCriterion.lean, line 1152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/AdicCompletionCriterion.lean#L1152). The attribute's comment: “generalized to a ringed site with a covering collection of objects testing surjectivity of sheaves of sets in the module universe, on the site and on its slices, and to an arbitrary sheaf of ideals; the Small and HasSheafify hypotheses that used to exclude the pro-etale site are gone, but the sliced bundle is not yet constructed for that site, so the pro-etale site is still NOT an instance of this statement”.

> **Stacks 09BY.** A sheaf of modules on a ringed site with enough weakly contractible
> objects which is derived complete along a sheaf of ideals and satisfies `IF = F`, that is
> whose adic quotient `F/IF` vanishes, is zero. The sheaf of ideals is assumed finitely
> generated on sections over the weakly contractible objects.
>
> This generalizes the content of the tag, whose site is `X_proétale` and whose coefficients are a
> constant ring `Λ` with a finitely generated ideal `I`: the site here is any ringed site with
> enough weakly contractible objects, `I` is any sheaf of ideals, and the finite-generation
> requirement is *weaker* than the source's, being asked only on sections over weakly contractible
> objects.
>
> The weakly contractible objects enter only through the bundle `hX`, whose members test
> surjectivity of sheaves of sets valued in the *module* universe `max u v`, on the site and on
> each of its slice sites. That is what makes the statement readable at a site whose objects
> outnumber its morphisms. The small pro-étale site of a scheme is such a site: it is a
> `RingedSite.{u + 1, u, _}` — for instance
> `AlgebraicGeometry.ProEtale.constantCoefficientRingedSite`, which is `X_proétale` ringed by the
> constant sheaf `Λ̲` — and its weak contractibility cannot be tested at the morphism universe `u`
> at all, since `Small.{u} X.ProEt` is false: the objects of `X.ProEt` lie in `Type (u + 1)` and
> the site is small, and essentially small, only at `u + 1`.

```lean
theorem isZero_of_isDerivedComplete_of_idealProduct_eq_top_of_slicedObjectsSituation
    (X : RingedSite.{u, v, max u v})
    [HasSheafify X.J AddCommGrpCat.{max u v}]
    [X.J.WEqualsLocallyBijective AddCommGrpCat.{max u v}]
    (hX : Stacks.WeaklyContractible.SlicedObjectsSituation.{w, v, u, max u v} X.C X.J)
    (I : SheafOfModules.Submodule
      (SheafOfModules.unit (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (hI : ∀ U : X.C, hX.B U →
      (I.toSubmodule.obj (op U)).FG)
    (F : SheafOfModules.{max u v} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))
    (hF : AlgebraicGeometry.RingedSite.IsDerivedComplete X I
      ((DerivedCategory.singleFunctor
        (SheafOfModules.{max u v} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) 0).obj F))
    (hIF : idealPowerProduct X I F 1 = ⊤) :
    IsZero F
```

**`AlgebraicGeometry.RingedSite.isZero_of_isDerivedComplete_of_idealProduct_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/AdicCompletionCriterion.lean, line 1424](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/AdicCompletionCriterion.lean#L1424).

> **Stacks 09BY.** A sheaf of modules on a ringed site with enough weakly contractible
> objects which is derived complete along a sheaf of ideals and satisfies `IF = F`, that is
> whose adic quotient `F/IF` vanishes, is zero. The sheaf of ideals is assumed finitely
> generated on sections over the weakly contractible objects.

```lean
theorem isZero_of_isDerivedComplete_of_idealProduct_eq_top
    (X : RingedSite.{u, v, max u v}) [Small.{v} X.C]
    [HasSheafify X.J (Type v)]
    [HasSheafify X.J AddCommGrpCat.{max u v}]
    [X.J.WEqualsLocallyBijective AddCommGrpCat.{max u v}]
    (hX : X.J.HasEnoughWeaklyContractibleObjects)
    (I : SheafOfModules.Submodule
      (SheafOfModules.unit (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (hI : ∀ U : X.C, X.J.IsWeaklyContractible U →
      (I.toSubmodule.obj (op U)).FG)
    (F : SheafOfModules.{max u v} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))
    (hF : AlgebraicGeometry.RingedSite.IsDerivedComplete X I
      ((DerivedCategory.singleFunctor
        (SheafOfModules.{max u v} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) 0).obj F))
    (hIF : idealPowerProduct X I F 1 = ⊤) :
    IsZero F
```

**`AlgebraicGeometry.RingedSite.isZero_of_isDerivedComplete_of_idealProduct_eq_top_of_sliceTestingFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/AdicCompletionCriterionSliceTesting.lean, line 796](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/AdicCompletionCriterionSliceTesting.lean#L796).

> **Stacks 09BY.** A sheaf of modules on a ringed site with enough weakly contractible
> objects which is derived complete along a sheaf of ideals and satisfies `IF = F`, that is
> whose adic quotient `F/IF` vanishes, is zero. The sheaf of ideals is assumed finitely
> generated on sections over the weakly contractible objects.

```lean
theorem isZero_of_isDerivedComplete_of_idealProduct_eq_top_of_sliceTestingFamily
    (X : RingedSite.{u, v, max u v w})
    [HasSheafify X.J AddCommGrpCat.{max u v w}]
    [X.J.WEqualsLocallyBijective AddCommGrpCat.{max u v w}]
    (B : Stacks.WeaklyContractible.SliceTestingFamily.{max u v w} X.C X.J)
    (I : SheafOfModules.Submodule
      (SheafOfModules.unit (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (hI : ∀ U : X.C, B.B U →
      (I.toSubmodule.obj (op U)).FG)
    (F : SheafOfModules.{max u v w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))
    (hF : AlgebraicGeometry.RingedSite.IsDerivedComplete.{u, v, max u v w, max u v w} X I
      ((DerivedCategory.singleFunctor
        (SheafOfModules.{max u v w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) 0).obj F))
    (hIF : idealPowerProductOfSize X I F 1 = ⊤) :
    IsZero F
```

**`AlgebraicGeometry.ProEtale.isZero_of_isDerivedComplete_constantCoefficients`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/DerivedCompleteConstantCoefficients.lean, line 249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/DerivedCompleteConstantCoefficients.lean#L249).

> **[Stacks, Tag 09BY].** Let `X` be a scheme, let `Λ` be a ring with a finitely generated
> ideal `I ⊂ Λ`, and let `ℱ` be a sheaf of `Λ`-modules on `X_proétale` — a sheaf of modules over
> the constant coefficient ring sheaf `Λ̲`. If `ℱ` is derived complete along the ideal sheaf `IΛ̲`
> cut out by `I`, and `ℱ/Iℱ = 0`, then `ℱ = 0`.
>
> This is the tag's own statement at the tag's own objects. It is
> `AlgebraicGeometry.ProEtale.isZero_of_isDerivedComplete_proetale` — the chapter's lemma at the
> small pro-étale site for an arbitrary sheaf of rings and an arbitrary sheaf of ideals — read at
> `𝒪 = Λ̲` and `ℐ = AlgebraicGeometry.ProEtale.constantCoefficientIdealSheaf`, with that
> statement's finite-generation hypothesis discharged by
> `AlgebraicGeometry.ProEtale.fg_constantCoefficientIdealSheaf_obj`. The two ringed sites agree
> on the nose, so no transport is needed at this step.
>
> `Λ` is an arbitrary commutative ring: `I.FG` is the only hypothesis on the coefficients, as in
> the source. The hypothesis `hIF` says the first ideal power product is everything, which is the
> vanishing of the adic quotient `ℱ/Iℱ`.

```lean
theorem isZero_of_isDerivedComplete_constantCoefficients (X : Scheme.{u}) (Λ : Type u)
    [CommRing Λ] (I : Ideal Λ) (hI : I.FG)
    (F : SheafOfModules.{u + 1}
      (Stacks.SheafOfModules.Tensor.ringSheaf (constantCoefficientRingedSite.{u, u, u} X Λ).O))
    (hF : RingedSite.IsDerivedComplete.{u + 1, u, u + 1, u + 1}
      (constantCoefficientRingedSite.{u, u, u} X Λ)
      (constantCoefficientIdealSheaf.{u, u, u} X Λ I)
      ((DerivedCategory.singleFunctor
        (SheafOfModules.{u + 1}
          (Stacks.SheafOfModules.Tensor.ringSheaf
            (constantCoefficientRingedSite.{u, u, u} X Λ).O)) 0).obj F))
    (hIF : RingedSite.idealPowerProduct (constantCoefficientRingedSite.{u, u, u} X Λ)
      (constantCoefficientIdealSheaf.{u, u, u} X Λ I) F 1 = ⊤) :
    IsZero F
```

## Tag 09BZ, a lemma

[Tag 09BZ](https://stacks.math.columbia.edu/tag/09BZ) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.exists_epi_biproduct_completedConstantCoefficientSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/CompletedConstantSheafMaps.lean, line 737](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/CompletedConstantSheafMaps.lean#L737). The attribute's comment: “`F/IF` is only assumed of finite type, which a locally constant sheaf of finite type is”.

> **Derived complete sheaves are quotients of finite sums of `\underline{Λ}^∧`.** Let `X` be a
> weakly contractible affine scheme, `Λ` a Noetherian ring and `I ⊆ Λ` an ideal. Let `F` be a
> derived complete sheaf of `Λ`-modules on `X_proét` with `F/IF` of finite type, for instance
> locally constant of finite type. Then there are an integer `t` and a surjection
> `(\underline{Λ}^∧)^{⊕ t} → F`.

```lean
theorem exists_epi_biproduct_completedConstantCoefficientSheaf [IsAffine X]
    (hX : IsWeaklyContractibleObj X)
    (F : RingedSite.Modules.{u + 1, u, max (u + 1) w}
      (constantCoefficientRingedSite.{u, max (u + 1) w, w} X Λ))
    (hF : RingedSite.IsDerivedComplete.{u + 1, u, max (u + 1) w, w}
      (constantCoefficientRingedSite.{u, max (u + 1) w, w} X Λ)
      (constantCoefficientIdealSheaf.{u, max (u + 1) w, w} X Λ I)
      ((DerivedCategory.singleFunctor _ 0).obj F))
    (hFI : (cokernel (RingedSite.idealPowerProductOfSize.{u + 1, u, w} _
      (constantCoefficientIdealSheaf.{u, max (u + 1) w, w} X Λ I) F 1).ι).IsFiniteType) :
    ∃ (t : ℕ) (α : (⨁ fun _ : Fin t =>
        (completedConstantCoefficientSheafFunctor.{u, max (u + 1) w, w} X Λ I).obj
          (Functor.unitModule Λ)) ⟶ F), Epi α
```

**`AlgebraicGeometry.ProEtale.exists_epi_sigma_completedConstantSheaf_of_isDerivedComplete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/DerivedCompleteFiniteGeneration.lean, line 682](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/DerivedCompleteFiniteGeneration.lean#L682).

> **[Stacks, Tag 09BZ].** Let `X` be a weakly contractible affine scheme, let `Λ` be a
> Noetherian ring and let `I ⊂ Λ` be an ideal. Let `ℱ` be a sheaf of `Λ`-modules on `X_proétale`
> which is derived complete, and such that `ℱ/Iℱ` is a locally constant sheaf of `Λ/I`-modules of
> finite type. Then there is an integer `t` and a surjection `(Λ̲^∧)^{⊕t} ⟶ ℱ`.

```lean
theorem exists_epi_sigma_completedConstantSheaf_of_isDerivedComplete
    [IsAffine X] (hX : ProetaleWContractible.IsWeaklyContractibleObj X)
    (F : RingedSite.Modules.{u + 1, u, u + 1} (constantCoefficientRingedSite.{u, u + 1, u} X Λ))
    (hF : RingedSite.IsDerivedComplete.{u + 1, u, u + 1, u + 1}
      (constantCoefficientRingedSite.{u, u + 1, u} X Λ)
      (constantCoefficientIdealSheaf.{u, u + 1, u} X Λ I)
      ((DerivedCategory.singleFunctor _ 0).obj F))
    (hFI : ∃ G : Sheaf (Scheme.ProEt.topology X) (ModuleCat.{u + 1} (Λ ⧸ I)),
      Stacks.ConstantSheaf.IsFiniteTypeLocallyConstant (Λ ⧸ I) (Scheme.ProEt.topology X) G ∧
      Nonempty ((toCoefficientModuleSheaf.{u, u + 1, u} X Λ).obj
          (cokernel (RingedSite.idealPowerProduct (constantCoefficientRingedSite.{u, u + 1, u} X Λ)
            (constantCoefficientIdealSheaf.{u, u + 1, u} X Λ I) F 1).ι) ≅
        (restrictQuotientScalars.{u + 1, u + 1, u} X Λ I).obj G)) :
    ∃ t : ℕ, ∃ α : (∐ fun _ : Fin t =>
        (moduleSheafOverConstantCoefficientsFunctor.{u, u + 1, u} X Λ).obj
          (Stacks.ConstantSheaf.completedConstantSheaf (Scheme.ProEt.topology X) I)) ⟶ F,
      Epi α
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 61.28, Tag 09BS](https://stacks.math.columbia.edu/tag/09BS)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
