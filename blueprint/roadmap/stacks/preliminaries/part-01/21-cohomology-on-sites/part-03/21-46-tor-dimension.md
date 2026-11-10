---
declaration: section
origin: cited
lean: Stacks.SheafOfModules.DerivedTensorProduct.HasTorAmplitude, Stacks.SheafOfModules.DerivedTensorProduct.HasFiniteTorDimension, Stacks.SheafOfModules.DerivedTensorProduct.HasTorDimensionLE, Stacks.SheafOfModules.DerivedTensorProduct.hasTorAmplitude_of_coversTop, Stacks.SheafOfModules.DerivedTensorProduct.hasFiniteTorDimension_of_locallyHasFiniteTorDimension, Stacks.SheafOfModules.DerivedTensorProduct.LocallyHasFiniteTorDimension, Stacks.SheafOfModules.DerivedTensorProduct.isFlat_cokernel_of_hasTorAmplitude, Stacks.SheafOfModules.DerivedTensorProduct.isFlat_cokernel_of_hasTorAmplitude_canonical
statement: formalized
proof: formalized
---

# 21.46 Tor dimension

Section 21.46 of the Stacks Project, [Tag 08FY](https://stacks.math.columbia.edu/tag/08FY). 10 tags here are carried by 22 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08FZ, a definition

[Tag 08FZ](https://stacks.math.columbia.edu/tag/08FZ) in the Stacks Project.

**`Stacks.SheafOfModules.DerivedTensorProduct.HasTorAmplitude`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/TorAmplitude/Defs.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/TorAmplitude/Defs.lean#L88). The attribute's comment: “tor amplitude in an interval”. References: SGA 6 I (5.2), “Tor-amp(F) ⊂ [m,n]”; SGA 4½ Rapport (4.5), “sheaf tor-dimension ≤ r”; SGA 4 XVII (4.1.9), “(i)”.

> **Stacks 08FZ (1).** An object `E` of `D(O)` has *Tor amplitude in `[a, b]`* for the derived
> tensor product `T` if, for every sheaf of `O`-modules `F`, the derived tensor product of `E`
> with `F` placed in degree zero has vanishing cohomology in every degree outside `[a, b]`.

```lean
noncomputable def HasTorAmplitude
    (T : DerivedTensorProduct.{u, v, w, d} X) (E : RingedSite.DerivedModules.{u, v, w, d} X)
    (a b : ℤ) : Prop
```

**`Stacks.SheafOfModules.DerivedTensorProduct.HasFiniteTorDimension`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/TorAmplitude/Defs.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/TorAmplitude/Defs.lean#L131). The attribute's comment: “finite tor dimension”. References: SGA 6 I (5.2), “finite flat amplitude”; SGA 4½ Rapport (4.5), “sheaf case, finite”.

> **Stacks 08FZ (2).** An object `E` of `D(O)` has *finite Tor dimension* for the derived
> tensor product `T` if it has Tor amplitude in some interval.

```lean
noncomputable def HasFiniteTorDimension (T : DerivedTensorProduct.{u, v, w, d} X)
    (E : RingedSite.DerivedModules.{u, v, w, d} X) : Prop
```

**`Stacks.SheafOfModules.DerivedTensorProduct.HasTorDimensionLE`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/TorAmplitude/Defs.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/TorAmplitude/Defs.lean#L149). The attribute's comment: “tor dimension of a module”. References: SGA 4½ Rapport (4.5), “sheaf module case”; SGA 4 XVII (4.1.9), “module case”.

> **Stacks 08FZ, the last sentence.** A sheaf of `O`-modules `F` has *Tor dimension at most
> `n`* when `F[0]`, viewed as an object of `D(O)`, has Tor amplitude in `[-n, 0]`.

```lean
noncomputable def HasTorDimensionLE (T : DerivedTensorProduct.{u, v, w, d} X)
    (F : RingedSite.Modules.{u, v, w} X) (n : ℤ) : Prop
```

**`Stacks.SheafOfModules.DerivedTensorProduct.hasTorAmplitude_of_coversTop`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/TorAmplitude/IntervalDescent.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/TorAmplitude/IntervalDescent.lean#L107). The attribute's comment: “the descent of tor amplitude in a fixed interval from a covering family to the object covered”.

> **Tor amplitude in a fixed interval descends along a covering family.** Let `V : ι → C` be a
> family of objects covering the final object of the site. If the restriction of `E` to the
> localized ringed site at each `V i` has Tor amplitude in `[a, b]`, measured against the derived
> tensor product `T' (V i)` on that slice, then `E` has Tor amplitude in `[a, b]` for `T`.

```lean
theorem hasTorAmplitude_of_coversTop
    (T : DerivedTensorProduct.{c, u, u, d} X)
    (T' : ∀ U : X.C, DerivedTensorProduct.{max c u, u, u, d} (X.over U))
    {ι : Type t} {V : ι → X.C} (hV : X.J.CoversTop V)
    (E : RingedSite.DerivedModules.{c, u, u, d} X) (a b : ℤ)
    (hamp : ∀ i, HasTorAmplitude (T' (V i))
      ((RingedSite.derivedRestriction.{c, u, u, d} X (V i)).obj E) a b) :
    HasTorAmplitude T E a b
```

**`Stacks.SheafOfModules.DerivedTensorProduct.hasFiniteTorDimension_of_locallyHasFiniteTorDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/TorAmplitude/IntervalDescent.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/TorAmplitude/IntervalDescent.lean#L127). The attribute's comment: “on a quasi-compact site, locally finite tor dimension is finite tor dimension”.

> **On a quasi-compact site, locally finite Tor dimension is finite Tor dimension.** If the
> site has a terminal object which is quasi-compact in the sense of Stacks 090H and `E` locally has
> finite Tor dimension, then `E` has finite Tor dimension.

```lean
theorem hasFiniteTorDimension_of_locallyHasFiniteTorDimension
    (T : DerivedTensorProduct.{c, u, u, d} X)
    (T' : ∀ U : X.C, DerivedTensorProduct.{max c u, u, u, d} (X.over U))
    (E : RingedSite.DerivedModules.{c, u, u, d} X)
    (hE : LocallyHasFiniteTorDimension T' E)
    (U : X.C) (hU : IsTerminal U) (hqc : X.J.IsQuasiCompactObject U) :
    HasFiniteTorDimension T E
```

**`Stacks.SheafOfModules.DerivedTensorProduct.LocallyHasFiniteTorDimension`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/TorAmplitude/LocallyFiniteTorDimension.lean, line 189](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/TorAmplitude/LocallyFiniteTorDimension.lean#L189). The attribute's comment: “locally finite tor dimension”.

> **Stacks 08FZ (3).** An object `E` of `D(O)` *locally has finite Tor dimension* if every
> object `U` of `C` carries a covering family on each member `V` of which the restriction of `E` to
> the localized ringed site has finite Tor dimension. Finite Tor dimension on the slice over `V`
> is measured against the given derived tensor product `T V` on that slice.

```lean
def LocallyHasFiniteTorDimension
    (T : ∀ U : X.C, DerivedTensorProduct.{max u v, v, w, d} (X.over U))
    (E : RingedSite.DerivedModules.{u, v, w, d} X) : Prop
```

## Tag 08G0, a lemma

[Tag 08G0](https://stacks.math.columbia.edu/tag/08G0) in the Stacks Project.

**`Stacks.SheafOfModules.DerivedTensorProduct.isFlat_cokernel_of_hasTorAmplitude`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/TorAmplitude/FlatCokernel.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/TorAmplitude/FlatCokernel.lean#L123). The attribute's comment: “variant: Tor amplitude measured against a derived tensor product datum `T` on D(O); the tag is Stacks.SheafOfModules.DerivedTensorProduct.isFlat_cokernel_of_hasTorAmplitude_canonical”.

> **Stacks 08G0.** The cokernel of the differential into the lowest degree of the
> Tor-amplitude interval of a bounded above complex of flat `O`-modules is a flat `O`-module.
>
> The complex is K-flat by Stacks 06YQ, so the Tor-amplitude hypothesis makes the three-term
> complex `K^{a-2} ⊗ F ⟶ K^{a-1} ⊗ F ⟶ K^a ⊗ F` exact for every `O`-module `F`. Hence
> `Coker(d^{a-1}) ⊗ -` preserves monomorphisms, and being right exact as well it is exact.

```lean
theorem isFlat_cokernel_of_hasTorAmplitude (T : DerivedTensorProduct.{u, v, w, d} X)
    (K : CochainComplex (RingedSite.Modules.{u, v, w} X) ℤ) (a b : ℤ)
    (hbound : ∃ n : ℤ, K.IsStrictlyLE n)
    (hflat : ∀ i : ℤ,
      AlgebraicGeometry.SheafOfModules.IsFlat.{v, u, w, w} (O := X.O) (K.X i))
    (hamp : HasTorAmplitude T (DerivedCategory.Q.obj K) a b) :
    AlgebraicGeometry.SheafOfModules.IsFlat.{v, u, w, w} (O := X.O)
      (cokernel (K.d (a - 1) a))
```

**`Stacks.SheafOfModules.DerivedTensorProduct.isFlat_cokernel_of_hasTorAmplitude_canonical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/TorAmplitude/FlatCokernelCanonical.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/TorAmplitude/FlatCokernelCanonical.lean#L64).

> **Stacks 08G0, for the derived tensor product of the site.** Let `(C, O)` be a ringed site
> and let `K` be a bounded above complex of flat `O`-modules which, as an object of `D(O)`, has
> Tor amplitude in `[a, b]` for the derived tensor product
> `Stacks.SheafOfModules.canonicalDerivedTensorProduct` of Stacks 06YU. Then the cokernel of the
> differential `K^{a-1} ⟶ K^a` is a flat `O`-module.
>
> No derived tensor product datum is supplied: the one Tor amplitude is measured against is the
> one Stacks 06YU constructs.

```lean
theorem isFlat_cokernel_of_hasTorAmplitude_canonical
    (K : CochainComplex (RingedSite.Modules.{u, u, u} X) ℤ) (a b : ℤ)
    (hbound : ∃ n : ℤ, K.IsStrictlyLE n)
    (hflat : ∀ i : ℤ,
      AlgebraicGeometry.SheafOfModules.IsFlat.{u, u, u, u} (O := X.O) (K.X i)) :
    letI : HasSheafify X.J AddCommGrpCat.{u} := inferInstance
    letI : X.J.WEqualsLocallyBijective AddCommGrpCat.{u} := inferInstance
    letI := Stacks.SheafOfModules.Tensor.sheafTensor_obj_additive.{u, u, u, u, u} X.O
    HasTorAmplitude (Stacks.SheafOfModules.canonicalDerivedTensorProduct.{u, u, d} X)
        (DerivedCategory.Q.obj K) a b →
      AlgebraicGeometry.SheafOfModules.IsFlat.{u, u, u, u} (O := X.O)
        (cokernel (K.d (a - 1) a))
```

## Tag 08G1, a lemma

[Tag 08G1](https://stacks.math.columbia.edu/tag/08G1) in the Stacks Project.

**`Stacks.SheafOfModules.DerivedTensorProduct.hasTorAmplitude_iff_exists_flatRepresentative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/TorAmplitude/FlatRepresentative.lean, line 288](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/TorAmplitude/FlatRepresentative.lean#L288). References: SGA 4 XVII (4.1.9), “(i) <=> (iii)”; SGA 6 I (5.1).

> **Stacks 08G1.** An object of `D(O)` has Tor amplitude in `[a, b]` exactly when some complex
> of flat `O`-modules vanishing in every degree outside `[a, b]` represents it.

```lean
theorem hasTorAmplitude_iff_exists_flatRepresentative
    (T : DerivedTensorProduct.{u, v, w, d} Y)
    (E : RingedSite.DerivedModules.{u, v, w, d} Y) (a b : ℤ) (hab : a ≤ b) :
    HasTorAmplitude T E a b ↔
      ∃ K : CochainComplex (RingedSite.Modules.{u, v, w} Y) ℤ,
        (∀ i : ℤ, AlgebraicGeometry.SheafOfModules.IsFlat.{v, u, w, w}
          (O := Y.O) (K.X i)) ∧
        (∀ i : ℤ, i ∉ Set.Icc a b → IsZero (K.X i)) ∧
        Nonempty (DerivedCategory.Q.obj K ≅ E)
```

**`Stacks.SheafOfModules.DerivedTensorProduct.hasTorAmplitude_canonical_iff_exists_flatRepresentative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/TorAmplitude/FlatRepresentativeCanonical.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/TorAmplitude/FlatRepresentativeCanonical.lean#L70). The attribute's comment: “for the derived tensor product of the site, with no datum assumed”. References: SGA 4 XVII (4.1.9), “(i) <=> (iii)”; SGA 6 I (5.1).

> **Stacks 08G1, for the derived tensor product of the site.** An object of `D(O)` has Tor
> amplitude in `[a, b]`, measured against the derived tensor product
> `Stacks.SheafOfModules.canonicalDerivedTensorProduct` of Stacks 06YU, exactly when some
> complex of flat `O`-modules vanishing in every degree outside `[a, b]` represents it.
>
> No derived tensor product datum is assumed: the one the statement speaks of is the one Stacks
> 06YU constructs.

```lean
theorem hasTorAmplitude_canonical_iff_exists_flatRepresentative
    (E : RingedSite.DerivedModules.{u, u, u, d} X) (a b : ℤ) (hab : a ≤ b) :
    letI : HasSheafify X.J AddCommGrpCat.{u} := inferInstance
    letI : X.J.WEqualsLocallyBijective AddCommGrpCat.{u} := inferInstance
    letI := Stacks.SheafOfModules.Tensor.sheafTensor_obj_additive.{u, u, u, u, u} X.O
    HasTorAmplitude (Stacks.SheafOfModules.canonicalDerivedTensorProduct.{u, u, d} X) E a b ↔
      ∃ K : CochainComplex (RingedSite.Modules.{u, u, u} X) ℤ,
        (∀ i : ℤ, AlgebraicGeometry.SheafOfModules.IsFlat.{u, u, u, u}
          (O := X.O) (K.X i)) ∧
        (∀ i : ℤ, i ∉ Set.Icc a b → IsZero (K.X i)) ∧
        Nonempty (DerivedCategory.Q.obj K ≅ E)
```

## Tag 0F1M, a lemma

[Tag 0F1M](https://stacks.math.columbia.edu/tag/0F1M) in the Stacks Project.

**`Stacks.SheafOfModules.hasTorAmplitudeGE_iff_exists_kFlatRepresentative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/TorAmplitude/BoundedBelowCanonical.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/TorAmplitude/BoundedBelowCanonical.lean#L64). The attribute's comment: “equivalence”.

> **Stacks 0F1M.** Let `(C, O)` be a ringed site, `E` an object of `D(O)` and `a` an integer.
> Then `E` has Tor amplitude in `[a, ∞]` for the derived tensor product of `D(O)` — that is,
> `E ⊗^L_O F[0]` has no cohomology below `a` for every `O`-module `F` — if and only if `E` is
> represented by a K-flat complex of flat `O`-modules vanishing in every degree below `a`.

```lean
theorem hasTorAmplitudeGE_iff_exists_kFlatRepresentative
    (E : RingedSite.DerivedModules.{u, u, u, d} X) (a : ℤ) :
    letI : X.J.WEqualsLocallyBijective AddCommGrpCat.{u} := inferInstance
    DerivedTensorProduct.HasTorAmplitudeGE (canonicalDerivedTensorProduct.{u, u, d} X) E a ↔
      ∃ K : CochainComplex (RingedSite.Modules.{u, u, u} X) ℤ,
        IsKFlat X.O K ∧
        (∀ i : ℤ, AlgebraicGeometry.SheafOfModules.IsFlat.{u, u, u, u} (O := X.O) (K.X i)) ∧
        (∀ i : ℤ, i < a → IsZero (K.X i)) ∧
        Nonempty (DerivedCategory.Q.obj K ≅ E)
```

**`Stacks.SheafOfModules.exists_pullbackStable_kFlatRepresentative_of_hasTorAmplitudeGE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/TorAmplitude/BoundedBelowCanonical.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/TorAmplitude/BoundedBelowCanonical.lean#L85). The attribute's comment: “the Moreover clause: the representative stays K-flat, and keeps flat terms, under pullback”.

> **Stacks 0F1M, the "moreover" clause.** An object `E` of `D(O)` with Tor amplitude in
> `[a, ∞]` for the derived tensor product of `D(O)` is represented by a complex `K` which is
> K-flat, has flat terms and vanishes in every degree below `a`, and which moreover stays K-flat
> with flat terms under pullback: for every morphism `f` of ringed topoi into `(C, O)` presented
> by a morphism of sites, the degreewise pullback `f^*K` is K-flat and each of its terms is
> flat.

```lean
theorem exists_pullbackStable_kFlatRepresentative_of_hasTorAmplitudeGE
    (E : RingedSite.DerivedModules.{u, u, u, d} X) (a : ℤ)
    (hE :
      letI : X.J.WEqualsLocallyBijective AddCommGrpCat.{u} := inferInstance
      DerivedTensorProduct.HasTorAmplitudeGE
        (canonicalDerivedTensorProduct.{u, u, d} X) E a) :
    letI : X.J.WEqualsLocallyBijective AddCommGrpCat.{u} := inferInstance
    ∃ K : CochainComplex (RingedSite.Modules.{u, u, u} X) ℤ,
      IsKFlat X.O K ∧
      (∀ i : ℤ, AlgebraicGeometry.SheafOfModules.IsFlat.{u, u, u, u} (O := X.O) (K.X i)) ∧
      (∀ i : ℤ, i < a → IsZero (K.X i)) ∧
      Nonempty (DerivedCategory.Q.obj K ≅ E) ∧
      ∀ X' : AlgebraicGeometry.RingedTopos.{u, u, u},
        letI : X'.J.WEqualsLocallyBijective AddCommGrpCat.{u} := inferInstance
        ∀ f : AlgebraicGeometry.RingedToposSiteHom X' (RingedSite.ringedTopos X),
          f.u.IsMorphismOfSites (RingedSite.ringedTopos X).J X'.J →
            IsKFlat X'.O
                ((Stacks.Sheaves.DerivedPullback.KFlatPullback.pullbackComplex f).obj K) ∧
              ∀ i : ℤ, AlgebraicGeometry.SheafOfModules.IsFlat.{u, u, u, u} (O := X'.O)
                (((Stacks.Sheaves.DerivedPullback.KFlatPullback.pullbackComplex f).obj K).X i)
```

## Tag 08H5, a lemma

[Tag 08H5](https://stacks.math.columbia.edu/tag/08H5) in the Stacks Project.

**`Stacks.SheafOfModules.DerivedTensorProduct.hasTorAmplitude_derivedPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/TorAmplitude/DerivedPullbackAlongRingedTopoi.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/TorAmplitude/DerivedPullbackAlongRingedTopoi.lean#L152).

> **Stacks 08H5.**  The derived pullback along a morphism of ringed topoi preserves Tor
> amplitude in a fixed interval.
>
> A degenerate interval `b < a` says that the derived tensor products of `E` with every module
> vanish in *every* degree, so in particular `E` has Tor amplitude in the one-point interval
> `[i + 1, i + 1]` for whichever degree `i` is being examined, and
> `hasTorAmplitude_derivedPullback_of_le` applies there.

```lean
theorem hasTorAmplitude_derivedPullback
    (T : DerivedTensorProduct Y.toRingedSite) (T' : DerivedTensorProduct X.toRingedSite)
    (E : RingedSite.DerivedModules Y.toRingedSite) (a b : ℤ)
    (hamp : HasTorAmplitude T E a b) :
    HasTorAmplitude T' ((derivedPullback f).obj E) a b
```

## Tag 08G2, a lemma

[Tag 08G2](https://stacks.math.columbia.edu/tag/08G2) in the Stacks Project.

**`Stacks.SheafOfModules.DerivedTensorProduct.hasTorAmplitude_obj₃`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/TorAmplitude/DistinguishedTriangles.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/TorAmplitude/DistinguishedTriangles.lean#L60). The attribute's comment: “(1)”.

> **Stacks 08G2 (1).** In a distinguished triangle `K ⟶ L ⟶ M ⟶ K[1]` of `D(O)`, if `K` has
> Tor amplitude in `[a + 1, b + 1]` and `L` has Tor amplitude in `[a, b]`, then `M` has Tor
> amplitude in `[a, b]`.

```lean
theorem hasTorAmplitude_obj₃
    (tri : Triangle (RingedSite.DerivedModules.{u, v, w, d} X))
    (htri : tri ∈ distinguishedTriangles) (a b : ℤ)
    (hK : HasTorAmplitude T tri.obj₁ (a + 1) (b + 1))
    (hL : HasTorAmplitude T tri.obj₂ a b) :
    HasTorAmplitude T tri.obj₃ a b
```

**`Stacks.SheafOfModules.DerivedTensorProduct.hasTorAmplitude_obj₂`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/TorAmplitude/DistinguishedTriangles.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/TorAmplitude/DistinguishedTriangles.lean#L78). The attribute's comment: “(2)”.

> **Stacks 08G2 (2).** In a distinguished triangle `K ⟶ L ⟶ M ⟶ K[1]` of `D(O)`, if `K` and
> `M` both have Tor amplitude in `[a, b]`, then so does `L`.

```lean
theorem hasTorAmplitude_obj₂
    (tri : Triangle (RingedSite.DerivedModules.{u, v, w, d} X))
    (htri : tri ∈ distinguishedTriangles) (a b : ℤ)
    (hK : HasTorAmplitude T tri.obj₁ a b)
    (hM : HasTorAmplitude T tri.obj₃ a b) :
    HasTorAmplitude T tri.obj₂ a b
```

**`Stacks.SheafOfModules.DerivedTensorProduct.hasTorAmplitude_obj₁`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/TorAmplitude/DistinguishedTriangles.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/TorAmplitude/DistinguishedTriangles.lean#L96). The attribute's comment: “(3)”.

> **Stacks 08G2 (3).** In a distinguished triangle `K ⟶ L ⟶ M ⟶ K[1]` of `D(O)`, if `L` has
> Tor amplitude in `[a + 1, b + 1]` and `M` has Tor amplitude in `[a, b]`, then `K` has Tor
> amplitude in `[a + 1, b + 1]`.

```lean
theorem hasTorAmplitude_obj₁
    (tri : Triangle (RingedSite.DerivedModules.{u, v, w, d} X))
    (htri : tri ∈ distinguishedTriangles) (a b : ℤ)
    (hL : HasTorAmplitude T tri.obj₂ (a + 1) (b + 1))
    (hM : HasTorAmplitude T tri.obj₃ a b) :
    HasTorAmplitude T tri.obj₁ (a + 1) (b + 1)
```

## Tag 09JA, a lemma

[Tag 09JA](https://stacks.math.columbia.edu/tag/09JA) in the Stacks Project.

**`Stacks.SheafOfModules.DerivedTensorProduct.hasTorAmplitude_tensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/TorAmplitude/TensorProduct.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/TorAmplitude/TensorProduct.lean#L178).

> **Stacks 09JA.** If `K` has Tor amplitude in `[a, b]` and `L` has Tor amplitude in
> `[c, d]`, then `K ⊗^L_O L` has Tor amplitude in `[a + c, b + d]`.
>
> A degenerate interval is replaced by a one-point interval chosen below the degree under
> consideration, which is a weaker hypothesis, and `hasTorAmplitude_tensor_of_le` applies.

```lean
theorem hasTorAmplitude_tensor (a b c d : ℤ)
    (hK : HasTorAmplitude T K a b) (hL : HasTorAmplitude T L c d) :
    HasTorAmplitude T ((T.tensor.obj K).obj L) (a + c) (b + d)
```

## Tag 08G3, a lemma

[Tag 08G3](https://stacks.math.columbia.edu/tag/08G3) in the Stacks Project.

**`Stacks.SheafOfModules.DerivedTensorProduct.hasTorAmplitude_of_biprod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/TorAmplitude/DirectSummands.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/TorAmplitude/DirectSummands.lean#L79).

> **Stacks 08G3.** If the direct sum `K ⊕ L` of two objects of `D(O)` has Tor amplitude in
> `[a, b]`, then both `K` and `L` have Tor amplitude in `[a, b]`.

```lean
theorem hasTorAmplitude_of_biprod (K L : RingedSite.DerivedModules.{u, v, w, d} X) (a b : ℤ)
    (h : HasTorAmplitude T (K ⊞ L) a b) :
    HasTorAmplitude T K a b ∧ HasTorAmplitude T L a b
```

## Tag 0942, a lemma

[Tag 0942](https://stacks.math.columbia.edu/tag/0942) in the Stacks Project.

**`Stacks.Sites.isUniformlyBoundedAbove_tensor_adicQuotientModule_of_isBoundedAbove`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/TorAmplitude/AdicQuotientsBoundedAbove.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/TorAmplitude/AdicQuotientsBoundedAbove.lean#L83). The attribute's comment: “uniformly bounded above”.

> **If `K ⊗^L_O O/I` is bounded above then `K ⊗^L_O O/Iⁿ` is uniformly bounded above**: one
> integer bounds the cohomology of every `K ⊗^L_O O/Iⁿ` from above. The graded pieces `Iⁿ/Iⁿ⁺¹`
> are killed by `I`, hence all bounded above by the bound of `K ⊗^L_O O/I` after tensoring with
> `K`, and the tower `0 → Iⁿ/Iⁿ⁺¹ → O/Iⁿ⁺¹ → O/Iⁿ → 0` carries that bound to every quotient.

```lean
theorem isUniformlyBoundedAbove_tensor_adicQuotientModule_of_isBoundedAbove
    (hQ : Stacks.DerivedCategory.IsBoundedAbove
      ((T.tensor.obj K).obj
        ((DerivedCategory.singleFunctor (RingedSite.Modules.{u, u, u} X) 0).obj
          (adicQuotientModule I 1))))
    :
    Stacks.DerivedCategory.IsUniformlyBoundedAbove
      (fun n : ℕ => (T.tensor.obj K).obj
        ((DerivedCategory.singleFunctor (RingedSite.Modules.{u, u, u} X) 0).obj
          (adicQuotientModule I n)))
```

**`Stacks.Sites.hasTorAmplitude_adicQuotient_of_hasTorAmplitude_adicQuotientOne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/TorAmplitude/AdicQuotientsTorAmplitude.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/TorAmplitude/AdicQuotientsTorAmplitude.lean#L135). The attribute's comment: “tor amplitude modulo every power of the ideal”.

> **Stacks 0942 part (2).** If `K ⊗^L_O O/I` has Tor amplitude in `[a, b]` as an object of
> `D(O/I)`, then `K ⊗^L_O O/Iⁿ` has Tor amplitude in `[a, b]` as an object of `D(O/Iⁿ)`, for
> every `n`.
>
> A sheaf `F` of `O/Iⁿ`-modules is tested by moving `(K ⊗^L_O O/Iⁿ) ⊗^L_{O/Iⁿ} F[0]` to `D(O)`:
> restriction of scalars reflects a vanishing cohomology sheaf, and the projection formula at
> `O ⟶ O/Iⁿ` identifies the restriction with `K ⊗^L_O F|_O`. There the filtration of `F|_O` by
> the powers of `I` reaches zero, so the vanishing follows from the one at the sheaves of
> `O`-modules killed by `I`, which is the hypothesis.

```lean
theorem hasTorAmplitude_adicQuotient_of_hasTorAmplitude_adicQuotientOne
    (T : Stacks.SheafOfModules.DerivedTensorProduct.{u, u, u, _} X)
    (T₁ : Stacks.SheafOfModules.DerivedTensorProduct.{u, u, u, _}
      (adicQuotientRingedSite X I 1))
    (n : ℕ)
    (Tₙ : Stacks.SheafOfModules.DerivedTensorProduct.{u, u, u, _}
      (adicQuotientRingedSite X I n))
    (K : RingedSite.DerivedModules.{u, u, u, _} X) (a b : ℤ)
    (h : HasTorAmplitude T₁
      ((Stacks.Cohomology.derivedCoefficientChange (toAdicQuotient I 1)).obj K) a b) :
    HasTorAmplitude Tₙ
      ((Stacks.Cohomology.derivedCoefficientChange (toAdicQuotient I n)).obj K) a b
```

## Tag 0DJJ, a lemma

[Tag 0DJJ](https://stacks.math.columbia.edu/tag/0DJJ) in the Stacks Project.

**`Stacks.SheafOfModules.DerivedTensorProduct.hasTorAmplitudeCanonical_derivedModuleFiber_canonical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/TorAmplitude/StalksCanonical.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/TorAmplitude/StalksCanonical.lean#L66). The attribute's comment: “part (1)”. References: SGA 6 I (5.6.2), “fiber direction”; SGA 6 III (3.3), “(i)=>(ii), f=id”; SGA 4 XVII (4.2.8), “(iii) f=id, forward”.

> If an object `E` of `D(O)` has Tor amplitude in `[a, b]` for the derived tensor product of the
> ringed site, then for every point `Φ` of the site its derived stalk `E_Φ` has Tor amplitude in
> `[a, b]` as an object of `D(O_Φ)`.

```lean
theorem hasTorAmplitudeCanonical_derivedModuleFiber_canonical
    (E : RingedSite.DerivedModules.{u, w, w, d} Y) (a b : ℤ)
    (hamp : HasTorAmplitude
      (Stacks.SheafOfModules.canonicalDerivedTensorProduct.{u, w, d} Y) E a b)
    (Φ : Y.J.Point.{w}) :
    letI : HasDerivedCategory.{d}
        (SheafOfModules.{w} (Stacks.commRingSheafToRingSheaf.{w, u, w} Y.O)) := hd
    StacksDraft.TorAmplitude.HasTorAmplitudeCanonical
      ((Φ.presheafFiber (A := CommRingCat.{w})).obj Y.O.obj)
      ((Stacks.derivedModuleFiber Φ Y.O).obj E) a b
```

**`Stacks.SheafOfModules.DerivedTensorProduct.hasTorAmplitude_canonical_of_forall_derivedModuleFiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/TorAmplitude/StalksCanonical.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/TorAmplitude/StalksCanonical.lean#L84). The attribute's comment: “part (2)”. References: SGA 6 I (5.6.2), “converse, enough points”; SGA 6 III (3.3), “(ii)=>(i), f=id”; SGA 4 XVII (4.2.8), “(iii) f=id, converse”.

> On a ringed site whose underlying site has a conservative family of points, an object `E`
> of `D(O)` has Tor amplitude in `[a, b]` for the derived tensor product of the site as soon as its
> derived stalk at every point of the site does.

```lean
theorem hasTorAmplitude_canonical_of_forall_derivedModuleFiber
    (E : RingedSite.DerivedModules.{u, w, w, d} Y) (a b : ℤ)
    (hY : Y.J.HasConservativeFamily.{w})
    (hE : ∀ Φ : Y.J.Point.{w},
      letI : HasDerivedCategory.{d}
          (SheafOfModules.{w} (Stacks.commRingSheafToRingSheaf.{w, u, w} Y.O)) := hd
      StacksDraft.TorAmplitude.HasTorAmplitudeCanonical
        ((Φ.presheafFiber (A := CommRingCat.{w})).obj Y.O.obj)
        ((Stacks.derivedModuleFiber Φ Y.O).obj E) a b) :
    HasTorAmplitude (Stacks.SheafOfModules.canonicalDerivedTensorProduct.{u, w, d} Y) E a b
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.46, Tag 08FY](https://stacks.math.columbia.edu/tag/08FY)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
