---
declaration: section
origin: cited
lean: AlgebraicGeometry.RingedSite.IsPseudoCoherentComplexFrom, AlgebraicGeometry.RingedSite.IsPseudoCoherentComplex, AlgebraicGeometry.RingedSite.IsPseudoCoherentFrom, AlgebraicGeometry.RingedSite.IsPseudoCoherent, AlgebraicGeometry.RingedSite.isPseudoCoherent_derivedRestriction_general, AlgebraicGeometry.RingedSite.isPseudoCoherentFrom_of_locally, AlgebraicGeometry.RingedSite.isPseudoCoherentComplexFrom_of_iso, AlgebraicGeometry.RingedSite.isPseudoCoherentFrom_derivedRestriction
statement: formalized
proof: formalized
---

# 21.45 Pseudo-coherent modules

Section 21.45 of the Stacks Project, [Tag 08FS](https://stacks.math.columbia.edu/tag/08FS). 7 tags here are carried by 29 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08FT, a definition

[Tag 08FT](https://stacks.math.columbia.edu/tag/08FT) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.IsPseudoCoherentComplexFrom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/PseudoCoherentObjects.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/PseudoCoherentObjects.lean#L79). The attribute's comment: “part (1)”.

> **Stacks 08FT, part (1).** A complex `E` of `O`-modules is `m`-*pseudo-coherent* if every
> object `U` of the site admits a covering `{V → U}` over each member of which there are a
> strictly perfect complex `P` of `O|_V`-modules and a map `P ⟶ E|_V` inducing isomorphisms on
> cohomology in every degree `> m` and an epimorphism on cohomology in degree `m`.

```lean
noncomputable def IsPseudoCoherentComplexFrom
    (E : CochainComplex (SheafOfModules.{m} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) ℤ)
    (m : ℤ) : Prop
```

**`AlgebraicGeometry.RingedSite.IsPseudoCoherentComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/PseudoCoherentObjects.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/PseudoCoherentObjects.lean#L94). The attribute's comment: “part (2)”.

> **Stacks 08FT, part (2).** A complex of `O`-modules is *pseudo-coherent* if it is
> `m`-pseudo-coherent for every integer `m`.

```lean
noncomputable def IsPseudoCoherentComplex
    (E : CochainComplex (SheafOfModules.{m} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) ℤ) :
    Prop
```

**`AlgebraicGeometry.RingedSite.IsPseudoCoherentFrom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/PseudoCoherentObjects.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/PseudoCoherentObjects.lean#L105). The attribute's comment: “part (3), m-pseudo-coherent”.

> **Stacks 08FT, part (3), first clause.** An object of `D(O)` is `m`-*pseudo-coherent* if
> it is isomorphic to the image of an `m`-pseudo-coherent complex.

```lean
noncomputable def IsPseudoCoherentFrom
    [HasDerivedCategory.{d} (SheafOfModules.{m} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))]
    (E : DerivedCategory (SheafOfModules.{m} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (m : ℤ) : Prop
```

**`AlgebraicGeometry.RingedSite.IsPseudoCoherent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/PseudoCoherentObjects.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/PseudoCoherentObjects.lean#L115). The attribute's comment: “part (3), pseudo-coherent”.

> **Stacks 08FT, part (3), second clause.** An object of `D(O)` is *pseudo-coherent* if it
> is isomorphic to the image of a pseudo-coherent complex.

```lean
noncomputable def IsPseudoCoherent
    [HasDerivedCategory.{d} (SheafOfModules.{m} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))]
    (E : DerivedCategory (SheafOfModules.{m} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) :
    Prop
```

## Tag 08FU, a lemma

[Tag 08FU](https://stacks.math.columbia.edu/tag/08FU) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.isPseudoCoherent_derivedRestriction_general`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherentSites/RestrictionGeneral.lean, line 276](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PseudoCoherentSites/RestrictionGeneral.lean#L276). The attribute's comment: “part (3), all degrees, restriction to a slice”.

> **Stacks 08FU, part (3), all degrees at once, in the direction which restricts
> pseudo-coherence to a slice**, at independent universes. If an object `E` of `D(O)` is
> pseudo-coherent, then its restriction to the localized ringed site over any object `V` of `C` is
> pseudo-coherent there.
>
> This is not the fixed-degree statement read in each degree: the all-degrees clause of Stacks
> 08FT (3) asks for **one** complex which is `m`-pseudo-coherent for every `m`, and a family of
> degreewise statements does not provide it.  What the proof restricts is the single complex that
> pseudo-coherence of `E` already provides, and it stays `m`-pseudo-coherent for every `m` by
> `AlgebraicGeometry.RingedSite.isPseudoCoherentComplexFrom_restrictComplex_general`, which is
> itself stated at one complex and an arbitrary degree; so no quantifier swap is needed.

```lean
theorem isPseudoCoherent_derivedRestriction_general
    (E : DerivedCategory (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (hE : X.IsPseudoCoherent E) (V : X.C) :
    (X.over V).IsPseudoCoherent
      ((SheafOfModules.overFunctor.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)
        V).mapDerivedCategory.obj E)
```

**`AlgebraicGeometry.RingedSite.isPseudoCoherentFrom_of_locally`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/LocalNature.lean, line 442](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/LocalNature.lean#L442). The attribute's comment: “part (3)”.

> **Stacks 08FU, part (3).** Let `(C, O)` be a ringed site and let `E` be an object of
> `D(O)`. If every object `U` of `C` admits a covering `{V → U}` over each member of which the
> restriction of `E` is `m`-pseudo-coherent, then `E` is `m`-pseudo-coherent.

```lean
theorem isPseudoCoherentFrom_of_locally
    (E : DerivedCategory (SheafOfModules.{0} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) (m : ℤ)
    (h : ∀ U : X.C, ∃ S : Presieve U, Sieve.generate S ∈ X.J U ∧
      ∀ ⦃V : X.C⦄ (f : V ⟶ U), S f →
        (X.over V).IsPseudoCoherentFrom
          ((SheafOfModules.overFunctor.{0}
            (Stacks.SheafOfModules.Tensor.ringSheaf X.O) V).mapDerivedCategory.obj E) m) :
    X.IsPseudoCoherentFrom E m
```

**`AlgebraicGeometry.RingedSite.isPseudoCoherentComplexFrom_of_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/Representatives.lean, line 504](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/Representatives.lean#L504). The attribute's comment: “part (2)”. References: SGA 6 I (2.2), “a)”.

> **Stacks 08FU, part (2).** Let `(C, O)` be a ringed site and let `E` be an object of `D(O)`
> which is `m`-pseudo-coherent. Then every complex of `O`-modules representing `E` is
> `m`-pseudo-coherent.

```lean
theorem isPseudoCoherentComplexFrom_of_iso
    [HasDerivedCategory.{d} (SheafOfModules.{0} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))]
    (E : DerivedCategory (SheafOfModules.{0} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) (m : ℤ)
    (hE : X.IsPseudoCoherentFrom E m)
    (K : CochainComplex (SheafOfModules.{0} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) ℤ)
    (e : DerivedCategory.Q.obj K ≅ E) :
    X.IsPseudoCoherentComplexFrom K m
```

**`AlgebraicGeometry.RingedSite.isPseudoCoherentFrom_derivedRestriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/Restriction.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/Restriction.lean#L203). The attribute's comment: “part (3), restriction to a slice”.

> **Stacks 08FU, part (3), in the direction which restricts pseudo-coherence to a slice.** If
> an object `E` of `D(O)` is `m`-pseudo-coherent, then its restriction to the localized ringed
> site over any object `V` of `C` is `m`-pseudo-coherent there.

```lean
theorem isPseudoCoherentFrom_derivedRestriction
    (E : DerivedCategory (SheafOfModules.{0} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) (m : ℤ)
    (hE : X.IsPseudoCoherentFrom E m) (V : X.C) :
    (X.over V).IsPseudoCoherentFrom
      ((SheafOfModules.overFunctor.{0} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)
        V).mapDerivedCategory.obj E) m
```

**`AlgebraicGeometry.RingedSite.isPseudoCoherentFrom_of_covering_of_terminal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/TerminalCovering.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/TerminalCovering.lean#L76). The attribute's comment: “part (1)”.

> Let `(C, O)` be a ringed site, let `E` be an object of `D(O)` and let `T` be a final object of
> `C`. If a covering `{V → T}` of `T` carries over each of its members a strictly perfect complex `P`
> of `O|_V`-modules and a morphism `P ⟶ E|_V` of `D(O|_V)` which is an isomorphism on cohomology in
> every degree `> m` and an epimorphism on cohomology in degree `m`, then `E` is `m`-pseudo-coherent.

```lean
theorem isPseudoCoherentFrom_of_covering_of_terminal
    (T : X.C) (hT : IsTerminal T)
    (E : DerivedCategory (SheafOfModules.{0} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) (m : ℤ)
    (S : Presieve T) (hS : Sieve.generate S ∈ X.J T)
    (hdata : ∀ ⦃V : X.C⦄ (f : V ⟶ T), S f →
      ∃ P : CochainComplex
          (SheafOfModules.{0} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).over V)) ℤ,
        IsStrictlyPerfect ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).over V) P ∧
        ∃ α : DerivedCategory.Q.obj P ⟶
            (SheafOfModules.overFunctor.{0}
              (Stacks.SheafOfModules.Tensor.ringSheaf X.O) V).mapDerivedCategory.obj E,
          (∀ j : ℤ, m < j → IsIso ((DerivedCategory.homologyFunctor _ j).map α)) ∧
          Epi ((DerivedCategory.homologyFunctor _ m).map α)) :
    X.IsPseudoCoherentFrom E m
```

## Tag 08H4, a lemma

[Tag 08H4](https://stacks.math.columbia.edu/tag/08H4) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.Hom.isPseudoCoherentFrom_derivedPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/DerivedPullbackAlongRingedTopoi.lean, line 321](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/DerivedPullbackAlongRingedTopoi.lean#L321).

> **Stacks 08H4.** The derived pullback along a morphism of ringed sites of an
> `m`-pseudo-coherent object of `D(O')` is `m`-pseudo-coherent.
>
> Stacks 08H2 makes the objects `u(W)` cover the final object of `Sh(C)`, and
> `CategoryTheory.GrothendieckTopology.coversTop_obj_subtype` refines that covering to the `u(W)`
> over which `K` carries a strictly perfect approximation. Over such an object the pullback of the
> approximation is a derived strictly perfect approximation of `(Lf^* E)|_{u(W)}`
> (`hasDerivedApproximation_image`), and it descends along any arrow into `u(W)` by exactness of
> restriction (`hasDerivedApproximation_of_hom`), which is what the arrows of that covering
> supply.

```lean
theorem Hom.isPseudoCoherentFrom_derivedPullback
    (E : DerivedCategory
      (SheafOfModules.{0} (Stacks.SheafOfModules.Tensor.ringSheaf (ringedTopos Y).O)))
    (m : ℤ)
    (hE : Y.IsPseudoCoherentFrom E m) :
    X.IsPseudoCoherentFrom ((derivedPullback f.toRingedToposSiteHom).obj E) m
```

## Tag 08FV, a lemma

[Tag 08FV](https://stacks.math.columbia.edu/tag/08FV) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.isPseudoCoherentFrom_of_distinguished_one_general`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/DistinguishedTriangles.lean, line 749](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/DistinguishedTriangles.lean#L749). The attribute's comment: “part (1), general universes”.

> **Stacks 08FV, part (1)**, with the site, its morphisms and the sections of the structure
> sheaf at independent universes. Let `(C, O)` be a ringed site and let
> `K ⟶ L ⟶ M ⟶ K[1]` be a distinguished triangle of `D(O)`. If `K` is `(m + 1)`-pseudo-coherent
> and `L` is `m`-pseudo-coherent, then `M` is `m`-pseudo-coherent.

```lean
theorem isPseudoCoherentFrom_of_distinguished_one_general (m : ℤ)
    (T : Triangle
      (DerivedCategory (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))))
    (hT : T ∈ distinguishedTriangles)
    (hK : X.IsPseudoCoherentFrom T.obj₁ (m + 1))
    (hL : X.IsPseudoCoherentFrom T.obj₂ m) :
    X.IsPseudoCoherentFrom T.obj₃ m
```

**`AlgebraicGeometry.RingedSite.isPseudoCoherentFrom_of_distinguished_two_general`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/DistinguishedTriangles.lean, line 773](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/DistinguishedTriangles.lean#L773). The attribute's comment: “part (2), general universes”.

> **Stacks 08FV, part (2)**, at independent site, morphism and module universes. If the
> first and third vertices of a distinguished triangle of
> `D(O)` are `m`-pseudo-coherent, so is the second.
>
> Apply part (1) to the inverse rotation `M[-1] ⟶ K ⟶ L ⟶ M`.

```lean
theorem isPseudoCoherentFrom_of_distinguished_two_general (m : ℤ)
    (T : Triangle
      (DerivedCategory (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))))
    (hT : T ∈ distinguishedTriangles)
    (hK : X.IsPseudoCoherentFrom T.obj₁ m)
    (hM : X.IsPseudoCoherentFrom T.obj₃ m) :
    X.IsPseudoCoherentFrom T.obj₂ m
```

**`AlgebraicGeometry.RingedSite.isPseudoCoherentFrom_of_distinguished_three_general`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/DistinguishedTriangles.lean, line 792](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/DistinguishedTriangles.lean#L792). The attribute's comment: “part (3), general universes”.

> **Stacks 08FV, part (3)**, at independent site, morphism and module universes. If the
> second vertex of a distinguished triangle of `D(O)` is
> `(m + 1)`-pseudo-coherent and the third is `m`-pseudo-coherent, then the first is
> `(m + 1)`-pseudo-coherent.
>
> Apply part (1) to the rotation `L ⟶ M ⟶ K[1] ⟶ L[1]` and shift back.

```lean
theorem isPseudoCoherentFrom_of_distinguished_three_general (m : ℤ)
    (T : Triangle
      (DerivedCategory (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))))
    (hT : T ∈ distinguishedTriangles)
    (hL : X.IsPseudoCoherentFrom T.obj₂ (m + 1))
    (hM : X.IsPseudoCoherentFrom T.obj₃ m) :
    X.IsPseudoCoherentFrom T.obj₁ (m + 1)
```

**`AlgebraicGeometry.RingedSite.isPseudoCoherentFrom_of_distinguished_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/DistinguishedTriangles.lean, line 819](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/DistinguishedTriangles.lean#L819). The attribute's comment: “part (1)”.

> **Stacks 08FV, part (1).** Let `(C, O)` be a ringed site and let
> `K ⟶ L ⟶ M ⟶ K[1]` be a distinguished triangle of `D(O)`. If `K` is `(m + 1)`-pseudo-coherent
> and `L` is `m`-pseudo-coherent, then `M` is `m`-pseudo-coherent.

```lean
theorem isPseudoCoherentFrom_of_distinguished_one (m : ℤ)
    (T : Triangle
      (DerivedCategory (SheafOfModules.{0} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))))
    (hT : T ∈ distinguishedTriangles)
    (hK : X.IsPseudoCoherentFrom T.obj₁ (m + 1))
    (hL : X.IsPseudoCoherentFrom T.obj₂ m) :
    X.IsPseudoCoherentFrom T.obj₃ m
```

**`AlgebraicGeometry.RingedSite.isPseudoCoherentFrom_of_distinguished_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/DistinguishedTriangles.lean, line 833](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/DistinguishedTriangles.lean#L833). The attribute's comment: “part (2)”. References: SGA 6 I (2.5), “b)”.

> **Stacks 08FV, part (2).** If the first and third vertices of a distinguished triangle of
> `D(O)` are `m`-pseudo-coherent, so is the second.
>
> Apply part (1) to the inverse rotation `M[-1] ⟶ K ⟶ L ⟶ M`.

```lean
theorem isPseudoCoherentFrom_of_distinguished_two (m : ℤ)
    (T : Triangle
      (DerivedCategory (SheafOfModules.{0} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))))
    (hT : T ∈ distinguishedTriangles)
    (hK : X.IsPseudoCoherentFrom T.obj₁ m)
    (hM : X.IsPseudoCoherentFrom T.obj₃ m) :
    X.IsPseudoCoherentFrom T.obj₂ m
```

**`AlgebraicGeometry.RingedSite.isPseudoCoherentFrom_of_distinguished_three`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/DistinguishedTriangles.lean, line 848](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/DistinguishedTriangles.lean#L848). The attribute's comment: “part (3)”.

> **Stacks 08FV, part (3).** If the second vertex of a distinguished triangle of `D(O)` is
> `(m + 1)`-pseudo-coherent and the third is `m`-pseudo-coherent, then the first is
> `(m + 1)`-pseudo-coherent.
>
> Apply part (1) to the rotation `L ⟶ M ⟶ K[1] ⟶ L[1]` and shift back.

```lean
theorem isPseudoCoherentFrom_of_distinguished_three (m : ℤ)
    (T : Triangle
      (DerivedCategory (SheafOfModules.{0} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))))
    (hT : T ∈ distinguishedTriangles)
    (hL : X.IsPseudoCoherentFrom T.obj₂ (m + 1))
    (hM : X.IsPseudoCoherentFrom T.obj₃ m) :
    X.IsPseudoCoherentFrom T.obj₁ (m + 1)
```

## Tag 09J9, a lemma

[Tag 09J9](https://stacks.math.columbia.edu/tag/09J9) in the Stacks Project.

**`Stacks.SheafOfModules.DerivedTensorProduct.isPseudoCoherentFrom_derivedTensorProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/DerivedTensorProduct.lean, line 734](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/DerivedTensorProduct.lean#L734). The attribute's comment: “part (1)”.

> **Stacks 09J9, part (1).** Let `(C, O)` be a ringed site and let `K`, `L` be objects of
> `D(O)`. If `K` is `n`-pseudo-coherent with `H^i(K) = 0` for `i > a`, and `L` is
> `m`-pseudo-coherent with `H^j(L) = 0` for `j > b`, then `K ⊗^{𝐋}_O L` is `t`-pseudo-coherent
> for `t = max (m + a) (n + b)`. Here `⊗^{𝐋}_O` is the derived tensor product of Stacks 06YU,
> `Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor`.

```lean
theorem isPseudoCoherentFrom_derivedTensorProduct
    (K L : DerivedCategory (_root_.SheafOfModules.{0} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (n m a b : ℤ)
    (hK : X.IsPseudoCoherentFrom K n)
    (hKa : ∀ i : ℤ, a < i →
      IsZero ((DerivedCategory.homologyFunctor
        (_root_.SheafOfModules.{0} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) i).obj K))
    (hL : X.IsPseudoCoherentFrom L m)
    (hLb : ∀ j : ℤ, b < j →
      IsZero ((DerivedCategory.homologyFunctor
        (_root_.SheafOfModules.{0} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) j).obj L)) :
    X.IsPseudoCoherentFrom
      ((Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor X.O |>.obj K).obj L)
      (max (m + a) (n + b))
```

**`Stacks.SheafOfModules.DerivedTensorProduct.isPseudoCoherent_derivedTensorProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/DerivedTensorProduct.lean, line 755](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/DerivedTensorProduct.lean#L755). The attribute's comment: “part (2)”.

> **Stacks 09J9, part (2).** Let `(C, O)` be a ringed site. If `K` and `L` are pseudo-coherent
> objects of `D(O)`, then `K ⊗^{𝐋}_O L` is pseudo-coherent. Here `⊗^{𝐋}_O` is the derived tensor
> product of Stacks 06YU, `Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor`.

```lean
theorem isPseudoCoherent_derivedTensorProduct
    (K L : DerivedCategory (_root_.SheafOfModules.{0} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (hK : X.IsPseudoCoherent K) (hL : X.IsPseudoCoherent L) :
    X.IsPseudoCoherent
      ((Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor X.O |>.obj K).obj L)
```

## Tag 08FW, a lemma

[Tag 08FW](https://stacks.math.columbia.edu/tag/08FW) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.isPseudoCoherentFrom_left_of_biprod_general`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/Summands.lean, line 375](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/Summands.lean#L375). The attribute's comment: “m-pseudo-coherent, first summand, general universes”.

> **Stacks 08FW**, at independent site, morphism and module universes. Let `(C, O)` be a
> ringed site and `n : ℤ`. If `K ⊞ L` is `n`-pseudo-coherent in `D(O)`, then so is `K`.
>
> Over an object `V` of the site carrying a strictly perfect approximation of `(K ⊞ L)|_V`, the
> cohomology of `K|_V` and of `L|_V` vanishes above the support of the approximation, so both are
> `N`-pseudo-coherent for that `N`; descending through the split distinguished triangles makes
> `K|_V` and `L|_V` `n`-pseudo-coherent, and Stacks 08FU (3) globalizes that.

```lean
theorem isPseudoCoherentFrom_left_of_biprod_general
    (K L : DerivedCategory (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (n : ℤ) (h : X.IsPseudoCoherentFrom (K ⊞ L) n) : X.IsPseudoCoherentFrom K n
```

**`AlgebraicGeometry.RingedSite.isPseudoCoherentFrom_right_of_biprod_general`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/Summands.lean, line 455](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/Summands.lean#L455). The attribute's comment: “m-pseudo-coherent, second summand, general universes”.

> **Stacks 08FW**, at independent site, morphism and module universes. If `K ⊞ L` is
> `n`-pseudo-coherent in `D(O)`, then so is `L`: exchange the two summands.

```lean
theorem isPseudoCoherentFrom_right_of_biprod_general
    (K L : DerivedCategory (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (n : ℤ) (h : X.IsPseudoCoherentFrom (K ⊞ L) n) : X.IsPseudoCoherentFrom L n
```

**`AlgebraicGeometry.RingedSite.isPseudoCoherent_left_of_biprod_general`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/Summands.lean, line 464](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/Summands.lean#L464). The attribute's comment: “pseudo-coherent, first summand, general universes”.

> **Stacks 08FW**, at independent site, morphism and module universes. If `K ⊞ L` is
> pseudo-coherent in `D(O)`, then so is `K`.

```lean
theorem isPseudoCoherent_left_of_biprod_general
    (K L : DerivedCategory (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (h : X.IsPseudoCoherent (K ⊞ L)) : X.IsPseudoCoherent K
```

**`AlgebraicGeometry.RingedSite.isPseudoCoherent_right_of_biprod_general`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/Summands.lean, line 474](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/Summands.lean#L474). The attribute's comment: “pseudo-coherent, second summand, general universes”.

> **Stacks 08FW**, at independent site, morphism and module universes. If `K ⊞ L` is
> pseudo-coherent in `D(O)`, then so is `L`.

```lean
theorem isPseudoCoherent_right_of_biprod_general
    (K L : DerivedCategory (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (h : X.IsPseudoCoherent (K ⊞ L)) : X.IsPseudoCoherent L
```

**`AlgebraicGeometry.RingedSite.isPseudoCoherentFrom_left_of_biprod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/Summands.lean, line 544](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/Summands.lean#L544). The attribute's comment: “m-pseudo-coherent, first summand”. References: SGA 6 I (2.12), “n-pc: sum ⇒ F'”.

> **Stacks 08FW.** Let `(C, O)` be a ringed site and `n : ℤ`. If `K ⊞ L` is
> `n`-pseudo-coherent in `D(O)`, then so is `K`.
>
> Over an object `V` of the site carrying a strictly perfect approximation of `(K ⊞ L)|_V`, the
> cohomology of `K|_V` and of `L|_V` vanishes above the support of the approximation, so both are
> `N`-pseudo-coherent for that `N`; descending through the split distinguished triangles makes
> `K|_V` and `L|_V` `n`-pseudo-coherent, and Stacks 08FU (3) globalizes that.

```lean
theorem isPseudoCoherentFrom_left_of_biprod
    (K L : DerivedCategory (SheafOfModules.{0} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (n : ℤ) (h : X.IsPseudoCoherentFrom (K ⊞ L) n) : X.IsPseudoCoherentFrom K n
```

**`AlgebraicGeometry.RingedSite.isPseudoCoherentFrom_right_of_biprod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/Summands.lean, line 552](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/Summands.lean#L552). The attribute's comment: “m-pseudo-coherent, second summand”. References: SGA 6 I (2.12), “n-pc: sum ⇒ F''”.

> **Stacks 08FW.** If `K ⊞ L` is `n`-pseudo-coherent in `D(O)`, then so is `L`: exchange the
> two summands and apply the previous statement.

```lean
theorem isPseudoCoherentFrom_right_of_biprod
    (K L : DerivedCategory (SheafOfModules.{0} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (n : ℤ) (h : X.IsPseudoCoherentFrom (K ⊞ L) n) : X.IsPseudoCoherentFrom L n
```

**`AlgebraicGeometry.RingedSite.isPseudoCoherent_left_of_biprod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/Summands.lean, line 560](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/Summands.lean#L560). The attribute's comment: “pseudo-coherent, first summand”. References: SGA 6 I (2.12), “pc: sum ⇒ F'”.

> **Stacks 08FW.** If `K ⊞ L` is pseudo-coherent in `D(O)`, then so is `K`.

```lean
theorem isPseudoCoherent_left_of_biprod
    (K L : DerivedCategory (SheafOfModules.{0} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (h : X.IsPseudoCoherent (K ⊞ L)) : X.IsPseudoCoherent K
```

**`AlgebraicGeometry.RingedSite.isPseudoCoherent_right_of_biprod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/Summands.lean, line 569](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/PseudoCoherent/Summands.lean#L569). The attribute's comment: “pseudo-coherent, second summand”.

> **Stacks 08FW.** If `K ⊞ L` is pseudo-coherent in `D(O)`, then so is `L`.

```lean
theorem isPseudoCoherent_right_of_biprod
    (K L : DerivedCategory (SheafOfModules.{0} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (h : X.IsPseudoCoherent (K ⊞ L)) : X.IsPseudoCoherent L
```

## Tag 08FX, a lemma

[Tag 08FX](https://stacks.math.columbia.edu/tag/08FX) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.isFiniteType_homology_general`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherentSites/TopCohomologyFinitenessGeneral.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PseudoCoherentSites/TopCohomologyFinitenessGeneral.lean#L55). The attribute's comment: “finite_type_top_cohomology, at independent universes”.

> The degree-`m` cohomology of an `m`-pseudo-coherent object of the derived category of modules
> over a ringed site `RingedSite.{u, v, w}`, whose cohomology vanishes above `m`, is of finite
> type.

```lean
theorem isFiniteType_homology_general (X : RingedSite.{u, v, w})
    [X.J.HasSheafCompose (forget₂ CommRingCat.{w} RingCat.{w})]
    [HasSheafify X.J AddCommGrpCat.{w}]
    [X.J.WEqualsLocallyBijective AddCommGrpCat.{w}]
    [∀ U : X.C, HasSheafify (X.J.over U) AddCommGrpCat.{w}]
    [∀ U : X.C, (X.J.over U).WEqualsLocallyBijective AddCommGrpCat.{w}]
    [∀ U : X.C, (X.J.over U).HasSheafCompose (forget₂ RingCat.{w} AddCommGrpCat.{w})]
    [HasDerivedCategory.{d} (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))]
    (K : DerivedCategory (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) (m : ℤ)
    (hK : X.IsPseudoCoherentFrom K m)
    (hvanish : ∀ i : ℤ, m < i →
      IsZero ((DerivedCategory.homologyFunctor
        (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) i).obj K)) :
    ((DerivedCategory.homologyFunctor
      (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) m).obj K).IsFiniteType
```

**`AlgebraicGeometry.RingedSite.isFiniteType_homology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriekAndPerfection/TopCohomologyFiniteness.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriekAndPerfection/TopCohomologyFiniteness.lean#L76). The attribute's comment: “finite_type_top_cohomology”.

> **Stacks 08FX**, finite type of the top cohomology. The degree-`m` cohomology of an
> `m`-pseudo-coherent object of the derived category whose higher cohomology vanishes is of
> finite type.

```lean
theorem isFiniteType_homology (X : RingedSite.{u, u, 0})
    [X.J.HasSheafCompose (forget₂ CommRingCat.{0} RingCat.{0})]
    [HasSheafify X.J AddCommGrpCat.{0}]
    [X.J.WEqualsLocallyBijective AddCommGrpCat.{0}]
    [∀ U : X.C, HasSheafify (X.J.over U) AddCommGrpCat.{0}]
    [∀ U : X.C, (X.J.over U).WEqualsLocallyBijective AddCommGrpCat.{0}]
    [∀ U : X.C, (X.J.over U).HasSheafCompose (forget₂ RingCat.{0} AddCommGrpCat.{0})]
    [HasDerivedCategory.{d} (SheafOfModules.{0} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))]
    (K : DerivedCategory (SheafOfModules.{0} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) (m : ℤ)
    (hK : X.IsPseudoCoherentFrom K m)
    (hvanish : ∀ i : ℤ, m < i →
      IsZero ((DerivedCategory.homologyFunctor
        (SheafOfModules.{0} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) i).obj K)) :
    ((DerivedCategory.homologyFunctor
      (SheafOfModules.{0} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) m).obj K).IsFiniteType
```

**`AlgebraicGeometry.RingedSite.isFinitePresentation_homology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriekAndPerfection/TopCohomologyFiniteness.lean, line 214](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriekAndPerfection/TopCohomologyFiniteness.lean#L214). The attribute's comment: “finite_presentation_top_cohomology”.

> **Stacks 08FX**, finite presentation of the top cohomology. The degree-`m + 1` cohomology
> of an `m`-pseudo-coherent object of the derived category whose cohomology vanishes above
> `m + 1` is finitely presented.

```lean
theorem isFinitePresentation_homology (X : RingedSite.{u, u, 0})
    [X.J.HasSheafCompose (forget₂ CommRingCat.{0} RingCat.{0})]
    [HasSheafify X.J AddCommGrpCat.{0}]
    [X.J.WEqualsLocallyBijective AddCommGrpCat.{0}]
    [∀ U : X.C, HasSheafify (X.J.over U) AddCommGrpCat.{0}]
    [∀ U : X.C, (X.J.over U).WEqualsLocallyBijective AddCommGrpCat.{0}]
    [∀ U : X.C, (X.J.over U).HasSheafCompose (forget₂ RingCat.{0} AddCommGrpCat.{0})]
    [HasDerivedCategory.{d} (SheafOfModules.{0} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))]
    (K : DerivedCategory (SheafOfModules.{0} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) (m : ℤ)
    (hK : X.IsPseudoCoherentFrom K m)
    (hvanish : ∀ i : ℤ, m + 1 < i →
      IsZero ((DerivedCategory.homologyFunctor
        (SheafOfModules.{0} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) i).obj K)) :
    ((DerivedCategory.homologyFunctor
      (SheafOfModules.{0} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) (m + 1)).obj
        K).IsFinitePresentation
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.45, Tag 08FS](https://stacks.math.columbia.edu/tag/08FS)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
