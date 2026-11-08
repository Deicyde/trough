---
declaration: theorem
origin: cited
lean: Representation.char_eq_zero_or_norm_char_eq_finrank, FDRep.char_eq_zero_or_norm_char_eq_finrank, FDRep.char_eq_zero_or_exists_apply_eq_smul, Representation.char_eq_zero_or_exists_apply_eq_smul
statement: formalized
proof: formalized
---

# Burnside's vanishing theorem

If the conjugacy class of `g` has size coprime to the degree
of an irreducible complex representation `ρ`, then its character either vanishes at `g` or attains
there the maximum absolute value `χ(1)` that any character value can have.

The average `χ(g) / χ(1)` is an algebraic integer (`Representation.isIntegral_char_div_finrank`)
and `χ(g)` is a sum of `χ(1)` roots of unity, so Kronecker's theorem leaves no other
possibility.

```lean
Representation.char_eq_zero_or_norm_char_eq_finrank.{u_1, u_2} {G : Type u_1} {V : Type u_2}
  [Group G] [Finite G] [AddCommGroup V] [_root_.Module ℂ V] [FiniteDimensional ℂ V]
  (ρ : Representation ℂ G V) [ρ.IsIrreducible] {g : G}
  (h : (Nat.card ↑(ConjClasses.mk g).carrier).Coprime (Module.finrank ℂ V)) :
  ρ.character g = 0 ∨ ‖ρ.character g‖ = ↑(Module.finrank ℂ V)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Schur's lemma, vanishing form](../../quantum-groups/quantum-groups-compact-reconstruction-and-generi/schurs-lemma-vanishing-form.md)

## Lean

Formalized in Tau Ceti as [`Representation.char_eq_zero_or_norm_char_eq_finrank`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/CharacterTable/Vanishing.html#Representation.char_eq_zero_or_norm_char_eq_finrank).

## Other forms

**Burnside's vanishing theorem, for a bundled finite-dimensional complex representation.** Formalized in Tau Ceti as [`FDRep.char_eq_zero_or_norm_char_eq_finrank`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/CharacterTable/Vanishing.html#FDRep.char_eq_zero_or_norm_char_eq_finrank).

```lean
FDRep.char_eq_zero_or_norm_char_eq_finrank.{u_1} {G : Type u_1} [Group G] [Finite G] (X : FDRep ℂ G)
  [Representation.IsIrreducible X.ρ] {g : G}
  (h : (Nat.card ↑(ConjClasses.mk g).carrier).Coprime (Module.finrank ℂ ↑X.V)) :
  X.character g = 0 ∨ ‖X.character g‖ = ↑(Module.finrank ℂ ↑X.V)
```

**Burnside's vanishing theorem, scalar form, for a bundled finite-dimensional complex representation.** Formalized in Tau Ceti as [`FDRep.char_eq_zero_or_exists_apply_eq_smul`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/CharacterTable/Vanishing.html#FDRep.char_eq_zero_or_exists_apply_eq_smul).

```lean
FDRep.char_eq_zero_or_exists_apply_eq_smul.{u_1} {G : Type u_1} [Group G] [Finite G] (X : FDRep ℂ G)
  [Representation.IsIrreducible X.ρ] {g : G}
  (h : (Nat.card ↑(ConjClasses.mk g).carrier).Coprime (Module.finrank ℂ ↑X.V)) :
  X.character g = 0 ∨ ∃ μ, X.ρ g = μ • 1
```

**Burnside's vanishing theorem, scalar form (Isaacs, Theorem 3.8).** Formalized in Tau Ceti as [`Representation.char_eq_zero_or_exists_apply_eq_smul`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/CharacterTable/Vanishing.html#Representation.char_eq_zero_or_exists_apply_eq_smul).

```lean
Representation.char_eq_zero_or_exists_apply_eq_smul.{u_1, u_2} {G : Type u_1} {V : Type u_2}
  [Group G] [Finite G] [AddCommGroup V] [_root_.Module ℂ V] [FiniteDimensional ℂ V]
  (ρ : Representation ℂ G V) [ρ.IsIrreducible] {g : G}
  (h : (Nat.card ↑(ConjClasses.mk g).carrier).Coprime (Module.finrank ℂ V)) :
  ρ.character g = 0 ∨ ∃ μ, ρ g = μ • 1
```

## Sources

- [Tau Ceti documentation: `Representation.char_eq_zero_or_norm_char_eq_finrank`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/CharacterTable/Vanishing.html#Representation.char_eq_zero_or_norm_char_eq_finrank)
- [Source of `Representation.char_eq_zero_or_norm_char_eq_finrank` in TauCeti/RepresentationTheory/CharacterTable/Vanishing.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/CharacterTable/Vanishing.lean#L126)
