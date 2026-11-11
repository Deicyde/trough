---
declaration: section
origin: cited
lean: Dualizing.isGorensteinRing_tensorProduct_of_essFiniteType_fieldExtension, Dualizing.gorensteinProperty_localization, Dualizing.gorensteinProperty_regularAscent, Dualizing.gorensteinProperty_faithfullyFlatDescent, Dualizing.gorensteinProperty_groundFieldExtension, Dualizing.gorensteinTarget_satisfies_formalFiberAxioms, Dualizing.IsGorensteinRing, Dualizing.isGorensteinRing_formalFibre_of_isDualizingComplex
statement: formalized
proof: formalized
---

# 47.23 Formal fibres

Section 47.23 of the Stacks Project, [Tag 0BJM](https://stacks.math.columbia.edu/tag/0BJM). 3 tags here are carried by 13 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BJN, a lemma

[Tag 0BJN](https://stacks.math.columbia.edu/tag/0BJN) in the Stacks Project.

**`Dualizing.isGorensteinRing_tensorProduct_of_essFiniteType_fieldExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/GorensteinFieldExtension.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/GorensteinFieldExtension.lean#L80). The attribute's comment: “gorenstein\_field\_extension”.

> **Stacks Project, Tag 0BJN, clause (A).** Let `k` be a field, `R` a Noetherian `k`-algebra and
> `K/k` an extension of fields which is finitely generated as a field extension. If `R` is
> Gorenstein, then `R ⊗_k K` is Gorenstein.
>
> The extension `K/k` is a localization of a global complete intersection `C` over `k`; base
> changing `C` along `k → R` gives a relative global complete intersection `R → R ⊗_k C`, so
> `R ⊗_k C` is Gorenstein by Tag 0DWA, and `R ⊗_k K` is a localization of `R ⊗_k C`.

```lean
public theorem isGorensteinRing_tensorProduct_of_essFiniteType_fieldExtension
    {k : Type u} {R : Type v} {K : Type w}
    [Field k] [CommRing R] [Field K] [Algebra k R] [Algebra k K]
    [IsNoetherianRing R] [Algebra.EssFiniteType k K]
    (hR : IsGorensteinRing R) :
    letI : IsNoetherianRing (R ⊗[k] K) :=
      Algebra.EssFiniteType.isNoetherianRing R (R ⊗[k] K)
    IsGorensteinRing (R ⊗[k] K)
```

**`Dualizing.gorensteinProperty_localization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/GorensteinFormalFibreAxioms.lean, line 198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/GorensteinFormalFibreAxioms.lean#L198). The attribute's comment: “(B)”.

> **Stacks Project, Tag 0BJN, clause (B).** The property of a map from a field to a Noetherian
> ring that its target is Gorenstein can be checked after localizing at every prime.

```lean
public theorem gorensteinProperty_localization (P : RingMapProperty.{u, u})
    (hP : ∀ (k R : Type u) [Field k] [CommRing R] [Algebra k R] [IsNoetherianRing R],
      P (algebraMap k R) ↔ IsGorensteinRing R) :
    ∀ (k R : Type u) [Field k] [CommRing R] [Algebra k R] [IsNoetherianRing R],
      (∀ p : PrimeSpectrum R, P (algebraMap k (Localization.AtPrime p.asIdeal))) ↔
        P (algebraMap k R)
```

**`Dualizing.gorensteinProperty_regularAscent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/GorensteinFormalFibreAxioms.lean, line 211](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/GorensteinFormalFibreAxioms.lean#L211). The attribute's comment: “(C)”.

> **Stacks Project, Tag 0BJN, clause (C).** For flat maps `A → B → C` of Noetherian rings with
> `B → C` regular, if every fibre of `A → B` is Gorenstein then so is every fibre of `A → C`.

```lean
public theorem gorensteinProperty_regularAscent (P : RingMapProperty.{u, u})
    (hP : ∀ (k R : Type u) [Field k] [CommRing R] [Algebra k R] [IsNoetherianRing R],
      P (algebraMap k R) ↔ IsGorensteinRing R) :
    ∀ (A B C : Type u) [CommRing A] [CommRing B] [CommRing C]
      [Algebra A B] [Algebra B C] [Algebra A C] [IsScalarTower A B C]
      [IsNoetherianRing A] [IsNoetherianRing B] [IsNoetherianRing C]
      [Module.Flat A B] [Module.Flat B C],
      (∀ p : PrimeSpectrum A, P (algebraMap p.asIdeal.ResidueField (p.asIdeal.Fiber B))) →
      (∀ q : PrimeSpectrum B,
        Algebra.IsGeometricallyRegular q.asIdeal.ResidueField (q.asIdeal.Fiber C)) →
      ∀ p : PrimeSpectrum A, P (algebraMap p.asIdeal.ResidueField (p.asIdeal.Fiber C))
```

**`Dualizing.gorensteinProperty_faithfullyFlatDescent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/GorensteinFormalFibreAxioms.lean, line 268](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/GorensteinFormalFibreAxioms.lean#L268). The attribute's comment: “(D)”.

> **Stacks Project, Tag 0BJN, clause (D).** For flat maps `A → B → C` of Noetherian rings with
> `B → C` faithfully flat, if every fibre of `A → C` is Gorenstein then so is every fibre of
> `A → B`.

```lean
public theorem gorensteinProperty_faithfullyFlatDescent (P : RingMapProperty.{u, u})
    (hP : ∀ (k R : Type u) [Field k] [CommRing R] [Algebra k R] [IsNoetherianRing R],
      P (algebraMap k R) ↔ IsGorensteinRing R) :
    ∀ (A B C : Type u) [CommRing A] [CommRing B] [CommRing C]
      [Algebra A B] [Algebra B C] [Algebra A C] [IsScalarTower A B C]
      [IsNoetherianRing A] [IsNoetherianRing B] [IsNoetherianRing C]
      [Module.Flat A B] [Module.FaithfullyFlat B C],
      (∀ p : PrimeSpectrum A, P (algebraMap p.asIdeal.ResidueField (p.asIdeal.Fiber C))) →
        ∀ p : PrimeSpectrum A, P (algebraMap p.asIdeal.ResidueField (p.asIdeal.Fiber B))
```

**`Dualizing.gorensteinProperty_groundFieldExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/GorensteinFormalFibreAxioms.lean, line 295](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/GorensteinFormalFibreAxioms.lean#L295). The attribute's comment: “(E)”.

> **Stacks Project, Tag 0BJN, clause (E).** Gorensteinness of the target is unchanged when the
> ground field is replaced by a separable algebraic extension of it inside the target: the
> condition does not refer to the ground field.

```lean
public theorem gorensteinProperty_groundFieldExtension (P : RingMapProperty.{u, u})
    (hP : ∀ (k R : Type u) [Field k] [CommRing R] [Algebra k R] [IsNoetherianRing R],
      P (algebraMap k R) ↔ IsGorensteinRing R) :
    ∀ (k K R : Type u) [Field k] [Field K] [CommRing R]
      [Algebra k K] [Algebra k R] [Algebra K R] [IsScalarTower k K R]
      [IsNoetherianRing R] [Algebra.IsAlgebraic k K] [Algebra.IsSeparable k K],
      P (algebraMap k R) → P (algebraMap K R)
```

**`Dualizing.gorensteinTarget_satisfies_formalFiberAxioms`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/GorensteinFormalFibreAxioms.lean, line 371](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/GorensteinFormalFibreAxioms.lean#L371). The attribute's comment: “all five clauses conjoined, stated through the `RingMapProperty` interface at the concrete property `Dualizing.gorensteinTarget`, whose value on a map is Gorensteinness of the target together with the Noetherian structure that Gorensteinness presupposes”.

> **Stacks Project, Tag 0BJN.** Gorensteinness of the target of a map from a field to a
> Noetherian ring satisfies properties (A)--(E) of [Stacks, Tag 0BIR]: it is preserved by finitely
> generated field extension of the ground field, is detected by the localizations at the primes of
> the target, passes through a composition of flat maps whose second map is regular, descends
> through a faithfully flat second map, and is unchanged upon replacing the ground field by a
> separable algebraic extension of it inside the target. Gorensteinness of the target is the
> property `Dualizing.gorensteinTarget`.

```lean
public theorem gorensteinTarget_satisfies_formalFiberAxioms :
    (∀ (k K R : Type u) [Field k] [Field K] [CommRing R] [Algebra k K]
      [Algebra k R] [IsNoetherianRing R] [Algebra.EssFiniteType k K],
      gorensteinTarget.{u} (algebraMap k R) →
        gorensteinTarget.{u}
          (Algebra.TensorProduct.includeRight (R := k) (A := R) (B := K)).toRingHom) ∧
    (∀ (k R : Type u) [Field k] [CommRing R] [Algebra k R] [IsNoetherianRing R],
      (∀ p : PrimeSpectrum R,
          gorensteinTarget.{u} (algebraMap k (Localization.AtPrime p.asIdeal))) ↔
        gorensteinTarget.{u} (algebraMap k R)) ∧
    (∀ (A B C : Type u) [CommRing A] [CommRing B] [CommRing C]
      [Algebra A B] [Algebra B C] [Algebra A C] [IsScalarTower A B C]
      [IsNoetherianRing A] [IsNoetherianRing B] [IsNoetherianRing C]
      [Module.Flat A B] [Module.Flat B C],
      (∀ p : PrimeSpectrum A,
        gorensteinTarget.{u} (algebraMap p.asIdeal.ResidueField (p.asIdeal.Fiber B))) →
      (∀ q : PrimeSpectrum B,
        Algebra.IsGeometricallyRegular q.asIdeal.ResidueField (q.asIdeal.Fiber C)) →
      ∀ p : PrimeSpectrum A,
        gorensteinTarget.{u} (algebraMap p.asIdeal.ResidueField (p.asIdeal.Fiber C))) ∧
    (∀ (A B C : Type u) [CommRing A] [CommRing B] [CommRing C]
      [Algebra A B] [Algebra B C] [Algebra A C] [IsScalarTower A B C]
      [IsNoetherianRing A] [IsNoetherianRing B] [IsNoetherianRing C]
      [Module.Flat A B] [Module.FaithfullyFlat B C],
      (∀ p : PrimeSpectrum A,
        gorensteinTarget.{u} (algebraMap p.asIdeal.ResidueField (p.asIdeal.Fiber C))) →
        ∀ p : PrimeSpectrum A,
          gorensteinTarget.{u} (algebraMap p.asIdeal.ResidueField (p.asIdeal.Fiber B))) ∧
    (∀ (k K R : Type u) [Field k] [Field K] [CommRing R]
      [Algebra k K] [Algebra k R] [Algebra K R] [IsScalarTower k K R]
      [IsNoetherianRing R] [Algebra.IsAlgebraic k K] [Algebra.IsSeparable k K],
      gorensteinTarget.{u} (algebraMap k R) → gorensteinTarget.{u} (algebraMap K R))
```

Declarations registered for the tag:

- [`Dualizing.IsGorensteinRing`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/Gorenstein.lean#L69), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/RingTheory/Dualizing/FormalFibre.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/FormalFibre.lean#L62) (StacksFrontier): “gorenstein\_local and gorenstein\_ground\_field: this predicate is defined by the condition at every prime localization and takes no ground field as input”.

## Tag 0AWY, a lemma

[Tag 0AWY](https://stacks.math.columbia.edu/tag/0AWY) in the Stacks Project.

**`Dualizing.isGorensteinRing_formalFibre_of_isDualizingComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/GorensteinFormalFibres.lean, line 287](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/GorensteinFormalFibres.lean#L287).

> **Stacks Project, Tag 0AWY.** Every formal fibre of a Noetherian local ring admitting a
> dualizing complex is Gorenstein.

```lean
theorem isGorensteinRing_formalFibre_of_isDualizingComplex
    (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (K : DerivedCategory (ModuleCat.{u} A)) (hK : IsDualizingComplex K)
    (p : Ideal A) [p.IsPrime] :
    ∃ h : IsNoetherianRing (AdicCompletion (maximalIdeal A) A ⊗[A] p.ResidueField),
      @IsGorensteinRing (AdicCompletion (maximalIdeal A) A ⊗[A] p.ResidueField)
        inferInstance h
```

## Tag 0BJP, a lemma

[Tag 0BJP](https://stacks.math.columbia.edu/tag/0BJP) in the Stacks Project.

**`localCompleteIntersectionProperty_fieldExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCompleteIntersection/FormalFibreAxioms.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCompleteIntersection/FormalFibreAxioms.lean#L132). The attribute's comment: “(A)”.

> **Stacks Project, Tag 0BJP, clause (A).** Being a local complete intersection is preserved by
> base change along a finitely generated extension of the ground field.

```lean
public theorem localCompleteIntersectionProperty_fieldExtension (P : RingMapProperty.{u, u})
    (hP : ∀ (k R : Type u) [Field k] [CommRing R] [Algebra k R] [IsNoetherianRing R],
      P (algebraMap k R) ↔ IsLocalCompleteIntersectionRing R) :
    ∀ (k K R : Type u) [Field k] [Field K] [CommRing R] [Algebra k K]
      [Algebra k R] [IsNoetherianRing R] [Algebra.EssFiniteType k K],
      P (algebraMap k R) →
        P (Algebra.TensorProduct.includeRight (R := k) (A := R) (B := K)).toRingHom
```

**`localCompleteIntersectionProperty_localization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCompleteIntersection/FormalFibreAxioms.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCompleteIntersection/FormalFibreAxioms.lean#L150). The attribute's comment: “(B)”.

> **Stacks Project, Tag 0BJP, clause (B).** Being a local complete intersection can be checked
> after localizing at every prime.

```lean
public theorem localCompleteIntersectionProperty_localization (P : RingMapProperty.{u, u})
    (hP : ∀ (k R : Type u) [Field k] [CommRing R] [Algebra k R] [IsNoetherianRing R],
      P (algebraMap k R) ↔ IsLocalCompleteIntersectionRing R) :
    ∀ (k R : Type u) [Field k] [CommRing R] [Algebra k R] [IsNoetherianRing R],
      (∀ p : PrimeSpectrum R, P (algebraMap k (Localization.AtPrime p.asIdeal))) ↔
        P (algebraMap k R)
```

**`localCompleteIntersectionProperty_regularAscent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCompleteIntersection/FormalFibreAxioms.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCompleteIntersection/FormalFibreAxioms.lean#L172). The attribute's comment: “(C)”.

> **Stacks Project, Tag 0BJP, clause (C).** For flat maps `A → B → C` of Noetherian rings with
> `B → C` regular, if every fibre of `A → B` is a local complete intersection then so is every
> fibre of `A → C`.
>
> The fibre of `A → C` at a prime `𝔭` is the base change `D = (κ(𝔭) ⊗_A B) ⊗_B C` of the fibre of
> `A → B` along `B → C`, which is flat, so
> `LocalCompleteIntersection.isLocalCompleteIntersectionRing_of_flat_of_fiber` reduces the claim to
> the fibres of `κ(𝔭) ⊗_A B → D`. At a prime `Q` of `κ(𝔭) ⊗_A B` lying over `𝔮 ⊆ B` that fibre is
> `κ(Q) ⊗_{κ(𝔮)} (κ(𝔮) ⊗_B C)`; the extension `κ(𝔮) → κ(Q)` is bijective, so the geometric
> regularity of `κ(𝔮) → κ(𝔮) ⊗_B C` makes it regular, hence a local complete intersection.

```lean
public theorem localCompleteIntersectionProperty_regularAscent (P : RingMapProperty.{u, u})
    (hP : ∀ (k R : Type u) [Field k] [CommRing R] [Algebra k R] [IsNoetherianRing R],
      P (algebraMap k R) ↔ IsLocalCompleteIntersectionRing R) :
    ∀ (A B C : Type u) [CommRing A] [CommRing B] [CommRing C]
      [Algebra A B] [Algebra B C] [Algebra A C] [IsScalarTower A B C]
      [IsNoetherianRing A] [IsNoetherianRing B] [IsNoetherianRing C]
      [Module.Flat A B] [Module.Flat B C],
      (∀ p : PrimeSpectrum A, P (algebraMap p.asIdeal.ResidueField (p.asIdeal.Fiber B))) →
      (∀ q : PrimeSpectrum B,
        Algebra.IsGeometricallyRegular q.asIdeal.ResidueField (q.asIdeal.Fiber C)) →
      ∀ p : PrimeSpectrum A, P (algebraMap p.asIdeal.ResidueField (p.asIdeal.Fiber C))
```

**`localCompleteIntersectionProperty_faithfullyFlatDescent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCompleteIntersection/FormalFibreAxioms.lean, line 237](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCompleteIntersection/FormalFibreAxioms.lean#L237). The attribute's comment: “(D)”.

> **Stacks Project, Tag 0BJP, clause (D).** For flat maps `A → B → C` of Noetherian rings with
> `B → C` faithfully flat, if every fibre of `A → C` is a local complete intersection then so is
> every fibre of `A → B`.
>
> The fibre of `A → C` at a prime `𝔭` is the base change along `B → C` of the fibre of `A → B`, and
> that base change is faithfully flat, so
> `LocalCompleteIntersection.isLocalCompleteIntersectionRing_of_faithfullyFlat` applies.

```lean
public theorem localCompleteIntersectionProperty_faithfullyFlatDescent
    (P : RingMapProperty.{u, u})
    (hP : ∀ (k R : Type u) [Field k] [CommRing R] [Algebra k R] [IsNoetherianRing R],
      P (algebraMap k R) ↔ IsLocalCompleteIntersectionRing R) :
    ∀ (A B C : Type u) [CommRing A] [CommRing B] [CommRing C]
      [Algebra A B] [Algebra B C] [Algebra A C] [IsScalarTower A B C]
      [IsNoetherianRing A] [IsNoetherianRing B] [IsNoetherianRing C]
      [Module.Flat A B] [Module.FaithfullyFlat B C],
      (∀ p : PrimeSpectrum A, P (algebraMap p.asIdeal.ResidueField (p.asIdeal.Fiber C))) →
        ∀ p : PrimeSpectrum A, P (algebraMap p.asIdeal.ResidueField (p.asIdeal.Fiber B))
```

**`localCompleteIntersectionProperty_groundFieldExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCompleteIntersection/FormalFibreAxioms.lean, line 265](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCompleteIntersection/FormalFibreAxioms.lean#L265). The attribute's comment: “(E)”.

> **Stacks Project, Tag 0BJP, clause (E).** Being a local complete intersection is unchanged
> when the ground field is replaced by a separable algebraic extension of it inside the target: the
> condition does not refer to the ground field.

```lean
public theorem localCompleteIntersectionProperty_groundFieldExtension (P : RingMapProperty.{u, u})
    (hP : ∀ (k R : Type u) [Field k] [CommRing R] [Algebra k R] [IsNoetherianRing R],
      P (algebraMap k R) ↔ IsLocalCompleteIntersectionRing R) :
    ∀ (k K R : Type u) [Field k] [Field K] [CommRing R]
      [Algebra k K] [Algebra k R] [Algebra K R] [IsScalarTower k K R]
      [IsNoetherianRing R] [Algebra.IsAlgebraic k K] [Algebra.IsSeparable k K],
      P (algebraMap k R) → P (algebraMap K R)
```

**`localCompleteIntersectionProperty_satisfies_formalFiberAxioms`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCompleteIntersection/FormalFibreAxioms.lean, line 289](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCompleteIntersection/FormalFibreAxioms.lean#L289).

> **Stacks 0BJP.** The property of a map from a field to a Noetherian ring that its target is a
> local complete intersection satisfies properties (A)--(E) of [Stacks, Tag 0BIR]: it is preserved
> by finitely generated field extension, is local on the target, passes through a composition of
> flat maps when the second map is regular, descends through a faithfully flat second map, and is
> unchanged upon replacing the ground field by a separable algebraic extension.
>
> The five clauses are `localCompleteIntersectionProperty_fieldExtension`,
> `localCompleteIntersectionProperty_localization`,
> `localCompleteIntersectionProperty_regularAscent`,
> `localCompleteIntersectionProperty_faithfullyFlatDescent` and
> `localCompleteIntersectionProperty_groundFieldExtension`. The shape is that of
> `cohenMacaulayProperty_satisfies_formalFiberAxioms` ([Stacks, Tag 0BJ9]) and of
> `Dualizing.gorensteinProperty_satisfies_formalFiberAxioms` ([Stacks, Tag 0BJN]).

```lean
public theorem localCompleteIntersectionProperty_satisfies_formalFiberAxioms
    (P : RingMapProperty.{u, u})
    (hP : ∀ (k R : Type u) [Field k] [CommRing R] [Algebra k R] [IsNoetherianRing R],
      P (algebraMap k R) ↔ IsLocalCompleteIntersectionRing R) :
    (∀ (k K R : Type u) [Field k] [Field K] [CommRing R] [Algebra k K]
      [Algebra k R] [IsNoetherianRing R] [Algebra.EssFiniteType k K],
      P (algebraMap k R) →
        P (Algebra.TensorProduct.includeRight (R := k) (A := R) (B := K)).toRingHom) ∧
    (∀ (k R : Type u) [Field k] [CommRing R] [Algebra k R] [IsNoetherianRing R],
      (∀ p : PrimeSpectrum R,
        P (algebraMap k (Localization.AtPrime p.asIdeal))) ↔ P (algebraMap k R)) ∧
    (∀ (A B C : Type u) [CommRing A] [CommRing B] [CommRing C]
      [Algebra A B] [Algebra B C] [Algebra A C] [IsScalarTower A B C]
      [IsNoetherianRing A] [IsNoetherianRing B] [IsNoetherianRing C]
      [Module.Flat A B] [Module.Flat B C],
      (∀ p : PrimeSpectrum A,
        P (algebraMap p.asIdeal.ResidueField (p.asIdeal.Fiber B))) →
      (∀ q : PrimeSpectrum B,
        Algebra.IsGeometricallyRegular q.asIdeal.ResidueField (q.asIdeal.Fiber C)) →
      ∀ p : PrimeSpectrum A,
        P (algebraMap p.asIdeal.ResidueField (p.asIdeal.Fiber C))) ∧
    (∀ (A B C : Type u) [CommRing A] [CommRing B] [CommRing C]
      [Algebra A B] [Algebra B C] [Algebra A C] [IsScalarTower A B C]
      [IsNoetherianRing A] [IsNoetherianRing B] [IsNoetherianRing C]
      [Module.Flat A B] [Module.FaithfullyFlat B C],
      (∀ p : PrimeSpectrum A,
        P (algebraMap p.asIdeal.ResidueField (p.asIdeal.Fiber C))) →
      ∀ p : PrimeSpectrum A,
        P (algebraMap p.asIdeal.ResidueField (p.asIdeal.Fiber B))) ∧
    (∀ (k K R : Type u) [Field k] [Field K] [CommRing R]
      [Algebra k K] [Algebra k R] [Algebra K R] [IsScalarTower k K R]
      [IsNoetherianRing R] [Algebra.IsAlgebraic k K] [Algebra.IsSeparable k K],
      P (algebraMap k R) → P (algebraMap K R))
```

Declarations registered for the tag:

- [`LocalCompleteIntersection.isLocalCompleteIntersectionRing_iff`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCompleteIntersection/Basic.lean#L140), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/RingTheory/Dualizing/FormalFibre.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/FormalFibre.lean#L51) (StacksFrontier): “localization”.
- [`LocalCompleteIntersection.IsLocalCompleteIntersectionRing`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCompleteIntersection/Basic.lean#L135), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/RingTheory/Dualizing/FormalFibre.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/FormalFibre.lean#L53) (StacksFrontier): “ground\_field\_change”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 47.23, Tag 0BJM](https://stacks.math.columbia.edu/tag/0BJM)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
