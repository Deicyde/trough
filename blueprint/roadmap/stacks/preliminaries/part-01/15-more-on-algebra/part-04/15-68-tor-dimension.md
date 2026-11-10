---
declaration: section
origin: cited
lean: StacksDraft.TorAmplitude.HasTorAmplitude, StacksDraft.TorAmplitude.HasFiniteTorDimension, StacksDraft.TorAmplitude.HasTorDimensionLE, StacksDraft.TorAmplitude.ModuleHasFiniteTorDimension, StacksDraft.TorAmplitude.cokernel_flat_of_torAmplitude, StacksDraft.TorAmplitude.hasTorAmplitudeCanonical_iff_hasFlatRepresentative, StacksDraft.TorAmplitude.hasTorAmplitudeAbove_iff_exists_kFlat_flat_representative_canonical, StacksDraft.TorAmplitude.hasTorAmplitude_obj₃_of_obj₁_obj₂
statement: formalized
proof: formalized
---

# 15.68 Tor dimension

Section 15.68 of the Stacks Project, [Tag 0651](https://stacks.math.columbia.edu/tag/0651). 20 tags here are carried by 25 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0652, a definition

[Tag 0652](https://stacks.math.columbia.edu/tag/0652) in the Stacks Project.

**`StacksDraft.TorAmplitude.HasTorAmplitude`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TorAmplitude/Defs.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/TorAmplitude/Defs.lean#L80). The attribute's comment: “(1)”. References: SGA 4½ Rapport (4.5), “tor-dimension ≤ r”; SGA 6 I (5.2), “Tor-amp(F) ⊂ [m,n]”.

> An object `K` of `D(R)` has Tor amplitude in `[a, b]` if, for every `R`-module `M`, the
> cohomology of `K ⊗ᴸ[R] M[0]` vanishes in every degree outside `[a, b]`.
>
> The `comparison` and `_isLeftDerived` arguments certify that `derivedTensor` is the total left
> derived functor of ordinary tensor product in the first variable.

```lean
public def HasTorAmplitude {R : Type u} [CommRing R]
    [HasDerivedCategory (ModuleCat.{v} R)]
    (derivedTensor :
      DerivedCategory (ModuleCat.{v} R) ⥤
        DerivedCategory (ModuleCat.{v} R) ⥤ DerivedCategory (ModuleCat.{v} R))
    (comparison : ∀ M : ModuleCat.{v} R,
      DerivedCategory.Q ⋙
          derivedTensor.flip.obj
            ((DerivedCategory.singleFunctor (ModuleCat.{v} R) 0).obj M) ⟶
        (tensorModuleRight M).mapHomologicalComplex
            (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
    (_isLeftDerived : ∀ M : ModuleCat.{v} R,
      (derivedTensor.flip.obj
          ((DerivedCategory.singleFunctor (ModuleCat.{v} R) 0).obj M)).IsLeftDerivedFunctor
        (comparison M)
        (HomologicalComplex.quasiIso (ModuleCat.{v} R) (ComplexShape.up ℤ)))
    (K : DerivedCategory (ModuleCat.{v} R)) (a b : ℤ) : Prop
```

**`StacksDraft.TorAmplitude.HasFiniteTorDimension`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TorAmplitude/Defs.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/TorAmplitude/Defs.lean#L107). The attribute's comment: “(2)”. References: SGA 4½ Rapport (4.5), “finite tor dimension”; SGA 5 I (1.10), “affine case (torf)”; SGA 6 I (5.2), “finite flat amplitude”.

> An object of `D(R)` has finite Tor dimension if it has Tor amplitude in some finite
> integer interval.

```lean
public def HasFiniteTorDimension {R : Type u} [CommRing R]
    [HasDerivedCategory (ModuleCat.{v} R)]
    (derivedTensor :
      DerivedCategory (ModuleCat.{v} R) ⥤
        DerivedCategory (ModuleCat.{v} R) ⥤ DerivedCategory (ModuleCat.{v} R))
    (comparison : ∀ M : ModuleCat.{v} R,
      DerivedCategory.Q ⋙
          derivedTensor.flip.obj
            ((DerivedCategory.singleFunctor (ModuleCat.{v} R) 0).obj M) ⟶
        (tensorModuleRight M).mapHomologicalComplex
            (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
    (isLeftDerived : ∀ M : ModuleCat.{v} R,
      (derivedTensor.flip.obj
          ((DerivedCategory.singleFunctor (ModuleCat.{v} R) 0).obj M)).IsLeftDerivedFunctor
        (comparison M)
        (HomologicalComplex.quasiIso (ModuleCat.{v} R) (ComplexShape.up ℤ)))
    (K : DerivedCategory (ModuleCat.{v} R)) : Prop
```

**`StacksDraft.TorAmplitude.HasTorDimensionLE`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TorAmplitude/Defs.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/TorAmplitude/Defs.lean#L129). The attribute's comment: “(3)”. References: SGA 4 XVII (4.1.9), “module over a ring”; SGA 4½ Rapport (4.5), “module case”.

> An `R`-module `M` has Tor dimension at most `d` if `M[0]` has Tor amplitude in
> `[-d, 0]`.

```lean
public def HasTorDimensionLE {R : Type u} [CommRing R]
    [HasDerivedCategory (ModuleCat.{v} R)]
    (derivedTensor :
      DerivedCategory (ModuleCat.{v} R) ⥤
        DerivedCategory (ModuleCat.{v} R) ⥤ DerivedCategory (ModuleCat.{v} R))
    (comparison : ∀ N : ModuleCat.{v} R,
      DerivedCategory.Q ⋙
          derivedTensor.flip.obj
            ((DerivedCategory.singleFunctor (ModuleCat.{v} R) 0).obj N) ⟶
        (tensorModuleRight N).mapHomologicalComplex
            (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
    (isLeftDerived : ∀ N : ModuleCat.{v} R,
      (derivedTensor.flip.obj
          ((DerivedCategory.singleFunctor (ModuleCat.{v} R) 0).obj N)).IsLeftDerivedFunctor
        (comparison N)
        (HomologicalComplex.quasiIso (ModuleCat.{v} R) (ComplexShape.up ℤ)))
    (M : ModuleCat.{v} R) (d : ℤ) : Prop
```

**`StacksDraft.TorAmplitude.ModuleHasFiniteTorDimension`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TorAmplitude/Defs.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/TorAmplitude/Defs.lean#L152). The attribute's comment: “(4)”.

> An `R`-module `M` has finite Tor dimension if `M[0]` has finite Tor dimension as an
> object of `D(R)`.

```lean
public def ModuleHasFiniteTorDimension {R : Type u} [CommRing R]
    [HasDerivedCategory (ModuleCat.{v} R)]
    (derivedTensor :
      DerivedCategory (ModuleCat.{v} R) ⥤
        DerivedCategory (ModuleCat.{v} R) ⥤ DerivedCategory (ModuleCat.{v} R))
    (comparison : ∀ N : ModuleCat.{v} R,
      DerivedCategory.Q ⋙
          derivedTensor.flip.obj
            ((DerivedCategory.singleFunctor (ModuleCat.{v} R) 0).obj N) ⟶
        (tensorModuleRight N).mapHomologicalComplex
            (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
    (isLeftDerived : ∀ N : ModuleCat.{v} R,
      (derivedTensor.flip.obj
          ((DerivedCategory.singleFunctor (ModuleCat.{v} R) 0).obj N)).IsLeftDerivedFunctor
        (comparison N)
        (HomologicalComplex.quasiIso (ModuleCat.{v} R) (ComplexShape.up ℤ)))
    (M : ModuleCat.{v} R) : Prop
```

## Tag 0653, a lemma

[Tag 0653](https://stacks.math.columbia.edu/tag/0653) in the Stacks Project.

**`StacksDraft.TorAmplitude.cokernel_flat_of_torAmplitude`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TorAmplitude/DerivedComparison.lean, line 497](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/TorAmplitude/DerivedComparison.lean#L497).

> **Stacks Tag 0653.** Let `R` be a ring, `a b : ℤ`, and `K` a bounded above cochain complex of
> flat `R`-modules which, as an object of `D(R)`, has Tor amplitude in `[a, b]` for some certified
> derived tensor product. Then `Coker(d_K^{a-1}) = K^a / Im(d_K^{a-1})` is a flat `R`-module.
>
> The ring universe `u` and the module universe are independent: `R : Type u` and the complex lives
> in `ModuleCat.{max u v} R`. Flatness of the terms is spelled out rather than written as
> `StacksDraft.TorAmplitude.Termwise.IsComplexOfFlats`, which is available only when the two
>   universes agree.
>
> The derived tensor product is an arbitrary certified one, so the statement does not depend on a
> construction of it. Boundedness enters through the comparison: the counit of the total left
> derived functor of termwise tensoring is invertible at a bounded above complex of flat modules
> (`isIso_termwiseDerivedCounit_app_of_flat`), which makes the given comparison map a split
> epimorphism there, and cohomology carries that split epimorphism from a vanishing source to a
> vanishing target.

```lean
public theorem cokernel_flat_of_torAmplitude
    (K : CochainComplex (ModuleCat.{max u v} R) ℤ) (a b : ℤ)
    (hbounded : BoundedAbove K) (hflat : ∀ n : ℤ, Module.Flat R (K.X n))
    (hamp : HasTorAmplitude derivedTensor comparison isLeftDerived
      (DerivedCategory.Q.obj K) a b) :
    Module.Flat R (cokernel (K.d (a - 1) a) : ModuleCat.{max u v} R)
```

## Tag 0654, a lemma

[Tag 0654](https://stacks.math.columbia.edu/tag/0654) in the Stacks Project.

**`StacksDraft.TorAmplitude.hasTorAmplitudeCanonical_iff_hasFlatRepresentative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TorAmplitude/CanonicalCertificate.lean, line 315](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/TorAmplitude/CanonicalCertificate.lean#L315). References: SGA 6 I (5.1), “affine case”; SGA 4 XVII (4.1.9), “over a ring, (i)<=>(iii)”.

> An object `K` of `D(R)` has Tor amplitude in `[a, b]` — at the canonical derived tensor
> product of Stacks 0BYI — if and only if it is represented by a complex of flat
> `R`-modules concentrated in degrees `[a, b]`.

```lean
public theorem hasTorAmplitudeCanonical_iff_hasFlatRepresentative (R : Type u) [CommRing R]
    (K : DerivedCategory (ModuleCat.{u} R)) (a b : ℤ) :
    HasTorAmplitudeCanonical R K a b ↔ HasFlatRepresentative K a b
```

## Tag 0BYL, a lemma

[Tag 0BYL](https://stacks.math.columbia.edu/tag/0BYL) in the Stacks Project.

**`StacksDraft.TorAmplitude.hasTorAmplitudeAbove_iff_exists_kFlat_flat_representative_canonical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TorAmplitude/KFlatRepresentative.lean, line 265](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/TorAmplitude/KFlatRepresentative.lean#L265). References: SGA 4 XVII (4.1.9), “ring case, one-sided”.

> **Stacks 0BYL.** An object `K` of `D(R)` has Tor amplitude in `[a, ∞]` — that is, the derived
> tensor product of `K` with any module `M` placed in cohomological degree zero has vanishing
> cohomology in all degrees below `a` — if and only if `K` is represented by a K-flat complex of
> flat modules concentrated in degrees at least `a`.
>
> The derived tensor product here is *the* canonical one,
> `CochainComplex.DerivedTensor.canonicalDerivedTensorProduct R` of Stacks 0BYI, so the statement
> is an assertion about a specific bifunctor rather than a claim quantified over certificates.
> It is obtained by instantiating
> `StacksDraft.TorAmplitude.hasTorAmplitudeAbove_iff_exists_kFlat_flat_representative`, which
> proves the equivalence for an arbitrary certified derived tensor bifunctor, at that canonical
> choice.

```lean
public theorem hasTorAmplitudeAbove_iff_exists_kFlat_flat_representative_canonical
    (K : DerivedCategory (ModuleCat.{u} R)) (a : ℤ) :
    (∀ (M : ModuleCat.{u} R) (i : ℤ), i < a →
        IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{u} R) i).obj
          (((CochainComplex.DerivedTensor.canonicalDerivedTensorProduct R).tensor.obj K).obj
            ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj M)))) ↔
      ∃ E : CochainComplex (ModuleCat.{u} R) ℤ,
        E.KFlat ∧
          (∀ n : ℤ, Module.Flat R (E.X n)) ∧
          E.IsStrictlyGE a ∧
          Nonempty (K ≅ DerivedCategory.Q.obj E)
```

## Tag 0655, a lemma

[Tag 0655](https://stacks.math.columbia.edu/tag/0655) in the Stacks Project.

**`StacksDraft.TorAmplitude.hasTorAmplitude_obj₃_of_obj₁_obj₂`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TorAmplitude/Triangle.lean, line 345](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/TorAmplitude/Triangle.lean#L345). The attribute's comment: “(1)”.

> **Stacks 0655 (1).** Let `K → L → M → K[1]` be a distinguished triangle in `D(R)`. If `K`
> has Tor amplitude in `[a + 1, b + 1]` and `L` has Tor amplitude in `[a, b]`, then `M` has Tor
> amplitude in `[a, b]`.
>
> Tor amplitude is `StacksDraft.TorAmplitude.HasTorAmplitude` of Stacks 0652, so the bifunctor
> `derivedTensor` is certified by `comparison` and `isLeftDerived` to be the derived tensor
> product. This is part (1) of the source statement; the mathematics is the long exact cohomology
> sequence of the triangle `(K, L, M)` tensored with `M'[0]`, as in the uncertified-datum helper
> `Stacks.TorAmplitudeTriangle.hasTorAmplitudeIn_obj₃_of_obj₁_obj₂`, which this endpoint does not use
> because that helper pins the module carriers to the ring universe.

```lean
theorem hasTorAmplitude_obj₃_of_obj₁_obj₂
    (T : Triangle (DerivedCategory (ModuleCat.{v} R)))
    (hT : T ∈ distTriang (DerivedCategory (ModuleCat.{v} R))) (a b : ℤ)
    (hK : HasTorAmplitude derivedTensor comparison isLeftDerived T.obj₁ (a + 1) (b + 1))
    (hL : HasTorAmplitude derivedTensor comparison isLeftDerived T.obj₂ a b) :
    HasTorAmplitude derivedTensor comparison isLeftDerived T.obj₃ a b
```

**`StacksDraft.TorAmplitude.hasTorAmplitude_obj₂_of_obj₁_obj₃`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TorAmplitude/Triangle.lean, line 374](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/TorAmplitude/Triangle.lean#L374). The attribute's comment: “(2)”.

> **Stacks 0655 (2).** Let `K → L → M → K[1]` be a distinguished triangle in `D(R)`. If `K`
> and `M` both have Tor amplitude in `[a, b]`, then `L` has Tor amplitude in `[a, b]`.
>
> Tor amplitude is `StacksDraft.TorAmplitude.HasTorAmplitude` of Stacks 0652, so the bifunctor
> `derivedTensor` is certified by `comparison` and `isLeftDerived` to be the derived tensor
> product. This is part (2) of the source statement; the mathematics is the long exact cohomology
> sequence of the triangle `(K, L, M)` tensored with `M'[0]`, as in the uncertified-datum helper
> `Stacks.TorAmplitudeTriangle.hasTorAmplitudeIn_obj₂_of_obj₁_obj₃`, which this endpoint does not use
> because that helper pins the module carriers to the ring universe.

```lean
theorem hasTorAmplitude_obj₂_of_obj₁_obj₃
    (T : Triangle (DerivedCategory (ModuleCat.{v} R)))
    (hT : T ∈ distTriang (DerivedCategory (ModuleCat.{v} R))) (a b : ℤ)
    (hK : HasTorAmplitude derivedTensor comparison isLeftDerived T.obj₁ a b)
    (hM : HasTorAmplitude derivedTensor comparison isLeftDerived T.obj₃ a b) :
    HasTorAmplitude derivedTensor comparison isLeftDerived T.obj₂ a b
```

**`StacksDraft.TorAmplitude.hasTorAmplitude_obj₁_of_obj₂_obj₃`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TorAmplitude/Triangle.lean, line 403](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/TorAmplitude/Triangle.lean#L403). The attribute's comment: “(3)”.

> **Stacks 0655 (3).** Let `K → L → M → K[1]` be a distinguished triangle in `D(R)`. If `L`
> has Tor amplitude in `[a + 1, b + 1]` and `M` has Tor amplitude in `[a, b]`, then `K` has Tor
> amplitude in `[a + 1, b + 1]`.
>
> Tor amplitude is `StacksDraft.TorAmplitude.HasTorAmplitude` of Stacks 0652, so the bifunctor
> `derivedTensor` is certified by `comparison` and `isLeftDerived` to be the derived tensor
> product. This is part (3) of the source statement; the mathematics is the long exact cohomology
> sequence of the triangle `(K, L, M)` tensored with `M'[0]`, as in the uncertified-datum helper
> `Stacks.TorAmplitudeTriangle.hasTorAmplitudeIn_obj₁_of_obj₂_obj₃`, which this endpoint does not use
> because that helper pins the module carriers to the ring universe.

```lean
theorem hasTorAmplitude_obj₁_of_obj₂_obj₃
    (T : Triangle (DerivedCategory (ModuleCat.{v} R)))
    (hT : T ∈ distTriang (DerivedCategory (ModuleCat.{v} R))) (a b : ℤ)
    (hL : HasTorAmplitude derivedTensor comparison isLeftDerived T.obj₂ (a + 1) (b + 1))
    (hM : HasTorAmplitude derivedTensor comparison isLeftDerived T.obj₃ a b) :
    HasTorAmplitude derivedTensor comparison isLeftDerived T.obj₁ (a + 1) (b + 1)
```

## Tag 066F, a lemma

[Tag 066F](https://stacks.math.columbia.edu/tag/066F) in the Stacks Project.

**`StacksDraft.TorAmplitude.hasTorDimensionLECanonical_iff_hasFlatRepresentative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TorAmplitude/CanonicalCertificate.lean, line 329](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/TorAmplitude/CanonicalCertificate.lean#L329). References: SGA 4 XVII (4.1.9), “module over a ring”; SGA 6 I (5.4), “commutative ring”; SGA 6 I (5.1), “module over a ring”.

> An `R`-module `M` has Tor dimension at most `d` — at the canonical derived
> tensor product — if and only if it admits a flat resolution of length `d`, that is, a complex of
> flat modules concentrated in degrees `[-d, 0]` representing `M[0]`.  In particular `M` has Tor
> dimension at most `0` if and only if `M` is flat.

```lean
public theorem hasTorDimensionLECanonical_iff_hasFlatRepresentative (R : Type u) [CommRing R]
    (M : ModuleCat.{u} R) (d : ℕ) :
    (HasTorDimensionLECanonical R M d ↔
        HasFlatRepresentative
          ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj M) (-(d : ℤ)) 0) ∧
      (HasTorAmplitudeCanonical R
          ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj M) 0 0 ↔
        Module.Flat R M)
```

## Tag 066G, a lemma

[Tag 066G](https://stacks.math.columbia.edu/tag/066G) in the Stacks Project.

**`StacksDraft.TorAmplitude.hasTorAmplitude_of_biprod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TorAmplitude/Summand.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/TorAmplitude/Summand.lean#L51).

> If `K ⊕ L` has Tor amplitude in `[a, b]`, then both `K` and `L` have Tor amplitude in
> `[a, b]`.

```lean
public theorem hasTorAmplitude_of_biprod {R : Type u} [CommRing R]
    (derivedTensor :
      DerivedCategory (ModuleCat.{v} R) ⥤
        DerivedCategory (ModuleCat.{v} R) ⥤ DerivedCategory (ModuleCat.{v} R))
    (comparison : ∀ M : ModuleCat.{v} R,
      DerivedCategory.Q ⋙
          derivedTensor.flip.obj
            ((DerivedCategory.singleFunctor (ModuleCat.{v} R) 0).obj M) ⟶
        (tensorModuleRight M).mapHomologicalComplex
            (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
    (isLeftDerived : ∀ M : ModuleCat.{v} R,
      (derivedTensor.flip.obj
          ((DerivedCategory.singleFunctor (ModuleCat.{v} R) 0).obj M)).IsLeftDerivedFunctor
        (comparison M)
        (HomologicalComplex.quasiIso (ModuleCat.{v} R) (ComplexShape.up ℤ)))
    (K L : DerivedCategory (ModuleCat.{v} R)) (a b : ℤ)
    (h : HasTorAmplitude derivedTensor comparison isLeftDerived (K ⊞ L) a b) :
    HasTorAmplitude derivedTensor comparison isLeftDerived K a b ∧
      HasTorAmplitude derivedTensor comparison isLeftDerived L a b
```

## Tag 066H, a lemma

[Tag 066H](https://stacks.math.columbia.edu/tag/066H) in the Stacks Project.

**`StacksDraft.TorAmplitude.hasTorAmplitude_and_finiteTorDimension_of_bounded_complex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TorAmplitude/Criteria.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/TorAmplitude/Criteria.lean#L166).

> **Stacks 066H.** A bounded complex whose term in degree `i` has Tor amplitude in
> `[a - i, b - i]` has Tor amplitude in `[a, b]`. In particular, if every term of a bounded
> complex has finite Tor dimension, then the complex has finite Tor dimension.

```lean
theorem hasTorAmplitude_and_finiteTorDimension_of_bounded_complex
    {R : Type} [CommRing R] (D : Stacks.TorAmplitudeTriangle.DerivedTensoring R)
    (K : CochainComplex (ModuleCat.{0} R) ℤ)
    (_hK : ∃ m n : ℤ, K.IsStrictlyGE m ∧ K.IsStrictlyLE n) :
    (∀ a b : ℤ, (∀ i : ℤ, Stacks.TorAmplitudeTriangle.HasTorAmplitudeIn D
          ((DerivedCategory.singleFunctor (ModuleCat.{0} R) 0).obj (K.X i))
          (a - i) (b - i)) →
        Stacks.TorAmplitudeTriangle.HasTorAmplitudeIn D (DerivedCategory.Q.obj K) a b) ∧
      ((∀ i : ℤ, ∃ aᵢ bᵢ : ℤ, Stacks.TorAmplitudeTriangle.HasTorAmplitudeIn D
          ((DerivedCategory.singleFunctor (ModuleCat.{0} R) 0).obj (K.X i)) aᵢ bᵢ) →
        ∃ a' b' : ℤ, Stacks.TorAmplitudeTriangle.HasTorAmplitudeIn D
          (DerivedCategory.Q.obj K) a' b')
```

## Tag 066I, a lemma

[Tag 066I](https://stacks.math.columbia.edu/tag/066I) in the Stacks Project.

**`StacksDraft.TorAmplitude.hasTorAmplitudeIn_of_cohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TorAmplitude/Criteria.lean, line 341](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/TorAmplitude/Criteria.lean#L341).

> **Stacks 066I.** A bounded derived object has Tor amplitude in `[a, b]` if its degree-`i`
> cohomology module has Tor amplitude in `[a - i, b - i]` for every `i`. In particular, if all
> of its cohomology modules have finite Tor dimension, then so does the derived object.

```lean
theorem hasTorAmplitudeIn_of_cohomology (R : Type) [CommRing R]
    (D : Stacks.TorAmplitudeTriangle.DerivedTensoring R)
    (K : DerivedCategory.Bounded (ModuleCat R)) :
    (∀ a b : ℤ,
      (∀ i : ℤ,
        Stacks.TorAmplitudeTriangle.HasTorAmplitudeIn D
          ((DerivedCategory.singleFunctor (ModuleCat R) 0).obj
            ((DerivedCategory.homologyFunctor (ModuleCat R) i).obj K.obj))
          (a - i) (b - i)) →
        Stacks.TorAmplitudeTriangle.HasTorAmplitudeIn D K.obj a b) ∧
      ((∀ i : ℤ, ∃ a b : ℤ,
        Stacks.TorAmplitudeTriangle.HasTorAmplitudeIn D
          ((DerivedCategory.singleFunctor (ModuleCat R) 0).obj
            ((DerivedCategory.homologyFunctor (ModuleCat R) i).obj K.obj)) a b) →
        ∃ a b : ℤ, Stacks.TorAmplitudeTriangle.HasTorAmplitudeIn D K.obj a b)
```

## Tag 0B66, a lemma

[Tag 0B66](https://stacks.math.columbia.edu/tag/0B66) in the Stacks Project.

**`StacksDraft.TorAmplitude.hasTorAmplitudeCanonical_derivedTensorProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TorAmplitude/CompositionCanonical.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/TorAmplitude/CompositionCanonical.lean#L70).

> Let `A → B` be a map of commutative rings and let `K` and `L` be complexes of `B`-modules. If
> `K` has Tor amplitude in `[a, b]` as a complex of `B`-modules and `L`, after restriction of
> scalars, has Tor amplitude in `[c, d]` as a complex of `A`-modules, then `K ⊗_B^L L`, after
> restriction of scalars, has Tor amplitude in `[a + c, b + d]` as a complex of `A`-modules.
>
> All three Tor amplitudes are those of Stacks 0652 at the canonical derived tensor product of
> Stacks 0BYI, and `K ⊗_B^L L` is that canonical derived tensor product over `B`.

```lean
public theorem hasTorAmplitudeCanonical_derivedTensorProduct
    (A B : Type u) [CommRing A] [CommRing B] [Algebra A B]
    (K L : CochainComplex (ModuleCat.{u} B) ℤ) (a b c d : ℤ)
    (hK : HasTorAmplitudeCanonical B (DerivedCategory.Q.obj K) a b)
    (hL : HasTorAmplitudeCanonical A
      ((ModuleCat.restrictScalars (algebraMap A B)).mapDerivedCategory.obj
        (DerivedCategory.Q.obj L)) c d) :
    HasTorAmplitudeCanonical A
      ((ModuleCat.restrictScalars (algebraMap A B)).mapDerivedCategory.obj
        (((canonicalDerivedTensorProduct B).tensor.obj (DerivedCategory.Q.obj K)).obj
          (DerivedCategory.Q.obj L))) (a + c) (b + d)
```

## Tag 066J, a lemma

[Tag 066J](https://stacks.math.columbia.edu/tag/066J) in the Stacks Project.

**`StacksDraft.TorAmplitude.hasTorAmplitudeIn_restrictScalars`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TorAmplitude/ChangeOfRings.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/TorAmplitude/ChangeOfRings.lean#L80).

> **Stacks 066J.** A complex of `B`-modules with Tor amplitude in `[a, b]` retains that
> Tor-amplitude bound after restriction of scalars along a flat ring map `A → B`.

```lean
theorem hasTorAmplitudeIn_restrictScalars
    (A : Type u) (B : Type v) [CommRing A] [CommRing B]
    [Algebra A B] [Module.Flat A B]
    (K : CochainComplex (ModuleCat.{w} B) ℤ) (a b : ℤ)
    (hK : ∃ E : CochainComplex (ModuleCat.{w} B) ℤ,
      StacksDraft.TorAmplitude.Termwise.IsComplexOfFlats E ∧ E.IsStrictlyGE a ∧ E.IsStrictlyLE b ∧
        Nonempty (DerivedCategory.Q.obj K ≅ DerivedCategory.Q.obj E)) :
    ∃ E : CochainComplex (ModuleCat.{w} A) ℤ,
      StacksDraft.TorAmplitude.Termwise.IsComplexOfFlats E ∧ E.IsStrictlyGE a ∧ E.IsStrictlyLE b ∧
        Nonempty ((DerivedCategory.Q.obj
          (((ModuleCat.restrictScalars.{w} (algebraMap A B)).mapHomologicalComplex
            (ComplexShape.up ℤ)).obj K) :
            DerivedCategory (ModuleCat.{w} A)) ≅
          DerivedCategory.Q.obj E)
```

## Tag 066K, a lemma

[Tag 066K](https://stacks.math.columbia.edu/tag/066K) in the Stacks Project.

**`StacksDraft.TorAmplitude.hasTorAmplitudeCanonicalLift_restrictScalars_of_torDimensionLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TorAmplitude/CompositionCanonical.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/TorAmplitude/CompositionCanonical.lean#L149).

> Let `f : A → B` be a map of commutative rings and let `K` be a complex of `B`-modules; the
> two rings and the carriers of `K` live in three independent universes. If `B` has Tor dimension
> at most `d` as an `A`-module, that is, if `B` placed in degree zero has Tor amplitude in
> `[-d, 0]` over `A`, then `K`, after restriction of scalars along `f`, has Tor amplitude in
> `[a - d, b]` over `A`.
>
> Tor amplitude is `HasTorAmplitudeCanonicalLift`, that is, Stacks 0652 at the canonical derived
> tensor product of Stacks 0BYI on the ring lifted into the ambient universe.

```lean
public theorem hasTorAmplitudeCanonicalLift_restrictScalars_of_torDimensionLE
    {A : Type u} {B : Type v} [CommRing A] [CommRing B] (f : A →+* B)
    (K : CochainComplex (ModuleCat.{w} B) ℤ) (a b d : ℤ)
    (hB : HasTorAmplitudeCanonicalLift.{u, v, w}
      ((DerivedCategory.singleFunctor (ModuleCat.{v} A) 0).obj
        ((ModuleCat.restrictScalars f).obj (ModuleCat.of B B))) (-d) 0)
    (hK : HasTorAmplitudeCanonicalLift.{v, w, u} (DerivedCategory.Q.obj K) a b) :
    HasTorAmplitudeCanonicalLift.{u, w, v}
      (DerivedCategory.Q.obj
        (((ModuleCat.restrictScalars.{w} f).mapHomologicalComplex (ComplexShape.up ℤ)).obj K))
      (a - d) b
```

## Tag 066L, a lemma

[Tag 066L](https://stacks.math.columbia.edu/tag/066L) in the Stacks Project.

**`StacksDraft.TorAmplitude.hasTorAmplitude_derivedExtendScalars`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TorAmplitude/BaseChange.lean, line 370](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/TorAmplitude/BaseChange.lean#L370).

> **Stacks 066L.** Let `A → B` be a map of commutative rings and let `K` be an object of
> `D(A)` with Tor amplitude in `[a, b]`. Then `K ⊗_A^L B` has Tor amplitude in `[a, b]` as an
> object of `D(B)`.
>
> The derived tensor products over `A` and over `B` are certified as in Stacks 0652, and derived
> extension of scalars is certified in the same style: `extendDerived` is equipped with a
> comparison map `extendComparison` to termwise extension of scalars making it the total left
> derived functor of the latter.

```lean
public theorem hasTorAmplitude_derivedExtendScalars {A B : Type u} [CommRing A] [CommRing B]
    [Algebra A B]
    (extendDerived : DerivedCategory (ModuleCat.{u} A) ⥤ DerivedCategory (ModuleCat.{u} B))
    (extendComparison : DerivedCategory.Q ⋙ extendDerived ⟶
      (ModuleCat.extendScalars (algebraMap A B)).mapHomologicalComplex (ComplexShape.up ℤ) ⋙
        DerivedCategory.Q)
    (extendIsLeftDerived : extendDerived.IsLeftDerivedFunctor extendComparison
      (HomologicalComplex.quasiIso (ModuleCat.{u} A) (ComplexShape.up ℤ)))
    (derivedTensorA : DerivedCategory (ModuleCat.{u} A) ⥤
      DerivedCategory (ModuleCat.{u} A) ⥤ DerivedCategory (ModuleCat.{u} A))
    (comparisonA : ∀ M : ModuleCat.{u} A,
      DerivedCategory.Q ⋙ derivedTensorA.flip.obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj M) ⟶
        (tensorModuleRight M).mapHomologicalComplex (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
    (isLeftDerivedA : ∀ M : ModuleCat.{u} A,
      (derivedTensorA.flip.obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj M)).IsLeftDerivedFunctor
        (comparisonA M)
        (HomologicalComplex.quasiIso (ModuleCat.{u} A) (ComplexShape.up ℤ)))
    (derivedTensorB : DerivedCategory (ModuleCat.{u} B) ⥤
      DerivedCategory (ModuleCat.{u} B) ⥤ DerivedCategory (ModuleCat.{u} B))
    (comparisonB : ∀ M : ModuleCat.{u} B,
      DerivedCategory.Q ⋙ derivedTensorB.flip.obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} B) 0).obj M) ⟶
        (tensorModuleRight M).mapHomologicalComplex (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
    (isLeftDerivedB : ∀ M : ModuleCat.{u} B,
      (derivedTensorB.flip.obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} B) 0).obj M)).IsLeftDerivedFunctor
        (comparisonB M)
        (HomologicalComplex.quasiIso (ModuleCat.{u} B) (ComplexShape.up ℤ)))
    (K : DerivedCategory (ModuleCat.{u} A)) (a b : ℤ)
    (hK : HasTorAmplitude derivedTensorA comparisonA isLeftDerivedA K a b) :
    HasTorAmplitude derivedTensorB comparisonB isLeftDerivedB (extendDerived.obj K) a b
```

## Tag 066M, a lemma

[Tag 066M](https://stacks.math.columbia.edu/tag/066M) in the Stacks Project.

**`StacksDraft.TorAmplitude.hasTorDimensionLECanonical_extendScalars_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TorAmplitude/CanonicalCertificate.lean, line 345](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/TorAmplitude/CanonicalCertificate.lean#L345).

> Let `f : A →+* B` be a flat homomorphism of commutative rings.  If the
> `A`-module `M` has Tor dimension at most `d`, then the `B`-module `B ⊗_A M` has Tor dimension at
> most `d`.  Both Tor dimensions are read at the canonical derived tensor product of the ring in
> question.

```lean
public theorem hasTorDimensionLECanonical_extendScalars_of_flat {A B : Type u} [CommRing A]
    [CommRing B] (f : A →+* B) (hf : f.Flat) (M : ModuleCat.{u} A) (d : ℕ)
    (hM : HasTorDimensionLECanonical A M d) :
    HasTorDimensionLECanonical B ((ModuleCat.extendScalars.{u, u, u} f).obj M) d
```

## Tag 0B67, a lemma

[Tag 0B67](https://stacks.math.columbia.edu/tag/0B67) in the Stacks Project.

**`StacksDraft.TorAmplitude.hasTorAmplitude_iff_localized_at_primes_iff_maximals`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TorAmplitude/Local.lean, line 636](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/TorAmplitude/Local.lean#L636).

> A complex of `B`-modules has Tor amplitude in `[a, b]` over `A` if and only if its localisation
> at every prime ideal `q` of `B` has Tor amplitude in `[a, b]` over `A_{q ∩ A}`; equivalently, it is
> enough to test this at every maximal ideal of `B`.

```lean
theorem hasTorAmplitude_iff_localized_at_primes_iff_maximals
    (A B : Type u) [CommRing A] [CommRing B] [Algebra A B]
    (K : CochainComplex (ModuleCat.{u} B) ℤ) (a b : ℤ) :
    (StacksDraft.TorAmplitude.FaithfullyFlat.HasTorAmplitude
        ((CochainComplex.restrictScalars (algebraMap A B)).obj K) a b ↔
      ∀ (q : Ideal B) [q.IsPrime], HasTorAmplitudeAt A K q a b) ∧
    ((∀ (q : Ideal B) [q.IsPrime], HasTorAmplitudeAt A K q a b) ↔
      ∀ (m : Ideal B) (hm : m.IsMaximal),
        letI : m.IsPrime := hm.isPrime
        HasTorAmplitudeAt A K m a b)
```

## Tag 066N, a lemma

[Tag 066N](https://stacks.math.columbia.edu/tag/066N) in the Stacks Project.

**`StacksDraft.TorAmplitude.hasTorAmplitude_of_localizationSpan`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TorAmplitude/Local.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/TorAmplitude/Local.lean#L147).

> If a complex has Tor amplitude in `[a, b]` after localization at every member of a set
> generating the unit ideal, then it has Tor amplitude in `[a, b]`.

```lean
theorem hasTorAmplitude_of_localizationSpan
    {R : Type u} [CommRing R] (s : Set R) (hs : Ideal.span s = ⊤)
    (K : CochainComplex (ModuleCat.{u} R) ℤ) (a b : ℤ)
    (hK : ∀ f : s, StacksDraft.TorAmplitude.FaithfullyFlat.HasTorAmplitude
      ((CochainComplex.extendScalars
        (algebraMap R (Localization.Away (f : R)))).obj K) a b) :
    StacksDraft.TorAmplitude.FaithfullyFlat.HasTorAmplitude K a b
```

## Tag 068S, a lemma

[Tag 068S](https://stacks.math.columbia.edu/tag/068S) in the Stacks Project.

**`StacksDraft.TorAmplitude.hasTorAmplitudeCanonical_of_faithfullyFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TorAmplitude/CanonicalCertificate.lean, line 358](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/TorAmplitude/CanonicalCertificate.lean#L358).

> Tor amplitude descends along a faithfully flat ring map `f : R →+* S`: if the base change of
> `K` along `f` has Tor amplitude in `[a, b]`, then so does `K`. Both sides are read at the
> canonical derived tensor products of the two rings lifted by `ULift` into the universe of the
> modules, and the base change is extension of scalars along the lifted ring map.

```lean
public theorem hasTorAmplitudeCanonical_of_faithfullyFlat
    {R : Type u} {S : Type v} [CommRing R] [CommRing S]
    (f : R →+* S) (hf : f.FaithfullyFlat)
    (K : CochainComplex (ModuleCat.{max u v w} (ULift.{max v w} R)) ℤ) (a b : ℤ)
    (h : HasTorAmplitudeCanonical (ULift.{max u w} S)
      (DerivedCategory.Q.obj
        ((CochainComplex.extendScalars (f.ulift.{max v w, max u w})).obj K)) a b) :
    HasTorAmplitudeCanonical (ULift.{max v w} R) (DerivedCategory.Q.obj K) a b
```

## Tag 0DJF, a lemma

[Tag 0DJF](https://stacks.math.columbia.edu/tag/0DJF) in the Stacks Project.

**`StacksDraft.TorAmplitude.FaithfullyFlat.hasTorAmplitudeIn_iff_extendScalars`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TorAmplitude/FaithfullyFlat.lean, line 1134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/TorAmplitude/FaithfullyFlat.lean#L1134).

> Let `R → A → B` be ring maps with `A → B` faithfully flat, and let `K ∈ D(A)`. Then, viewing
> both `K` and `K ⊗_A^L B` as objects of `D(R)` via restriction of scalars, `K` has tor-amplitude in
> `[a, b]` over `R` if and only if `K ⊗_A^L B` has tor-amplitude in `[a, b]` over `R`.

```lean
theorem hasTorAmplitudeIn_iff_extendScalars
    (R A B : Type u) [CommRing R] [CommRing A] [CommRing B]
    [Algebra R A] [Algebra A B] [Algebra R B] [IsScalarTower R A B]
    [Module.FaithfullyFlat A B]
    (K : CochainComplex (ModuleCat.{u} A) ℤ) (a b : ℤ) :
    HasTorAmplitude ((CochainComplex.restrictScalars (algebraMap R A)).obj K) a b ↔
      HasTorAmplitude ((CochainComplex.restrictScalars (algebraMap R B)).obj
        ((CochainComplex.extendScalars (algebraMap A B)).obj K)) a b
```

## Tag 066P, a lemma

[Tag 066P](https://stacks.math.columbia.edu/tag/066P) in the Stacks Project.

**`StacksDraft.TorAmplitude.torAmplitude_and_finiteTorDimension_of_globalDimension_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TorAmplitude/GlobalDimension.lean, line 331](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/TorAmplitude/GlobalDimension.lean#L331). References: SGA 6 I (5.9), “special case”; SGA 6 III (3.2), “special case”.

> **Stacks 066P.** Let `R` be a ring of global dimension at most `d`. Then
>
> 1. every `R`-module placed in degree `0` has Tor amplitude in `[-d, 0]`, i.e. Tor dimension at
>    most `d`;
> 2. a complex whose cohomology is concentrated in `[a, b]` has Tor amplitude in `[a - d, b]`;
> 3. a complex has finite Tor dimension if and only if it lies in the bounded derived
>    category.

```lean
public theorem torAmplitude_and_finiteTorDimension_of_globalDimension_le
    (R : Type u) [CommRing R] (d : ℕ) (hR : ringGlobalDimension R ≤ d) :
    (∀ M : ModuleCat.{u} R,
      StacksDraft.TorAmplitude.FaithfullyFlat.HasTorAmplitude
        ((CochainComplex.singleFunctor (ModuleCat.{u} R) 0).obj M) (-(d : ℤ)) 0) ∧
    (∀ (K : CochainComplex (ModuleCat.{u} R) ℤ) (a b : ℤ),
      (∀ i : ℤ, (i < a ∨ b < i) → IsZero (K.homology i)) →
        StacksDraft.TorAmplitude.FaithfullyFlat.HasTorAmplitude K (a - d) b) ∧
    (∀ K : CochainComplex (ModuleCat.{u} R) ℤ,
      (∃ a b : ℤ, StacksDraft.TorAmplitude.FaithfullyFlat.HasTorAmplitude K a b) ↔
        (DerivedCategory.TStructure.t (C := ModuleCat.{u} R)).bounded
          (DerivedCategory.Q.obj K))
```

## Tag 0H75, a lemma

[Tag 0H75](https://stacks.math.columbia.edu/tag/0H75) in the Stacks Project.

**`StacksDraft.TorAmplitude.hasTorAmplitudeIn_derivedExtensionScalars_certified_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TorAmplitude/NilpotentCertified.lean, line 418](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/TorAmplitude/NilpotentCertified.lean#L418).

> **Stacks 0H75.** Let `f : R' → R` be a surjective map of commutative rings whose kernel is a
> nilpotent ideal, and let `L` be the derived base change along `f`. For every object `K` of `D(R')`
> and every finite interval `[a, b]`, the object `L.obj K` has Tor amplitude in `[a, b]` if and only
> if `K` does.
>
> `L` is quantified over together with its comparison to termwise extension of scalars and the
> `Functor.IsLeftDerivedFunctor` certificate, which pins it down as *the* derived base change rather
> than an arbitrary functor. Each of the two derived tensor products is quantified as a
> `StacksDraft.TorAmplitude.CertifiedDerivedTensoring`: the bifunctor, its comparison with termwise
> tensoring by a module placed in degree zero, and the universal property making each `- ⊗ᴸ M[0]` the
> total left derived functor of `- ⊗ M`. That is exactly the datum Stacks 0652 reads Tor amplitude
> off, and no more; in particular neither the comparison at pairs of K-flat complexes nor exactness
> in the second variable is assumed.
>
> The universe of `R'`, the universe of `R` and the universe of the module carriers are independent:
> `R' : Type u`, `R : Type v`, and both rings' modules are read in `ModuleCat.{max u v w}`, as in the
> source statement. Neither ring is `ULift`ed in the statement.
>
> The proof moves both sides into the lifted rings, where the ring universe and the module universe
> coincide, by `hasTorAmplitude_iff_scalarLift` for the Tor amplitudes and
> `derivedExtensionLiftSquare` for the base change, and there applies
> `hasTorAmplitudeIn_derivedExtensionScalars_iff_sameUniverse` to the canonical derived tensor
> product of Stacks 0BYI.

```lean
public theorem hasTorAmplitudeIn_derivedExtensionScalars_certified_iff
    (hf : Function.Surjective f) (hnil : IsNilpotent (RingHom.ker f))
    (L : DerivedCategory (ModuleCat.{max u v w} R') ⥤ DerivedCategory (ModuleCat.{max u v w} R))
    (comparison : DerivedCategory.Q (C := ModuleCat.{max u v w} R') ⋙ L ⟶
      (ModuleCat.extendScalars.{u, v, max u v w} f).mapHomologicalComplex
          (ComplexShape.up ℤ) ⋙ DerivedCategory.Q (C := ModuleCat.{max u v w} R))
    [L.IsLeftDerivedFunctor comparison
      (HomologicalComplex.quasiIso (ModuleCat.{max u v w} R') (ComplexShape.up ℤ))]
    (D' : CertifiedDerivedTensoring.{u, max u v w} R')
    (D : CertifiedDerivedTensoring.{v, max u v w} R)
    (K : DerivedCategory (ModuleCat.{max u v w} R')) (a b : ℤ) :
    D.HasTorAmplitudeIn (L.obj K) a b ↔ D'.HasTorAmplitudeIn K a b
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.68, Tag 0651](https://stacks.math.columbia.edu/tag/0651)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
