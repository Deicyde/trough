---
declaration: theorem
origin: cited
lean: TauCeti.KummerDedekind.Ideal.irreducible_map_iff_irreducible_minpoly
statement: formalized
proof: formalized
---

# The Kummer–Dedekind irreducibility criterion

`p` stays prime in `S` exactly when
`minpoly R x` is irreducible modulo `p`.

```lean
TauCeti.KummerDedekind.Ideal.irreducible_map_iff_irreducible_minpoly.{u_1, u_2} {R : Type u_1}
  {S : Type u_2} [CommRing R] [CommRing S] [Algebra R S] [IsDomain R] [IsIntegrallyClosed R]
  [IsDedekindDomain S] [Module.IsTorsionFree R S] {x : S} {p : Ideal R} (hp : p.IsMaximal)
  (hp0 : p ≠ ⊥) (hx : Ideal.comap (algebraMap R S) (conductor R x) ⊔ p = ⊤) (hx' : IsIntegral R x) :
  Irreducible (Ideal.map (algebraMap R S) p) ↔
    Irreducible (Polynomial.map (Ideal.Quotient.mk p) (minpoly R x))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.KummerDedekind.Ideal.irreducible_map_iff_irreducible_minpoly`](https://taucetiproject.org/docs/TauCeti/RingTheory/DedekindDomain/KummerDedekind.html#TauCeti.KummerDedekind.Ideal.irreducible_map_iff_irreducible_minpoly).

## Sources

- [Tau Ceti documentation: `TauCeti.KummerDedekind.Ideal.irreducible_map_iff_irreducible_minpoly`](https://taucetiproject.org/docs/TauCeti/RingTheory/DedekindDomain/KummerDedekind.html#TauCeti.KummerDedekind.Ideal.irreducible_map_iff_irreducible_minpoly)
- [Source of `TauCeti.KummerDedekind.Ideal.irreducible_map_iff_irreducible_minpoly` in TauCeti/RingTheory/DedekindDomain/KummerDedekind.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/DedekindDomain/KummerDedekind.lean#L228)
