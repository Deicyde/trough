---
declaration: section
origin: cited
lean: Rig.exists_finiteType_algEquiv_of_isRigEtale_principal, Rig.exists_finiteType_algEquiv_adicCompletion_of_isRigEtale, Rig.exists_isEtaleOutside_finiteType_algEquiv_of_isRigEtale_principal, Rig.isRigEtale_iff_exists_isEtaleOutside_algEquiv, Rig.isRigEtale_of_isEtaleOutside_of_algEquiv
statement: formalized
proof: formalized
---

# 88.10 Algebraization of rig-étale algebras

Section 88.10 of the Stacks Project, [Tag 0AK5](https://stacks.math.columbia.edu/tag/0AK5). 3 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0ALS, a lemma

[Tag 0ALS](https://stacks.math.columbia.edu/tag/0ALS) in the Stacks Project.

**`Rig.exists_finiteType_algEquiv_of_isRigEtale_principal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/Algebraization/PrincipalIsomorphism.lean, line 221](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/Algebraization/PrincipalIsomorphism.lean#L221). The attribute's comment: “the rig-étale case of Elkik III Theorem 7, over a principal ideal”.

> **Stacks 0ALS**, the rig-étale case of [Elkik, III Theorem 7], with no restriction on the
> universe of `B`.  Let `A` be a Noetherian ring and `I = (a)` a principal ideal.  Let `B` be an
> object of the category of `I`-adically complete `A`-algebras of finite type modulo `I`
> (Stacks 0AL4) which is rig-étale over `(A, I)`.  Then there is a finite type `A`-algebra `C`
> and an isomorphism `B ≅ C^∧`.
>
> The carrier of `B` is replaced by the quotient `A⟨x₁, …, x_r⟩/J` of a presentation of `B`
> (`Rig.quotientObj`), which lives in the universe of `A` and is `A`-algebra isomorphic to
> `B.carrier` by `Rig.CompletedPolynomialPresentation.quotientEquiv`; rig-étaleness transports
> across that isomorphism by `Rig.isRigEtale_of_algEquiv` (Stacks 0GB2), and
> `Rig.exists_finiteType_algEquiv_of_isRigEtale_principal_sameUniverse` applies to it.

```lean
public theorem exists_finiteType_algEquiv_of_isRigEtale_principal
    (hI : I.IsPrincipal) (B : AdicFiniteTypeAlgebra.{u, v} A I) (hB : IsRigEtale B) :
    ∃ (C : Type u) (_ : CommRing C) (_ : Algebra A C),
      Algebra.FiniteType A C ∧
        Nonempty (B.carrier ≃ₐ[A] AdicCompletion (I.map (algebraMap A C)) C)
```

## Tag 0AKA, a lemma

[Tag 0AKA](https://stacks.math.columbia.edu/tag/0AKA) in the Stacks Project.

**`Rig.exists_finiteType_algEquiv_adicCompletion_of_isRigEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/Algebraization/RigEtaleAlgebraization.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/Algebraization/RigEtaleAlgebraization.lean#L82).

> Let `A` be a Noetherian ring and `I ⊆ A` an ideal. If `B` is an object of
> `Rig.AdicFiniteTypeAlgebra A I` which is rig-étale over `(A, I)`, then there is a finite type
> `A`-algebra `C` and an isomorphism `B ≅ C^∧` with its `I`-adic completion.

```lean
public theorem exists_finiteType_algEquiv_adicCompletion_of_isRigEtale
    {A : Type u} [CommRing A] [IsNoetherianRing A] {I : Ideal A}
    (B : AdicFiniteTypeAlgebra.{u, v} A I) (hB : IsRigEtale B) :
    ∃ (C : Type u) (_ : CommRing C) (_ : Algebra A C),
      Algebra.FiniteType A C ∧
        Nonempty (B.carrier ≃ₐ[A] AdicCompletion (I.map (algebraMap A C)) C)
```

## Tag 0AKG, a lemma

[Tag 0AKG](https://stacks.math.columbia.edu/tag/0AKG) in the Stacks Project.

**`Rig.exists_isEtaleOutside_finiteType_algEquiv_of_isRigEtale_principal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/Algebraization/EtaleOutside.lean, line 270](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/Algebraization/EtaleOutside.lean#L270). The attribute's comment: “the converse implication, over a PRINCIPAL ideal: the equivalent conditions of Stacks 0AJU imply condition (8). Stacks 0ALS algebraizes a rig-étale object over a principal ideal and the improvement step above makes the algebraization étale over the complement of V(I); that improvement step, `Rig.exists_isEtaleOutside_finiteType_algEquiv_of_algEquiv_adicCompletion`, is proved for an arbitrary ideal”.

> **Stacks 0AKG, the equivalent conditions of Stacks 0AJU imply condition (8), over a
> principal ideal.** Let `A` be a Noetherian ring and `I = (a)` a principal ideal. Let `B` be an
> object of the category of `I`-adically complete `A`-algebras of finite type modulo `I` (Stacks
> 0AL4) which is rig-étale over `(A, I)`. Then there is a finite type `A`-algebra `C` with
> `Spec(C) → Spec(A)` étale over `Spec(A) ∖ V(I)` and an isomorphism `B ≅ C^∧`.
>
> Stacks 0ALS (`Rig.exists_finiteType_algEquiv_of_isRigEtale_principal`) algebraizes `B` over a
> principal ideal, and
> `Rig.exists_isEtaleOutside_finiteType_algEquiv_of_algEquiv_adicCompletion` improves the
> algebraization to one étale off `V(I)`.

```lean
public theorem exists_isEtaleOutside_finiteType_algEquiv_of_isRigEtale_principal
    (hI : I.IsPrincipal) (B : AdicFiniteTypeAlgebra.{u, v} A I) (hB : IsRigEtale B) :
    ∃ (C : Type u) (_ : CommRing C) (_ : Algebra A C),
      Algebra.FiniteType A C ∧ IsEtaleOutside I C ∧
        Nonempty (B.carrier ≃ₐ[A] AdicCompletion (I.map (algebraMap A C)) C)
```

**`Rig.isRigEtale_iff_exists_isEtaleOutside_algEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/Algebraization/RigEtaleAlgebraization.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/Algebraization/RigEtaleAlgebraization.lean#L102).

> Let `A` be a Noetherian ring, `I ⊆ A` an ideal and `B` an `I`-adically complete `A`-algebra
> with `A ⧸ I → B ⧸ IB` of finite type. Then `B` is rig-étale if and only if there is a finite type
> `A`-algebra `C` with `Spec(C) → Spec(A)` étale over `Spec(A) ∖ V(I)` and an isomorphism
> `B ≅ C^∧` of `A`-algebras.

```lean
public theorem isRigEtale_iff_exists_isEtaleOutside_algEquiv
    {A : Type u} [CommRing A] [IsNoetherianRing A] {I : Ideal A}
    (B : AdicFiniteTypeAlgebra.{u, v} A I) :
    IsRigEtale B ↔
      ∃ (C : Type u) (_ : CommRing C) (_ : Algebra A C),
        Algebra.FiniteType A C ∧ IsEtaleOutside I C ∧
          Nonempty (B.carrier ≃ₐ[A] AdicCompletion (I.map (algebraMap A C)) C)
```

**`Rig.isRigEtale_of_isEtaleOutside_of_algEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/RigEtaleLocus.lean, line 590](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/RigEtaleLocus.lean#L590). The attribute's comment: “condition (8) implies the equivalent conditions of Stacks 0AJU; the converse implication is not covered, since it rests on the algebraization lemma — that a rig-étale object of this category is the completion of a finite type algebra — which this library does not carry”.

> **Stacks 0AKG, condition (8) implies the equivalent conditions of Stacks 0AJU.**  Let `A`
> be a Noetherian ring, `I ⊆ A` an ideal and `B` an `I`-adically complete `A`-algebra of finite
> type modulo `I`.  If `B` is isomorphic as an `A`-algebra to the `I`-adic completion `C^∧` of a
> finite type `A`-algebra `C` with `Spec(C) → Spec(A)` étale over `Spec(A) ∖ V(I)`, then `B` is
> rig-étale over `(A, I)`.
>
> This is Stacks 0ALQ, part (1) applied to `C`, followed by the invariance of rig-étaleness
> under isomorphism.

```lean
public theorem isRigEtale_of_isEtaleOutside_of_algEquiv
    {B : AdicFiniteTypeAlgebra.{u, w} A I} {C : Type v} [CommRing C] [Algebra A C]
    [Algebra.FiniteType A C] (hC : IsEtaleOutside I C)
    (e : B.carrier ≃ₐ[A] (adicCompletionObj I (B := C)).carrier) :
    IsRigEtale B
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 88.10, Tag 0AK5](https://stacks.math.columbia.edu/tag/0AK5)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
