---
declaration: theorem
origin: cited
lean: TauCeti.AlgebraicGeometry.Scheme.coheight_eq_one_of_maximal_mem_zeroLocus
statement: formalized
proof: formalized
---

# Krull's principal ideal theorem on a scheme

A maximal point of the zero locus of a
nonzero global function on an integral locally Noetherian scheme, that is, the generic point of
an irreducible component of that zero locus, has coheight one.

```lean
TauCeti.AlgebraicGeometry.Scheme.coheight_eq_one_of_maximal_mem_zeroLocus.{u}
  {X : AlgebraicGeometry.Scheme} [AlgebraicGeometry.IsLocallyNoetherian X]
  [AlgebraicGeometry.IsIntegral X] {a : ↑(X.presheaf.obj (Opposite.op ⊤))} (ha : a ≠ 0) {x : ↥X}
  (hx : Maximal (fun x => x ∈ X.zeroLocus {a}) x) : Order.coheight x = 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.Scheme.coheight_eq_one_of_maximal_mem_zeroLocus`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Scheme/ZeroLocusComponents.html#TauCeti.AlgebraicGeometry.Scheme.coheight_eq_one_of_maximal_mem_zeroLocus).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.Scheme.coheight_eq_one_of_maximal_mem_zeroLocus`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Scheme/ZeroLocusComponents.html#TauCeti.AlgebraicGeometry.Scheme.coheight_eq_one_of_maximal_mem_zeroLocus)
- [Source of `TauCeti.AlgebraicGeometry.Scheme.coheight_eq_one_of_maximal_mem_zeroLocus` in TauCeti/AlgebraicGeometry/Scheme/ZeroLocusComponents.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/Scheme/ZeroLocusComponents.lean#L182)
