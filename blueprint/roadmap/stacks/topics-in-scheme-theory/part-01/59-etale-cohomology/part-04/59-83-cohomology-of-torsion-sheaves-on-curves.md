---
declaration: section
origin: cited
lean: Stacks.EtaleCohomology.TorsionSheafSituation, Stacks.EtaleCohomology.TorsionSheafSituation.isVanishingAboveDegreeTwo, Stacks.EtaleCohomology.IsVanishingAboveDegreeTwo, Stacks.EtaleCohomology.IsAffineVanishingAboveDegreeOne, Stacks.EtaleCohomology.TorsionSheafSituation.isAffineVanishingAboveDegreeOne, Stacks.EtaleCohomology.TorsionSheafSituation.isPrimePowerTorsionVanishing, Stacks.EtaleCohomology.IsPrimePowerTorsionVanishing, Stacks.EtaleCohomology.TorsionSheafSituation.finiteCohomologyOfPrimeToCharacteristic
statement: formalized
proof: formalized
---

# 59.83 Cohomology of torsion sheaves on curves

Section 59.83 of the Stacks Project, [Tag 03SB](https://stacks.math.columbia.edu/tag/03SB). 20 tags here are carried by 47 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0A52, a situation

[Tag 0A52](https://stacks.math.columbia.edu/tag/0A52) in the Stacks Project.

**`Stacks.EtaleCohomology.TorsionSheafSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/TorsionSheafSituation.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/TorsionSheafSituation.lean#L42).

> An algebraically closed field `k`, a separated scheme `X` of finite type over `k` whose
> underlying space has Krull dimension at most one, and a torsion abelian sheaf `F` on the small
> étale site of `X`.

```lean
public structure TorsionSheafSituation
```

## Tag 0A53, an item

[Tag 0A53](https://stacks.math.columbia.edu/tag/0A53) in the Stacks Project.

**`Stacks.EtaleCohomology.TorsionSheafSituation.isVanishingAboveDegreeTwo`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/CurveCohomologyTheorem.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/CurveCohomologyTheorem.lean#L79).

> **Stacks Project, Tag 0A53**, statement (1) of Situation 0A52: `H^q(X, F) = 0` for `q > 2`.

```lean
theorem isVanishingAboveDegreeTwo
    [HasExt.{w} (Sheaf S.X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v})] :
    IsVanishingAboveDegreeTwo.{u, v, w} S.F
```

**`Stacks.EtaleCohomology.IsVanishingAboveDegreeTwo`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/VanishingAboveDegreeTwo.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/VanishingAboveDegreeTwo.lean#L91). The attribute's comment: “item (1) of 0A52: H^q(X, F) = 0 for q > 2”.

> **Stacks Project, Tag 0A53.** Statement (1) of the list of Situation 0A52: the étale
> cohomology `H^q_étale(X, F)` vanishes for every degree `q > 2`.

```lean
def IsVanishingAboveDegreeTwo
    (F : Sheaf X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v}) : Prop
```

## Tag 0A54, an item

[Tag 0A54](https://stacks.math.columbia.edu/tag/0A54) in the Stacks Project.

**`Stacks.EtaleCohomology.IsAffineVanishingAboveDegreeOne`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/AffineVanishingAboveDegreeOne.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/AffineVanishingAboveDegreeOne.lean#L54). The attribute's comment: “item (2) of 0A52: H^q(X, F) = 0 for q > 1 if X is affine”.

> Statement (2) of the list of Situation 0A52: the étale cohomology `H^q_étale(X, F)` vanishes
> for every `q > 1` if `X` is affine.

```lean
def IsAffineVanishingAboveDegreeOne
    (F : Sheaf X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v}) : Prop
```

**`Stacks.EtaleCohomology.TorsionSheafSituation.isAffineVanishingAboveDegreeOne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/CurveCohomologyTheorem.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/CurveCohomologyTheorem.lean#L87).

> **Stacks Project, Tag 0A54**, statement (2) of Situation 0A52: if `X` is affine then
> `H^q(X, F) = 0` for `q > 1`.

```lean
theorem isAffineVanishingAboveDegreeOne
    [HasExt.{w} (Sheaf S.X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v})] :
    IsAffineVanishingAboveDegreeOne.{u, v, w} S.F
```

## Tag 0A55, an item

[Tag 0A55](https://stacks.math.columbia.edu/tag/0A55) in the Stacks Project.

**`Stacks.EtaleCohomology.TorsionSheafSituation.isPrimePowerTorsionVanishing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/CurveCohomologyTheorem.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/CurveCohomologyTheorem.lean#L95).

> **Stacks Project, Tag 0A55**, statement (3) of Situation 0A52: if `p = char(k) > 0` and `F`
> is `p`-power torsion then `H^q(X, F) = 0` for `q > 1`.

```lean
theorem isPrimePowerTorsionVanishing
    [HasExt.{w} (Sheaf S.X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v})]
    (p : ℕ) [CharP S.k p] :
    IsPrimePowerTorsionVanishing.{u, v, w} S.structureMorphism p S.F
```

**`Stacks.EtaleCohomology.IsPrimePowerTorsionVanishing`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/PrimePowerVanishingStatement.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/PrimePowerVanishingStatement.lean#L200). The attribute's comment: “item (3) of 0A52: H^q(X, F) = 0 for q > 1 if p = char(k) > 0 and F is p-power torsion”.

> **Stacks Project, Tag 0A55**, item (3) of Situation 0A52:
>
> > `H^q_étale(X, F) = 0` for `q > 1` if `p = char(k) > 0` and `F` is `p`-power torsion.
>
> Here `X` is a scheme with a morphism `π` to the spectrum of a field `k` of characteristic `p`,
> and `F` is an abelian sheaf on the small étale site of `X`. The source states this as one entry
> of the list of eight statements that Situation 0A52 asks for, not as an assertion, so it is a
> predicate on the data; the situation's further hypotheses — `k` algebraically closed, `X`
> separated of finite type of dimension at most one, `F` torsion — are what make the item a
> theorem at Tag 03SC, and are not imposed here.

```lean
def IsPrimePowerTorsionVanishing (π : X ⟶ Spec (.of k)) (p : ℕ) [CharP k p]
    (F : Sheaf X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v})
    [HasExt.{w} (Sheaf X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v})] : Prop
```

## Tag 0A56, an item

[Tag 0A56](https://stacks.math.columbia.edu/tag/0A56) in the Stacks Project.

**`Stacks.EtaleCohomology.TorsionSheafSituation.finiteCohomologyOfPrimeToCharacteristic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/CurveCohomologyTheorem.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/CurveCohomologyTheorem.lean#L104). References: SGA 5 VI (3.1), “Finite length of H^i(X”.

> **Stacks Project, Tag 0A56**, statement (4) of Situation 0A52: if `F` is constructible and
> torsion prime to `char(k)` then `H^q(X, F)` is finite.

```lean
theorem finiteCohomologyOfPrimeToCharacteristic (B : BigEtaleSite.{u}) (hX : B.Contains S.X)
    [HasExt.{w} (Sheaf S.X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v})] :
    S.FiniteCohomologyOfPrimeToCharacteristic.{u, v, w} B hX
```

**`Stacks.EtaleCohomology.TorsionSheafSituation.FiniteCohomologyOfPrimeToCharacteristic`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/PrimeToCharacteristicFiniteness.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/PrimeToCharacteristicFiniteness.lean#L89). The attribute's comment: “statement (4) of Situation 0A52, as a predicate on the situation”.

> Statement (4) of Situation 0A52. For an algebraically closed
> field `k`, a separated finite-type scheme `X` of dimension at most one over `k` and a torsion
> abelian sheaf `F` on the small étale site of `X`: if `F` is constructible and its torsion is prime
> to the characteristic of `k`, then `H^q_étale(X, F)` is finite for every `q`.
>
> "Torsion prime to the characteristic" is taken at the exponential characteristic.

```lean
def FiniteCohomologyOfPrimeToCharacteristic : Prop
```

## Tag 0A57, an item

[Tag 0A57](https://stacks.math.columbia.edu/tag/0A57) in the Stacks Project.

**`Stacks.EtaleCohomology.TorsionSheafSituation.finiteCohomologyOfIsProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/CurveCohomologyTheorem.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/CurveCohomologyTheorem.lean#L114).

> **Stacks Project, Tag 0A57**, statement (5) of Situation 0A52: if `X` is proper and `F` is
> constructible then `H^q(X, F)` is finite.

```lean
theorem finiteCohomologyOfIsProper (B : BigEtaleSite.{u}) (hX : B.Contains S.X)
    [HasExt.{w} (Sheaf S.X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v})] :
    S.FiniteCohomologyOfIsProper.{u, v, w} B hX
```

**`Stacks.EtaleCohomology.TorsionSheafSituation.FiniteCohomologyOfIsProper`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/ProperFinitenessStatement.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/ProperFinitenessStatement.lean#L151). The attribute's comment: “statement (5) of Situation 0A52, as a predicate on the situation”.

> **Stacks Project, Tag 0A57**, statement (5) of Situation 0A52. For an algebraically closed
> field `k`, a separated finite-type scheme `X` of dimension at most one over `k` and a torsion
> abelian sheaf `F` on the small étale site of `X`: if the structure morphism of `X` is proper and
> `F` is constructible, then `H^q_étale(X, F)` is finite for every `q`.
>
> The source states this as one entry of the list of eight statements that Situation 0A52 asks
> for, not as an assertion, so it is a predicate on the data of the situation.

```lean
def TorsionSheafSituation.FiniteCohomologyOfIsProper (S : TorsionSheafSituation.{u, v})
    (B : BigEtaleSite.{u}) (hX : B.Contains S.X)
    [HasExt.{w} (Sheaf S.X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v})] : Prop
```

## Tag 0A58, an item

[Tag 0A58](https://stacks.math.columbia.edu/tag/0A58) in the Stacks Project.

**`Stacks.EtaleCohomology.TorsionSheafSituation.BaseChangePrimeToCharacteristic`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/BaseChangePrimeToCharacteristic.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/BaseChangePrimeToCharacteristic.lean#L63). The attribute's comment: “statement (6) of Situation 0A52, as a predicate on the situation”.

> Statement (6) of the list of statements of Situation 0A52: if the torsion of the situation's
> abelian sheaf `F` is prime to the characteristic of the algebraically closed ground field `k`,
> then for every algebraically closed extension `k'/k` and every degree `q` the restriction map
> `H^q_étale(X, F) → H^q_étale(X_{k'}, F|_{X_{k'}})` is bijective.
>
> "Torsion prime to the characteristic" is taken at the exponential characteristic, so that in
> characteristic zero it is the torsion condition the situation already carries.

```lean
def TorsionSheafSituation.BaseChangePrimeToCharacteristic
    (S : TorsionSheafSituation.{u, v}) : Prop
```

**`Stacks.EtaleCohomology.TorsionSheafSituation.baseChangePrimeToCharacteristic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/CurveCohomologyTheorem.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/CurveCohomologyTheorem.lean#L125).

> **Stacks Project, Tag 0A58**, statement (6) of Situation 0A52: if `F` is torsion prime to
> `char(k)` then `H^q(X, F) → H^q(X_{k'}, F|_{X_{k'}})` is bijective for every extension `k'/k` of
> algebraically closed fields.

```lean
theorem baseChangePrimeToCharacteristic : S.BaseChangePrimeToCharacteristic.{u, v, w}
```

## Tag 0A59, an item

[Tag 0A59](https://stacks.math.columbia.edu/tag/0A59) in the Stacks Project.

**`Stacks.EtaleCohomology.TorsionSheafSituation.ProperBaseChangeStatement`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/ProperBaseChangeStatement.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/ProperBaseChangeStatement.lean#L58). The attribute's comment: “item (7) of Situation 0A52, as a predicate on the situation”.

> Statement (7) of Situation 0A52. For an algebraically closed field `k`, a separated
> finite-type scheme `X` of dimension at most one over `k` and a torsion abelian sheaf `F` on the
> small étale site of `X`: if the structure morphism of `X` is proper then
> `H^q_étale(X, F) → H^q_étale(X_{k'}, F|_{X_{k'}})` is an isomorphism in every degree, for every
> extension `k'/k` of algebraically closed fields.

```lean
def TorsionSheafSituation.ProperBaseChangeStatement (S : TorsionSheafSituation.{u, v}) : Prop
```

**`Stacks.EtaleCohomology.TorsionSheafSituation.properBaseChangeStatement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/CurveCohomologyTheorem.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/CurveCohomologyTheorem.lean#L133).

> **Stacks Project, Tag 0A59**, statement (7) of Situation 0A52: if `X` is proper then
> `H^q(X, F) → H^q(X_{k'}, F|_{X_{k'}})` is bijective for every extension `k'/k` of algebraically
> closed fields.

```lean
theorem properBaseChangeStatement : S.ProperBaseChangeStatement.{u, v, w}
```

## Tag 0A5A, an item

[Tag 0A5A](https://stacks.math.columbia.edu/tag/0A5A) in the Stacks Project.

**`Stacks.EtaleCohomology.TorsionSheafSituation.isDegreeTwoOpenRestrictionSurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/CurveCohomologyTheorem.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/CurveCohomologyTheorem.lean#L140).

> **Stacks Project, Tag 0A5A**, statement (8) of Situation 0A52: `H²(X, F) → H²(U, F)` is
> surjective for every open `U ⊆ X`.

```lean
theorem isDegreeTwoOpenRestrictionSurjective
    [HasExt.{w} (Sheaf S.X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v})] :
    IsDegreeTwoOpenRestrictionSurjective.{u, v, w} S.F
```

**`Stacks.EtaleCohomology.IsDegreeTwoOpenRestrictionSurjective`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/DegreeTwoOpenRestrictionSurjectivity.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/DegreeTwoOpenRestrictionSurjectivity.lean#L48). The attribute's comment: “item (8) of 0A52: H²(X, F) → H²(U, F) surjective for all open U ⊆ X”.

> The restriction map `H²_étale(X, F) → H²_étale(U, F)` is surjective for every open subscheme
> `U ⊆ X`.

```lean
def IsDegreeTwoOpenRestrictionSurjective
    (F : Sheaf X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v}) : Prop
```

## Tag 0A5B, a lemma

[Tag 0A5B](https://stacks.math.columbia.edu/tag/0A5B) in the Stacks Project.

**`Stacks.EtaleCohomology.curveStatements_constantSheaf_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/SmoothConstantCurveStatements.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/SmoothConstantCurveStatements.lean#L98).

> **Stacks Project, Lemma 0A5B.** In Situation 0A52 — `k` algebraically closed, `X` separated,
> of finite type and of dimension at most one over `k` — assume `X` is smooth over `k` and let
> `F = 𝐙/ℓ𝐙` be the constant sheaf on `X_étale` for a prime `ℓ`, with value any abelian group `E`
> cyclic of order `ℓ`. Then statements (1) -- (8) of Situation 0A52 hold for `F`, in the sense of
> `Stacks.EtaleCohomology.CurveStatements`, at every coefficient universe and every `Ext`
> universe.
>
> On the smooth curve components of `X` this is `curveStatementsConstantOnSmoothCurves_of_prime`
> (Cases I and II of the source); the reduction theorem
> `curveStatements_of_torsionSheafProperty_max` carries it to `X` and to the coefficients
> `AddCommGrpCat.{max (u + 1) v}`, the constant sheaf with finite value being torsion.

```lean
theorem curveStatements_constantSheaf_of_smooth {k : Type u} [Field k] [IsAlgClosed k]
    {X : Scheme.{u}} (π : X ⟶ Spec (.of k)) [IsSeparated π] [LocallyOfFiniteType π]
    [QuasiCompact π] [Smooth π] (hdim : topologicalKrullDim X ≤ 1) {ℓ : ℕ} (hℓ : ℓ.Prime)
    (E : AddCommGrpCat.{max (u + 1) v}) (hE : Nonempty (E ≃+ ZMod ℓ))
    [HasExt.{w} (Sheaf X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v})] :
    CurveStatements.{u, v, w} π
      ((constantSheaf X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v}).obj E)
```

## Tag 0A47, a remark

[Tag 0A47](https://stacks.math.columbia.edu/tag/0A47) in the Stacks Project.

**`Stacks.ArtinSchreier.exact_affineLineBoundary`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ArtinSchreierSequence/AffineLine.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ArtinSchreierSequence/AffineLine.lean#L113). The attribute's comment: “the exact sequence k[x] → k[x] → H¹(A¹_k, Z/p) → 0, first arrow f ↦ f^p - f”.

> **The exact sequence `k[x] ⟶ k[x] ⟶ H¹(𝐀¹_k, 𝐙/p𝐙) ⟶ 0`.** Let `k` be a field of
> characteristic `p > 0`. The boundary of the Artin–Schreier sequence on the affine line is onto
> `H¹(𝐀¹_k, 𝐙/p𝐙)` and its kernel is the image of `f ↦ f ^ p - f`.
>
> The source states this for `k` algebraically closed; only the characteristic of `k` is needed.

```lean
theorem exact_affineLineBoundary :
    Function.Exact (ringArtinSchreier k[X] p) (affineLineBoundary.{w} k p) ∧
      Function.Surjective (affineLineBoundary.{w} k p)
```

**`Stacks.ArtinSchreier.existsUnique_affineLineBoundary_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ArtinSchreierSequence/AffineLine.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ArtinSchreierSequence/AffineLine.lean#L137). The attribute's comment: “every class of H¹(A¹_k, Z/p) is the image of exactly one sum over p ∤ n of λ_n x^n”.

> **The representatives, read in cohomology.** Let `k` be an algebraically closed field of
> characteristic `p > 0`. Every class in `H¹(𝐀¹_k, 𝐙/p𝐙)` is the boundary of exactly one polynomial
> `∑_{p ∤ n} λₙ xⁿ`.

```lean
theorem existsUnique_affineLineBoundary_eq [IsAlgClosed k]
    (c : Sheaf.H.{w} (etaleConstantZMod (affineLine k) p) 1) :
    ∃! f : k[X], (∀ n, p ∣ n → f.coeff n = 0) ∧ affineLineBoundary.{w} k p f = c
```

**`Stacks.ArtinSchreier.not_surjective_etaleCohomologyRestrictionMap_affineLine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ArtinSchreierSequence/AffineLine.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ArtinSchreierSequence/AffineLine.lean#L238). The attribute's comment: “H¹(A¹_k, Z/p) → H¹(A¹_{k'}, Z/p) is not surjective when k ⊊ k'”.

> **`H¹(𝐀¹_k, 𝐙/p𝐙) → H¹(𝐀¹_{k'}, 𝐙/p𝐙)` is not surjective.** Let `k` be an algebraically closed
> field of characteristic `p > 0` and `k'/k` an extension with `k' ≠ k`. Then the restriction map
> `H¹(𝐀¹_k, 𝐙/p𝐙) → H¹(𝐀¹_{k'}, 𝐙/p𝐙)` along `𝐀¹_{k'} ⟶ 𝐀¹_k` is not surjective — in particular not
> an isomorphism: for `λ ∈ k' ∖ k` the class of `λ x` is not in its image.
>
> The source takes `k'` algebraically closed; that is not used.

```lean
theorem not_surjective_etaleCohomologyRestrictionMap_affineLine [IsAlgClosed k]
    (hk : ¬ Function.Surjective (algebraMap k k'))
    [HasExt.{w} (Sheaf (affineLine k).smallEtaleTopology AddCommGrpCat.{u + 1})]
    [HasExt.{w} (Sheaf (scalarExtension k k' (affineLineStructure k)).smallEtaleTopology
      AddCommGrpCat.{u + 1})] :
    ¬ Function.Surjective (etaleCohomologyRestrictionMap.{u, 0, w}
      (scalarExtensionFst k k' (affineLineStructure k))
      (etaleConstantZMod (affineLine k) p) 1)
```

**`Stacks.ArtinSchreier.exists_not_bijective_etaleCohomologyRestrictionMap_affineLine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ArtinSchreierSequence/AffineLine.lean, line 291](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ArtinSchreierSequence/AffineLine.lean#L291). The attribute's comment: “so H¹(A¹_k, Z/p) → H¹(A¹_{k'}, Z/p) is not an isomorphism in general”.

> **The restriction map is not an isomorphism in general.** For every algebraically closed field
> `k` of characteristic `p > 0` there is an algebraically closed extension `k'/k` — an algebraic
> closure of `k(t)` — for which `H¹(𝐀¹_k, 𝐙/p𝐙) → H¹(𝐀¹_{k'}, 𝐙/p𝐙)` is not an isomorphism.

```lean
theorem exists_not_bijective_etaleCohomologyRestrictionMap_affineLine [IsAlgClosed k] :
    ∃ (k' : Type u) (_ : Field k') (_ : Algebra k k') (_ : IsAlgClosed k'),
      ∀ [HasExt.{w} (Sheaf (affineLine k).smallEtaleTopology AddCommGrpCat.{u + 1})]
        [HasExt.{w} (Sheaf (scalarExtension k k' (affineLineStructure k)).smallEtaleTopology
          AddCommGrpCat.{u + 1})],
        ¬ Function.Bijective (etaleCohomologyRestrictionMap.{u, 0, w}
          (scalarExtensionFst k k' (affineLineStructure k))
          (etaleConstantZMod (affineLine k) p) 1)
```

**`Stacks.ArtinSchreier.bijective_etaleCohomologyRestrictionMap_affineLine_of_isUnit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ArtinSchreierSequence/AffineLine.lean, line 338](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ArtinSchreierSequence/AffineLine.lean#L338). The attribute's comment: “only in characteristic p with p-power torsion: bijective for Z/n, n invertible in k”.

> **The phenomenon only occurs with `p`-power torsion coefficients.** Let `k'/k` be an
> extension of algebraically closed fields and let `n` be invertible in `k`. Then
> `H^q(𝐀¹_k, 𝐙/n𝐙) → H^q(𝐀¹_{k'}, 𝐙/n𝐙)` is bijective in every degree `q`: this is statement (6)
> of Situation 0A52 (Tag 0A58) for the affine line. In characteristic `0` every `n ≥ 1` is
> invertible, so the base change map is an isomorphism for every finite cyclic coefficient group.

```lean
theorem bijective_etaleCohomologyRestrictionMap_affineLine_of_isUnit {n : ℕ} (hn : IsUnit (n : k))
    [HasExt.{w} (Sheaf (affineLine k).smallEtaleTopology AddCommGrpCat.{max (u + 1) v})]
    [HasExt.{w} (Sheaf (scalarExtension k k' (affineLineStructure k)).smallEtaleTopology
      AddCommGrpCat.{max (u + 1) v})] (q : ℕ) :
    Function.Bijective (etaleCohomologyRestrictionMap.{u, v, w}
      (scalarExtensionFst k k' (affineLineStructure k))
      ((constantSheaf (affineLine k).smallEtaleTopology AddCommGrpCat.{max (u + 1) v}).obj
        (AddCommGrpCat.of (ULift.{max (u + 1) v} (ZMod n)))) q)
```

**`Stacks.ArtinSchreier.not_bijective_etaleFundamentalGroupMap_affineLine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/AffineLineScalarExtension.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/AffineLineScalarExtension.lean#L223). The attribute's comment: “π₁(A¹_{k'}) → π₁(A¹_k) is not an isomorphism for algebraically closed k ⊊ k'”. References: SGA 1 IX (6.3), “more general”; SGA 1 X (1.10), “partial”; SGA 1 XIII (2.13), “partial”.

> **[Stacks, Tag 0A47]: `π₁(𝐀¹_{k'}) → π₁(𝐀¹_k)` is not an isomorphism.** Let `k'/k` be an
> extension of algebraically closed fields of characteristic `p > 0` with `k' ≠ k`. Then for every
> geometric point `x` of `𝐀¹_{k'}` the map of étale fundamental groups
> `π₁(𝐀¹_{k'}, x) → π₁(𝐀¹_k, x)` induced by `𝐀¹_{k'} ⟶ 𝐀¹_k` is not bijective.

```lean
theorem not_bijective_etaleFundamentalGroupMap_affineLine {p : ℕ} [hp : Fact p.Prime] [CharP k p]
    [IsAlgClosed k] [IsAlgClosed k'] (hk : ¬ Function.Surjective (algebraMap k k'))
    (x : GeometricPoint (scalarExtension k k' (affineLineStructure k))) :
    ¬ Function.Bijective
      (etaleFundamentalGroupMap (scalarExtensionFst k k' (affineLineStructure k)) x)
```

**`Stacks.ArtinSchreier.exists_not_bijective_etaleFundamentalGroupMap_affineLine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/AffineLineScalarExtension.lean, line 273](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/AffineLineScalarExtension.lean#L273). The attribute's comment: “so the étale fundamental group of A¹ depends on the algebraically closed field”. References: SGA 1 IX (6.3); SGA 1 X (1.10), “partial”.

> **[Stacks, Tag 0A47]: the étale fundamental group of the affine line depends on the
> algebraically closed ground field.** For every algebraically closed field `k` of characteristic
> `p > 0` there is an algebraically closed extension `k'/k` — an algebraic closure of `k(t)` — for
> which `π₁(𝐀¹_{k'}, x) → π₁(𝐀¹_k, x)` is not bijective at any geometric point `x`.
>
> The source concludes that the étale homotopy type of the affine line depends on the algebraically
> closed ground field; the étale homotopy type is not available here, and this statement, with
> `Stacks.ArtinSchreier.exists_not_bijective_etaleCohomologyRestrictionMap_affineLine` for `H¹`, is
> the content of that conclusion for the invariants `π₁` and `H¹` of the homotopy type.

```lean
theorem exists_not_bijective_etaleFundamentalGroupMap_affineLine {p : ℕ} [Fact p.Prime]
    [CharP k p] [IsAlgClosed k] :
    ∃ (k' : Type u) (_ : Field k') (_ : Algebra k k') (_ : IsAlgClosed k'),
      ∀ x : GeometricPoint (scalarExtension k k' (affineLineStructure k)),
        ¬ Function.Bijective
          (etaleFundamentalGroupMap (scalarExtensionFst k k' (affineLineStructure k)) x)
```

**`Polynomial.existsUnique_sub_mem_range_ringArtinSchreier`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Polynomial/ArtinSchreierCokernel.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Polynomial/ArtinSchreierCokernel.lean#L171). The attribute's comment: “the polynomials sum over p ∤ n of λ_n x^n represent the cokernel of f ↦ f^p - f”.

> **[Stacks, Tag 0A47], the representatives of the cokernel.** Let `k` be an algebraically
> closed field of characteristic `p > 0`. Every polynomial `g ∈ k[x]` is congruent modulo the image
> of `f ↦ f ^ p - f` to exactly one polynomial `∑_{p ∤ n} λₙ xⁿ`, that is, to exactly one
> polynomial with no coefficient in a degree divisible by `p` (the degree `0` included). In other
> words these polynomials form a set of representatives for the cokernel of
> `k[x] → k[x], f ↦ f ^ p - f`.

```lean
theorem existsUnique_sub_mem_range_ringArtinSchreier [IsAlgClosed k] (g : k[X]) :
    ∃! f : k[X], (∀ n, p ∣ n → f.coeff n = 0) ∧
      g - f ∈ (ringArtinSchreier k[X] p).range
```

**`Polynomial.exists_sub_mem_range_ringArtinSchreier_of_perfectRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Polynomial/ArtinSchreierCokernel.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Polynomial/ArtinSchreierCokernel.lean#L225). The attribute's comment: “if k is not algebraically closed, constants have to be added (k perfect)”.

> **[Stacks, Tag 0A47], the parenthetical case of a field that is not algebraically closed.**
> Let `k` be a perfect field of characteristic `p > 0`. Then the representatives of the cokernel of
> `f ↦ f ^ p - f` on `k[x]` need constants added: every `g ∈ k[x]` is congruent to a polynomial
> `∑_{p ∤ n} λₙ xⁿ + c`, and two such polynomials are congruent exactly when their coefficients
> `λₙ` agree and their constant terms differ by a value `a ^ p - a` of `k`. So the constants needed
> are a set of representatives of `k / {a ^ p - a}`, which is zero for algebraically closed `k`.
>
> The source says "if `k` is not algebraically closed"; perfectness is needed and is assumed here:
> over an imperfect field the description fails, by
> `Polynomial.not_exists_sub_mem_range_ringArtinSchreier_of_not_pth_power`.

```lean
theorem exists_sub_mem_range_ringArtinSchreier_of_perfectRing [PerfectRing k p] :
    (∀ g : k[X], ∃ f : k[X], (∀ n, 0 < n → p ∣ n → f.coeff n = 0) ∧
      g - f ∈ (ringArtinSchreier k[X] p).range) ∧
    ∀ f f' : k[X], (∀ n, 0 < n → p ∣ n → f.coeff n = 0) →
      (∀ n, 0 < n → p ∣ n → f'.coeff n = 0) →
      (f - f' ∈ (ringArtinSchreier k[X] p).range ↔
        (∀ n, n ≠ 0 → f.coeff n = f'.coeff n) ∧
          f.coeff 0 - f'.coeff 0 ∈ (ringArtinSchreier k p).range)
```

## Tag 0A5C, a lemma

[Tag 0A5C](https://stacks.math.columbia.edu/tag/0A5C) in the Stacks Project.

**`Stacks.EtaleCohomology.CurveStatements.of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/CurveStatementsShortExactConstructible.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/CurveStatementsShortExactConstructible.lean#L101). The attribute's comment: “all eight statements of 0A52 at once, at the coefficients AddCommGrpCat.{u+1}”.

> Let `0 → F₁ → F → F₂ → 0` be a short exact sequence of abelian sheaves on the small étale
> site of a Noetherian scheme `X` over a field. If statements (1) -- (8) of Situation 0A52 hold for
> `F₁` and `F₂`, then they hold for `F`.

```lean
theorem CurveStatements.of_shortExact (hS : S.ShortExact)
    (h₁ : CurveStatements.{u, 0, w} π S.X₁) (h₃ : CurveStatements.{u, 0, w} π S.X₃) :
    CurveStatements.{u, 0, w} π S.X₂
```

**`Stacks.EtaleCohomology.curveCohomologyStatements_X₂_of_shortExact_isConstructible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/ShortExactCurveStatements.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/ShortExactCurveStatements.lean#L210). The attribute's comment: “the eight statements of Situation 0A52 pass to the middle term of a short exact sequence of abelian sheaves, with constructibility of the sub- and the quotient sheaf supplied by Proposition 09BH (2)”.

> **Stacks Project, Tag 0A5C.** Let `X` be a Noetherian scheme, let `π` be a morphism from `X`
> to the spectrum of a field, let `i` be a morphism of schemes to `X`, and let
> `0 → S.X₁ → S.X₂ → S.X₃ → 0` be a short exact sequence of abelian sheaves on the small étale site
> of `X`. If the eight statements of Situation 0A52 hold for `S.X₁` and for `S.X₃`, then they hold
> for `S.X₂`.
>
> The eight statements, bundled as `Stacks.EtaleCohomology.CurveCohomologyStatements`, are: the
> vanishing of `H^q(X, -)` above degree two; its vanishing above degree one over an affine `X`; its
> vanishing above degree one for coefficients of `l`-power torsion; the finiteness of `H^q(X, -)`
> for constructible coefficients of torsion prime to `p`; its finiteness for constructible
> coefficients over a proper `X`; the bijectivity of restriction along `i` for coefficients of
> torsion prime to `p`; the bijectivity of restriction along `i` over a proper `X`; and the
> surjectivity of restriction along `i` in degree two. In the source `l` and `p` are the
> characteristic and the exponential characteristic of the base field, and `i` is the projection of
> a scalar extension along an extension of algebraically closed fields in statements (6) and (7)
> and the inclusion of an open subscheme in statement (8); none of those identifications is imposed
> here, so this statement is stronger than the one the source makes.
>
> Constructibility of an abelian sheaf is `AlgebraicGeometry.IsConstructibleEtaleSiteAbelianSheaf`,
> read on the small étale site of Stacks 021B across its dense subsite comparison with the site
> `AlgebraicGeometry.Scheme.smallEtaleTopology` that carries the cohomology. Its descent to the sub-
> and the quotient sheaf of a short exact sequence, which statements (4) and (5) need, is
> Proposition 09BH (2) and is what the Noetherian hypothesis is for; the other six transfers use no
> hypothesis on `X` at all. Situation 0A52 asks `X` to be separated of finite type over an
> algebraically closed field and of dimension at most one, and asks the sheaves to be torsion;
> finite type over a field makes `X` Noetherian, and the remaining hypotheses are not used and so do
> not appear.

```lean
theorem curveCohomologyStatements_X₂_of_shortExact_isConstructible [IsNoetherian X.obj]
    {k : Type u} [Field k] (π : X.obj ⟶ Spec (.of k)) (l p : ℕ) (hS : S.ShortExact)
    (h₁ : CurveCohomologyStatements.{u, u + 1, w} i π l p
      (IsConstructibleEtaleSiteAbelianSheaf B X) S.X₁)
    (h₃ : CurveCohomologyStatements.{u, u + 1, w} i π l p
      (IsConstructibleEtaleSiteAbelianSheaf B X) S.X₃) :
    CurveCohomologyStatements.{u, u + 1, w} i π l p
      (IsConstructibleEtaleSiteAbelianSheaf B X) S.X₂
```

**`Stacks.EtaleCohomology.finite_etaleCohomology_X₂_of_shortExact_of_isPrimeToCharacteristicTorsion_isConstructible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/ShortExactCurveStatements.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/ShortExactCurveStatements.lean#L236). The attribute's comment: “statement (4): the finiteness of etale cohomology for constructible coefficients of torsion prime to the characteristic passes to the middle term of a short exact sequence, with the constructibility of the sub- and the quotient sheaf supplied by Proposition 09BH (2)”.

> **Statement (4) of Situation 0A52 passes to extensions, for constructible coefficients.** Let
> `X` be a Noetherian scheme, let `p` be a natural number — the characteristic of the base field in
> the source — and let `0 → S.X₁ → S.X₂ → S.X₃ → 0` be a short exact sequence of abelian sheaves on
> the small étale site of `X`. If the finiteness of étale cohomology for coefficients that are
> constructible and torsion prime to `p` holds for the sub- and the quotient sheaf, then it holds
> for the middle sheaf.
>
> This is `finite_etaleCohomology_X₂_of_shortExact_of_isPrimeToCharacteristicTorsion` with the
> coefficient condition taken to be constructibility of an abelian sheaf and its descent to the sub-
> and the quotient sheaf *discharged*, by Proposition 09BH (2), rather than assumed: that descent is
> what Tag 0A5C cites at this point, and it is the only use of the Noetherian hypothesis.

```lean
theorem finite_etaleCohomology_X₂_of_shortExact_of_isPrimeToCharacteristicTorsion_isConstructible
    [IsNoetherian X.obj] (p : ℕ) (hS : S.ShortExact)
    (h₁ : IsConstructibleEtaleSiteAbelianSheaf B X S.X₁ →
      Stacks.Torsion.IsPrimeToCharacteristicTorsion X.obj.smallEtaleTopology p S.X₁ →
      ∀ q : ℕ, Finite (Sheaf.H.{w} S.X₁ q))
    (h₃ : IsConstructibleEtaleSiteAbelianSheaf B X S.X₃ →
      Stacks.Torsion.IsPrimeToCharacteristicTorsion X.obj.smallEtaleTopology p S.X₃ →
      ∀ q : ℕ, Finite (Sheaf.H.{w} S.X₃ q))
    (hc : IsConstructibleEtaleSiteAbelianSheaf B X S.X₂)
    (ht : Stacks.Torsion.IsPrimeToCharacteristicTorsion X.obj.smallEtaleTopology p S.X₂)
    (q : ℕ) :
    Finite (Sheaf.H.{w} S.X₂ q)
```

**`Stacks.EtaleCohomology.finite_etaleCohomology_X₂_of_shortExact_of_isProper_isConstructible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/ShortExactCurveStatements.lean, line 266](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/ShortExactCurveStatements.lean#L266). The attribute's comment: “statement (5): the finiteness of etale cohomology for constructible coefficients over a proper scheme passes to the middle term of a short exact sequence, with the constructibility of the sub- and the quotient sheaf supplied by Proposition 09BH (2)”.

> **Statement (5) of Situation 0A52 passes to extensions, for constructible coefficients.** Let
> `X` be a Noetherian scheme, let `π` be its structure morphism to the spectrum of a field, and let
> `0 → S.X₁ → S.X₂ → S.X₃ → 0` be a short exact sequence of abelian sheaves on the small étale site
> of `X`. If the finiteness of étale cohomology for constructible coefficients over a proper `X`
> holds for the sub- and the quotient sheaf, then it holds for the middle sheaf.
>
> This is `Stacks.EtaleCohomology.finite_etaleCohomology_X₂_of_shortExact_of_isProper` with the
> coefficient condition taken to be constructibility of an abelian sheaf and its descent to the sub-
> and the quotient sheaf discharged by Proposition 09BH (2), exactly as in statement (4). The
> properness condition constrains the scheme and is passed to the outer terms unchanged.

```lean
theorem finite_etaleCohomology_X₂_of_shortExact_of_isProper_isConstructible
    [IsNoetherian X.obj] {k : Type u} [Field k] (π : X.obj ⟶ Spec (.of k)) (hS : S.ShortExact)
    (h₁ : IsConstructibleEtaleSiteAbelianSheaf B X S.X₁ → IsProper π →
      ∀ q : ℕ, Finite (Sheaf.H.{w} S.X₁ q))
    (h₃ : IsConstructibleEtaleSiteAbelianSheaf B X S.X₃ → IsProper π →
      ∀ q : ℕ, Finite (Sheaf.H.{w} S.X₃ q))
    (hc : IsConstructibleEtaleSiteAbelianSheaf B X S.X₂) (hπ : IsProper π) (q : ℕ) :
    Finite (Sheaf.H.{w} S.X₂ q)
```

**`Stacks.EtaleCohomology.subsingleton_etaleCohomology_X₂_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/ShortExactExtension.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/ShortExactExtension.lean#L72). The attribute's comment: “vanishing”.

> If the étale cohomology of the sub- and the quotient sheaf of a short exact sequence of abelian
> sheaves vanishes above degree two, then so does that of the middle sheaf.

```lean
theorem subsingleton_etaleCohomology_X₂_of_shortExact (hS : S.ShortExact)
    (h₁ : ∀ q : ℕ, 2 < q → Subsingleton (Sheaf.H.{w} S.X₁ q))
    (h₃ : ∀ q : ℕ, 2 < q → Subsingleton (Sheaf.H.{w} S.X₃ q))
    (q : ℕ) (hq : 2 < q) :
    Subsingleton (Sheaf.H.{w} S.X₂ q)
```

**`Stacks.EtaleCohomology.subsingleton_etaleCohomology_X₂_of_shortExact_of_isAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/ShortExactExtension.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/ShortExactExtension.lean#L85). The attribute's comment: “affine vanishing”.

> If, for an affine scheme, the étale cohomology of the sub- and the quotient sheaf of a short
> exact sequence of abelian sheaves vanishes above degree one, then so does that of the middle
> sheaf.

```lean
theorem subsingleton_etaleCohomology_X₂_of_shortExact_of_isAffine (hS : S.ShortExact)
    (h₁ : IsAffine X → ∀ q : ℕ, 1 < q → Subsingleton (Sheaf.H.{w} S.X₁ q))
    (h₃ : IsAffine X → ∀ q : ℕ, 1 < q → Subsingleton (Sheaf.H.{w} S.X₃ q))
    (hX : IsAffine X) (q : ℕ) (hq : 1 < q) :
    Subsingleton (Sheaf.H.{w} S.X₂ q)
```

**`Stacks.EtaleCohomology.subsingleton_etaleCohomology_X₂_of_shortExact_of_isPrimePowerTorsion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/ShortExactExtension.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/ShortExactExtension.lean#L98). The attribute's comment: “characteristic-primary vanishing”.

> Let `l` be a natural number. If the vanishing of étale cohomology above degree one for
> `l`-power torsion coefficients holds for the sub- and the quotient sheaf of a short exact sequence
> of abelian sheaves, then it holds for the middle sheaf.

```lean
theorem subsingleton_etaleCohomology_X₂_of_shortExact_of_isPrimePowerTorsion
    (l : ℕ) (hS : S.ShortExact)
    (h₁ : Stacks.Torsion.IsPrimePowerTorsion X.smallEtaleTopology l S.X₁ →
      ∀ q : ℕ, 1 < q → Subsingleton (Sheaf.H.{w} S.X₁ q))
    (h₃ : Stacks.Torsion.IsPrimePowerTorsion X.smallEtaleTopology l S.X₃ →
      ∀ q : ℕ, 1 < q → Subsingleton (Sheaf.H.{w} S.X₃ q))
    (h₂ : Stacks.Torsion.IsPrimePowerTorsion X.smallEtaleTopology l S.X₂) (q : ℕ) (hq : 1 < q) :
    Subsingleton (Sheaf.H.{w} S.X₂ q)
```

**`Stacks.EtaleCohomology.bijective_etaleCohomologyRestrictionMap_X₂_of_shortExact_of_isPrimeToCharacteristicTorsion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/ShortExactExtension.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/ShortExactExtension.lean#L171). The attribute's comment: “prime-to-characteristic base change”.

> Let `p` be a natural number and let `i` be a morphism of schemes. If the bijectivity of
> restriction along `i` for coefficients of torsion prime to `p` holds in every degree for the sub-
> and the quotient sheaf of a short exact sequence of abelian sheaves, then it holds for the middle
> sheaf.

```lean
theorem bijective_etaleCohomologyRestrictionMap_X₂_of_shortExact_of_isPrimeToCharacteristicTorsion
    (p : ℕ) (hS : S.ShortExact)
    (h₁ : Stacks.Torsion.IsPrimeToCharacteristicTorsion X.smallEtaleTopology p S.X₁ →
      ∀ q, Function.Bijective (etaleCohomologyRestrictionMap.{u, v, w} i S.X₁ q))
    (h₃ : Stacks.Torsion.IsPrimeToCharacteristicTorsion X.smallEtaleTopology p S.X₃ →
      ∀ q, Function.Bijective (etaleCohomologyRestrictionMap.{u, v, w} i S.X₃ q))
    (h₂ : Stacks.Torsion.IsPrimeToCharacteristicTorsion X.smallEtaleTopology p S.X₂) (q : ℕ) :
    Function.Bijective (etaleCohomologyRestrictionMap.{u, v, w} i S.X₂ q)
```

**`Stacks.EtaleCohomology.bijective_etaleCohomologyRestrictionMap_X₂_of_shortExact_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/ShortExactExtension.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/ShortExactExtension.lean#L187). The attribute's comment: “proper base change”.

> Let `π` be a morphism from `X` to the spectrum of a field `k` and let `i` be a morphism of
> schemes. If the bijectivity of restriction along `i` when `π` is proper holds in every degree for
> the sub- and the quotient sheaf of a short exact sequence of abelian sheaves, then it holds for
> the middle sheaf.

```lean
theorem bijective_etaleCohomologyRestrictionMap_X₂_of_shortExact_of_isProper
    {k : Type u} [Field k] (π : X ⟶ Spec (.of k)) (hS : S.ShortExact)
    (h₁ : IsProper π → ∀ q, Function.Bijective (etaleCohomologyRestrictionMap.{u, v, w} i S.X₁ q))
    (h₃ : IsProper π → ∀ q, Function.Bijective (etaleCohomologyRestrictionMap.{u, v, w} i S.X₃ q))
    (hπ : IsProper π) (q : ℕ) :
    Function.Bijective (etaleCohomologyRestrictionMap.{u, v, w} i S.X₂ q)
```

**`Stacks.EtaleCohomology.surjective_etaleCohomologyRestrictionMap_X₂_of_shortExact_of_vanishing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/ShortExactExtension.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/ShortExactExtension.lean#L200). The attribute's comment: “restriction surjectivity”.

> Let `i` be a morphism of schemes. If restriction along `i` is surjective in degree two for the
> sub- and the quotient sheaf of a short exact sequence of abelian sheaves, and the étale
> cohomology of the sub-sheaf vanishes above degree two, then restriction is surjective in degree
> two for the middle sheaf.

```lean
theorem surjective_etaleCohomologyRestrictionMap_X₂_of_shortExact_of_vanishing (hS : S.ShortExact)
    (hvanishing : ∀ q : ℕ, 2 < q → Subsingleton (Sheaf.H.{w} S.X₁ q))
    (h₁ : Function.Surjective (etaleCohomologyRestrictionMap.{u, v, w} i S.X₁ 2))
    (h₃ : Function.Surjective (etaleCohomologyRestrictionMap.{u, v, w} i S.X₃ 2)) :
    Function.Surjective (etaleCohomologyRestrictionMap.{u, v, w} i S.X₂ 2)
```

## Tag 0A5D, a lemma

[Tag 0A5D](https://stacks.math.columbia.edu/tag/0A5D) in the Stacks Project.

**`Stacks.EtaleCohomology.CurveStatements.directImage_of_isFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/CurveStatementsFiniteDirectImageGeneral.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/CurveStatementsFiniteDirectImageGeneral.lean#L104). The attribute's comment: “all eight statements of 0A52 at once, at the coefficients AddCommGrpCat.{u+1}; only f finite and X Noetherian are used”.

> **Stacks Project, Lemma 0A5D.** Let `f : X ⟶ Y` be a finite morphism of schemes over a field
> `k`, with `X` Noetherian, and let `F` be an abelian sheaf on `X_étale`. If statements (1) -- (8)
> of Situation 0A52 hold for `F`, they hold for `f_* F`.

```lean
theorem CurveStatements.directImage_of_isFinite [IsNoetherian X]
    [HasExt.{u + 1} (Sheaf X.smallEtaleTopology AddCommGrpCat.{u + 1})]
    [HasExt.{u + 1} (Sheaf Y.smallEtaleTopology AddCommGrpCat.{u + 1})]
    {F : Sheaf X.smallEtaleTopology AddCommGrpCat.{u + 1}}
    (h : CurveStatements.{u, 0, u + 1} (f ≫ π) F) :
    CurveStatements.{u, 0, u + 1} π ((etaleAbelianDirectImage.{u, 0} f).obj F)
```

**`Stacks.EtaleCohomology.curveCohomologyStatements_smallEtaleDirectImageAb`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/FiniteDirectImage.lean, line 303](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/FiniteDirectImage.lean#L303). The attribute's comment: “the eight statements of Situation 0A52 pass to a finite direct image, over the Leray comparison and over the transfer of the torsion and constructibility side conditions”.

> Let `f : X ⟶ Y` be a finite morphism of schemes and let `F` be an abelian sheaf on the small
> étale site of `X`. If the eight statements of Situation 0A52 hold for `F`, relative to the
> structure morphism `f ≫ π` of `X` and to restriction along `j`, then they hold for the direct
> image `f_* F`, relative to the structure morphism `π` of `Y` and to restriction along `i`.
>
> The input is the comparison `c` of the étale cohomology of `F` with that of `f_* F`, which for a
> finite morphism comes from the vanishing of the higher direct images and the Leray spectral
> sequence. Beyond it the proof needs that the side conditions of the eight statements move between
> the two sheaves. The two conditions on the scheme move by finiteness of `f`: an affine `Y` forces
> an affine `X`, and a proper `π` forces a proper `f ≫ π`. The three conditions on the coefficient
> sheaf are carried: `hprimePower` and `hprimeToChar` for the two torsion conditions and
> `hconstructible` for constructibility, each in the direction from `f_* F` to `F`, which for a
> finite morphism holds because the stalks of `f_* F` are the sums of the stalks of `F` over the
> fibres.

```lean
theorem curveCohomologyStatements_smallEtaleDirectImageAb {k : Type u} [Field k]
    (π : Y ⟶ Spec (.of k)) (l p : ℕ) [IsFinite f]
    {constructibleSource : Sheaf X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v} → Prop}
    {constructibleTarget : Sheaf Y.smallEtaleTopology AddCommGrpCat.{max (u + 1) v} → Prop}
    (c : DirectImageCohomologyComparison.{u, v, w} f i j F)
    (hprimePower : Stacks.Torsion.IsPrimePowerTorsion Y.smallEtaleTopology l
        ((smallEtaleDirectImageAb f).obj F) →
      Stacks.Torsion.IsPrimePowerTorsion X.smallEtaleTopology l F)
    (hprimeToChar : Stacks.Torsion.IsPrimeToCharacteristicTorsion Y.smallEtaleTopology p
        ((smallEtaleDirectImageAb f).obj F) →
      Stacks.Torsion.IsPrimeToCharacteristicTorsion X.smallEtaleTopology p F)
    (hconstructible : constructibleTarget ((smallEtaleDirectImageAb f).obj F) →
      constructibleSource F)
    (h : CurveCohomologyStatements.{u, v, w} j (f ≫ π) l p constructibleSource F) :
    CurveCohomologyStatements.{u, v, w} i π l p constructibleTarget
      ((smallEtaleDirectImageAb f).obj F)
```

**`Stacks.EtaleCohomology.curveCohomologyAssertions_smallEtaleDirectImageAb`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/FiniteDirectImageCurveAssertions.lean, line 498](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/FiniteDirectImageCurveAssertions.lean#L498). The attribute's comment: “statements (1)-(8) of Situation 0A52 pass to f_* for finite f”.

> Let `k` be a field, let `f : X ⟶ Y` be a finite morphism of schemes of finite type over `k`,
> and let `F` be an abelian sheaf on the small étale site of `X`. If statements (1) – (8) of
> Situation 0A52 hold for `F`, then they hold for `f_* F`.
>
> Statements (1) – (8) are `Stacks.EtaleCohomology.CurveCohomologyAssertions`, read on `X`
> relative to its structure morphism `f ≫ π` and on `Y` relative to `π`, with constructibility read
> in a big étale site `B` containing both schemes. The remaining hypotheses of Situation 0A52 —
> that `k` is algebraically closed, that `X` and `Y` are separated of dimension at most one, and
> that `F` is torsion — are not assumed.

```lean
theorem curveCohomologyAssertions_smallEtaleDirectImageAb (π : Y ⟶ Spec (.of k))
    [LocallyOfFiniteType π] [QuasiCompact π] (f : X ⟶ Y) [IsFinite f]
    {F : Sheaf X.smallEtaleTopology AddCommGrpCat.{u + 1}}
    (h : CurveCohomologyAssertions B hX (f ≫ π) F) :
    CurveCohomologyAssertions B hY π ((smallEtaleDirectImageAb f).obj F)
```

## Tag 0GJA, a lemma

[Tag 0GJA](https://stacks.math.columbia.edu/tag/0GJA) in the Stacks Project.

**`Stacks.EtaleCohomology.curveStatements_iff_curveStatements_extensionByZero_of_dense`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/CurveCohomologyTheorem.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/CurveCohomologyTheorem.lean#L163). The attribute's comment: “for every torsion sheaf F, not only constructible ones”.

> In Situation 0A52 let `j : X' → X` be the inclusion of a dense open subscheme. Then statements
> (1) -- (8) hold for `F` if and only if they hold for `j_! j^{-1} F`.
>
> The source assumes `F` constructible; that is not needed here, both sides being true for every
> torsion `F` by Theorem 03SC (`j_! j^{-1} F` is a subsheaf of `F`, hence torsion). The direction
> from `j_! j^{-1} F` to `F` is the dense-open reduction of
> `Stacks.EtaleCohomology.curveStatements_of_curveStatements_extensionByZero_of_dense`.

```lean
theorem curveStatements_iff_curveStatements_extensionByZero_of_dense
    (F : Sheaf X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v})
    (hF : Stacks.Torsion.torsionSheafProperty X.smallEtaleTopology F) :
    CurveStatements.{u, v, w} π F ↔ CurveStatements.{u, v, w} π
      ((extensionByZero.{u, v} j).obj ((etaleRestriction.{u, v} j).obj F))
```

## Tag 03SG, a lemma

[Tag 03SG](https://stacks.math.columbia.edu/tag/03SG) in the Stacks Project.

**`Stacks.EtaleCohomology.curveStatements_extensionByZero_zmod_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/SmoothExtensionByZeroCurveStatements.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/SmoothExtensionByZeroCurveStatements.lean#L66).

> **Stacks Project, Lemma 03SG.** In Situation 0A52 — `k` algebraically closed, `X` separated,
> of finite type and of dimension at most one over `k` — assume `X` is smooth over `k`. Let
> `j : U ⟶ X` be an open immersion, `ℓ` a prime and `F = j_! 𝐙/ℓ𝐙` the extension by zero of the
> constant sheaf on `U_étale` with value an abelian group `E` cyclic of order `ℓ`. Then statements
> (1) -- (8) of Situation 0A52 hold for `F`, in the sense of
> `Stacks.EtaleCohomology.CurveStatements`, at every coefficient universe and every `Ext`
> universe.
>
> A smooth `X` over a field is reduced, so this is Lemma 0A3Q,
> `curveStatements_extensionByZero_constantSheaf_of_prime`.

```lean
theorem curveStatements_extensionByZero_zmod_of_smooth {k : Type u} [Field k] [IsAlgClosed k]
    {X U : Scheme.{u}} (π : X ⟶ Spec (.of k)) [IsSeparated π] [LocallyOfFiniteType π]
    [QuasiCompact π] [Smooth π] (hdim : topologicalKrullDim X ≤ 1) (j : U ⟶ X)
    [IsOpenImmersion j] {ℓ : ℕ} (hℓ : ℓ.Prime) (E : AddCommGrpCat.{max (u + 1) v})
    (hE : Nonempty (E ≃+ ZMod ℓ))
    [HasExt.{w} (Sheaf X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v})] :
    CurveStatements.{u, v, w} π ((extensionByZero.{u, v} j).obj
      ((constantSheaf U.smallEtaleTopology AddCommGrpCat.{max (u + 1) v}).obj E))
```

## Tag 0A3Q, a lemma

[Tag 0A3Q](https://stacks.math.columbia.edu/tag/0A3Q) in the Stacks Project.

**`Stacks.EtaleCohomology.curveStatements_extensionByZero_constantSheaf_of_prime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/ReducedExtensionByZeroStatements.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/ReducedExtensionByZeroStatements.lean#L82).

> **Stacks Project, Lemma 0A3Q.** In Situation 0A52 — `k` algebraically closed, `X` separated,
> of finite type and of dimension at most one over `k` — assume `X` is reduced. Let `j : U → X` be
> an open immersion, `ℓ` a prime, and `F = j_! 𝐙/ℓ𝐙` the extension by zero of the constant sheaf
> on `U_étale` with value any abelian group `E` cyclic of order `ℓ`. Then statements (1) -- (8) of
> Situation 0A52 hold for `F`, in the sense of `Stacks.EtaleCohomology.CurveStatements`, at every
> coefficient universe and every `Ext` universe.
>
> The sheaf `F` is killed by `ℓ`, hence torsion, so this is the reduction theorem
> `curveStatements_of_torsionSheafProperty_max` applied with Lemma 0A5B on smooth curves
> (`curveStatementsConstantOnSmoothCurves_of_prime`).

```lean
theorem curveStatements_extensionByZero_constantSheaf_of_prime {k : Type u} [Field k]
    [IsAlgClosed k] {X U : Scheme.{u}} (π : X ⟶ Spec (.of k)) [IsSeparated π]
    [LocallyOfFiniteType π] [QuasiCompact π] [IsReduced X] (hdim : topologicalKrullDim X ≤ 1)
    (j : U ⟶ X) [IsOpenImmersion j] {ℓ : ℕ} (hℓ : ℓ.Prime) (E : AddCommGrpCat.{max (u + 1) v})
    (hE : Nonempty (E ≃+ ZMod ℓ))
    [HasExt.{w} (Sheaf X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v})] :
    CurveStatements.{u, v, w} π ((extensionByZero.{u, v} j).obj
      ((constantSheaf U.smallEtaleTopology AddCommGrpCat.{max (u + 1) v}).obj E))
```

## Tag 03SD, a lemma

[Tag 03SD](https://stacks.math.columbia.edu/tag/03SD) in the Stacks Project.

**`Stacks.EtaleCohomology.curveStatements_extensionByZero_forget₂_of_isFiniteLocallyConstant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/LocallyConstantCurveStatements.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/LocallyConstantCurveStatements.lean#L63). References: SGA 4 XVI (5.2), “partial”.

> **Stacks Project, Lemma 03SD.** In Situation 0A52 — `k` algebraically closed, `X` separated,
> of finite type and of dimension at most one over `k` — assume `X` is reduced. Let `j : U ⟶ X` be
> an open immersion with `U` connected, `ℓ` a prime and `G` a finite locally constant sheaf of
> `F_ℓ`-vector spaces (`ZMod ℓ`-modules) on `U_étale`. Then statements (1) -- (8) of Situation
> 0A52 (`Stacks.EtaleCohomology.CurveStatements`) hold for the abelian sheaf `F = j_! G`, at every
> coefficient universe and every `Ext` universe.
>
> `j_! G` is killed by `ℓ`, hence torsion, so this is the reduction theorem
> `curveStatements_of_torsionSheafProperty_max` applied with Lemma 0A5B on smooth curves
> (`curveStatementsConstantOnSmoothCurves_of_prime`). The hypotheses that `X` is reduced, that `U`
> is connected and that `G` is finite locally constant are those of the source; the proof does not
> use them.

```lean
theorem curveStatements_extensionByZero_forget₂_of_isFiniteLocallyConstant {k : Type u}
    [Field k] [IsAlgClosed k] {X U : Scheme.{u}} (π : X ⟶ Spec (.of k)) [IsSeparated π]
    [LocallyOfFiniteType π] [QuasiCompact π] [IsReduced X] (hdim : topologicalKrullDim X ≤ 1)
    (j : U ⟶ X) [IsOpenImmersion j] [ConnectedSpace U] {ℓ : ℕ} (hℓ : ℓ.Prime)
    (G : Sheaf U.smallEtaleTopology (ModuleCat.{max (u + 1) v} (ZMod ℓ)))
    [Stacks.ConstantSheaf.IsFiniteLocallyConstant U.smallEtaleTopology G]
    [HasExt.{w} (Sheaf X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v})] :
    CurveStatements.{u, v, w} π ((extensionByZero.{u, v} j).obj
      ((sheafCompose U.smallEtaleTopology
        (forget₂ (ModuleCat.{max (u + 1) v} (ZMod ℓ)) AddCommGrpCat.{max (u + 1) v})).obj G))
```

## Tag 03SC, a theorem

[Tag 03SC](https://stacks.math.columbia.edu/tag/03SC) in the Stacks Project.

**`Stacks.EtaleCohomology.torsionCurveAssertions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/ScalarExtensionColimit.lean, line 257](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/ScalarExtensionColimit.lean#L257). References: SGA 4 IX (5.7), “special case”; SGA 4 X (5.2), “special case”; SGA 4 XIV (1.2), “special case”; SGA 4½ Arcata (3.3.6); SGA 5 VI (2.2.1), “special case”.

> **Stacks Project, Tag 03SC.** Let `k` be an algebraically closed field, let `X` be a separated
> scheme of finite type over `k` of dimension at most one, with structure morphism `f`, and let `F`
> be a torsion abelian sheaf on `X_étale`. Then
> 1. `H^q(X, F) = 0` for `q > 2`;
> 2. `H^q(X, F) = 0` for `q > 1` if `X` is affine;
> 3. `H^q(X, F) = 0` for `q > 1` if `char k = p > 0` and `F` is `p`-power torsion;
> 4. `H^q(X, F)` is finite if `F` is constructible and torsion prime to `char k`;
> 5. `H^q(X, F)` is finite if `X` is proper and `F` is constructible;
> 6. `H^q(X, F) → H^q(X_{k'}, F|_{X_{k'}})` is an isomorphism for every extension `k'/k` of
>    algebraically closed fields if `F` is torsion prime to `char k`;
> 7. the same map is an isomorphism if `X` is proper;
> 8. `H^2(X, F) → H^2(U, F|_U)` is surjective for every open `U ⊂ X`.
>
> These are the fields of `Stacks.EtaleCohomology.TorsionCurveAssertions` (étale cohomology is
> `CategoryTheory.Sheaf.H` on Mathlib's small étale site, at coefficients `AddCommGrpCat.{u + 1}`).
> "Finite type" is `LocallyOfFiniteType f` together with `QuasiCompact f`; the dimension is the
> topological Krull dimension.

```lean
theorem torsionCurveAssertions {k : Type u} [Field k] [IsAlgClosed k] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) [IsSeparated f] [LocallyOfFiniteType f] [QuasiCompact f]
    [HasExt.{u + 1} (Sheaf X.smallEtaleTopology AddCommGrpCat.{u + 1})]
    (hdim : topologicalKrullDim X ≤ 1) (F : Sheaf X.smallEtaleTopology AddCommGrpCat.{u + 1})
    (hF : Stacks.Torsion.torsionSheafProperty X.smallEtaleTopology F) :
    TorsionCurveAssertions f F
```

## Tag 03RT, a theorem

[Tag 03RT](https://stacks.math.columbia.edu/tag/03RT) in the Stacks Project.

**`Stacks.EtaleCohomology.subsingleton_sheafH_of_three_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/NonseparatedCurveVanishing.lean, line 263](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/NonseparatedCurveVanishing.lean#L263). The attribute's comment: “H^q(X, F) = 0 for q ≥ 3”. References: SGA 4 XVII (5.2.8.1), “special case”; SGA 4½ Arcata (3.3.6), “more general”.

> **Stacks Project, Tag 03RT.** Let `X` be a scheme of finite type and of dimension at most one
> over an algebraically closed field `k`, and let `F` be a torsion abelian sheaf on `X_étale`. Then
> `H^q_étale(X, F) = 0` for every `q ≥ 3`.
>
> No separatedness is assumed. The source's "dimension 1" is the case of equality of the bound
> `topologicalKrullDim X ≤ 1`.

```lean
theorem subsingleton_sheafH_of_three_le (q : ℕ) (hq : 3 ≤ q) :
    Subsingleton (Sheaf.H.{w} F q)
```

**`Stacks.EtaleCohomology.subsingleton_sheafH_two_of_isAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/NonseparatedCurveVanishing.lean, line 289](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionSheavesCurves/NonseparatedCurveVanishing.lean#L289). The attribute's comment: “H^2(X, F) = 0 if X is affine”. References: SGA 4½ Arcata (3.3.6), “(ii), degree q=2”.

> **Stacks Project, Tag 03RT.** Let `X` be an affine scheme of finite type and of dimension at
> most one over an algebraically closed field `k`, and let `F` be a torsion abelian sheaf on
> `X_étale`. Then `H^2_étale(X, F) = 0`.
>
> An affine scheme is separated over `k`, so this is Theorem 03SC (2), Tag 0A54.

```lean
theorem subsingleton_sheafH_two_of_isAffine [IsAffine X] : Subsingleton (Sheaf.H.{w} F 2)
```

## Tag 0A5E, a lemma

[Tag 0A5E](https://stacks.math.columbia.edu/tag/0A5E) in the Stacks Project.

Declarations registered for the tag:

- [`Stacks.EtaleCohomology.etaleCohomologyBaseChangeMap_bijective_of_isSepClosed`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/ProperBaseChangeTheoremUnconditional.lean#L80), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/ProperBaseChangeStacksTags.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/ProperBaseChangeStacksTags.lean#L51) (StacksFrontier).

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.83, Tag 03SB](https://stacks.math.columbia.edu/tag/03SB)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
