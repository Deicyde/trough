---
declaration: theorem
origin: cited
lean: CategoryTheory.SpectralSequence.Hom.isoModSerre_hom_f_of_le
statement: formalized
proof: formalized
---

# The comparison theorem modulo a Serre class

A morphism of spectral sequences which is an
isomorphism modulo a Serre class `P` on every object of the page `r` is an isomorphism modulo `P`
on every object of every page `r' ≥ r`.

```lean
CategoryTheory.SpectralSequence.Hom.isoModSerre_hom_f_of_le.{v_1, u_1, u_2} {C : Type u_1}
  {κ : Type u_2} [CategoryTheory.Category.{v_1, u_1} C] [CategoryTheory.Abelian C]
  {c : ℤ → ComplexShape κ} {r₀ : ℤ} {E : CategoryTheory.SpectralSequence C c r₀}
  (P : CategoryTheory.ObjectProperty C) [P.IsSerreClass]
  {E' : CategoryTheory.SpectralSequence C c r₀} (f : E ⟶ E') (r : ℤ) (hr : r₀ ≤ r)
  (h : ∀ (pq : κ), P.isoModSerre ((f.hom r hr).f pq)) (r' : ℤ) (hrr' : r ≤ r') (pq : κ) :
  P.isoModSerre ((f.hom r' ⋯).f pq)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CategoryTheory.SpectralSequence.Hom.isoModSerre_hom_f_of_le`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/SpectralSequence/SerreClass.html#CategoryTheory.SpectralSequence.Hom.isoModSerre_hom_f_of_le).

## Sources

- [Tau Ceti documentation: `CategoryTheory.SpectralSequence.Hom.isoModSerre_hom_f_of_le`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/SpectralSequence/SerreClass.html#CategoryTheory.SpectralSequence.Hom.isoModSerre_hom_f_of_le)
- [Source of `CategoryTheory.SpectralSequence.Hom.isoModSerre_hom_f_of_le` in TauCeti/Algebra/Homology/SpectralSequence/SerreClass.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Homology/SpectralSequence/SerreClass.lean#L121)
