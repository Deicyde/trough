---
declaration: theorem
origin: cited
lean: TauCeti.Huber.Pair.Hom.spaComap_orbits_of_isFiniteEtaleTorsor
statement: formalized
proof: formalized
---

# The base is the `G`-quotient of the adic spectrum of a finite étale torsor

If `B` is a
finite étale `G`-torsor over a Tate ring `A`, carries its natural topology and has plus ring the
integral closure of `A⁺`, then `Spa(B, B⁺) → Spa(A, A⁺)` is surjective and open, and its fibres
are the `G`-orbits for `(g • y)(b) = y(g⁻¹ • b)`. Hence it identifies `Spa(A, A⁺)` with the
orbit space `Spa(B, B⁺) / G`.

```lean
TauCeti.Huber.Pair.Hom.spaComap_orbits_of_isFiniteEtaleTorsor.{u_1, u_2, u_3} {G : Type u_1}
  {A : Type u_2} {B : Type u_3} [Group G] [Finite G] [CommRing A] [TopologicalSpace A]
  [IsTopologicalRing A] [TauCeti.Huber.IsTateRing A] [CommRing B] [TopologicalSpace B]
  [IsTopologicalRing B] [TauCeti.Huber.IsHuberRing B] [Algebra A B] [IsModuleTopology A B]
  [MulSemiringAction G B] [SMulCommClass G A B] [TauCeti.Algebra.IsFiniteEtaleTorsor G A B]
  {S : TauCeti.Huber.Pair A} {T : TauCeti.Huber.Pair B} {φ : S.Hom T}
  (hφ : φ.toRingHom = algebraMap A B)
  (hT : T.plus = (integralClosure (↥(Subring.map (algebraMap A B) S.plus)) B).toSubring) :
  Function.Surjective φ.spaComap ∧
    IsOpenMap φ.spaComap ∧
      ∀ (x y : ↑(TauCeti.ValuationSpectrum.spa T.plus)),
        φ.spaComap x = φ.spaComap y ↔
          ∃ g, ↑y = TauCeti.ValuationSpectrum.comap (MulSemiringAction.toRingHom G B g⁻¹) ↑x
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Huber.Pair.Hom.spaComap_orbits_of_isFiniteEtaleTorsor`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/Spa/Torsor.html#TauCeti.Huber.Pair.Hom.spaComap_orbits_of_isFiniteEtaleTorsor).

## Sources

- [Tau Ceti documentation: `TauCeti.Huber.Pair.Hom.spaComap_orbits_of_isFiniteEtaleTorsor`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/Spa/Torsor.html#TauCeti.Huber.Pair.Hom.spaComap_orbits_of_isFiniteEtaleTorsor)
- [Source of `TauCeti.Huber.Pair.Hom.spaComap_orbits_of_isFiniteEtaleTorsor` in TauCeti/AlgebraicGeometry/AdicSpace/Spa/Torsor.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/AdicSpace/Spa/Torsor.lean#L147)
- [Tau Ceti roadmap status: Analytic adic geometry for diamonds](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AdicEtaleGeometry/STATUS.md)
