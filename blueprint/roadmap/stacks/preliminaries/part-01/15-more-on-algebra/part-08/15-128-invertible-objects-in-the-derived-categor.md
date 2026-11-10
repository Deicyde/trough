---
declaration: section
origin: cited
lean: DerivedCategory.Invertible.derivedCategory_symmetricMonoidalCategory, exists_subcomplex_bounded_finiteFree, DerivedCategory.Invertible.isPerfect_iff_exists_leftDual, DerivedCategory.Invertible.isInvertible_iff_locallyShiftedUnit
statement: formalized
proof: formalized
---

# 15.128 Invertible objects in the derived category

Section 15.128 of the Stacks Project, [Tag 0FNP](https://stacks.math.columbia.edu/tag/0FNP). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FNQ, a lemma

[Tag 0FNQ](https://stacks.math.columbia.edu/tag/0FNQ) in the Stacks Project.

**`DerivedCategory.Invertible.derivedCategory_symmetricMonoidalCategory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedCategory/Monoidal/Basic.lean, line 471](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/DerivedCategory/Monoidal/Basic.lean#L471).

> **Stacks 0FNQ.** The derived category of modules over a commutative ring is symmetric
> monoidal under derived tensor product. Under the canonical comparison with tensor products of
> K-flat representatives, its associator is induced by the ordinary associator of complexes, and
> its braiding is the canonical Koszul symmetry.

```lean
public theorem derivedCategory_symmetricMonoidalCategory (R : Type u) [CommRing R] :
    let D := DerivedCategory (ModuleCat.{u} R)
    let C := CochainComplex (ModuleCat.{u} R) ℤ
    let Q := DerivedCategory.Q (C := ModuleCat.{u} R)
    let T := CochainComplex.DerivedTensor.canonicalSymmetricDerivedTensorProduct R
    ∃ m : MonoidalCategory D,
      letI := m
      ∃ s : SymmetricCategory D,
        letI := s
        ∃ e : curriedTensor D ≅ T.tensorProduct.tensor,
          (∀ K L : D,
              (β_ K L).hom ≫ ((e.app L).app K).hom =
                ((e.app K).app L).hom ≫ ((T.braiding.iso.app K).app L).hom) ∧
            ∀ (K L M : C) (hK : K.KFlat) (hL : L.KFlat) (hM : M.KFlat)
                (hKL : (K ⊗ L).KFlat) (hLM : (L ⊗ M).KFlat),
              let comparison : ∀ (A B : C), A.KFlat → B.KFlat →
                  (Q.obj A ⊗ Q.obj B ⟶ Q.obj (A ⊗ B)) :=
                fun A B hA hB =>
                  ((e.app (Q.obj A)).app (Q.obj B)).hom ≫
                    (T.tensorProduct.comparison A B hA hB).hom
              (α_ (Q.obj K) (Q.obj L) (Q.obj M)).hom ≫
                    (Q.obj K ◁ comparison L M hL hM) ≫
                    comparison K (L ⊗ M) hK hLM =
                ((comparison K L hK hL :
                    Q.obj K ⊗ Q.obj L ⟶ Q.obj (K ⊗ L)) ▷ Q.obj M) ≫
                  comparison (K ⊗ L) M hKL hM ≫
                  Q.map (HomologicalComplex.associator K L M).hom
```

## Tag 0FNR, a lemma

[Tag 0FNR](https://stacks.math.columbia.edu/tag/0FNR) in the Stacks Project.

**`exists_subcomplex_bounded_finiteFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/FiniteFreeSubcomplex.lean, line 357](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/FiniteFreeSubcomplex.lean#L357).

> **Stacks Tag 0FNR (Lemma 15.128.2).**
> Let `R` be a ring and let `F` be a bounded above complex of free `R`-modules. Given a finite
> family of pairs `(n i, f i)` (indexed by `i : Fin N`), with `n i ∈ ℤ` and `f i ∈ F^{n i}`,
> there exists a subcomplex `G ⊆ F` such that:
> 1. `f i ∈ G^{n i}` for every `i` (i.e. `G` contains all the `f i`);
> 2. `G` is bounded; and
> 3. `G` consists of finite free `R`-modules.

```lean
theorem exists_subcomplex_bounded_finiteFree (F : ZComplex R) (hFa : F.BoundedAbove) (hFfree :
  F.IsFree)
    {N : ℕ} (n : Fin N → ℤ) (f : ∀ i, F.obj (n i)) :
    ∃ G : F.Subcomplex,
      (∀ i, f i ∈ G.carrier (n i)) ∧ G.Bounded ∧ G.FiniteFree
```

## Tag 0FNS, a lemma

[Tag 0FNS](https://stacks.math.columbia.edu/tag/0FNS) in the Stacks Project.

**`DerivedCategory.Invertible.isPerfect_iff_exists_leftDual`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedCategory/Monoidal/Dual.lean, line 1161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/DerivedCategory/Monoidal/Dual.lean#L1161).

> **Stacks 0FNS.** An object of the derived category has a left dual exactly when it is perfect.
> For a perfect object the derived dual `RHom(M, R)` is a left dual, and every other left dual is
> isomorphic to it.

```lean
public theorem isPerfect_iff_exists_leftDual
    (M : DerivedCategory (ModuleCat.{max u v} (ULift.{v} R))) :
    ((∃ N : DerivedCategory (ModuleCat.{max u v} (ULift.{v} R)),
        Nonempty (DerivedLeftDualPairing M N)) ↔
        IsPerfect M) ∧
      (IsPerfect M →
        Nonempty (DerivedLeftDualPairing M (derivedDual M))) ∧
      (∀ (N : DerivedCategory (ModuleCat.{max u v} (ULift.{v} R))),
        DerivedLeftDualPairing M N →
        Nonempty (N ≅ derivedDual M))
```

## Tag 0FNT, a lemma

[Tag 0FNT](https://stacks.math.columbia.edu/tag/0FNT) in the Stacks Project.

**`DerivedCategory.Invertible.isInvertible_iff_locallyShiftedUnit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedCategory/Monoidal/Invertible.lean, line 1096](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/DerivedCategory/Monoidal/Invertible.lean#L1096).

> **Stacks 0FNT.** A derived object is invertible if and only if it is locally a shift of the
> ring. In that case it is perfect, is the direct sum of its cohomology modules, every cohomology
> module is finite projective, and those modules are invertible on the factors of a finite product
> decomposition of the ring.

```lean
public theorem isInvertible_iff_locallyShiftedUnit
    (M : DerivedCategory (ModuleCat.{u} R)) :
    let derivedMonoidal := (derivedCategory_symmetricMonoidalCategory R).choose
    letI := derivedMonoidal
    (MonoidalCategory.IsInvertible M ↔ IsLocallyShiftedUnit M) ∧
      (MonoidalCategory.IsInvertible M →
        StacksDraft.Perfect.IsPerfect M ∧
          SplitsAsCohomology M ∧
          (∀ n : ℤ,
            Module.Finite R
                ((DerivedCategory.homologyFunctor (ModuleCat.{u} R) n).obj M) ∧
              Module.Projective R
                ((DerivedCategory.homologyFunctor (ModuleCat.{u} R) n).obj M)) ∧
          HasInvertibleCohomologyDecomposition M)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.128, Tag 0FNP](https://stacks.math.columbia.edu/tag/0FNP)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
