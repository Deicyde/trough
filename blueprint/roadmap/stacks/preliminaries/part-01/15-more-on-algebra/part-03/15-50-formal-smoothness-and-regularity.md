---
declaration: section
origin: cited
lean: exists_derivation_extension_of_formallySmoothNAdic, isRegularRingHom_flat_geometricallyRegular_specialFiber_formallySmooth_tfae, isRegularRingHom_flat_geometricallyRegular_specialFiber_formallySmooth_tfae_0h7u
statement: formalized
proof: formalized
---

# 15.50 Formal smoothness and regularity

Section 15.50 of the Stacks Project, [Tag 07PK](https://stacks.math.columbia.edu/tag/07PK). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07PL, a lemma

[Tag 07PL](https://stacks.math.columbia.edu/tag/07PL) in the Stacks Project.

**`exists_derivation_extension_of_formallySmoothNAdic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FormallySmooth/Regularity.lean, line 274](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/FormallySmooth/Regularity.lean#L274).

> A derivation of a Noetherian local ring extends across a local homomorphism to a complete
> Noetherian local ring that is formally smooth for its maximal-ideal-adic topology.

```lean
public theorem exists_derivation_extension_of_formallySmoothNAdic.{u, v}
    {A : Type u} {B : Type v}
    [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    [CommRing B] [IsNoetherianRing B] [IsLocalRing B]
    (f : A →+* B) [IsLocalHom f]
    [IsAdicComplete (IsLocalRing.maximalIdeal B) B]
    (hfs : RingHom.FormallySmoothNAdic.{max u v, u, v} f (IsLocalRing.maximalIdeal B))
    (D : Derivation ℤ A A) :
    ∃ D' : Derivation ℤ B B, ∀ a : A, D' (f a) = f (D a)
```

## Tag 07PM, a proposition

[Tag 07PM](https://stacks.math.columbia.edu/tag/07PM) in the Stacks Project.

**`isRegularRingHom_flat_geometricallyRegular_specialFiber_formallySmooth_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FormallySmooth/Regularity.lean, line 1018](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/FormallySmooth/Regularity.lean#L1018). References: EGA 0 (19.7.1), “complete case”; EGA 0 (19.0.2), “I, complete case”; EGA IV (7.5.4), “(i)”; EGA IV (7.5.3), “(iv), special case”; SGA 1 III (1.7), “Noetherian complete case”; SGA 1 III (1.3), “special case”.

> Let `f : A → B` be a local homomorphism of Noetherian complete local rings, let `k` be
> the residue field of `A`, and let `B̄ = k ⊗[A] B` be the special fibre. The following are
> equivalent:
>
> 1. `f` is regular;
> 2. `f` is flat and `B̄` is geometrically regular over `k`;
> 3. `f` is flat and `k → B̄` is formally smooth for the maximal-ideal-adic topology;
> 4. `f` is formally smooth for the maximal-ideal-adic topology on `B`.

```lean
public theorem isRegularRingHom_flat_geometricallyRegular_specialFiber_formallySmooth_tfae
    {A : Type u} {B : Type v}
    [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    [IsAdicComplete (maximalIdeal A) A]
    [CommRing B] [IsNoetherianRing B] [IsLocalRing B]
    [IsAdicComplete (maximalIdeal B) B]
    (f : A →+* B) [IsLocalHom f] :
    letI : Algebra A B := f.toAlgebra
    let k := ResidueField A
    let Bbar := k ⊗[A] B
    List.TFAE [
      IsRegularRingHom f,
      Module.Flat A B ∧ Algebra.IsGeometricallyRegular k Bbar,
      Module.Flat A B ∧
        RingHom.FormallySmoothNAdic.{max u v}
          (algebraMap k Bbar) (maximalIdeal Bbar),
      RingHom.FormallySmoothNAdic.{max u v} f (maximalIdeal B)]
```

## Tag 0H7U, a theorem

[Tag 0H7U](https://stacks.math.columbia.edu/tag/0H7U) in the Stacks Project.

**`isRegularRingHom_flat_geometricallyRegular_specialFiber_formallySmooth_tfae_0h7u`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FormallySmooth/Regularity.lean, line 1271](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/FormallySmooth/Regularity.lean#L1271). References: EGA 0 (19.0.2), “I, A→A^∧ regular”; EGA 0 (19.7.1), “A → A^ regular”; EGA IV (7.5.4), “(i)”; EGA IV (7.5.3), “(iv), special case”; SGA 1 III (1.3), “special case”.

> Let `f : A → B` be a local homomorphism of Noetherian local rings and assume that the
> canonical map from `A` to its maximal-ideal-adic completion is regular. Let `k` be the residue
> field of `A` and let `B̄ = k ⊗[A] B` be the special fibre. The following are equivalent:
>
> 1. `f` is regular;
> 2. `f` is flat and `B̄` is geometrically regular over `k`;
> 3. `f` is flat and `k → B̄` is formally smooth for the maximal-ideal-adic topology;
> 4. `f` is formally smooth for the maximal-ideal-adic topology on `B`.

```lean
public theorem isRegularRingHom_flat_geometricallyRegular_specialFiber_formallySmooth_tfae_0h7u
    {A : Type u} {B : Type v}
    [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    [CommRing B] [IsNoetherianRing B] [IsLocalRing B]
    (f : A →+* B) [IsLocalHom f]
    (hA : letI : WithIdeal A := ⟨maximalIdeal A⟩
      IsRegularRingHom
        (Completion.coeRingHom : A →+* Completion A)) :
    letI : Algebra A B := f.toAlgebra
    let k := ResidueField A
    let Bbar := k ⊗[A] B
    List.TFAE [
      IsRegularRingHom f,
      Module.Flat A B ∧ Algebra.IsGeometricallyRegular k Bbar,
      Module.Flat A B ∧
        RingHom.FormallySmoothNAdic.{max u v}
          (algebraMap k Bbar) (maximalIdeal Bbar),
      RingHom.FormallySmoothNAdic.{max u v} f (maximalIdeal B)]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.50, Tag 07PK](https://stacks.math.columbia.edu/tag/07PK)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
