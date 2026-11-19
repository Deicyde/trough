---
declaration: theorem
origin: cited
lean: TauCeti.AlgebraicGeometry.tilde_toOpen_bijective_of_two_le_depth, TauCeti.AlgebraicGeometry.StructureSheaf.toOpenₗ_bijective_of_two_le_depth
statement: formalized
proof: formalized
---

# Hartogs principle for `M~` on `Spec R`

Let `M` be a finite module over a Noetherian ring
`R` and `U` an open subset of `Spec R` such that `depth M_p ≥ 2` for every prime `p ∉ U`. Then
`M → M~(U)` is bijective: every section of `M~` over `U` comes from a unique element of `M`.
Stacks, Lemma 31.5.11 (0E9I), for the affine scheme `Spec R` and `M~`, with `M_p` the stalk
of `M~` at `p`.

```lean
TauCeti.AlgebraicGeometry.tilde_toOpen_bijective_of_two_le_depth.{u} {R : CommRingCat}
  [IsNoetherianRing ↑R] (M : ModuleCat ↑R) [Module.Finite ↑R ↑M]
  (U : (AlgebraicGeometry.Spec R).Opens)
  (h : ∀ p ∉ U, 2 ≤ IsLocalRing.depth ↧(LocalizedModule p.asIdeal.primeCompl ↑M)) :
  Function.Bijective ⇑(ModuleCat.Hom.hom (AlgebraicGeometry.tilde.toOpen M U))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Algebraic Hartogs principle](algebraic-hartogs-principle.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.tilde_toOpen_bijective_of_two_le_depth`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Modules/Tilde/Hartogs.html#TauCeti.AlgebraicGeometry.tilde_toOpen_bijective_of_two_le_depth).

## Other forms

**Hartogs principle for the structure sheaf of a module.** Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.StructureSheaf.toOpenₗ_bijective_of_two_le_depth`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Modules/Tilde/Hartogs.html#TauCeti.AlgebraicGeometry.StructureSheaf.toOpen%E2%82%97_bijective_of_two_le_depth).

```lean
TauCeti.AlgebraicGeometry.StructureSheaf.toOpenₗ_bijective_of_two_le_depth.{u} {R M : Type u}
  [CommRing R] [AddCommGroup M] [_root_.Module R M] [IsNoetherianRing R] [Module.Finite R M]
  (U : TopologicalSpace.Opens ↑(AlgebraicGeometry.PrimeSpectrum.Top R))
  (h : ∀ p ∉ U, 2 ≤ IsLocalRing.depth ↧(LocalizedModule p.asIdeal.primeCompl M)) :
  Function.Bijective ⇑(AlgebraicGeometry.StructureSheaf.toOpenₗ R M U)
```

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.tilde_toOpen_bijective_of_two_le_depth`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Modules/Tilde/Hartogs.html#TauCeti.AlgebraicGeometry.tilde_toOpen_bijective_of_two_le_depth)
- [Source of `TauCeti.AlgebraicGeometry.tilde_toOpen_bijective_of_two_le_depth` in TauCeti/AlgebraicGeometry/Modules/Tilde/Hartogs.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/Modules/Tilde/Hartogs.lean#L233)
