---
declaration: section
origin: cited
lean: Stacks.Examples.exists_localHom_no_quasiFinite_quotient
statement: formalized
proof: formalized
---

# 110.39 Topology of a finite type ring map

Section 110.39 of the Stacks Project, [Tag 05JH](https://stacks.math.columbia.edu/tag/05JH). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 05JI, a lemma

[Tag 05JI](https://stacks.math.columbia.edu/tag/05JI) in the Stacks Project.

**`Stacks.Examples.exists_localHom_no_quasiFinite_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Algebra/FiniteTypeTopology.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Algebra/FiniteTypeTopology.lean#L101).

> A local map of local domains, essentially of finite type with finite residue extension,
> whose target has a nonmaximal prime but no quotient by such a prime is a localization of a
> quasi-finite algebra.

```lean
public theorem exists_localHom_no_quasiFinite_quotient :
    ∃ (A B : Type u) (_ : CommRing A) (_ : CommRing B)
      (_ : IsDomain A) (_ : IsDomain B) (_ : IsLocalRing A) (_ : IsLocalRing B)
      (f : A →+* B) (hf : IsLocalHom f),
      IsEssentiallyOfFiniteType A B f ∧
      (letI : IsLocalHom f := hf
       letI := (IsLocalRing.ResidueField.map f).toAlgebra
       Module.Finite (IsLocalRing.ResidueField A) (IsLocalRing.ResidueField B)) ∧
      (∃ q : PrimeSpectrum B, q.asIdeal ≠ IsLocalRing.maximalIdeal B) ∧
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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
