---
declaration: theorem
origin: cited
lean: TauCeti.ncard_isomorphic_mul_natCard_algEquiv
statement: formalized
proof: formalized
---

# The orbit count

([Serre 1978, Remarque 3°]): for `L ∈ σ_K(n)`, the isomorphism class of `L`
inside `σ_K(n)` has `n / #Aut_K(L)` members, in multiplied form. The extension `L / K` is separable
of degree `n`, so it has `n` embeddings into `SeparableClosure K`; their images are the members of
the class, and the embeddings with a given image form a torsor under `Aut_K(L)`.

```lean
TauCeti.ncard_isomorphic_mul_natCard_algEquiv.{u_1} {K : Type u_1} [Field K] [ValuativeRel K]
  [TopologicalSpace K] [IsNonarchimedeanLocalField K] {n : ℕ}
  {L : IntermediateField K (SeparableClosure K)} (hL : L ∈ TauCeti.totallyRamifiedOfDegree K n) :
  {M | M ∈ TauCeti.totallyRamifiedOfDegree K n ∧ Nonempty (↥L ≃ₐ[K] ↥M)}.ncard *
      Nat.card Gal(↥L/K) =
    n
```

## Depends on

- [TauCeti.totallyRamifiedOfDegree](tauceti-totallyramifiedofdegree.md)

## Proof depends on

- [TauCeti.algebraicExtensionNormedField](../../part-04/local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ncard_isomorphic_mul_natCard_algEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Orbit.html#TauCeti.ncard_isomorphic_mul_natCard_algEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.ncard_isomorphic_mul_natCard_algEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Orbit.html#TauCeti.ncard_isomorphic_mul_natCard_algEquiv)
- [Source of `TauCeti.ncard_isomorphic_mul_natCard_algEquiv` in TauCeti/NumberTheory/LocalField/MassFormula/Orbit.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/MassFormula/Orbit.lean#L63)
- [Tau Ceti roadmap status: Counting totally ramified extensions of a local field, and Serre's mass formula](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/MassFormula/STATUS.md)
