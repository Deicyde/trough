---
declaration: theorem
origin: cited
lean: ContRepresentation.exists_eq_smul_one_of_isIrreducible, ContRepresentation.eq_zero_of_isEmpty_equiv
statement: formalized
proof: formalized
---

# Schur's lemma, scalar half

Every continuous self-intertwiner of an irreducible
finite-dimensional representation over an algebraically closed field is a scalar multiple of the
identity.

```lean
ContRepresentation.exists_eq_smul_one_of_isIrreducible.{u_1, u_2, u_3} {𝕜 : Type u_1} {G : Type u_2}
  {V : Type u_3} [Field 𝕜] [IsAlgClosed 𝕜] [Monoid G] [AddCommGroup V] [_root_.Module 𝕜 V]
  [TopologicalSpace V] [IsTopologicalAddGroup V] [ContinuousConstSMul 𝕜 V] [FiniteDimensional 𝕜 V]
  (π : ContRepresentation 𝕜 G V)
  (hirr : (ContRepresentation.toRepresentation 𝕜 G V π).IsIrreducible)
  (f : ContIntertwiningMap π π) : ∃ c, f = c • 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContRepresentation.exists_eq_smul_one_of_isIrreducible`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Continuous/Schur.html#ContRepresentation.exists_eq_smul_one_of_isIrreducible).

## Other forms

**Schur's lemma, vanishing half.** Formalized in Tau Ceti as [`ContRepresentation.eq_zero_of_isEmpty_equiv`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Continuous/Schur.html#ContRepresentation.eq_zero_of_isEmpty_equiv).

```lean
ContRepresentation.eq_zero_of_isEmpty_equiv.{u_1, u_2, u_3, u_4} {𝕜 : Type u_1} {G : Type u_2}
  {V : Type u_3} {W : Type u_4} [NontriviallyNormedField 𝕜] [CompleteSpace 𝕜] [Monoid G]
  [AddCommGroup V] [_root_.Module 𝕜 V] [TopologicalSpace V] [IsTopologicalAddGroup V]
  [ContinuousSMul 𝕜 V] [T2Space V] [FiniteDimensional 𝕜 V] [AddCommGroup W] [_root_.Module 𝕜 W]
  [TopologicalSpace W] [IsTopologicalAddGroup W] [ContinuousSMul 𝕜 W] [T2Space W]
  {π : ContRepresentation 𝕜 G V} {ρ : ContRepresentation 𝕜 G W}
  (hπ : (ContRepresentation.toRepresentation 𝕜 G V π).IsIrreducible)
  (hρ : (ContRepresentation.toRepresentation 𝕜 G W ρ).IsIrreducible) (hne : IsEmpty (π.Equiv ρ))
  (f : ContIntertwiningMap π ρ) : f = 0
```

## Sources

- [Tau Ceti documentation: `ContRepresentation.exists_eq_smul_one_of_isIrreducible`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Continuous/Schur.html#ContRepresentation.exists_eq_smul_one_of_isIrreducible)
- [Source of `ContRepresentation.exists_eq_smul_one_of_isIrreducible` in TauCeti/RepresentationTheory/Continuous/Schur.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Continuous/Schur.lean#L83)
