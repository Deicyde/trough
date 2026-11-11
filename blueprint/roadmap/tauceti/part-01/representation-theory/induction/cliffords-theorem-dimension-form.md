---
declaration: theorem
origin: cited
lean: FDRep.clifford_restrict_finrank, FDRep.clifford_restrict_iso_of_isAtom, TauCeti.clifford_restrict_character, Representation.finrank_linearMap_eq_of_isAtom, Representation.finrank_linearMap_eq_of_isAtom_of_isAtom, FDRep.clifford_restrict_iso, TauCeti.Representation.exists_nonempty_linearEquiv_conjSubrep, TauCeti.Representation.exists_isAtom_forall_nonempty_linearEquiv_conjSubrep, Representation.exists_forall_finrank_linearMap_eq
statement: formalized
proof: formalized
---

# Clifford's theorem, dimension form

The dimension of an irreducible representation of `G`
is the common multiplicity `e` of the constituents of its restriction to `N`, times the number
`[G : inertia V]` of those constituents, times the dimension of one of them.

The decomposition `Res_N W ≅ V.cliffordSum e` that `FDRep.clifford_restrict_iso` supplies is
returned alongside the identity, so that `V` is exhibited as a constituent of the restriction and
not merely named by it.

In particular the index of the inertia group of a constituent divides the dimension of `W`; that
is the arithmetic that `FDRep.clifford_restrict_dvd_finrank` reads off and that
`FDRep.clifford_restrict_inertia_eq_top_of_coprime` exploits.

```lean
FDRep.clifford_restrict_finrank.{u, v} {k : Type u} {G : Type v} [Field k] [Group G]
  {N : Subgroup G} [N.Normal] [IsAlgClosed k] (W : FDRep k G) [CategoryTheory.Simple W] :
  ∃ V,
    ∃ (_ : CategoryTheory.Simple V) (hfinite : Finite (G ⧸ TauCeti.inertia V)),
      have x := hfinite;
      ∃ e,
        e ≠ 0 ∧
          Nonempty (N.resFDRep W ≅ V.cliffordSum e) ∧
            Module.finrank k ↑W.V = e * (TauCeti.inertia V).index * Module.finrank k ↑V.V
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The multiplicity theorem](../../ring-theory/part-01/semisimple/the-multiplicity-theorem.md)

## Lean

Formalized in Tau Ceti as [`FDRep.clifford_restrict_finrank`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/Clifford/Dimension.html#FDRep.clifford_restrict_finrank).

## Other forms

**Clifford's theorem for a specified constituent.** Formalized in Tau Ceti as [`FDRep.clifford_restrict_iso_of_isAtom`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/Clifford/Equivalence.html#FDRep.clifford_restrict_iso_of_isAtom).

```lean
FDRep.clifford_restrict_iso_of_isAtom.{u, v} {k : Type u} {G : Type v} [Field k] [Group G]
  {N : Subgroup G} [N.Normal] [IsAlgClosed k] (W : FDRep k G) [CategoryTheory.Simple W]
  (σ : Subrepresentation (W.ρ.comp N.subtype)) (hσ : IsAtom σ) :
  ∃ (hfinite : Finite (G ⧸ TauCeti.inertia (FDRep.of σ.toRepresentation))),
    have x := hfinite;
    ∃ e, e ≠ 0 ∧ Nonempty (N.resFDRep W ≅ (FDRep.of σ.toRepresentation).cliffordSum e)
```

**Clifford's theorem, character form.** Formalized in Tau Ceti as [`TauCeti.clifford_restrict_character`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/Clifford/Decomposition.html#TauCeti.clifford_restrict_character).

```lean
TauCeti.clifford_restrict_character.{u, v} {k : Type u} {G : Type v} [Field k] [Group G]
  {N : Subgroup G} [N.Normal] [Finite G] [IsAlgClosed k] (hG : IsUnit ↑(Nat.card G)) (W : FDRep k G)
  [CategoryTheory.Simple W] :
  ∃ V,
    ∃ (_ : CategoryTheory.Simple V),
      ∃ e reps,
        e ≠ 0 ∧
          (∀ (g : G), ∃! r, r ∈ reps ∧ g⁻¹ * r ∈ TauCeti.inertia V) ∧
            ∀ (n : ↥N), W.character ↑n = ↑e * ∑ g ∈ reps, (TauCeti.conjNormalFDRep g V).character n
```

**Clifford's theorem, multiplicity form.** Formalized in Tau Ceti as [`Representation.finrank_linearMap_eq_of_isAtom`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/Clifford/Multiplicity.html#Representation.finrank_linearMap_eq_of_isAtom).

```lean
Representation.finrank_linearMap_eq_of_isAtom.{u_1, u_2, u_3} {k : Type u_1} {G : Type u_2}
  {V : Type u_3} [Field k] [Group G] [AddCommGroup V] [_root_.Module k V] {N : Subgroup G}
  [N.Normal] (ρ : Representation k G V) [ρ.IsIrreducible]
  {σ : Subrepresentation (MonoidHom.comp ρ N.subtype)} (hσ : IsAtom σ)
  (T : Submodule (MonoidAlgebra k ↥N) (Representation.asModule (MonoidHom.comp ρ N.subtype)))
  [IsSimpleModule (MonoidAlgebra k ↥N) ↥T] :
  Module.finrank k
      (↥T →ₗ[MonoidAlgebra k ↥N] Representation.asModule (MonoidHom.comp ρ N.subtype)) =
    Module.finrank k
      (↥σ.asSubmodule →ₗ[MonoidAlgebra k ↥N] Representation.asModule (MonoidHom.comp ρ N.subtype))
```

**Clifford's theorem, multiplicity form, for two minimal subspaces.** Formalized in Tau Ceti as [`Representation.finrank_linearMap_eq_of_isAtom_of_isAtom`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/Clifford/Multiplicity.html#Representation.finrank_linearMap_eq_of_isAtom_of_isAtom).

```lean
Representation.finrank_linearMap_eq_of_isAtom_of_isAtom.{u_1, u_2, u_3} {k : Type u_1}
  {G : Type u_2} {V : Type u_3} [Field k] [Group G] [AddCommGroup V] [_root_.Module k V]
  {N : Subgroup G} [N.Normal] (ρ : Representation k G V) [ρ.IsIrreducible]
  {σ τ : Subrepresentation (MonoidHom.comp ρ N.subtype)} (hσ : IsAtom σ) (hτ : IsAtom τ) :
  Module.finrank k
      (↥σ.asSubmodule →ₗ[MonoidAlgebra k ↥N] Representation.asModule (MonoidHom.comp ρ N.subtype)) =
    Module.finrank k
      (↥τ.asSubmodule →ₗ[MonoidAlgebra k ↥N] Representation.asModule (MonoidHom.comp ρ N.subtype))
```

**Clifford's theorem, representation form.** Formalized in Tau Ceti as [`FDRep.clifford_restrict_iso`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/Clifford/Equivalence.html#FDRep.clifford_restrict_iso).

```lean
FDRep.clifford_restrict_iso.{u, v} {k : Type u} {G : Type v} [Field k] [Group G] {N : Subgroup G}
  [N.Normal] [IsAlgClosed k] (W : FDRep k G) [CategoryTheory.Simple W] :
  ∃ V,
    ∃ (_ : CategoryTheory.Simple V) (hfinite : Finite (G ⧸ TauCeti.inertia V)),
      have x := hfinite;
      ∃ e, e ≠ 0 ∧ Nonempty (N.resFDRep W ≅ V.cliffordSum e)
```

**Clifford's theorem, single-orbit form.** Formalized in Tau Ceti as [`TauCeti.Representation.exists_nonempty_linearEquiv_conjSubrep`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/Clifford/Orbit/Basic.html#TauCeti.Representation.exists_nonempty_linearEquiv_conjSubrep).

```lean
TauCeti.Representation.exists_nonempty_linearEquiv_conjSubrep.{u_1, u_2, u_3} {k : Type u_1}
  {G : Type u_2} {V : Type u_3} [Field k] [Group G] [AddCommGroup V] [_root_.Module k V]
  {N : Subgroup G} [N.Normal] (ρ : Representation k G V) [ρ.IsIrreducible]
  {σ τ : Subrepresentation (MonoidHom.comp ρ N.subtype)} (hσ : IsAtom σ) (hτ : IsAtom τ) :
  ∃ g,
    Nonempty
      (↥τ.asSubmodule ≃ₗ[MonoidAlgebra k ↥N] ↥(TauCeti.Representation.conjSubrep ρ g σ).asSubmodule)
```

**Clifford's theorem, single-orbit form, packaged.** Formalized in Tau Ceti as [`TauCeti.Representation.exists_isAtom_forall_nonempty_linearEquiv_conjSubrep`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/Clifford/Orbit/Basic.html#TauCeti.Representation.exists_isAtom_forall_nonempty_linearEquiv_conjSubrep).

```lean
TauCeti.Representation.exists_isAtom_forall_nonempty_linearEquiv_conjSubrep.{u_1, u_2, u_3}
  {k : Type u_1} {G : Type u_2} {V : Type u_3} [Field k] [Group G] [AddCommGroup V]
  [_root_.Module k V] {N : Subgroup G} [N.Normal] (ρ : Representation k G V) [ρ.IsIrreducible]
  [FiniteDimensional k V] :
  ∃ σ,
    IsAtom σ ∧
      ∀ (τ : Subrepresentation (MonoidHom.comp ρ N.subtype)),
        IsAtom τ →
          ∃ g,
            Nonempty
              (↥τ.asSubmodule ≃ₗ[MonoidAlgebra k ↥N]
                ↥(TauCeti.Representation.conjSubrep ρ g σ).asSubmodule)
```

**Clifford's theorem, the common multiplicity.** Formalized in Tau Ceti as [`Representation.exists_forall_finrank_linearMap_eq`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/Clifford/Multiplicity.html#Representation.exists_forall_finrank_linearMap_eq).

```lean
Representation.exists_forall_finrank_linearMap_eq.{u_1, u_2, u_3} {k : Type u_1} {G : Type u_2}
  {V : Type u_3} [Field k] [Group G] [AddCommGroup V] [_root_.Module k V] {N : Subgroup G}
  [N.Normal] (ρ : Representation k G V) [ρ.IsIrreducible] [FiniteDimensional k V] :
  ∃ e,
    0 < e ∧
      ∀ (σ : Subrepresentation (MonoidHom.comp ρ N.subtype)),
        IsAtom σ →
          Module.finrank k
              (↥σ.asSubmodule →ₗ[MonoidAlgebra k ↥N]
                Representation.asModule (MonoidHom.comp ρ N.subtype)) =
            e
```

## Sources

- [Tau Ceti documentation: `FDRep.clifford_restrict_finrank`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/Clifford/Dimension.html#FDRep.clifford_restrict_finrank)
- [Source of `FDRep.clifford_restrict_finrank` in TauCeti/RepresentationTheory/Induction/Clifford/Dimension.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Induction/Clifford/Dimension.lean#L72)
