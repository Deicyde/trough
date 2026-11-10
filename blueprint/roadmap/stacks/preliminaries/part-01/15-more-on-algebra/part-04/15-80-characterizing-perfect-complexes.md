---
declaration: section
origin: cited
lean: StacksDraft.Perfect.isPerfect_eq_triangEnvelope_singleton_regularModule, Stacks.MappingTelescope.isIso_colimHomComparison, StacksDraft.Perfect.isPerfect_iff_isCompactObject, StacksDraft.Perfect.isPerfect_of_isPerfect_mod_isNilpotent, StacksDraft.Perfect.isPerfect_derivedReduction_mul
statement: formalized
proof: formalized
---

# 15.80 Characterizing perfect complexes

Section 15.80 of the Stacks Project, [Tag 07LQ](https://stacks.math.columbia.edu/tag/07LQ). 5 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0ATI, a lemma

[Tag 0ATI](https://stacks.math.columbia.edu/tag/0ATI) in the Stacks Project.

**`StacksDraft.Perfect.isPerfect_eq_triangEnvelope_singleton_regularModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/Characterizing.lean, line 330](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Perfect/Characterizing.lean#L330).

> **Stacks 0ATI.** The perfect objects of `D(R)` form the smallest strictly full, saturated,
> triangulated subcategory containing the regular module `R` in degree zero. Equivalently, `R[0]`
> is a classical generator of the perfect derived category.

```lean
theorem isPerfect_eq_triangEnvelope_singleton_regularModule {R : Type u} [Ring R] :
    (IsPerfect : ObjectProperty (DerivedCategory (ModuleCat.{u} R))) =
      (ObjectProperty.singleton
        ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj
          (ModuleCat.of R R))).triangEnvelope
```

## Tag 07LR, a lemma

[Tag 07LR](https://stacks.math.columbia.edu/tag/07LR) in the Stacks Project.

**`Stacks.MappingTelescope.isIso_colimHomComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedCategory/HomColimit.lean, line 451](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/DerivedCategory/HomColimit.lean#L451).

> **Stacks 07LR**.
> Let `R` be a ring and let `K ∈ D(R)` be such that for every sequence `(E_n)` of objects of `D(R)`
> with a coproduct, the canonical map `⨁_n Hom_{D(R)}(K, E_n) → Hom_{D(R)}(K, ⨁_n E_n)` is an
> isomorphism. Then for every system of complexes `(L_n, t_n)` over `ℕ` with termwise colimit `L`,
> the canonical map `colim_n Hom_{D(R)}(K, L_n) → Hom_{D(R)}(K, L)` is an isomorphism.

```lean
theorem isIso_colimHomComparison (K : DMod R) (hK : CommutesWithCountableCoproducts K)
    (L : System R) :
    IsIso (colimHomComparison L K)
```

## Tag 07LT, a proposition

[Tag 07LT](https://stacks.math.columbia.edu/tag/07LT) in the Stacks Project.

**`StacksDraft.Perfect.isPerfect_iff_isCompactObject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/Characterizing.lean, line 1129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Perfect/Characterizing.lean#L1129).

> **Stacks 07LT.** An object of the derived category of modules over a ring is perfect if and
> only if it is compact. Perfectness is thus intrinsic to the triangulated category `D(R)` with its
> coproducts, referring neither to a representing complex nor to the ring.

```lean
theorem isPerfect_iff_isCompactObject
    {R : Type u} [Ring R] (K : DerivedCategory (ModuleCat.{u} R)) :
    IsPerfect K ↔ IsCompactObject.{u} K
```

## Tag 07LU, a lemma

[Tag 07LU](https://stacks.math.columbia.edu/tag/07LU) in the Stacks Project.

**`StacksDraft.Perfect.isPerfect_of_isPerfect_mod_isNilpotent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/NilpotentLifting.lean, line 884](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Perfect/NilpotentLifting.lean#L884).

> **Stacks 07LU.** An object of `D(R)` whose derived reduction modulo a nilpotent ideal `I` is
> perfect is itself perfect.
>
> A bounded complex of finite projective `R ⧸ I`-modules representing the reduction lifts, by
> [stacks 09AR], to a bounded above complex `P` of projective `R`-modules representing `K`. Each
> term of `P` is finite because its reduction is, by Nakayama for a nilpotent ideal
> (`finite_of_finite_quotient_of_isNilpotent`), and `P` vanishes below the lower bound of the given
> complex because a module with vanishing reduction modulo a nilpotent ideal vanishes.

```lean
public theorem isPerfect_of_isPerfect_mod_isNilpotent
    {R : Type u} [CommRing R] (I : Ideal R)
    (K : DerivedCategory (ModuleCat.{max v u} R))
    (hK : IsPerfect
      ((totalDerivedExtensionScalars.{u, u, v} (Ideal.Quotient.mk I)).functor.obj K))
    (hI : IsNilpotent I) :
    IsPerfect K
```

## Tag 09AS, a lemma

[Tag 09AS](https://stacks.math.columbia.edu/tag/09AS) in the Stacks Project.

**`StacksDraft.Perfect.isPerfect_derivedReduction_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/ProductOfIdeals.lean, line 621](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Perfect/ProductOfIdeals.lean#L621).

> **Stacks 09AS.** Let `I` and `J` be ideals of a commutative ring `R` and let `K` be an object
> of the derived category of `R`-modules. If the derived reductions of `K` modulo `I` and modulo `J`
> are both perfect, then so is the derived reduction of `K` modulo `I * J`.
>
> Perfectness modulo `I ∩ J` follows from `isPerfect_of_isPerfect_reductions`, applied over the ring
> `R/(I ∩ J)` where the images of `I` and of `J` meet in zero; and `R/(I * J) → R/(I ∩ J)` is
> surjective with nilpotent kernel, so perfectness descends along it.

```lean
theorem isPerfect_derivedReduction_mul (I J : Ideal R)
    (K : DerivedCategory (ModuleCat.{max u v} R))
    (hI : IsPerfect
      ((totalDerivedExtensionScalars.{u, u, v} (Ideal.Quotient.mk I)).functor.obj K))
    (hJ : IsPerfect
      ((totalDerivedExtensionScalars.{u, u, v} (Ideal.Quotient.mk J)).functor.obj K)) :
    IsPerfect
      ((totalDerivedExtensionScalars.{u, u, v} (Ideal.Quotient.mk (I * J))).functor.obj K)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.80, Tag 07LQ](https://stacks.math.columbia.edu/tag/07LQ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
