---
declaration: def
origin: cited
lean: TauCeti.ResolventSpec.orbitQuotientEquivFactors
statement: formalized
---

# The factorization theorem for a separable resolvent

Let `f` be monic of
degree `n`, let `E` be a normal splitting extension, number the roots of `f` in `E` by `e`, and
let the resolvent of `f` for the specification be separable. The orbits of the Galois image, read
through `e`, on the cosets of `H` are then in bijection with the monic irreducible factors of the
resolvent over `F`: the orbit of the coset of `τ` goes to the minimal polynomial of the value at
the roots of the invariant renamed along `τ`.

The degree of each factor is the size of the matching orbit,
`TauCeti.ResolventSpec.natCard_orbit_eq_natDegree_factor`.

```lean
TauCeti.ResolventSpec.orbitQuotientEquivFactors.{u, v} {F : Type u} [Field F] {E : Type v} [Field E]
  [Algebra F E] {f : Polynomial F} {n : ℕ} (spec : TauCeti.ResolventSpec n)
  [Fact (Polynomial.map (algebraMap F E) f).Splits] [Normal F E] (hf : f.Monic)
  (hdeg : f.natDegree = n) (e : ↑(f.rootSet E) ≃ Fin n)
  (hres : TauCeti.ResolventSeparationEvidence spec f) :
  MulAction.orbitRel.Quotient
      (↥(Subgroup.map (↑e.permCongrHom) (Polynomial.Gal.galActionHom f E).range))
      (Equiv.Perm (Fin n) ⧸ spec.H) ≃
    (spec.specialize F f).Factors
```

## Depends on

- [Separation evidence for a specialized resolvent](separation-evidence-for-a-specialized-resolvent.md)
- [TauCeti.ResolventSpec](tauceti-resolventspec.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ResolventSpec.orbitQuotientEquivFactors`](https://taucetiproject.org/docs/TauCeti/FieldTheory/GaloisGroups/Resolvent/Root.html#TauCeti.ResolventSpec.orbitQuotientEquivFactors).

## Sources

- [Tau Ceti documentation: `TauCeti.ResolventSpec.orbitQuotientEquivFactors`](https://taucetiproject.org/docs/TauCeti/FieldTheory/GaloisGroups/Resolvent/Root.html#TauCeti.ResolventSpec.orbitQuotientEquivFactors)
- [Source of `TauCeti.ResolventSpec.orbitQuotientEquivFactors` in TauCeti/FieldTheory/GaloisGroups/Resolvent/Root.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/GaloisGroups/Resolvent/Root.lean#L399)
- [Tau Ceti roadmap status: Galois groups of polynomials](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/PolynomialGaloisGroups/STATUS.md)
