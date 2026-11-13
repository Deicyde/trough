---
declaration: section
origin: cited
lean: Stacks.Examples.exists_localHom_not_isNoetherianRing_no_quasiFinite_quotient
statement: formalized
proof: formalized
---

# 110.39 Topology of a finite type ring map

Section 110.39 of the Stacks Project, [Tag 05JH](https://stacks.math.columbia.edu/tag/05JH). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05JI, a lemma

[Tag 05JI](https://stacks.math.columbia.edu/tag/05JI) in the Stacks Project.

**`Stacks.Examples.exists_localHom_not_isNoetherianRing_no_quasiFinite_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Algebra/FiniteTypeTopologyNonNoetherian.lean, line 584](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Algebra/FiniteTypeTopologyNonNoetherian.lean#L584).

> **Stacks 05JI.** There is a local homomorphism `f : A → B` of local domains, essentially of
> finite type, with finite residue field extension, such that for every prime `q ≠ m_B` of `B`
> the map `A → B/q` is not a localization of a quasi-finite ring map.
>
> The witness is the one of Stacks: `A` is not Noetherian and some prime of `B` (namely `(0)`)
> does not lie over `m_A`. So all hypotheses of Stacks 05GT except the Noetherian one hold, with
> `V = Spec B`, while its conclusion fails.

```lean
public theorem exists_localHom_not_isNoetherianRing_no_quasiFinite_quotient :
    ∃ (A B : Type u) (_ : CommRing A) (_ : CommRing B)
      (_ : IsDomain A) (_ : IsDomain B) (_ : IsLocalRing A) (_ : IsLocalRing B)
      (f : A →+* B) (hf : IsLocalHom f),
      IsEssentiallyOfFiniteType A B f ∧
      (letI : IsLocalHom f := hf
       letI := (IsLocalRing.ResidueField.map f).toAlgebra
       Module.Finite (IsLocalRing.ResidueField A) (IsLocalRing.ResidueField B)) ∧
      ¬ IsNoetherianRing A ∧
      (∃ q : PrimeSpectrum B, q.asIdeal.comap f ≠ IsLocalRing.maximalIdeal A) ∧
      (∀ q : PrimeSpectrum B, q.asIdeal ≠ IsLocalRing.maximalIdeal B →
        ¬ (letI := f.toAlgebra
           ∃ (C : Type u) (_ : CommRing C) (_ : Algebra A C)
             (_ : Algebra.FiniteType A C) (_ : Algebra.QuasiFinite A C)
             (M : Submonoid C) (_ : Algebra C (B ⧸ q.asIdeal)),
             IsScalarTower A C (B ⧸ q.asIdeal) ∧ IsLocalization M (B ⧸ q.asIdeal)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.39, Tag 05JH](https://stacks.math.columbia.edu/tag/05JH)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
