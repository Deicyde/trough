---
declaration: section
origin: cited
lean: Stacks.Etale.exists_finiteType_etale_lift, Stacks.Etale.exists_finiteType_etale_lift_of_isNilpotent, Stacks.Etale.exists_finiteType_etale_lift_of_eq_top
statement: formalized
proof: formalized
---

# 88.9 A pushout argument

Section 88.9 of the Stacks Project, [Tag 0AK8](https://stacks.math.columbia.edu/tag/0AK8). 1 tag here is carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0ALT, a lemma

[Tag 0ALT](https://stacks.math.columbia.edu/tag/0ALT) in the Stacks Project.

**`Stacks.Etale.exists_finiteType_etale_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/PushoutLift/Main.lean, line 381](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/PushoutLift/Main.lean#L381).

> **Stacks 0ALT.** Let `A` be a Noetherian ring, `I ⊆ A` an ideal and `J ⊆ A` a nilpotent
> ideal, and consider a commutative diagram of finite type ring maps
>
> ```
> C  --->  C ⧸ JC
>           ^
>          B₀
>           ^
> A  --->  A ⧸ J
> ```
>
> such that `Spec C → Spec A` is étale over `Spec A \ V(I)`, such that `Spec B₀ → Spec (A ⧸ J)` is
> étale over `Spec (A ⧸ J) \ V(I (A ⧸ J))`, and such that `B₀ → C ⧸ JC` is étale and induces an
> isomorphism `B₀ ⧸ I B₀ = (C ⧸ JC) ⧸ I (C ⧸ JC)`. Then the diagram can be filled in: there are a
> finite type `A`-algebra `B`, an `A`-algebra map `B → C` which is étale, and an isomorphism
> `B ⧸ JB ≅ B₀` compatible with the maps to `C ⧸ JC`, such that `Spec B → Spec A` is étale over
> `Spec A \ V(I)`.

```lean
theorem exists_finiteType_etale_lift
    (A C B₀ : Type u) [CommRing A] [CommRing C] [CommRing B₀]
    [IsNoetherianRing A] [Algebra A C] [Algebra.FiniteType A C]
    (I J : Ideal A) (hJ : IsNilpotent J)
    [Algebra A B₀] [Algebra (A ⧸ J) B₀] [IsScalarTower A (A ⧸ J) B₀]
    [Algebra.FiniteType (A ⧸ J) B₀]
    [Algebra (A ⧸ J) (C ⧸ J.map (algebraMap A C))]
    [IsScalarTower A (A ⧸ J) (C ⧸ J.map (algebraMap A C))]
    [Algebra B₀ (C ⧸ J.map (algebraMap A C))]
    [IsScalarTower (A ⧸ J) B₀ (C ⧸ J.map (algebraMap A C))]
    [Algebra.Etale B₀ (C ⧸ J.map (algebraMap A C))]
    (hC : ∀ q : Ideal C, ∀ _ : q.IsPrime, ¬ I ≤ q.comap (algebraMap A C) →
      Algebra.IsEtaleAt A q)
    (hB₀ : ∀ q : Ideal B₀, ∀ _ : q.IsPrime,
      ¬ I.map (Ideal.Quotient.mk J) ≤ q.comap (algebraMap (A ⧸ J) B₀) →
        Algebra.IsEtaleAt (A ⧸ J) q)
    (hmod : Function.Bijective (Ideal.quotientMap
      (((I.map (Ideal.Quotient.mk J)).map (algebraMap (A ⧸ J) B₀)).map
        (algebraMap B₀ (C ⧸ J.map (algebraMap A C))))
      (algebraMap B₀ (C ⧸ J.map (algebraMap A C))) Ideal.le_comap_map)) :
    ∃ (B : Type u) (_ : CommRing B) (_ : Algebra A B) (_ : Algebra.FiniteType A B)
      (_ : Algebra B C) (_ : IsScalarTower A B C) (_ : Algebra.Etale B C)
      (e : (B ⧸ J.map (algebraMap A B)) ≃ₐ[A] B₀),
      (∀ q : Ideal B, ∀ _ : q.IsPrime, ¬ I ≤ q.comap (algebraMap A B) →
        Algebra.IsEtaleAt A q) ∧
      ∀ b : B, algebraMap B₀ (C ⧸ J.map (algebraMap A C))
            (e (Ideal.Quotient.mk (J.map (algebraMap A B)) b)) =
          Ideal.Quotient.mk (J.map (algebraMap A C)) (algebraMap B C b)
```

**`Stacks.Etale.exists_finiteType_etale_lift_of_isNilpotent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/PushoutLiftAcrossNilpotent.lean, line 182](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/PushoutLiftAcrossNilpotent.lean#L182). The attribute's comment: “extra hypothesis: the ideal I·B₀ is nilpotent, equivalently the open set Spec(B₀) minus V(I·B₀) along which the source glues is empty; the conclusion is delivered in full”.

> Let `A` be a Noetherian ring, `I ⊆ A` an ideal and `J ⊆ A` a nilpotent ideal, and consider a
> commutative diagram of finite type ring maps
>
> ```
> C  --->  C ⧸ JC
>           ^
>          B₀
>           ^
> A  --->  A ⧸ J
> ```
>
> such that `Spec C → Spec A` is étale over `Spec A \ V(I)`, such that `Spec B₀ → Spec (A ⧸ J)` is
> étale over `Spec (A ⧸ J) \ V(I (A ⧸ J))`, and such that `B₀ → C ⧸ JC` is étale and induces an
> isomorphism `B₀ ⧸ I B₀ = (C ⧸ JC) ⧸ I (C ⧸ JC)`.  Then the diagram can be filled in: there are a
> finite type `A`-algebra `B`, an `A`-algebra map `B → C` which is étale, and an isomorphism
> `B ⧸ JB ≅ B₀` compatible with the maps to `C ⧸ JC`, such that `Spec B → Spec A` is étale over
> `Spec A \ V(I)`.
>
> This takes the extra hypothesis `hnil` that `I B₀` is nilpotent, equivalently that the open set
> `Spec B₀ \ V(I B₀)` is empty.

```lean
theorem exists_finiteType_etale_lift_of_isNilpotent
    (A C B₀ : Type u) [CommRing A] [CommRing C] [CommRing B₀]
    [IsNoetherianRing A] [Algebra A C] [Algebra.FiniteType A C]
    (I J : Ideal A) (_hJ : IsNilpotent J)
    [Algebra A B₀] [Algebra (A ⧸ J) B₀] [IsScalarTower A (A ⧸ J) B₀]
    [Algebra.FiniteType (A ⧸ J) B₀]
    [Algebra (A ⧸ J) (C ⧸ J.map (algebraMap A C))]
    [IsScalarTower A (A ⧸ J) (C ⧸ J.map (algebraMap A C))]
    [Algebra B₀ (C ⧸ J.map (algebraMap A C))]
    [IsScalarTower (A ⧸ J) B₀ (C ⧸ J.map (algebraMap A C))]
    [Algebra.Etale B₀ (C ⧸ J.map (algebraMap A C))]
    (hC : ∀ q : Ideal C, ∀ _ : q.IsPrime, ¬ I ≤ q.comap (algebraMap A C) →
      Algebra.IsEtaleAt A q)
    (_hB₀ : ∀ q : Ideal B₀, ∀ _ : q.IsPrime,
      ¬ I.map (Ideal.Quotient.mk J) ≤ q.comap (algebraMap (A ⧸ J) B₀) →
        Algebra.IsEtaleAt (A ⧸ J) q)
    (hmod : Function.Bijective (Ideal.quotientMap
      (((I.map (Ideal.Quotient.mk J)).map (algebraMap (A ⧸ J) B₀)).map
        (algebraMap B₀ (C ⧸ J.map (algebraMap A C))))
      (algebraMap B₀ (C ⧸ J.map (algebraMap A C))) Ideal.le_comap_map))
    (hnil : IsNilpotent ((I.map (Ideal.Quotient.mk J)).map (algebraMap (A ⧸ J) B₀))) :
    ∃ (B : Type u) (_ : CommRing B) (_ : Algebra A B) (_ : Algebra.FiniteType A B)
      (_ : Algebra B C) (_ : IsScalarTower A B C) (_ : Algebra.Etale B C)
      (e : (B ⧸ J.map (algebraMap A B)) ≃ₐ[A] B₀),
      (∀ q : Ideal B, ∀ _ : q.IsPrime, ¬ I ≤ q.comap (algebraMap A B) →
        Algebra.IsEtaleAt A q) ∧
      ∀ b : B, algebraMap B₀ (C ⧸ J.map (algebraMap A C))
            (e (Ideal.Quotient.mk (J.map (algebraMap A B)) b)) =
          Ideal.Quotient.mk (J.map (algebraMap A C)) (algebraMap B C b)
```

**`Stacks.Etale.exists_finiteType_etale_lift_of_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/PushoutLiftAcrossNilpotent.lean, line 233](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/PushoutLiftAcrossNilpotent.lean#L233). The attribute's comment: “extra hypothesis: I·B₀ is the unit ideal of B₀, equivalently the closed set V(I·B₀) in Spec(B₀) along which the source glues is empty; the conclusion is delivered in full”.

> The data and the conclusion are those of `exists_finiteType_etale_lift_of_isNilpotent`, with
> the extra hypothesis `htop` that `I B₀` is the unit ideal, equivalently that the closed set
> `V(I B₀) ⊆ Spec B₀` is empty, in place of `hnil`.

```lean
theorem exists_finiteType_etale_lift_of_eq_top
    (A C B₀ : Type u) [CommRing A] [CommRing C] [CommRing B₀]
    [IsNoetherianRing A] [Algebra A C] [Algebra.FiniteType A C]
    (I J : Ideal A) (hJ : IsNilpotent J)
    [Algebra A B₀] [Algebra (A ⧸ J) B₀] [IsScalarTower A (A ⧸ J) B₀]
    [Algebra.FiniteType (A ⧸ J) B₀]
    [Algebra (A ⧸ J) (C ⧸ J.map (algebraMap A C))]
    [IsScalarTower A (A ⧸ J) (C ⧸ J.map (algebraMap A C))]
    [Algebra B₀ (C ⧸ J.map (algebraMap A C))]
    [IsScalarTower (A ⧸ J) B₀ (C ⧸ J.map (algebraMap A C))]
    [Algebra.Etale B₀ (C ⧸ J.map (algebraMap A C))]
    (hC : ∀ q : Ideal C, ∀ _ : q.IsPrime, ¬ I ≤ q.comap (algebraMap A C) →
      Algebra.IsEtaleAt A q)
    (hB₀ : ∀ q : Ideal B₀, ∀ _ : q.IsPrime,
      ¬ I.map (Ideal.Quotient.mk J) ≤ q.comap (algebraMap (A ⧸ J) B₀) →
        Algebra.IsEtaleAt (A ⧸ J) q)
    (_hmod : Function.Bijective (Ideal.quotientMap
      (((I.map (Ideal.Quotient.mk J)).map (algebraMap (A ⧸ J) B₀)).map
        (algebraMap B₀ (C ⧸ J.map (algebraMap A C))))
      (algebraMap B₀ (C ⧸ J.map (algebraMap A C))) Ideal.le_comap_map))
    (htop : (I.map (Ideal.Quotient.mk J)).map (algebraMap (A ⧸ J) B₀) = ⊤) :
    ∃ (B : Type u) (_ : CommRing B) (_ : Algebra A B) (_ : Algebra.FiniteType A B)
      (_ : Algebra B C) (_ : IsScalarTower A B C) (_ : Algebra.Etale B C)
      (e : (B ⧸ J.map (algebraMap A B)) ≃ₐ[A] B₀),
      (∀ q : Ideal B, ∀ _ : q.IsPrime, ¬ I ≤ q.comap (algebraMap A B) →
        Algebra.IsEtaleAt A q) ∧
      ∀ b : B, algebraMap B₀ (C ⧸ J.map (algebraMap A C))
            (e (Ideal.Quotient.mk (J.map (algebraMap A B)) b)) =
          Ideal.Quotient.mk (J.map (algebraMap A C)) (algebraMap B C b)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 88.9, Tag 0AK8](https://stacks.math.columbia.edu/tag/0AK8)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
